# Recognizing a flat-rank source from contaminated training

The [pure-source precision floor](precision_floor.md) treats one unknown ray. Here the clean class is uniform on an unknown rank-$`r`$ support $`P`$. The balanced model $`d=2r`$ gives matching finite-copy risk bounds for both coherent retention and measurement-first compilation. It also gives an exact limiting recognition error when the contamination is below the clean population of one support direction.

## Model and result

The known rank is $`r\ge1`$, the dimension is $`d=2r`$, and the known clean fraction is $`a\in(0,1]`$. Write

```math
\eta=1-a,\qquad \alpha=a/r,\qquad x=\eta/\alpha,\qquad
\rho=\alpha P+\eta\sigma.
```

The unknown density operator $`\sigma`$ is fixed within an instance and can depend on $`P`$. The learner receives at most $`N`$ IID copies of $`\rho`$ before one test, which is $`P/r`$ or $`I/(2r)`$ with equal prior probabilities. A coherent learner may retain the training systems. A classical compiler may measure them collectively and keep an unlimited classical record before the test arrives. The test and source copies are independent conditional on the hidden parameters and the test label.

If $`E`$ is the effect for accepting the clean class, the error and excess over the oracle are

```math
R(E,P)=\frac{1-\operatorname{tr}(EP)/r+\operatorname{tr}(E)/(2r)}2,
\qquad
R(E,P)-\frac14
=\frac{\operatorname{tr}[P(I-E)]+\operatorname{tr}[(I-P)E]}{4r}.
```

For a training protocol this effect is induced by fixing the training state, with any measurement randomness averaged. Let $`E_{\rm Q}(N;r,a)`$ and $`E_{\rm C}(N;r,a)`$ denote the minimax excess for the coherent learner and the classical compiler, respectively. For all $`N\ge1`$ and both learner classes the bounds hold with absolute constants:

```math
E_{\rm Q}(N;r,a),\ E_{\rm C}(N;r,a)
=\Theta\!\left(
\min\left\{1,\frac{r^2}{N}+\frac{\min\{x^2,x,r\}}{r}\right\}\right).
```

With $`N=0`$ both minimax excesses equal $`1/4`$. At fixed $`r,a`$ with $`0\le x\lt1`$, the exact limit in either class is

```math
\lim_{N\to\infty} E_{\rm Q}(N;r,a)
=\lim_{N\to\infty} E_{\rm C}(N;r,a)
=\frac{1-\sqrt{1-x^2}}{4r}.
```

The two finite-copy terms have separate origins. A subfamily has the full clean classification cost. Other instances leave different clean supports compatible with exactly the same specimen. At balanced rank, tomography followed by a support measurement attains the same risk order as coherent retention.

## Common specimens and the recognition converse

Two rank-$`r`$ projectors $`P,Q`$ can yield one shared density matrix exactly when

```math
\sum_i\sin\theta_i(P,Q)\le x,
```

where $`\theta_i(P,Q)`$ are their principal angles. To see this, write $`A=\alpha P`$, $`B=\alpha Q`$. A common training density must dominate both $`A`$ and $`B`$. For any such upper bound $`X`$, use the support projector $`\Pi`$ of $`(A-B)_+`$ to obtain

```math
\operatorname{tr}X
\ge \operatorname{tr}(\Pi A)+\operatorname{tr}[(I-\Pi)B]
=a+\frac12\lVert A-B\rVert_1.
```

