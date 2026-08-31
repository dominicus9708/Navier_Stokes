# DSD M5-394 — Natural productive source forms a misaligned companion flux carrier

Date: 2026-08-31

Status: **M5-377 ONLY NEEDED POSITIVE SOURCE CAPACITY TO FORCE LOCAL PALINSTROPHY, BUT M5-392 STAGE-WIDE ANALYTICITY GIVES MORE / EVERY FIXED-FRACTION NATURAL PRODUCTIVE BIOT--SAVART SOURCE CONTAINS A FIXED NORMALIZED BALL ON WHICH VORTICITY HAS ORDER-ONE MAGNITUDE AND A FIXED ANGULAR SEPARATION FROM THE FIRST-HITTING CORE / A TRANSVERSE DISK IN THAT BALL THEREFORE CARRIES A FIXED SIGNED NORMALIZED FLUX, HENCE A PHYSICAL VORTICITY FLUX OF ORDER `W r^2 = nu` / THE LOCAL STRETCHING SOURCE IS THUS A FORMED MISALIGNED COMPANION FLUX CARRIER, NOT MERELY AN ABSTRACT POSITIVE-MEASURE OCCUPANCY SET / ITS LATER LOSS, CONTACT, REORIENTATION, OR EXPORT CAN BE FED INTO THE SAME MATERIAL-GENEALOGY LEDGER AS THE MAIN CARRIER / THIS SHARPENS THE LOCAL H FRONTIER BUT DOES NOT YET PRICE REPEATED DUAL-CARRIER RECURRENCE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-393 routes a persistent coherent material-flux funnel to the angular Biot--Savart source network of M5-362.

M5-376--377 then say that if a fixed fraction of the productive source remains at the natural scale, it has positive spatial capacity and forces local normalized palinstrophy occupancy.

M5-392 subsequently strengthened the smooth first-hitting setting by proving a uniform normalized analyticity radius and fixed-order derivative bounds throughout every late stage.

That analyticity upgrade should be propagated back into the natural-source statement.

The question is:

> Can a fixed-fraction natural productive source be upgraded from a positive-measure set to an actual coherent signed-flux packet?

The answer is yes.

---

## 2. Natural productive event from M5-377

At a first-hitting stretching event choose a spatial vorticity maximum `x_*`, amplitude

\[
W_*=\|\omega(t_*)\|_\infty,
\]

and natural scale

\[
r_*:=\sqrt{\frac{\nu}{W_*}}.
\]

Normalize by

\[
Y=\frac{x-x_*}{r_*},
\qquad
\Omega(Y)=\frac{\omega(x_*+r_*Y,t_*)}{W_*}.
\]

Then

\[
|\Omega|\le1,
\qquad
|\Omega(0)|=1.
\]

Let

\[
\xi_0:=\Omega(0).
\]

On the natural productive branch M5-377 selects a fixed annulus

\[
A=\{c_1\le|Y|\le c_2\}
\]

and a productive set

\[
E\subset A
\]

with

\[
|E|\ge m_0>0,
\]

such that for every `Y in E`

\[
\boxed{
|\Omega(Y)|\ge\lambda_0>0
}
\]

and

\[
\boxed{
|D(\widehat Y,\Xi(Y),\xi_0)|\ge\delta_0>0,
}
\]

where

\[
\Xi(Y)=\frac{\Omega(Y)}{|\Omega(Y)|}.
\]

Since

\[
|D|\le|\Xi(Y)\times\xi_0|,
\]

we have the angular separation

\[
\boxed{
|\Xi(Y)\times\xi_0|
\ge\delta_0.
}
\]

Thus every point of the productive set carries order-one normalized vorticity and is quantitatively misaligned with the central core direction.

---

## 3. M5-392 gives a global normalized Lipschitz bound

Stage-wide first-hitting analyticity gives, in the parent normalized variables,

\[
\boxed{
\|\nabla_Y\Omega\|_{L^\infty(\mathbb R^3)}
\le C_1
}
\]

with `C1` independent of the late stage index.

