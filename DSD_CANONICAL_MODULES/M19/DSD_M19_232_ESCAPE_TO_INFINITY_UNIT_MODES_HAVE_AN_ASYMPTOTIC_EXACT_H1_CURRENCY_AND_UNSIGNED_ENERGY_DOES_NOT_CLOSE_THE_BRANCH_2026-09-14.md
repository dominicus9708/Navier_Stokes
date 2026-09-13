# M19-232 — Escape-to-infinity cavity unit modes have an asymptotically exact H1 currency, and unsigned energy does not close the branch

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / ESCAPE-BRANCH ENERGY IDENTITY + UNSIGNED-ENERGY NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-231

Let

\[
R_j\to\infty
\]

and let \(w_j\) be normalized primal zero-boundary cavity unit modes with

\[
\int_0^{S_j}\|w_j(s)\|_{L^2(B_{R_j})}^2\,ds=1,
\]

solving

\[
\partial_s w_j
=\nu\Delta w_j
-\left(\frac y2+U_j\right)\cdot\nabla w_j
-\frac12w_j
-(w_j\cdot\nabla)U_j
-\nabla\pi_j,
\qquad
\nabla\cdot w_j=0,
\]

with

\[
w_j|_{S_{R_j}}=0
\]

and relative-periodic return

\[
w_j(S_j)=\mathcal R_{Q_j}w_j(0).
\]

Assume we are in the M19-231 escape branch:

\[
\boxed{
\forall r<\infty:
\quad
\int_0^{S_j}\int_{B_r}|w_j|^2\,dy\,ds\to0.
}
\]

The retained remote spectator/scattering corridor has the uniform far-field coefficient decay

\[
\boxed{
\sup_{j,s,|y|\ge r}|S_{U_j}(y,s)|\to0
\qquad(r\to\infty),
}
\]

consistent with the critical remote tail \(U=O(r^{-1})\), \(\nabla U=O(r^{-2})\).

## 2. Exact cavity velocity-energy identity

Take the \(L^2(B_{R_j})\) inner product with \(w_j\).

The viscous term gives

\[
-\nu\|\nabla w_j\|_2^2.
\]

Because \(w_j=0\) on \(S_{R_j}\), the similarity drift gives

\[
-\int w_j\cdot\frac y2\cdot\nabla w_j
=\frac34\|w_j\|_2^2.
\]

The explicit amplitude term contributes

\[
-\frac12\|w_j\|_2^2.
\]

Hence similarity drift plus amplitude contributes

\[
\boxed{\frac14\|w_j\|_2^2.}
\]

The background transport term vanishes by incompressibility and the zero boundary trace:

\[
-\int w_j\cdot(U_j\cdot\nabla)w_j=0.
\]

The pressure term also vanishes:

\[
-\int w_j\cdot\nabla\pi_j=0.
\]

Finally,

\[
-\int w_j\cdot(w_j\cdot\nabla)U_j
=-\int w_j^TS_{U_j}w_j.
\]

Therefore

\[
\boxed{
\frac12\frac d{ds}\|w_j\|_2^2
=-\nu\|\nabla w_j\|_2^2
+\frac14\|w_j\|_2^2
-\int_{B_{R_j}}w_j^TS_{U_j}w_j\,dy.
}
\]

## 3. Period integration

The relative rotation is an \(L^2\) isometry, so

\[
\|w_j(S_j)\|_2=\|w_j(0)\|_2.
\]

Integrating over one period gives

\[
\boxed{
\nu\int_0^{S_j}\|\nabla w_j\|_2^2\,ds
=\frac14
-\int_0^{S_j}\int_{B_{R_j}}w_j^TS_{U_j}w_j\,dy\,ds.
}
\]

The normalization has already replaced the period-integrated \(L^2\) term by one.

## 4. The strain correction vanishes on the escape branch

Fix \(r<\infty\). Split

\[
\int w_j^TS_{U_j}w_j
=
\int_{B_r}w_j^TS_{U_j}w_j
+
\int_{B_{R_j}\setminus B_r}w_j^TS_{U_j}w_j.
\]

