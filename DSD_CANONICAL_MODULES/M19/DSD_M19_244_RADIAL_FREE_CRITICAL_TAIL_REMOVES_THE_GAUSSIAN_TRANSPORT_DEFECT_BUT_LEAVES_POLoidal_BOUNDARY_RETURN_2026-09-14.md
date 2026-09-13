# M19-244 — Radial-free critical tail removes the Gaussian transport defect but leaves poloidal boundary return

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / RADIAL-FREE SUBBRANCH REDUCTION + SCOPE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-242--243 reduce the full expanding-cavity shell obstruction to two leading channels:

\[
\text{critical radial transport}
\quad\text{and}\quad
\text{radial/poloidal no-slip boundary response}.
\]

This module isolates the radial-free critical-tail subbranch and determines exactly what is removed and what remains.

## 2. Critical remote background decomposition

Write the leading critical remote background as

\[
U(r,\omega,s)
=
\frac1r\Big(A_r(q,\omega,s)\,\omega+A_T(q,\omega,s)\Big)
+U_{sub},
\qquad
q=\log r-\frac s2,
\]

with \(A_T\cdot\omega=0\).

For the leading \(r^{-1}\) field,

\[
\nabla\cdot\left[r^{-1}(A_r\omega+A_T)\right]
=
\frac1{r^2}
\left[(\partial_q+1)A_r+\operatorname{div}_{S^2}A_T\right].
\]

Therefore incompressibility gives the exact critical constraint

\[
\boxed{
(\partial_q+1)A_r+\operatorname{div}_{S^2}A_T=0.
}
\]

## 3. Radial-free critical coefficient is toroidal

Assume first the **leading critical radial coefficient vanishes**:

\[
\boxed{A_r=0.}
\]

Then

\[
\boxed{\operatorname{div}_{S^2}A_T=0.}
\]

Since \(H^1(S^2)=0\), the tangential Hodge decomposition contains no harmonic one-form. Hence there exists a scalar stream function \(\psi\) such that

\[
\boxed{
A_T=\omega\times\nabla_{S^2}\psi
}
\]

(up to the usual additive constant in \(\psi\)).

Thus the leading critical radial-free background is a toroidal angular flow.

## 4. The Gaussian transport defect disappears at leading critical order

M19-242 gives, with

\[
\rho=e^{-|y|^2/(4\nu)},
\]

the background-transport contribution

\[
-\int\rho\,w\cdot(U\cdot\nabla)w
=-\frac1{4\nu}\int\rho\,(U\cdot y)|w|^2.
\]

For the critical expansion,

\[
U\cdot y
=
A_r+y\cdot U_{sub}.
\]

Therefore

\[
\boxed{
A_r=0
\Longrightarrow
U\cdot y=y\cdot U_{sub}.
}
\]

If the retained remote expansion has the next radial term \(U_{sub,r}=O(r^{-3})\), then

\[
U\cdot y=O(r^{-2}),
\]

so on a shell \(r\sim R\),

\[
\boxed{
\left|\frac1{4\nu}\int\rho(U\cdot y)|w|^2\right|
\lesssim
\frac{C}{\nu R^2}\int\rho|w|^2.
}
\]

In the stronger **exact radial-free** case \(U_r\equiv0\) on the region considered,

\[
\boxed{U\cdot y\equiv0,}
\]

and \(U\cdot\nabla\) is exactly skew with respect to the Gaussian measure:

\[
\int\rho\,w\cdot(U\cdot\nabla)w=0.
\]

This removes the first leading defect of M19-242.

## 5. Stretching remains lower order on a remote shell

The stretching contribution is

\[
-\int\rho\,w^TS_Uw.
\]

The critical remote estimate

\[
|\nabla U|=O(r^{-2})
\]

gives, on \(r\sim R\),

\[
\boxed{
\left|\int\rho\,w^TS_Uw\right|
\lesssim CR^{-2}\int\rho|w|^2.
}
\]

Hence in the radial-free subbranch both bulk background defects are lower order in the remote shell.

## 6. Pressure defect survives only through the radial/poloidal part of the perturbation

The weighted pressure term remains

\[
-\int\rho\,w\cdot\nabla\pi
=-\frac1{2\nu}\int\rho\,\pi\,(y\cdot w).
\]

Writing \(w=w_r\omega+w_T\),

\[
y\cdot w=r w_r,
\]

so

\[
\boxed{
\mathcal P_\rho[w,\pi]
=-\frac1{2\nu}\int\rho\,\pi\,r w_r.
}
\]

Thus a purely toroidal perturbation with \(w_r=0\) has no weighted pressure defect. The pressure channel is intrinsically radial/poloidal.

This matches the spherical Hodge decomposition: scalar pressure gradients lie in the poloidal/gradient sector and cannot directly act as a toroidal tangential forcing.

## 7. Bare toroidal gap becomes the correct leading radial-free bulk model

For a purely toroidal perturbation and an exact radial-free background, the two leading M19-242 defects vanish:

\[
U\cdot y=0,
\qquad
\pi\text{-work}=0.
\]

The only remaining bulk perturbation of the M19-241 bare operator is the \(O(R^{-2})\) stretching/mode-mixing produced by \(\nabla U\).

Formally, on a remote shell,

\[
\boxed{
L_U^{tor}
=A_0^{tor}+O(R^{-2})
}
\]

at the coefficient level.

However this does **not** yet yield a uniform full-shell spectral gap, because:

1. the Gaussian conjugation is exponentially ill-conditioned across an expanding shell;
2. toroidal/poloidal subspaces need not remain exactly invariant under the full variable background;
3. a small coefficient perturbation of a highly nonnormal realization need not be a small resolvent perturbation in the unweighted cavity norm;
4. the no-slip boundary can inject a poloidal component even if the outer leading field is nearly toroidal.

Therefore

\[
\boxed{
A_r=0
\neq
\text{full cavity-shell closure}.
}
\]

## 8. Exact leading reduction of the shell-return obstruction

The M19-243 two-channel shell problem

\[
\text{radial critical transport}
\lor
\text{radial/poloidal boundary response}
\]

reduces, on the leading \(A_r=0\) branch, to

\[
\boxed{
\mathcal T_{shell}^{pol}:
\text{exclude an }O(1)\text{-period weak-zero shell return sustained by radial/poloidal no-slip pressure coupling and lower-order bulk mixing}.}
\]

In the stronger exact radial-free case, all order-one Gaussian bulk transport forcing disappears. Any surviving unit return must therefore use the radial/poloidal boundary channel or a loss of the compactness assumptions used in the shell reduction.

## 9. Scope firewall

There are two distinct statements:

\[
\boxed{A_r=0\text{ at critical leading order}}
\]

and

\[
\boxed{U_r\equiv0\text{ exactly on the shell}}.
\]

The first only makes \(U\cdot y\) subcritical; the second makes it identically zero. They must not be conflated.

Likewise,

\[
\boxed{
\text{leading radial-free toroidal background}
\neq
\text{invariant toroidal perturbation subspace}.
}
\]

The remaining calculation must therefore resolve the no-slip poloidal boundary response rather than import the bare toroidal gap as if it were the full operator.

## 10. Next target

The natural next object is the boundary-layer Dirichlet-to-Neumann/impedance law. M19-237 already gives the leading profile

\[
f(z)=1-e^{-z},
\qquad
z=\frac{R}{2\nu}(R-r).
\]

The next module will convert this profile into the exact leading boundary shear and dissipation paid by an outer tangential amplitude. This will determine whether the no-slip layer is an active source of unit return or only a passive dissipative load that must be replenished by the poloidal outer shell.