This is stronger than the continuity-radius split originally used in M5-377.

Choose any point

\[
Y_s\in E.
\]

Set

\[
e_s:=\Xi(Y_s).
\]

The goal is to construct a fixed normalized ball around `Y_s` on which both the amplitude and the angular mismatch remain quantitative.

---

## 4. Fixed source ball from analyticity

For

\[
|Y-Y_s|\le\rho,
\]

the normalized Lipschitz bound gives

\[
|\Omega(Y)-\Omega(Y_s)|
\le C_1\rho.
\]

Choose

\[
\rho_s
:=
\min\left\{
\frac{\lambda_0}{8C_1},
\frac{\lambda_0\delta_0}{32C_1},
\frac{c_1}{8},
1
\right\}.
\]

Then for every

\[
Y\in B_{\rho_s}(Y_s)
\]

we have

\[
|\Omega(Y)|
\ge
|\Omega(Y_s)|-C_1\rho_s
\ge
\frac{7}{8}\lambda_0.
\]

In particular the vorticity direction is defined throughout this ball.

For nonzero vectors `a,b`, the normalized-direction estimate

\[
\left|
\frac a{|a|}-\frac b{|b|}
\right|
\le
\frac{2|a-b|}{\min\{|a|,|b|\}}
\]

gives

\[
|\Xi(Y)-e_s|
\le
\frac{4C_1\rho_s}{\lambda_0}
\le
\frac{\delta_0}{8}.
\]

Therefore

\[
|\Xi(Y)\times\xi_0|
\ge
|e_s\times\xi_0|-|\Xi(Y)-e_s|
\ge
\frac{7}{8}\delta_0.
\]

Thus

\[
\boxed{
B_{\rho_s}(Y_s)
\text{ is a fixed normalized coherent misaligned vorticity packet.}
}
\]

The radius `rho_s` is independent of the late first-hitting stage.

---

## 5. Signed source disk and fixed normalized flux

Inside the source ball choose a flat disk

\[
D_s
\subset B_{\rho_s}(Y_s)
\]

of radius

\[
\rho_s/2
\]

whose unit normal is `e_s`.

For `Y in D_s`,

\[
\Omega(Y)\cdot e_s
\ge
\Omega(Y_s)\cdot e_s
-|\Omega(Y)-\Omega(Y_s)|.
\]

Since

\[
\Omega(Y_s)\cdot e_s
=|\Omega(Y_s)|
\ge\lambda_0,
\]

we obtain

\[
\Omega(Y)\cdot e_s
\ge
\frac78\lambda_0.
\]

Hence the normalized signed flux through `D_s` satisfies

\[
\boxed{
\Phi_s^{norm}
:=
\int_{D_s}\Omega\cdot e_s\,dA_Y
\ge
c_s
:=
\frac78\lambda_0\pi\left(\frac{\rho_s}{2}\right)^2
>0.
}
\]

This is a genuine directed flux, not merely an enstrophy or positive-volume statement.

---

## 6. Physical flux is scale invariant

The corresponding physical disk is

\[
D_s^{phys}
=x_*+r_*D_s.
\]

Its signed vorticity flux is

\[
\begin{aligned}
\Phi_s^{phys}
&=
\int_{D_s^{phys}}
\omega\cdot e_s\,dA_x\\
&=
W_*r_*^2
\int_{D_s}\Omega\cdot e_s\,dA_Y.
\end{aligned}
\]

Since

\[
W_*r_*^2=\nu,
\]

we get

\[
\boxed{
\Phi_s^{phys}
\ge
c_s\nu.
}
\]

Thus the natural productive source contains a second scale-invariant flux carrier of the same physical order as the central first-hitting Taylor carrier.

---

## 7. Spatial and angular separation from the main carrier

The source center lies in the fixed annulus

\[
c_1\le|Y_s|\le c_2.
\]

Therefore its physical distance from the first-hitting center is

\[
\boxed{
|x_s-x_*|
\asymp r_*.
}
\]

