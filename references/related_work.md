# Related work and attribution

The question here is prediction from contaminated training specimens: an unknown pure state $`P`$ contributes a known fraction $`a`$ to $`\rho=aP+(1-a)\sigma`$, while the later test is clean $`P`$ or the known background $`I/d`$. The results concern the ambiguity of that prediction task and explicit coherent constructions. They do not introduce a new scalar entropy inequality, a new Hamiltonian-simulation primitive, or a general robustness theorem for quantum hardware.

## What is inherited and what is established here

| Ingredient or nearby result | Earlier source | Role in this account |
|---|---|---|
| Independent contamination by an arbitrary distribution | [Huber1964](#huber1964) | Motivation for the mixture model; the present source and prediction are quantum. |
| Different pure-state ensembles representing one density matrix | [HJW1993](#hjw1993) | The general ambiguity of a density-matrix decomposition is inherited quantum-information background. |
| Binary discrimination and convex minimax | [Sion1958](#sion1958) and standard quantum hypothesis testing | The decision-theoretic tools are inherited. |
| Exact scalar Rényi-entropy versus distance-to-uniform frontier | [Rioul2023](#rioul2023), Theorem 6, Eq. (88) | Supplies the extremal probability vector after the quantum compatibility reduction. |
| Exponentiating an unknown density matrix from copies | [LMR2014](#lmr2014), [Kimmel2017](#kimmel2017), [Go2025](#go2025) | Supplies the coherent spectral-processing mechanism; its copies and gates are charged. |
| Robust selection from a given quantum hypothesis family | [Qiu2026](#qiu2026) | A different robustness task with supplied candidates and a separation margin. |
| Stability of an existing classifier under perturbed test inputs | [Weber2021](#weber2021) | A different location of the uncertainty: the inference input rather than the hidden training decomposition. |
| Exact clean flat-rank classification and a classical-compilation converse | [Quantum Classification Rank Limits](#rank-limits) | Supplies a clean comparison and an inherited lower-bound subfamily. |

The contribution developed here is the [exact operational compatibility law](../science/precision_floor.md) for contaminated training, its least-favorable family of nonorthogonal clean targets, and the resulting [difference between commuting and unrestricted contamination](../science/commuting_comparison.md). The [finite-copy constructions](../science/finite_copy.md) apply established sample-based tools to this prediction problem. Their attaining bounds are stated separately from optimality claims, with the full charges in [the resource account](../science/resources.md).

## Classical scalar frontier

<a id="rioul2023"></a>
**[Rioul2023]** Olivier Rioul, [*The Interplay between Error, Total Variation, Alpha-Entropy and Guessing: Fano and Pinsker Direct and Reverse Inequalities*](https://doi.org/10.3390/e25070978), *Entropy* **25**(7), 978 (2023). [Author's full text](https://perso.telecom-paristech.fr/rioul/publis/202306rioul.pdf).

Theorem 6, Eq. (88), gives the sharp reverse-Pinsker extremal for a Schur-concave randomness measure at fixed distance from uniform. Its proof uses Lemma 4, Eq. (85); Proposition 4, Eq. (90), describes the continuous lower boundary. Setting the alphabet size to $`d`$, its statistical-randomness parameter to $`q`$, and the entropy order to $`1/2`$ gives exactly the concentrated vector used here:

```math
p_*(q)=\left(1-q,\underbrace{1/d,\ldots,1/d}_{\lfloor dq\rfloor},q-\frac{\lfloor dq\rfloor}{d},0,\ldots\right).
```

That scalar extremal is inherited. The additional quantum step is to derive the feasible set $`(\sum_i\sqrt{p_i})^2\le1/a`$ from $`aP\preceq\rho`$, then realize the extremal by different pure-state phase choices producing one identical contaminated training state. This turns the scalar boundary into a prediction limit that applies even with unlimited coherent processing.

<a id="huber1964"></a>
**[Huber1964]** Peter J. Huber, [*Robust Estimation of a Location Parameter*](https://doi.org/10.1214/aoms/1177703732), *Annals of Mathematical Statistics* **35**(1), 73–101 (1964). The familiar contamination mixture is a statistical modeling antecedent, rather than a source of the quantum minimax formula.

<a id="sion1958"></a>
**[Sion1958]** Maurice Sion, [*On general minimax theorems*](https://doi.org/10.2140/pjm.1958.8.171), *Pacific Journal of Mathematics* **8**(1), 171–176 (1958). Its compact convex minimax theorem justifies interchanging the effect and compatible-probability optimizations. No new minimax principle is claimed.

## Robust quantum learning and classification

<a id="hjw1993"></a>
**[HJW1993]** Lane P. Hughston, Richard Jozsa, and William K. Wootters, [*A complete classification of quantum ensembles having a given density matrix*](https://doi.org/10.1016/0375-9601(93)90880-9), *Physics Letters A* **183**(1), 14–18 (1993).

The nonuniqueness of a density matrix's ensemble decomposition is established background. The elementary compatibility condition $`aP\preceq\rho`$ is not a new ensemble theorem. The issue settled here is the worst clean-prediction error associated with that compatibility set, including an explicit least-favorable phase family and a matched commuting comparison.

<a id="qiu2026"></a>
**[Qiu2026]** Yixian Qiu, Lirandë Pira, and Patrick Rebentrost, [*Quantum learning with tunable loss functions*](https://doi.org/10.1038/s41534-026-01259-2), *npj Quantum Information* **12**, 131 (2026), version of record dated 7 August 2026. The earlier [arXiv:2508.21369v1](https://arxiv.org/abs/2508.21369v1) is dated 29 August 2025 and does not contain all of the published robustness discussion.

The published Definition 1 and Theorem 1 concern a supplied family of projector-valued hypotheses and tilted empirical risk. Its robustness section treats source perturbations and outliers. The robust-selection application forms pairwise Helstrom projectors for known candidate states and assumes that the clean target is one candidate separated from the others by a positive trace-distance margin; Supplementary Note 6 contains the detailed contamination statement.

Here the pure target ranges over an unknown continuum and no candidate family or positive identification margin is supplied. Different targets can yield the exact same $`\rho`$. The objective is the best error on one subsequent clean test, rather than recovery of a candidate index or minimization of a tilted risk. The finite-candidate guarantee therefore does not establish the compatibility floor, its dimension dependence, or the commuting-contaminant comparison.

<a id="weber2021"></a>
**[Weber2021]** Maurice Weber, Nana Liu, Bo Li, Ce Zhang, and Zhikuan Zhao, [*Optimal provable robustness of quantum classification via quantum hypothesis testing*](https://doi.org/10.1038/s41534-021-00410-5), *npj Quantum Information* **7**, 76 (2021); [arXiv:2009.10064](https://arxiv.org/abs/2009.10064).

Their Theorem 1 bounds changes in an existing classifier's outcome under inference-time input perturbations using hypothesis-testing errors. Their pure- and mixed-state corollaries express robustness through fidelity, Bures distance, and trace distance. The present learner instead receives corrupted training specimens and later classifies a clean test; the unknown decomposition is the source of uncertainty. Applying a continuity bound to a fixed classifier does not determine the optimal learner or its exact ambiguity floor.

## Sample-based coherent spectral processing

<a id="lmr2014"></a>
**[LMR2014]** Seth Lloyd, Masoud Mohseni, and Patrick Rebentrost, [*Quantum principal component analysis*](https://doi.org/10.1038/nphys3029), *Nature Physics* **10**, 631–633 (2014); [arXiv:1307.0401](https://arxiv.org/abs/1307.0401).

<a id="kimmel2017"></a>
**[Kimmel2017]** Shelby Kimmel, Cedric Yen-Yu Lin, Guang Hao Low, Maris Ozols, and Theodore J. Yoder, [*Hamiltonian simulation with optimal sample complexity*](https://doi.org/10.1038/s41534-017-0013-7), *npj Quantum Information* **3**, 13 (2017); [arXiv:1608.00281v1](https://arxiv.org/abs/1608.00281v1).

Density matrix exponentiation and the sample-based simulation viewpoint are inherited from these works. Copies of an unknown program state drive a partial-SWAP simulation of its Hamiltonian. This is the appropriate input model here; there is no classical matrix-loading oracle.

<a id="go2025"></a>
**[Go2025]** Byeongseon Go, Hyukjoon Kwon, Siheon Park, Dhrumil Patel, and Mark M. Wilde, [*Sample-based Hamiltonian and Lindbladian simulation: Non-asymptotic analysis of sample complexity*](https://doi.org/10.1088/2058-9565/ae075b), *Quantum Science and Technology* **10**, 045058 (2025); [arXiv:2412.02134v3](https://arxiv.org/abs/2412.02134v3), 29 September 2025.

Their current nonasymptotic analysis gives a DME copy upper bound $`4t^2/\epsilon`$ in normalized diamond distance and explains an incompleteness in the earlier upper-bound proof. The present resource account uses an explicit controlled partial-SWAP derivation and a composed error budget. DME optimality for simulating $`e^{-it\rho}`$ does not imply optimal classification-copy complexity; no such transfer is made.

<a id="tang2021"></a>
**[Tang2021]** Ewin Tang, [*Quantum Principal Component Analysis Only Achieves an Exponential Speedup Because of Its State Preparation Assumptions*](https://doi.org/10.1103/PhysRevLett.127.060503), *Physical Review Letters* **127**, 060503 (2021); [arXiv:1811.00414](https://arxiv.org/abs/1811.00414).

Tang supplies classical analogues when classical input data support comparable sampling access. The inputs here are native unknown specimens, not classically specified amplitudes. The comparison therefore concerns retaining quantum training information versus compiling it into a classical record. Preparation costs remain explicit, and a copy separation alone is not a hardware-runtime claim.

## Related scientific accounts by the author

<a id="rank-limits"></a>
[**Quantum Classification Rank Limits**](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/tree/5974494ec900f2e5ed8193db18ef6c5633d4a48e) treats a clean flat-rank source $`P/r`$ and a later test from that same source or $`I/d`$. Its [classical-compilation theorem C1](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/5974494ec900f2e5ed8193db18ef6c5633d4a48e/science/classical_compilation.md) already gives a lower bound for arbitrary collective training measurements followed by classical-only storage. Setting $`r=1`$ supplies a clean subfamily here. The new problem is that the later desired source is the clean $`P`$, while training supplies $`\rho\ne P`$. A rank parameter for $`\rho`$ does not settle which compatible pure target should be accepted.

[**Quantum Learning Label Noise**](https://github.com/GoGoKo699/Quantum-Learning-Label-Noise/tree/f305698454964e101311b3a337efe49c71808cff) changes independent annotations on one fixed hidden-Pauli supervised source. Its sample and computational separations do not yield the state-contamination compatibility floor: here the uncertainty changes the training state itself, and the test label refers to a clean unknown pure source.

[**Quantum Training Robustness**](https://github.com/GoGoKo699/Quantum-Training-Robustness/tree/32870662da8731510d31813fe50d5670e83391ad) studies how a finite trusted pure-input menu transfers measured training loss to Haar-average channel infidelity. Its common right-eigenoperator criterion and variance gap concern certification of an operation. The present source has an untrusted state decomposition and an unrestricted effect chosen for one later prediction; no channel-training loss-transfer theorem is being restated.

## Consequence and scope of the comparison

The strongest distinction is within the same quantum prediction model. If $`[\sigma,P]=0`$, a known $`\rho`$ permits acceptance of its eigenspaces with eigenvalues at least $`a`$; the worst risk is $`\min\{d,\lfloor1/a\rfloor\}/(2d)`$. Allowing noncommuting contaminants instead gives the exact phase-orbit ambiguity law. For fixed $`a\in(0,1)`$, its excess has order $`d^{-1/2}`$, rather than the commuting risk's order $`d^{-1}`$. In particular, when $`a \gt 1/2`$, commuting contamination permits the exact oracle limit, while unrestricted contamination gives a positive excess whenever $`a \lt 1`$. This isolates a cost of nonorthogonal decompositions. It is distinct from the inherited fact that a SWAP test already retains constant prediction advantage at fixed contamination.

The literature comparison uses the explicit theorem statements above and the cited public scientific accounts. The published QTERM main robustness discussion and its finite-candidate application were inspected; the full published supplement was not available in that inspection, so no claim about every supplementary extension is made. This is a scoped comparison, not exhaustive priority certification. The results retain their pure-target, maximally-mixed-background, IID-contamination, clean-test, and ideal-processing assumptions.

## Flat-rank recognition

The [balanced-rank account](../science/flat_rank_training.md) uses [Chen, Gao, and Ren’s contamination modulus, Theorem 3.2](https://arxiv.org/abs/1511.04144) as the classical precedent for comparing distinct hidden sources that share one observable mixture. The quantum argument evaluates the exact common-specimen criterion by the trace norm of a projector difference, using the principal planes of two projections. [Halmos’s two-subspace theorem](https://doi.org/10.1090/S0002-9947-1969-0251519-5) gives the underlying block representation.

[Quantum Classification Rank Limits, Q2](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/997088928d85e363fbbed1a913d6fd9284ba643f/science/quantum_precision.md) supplies the finite-copy converse for the admissible clean subfamily. [O’Donnell and Wright, Theorem 1.2](https://arxiv.org/html/1508.01907v2) supplies the collective tomography error for the observed contaminated density. Combining those ingredients with the contamination-specific decision bounds gives the balanced finite-copy rate and its exact weak-contamination limit. [Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/science/contaminated_reflections.md) develops the consequence of the shared ambiguity for ordinary reflection.
