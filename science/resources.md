# Access, storage and implementation costs

The learner receives physical quantum training specimens. It is not given a classical vector of amplitudes, a purification, a preparation unitary, its inverse, or quantum random access to a classical dataset. The supplied-state model is appropriate when an experiment produces native quantum data. A classical dataset would require a separate encoding procedure, whose cost is not removed by the results here.

The [finite-copy construction](finite_copy.md) uses density-matrix simulation only through the training copies and known partial swaps. Its output is one classical classification bit for one clean test. The retained samples are consumed; no reusable learned model is promised.

## Chronology and memory

All $`N`$ training copies arrive before the test. With $`n=\lceil\log_2d\rceil`$, retaining the actual input copies uses $`Nn`$ qubits. They remain stored until the test arrives and the prediction circuit consumes them. The method needs no additional source call after that arrival.

The simulator couples the test to one retained copy at a time in a fixed predetermined order. This is sequential consumption of stored specimens, with no coherent addressing or QRAM operation. Its active processing uses two specimen-sized registers, a phase-estimation register of $`m`$ qubits, and a constant number of auxiliary qubits. Each phase-estimation round can be measured before the next, leaving $`O(rm)`$ classical record bits for the median. Thus

```math
\text{stored training qubits}=Nn,
\qquad
\text{total quantum width}\le(N+1)n+m+O(1),
```

```math
\text{active processing width}=2n+m+O(1).
```

The smaller active width does not replace the total storage bound. Exact copies and ideal storage are part of the present circuit model. A specified memory-noise or lifetime model would change the task and its resource comparison.

When $`d`$ is not a power of two, use a known $`d`$-dimensional subspace of the $`n`$-qubit register. The training states and both test hypotheses lie in that subspace. Swap gates act on the entire registers, while the maximally mixed reference remains $`I_d/d`$ on the valid subspace. No change of the background dimension is made.

## A finite circuit over known gates

Write $`S=\operatorname{SWAP}_{AB}`$. Since $`S^2=I`$, a partial swap is

```math
e^{-ihS}=\cos(h)I-i\sin(h)S.
```

It can be implemented by coherently recording the eigenvalue of $`S`$ in one auxiliary qubit, applying the known phase $`e^{-ihZ}`$ there, and uncomputing that record. Recording the eigenvalue uses a Hadamard, a controlled swap, and a Hadamard. A control on the phase gate therefore implements

```math
e^{-ih|1\rangle\langle1|_C\otimes S}
```

with two known controlled swaps and a controlled single-qubit rotation. A swap between $`n`$-qubit registers is a product of $`n`$ pairwise swaps, so the controlled partial swap requires $`O(n)`$ elementary known gates before rotation synthesis. These gates do not depend on the unknown target, contamination state or spectrum.

One phase-estimation round also uses an inverse Fourier transform on $`m`$ qubits. A direct circuit uses $`O(m^2)`$ elementary known gates. Classical comparisons and a median of $`r`$ numbers of $`m`$ bits have a finite polynomial cost in $`r,m`$. The ideal-rotation gate count is therefore

```math
M=O(Nn+rm^2).
\tag{R1}
```

This is the usual circuit model with arbitrary pairs of registers available for known two-qubit gates. A hardware connectivity constraint would require adding its routing gates. No local-depth or hardware-wall-time optimum is asserted.

### Finite gate-set synthesis