The source direction satisfies

\[
\boxed{
|e_s\times\xi_0|
\ge\delta_0.
}
\]

Hence the natural-source event contains two simultaneously formed flux objects:

1. the central Taylor carrier with direction `xi_0` and flux `~nu`;
2. a companion source carrier at distance `~r_*`, direction separated by a fixed angle, and flux `~nu`.

Symbolically,

\[
\boxed{
P_{\rm angular,natural}
\Longrightarrow
G_{\rm dual\,flux}^{formed}.
}
\]

This is stronger geometric information than the earlier local-Poincare occupancy conclusion, although it does not replace that conclusion.

---

## 8. Relation to the M5-377 palinstrophy bound

The two-carrier structure automatically contains two positive-volume vector states separated by a fixed amount inside a fixed normalized ball containing both carriers.

Therefore the vector Poincare argument of M5-377 still gives

\[
\boxed{
\int_{B_R}|\nabla_Y\Omega|^2dY
\ge c_P>0.
}
\]

The present note adds that the source side of that Poincare comparison is not merely a positive-measure irregular set.

It contains a fixed coherent flux disk.

Thus

\[
\boxed{
G_{\rm dual\,flux}^{formed}
\Longrightarrow
H_{\rm crit\,local\,occupancy}
}
\]

while also providing a material object that can be followed dynamically.

---

## 9. Assign material identity to the companion immediately

Because the flow is smooth at the event time, choose a short source cylinder around `D_s^{phys}` inside the coherent source ball and assign it a material identity by the exact flow map.

Denote this source carrier by

\[
B_j^0
\]

and its material image by

\[
B_j(t)=\Phi_{t_*,t}(B_j^0).
\]

The companion carrier therefore enters the same DSD material ledger as the main carrier.

At a later comparison time, only the following types of behavior are possible:

\[
\boxed{
\text{source-carrier contact/persistence}
\lor
\text{viscous flux change}
\lor
\text{projective reorganization}
\lor
\text{replacement}
\lor
\text{spatial export}.
}
\]

There is no need to keep the local productive source as an unformed cloud once it is natural-scale and first-hitting analyticity is available.

---

## 10. Apply the M5-393 material-flux distinction to the companion

M5-393 showed that positive material overlap must not be confused with persistent flux ancestry.

The same distinction applies to the companion source carrier.

If its later material image continues to represent a fixed fraction of a later productive source flux, it becomes a genuine material-flux lineage and pays the cross-sectional funnel/deformation action.

If not, then its flux identity is lost through

\[
\boxed{
H_{\rm viscous\ flux}
\lor
T_{\rm projective/replacement/export}.
}
\]

Thus natural source formation can be recursively fed into the same genealogy machinery rather than ending at a purely Eulerian capacity label.

---

## 11. This does not imply binary branching of material ancestry

A crucial M5-358 firewall remains in force.

The simultaneous existence of a main carrier and a source carrier at one stage does not imply that every later stage contains twice as many surviving descendants.

The two carriers may:

- merge later;
- exchange roles;
- be different segments of one connected material vortex structure;
- undergo replacement;
- export one branch;
- lose flux identity diffusively.

Therefore

\[
\boxed{
G_{\rm dual\,flux}^{formed}
\not\Longrightarrow
\text{exponential material tree width}.
}
\]

No branching contradiction is claimed.

---

## 12. Same connected vortex tube remains possible

The main and companion carriers are spatially separated by order `r_*` and their directions differ by a fixed angle.

They can nevertheless be two bent segments of the same connected vortex tube.

Stage-wide analyticity permits an order-one directional turn over an order-one normalized distance.

Thus one must not infer

\[
\text{misaligned companion}
\Rightarrow
\text{independent material tube}.
\]

If the two carriers are connected, the relevant future descriptor is a natural-scale bend/relative-axis network.

If they are materially distinct, the relevant descriptor is multi-carrier genealogy.

Both remain formed objects.

---

## 13. DSD formation analysis

### Previously

The productive natural source was represented as a positive-capacity set `E`.

