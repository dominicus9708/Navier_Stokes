# M19-019 — CE-H toroidal dipole forces linear-in-radius winding reuse or bounded tail topology and saturates the annular volume budget

**Date:** 2026-09-11  
**Status:** CALCULATION / CONDITIONAL CE-H CRITICAL TAIL / TOROIDAL DIPOLE WINDING LOWER BOUND / CRITICAL PACKING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope

This module is **conditional** on the extra CE-H tail hypotheses of M17-349--350.

They are not assumptions on the full upstream R-critical root.

On the coefficient-compact harmonic-exterior subbranch,

\[
\Delta\Omega=0
\]

outside a large ball, and finite enstrophy plus divergence-free structure reduces the unique weak-critical harmonic obstruction to

\[
\boxed{
\Omega(x)
=
\frac{a\times x}{|x|^3}
+O(|x|^{-3}),
\qquad a\ne0.
}
\]

The leading term is toroidal and of size \(r^{-2}\).

M17-350 qualitatively identifies large winding/reuse or axial/lower-order escape. The present module quantifies the winding scale.

## 2. Work away from the dipole axis

Choose coordinates with

\[
a=|a|e_z.
\]

Fix a conical sector away from the axis,

\[
\boxed{
\mathcal C_{\theta_0}
:=
\{x:\sin\theta\ge s_0>0\}.
}
\]

On this sector,

\[
\left|
\frac{a\times x}{r^3}
\right|
=
\frac{|a|\sin\theta}{r^2}
\ge
\frac{|a|s_0}{r^2}.
\]

For sufficiently large \(r\), the \(O(r^{-3})\) remainder is smaller than half the leading term, so

\[
\boxed{
 c_0r^{-2}
\le
|\Omega(x)|
\le
C_0r^{-2}
}
\]

on the retained cone.

## 3. Radial velocity of a vortex line is one order smaller

The leading dipole is tangent to spheres:

\[
\left(\frac{a\times x}{r^3}\right)\cdot e_r=0.
\]

Therefore the radial vorticity component comes only from the lower-order remainder:

\[
\boxed{
|\Omega\cdot e_r|
\le
Cr^{-3}.
}
\]

Let \(\gamma(\ell)\) be a vortex line parametrized by arclength, so its unit tangent is

\[
T=\frac{\Omega}{|\Omega|}.
\]

Then

\[
\left|\frac{dr}{d\ell}\right|
=|T\cdot e_r|
\le
\frac{Cr^{-3}}{c_0r^{-2}}
\le
\frac{C_1}{r}.
\]

Hence on the annulus

\[
R\le r\le2R,
\]

\[
\boxed{
\left|\frac{dr}{d\ell}\right|
\le
\frac{C_1}{R}.
}
\]

## 4. Radial traversal requires length of order R^2

If one vortex-line segment remains in the retained cone while moving from radius \(R\) to radius \(2R\), then

\[
R
\le
\int\left|\frac{dr}{d\ell}\right|d\ell
\le
\frac{C_1}{R}L.
\]

Therefore

\[
\boxed{
L
\ge
c_1R^2.
}
\]

Thus an unbounded vortex line cannot cross one dyadic annulus by an approximately radial path. It must accumulate order \(R^2\) arclength inside an annulus whose geometric circumference scale is only order \(R\).

## 5. Linear winding lower bound

Away from the axis the leading direction is azimuthal.

One full toroidal revolution has arclength of order \(R\).

A path length

\[
L\gtrsim R^2
\]

therefore corresponds, at the scaling level, to at least

\[
\boxed{
N_{wind}(R)
\gtrsim
R
}
\]

turns/reuses before the line can change radius by a factor of two, unless it exits the retained conical sector or the lower-order remainder ceases to be controlled.

Thus the qualitative M17-350 winding branch has a quantitative linear-in-radius lower bound.

## 6. Flux-tube volume identity

For an infinitesimal vortex tube carrying instantaneous vorticity flux \(d\Phi\), the exact tube-coordinate volume element is

\[
\boxed{
dV
=
\frac{d\Phi}{|\Omega|}d\ell.
}
\]

On the dipole annulus,

\[
|\Omega|\le C_0R^{-2},
\]

so

\[
\frac1{|\Omega|}
\ge
cR^2.
\]

For a tube segment that traverses the annulus while staying in the cone,

\[
L\ge cR^2.
\]

Hence its occupied volume satisfies

\[
\boxed{
V_{tube}
\ge
c\,d\Phi\,R^4.
}
\]

