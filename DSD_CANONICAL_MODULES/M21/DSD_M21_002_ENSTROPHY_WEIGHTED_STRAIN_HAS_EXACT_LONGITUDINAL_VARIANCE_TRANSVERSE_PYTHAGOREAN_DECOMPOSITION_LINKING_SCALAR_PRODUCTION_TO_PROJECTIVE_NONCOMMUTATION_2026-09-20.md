# M21-002 — Enstrophy-weighted strain admits an exact longitudinal-variance-transverse Pythagorean decomposition linking scalar production to projective noncommutation

Date: 2026-09-20  
Canonical ID: **M21-002**  
Status: **FINITE-DEPTH COUPLING IDENTITY / AT EVERY WEDGE DEPTH THE ENSTROPHY-WEIGHTED STRAIN ACTION SEEN BY THE VORTICITY DIRECTION SPLITS EXACTLY INTO MEAN AXIAL STRETCHING SQUARED, AXIAL-STRETCHING VARIANCE, AND TRANSVERSE PROJECTIVE STRAIN NONCOMMUTATION / THE M5-587 SCALAR PRODUCTION WITNESS AND THE M20-013 PROJECTIVE COMPENSATION WITNESS THEREFORE DRAW FROM ORTHOGONAL COMPONENTS OF ONE COMMON STRAIN-SQUARE BUDGET / THIS GIVES A SHARP SAME-DEPTH TRADEOFF BUT DOES NOT BY ITSELF FORCE THEIR DEPTHS TO OVERLAP / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Finite-depth vorticity probability

At any depth z with nonzero total enstrophy coefficient, define

\[
E(z,q,\omega):=|G|^2,
\]

and

\[
\boxed{
W(z)
:=
\left\langle
\int E\,d\omega
\right\rangle_q
>0.
}
\]

Define the enstrophy probability

\[
\boxed{
d\pi_z
=
\frac{E}{W(z)}\,d\mu.
}
\]

Let

\[
\xi=\frac{G}{|G|}
\]

on the nonzero-vorticity set.

## 2. Longitudinal and transverse strain

Let \(\Sigma_F\) be the finite-depth strain coefficient.

Define the axial stretching scalar

\[
\boxed{
\Gamma
:=
\xi^T\Sigma_F\xi.
}
\]

Define the transverse strain vector

\[
\boxed{
s_\perp
:=
P_\xi^\perp\Sigma_F\xi.
}
\]

Then pointwise,

\[
\boxed{
\Sigma_F\xi
=
\Gamma\xi+s_\perp,
}
\]

with

\[
\xi\cdot s_\perp=0.
\]

Therefore

\[
\boxed{
|\Sigma_F\xi|^2
=
\Gamma^2+|s_\perp|^2.
}
\]

## 3. Scalar stretching production

The q-averaged finite-depth vortex-stretching production is

\[
\boxed{
\mathscr Q_\omega(z)
=
\left\langle
\int E\Gamma\,d\omega
\right\rangle_q.
}
\]

Hence

\[
\boxed{
\bar\Gamma(z)
:=
\mathbb E_{\pi_z}\Gamma
=
\frac{\mathscr Q_\omega(z)}{W(z)}.
}
\]

## 4. Projective strain density

M20-013 defines

\[
K
=
\|[\Sigma_F,Q]\|_F^2
=
2|s_\perp|^2.
\]

Therefore the joint density is

\[
J=EK,
\]

and

\[
\boxed{
\mathscr Z(z)
=
\left\langle
\int EK\,d\omega
\right\rangle_q
=
2W(z)
\mathbb E_{\pi_z}|s_\perp|^2.
}
\]

Thus

\[
\boxed{
\mathbb E_{\pi_z}|s_\perp|^2
=
\frac{\mathscr Z(z)}{2W(z)}.
}
\]

## 5. Enstrophy-weighted strain-square action

Define

\[
\boxed{
\mathscr S_{\omega\Sigma}(z)
:=
\left\langle
\int
E|\Sigma_F\xi|^2
\,d\omega
\right\rangle_q.
}
\]