The operator $`B+(A-B)_+`$ realizes equality. If its trace is at most one, adding any positive operator of the remaining trace gives a common $`\rho`$. For $`\eta\gt0`$ the differences $`(\rho-A)/\eta`$ and $`(\rho-B)/\eta`$ are valid contaminants. At $`\eta=0`$ the condition forces $`P=Q`$. On each principal plane the two eigenvalues of $`P-Q`$ are $`\pm\sin\theta_i`$, which yields the stated criterion. This follows the same indistinguishability principle as the classical contamination modulus of [Chen, Gao, and Ren, Theorem 3.2](https://arxiv.org/abs/1511.04144), with the positive operator calculation replacing total variation of distributions.

Under equal prior weights on two compatible hidden supports, their common training state contributes no distinction. The average clean test is $`(P+Q)/(2r)`$. In each principal plane its eigenvalues are $`(1\pm\cos\theta_i)/(2r)`$. Zero-angle directions may be paired with common kernel directions because $`d=2r`$. Binary state discrimination against $`I/(2r)`$ then gives average excess

```math
\frac{1}{4r}\sum_{i=1}^r (1-\cos\theta_i).
```

For $`0\le x\le1`$ choose one plane with $`\sin\theta_1=x`$. For $`x\ge1`$ choose $`\min\{r,\lfloor x\rfloor\}`$ mutually orthogonal planes with angle $`\pi/2`$. This proves the lower bound of order $`\min\{x^2,x,r\}/r`$ for every specimen count and both learner classes.

The admissible choice $`\sigma=P/r`$ reduces training to the clean experiment of [Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits). Its [coherent precision converse, Q2](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/997088928d85e363fbbed1a913d6fd9284ba643f/science/quantum_precision.md) gives excess of order at least $`\min\{1,r^2/N\}`$ at $`d=2r`$ by keeping the clean contrast $`(1-r/d)/2=1/4`$. Every classical compiler is a coherent learner with a restriction on retained information, so this converse also applies to it. Taking the larger of the two independent lower bounds gives the stated order.

## Coherent construction with finite copies

Use a Hadamard test for the controlled evolution with data-branch unitary

```math
U=e^{-iT\rho},\qquad T=\pi/\alpha,\qquad U_0=e^{-i\pi P}=I-2P.
```

Assign the minus control outcome to the clean class. The ideal measurement effect is $`E=(I-(U+U^\dagger)/2)/2`$. The missed clean mass and the accepted background mass in the excess formula are

```math
\operatorname{tr}[P(I-E)]=\frac{\lVert (U+I)P\rVert_F^2}{4},
\qquad
\operatorname{tr}[(I-P)E]=\frac{\lVert (U-I)(I-P)\rVert_F^2}{4}.
```

Together these give the exact ideal excess $`\lVert U-U_0\rVert_F^2/(16r)`$. The integral identity for the difference of two unitary evolutions and unitary invariance of the Schatten norms yield $`\lVert U-U_0\rVert_F\le\pi x`$ and $`\lVert U-U_0\rVert_1\le\pi x`$. Also $`\lVert U-U_0\rVert_\infty\le2`$, so $`\lVert U-U_0\rVert_F^2\le2\pi x`$ and $`\lVert U-U_0\rVert_F^2\le8r`$. The ideal excess is therefore at most a constant times $`\min\{x^2,x,r\}/r`$.

Replace the controlled evolution by $`N`$ controlled partial swaps of time $`T/N`$, one per fresh stored specimen. Each swap is a known gate and is controlled on the same Hadamard-test qubit. The [reference-stable implementation](finite_copy.md#controlled-density-matrix-simulation-from-copies) gives an unhalved diamond error of at most $`4T^2/N`$, which contributes at most $`2T^2/N`$ to risk. For $`x\le r`$, we have $`a\ge1/2`$ and this contribution is $`O(r^2/N)`$. If $`x\gt r`$, a fair coin gives excess $`1/4`$. A fair coin also caps the bound when the specimen budget is small.

The construction consumes the stored specimens and produces one bit from the later test. Storage for the copies is $`N\lceil\log_2 d\rceil`$ qubits in a binary encoding, and the active test, control, and currently used specimen occupy $`2\lceil\log_2 d\rceil+1`$ qubits before any synthesis workspace. State preparation is charged per supplied copy. With a fixed universal gate set, approximating each controlled rotation to diamond error $`O(r^2/N^2)`$ in the regime $`r^2/N\lt1`$ keeps total synthesis error of order $`r^2/N`$. The general [resource conventions](resources.md) apply.

## Measurement first and a spectral threshold

Apply [O’Donnell and Wright, Theorem 1.2](https://arxiv.org/html/1508.01907v2) during training to obtain a Hermitian estimate $`\widehat\rho`$ with

```math
\mathbb E\lVert\widehat\rho-\rho\rVert_F^2\le (4d-3)/N.
```

Keep only the classical record and predict the clean class using the rank-$`r`$ effect $`\widehat Q`$ onto the leading eigenspace of $`\widehat\rho`$. Resolve ties by a fixed measurable rule. Write $`L=\operatorname{tr}[P(I-\widehat Q)]`$ and $`e=\lVert\widehat\rho-\rho\rVert_F`$. The excess is $`L/(2r)`$. Because $`\alpha\widehat Q`$ is a closest scaled rank-$`r`$ projector to $`\widehat\rho`$ in Frobenius norm, we have

```math
2\alpha^2 L=\lVert\alpha(P-\widehat Q)\rVert_F^2
\le 4(e+\eta)^2,
\qquad
L\le 4(x^2+e^2/\alpha^2).
```

For the linear-contamination regime, the same spectral optimality gives $`\operatorname{tr}[\widehat\rho(\widehat Q-P)]\ge0`$. Since $`\lVert\widehat Q-P\rVert_\infty\le1`$, this yields

```math
\alpha L\le\eta+e\sqrt{2L},
\qquad
L\le 2x+2e^2/\alpha^2.
```

Use also $`L\le r`$. Taking expectations at $`x\le r`$ and $`d=2r`$ gives the same upper bound as the coherent construction. For stronger contamination or a small budget, the fair-coin cap again applies.

## Exact limit below the population of one support direction

For $`x\lt1`$ let $`Q_\star`$ be the top-$`r`$ projector of the exact matrix $`\rho`$. The $`r`$th eigenvalue of $`\rho`$ is at least $`\alpha`$ and the next eigenvalue is at most $`\eta`$. Along the path $`\rho_t=\alpha P+t\eta\sigma`$ for $`t\in[0,1]`$, the corresponding projector is continuous by the same positive gap. In a principal plane at time $`t`$, pick orthonormal vectors $`u`$, $`v`$ in that projector's range and kernel, respectively. Orthogonality of the spectral blocks implies

```math
\alpha\sin(2\theta)
=2t\eta\,|\langle u|\sigma|v\rangle|
\le t\eta(\langle u|\sigma|u\rangle+\langle v|\sigma|v\rangle).
```

The equality uses the single rank-one block of $`P`$ in that plane. The inequality uses positivity of the restriction of $`\sigma`$ to the plane. Since $`\sin(2\theta)\le tx\lt1`$, no principal angle continuous from zero can reach $`\pi/4`$. Summing over disjoint principal planes at $`t=1`$ gives $`\sum_i\sin(2\theta_i)\le x`$ because $`\operatorname{tr}\sigma=1`$.

For $`f(z)=(1-\sqrt{1-z^2})/2`$, convexity and $`f(0)=0`$ give $`\sum_i f(z_i)\le f(\sum_i z_i)`$ when $`z_i\ge0`$ and the sum is at most one. Therefore the effect $`Q_\star`$ has excess

```math
\frac1{2r}\sum_i\sin^2\theta_i
=\frac1{2r}\sum_i f(\sin 2\theta_i)
\le \frac{1-\sqrt{1-x^2}}{4r}.
```

For equality, use the common-specimen construction with two supports sharing $`r-1`$ directions, and choose the remaining rays symmetrically at angles $`\pm\frac12\arcsin x`$ from one axis. Their mutual principal angle is $`\arcsin x`$, and their Bayes excess equals the upper bound. Both learner classes attain this limit from copies. For fixed $`r,a`$, the uniform Frobenius consistency of tomography and the uniform gap $`\alpha-\eta\gt0`$ imply uniform convergence of the estimated top projector to $`Q_\star`$. Indeed the eigenprojector map is continuous on matrices with that gap, the set of admissible density matrices is compact, and the excess of every effect is bounded.

The rank-one formula in [the original precision account](precision_floor.md) treats every dimension and all contamination levels. The branch here determines the exact balanced-rank limit for $`x\lt1`$ and the finite-copy law up to constants for all $`a`$ at $`d=2r`$.

## Small contamination outside balanced rank

For general $`1\le r\lt d`$, the clean-support oracle has risk $`r/(2d)`$. The missed support mass $`\operatorname{tr}[P(I-E)]`$ and accepted kernel mass $`\operatorname{tr}[(I-P)E]`$ enter the excess with coefficients $`(1/r-1/d)/2`$ and $`1/(2d)`$, respectively. Each coefficient is at most $`1/(2r)`$. Applying these weights to the Hadamard-test norm identities above and charging the same controlled-simulation error gives the coherent upper bound below. A rank-$`r`$ tomography effect still has excess $`L/(2r)`$, so the preceding two estimates on $`L`$ give the compiler bound. For $`a\ge1/2`$ and $`N\ge1`$, the sufficient excess orders are

```math
O\!\left(\frac{r^2}{N}+\frac{\min\{x^2,x\}}r\right)
\quad\text{and}\quad
O\!\left(\frac{rd}{N}+\frac{\min\{x^2,x\}}r\right),
```

respectively, with the fair-coin cap in either class.

For $`1\le r\le d/2`$ and $`0\le x\le\sqrt{r/d}`$, both orders are matched. Use a compatible pair sharing $`r-1`$ directions and separated by the principal angle $`\arcsin x`$. In its differing plane the equal-pair average clean test has eigenvalues $`(1-f(x))/r`$ and $`f(x)/r`$, where $`f(x)=(1-\sqrt{1-x^2})/2`$. Against background $`I/d`$, the pair incurs excess $`\min\{f(x),r/d\}/(2r)`$. In the stated range $`f(x)\le r/d`$ and this is of order $`x^2/r`$. The clean subfamily separately gives the statistical lower bounds from [Q2 and C3](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/main/science/contaminated_training.md). Thus the coherent and compiler minimax excesses have the respective orders above with $`\min\{x^2,x\}`$ replaced by $`x^2`$ and each total capped at constant order.

## A four-dimensional instance

Take $`d=4`$, $`r=2`$, $`a=2/3`$, and $`\rho=\operatorname{diag}(3/8,3/8,1/8,1/8)`$. This instance has $`x=1`$. For an isometry $`V`$ with $`P=VV^\dagger`$, the condition $`P/3\preceq\rho`$ is equivalent to $`V^\dagger\rho^{-1}V\preceq3I`$. In the two spectral blocks this bounds each squared principal sine relative to the top two directions by $`1/16`$. Their rank-two effect consequently has risk at most $`9/32`$ for this specific $`\rho`$.

For equality, pair each top direction with a lower direction and take a ray with squared lower component $`1/16`$ in each plane. Vary the two lower-component signs independently. All four supports satisfy the same compatibility condition. Their average clean state has top-block eigenvalues $`15/32`$ and bottom-block eigenvalues $`1/32`$, each repeated twice. Its optimal test against $`I/4`$ has risk $`9/32`$. This is the conditional minimax value at the displayed density, where the clean-support oracle has risk $`1/4`$.

## One source ambiguity, two different tasks

[Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/science/contaminated_reflections.md) uses the same positive-order criterion for deterministic ordinary reflection channels on a batch. Rotating a single support direction changes the channel at first order in the angle, and suitable batch inputs amplify that change. The resulting unhalved diamond ambiguity is of order $`\min\{1,kx\}`$ for $`k`$ jointly available targets. Balanced recognition instead pays quadratically at small $`x`$ because its error involves squared amplitudes. The clean statistical converse and the limits of the phase-anchored transfer are explained in [Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits/blob/main/science/contaminated_training.md).
