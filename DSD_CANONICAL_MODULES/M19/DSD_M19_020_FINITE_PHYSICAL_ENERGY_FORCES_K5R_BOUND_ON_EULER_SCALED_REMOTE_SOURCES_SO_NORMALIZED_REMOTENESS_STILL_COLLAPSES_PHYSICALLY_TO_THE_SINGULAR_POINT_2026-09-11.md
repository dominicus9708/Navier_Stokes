# M19-020 — Finite physical energy forces a K^5 r bound on Euler-scaled remote sources, so normalized remoteness still collapses physically to the singular point

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE ENTRY / TYPE-II EULER-SCALE ENERGY CONSTRAINT / PHYSICAL-LOCALITY REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M5-443 gives the canonical Type-II remote-source scaling.

At first-hitting natural scale

\[
r_j=\sqrt{\frac{\nu}{W_j}},
\]

a strong remote source lies at source scale

\[
R_j=K_jr_j,
\qquad K_j\to\infty,
\]

with Euler velocity scale

\[
\boxed{
U_j^E
=\frac{\nu K_j^2}{R_j}
=\frac{\nu K_j}{r_j}.
}
\]

The Euler time scale is

\[
T_j^E=\frac{R_j}{U_j^E}=\frac{r_j^2}{\nu},
\]

and the normalized viscosity is

\[
\varepsilon_j=K_j^{-2}\to0.
\]

The source nontriviality survives as a fixed local oscillation lower bound

\[
\boxed{
\inf_c\|V_j-c\|_{L^2(D_1)}
\ge c_0>0.
}
\]

## 2. Convert normalized source energy back to the physical parent

Write

\[
V_j(y,0)
=\frac{u(x_j^s+R_jy,t_j)-c_j}{U_j^E}.
\]

Hence

\[
\int_{D_{R_j}(x_j^s)}|u-c_j|^2dx
=(U_j^E)^2R_j^3
\int_{D_1}|V_j|^2dy.
\]

Using the fixed oscillation lower bound,

\[
\boxed{
E_{src,j}^{osc}
\gtrsim
(U_j^E)^2R_j^3.
}
\]

Now

\[
(U_j^E)^2R_j^3
=
\left(\frac{\nu K_j^2}{R_j}\right)^2R_j^3
=\nu^2K_j^4R_j.
\]

Since

\[
R_j=K_jr_j,
\]

we obtain

\[
\boxed{
E_{src,j}^{osc}
\gtrsim
\nu^2K_j^5r_j.
}
\]

## 3. Finite physical kinetic energy gives an upper growth law for K

The original finite-energy solution has a uniform kinetic-energy bound

\[
\|u(t)\|_2^2\le E_0<\infty.
\]

A Galilean constant must be handled locally because the global \(L^2\) energy is not Galilean invariant on \(\mathbb R^3\). The source oscillation in M5-443 is measured by an infimum over constants on the source region, and the corresponding local variance is bounded above by a fixed multiple of the local kinetic energy after choosing the local mean/minimizer. Thus on the controlled source region,

\[
E_{src,j}^{osc}\lesssim E_0
\]

up to the fixed localization convention.

Combining with Section 2 gives

\[
\boxed{
\nu^2K_j^5r_j
\lesssim E_0.
}
\]

Equivalently,

\[
\boxed{
K_j
\lesssim
C_E r_j^{-1/5},
}
\]

where the constant absorbs \(E_0\) and \(\nu\).

This is a genuine finite-energy restriction on Type-II remoteness.

## 4. The remote source scale still collapses physically

Because

\[
R_j=K_jr_j,
\]

Section 3 gives

\[
R_j
\lesssim
C_Er_j^{4/5}.
\]

Since

\[
r_j\to0,
\]

we obtain

\[
\boxed{
R_j\to0.
}
\]

Thus

\[
\boxed{
K_j\to\infty
\quad\text{does not imply a physically remote source at a fixed macroscopic distance.}
}
\]

The source is remote only relative to the much smaller first-hitting natural scale \(r_j\).

In original coordinates, every finite-energy strong Type-II source allowed by this scaling still collapses into the singular point/region.

## 5. Separation from genuine physical export

Suppose instead a source stayed at physical scale/distance bounded below:

\[
R_j\ge R_*>0.
\]

Then

