"""Phase-sensitive finite checks of the copy-based spectral classifier.

The exact physical dilation is compared with the desired controlled evolution
on inputs entangled with an untouched reference. Finite inputs do not certify
a diamond-norm theorem; the analytical remainder and hybrid proof do that.
"""

import numpy as np
from scipy.linalg import expm
from scipy.stats import binom


def trace_norm(matrix):
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def controlled_dilation(d, reference_dimension):
    dims = (2, d, reference_dimension, d)
    size = int(np.prod(dims))
    swap = np.zeros((size, size))
    for column, (control, left, ref, right) in enumerate(np.ndindex(*dims)):
        row = np.ravel_multi_index((control, right, ref, left), dims)
        swap[row, column] = 1.
    control_one = np.diag(np.repeat([0., 1.], d * reference_dimension * d))
    return control_one @ swap


def trace_copy(matrix, kept_dimension, copy_dimension):
    return np.einsum("ibjb->ij", matrix.reshape(
        kept_dimension, copy_dimension, kept_dimension, copy_dimension))


def qpe_probabilities(lam, length):
    angles = 2 * np.pi * np.arange(length) / length
    delta = (lam - angles + np.pi) % (2 * np.pi) - np.pi
    amplitudes = np.sinc(length * delta / (2 * np.pi)) / np.sinc(delta / (2 * np.pi))
    probabilities = amplitudes**2
    signed_angles = (angles + np.pi) % (2 * np.pi) - np.pi
    estimates = np.clip(signed_angles, 0., 1.)
    return probabilities, estimates


def run_checks():
    rng = np.random.default_rng(20261116)
    derivative_errors = []
    controlled_cases = []
    sign_sensitivity = []
    for spectrum in [[.7, .3], [.6, .3, .1]]:
        d = len(spectrum)
        rho = np.diag(spectrum)
        r = 2
        kept = 2 * d * r
        hamiltonian = controlled_dilation(d, r)
        effective = np.kron(np.diag([0., 1.]), np.kron(rho, np.eye(r)))
        psi = rng.normal(size=kept) + 1j * rng.normal(size=kept)
        psi /= np.linalg.norm(psi)
        state = np.outer(psi, psi.conj())
        joint = np.kron(state, rho)
        derivative = trace_copy(hamiltonian @ joint - joint @ hamiltonian, kept, d)
        claimed = effective @ state - state @ effective
        derivative_error = trace_norm(derivative - claimed)
        derivative_errors.append(derivative_error)
        assert derivative_error < 1e-12

        for h in [.005, .03, .1, -.03]:
            physical_unitary = expm(-1j * h * hamiltonian)
            physical = trace_copy(physical_unitary @ joint @ physical_unitary.conj().T,
                                  kept, d)
            intended_unitary = expm(-1j * h * effective)
            intended = intended_unitary @ state @ intended_unitary.conj().T
            error = trace_norm(physical - intended)
            assert error <= 4 * h**2 + 1e-12
            controlled_cases.append({"d": d, "reference_dimension": r, "h": h,
                                     "trace_distance_unhalved": error,
                                     "quadratic_upper": 4 * h**2})
            if h == .005:
                wrong_unitary = expm(1j * h * effective)
                wrong_error = trace_norm(physical - wrong_unitary @ state @ wrong_unitary.conj().T)
                # This input has coherent control branches. Reversing their phase
                # produces a first-order discrepancy, unlike the correct simulator.
                assert wrong_error > 5 * error
                sign_sensitivity.append({"d": d, "correct_error": error,
                                         "reversed_sign_error": wrong_error})

        total_time = 1.
        for copies in [8, 32]:
            # Positive QPE evolution exp(+i rho T) requires negative step h.
            h = -total_time / copies
            unitary = expm(-1j * h * hamiltonian)
            output = state.copy()
            for _ in range(copies):
                expanded = np.kron(output, rho)
                output = trace_copy(unitary @ expanded @ unitary.conj().T, kept, d)
            desired_unitary = expm(1j * total_time * effective)
            desired = desired_unitary @ state @ desired_unitary.conj().T
            error = trace_norm(output - desired)
            assert error <= 4 * total_time**2 / copies + 1e-12
            controlled_cases.append({"d": d, "copies": copies,
                                     "positive_qpe_time": total_time,
                                     "trace_distance_unhalved": error,
                                     "hybrid_upper": 4 * total_time**2 / copies})

    qpe_cases = []
    for threshold in [.25, .07]:
        length = 2**int(np.ceil(np.log2(64 * np.pi / threshold)))
        gamma = .01
        repeats = int(np.ceil(4 * np.log(1 / gamma)))
        if repeats % 2 == 0:
            repeats += 1
        phases = list(np.linspace(0., 1., 31))
        phases += [threshold, 2 * threshold, np.pi / length,
                   (int(length / (4 * np.pi)) + .5) * 2 * np.pi / length]
        max_round_failure = 0.
        max_filter_error = 0.
        for lam in phases:
            probabilities, estimates = qpe_probabilities(lam, length)
            assert abs(probabilities.sum() - 1) < 1e-10
            failure = float(probabilities[np.abs(estimates - lam) >= threshold / 2].sum())
            max_round_failure = max(max_round_failure, failure)
            assert failure <= 1 / 17 + 1e-10
            one_round_acceptance = float(probabilities[estimates > 3 * threshold / 2].sum())
            median_acceptance = float(binom.sf(repeats // 2, repeats,
                                              min(1., max(0., one_round_acceptance))))
            if lam <= threshold:
                max_filter_error = max(max_filter_error, median_acceptance)
                assert median_acceptance <= gamma + 1e-10
            if lam >= 2 * threshold:
                max_filter_error = max(max_filter_error, 1 - median_acceptance)
                assert 1 - median_acceptance <= gamma + 1e-10
        qpe_cases.append({"t": threshold, "L": length, "r": repeats, "gamma": gamma,
                          "maximum_one_round_failure": max_round_failure,
                          "maximum_cutoff_endpoint_error": max_filter_error})

    return {"status": "passed", "maximum_first_order_identity_error": max(derivative_errors),
            "controlled_channel_cases": controlled_cases,
            "coherent_control_sign_sensitivity": sign_sensitivity,
            "phase_estimation_cases": qpe_cases,
            "limits": "Finite entangled inputs check phase and reference conventions; they do not certify a diamond norm or a universal QPE tail theorem."}


if __name__ == "__main__":
    import json
    print(json.dumps(run_checks(), indent=2))