Every required angle is computable from $`t,\gamma`$ and the integer copy allocation in F1a. Approximate the ideal single-qubit rotations by a finite universal gate set, retaining exact known controlled-swap decompositions. If every synthesized elementary rotation has operator-norm error at most $`\xi_{\rm gate}/(2M)`$, a circuit hybrid bounds the resulting unhalved diamond error by $`\xi_{\rm gate}`$. One may use the constructive [Solovay–Kitaev compiler of Dawson and Nielsen](https://arxiv.org/abs/quant-ph/0505030v2), whose gate-count overhead is $`O(\log^{3.97}(M/\xi_{\rm gate}))`$ per rotation. This gives the conservative finite gate-set bound

```math
G_{\rm proc}
=O\!\left[
(Nn+rm^2)\log^{3.97}\!\left(\frac{Nn+rm^2}{\xi_{\rm gate}}\right)
\right].
\tag{R2}
```

The compiler is inherited; more efficient rotation-synthesis methods can improve this overhead. F1 includes its error in the same prediction-risk budget as simulation error. The result does not assume exact implementation of arbitrary real rotation angles by a finite gate alphabet.

## Source preparation and output

Let $`G_\rho`$ be the actual cost of supplying one independent copy of the contaminated source, including any required encoding or experimental preparation. Let $`G_{\rm test}`$ be the cost of supplying the one test. The complete gate-work account, when these costs are expressed in gate units, is

```math
G_{\rm total}
=N G_\rho+G_{\rm test}+G_{\rm proc}.
\tag{R3}
```

All $`N`$ source invocations are charged, even though the learner may not know their generating circuits. Independent samples, rather than coherent control of a preparation map, are enough. Clean work-qubit initialization, measurement and discarding consumed samples are allowed known operations. Their number is polynomial in the displayed circuit size and is included when they are assigned a nonunit cost.

The final output is one bit. The optional phase estimates occupy only the stated classical records; the algorithm does not print the density matrix, its eigenvectors or a classical description of $`P`$. Its preparation and output costs therefore differ from a tomography task.

For a native source with polynomial $`G_\rho`$ in $`n`$ and fixed $`a,\varepsilon`$, F2 together with R2–R3 has polynomial processing work in $`n`$. If generating each source specimen is itself expensive, that expense remains in $`NG_\rho`$. A copy-complexity statement alone is not an unconditional end-to-end runtime speedup.

## What changes with the demanded precision

The sufficient budgets in [F2 and F3](finite_copy.md) are

| Guarantee | Sufficient dimension regime | Training copies, up to constants |
|---|---|---|
| $`R\le\varepsilon`$, every $`a>0`$ | $`d\ge8/(a\varepsilon^2)`$ | $`a^{-2}\varepsilon^{-3}\log^2(1/\varepsilon)`$ |
| $`R\le1/(2d)+\varepsilon`$, $`0<\eta=1-a\le1/4`$, $`\varepsilon\le\eta^2`$ | $`d\ge16\eta^2/(a^2\varepsilon^2)`$ | $`\eta^2a^{-4}\varepsilon^{-3}\log^2(1/\varepsilon)`$ |
| $`R\le1/(2d)+\eta^2/(2a^2)+\delta`$, $`\eta\le1/4`$ | Every $`d\ge2`$ | $`\delta^{-1}\log^2(1/\delta)`$ |

These are constructive sufficient bounds. At fixed risk and clean fraction they have no dimension dependence in their number of samples. When the requested excess error is of order $`\eta/\sqrt d`$, the fine-precision bound may instead require order $`d^{3/2}`$ samples, up to contamination factors and logarithms. It must not be described as a dimension-independent high-precision algorithm.

The clean subfamily $`\sigma=P`$ is admissible for every $`a`$. Therefore any lower bound for classical compilation of unknown pure-state training data remains a lower bound in the contaminated class, under the same chronology and prediction accuracy. In particular the known fixed-risk $`\Omega(d)`$ compiler bound gives an exponential separation in $`n`$ from F2 at fixed $`a,\varepsilon`$. The comparator is permitted a collective training measurement and unlimited classical storage; it must discard all quantum training information before the test. This is a restriction on the information retained across the train–test boundary, not a restriction on its classical computation. The inherited clean comparison and its source are discussed in the [related-work account](../references/related_work.md).

No matching finite-copy precision law is proved here. The exact limiting contamination risk, the achievable finite circuit, and the classical-compilation comparison are separate statements with separate proof dependencies.
