# M19-024 — Nondegenerate K^5 r gives a global source L2 bound and splits the ancient Euler limit into energy-tight or escape-to-source-infinity

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE GLOBAL ENERGY / EULER TIGHTNESS SPLIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Source normalization

Use the original physical inertial frame from M19-023:

\[
V_j(y,\tau)
=
\frac{u(x_j^s+R_jy,t_j+T_j^E\tau)}{U_j^E}.
\]

Recall

\[
(U_j^E)^2R_j^3
=
\nu^2\Lambda_j,
\qquad
\Lambda_j:=K_j^5r_j.
\]

## 2. Exact global L2 scaling

Changing variables on all of \(\mathbb R^3\),

\[
\boxed{
\|V_j(\tau)\|_{L^2(\mathbb R^3)}^2
=
\frac{
\|u(t_j+T_j^E\tau)\|_2^2
}{\nu^2\Lambda_j}.
}
\]

Hence if

\[
\Lambda_j\ge\Lambda_->0,
\]

then the physical kinetic-energy inequality gives

\[
\boxed{
\sup_{\tau\in[-T,0]}
\|V_j(\tau)\|_2^2
\le
\frac{E_0}{\nu^2\Lambda_-}
}
\]

for every fixed backward Euler-time window.

Thus the nondegenerate remote branch has a global source-scale \(L^2\) bound, not merely local velocity variance control.

## 3. Weak global L2 limit

M19-022--023 give strong local \(L^2\) convergence after extraction:

\[
V_j\to V
\quad\text{in }L^2_{loc}.
\]

The global bound also gives

\[
V_j\rightharpoonup V
\quad\text{weak-* in }L^\infty_{loc}((-\infty,0];L^2(\mathbb R^3)).
\]

Therefore

\[
\boxed{
V\in L^\infty_{loc}((-\infty,0];L^2(\mathbb R^3)).
}
\]

The compact Euler limit is a finite-energy ancient Euler solution.

## 4. Energy tightness is an additional issue

Weak global \(L^2\) convergence does not imply

\[
\|V_j\|_2^2\to\|V\|_2^2.
\]

Define source-space tail energy

\[
\boxed{
\mathcal T_j(L,\tau)
:=
\int_{|y|>L}|V_j(y,\tau)|^2dy.
}
\]

There are two cases.

### A. Energy-tight branch

For every fixed compact time interval,

\[
\boxed{
\lim_{L\to\infty}
\sup_j\sup_{\tau\in[-T,0]}
\mathcal T_j(L,\tau)
=0.
}
\]

Then local strong \(L^2\) convergence upgrades to global strong \(L^2\):

\[
\boxed{
V_j\to V
\quad\text{strongly in }L^2(\mathbb R^3)
}
\]

at the corresponding times, and similarly in spacetime after the usual compactness argument.

### B. Energy-escape branch

There exist \(\eta_*>0\), radii \(L_n\to\infty\), and indices/times such that

\[
\boxed{
\int_{|y|>L_n}|V_{j_n}|^2dy
\ge\eta_*.
}
\]

Then a fixed portion of normalized source energy escapes to source-space infinity.

This is not failure of local Euler compactness; it is a genuine global source-tail defect.

## 5. Physical interpretation of source-space infinity

The region

\[
|y|>L
\]

corresponds to physical distance

\[
|x-x_j^s|>LR_j.
\]

Since M19-020 gives

\[
R_j\to0,
\]

source-space infinity does not automatically mean physical infinity.

For fixed \(L\), the physical radius \(LR_j\) still shrinks to the singular point.

Therefore the escape branch must be interpreted as a **multiscale energy halo around the shrinking Type-II source**, not automatically as macroscopic spatial export.

This distinction is mandatory.

## 6. A two-scale version

Choose \(L_j\to\infty\) with

\[
L_jR_j\to0.
\]

If

\[
\int_{|y|>L_j}|V_j|^2dy
\ge\eta_*,
\]

then the escaped source energy still lies, in physical variables, outside a radius larger than the main source scale but inside a radius tending to zero.

This is a genuine intermediate-scale concentration cascade.

If instead one needs

\[
L_jR_j\not\to0

to capture the escaped energy, the defect reconnects to the broader remote/macroscopic-tail root.

Thus source-space energy escape naturally splits into

\[
\boxed{
G_{intermediate\ concentration\ halo}
\lor
G_{macroscopic\ remote/tail}.
}
\]

## 7. Energy-tight branch gives a stronger Euler object

If source energy is tight, the limit satisfies

\[
\boxed{
V\in L^\infty_{loc}(( -\infty,0];L^2(\mathbb R^3))
}
\]

and is obtained by global strong \(L^2\) convergence on compact time intervals.

Together with the inherited bounded-vorticity normalization,

\[
\|\omega_V\|_\infty\le q,
\]

this is a substantially narrower Euler rigidity class than the local object of M5-443.

It is still not known here to be trivial.

## 8. Updated compact remote split

The nondegenerate remote source branch now satisfies

\[
\boxed{
\Lambda_j\ge\Lambda_->0
\Longrightarrow
\begin{cases}
E_{ancient}^{Euler,finite\ energy,tight},\\
G_{intermediate\ energy\ halo},\\
G_{macroscopic\ remote/tail}.
\end{cases}
}
\]

The first line is the next Euler-rigidity candidate.

## 9. Next calculation

The source oscillation lower bound and \(\Lambda_j\ge\Lambda_->0\) imply a fixed amount of **physical kinetic energy** inside a ball whose radius \(R_j\to0\).

M19-025 should calculate this concentration in the original variables and identify whether it forces a terminal kinetic-energy concentration defect at the singular point.

That route is independent of any Euler Liouville theorem and may be stronger than attacking the ancient Euler profile directly.

---

\[
\boxed{\text{M19-024 COMPLETE; NONDEGENERATE REMOTE SOURCES ARE FINITE-ENERGY EULER SOURCES, WITH GLOBAL TAIL TIGHTNESS AS THE NEXT SPLIT.}}
\]
