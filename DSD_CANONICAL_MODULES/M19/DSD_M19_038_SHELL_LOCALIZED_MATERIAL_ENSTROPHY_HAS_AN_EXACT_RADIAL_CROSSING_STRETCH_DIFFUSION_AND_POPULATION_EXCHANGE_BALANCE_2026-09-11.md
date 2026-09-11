# M19-038 — Shell-localized material enstrophy has an exact radial-crossing, stretch, diffusion, and population-exchange balance

**Date:** 2026-09-11  
**Status:** CALCULATION / SAME-POPULATION RADIAL-RESIDENCE EQUATION / RETURN-DEFICIENCY DYNAMICALIZATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-037 reduces the bulk-dominant annular ancestry charge to a shell-localized enstrophy quantity carried, on the quiet population-coverage branch, by a persistent material population.

The remaining issue is that the shell is Eulerian while the population is material.

Fix a smooth radial annular cutoff \(\chi_R\), supported in a comparable shell of radius \(R\), with

\[
|\nabla\chi_R|\lesssim R^{-1}.
\]

Let \(P_i(t)\) be one material population and define

\[
\boxed{
M_{i,R}(t)
:=
\int_{P_i(t)}\chi_R(x)|\omega(x,t)|^2dx.
}
\]

## 2. Material Reynolds derivative

Because \(P_i(t)\) is material and the flow is incompressible,

\[
\frac d{dt}M_{i,R}
=
\int_{P_i(t)}D_t\bigl(\chi_R|\omega|^2\bigr)dx.
\]

For a fixed shell cutoff,

\[
D_t\chi_R=u\cdot\nabla\chi_R.
\]

The vorticity equation is

\[
D_t\omega=S\omega+\nu\Delta\omega,
\]

so

\[
D_t|\omega|^2
=
2\omega\cdot S\omega
+2\nu\omega\cdot\Delta\omega.
\]

Therefore

\[
\boxed{
\frac d{dt}M_{i,R}
=
C_{rad,i}
+S_i
+2\nu\int_{P_i}\chi_R\,\omega\cdot\Delta\omega\,dx,
}
\]

where

\[
C_{rad,i}
:=
\int_{P_i}(u\cdot\nabla\chi_R)|\omega|^2dx
\]

and

\[
S_i
:=
2\int_{P_i}\chi_R\,\omega\cdot S\omega\,dx.
\]

## 3. Diffusion decomposition

Integrating by parts on the material population,

\[
\begin{aligned}
2\nu\int_{P_i}\chi_R\omega\cdot\Delta\omega\,dx
={}&
-2\nu\int_{P_i}\chi_R|\nabla\omega|^2dx\\
&-2\nu\int_{P_i}\nabla\chi_R\cdot(\omega\cdot\nabla\omega)dx\\
&+2\nu\int_{\partial P_i}\chi_R\,\omega\cdot\partial_n\omega\,dS.
\end{aligned}
\]

Since

\[
2\omega\cdot\nabla\omega=\nabla|\omega|^2
\]

componentwise in the contracted direction,

\[
-2\nu\nabla\chi_R\cdot(\omega\cdot\nabla\omega)
=-\nu\nabla\chi_R\cdot\nabla|\omega|^2.
\]

Define

\[
D_{bulk,i}
:=-2\nu\int_{P_i}\chi_R|\nabla\omega|^2dx,
\]

\[
C_{diff,R,i}
:=-\nu\int_{P_i}\nabla\chi_R\cdot\nabla|\omega|^2dx,
\]

and

\[
E_{pop,i}
:=
2\nu\int_{\partial P_i}\chi_R\omega\cdot\partial_n\omega\,dS.
\]

Then the exact balance is

\[
\boxed{
M_{i,R}'
=
C_{rad,i}
+S_i
+D_{bulk,i}
+C_{diff,R,i}
+E_{pop,i}.
}
\]

## 4. Interpretation of the five terms

### 4.1 Radial shell crossing

\[
C_{rad,i}
=
\int_{P_i}(u\cdot\nabla\chi_R)|\omega|^2dx.
\]

This is the exact advective current of population enstrophy across the Eulerian shell cutoff.

If the shell is centered at a moving reference point \(X(t)\), then

\[
D_t\chi_R(x-X(t))
=(u-\dot X)\cdot\nabla\chi_R,
\]

so the relevant velocity is the relative material velocity, not an arbitrary Galilean constant.

### 4.2 Stretch/source

\[
S_i=2\int\chi_R\omega\cdot S\omega.
\]

This is the ordinary vorticity-stretching source already represented in the projective/strain ledgers.

### 4.3 Bulk diffusion

\[
D_{bulk,i}
=-2\nu\int\chi_R|\nabla\omega|^2\le0.
\]

This is a genuine higher-derivative payment.

### 4.4 Diffusive shell crossing

