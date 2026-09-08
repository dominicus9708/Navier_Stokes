# DSD M17-437 — Material/spatial jet commutator gives own-time persistence of any fixed record-matched finite kappa jet under normalized high-jet compactness

Date: 2026-09-08  
Canonical ID: **M17-437**

Status: **ACTIVE SPACE-TIME JET PERSISTENCE THEOREM / HIGHER-ORDER ZERO-TRANSITION BRIDGE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Goal

M17-418 proves that any fixed finite record-matched spatial coefficient jet order

\[
r_p=|D^p\kappa|^{-1/(p+2)}\asymp r
\]

creates an own-scale spatial raw-`H2` packet.

M17-435 closes repeated first-order regular zero crossings when the zero geometry persists for a fixed fraction of one own-time.

The missing step for higher-order crossings is temporal persistence of the finite spatial jet.

The present module supplies that step under normalized high-jet compactness.

## 2. Material/spatial derivative commutator

Let

\[
D_t=\partial_t+u\cdot\nabla.
\]

For a scalar `f` and multi-index `alpha`, `|alpha|=p`,

\[
\partial^\alpha(u\cdot\nabla f)
=
\sum_{\beta\le\alpha}
{\alpha\choose\beta}
(\partial^\beta u)\cdot
\nabla\partial^{\alpha-\beta}f.
\]

Therefore

\[
\boxed{
[D_t,\partial^\alpha]f
:=D_t\partial^\alpha f-\partial^\alpha D_tf
=
-\sum_{0<\beta\le\alpha}
{\alpha\choose\beta}
(\partial^\beta u)\cdot
\nabla\partial^{\alpha-\beta}f.
}
\]

Applying this to `f=kappa`,

\[
\boxed{
D_t\partial^\alpha\kappa
=
\partial^\alpha D_t\kappa
-
\sum_{0<\beta\le\alpha}
{\alpha\choose\beta}
(\partial^\beta u)\cdot
\nabla\partial^{\alpha-\beta}\kappa.
}
\]

## 3. Exact own-scale homogeneity of the commutator

At spatial scale `r`, define normalized velocity and coefficient jets

\[
U_b:=r^{b+1}|D^bu|,
\qquad b\ge1,
\]

\[
K_q:=r^{q+2}|D^q\kappa|,
\qquad q\ge0.
\]

For one commutator term with `|beta|=b`,

\[
|D^bu|
\sim r^{-(b+1)}U_b,
\]

while

\[
|\nabla D^{p-b}\kappa|
\sim r^{-(p-b+3)}K_{p-b+1}.
\]

Thus every term has the same parabolic order

\[
r^{-(b+1)}r^{-(p-b+3)}
=r^{-(p+4)}.
\]

Hence

\[
\boxed{
r^{p+4}|[D_t,D^p]\kappa|
\le
C_p
\sum_{b=1}^{p}U_bK_{p-b+1}.
}
\]

There is no hidden worse scale in the material/spatial commutator.

## 4. Differentiate the exact coefficient constitutive law

M17-339 gives

\[
D_t\kappa
=
L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{geom},
\]

with

\[
L_\rho f
=
\Delta f+2\nabla\log\rho\cdot\nabla f.
\]

Taking `p` spatial derivatives gives

\[
D^pD_t\kappa
=
D^p\Delta\kappa
+2D^p(\nabla\log\rho\cdot\nabla\kappa)
+D^p\Delta\sigma
+2D^p(\nabla\log\rho\cdot\nabla\sigma)
+D^p\mathcal R_{geom}.
\]

The principal terms are

\[
D^{p+2}\kappa,
\qquad
D^{p+2}\sigma,
\]

and every product term has the same total own-scale order `r^{-(p+4)}` when written in dimensionless jets.

Thus there is a finite polynomial `P_p` such that

\[
\boxed{
r^{p+4}|D^pD_t\kappa|
\le
\mathcal P_p(\mathcal J_{p+2}),
}
\]

where `J_{p+2}` denotes the finite collection of normalized coefficient, velocity/strain, amplitude-logarithmic, vorticity, and direction jets needed through the derivative orders produced by `D^p R_geom`.

The exact list grows with `p`, but it is finite for each fixed `p`.

## 5. Master material p-jet speed bound

Combining Sections 2--4,

\[
\boxed{
r^{p+4}|D_tD^p\kappa|
\le
\mathcal Q_p(\mathcal J_{p+2}),
}
\]

