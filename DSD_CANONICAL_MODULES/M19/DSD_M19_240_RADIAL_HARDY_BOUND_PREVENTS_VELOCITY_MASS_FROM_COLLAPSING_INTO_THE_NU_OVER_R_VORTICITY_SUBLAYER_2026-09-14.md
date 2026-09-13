# M19-240 — A radial Hardy bound prevents velocity mass from collapsing into the nu/R vorticity sublayer

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / WEAK-ZERO VELOCITY-CONCENTRATION GEOMETRY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-239 removes every nonzero regular macroscopic weak bulk limit. Thus an escaping cavity unit mode can still preserve its normalized one-period L2 mass only through macroscopic noncompactness: oscillation/scaled-derivative loss or velocity concentration into a shrinking relative boundary region.

M19-237 identifies a local vorticity/no-slip sublayer of natural physical thickness

\[
\delta_{vort}\asymp\frac\nu R.
\]

We now test whether the normalized **velocity mass itself** can live in such a thin layer.

The answer is no, using only no-slip and the fixed M19-232 H1 currency.

## 2. Radial no-slip estimate

Let \(w\in H_0^1(B_R)\) and let

\[
0<D\le R/2.
\]

For each direction \(\omega\in S^2\) and each \(r\in[R-D,R]\),

\[
w(r\omega)
=-\int_r^R\partial_\rho w(\rho\omega)d\rho.
\]

By Cauchy--Schwarz,

\[
|w(r\omega)|^2
\le
D\int_{R-D}^R|\partial_\rho w(\rho\omega)|^2d\rho.
\]

Since \(R-D\ge R/2\), comparison of the radial volume weights gives

\[
\boxed{
\int_{R-D<|y|<R}|w(y)|^2dy
\le C D^2
\int_{R-D<|y|<R}|\partial_rw(y)|^2dy
}
\]

with a universal geometric constant \(C\).

Hence

\[
\boxed{
\int_{R-D<|y|<R}|w|^2
\le C D^2\int_{B_R}|\nabla w|^2.
}
\]

## 3. One-period bound for cavity unit modes

Apply the estimate to \(w_j(s)\) and integrate over one relative period:

\[
\boxed{
\int_0^{S_j}\int_{R_j-D_j<|y|<R_j}|w_j|^2dy ds
\le
C D_j^2
\int_0^{S_j}\|\nabla w_j\|_2^2ds.
}
\]

M19-232 gives

\[
\int_0^{S_j}\|\nabla w_j\|_2^2ds
\to\frac1{4\nu}.
\]

Therefore

\[
\boxed{
\limsup_{j\to\infty}
\int_0^{S_j}\int_{R_j-D_j<|y|<R_j}|w_j|^2
\le
\frac{C}{4\nu}
\limsup_{j\to\infty}D_j^2.
}
\]

## 4. Velocity mass cannot live in an o(sqrt(nu)) physical layer

If

\[
D_j=o(\sqrt\nu),
\]

then

\[
\boxed{
\int_0^{S_j}\int_{R_j-D_j<|y|<R_j}|w_j|^2\to0.
}
\]

In particular, the M19-237 no-slip/vorticity sublayer has

\[
D_j\asymp\frac\nu{R_j},
\]

and therefore

\[
\frac{D_j}{\sqrt\nu}
\sim
\frac{\sqrt\nu}{R_j}
\to0.
\]

Hence

\[
\boxed{
\text{the normalized velocity L2 mass cannot collapse into the }\nu/R_j\text{ vorticity sublayer}.}
\]

## 5. Two nested boundary scales are therefore necessary

If the macroscopic weak limit is zero because velocity mass concentrates at the boundary, then the concentration must involve a layer whose physical thickness is at least order \(\sqrt\nu\) in the sense required to carry order-one L2 mass under the fixed H1 budget.

Meanwhile M19-237 shows that the final no-slip adjustment producing the boundary shear can occur on the much thinner scale

\[
\nu/R_j.
\]

Thus the escape branch necessarily has a two-scale structure:

\[
\boxed{
\begin{array}{c}
\text{outer velocity-carrying boundary region}
\\
\text{physical thickness }\gtrsim\sqrt\nu
\\[1mm]
\Downarrow
\\[1mm]
\text{inner no-slip/vorticity adjustment sublayer}
\\
\text{thickness }\asymp\nu/R_j.
\end{array}}
\]

The statement is a scale separation, not yet a full matched-asymptotic construction.

## 6. Why this still does not close concentration

A physical thickness \(D=O(1)\) is a relative thickness

\[
D/R_j\to0.
\]

Therefore an O(1)-thick velocity shell can carry all normalized L2 mass and still converge weakly to zero after the macroscopic scaling \(x=y/R_j\).

The radial Hardy bound rules out an arbitrarily thinner velocity layer, but it does not exclude this O(1)-scale shell.

Permanent firewall:

\[
\boxed{
\text{minimum physical velocity-layer thickness}
\neq
\text{velocity-concentration exclusion}.}
\]

## 7. New dynamical issue: residence time

Near \(r=R_j\), the bare similarity transport speed is of order

\[
\frac{R_j}{2}.
\]

A velocity-carrying shell of physical thickness \(D=O(1)\) therefore has a bare outward transport residence time of order

\[
\boxed{t_{res}\asymp\frac{D}{R_j}.}
\]

This tends to zero while the relative period remains bounded below by \(S_*>0\).

Hence a period-normalized order-one velocity mass in such a shell cannot be interpreted as a single passively transported packet. It would require repeated replenishment, a compensating pressure/core transfer, or a different scaled-derivative mechanism.

This residence statement is at present a structural target, not yet a certified contradiction, because a localized velocity-energy law contains pressure/current terms that must be controlled representation-safely.

## 8. Updated boundary-concentration frontier

The weak-zero concentration branch is sharpened to

\[
\boxed{
\mathcal T_{shell}^{res}:
\begin{array}{l}
\text{classify/exclude an O(1)-or-larger physical velocity shell at radius }R_j\\
\text{that feeds the }\nu/R_j\text{ no-slip vorticity layer while surviving an }O(1)\text{ relative period}. 
\end{array}}
\]

The next calculation must turn the vanishing bare residence time into a pressure-safe flux/turnover identity, or else show that the required replenishment is exactly another already typed mode/scattering branch.

---

\[
\boxed{\text{M19-240 COMPLETE: VELOCITY MASS AND VORTICITY SHEAR LIVE ON DISTINCT BOUNDARY SCALES; THE NEXT OBSTRUCTION IS SHELL RESIDENCE/REPLENISHMENT.}}
\]
