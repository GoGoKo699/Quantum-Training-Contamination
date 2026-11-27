# Quantum Training Contamination

**How accurately can a quantum learner recognize a clean source when its training specimens are contaminated?**

An unknown pure state $`P=|\psi\rangle\langle\psi|`$ contributes a known fraction $`a`$ to every training mixture,

```math
\rho=aP+(1-a)\sigma,
```

where the hidden contaminant $`\sigma`$ is arbitrary. All training specimens arrive before one clean test, drawn equally from $`P`$ or the known maximally mixed background $`I/d`$. The output is one label.

The learner retains the training specimens and consumes them in a circuit of known partial SWAPs, phase estimation, measurements and classical thresholding. It returns one prediction without reconstructing the clean state. This repository gives the finite construction and its resource costs, then determines the prediction error that remains when different clean sources emit exactly the same training density matrix.

## Implement the finite learner

The [circuit guide](science/learner_circuit.md) specifies the registers, copy allocation, gates and decision rule. The input is physical quantum specimens with a known clean fraction; the gate sequence uses no classical description of their unknown states. The spectral filter requires no eigenvalue-gap promise.

| Step | Operation |
|---|---|
| Retain the training | Store every supplied copy until the one test arrives. |
| Interact with a stored specimen | Use a known controlled partial-SWAP gadget, then discard the consumed specimen. Repeat in a fixed order with fresh stored copies. |
| Estimate the spectral weight | Use those interactions for the controlled evolutions in phase estimation, followed by an inverse Fourier transform and computational-basis measurement. |
| Combine the readouts | Unwrap and clip the phase estimates, then take their classical median. |
| Predict | Compare the median with the prescribed cutoff and return one bit. |

For a known $`a\in(0,1]`$ and target risk $`0 \lt \varepsilon\le1/4`$, the existing [F2 construction](science/finite_copy.md#f2-arbitrary-positive-clean-fraction) gives

```math
R\le\varepsilon,
\qquad
N=O\!\left(\frac{\log^2(1/\varepsilon)}{a^2\varepsilon^3}\right),
```

when $`d\ge8/(a\varepsilon^2)`$. At fixed clean fraction and target risk, this sufficient training-copy count is independent of dimension in the stated regime. [F1](science/finite_copy.md#f1-a-spectral-classifier-without-a-gap-promise) supplies the explicit integer allocation and includes simulation and gate-synthesis errors; [F3](science/finite_copy.md#f3-dependence-on-a-small-contamination-fraction) resolves other precision regimes.

With $`n=\lceil\log_2d\rceil`$, the stored training alone occupies $`Nn`$ qubits. The active processor uses two specimen-sized registers, a phase register and constant auxiliary space. [The resource account](science/resources.md) separately charges total storage, known gates, finite gate synthesis and every source preparation. The specimens are consumed for this prediction, and storage and processing are ideal apart from the stated synthesis errors.

The finite circuit gives achievable error bounds. The exact law below describes the optimal limiting error at fixed dimension and clean fraction as the training budget grows; it is a separate result.

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

At fixed contamination the pure-source oracle error is of order $`d^{-1}`$, while the contaminated limit is of order $`d^{-1/2}`$. The pure-source constructions give achievable finite-copy guarantees in general dimension.

## Related projects on flat-rank training

[Quantum Classification Rank Limits](https://github.com/GoGoKo699/Quantum-Classification-Rank-Limits) supplies the clean flat-rank accuracy converse. [Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming) uses contaminated specimens to program an ordinary reflection. A rotation between compatible clean supports changes the reflection channel to first order, whereas its balanced recognition cost is quadratic for weak contamination.

For [flat-rank recognition](science/flat_rank_training.md), the clean class is $`P/r`$, the dimension is $`d=2r`$, and training has state $`\rho=aP/r+(1-a)\sigma`$. With $`x=r(1-a)/a`$ and $`N\ge1`$, both coherent retention and measurement-first compilation have the same minimax excess risk order:

```math
\Theta\!\left(\min\left\{1,\frac{r^2}{N}+\frac{\min\{x^2,x,r\}}r\right\}\right).
```

At fixed $`r,a`$ with $`x\lt1`$, their exact excess over the oracle tends to $`(1-\sqrt{1-x^2})/(4r)`$. The [reflection account](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/science/contaminated_reflections.md) gives a separate contamination floor of order $`\min\{1,kx\}`$ in unhalved diamond norm for a batch of $`k`$ targets.

## Read the connected scientific account

| Reader's question | Route |
|---|---|
| What do I prepare, apply and measure? | [Circuit guide](science/learner_circuit.md), then the [finite-copy proof](science/finite_copy.md) and [resource charges](science/resources.md) |
| What is the task, and how accurately can any learner solve it? | [Pure-source model](science/model.md), [exact precision proof](science/precision_floor.md) and [commuting comparison](science/commuting_comparison.md) |
| What changes for a clean source with higher rank? | [Flat-rank recognition](science/flat_rank_training.md), including its distinct coherent and measurement-first constructions |

[llms.txt](llms.txt) maps these questions to the authoritative statements for automated readers.

The exact scalar Rényi-entropy/variation extremal is inherited from Rioul. Ensemble nonuniqueness, minimax theory, sample-based Hamiltonian simulation and clean quantum-reference advantages are established ingredients. The contribution here is their operational connection to the solved contaminated-training prediction limit and its noncommuting-source consequence. [Related work](references/related_work.md) and [bibliography](references/references.bib) identify the dependencies and nearby tasks.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript. The learning route connects selected textbook foundations to the pure-source results and the balanced flat-rank extension.

| To understand | Read |
|---|---|
| How the learning materials fit together | [Learning overview](learning/README.md) |
| The existing finite learner as registers, gates and readouts | [Circuit guide](science/learner_circuit.md) |
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
