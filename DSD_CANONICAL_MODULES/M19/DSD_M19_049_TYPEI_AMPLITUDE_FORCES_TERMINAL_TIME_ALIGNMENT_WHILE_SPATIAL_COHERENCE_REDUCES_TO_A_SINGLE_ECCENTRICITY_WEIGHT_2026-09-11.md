# M19-049 — Type-I amplitude forces terminal-time alignment while spatial coherence reduces to a single eccentricity weight

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC KINETIC-MORREY REPRESENTATION / TEMPORAL ALIGNMENT CLOSED / SPATIAL ECCENTRICITY FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-048 reduces the retained quiet compact R-AC survivor to shell-local kinetic Morrey charges

\[
\boxed{
\mathcal M_k^{own}
:=
\frac1{\rho_k}
\inf_c
\int_{E_k^+}|u(x,t_k)-c|^2dx
\gtrsim J_k,
}
\]

with

\[
\sum_kJ_k^{3/2}=\infty,
\qquad
\frac{J_k}{\rho_k}\to\infty
\]

in cubic-mass density on extracted geometric shrinking-radius blocks.

The remaining representation question is whether these moving-center shell witnesses form one terminal critical stack.

## 2. Cubic-dominant amplitude diverges

M19-046 gives the pointwise shell amplitude floor

\[
\|\omega(t_k)\|_\infty
\ge
c_\omega
\frac{J_k^{1/2}}{\rho_k^2}.
\]

Define

\[
A_k
:=
\frac{J_k^{1/2}}{\rho_k^2}.
\]

Since

\[
\frac{J_k}{\rho_k}\to\infty
\]

and

\[
\rho_k\to0,
\]

we can write

\[
A_k
=
\left(\frac{J_k}{\rho_k}\right)^{1/2}
\rho_k^{-3/2}.
\]

Hence

\[
\boxed{A_k\to\infty.}
\]

Thus every cubic-dominant kinetic-Morrey shell is necessarily attached to arbitrarily large physical vorticity amplitude.

## 3. First-hitting times force terminal alignment

Choose the first-hitting stage \(n(k)\) satisfying

\[
W_{n(k)}\asymp A_k.
\]

Because

\[
A_k\to\infty,
\]

we have

\[
n(k)\to\infty.
\]

On the Type-I corridor,

\[
\Theta_n
=W_n(T_*-t_n)
\le\Theta_+,
\]

so

\[
T_*-t_{n(k)}
\lesssim
A_k^{-1}
=
\frac{\rho_k^2}{J_k^{1/2}}.
\]

A shell contact carrying the amplitude floor cannot occur before its corresponding first-hitting amplitude is available. Therefore

\[
t_k\ge t_{n(k)}.
\]

Hence

\[
0<T_*-t_k
\le
T_*-t_{n(k)}
\lesssim
\frac{\rho_k^2}{J_k^{1/2}}.
\]

Since \(J_k/\rho_k\to\infty\),

\[
\frac{\rho_k^2}{J_k^{1/2}}
=
\rho_k^{3/2}
\left(\frac{\rho_k}{J_k}\right)^{1/2}
\to0.
\]

Therefore

\[
\boxed{t_k\uparrow T_*}
\]

along every cubic-dominant extracted shell sequence.

This closes the temporal-placement part of the R-AC kinetic-Morrey representation problem on the Type-I corridor.

## 4. Spatial center split

Let \(x_k\) be the physical center of the shell witness.

If

\[
|x_k|\to\infty
\]

or the centers have an unbounded subsequence, this is genuine physical export and is already typed by the remote/export analysis.

Thus on the retained no-export branch assume

\[
\sup_k|x_k|<\infty.
\]

By subsequence extraction,

\[
\boxed{x_k\to x_\infty}
\]

for some finite physical point \(x_\infty\).

This physical convergence is enough to define a common-center eccentricity, but not enough to make that eccentricity bounded in shell units.

## 5. Exact common-center eccentricity factor

Define

\[
\boxed{
\eta_k
:=
\frac{|x_k-x_\infty|}{\rho_k}.
}
\]

Let \(C_E\rho_k\) be a radius containing the enlarged shell collar \(E_k^+\) around \(x_k\).

Set

\[
R_k^{com}
:=
|x_k-x_\infty|+C_E\rho_k
=
\rho_k(\eta_k+C_E).
\]

Then

\[
E_k^+
\subset
B_{R_k^{com}}(x_\infty).
\]

For every constant \(c\),

\[
\int_{B_{R_k^{com}}(x_\infty)}|u-c|^2dx
\ge
\int_{E_k^+}|u-c|^2dx.
\]

Taking the infimum over \(c\),

\[
\inf_c
\int_{B_{R_k^{com}}(x_\infty)}|u-c|^2dx
\ge
\inf_c
\int_{E_k^+}|u-c|^2dx.
\]

Therefore the common-center kinetic Morrey charge obeys

\[
\begin{aligned}
\mathcal M_k^{com}
&:=
\frac1{R_k^{com}}
\inf_c
\int_{B_{R_k^{com}}(x_\infty)}|u(x,t_k)-c|^2dx\\
&\gtrsim
\frac{J_k\rho_k}{\rho_k(\eta_k+C_E)}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal M_k^{com}
\gtrsim
\frac{J_k}{\eta_k+C_E}.
}
\]

This is the exact spatial-coherence loss factor.

## 6. Bounded eccentricity carries the full cubic divergence into one terminal center

