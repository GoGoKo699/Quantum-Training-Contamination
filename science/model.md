# Learning a clean decision from contaminated quantum specimens

This chapter specifies the pure-source model. [Flat-rank recognition](flat_rank_training.md) replaces the pure class by the uniform state on an unknown rank-$`r`$ support and studies finite-copy precision at $`d=2r`$.

A source repeatedly prepares a quantum state, but its training specimens contain an uncontrolled admixture. The learner is asked to recognize one later clean specimen. Reconstructing the clean state would be sufficient for that task, yet reconstruction can be impossible even with unlimited training: several nonorthogonal pure states can have the same contaminated density matrix. This account asks what that ambiguity actually costs for prediction.

The background class is the known maximally mixed state. It is deliberately diffuse. A classifier can accept a small uncertainty subspace without paying a large background false-positive probability. This property makes the distinction between state identification and prediction quantitatively accessible. The exact answer is specific to this source and background; it is not a universal statement about poisoned datasets.

## The experiment

Fix a dimension $`d\ge2`$ and a known clean fraction $`a\in(0,1]`$. Write $`\eta=1-a`$. The hidden clean state and training state are

```math
P=|\psi\rangle\langle\psi|,
\qquad
\rho=aP+(1-a)\sigma,
```

where $`\sigma`$ is any density operator on the same space. It can depend on $`P`$ but is fixed within an instance. The learner receives $`N`$ independent copies of $`\rho`$. No flags identify the clean component. There is no classical description of $`P`$ or $`\sigma`$, purification, preparation inverse, controlled source oracle, QRAM or free data-loading operation.

All training specimens arrive before one test register. The test label $`H`$ has equal prior probabilities, and its conditional state is

```math
H=1:\ P,
\qquad
H=0:\ \tau_d:=I_d/d.
```

Training and test are independent conditional on the hidden source and label. The test is clean under $`H=1`$; contamination affects training alone. The learner outputs one classical label and may consume every supplied specimen. Further source calls after test arrival and a reusable learned model are not supplied resources.

The known value $`a`$ can also be interpreted as a lower bound on the true clean fraction. Indeed, the admissible training states are exactly those satisfying $`\rho\succeq aP`$: any excess clean fraction can be included in $`\sigma`$.

## Learners and risks

A coherent learner may retain the training systems and use arbitrary known quantum processing, ancillas and intermediate measurements. Its complete experiment is a binary effect $`0\preceq T\preceq I`$ on the training systems and test. Its expected error is

```math
R_N(T;P,\sigma)
=\frac12\mathrm{Tr}[(I-T)(\rho^{\otimes N}\otimes P)]
+\frac12\mathrm{Tr}[T(\rho^{\otimes N}\otimes\tau_d)].
```

The minimax risk is

```math
R_N^{\mathrm Q}(d,a)
=\inf_T\sup_{P\ \mathrm{pure},\ \sigma\ \mathrm{state}}
R_N(T;P,\sigma).
```

All internal randomness and measurement outcomes are included in this expectation. The guarantee is not a separate confidence statement about every realized training record.

A classical compiler may make an arbitrary collective POVM on all training systems, keep an unlimited classical record $`y`$, and choose any later test effect $`E_y`$ from that record. Every quantum system correlated with the source must be discarded before the test arrives. The resulting positive-decision effect has the form

```math
T_{\mathrm C}=\int F(dy)\otimes E_y,
\qquad
0\preceq E_y\preceq I.
```

This permits quantum processing during training and at test time, unbounded classical computation and continuous records. The restriction concerns retained source-dependent quantum information. It is stronger than comparing with separately measured training examples, and it is not a restriction to a particular tomography algorithm. Its minimax risk is denoted $`R_N^{\mathrm C}(d,a)`$.

If $`P`$ is known, the effect $`P`$ attains the oracle risk

```math
R_\star(d)=\frac1{2d}.
```

We use **risk** for the total error and **excess risk** for error minus $`R_\star`$. These quantities must remain distinct in finite-copy and dimension-dependent statements.

