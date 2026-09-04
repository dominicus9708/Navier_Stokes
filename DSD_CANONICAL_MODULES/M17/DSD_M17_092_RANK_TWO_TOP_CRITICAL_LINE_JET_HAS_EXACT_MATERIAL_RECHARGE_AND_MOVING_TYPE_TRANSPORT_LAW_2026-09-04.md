# DSD M17-092 — The Rank-2 top critical line jet has an exact material recharge and moving-type transport law

Date: 2026-09-04
Canonical ID: **M17-092**

Status: **INTERNAL RANK-2 CRITICAL-TYPE TURNOVER DYNAMICS / ON CE-H, `D_B log rho=sigma+kappa-1`. BECAUSE THE VORTICITY DIRECTION IS MATERIAL (`D_B xi=0`) AND IS A STRAIN EIGENDIRECTION, `D_xi B=(sigma+1/2)xi`, SO THE SCALAR COMMUTATOR IS `[D_B,D_xi]=-(sigma+1/2)D_xi`. AT A FIXED FINITE-ORDER LINE MAXIMUM TYPE `nu`, DEFINE `g=D_xi log rho`, `G_j=D_xi^j g`, WITH `G_j=0` FOR `j<nu` AND `H_nu=G_nu<0`. COMMUTING `D_B` THROUGH `D_xi^nu` AND USING THE VANISHING OF EVERY LOWER G-JET REMOVES ALL LOWER COMMUTATOR TERMS AND GIVES THE EXACT TOP-JET LAW `D_B H_nu=D_xi^(nu+1)(sigma+kappa)-(nu+1)(sigma+1/2)H_nu`. ALONG A MOVING CRITICAL POINT/SHEET TRAJECTORY WITH RELATIVE VELOCITY `V_rel^max`, THE ONLY ADDITION IS `V_rel^max·grad H_nu`. THUS PERSISTENT RECURRENCE OF A NONZERO CRITICAL TYPE REQUIRES AN EXACT HIGHER-LINE-JET RECHARGE/RELATIVE-TRANSPORT BALANCE, WHILE TYPE CHANGE TO HIGHER DEGENERACY REQUIRES `H_nu->0`. THIS PROVIDES THE DYNAMIC CARRIER NEEDED FOR THE RANK-2 CRITICAL-TYPE TURNOVER GATE BUT DOES NOT FIX A SIGN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Amplitude material law

On CE-H,

\[
D_BW=(\sigma+\kappa-1)W.
\]

With

\[
\rho=|W|>0,
\]

we get

\[
\boxed{
D_B\log\rho
=\sigma+\kappa-1.
}
\]

Define the line-amplitude gradient

\[
\boxed{
g:=D_\xi\log\rho.}
\]

---

## 2. Directional material commutator

The director is material:

\[
\boxed{D_B\xi=0.}
\]

Also the vorticity direction is a strain eigendirection:

\[
\Sigma\xi=\sigma\xi.
\]

The antisymmetric velocity-gradient part acts by cross product with the vorticity direction and therefore

\[
\Omega\xi=0.
\]

Hence

\[
\nabla U\,\xi=\sigma\xi.
\]

Since

\[
B=U+\frac12y,
\]

we obtain

\[
\boxed{
D_\xi B
=(\sigma+\frac12)\xi.
}
\]

For any scalar `f`,

\[
D_B(D_\xi f)
=D_\xi(D_Bf)-(D_\xi B)\cdot\nabla f.
\]

Therefore

\[
\boxed{
[D_B,D_\xi]f
=-(\sigma+\frac12)D_\xi f.
}
\]

Set

\[
\boxed{\mu:=\sigma+\frac12.}
\]

---

## 3. First material law for g

Apply the commutator to `log rho`:

\[
\begin{aligned}
D_Bg
&=D_\xi(D_B\log\rho)-\mu g\\
&=D_\xi(\sigma+\kappa)-\mu g.
\end{aligned}
\]

Thus

