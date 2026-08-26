# DSD M5-9 — Critical weighted local-energy flux certificate

Date: 2026-08-26

Status: **DERIVED WEIGHTED ENERGY IDENTITY / CROSS-RADIUS CRITICAL CORRIDOR REQUIRES A SCALE-CRITICAL RADIAL ENERGY-FLUX HISTORY / NO UNIVERSAL SIGN OR FINITE LARGE-DATA BOUND OBTAINED / M5 REMAINS OPEN.**

## 1. Critical weighted energy

Fix a candidate point `X_*` and write

\[
r=|x-X_*|.
\]

Define

\[
\boxed{
\mathcal W(t)
:=
\frac12\int_{\mathbb R^3}\frac{|u(x,t)|^2}{r}\,dx.
}
\]

This quantity is invariant under the Navier--Stokes spatial scaling and is therefore a genuine `beta=0` candidate ledger.

For every smooth pre-singular time it is finite: near `X_*` smoothness makes `1/r` locally integrable against `|u|^2`, while at infinity `1/r<=1` and the physical energy is finite.

## 2. Exact weighted local-energy identity

Use smooth radial approximations to `1/r` in the standard local-energy equality and pass to the limit. Since

\[
\nabla\frac1r
=-\frac{x-X_*}{r^3},
\qquad
\Delta\frac1r
=-4\pi\delta_{X_*},
\]

one obtains on every smooth interval

\[
\boxed{
\frac{d\mathcal W}{dt}
+\nu\int\frac{|\nabla u|^2}{r}\,dx
+2\pi\nu |u(X_*,t)|^2
=
-\int
\left(\frac{|u|^2}{2}+p\right)
\frac{u\cdot(x-X_*)}{r^3}\,dx.
}
\]

The delta contribution has the favorable sign and has been moved to the left.

## 3. Radial energy-flux representation

Define the energy/pressure flux through the sphere `S_r(X_*)` by

\[
\mathcal F_E(r,t)
:=
\int_{S_r(X_*)}
\left(\frac{|u|^2}{2}+p\right)
u_r\,dS,
\]

where

\[
u_r=u\cdot n.
\]

Then coarea gives

\[
\boxed{
-\int
\left(\frac{|u|^2}{2}+p\right)
\frac{u\cdot(x-X_*)}{r^3}\,dx
=
-\int_0^\infty\frac{\mathcal F_E(r,t)}{r^2}\,dr.
}
\]

Because incompressibility gives

\[
\int_{S_r}u\cdot n\,dS=0,
\]

adding a spatially constant pressure gauge does not change `F_E`. Thus this flux is gauge-independent.

The weighted-energy ledger is therefore

\[
\boxed{
\frac{d\mathcal W}{dt}
+\nu\mathcal D_W(t)
+2\pi\nu|u(X_*,t)|^2
=
-\int_0^\infty\frac{\mathcal F_E(r,t)}{r^2}\,dr,
}
\]

with

\[
\mathcal D_W(t)
:=
\int\frac{|\nabla u|^2}{r}dx.
\]

## 4. Relation to the cross-radius critical corridor

In the retained physical `1/r` corridor, a dyadic shell with nonzero cubic critical mass and the Type-I envelope satisfies

\[
|u(x,t)|\le\frac{A_0}{r}.
\]

Hence pointwise on such a shell

\[
\frac{|u|^2}{r}
\ge
\frac{|u|^3}{A_0}.
\]

If the shell carries

\[
\int_{r<|x-X_*|<2r}|u|^3dx\ge m_*>0,
\]

then its contribution to `W` is at least

\[
\frac{m_*}{2A_0}.
\]

Therefore a coherent family of `N` dyadic critical shells forces

\[
\boxed{
\mathcal W(t)\gtrsim cN.
}
\]

With the inner scale

\[
r_*(t)\sim\sqrt{T_*-t},
\]

one has

\[
N(t)\sim\log\frac{r_0}{r_*(t)}
\sim\frac12\log\frac1{T_*-t},
\]

so the corridor requires the critical weighted energy to grow at least logarithmically along the corresponding shell-density lane.

This statement is to be read in the lane where the shell lower bound is available; the general Abel/Cesaro endpoint should not be silently upgraded to a pointwise shell statement without its existing hypotheses.

## 5. DSD consequence: a dynamic flux certificate

The growth of `W` cannot come from ordinary physical-energy creation. The exact identity shows that it must be accompanied by the critical weighted radial flux

\[
\boxed{
\Phi_W(t)
:=-\int_0^\infty\frac{\mathcal F_E(r,t)}{r^2}dr.
}
\]

Thus a surviving cross-radius family is not merely a static collection of `1/r` shells. It requires a compatible **time history of gauge-invariant critical radial energy/pressure flux** capable of balancing

\[
\frac{d\mathcal W}{dt}
+\nu\mathcal D_W.
\]

This is a stronger dynamic certificate than the scalar fixed-time Morrey quantity rejected in M5-7.

## 6. Why this is still not a contradiction

For the model critical scaling `u~1/r` down to `r_*(t)~sqrt(T_*-t)`, the terms in this weighted ledger naturally reach critical size. In particular the weighted dissipation behaves at the endpoint scale like a quantity of order `(T_*-t)^{-1}` in the exact self-similar dimensional model, whose time integral is logarithmically divergent.

The radial flux has the same critical scaling and no universal sign is available from the local-energy identity.

Therefore ordinary finite physical energy and finite unweighted total dissipation do not bound `W`, `D_W`, or `Phi_W` uniformly enough to close M5.

This reproduces the same endpoint barrier in a genuinely scale-critical physical-time ledger rather than a subcritical one.

## 7. Relation to standard local-energy theory

The identity is a singular-weight form of the suitable/local energy framework. Weighted/local-energy methods are standard tools in partial-regularity theory, but the missing large-data statement here is precisely a uniform critical control of the weighted flux/tail, not the formal validity of the local-energy identity itself.

## 8. Updated M5 target

M5-8 and M5-9 together give the following necessary structure for a survivor:

\[
\boxed{
\text{cross-radius cubic memory}
\Longrightarrow
\text{radial variation and/or angular-vorticity action}
\Longrightarrow
\text{critical weighted energy/flux history}.
}
\]

A closing theorem would need to prove that this critical weighted flux history cannot be generated by a finite-energy Navier--Stokes prelimit, or else upgrade it to an already excluded strong-critical class.

No such theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
