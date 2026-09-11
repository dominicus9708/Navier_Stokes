# M19-025 — A nondegenerate remote source forces a terminal kinetic-energy defect atom unless the strong L2 trace fails

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE TO R-CRITICAL REDUCTION / SHRINKING SOURCE ENERGY CONCENTRATION / TERMINAL TRACE DEFECT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Source oscillation lower bound in physical variables

M5-443 gives a fixed normalized source oscillation lower bound. In physical variables, on a source-scale domain \(D_{R_j}\) of diameter comparable to

\[
R_j=K_jr_j,
\]

\[
\inf_c
\|u-c\|_{L^2(D_{R_j})}
\ge
c_0\nu K_j^2R_j^{1/2}.
\]

Squaring,

\[
\boxed{
\inf_c
\int_{D_{R_j}}|u-c|^2dx
\ge
c_0^2\nu^2K_j^4R_j.
}
\]

Since

\[
K_j^4R_j
=K_j^5r_j
=\Lambda_j,
\]

we obtain

\[
\boxed{
\inf_c
\int_{D_{R_j}}|u-c|^2dx
\ge
c_0^2\nu^2\Lambda_j.
}
\]

Taking the particular constant \(c=0\) yields the actual kinetic-energy lower bound

\[
\boxed{
\int_{D_{R_j}}|u(x,t_j)|^2dx
\ge
c_0^2\nu^2\Lambda_j.
}
\]

## 2. Nondegenerate Lambda gives fixed energy in a shrinking region

Assume

\[
\Lambda_j\ge\Lambda_->0.
\]

Then

\[
\boxed{
\int_{D_{R_j}}|u(x,t_j)|^2dx
\ge
e_*
:=c_0^2\nu^2\Lambda_->0.
}
\]

M19-020 gives

\[
R_j\to0.
\]

The remote source center lies at distance \(O(R_j)\) from the corresponding first-hitting center. Along the singular genealogy, those centers converge to the singular point \(x_*\). Therefore

\[
\boxed{
D_{R_j}\subset B_{C R_j}(x_*)
}
\]

for all sufficiently large \(j\), after increasing the geometric constant \(C\).

Hence

\[
\boxed{
\int_{B_{CR_j}(x_*)}|u(x,t_j)|^2dx
\ge e_*>0,
\qquad
CR_j\to0.
}
\]

## 3. Energy measures develop an atom

Define the finite positive measures

\[
\mu_j:=|u(x,t_j)|^2dx.
\]

The kinetic-energy inequality gives

\[
\mu_j(\mathbb R^3)\le E_0.
\]

After extracting a subsequence,

\[
\mu_j\stackrel{*}{\rightharpoonup}\mu
\]

as finite Radon measures.

Fix \(\delta>0\). For large \(j\),

\[
B_{CR_j}(x_*)\subset\overline{B_\delta(x_*)}.
\]

Therefore

\[
\mu_j(\overline{B_\delta(x_*)})\ge e_*.
\]

By weak-* convergence and the closed-set inequality,

\[
\mu(\overline{B_\delta(x_*)})\ge e_*.
\]

Letting \(\delta\downarrow0\),

\[
\boxed{
\mu(\{x_*\})\ge e_*>0.
}
\]

Thus the pre-singular kinetic-energy measures have a nonzero atomic concentration at the singular point.

## 4. Strong L2 terminal trace would exclude the atom

Suppose there exists a terminal velocity

\[
u_*\in L^2(\mathbb R^3)
\]

such that

\[
\boxed{
u(t_j)\to u_*\quad\text{strongly in }L^2.}
\]

Then

\[
|u(t_j)|^2\to|u_*|^2
\quad\text{strongly in }L^1,
\]

so

\[
\mu=|u_*|^2dx.
\]

But an \(L^1\) density has no point atoms:

\[
|u_*|^2dx(\{x_*\})=0.
\]

This contradicts

\[
\mu(\{x_*\})\ge e_*.
\]

Hence

\[
\boxed{
\Lambda_j\ge\Lambda_->0
\Longrightarrow
\text{failure of strong left }L^2\text{ terminal trace at }T_*.
}
\]

## 5. Defect-measure form

Suppose only that

\[
u(t_j)\rightharpoonup u_*
\quad\text{weakly in }L^2.
\]

For every nonnegative compactly supported \(\phi\), weak lower semicontinuity gives

\[
\int\phi|u_*|^2dx
\le
\liminf_j
\int\phi|u(t_j)|^2dx.
\]

Thus the weak-* energy measure has the decomposition

\[
\boxed{
\mu=|u_*|^2dx+\mu_{def},
\qquad
\mu_{def}\ge0.
}
\]

Since the absolutely continuous part has no atom,

\[
\boxed{
\mu_{def}(\{x_*\})\ge e_*.
}
\]

The nondegenerate remote source therefore forces a genuine terminal kinetic-energy concentration defect.

## 6. Relation to the energy jump

If the Leray--Hopf continuation is assigned a value \(u(T_*)\in L^2\), then any atomic defect contributes to the possible left energy drop:

\[
\lim_{t\uparrow T_*}\|u(t)\|_2^2
-
\|u(T_*)\|_2^2
\ge
\mu_{def}(\mathbb R^3)
\ge e_*
\]

provided the chosen subsequence realizes the full left-limit energy measure.

The module does **not** assume that such an energy jump is impossible for a hypothetical singular Leray--Hopf continuation. It identifies the exact defect that must occur.

## 7. Root recompression

The nondegenerate remote branch no longer needs to be regarded as an entirely separate compact-Euler mystery before terminal trace is considered.

It satisfies

\[
\boxed{
\Lambda_j\ge\Lambda_->0
\Longrightarrow
G_{terminal\ kinetic\ energy\ atom/strong\ trace\ failure}.
}
\]

This is naturally part of the M18 critical/realization complex:

\[
\boxed{
\mathcal R_{remote}^{nondeg}
\to
\mathcal R_{critical}^{terminal\ trace/energy\ defect}.
}
\]

The ancient Euler limit remains a useful representation of the same branch, but the parent-coordinate defect is already visible without an Euler Liouville theorem.

## 8. What remains genuinely remote

The unresolved remote source route is therefore sharpened to

\[
\boxed{
\mathcal R_{remote}
\Longrightarrow
\begin{cases}
\Lambda_j\to0
&\text{(Euler velocity/low-frequency energy dilution)},\\
G_{source\ derivative/frequency/tail\ noncompact},\\
\mathcal R_{critical}^{terminal\ energy\ defect}.
\end{cases}
}
\]

The last line is transferred to R-critical.

## 9. Next calculation

The highest-value next task is the dilute branch

\[
\boxed{
\Lambda_j=K_j^5r_j\to0.
}
\]

M19-026 should determine whether the fixed source oscillation lower bound plus bounded Euler-scaled vorticity forces a minimum growth of a harmonic/low-frequency velocity component when \(\Lambda_j\to0\), and whether that component can be routed to the already identified critical tail / remote-of-remote structure.

---

\[
\boxed{\text{M19-025 CONVERTS THE NONDEGENERATE REMOTE SOURCE INTO A TERMINAL ENERGY-DEFECT ROOT.}}
\]
