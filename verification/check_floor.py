"""Finite checks for the contaminated-training minimax floor.

The analytical proof is authoritative. These computations test independent LP
formulations, actual contamination witnesses, endpoints, and specified limits.
They establish neither a universal theorem nor a priority claim.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog

SEED = 20261115
TOL = 3e-8


def root_floor(d: int, a: float) -> tuple[float, float]:
    """Evaluate the proposed scalar formula; return q and classification risk."""
    if a <= 1 / d:
        return 1 - 1 / d, .5
    if a == 1:
        return 0., 1 / (2 * d)

    def s(q: float) -> float:
        if q >= 1 - 1 / d:
            return float(np.sqrt(d))
        k = min(int(np.floor(d * q)), d - 1)
        remainder = max(0., q - k / d)
        return float(np.sqrt(1 - q) + k / np.sqrt(d) + np.sqrt(remainder))

    q = brentq(lambda x: s(x) - a**-.5, 0., 1 - 1 / d,
               xtol=1e-14, rtol=1e-14)
    return q, (1 / d + q) / 2


def least_favorable_spectrum(d: int, q: float) -> tuple[np.ndarray, np.ndarray]:
    """Construct the claimed amplitudes and the associated density spectrum."""
    p = np.zeros(d)
    p[0] = 1 - q
    k = min(int(np.floor(d * q)), d - 1)
    p[1:k + 1] = 1 / d
    if k + 1 < d:
        p[k + 1] = max(0., q - k / d)
    p /= p.sum()
    lam = np.sqrt(p)
    lam /= lam.sum()
    return p, lam


def primal_lp(lam: np.ndarray, a: float) -> tuple[float, np.ndarray]:
    """Directly minimize TV over every compatible amplitude distribution.

    Variables p_i,t_i satisfy sum p=1, sum p_i/lambda_i<=1/a,
    t_i>=p_i-1/d, p_i,t_i>=0. This uses no root or witness formula.
    """
    d = len(lam)
    active = np.flatnonzero(lam > 1e-14)
    s = len(active)
    objective = np.r_[np.zeros(s), np.ones(s)]
    inequalities = np.vstack([
        np.r_[1 / lam[active], np.zeros(s)],
        np.hstack([np.eye(s), -np.eye(s)]),
    ])
    rhs = np.r_[1 / a, np.full(s, 1 / d)]
    equality = np.r_[np.ones(s), np.zeros(s)][None, :]
    result = linprog(objective, A_ub=inequalities, b_ub=rhs,
                     A_eq=equality, b_eq=[1.], bounds=[(0, None)] * (2 * s),
                     method="highs")
    if not result.success:
        raise AssertionError(f"Compatible-spectrum primal LP failed: {result.message}")
    p = np.zeros(d)
    p[active] = result.x[:s]
    return float(result.fun), p


def compatible_vertices(lam: np.ndarray, a: float) -> np.ndarray:
    """Enumerate the entire amplitude polytope's vertices, without an LP.

    It is a simplex cut by one halfspace. Vertices are admitted basis vectors
    and intersections of its edges with the harmonic boundary.
    """
    active = np.flatnonzero(lam > 1e-14)
    h = 1 / lam[active]
    cap = 1 / a
    vertices = []
    for i in range(len(active)):
        if h[i] <= cap + 1e-10:
            p = np.zeros(len(lam))
            p[active[i]] = 1.
            vertices.append(p)
    for i in range(len(active)):
        for j in range(i + 1, len(active)):
            if (h[i] - cap) * (h[j] - cap) < -1e-16:
                weight_i = (cap - h[j]) / (h[i] - h[j])
                p = np.zeros(len(lam))
                p[active[i]] = weight_i
                p[active[j]] = 1 - weight_i
                vertices.append(p)
    if not vertices:
        raise AssertionError("Spectrum has no compatible target.")
    return np.asarray(vertices)


def decision_lp(vertices: np.ndarray) -> tuple[float, np.ndarray]:
    """Find the best effect against all continuum targets via vertex constraints.

    Maximize g subject to g<=e.(p-u) for every vertex, and 0<=e<=1.
    A linear objective attains its minimum at a vertex, so this construction
    certifies the stated effect's contrast on the full amplitude polytope.
    """
    d = vertices.shape[1]
    objective = np.r_[np.zeros(d), -1.]
    inequalities = np.hstack([-(vertices - 1 / d), np.ones((len(vertices), 1))])
    result = linprog(objective, A_ub=inequalities, b_ub=np.zeros(len(vertices)),
                     bounds=[(0, 1)] * d + [(None, None)], method="highs")
    if not result.success:
        raise AssertionError(f"Continuum decision LP failed: {result.message}")
    return float(result.x[-1]), result.x[:-1]


def commuting_risk_lp(lam: np.ndarray, a: float) -> float:
    """Independent minimax LP when the contaminant commutes with the pure target."""
    d = len(lam)
    admissible = np.flatnonzero(lam >= a - 1e-12)
    vertices = np.eye(d)[admissible]
    contrast, _ = decision_lp(vertices)
    return (1 - contrast) / 2


def run_checks() -> dict:
    rng = np.random.default_rng(SEED)
    maxima = {"witness_lp_gap": 0., "primal_decision_gap": 0.,
              "continuum_bound_excess": 0., "commuting_formula_gap": 0.}
    minimum_psd = 1.
    witnesses = []
    arbitrary_spectra = []
    commuting_cases = []

    for d in [2, 3, 5, 11]:
        for a in sorted(set([1 / d, (1 + 1 / d) / 2, .6, .8, .99, 1.])):
            q, predicted = root_floor(d, a)
            p, lam = least_favorable_spectrum(d, q)
            contrast, _ = primal_lp(lam, a)
            attained = (1 - contrast) / 2
            gap = abs(attained - predicted)
            maxima["witness_lp_gap"] = max(maxima["witness_lp_gap"], gap)
            assert gap < TOL, (d, a, predicted, attained)
            for _ in range(3):
                psi = np.sqrt(p) * np.exp(1j * rng.uniform(0, 2 * np.pi, d))
                residual = np.diag(lam) - a * np.outer(psi, psi.conj())
                mineig = float(np.linalg.eigvalsh(residual).min())
                minimum_psd = min(minimum_psd, mineig)
                assert mineig > -TOL, (d, a, mineig)
                assert abs(np.trace(residual).real - (1 - a)) < TOL
                if a < 1:
                    sigma = residual / (1 - a)
                    assert np.linalg.eigvalsh(sigma).min() > -TOL
                    assert abs(np.trace(sigma).real - 1) < TOL
            witnesses.append({"d": d, "a": a, "q": q,
                              "root_risk": predicted, "lp_risk": attained})

            if a == 1:
                continue
            for _ in range(5):
                base = rng.dirichlet(np.full(d, .4))
                j = int(rng.integers(d))
                necessary = max(0., (a - base[j]) / (1 - base[j]))
                mixing = necessary + (1 - necessary) * rng.uniform()
                trial = (1 - mixing) * base
                trial[j] += mixing
                g_primal, _ = primal_lp(trial, a)
                vertices = compatible_vertices(trial, a)
                g_decision, effect = decision_lp(vertices)
                dualgap = abs(g_primal - g_decision)
                maxima["primal_decision_gap"] = max(maxima["primal_decision_gap"], dualgap)
                assert dualgap < TOL, (trial, g_primal, g_decision)
                # Enumerated vertices check every compatible amplitude distribution;
                # random convex combinations also exercise nonvertex pure targets.
                assert min((vertices - 1 / d) @ effect) >= g_decision - TOL
                weights = rng.dirichlet(np.ones(len(vertices)))
                interior_p = weights @ vertices
                assert np.dot(effect, interior_p - 1 / d) >= g_decision - TOL
                actual_risk = (1 - g_decision) / 2
                excess = actual_risk - predicted
                maxima["continuum_bound_excess"] = max(maxima["continuum_bound_excess"], excess)
                assert excess < TOL, (d, a, actual_risk, predicted)
                arbitrary_spectra.append({"d": d, "a": a,
                                          "risk": actual_risk, "universal_floor": predicted,
                                          "vertex_count": len(vertices)})

        # A flat high-eigenvalue spectrum realizes the worst commuting case.
        for a in [1 / d, .3, .6, .8, 1.]:
            count = min(d, int(np.floor(1 / a + 1e-12)))
            lam = np.zeros(d)
            lam[:count] = 1 / count
            attained = commuting_risk_lp(lam, a)
            predicted = count / (2 * d)
            gap = abs(attained - predicted)
            maxima["commuting_formula_gap"] = max(maxima["commuting_formula_gap"], gap)
            assert gap < TOL, (d, a, attained, predicted)
            # The general-contamination model includes this commuting model.
            assert root_floor(d, a)[1] >= attained - TOL
            commuting_cases.append({"d": d, "a": a, "compatible_dimension": count,
                                    "risk": attained})

    # Check both endpoints directly and the two-coordinate closed form when k=0.
    for d in [2, 7, 101]:
        assert root_floor(d, 1.)[1] == 1 / (2 * d)
        assert root_floor(d, 1 / d)[1] == .5
        assert root_floor(d, .5 / d)[1] == .5
        for eta in [.001, .01, .1]:
            q, _ = root_floor(d, 1 - eta)
            if q < 1 / d - 1e-10:
                ratio = eta / (1 - eta)
                closed = ratio**2 / (2 * (1 + np.sqrt(1 - ratio**2)))
                assert abs(q - closed) < TOL

    limits = []
    for eta in [.01, .1, .25, .7]:
        a = 1 - eta
        coefficient = a**-.5 - 1
        for d in [1000, 10000, 1000000]:
            q, _ = root_floor(d, a)
            # The statement is fixed eta then d->infinity. No joint-limit exponent
            # is inferred from this finite check.
            remainder = d * (q - coefficient / np.sqrt(d))
            limits.append({"eta": eta, "d": d, "sqrt_d_q": np.sqrt(d) * q,
                           "limit_coefficient": coefficient,
                           "d_scaled_remainder": remainder})
            assert abs(remainder) < 4 + coefficient**2

    return {
        "status": "passed", "seed": SEED,
        "conventions": {"a": "clean fraction", "test_priors": "equal",
                        "risk": "misclassification probability", "tv": "half l1"},
        "maxima": maxima, "minimum_witness_residual_eigenvalue": minimum_psd,
        "least_favorable_witness_cases": witnesses,
        "arbitrary_spectrum_continuum_checks": arbitrary_spectra,
        "commuting_comparator_cases": commuting_cases, "fixed_eta_limit_checks": limits,
        "limits": "Finite numerical checks do not prove the theorem, external novelty, or a finite-copy quantum advantage.",
    }


if __name__ == "__main__":
    report = run_checks()
    destination = Path(__file__).with_name("floor_results.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "maxima": report["maxima"],
                      "minimum_witness_residual_eigenvalue":
                      report["minimum_witness_residual_eigenvalue"]}, indent=2))
