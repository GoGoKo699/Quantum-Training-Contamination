# Build the finite-copy learner

The pure-source learner takes stored quantum training specimens and one later test, applies known gates, and returns one classical label. This guide puts the construction from [F1](finite_copy.md#f1-a-spectral-classifier-without-a-gap-promise) in execution order. The proof and resource guarantees remain in [finite-copy classification](finite_copy.md) and [the resource account](resources.md).

## Inputs and the training boundary

Fix the known dimension $`d\ge2`$ and clean fraction $`0 \lt a\le1`$. The training input consists of $`N`$ independent copies of

```math
\rho=aP+(1-a)\sigma,
\qquad
P=|\psi\rangle\langle\psi|,
```

where the pure target $`P`$ and contaminant $`\sigma`$ are unknown. The later test is $`P`$ with label $`1`$ or $`I_d/d`$ with label $`0`$, with equal priors. It is independent of the training specimens conditional on the hidden source and label. These are the inputs specified in [the model](model.md#the-experiment).

All training copies arrive before the test. Retain them until the test arrives, then consume them in a fixed order during the prediction circuit. Each physical copy is assigned to one simulation step. The circuit needs neither a classical description of the source nor its preparation unitary, inverse or controlled evolution. It makes no further source calls after test arrival.

The output is one predicted label for this one test. The circuit consumes the retained training specimens and does not produce a reusable learned model.

## Choose the finite circuit

Choose the cutoff parameter $`0 \lt t\le1/4`$, spectral-estimation failure budget $`0 \lt\gamma\lt1/2`$, and positive implementation budgets $`\xi_{\rm sim},\xi_{\rm gate}`$. Let $`L=2^m`$ be the smallest power of two satisfying $`L\ge64\pi/t`$, and take the smallest odd integer $`r\ge4\ln(1/\gamma)`$. Here $`r`$ counts phase-estimation rounds.

Each round uses controlled evolution times $`2^0,2^1,\ldots,2^{m-1}`$. Enumerate all $`K=rm`$ segments, including every repetition, as $`T_1,\ldots,T_K`$. Compute

```math
T_{\rm tot}=\sum_{j=1}^{K}T_j=r(L-1),
\qquad
n_j=\left\lceil\frac{4T_jT_{\rm tot}}{\xi_{\rm sim}}\right\rceil,
```

```math
N=\sum_{j=1}^{K}n_j
\le\frac{4T_{\rm tot}^2}{\xi_{\rm sim}}+K.
```

Segment $`j`$ consumes its own $`n_j`$ stored copies. This is the allocation in F1a. All segment times, copy counts and gate angles are determined by the chosen parameters before processing the unknown states.

For a concrete target-risk choice already proved in [F2](finite_copy.md#f2-arbitrary-positive-clean-fraction), take $`0 \lt\varepsilon\le1/4`$ and suppose $`d\ge8/(a\varepsilon^2)`$. Set

```math
t=\frac{a\varepsilon}{4},
\qquad
\gamma=\frac{\varepsilon}{4},
\qquad
\xi_{\rm sim}=\xi_{\rm gate}=\frac{\varepsilon}{4}.
```

The resulting circuit has risk at most $`\varepsilon`$ and uses

```math
N=O\!\left(\frac{\log^2(1/\varepsilon)}{a^2\varepsilon^3}\right)
```

training copies. The copy count is independent of $`d`$ at fixed $`a,\varepsilon`$ in this dimension regime. [F3](finite_copy.md#f3-dependence-on-a-small-contamination-fraction) supplies other sufficient choices when the contamination fraction is small.

## Allocate registers

Let $`n=\lceil\log_2d\rceil`$.

| Register | Allocation and use |
|---|---|
| Training registers $`B_1,\ldots,B_N`$ | $`Nn`$ qubits, retained across the training boundary and consumed sequentially |
| Test register $`A`$ | $`n`$ qubits, holding the same single test throughout all rounds |
| Phase register | $`m`$ qubits, measured and reinitialized after each round |
| Swap-sign auxiliary $`Q`$ | One clean qubit, returned to $`\lvert0\rangle`$ by each exact partial-SWAP gadget |
| Classical records | $`O(rm)`$ bits for the measured phase outcomes and their median |

The phase-estimation control $`C`$ used below is one qubit of the phase register. Known gate decompositions may use a constant number of additional auxiliaries. Thus the total quantum width is at most $`(N+1)n+m+O(1)`$, while the active processing width is $`2n+m+O(1)`$. The remaining stored training registers still count toward total memory.

For a dimension that is not a power of two, use the known $`d`$-dimensional subspace described in [the resource account](resources.md#chronology-and-memory). Full-register swaps preserve that subspace. The background test remains $`I_d/d`$ on it.

## Implement one controlled partial swap

Let $`B`$ be the next unused training register and write $`S=\mathrm{SWAP}_{AB}`$. The required known unitary is

```math
V_h=e^{-ih|1\rangle\langle1|_C\otimes S}.
```

Initialize $`Q`$ to $`|0\rangle`$. Apply a Hadamard to $`Q`$, a full-register SWAP of $`A,B`$ controlled by $`Q`$, and another Hadamard to $`Q`$. This records the SWAP eigenvalue: $`+1`$ corresponds to $`Q=0`$ and $`-1`$ to $`Q=1`$.

Apply $`e^{-ihZ_Q}`$ conditioned on $`C=1`$, then reverse the three recording gates. The auxiliary returns to $`|0\rangle`$. In the convention $`R_z(\theta)=e^{-i\theta Z/2}`$, the middle gate is controlled-$`R_z(2h)`$. Its action on $`(C,Q)`$ is

```math
\mathrm{diag}(1,1,e^{-ih},e^{ih}).
```

Retain both phases in this controlled gate. In particular, the phase on the $`C=1,Q=0`$ branch is relative to the $`C=0`$ branch and affects the later phase measurement.

The gadget uses two known controlled full-register swaps and one controlled single-qubit rotation. Each full-register swap is a product of $`n`$ pairwise swaps, so the ideal-rotation gate cost is $`O(n)`$. The gates depend on the known angle $`h`$, not on $`P`$, $`\sigma`$ or the spectrum of $`\rho`$.

For the positive evolution $`e^{+i\rho T_j}`$ required by this phase-estimation circuit, use

```math
h_j=-\frac{T_j}{n_j}.
```

Apply the gadget once to each of the segment's $`n_j`$ fresh stored copies, discarding each consumed register afterward. The sign is part of the implementation: the physical gadget has exponent $`-ih_j`$, so positive target evolution requires a negative step.

The [controlled-simulation proof](finite_copy.md#controlled-density-matrix-simulation-from-copies) bounds the segment's unhalved diamond error by $`4T_j^2/n_j`$, including inputs entangled with untouched registers. Summing over the allocated segments gives total simulation error at most $`\xi_{\rm sim}`$.

## Run the rounds and read one label

For each of the $`r`$ rounds, initialize the phase register to $`|0^m\rangle`$ and apply Hadamards to its qubits. For phase qubit $`k\in\{0,\ldots,m-1\}`$, implement the controlled positive evolution at time $`2^k`$ with the corresponding segment of stored copies. Use the usual binary assignment of these powers and the inverse Fourier transform on the phase register, then measure it to obtain $`z\in\{0,\ldots,L-1\}`$. Retain the same test register for the next round and reinitialize only the phase and work registers.

Convert each measured outcome to an eigenvalue estimate in this order:

1. Interpret $`2\pi z/L`$ in $`[-\pi,\pi)`$ by subtracting $`2\pi`$ when $`z\ge L/2`$.
2. Clip that signed value to $`[0,1]`$.
3. After all rounds, take the median of the $`r`$ clipped estimates.

Output label $`1`$ exactly when the median strictly exceeds $`3t/2`$. Otherwise output label $`0`$.

For the ideal phase-estimation circuit, the [filter proof](finite_copy.md#a-finite-phase-estimation-filter) shows that an eigenvalue at most $`t`$ is accepted with probability at most $`\gamma`$, and one at least $`2t`$ is accepted with probability at least $`1-\gamma`$. The transition interval $`(t,2t)`$ is allowed; the contaminated state needs no spectral-gap promise. The proof applies the resulting diagonal effect to arbitrary test states, including coherent superpositions of eigenvectors.

## Guarantee and costs

Approximate the remaining known gates with total unhalved diamond error at most $`\xi_{\rm gate}`$. With $`\xi\le\xi_{\rm sim}+\xi_{\rm gate}`$, F1 gives

```math
R\le\frac{t}{a}+\frac1{2dt}+\gamma+\frac\xi2.
```

This is the expected classification error, including the training and measurement randomness, uniformly over the admitted pure targets and contaminants. It is not a separate confidence guarantee for every realized training record.

The [resource account](resources.md#a-finite-circuit-over-known-gates) gives the ideal-rotation processing cost and its conservative finite-gate-set synthesis bound:

```math
M=O(Nn+rm^2),
```

```math
G_{\rm proc}
=O\!\left[
(Nn+rm^2)\log^{3.97}\!\left(\frac{Nn+rm^2}{\xi_{\rm gate}}\right)
\right].
```

The inverse Fourier transforms contribute the $`rm^2`$ term. Classical comparisons and median processing have finite polynomial cost in $`r,m`$. [Finite gate-set synthesis](resources.md#finite-gate-set-synthesis) explains how the inherited Solovay–Kitaev compiler fits the gate-error budget.

If $`G_\rho`$ is the actual cost of preparing one independent training copy and $`G_{\rm test}`$ the cost of preparing the test, the full gate-work account is

```math
G_{\rm total}=NG_\rho+G_{\rm test}+G_{\rm proc}.
```

Every supplied copy is charged. Initialization, measurement and discarding also have polynomial counts and are included when assigned a nonunit cost. The circuit assumes ideal stored copies and trusted processing. Hardware connectivity would add routing costs; physical storage noise requires a separate model.

## Proof and verification boundaries

This guide restates the existing pure-source finite circuit. F1–F3 are constructive sufficient bounds. The [exact limiting-risk theorem](precision_floor.md) describes the optimal asymptotic risk at each fixed $`d,a`$; it does not assert that this finite circuit attains that law with optimal copy or gate counts. Changing the demanded precision with dimension also changes the sufficient resource budgets.

[Flat-rank recognition](flat_rank_training.md) has a separate input model, circuit and finite-copy theorem. The parameter $`r`$ used here counts repeated phase-estimation rounds, not a clean-support rank.

The existing [circuit checker](../verification/check_circuit.py) examines controlled dilations, the positive-evolution sign and finite phase-estimation cases. Its checks support the conventions used in this guide. The analytical arguments in [the finite-copy chapter](finite_copy.md) supply the universal simulation and risk guarantees; the checker is not a hardware execution backend.