\[
K_j=\frac{R_j}{r_j}
\gtrsim r_j^{-1}.
\]

Consequently

\[
K_j^5r_j
\gtrsim r_j^{-4}\to\infty,
\]

contradicting the finite-energy bound of Section 3.

Therefore the M5-443 strong source with the fixed normalized oscillation lower bound cannot persist at a fixed physical scale.

A genuinely macroscopic export branch must lose at least one of the M5-443 strong-source hypotheses or be represented by a different, weaker remote mechanism.

## 6. Vorticity amplitude remains bounded in Euler variables

M5-443 gives

\[
\boxed{
\|\Omega_j^E\|_\infty\le q.
}
\]

The physical vorticity scale corresponding to order-one Euler vorticity is

\[
\frac{U_j^E}{R_j}
=
\frac{\nu K_j^2}{R_j^2}
=
\frac{\nu}{r_j^2}
=W_j.
\]

Thus the Euler normalization preserves first-hitting vorticity amplitude while enlarging the spatial source scale by \(K_j\).

The Type-II character is carried by velocity/length separation, not by unbounded Euler-scaled vorticity amplitude.

## 7. Source-scale normalized energy economics

The normalization denominator for source kinetic energy is

\[
(U_j^E)^2R_j^3
=\nu^2K_j^5r_j.
\]

Hence the global physical energy bound gives

\[
\boxed{
\|V_j\|_{L^2(\text{source region})}^2
\lesssim
\frac{E_0}{\nu^2K_j^5r_j}.
}
\]

A uniform source-scale normalized \(L^2\) upper bound is therefore automatic only if

\[
K_j^5r_j\gtrsim c>0.
\]

If

\[
K_j^5r_j\to0,
\]

finite physical energy permits the Euler-normalized energy to diverge.

Thus the compactness frontier naturally splits according to the dimensionless product

\[
\boxed{\Lambda_j:=K_j^5r_j.}
\]

## 8. Three regimes of the energy parameter

### A. Nondegenerate Euler-energy regime

If

\[
0<c\le K_j^5r_j\le C,
\]

then the finite physical energy gives a uniform source-scale \(L^2\) bound while M5-443 gives a fixed nonzero lower bound.

This is the favorable regime for Euler compactness, subject still to derivative, pressure, tail, and time compactness.

### B. Energy-dilute normalization regime

If

\[
K_j^5r_j\to0,
\]

then the normalization volume/velocity scale carries vanishing physical energy per unit normalized source energy.

The source may remain nontrivial locally, but global normalized \(L^2\) control is not inherited from finite parent energy.

This is a genuine source-scale noncompactness channel.

### C. Supercritical energy regime

\[
K_j^5r_j\to\infty
\]

is incompatible with the fixed source oscillation lower bound and finite physical kinetic energy.

Thus it is closed.

## 9. Updated R-remote scaling split

The strong remote Type-II branch now satisfies

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
\begin{cases}
0<c\lesssim K_j^5r_j\lesssim C
&\text{(Euler-energy compactness candidate)},\\
K_j^5r_j\to0
&\text{(energy-dilute Euler normalization)},\\
\text{derivative/pressure/tail/time noncompactness},\\
\text{already typed weaker export/geometry loss}.
\end{cases}
}
\]

The regime \(K_j^5r_j\to\infty\) is excluded by finite physical energy.

## 10. Main gain

The word `remote` is now representation-separated:

\[
\boxed{
\text{remote in first-hitting units}
\neq
\text{remote in original physical coordinates}.
}
\]

For the strong source-scale Type-II branch, finite energy forces physical localization:

\[
\boxed{R_j\to0.}
\]

Thus this branch is better viewed as a **multi-scale local Type-II concentration** rather than permanent macroscopic spatial export.

## 11. Next calculation

M19-021 should calculate the normalized local energy, enstrophy, and derivative scalings in the two surviving regimes of

\[
\Lambda_j=K_j^5r_j.
\]

In particular, determine whether the first-hitting vorticity cap plus the nondegenerate \(\Lambda_j\) regime gives enough spatial compactness for an ancient Euler limit, and what exact quantity must diverge in the energy-dilute regime.

---

\[
\boxed{\text{M19-020 COMPLETE; R-REMOTE STRONG SOURCE IS PHYSICALLY LOCAL AND CONTROLLED BY }K^5r.}
\]
