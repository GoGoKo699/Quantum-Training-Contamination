# Classification with finitely many contaminated training copies

The exact information limit asks what remains unknown even when the training density matrix is known perfectly. This chapter gives a finite circuit that uses copies of that density matrix directly. It accepts the spectral modes that could carry appreciable weight of the clean target. No spectral-gap promise is imposed on the contaminated state.

The input is $`N`$ independent copies of

```math
\rho=aP+(1-a)\sigma,\qquad
P=|\psi\rangle\langle\psi|,\qquad 0 \lt a\le1.
```

All training copies arrive before the test. The learner retains them, then consumes them while classifying one test drawn with equal prior probabilities from $`P`$ or $`I/d`$. There is no post-test source access. The output is one classical label. The [resource account](resources.md) includes the stored training registers and the cost of preparing every supplied copy.

## F1: a spectral classifier without a gap promise

Let $`0 \lt t\le1/4`$, $`0 \lt \gamma \lt 1/2`$, and $`\xi \gt 0`$. There is a finite circuit with classification risk

**Equation (F1).**

```math
R\le \frac{t}{a}+\frac{1}{2dt}+\gamma+\frac{\xi}{2}.
```

Here $`\gamma`$ is the ideal spectral-estimation failure probability, and $`\xi`$ bounds the **unhalved** diamond distance between the implemented measurement channel and that ideal circuit. The circuit does not need the eigenvectors or eigenvalues of $`\rho`$ in classical form.

Choose a power of two $`L=2^m\ge64\pi/t`$ and let $`r`$ be an odd integer satisfying $`r\ge4\ln(1/\gamma)`$. The ideal circuit uses $`r`$ standard phase-estimation experiments for $`e^{i\rho}`$, taking the median of their eigenvalue estimates. Its controlled evolution times are $`T_j\in\{2^0,2^1,\ldots,2^{m-1}\}`$, repeated $`r`$ times, with

```math
K=rm,\qquad
T_{\rm tot}=\sum_{j=1}^{K}T_j=r(L-1).
```

For any allocated simulation error $`\xi_{\rm sim} \gt 0`$, it suffices to supply

**Equation (F1a).**

```math
n_j=\left\lceil\frac{4T_jT_{\rm tot}}{\xi_{\rm sim}}\right\rceil,
\qquad
N=\sum_{j=1}^{K}n_j
\le\frac{4T_{\rm tot}^2}{\xi_{\rm sim}}+K
```

copies, and to approximate the remaining known gates with total unhalved diamond error at most $`\xi_{\rm gate}`$. Then $`\xi\le\xi_{\rm sim}+\xi_{\rm gate}`$. The ceiling bound can be replaced by a strict inequality when its right side is nonintegral; the displayed nonstrict bound is valid.

### Why the spectral cutoff controls the prediction risk

Let $`\rho=\sum_i\lambda_i|i\rangle\langle i|`$ and $`p_i=|\langle i|\psi\rangle|^2`$. The contamination promise implies

**Equation (1).**

```math
aP\le\rho,
\qquad
\sum_{i:\lambda_i \gt 0}\frac{p_i}{\lambda_i}\le\frac1a,
\qquad
p_i=0\ \text{if}\ \lambda_i=0.
```

The ideal phase-estimation circuit has a diagonal acceptance effect $`F=f(\rho)`$ with

**Equation (2).**

```math
0\le f(\lambda)\le1,\qquad
f(\lambda)\le\gamma\quad(\lambda\le t),\qquad
f(\lambda)\ge1-\gamma\quad(\lambda\ge2t).
```

No restriction is needed inside the transition interval $`(t,2t)`$. Equation (1) gives

```math
\mathrm{Tr}[(I-F)P]
\le\sum_{\lambda_i \lt 2t}p_i+\gamma
\le\frac{2t}{a}+\gamma.
```

At most $`1/t`$ eigenvalues exceed $`t`$, because $`\mathrm{Tr}\rho=1`$. Hence

```math
\frac{\mathrm{Tr}F}{d}
\le\frac1{dt}+\gamma.
```

The risk is half the sum of these two error probabilities. An unhalved diamond perturbation of at most $`\xi`$ changes either conditional binary outcome probability by at most $`\xi/2`$, so it changes their average risk by at most $`\xi/2`$. This proves (F1).

### A finite phase-estimation filter

For an eigenstate with eigenvalue $`\lambda\in[0,1]`$, one standard phase-estimation round produces an outcome $`z\in\{0,\ldots,L-1\}`$ with probability

**Equation (3).**

```math
\Pr(z\mid\lambda)
=\left|\frac1L\sum_{\ell=0}^{L-1}
e^{i\ell(\lambda-2\pi z/L)}\right|^2.
```

