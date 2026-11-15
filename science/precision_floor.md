# The exact prediction floor under contaminated training

An arbitrarily long training record determines the density matrix emitted by the source. It need not determine which clean pure state was mixed with the contaminant. This chapter computes the smallest worst-case error for one future recognition decision after that remaining ambiguity is made explicit.

The experiment and all input charges are specified in [the model](model.md). The clean state is $`P=|\psi\rangle\langle\psi|`$ on $`\mathbb C^d`$, the known clean fraction is $`a\in(0,1]`$, and every training sample has density matrix

```math
\rho=aP+(1-a)\sigma.
```

The contaminant $`\sigma`$ is an arbitrary hidden density matrix and may depend on $`P`$. A single later test is equally likely to be $`P`$ or $`I_d/d`$. An effect $`0\le E\le I_d`$ means “accept the clean class” and has error

```math
R(E,P)=\frac{1-\mathrm{tr}(EP)
                    +\mathrm{tr}(E)/d}{2}.
```

If $`P`$ is known, $`E=P`$ is optimal and its error is $`R_*(d)=1/(2d)`$. Contamination is confined to training; the positive test is the clean state.

## What infinite training reveals

For a known training density matrix define its compatible clean states by

```math
\mathcal P_a(\rho)
=\{P:\ P\text{ is rank one},\ \mathrm{tr}P=1,
                   \ aP\le\rho\}.
```

For $`a \lt 1`$, the inequality is equivalent to the existence of a density matrix $`\sigma=(\rho-aP)/(1-a)`$. At $`a=1`$, compatibility instead forces $`\rho=P`$. Thus the exact-training benchmark is

```math
R_\infty(d,a)
=\sup_{\rho:\mathcal P_a(\rho)\ne\varnothing}
  \inf_{0\le E\le I_d}\sup_{P\in\mathcal P_a(\rho)}R(E,P).
```

This benchmark gives the learner an exact classical description of $`\rho`$. It is an identifiability limit, shared by every learner once sufficiently many training copies are available. It is not itself a finite-sample quantum speedup.

## Exact law, including the endpoints

Put $`c=1/d`$. For $`q\in[0,1-c]`$ let $`k=\lfloor dq\rfloor`$ and define

```math
S_d(q)=\sqrt{1-q}+\frac{k}{\sqrt d}
                         +\sqrt{q-\frac{k}{d}}.
```

The formula is continuous at every grid point $`q=j/d`$. A zero last term is simply omitted. In particular,

```math
S_d(0)=1,
\qquad
S_d(1-1/d)=\sqrt d.
```

It is strictly increasing on the full interval. If $`1/d \lt a\le1`$, let $`q_d(a)`$ be the unique solution of

```math
S_d\bigl(q_d(a)\bigr)=a^{-1/2}.
```

Then the exact error and the excess above the known-state benchmark are

```math
R_\infty(d,a)=\frac{1/d+q_d(a)}{2},
\qquad
R_\infty(d,a)-R_*(d)=\frac{q_d(a)}{2}.
```

For $`0 \lt a\le1/d`$ the error is $`R_\infty(d,a)=1/2`$. One may extend the notation continuously by setting $`q_d(a)=1-1/d`$ there. At $`a=1`$ one has $`q_d(1)=0`$, recovering the known-state error. At every $`a \lt 1`$ with $`a \gt 1/d`$, the contamination excess is strictly positive.

