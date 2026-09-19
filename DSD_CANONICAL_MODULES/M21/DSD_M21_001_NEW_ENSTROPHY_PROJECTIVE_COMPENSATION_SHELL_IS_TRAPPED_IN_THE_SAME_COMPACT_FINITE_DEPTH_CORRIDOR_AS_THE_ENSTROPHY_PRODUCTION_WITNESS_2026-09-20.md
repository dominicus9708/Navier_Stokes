# M21-001 — The new enstrophy-projective compensation shell is trapped in the same compact finite-depth corridor as the enstrophy-production witness

Date: 2026-09-20  
Canonical ID: **M21-001**  
Status: **M21 OPENING MODULE / THE M20-013 JOINT COMPENSATION MAXIMUM CANNOT APPROACH THE TERMINAL BOUNDARY OR ESCAPE INTO THE SMOOTH TYPE-I CORE / COMPACT TERMINAL-JET CONTROL AND UNIFORM CENTER DECAY TRAP z_EK IN A COMPONENT-UNIFORM COMPACT DEPTH INTERVAL / COMBINED WITH THE EXISTING M5-587 ENSTROPHY-PRODUCTION WITNESS, BOTH EVENTS LIE IN ONE FIXED WEDGE CORRIDOR / SAME-DEPTH OVERLAP IS STILL NOT AUTOMATIC / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. M21 input from M20-013

Define

\[
\mathscr Z(z)
=
\left\langle
\int
|G|^2
\|[\Sigma_F,Q]\|_F^2
\,d\omega
\right\rangle_q
\ge0,
\]

and the associated radial flux

\[
\mathscr F(z)
=
\left\langle
\int
|G|^2
\|[\Sigma_F,Q]\|_F^2
F_r
\,d\omega
\right\rangle_q.
\]

M20-013 defines

\[
\boxed{
\mathscr Y_{EK}(z)
=
z^{5/2}\mathscr Z(z)
+
2z^{7/2}\mathscr F(z)
}
\]

and proves that on the terminal projective-strain branch:

- \(\mathscr Y_{EK}(z)>0\) for small \(z>0\);
- \(\mathscr Y_{EK}(z)\to0\) as \(z\to\infty\);
- hence there is a positive interior maximum at some

\[
z_{EK}\in(0,\infty).
\]

At such a maximum,

\[
\boxed{
\mathscr R(z_{EK})
-
2\mathscr G(z_{EK})
=
\frac{5}{2z_{EK}}
\mathscr Z(z_{EK})
>0.
}
\]

## 2. Quantitative terminal floor

M20-013 obtains a terminal lower bound

\[
\boxed{
\mathscr Z(0)\ge Z_*>0
}
\]

from:

- a robust high-vorticity threshold;
- a fixed transverse projective-strain floor.

Compact terminal-jet regularity supplies a fixed small interval

\[
0\le z\le z_0
\]

on which

\[
|\mathscr Z(z)-\mathscr Z(0)|
\le
M_Zz,
\]

and

\[
|\mathscr G(z)|+|\mathscr R(z)|
\le
M_{GR}.
\]

The constants depend only on the fixed compact hard component and the selected quantitative projective-strain branch.

## 3. The joint maximum cannot approach z=0

M20-013 gives

\[
\mathscr Y_{EK}'
=
z^{5/2}(2\mathscr G-\mathscr R)
+
\frac52z^{3/2}\mathscr Z.
\]

Choose \(a_{EK}>0\) small enough that

\[
a_{EK}\le z_0,
\]

\[
\mathscr Z(z)\ge \frac12Z_*
\qquad
(0\le z\le a_{EK}),
\]

and

\[
z\,M_{GR}
\le
\frac58 Z_*
\qquad
(0\le z\le a_{EK}).
\]

Then for \(0<z\le a_{EK}\),

\[
\begin{aligned}
\mathscr Y_{EK}'(z)
&\ge
-M_{GR}z^{5/2}
+
\frac54 Z_*z^{3/2}
\\
&\ge
\frac58 Z_*z^{3/2}
>0.
\end{aligned}
\]

Therefore

\[
\boxed{
z_{EK}\ge a_{EK}>0.
}
\]

The maximum cannot hide arbitrarily close to the terminal boundary.

## 4. A fixed positive joint-current level is reached

Integrating the lower derivative bound,

\[
\mathscr Y_{EK}(a_{EK})
\ge
\frac58Z_*
\int_0^{a_{EK}}z^{3/2}dz.
\]

Thus

\[
\boxed{
\mathscr Y_{EK}(a_{EK})
\ge
y_{EK,*}
:=
\frac14Z_*a_{EK}^{5/2}
>0.
}
\]

Hence the global interior maximum satisfies

\[
\boxed{
\mathscr Y_{EK}(z_{EK})
\ge
y_{EK,*}.
}
\]

## 5. The joint maximum cannot escape to infinity

The smooth Type-I core estimates from M20-013 give uniformly

\[
\mathscr Z(z)=O(z^{-4}),
\]

and

\[
\mathscr F(z)=O(z^{-9/2}).
\]

Therefore

\[
\mathscr Y_{EK}(z)
=
O(z^{-3/2})
+
O(z^{-1})
\to0.
\]

By compactness of the hard component, choose \(b_{EK}<\infty\) so large that

\[
\boxed{
\sup_{z\ge b_{EK}}
|\mathscr Y_{EK}(z)|
<
\frac12y_{EK,*}.
}
\]

But

\[
\mathscr Y_{EK}(z_{EK})
\ge
y_{EK,*}.
\]

Therefore

\[
\boxed{
z_{EK}\le b_{EK}<\infty.
}
\]

