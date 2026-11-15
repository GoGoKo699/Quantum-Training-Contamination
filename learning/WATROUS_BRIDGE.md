# From Watrous to clean prediction with contaminated training

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. This bridge uses the author's **standard-layout pre-publication manuscript** linked from his [official book page](https://cs.uwaterloo.ca/~watrous/TQI/). All page numbers below are the printed page numbers in that layout; a chapter PDF's viewer-page count differs. The official source provides access to the manuscript. No copy is redistributed here.

The problem begins with a familiar distinction. A device can learn enough to make a decision without learning everything about its source. Here training copies contain an unknown admixture, while the later positive test is clean. Different pure sources can explain exactly the same training density matrix. The scientific question is how much recognition error that unresolved explanation forces.

Use this bridge beside the [worked tutorial](TUTORIAL.md) and the [30-milestone map](MILESTONES.md). The [model](../science/model.md) is authoritative for the experiment and theorem scope. Reading the whole textbook is unnecessary.

## Targeted source map

| Need in the project | Verified Watrous location, standard layout | What to carry into this project |
|---|---|---|
| Positive operators, supports, and spectral functions | §1.1.2, pp. 17–20; §1.1.3, pp. 24–28 | Operator positivity and diagonalization justify testing whether a proposed contaminant is a state. |
| Compact convex optimization | §1.2.1, pp. 35–47; Theorem 1.12, pp. 46–47 | Sion's theorem permits the continuous bilinear minimax interchange used here. |
| Independent repetitions | §1.2.2; Theorem 1.16, p. 51 | Bounded-outcome concentration supports tomography and repeated spectral-estimation rounds. |
| Density matrices, mixtures, and discarded registers | §2.1.2, p. 61 onward; mixtures p. 63; §2.1.3, p. 67 onward | An unflagged mixture is one density operator; discarding a program register is a partial trace. |
| Channels and binary effects | §2.2.1, p. 72 onward; §2.3.1, p. 100 onward | A physical learner is a channel, and one label is represented by a two-outcome measurement. |
| Optimal binary and composite decisions | §3.1.1; Theorem 3.4, p. 128; Theorem 3.7, pp. 131–132 | Trace-norm discrimination and convex uncertainty sets provide the decision-theoretic foundation. |
| Norm conventions and composed circuit error | §3.3.2; Definition 3.43, p. 170; Proposition 3.48, p. 174 | The completely bounded trace norm controls an implementation even when its input has a reference system. |
| Removing irrelevant phases | §4.1.1; Definition 4.4, p. 203 | Pinching provides the channel language for suppressing off-diagonal entries. |
| Ordering probability vectors | §4.3.1, p. 233 onward; Definition 4.29, p. 235 | Majorization fixes the direction of the scalar extremal argument. |
| An optional connection to ensemble ambiguity | §4.3.2; Theorem 4.34, pp. 245–246 | A density matrix can admit nonorthogonal pure-state ensembles; its spectrum need not identify its preparation history. |

These sections supply foundations. The exact contamination reduction and asymptotic limits are proved in [the precision account](../science/precision_floor.md). Rioul's entropy boundary and sample-based Hamiltonian simulation remain explicitly cited research ingredients, not extra educational anchors.

## Conventions

| Watrous notation or convention | Notation here |
|---|---|
| A unit column vector $`u`$ and its matrix $`uu^*`$ | $`\vert \psi\rangle`$ and $`P=\vert \psi\rangle\langle\psi\vert `$ |
| $`\mathrm D(\mathcal X)`$, $`\mathrm{Pos}(\mathcal X)`$, identity $`1_{\mathcal X}`$ | Density operators, positive semidefinite operators, and $`I_d`$ on $`\mathbb C^d`$ |
| A measurement $`\mu`$ with outcomes zero and one | $`\mu(1)=E`$, $`\mu(0)=I-E`$; $`E`$ means predict the clean class |
| Hilbert–Schmidt pairing $`\langle A,B\rangle=\mathrm{Tr}(A^*B)`$ | For effects and states, $`\mathrm{Tr}(E\rho)`$ is an acceptance probability |
| Root fidelity $`F(\rho,\tau)=‖\sqrt\rho\sqrt\tau‖_1`$ (§3.2) | Reconstruction overlap $`\mathrm{Tr}(P\widehat\tau)`$ equals $`F(P,\widehat\tau)^2`$ |
| Completely bounded trace norm $`\vert \vert \vert \Phi\vert \vert \vert _1`$ | $`‖\Phi‖_\diamond`$, unhalved; a separately named normalized channel distance is half this value |
| $`v\prec u`$ means $`u`$ majorizes $`v`$ | $`p\prec p^*(q)`$; the concentrated vector is on the majorizing side |

