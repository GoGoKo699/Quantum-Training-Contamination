# Reproduce the finite checks

The analytical scientific account supplies the proofs. This suite tests the
scalar formula against an independently formulated minimax problem and checks
the physical contamination witnesses. It does not establish external novelty,
an asymptotic theorem by simulation, or a finite-copy quantum advantage.

Use Python 3.12 or later with the pinned numerical dependencies:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The command writes [results.json](results.json), including the actual Python,
NumPy and SciPy versions, fixed random seed, errors and tested parameter values.
Successful execution prints `"status": "passed"` and exits with code zero.
Run `python3 verification/check_floor.py` separately to write the more focused
`floor_results.json` report.

## What is checked

- **A separate fixed-spectrum optimization.** A linear program minimizes total
  variation over every target-amplitude distribution compatible with an
  arbitrary training spectrum. Its constraints use the rank-one compatibility
  condition, rather than the proposed root or least-favorable spectrum.
- **A classifier for the full compatibility continuum.** For arbitrary spectra,
  the code independently enumerates every vertex of the simplex intersected
  with the harmonic halfspace. A second linear program constructs a diagonal
  decision effect against all vertices. Linearity extends its guarantee to the
  full polytope; arbitrary phases do not affect this diagonal effect. Interior
  compatible pure targets are exercised as additional numerical checks.
- **An attaining contamination family.** The claimed least-favorable spectrum
  reaches the scalar risk in the first LP. Several actual phase-orbit targets
  have positive semidefinite residual `rho - a P`, the correct trace, and a
  normalized contaminating density matrix whenever `a < 1`.
- **A commuting comparator.** A separate eigenvector minimax LP verifies the
  flat-spectrum witnesses for the commuting-contaminant benchmark. The general
  contamination floor is at least this restricted benchmark.
- **Endpoints and limiting order.** The suite covers clean training, the fully
  unidentifiable threshold, the two-coordinate closed form when applicable,
  and the stated limit with contamination fixed before dimension grows. It
  does not reinterpret that ordered limit as a joint precision-dimension law.
- **Coherent controlled simulation.** An exact controlled-swap dilation acts on
  a test entangled with an untouched reference. Its first derivative and finite
  output states are compared with the intended controlled evolution. A sign
  reversal is deliberately checked to ensure the inputs detect relative
  control-branch phases. Fresh-copy composition is also checked using the
  negative step sign required for positive phase-estimation evolution.
- **The finite phase-estimation filter.** Direct Fourier probabilities test
  signed-phase unwrapping, clipping, single-round tails, and the repeated-median
  acceptance bounds at both sides of the cutoff band.
- **The shared learning route.** Source checks require exactly 30 ordered
  milestone headings, nonempty stated fields, the declared 12/18 phase split,
  and dependencies pointing only to earlier milestones. Required shared pages
  must exist; known personal coaching/learner-record filenames must be absent.
  These checks do not grade understanding targets or establish scientific
  correctness. Local link/fence checks and actual hosted mathematical review
  remain separate.

The checks use dimensions up to 11 for the matrix and continuum-LP comparisons;
the scalar limit evaluation reaches dimension one million. Positive-semidefinite
and LP comparisons use an absolute tolerance of `3e-8`. The seeded spectra are
finite examples, so passing them cannot certify the universal worst case.

The runner also checks local Markdown file and heading links, plus balanced
code fences. These checks do not inspect the hosting renderer. The exact-law
[figure and generator](figures/README.md) have a separate optional plotting
dependency and an explicit ordered-limit caption.
The controlled-channel tests use dimensions two and three and an entangled
two-dimensional reference. They check consequential phase conventions; the
analytical proof supplies the diamond-norm guarantee for arbitrary references.

## Checks for the sister results

The [rank and contamination comparison](../science/flat_rank_training.md) uses the existing clean verification above. The [joint finite-instance suite](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/verification/check_contamination.py) checks the shared-density construction, the balanced recognition risk, and its contrast with reference-stable reflection programming.
