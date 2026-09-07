# DSD M17-350 — A harmonic `L2` exterior vorticity tail has only a toroidal `r^-2` dipole as the strong-`L3` obstruction

Date: 2026-09-08  
Canonical ID: **M17-350**

Status: **ACTIVE HARMONIC-TAIL MULTIPOLE REDUCTION / CONDITIONAL ON M17-349 HARMONIC EXTERIOR**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-349 and M5-477

On the harmonic-exterior branch,

\[
\boxed{
\Delta\Omega=0
\qquad(|x|>R_0).
}
\]

The marked ancient element has finite global enstrophy at each fixed time:

\[
\boxed{
\Omega\in L^2(\mathbb R^3).
}
\]

Also

\[
\nabla\cdot\Omega=0.
\]

We classify the exterior harmonic tail at one fixed smooth ancient time slice.

## 2. Exterior harmonic expansion

Each component of `Omega` is harmonic outside `B_{R_0}`.  The standard decaying exterior spherical-harmonic expansion is

\[
\Omega_i(r,\omega)
=
\sum_{\ell=0}^{\infty}
\sum_m
b_{i,\ell m}
r^{-(\ell+1)}Y_{\ell m}(\omega).
\]

Growing harmonic modes are excluded by `L2`.

The `ell=0` term behaves like

\[
r^{-1}.
\]

But

\[
\int_R^\infty r^2(r^{-1})^2dr
=\infty.
\]

Therefore the scalar monopole term vanishes componentwise.

The first possible nonzero term is `ell=1`, of size `r^-2`.

## 3. Matrix form of the leading ell=1 mode

Every vector-valued `ell=1` exterior harmonic term can be written

\[
\boxed{
\Omega^{(1)}(x)
=
\frac{Ax}{|x|^3}
}
\]

for a constant `3 x 3` matrix `A`.

Compute

\[
\nabla\cdot\left(\frac{Ax}{r^3}\right)
=
\frac{\operatorname{tr}A}{r^3}
-
3\frac{x^TAx}{r^5}.
\]

Only the symmetric part of `A` contributes to `x^T A x`.  Requiring divergence zero for every direction gives

\[
\boxed{
\operatorname{Sym}A
=
\frac{\operatorname{tr}A}{3}I.
}
\]

Thus

\[
A=cI+K,
\qquad
K^T=-K.
\]

## 4. Global vorticity flux removes the radial part

The radial part is

\[
\frac{cx}{r^3}.
\]

Its flux through a large sphere is

\[
\int_{S_R}
\frac{cx}{r^3}\cdot n\,dS
=4\pi c.
\]

But `Omega` is a globally smooth divergence-free vorticity field, so by the divergence theorem

\[
\int_{S_R}\Omega\cdot n\,dS=0
\]

for every large `R`.

Higher multipoles have zero net flux.  Therefore

\[
\boxed{c=0.}
\]

Hence `A` is skew-symmetric.

Every skew matrix has the form

\[
Kx=a\times x
\]

for a unique vector `a`.

Therefore the entire possible `r^-2` leading tail is

\[
\boxed{
\Omega_{dip}(x)
=
\frac{a\times x}{|x|^3}.
}
\]

This is tangential to spheres and has zero radial flux.

## 5. If the toroidal dipole vanishes, strong L3 follows

If

\[
\boxed{a=0,}
\]

then the next exterior harmonic multipoles begin at `ell>=2`, so

\[
\boxed{
|\Omega(x)|\le C|x|^{-3}
\qquad(|x|\gg1).
}
\]

Consequently

\[
\Omega\in L^{3/2}(\{|x|>R_0\}).
\]

On the bounded interior region, finite `L2` implies `L^{3/2}` by finite volume.  Therefore

\[
\boxed{
\Omega\in L^{3/2}(\mathbb R^3).
}
\]

After fixing the Galilean constant, Biot--Savart is a Riesz potential of order one, so Hardy--Littlewood--Sobolev gives

\[
\boxed{
V\in L^3(\mathbb R^3).
}
\]

Thus on the harmonic-exterior branch,

\[
\boxed{
a=0\Longrightarrow\text{global strong-}L^3\text{ velocity tail}.}
\]

This is precisely the missing tail upgrade required by the external rigidity gate of M17-347 on periodic/self-similar subbranches.

## 6. If the dipole is nonzero, it is the unique weak-critical obstruction

If

\[
a\ne0,
\]

then

\[
|\Omega_{dip}(x)|\asymp |x|^{-2}
\]

away from the dipole axis.

This belongs to weak `L^{3/2}` but not strong `L^{3/2}` at infinity.  Its induced velocity is correspondingly of critical `1/r` type and may fail strong `L3` logarithmically.

Therefore the entire harmonic weak-critical obstruction is reduced to the finite-dimensional vector parameter

\[
\boxed{a\in\mathbb R^3.}
\]

Symbolically,

\[
\boxed{
H_{harmonic\ exterior}
\Longrightarrow
G_{strong\ L^3\ tail}
\lor
G_{toroidal\ dipole\ tail}(a\ne0).
}
\]

## 7. Geometry of the nonzero dipole branch

The leading field

\[
\frac{a\times x}{r^3}
\]

is tangent to spheres and circulates around the axis `a`.

Hence a nonzero dipole is naturally a **toroidal/winding tail** rather than a radial outgoing tail.

Lower `O(r^-3)` multipoles may produce slow radial drift, so we do **not** claim that every exact vortex line is a closed circle.

The correct geometric classification is

\[
\boxed{
G_{toroidal\ dipole}
\Longrightarrow
G_{large\ winding/reuse\ at\ infinity}
\lor
G_{axial/lower\text{-}order\ escape}.
}
\]

A separate quantitative winding theorem is needed before converting this into a contradiction.

## 8. Relation to the DSD heuristic

The useful DSD step is to replace the vague phrase `weak-critical tail` by the smallest structural parameter that actually survives all exact constraints.

The mathematics is standard exterior harmonic expansion, divergence-free flux cancellation, and Hardy--Littlewood--Sobolev.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated tail frontier

Combining M17-349 and M17-350,

\[
\boxed{
\begin{aligned}
H_{coefficient\text{-}compact\ CEH\ tail}
\Longrightarrow{}&
G_{tail\ topology/winding}\\
&\lor G_{toroidal\ dipole}(a\ne0)\\
&\lor G_{strong\ L^3\ tail}.
\end{aligned}
}
\]

On a periodic dilation branch, the last alternative enters the externally known strong-`L3` nonexistence gate audited in M17-347.

The new internal target is therefore to eliminate or classify the single toroidal dipole coefficient `a` using the inherited material/genealogical structure.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
