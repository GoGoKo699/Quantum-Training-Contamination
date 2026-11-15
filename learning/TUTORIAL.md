# From contaminated specimens to one reliable decision

A source can hide which pure state it meant to prepare without making every later prediction useless. The distinction becomes visible when the task is to recognize one clean specimen against a known, diffuse background. This tutorial follows one qubit example from its density matrices to the exact decision limit, then explains what changes in large dimension and how retained training specimens implement a finite decision circuit.

The [30-milestone map](MILESTONES.md) supplies the dependencies and scientific reading route. The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) identifies the relevant definitions, theorems and source locators; the project-specific arguments live in the linked science chapters.

## The three objects in the experiment

**Milestones M01–M05.** Keep the clean target, the training state and the background separate.

The clean target is a hidden pure state $`P=|\psi\rangle\langle\psi|`$ in dimension $`d`$. Every training specimen is an independent copy of

```math
\rho=aP+(1-a)\sigma,
\qquad a=1-\eta.
```

The clean fraction $`a \gt 0`$ is known. The contaminant $`\sigma`$ is an arbitrary fixed density matrix and may depend on $`P`$. A training specimen has no flag saying which part of this mixture produced it. Its accessible state is $`\rho`$, not a labeled pair consisting of a mixture component and a state.

All training specimens arrive before one test. The test has equal prior probabilities of being $`P`$ or the known background $`I_d/d`$. The positive test is clean; contamination affects training alone. The learner returns one classical label and may consume the specimens.

| Object | State | What is supplied |
|---|---|---|
| Clean target | $`P`$ | Hidden source property; no classical description |
| Training | $`\rho^{\otimes N}`$ | $`N`$ independent specimens before the test |
| Positive test | $`P`$ | One register, if the positive label was drawn |
| Negative test | $`I_d/d`$ | The same register interface, with the negative label |

The background is important. Accepting a rank-$`s`$ subspace gives a background false-positive probability $`s/d`$. A small uncertainty subspace can therefore cover several possible clean targets cheaply when $`d`$ is large. This feature would need to be reconsidered for a different background.

## A qubit source with ten percent contamination

Take $`d=2`$, $`a=9/10`$ and $`\eta=1/10`$. Define

```math
q=\frac{9-4\sqrt5}{18}
\approx0.003096005000046,
\qquad
|\psi_\pm\rangle
=\sqrt{1-q}\,|0\rangle\ \pm\sqrt q\,|1\rangle.
```

These are two different nonorthogonal candidate clean states. Pair them with opposite-sign equatorial contaminants,

```math
\sigma_+=|-\rangle\langle-|,
\qquad
\sigma_-=|+\rangle\langle+|,
\qquad
|\pm\rangle=\frac{|0\rangle\pm|1\rangle}{\sqrt2}.
```

Both pairs produce exactly the same training density matrix:

```math
\frac9{10}|\psi_+\rangle\langle\psi_+|
+\frac1{10}\sigma_+
=\frac9{10}|\psi_-\rangle\langle\psi_-|
+\frac1{10}\sigma_-
=\rho,
```

```math
\rho=
\begin{pmatrix}
\frac12+\frac1{\sqrt5}&0\\
0&\frac12-\frac1{\sqrt5}
\end{pmatrix}
\approx
\begin{pmatrix}
0.9472135955&0\\
0&0.0527864045
\end{pmatrix}.
```

The cancellation can be checked directly. Since $`\sqrt{q(1-q)}=1/18`$, the clean contribution has off-diagonal entry $`\pm1/20`$. The contaminant contributes $`\mp1/20`$. The remaining diagonal entries are the same in both cases.

Consequently no training measurement can determine which sign was clean. Giving the learner more copies does not change that fact: both instances supply precisely $`\rho^{\otimes N}`$. Even an exact classical description of $`\rho`$ leaves the sign unresolved. This is ambiguity of the mixture decomposition, rather than uncertainty caused by a short training record.

## A decision has two error terms

**Milestones M06–M12.** A binary quantum decision is an effect $`0\le E\le I_d`$. Its acceptance probability on a state $`\tau`$ is $`\mathrm{Tr}(E\tau)`$. For the present equal-prior test its error is

