# DSD M5-675 — Positive-middle-strain packet forces a bounded-distance coherent vorticity source

Date: 2026-09-03

Status: **INTERNAL BIOT-SAVART SOURCE EXTRACTION / THE M5-674 POSITIVE-MIDDLE-STRAIN PAYER CANNOT BE A SOURCE-FREE LOW-VORTICITY STRAIN GHOST: THE WHOLE-SPACE STRAIN KERNEL, ITS PRINCIPAL-VALUE CANCELLATION, THE UNIFORM `C^1` VORTICITY CAP, AND FINITE ENSTROPHY IMPLY THAT EVERY FIXED ORDER-ONE STRAIN POINT HAS A FIXED-AMPLITUDE VORTICITY SOURCE WITHIN A FIXED DISTANCE / SMOOTH THICKENING THEN PRODUCES A COHERENT FIXED-FLUX SOURCE PACKET / THE SOURCE NEED NOT BE THE SAME MATERIAL LINEAGE AS THE STRAIN PAYER, SO THIS IS A COUPLING/ATTRIBUTION RESULT RATHER THAN A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-674

M5-674 yields a positive-frequency family of finite-core regions where

\[
\boxed{\lambda_2\ge\lambda_{2,*}>0}
\]

and

\[
\boxed{|\Sigma|\ge s_*>0.}
\]

Choose one point `x` in such a strain payer region.

The question is whether this order-one strain can be sustained while all nearby vorticity amplitudes are arbitrarily small.

---

## 2. Whole-space strain kernel

For divergence-free velocity, the strain is a Calderon--Zygmund transform of vorticity:

\[
\boxed{
\Sigma(x)
=
\operatorname{p.v.}
\int_{\mathbb R^3}K(x-y)W(y)dy,
}
\]

where the matrix kernel is homogeneous of degree `-3`, smooth away from the origin, and has zero spherical mean.

Thus

\[
|K(z)|\le C|z|^{-3}.
\]

The zero-mean property permits subtraction of `W(x)` in the near principal-value part.

---

## 3. Near / intermediate / far decomposition

Fix radii

\[
0<\delta<1<R.
\]

Write

\[
\Sigma=I_{near}+I_{mid}+I_{far}
\]

according to

\[
|x-y|<\delta,
\qquad
\delta<|x-y|<R,
\qquad
|x-y|>R.
\]

The all-order compact hull gives

\[
\boxed{\|\nabla W\|_\infty\le M_1.}
\]

---

## 4. Near field

By principal-value cancellation,

\[
I_{near}
=
\operatorname{p.v.}
\int_{|z|<\delta}K(z)[W(x-z)-W(x)]dz.
\]

Hence

\[
|I_{near}|
\le
CM_1
\int_0^\delta r^{-3}r\,r^2dr
\le
CM_1\delta.
\]

Thus

\[
\boxed{|I_{near}|\le C M_1\delta.}
\]

---

## 5. Intermediate field under a small-amplitude hypothesis

Suppose temporarily that

\[
\sup_{B_R(x)}|W|\le\varepsilon.
\]

Then

\[
|I_{mid}|
\le
C\varepsilon
\int_\delta^R r^{-3}r^2dr
\le
C\varepsilon\log\frac{R}{\delta}.
\]

Hence

\[
\boxed{
|I_{mid}|
\le
C\varepsilon\log(R/\delta).
}
\]

---

## 6. Far field

Use Cauchy--Schwarz and the enstrophy cap

\[
\|W\|_2^2=E\le Z_*.
\]

Since

\[
\int_{|z|>R}|K(z)|^2dz
\le
C\int_R^\infty r^{-6}r^2dr
\le
CR^{-3},
\]

we obtain

\[
\boxed{
|I_{far}|
\le
C Z_*^{1/2}R^{-3/2}.
}
\]

This estimate does not even require the stronger tail-tightness results.

---

## 7. Fixed source-amplitude extraction

At the selected payer point,

\[
|\Sigma(x)|\ge s_*.
\]

Choose `delta_*` depending only on `s_*` and `M_1` so that

\[
CM_1\delta_*
\le\frac14s_*.
\]

Next choose `R_*` depending only on `s_*` and `Z_*` so that

\[
C Z_*^{1/2}R_*^{-3/2}
\le\frac14s_*.
\]

Finally define

\[
\boxed{
 w_*:=
\frac{s_*}{4C\log(R_*/\delta_*)}>0.
}
\]

If

\[
\sup_{B_{R_*}(x)}|W|<w_*,
\]

then all three pieces together give

\[
|\Sigma(x)|<\frac34s_*,
\]

contradicting the payer lower bound.

Therefore

\[
\boxed{
|\Sigma(x)|\ge s_*
\Longrightarrow
\sup_{B_{R_*}(x)}|W|\ge w_*.
}
\]

All constants are uniform over the compact hard hull.

---

## 8. Coherent vorticity packet

Choose `y_* in B_{R_*}(x)` with

\[
|W(y_*)|\ge w_*.
\]

The uniform gradient bound gives a fixed radius `r_*>0` such that

\[
\boxed{
|W(y)|\ge\frac12w_*
\quad\text{on }B_{r_*}(y_*).
}
\]

After reducing `r_*` further, the direction field is coherent on the ball because `rho>=w_*/2` and the compact hull controls derivatives.

A transverse disk then carries a fixed directed vorticity flux

\[
\boxed{|\Phi_{src}|\ge\phi_{src}>0.}
\]

Thus every positive-middle-strain payer event has a bounded-distance coherent fixed-flux vorticity source packet.

---

## 9. Finite-core localization

The M5-674 strain payer lies in a fixed active core.

Because `R_*` is fixed, the extracted source lies in a slightly enlarged but still fixed bounded core.

Therefore spectator-tail vorticity cannot be the source of the mandatory positive-middle-strain population.

---

## 10. Genealogical consequence

Positive-middle-strain events occur with positive frequency.

At every such event there is a fixed-flux coherent source packet.

Finite-memory saturation therefore gives the usual split:

\[
\boxed{
\text{persistent source lineage}
\lor
\text{positive-rate source replacement/turnover}.
}
\]

If persistent, M5-657 applies to that source lineage and forces a same-component strongly-negative `kappa` payer.

If replaced, the event joins the already retained material/flux turnover mechanisms.

Thus the positive-middle-strain payer is now tied back to the finite vorticity genealogy.

---

## 11. Firewall

The result does **not** prove that the vorticity source packet is spatially coincident with the positive-middle-strain region.

Nor does it prove that the source packet is the same lineage as the high-vorticity maximum or production payer.

Strain is nonlocal, so bounded-distance attribution is the correct conclusion.

No contradiction follows from source extraction alone.

---

## 12. Updated frontier

Every hard CE-H survivor now contains a recurrent finite network in which:

1. persistent high-vorticity lineages require strongly-negative same-component `kappa` payers;
2. positive enstrophy production requires positive middle strain;
3. every positive-middle-strain packet requires a bounded-distance coherent fixed-flux vorticity source;
4. every such source is persistent or repeatedly replaced.

The next useful step is to test whether a **persistent middle-strain source lineage** can satisfy its own M5-657 negative-`kappa` payer and the M5-671 spectral-gap identity without forcing a recursive expansion of distinct coherent packets beyond the finite-lineage saturation bound.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
