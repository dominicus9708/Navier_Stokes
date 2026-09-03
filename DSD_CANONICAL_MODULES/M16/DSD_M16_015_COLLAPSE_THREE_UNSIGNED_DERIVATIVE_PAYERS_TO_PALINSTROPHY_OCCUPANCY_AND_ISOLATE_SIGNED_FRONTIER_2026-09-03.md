# DSD M16-015 — Collapse three unsigned derivative payers to palinstrophy occupancy and isolate the signed frontier

Date: 2026-09-03
Canonical ID: **M16-015**

Status: **INTERNAL AUDIT / P1, P4, AND P5 FROM M16-014 DO NOT YET FORCE MATERIAL TURNOVER OR SOURCE REPLACEMENT. UNDER THE CE-H EIGENLINE CONDITION THEY ARE QUANTITATIVELY DOMINATED BY PALINSTROPHY-TYPE OCCUPANCY. THIS REMOVES AN OVERINTERPRETATION AND ISOLATES THE TRUE SIGNED FRONTIER TO STRAIN RESIDENCE AND AMPLITUDE-TRANSITION CURRENT, OR ELSE A NEW BOUNDED RESOURCE/CYCLE IDENTITY MUST BE FOUND. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M16-014

On the retained compact CE-H component, at positive invariant time density at least one of

\[
P_1,\ P_2,\ P_3,\ P_4,\ P_5
\]

occurs with a uniform positive floor.

The derivative-type payers are

\[
P_1:\quad
D_\sigma
=
\int e^{2\kappa}\chi\rho^2|\nabla\sigma|^2dy,
\]

\[
P_4:\quad
\mathfrak T_{\Sigma W}
=
\int e^{2\kappa}\chi\,\Sigma:\mathsf G_Wdy,
\qquad
\mathsf G_W{}_{ij}=\partial_iW\cdot\partial_jW,
\]

and

\[
P_5:\quad
M_\rho
=
\int e^{2\kappa}\chi|\nabla\rho|^2dy.
\]

The purpose of this audit is to determine whether these three already force a new material-genealogy event.

---

## 2. Exact derivative identity for the aligned strain eigenvalue

On the CE-H eigenline branch write

\[
W=\rho\xi,
\qquad |\xi|=1,
\qquad
\Sigma\xi=\sigma\xi.
\]

Differentiate the eigenvalue relation in the coordinate direction `k`:

\[
(\partial_k\Sigma)\xi+\Sigma\partial_k\xi
=(\partial_k\sigma)\xi+\sigma\partial_k\xi.
\]

Take the scalar product with `xi`. Since `Sigma` is symmetric,

\[
\xi\cdot\Sigma\partial_k\xi
=(\Sigma\xi)\cdot\partial_k\xi
=\sigma\,\xi\cdot\partial_k\xi=0,
\]

and also

\[
\xi\cdot\partial_k\xi=0.
\]

Therefore

\[
\boxed{
\partial_k\sigma
=
\xi\cdot(\partial_k\Sigma)\xi.
}
\]

Hence pointwise

\[
\boxed{
|\nabla\sigma|\le |\nabla\Sigma|.
}
\]

This removes any need to assign an independent derivative of `xi` to P1.

---

## 3. Biot–Savart / Riesz control

For divergence-free velocity in `R^3`, strain is an order-zero singular-integral transform of vorticity:

\[
\Sigma=\mathcal R_0[W].
\]

After one spatial derivative,

\[
\nabla\Sigma=\mathcal R_0[\nabla W],
\]

where `R_0` denotes a finite matrix of Riesz-type Fourier multipliers of degree zero.

Therefore

\[
\boxed{
\|\nabla\Sigma\|_{L^2}
\le C_{BS}\|\nabla W\|_{L^2}.
}
\]

Let

\[
P:=\|\nabla W\|_2^2.
\]

On the compact high-amplitude core the weights have uniform upper caps

\[
A_*:=\sup e^{2\kappa}\chi\rho^2<\infty,
\qquad
B_*:=\sup e^{2\kappa}\chi<\infty,
\qquad
S_*:=\|\Sigma\|_\infty<\infty.
\]

Then

\[
D_\sigma
\le A_*\|\nabla\sigma\|_2^2
\le A_*C_{BS}^2P.
\]

