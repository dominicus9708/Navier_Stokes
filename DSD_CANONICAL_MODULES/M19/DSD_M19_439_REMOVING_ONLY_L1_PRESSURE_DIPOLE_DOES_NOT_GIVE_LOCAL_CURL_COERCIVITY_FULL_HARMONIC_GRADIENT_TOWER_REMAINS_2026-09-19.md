# M19-439 — Removing only the l=1 pressure dipole does not give local curl coercivity: the full harmonic-gradient multipole tower is a kernel on a bounded annulus

Date: 2026-09-19  
Canonical ID: **M19-439**  
Status: **CORRECTION TO THE PROPOSED POST-M19-438 CURL-COERCIVITY STEP / ON A BOUNDED PHYSICAL ANNULUS THERE ARE DIVERGENCE-FREE CURL-FREE GRADIENTS OF DECAYING HARMONIC MULTIPOLES FOR EVERY l>=1 / QUOTIENTING ONLY THE l=1 PRESSURE DIPOLE LEAVES l=2,3,... HARMONIC-GRADIENT KERNELS / THE ODD FUCHSIAN PRESSURE-MULTIPOLE TOWER M5-142--145 IS A REALIZED SUBFAMILY OF THIS OBSTRUCTION / ANY USEFUL CURL OBSERVABILITY MUST ALSO USE GLOBAL SCALE/TAIL REALIZATION, NOT LOCAL HODGE THEORY ALONE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Proposed shortcut to audit

After M19-433--438, one might try to remove the \(l=1\) harmonic pressure-dipole sector and prove on the compact wedge corridor

\[
\|F_z^{rem}\|
\le
C
\|\operatorname{curl}(r^{-3}F_z^{rem})\|.
\]

If valid, this would convert every remaining depth-acceleration event into vorticity-visible activity.

The estimate is false at the level of a bounded annulus.

## 2. Decaying harmonic multipoles

For every scalar spherical harmonic

\[
Y_{\ell m}(\omega),
\qquad
\ell\ge1,
\]

define

\[
\boxed{
\phi_{\ell m}(x)
=
r^{-(\ell+1)}
Y_{\ell m}(\omega).
}
\]

This is harmonic on the punctured space:

\[
\boxed{
\Delta\phi_{\ell m}=0
\qquad
(x\neq0).
}
\]

Its gradient

\[
\boxed{
g_{\ell m}
=
\nabla\phi_{\ell m}
}
\]

therefore satisfies

\[
\boxed{
\nabla\cdot g_{\ell m}=0,
\qquad
\nabla\times g_{\ell m}=0.
}
\]

## 3. The l=1 mode is only the first member

For \(\ell=1\),

\[
\phi_{1}
=
r^{-2}Y_1
\]

and

\[
g_1
\sim
r^{-3},
\]

which is exactly the M19-433 harmonic pressure dipole.

But for \(\ell=3\),

\[
\phi_3
=
r^{-4}Y_3,
\]

and

\[
\boxed{
g_3
=
\nabla(r^{-4}Y_3)
\sim
r^{-5}.
}
\]

On a fixed annulus, for example

\[
1<r<2,
\]

this is a perfectly nonzero smooth divergence-free curl-free vector field.

It is orthogonal in spherical harmonic degree to the \(l=1\) dipole sector.

Therefore subtracting the dipole does not remove the curl kernel.

## 4. Explicit failure of dipole-only curl coercivity

Let

\[
\Pi_{dip}
\]

denote projection onto the three-dimensional \(l=1\) pressure-dipole gradient space.

For \(g_3\),

\[
\Pi_{dip}g_3=0,
\]

while

\[
\operatorname{curl}g_3=0
\]

and

\[
\|g_3\|_{L^2(1<r<2)}>0.
\]

Hence no estimate of the form

\[
\boxed{
\|(I-\Pi_{dip})g\|_{L^2(A)}
\le
C
\|\operatorname{curl}g\|_{X(A)}
}
\]

can hold for arbitrary divergence-free fields on a bounded annulus without additional boundary/global conditions.

## 5. Relation to the pressure multipole tower

M5-142 identifies the realized odd terminal pressure multipoles

\[
p_n^{harm}
=
(-s)^n
r^{-(2n+2)}
Y_{2n+1}(\omega).
\]

Each is harmonic away from the center.

Its gradient is therefore divergence free and curl free.

The first terms are

