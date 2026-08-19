# Near-max-mid defect reorganization -> derivative/visibility — 2026-08-20

Status: **ACTIVE REDUCTION NOTE — LOCAL FUNCTIONAL INEQUALITY PROVED; GLOBAL SUMMABILITY STILL OPEN.**

This note continues `RIGIDITY_KERNEL_INVARIANT_2026-08-20.md` and shows that the gauge-invariant near-max-mid defect cannot reorganize independently of the ordinary strain derivative hierarchy.

---

## 1. Near-max-mid decomposition

On the positive-middle sector write

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\]

and assume the near-max-mid regime

\[
\boxed{0\le d/m<1/3.}
\]

Let `P_-` be the rank-one spectral projector onto the compressive eigenspace `s_1=-2m`.

Define

\[
S_{mm}=m(I-3P_-)
\]

and the gauge-invariant max-mid defect tensor

\[
\boxed{D=S-S_{mm}.}
\]

Then

\[
|D|^2=2d^2.
\]

The previous invariant rigidity calculation yielded, for a fixed near-max-mid window,

\[
\boxed{
\|m\|_9^3
\lesssim
\int m|\nabla D|^2
+
\|\Delta S\|_2\,\|P_{st}Q\|_2,
}
\]

where

\[
Q=\frac13S^2+\frac14\omega\otimes\omega.
\]

---

## 2. The compressive eigenspace is uniformly isolated

In the regime `d/m<1/3`,

\[
s_2-s_1=3m-d>\frac83m,
\]

and

\[
s_3-s_1=3m+d>3m.
\]

Thus the compressive eigenvalue has a uniform relative spectral gap

\[
\boxed{
\operatorname{gap}_-
:=\min\{s_2-s_1,s_3-s_1\}
>\frac83m.
}
\]

Consequently the spectral projector `P_-` is differentiable wherever `S` is differentiable and obeys the standard projector derivative estimate

\[
\boxed{
|\nabla P_-|
\lesssim
\frac{|\nabla S|}{m}.
}
\]

This estimate is projective/sign-free; no choice of eigenvector orientation is required.

---

## 3. The defect derivative is controlled by the ordinary strain derivative

Differentiate

\[
D=S-mI+3mP_-.
\]

Then

\[
\nabla D
=
\nabla S
-(\nabla m)I
+3(\nabla m)P_-
+3m\nabla P_-.
\]

Since

\[
m=-s_1/2,
\]

the eigenvalue Lipschitz bound gives

\[
|\nabla m|\lesssim|\nabla S|.
\]

Together with the projector estimate,

\[
\boxed{
|\nabla D|
\lesssim
|\nabla S|.
}
\]

Thus the apparent `P_defect` channel is not a derivative-free hidden degree of freedom.

---

## 4. Weighted defect action is controlled by the H^1/H^2 hierarchy

Because

\[
|S|^2=6m^2+2d^2\ge6m^2,
\]

one has

\[
m\le |S|/\sqrt6.
\]

Therefore

\[
\int m|\nabla D|^2
\lesssim
\int |S||\nabla S|^2.
\]

Use Holder with exponents `6` and `12/5`:

\[
\int |S||\nabla S|^2
\le
\|S\|_6\,\|\nabla S\|_{12/5}^2.
\]

Sobolev gives

\[
\|S\|_6\lesssim\|\nabla S\|_2.
\]

Interpolating `L^(12/5)` between `L^2` and `L^6` for `nabla S`,

\[
\|\nabla S\|_{12/5}
\lesssim
\|\nabla S\|_2^{3/4}
\|\nabla S\|_6^{1/4}
\lesssim
\|\nabla S\|_2^{3/4}
\|\Delta S\|_2^{1/4}.
\]

Hence

\[
\boxed{
\int m|\nabla D|^2
\lesssim
\|\nabla S\|_2^{5/2}
\|\Delta S\|_2^{1/2}.
}
\]

Let

\[
P=\|\nabla S\|_2^2,
\qquad
H=\|\Delta S\|_2^2.
\]

Then

\[
\boxed{
\int m|\nabla D|^2
\lesssim
P^{5/4}H^{1/4}.
}
\]

---

## 5. Strengthened near-max-mid rigidity inequality

Insert the derivative bound into the previous invariant inequality:

\[
\boxed{
\|m\|_9^3
\lesssim
P^{5/4}H^{1/4}
+
H^{1/2}\|P_{st}Q\|_2.
}
\]

All terms have the same Navier--Stokes scaling, so this is a scale-consistent inequality.

If the projection-visible term is perturbative in the sense that

\[
H^{1/2}\|P_{st}Q\|_2
\le
\varepsilon\|m\|_9^3
\]

with sufficiently small universal `epsilon`, then

\[
\|m\|_9^3
\lesssim
P^{5/4}H^{1/4}.
\]

Therefore

\[
\boxed{
H
\gtrsim
\frac{\|m\|_9^{12}}{P^5}.
}
\]

Thus a nontrivial near-max-mid core with small projection visibility must pay a quantitative higher-derivative cost.

---

## 6. Routing of the P_defect branch

The previous local tree contained an apparently separate

\[
P_{defect}^*
\]

channel measured by

\[
\int m|\nabla D|^2.
\]

The present estimate shows that this action is already contained in the standard strain derivative hierarchy. Therefore:

- if `P_st Q` is small, nontrivial defect action forces `H`;
- if `P_st Q` is not small, the quadratic stress is projection-visible and returns to the full-NS projective residual channel `P_V` (or derivative-expensive advection cancellation).

Hence

\[
\boxed{
P_{defect}^*
\Longrightarrow
H\lor P_V^*.
}
\]

`P_defect` is therefore no longer an independent final survivor.

---

## 7. Updated local endgame

Combined with `LOCAL_CONSTANT_MIDDLE_AXIS_2026-08-20.md`, which routes the fixed-gap nonsaturated `M` branch to `H/T`, the local tree becomes

\[
\boxed{
H
\lor
T_{bounded}
\lor
P_V^*.
}
\]

Thus all currently isolated positive-middle-strain geometric subbranches have been absorbed into derivative action, bounded-radius turnover, or the genuinely full-Navier--Stokes projective residual.

The remaining non-H/non-T target is now

\[
\boxed{
P_V^*:
\text{repeated vorticity--strain/projective residual action.}
}
\]

---

## 8. Next target

Return to the exact strain-shape equation

\[
\|S\|_2\partial_t\Psi
=
\nu P_{\Psi^\perp}\Delta S
-\frac23P_{\Psi^\perp}P_{st}(S^2)
-\mathcal R_{NS}
\]

and isolate the genuinely vorticity-dependent part of `mathcal R_NS` after the derivative-expensive advection cancellation route is removed.

The next useful object should be a projective action functional measuring the angle between

\[
P_{st}(S^2)
\quad\text{and}\quad
P_{st}(\omega\otimes\omega),
\]

or equivalently the vorticity-dependent part of the orthogonal strain-shape velocity. The goal is to show that infinitely repeated `P_V` motion either creates vorticity-direction derivative action (`H_xi`) or requires bounded-radius material replacement (`T`).

Status: **P_DEFECT ABSORBED INTO H OR PROJECTION-VISIBLE FULL-NS ACTION; LOCAL ENDGAME = H / T / P_V.**