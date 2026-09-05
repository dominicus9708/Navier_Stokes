# DSD M17-190 — A positive-flux family of compact high-amplitude recurrent winding loops forces the M5-688 strain-gradient payer

Date: 2026-09-06  
Canonical ID: **M17-190**

Status: **STRAIN-GRADIENT PAYER CLOSURE OF ONE SUBBRANCH / M17-188 SHOWS THAT A SAME-MATERIAL CLOSED WINDING LOOP WITH RECURRENT COMPARABLE LENGTH, LINE WEIGHT, AND MATERIAL FLUX MUST CARRY A TIME-AVERAGED `3/4` STRAIN-AMPLITUDE COVARIANCE AND HENCE POSITIVE TANGENTIAL `grad sigma`/`grad rho` PRODUCT. ON A COMPACT HIGH-AMPLITUDE LOOP FAMILY, `rho` HAS A UNIFORM POSITIVE FLOOR AND `partial_s rho` HAS A UNIFORM UPPER BOUND, SO THE PRODUCT LOWER BOUND FORCES A UNIFORM POSITIVE TIME-AVERAGED `int |partial_s sigma|^2 ds`. IF SUCH LOOPS CARRY A FIXED POSITIVE TRANSVERSE FLUX MASS, GREAT-CIRCLE FLUX COORDINATES CONVERT THIS DIRECTLY INTO A POSITIVE LOWER BOUND FOR THE M5-688 EXPONENTIALLY WEIGHTED STRAIN-GRADIENT CHARGE `D_sigma`. THUS THIS SUBBRANCH DOES NOT EVADE THE M5-688 PAYER DICHOTOMY; IT LANDS IN THE STRAIN-GRADIENT PAYER CASE. THIS IS STILL A RECURRENT OCCUPANCY, NOT A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Closed-loop family assumptions

Let `A(theta)` be a measurable family of material closed great-circle vortex loops in the retained regular Rank-1 ensemble.

Assume the family carries a fixed positive current transverse-flux mass

\[
\boxed{
\int_{\mathcal A(\theta)}d\Phi\ge\Phi_*>0
}
\]

on the recurrent time set under consideration.

Assume uniform compact loop bounds

\[
0<\ell_*\le\ell_\Gamma\le\ell^*,
\]

\[
0<L_*\le L_\rho\le L^*<\infty,
\]

and a high-amplitude floor

\[
\boxed{\rho\ge a_*>0}
\]

on the loops.

Also assume the compact hard hull gives

\[
|\kappa|\le K_*
\]

and a uniform pointwise first-derivative bound for `rho` on these loops.

If any of these conditions fails, that is the corresponding thin/threshold/noncompact loop exit rather than the subbranch treated here.

---

## 2. Input from M17-188

For each same-material recurrent loop, M17-188 gives

\[
\left\langle
\bar\sigma_\rho-\bar\sigma_{ds}
\right\rangle
=\frac34.
\]

It also gives

\[
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le
C_*
\|\partial_s\sigma\|_{L^2(ds)}
\|\partial_s\rho\|_{L^2(ds)},
\]

where `C_*` depends only on the uniform loop geometry.

---

## 3. Uniform amplitude-gradient upper bound

Compact fixed-order regularity and the uniform length bound imply

\[
\boxed{
\|\partial_s\rho\|_{L^2(ds)}
\le M_\rho<\infty
}
\]

uniformly on the family.

Therefore

\[
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le C_*M_\rho
\|\partial_s\sigma\|_2.
\]

Take the recurrent time average and use the exact `3/4` mean:

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_2
\right\rangle
\ge
\frac{3}{4C_*M_\rho}
=:c_1>0.
}
\]

By Jensen/Cauchy,

\[
\boxed{
\left\langle
\int_\Gamma|\partial_s\sigma|^2ds
\right\rangle
\ge c_1^2
=:c_\sigma>0.
}
\]

Thus the strain-gradient occupancy itself, not merely the product with the amplitude gradient, is forced on this compact high-amplitude subbranch.

---

## 4. Convert to the spatial M5-688 charge

M5-688 uses

\[
D_\sigma
:=\left\langle
\int
\chi(\rho)\rho^2e^{2\kappa}|\nabla\sigma|^2dy
\right\rangle.
\]

On the family in Section 1 choose the fixed high-amplitude cutoff so that

\[
\chi=1.
\]

Great-circle vortex-flow coordinates give

\[
dy=\frac{d\Phi\,ds}{\rho}.
\]

Therefore the contribution of the loop family is

\[
\int_{\mathcal A}
\int_\Gamma
\rho e^{2\kappa}|\nabla\sigma|^2ds\,d\Phi.
\]

Use

\[
\rho\ge a_*,
\qquad
e^{2\kappa}\ge e^{-2K_*},
\qquad
|\nabla\sigma|^2\ge|\partial_s\sigma|^2.
\]

Hence

\[
D_\sigma
\ge
e^{-2K_*}a_*
\left\langle
\int_{\mathcal A}
\int_\Gamma|\partial_s\sigma|^2ds\,d\Phi
\right\rangle.
\]

If the recurrent family carries the fixed positive flux mass `Phi_*` and the M17-188 recurrence condition holds uniformly on that family, the lower bound in Section 3 yields

\[
\boxed{
D_\sigma
\ge
e^{-2K_*}a_*\Phi_*c_\sigma
=:d_\sigma^{loop}>0.
}
\]

---

## 5. Relation to M5-688

M5-688 already gives a payer dichotomy in which one branch is a fixed positive strain-gradient charge.

The present module shows that a positive-flux population of same-material compact high-amplitude recurrent winding loops **automatically belongs to that branch**.

Thus

\[
\boxed{
R_{1}^{closed\ winding,
 same\ material,
 compact,
 high\ amplitude,
 positive\ flux}
\Longrightarrow
D_\sigma\ge d_\sigma^{loop}>0.
}
\]

It cannot evade the multiplier-diffusion payment by declaring the strain-residence channel geometrically quiet.

---

## 6. Why this is not a contradiction

A compact smooth recurrent state may carry a permanently positive fixed-order strain-gradient norm.

No monotone global functional has yet been shown to decrease by `d_sigma^(loop)` per recurrence cycle.

Thus the result identifies the actual payer but does not exhaust it.

To close this branch one would need either

1. a finite spacetime budget for repeated aligned-strain-gradient occupancy;
2. an independent transport theorem preventing reuse of the same gradient architecture;
3. a relation forcing `D_sigma` to exceed an already finite critical budget.

None is presently established.

---

## 7. Exit branches

If the uniform argument fails, at least one of the following occurs:

\[
\boxed{
\rho_{min}\to0,
\quad
L_\rho\to0\text{ or }\infty,
\quad
\ell_\Gamma\to0\text{ or }\infty,
\quad
\|\partial_s\rho\|_2\to\infty,
\quad
\Phi(\mathcal A)\to0,
}
\]

or same-material loop recurrence itself fails.

These are explicit thin/noncompact/turnover branches rather than hidden failures.

---

## 8. DSD audit

### Audit A — using a pointwise amplitude floor on an arbitrary M5 flow-box segment
The theorem is restricted to closed loops that remain uniformly high-amplitude. Partial high-amplitude segments are a separate threshold-current branch.

### Audit B — claiming `D_sigma>0` is dissipative loss
Rejected. It is a spatial fixed-order charge.

### Audit C — ensemble versus same-label recurrence
The same-material recurrence assumption is explicit.

### Audit D — proof status
One regular Rank-1 subbranch is routed to a precise M5-688 payer, not closed globally.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
