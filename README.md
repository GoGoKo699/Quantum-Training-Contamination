# Quantum Training Contamination

How accurately can a quantum learner recognize a clean source when its training specimens are contaminated?

An unknown pure state supplies a fixed fraction of each training mixture. The remaining fraction is an arbitrary unknown state. After all training specimens arrive, one clean test is drawn either from the pure source or from the known maximally mixed background, with equal probabilities.

The scientific question is the distinction between learning the clean state and learning the decision. Different clean states can produce exactly the same contaminated training state. That ambiguity need not cause the same prediction error: accepting a small uncertainty subspace is inexpensive against a diffuse background.

The account develops the exact asymptotic minimax prediction limit, a comparison with commuting contamination, and explicit finite-copy coherent constructions. Scalar Rényi-entropy extremals and sample-based Hamiltonian simulation are established ingredients and are attributed separately from their operational use here.

The model concerns independent state-level contamination, ideal quantum processing, a clean test and one consumed prediction. Source preparation, retained training systems, gates and approximation errors are charged. It does not assume QRAM, a preparation inverse or further source calls after the test arrives.

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
