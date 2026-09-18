# M19-441 — Terminal curl classifies the mean-free first residual into the harmonic dipole kernel or a pressure-free vorticity residual

Date: 2026-09-19  
Canonical ID: **M19-441**  
Status: **POST-M19-440 RESIDUAL REBASE / CURL OF THE DEGREE-minus-3 FIRST TERMINAL JET REMOVES PRESSURE EXACTLY / ON THE BOUNDED TWO-SIDED RECURRENT DIVERGENCE-FREE CLASS THE CURL-FREE KERNEL IS PRECISELY THE q-CONSTANT l=1 HARMONIC PRESSURE-DIPOLE GRADIENT / THEREFORE THE MANDATORY ANGULAR FIRST-JET ACTIVITY ROUTES TO EITHER THE ALREADY-CLASSIFIED CRITICAL CONSERVATIVE DIPOLE FIREWALL OR A GENUINE PRESSURE-FREE VORTICITY-TIME-DERIVATIVE EVENT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Return to the genuine residual frontier

M19-440 removes the Hardy-excess payer tree as an independent source of rigidity.

The robust terminal input is again M19-413--418:

\[
C
=
\mathcal R_{stat}[A,P]
\neq0,
\]

with mandatory syndetic mean-free angular activity in

\[
C^\perp.
\]

We now apply curl directly to the physical first-jet field

\[
r^{-3}C.
\]

## 2. Degree-minus-three curl operator

For a general vector field

\[
g(x)
=
r^{-m}F(q,\omega),
\]

the spherical curl decomposition gives

\[
\operatorname{curl}g
=
r^{-m-1}
\left[
(\operatorname{curl}_{S^2}F_T)\omega
+
\omega\times
\left(
(\partial_q+1-m)F_T
-
\nabla_{S^2}F_r
\right)
\right].
\]

For \(m=3\), define

\[
\boxed{
\mathcal K_3C
:=
(\operatorname{curl}_{S^2}C_T)\omega
+
\omega\times
\left[
(\partial_q-2)C_T
-
\nabla_{S^2}C_r
\right].
}
\]

Then

\[
\boxed{
\operatorname{curl}(r^{-3}C)
=
r^{-4}\mathcal K_3C.
}
\]

## 3. Exact vorticity-time interpretation

The terminal velocity expansion is

\[
u(x,s)
=
r^{-1}A
+
(-s)r^{-3}C
+
\cdots.
\]

Therefore

\[
\partial_su(x,0^-)
=
-r^{-3}C.
\]

Taking curl,

\[
\boxed{
\partial_s\omega(x,0^-)
=
-r^{-4}\mathcal K_3C.
}
\]

Thus \(\mathcal K_3C\) is exactly the normalized first terminal vorticity-time derivative.

It is not merely an auxiliary angular derivative of C.

## 4. Pressure disappears exactly

The first residual has the form

\[
C
=
C_{vis}
+
C_{conv}
+
\mathfrak G_2P.
\]

But

\[
\operatorname{curl}\nabla p=0.
\]

Therefore

\[
\boxed{
\mathcal K_3C
=
\mathcal K_3
(C_{vis}+C_{conv}),
}
\]

with no pressure contribution.

This is the pressure-free terminal residual observable sought after M19-440.

## 5. Classify the curl-free recurrent kernel

Assume

\[
\boxed{
\mathcal K_3C=0.
}
\]

M19-418 gives the degree-minus-three divergence constraint

\[
(\partial_q-1)C_r
+
\operatorname{div}_{S^2}C_T
=
0.
\]

Hence the physical field

\[
g=r^{-3}C
\]

is both divergence free and curl free on \(\mathbb R^3\setminus\{0\}\).

Because the punctured three-dimensional space is simply connected,

\[
g=\nabla\phi
\]

for a scalar potential \(\phi\).

Divergence freedom gives

\[
\Delta\phi=0.
\]

## 6. Critical harmonic potential equation

Since

\[
g=O(r^{-3})
\]

with bounded recurrent coefficient, choose the corresponding critical potential form

\[
\phi
=
r^{-2}H(q,\omega)
\]

up to an irrelevant constant.

Harmonicity gives

\[
\boxed{
\left[
(\partial_q-2)(\partial_q-1)
+
\Delta_{S^2}
\right]H
=
0.
}
\]

Project onto scalar spherical degree \(l\):

\[
-\Delta_{S^2}H_l
=
\lambda_lH_l,
\qquad
\lambda_l=l(l+1).
\]

Then

\[
\boxed{
(\partial_q-(l+2))
(\partial_q-(1-l))
H_l
=
0.
}
\]

## 7. Bounded two-sided recurrence leaves only l=1 zero frequency

The two radial exponents are

\[
l+2,
\qquad
1-l.
\]

