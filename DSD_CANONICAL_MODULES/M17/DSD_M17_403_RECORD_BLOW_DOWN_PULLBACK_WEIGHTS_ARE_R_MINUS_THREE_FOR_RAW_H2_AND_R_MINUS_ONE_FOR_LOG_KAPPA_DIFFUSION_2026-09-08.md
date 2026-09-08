# DSD M17-403 — Record blow-down pullback weights are `R^{-3}` for raw-`H2` and `R^{-1}` for log-`kappa` diffusion

Date: 2026-09-08  
Canonical ID: **M17-403**

Status: **ACTIVE CROSS-GENERATION SCALING AUDIT / EXACT ANCESTRY WEIGHTS / BUDGET STATUS SEPARATED FROM SCALING**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Record blow-down map

Let the first-generation ancient vorticity be

\[
\Omega(x,t),
\]

and let a second-generation record cell be obtained by the standard record blow-down

\[
\boxed{
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
}
\]

with `R>1` the record blow-down factor.

On exact CE-H,

\[
\Delta_x\Omega=\kappa\Omega.
\]

The coefficient transforms as

\[
\boxed{
\kappa_R(y,s)=R^2\kappa(Ry,R^2s).
}
\]

Write

\[
\rho=|\Omega|,
\qquad
\rho_R=|\Omega_R|=R^2\rho.
\]

Fix a normalized time window

\[
I=[-b,-a]\Subset(-\infty,0).
\]

Its ancestral physical-time window is

\[
I_R^{anc}=R^2I.
\]

## 2. Exact raw-`H2` scaling

Differentiate twice in `y`:

\[
\Delta_y\Omega_R
=R^4\Delta_x\Omega.
\]

Therefore at one time,

\[
\begin{aligned}
\|\Delta_y\Omega_R(s)\|_2^2
&=
\int R^8|\Delta_x\Omega|^2R^{-3}dx\\
&=R^5\|\Delta_x\Omega(R^2s)\|_2^2.
\end{aligned}
\]

Since

\[
ds=R^{-2}dt,
\]

we obtain

\[
\boxed{
\int_I\|\Delta_y\Omega_R(s)\|_2^2ds
=R^3
\int_{R^2I}\|\Delta_x\Omega(t)\|_2^2dt.
}
\]

Equivalently, one descendant raw-`H2` payment pulls back with weight

\[
\boxed{
R^{-3}.
}
\]

This agrees with the general derivative scaling

\[
q(2+k-3/p)-2
\]

at `k=2`, `p=q=2`.

## 3. Exact log-`kappa` diffusion scaling

Define the physical logarithmic coefficient diffusion charge

\[
\mathscr D_{\log\kappa}^{anc}(J)
:=
\int_J\int
\rho^2
|\nabla_x\log|\kappa||^2dxdt,
\]

on a sign-preserving region where `kappa != 0`.

Because

\[
\log|\kappa_R|
=
\log|\kappa|+2\log R,
\]

the additive constant disappears after differentiation:

\[
\boxed{
\nabla_y\log|\kappa_R|
=R\nabla_x\log|\kappa|.
}
\]

Hence

\[
\rho_R^2
|\nabla_y\log|\kappa_R||^2
=R^6
\rho^2|\nabla_x\log|\kappa||^2.
\]

With

\[
dy=R^{-3}dx,
\qquad
 ds=R^{-2}dt,
\]

we obtain

\[
\boxed{
\mathscr D_{\log\kappa,R}(I)
=R
\mathscr D_{\log\kappa}^{anc}(R^2I).
}
\]

Thus the exact ancestry weight is

\[
\boxed{R^{-1}.}
\]

This is the same record exponent as vorticity palinstrophy, although the controlled quantity is different.

## 4. Conditional finite-overlap ledgers

For geometric record factors `R_m`, the windows

\[
R_m^2I
\]

have uniformly finite overlap after the same fixed residue-class decomposition used in M17-307.

Therefore, **if** the first-generation ancient solution satisfied

\[
\mathscr H_{anc}
:=
\int_{-\infty}^0
\|\Delta\Omega(t)\|_2^2dt
<\infty,
\]

then automatically

\[
\boxed{
\sum_m
R_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds
\le C_I\mathscr H_{anc}<\infty.
}
\]

Likewise, if an ancestral sign-preserving log-diffusion total were finite,

\[
\mathscr D_{\log\kappa,anc}<\infty,
\]

then

\[
\boxed{
\sum_m
R_m^{-1}
\mathscr D_{\log\kappa,m}(I)
<\infty.
}
\]

The scaling statements are unconditional; the finiteness statements require the corresponding ancestral totals.

## 5. Immediate multiplicity thresholds

Suppose record cell `m` contains `N_m` pairwise spacetime-disjoint descendant events, each carrying an order-one normalized raw-`H2` payment

\[
\int_{Q_{m,j}}|\Delta\Omega_m|^2dyds\ge c_H>0.
\]

A finite raw-`H2` ancestor would then give only

\[
\boxed{
\sum_m\frac{N_m}{R_m^3}<\infty.
}
\]

Thus a contradiction would require

\[
\boxed{
\sum_m\frac{N_m}{R_m^3}=\infty.
}
\]

Similarly, an order-one normalized log-diffusion event would require

\[
\boxed{
\sum_m\frac{N_m}{R_m}=\infty
}
\]

provided a finite ancestral log-diffusion total existed.

Therefore the two resources have different ancestry discounts even though both are scale-critical in their own local normalization.

## 6. Audit firewall

The following inferences are rejected:

1. using the shrinking own-scale radius of M17-388--396 as the growing record factor `R_m`;
2. importing the M17-307 `R_m^{-1}` palinstrophy weight into raw-`H2` without recomputation;
3. declaring a finite ledger from scaling alone;
4. treating the logarithmic coordinate across `kappa=0` as regular.

The exact record weights are

\[
\boxed{
R_m^{-3}\quad\text{for raw-`H2`,}
\qquad
R_m^{-1}\quad\text{for away-zero log-`kappa` diffusion.}
}
\]

## 7. Next proof obligation

The raw-`H2` budget question is now sharply separated from scaling:

\[
\boxed{
\text{Does M5-475 Type-I backward decay plus M5-477 finite palinstrophy imply}
\int_{-\infty}^0\|\Delta\Omega\|_2^2dt<\infty?
}
\]

This can be attacked directly through the ancient vorticity equation regarded as a forced heat equation.

The log-`kappa` total remains a separate coefficient/zero-corridor problem.

## 8. DSD audit role

DSD contributes only the instruction to keep currencies and scale maps separate. The canonical result is the exact Navier--Stokes parabolic scaling calculation above.

## 9. Audit verdict

**PASS — exact ancestry weights identified; budget finiteness remains a separate theorem.**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
