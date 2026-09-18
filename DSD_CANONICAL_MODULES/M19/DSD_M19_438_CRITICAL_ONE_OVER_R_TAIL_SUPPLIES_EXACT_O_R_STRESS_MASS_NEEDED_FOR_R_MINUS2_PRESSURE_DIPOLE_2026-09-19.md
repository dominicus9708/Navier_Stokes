# M19-438 — A critical 1/r velocity tail already supplies exactly the O(R) Reynolds-stress mass needed for an r^-2 pressure dipole; no supercritical stress growth is forced

Date: 2026-09-19  
Canonical ID: **M19-438**  
Status: **PRESSURE-DIPOLE PHYSICAL-SCALING AUDIT / COMPACT INTERIOR STRESS PRODUCES ONLY r^-3 PRESSURE AS IN M19-060, BUT A SCALE-COMPARABLE CRITICAL u~r^-1 TAIL HAS O(R) REYNOLDS-STRESS MASS AND THE r^-3 PRESSURE KERNEL CONVERTS IT EXACTLY TO r^-2 PRESSURE / A NONZERO DIPLOE THEREFORE REQUIRES ANISOTROPIC CRITICAL TAIL STRESS BUT NOT A BETTER-THAN-CRITICAL OR SUPERLINEAR RESOURCE / FINITE-ENERGY PRELIMITS CAN REALIZE THIS THROUGH A NONUNIFORM FAR-FIELD LIMIT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Pressure representation

For an incompressible whole-space velocity field,

\[
-\Delta p
=
\partial_i\partial_j(U_iU_j),
\]

and, after fixing the standard pressure gauge,

\[
\boxed{
p(y)
=
\int
K_{ij}(y-z)
U_i(z)U_j(z),dz,
}
\]

where

\[
K_{ij}(x)
=
\frac1{4\pi}
\partial_i\partial_j\frac1{|x|}
\]

is homogeneous of degree \(-3\).

M19-060 already shows that a uniformly compact interior stress source contributes only

\[
O(R^{-3})
\]

to the far pressure.

The question is what the critical tail contributes.

## 2. Critical tail stress scaling

Let

\[
U(y)
=
r^{-1}A(\log r,\omega)
\]

on the retained hard tail.

Then

\[
\boxed{
U\otimes U
=
r^{-2}
Q(\log r,\omega),
}
\]

with

\[
Q=A\otimes A.
\]

Thus one shell of physical radial thickness comparable to R carries stress mass of order

\[
R^{-2}\times R^3
=
\boxed{O(R)}.
\]

Equivalently, on an annulus

\[
\mathcal A_R
=
\{cR<|z|<CR\},
\]

one has

\[
\boxed{
\int_{\mathcal A_R}
|U|^2dz
=
O(R)
}
\]

under the compact amplitude ceiling.

On nontrivial recurrent hard components this order is also naturally attained on recurrent selected phases.

## 3. Scale the pressure contribution from a comparable annulus

Evaluate the pressure at

\[
y=R\omega.
\]

Restrict the integral to

\[
z=R\zeta,
\qquad
c<|\zeta|<C.
\]

Then

\[
K_{ij}(R\omega-R\zeta)
=
R^{-3}
K_{ij}(\omega-\zeta),
\]

while

\[
U_i(R\zeta)U_j(R\zeta)
=
R^{-2}
|\zeta|^{-2}
Q_{ij}
(\log R+\log|\zeta|,\widehat\zeta),
\]

and

\[
dz=R^3d\zeta.
\]

Therefore the comparable-scale pressure contribution is exactly

\[
\boxed{
p_{\mathcal A_R}(R\omega)
=
R^{-2}
\mathcal P_R(\omega),
}
\]

where \(\mathcal P_R\) is a dimensionless angular/log-phase integral.

Thus the critical tail produces the correct pressure homogeneity without any extra scale gain.

## 4. Why compact core and critical tail differ by one power

For a compact interior stress source,

\[
\int|U|^2dz
=
O(1),
\]

so the far kernel gives

\[
R^{-3}\times O(1)
=
O(R^{-3}).
\]

For the critical tail,

\[
\int_{|z|\sim R}|U|^2dz
=
O(R),
\]

so

\[
R^{-3}\times O(R)
=
\boxed{O(R^{-2})}.
\]

Hence the one-power gap in M19-060 is exactly supplied by the linear stress-mass growth of a \(1/r\) velocity tail.

## 5. Dipole coefficient is an anisotropic projection of this critical stress

A nonzero \(l=1\) pressure coefficient

\[
a(s)\cdot\omega
\]

requires a nonzero corresponding angular projection of the dimensionless tail-pressure functional