The project writes $`D(\rho,\tau)=\frac12‖\rho-\tau‖_1`$ when using normalized trace distance. Total classification risk $`R`$ is an error probability; excess risk is $`R-1/(2d)`$. Neither quantity is the fidelity or the norm error of a reconstructed state. The control error $`\xi`$ in the finite-copy theorem is an **unhalved** diamond bound, so its contribution to risk is at most $`\xi/2`$.

## From the book to the prediction floor

### 1. A mixture gives a compatibility set

Let $`a\in(0,1]`$ be known, and let the independent training specimens have state

```math
\rho=aP+(1-a)\sigma,\qquad P=|\psi\rangle\langle\psi|.
```

The learner has no preparation description or flag telling it which part was clean. Even exact knowledge of $`\rho`$ leaves all pure $`P`$ satisfying $`aP\preceq\rho`$ possible. For $`a \lt 1`$, the converse is immediate: $`(\rho-aP)/(1-a)`$ is a valid contaminant whenever that inequality holds.

The book's positivity language now turns an explanation of a source into a checkable inequality. On the support of $`\rho`$, conjugation by $`\rho^{-1/2}`$ gives a rank-one operator dominated by the identity. Diagonalizing $`\rho=\sum_i\lambda_i|i\rangle\langle i|`$ and writing $`p_i=|\langle i|\psi\rangle|^2`$ yields the project's local derivation

```math
aP\preceq\rho
\quad\Longleftrightarrow\quad
\sum_{\lambda_i \gt 0}\frac{p_i}{\lambda_i}\le\frac1a,
\qquad p_i=0\ \text{when}\ \lambda_i=0.
```

An inverse on the full space was not assumed: zero eigenvalues exclude clean components outside the support. This distinction matters in the least-favorable examples, whose training states can have low rank.

### 2. A decision effect pays for missed signal and accepted background

One later test is either the clean $`P`$ or $`I/d`$, with equal priors. The binary effect $`E`$ therefore has risk

```math
R(E,P)=\frac{1-\mathrm{Tr}(EP)+\mathrm{Tr}(E)/d}{2}.
```

The first error term rejects the clean test. The second accepts background. If $`P`$ were known, accepting only its ray gives $`R_\star=1/(2d)`$. A larger accepted subspace can hedge uncertainty, but its dimension increases the background cost. This explicit cost is why state reconstruction and prediction can have very different robustness.

### 3. Phase symmetry turns the robust decision into a probability game

Independent phase rotations in an eigenbasis leave $`\rho`$ unchanged and preserve all compatible targets. Averaging any proposed effect over them preserves its trace and cannot worsen its minimum acceptance over that set. This is a project-specific use of pinching, not permission to dephase the unknown clean test experimentally.

An optimal robust effect may thus be diagonal with entries $`e_i\in[0,1]`$. Its compatible probability vectors form a compact convex set $`K_\lambda`$. Applying the verified minimax theorem gives

```math
\max_e\min_{p\in K_\lambda}\sum_i e_i(p_i-1/d)
=\min_{p\in K_\lambda}\sum_i(p_i-1/d)_+
=\min_{p\in K_\lambda}\mathrm{TV}(p,u_d).
```

Here $`u_d`$ is uniform. After $`p`$ is fixed, the maximizing effect accepts its positive excess coordinates. The minimax equality is what permits using this choice to evaluate a learner that must commit before knowing the target. It is not an illicit assumption that the learner already knows $`p`$.

### 4. Eliminating the spectrum exposes the entropy boundary

The worst source also chooses $`\lambda`$. For fixed $`p`$, Cauchy–Schwarz shows that its smallest compatible harmonic sum is

```math
\min_{\lambda\in\Delta_d}\sum_i\frac{p_i}{\lambda_i}
=\left(\sum_i\sqrt{p_i}\right)^2,
\qquad
\lambda_i=\frac{\sqrt{p_i}}{\sum_j\sqrt{p_j}}.
```