\[
\boxed{
D_Bg
=D_\xi(\sigma+\kappa)
-(\sigma+\frac12)g.
}
\]

At any line critical point `g=0`,

\[
\boxed{
D_Bg=D_\xi(\sigma+\kappa).
}
\]

This already shows that a material marker does not remain a line maximum automatically; it must satisfy an additional line-derivative condition or be replaced by a moving maximum marker.

---

## 4. Fixed critical type

Let `nu` be the first nonzero line-jet order of `g` at a maximum:

\[
\boxed{
G_j:=D_\xi^jg=0
\qquad(0\le j\le\nu-1),
}
\]

and

\[
\boxed{
H_\nu:=D_\xi^\nu g<0.
}
\]

For a regular maximum,

\[
\nu=1,
\qquad
H_1=C=D_\xi g<0.
\]

For a degenerate maximum of M17-087,

\[
\nu=3,5,7,\ldots.
\]

---

## 5. Commuting D_B through repeated line derivatives

Repeated use of

\[
[D_B,D_\xi]=-\mu D_\xi
\]

produces derivatives of `mu` multiplying lower line jets.
Schematically,

\[
D_BD_\xi^\nu f
=D_\xi^\nu D_Bf
-\nu\mu D_\xi^\nu f
+\sum_{j<\nu}
C_{\nu j}[D_\xi^{\nu-j}\mu]D_\xi^jf.
\]

When `f=g` is evaluated at a fixed type-`nu` critical point, every lower derivative

\[
D_\xi^jg=0
\qquad(j<\nu)
\]

vanishes.
Therefore all lower commutator terms disappear and

\[
\boxed{
D_BH_\nu
=D_\xi^\nu(D_Bg)
-\nu\mu H_\nu.
}
\]

---

## 6. Exact top critical-jet material law

Use

\[
D_Bg
=D_\xi(\sigma+\kappa)-\mu g.
\]

At the type-`nu` critical point,

\[
D_\xi^\nu(\mu g)
=\mu H_\nu
\]

because every lower `g` jet vanishes.
Thus

\[
D_\xi^\nu(D_Bg)
=D_\xi^{\nu+1}(\sigma+\kappa)-\mu H_\nu.
\]

Combine with Section 5:

\[
\boxed{
D_BH_\nu
=D_\xi^{\nu+1}(\sigma+\kappa)
-(\nu+1)(\sigma+\frac12)H_\nu.
}
\]

This is the canonical material recharge law for the top critical line jet.

---

## 7. Normalized top-jet recharge

As long as

\[
H_\nu<0,
\]

define

\[
\boxed{
\mathcal R_\nu^{line}
:=\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{H_\nu}.
}
\]

Then

\[
\boxed{
D_B\log(-H_\nu)
=\mathcal R_\nu^{line}
-(\nu+1)(\sigma+\frac12).
}
\]

Thus a same-marker recurrent nonzero critical type, if it exists, must satisfy

\[
\boxed{
\left\langle\mathcal R_\nu^{line}\right\rangle
=(\nu+1)
\left(\langle\sigma\rangle+\frac12\right).
}
\]

No same-marker recurrence is assumed in the general branch tree; this is only the restricted material-marker law.

---

## 8. Moving critical-point trajectory

A recurrent Eulerian maximum generally moves relative to the material flow.
Let its trajectory have velocity

\[
\boxed{
\dot X_*
=B(X_*)+V_{rel}^{max}.
}
\]

Define the derivative along the moving critical point

\[
\boxed{
D_*:=D_B+V_{rel}^{max}\cdot\nabla.
}
\]

Then Section 6 becomes

\[
\boxed{
D_*H_\nu
=D_\xi^{\nu+1}(\sigma+\kappa)
-(\nu+1)(\sigma+\frac12)H_\nu
+V_{rel}^{max}\cdot\nabla H_\nu.
}
\]

For `H_nu!=0`,

\[
\boxed{
D_*\log(-H_\nu)
=
\mathcal R_\nu^{line}
-(\nu+1)(\sigma+\frac12)
+V_{rel}^{max}\cdot\nabla\log(-H_\nu).
}
\]

