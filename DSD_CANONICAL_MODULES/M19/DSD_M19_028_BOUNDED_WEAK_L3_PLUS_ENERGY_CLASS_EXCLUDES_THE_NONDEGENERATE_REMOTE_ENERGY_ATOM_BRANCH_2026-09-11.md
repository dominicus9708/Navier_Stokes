# M19-028 — Bounded weak-L3 plus the energy class excludes the nondegenerate remote energy-atom branch

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE TO W1 INTERFACE / L4 ENERGY EQUALITY / NONDEGENERATE REMOTE EXCLUSION UNDER WEAK-L3 COMPACTNESS

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-025

M19-025 proves that on the nondegenerate remote source branch

\[
\Lambda_j=K_j^5r_j\ge\Lambda_->0,
\]

the pre-singular kinetic-energy measures develop a fixed atom at the singular point. Equivalently, a strong left terminal \(L^2\) trace fails.

The present module asks whether this is compatible with the bounded weak-\(L^3\) corridor used in W1.

## 2. Assume bounded weak-L3 near the first singular time

Suppose that on a terminal interval \([t_0,T_*)\),

\[
\boxed{
\sup_{t_0<t<T_*}
\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}
\le M<\infty.
}
\]

Navier--Stokes scaling preserves the weak-\(L^3\) norm, so this is exactly the physical counterpart of the bounded weak-critical W1 corridor.

## 3. Energy class supplies L2_t L6_x

The finite-energy identity gives

\[
\int_{t_0}^{T_*}\|\nabla u(t)\|_2^2dt<\infty.
\]

Sobolev gives

\[
\|u(t)\|_6\lesssim\|\nabla u(t)\|_2.
\]

Therefore

\[
\boxed{u\in L^2(t_0,T_*;L^6(\mathbb R^3)).}
\]

## 4. Lorentz interpolation gives L4_t L4_x

The standard Lorentz interpolation inequality gives

\[
\boxed{
\|f\|_4
\le
C\|f\|_{L^{3,\infty}}^{1/2}\|f\|_6^{1/2}.
}
\]

Hence

\[
\|u(t)\|_4^4
\le
CM^2\|u(t)\|_6^2.
\]

Integrating in time,

\[
\boxed{u\in L^4(t_0,T_*;L^4(\mathbb R^3)).}
\]

This is strictly inside the classical energy-equality regime.

## 5. Energy equality restores the terminal norm

For Leray--Hopf solutions, the classical Lions--Shinbrot energy-equality criterion applies to the \(L^4_tL^4_x\) class. Thus the kinetic-energy balance has no anomalous loss at \(T_*\).

If

\[
u(t)\rightharpoonup u(T_*)
\]

is read with the leading field symbol equal to \(u(t)\), then energy equality yields

\[
\boxed{
\|u(t)\|_2\to\|u(T_*)\|_2
\qquad(t\uparrow T_*).
}
\]

Weak convergence plus convergence of the Hilbert norm therefore gives

\[
\boxed{u(t)\to u(T_*)\quad\text{strongly in }L^2.}
\]

Thus

\[
|u(t)|^2dx
\stackrel{*}{\longrightarrow}
|u(T_*)|^2dx,
\]

and the terminal kinetic-energy measure has no atom.

This is also consistent with the peer-reviewed energy-measure results of Leslie--Shvydkoy, which exclude atomic concentration under suitable strict \(L^q_tL^p_x\) conditions.

## 6. Contradiction with M19-025

M19-025 gives on \(\Lambda_j\ge\Lambda_->0\)

\[
\mu_{def}(\{x_*\})\ge e_*>0.
\]

Section 5 gives

\[
\mu_{def}=0.
\]

Therefore

\[
\boxed{
\sup_{t<T_*}\|u(t)\|_{L^{3,\infty}}<\infty
\quad\Longrightarrow\quad
\text{no nondegenerate remote source sequence}.
}
\]

Equivalently,

\[
\boxed{
\mathcal R_{remote}^{nondeg}
\Longrightarrow
G_{weak\text{-}L^3\ escalation}.
}
\]

## 7. Root recompression

M18 already routes weak-\(L^3\) escalation into the critical/remote boundary complex rather than treating it as a quiet W1 survivor.

Hence the nondegenerate Type-II remote branch is removed from the bounded-W1 corridor.

The genuinely independent remote survivor is now forced toward

\[
\boxed{\Lambda_j\to0}
\]

or toward an already typed weak-\(L^3\)/critical-tail compactness loss.

This is stronger than M19-025 alone: under W1 compactness, the terminal energy atom is not merely exposed but excluded.

## 8. Scope firewall

This module does **not** prove a global bound on \(\|u(t)\|_{L^{3,\infty}}\) for an arbitrary hypothetical singular solution.

Therefore it does not close the full remote root.

It proves only

\[
\boxed{
\text{bounded weak-L3}
+
\text{nondegenerate remote}
\Rightarrow
\text{contradiction}.
}
\]

If weak-\(L^3\) blows up, the branch exits W1 and must be handled by the already identified critical/remote root machinery.

## 9. Next calculation

The remote root has now been reduced chiefly to the dilute branch

\[
\Lambda_j\to0
\]

with logarithmic harmonic-strain halo, plus weak-\(L^3\)/tail escalation.

The next calculation should decide whether the logarithmic halo itself forces weak-\(L^3\) escalation. If so, R-remote would be absorbed almost completely into R-critical. If not, the surviving dilute halo is a genuinely separate Type-II mechanism.

---

\[
\boxed{\text{M19-028 EXCLUDES NONDEGENERATE REMOTE SOURCES INSIDE THE BOUNDED WEAK-L3 CORRIDOR.}}
\]
