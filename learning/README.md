# Learning the project

Start with the learner's operations: retain contaminated specimens, couple them to one later test through known controlled swaps, measure phase registers, and make one classical decision. The [circuit guide](../science/learner_circuit.md) supplies this entry route, while the [tutorial preview](TUTORIAL.md#start-with-the-circuit) introduces its purpose before developing the argument.

The guiding question is how well one can recognize a clean quantum source from training specimens containing an arbitrary admixture. The key distinction is between recovering the hidden pure state and learning the decision needed for one later clean test.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript linked from his [official page](https://cs.uwaterloo.ca/~watrous/TQI/). The material below uses selected foundations from that source and supplies the project-specific steps locally.

| Reader's purpose | Route |
|---|---|
| Follow the learner from input registers to one output bit | [Circuit guide](../science/learner_circuit.md) and [short tutorial preview](TUTORIAL.md#start-with-the-circuit) |
| Follow one complete concrete experiment | [Worked tutorial](TUTORIAL.md) |
| Translate the chosen textbook into this problem | [Watrous bridge and verified reading locations](WATROUS_BRIDGE.md) |
| Understand the dependencies of the complete scientific story | [30-milestone understanding map](MILESTONES.md) |
| Check the precise claims and assumptions | [Operational model](../science/model.md) |
| Follow the exact information limit and its source ambiguity | [Precision floor](../science/precision_floor.md) |
| Isolate what noncommuting contamination changes | [Commuting comparison](../science/commuting_comparison.md) |
| Connect the theorem to stored specimens and known gates | [Finite-copy construction](../science/finite_copy.md) and [resources](../science/resources.md) |
| Compare finite-copy recognition and reflection on flat supports | [Balanced-rank recognition](../science/flat_rank_training.md) and [its connection to programming](../science/flat_rank_training.md#one-source-ambiguity-two-different-tasks) |
| Separate textbook foundations from inherited research ingredients | [Related work](../references/related_work.md) |

The tutorial develops the pure-source experiment. The milestone map extends that route to balanced-rank recognition, including the matched finite-copy rates and the distinction between recognition error and reflection error.

The worked qubit example first supplies the exact training matrix to explain its optimal limiting decision. It then connects that decision to the existing finite-copy spectral filter, which receives specimens rather than a classical eigenbasis. The exact limiting law, sufficient finite-copy budgets and train–test memory comparison retain their separate guarantees.