### After M5-392 propagation

The source contains a fixed-radius coherent sub-ball and a fixed signed flux disk.

Thus the correct descriptor is

\[
\boxed{
\text{formed companion flux carrier}
}
\]

inside the larger productive source set.

### Kept distinct

- source carrier versus main maximum carrier;
- Eulerian spatial proximity versus material ancestry;
- angular misalignment versus topological disconnection;
- flux persistence versus volume persistence.

---

## 14. DSD axis-property analysis

The first-hitting stretching event now has an explicit relative-axis pair

\[
(\xi_0,e_s)
\]

with

\[
|e_s\times\xi_0|\ge\delta_0.
\]

The Biot--Savart stretching source is therefore not an abstract scalar strain.

It has a realized directional network at the natural scale.

The axis-property descriptor is

\[
\boxed{
\mathcal G_j
=
\left(
C_j^{main},
B_j^{source},
\xi_j,
e_j,
\operatorname{dist}\asymp r_j,
\Phi^{main}\asymp\nu,
\Phi^{source}\asymp\nu
\right).
}
\]

This object is suitable for later material-contact/replacement audits.

---

## 15. DSD audit firewall

### Valid

- positive source capacity comes from M5-377;
- fixed normalized gradient bound comes from M5-392;
- the fixed source ball follows by the mean-value estimate;
- direction is used only after the amplitude lower bound keeps vorticity away from zero;
- fixed physical flux follows from `W r^2 = nu`;
- material identity is assigned only after the coherent source packet has been formed.

### Forbidden

Do not infer that the source carrier persists to the next stage.

Do not infer that it is materially distinct from the main carrier.

Do not infer growing tree width from simultaneous two-carrier formation.

Do not add the energy of nested or repeatedly reused source carriers as independent mass.

Do not claim local critical occupancy is globally contradictory.

---

## 16. Sharpened local source frontier

On the natural-source branch feeding first-hitting longitudinal stretching,

\[
\boxed{
H_{\rm crit\,local\,source/occupancy}
\quad\text{can be represented by}\quad
G_{\rm dual\,flux}^{formed}.
}
\]

This does not eliminate every occurrence of the broader symbol

\[
H_{\rm crit\,mass/occupancy}
\]

elsewhere in the proof tree.

It specifically sharpens the local Biot--Savart source branch created by M5-362 and used in M5-393.

The corresponding funnel-source frontier becomes

\[
\boxed{
G_{\rm dual\,flux}^{formed}
\lor
H_{\rm remote\,relative-frequency/nonlocal\,strain}
\lor
T_{\rm replacement/export/projective}^{formed}.
}
\]

---

## 17. Next target

The next efficient question is whether a recurrent sequence of dual-flux source graphs can avoid one of the following:

1. repeated reuse of a bounded-age material source carrier;
2. fresh companion creation at positive frequency;
3. projective reorganization;
4. remote source export.

The existing finite-memory replacement machinery can potentially be lifted from a single carrier to the ordered pair

\[
(C_j^{main},B_j^{source}).
\]

The key audit will be to avoid the M5-358 error: positive-frequency source renewal does not by itself imply growing tree width or a nonsummable energy cost.

What is needed is a scale-invariant **source-flux replacement charge**, not a fragment count.

---

## 18. Audit verdict

### NEW FORMATION RESULT

\[
\boxed{
\text{fixed-fraction natural productive source}
\Longrightarrow
\text{fixed-radius coherent misaligned source ball}.
}
\]

### NEW FLUX RESULT

\[
\boxed{
\Phi_{source}^{phys}
\ge c_s\nu.
}
\]

### NEW STRUCTURAL OBJECT

\[
\boxed{
G_{\rm dual\,flux}^{formed}
=
\text{main first-hitting carrier}
+
\text{misaligned natural companion carrier}.
}
\]

### STILL OPEN

- recurrent genealogy of the companion source carrier;
- scale-invariant pricing of fresh source-carrier creation;
- remote/nonlocal strain closure;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