Interpret $`2\pi z/L`$ in $`[-\pi,\pi)`$, then clip the result to $`[0,1]`$. Call this estimate $`\widehat\lambda`$. Let $`z_0`$ be a nearest phase-grid point to $`\lambda`$. If $`z`$ has circular grid-index distance $`j\ge1`$ from $`z_0`$, its phase distance is at least $`(2\pi/L)(j-1/2)`$. Using $`|\sin(x/2)|\ge|x|/\pi`$ for $`|x|\le\pi`$ in the geometric sum gives

```math
\Pr(z\mid\lambda)\le\frac1{4(j-1/2)^2}.
```

There are at most two outcomes at each positive distance. Therefore the total probability of $`j\ge10`$ is at most

**Equation (4).**

```math
\frac12\sum_{j=10}^{\infty}\frac1{(j-1/2)^2}
\le\frac1{17}.
```

For the remaining outcomes, the phase error is below $`20\pi/L\le5t/16 \lt t/2`$. Unwrapping and clipping do not increase this error, since the true eigenvalue lies in $`[0,1]`$ and this interval is separated from the phase branch cut. Thus a round estimates $`\lambda`$ to error strictly below $`t/2`$ with failure probability at most $`1/17`$.

Conditional on an eigenstate, repeated ideal rounds leave that eigenstate unchanged and use fresh phase registers. Hoeffding's inequality bounds the probability that a majority of the $`r`$ rounds fail by

```math
\exp\!\left[-2r\left(\frac12-\frac1{17}\right)^2\right]
\le e^{-r/4}\le\gamma.
```

Accept when the median estimate exceeds $`3t/2`$. An eigenvalue at most $`t`$ is rejected, and one at least $`2t`$ is accepted, whenever the median estimate is good. This proves (2), including the band endpoints. Linearity then gives the same diagonal effect on every test state, including coherent superpositions of eigenvectors.

### Controlled density-matrix simulation from copies

The simulator uses known swap gates; it does not assume controlled access to an unknown unitary. Let $`C`$ be a control qubit, $`A`$ the test, and $`B`$ one training register in state $`\rho`$. Put

```math
H=|1\rangle\langle1|_C\otimes\mathrm{SWAP}_{AB},
\qquad
H_{\rm eff}=|1\rangle\langle1|_C\otimes\rho_A.
```

The physical one-copy map and the desired one-step channel are

```math
\Phi_h(X)=\mathrm{Tr}_B
\left[e^{-ihH}(X\otimes\rho_B)e^{ihH}\right],
\qquad
\mathcal U_h(X)=e^{-ihH_{\rm eff}}Xe^{ihH_{\rm eff}}.
```

Their zeroth- and first-order terms agree:

**Equation (5).**

```math
\mathrm{Tr}_B[H,X\otimes\rho]
=[H_{\rm eff},X].
```

This identity also holds when $`X`$ includes an arbitrary untouched reference. Both Hamiltonians have operator norm at most one. The second-order integral remainder of either unitary channel has diamond norm at most $`2h^2`$: its commutator generator has diamond norm at most two, while unitary channels, tensoring with a state, and partial trace have diamond norm one. Consequently

**Equation (6).**

```math
‖\Phi_h-\mathcal U_h‖_\diamond\le4h^2.
```

This bound holds for real $`h`$, with either sign. Composing $`n`$ fresh-copy steps of size $`h=T/n`$ and using a channel hybrid gives

**Equation (7).**

```math
‖\Phi_{T/n}^{,n}-\mathcal U_T‖_\diamond
\le\frac{4T^2}{n}.
```

The ideal phase-estimation circuit uses positive exponents $`e^{+i\rho T_j}`$. For each such segment, take the physical step $`h=-T_j/n_j`$ in (6). Apply (7), with this sign change, to every controlled evolution in phase estimation. The allocation (F1a) makes the sum of the simulation errors at most $`\xi_{\rm sim}`$. Measurements, classical median processing, and adaptive control do not enlarge the hybrid bound. The construction uses only the stored independent program copies. Correlations created among the remaining test and work registers are already covered by the diamond norm.