\[
n=0:
\quad
r^{-2}Y_1,
\]

\[
n=1:
\quad
(-s)r^{-4}Y_3,
\]

\[
n=2:
\quad
(-s)^2r^{-6}Y_5,
\]

and so on.

In wedge variables,

\[
p
=
r^{-2}H,
\]

these become

\[
\boxed{
H_n^{harm}
=
z^nY_{2n+1}.
}
\]

Thus the historical odd Fuchsian pressure-resonance tower is a realized Navier--Stokes subfamily of the general annular harmonic-gradient kernel.

## 6. M5-144--145 restrict but do not annihilate the tower

M5-144 proves that every realized odd harmonic pressure coefficient is a minimal-set invariant.

M5-145 proves all finite algebraic same-tail coefficients are rigid.

But neither theorem says the coefficients vanish.

Therefore the higher harmonic-gradient modes cannot simply be dropped from the finite-depth momentum equation.

They are globally selected, not locally absent.

## 7. Why higher multipoles were invisible in the leading terminal hard balance

At fixed physical terminal scaling, the \(l=1\) pressure dipole is critical:

\[
p_{dip}
\sim
r^{-2}.
\]

Higher multipoles have faster spatial decay:

\[
r^{-4},r^{-6},\ldots
\]

and therefore do not enter the leading \(z=0\) critical pressure coefficient.

This is why M19-436 can quotient the leading dipole cleanly in the terminal Hardy-excess identity.

At finite wedge depth \(z=O(1)\), however,

\[
(-s)^nr^{-(2n+2)}
=
r^{-2}z^n,
\]

so the normalized coefficients can all be order one.

Thus finite-depth curl observability sees a larger kernel than the terminal leading-order problem.

## 8. Consequence for M19-432's Z_E branch

The depth-acceleration branch cannot be reduced simply to

\[
Z_{curl}
\lor
Z_{dip}.
\]

A more accurate local decomposition is

\[
\boxed{
Z_E
\Longrightarrow
Z_{curl}
\lor
Z_{harm}
\lor
Z_{mixed},
}
\]

where

\[
Z_{harm}
\]

contains the globally realized harmonic pressure-gradient sector, including but not limited to the dipole.

The \(l=1\) dipole remains the leading critical member and is fully classified by M19-433--438.

## 9. Local Hodge theory is insufficient

On a bounded annulus, curl and divergence determine a vector field only after appropriate boundary/harmonic data are fixed.

The harmonic-gradient kernel is not finite dimensional when arbitrary boundary data are allowed.

Therefore the desired bounded-corridor observability theorem must use more than

- divergence free;
- curl;
- local annular norms.

It must use global pressure realization, scale behavior, recurrence, or boundary data inherited from the full ancient solution.

## 10. Useful reduction from Navier--Stokes structure

Although the local harmonic kernel is broad, the realized terminal/Fuchsian harmonic sector is much more structured.

At every finite algebraic order it lies in the odd sequence

\[
\boxed{
\ell=1,3,5,\ldots
}
\]

with coefficient fixed on the minimal set.

Thus one possible route is to quotient the **entire realized odd harmonic pressure tower**, not just the first dipole.

What remains would then be the vorticity-visible momentum component plus any Fuchsian-flat/global harmonic remainder.

## 11. New exact target

The correct observability question becomes

\[
\boxed{
\mathcal T_{curl/pressure}:
\text{after removing the globally realized harmonic pressure-gradient sector, does the bounded-corridor acceleration admit a uniform curl estimate?}
}
\]

This requires a global pressure decomposition, not a local sphere-only calculation.

## 12. Strategic verdict

The immediate post-M19-438 shortcut

\[
\text{remove dipole}
\Rightarrow
\text{curl coercivity}
\]

is closed as invalid.

But the failure is highly structured.

It identifies the exact missing data:

\[
\boxed{
\text{harmonic pressure-gradient tower / global pressure realization}.
}
\]

The next calculation should determine whether the entire realized harmonic tower is conservative in the energy ledger in the same sense as M19-436--437.

If yes, it can be quotiented as transport, leaving the productive acceleration genuinely curl visible.

\[
\boxed{\text{M19-439 COMPLETE; DIPOLE-ONLY QUOTIENT DOES NOT GIVE LOCAL CURL COERCIVITY BECAUSE HIGHER HARMONIC PRESSURE GRADIENTS REMAIN.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
