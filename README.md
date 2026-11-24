# Quantum Training Contamination

**How accurately can a quantum learner recognize a clean source when its training specimens are contaminated?**

An unknown pure state $`P=|\psi\rangle\langle\psi|`$ contributes a known fraction $`a`$ to every training mixture,

```math
\rho=aP+(1-a)\sigma,
```

where the hidden contaminant $`\sigma`$ is arbitrary. All training specimens arrive before one clean test, drawn equally from $`P`$ or the known maximally mixed background $`I/d`$. The output is one label.

Different clean states can produce exactly the same training density matrix. This repository computes what that ambiguity costs for prediction, compares commuting and noncommuting contamination, and constructs finite-copy coherent decisions with their costs included.

## Related projects on flat-rank training

[Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits) supplies the clean flat-rank accuracy converse. [Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming) uses contaminated specimens to program an ordinary reflection. A rotation between compatible clean supports changes the reflection channel to first order, whereas its balanced recognition cost is quadratic for weak contamination.

For [flat-rank recognition](science/flat_rank_training.md), the clean class is $`P/r`$, the dimension is $`d=2r`$, and training has state $`\rho=aP/r+(1-a)\sigma`$. With $`x=r(1-a)/a`$ and $`N\ge1`$, both coherent retention and measurement-first compilation have the same minimax excess risk order:

```math
\Theta\!\left(\min\left\{1,\frac{r^2}{N}+\frac{\min\{x^2,x,r\}}r\right\}\right).
```

At fixed $`r,a`$ with $`x\lt1`$, their exact excess over the oracle tends to $`(1-\sqrt{1-x^2})/(4r)`$. The [reflection account](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/science/contaminated_reflections.md) gives a separate contamination floor of order $`\min\{1,kx\}`$ in unhalved diamond norm for a batch of $`k`$ targets.

## The exact prediction limit

Write $`\eta=1-a`$. The known-clean-state optimum is $`R_\star=1/(2d)`$. For $`1/d \lt a\le1`$, define $`q_d(a)`$ as the unique root on $`[0,1-1/d]`$ of

```math
\sqrt{1-q}+\frac{\lfloor dq\rfloor}{\sqrt d}
+\sqrt{q-\frac{\lfloor dq\rfloor}{d}}=a^{-1/2}.
```

The exact asymptotic minimax risk is

```math
R_\infty(d,a)=\frac{1/d+q_d(a)}2.
```

If $`a\le1/d`$, it is $`1/2`$. The limit is taken with dimension and clean fraction fixed while the training budget grows. The [proof](science/precision_floor.md) gives explicit different clean sources that emit identical contaminated training data.

| Consequence | Precise content | Scientific account |
|---|---|---|
| Uniform small-contamination law | For $`0 \lt \eta\le1/4`$, excess risk is $`\Theta(\min\{\eta^2,\eta/\sqrt d\})`$. | [Exact limit and scaling](science/precision_floor.md) |
| Recognition versus reconstruction | At each fixed $`a\in(0,1)`$, recognition risk tends to zero as $`d^{-1/2}`$ while worst-case clean-state reconstruction has a nonzero ambiguity. | [Meaning and limits](science/interpretation.md) |
| Commuting contamination | Under $`[\sigma,P]=0`$, the exact limiting risk is $`\min\{d,\lfloor1/a\rfloor\}/(2d)`$; it equals the oracle risk when $`a \gt 1/2`$. | [Same-interface comparison](science/commuting_comparison.md) |
| Explicit finite-copy decisions | A gap-free spectral filter gives sufficient copy budgets, with controlled simulation and synthesis error included. | [F1–F3 and proofs](science/finite_copy.md) |
| Complete resource charges | Source preparation, all offline samples, total and active width, known gates and the single output are counted. | [Resource account](science/resources.md) |

At fixed contamination the pure-source oracle error is of order $`d^{-1}`$, while the contaminated limit is of order $`d^{-1/2}`$. The pure-source constructions give achievable finite-copy guarantees in general dimension.

## Read the connected scientific account

Start with the [pure-source model](science/model.md), then follow the [exact precision proof](science/precision_floor.md) and [commuting comparison](science/commuting_comparison.md). The [finite-copy construction](science/finite_copy.md) implements a decision using retained training specimens, with explicit [resource charges](science/resources.md). The [flat-rank proof](science/flat_rank_training.md) develops the balanced finite-copy law and the distinct coherent and measurement-first constructions. [llms.txt](llms.txt) maps the authoritative statements for automated readers.

The exact scalar Rényi-entropy/variation extremal is inherited from Rioul. Ensemble nonuniqueness, minimax theory, sample-based Hamiltonian simulation and clean quantum-reference advantages are established ingredients. The contribution here is their operational connection to the solved contaminated-training prediction limit and its noncommuting-source consequence. [Related work](references/related_work.md) and [bibliography](references/references.bib) identify the dependencies and nearby tasks.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript. The learning route connects selected textbook foundations to the pure-source results and the balanced flat-rank extension.

| To understand | Read |
|---|---|
| How the learning materials fit together | [Learning overview](learning/README.md) |
| One complete qubit experiment and its generalization | [Worked tutorial](learning/TUTORIAL.md) |
| Relevant textbook locations, notation, and the missing steps | [Watrous bridge](learning/WATROUS_BRIDGE.md) |
| The complete project's conceptual dependencies | [30-milestone map](learning/MILESTONES.md), with 12 background and 18 narrative milestones |

## Reproduce the finite checks

With Python 3.12 or later:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) explains independent compatible-spectrum and decision optimizations, physical contamination witnesses, endpoints, the commuting comparator and circuit checks. [Recorded results](verification/results.json) retain actual versions and numerical errors. These finite checks support the analytical account; they do not prove universal rates or establish priority.

## Scope

Both models use native unknown quantum specimens, IID contamination confined to training, ideal processing, and one consumed prediction against a maximally mixed background. All training copies arrive before the test. The coherent constructions store those copies, with active width and total storage charged separately. The compiler may measure the training systems collectively and retain an unrestricted classical record.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