\[
\mathcal P_R(\omega).
\]

Therefore

\[
\boxed{
a(s)\neq0
\Longrightarrow
\text{nontrivial anisotropic critical Reynolds-stress organization on scale-comparable shells}.
}
\]

But it does **not** imply

\[
\int_{|z|<R}|U|^2dz
\gg R.
\]

The natural \(O(R)\) critical growth is sufficient.

## 6. No new unsigned budget

The hard tail already carries nontrivial critical square/cubic densities.

M19-267 gives a positive mean square-amplitude density on the terminal component.

Consequently linear-in-radius normalized energy/stress growth is part of the existing critical hard-tail geometry.

Therefore

\[
\boxed{
a(s)\neq0
\not\Rightarrow
\text{new supercritical energy or stress budget}.
}
\]

The pressure dipole does not create a new nonsummable physical resource.

## 7. Prelimit finite-energy scaling

Let a normalized blow-up field at physical scale \(r_j\) be schematically

\[
U_j(y)
=
r_j
u(x_j+r_jy,t_j).
\]

Then

\[
\int_{|y|\sim R}
|U_j|^2dy
=
r_j^{-1}
\int_{|x-x_j|\sim r_jR}
|u(x,t_j)|^2dx.
\]

Thus normalized critical stress mass

\[
O(R)
\]

corresponds to physical stress/energy mass

\[
\boxed{
O(r_jR).
}
\]

For every fixed normalized R,

\[
r_jR\to0
\]

as \(j\to\infty\).

Hence a nonzero critical tail coefficient in the blow-up limit is compatible with finite physical energy at every prelimit stage.

The nonuniformity appears only because the normalized far-field transition scale tends to infinity.

## 8. Noncommuting-limit interpretation

At each finite prelimit stage, sufficiently far beyond the active normalized corridor, the finite-energy pressure must revert to the faster whole-space far-field behavior.

But the radius at which this happens can diverge under blow-up normalization.

Thus

\[
\boxed{
\lim_{j\to\infty}
\lim_{R\to\infty}
R^2p_j(R\omega)
=
0
}
\]

can coexist with

\[
\boxed{
\lim_{R\to\infty}
\lim_{j\to\infty}
R^2p_j(R\omega)
=
a(s)\cdot\omega
\neq0.
}
\]

This is the correct structural meaning of the pressure-dipole defect.

It is a noncommuting far-field/blow-up limit supported by a critical stress corridor.

## 9. Relation to M19-274-style stress tightness defects

The mechanism is analogous to the earlier momentum-stress noncommuting-limit firewall:

- every finite approximant has the correct whole-space cancellation/decay;
- the convergence is not uniform over expanding normalized radii;
- the blow-up limit retains an order-one critical far-field observable.

Therefore excluding the dipole would require a **uniform tail tightness theorem** stronger than finite energy.

Ordinary finite energy does not supply such a theorem at the normalized critical scale.

## 10. Consequence for the overlap strategy

The finite-dimensional dipole sector has now been classified as

\[
\boxed{
\text{vorticity invisible}
+
\text{energy conservative}
+
\text{exactly critical in stress scaling}.
}
\]

Therefore its mere nonzero amplitude cannot close the hard branch.

It is a genuine firewall/transport phase.

The productive overlap analysis should quotient it out and focus on the curl-visible, dipole-free acceleration.

## 11. Updated pressure-dipole verdict

Combining M19-433--438:

\[
\boxed{
Z_{dip}^{3D-time}
=
\text{finite-dimensional conservative critical tail-stress defect}.
}
\]

It is tightly classified but not excluded.

No additional positive payer should be assigned to it.

## 12. Next target

The remaining potentially productive acceleration is

\[
\boxed{
Z_{curl}^{rem}
}
\]

after subtracting the harmonic pressure-dipole sector.

Because the dipole is the only divergence-free/curl-free homogeneous degree-minus-three harmonic-gradient mode in the \(l=1\) sector, the next calculation should establish a quantitative Hodge estimate on the compact corridor for the dipole-free acceleration:

\[
\|F_z^{rem}\|
\lesssim
\|\operatorname{curl}(r^{-3}F_z^{rem})\|
+
\text{controlled lower-order terms}.
\]

If such an estimate holds uniformly, the acceleration escape can finally be coupled to the vorticity equation modulo the now-classified dipole firewall.

\[
\boxed{\text{M19-438 COMPLETE; THE PRESSURE DIPOLE REQUIRES ONLY THE ALREADY-CRITICAL O(R) TAIL STRESS MASS, NOT A SUPERCRITICAL RESOURCE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