Section 2 gives

\[
\mathscr S_{\omega\Sigma}
=
W\,
\mathbb E_{\pi_z}\Gamma^2
+
\frac12\mathscr Z.
\]

Now

\[
\mathbb E\Gamma^2
=
\bar\Gamma^2
+
\operatorname{Var}_{\pi_z}(\Gamma).
\]

Therefore

\[
\boxed{
\mathscr S_{\omega\Sigma}
=
W\bar\Gamma^2
+
W\operatorname{Var}_{\pi_z}(\Gamma)
+
\frac12\mathscr Z.
}
\]

Using

\[
\bar\Gamma=\frac{\mathscr Q_\omega}{W},
\]

we obtain the canonical M21-002 identity:

\[
\boxed{
\mathscr S_{\omega\Sigma}(z)
=
\frac{\mathscr Q_\omega(z)^2}{W(z)}
+
W(z)\operatorname{Var}_{\pi_z}(\Gamma)
+
\frac12\mathscr Z(z).
}
\]

## 6. Three orthogonal strain costs

The common enstrophy-weighted strain-square budget splits into exactly three nonnegative parts:

### L1 — mean longitudinal stretching

\[
\boxed{
\frac{\mathscr Q_\omega^2}{W}.
}
\]

### L2 — longitudinal stretching heterogeneity

\[
\boxed{
W\,\operatorname{Var}_{\pi_z}(\Gamma).
}
\]

### T — transverse projective noncommutation

\[
\boxed{
\frac12\mathscr Z.
}
\]

Thus

\[
\boxed{
\text{mean stretch}
\oplus
\text{stretch variance}
\oplus
\text{projective misalignment}
=
\text{total enstrophy-weighted strain-square}.
}
\]

This is an exact Pythagorean decomposition.

## 7. Immediate lower bounds

Since all three terms are nonnegative,

\[
\boxed{
\mathscr S_{\omega\Sigma}
\ge
\frac{\mathscr Q_\omega^2}{W},
}
\]

and

\[
\boxed{
\mathscr S_{\omega\Sigma}
\ge
\frac12\mathscr Z.
}
\]

More strongly,

\[
\boxed{
\mathscr S_{\omega\Sigma}
\ge
\frac{\mathscr Q_\omega^2}{W}
+
\frac12\mathscr Z.
}
\]

Therefore simultaneous large scalar stretching and large projective noncommutation at one depth require a correspondingly large common strain-square action.

## 8. Same-depth compactness tradeoff

On the M21 compact corridor

\[
z\in[a_{21},b_{21}],
\]

the compact smooth hard component gives a uniform bound

\[
\boxed{
\mathscr S_{\omega\Sigma}(z)
\le
S_{21,\max}<\infty.
}
\]

Therefore

\[
\boxed{
\frac{\mathscr Q_\omega(z)^2}{W(z)}
+
\frac12\mathscr Z(z)
\le
S_{21,\max}.
}
\]

This gives a same-depth exclusion rule:

if one channel approaches the full compact strain-square ceiling, the other must be depleted.

But ordinary positive floors in both channels can coexist if the ceiling is large enough.

## 9. Relation to the enstrophy-production shell

At the M5-587 witness depth,

\[
z=z_\omega,
\]

one has

\[
\mathscr Q_\omega
-
\mathscr P_\omega
=
\frac{\mathscr K_\omega}{2z_\omega}
>0.
\]

Hence

\[
\boxed{
\mathscr Q_\omega(z_\omega)>0.
}
\]

Therefore the mean longitudinal stretching component

\[
\frac{\mathscr Q_\omega(z_\omega)^2}{W(z_\omega)}
\]

is strictly positive.

The enstrophy-production shell necessarily occupies the longitudinal part of the common strain-square budget.

## 10. Relation to the projective compensation shell

At

\[
z=z_{EK},
\]

M20-013 provides