Density-matrix exponentiation and its dimension-independent sample order are inherited from [Lloyd, Mohseni and Rebentrost](https://doi.org/10.1038/nphys3029), [Kimmel et al.](https://doi.org/10.1038/s41534-017-0013-7), and the current rigorous analysis of [Go et al.](https://arxiv.org/abs/2412.02134v3). The controlled calculation (5)–(7) makes the precise access used here explicit; it does not confer control over an independently supplied unknown evolution.

## F2: arbitrary positive clean fraction

For $`0 \lt \varepsilon\le1/4`$, suppose

```math
d\ge\frac8{a\varepsilon^2}.
```

Take $`t=a\varepsilon/4`$, $`\gamma=\varepsilon/4`$, and allocate $`\xi_{\rm sim}=\xi_{\rm gate}=\varepsilon/4`$. Then (F1) gives

**Equation (F2).**

```math
R\le\varepsilon,
\qquad
N=O\!\left(
\frac{\log^2(1/\varepsilon)}{a^2\varepsilon^3}
\right).
```

The constants are universal and an explicit finite copy allocation is (F1a). At fixed $`a \gt 0`$ and fixed risk, the number of training copies does not depend on $`d`$. In particular, the clean target need not be the majority component. This is one clean-test prediction against the known maximally mixed background; it is not recovery of the clean target state or identification of which mixture component was clean.

## F3: dependence on a small contamination fraction

Write $`\eta=1-a`$ and assume $`0\le\eta\le1/4`$. Let $`v=\lambda_1(\rho)`$ and $`b=1-v`$. Then $`v\ge a`$, $`b\le\eta`$, and all other eigenvalues are at most $`\eta`$. When $`t\le a/4`$, subtracting the largest-eigenvalue contribution from (1) gives

```math
\sum_{i\ge2}p_i\left(\frac1{\lambda_i}-\frac1v\right)
\le\frac{v-a}{av}.
```

There is no contribution from the largest eigenvector below $`2t`$. Thus

```math
\sum_{\lambda_i \lt 2t}p_i
\le\frac{2t(v-a)}{a(v-2t)}.
```

Moreover at most $`b/t`$ nonprincipal eigenvalues exceed $`t`$. The same finite circuit therefore satisfies the more precise bound

**Equation (F3).**

```math
R-\frac1{2d}
\le
\frac{t(v-a)}{a(v-2t)}+\frac{b}{2dt}
+\gamma+\frac\xi2
\le\frac{2\eta t}{a^2}+\frac\eta{2dt}
+\gamma+\frac\xi2.
```

This statement uses no knowledge of $`v`$ or $`b`$ in the implementation; its final bound depends only on the promised contamination level.

For $`0 \lt \eta\le1/4`$, $`0 \lt \varepsilon\le\eta^2`$, and

```math
d\ge\frac{16\eta^2}{a^2\varepsilon^2},
```

choose $`t=a^2\varepsilon/(8\eta)`$ and the same error allocation as in F2. Then $`t\le a/4`$ and

**Equation (F3a).**

```math
R\le\frac1{2d}+\varepsilon,
\qquad
N=O\!\left(
\frac{\eta^2\log^2(1/\varepsilon)}{a^4\varepsilon^3}
\right).
```

The required precision is above a constant multiple of $`\eta/\sqrt d`$, consistent with the exact information floor. The displayed sample order is an achievable upper bound, not an optimal finite-copy law.

### A coarse-precision branch close to the clean problem

Let $`|v_1\rangle`$ be a top eigenvector. Projecting its eigenvalue equation onto the orthogonal complement of $`|\psi\rangle`$ yields

```math
v(I-P)|v_1\rangle
=\eta(I-P)\sigma|v_1\rangle.
```

Hence $`1-|\langle\psi|v_1\rangle|^2\le\eta^2/a^2`$. The top-eigenvector projector has risk at most

```math
\frac1{2d}+\frac{\eta^2}{2a^2}.
```

Here the top eigenvalue is at least $`3/4`$ and the remaining ones at most $`1/4`$. The phase-estimation filter with $`t=1/4`$ therefore approximates this projector with a constant spectral separation. Allocating spectral failure and implementation error to a total risk increment $`\delta\in(0,1/4]`$ gives

**Equation (F3b).**

```math
R\le\frac1{2d}+\frac{\eta^2}{2a^2}+\delta,
\qquad
N=O\!\left(\delta^{-1}\log^2(1/\delta)\right).
```

For $`\eta=0`$ this recovers the clean inverse-precision order up to logarithms. F3b is useful above the $`O(\eta^2)`$ ambiguity scale; F3a addresses finer precision when the dimension permits it.

## What these bounds establish

The exact contamination law and the finite-copy bounds answer different questions. The former is the optimal limiting risk; F1–F3 give explicit implementations and sufficient sample budgets. Substituting a precision that decreases with dimension into these budgets can remove their fixed-precision copy advantage. No matching joint law in $`N,d,a`$, no optimal gate count, and no reusable quantum model are asserted. The construction assumes ideal stored copies and trusted known gates; synthesis error is included, while physical storage and gate noise require a separate model.
