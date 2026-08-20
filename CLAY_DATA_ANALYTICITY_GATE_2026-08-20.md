# Clay-Data Analyticity Gate — 2026-08-20

Status: **SMOOTH RAPIDLY-DECAYING INITIAL-DATA TRACK — GLOBAL REGULARITY NOT PROVED.**

This note clarifies the hypothesis behind the uniform first-hitting analytic strip and inserts a standard vorticity analyticity theorem into `ANALYTICITY_LOCAL_MASS_LEAKAGE_GATE_2026-08-20.md`.

External analytic input: the vorticity spatial-analyticity theorem recalled in Grujic--Xu, *Asymptotic Criticality of the Navier--Stokes Regularity Problem*, Theorem 2.1, after Bradshaw et al. For viscosity one, if the restart vorticity belongs to `L^infinity cap L^1`, then for every `M>1` there is `c(M)` such that the mild solution exists for at least

\[
T\ge\frac{1}{c(M)\|\omega_0\|_\infty}
\]

and has complex vorticity bound at most `M ||omega_0||_infinity` in a strip of radius at least

\[
\frac{\sqrt t}{\sqrt{c(M)}}.
\]

The `L^1` membership is important and is not automatic on the larger suitable finite-energy class.

## 1. Why the Clay-data track meets the L1 membership condition

For smooth rapidly decaying initial data, `omega_0 in L1`. During every smooth interval before a hypothetical first singular time, the vorticity magnitude inequality gives schematically

\[
\frac d{dt}\|\omega(t)\|_1
\le
\|S(t)\|_\infty\|\omega(t)\|_1.
\]

Since `||S||_infinity` is finite on every compact subinterval of the smooth lifespan,

\[
\omega(t)\in L^1
\qquad(t<T^*).
\]

Thus the theorem can be restarted at every pre-singular first-hitting stage on the smooth rapidly-decaying initial-data track.

This does **not** justify the same statement for an arbitrary suitable finite-energy solution with no `L1` vorticity hypothesis.

## 2. Restore arbitrary viscosity

Write

\[
u=\nu v,
\qquad
\tau=\nu t,
\qquad
p=\nu^2q.
\]

Then `v` solves the viscosity-one Navier--Stokes equation and its vorticity is

\[
\zeta=\omega/\nu.
\]

At a first-hitting restart time `t_j^-`, assume

\[
\|\omega(t_j^-)\|_\infty\le W_j.
\]

Then

\[
\|\zeta(t_j^-)\|_\infty\le W_j/\nu.
\]

For any fixed `M>1` and `0<sigma<1`, choose the physical elapsed time

\[
\Delta t
=\frac{\sigma}{c(M)W_j}.
\]

This lies strictly inside the guaranteed analytic interval.

The physical analytic radius is at least

\[
\sqrt{\frac{\nu\sigma}{c(M)^2W_j}}.
\]

In first-hitting coordinates

\[
y=\sqrt{W_j}(x-X_*),
\qquad
\Omega=\omega/W_j,
\]

we therefore obtain the uniform normalized constants

\[
\boxed{
M_0=M,
\qquad
\rho_0=\frac{\sqrt{\sigma\nu}}{c(M)}.
}
\]

## 3. Insert into the local analytic leakage gate

The previous local exclusion radius was

\[
R_{ex}
=
\min\left\{
\frac{\rho_0}{12M_0},
\frac{0.05976760\rho_0}{\sqrt{M_0}}
\right\}.
\]

Hence on the smooth rapidly-decaying initial-data track,

\[
\boxed{
R_{ex}(M,\sigma)
=
\frac{\sqrt{\sigma\nu}}{c(M)}
\min\left\{
\frac1{12M},
\frac{0.05976760}{\sqrt M}
\right\}.
}
\]

For every first-hitting active core radius `R <= R_ex`, the normalized annular leakage obeys

\[
\boxed{
\mathcal L_R\ge0.8399984284.
}
\]

Consequently at least one of the two normalized annular channels must satisfy

\[
R\frac{\|\nabla\Omega\|_{L^2(A_R)}}
{\|\Omega\|_{L^2(B_R)}}
\ge
\frac{0.4199992142}{C_{loc}^{(2)}}
\]

or

\[
\frac{\|\Omega\|_{L^2(A_R)}}
{\|\Omega\|_{L^2(B_R)}}
\ge
\frac{0.4199992142}{C_{loc}^{(2)}}.
\]

These are respectively derivative escape (`H`) and comparable annular/core mass (`T`) candidates.

## 4. Convenient M=2 specialization

Choosing `M=2`, the first entry in the minimum is slightly smaller, so

\[
\boxed{
R_{ex}(2,\sigma)
=
\frac{\sqrt{\sigma\nu}}{24c(2)}.
}
\]

For example, the safe choice `sigma=1/2` gives

\[
\boxed{
R_{ex}
=
\frac{1}{24\sqrt2\,c(2)}\sqrt\nu
\approx
\frac{0.0294628}{c(2)}\sqrt\nu.
}
\]

The numerical value of `c(2)` is not supplied by the cited theorem statement, so this is not yet a fully numerical universal radius.

## 5. Updated rigor split

The active route should distinguish:

1. **Smooth rapidly-decaying/Clay initial data:** the uniform analytic strip above is available through the `L1 cap L-infinity` vorticity theorem, and the local leakage gate is unconditional within the smooth lifespan.
2. **General suitable finite-energy extension:** the same uniform `(rho_0,M_0)` cannot be imported from that theorem without an additional vorticity integrability or analyticity input.

The proof challenge can remain focused on the first track, because proving global regularity there already addresses the standard whole-space smooth-data problem. The larger suitable class should remain an extension target, not a hidden assumption in the main chain.

Status: **ON THE SMOOTH RAPIDLY-DECAYING INITIAL-DATA TRACK, THE FIRST-HITTING ANALYTIC CONSTANTS CAN BE WRITTEN AS `M_0=M` AND `rho_0=sqrt(sigma*nu)/c(M)`. THIS TURNS THE LOCAL SOLENOIDAL LEAKAGE LAW INTO A UNIVERSAL-SCALE `sqrt(nu)` DICHOTOMY, UP TO THE ANALYTICITY CONSTANT `c(M)`.**