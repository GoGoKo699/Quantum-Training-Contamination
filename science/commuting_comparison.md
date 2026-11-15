# What changes when contamination commutes with the clean state

The exact prediction floor changes if the contaminant is required to preserve the clean state’s eigendirection. This comparison keeps the same quantum input and output interfaces as [the model](model.md): iid contaminated training states, one later test equal to the clean pure state or $`I_d/d`$, and one output label. It changes only the promise

```math
[\sigma,P]=0.
```

No common eigenbasis is given to the learner. The clean state may be an arbitrary unknown vector in $`\mathbb C^d`$. The following result therefore compares two classes of quantum sources under the same exact-training information, rather than granting one learner a known classical label.

## Exact commuting-contamination benchmark

Let $`R_\infty^{\mathrm{comm}}(d,a)`$ be the exact-training minimax error with this additional promise. Then for every $`d\ge2`$ and $`a\in(0,1]`$,

```math
R_\infty^{\mathrm{comm}}(d,a)
=\frac{\min\{d,\lfloor1/a\rfloor\}}{2d}.
```

At $`a=1`$ this is the known-state error $`1/(2d)`$. At $`a\le1/d`$ it is $`1/2`$. For $`a>1/2`$, exact training identifies the clean pure state uniquely and the contamination causes no prediction excess.

To prove the law, fix a known training density matrix $`\rho`$. Since $`\rho=aP+(1-a)\sigma`$, the commuting promise implies $`[\rho,P]=0`$. A rank-one projector commutes with $`\rho`$ exactly when its vector belongs to one eigenspace of $`\rho`$. Such a vector is compatible precisely when its eigenvalue is at least $`a`$. Conversely every such vector yields a positive normalized contaminant commuting with $`P`$ when $`a<1`$. The uncontaminated endpoint is immediate.

Define the high-eigenvalue subspace and its dimension by

```math
\mathcal H_{\ge a}(\rho)
=\bigoplus_{\lambda\ge a}\ker(\rho-\lambda I_d),
\qquad
L(\rho)=\dim\mathcal H_{\ge a}(\rho).
```

Only training states with $`L\ge1`$ are relevant. Within a degenerate high-eigenvalue eigenspace, every pure vector is allowed. Superpositions across distinct eigenvalues need not be allowed; the proof does not replace the compatible set by that larger set.

Accepting the entire high-eigenvalue subspace, $`E=\Pi_{\ge a}`$, never rejects a compatible clean test and accepts the maximally mixed background with probability $`L/d`$. It therefore has error $`L/(2d)`$.

For the converse, choose an orthonormal eigenbasis of that subspace and average uniformly over its $`L`$ compatible clean basis states. For any effect set $`x=\operatorname{tr}(E\Pi_{\ge a})`$. Its averaged error obeys

```math
\begin{aligned}
\frac1L\sum_{j=1}^{L}R(E,|j\rangle\langle j|)
&=\frac{1-x/L+\operatorname{tr}(E)/d}{2}\\
&\ge\frac{1-x/L+x/d}{2}\\
&\ge\frac{L}{2d},
\qquad 0\le x\le L.
\end{aligned}
```

The last inequality uses $`L\le d`$; if $`L=d`$ its coefficient is zero. Worst-case error is at least this average. Thus the exact robust error for the fixed $`\rho`$ is $`L/(2d)`$.

Finally, trace one gives $`aL\le1`$, so $`L\le m:=\min\{d,\lfloor1/a\rfloor\}`$. This count is attainable. If $`m=d`$, take $`\rho=I_d/d`$. If $`m<d`$, take $`m`$ eigenvalues initially equal to $`a`$, assign the leftover mass $`1-ma`$ to one of them, and set all other eigenvalues to zero. Exactly $`m`$ eigenvalues are then at least $`a`$. This proves the worst-case law, including fractions $`a=1/m`$ where the floor function changes.

## A precision distinction within the same quantum experiment

For a fixed clean fraction $`a\in(0,1)`$, the commuting error is $`\Theta_a(d^{-1})`$. With arbitrary contamination, [the exact law](precision_floor.md) instead gives

```math
R_\infty(d,a)
=\frac{a^{-1/2}-1}{2\sqrt d}+O_a(d^{-1}).
```

Thus the worst-case error has orders $`d^{-1}`$ and $`d^{-1/2}`$ in the respective source classes. When $`a>1/2`$, the contrast is sharper at finite dimension: commuting contamination causes no excess at all, while arbitrary contamination causes positive excess for every $`a<1`$.

The mechanism is not that a high-eigenvalue eigenspace has an unknown basis. Exact knowledge of $`\rho`$ already specifies that subspace, and accepting it is enough. Arbitrary contamination permits different nonorthogonal clean vectors, with different phases in the eigenbasis, to generate the same training density matrix. Those vectors need not be eigenvectors of $`\rho`$. The finite least-favorable family in [the precision proof](precision_floor.md) makes this ambiguity explicit. Its cost concerns recognizing one clean test against a maximally mixed background, not estimating an arbitrary test distribution or preserving a fixed classifier’s decision under test-time perturbations.

## The fully classical specialization

If the entire source is further restricted to a fixed known diagonal algebra and the clean target is a basis point $`|x\rangle\langle x|`$, exact training reveals a probability vector $`\lambda`$. Its compatible clean labels are precisely the indices with $`\lambda_x\ge a`$. There are $`L`$ such labels, and accepting them all gives error $`L/(2d)`$. The same averaging converse and counting argument recover exactly the formula above.

The known-basis point-target experiment is therefore a classical specialization of the commuting quantum theorem. Neither comparison is a statement about all classical robust-learning problems: the positive test is a clean point or pure state, the background is known and uniform, contamination affects training only, and the benchmark supplies the exact training distribution or density matrix. Finite-copy complexity and its quantum/classical compilation distinction are separate questions.
