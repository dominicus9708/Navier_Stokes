# DSD M5-617 — Generalized kappa-force lobes lift to nearby coherent vorticity packets

Date: 2026-09-03

Status: **NODAL/DERIVATIVE BRIDGE / THE GLOBAL GENERALIZED FORCE FROM M5-616 HAS THE EXACT WRONSKIAN FORM `F_j = W·partial_j Delta W - Delta W·partial_j W`, WHICH USES NO DIVISION BY `|W|` / A FIXED FORCE LOBE THEREFORE EITHER ALREADY HAS FIXED VORTICITY AMPLITUDE OR HAS A FIXED FIRST-DERIVATIVE LOWER BOUND / UNIFORM HIGHER-DERIVATIVE CAPS THEN TURN THE LATTER INTO A FIXED-AMPLITUDE VORTICITY POINT WITHIN A FIXED DISTANCE BY A FINITE-DIFFERENCE/TAYLOR ARGUMENT / SMOOTHNESS THICKENS THAT POINT INTO A COHERENT FIXED-FLUX PACKET / HENCE THE TWO SEPARATED GENERALIZED KAPPA-FORCE LOBES FORCE TWO SEPARATED ACTIVE VORTICITY SOURCE PACKETS UP TO CONTROLLED LOCAL OFFSETS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Global force formula without kappa

M5-616 defines

\[
\mathcal F_\kappa=-2\nabla\cdot\mathbb T,
\]

with

\[
\mathbb T_{ij}
=
\partial_iW\cdot\partial_jW
-
\frac12
\left(
|\nabla W|^2+W\cdot\Delta W
\right)\delta_{ij}.
\]

Expand one divergence:

\[
\partial_i\mathbb T_{ij}
=
\frac12
\left(
\Delta W\cdot\partial_jW
-
W\cdot\partial_j\Delta W
\right).
\]

Therefore

\[
\boxed{
(\mathcal F_\kappa)_j
=
W\cdot\partial_j\Delta W
-
\Delta W\cdot\partial_jW.
}
\]

On `W!=0` this agrees with `|W|^2 partial_j kappa`, but the Wronskian form is globally smooth and valid at nodal points.

---

## 2. Fixed force lobe

M5-616 extracts sign-opposed lobes with a fixed projected amplitude after compact smooth thickening.

Thus on each selected lobe there exists a point `x_*` and coordinate/component `j` with

\[
\boxed{
|F_j(x_*)|\ge f_*>0.
}
\]

Uniform compact smoothness gives

\[
\|\partial_j\Delta W\|_\infty\le M_3,
\qquad
\|\Delta W\|_\infty\le M_2,
\]

and uniform first/second derivative caps.

---

## 3. Direct active-vorticity case

If

\[
|W(x_*)|
\ge
\frac{f_*}{4M_3}
=:w_1>0,
\]

then the lobe already contains a fixed-amplitude vorticity point.

The `C1` bound thickens it to a fixed ball with

\[
|W|\ge w_1/2
\]

and, after a further fixed shrinking, one angular sector.

This is directly a coherent fixed-flux packet.

---

## 4. Derivative-dominated case

Suppose instead

\[
|W(x_*)|<w_1.
\]

Then

\[
|W\cdot\partial_j\Delta W|
\le f_*/4.
\]

Since

\[
|F_j|
=
|W\cdot\partial_j\Delta W
-
\Delta W\cdot\partial_jW|
\ge f_*,
\]

we obtain

\[
|\Delta W\cdot\partial_jW|
\ge 3f_*/4.
\]

Using `|Delta W|<=M_2`,

\[
\boxed{
|\partial_jW(x_*)|
\ge
c_1:=\frac{3f_*}{4M_2}>0.
}
\]

Thus a derivative/nodal force lobe has a fixed first-derivative floor.

---

## 5. Finite-difference extraction of nearby vorticity amplitude

Let

\[
e_j
\]

be the corresponding coordinate direction.

Taylor expansion gives

\[
W(x_*+he_j)
=
W(x_*)+h\partial_jW(x_*)+O(M_{2,\infty}h^2).
\]

Apply the same formula at `-h` and subtract:

\[
W(x_*+he_j)-W(x_*-he_j)
=2h\partial_jW(x_*)+O(M_{3?}h^3)
\]

or use the one-sided estimate with a fixed higher-derivative cap.

Choose a universal small

\[
0<h_0\le h_*
\]

depending only on `c1` and the compact second-derivative bound so that the Taylor error is at most a fixed fraction of `h_0 c1`.

Then at least one of

\[
x_*+h_0e_j,
\qquad
x_*-h_0e_j
\]

satisfies

\[
\boxed{
|W|\ge w_2>0.
}
\]

Thus fixed force amplitude cannot remain confined to an arbitrarily low-vorticity nodal region.

---

## 6. Coherent packet thickening

At the nearby active point, use the uniform `C1` cap on `W` to obtain a fixed radius `r_W>0` with

\[
|W|\ge w_2/2
\]

on a small ball.

After shrinking by the direction-continuity scale, `W/|W|` lies in one fixed cone.

A cross-sectional disk then carries

\[
\boxed{
|\Phi_{packet}|\ge\phi_W>0.
}
\]

Hence every fixed generalized-force lobe lifts to a coherent fixed-flux vorticity packet within a uniformly bounded offset.

---

## 7. Preserve two-lobe separation

M5-616 gives a barycentric separation

\[
d_F>0
\]

between positive and negative force populations.

Choose the finite-difference radius in the derivative branch no larger than a fixed fraction of `d_F` whenever needed; reducing `h_0` only reduces the extracted amplitude by a fixed factor and does not destroy positivity.

After the subsequent coherent-ball shrinking, the two packets can still be selected with a definite separation

\[
\boxed{d_W>0.}
\]

Thus the generalized force dipole yields a genuine two-center active vorticity architecture.

---

## 8. Genealogical consequence

Each extracted packet has

1. fixed normalized amplitude;
2. fixed spatial scale;
3. fixed directed vorticity flux;
4. a fixed separation from the opposite force-lobe packet.

Therefore each packet may be inserted into the finite-memory material-flux genealogy.

Repeated force-dipole events must eventually be represented by the finite persistent lineage/satellite network or pay replacement/viscous-flux turnover.

---

## 9. Relation to the earlier dual geometry

The CE-H hard core now carries two independently forced dual architectures:

1. M5-455/M5-490 production-induced noncollinear dual-flux lineages;
2. M5-615--617 zero-net-force/positive-virial kappa-force dipole packets.

They are not yet proved to be the same pair.

The next high-value target is a finite-pigeonhole overlap theorem: because both architectures recur in one finite saturated fixed-flux network, determine whether one fixed ordered pair of persistent lineages must carry both the production-dual mark and the kappa-force-dipole mark at positive frequency, or else force additional replacement/turnover.

---

## 10. Firewall

The sign of the generalized force lobe is not automatically the sign of `kappa` itself, especially near the nodal set.

M5-617 extracts active packets from force geometry but does not assign them a negative/positive kappa value without a separate active-set check.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