The scalar extremal distribution behind $`S_d`$ is inherited from Rioul’s sharp Rényi-entropy/total-variation inequalities: [Rioul, *Entropy* **25**, 978 (2023), Section 4, Theorem 6 and Example 19, Eq. (96)](https://doi.org/10.3390/e25070978). The proof below reconstructs that scalar fact to make its use transparent. The operational reduction from compatible contaminated quantum sources to that entropy frontier is the result being established here.

## From quantum compatibility to a scalar decision problem

Diagonalize $`\rho`$ as $`\rho=\sum_i\lambda_i|i\rangle\langle i|`$. A compatible vector lies in the support of $`\rho`$. With $`p_i=|\langle i|\psi\rangle|^2`$, rank-one domination is equivalent to

```math
aP\le\rho
\quad\Longleftrightarrow\quad
\sum_{i:\lambda_i \gt 0}\frac{p_i}{\lambda_i}\le\frac1a,
\qquad p_i=0\text{ if }\lambda_i=0.
```

Indeed, conjugating the inequality by the inverse square root on the support gives $`a|v\rangle\langle v|\le I`$ with $`|v\rangle=\rho^{-1/2}|\psi\rangle`$. A rank-one positive operator has its squared vector norm as its only nonzero eigenvalue, giving the displayed condition.

Every independent eigenbasis phase rotation commutes with $`\rho`$ and preserves the compatibility set. Averaging an effect over these rotations keeps its trace and cannot reduce its minimum acceptance over compatible clean states. Consequently an optimal robust effect may be taken diagonal, $`E=\sum_i e_i|i\rangle\langle i|`$, with $`0\le e_i\le1`$.

The feasible probability vectors form the compact convex set

```math
K_\lambda
=\left\{p\in\Delta_d:\ p_i=0\text{ if }\lambda_i=0,
                \ \sum_{\lambda_i \gt 0}\frac{p_i}{\lambda_i}\le\frac1a\right\}.
```

Every such vector is realized by a compatible pure state, with arbitrary phases. The robust contrast at this spectrum is therefore

```math
\begin{aligned}
g_a(\lambda)
&=\max_{e\in[0,1]^d}\min_{p\in K_\lambda}
       \sum_i e_i(p_i-c)\\
&=\min_{p\in K_\lambda}\max_{e\in[0,1]^d}
       \sum_i e_i(p_i-c)\\
&=\min_{p\in K_\lambda}\mathrm{TV}(p,u_d).
\end{aligned}
```

The interchange uses the compact convex bilinear minimax theorem. The final equality follows by setting $`e_i=1`$ on positive coordinates of $`p_i-c`$ and zero on negative ones. Here $`u_d=(c,\ldots,c)`$ and $`\mathrm{TV}(p,u_d)=\frac12\sum_i|p_i-c|`$. The optimal robust error at $`\rho`$ is $`(1-g_a(\lambda))/2`$.

The outer adversary also chooses $`\lambda`$. For a fixed probability vector, Cauchy–Schwarz gives

```math
\left(\sum_i\sqrt{p_i}\right)^2
\le \left(\sum_{\lambda_i \gt 0}\frac{p_i}{\lambda_i}\right)
     \left(\sum_i\lambda_i\right).
```

The minimum is attained at $`\lambda_i=\sqrt{p_i}/\sum_j\sqrt{p_j}`$, with zero entries where $`p_i=0`$. Thus a spectrum compatible with $`p`$ exists exactly when

```math
\left(\sum_i\sqrt{p_i}\right)^2\le\frac1a.
```

Both the spectrum and the compatible vector are minimized in the outer contrast, so this step eliminates a joint minimization; it does not exchange an adversarial maximum with a learner’s minimum. It yields the operational identity

```math
1-2R_\infty(d,a)
=\min_{\substack{p\in\Delta_d\\
       (\sum_i\sqrt{p_i})^2\le1/a}}
     \mathrm{TV}(p,u_d).
```

Equivalently, the admissible vectors obey the Rényi-entropy constraint $`H_{1/2}(p)\le-\log a`$, since $`H_{1/2}(p)=2\log\sum_i\sqrt{p_i}`$. The logarithm base does not affect the constraint.

## Evaluating the inherited entropy frontier

For any $`p\in\Delta_d`$ put

```math
F(p)=\sum_i\min\{p_i,c\}
     =1-\mathrm{TV}(p,u_d),
\qquad q=F(p)-c.
```

Then $`0\le q\le1-c`$. At a given $`q`$, the probability vector

```math
p^{\star}(q)
=\left(1-q,\ \underbrace{c,\ldots,c}_{k\text{ entries}},
                   \ q-kc,\ 0,\ldots,0\right),
\qquad k=\lfloor dq\rfloor,
```

has the smallest possible square-root sum. Zero entries, including a zero fractional entry, are omitted or padded to give exactly $`d`$ coordinates. The endpoint $`q=1-c`$ is the uniform vector.

To verify the extremal property, sort $`p`$ decreasingly. For every $`j`$,

```math
F(p)\le jc+\sum_{i \gt j}p_i,
\qquad
\sum_{i\le j}p_i\le\min\{1,1-q+(j-1)c\}.
```

The right side equals the corresponding partial sum of $`p^{\star}(q)`$ until that vector’s total mass has been reached; afterwards the bound is one. Hence $`p^{\star}(q)`$ majorizes $`p`$. Concavity of the square root implies

```math
\sum_i\sqrt{p_i}\ge\sum_i\sqrt{p_i^{\star}(q)}=S_d(q).
```

Conversely $`p^{\star}(q)`$ attains the stated $`F=c+q`$ and equality. This is the relevant specialization of Rioul’s theorem. On each interval $`k/d \lt q \lt (k+1)/d`$ the derivative of $`S_d`$ is

```math
S_d'(q)=\frac1{2\sqrt{q-k/d}}-\frac1{2\sqrt{1-q}} \gt 0,
```

because the fractional coordinate is smaller than the leading coordinate in the interior. Together with the matching one-sided boundary values, this proves continuity and strict increase. Maximizing the feasible $`F`$ now gives the root formula. If $`a\le1/d`$, the uniform vector is feasible and the minimum contrast is zero, completing the endpoint proof.

## A finite least-favorable family of indistinguishable sources

The lower bound does not require an adversary with a continuously distributed hidden state. Suppose $`1/d \lt a \lt 1`$, set $`q=q_d(a)`$, and retain the $`s`$ nonzero entries of $`p=p^{\star}(q)`$. Number their basis vectors from zero to $`s-1`$. Define

```math
\lambda_j=\frac{\sqrt{p_j}}{\sum_i\sqrt{p_i}},
\qquad
\rho=\sum_{j=0}^{s-1}\lambda_j|j\rangle\langle j|,
\qquad
|\psi_\ell\rangle
=\sum_{j=0}^{s-1}\sqrt{p_j}\,
       e^{2\pi i\ell j/s}|j\rangle,
\quad 0\le\ell \lt s.
```

The compatibility expression equals $`1/a`$ for every $`\ell`$. Therefore

```math
\sigma_\ell=\frac{\rho-a|\psi_\ell\rangle\langle\psi_\ell|}{1-a}
```

is positive and has trace one. Every target–contaminant pair emits exactly the same training state $`\rho`$, so even an arbitrarily large collective training measurement cannot reveal $`\ell`$. The uniform average of the clean states is $`\mathrm{diag}(p)`$, because the finite Fourier phases cancel every off-diagonal term.

For this uniform prior the best possible test has error

```math
\frac{1-\mathrm{TV}(p,u_d)}2
=\frac{1/d+q_d(a)}2.
```

Worst-case error is at least average error. The preceding minimax calculation supplies an effect attaining the same global bound for every training density matrix. Thus the finite family witnesses the exact floor, not merely an unattainability of state reconstruction. For $`a\le1/d`$, take $`\rho=I_d/d`$ and a uniform orthonormal target ensemble; for $`a=1`$ the uncontaminated benchmark already gives the endpoint.

## The literal finite-training limit

Let $`R_N^{\mathrm Q}(d,a)`$ and $`R_N^{\mathrm C}(d,a)`$ be the coherent and classical-compiler minimax risks defined in [the model](model.md#learners-and-risks). For every fixed $`d`$ and $`a`$,

```math
R_N^{\mathrm C}(d,a)\ge R_N^{\mathrm Q}(d,a)\ge R_\infty(d,a),
\qquad
\lim_{N\to\infty}R_N^{\mathrm Q}(d,a)
=\lim_{N\to\infty}R_N^{\mathrm C}(d,a)=R_\infty(d,a).
```

The lower inequalities hold because every classical compiler is a coherent learner and knowing $`\rho`$ exactly is at least as informative as receiving finitely many copies. For the upper direction, informationally complete tomography at fixed dimension supplies a normalized positive estimator $`\widehat\rho`$ with

```math
\|\widehat\rho-\rho\|_\infty\le\delta
```

except with probability $`\zeta`$, uniformly over all density matrices, once sufficiently many copies are used. This follows, for example, by estimating a finite Hermitian operator basis with independent bounded measurements and projecting the reconstructed matrix onto the density matrices. At fixed $`d`$ the reconstruction is a continuous finite-dimensional linear operation; increasing repetitions makes both the norm error and the failure probability arbitrarily small.

On the good event set

```math
\tau=\frac{\widehat\rho+\delta I_d}{1+d\delta},
\qquad
a'=\frac{a}{1+d\delta}.
```

The operator inequality $`\widehat\rho+\delta I_d\ge\rho\ge aP`$ gives $`\tau\ge a'P`$. Apply an optimal exact-training robust effect for $`\tau`$ at clean fraction $`a'`$. Its risk is at most $`R_\infty(d,a')`$ on the good event and at most one otherwise, hence

```math
R_N^{\mathrm Q}(d,a)\le R_N^{\mathrm C}(d,a)
\le R_\infty(d,a')+\zeta
```

for sufficiently large $`N`$. This strategy measures the training systems before the test arrives and retains only a classical description of the estimator, so it is already a classical compiler. The root law is continuous in $`a`$, including $`a=1/d`$ and $`a=1`$. Letting $`\delta,\zeta\to0`$ proves both limits. Arbitrarily accurate finite-precision choices of the robust effect suffice; no exact-real computation is being assumed as an implementation primitive.

This argument establishes the order of limits: first $`N\to\infty`$ with $`d,a`$ fixed. It uses tomography and does not establish an efficient or optimal finite-$`N`$ rate. The [finite-copy construction](finite_copy.md) and its separate [resource account](resources.md) give constructive bounds outside this limit argument.

## Small contamination, uniformly in dimension

Write $`\eta=1-a`$. There are universal positive constants such that for all $`d\ge2`$ and $`0 \lt \eta\le1/4`$,

```math
R_\infty(d,1-\eta)-\frac1{2d}
=\Theta\!\left(\min\left\{\eta^2,\frac{\eta}{\sqrt d}\right\}\right).
```

Here the constants are independent of both parameters. A direct proof avoids treating two ordered limits as a uniform statement. Put $`\beta=a^{-1/2}-1`$, so $`\eta/2\le\beta\le\eta`$ in this regime, and let $`q=q_d(a)`$. Since

```math
\sum_i\sqrt{p_i}\ge\frac1{\sqrt{p_{\max}}},
```

the entropy constraint forces $`p_{\max}\ge a`$. Applied to $`p^{\star}(q)`$, this gives $`q\le\eta\le1/4`$.

Let $`W`$ be the square-root sum of its tail coordinates, whose total mass is $`q`$ and each of which is at most $`1/d`$. Then

```math
\max\{\sqrt q,q\sqrt d\}\le W
\le\sqrt q+q\sqrt d
\le2\max\{\sqrt q,q\sqrt d\}.
```

The upper bound follows by separating the filled coordinates from the fractional coordinate. Moreover,

```math
\beta=W-\bigl(1-\sqrt{1-q}\bigr),
\qquad
0\le1-\sqrt{1-q}\le q\le\frac W2.
```

Consequently $`\frac12\max\{\sqrt q,q\sqrt d\}\le\beta\le2\max\{\sqrt q,q\sqrt d\}`$. Inverting this pair of inequalities gives

```math
\frac14\min\left\{\beta^2,\frac\beta{\sqrt d}\right\}
\le q
\le4\min\left\{\beta^2,\frac\beta{\sqrt d}\right\}.
```

For example, this proves the fully uniform bounds

```math
\frac1{32}\min\left\{\eta^2,\frac\eta{\sqrt d}\right\}
\le R_\infty(d,1-\eta)-\frac1{2d}
\le2\min\left\{\eta^2,\frac\eta{\sqrt d}\right\}.
```

The constants are not claimed optimal. In the first root interval $`q\le1/d`$ the exact expression simplifies to

```math
q_d(1-\eta)
=\frac{1-\sqrt{1-[\eta/(1-\eta)]^2}}2.
```

This expression is used only when its value lies in that first interval; it is not an all-dimension formula for arbitrary contamination.

## Fixed clean fraction and growing dimension

For every fixed $`a\in(0,1)`$,

```math
q_d(a)=\frac{a^{-1/2}-1}{\sqrt d}+O_a(d^{-1}),
\qquad
R_\infty(d,a)=\frac{a^{-1/2}-1}{2\sqrt d}+O_a(d^{-1}).
```

To control the grid remainder, write $`r=\{dq\}`$. The exact identity is

```math
S_d(q)=\sqrt{1-q}+q\sqrt d+\frac{\sqrt r-r}{\sqrt d},
\qquad 0\le\sqrt r-r\le\frac14.
```

At the root $`\beta=S_d(q)-1\ge q(\sqrt d-1)`$, so $`q=O_a(d^{-1/2})`$. Substitution into the same identity gives the displayed expansion with an $`O_a(d^{-1})`$ residual. The estimate is not uniform when $`a`$ approaches zero or $`1/d`$ with $`d`$. It is taken after the fixed-dimension infinite-training limit, and does not assert a matching joint law in $`N,d,a`$.

## Recognition does not require reconstructing the clean state

The prediction floor can vanish with dimension even while clean-state reconstruction remains ambiguous by a constant amount. Let $`\eta=1-a \gt 0`$ and choose two pure states $`P,Q`$ with trace distance

```math
D(P,Q)=\frac12\|P-Q\|_1
=t:=\min\left\{1,\frac\eta a\right\}.
```

There is one density matrix compatible with both. Indeed,

```math
B=\frac{P+Q+|P-Q|}{2}
```

satisfies $`B\ge P,Q`$ and $`\mathrm{tr}B=1+t`$. Since $`a(1+t)\le1`$, add any positive operator of trace $`1-a(1+t)`$ to $`aB`$ to obtain a normalized $`\rho\ge aP,aQ`$. The associated contaminants are valid and produce the same training state for both targets.

Every density-matrix estimator built from this training source has the same output distribution in the two cases. The trace-distance triangle inequality therefore gives

```math
\max\left\{\mathbb E D(\widehat\tau,P),
             \mathbb E D(\widehat\tau,Q)\right\}\ge\frac t2.
```

For infidelity loss, the largest eigenvalue of $`(P+Q)/2`$ is $`(1+\sqrt{1-t^2})/2`$, giving the additional lower bound

```math
\max\left\{\mathbb E[1-\mathrm{tr}(P\widehat\tau)],
             \mathbb E[1-\mathrm{tr}(Q\widehat\tau)]\right\}
\ge\frac{1-\sqrt{1-t^2}}2.
```

These reconstruction bounds hold even with exact $`\rho`$ and for every finite training budget. In contrast, at fixed $`a \gt 0`$ the one-test recognition error tends to zero as $`d\to\infty`$. The distinction is task specific: accepting some extra directions is inexpensive against the known maximally mixed background. It supplies neither recovery of $`P`$ nor a reusable predictor, and need not persist for a different background. [The commuting comparison](commuting_comparison.md) isolates the role of noncommuting contamination within the same supplied-state experiment.
