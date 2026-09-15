# M19-279 — Winding index is material, but regular nodal-Jacobian drift is an exact coboundary and cannot pay positive-mean lag

**Date:** 2026-09-16  
**Status:** CALCULATION / DYNAMIC CORE SIGNED-INDEX AUDIT / REGULAR WINDING NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-271 shows that the positive-mean signed energy event cannot be represented by a bounded finite-lag state coboundary. After M19-278 removes the critical radial weighted source as a finite core payer, a natural remaining candidate is the integer winding/index carried by the rank-one great-circle nodal branch.

M16-028 and M17-006--007 already provide the exact structure:

\[
f=W_1+iW_2=\rho e^{i\psi},
\qquad
N_\gamma=\frac1{2\pi}\oint_\gamma d\psi\in\mathbb Z,
\]

and regular codimension-two winding filaments are material. Hence the winding index is frozen along a regular material defect.

This module audits whether that index, or the natural signed nodal-Jacobian multiplier attached to it, can supply the missing non-coboundary lag payer.

The answer is negative on the regular branch.

## 2. Frozen winding index

For a small material loop \(\gamma(\theta)\) linking one regular nodal filament, M17-007 gives

\[
\boxed{
N_\gamma(\theta)
=\frac1{2\pi}\oint_{\gamma(\theta)}d\psi
=\text{constant}
}
\]

as long as the filament remains regular and no zero crosses the loop.

Therefore for every finite lag \(h\),

\[
\boxed{
N_\gamma\circ\sigma_h-N_\gamma=0.
}
\]

Thus the integer index is a state label, not a positive signed drift observable.

## 3. Exact nodal-Jacobian drift

M17-010 gives, at a regular great-circle winding filament, the horizontal Jacobian law

\[
D_BG_h
=\left(\kappa-\frac32\right)G_h.
\]

Whenever \(\det G_h\neq0\),

\[
\boxed{
D_B\log|\det G_h|
=2\kappa-3.
}
\]

Integrating along one material filament from \(\theta\) to \(\theta+h\) gives the exact finite-lag identity

\[
\boxed{
\int_\theta^{\theta+h}(2\kappa-3)\,d\tau
=
\log|\det G_h(\theta+h)|
-
\log|\det G_h(\theta)|.
}
\]

Hence the natural signed regular-nodal multiplier is itself an exact coboundary.

## 4. Recurrent compact branch

If the regular nodal filament remains uniformly nondegenerate,

\[
0<c_G\le|\det G_h|\le C_G<\infty,
\]

then \(\log|\det G_h|\) is bounded/integrable on the recurrent hull. Invariant averaging gives

\[
\boxed{
\left\langle
\int_0^{h}(2\kappa-3)\circ\sigma_\tau\,d\tau
\right\rangle=0.
}
\]

Equivalently,

\[
\boxed{
\langle\kappa\rangle_{nodal}=\frac32.
}
\]

This signed mean constraint is real, but it is exactly the vanishing-drift condition of the bounded Jacobian observable. It does not provide the positive-mean remainder required by M19-271.

## 5. Slanted regular filament

If the vertical derivative column also remains uniformly nonzero, M17-010 gives

\[
D_B\log|G_3|
=3\lambda+\kappa-\frac32.
\]

The same recurrence argument yields

\[
\boxed{\langle\lambda\rangle_{nodal}=0.}
\]

after using \(\langle\kappa\rangle=3/2\).

This is again a coboundary recurrence constraint rather than a one-way signed payer.

## 6. Where an index change can occur

M17-007 gives

\[
\boxed{
\text{winding topology change}
\Longrightarrow
\operatorname{rank}(\nabla W_1,\nabla W_2)<2
}
\]

at a nodal event.

M17-009 then proves that on the compact analytic hard hull every such event has uniformly bounded finite vanishing order and a nonzero finite-jet floor.

Therefore the only way to change winding is the explicit branch

\[
\boxed{
T_{nodal}^{finite\text{-}jet}.
}
\]

But M17-009 also records the key firewall: a positive-density finite-order nodal event is still an unsigned analytic-geometry event. No signed monotone budget follows from its existence alone.

## 7. Consequence for M19-271

The winding route splits exactly as

\[
\boxed{
\begin{aligned}
\mathcal T_{aper}^{signed/index}
\text{ via winding}
\Longrightarrow{}&
\text{regular material winding}
\\
&\lor
T_{nodal}^{finite\text{-}jet}
\\
&\lor
G_{winding/reuse/decompactification}.
\end{aligned}
}
\]

On the regular branch:

- integer winding is frozen;
- the natural Jacobian signed multiplier is a bounded-state coboundary;
- its invariant mean drift is zero.

On the topology-changing branch:

- finite-order coherent events exist;
- but they are unsigned unless an additional orientation/index-production law is derived.

On the decompactifying branch, M17-355--356 and M19-019 already reduce large winding to critical packing, flux fragmentation, spatial reuse, or geometry escape rather than a one-way signed accumulation theorem.

Hence

\[
\boxed{
\text{ordinary great-circle winding/index is not yet the missing M19-271 non-coboundary payer.}
}
\]

## 8. New precise target

The only potentially useful index mechanism would have to be a **signed index-production defect** at nodal topology change, not the conserved winding itself.

The next question is therefore:

\[
\boxed{
\text{Can interior finite-jet nodal events change a material cross-section's total algebraic winding,}
}
\]

or is the total index fixed by the phase degree on the material boundary?

If the latter, then even topology turnover cannot supply net signed index, and the winding route is removed as a standalone candidate for \(\mathcal T_{aper}^{signed/index}\).

---

\[
\boxed{\text{M19-279 COMPLETE; REGULAR WINDING INDEX AND NODAL-JACOBIAN DRIFT DO NOT SUPPLY THE POSITIVE-MEAN LAG DEFECT.}}
\]