Zero coordinates are handled on the support. This produces the exact operational identity

```math
1-2R_\infty(d,a)
=\min_{p:\,(\sum_i\sqrt{p_i})^2\le1/a}
\mathrm{TV}(p,u_d).
```

The square-root sum can be written as a Rényi-entropy constraint, but introducing entropy has not supplied a new data-access assumption. It has expressed the set of compatible quantum explanations as a classical optimization.

At fixed $`q=1-\mathrm{TV}(p,u_d)-1/d`$, Rioul's established sharp boundary is attained by $`p^*(q)`$: one leading coordinate $`1-q`$, as many $`1/d`$ coordinates as fit, one remainder, and zeros. Watrous's majorization convention explains why concentration lowers the square-root sum. The exact extremal and its provenance are given in [the proof](../science/precision_floor.md#evaluating-the-inherited-entropy-frontier) and [related work](../references/related_work.md#rioul2023). This research ingredient is beyond the textbook's foundational map.

### 5. A finite Fourier family makes the lower bound physical

For the extremal $`p`$, choose $`\rho`$ with eigenvalues proportional to $`\sqrt{p_i}`$. Let its $`s`$ occupied coordinates carry the Fourier-phase targets

```math
|\psi_\ell\rangle
=\sum_{j=0}^{s-1}\sqrt{p_j}\,e^{2\pi i\ell j/s}|j\rangle,
\qquad 0\le\ell \lt s.
```

Every target has a valid contaminant and produces this same $`\rho`$. Averaging the $`s`$ targets cancels off-diagonal entries. Thus the training systems reveal no target index, and ordinary binary discrimination of the averaged target against $`I/d`$ gives the bound already found by minimax. The issue is an indistinguishable source family, so allowing a collective measurement on arbitrarily many training copies cannot remove it.

The [commuting comparison](../science/commuting_comparison.md) identifies the escaped ambiguity: if $`[\sigma,P]=0`$, the clean vector must lie in an eigenspace with eigenvalue at least $`a`$. Accepting those eigenspaces costs only their dimension divided by $`d`$. Their dimension is at most $`\min\{d,\lfloor1/a\rfloor\}`$. For $`a \gt 1/2`$, this recovers the oracle limit, whereas unrestricted contamination still has a positive excess whenever $`a \lt 1`$.

## From an information limit to a finite experiment

Knowing a density matrix exactly is a benchmark. It does not provide an implementation. The [finite-copy chapter](../science/finite_copy.md) instead retains the supplied specimens until the single test arrives and uses known controlled partial-SWAP gates. Fresh stored copies drive an approximation to controlled $`e^{it\rho}`$; no controlled unknown source circuit or inverse is supplied.

Phase estimation then produces a soft spectral effect $`f(\rho)`$. Eigenvalues below $`t`$ are usually rejected; those above $`2t`$ are usually accepted. The band between them is allowed to be arbitrary. The harmonic compatibility bound controls the clean weight in low modes, while trace one bounds how many high modes can falsely accept background. The phase-estimation probability formula, its finite-tail estimate, and DME are derived locally and attributed to their primary sources. Watrous supplies channel and probability foundations rather than an unstated phase-estimation theorem.

Composition in the completely bounded trace norm makes the error allocation valid while the test is correlated with work registers. Each program copy is discarded after its controlled interaction. The exact scalar floor, the filter's statistical failure $`\gamma`$, its implementation error $`\xi`$, and the cost of finite-precision gate synthesis are separate quantities. [F1–F3](../science/finite_copy.md) state the achievable upper bounds and their parameter regimes.

Finally, [the resource account](../science/resources.md) charges preparation, every stored training system, known gates, and the one consumed test. The clean subfamily supplies the inherited classical-compilation lower bound. The dimension-independent quantum copy statement fixes the target risk and clean fraction before growing $`d`$; substituting a dimension-dependent precision can change the comparison. Likewise, the exact information limit takes $`N\to\infty`$ first at fixed $`d,a`$. These are different conclusions, and neither is an optimal joint finite-copy law or a hardware-noise guarantee.

Continue with the [tutorial](TUTORIAL.md) for a complete qubit instance, or use [the milestone map](MILESTONES.md) to connect these steps to the full proofs. Research citations remain in [related work](../references/related_work.md); Watrous remains the only educational anchor.
