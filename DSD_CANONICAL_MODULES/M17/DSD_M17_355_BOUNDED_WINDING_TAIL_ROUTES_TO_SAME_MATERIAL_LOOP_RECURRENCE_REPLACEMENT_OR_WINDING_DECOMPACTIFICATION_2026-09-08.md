# DSD M17-355 — A bounded/winding tail routes to same-material loop recurrence, replacement, or winding decompactification

Date: 2026-09-08  
Canonical ID: **M17-355**

Status: **ACTIVE TAIL-TO-EXISTING-LOOP-BRANCH ROUTING / NO NEW LIOUVILLE CLAIM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-349--354

The coefficient-compact exterior branch with unbounded vortex-line coverage and uniformly bounded normalized harmonic onset is closed by M17-353--354.

The remaining geometric exterior alternative is that arbitrarily far active tail points lie on vortex lines/components that remain in bounded radial ranges rather than reaching spatial infinity.

Call this

\[
G_{bounded/winding\ tail}.
\]

The goal is to replace this broad label by explicit material alternatives.

## 2. Record-scale normalization

At a backward record radius `R_m`, use the M5-478 cell coordinates

\[
y=x/R_m.
\]

A physical tail line contained in an annular radial range comparable to `R_m` becomes a line/component in a fixed normalized annulus.

On the bounded tail-cell lane, field amplitudes and derivatives are compact on fixed annuli.  Therefore the only geometric noncompactness left inside one normalized annulus is in the **line representation itself**: length, winding/reuse, endpoints/interfaces, or label replacement.

## 3. Material-loop alternatives

Follow one activity-carrying normalized bounded line/component through the material flow whenever the label survives.

There are three mutually exhaustive structural alternatives along a subsequence:

### A. Compact same-material loop recurrence

The same material loop returns inside a compact nondegenerate loop class with comparable

\[
\ell_\Gamma,
\qquad
L_\rho,
\qquad
\Phi.
\]

Then the existing M17-188 theorem applies.

### B. Material replacement / repartition

No same material loop survives long enough to recur because the active tail is repeatedly reassigned through

\[
\boxed{
G_{loop\ replacement/interface/genealogy}.
}
\]

This is not allowed to masquerade as recurrence of one loop.

### C. Winding/length decompactification

A same-label line survives but its normalized arclength/reuse number escapes every compact loop class:

\[
\boxed{
G_{winding/length\ decompactification}.
}
\]

This includes increasingly wound annular lines and repeated reuse of the same geometric region by a long material line.

## 4. Same-material recurrent loop returns to M17-188

On branch A, M17-188 gives the exact material laws

\[
\frac d{d\theta}\log\ell_\Gamma
=
\bar\sigma_{ds}+\frac12,
\]

\[
\frac d{d\theta}\log L_\rho
=
\kappa-\frac12+2\bar\sigma_\rho,
\]

and

\[
\frac d{d\theta}\log\Phi=
\kappa.
\]

Comparable recurrent endpoint values force

\[
\boxed{
\langle\bar\sigma_{ds}\rangle=-\frac12,
}
\]

\[
\boxed{
\langle\kappa\rangle=0,
}
\]

and

\[
\boxed{
\langle\bar\sigma_\rho\rangle=\frac14.
}
\]

Hence

\[
\boxed{
\left\langle
\bar\sigma_\rho-
\bar\sigma_{ds}
\right\rangle
=
\frac34.
}
\]

## 5. Tangential-gradient payer on the compact recurrent loop

M17-188 identifies the difference as the normalized line covariance of `sigma` and `rho`.

Circle Poincare and Cauchy--Schwarz give, under compact loop bounds,

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_{L^2(\Gamma)}
\|\partial_s\rho\|_{L^2(\Gamma)}
\right\rangle
\ge c_*>0.
}
\]

Thus branch A is not a cost-free topology exit.  It enters the existing strain-gradient / amplitude-gradient payer architecture.

This remains an occupancy statement, not yet a finite global dissipation contradiction.

## 6. Kappa dynamics on the recurrent loop

Because exact CE-H gives

\[
D_\xi\kappa=0,
\]

one connected regular vortex loop has one scalar material value

\[
\kappa_\Gamma(\theta).
\]

The recurrent flux condition forces

\[
\langle\kappa_\Gamma\rangle=0.
\]

Therefore the same-loop branch further splits into

\[
\boxed{
H_{\kappa\text{-}phase\ locking\ near\ 0}
\lor
H_{positive/negative\ loop\ excursions}.
}
\]

If both signs persist with nonvanishing excursion mass on a compact same-label hull, the fixed-generation crossing arguments M17-332--334 apply and generate nonzero material coefficient variation / crossing frequency.

If the loop remains locked near `kappa=0`, it enters the zero-level/degenerate-jet geometry rather than an unrelated topology branch.

## 7. Updated bounded-tail routing

Hence

\[
\boxed{
\begin{aligned}
G_{bounded/winding\ tail}
\Longrightarrow{}&
H_{closed\ loop\ gradient\ payer}\\
&\lor H_{same\text{-}loop\ zero\text{-}level\ dynamics}\\
&\lor G_{loop\ replacement/interface/genealogy}\\
&\lor G_{winding/length\ decompactification}.
\end{aligned}
}
\]

The old generic topology exit is therefore refined but not fully closed.

## 8. DSD-theory role

The useful heuristic is identity preservation: recurrence of a geometric loop position is not recurrence of the same material loop.

The actual routing uses standard material-flow identity, the exact CE-H line constancy, and the already derived M17-188 line laws.

No DSD axiom enters the PDE.

## 9. Next target

The highest-value new branch is

\[
\boxed{G_{winding/length\ decompactification}.}
\]

A quantitative theorem should test whether arbitrarily large normalized winding can coexist with the compact all-order CE-H coefficient bounds, finite enstrophy, and the fixed annular tail marks without forcing either line reuse/intersection, vanishing flux per turn, or a growing curvature/director-gradient charge.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