Thus

\[
\boxed{
P_1\text{ with }D_\sigma\ge c_1
\Longrightarrow
P\ge \frac{c_1}{A_*C_{BS}^2}.
}
\]

---

## 4. P5 is directly a palinstrophy subcharge

Because `rho=|W|`, wherever `rho>0`,

\[
\partial_k\rho=\xi\cdot\partial_kW,
\]

so

\[
|\nabla\rho|\le|\nabla W|.
\]

Consequently

\[
M_\rho
\le B_*P.
\]

Hence

\[
\boxed{
P_5\text{ with }M_\rho\ge c_5
\Longrightarrow
P\ge\frac{c_5}{B_*}.
}
\]

A positive magnitude-gradient packet is therefore a quantitative palinstrophy packet, but not yet a signed threshold crossing.

---

## 5. P4 is also controlled by palinstrophy occupancy

Since

\[
|\Sigma:\mathsf G_W|
\le |\Sigma|\,|\nabla W|^2,
\]

one has

\[
|\mathfrak T_{\Sigma W}|
\le B_*S_*P.
\]

Therefore

\[
\boxed{
P_4\text{ with }|\mathfrak T_{\Sigma W}|\ge c_4
\Longrightarrow
P\ge\frac{c_4}{B_*S_*}.
}
\]

P4 does force overlap of strain and vorticity derivative on a coherent packet, as established in M16-014, but the present audit shows that its scalar lower-bound content is still of palinstrophy type.

---

## 6. Comparison with the already-existing palinstrophy floor

Earlier compact-recurrence work already gave positive mean palinstrophy on the nontrivial retained component:

\[
\langle P\rangle>0,
\]

and, on the globally smooth compact branch, `P` has a finite uniform upper cap.

Consequently positive mean palinstrophy already implies a positive-density family of times on which

\[
P\ge p_0>0.
\]

Therefore the scalar conclusions extracted above from P1, P4, and P5 do **not** by themselves create a new contradiction or a new finite-resource debit.

They refine the geometry of where palinstrophy sits, but they do not yet show that material labels are replaced, exported, or forced across an amplitude sheet.

This is an important audit correction.

---

## 7. What remains genuinely directional

The five-payer alternative of M16-014 should therefore be reorganized into three classes.

### Class A — unsigned derivative occupancy

\[
\boxed{
\mathcal P_{der}
:=P_1\lor P_4\lor P_5.
}
\]

Its current rigorous content is coherent palinstrophy/strain-gradient occupancy.

### Class B — signed strain residence

\[
\boxed{
\mathcal P_{str}
:=P_2^+\lor P_2^-.
}
\]

The positive branch can be compared with the M15 positive-production genealogy. The negative branch is a compressive payer and requires a compensation audit; it cannot be relabeled as positive production.

### Class C — amplitude-transition activity

\[
\boxed{
\mathcal P_{amp}:=P_3.
}
\]

This is localized to the cutoff/threshold layer but remains unsigned until matched to the exact moving-level material current of M14--M15.

Thus

\[
\boxed{
E_{CEH}^{hard}
\Longrightarrow
\mathcal P_{der}
\lor
\mathcal P_{str}
\lor
\mathcal P_{amp}.
}
\]

---

## 8. DSD audit: prohibited shortcut

The following implication is **not** established:

\[
\mathcal P_{der}
\Longrightarrow
\text{turnover/replacement}.
\]

A recurrent smooth field may carry a persistent spatial gradient without any one-way material crossing.

Likewise

\[
|\mathcal C_{tot}|>0
\]

is not automatically a signed outward or inward amplitude flux.

Accordingly no derivative payer is allowed to be counted as a genealogy exit until an exact signed balance or a finite-resource debit is exhibited.

---

## 9. Reduced frontier

The correct next task is no longer to classify five local structures separately.

It is to answer one of the following two questions:

1. Can `P2` or `P3` be converted, using the exact CE-H material laws, into a signed threshold/source current already covered by M14--M15?

2. If the survivor remains in `P_der`, is there a bounded state resource `F` such that the derivative occupancy is forced to debit `F` monotonically or appears in an exact dissipative ledger?

Without one of these two closure mechanisms, positive derivative occupancy is compatible with compact recurrence.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
