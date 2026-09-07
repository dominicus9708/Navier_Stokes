# DSD M17-315 — M17-147 full-gradient equation survives, but becomes a transverse `kappa`-geometry convexity gate rather than a fold-driver theorem

Date: 2026-09-07  
Canonical ID: **M17-315**

Status: **DOWNSTREAM REPAIR AFTER M17-313 / M17-147 DERIVES AN EXACT FULL-GRADIENT MATERIAL PDE FOR `G=grad kappa`. THAT PDE DOES NOT DEPEND ON `D_xi kappa` BEING NONZERO AND THEREFORE SURVIVES THE M17-313 CORRECTION. WHAT FAILS IS ONLY ITS FOLD INTERPRETATION: EXACT CE-H GIVES `G dot xi=0`, SO `G` IS PURELY TRANSVERSE AND CANNOT SERVE AS M17-144'S LONGITUDINAL FOLD DRIVER. THE QUIET BOCHNER/MAXIMUM-PRINCIPLE ARGUMENT CAN BE SHARPENED ACCORDINGLY. AT AN INTERIOR MAXIMUM OF `|G|`, ONLY THE LARGEST EIGENVALUE OF `Hess(log rho)` RESTRICTED TO `xi^perp` MATTERS. IF THAT TRANSVERSE EIGENVALUE STAYS BELOW `3/4-delta`, ORDER-ONE FULL `kappa` GRADIENT CANNOT BE MAINTAINED/REGENERATED IN THE QUIET CONTROLLED CORRIDOR. THUS M17-147 IS RETAINED AS A TRANSVERSE COEFFICIENT-GEOMETRY RIGIDITY GATE, NOT AS A GENERIC-FOLD GATE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact full-gradient equation retained

M17-147 defines

\[
\boxed{G:=\nabla\kappa}
\]

and, differentiating the M5-682 constitutive law, obtains the exact active-set equation

\[
\boxed{
D_BG
=
L_\rho G
+\left[2\nabla^2\psi-(\nabla B)^T-I\right]G
+\mathcal F_G,
}
\]

where

\[
\psi:=\log\rho
\]

and

\[
\mathcal F_G
=
\nabla L_\rho\sigma
+\nabla\mathcal R_{geom}.
\]

This derivation is independent of whether one component of `G` vanishes.

Therefore M17-313 does **not** retract the full-gradient PDE.

---

## 2. Insert the exact CE-H orthogonality

M17-313 proves

\[
\boxed{D_\xi\kappa=0.}
\]

Hence

\[
\boxed{G\cdot\xi=0.}
\]

Thus every surviving coefficient gradient lies in the two-dimensional plane

\[
\boxed{\xi^\perp.}
\]

The old longitudinal component

\[
K_\xi=\xi\cdot G
\]

is identically zero.

---

## 3. Quiet reduced full-gradient equation

Under the same quiet low-amplitude high-jet assumptions used in M17-147,

\[
(\nabla B)^T
=\frac12I+o(1)
\]

and

\[
\mathcal F_G=o(1).
\]

Therefore

\[
\boxed{
D_BG
=
L_\rho G
+\left(2\nabla^2\psi-\frac32I\right)G
+o(1).
}
\]

This leading equation remains valid for the transverse `G`.

---

## 4. Bochner identity retained

M17-147 gives

\[
\boxed{
\begin{aligned}
D_B\frac{|G|^2}{2}
={}&
\frac12L_\rho|G|^2
-|\nabla G|^2\\
&+2G\cdot(\nabla^2\psi)G
-\frac32|G|^2
+o(|G|^2+|G|).
\end{aligned}
}
\]

At an interior spatial maximum of `|G|^2`,

\[
L_\rho|G|^2\le0.
\]

The only positive leading quadratic term is the Hessian contribution.

---

## 5. Transverse Hessian eigenvalue

Because

\[
G\perp\xi,
\]

define the transverse largest eigenvalue

\[
\boxed{
\lambda_\perp(\psi)
:=
\max_{v\perp\xi,\ |v|=1}
 v\cdot(\nabla^2\psi)v.
}
\]

Then

\[
\boxed{
G\cdot(\nabla^2\psi)G
\le
\lambda_\perp(\psi)|G|^2.
}
\]

This is sharper than the unrestricted `lambda_max` used in the original fold interpretation of M17-147.

---

## 6. Correct `3/4` transverse convexity gate

At an interior positive maximum,

\[
D_B\frac{|G|^2}{2}
\le
\left(2\lambda_\perp(\psi)-\frac32\right)|G|^2
+o(1).
\]

Therefore, if for some fixed `delta>0`,

\[
\boxed{
\lambda_\perp(\log\rho)
\le
\frac34-\delta
}
\]

through a controlled quiet corridor, then sufficiently far out in the remote sequence

\[
\boxed{
D_B|G|^2
\le
-4\delta|G|^2+o(1)
}
\]

at every positive interior maximum.

Hence order-one transverse `kappa` gradient cannot be recurrently regenerated in that corridor without boundary import or failure of the quiet hard-hull assumptions.

---

## 7. Correct interpretation

The valid implication is now

\[
\boxed{
\text{recurrent order-one transverse }|\nabla\kappa|
\Longrightarrow
\lambda_\perp(\nabla^2\log\rho)
\ge
\frac34-o(1)
}
\]

somewhere in the required controlled genealogy, unless

\[
G_{boundary/import}
\lor
G_{high\ jet/noncompact}
\lor
G_{nodal/interface}.
\]

It is **not** a generic-fold requirement.

---

## 8. Relation to M5-687 and M17-234/235

M5-687 forces nonzero full `kappa`-gradient diffusion on the compact CE-H hull.

M17-234/235 force critical/full `kappa`-gradient activity on remote intrinsic packets.

M17-313 now says that all of this activity is transverse:

\[
\boxed{
\nabla\kappa
=P_{\xi^\perp}\nabla\kappa.
}
\]

M17-315 gives a corresponding necessary normalized geometry for sustaining that transverse activity:

\[
\boxed{
\lambda_\perp(\nabla^2\log\rho)
\gtrsim\frac34.
}
\]

Thus the surviving coefficient problem is effectively a two-dimensional cross-vortex geometry problem at the level of the principal multiplier gradient.

---

## 9. Downstream audit rule

Any later module using M17-147 should be separated into two classes.

### Retain

Arguments using only

1. the exact full-gradient PDE;
2. full `|grad kappa|` magnitude;
3. Bochner diffusion;
4. log-amplitude Hessian geometry;
5. transverse/nodal coefficient structure.

### Supersede or rewrite

Arguments whose conclusion requires

\[
|D_\xi\kappa|\gtrsim1
\]

or identifies an order-one full gradient specifically with a longitudinal generic-fold driver.

---

## 10. DSD audit

- The exact full-gradient PDE is preserved rather than discarded with the invalid component interpretation.
- `G dot xi=0` is inserted before the Hessian estimate.
- The unrestricted largest Hessian eigenvalue is sharpened to the transverse largest eigenvalue.
- No generic-fold lower bound is inferred from `|G|`.
- Full transverse coefficient-gradient channels remain active.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