## Perfect-density information and its asymptotic meaning

Suppose the learner is given the exact training density matrix $`\rho`$. The clean target remains any pure state in

```math
\mathcal P_a(\rho)=\{P\text{ pure}:aP\preceq\rho\}.
```

The resulting robust risk is

```math
R_\infty(d,a)
=\sup_{\rho:\mathcal P_a(\rho)\ne\varnothing}
\inf_{0\preceq E\preceq I}
\sup_{P\in\mathcal P_a(\rho)}
\frac{1-\mathrm{Tr}(EP)+\mathrm{Tr}(E)/d}{2}.
```

This is a lower bound on every finite-copy learner, including coherent learners. Exact density information can simulate any training experiment without disclosing which compatible clean state generated it. Conversely, uniform tomography with a relaxed compatibility constraint proves

```math
\lim_{N\to\infty}R_N^{\mathrm Q}(d,a)
=\lim_{N\to\infty}R_N^{\mathrm C}(d,a)
=R_\infty(d,a)
```

for each fixed $`d,a`$. The proof is in [the exact precision account](precision_floor.md#the-literal-finite-training-limit). This is an ordered limit, not a dimension-uniform finite-sample rate.

## Results and authoritative routes

| Result | Supported statement | Canonical account |
|---|---|---|
| Exact contamination limit | The robust prediction problem reduces to the nearest-to-uniform probability vector with $`(\sum_i\sqrt{p_i})^2\le1/a`$. A scalar root gives the exact finite-$`d`$ risk and an explicit least-favorable phase family. | [Precision floor](precision_floor.md) |
| Small contamination and large dimension | For $`0 \lt \eta\le1/4`$, the unavoidable excess is $`\Theta(\min\{\eta^2,\eta/\sqrt d\})`$. At each fixed $`a\in(0,1)`$, its leading term is $`(a^{-1/2}-1)/(2\sqrt d)`$. | [Scaling and limits](precision_floor.md) |
| Commuting contamination | If $`[\sigma,P]=0`$, the exact perfect-density risk is $`\min\{d,\lfloor1/a\rfloor\}/(2d)`$. | [Commuting comparison](commuting_comparison.md) |
| Finite-copy construction | A smoothed spectral decision with controlled sample-based simulation achieves explicit error bounds without an eigenvalue-gap promise. Its copy count is independent of $`d`$ at fixed clean fraction and target risk in the stated dimension regime. | [Finite-copy decision](finite_copy.md) |
| Full charges and comparator | Preparation, all retained samples, known gates, synthesis and the single output are counted. The clean subfamily supplies an inherited $`\Omega(d)`$ classical-compilation lower bound at fixed nontrivial accuracy. | [Resources](resources.md) |

The scalar Rényi/total-variation extremal is a prior theorem of Rioul. Density-matrix exponentiation and the clean quantum-reference advantage are established mechanisms. The operational contamination reduction, compatible-source realization and resulting precision comparison are the contribution developed here. [Related work](../references/related_work.md) separates these roles.

## Reading route and boundaries

Read the [precision proof](precision_floor.md) for the information limit, then [the commuting comparison](commuting_comparison.md) for the role of noncommuting contamination. The [finite-copy account](finite_copy.md) constructs the decision from retained specimens; [resources](resources.md) explains the cost and sample-only comparator. [Interpretation](interpretation.md) joins the consequences and limitations.

At $`N=0`$ the minimax risk is $`1/2`$. If $`a\le1/d`$, the common training state $`I/d`$ is compatible with every pure target and every sample budget still has risk $`1/2`$. At $`a=1`$, the asymptotic risk is the oracle value. The source is IID, the clean target is pure, the background is known, and processing is ideal. Correlated batch poisoning, contaminated tests, arbitrary mixed clean sources, arbitrary backgrounds, hardware-noise tolerance and an optimal joint finite-$`N,d,a`$ law require different arguments.
