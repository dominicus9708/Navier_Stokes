# M19-032 — A nested remote cascade with bounded center eccentricity forces critical Morrey activity at the accumulation point

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE TO R-CRITICAL BRIDGE / CENTER-ECCENTRICITY SPLIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Nested common-frame branch from M19-031

Work on the finite-path nested branch

\[
x_m\to x_\infty,
\qquad
r_m\to0.
\]

Assume the selected physical event times satisfy

\[
t_m\uparrow T_*
\]

along the singular genealogy. If this terminal-time alignment fails, record a historical/return-placement defect rather than silently treating the events as one terminal critical stack.

## 2. Certified first-hitting velocity-variance floor

The first-hitting normalization and the earlier M18 clock/variance calculation provide a fixed normalized local velocity-variance floor. In natural physical variables this has the form

\[
\boxed{
\inf_{c\in\mathbb R^3}
\int_{B_{Cr_m}(x_m)}
|u(x,t_m)-c|^2dx
\ge
v_*\nu^2r_m
}
\]

for fixed constants

\[
C<\infty,
\qquad
v_*>0.
\]

This is the natural scaling: velocity amplitude is \(\nu/r_m\), volume is \(r_m^3\), hence the kinetic variance is order \(\nu^2r_m\).

## 3. Recenter at the physical accumulation point

Define the center eccentricity

\[
\boxed{
\eta_m
:=
\frac{|x_m-x_\infty|}{r_m}.
}
\]

Let

\[
\rho_m
:=
|x_m-x_\infty|+Cr_m
=r_m(\eta_m+C).
\]

Then

\[
B_{Cr_m}(x_m)
\subset
B_{\rho_m}(x_\infty).
\]

Therefore

\[
\inf_c
\int_{B_{\rho_m}(x_\infty)}
|u-c|^2dx
\ge
v_*\nu^2r_m.
\]

Divide by \(\rho_m\):

\[
\boxed{
\frac1{\rho_m}
\inf_c
\int_{B_{\rho_m}(x_\infty)}
|u(x,t_m)-c|^2dx
\ge
\frac{v_*\nu^2}{\eta_m+C}.
}
\]

This is an exact critical Morrey-scale variance estimate at the common accumulation point.

## 4. Bounded eccentricity gives an R-critical event

Suppose

\[
\boxed{
\sup_m\eta_m\le E_*<\infty.
}
\]

Then

\[
\boxed{
\frac1{\rho_m}
\inf_c
\int_{B_{\rho_m}(x_\infty)}
|u-c|^2dx
\ge
\frac{v_*\nu^2}{E_*+C}
=:
\mathfrak m_*>0.
}
\]

Since

\[
\rho_m=r_m(\eta_m+C)\to0,
\]

we obtain a terminal stack of scale-invariant kinetic Morrey activity at the single physical point \(x_\infty\).

Thus

\[
\boxed{
\text{nested remote cascade}
+
\sup_m\frac{|x_m-x_\infty|}{r_m}<\infty
\Longrightarrow
\mathcal R_{critical}^{Morrey}.
}
\]

The remote branch has merged into R-critical on this subcase.

## 5. Unbounded eccentricity is the genuine off-center branch

If

\[
\eta_m\to\infty
\]

along a subsequence, then

\[
\frac{r_m}{\rho_m}
=
\frac1{\eta_m+C}
\to0.
\]

The local first-hitting energy witness still exists at \(x_m\), but it becomes too eccentric relative to the common accumulation point to create a fixed Morrey floor there.

This is not loss of the local witness. It is a geometric/genealogical decorrelation:

\[
\boxed{
\text{event scale }r_m
\ll
\text{distance from event center to common accumulation point}.
}
\]

Hence the remaining nested remote branch is an **off-center scale cascade**.

## 6. Relation to remote geometry

Although

\[
x_m\to x_\infty,
\]

unbounded \(\eta_m\) means that from the perspective of its own natural scale the event center remains remote from the final accumulation point:

\[
\frac{|x_m-x_\infty|}{r_m}\to\infty.
\]

Thus the chain can converge physically while remaining infinitely remote in its own scale coordinates.

This explains why physical-center convergence alone does not automatically produce a critical single-center stack.

## 7. Temporal alignment split

The preceding R-critical conclusion also requires that the selected event times belong to one terminal genealogy:

\[
t_m\uparrow T_*.
\]

If the spatial conditions hold but the events occur on separated historical epochs without terminal alignment, the correct routing is not R-critical Morrey concentration but

\[
\boxed{
G_{historical\ return/time\ placement}
}

which belongs to the R-AC interface.

Thus the full common-center split is

\[
\boxed{
\begin{aligned}
G_{nested\ remote}
\Longrightarrow{}&
G_{bounded\ eccentricity+terminal\ alignment\to R\text{-}critical}\\
&\lor
G_{off\text{-}center\ eccentricity}\\
&\lor
G_{historical/time\ placement\to R\text{-}AC}.
\end{aligned}
}
\]

## 8. Off-center branch and R-AC

On the off-center branch, the unresolved issue is not the existence of local critical activity. Each generation already has it in its own ball.

The issue is whether these moving-center scale witnesses can be embedded into one fixed-parent nonreused event family with sufficient return occupancy.

That is structurally the same kind of representation/genealogy problem exposed by

\[
\boxed{\mathcal T_{AC}.}
\]

Hence the new missing bridge is narrowed further to

\[
\boxed{
\mathcal B_{ecc}:
\eta_m\to\infty
\Longrightarrow
\text{R-AC event embedding / return deficiency}
\lor
\text{critical-tail export}.
}
\]

## 9. Remote-root status after this calculation

Combining M19-029--032:

1. strong remote throughput \(\to\) weak-\(L^3\) escalation;
2. quiet detached finite termination \(\to\) contradiction or typed exit;
3. infinite remote recursion \(\to\) common-frame scale/path alternatives;
4. finite-path nested recursion with bounded center eccentricity \(\to\) R-critical Morrey activity.

Therefore the genuinely independent remote remainder is now largely an off-center/historical representation problem rather than a new local PDE payer.

## 10. Next calculation

M19-033 should attack the off-center eccentricity branch by comparing the sequence

\[
\eta_m=\frac{|x_m-x_\infty|}{r_m}
\]

with the parent first-hitting age ratio and the fixed-lag contact/replacement genealogy.

The target is to show that large \(\eta_m\) either

- forces spatial export through successively disjoint annuli;
- requires repeated fresh-carrier replacement, hence finite-memory typed exits;
- or realizes precisely the sparse return-incidence defect \(\mathcal T_{AC}\).

---

\[
\boxed{\text{M19-032 COMPLETE; BOUNDED-ECCENTRICITY NESTED REMOTE CASCADES ARE R-CRITICAL MORREY CASCADES.}}
\]