## 7. Annular packing forces radial through-flux to be O(1/R)

The geometric volume of the dyadic annulus is

\[
|A_R|\asymp R^3.
\]

Disjoint material/vortex-tube volume cannot exceed the annulus volume.

Therefore the total flux \(\Phi_{through}(R)\) carried by a disjoint family of cone-staying vortex tubes that genuinely traverse from \(R\) to \(2R\) satisfies

\[
 c\Phi_{through}(R)R^4
\lesssim
R^3.
\]

Thus

\[
\boxed{
\Phi_{through}(R)
\lesssim
R^{-1}.
}
\]

This matches the direct radial-component scaling:

\[
\Omega_r=O(R^{-3})
\]

through a sphere of area \(O(R^2)\).

## 8. Yet the toroidal cross-flux is order one

Take a meridional surface transverse to the leading azimuthal direction, with area of order \(R^2\) inside the annulus and away from the axis.

The leading dipole has magnitude

\[
|\Omega_{dip}|\asymp R^{-2}.
\]

Therefore its absolute toroidal crossing flux is of order

\[
\boxed{
\Phi_{tor}(R)\asymp1
}
\]

on a fixed angular sector.

Hence the ratio between toroidal crossing activity and genuine radial through-flux is at least

\[
\boxed{
\frac{\Phi_{tor}(R)}{\Phi_{through}(R)}
\gtrsim
R.
}
\]

This is another form of the winding/reuse lower bound.

The same small amount of outward-through flux must be seen repeatedly as toroidal crossing flux.

## 9. Critical volume saturation

Suppose the through-flux has the maximal scaling allowed by Section 7:

\[
\Phi_{through}(R)\asymp R^{-1}.
\]

Then the tube volume cost is

\[
V_{tube}
\sim
R^{-1}\times R^2\times R^2
\sim
R^3.
\]

Thus

\[
\boxed{
\text{nontrivial unbounded dipole transport saturates the full annular volume scaling.}
}
\]

This explains why no simple volume contradiction appears.

The dipole branch is exactly critical: winding multiplicity, vorticity amplitude, and available annular volume balance at equality of homogeneity.

## 10. Escape through the axis or lower-order geometry

The estimates above require a fixed cone away from the dipole axis and the controlled \(O(r^{-3})\) remainder.

A line may attempt to avoid linear winding by moving toward the axis where the leading toroidal dipole amplitude vanishes, or by entering a region where lower-order modes determine the direction.

This is retained as

\[
\boxed{
G_{axial/lower\text{-}order\ tail\ escape}.
}
\]

The conical boundary itself is almost tangent to the leading dipole, so significant cross-cone transport must again be supplied by lower-order structure.

No silent closure is claimed.

## 11. Updated conditional dipole branch

The nonzero harmonic dipole now satisfies

\[
\boxed{
G_{toroidal\ dipole}
\Longrightarrow
G_{R\text{-}linear\ winding/reuse}
\lor
G_{bounded\ toroidal\ tail\ topology}
\lor
G_{axial/lower\text{-}order\ escape}.
}
\]

The first branch additionally obeys the critical packing law

\[
\boxed{
\Phi_{through}(R)\lesssim R^{-1},
\qquad
N_{wind}(R)\gtrsim R.
}
\]

## 12. Genealogical meaning

A fixed positive material-flux lineage cannot simply travel outward once through each large annulus on the controlled dipole geometry: the total outward-through flux capacity shrinks like \(R^{-1}\).

Thus coupling the core fixed-flux lineage to the dipole tail requires one of:

- fragmentation into smaller tail flux populations;
- repeated spatial reuse/winding;
- axial/lower-order transfer;
- bounded toroidal storage.

These are more precise targets for a future genealogy calculation.

However finite-lineage storage does not by itself rule out repeated reuse of the **same** small through-flux, so no contradiction follows here.

## 13. M19-019 verdict

The toroidal dipole is not a cheap ordinary far-field mode.

It is a critical space-filling winding mechanism whose outward flux shrinks as \(R^{-1}\) while its toroidal crossing multiplicity grows as \(R\).

The two effects exactly balance the annular volume budget.

Therefore the conditional CE-H dipole branch is sharpened substantially but remains open through winding/topology/axial escape.

---

\[
\boxed{\text{M19-019 COMPLETE; CONDITIONAL CE-H DIPOLE IS A CRITICAL WINDING-PACKING FRONTIER.}}
\]