for another finite polynomial `Q_p`.

Therefore, on a normalized state class satisfying

\[
\boxed{
\sup\mathcal J_{p+2}\le M_p<\infty,
}
\]

we obtain

\[
\boxed{
r^{p+4}|D_tD^p\kappa|
\le C_{p,M_p}<\infty.
}
\]

For `p=0`, this reduces to the M17-436 transition-speed principle.

## 6. Own-time persistence along a material trajectory

Let `X(a,t)` be the material flow and suppose at `t=t_0`

\[
\boxed{
|D^p\kappa(X(a,t_0),t_0)|
\ge
c_pr^{-(p+2)}.
}
\]

Along the material trajectory,

\[
\frac d{dt}
D^p\kappa(X(a,t),t)
=
D_tD^p\kappa(X(a,t),t).
\]

Hence

\[
\left|
D^p\kappa(X(a,t),t)
-D^p\kappa(X(a,t_0),t_0)
\right|
\le
C_{p,M_p}r^{-(p+4)}|t-t_0|.
\]

Choose

\[
\boxed{
\tau_p
:=
\frac{c_p}{2C_{p,M_p}}r^2.
}
\]

Then for

\[
|t-t_0|\le\tau_p
\]

inside the retained regular interval,

\[
\boxed{
|D^p\kappa(X(a,t),t)|
\ge
\frac{c_p}{2}r^{-(p+2)}.
}
\]

Thus any fixed record-matched finite `p`-jet persists for a fixed positive fraction of one own-time.

## 7. Lower-order-jet dichotomy during persistence

Suppose `p` is the first record-matched nonzero spatial coefficient jet at the central zero state at `t_0`.

During the own-time interval from Section 6, one of two things happens:

1. some lower order `q<p` becomes record-matched and nondegenerate;
2. all lower normalized jets remain below fixed small thresholds while the `p`-jet remains bounded below.

Case 1 is not a failure: it routes to the already lower-order zero-jet packet mechanism.

In Case 2, normalized Taylor expansion with bounded `(p+1)`-jet gives a fixed transverse own-scale subset on which

\[
\boxed{|\kappa|\gtrsim cr^{-2}.}
\]

The exact subset may avoid the algebraic nodal directions of the leading `p`-homogeneous polynomial, but it has a fixed positive normalized volume fraction determined by the compact jet margins.

Therefore either branch creates a fixed own-scale coefficient packet for a fixed fraction of one own-time.

## 8. Raw-H2 packet consequence

Exact CE-H gives

\[
|\Delta\Omega|^2
=\kappa^2\rho^2.
\]

With the retained amplitude floor and tube geometry, the own-scale coefficient subset from Section 7 yields

\[
\boxed{
h_{p,seg}^{norm}\ge h_p>0}
\]

for one normalized loop segment and a fixed positive fraction of one own-time.

Thus M17-418's spatial finite-jet packet is upgraded to a **space-time finite-jet packet** for every fixed `p` under normalized high-jet compactness.

## 9. What is not yet proved by this module

M17-437 is a fixed-order theorem.

It does not by itself prove that one uniform finite order `p` controls every transition across every record.

A sequence could in principle attempt to send the first nonzero transition jet order to infinity while the record changes.

Closing that possibility requires a compact normalized transition-state argument plus exclusion of analytic infinite-flat positive-flux transition states.

That is the next canonical step.

## 10. Exact surviving exits

Failure of the M17-437 persistence theorem for a fixed record-matched finite jet implies at least one of:

\[
\boxed{G_{normalized\ high\text{-}jet\ decompactification}},
\]

\[
\boxed{G_{jet\text{-}scale/record\text{-}scale\ mismatch}},
\]

\[
\boxed{G_{amplitude/nodal\ loss}},
\]

\[
\boxed{G_{tube/flow/interface/CEH/domain\ loss}}.
\]

Material/spatial commutation itself creates no additional scale defect.

## 11. DSD role

DSD is used only to insist that a spatial finite-jet descriptor be audited for temporal persistence before being counted repeatedly in space-time.

The mathematics is the exact material/spatial commutator, the M17-339 constitutive equation, parabolic scaling, and Taylor compactness.

## 12. Audit verdict

**PASS as a fixed-order higher-zero space-time persistence theorem.**

Every fixed record-matched finite coefficient jet survives for a fixed own-time fraction under normalized finite-jet compactness and therefore carries an order-one normalized raw-`H2` space-time packet.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