For \(l=0\), both are positive.

For \(l\ge2\), one is positive and one is negative.

A nonzero exponential in either direction is incompatible with bounded two-sided recurrence.

Only \(l=1\) has the neutral exponent

\[
1-l=0.
\]

The other exponent is 3 and is excluded by boundedness.

Therefore

\[
\boxed{
H(q,\omega)
=
a\cdot\omega
}
\]

with a q-independent vector \(a\).

Consequently

\[
\boxed{
C
=
W_a
=
a-3(a\cdot\omega)\omega.
}
\]

Thus the entire bounded recurrent divergence-free curl-free kernel is exactly the three-dimensional harmonic pressure-dipole gradient sector.

## 8. Exact kernel theorem

We have proved

\[
\boxed{
\ker
\left(
\mathcal K_3
\mid
\{C:\operatorname{div}(r^{-3}C)=0,
\ C\text{ bounded recurrent}\}
\right)
=
\mathcal D_{dip}.
}
\]

There are no other recurrent critical curl-free first-jet modes at the terminal order.

This is stronger than the bounded-annulus statement of M19-439.

M19-439's higher harmonic kernels are finite-depth/subcritical modes, not leading terminal critical recurrent kernels.

## 9. Residual channel split

Let

\[
\Pi_{dip}C
\]

be the projection onto \(\mathcal D_{dip}\), and write

\[
C=C_{dip}+C_{curl}.
\]

Then

\[
\boxed{
\mathcal K_3C
=
\mathcal K_3C_{curl}.
}
\]

The mandatory M19-418 angular residual activity therefore has only two structural interpretations:

\[
\boxed{
D_{dip}^{crit}
\quad\lor\quad
V_{res}^{curl}.
}
\]

Here

\[
D_{dip}^{crit}
:
\Pi_{dip}C\neq0,
\]

and

\[
V_{res}^{curl}
:
\mathcal K_3C\neq0.
\]

## 10. Compact selected-event gap

M19-417 supplies a fixed residual detector occurring syndetically.

Restrict to the compact closure of one selected residual-event set on which the first-jet norm is bounded below.

The continuous map

\[
C
\mapsto
\left(
\Pi_{dip}C,
\mathcal K_3C
\right)
\]

has no simultaneous zero there by Section 8.

Compactness therefore gives a component/event-dependent positive gap

\[
\boxed{
\|\Pi_{dip}C\|^2
+
\|\mathcal K_3C\|^2
\ge
\varepsilon_{curl}>0
}
\]

in the selected detector norm.

After finite channel selection and minimal recurrence, at least one of the two channel events is syndetic.

## 11. Dipole branch status

M19-433--438 classify

\[
D_{dip}^{crit}
\]

as

- vorticity invisible;
- finite dimensional;
- terminal q-invariant;
- finite-depth physical-time cocycle;
- conservative in the energy ledger;
- supported by exactly critical tail stress scaling.

Therefore it is a fully typed critical firewall, not an unclassified pressure freedom.

## 12. Curl-visible branch status

On

\[
V_{res}^{curl},
\]

the terminal hard state carries a recurrent nonzero vorticity-time derivative

\[
\boxed{
\partial_s\omega
=
-r^{-4}\mathcal K_3C.
}
\]

This branch is pressure free.

Its physical homogeneity is one derivative stronger than the velocity first jet.

However its natural spacetime square cost remains critical:

\[
r^{-8}
\times
r^3
\times
r^2
=
r^{-3},
\]

the same ancestry weight already encountered in M19-414.

Thus direct unsigned accumulation is still blocked.

## 13. Corrected live terminal frontier

After M19-440--441, the terminal residual frontier is

\[
\boxed{
D_{dip}^{crit,conservative}
\quad\lor\quad
V_{res}^{curl,critical}.
}
\]

This replaces the non-authoritative M19-429 terminal master fork.

The first branch is finite-dimensional but not excluded.

The second branch is genuinely pressure free and is now the highest-value PDE channel.

## 14. Next target

The curl-visible residual is exactly a terminal vorticity-time derivative.

The next calculation should insert it into the terminal vorticity equation and decompose

\[
\mathcal K_3C
\]

into

- viscous vorticity diffusion;
- vorticity advection;
- vortex stretching.

Unlike the energy ledger, vortex stretching is not purely conservative and may retain a genuinely signed production term.

The audit must determine whether the mandatory curl residual can still be a complete coboundary/transport balance or whether it forces a nonzero stretching-production covariance.

\[
\boxed{\text{M19-441 COMPLETE; THE TERMINAL FIRST RESIDUAL IS REDUCED TO THE HARMONIC DIPOLE KERNEL OR A PRESSURE-FREE VORTICITY RESIDUAL.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
