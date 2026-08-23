# Moving Relative-Variance Turnover Ledger — 2026-08-23

Status: **EXACT LOCAL IDENTITY / PARTIAL TURNOVER BRIDGE — GLOBAL REGULARITY NOT PROVED.**

The relative-Campanato remote-strain gate reduces the active remote obstruction to a large relative-velocity reservoir. This note records the exact local energy identity that determines how such a reservoir can grow, contract, move, or be replaced.

---

## 1. Weighted relative velocity

Let `phi(x,t)` be a smooth compactly supported nonnegative cutoff and define the weighted mean

\[
\bar u_\phi(t)
:=
\frac{\int \phi u\,dx}{\int \phi\,dx}.
\]

Set

\[
v=u-\bar u_\phi,
\qquad
V_\phi(t)
:=
\frac12\int \phi|v|^2\,dx.
\]

By construction,

\[
\boxed{\int \phi v\,dx=0.}
\]

Therefore the time derivative of the moving mean creates no bulk term:

\[
\int \phi v\cdot \bar u_\phi'(t)\,dx=0.
\]

This cancellation is the reason to use relative velocity rather than absolute local kinetic energy.

---

## 2. Exact relative-variance identity

For a smooth incompressible Navier–Stokes solution

\[
\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
\qquad \nabla\cdot u=0,
\]

a direct integration by parts gives, for arbitrary scalar `c(t)`,

\[
\boxed{
\begin{aligned}
V_\phi'
+\nu\int \phi|\nabla u|^2\,dx
={}&
\frac12\int |v|^2
\left(\phi_t+u\cdot\nabla\phi+\nu\Delta\phi\right)dx\\
&+
\int (p-c(t))v\cdot\nabla\phi\,dx.
\end{aligned}
}
\]

No absolute velocity mean appears in the bulk dissipation term.

This identity is exact for the smooth regime under consideration.

---

## 3. Moving and dilating observation ball

Take

\[
\phi(x,t)
=
\Phi\!\left(\frac{x-X(t)}{\ell(t)}\right),
\]

where `Phi` is a fixed cutoff profile, `X(t)` a tracked center, and `ell(t)` a physical observation radius.

Then

\[
\boxed{
\phi_t+u\cdot\nabla\phi
=
\left(
 u-\dot X
-\frac{\dot\ell}{\ell}(x-X)
\right)\cdot\nabla\phi.
}
\]

Hence

\[
\boxed{
\begin{aligned}
V_\phi'
+\nu D_\phi
={}&
\frac12\int|v|^2
\left[
\left(
 u-\dot X
-\frac{\dot\ell}{\ell}(x-X)
\right)\cdot\nabla\phi
+\nu\Delta\phi
\right]dx\\
&+
\int(p-c)v\cdot\nabla\phi\,dx,
\end{aligned}
}
\]

with

\[
D_\phi:=\int\phi|\nabla u|^2dx.
\]

---

## 4. Turnover channels exposed by the identity

The right-hand side contains exactly four geometric mechanisms.

### T_mat: material crossing

\[
\boxed{
\mathcal T_{mat}
:=
\frac12\int|v|^2(u-\dot X)\cdot\nabla\phi\,dx.
}
\]

This measures relative-energy transport through the moving shell boundary.

### T_rad: boundary contraction / expansion

\[
\boxed{
\mathcal T_{rad}
:=
-\frac12\frac{\dot\ell}{\ell}
\int|v|^2(x-X)\cdot\nabla\phi\,dx.
}
\]

This records the work caused by changing the observation radius itself.

### T_vis: viscous boundary leakage

\[
\boxed{
\mathcal T_{vis}
:=
\frac\nu2\int|v|^2\Delta\phi\,dx.
}
\]

The interior viscous dissipation `nu D_phi` remains on the coercive left-hand side.

### T_pres: pressure work

\[
\boxed{
\mathcal T_{pres}
:=
\int(p-c)v\cdot\nabla\phi\,dx.
}
\]

Only pressure oscillation relative to an arbitrary scalar gauge matters.

Thus

\[
\boxed{
V_\phi'+\nu D_\phi
=
\mathcal T_{mat}
+\mathcal T_{rad}
+\mathcal T_{vis}
+\mathcal T_{pres}.
}
\]

This is the natural quantitative ledger for the project’s turnover channel `T`.

---

## 5. Connection to relative Campanato escalation

At a normalized scale `rho`, the relative Campanato quantity is

\[
\mathcal C_\rho
=\rho^{-1}
\int_{B_\rho}|U-(U)_{B_\rho}|^2.
\]

The preceding remote-strain gate shows that an order-one remote influence at normalized radius `R` forces, at some `rho>=R`,

\[
\mathcal C_\rho\gtrsim R^4.
\]

Such a reservoir cannot appear, disappear, contract, or be replaced without changing an appropriate relative-variance functional `V_phi`. The exact identity therefore converts the qualitative phrase “turnover” into a finite list of possible payers.

The remaining target lemma is of the form

\[
\boxed{
\left|\Delta V_\phi\right|\ge \delta V_{ref}
\Longrightarrow
\int_I
\frac{
|\mathcal T_{mat}|+|\mathcal T_{rad}|+|\mathcal T_{vis}|+|\mathcal T_{pres}|+
u D_\phi
}{V_{ref}}dt
\ge c(\delta)>0.
}
\]

The identity itself makes this implication nearly tautological once a single coherent reference reservoir and cutoff are fixed. The nontrivial part is choosing the reservoir consistently across consecutive first-hitting stages so that source replacement cannot evade the comparison.

---

## 6. Coherent affine-strain corridor

The scaling

\[
U(y)\approx Ay,
\qquad |A|\sim1,
\]

saturates

\[
\mathcal C_R\sim R^4.
\]

Thus the last active remote obstruction is not a constant Galilean drift. It is a coherent large-scale affine/strain component.

For such a component, changing the active physical radius, changing the center, or replacing the contributing affine source necessarily enters one of the boundary terms above. This is why the relative-variance ledger is more appropriate than an absolute-energy argument.

---

## 7. Center drift must be kept separate

A moving weighted-mean center `X(t)` is not automatically a material trajectory. Therefore one must not identify contraction of `|x-X(t)|` with contraction of a material line unless

\[
\dot X=u(X,t)
\]

or a comparable material-center statement has been proved.

If the center is not material, the mismatch

\[
\boxed{\dot X-u(X,t)}
\]

appears explicitly inside `T_mat` and is itself a center-turnover contribution.

This corrects an over-strong interpretation in the earlier contracting-active-halo note.

---

## 8. Current proof obligation

The next finite-stage closure should prove one of the following equivalent-style statements:

1. no-turnover bounds all four normalized boundary actions, forcing a uniform relative-Campanato bound; or
2. relative-Campanato escalation forces one normalized boundary action to exceed a universal positive threshold in that stage.

If either is established, the `R^{-2}` relative-Campanato remote-strain gate removes dynamically active `H_remote` from normalized radius infinity.

Status: **THE TURNOVER LEDGER IS NOW AN EXACT MOVING-RELATIVE-ENERGY IDENTITY. THE REMAINING GAP IS A CROSS-STAGE COHERENT-RESERVOIR SELECTION / LOWER-BOUND LEMMA, NOT THE LOCAL ENERGY ALGEBRA ITSELF.**