Combining Sections 3 and 5,

\[
\boxed{
a_{EK}
\le
z_{EK}
\le
b_{EK}.
}
\]

## 6. Existing enstrophy-production witness

M5-587 defines

\[
\mathscr Y_\omega(z)
=
\frac12z^{1/2}\mathscr K_\omega(z)
+
z^{3/2}\mathscr J_\omega(z).
\]

It has an interior maximum at

\[
z_\omega\in(0,\infty),
\]

where

\[
\boxed{
\mathscr Q_\omega(z_\omega)
-
\mathscr P_\omega(z_\omega)
=
\frac{\mathscr K_\omega(z_\omega)}
{2z_\omega}
>0.
}
\]

The terminal expansion and Type-I center decay yield fixed component-dependent bounds

\[
\boxed{
a_\omega
\le
z_\omega
\le
b_\omega.
}
\]

This part does not depend on the non-authoritative M19-429 payer trichotomy.

## 7. Common M21 compact corridor

Define

\[
\boxed{
a_{21}
:=
\min(a_{EK},a_\omega)
>0,
}
\]

and

\[
\boxed{
b_{21}
:=
\max(b_{EK},b_\omega)
<\infty.
}
\]

Then

\[
\boxed{
z_{EK},z_\omega
\in
[a_{21},b_{21}].
}
\]

Thus both:

- the scalar enstrophy-production witness;
- the enstrophy-weighted projective-strain compensation witness;

occur in one fixed intermediate wedge corridor.

## 8. Similarity-annulus interpretation

Since

\[
|y|=z^{-1/2},
\]

the common corridor corresponds to the compact similarity annulus

\[
\boxed{
b_{21}^{-1/2}
\le
|y|
\le
a_{21}^{-1/2}.
}
\]

Neither witness can escape:

- to the remote terminal tail;
- nor into the smooth center.

The comparison problem is therefore a bounded finite-depth PDE problem.

## 9. Conditional relation to the former energy witness

M19-430 also localized an energy maximum on the former residual-slope branch.

M19-440 later removed the unconditional status of that payer branch.

Therefore M21 does not use that energy maximum as an unconditional input.

If an independent argument reactivates the relevant energy-slope hypothesis, its witness may also be inserted into the same enlarged corridor.

The authoritative M21 opening uses only:

\[
z_\omega
\]

and

\[
z_{EK}.
\]

## 10. Common corridor still does not force overlap

The facts

\[
z_{EK},z_\omega\in[a_{21},b_{21}]
\]

do not imply

\[
z_{EK}=z_\omega.
\]

Nor do they imply that neighborhoods on which the two signed gaps are positive intersect.

The two extrema correspond to different functionals:

\[
\mathscr Y_\omega
\]

and

\[
\mathscr Y_{EK}.
\]

Therefore

\[
\boxed{
\text{common compact corridor}
\not\Rightarrow
\text{same-depth overlap}.
}
\]

A genuine coupling theorem is still required.

## 11. Why the new witness is more tightly coupled to vorticity geometry

The scalar witness at \(z_\omega\) uses

\[
\mathscr Q_\omega-\mathscr P_\omega.
\]

The new witness uses

\[
\mathscr Z
=
\left\langle
|G|^2
\|[\Sigma_F,Q]\|_F^2
\right\rangle.
\]

Thus both depend on the same finite-depth vorticity \(G\) and strain \(\Sigma_F\).

In particular,

\[
\mathscr Q_\omega
=
\left\langle
|G|^2
\Gamma_F
\right\rangle,
\]

while

\[
\mathscr Z
=
\left\langle
|G|^2
\cdot
2|P_\xi^\perp\Sigma_F\xi|^2
\right\rangle.
\]

They are respectively the longitudinal and transverse strain actions seen by the same enstrophy weight.

This is a stronger structural relationship than the former energy/enstrophy comparison.

## 12. Longitudinal/transverse strain decomposition

Pointwise,

\[
\Sigma_F\xi
=
\Gamma_F\xi
+
s_\perp.
\]

Therefore

\[
|\Sigma_F\xi|^2
=
\Gamma_F^2
+
|s_\perp|^2.
\]

Since

\[
K=2|s_\perp|^2,
\]

we have

\[
\boxed{
|G|^2|\Sigma_F\xi|^2
=
|G|^2\Gamma_F^2
+
\frac12J.
}
\]

Hence the new M21 joint density J is exactly the transverse part of the enstrophy-weighted strain-square density.

This gives the first direct algebraic bridge between the two M21 witnesses.

## 13. Next coupling target

The scalar enstrophy-production term is linear in \(\Gamma_F\):

\[
\mathscr Q_\omega
=
\langle E\Gamma_F\rangle.
\]

The projective-strain density is quadratic in the transverse part:

\[
\mathscr Z
=
2\langle E|s_\perp|^2\rangle.
\]

M21-002 should derive a finite-depth longitudinal/transverse strain covariance identity connecting

\[
\langle E\Gamma_F\rangle,
\]

\[
\langle E\Gamma_F^2\rangle,
\]

and

\[
\langle E|s_\perp|^2\rangle.
\]

The immediate question is whether a large transverse compensation shell can coexist with a stretching-dominant enstrophy shell while keeping the total enstrophy-weighted strain-square bounded by the existing Type-I compactness.

That is now a bounded-corridor covariance problem.

\[
\boxed{\text{M21-001 COMPLETE; THE NEW PROJECTIVE COMPENSATION SHELL AND THE ENSTROPHY-PRODUCTION SHELL ARE TRAPPED IN ONE COMMON COMPACT WEDGE CORRIDOR.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