If on a subset \(\mathcal K\)

\[
\sup_{k\in\mathcal K}\eta_k<\infty,
\]

then

\[
\mathcal M_k^{com}
\gtrsim
J_k.
\]

Thus if \(\mathcal K\) carries divergent cubic shell mass,

\[
\sum_{k\in\mathcal K}J_k^{3/2}=\infty,
\]

we obtain

\[
\boxed{
\sum_{k\in\mathcal K}
(\mathcal M_k^{com})^{3/2}
=\infty.
}
\]

Together with

\[
t_k\uparrow T_*,
\]

this gives a terminal common-center nonsummable kinetic-Morrey genealogy.

It is stronger than a collection of unrelated moving-center witnesses, but still weaker than a fixed positive Morrey floor because \(J_k\) may tend to zero.

## 7. Cubic-mass weighted eccentricity deficiency

Define the coherence factor

\[
\boxed{
b_k:=\frac1{\eta_k+C_E}.}
\]

Then

\[
\mathcal M_k^{com}
\gtrsim
b_kJ_k.
\]

If

\[
\sum_k(b_kJ_k)^{3/2}=\infty,
\]

then the terminal common-center kinetic branch carries nonsummable cubic Morrey mass.

If instead

\[
\sum_kb_k^{3/2}J_k^{3/2}<\infty
\]

while

\[
\sum_kJ_k^{3/2}=\infty,
\]

then exactly as in the return-deficiency argument, the cubic-mass weighted average satisfies

\[
\frac{
\sum_{k\le N}b_k^{3/2}J_k^{3/2}
}{
\sum_{k\le N}J_k^{3/2}
}
\to0.
\]

Moreover for every fixed \(\varepsilon>0\), the sector

\[
\{k:b_k\ge\varepsilon\}
\]

carries only finite cubic mass.

Equivalently, for every fixed \(E<\infty\),

\[
\boxed{
\sum_{k:\eta_k\le E}J_k^{3/2}<\infty
}
\]

in the spatially deficient survivor.

Thus all divergent cubic mass is forced onto increasingly eccentric shell witnesses.

## 8. Temporal versus spatial synchronization

The earlier R-AC formulation mixed two possible decorrelations:

1. wrong historical time / record phase;
2. wrong spatial center.

M19-049 shows that on the cubic-dominant Type-I kinetic branch, the first is gone:

\[
\boxed{t_k\uparrow T_*\text{ automatically}.}
\]

The only remaining common-center representation loss is

\[
\boxed{
\eta_k
=
|x_k-x_\infty|/\rho_k.
}
\]

Therefore the active R-AC representation problem has become spatial rather than temporal.

## 9. Relation to M19-032--044

M19-032 already proves that bounded eccentricity plus terminal alignment produces a critical Morrey stack when each event has a fixed positive own-scale floor.

M19-049 extends the geometry to the variable-charge situation:

\[
\mathcal M_k^{com}
\gtrsim
J_k/(1+\eta_k).
\]

M19-044 classifies unbounded-center export separately and shows there is no independent quiet remote root.

Thus the new unresolved survivor is exactly:

\[
\boxed{
\text{bounded physical centers}
+\text{terminal times}
+\text{cubic mass concentrated on }\eta_k\to\infty.
}
\]

This is an off-center critical genealogy, not a return-count problem.

## 10. New theorem frontier

Define

\[
\boxed{
\mathcal T_{ecc}^{cubic}:
\sum_kJ_k^{3/2}=\infty,
\quad
\frac{J_k}{\rho_k}\to\infty\text{ in cubic-mass density},
\quad
\eta_k\to\infty\text{ in cubic-mass density}
}
\]

for terminally aligned kinetic-Morrey shell witnesses with bounded physical centers.

The next question is whether such an increasingly eccentric terminal family can remain spatially sparse without either

- generating enough same-shell multiplicity to recover a common-center critical Morrey/scattering tail;
- forcing physical center turnover/export;
- or producing a new smaller-scale remote/high-frequency event already typed upstream.

## 11. What is not proved

M19-049 does not prove bounded eccentricity.

It does not prove that nonsummable common-center Morrey charges produce a nonzero scattering datum.

It does not identify moving shell centers with one material point unless separately certified.

It proves temporal terminal alignment and isolates the exact remaining spatial coherence factor.

## 12. Next calculation

The highest-value next target is the eccentricity survivor.

Use the controlled center-drift estimate from M19-039 together with the Type-I remaining-time bound from M19-046.

For one shell event,

\[
|\dot X|\lesssim \rho^{-1}
\]

and

\[
T_*-t_k\lesssim \rho^2/J^{1/2}.
\]

If the **same persistent center trajectory** survives from the shell event to the terminal point, its remaining displacement is at most order

\[
\boxed{
\rho/J^{1/2}.
}
\]

which means

\[
\eta_k\lesssim J_k^{-1/2}.
\]

Then the common-center Morrey charge would satisfy

\[
\mathcal M_k^{com}
\gtrsim
J_k^{3/2}.
\]

The next module must audit whether the current genealogy actually certifies that same-center trajectory to \(T_*\), or whether failure is precisely a center-turnover/population-replacement exit.

---

\[
\boxed{\text{M19-049 COMPLETE; TEMPORAL ALIGNMENT IS CLOSED AND R-AC REDUCES TO CUBIC-MASS-WEIGHTED SPATIAL ECCENTRICITY.}}
\]