On the fixed core, local coefficient boundedness and M19-231 escape give

\[
\left|
\int_0^{S_j}\int_{B_r}w_j^TS_{U_j}w_j
\right|
\to0
\qquad(j\to\infty).
\]

On the exterior,

\[
\left|
\int_0^{S_j}\int_{B_{R_j}\setminus B_r}w_j^TS_{U_j}w_j
\right|
\le
\sup_{j,s,|y|\ge r}|S_{U_j}|
\int_0^{S_j}\|w_j\|_2^2ds.
\]

The final factor is one. Therefore first \(j\to\infty\), then \(r\to\infty\), gives

\[
\boxed{
\int_0^{S_j}\int w_j^TS_{U_j}w_j\,dy\,ds\to0.
}
\]

## 5. Asymptotically exact H1 currency

Substitution into the period energy identity yields

\[
\boxed{
\nu\int_0^{S_j}\|\nabla w_j\|_2^2\,ds
\longrightarrow\frac14.
}
\]

Equivalently,

\[
\boxed{
\int_0^{S_j}\|\nabla w_j\|_2^2\,ds
\longrightarrow\frac1{4\nu}.
}
\]

Because \(w_j\in H_0^1(B_{R_j})\) is divergence free,

\[
\int_{B_{R_j}}|\nabla w_j|^2
=
\int_{B_{R_j}}|\nabla\times w_j|^2,
\]

so, writing

\[
\eta_j:=\nabla\times w_j,
\]

we also obtain

\[
\boxed{
\int_0^{S_j}\|\eta_j\|_2^2\,ds
\longrightarrow\frac1{4\nu}.
}
\]

Thus a normalized escaping cavity unit mode cannot become a low-frequency or nearly irrotational artifact. It carries a fixed nonzero one-period vorticity currency.

## 6. Why this does not yet contradict escape

The identity is compatible with normalized modes of order-one local thickness that translate to larger and larger similarity radii.

Indeed the bare remote similarity operator itself contains the positive velocity-energy production

\[
+\frac14\|w\|_2^2,
\]

which balances viscosity exactly at the level

\[
\nu\|\nabla w\|_2^2\sim\frac14\|w\|_2^2.
\]

Therefore

\[
\boxed{
\text{remote background smallness}
+\text{unsigned velocity energy}
\neq
\text{escape-to-infinity contradiction}.
}
\]

This is a new permanent firewall for the cavity branch.

## 7. New leverage: velocity and vorticity energies have opposite similarity signs

The result nevertheless gives a useful next target.

For velocity, the bare similarity contribution is

\[
+\frac14\|w\|_2^2.
\]

For the linearized vorticity \(\eta=\nabla\times w\), the similarity amplitude is one degree stronger and the bare vorticity energy contribution is

\[
-\frac14\|\eta\|_2^2.
\]

Hence a remote escaping mode with

\[
\int_0^{S_j}\|\eta_j\|_2^2ds\to\frac1{4\nu}>0
\]

cannot satisfy a boundary-free remote vorticity period identity unless another flux/cutoff/boundary term replenishes this negative similarity-vorticity budget.

This identifies the next calculation precisely: localize the vorticity identity and determine where the compensating replenishment must enter.

## 8. Updated escape frontier

The escape branch is now sharpened from mere spatial noncompactness to

\[
\boxed{
\mathcal T_{cav}^{esc,H1}:
\begin{array}{l}
\text{classify an escaping normalized cavity unit mode carrying the fixed currency}\\
\displaystyle \int_0^{S_j}\|\eta_j\|_2^2ds\to\frac1{4\nu},\\
\text{and identify the flux/boundary mechanism that offsets the negative remote vorticity similarity budget.}
\end{array}}
\]

---

\[
\boxed{\text{M19-232 COMPLETE: ESCAPE HAS A FIXED H1/VORTICITY CURRENCY, BUT UNSIGNED VELOCITY ENERGY DOES NOT CLOSE IT.}}
\]