\[
C_{diff,R,i}
=-\nu\int\nabla\chi_R\cdot\nabla|\omega|^2.
\]

This is diffusion through the artificial Eulerian shell boundary.

### 4.5 Material-population exchange

\[
E_{pop,i}
=2\nu\int_{\partial P_i}\chi_R\omega\cdot\partial_n\omega.
\]

For a compatible material-population partition, internal interfaces occur with opposite normals and produce the antisymmetric population exchange structure already audited in M18-088--089.

## 5. Exact dynamicalization of return deficiency

Suppose the same persistent population carries a nondegenerate shell mark at time \(t_a\):

\[
M_{i,R}(t_a)\ge m_*.
\]

If at a nearby time \(t_b\)

\[
M_{i,R}(t_b)\le\frac12m_*,
\]

then

\[
\frac12m_*
\le
\int_{t_a}^{t_b}
\left(
|C_{rad,i}|+|S_i|+|D_{bulk,i}|+|C_{diff,R,i}|+|E_{pop,i}|
\right)dt.
\]

Hence

\[
\boxed{
\text{rapid loss of same-population shell mass}
\Longrightarrow
\text{radial crossing}
\lor
\text{stretch/source}
\lor
\text{bulk diffusion}
\lor
\text{diffusive shell crossing}
\lor
\text{population exchange}.
}
\]

There is no sixth quiet mechanism.

## 6. Relation to M19-036

M19-036 showed that repeated dominant-lineage switching is paid once the ancestry mark is realized by a population state variable.

M19-037--038 now refine this:

- if the shell gradient charge is boundary dominated, it exits through the Hodge shell-boundary defect;
- if it is bulk-enstrophy dominated but carried by fresh/unrepresented material, it exits through replacement/turnover;
- if it is bulk dominated and carried by one persistent population, any loss of the localized mark is governed by the exact balance above.

Thus on the fully quiet branch the only genuinely new term is

\[
\boxed{C_{rad,i},}
\]

the relative radial material crossing current.

All other terms are already existing source/exchange/derivative currencies.

## 7. Spatial vortex-line residence is not temporal material residence

M18-068 gives the flux-line spatial identity

\[
dV=\frac{d\nu\,ds}{\rho},
\]

and expresses amplitude moments as spatial residence integrals along vorticity lines.

That variable \(s\) is arclength along the instantaneous vorticity line.

The present ancestry return is physical time along a material trajectory.

Since fluid velocity is not generally parallel to vorticity,

\[
\boxed{
\text{vortex-line spatial residence}
\not\Rightarrow
\text{material temporal shell residence}.
}
\]

The exact conversion term between the two descriptions is the relative radial current \(C_{rad,i}\), together with the already typed source/exchange terms.

This prevents an invalid shortcut from M18-068 directly to the R-AC temporal return bound.

## 8. Scaling of the radial current

Since

\[
|\nabla\chi_R|\lesssim R^{-1},
\]

\[
|C_{rad,i}|
\lesssim
\frac1R
\int_{P_i\cap\operatorname{collar}(A_R)}
|u-\dot X|\,|\omega|^2dx
\]

for a moving shell center \(X(t)\).

Thus a fast shell escape requires a large \(\rho^2\)-weighted relative radial velocity.

Define the weighted radial speed

\[
\boxed{
U_{rad,i}(R,t)
:=
\frac{
\int \!|u-\dot X|\,|\omega|^2|\nabla\chi_R|\,dx
}{
R^{-1}\int \!|\omega|^2\mathbf 1_{collar}\,dx
}
}
\]

when the denominator is nonzero.

Then schematically

\[
|C_{rad,i}|
\lesssim
\frac{U_{rad,i}}{R}
M_{i,R}^{collar}.
\]

Therefore the next issue is quantitative: how large can the weighted relative radial velocity be on a cubic-mass-bearing persistent population while remaining inside the bounded weak-critical corridor?

## 9. Sharpened R-AC frontier

Modulo already typed Hodge-boundary, replacement, stretching, diffusion and population-exchange exits,

\[
\boxed{
\mathcal T_{AC}^{corr}
\to
\mathcal T_{radial}:
\text{control weighted relative radial transport of one persistent cubic-mass lineage}.
}
\]

This is now a concrete transport theorem rather than a generic correlation statement.

## 10. Next calculation

The next module should compare \(U_{rad,i}\) with the bounded weak-\(L^3\) corridor and the packet scale \(r\) inside a parent shell radius \(R=Kr\).

The critical question is whether weak-\(L^3\) control upgrades the raw child-time residence fraction \(K^{-2}\) to a shell-crossing fraction of order \(K^{-1}\), and whether that improvement is sufficient for the cubic ancestry threshold.

---

\[
\boxed{\text{M19-038 COMPLETE; RETURN DEFICIENCY IS NOW AN EXACT RADIAL-TRANSPORT PROBLEM ON THE QUIET BRANCH.}}
\]