```math
R(E,P)=\frac{1-\mathrm{Tr}(EP)}2
       +\frac{\mathrm{Tr}E}{2d}.
```

The first term is rejection of a clean test. The second is acceptance of the background. If the target were known, taking $`E=P`$ would never reject it and would accept the background with probability $`1/d`$. The oracle error is therefore $`R_\star=1/(2d)`$.

For the qubit training state above, choose the effect $`E=|0\rangle\langle0|`$. It treats both candidate signs equally:

| Decision | Clean-test rejection | Background acceptance | Equal-prior error |
|---|---|---|---|
| Known-target oracle $`E=P`$ | $`0`$ | $`1/2`$ | $`0.25`$ |
| Robust effect $`E=\vert 0\rangle\langle0\vert `$ | $`q`$ | $`1/2`$ | $`1/4+q/2\approx0.2515480025`$ |

The distinction between risk and excess risk is visible here. The total robust error is about $`0.251548`$; the contamination excess above the oracle is about $`0.001548`$. The example attains the exact worst-case perfect-training risk at these parameters, as the general law below shows.

Coherent and classical-compilation learners differ before making this decision. A coherent learner may retain the actual training registers until the test arrives. A classical compiler may use any collective training measurement and retain an unlimited classical record, but must discard every source-dependent quantum register before the test. Its later test effect can depend on that record. Neither learner can identify the sign in this example from training alone, because their input density matrices agree. Their finite-sample costs for other admissible instances can still differ.

## Turning decomposition ambiguity into a precise feasible set

**Milestones M13–M16.** The mixture equation is equivalent to the operator inequality $`aP\le\rho`$: subtract $`aP`$, divide by $`1-a`$, and the remainder is a positive trace-one contaminant. At $`a=1`$, the promise instead forces $`\rho=P`$.

Write $`\rho=\sum_i\lambda_i|i\rangle\langle i|`$ and $`p_i=|\langle i|\psi\rangle|^2`$. On the support of $`\rho`$, conjugating by its inverse square root gives the rank-one inequality

```math
a\,\rho^{-1/2}P\rho^{-1/2}\le I
\quad\Longleftrightarrow\quad
\sum_{i:\lambda_i \gt 0}\frac{p_i}{\lambda_i}\le\frac1a.
```

A target has no weight in a zero-eigenvalue direction. Every feasible probability vector $`p`$ can have arbitrary phases in the eigenbasis. Thus the training spectrum constrains possible target amplitudes without revealing those phases.

For the qubit example, $`p=(1-q,q)`$ saturates this inequality. Replacing the relative sign by any phase also preserves compatibility. A classifier seeking a worst-case guarantee can average its effect over these phase rotations. The trace cost stays fixed and the worst compatible acceptance cannot become worse. This removes off-diagonal entries of the effect, so the robust decision can be studied through real acceptance numbers $`e_i\in[0,1]`$.

At a fixed spectrum, convex minimax then turns the best robust contrast into

```math
g_a(\lambda)
=\min_{\substack{p\in\Delta_d\\\sum_i p_i/\lambda_i\le1/a}}
\mathrm{TV}(p,u_d),
\qquad u_d=(1/d,\ldots,1/d).
```

The optimal error at this training state is $`(1-g_a(\lambda))/2`$. Total variation appears because, once $`p`$ is fixed, the best diagonal effect accepts coordinates where $`p_i \gt 1/d`$. This is the classical form of the binary discrimination calculation, reached after respecting the quantum compatibility and symmetry.

The adversary may also choose the training spectrum. For fixed $`p`$, Cauchy–Schwarz gives

```math
\min_{\lambda\in\Delta_d}\sum_i\frac{p_i}{\lambda_i}
=\left(\sum_i\sqrt{p_i}\right)^2,
\qquad
\lambda_i=\frac{\sqrt{p_i}}{\sum_j\sqrt{p_j}}.
```

The quantum source problem therefore reaches a scalar constraint on the Rényi entropy of order one half. The complete reduction is proved in [the precision chapter](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem); it is the step connecting the source’s possible decompositions to the exact prediction limit.

## The exact answer and an indistinguishable family

