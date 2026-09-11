# M19-028 — Bounded weak-L3 plus the energy class excludes the nondegenerate remote energy-atom branch

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE TO W1 INTERFACE / L4 ENERGY EQUALITY / NONDEGENERATE REMOTE EXCLUSION UNDER WEAK-L3 COMPACTNESS

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-025

M19-025 proves that if

\[
\Lambda_j=K_j^5r_j\ge\Lambda_->0,
\]

then the pre-singular kinetic-energy measures develop a fixed atom at the singular point, equivalently a strong left terminal \(L^2\) trace fails.

## 2. Bounded weak-L3 assumption

Assume on a terminal interval \([t_0,T_*)\)

\[
\boxed{
\sup_{t_0<t<T_*}
\|u(t)\|_{L^{3,\infty}(\mathbb R^3)}
\le M<\infty.
}
\]

This is the physical form of the bounded weak-critical W1 corridor.

## 3. Energy class and interpolation

The finite-energy identity and Sobolev give

\[
\boxed{u\in L^2(t_0,T_*;L^6(\mathbb R^3)).}
\]

The Lorentz interpolation estimate

\[
\|f\|_4
\le
C\|f\|_{L^{3,\infty}}^{1/2}\|f\|_6^{1/2}
\]

implies

\[
\|u(t)\|_4^4
\le
CM^2\|u(t)\|_6^2.
\]

Therefore

\[
\boxed{u\in L^4(t_0,T_*;L^4(\mathbb R^3)).}
\]

## 4. Energy equality and strong terminal trace

The classical Lions--Shinbrot energy-equality criterion applies to \(L^4_tL^4_x\). Thus there is no anomalous kinetic-energy loss at \(T_*\).

For the Leray--Hopf weak continuation,

\[
u(t)\rightharpoonup u(T_*)
\]

should be read simply as the usual weak convergence of the velocity field \(u(t)\) to \(u(T_*)\). Energy equality gives

\[
\|u(t)\|_2\to\|u(T_*)\|_2.
\]

Weak convergence plus convergence of the Hilbert norm yields

\[
\boxed{u(t)\to u(T_*)\quad\text{strongly in }L^2.}
\]

Consequently

\[
|u(t)|^2dx
\stackrel{*}{\longrightarrow}
|u(T_*)|^2dx,
\]

and the terminal energy measure has no point atom.

This agrees with the peer-reviewed energy-measure results of Leslie--Shvydkoy under strict \(L^q_tL^p_x\) hypotheses.

## 5. Contradiction with M19-025

M19-025 gives

\[
\mu_{def}(\{x_*\})\ge e_*>0
\]

on the nondegenerate remote branch, while Section 4 gives

\[
\mu_{def}=0.
\]

Hence

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

## 6. Root recompression

The nondegenerate Type-II remote branch is therefore removed from the bounded-W1 corridor.

The independent remote survivor is forced toward

\[
\boxed{\Lambda_j\to0}
\]

or toward an already typed weak-\(L^3\)/critical-tail compactness loss.

## 7. Scope firewall

This module does not prove a uniform weak-\(L^3\) bound for an arbitrary hypothetical singular solution. It proves only

\[
\boxed{
\text{bounded weak-L3}
+
\text{nondegenerate remote}
\Rightarrow
\text{contradiction}.
}
\]

## 8. Next calculation

The next remote calculation should test whether the dilute logarithmic harmonic-strain halo itself forces weak-\(L^3\) escalation. If so, R-remote would be absorbed almost completely into R-critical; if not, the dilute halo remains an independent Type-II mechanism.

---

\[
\boxed{\text{M19-028 EXCLUDES NONDEGENERATE REMOTE SOURCES INSIDE THE BOUNDED WEAK-L3 CORRIDOR.}}
\]