This is the type-amplitude analogue of the moving recharge laws in M17-076 and M17-080.

---

## 9. Recurrent moving-type balance

If a moving type-`nu` critical point remains on a compact recurrent branch with

\[
0<c_\nu\le -H_\nu\le C_\nu<\infty,
\]

then along recurrence intervals

\[
\left\langle
D_*\log(-H_\nu)
\right\rangle=0.
\]

Therefore

\[
\boxed{
\left\langle
\mathcal R_\nu^{line}
+V_{rel}^{max}\cdot\nabla\log(-H_\nu)
\right\rangle
=(\nu+1)
\left(
\langle\sigma\rangle+\frac12
\right).
}
\]

This is an exact recharge/turnover obligation for a recurrent critical type.

It is signed but not sign-definite.

---

## 10. Type-change mechanisms

A fixed type `nu` ceases to apply if either:

1. its top jet loses the nonzero floor:

\[
\boxed{H_\nu\to0,}
\]

opening a transition to a higher degeneracy order;

2. a lower vanishing jet becomes nonzero, producing a lower-order/regular type;

3. the transverse fixed-order compatibility hierarchy of M17-087 fails;

4. rank/interface/chart structure changes.

Therefore the critical-type transition set is contained in

\[
\boxed{
H_\nu=0
\ \lor\
\text{lower-jet unlock}
\ \lor\
T_{rank/interface/chart}.
}
\]

---

## 11. Finite-state consequence with M17-088

On the compact stable two-end decaying hull of M17-088,

\[
\nu\le\nu_*<\infty.
\]

Hence the recurrent peak geometry can visit only finitely many critical orders.
For each order, M17-092 supplies a continuous top-jet amplitude `H_nu` and a moving recharge law.

Thus a future type-resolved turnover measure can be supported on the finite state set

\[
\boxed{
\{1,3,5,\ldots,\nu_*\}.
}
\]

The transition current between those states is carried by the zero-floor events `H_nu=0` and lower-jet unlock events, not by an abstract label switch.

---

## 12. DSD analysis

The Rank-2 critical type now has two explicit continuous descriptors:

1. compensation margin `M_R2` or `M_deg^(nu)`;
2. top critical amplitude `H_nu`.

The first prevents Riccati focusing.
The second maintains the critical order itself.

Therefore a recurrent type must service **two coupled recharge ledgers** rather than merely remain in a discrete category.

---

## 13. DSD audit

### Audit A — treating nu as a purely discrete conserved label
Rejected. Type persistence is carried by the nonzero continuous jet `H_nu`.

### Audit B — forgetting derivatives of sigma in repeated commutators
They occur only multiplying lower `g` jets and vanish at a fixed type-`nu` critical point. They must be retained away from the critical set.

### Audit C — applying same-marker recurrence to moving maxima
Rejected in the general law. The moving relative-transport term is explicit.

### Audit D — claiming H_nu cannot reach zero
Not claimed. `H_nu=0` is exactly the type-increase/degeneration event.

### Audit E — assigning a sign to D_xi^(nu+1)(sigma+kappa)
Rejected. It is the signed recharge source.

### Audit F — proof status
The type dynamics is explicit but no turnover contradiction is obtained.

---

## 14. Updated RCTTG frontier

On the finite critical-order compact decaying Rank-2 hull, each retained type `nu` must simultaneously satisfy

\[
\boxed{
\mathcal M^{(\nu)}>0
}
\]

for Riccati compensation and

\[
\boxed{
D_*\log(-H_\nu)
=
\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{H_\nu}
-(\nu+1)(\sigma+\frac12)
+V_{rel}^{max}\cdot\nabla\log(-H_\nu)
}
\]

for type maintenance.

The next target is to determine whether one weighting can combine these two ledgers with the director-area/area-curvature current so that the explicit strain multiplier cancels, as the `3/2` normalization did in M17-076--080.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
