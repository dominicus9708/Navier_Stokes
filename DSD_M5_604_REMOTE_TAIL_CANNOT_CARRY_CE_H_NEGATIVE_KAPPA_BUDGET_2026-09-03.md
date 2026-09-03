# DSD M5-604 — Remote spectator tail cannot carry the CE-H negative-kappa budget

Date: 2026-09-03

Status: **MEASURE-BRIDGE STEP / ON CE-H, `kappa |W|^2 = W·Delta W`; A LARGE-R CUTOFF INTEGRATION BY PARTS SHOWS THAT THE EXTERIOR KAPPA BUDGET IS CONTROLLED BY THE EXTERIOR H1 VORTICITY TAIL PLUS ONE CUTOFF COMMUTATOR / M5-508 GIVES UNIFORM H1 TAIL TIGHTNESS ON THE COMPACT BRANCH, SO BOTH TERMS VANISH AS R→INFINITY / THEREFORE THE STRICT GLOBAL IDENTITY `int kappa |W|^2 = -P < 0` CANNOT BE PAID BY THE REMOTE SPECTATOR TAIL / EVERY FIXED NEGATIVE KAPPA BUDGET MUST REMAIN IN A FINITE SIMILARITY CORE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H input

On the CE-H branch,

\[
\boxed{\Delta W=\kappa W.}
\]

Therefore

\[
\boxed{\kappa|W|^2=W\cdot\Delta W.}
\]

Globally,

\[
\boxed{
\int_{\mathbb R^3}\kappa|W|^2dy
=-\int_{\mathbb R^3}|\nabla W|^2dy
=-P<0
}
\]

for every nonzero state.

---

## 2. Exterior cutoff

Choose a smooth radial cutoff `chi_R` with

\[
\chi_R=0\quad\text{on }B_R,
\qquad
\chi_R=1\quad\text{outside }B_{2R},
\]

and

\[
|\nabla\chi_R|\le C/R.
\]

Then

\[
\int\chi_R\kappa|W|^2
=
\int\chi_R W\cdot\Delta W.
\]

Integration by parts gives

\[
\boxed{
\int\chi_R\kappa|W|^2
=
-\int\chi_R|\nabla W|^2
-\int \nabla\chi_R\cdot(W\cdot\nabla W).
}
\]

---

## 3. Main exterior derivative term

M5-508 gives uniform Sobolev-tail tightness on the compact branch. In particular,

\[
\boxed{
\sup_{Y\in\mathfrak H}
\int_{|y|>R}|\nabla W_Y|^2dy
\to0
\qquad(R\to\infty).
}
\]

Hence

\[
\sup_Y
\left|
\int\chi_R|\nabla W_Y|^2
\right|
\to0.
\]

---

## 4. Cutoff commutator

The commutator is supported on

\[
A_R=\{R<|y|<2R\}.
\]

By Cauchy--Schwarz,

\[
\left|
\int \nabla\chi_R\cdot(W\cdot\nabla W)
\right|
\le
\frac{C}{R}
\|W\|_{L^2(A_R)}
\|\nabla W\|_{L^2(A_R)}.
\]

M5-508 gives uniform `L2` and `H1` tail tightness, so the product tends to zero uniformly; the additional factor `1/R` is harmless.

Therefore

\[
\boxed{
\sup_{Y\in\mathfrak H}
\left|
\int\chi_R\kappa|W|^2
\right|
\to0.
}
\]

---

## 5. Fixed finite-core localization of the negative budget

Suppose the marked compact CE-H component has a uniform palinstrophy floor

\[
P(Y)\ge p_0>0.
\]

This floor follows on a compact nonzero marked component whenever zero is excluded by the fixed persistent carrier mark: if a sequence had `P -> 0`, compactness would give an `H1` limit with `nabla W=0`; whole-space `L2` then forces `W=0`, contradicting the retained nonzero carrier.

Choose `R_kappa` large enough that

\[
\left|
\int_{|y|>R_\kappa}\kappa|W|^2
\right|
\le p_0/4
\]

uniformly on the component.

Since globally

\[
\int\kappa|W|^2=-P\le-p_0,
\]

we obtain

\[
\boxed{
\int_{B_{R_\kappa}}\kappa|W|^2dy
\le -\frac34p_0<0.
}
\]

Thus the negative CE-H budget is a finite-core phenomenon.

---

## 6. Relation to the endpoint spectator tail

The remote endpoint tail was already shown to be dynamically negligible for finite-core velocity, strain, and one-generation accumulated action.

The present calculation adds a stronger CE-H statement:

\[
\boxed{
\text{remote spectator tail}
\text{ cannot even carry a fixed fraction of }
-\int\kappa|W|^2.
}
\]

Hence the measure mismatch exposed in M5-603 must be resolved inside the same finite active core that contains the persistent production network.

---

## 7. Next target

Inside `B_{R_kappa}`, decompose the negative density

\[
-\kappa|W|^2
\]

between

1. fixed coherent neighborhoods of the finite persistent lineage network;
2. residual finite-core vorticity.

If a fixed residual negative part recurs, compact derivative bounds should extract a fixed-amplitude/fixed-flux coherent `kappa`-sink packet. The finite-memory genealogy can then test whether this packet is absorbed into the persistent network or generates a new/replacement label.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