**Milestones M17–M20.** The sharp scalar entropy/total-variation frontier is inherited from Rioul. At a fixed overlap with the uniform distribution, its relevant extremal vector has one large coordinate, several coordinates equal to $`1/d`$, and at most one fractional coordinate:

```math
p^\star(q)
=\left(1-q,
\underbrace{1/d,\ldots,1/d}_{k\text{ coordinates}},
q-k/d,0,\ldots,0\right),
\qquad k=\lfloor dq\rfloor.
```

Its square-root sum is

```math
S_d(q)=\sqrt{1-q}+\frac{k}{\sqrt d}+\sqrt{q-k/d}.
```

For $`a \gt 1/d`$, the unique root $`S_d(q_d(a))=a^{-1/2}`$ gives

```math
R_\infty(d,a)=\frac{1/d+q_d(a)}2,
\qquad
R_\infty-R_\star=\frac{q_d(a)}2.
```

The qubit example lies in the first interval, where the root simplifies to

```math
q_2(1-\eta)
=\frac{1-\sqrt{1-[\eta/(1-\eta)]^2}}2.
```

At $`\eta=1/10`$ this is exactly the chosen $`q`$. The formula is used only when the root lies in the first interval; the scalar definition handles the other cases.

The root is not merely an optimization without a physical witness. Given $`p^\star`$, choose $`\lambda_i\propto\sqrt{p_i^\star}`$ and take a finite Fourier family of clean vectors with those amplitudes. Averaging their phases gives $`\mathrm{diag}(p^\star)`$. Each clean vector has a positive contaminant making the training density matrix equal to the same $`\rho`$. For two nonzero coordinates this finite family is precisely the two signs used above. Binary discrimination of its averaged clean test from $`I_d/d`$ gives the stated error lower bound. The robust minimax effect supplies the matching upper bound.

At $`a\le1/d`$, the common training state $`I_d/d`$ is compatible with every pure target, and the minimax error is $`1/2`$. At $`a=1`$, the limit is the oracle value. For each fixed $`d,a`$, both coherent and classical-compilation risks converge to $`R_\infty`$ as $`N\to\infty`$. Tomography can eventually estimate the common density matrix, even though it cannot identify a decomposition that the density matrix itself does not specify. This limiting statement gives no dimension-uniform sample rate.

## Dimension helps recognition while ambiguity remains

**Milestones M21–M24.** For small contamination, the unavoidable excess obeys the uniform order

```math
R_\infty(d,1-\eta)-\frac1{2d}
=\Theta\!\left(\min\left\{\eta^2,\frac\eta{\sqrt d}\right\}\right),
\qquad 0 \lt \eta\le1/4.
```

At each fixed $`a\in(0,1)`$, the large-dimension expansion is

```math
R_\infty(d,a)
=\frac{a^{-1/2}-1}{2\sqrt d}+O_a(d^{-1}).
```

The infinite-training limit is taken at fixed dimension first. The dimension expansion is a second, separate limit. At ten percent contamination, the qubit risk is about $`0.251548`$; at $`d=2^{20}`$ the exact limiting risk is about $`2.678608\times10^{-5}`$. These numbers concern perfect training-state information, not finite-sample hardware performance.

The known-state oracle decreases faster, as $`1/(2d)`$. Although the absolute contamination excess vanishes, its ratio to the oracle error grows as order $`\sqrt d`$ for fixed nonzero contamination. Vanishing error is therefore different from matching oracle scaling.

There is also a source-level contrast. If the contaminant must commute with the clean state, exact training restricts the target to eigenspaces of $`\rho`$ whose eigenvalues are at least $`a`$. Accepting their union is optimal, giving

```math
R_\infty^{\rm comm}(d,a)
=\frac{\min\{d,\lfloor1/a\rfloor\}}{2d}.
```

No common basis is supplied in this comparison. It changes only the contamination promise. For $`a \gt 1/2`$, the clean eigendirection is unique and there is no contamination excess. The qubit example uses noncommuting contaminants and thus exhibits a positive excess that the commuting promise excludes.

