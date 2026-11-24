# Thirty milestones for understanding contaminated quantum training

The educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [source bridge](WATROUS_BRIDGE.md) identifies the relevant sections and notation. The [tutorial](TUTORIAL.md) develops a complete pure-source instance. The later milestones connect it to balanced flat-rank training.

The allocation is **twelve background/preliminaries milestones and eighteen narrative/innovation milestones**. The background joins the state, decision, convex-geometric and circuit objects needed to formulate one complete experiment. The narrative then joins the compatibility reduction and exact precision law to its physical witnesses, constructive decision and full resource comparison. The extra narrative space reflects the project’s two distinct endpoints: an optimal limiting error and explicit sufficient finite-copy budgets. Within each phase the route progresses from local objects to the integrated account. Specialist calculations remain in the canonical scientific chapters.

Watrous supplies the foundations. Rioul’s sharp scalar Rényi/variation frontier, density-matrix exponentiation and the clean quantum-reference comparison retain their separate research attribution. The map distinguishes these ingredients from the operational result developed here.

## Background and preliminaries

### M01 — A specimen, a pure state and a diffuse background

- **Phase:** background/preliminaries.
- **Central question:** What physical objects are compared when one clean quantum specimen must be recognized against a maximally mixed background?
- **Understanding target:** Distinguish a vector, its rank-one density operator $`P`$, a physical copy of that state, and the known reference $`I_d/d`$. Explain why the dimension controls the cost of accepting an extra direction.
- **Dependencies and story role:** None; this establishes the local state objects before introducing training or learning.
- **Conceptual connection:** Positivity and trace one describe possible specimens, while the contrast between a concentrated pure state and a diffuse background creates the recognition opportunity.
- **Source pointers:** Watrous §§1.1.2 and 2.1.2; [model: the experiment](../science/model.md#the-experiment).

### M02 — What a contaminated training copy actually contains

- **Phase:** background/preliminaries.
- **Central question:** What information is supplied by repeated copies of $`\rho=aP+(1-a)\sigma`$ when no component labels are revealed?
- **Understanding target:** Explain the known clean fraction, hidden fixed contaminant, IID product input and absence of clean/contaminant flags. Distinguish an ensemble decomposition from accessible classical side information.
- **Dependencies and story role:** M01; this turns individual states into the supplied training source without adding access that the experiment does not provide.
- **Conceptual connection:** The density matrix summarizes all available one-copy statistics; repeating it does not reveal a particular hidden decomposition merely because that decomposition appears in the model.
- **Source pointers:** Watrous §2.1.2, especially mixtures of states; [model: the experiment](../science/model.md#the-experiment); [interpretation: hidden clean sources](../science/interpretation.md#one-training-state-can-hide-several-clean-sources).

### M03 — A binary effect and the oracle error

- **Phase:** background/preliminaries.
- **Central question:** How does one effect turn the two test hypotheses into a classification risk?
- **Understanding target:** Derive the two conditional errors and their equal-prior average $`R(E,P)=[1-\mathrm{tr}(EP)+\mathrm{tr}(E)/d]/2`$. Explain why a known clean state permits the oracle error $`1/(2d)`$.
- **Dependencies and story role:** M01, M02; this attaches a concrete output and performance criterion to the source.
- **Conceptual connection:** Measurement effects make the tradeoff between missed clean tests and accepted background directions explicit. Total risk and excess above the oracle are different quantities.
- **Source pointers:** Watrous §2.3.1 and §3.1.1, Theorem 3.4; [model: learners and risks](../science/model.md#learners-and-risks); [precision floor: opening risk definition](../science/precision_floor.md).

### M04 — Positive domination and support

- **Phase:** background/preliminaries.
- **Central question:** What does $`aP\preceq\rho`$ say about which clean states a training density matrix can hide?
- **Understanding target:** Read a positive-semidefinite inequality, distinguish it from an entrywise inequality, and explain why a compatible pure vector must lie in the support of $`\rho`$. Recognize that an inverse must be restricted to that support.
- **Dependencies and story role:** M01, M02; this introduces the local feasibility relation from which the exact law will follow.
- **Conceptual connection:** Positivity is an operational promise: subtracting the promised clean component must leave a valid contaminant, rather than merely a matrix of trace $`1-a`$.
- **Source pointers:** Watrous §1.1.2 and §1.1.3; [precision floor: what infinite training reveals](../science/precision_floor.md#what-infinite-training-reveals).

### M05 — A spectrum is not a unique source decomposition

- **Phase:** background/preliminaries.
- **Central question:** Why can knowing all eigenvalues and eigenvectors of $`\rho`$ still leave the clean target unknown?
- **Understanding target:** Distinguish the spectral decomposition from other convex decompositions of the same density matrix. Explain how clean vectors with different eigenbasis phases can have the same coordinate probabilities and remain compatible with one training state.
- **Dependencies and story role:** M02, M04; this exposes the source ambiguity before any minimax calculation.
- **Conceptual connection:** The spectral theorem organizes the observed matrix; it does not identify which term an unflagged physical mixture was intended to contain.
- **Source pointers:** Watrous §1.1.3 and §4.3.2, Theorem 4.34; [interpretation: hidden clean sources](../science/interpretation.md#one-training-state-can-hide-several-clean-sources).

### M06 — Trace distance as a decision contrast

- **Phase:** background/preliminaries.
- **Central question:** How does optimizing a binary measurement become a trace norm, and when does it become classical total variation?
- **Understanding target:** Explain the Helstrom variational principle and its reduction to $`\mathrm{TV}(p,u_d)`$ for diagonal states. Keep the factors of two in contrast, trace distance and equal-prior risk consistent.
- **Dependencies and story role:** M03, M05; this connects local effects to the scalar objective that appears in the main proof.
- **Conceptual connection:** Quantum and classical discrimination share a variational structure, while the set of admissible clean states can remain genuinely quantum.
- **Source pointers:** Watrous §3.1.1, Theorems 3.4 and 3.7; [precision floor: scalar decision reduction](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem).

### M07 — What crosses the training–test boundary

- **Phase:** background/preliminaries.
- **Central question:** How do a coherent learner and a classical compiler differ when both may process the training data collectively?
- **Understanding target:** Explain the chronology of all training copies arriving before one test. Distinguish retaining source-dependent quantum systems from keeping an unrestricted classical record, without restricting the compiler to separate measurements or cheap classical computation.
- **Dependencies and story role:** M02, M03, M06; this places the decision inside the complete learning experiment.
- **Conceptual connection:** The comparison concerns retained information, not an artificial limitation on the quality of training measurements. Exact knowledge of $`\rho`$ is a separate information benchmark.
- **Source pointers:** Watrous §§2.2.1 and 2.3.1; [model: learners and risks](../science/model.md#learners-and-risks); [resources: chronology and memory](../science/resources.md#chronology-and-memory).

### M08 — Symmetry, convexity and robust decisions

- **Phase:** background/preliminaries.
- **Central question:** When can a worst-case decision problem be simplified by averaging an effect and exchanging convex optimizations?
- **Understanding target:** Distinguish a symmetry-preserving average from an unsupported restriction on measurements. Identify the compact convex sets and bilinear payoff needed for minimax, and explain why averaging over eigenbasis phases leads to diagonal effects here.
- **Dependencies and story role:** M04, M05, M06; this supplies the proof framework rather than assuming the source ambiguity can be ignored.
- **Conceptual connection:** The robust compatible-source set and a measurement’s linear payoff allow symmetry and convexity to simplify the same operational game.
- **Source pointers:** Watrous §1.2.1, Theorem 1.12; §3.1.1, Theorem 3.7; §4.1.1, Definition 4.4; [precision floor: scalar decision reduction](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem).

### M09 — Probability vectors, majorization and Rényi order one-half

- **Phase:** background/preliminaries.
- **Central question:** What information does $`\sum_i\sqrt{p_i}`$ retain about a probability vector beyond its largest coordinate?
- **Understanding target:** Interpret $`H_{1/2}(p)=2\log\sum_i\sqrt{p_i}`$, read a majorization relation and apply concavity of the square root in the correct direction. Distinguish textbook majorization tools from the sharp scalar frontier imported from Rioul.
- **Dependencies and story role:** M05, M06, M08; this prepares the entropy geometry without substituting it for the operational quantum proof.
- **Conceptual connection:** Once compatibility has been reduced to amplitudes, the geometry of probability vectors controls the nearest admissible distribution to uniform.
- **Source pointers:** Watrous §4.3.1, especially Definition 4.29; [precision floor: inherited entropy frontier](../science/precision_floor.md#evaluating-the-inherited-entropy-frontier); [related work](../references/related_work.md).

### M10 — Channels and an error budget that survives composition

- **Phase:** background/preliminaries.
- **Central question:** How can small implementation errors be converted into a valid bound on the final classification risk?
- **Understanding target:** Distinguish an operator, a quantum channel and a measurement channel. Explain why diamond distance includes arbitrary untouched references, why channel hybrids add segment errors, and why the unhalved convention matters for a binary outcome probability.
- **Dependencies and story role:** M03, M07; this introduces the local error language needed to turn a spectral rule into a finite circuit.
- **Conceptual connection:** A circuit may create correlations among test and work registers; a reference-stable channel norm controls their effect without assuming the registers remain independent.
- **Source pointers:** Watrous §2.2.1 and §3.3.2, Definition 3.43 and Proposition 3.48; [finite-copy decision: controlled simulation](../science/finite_copy.md#controlled-density-matrix-simulation-from-copies).

### M11 — Known controls are different from a controlled source oracle

- **Phase:** background/preliminaries.
- **Central question:** How can copies of an unknown state program a known-gate circuit without giving control of its unknown preparation?
- **Understanding target:** Explain a swap between two supplied registers, a controlled known gate, sequential consumption of stored copies, and the role of phase estimation. Keep these operations separate from QRAM, a purification, an inverse preparation map or a controlled unknown evolution.
- **Dependencies and story role:** M02, M07, M10; this connects the allowed hardware-level operations to the algorithm’s input contract.
- **Conceptual connection:** State copies are a resource consumed by sample-based simulation. The implemented controls are known operations on those copies, not extra black-box access to their generator.
- **Source pointers:** Watrous §2.2.1 for channel foundations; [finite-copy decision: finite phase-estimation filter](../science/finite_copy.md#a-finite-phase-estimation-filter) and [controlled simulation](../science/finite_copy.md#controlled-density-matrix-simulation-from-copies); [resources: a finite known-gate circuit](../science/resources.md#a-finite-circuit-over-known-gates). Phase estimation and sample-based simulation are supplied by these project and research sources, not assigned to an unverified textbook section.

### M12 — The complete question before its solution

- **Phase:** background/preliminaries.
- **Central question:** Which assumptions, outputs, information limits and costs must be kept together to state this learning problem correctly?
- **Understanding target:** Reconstruct the experiment from source to one output bit. Distinguish unknown pure-target recovery, one-test recognition, an exact-density information limit, and a finite-copy implementation. Explain why none of these automatically proves an unconditional total-runtime advantage.
- **Dependencies and story role:** M01–M11; this integrates the background phase into the full problem that the narrative resolves.
- **Conceptual connection:** States, effects, source compatibility, train–test chronology, convex geometry and channel errors now belong to one consistent resource model.
- **Source pointers:** Watrous foundations collected in [the bridge](WATROUS_BRIDGE.md); [model](../science/model.md), [precision floor](../science/precision_floor.md), [commuting comparison](../science/commuting_comparison.md), [finite-copy decision](../science/finite_copy.md), [resources](../science/resources.md), and [interpretation](../science/interpretation.md).

## Narrative and innovation

### M13 — The inverse-weighted compatibility condition

- **Phase:** narrative/innovation.
- **Central question:** How does positive domination become an exact condition on the clean state’s eigenbasis amplitudes?
- **Understanding target:** Derive $`aP\preceq\rho\Leftrightarrow\sum_{\lambda_i \gt 0}p_i/\lambda_i\le1/a`$, with zero amplitude outside the support. Explain why purity is essential to this rank-one inverse criterion.
- **Dependencies and story role:** M04, M05, M12; this is the first local step of the operational reduction.
- **Conceptual connection:** Conjugating by the support inverse square root replaces a matrix inequality by the only nonzero eigenvalue of a rank-one operator.
- **Source pointers:** Watrous §§1.1.2–1.1.3; [precision floor: scalar decision reduction](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem).

### M14 — Why eigenbasis phases can be averaged out of the effect

- **Phase:** narrative/innovation.
- **Central question:** Which phase information creates source ambiguity, and why may the learner nevertheless use a diagonal robust effect?
- **Understanding target:** Show that the compatible-source set is invariant under independent eigenbasis phases and that averaging an effect preserves its trace while improving or retaining worst-case acceptance. Keep the allowed target phases in the adversarial set rather than discarding them.
- **Dependencies and story role:** M08, M13; this removes irrelevant measurement coordinates while preserving the full robust task.
- **Conceptual connection:** Symmetry simplifies the learner’s decision precisely because all phase-related clean sources must still be handled.
- **Source pointers:** Watrous §4.1.1 for pinching and §1.2.1 for convexity; [precision floor: scalar decision reduction](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem).

### M15 — The fixed-density robust game becomes total variation

- **Phase:** narrative/innovation.
- **Central question:** Why is the optimal contrast at known $`\rho`$ the smallest total variation from uniform among its compatible amplitude distributions?
- **Understanding target:** Identify $`K_\lambda`$, the effect cube $`[0,1]^d`$ and their bilinear payoff. Justify minimax and derive $`g_a(\lambda)=\min_{p\in K_\lambda}\mathrm{TV}(p,u_d)`$, retaining the risk conversion $`(1-g_a)/2`$.
- **Dependencies and story role:** M06, M08, M14; this completes the fixed-source decision reduction before optimizing the contaminating source.
- **Conceptual connection:** The trace-norm discrimination principle acts on the convexified compatible alternatives, not on an arbitrarily chosen single reconstruction of the target.
- **Source pointers:** Watrous §1.2.1, Theorem 1.12, and §3.1.1, Theorems 3.4 and 3.7; [precision floor: scalar decision reduction](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem).

### M16 — Eliminating the contaminated spectrum

- **Phase:** narrative/innovation.
- **Central question:** Why does the adversary’s freedom to choose $`\rho`$ produce a Rényi-order-one-half constraint?
- **Understanding target:** Apply Cauchy–Schwarz to minimize $`\sum_i p_i/\lambda_i`$ over spectra and obtain $`\lambda_i\propto\sqrt{p_i}`$. Explain why the resulting joint minimization is legitimate and does not interchange opposing optimization orders.
- **Dependencies and story role:** M09, M13, M15; this is the central bridge from physical source compatibility to a sharp classical entropy frontier.
- **Conceptual connection:** The operational theorem uses a familiar inequality to identify exactly which probability vectors an adversarial contaminated quantum source can conceal.
- **Source pointers:** Watrous §1.1.2 for the underlying operator and vector setting; [precision floor: scalar decision reduction](../science/precision_floor.md#from-quantum-compatibility-to-a-scalar-decision-problem); [related work](../references/related_work.md).

### M17 — The inherited extremal probability vector

- **Phase:** narrative/innovation.
- **Central question:** At fixed variation from uniform, why does one large coordinate plus filled $`1/d`$ coordinates minimize the square-root sum?
- **Understanding target:** Explain the partial-sum majorization argument for $`p^\star(q)`$, the fractional final coordinate and the direction of square-root concavity. Attribute this scalar frontier to Rioul rather than treating its reconstruction as a new inequality.
- **Dependencies and story role:** M09, M16; this evaluates the scalar problem that the operational reduction has earned.
- **Conceptual connection:** Watrous’s majorization foundations make the imported research theorem readable; Rioul’s sharp frontier is the separate load-bearing scalar dependency.
- **Source pointers:** Watrous §4.3.1; [precision floor: inherited entropy frontier](../science/precision_floor.md#evaluating-the-inherited-entropy-frontier); Rioul (2023), Theorem 6 and Example 19, Eq. (96), as attributed in [related work](../references/related_work.md).

### M18 — The exact root law and its endpoints

- **Phase:** narrative/innovation.
- **Central question:** How does the scalar frontier determine the exact finite-dimension irreducible prediction error?
- **Understanding target:** Read $`S_d(q_d(a))=a^{-1/2}`$ and $`R_\infty=(1/d+q_d(a))/2`$, explain continuity at grid boundaries, and handle $`a=1`$, $`a=1/d`$ and $`a \lt 1/d`$ correctly. Keep total error distinct from $`q_d(a)/2`$ excess.
- **Dependencies and story role:** M15, M16, M17; this assembles the first global result of the narrative.
- **Conceptual connection:** The operational robust game and inherited entropy geometry now give one optimal information limit with explicit boundary conventions.
- **Source pointers:** [Precision floor: exact law](../science/precision_floor.md#exact-law-including-the-endpoints) and [entropy-frontier proof](../science/precision_floor.md#evaluating-the-inherited-entropy-frontier); [model: perfect-density information](../science/model.md#perfect-density-information-and-its-asymptotic-meaning).

### M19 — A finite physical family attaining the ambiguity

- **Phase:** narrative/innovation.
- **Central question:** Which actual target–contaminant pairs force the exact lower bound, even after arbitrary collective training?
- **Understanding target:** Construct the finite Fourier-phase targets, common spectrum $`\lambda_i\propto\sqrt{p_i}`$ and positive normalized contaminants. Explain why every training input is identical while the average clean test becomes $`\mathrm{diag}(p)`$.
- **Dependencies and story role:** M05, M13, M16, M18; this turns an optimized scalar value into an operational impossibility witness.
- **Conceptual connection:** Ensemble nonuniqueness is used to build explicit compatible physical instances, and Helstrom discrimination converts their average test state into the exact risk.
- **Source pointers:** Watrous §4.3.2 for ensemble foundations and §3.1.1 for discrimination; [precision floor: finite least-favorable family](../science/precision_floor.md#a-finite-least-favorable-family-of-indistinguishable-sources).

### M20 — Why both learner classes reach the same limiting floor

- **Phase:** narrative/innovation.
- **Central question:** Is exact-density information merely a genie benchmark, or is it the actual limit of finite training?
- **Understanding target:** Explain the tomography-and-relaxed-compatibility construction with $`\tau=(\widehat\rho+\delta I)/(1+d\delta)`$ and $`a'=a/(1+d\delta)`$. Conclude that both coherent and classical-compiler risks tend to $`R_\infty`$ with $`d,a`$ fixed, without inferring an efficient finite-copy rate.
- **Dependencies and story role:** M07, M10, M13, M18; this connects the exact information theorem to the original learning chronology.
- **Conceptual connection:** A classical record eventually suffices at fixed dimension, while finite-training costs can still differ greatly. Equality of limits is not equality of sample complexity.
- **Source pointers:** Watrous §§2.2.1 and 2.3.1 for the allowed channels and measurements; [precision floor: literal finite-training limit](../science/precision_floor.md#the-literal-finite-training-limit); [model: perfect-density information](../science/model.md#perfect-density-information-and-its-asymptotic-meaning).

### M21 — Two small-contamination precision scales

- **Phase:** narrative/innovation.
- **Central question:** Why does the unavoidable excess have order $`\min\{\eta^2,\eta/\sqrt d\}`$ uniformly for small contamination?
- **Understanding target:** Follow the tail square-root bounds that relate $`q_d(a)`$ to $`\max\{\sqrt q,q\sqrt d\}`$. Explain the low-dimensional plateau and the many-direction regime, including why the constants are uniform in $`d`$ and $`\eta\le1/4`$.
- **Dependencies and story role:** M17, M18; this extracts a useful global precision comparison from the exact root without replacing it by an uncontrolled asymptotic.
- **Conceptual connection:** The fractional-coordinate frontier creates two ways to spend compatible amplitude mass, with different recognition costs.
- **Source pointers:** [Precision floor: uniform small-contamination law](../science/precision_floor.md#small-contamination-uniformly-in-dimension); [interpretation: two precision scales](../science/interpretation.md#two-precision-scales); [exact-law figure](../verification/figures/README.md).

### M22 — Absolute error, oracle-relative error and ordered limits

- **Phase:** narrative/innovation.
- **Central question:** What does the $`d^{-1/2}`$ expansion say, and what does it leave unproved?
- **Understanding target:** Explain the controlled fractional-grid remainder and the fixed-$`a`$ coefficient $`(a^{-1/2}-1)/2`$. Distinguish vanishing absolute error from the growing ratio to the $`d^{-1}`$ oracle error, and preserve the order $`N\to\infty`$ before $`d\to\infty`$.
- **Dependencies and story role:** M18, M20, M21; this gives the exact law its asymptotic meaning without asserting a joint finite-$`N,d,a`$ theorem.
- **Conceptual connection:** The information limit, its dimension expansion and the cost of approaching it are separate mathematical statements.
- **Source pointers:** [Precision floor: fixed clean fraction](../science/precision_floor.md#fixed-clean-fraction-and-growing-dimension); [interpretation: absolute and relative error](../science/interpretation.md#absolute-error-and-relative-oracle-accuracy).

### M23 — Isolating the cost of noncommuting contamination

- **Phase:** narrative/innovation.
- **Central question:** What changes if the contaminant commutes with the unknown clean state, without revealing a common basis?
- **Understanding target:** Identify compatible clean vectors as eigenvectors of $`\rho`$ with eigenvalue at least $`a`$, including degenerate eigenspaces. Derive the optimal high-subspace effect and exact risk $`\min\{d,\lfloor1/a\rfloor\}/(2d)`$, and recognize the known-basis point model as a specialization.
- **Dependencies and story role:** M04, M05, M18, M22; this compares source classes within the same quantum experiment rather than changing the learner’s supplied information.
- **Conceptual connection:** Nonorthogonal compatible decompositions create a precision cost that cannot be reduced to uncertainty about an unknown classical point label.
- **Source pointers:** Watrous §1.1.3 for spectral and commuting structure; [commuting comparison](../science/commuting_comparison.md); [interpretation: noncommuting contamination](../science/interpretation.md#the-role-of-noncommuting-contamination).

### M24 — Recognition despite unrecoverable clean-state information

- **Phase:** narrative/innovation.
- **Central question:** How can accurate recognition remain possible when estimating the clean state has a nonzero limiting error?
- **Understanding target:** Explain the common-density construction for two pure states using $`(P+Q+|P-Q|)/2`$ and the resulting trace-distance reconstruction lower bound. Contrast that fixed ambiguity with the decreasing recognition error against $`I_d/d`$.
- **Dependencies and story role:** M06, M19, M22, M23; this integrates the information-limit part of the narrative into its physical meaning.
- **Conceptual connection:** Prediction can tolerate accepting extra directions when its background is diffuse. The conclusion concerns this recognition task, not arbitrary backgrounds, state recovery or a reusable learned model.
- **Source pointers:** Watrous §3.1.1 for trace-distance decision geometry; [precision floor: recognition versus reconstruction](../science/precision_floor.md#recognition-does-not-require-reconstructing-the-clean-state); [flat-rank compatibility](../science/flat_rank_training.md#common-specimens-and-the-recognition-converse); [interpretation](../science/interpretation.md).

### M25 — A spectral decision with controlled missed mass

- **Phase:** narrative/innovation.
- **Central question:** How can a finite learner recognize the clean test without learning the entire eigenbasis or identifying the clean component?
- **Understanding target:** Use inverse-weighted compatibility to bound clean mass below a cutoff and trace one to bound the number of accepted modes. Derive the two terms $`t/a`$ and $`1/(2dt)`$ in the classifier’s risk, keeping purity and the uniform background visible.
- **Dependencies and story role:** M03, M11, M13, M24; this starts the constructive part from the operational decision needed, rather than from a reconstruction algorithm.
- **Conceptual connection:** A smooth function of $`\rho`$ can provide the needed test even when the source’s eigendirections remain unknown in classical form.
- **Source pointers:** [Finite-copy decision: spectral classifier](../science/finite_copy.md#f1-a-spectral-classifier-without-a-gap-promise) and [cutoff risk proof](../science/finite_copy.md#why-the-spectral-cutoff-controls-the-prediction-risk).

### M26 — Finite phase estimation without a spectral-gap promise

- **Phase:** narrative/innovation.
- **Central question:** How does a finite phase-estimation circuit approximate the spectral acceptance rule without deciding every near-threshold eigenvalue correctly?
- **Understanding target:** Explain the finite phase grid, a transition interval, fresh phase registers and median amplification with independence conditional on an eigenvalue. Distinguish a controlled failure probability from a nonexistent gap promise, and translate the ideal spectral error into classification error.
- **Dependencies and story role:** M10, M11, M25; this supplies a finite measurement realization of the desired spectral rule.
- **Conceptual connection:** The risk argument tolerates arbitrary behavior inside a band, so the circuit needs bounded estimation accuracy rather than an exact discontinuous projector.
- **Source pointers:** Watrous §1.2.2, Theorem 1.16, for concentration; [finite-copy decision: finite phase-estimation filter](../science/finite_copy.md#a-finite-phase-estimation-filter). The explicit phase-estimation construction is supplied in that chapter.

### M27 — Controlled simulation from consumed training copies

- **Phase:** narrative/innovation.
- **Central question:** Which allowed circuit implements the controlled evolution, and how are its simulation errors charged?
- **Understanding target:** Reconstruct the controlled partial-swap identity, its reference-stable remainder and the $`4T^2/n`$ hybrid bound. Apply the bound to phase-estimation segments for a pure source and to a single Hadamard test for a balanced support.
- **Dependencies and story role:** M10, M11, M26; this closes the access and error-budget gap between the formal filter and a supplied-copy algorithm.
- **Conceptual connection:** Known-gate control and sample-based simulation produce the measurement channel with an explicit diamond-error account; correlations among test and work registers are already included.
- **Source pointers:** Watrous §3.3.2, Definition 3.43 and Proposition 3.48; [finite-copy decision: controlled simulation](../science/finite_copy.md#controlled-density-matrix-simulation-from-copies); [balanced-rank Hadamard test](../science/flat_rank_training.md#coherent-construction-with-finite-copies).

### M28 — Which finite-copy bound applies at the requested precision

- **Phase:** narrative/innovation.
- **Central question:** How do the arbitrary-clean-fraction, fine-precision and leading-eigenvector branches fit the two precision scales?
- **Understanding target:** Read F2, F3a and F3b with their dimension and error regimes. Distinguish risk from excess, fixed precision from precision shrinking with $`d`$, and sufficient budgets from an optimal joint law. Explain why substituting the limiting $`\eta/\sqrt d`$ scale can make the stated copy upper bound grow with dimension.
- **Dependencies and story role:** M21, M22, M25, M27; this integrates the constructive guarantees with the earlier information limit.
- **Conceptual connection:** The same spectral mechanism is used at different thresholds; resolving smaller thresholds costs more simulated evolution and more program copies.
- **Source pointers:** [Finite-copy decision: F2](../science/finite_copy.md#f2-arbitrary-positive-clean-fraction), [F3](../science/finite_copy.md#f3-dependence-on-a-small-contamination-fraction), and [coarse-precision branch](../science/finite_copy.md#a-coarse-precision-branch-close-to-the-clean-problem); [resources: precision changes](../science/resources.md#what-changes-with-the-demanded-precision).

### M29 — The complete resource comparison

- **Phase:** narrative/innovation.
- **Central question:** What remains of the quantum learning comparison after every supplied copy, stored register, known gate and output is charged?
- **Understanding target:** Distinguish active processing width from all retained training storage, add source and test preparation to processing and synthesis, and identify the single-bit output. Explain how the clean subfamily gives a compiler lower bound and why tomography reaches the coherent risk order at balanced rank.
- **Dependencies and story role:** M07, M12, M27, M28; this evaluates the full implementation and its correctly matched comparator.
- **Conceptual connection:** The scientific benefit concerns the information that survives the train–test boundary; explicit preparation and storage charges keep that statement separate from free loading or hidden quantum memory.
- **Source pointers:** [Resources](../science/resources.md), [precision and comparator scope](../science/resources.md#what-changes-with-the-demanded-precision), and [measurement-first construction](../science/flat_rank_training.md#measurement-first-and-a-spectral-threshold).

### M30 — One integrated account of what contamination costs

- **Phase:** narrative/innovation.
- **Central question:** How does one source ambiguity produce different costs for pure-source recognition, balanced recognition and ordinary reflection?
- **Understanding target:** State the exact pure-source floor and distinguish it from the balanced finite-copy law. Explain why balanced recognition is quadratic in weak contamination while the reflection error is linear and grows with batch size.
- **Dependencies and story role:** M18, M19, M22, M23, M24, M27, M28, M29. This joins the pure-source results and the balanced comparison using their common specimen geometry.
- **Conceptual connection:** The same training density can hide several clean sources. The output task determines which differences between those sources affect the loss.
- **Source pointers:** [Pure-source precision floor](../science/precision_floor.md), [balanced recognition and reflection](../science/flat_rank_training.md#one-source-ambiguity-two-different-tasks), and [Watrous bridge](WATROUS_BRIDGE.md#from-a-ray-to-a-balanced-support).