\[
\mathscr Z(z_{EK})>0,
\]

and

\[
\mathscr R(z_{EK})
-
2\mathscr G(z_{EK})
=
\frac{5}{2z_{EK}}\mathscr Z(z_{EK})
>0.
\]

Thus the projective compensation shell necessarily occupies the transverse part of the same common strain-square budget.

## 11. Why this still does not force same-depth overlap

The identity in Section 5 is pointwise in z.

It says:

- if scalar production and projective noncommutation are both large at one depth, they must share the same strain-square budget.

It does not say that the depth maximizing one functional must also carry the other.

A profile may place:

- longitudinal stretching near one depth;
- transverse projective noncommutation near another depth;

while respecting the compact ceiling everywhere.

Therefore

\[
\boxed{
\text{orthogonal common budget}
\not\Rightarrow
z_\omega=z_{EK}.
}
\]

## 12. Occupancy formulation

Fix thresholds

\[
q_*>0,
\qquad
z_*>0.
\]

At one depth define the events

\[
A_q:=\{\Gamma\ge q_*\},
\]

and

\[
A_T:=\{|s_\perp|^2\ge z_*\}.
\]

Positive mean stretching and positive transverse mean separately give lower bounds on the \(\pi_z\)-masses of these events under compact pointwise ceilings.

However their intersection is guaranteed only if the two occupancy lower bounds sum to more than one.

No current theorem forces that inequality.

Hence even at one fixed depth,

\[
\boxed{
\mathbb E\Gamma>0
\quad\text{and}\quad
\mathbb E|s_\perp|^2>0
}
\]

do not automatically imply a positive-measure set where both are simultaneously large.

## 13. Natural covariance target

The missing same-depth overlap information is encoded by the covariance

\[
\boxed{
C_{\Gamma T}(z)
:=
\operatorname{Cov}_{\pi_z}
\left(
\Gamma,
|s_\perp|^2
\right).
}
\]

If

\[
C_{\Gamma T}>0,
\]

stretching-favored regions also favor projective misalignment.

If

\[
C_{\Gamma T}<0,
\]

the flow segregates longitudinal stretching from transverse misalignment.

M20-011 already identified such gamma--K phase segregation at the terminal level.

M21-002 shows that the same covariance is the natural finite-depth overlap variable.

## 14. Exact relation to K

Since

\[
K=2|s_\perp|^2,
\]

we have

\[
\boxed{
\operatorname{Cov}_{\pi_z}(\Gamma,K)
=
2C_{\Gamma T}(z).
}
\]

Thus the finite-depth continuation of the M20-011 gamma--K covariance is immediate and does not require a new observable.

The same signed covariance now has a direct geometric meaning inside the compact wedge corridor.

## 15. Current M21 coupling frontier

The two witnesses are now connected by:

1. one common corridor;
2. one common enstrophy probability;
3. one common strain-square budget;
4. one signed longitudinal/transverse covariance.

The unresolved quantity is

\[
\boxed{
C_{\Gamma T}(z).
}
\]

A same-depth overlap theorem would require controlling its sign or integrated variation across the corridor.

## 16. Next target

M21-003 should derive the finite-depth evolution equation for

\[
C_{\Gamma T}(z)
\]

or, more robustly, for the mixed moment

\[
\boxed{
\mathscr M_{\Gamma T}(z)
=
\left\langle
\int
E\,\Gamma\,|s_\perp|^2
\,d\omega
\right\rangle_q.
}
\]

This mixed moment is exactly the enstrophy-weighted version of the M20-011 signed projective-strain damping term.

Its finite-depth evolution will show whether longitudinal/transverse phase segregation is itself conservative/recurrent or must be replenished by pressure/diffusion transport.

\[
\boxed{\text{M21-002 COMPLETE; SCALAR STRETCHING AND PROJECTIVE NONCOMMUTATION ARE ORTHOGONAL COMPONENTS OF ONE ENSTROPHY-WEIGHTED STRAIN-SQUARE BUDGET.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