Recognition can also succeed when reconstruction cannot. Two distinct pure targets can share a training density matrix while remaining a constant trace distance apart. An estimator of the clean state must then be wrong for at least one of them. A classifier has the different option of covering uncertain directions at a background cost proportional to their dimension. [The reconstruction comparison](../science/precision_floor.md#recognition-does-not-require-reconstructing-the-clean-state) proves this distinction quantitatively; it does not infer recovery from a good label predictor.

## Building a finite decision from retained specimens

**Milestones M25–M29.** The finite circuit works without first printing the density matrix. It uses a spectral acceptance effect $`f(\rho)`$ that mostly rejects eigenvalues at most $`t`$ and mostly accepts eigenvalues at least $`2t`$. Behavior inside the transition interval is unrestricted; an eigenvalue gap around the threshold is not promised.

The inverse-compatibility inequality makes the tradeoff transparent. The clean target has weight at most $`2t/a`$ in eigenvalues below $`2t`$. Conversely, there are at most $`1/t`$ eigenvalues above $`t`$, so accepting all those directions costs at most $`1/(dt)`$ background probability. With spectral-estimation failure $`\gamma`$ and total unhalved diamond implementation error $`\xi`$, the resulting risk satisfies

```math
R\le\frac ta+\frac1{2dt}+\gamma+\frac\xi2.
```

To implement the effect, the circuit performs phase estimation of $`e^{i\rho}`$ on the test and takes a median of repeated estimates. The evolution is synthesized by consuming the stored training copies through known controlled partial swaps. A one-copy step approximates the desired controlled evolution with error of order the squared step size. Adding those errors in diamond norm covers the whole test circuit, including untouched references. Control is applied to known swap gates; no controlled preparation oracle or controlled unknown unitary is supplied.

The [finite-copy proof](../science/finite_copy.md) makes this finite: it specifies the phase-register size, the number of repetitions, the integer number of copies used in every simulated evolution, and the gate-synthesis error budget. One sufficient choice gives

```math
R\le\varepsilon,
\qquad
N=O\!\left(a^{-2}\varepsilon^{-3}
                  \log^2(1/\varepsilon)\right),
\qquad
d\ge\frac8{a\varepsilon^2}.
```

At fixed clean fraction and fixed target risk, this sample budget is independent of dimension. A clean majority is not required in that regime. The qubit decision table earlier describes the exact-density limit; it is not a claim that this sufficient large-dimension cutoff bound attains that table with a particular finite sample budget.

For $`\eta\le1/4`$, a constant-gap leading-eigenvector filter is useful above an $`O(\eta^2)`$ excess scale. A lower spectral threshold handles finer precision in a sufficiently large dimension. Its sufficient copy count can grow as $`d^{3/2}`$ near the $`\eta/\sqrt d`$ floor. These upper bounds do not establish the optimal joint dependence on precision, dimension and sample number.

The storage and preparation charges remain concrete. All $`N`$ specimens are retained before the test, using $`N\lceil\log_2d\rceil`$ training qubits. Sequential consumption reduces active processing width, not that offline storage. If one source specimen costs $`G_\rho`$, the account includes $`NG_\rho`$, the one test, known gates, finite gate synthesis and the final output bit. This is native quantum-state access, with no free loading of a classical feature table.

A classical compiler still needs $`\Omega(d)`$ training specimens at fixed nontrivial error in the worst case, through an inherited clean subfamily contained in the contaminated model. That comparator allows collective training measurements and unlimited classical records and computation. The separation concerns what can be retained across the train–test boundary. It is distinct from the infinite-training floor, which both learner classes eventually share.

## The connected scientific claim

**Milestone M30.** A contaminated density matrix can leave nonorthogonal clean targets indistinguishable, yet one clean recognition decision can have vanishing error against a known maximally mixed background. The exact scalar root measures the unavoidable cost of that ambiguity. The commuting comparison identifies a larger precision penalty permitted by noncommuting contamination. The finite-copy circuit then supplies an explicit way to make useful predictions from retained specimens, with its own achievable accuracy and resource bounds.

The source is IID, the clean target is pure, the positive test is clean, and the background is known. The result concerns one consumable prediction under ideal processing. These assumptions do not cover correlated poisoned batches, arbitrary backgrounds, noisy tests or repeated model reuse. Rioul’s scalar extremal, binary discrimination and convex minimax, density-matrix simulation, and clean quantum-reference advantages are inherited tools; [the related-work account](../references/related_work.md) distinguishes them from the operational contamination result.
