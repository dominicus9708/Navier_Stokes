# Local covariance alignment to Miller cross-vorticity norm

Date: 2026-08-13

Status: **DERIVED LOCAL AVERAGING/AXIS-FIELD BRIDGE + COROLLARY OF EXTERNAL MILLER CRITERION / GLOBAL REGULARITY NOT PROVED**.

This note upgrades the local covariance-axis information from an averaged neighborhood statement to an actual `L^2_x` bound on the cross-vorticity field

\[
n_r(x,t)\times\omega(x,t),
\]

provided the local principal axis has controlled spatial variation.

The external regularity theorem is Evan Miller's locally anisotropic criterion. The averaging estimate below is elementary.

## 1. Local covariance axis

Let

\[
E_r(z)
=\int\eta_r(z-y)|\omega(y)|^2dy,
\]

\[
C_r(z)
=\frac{
\int\eta_r(z-y)\omega(y)\otimes\omega(y)dy
}{E_r(z)},
\]

and let `n_r(z)` be a principal unit eigenvector where the principal eigenvalue is simple.

Define

\[
\Pi_r(z)=1-\mu_1(C_r(z)).
\]

Exactly,

\[
\boxed{
E_r(z)\Pi_r(z)
=
\int\eta_r(z-y)
|n_r(z)\times\omega(y)|^2dy.
}
\]

## 2. Compare the axis at the observation center with the axis at the vorticity point

For every pair `(y,z)`,

\[
\begin{aligned}
|n_r(y)\times\omega(y)|
&\le
|n_r(z)\times\omega(y)|\\
&\quad+
|n_r(y)-n_r(z)|\,|\omega(y)|.
\end{aligned}
\]

Using `(a+b)^2<=2a^2+2b^2`, averaging in `z` with the normalized kernel `eta_r(z-y)`, and then integrating in `y`, gives

\[
\begin{aligned}
\|n_r\times\omega\|_2^2
&\le
2\iint
\eta_r(z-y)|n_r(z)\times\omega(y)|^2dzdy\\
&\quad+
2\int|\omega(y)|^2
\int\eta_r(z-y)|n_r(y)-n_r(z)|^2dzdy.
\end{aligned}
\]

The first term is exactly

\[
2\int E_r(z)\Pi_r(z)dz.
\]

## 3. Control the axis-variation error

Assume

\[
L_r=\|\nabla_x n_r\|_\infty<\infty.
\]

Then

\[
|n_r(y)-n_r(z)|
\le L_r|y-z|.
\]

For the Student-type kernel used in the local covariance lemma,

\[
\int|z-y|^2\eta_r(z-y)dz
=\kappa_m r^2,
\qquad
\kappa_m=\frac{3}{2m-5}.
\]

Therefore

\[
\boxed{
\|n_r\times\omega\|_2^2
\le
2\int E_r\Pi_r
+2\kappa_m r^2L_r^2E,
}
\]

where

\[
E=\|\omega\|_2^2.
\]

This estimate is exact up to the elementary factor `2` from `(a+b)^2`.

## 4. Uniform local projective defect

Assume

\[
\boxed{
\varepsilon_r(t)
=\sup_x\Pi_r(x,t)
\le\varepsilon_0<\frac12.
}
\]

Because

\[
\int E_r(z)dz=E,
\]

the first term satisfies

\[
\int E_r\Pi_r
\le\varepsilon_rE.
\]

The local covariance-axis lemma gives

\[
r|\nabla n_r|
\le
m\frac{\sqrt{\mu_1\Pi_r}}{\mu_1-\mu_2}.
\]

Using

\[
\mu_1\le1,
\qquad
\mu_1-\mu_2\ge1-2\Pi_r
\ge1-2\varepsilon_0,
\]

we obtain

\[
\boxed{
rL_r
\le
\frac{m}{1-2\varepsilon_0}
\sqrt{\varepsilon_r}.}
\]

Substituting into the averaging bridge yields

\[
\boxed{
\|n_r\times\omega\|_2^2
\le
C_{m,\varepsilon_0}\,
\varepsilon_rE.
}
\]

Thus local covariance alignment controls the actual cross-vorticity norm, not merely an averaged proxy.

## 5. Conditions needed for the external Miller criterion

Miller's criterion allows a unit direction field varying in space and time provided its **spatial** gradient is bounded in the required local `L^infty` sense, and requires the cross-vorticity in the critical class `L_t^4L_x^2`.

The present bridge supplies those two inputs under explicit conditions.

### Spatial-gradient condition

It is sufficient that

\[
\boxed{
\sup_{t<T^*}
\frac{\sqrt{\varepsilon_r(t)}}{r(t)}
<\infty
}
\]

for the chosen scale function `r(t)` while `epsilon_r<=epsilon_0<1/2`.

### Cross-vorticity condition

Since

\[
\|n_r\times\omega\|_2^4
\lesssim
\varepsilon_r^2E^2,
\]

it is sufficient that

\[
\boxed{
\int_0^{T^*}
\varepsilon_r(t)^2E(t)^2dt
<\infty.
}
\]

Under both conditions, Miller's theorem excludes finite-time blowup.

## 6. A convenient stronger pointwise-in-time certificate

The kinetic-energy dissipation law gives

\[
E\in L^1(0,T^*).
\]

Therefore the stronger bound

\[
\boxed{
\sup_{t<T^*}
E(t)\varepsilon_r(t)^2
<\infty
}
\]

implies

\[
\int\varepsilon_r^2E^2dt
\le
\left(\sup E\varepsilon_r^2\right)
\int E dt
<\infty.
\]

Thus one explicit sufficient package is

\[
\boxed{
\varepsilon_r\le\varepsilon_0<1/2,
\quad
\sup\frac{\sqrt{\varepsilon_r}}{r}<\infty,
\quad
\sup E\varepsilon_r^2<\infty.
}
\]

This package is not claimed to hold automatically.

## 7. Natural-scale interpretation

At the natural vorticity scale

\[
r(t)\sim\|\omega(t)\|_\infty^{-1/2},
\]

the axis-gradient condition becomes schematically

\[
\boxed{
\varepsilon_r(t)\,\|\omega(t)\|_\infty
\lesssim1.
}
\]

Thus if the observation scale collapses with the vorticity magnitude, the projective defect must collapse correspondingly fast for the local principal-axis field to remain spatially regular.

This makes the required small-scale alignment rate explicit.

## 8. Relation to occupancy trichotomy

Suppose the intense core has nontrivial local enstrophy mass `h`. The occupancy--projective lemma showed that small `J_r` forces most of that core to align with `n_r` in an averaged sense.

The present bridge shows that **uniform** small `Pi_r` plus the axis-gradient estimate upgrades the neighborhood average to the actual mixed-norm quantity used by Miller.

Therefore the aligned branch of the occupancy trichotomy is no longer purely qualitative. It becomes a conditional external regularity gate once the scale-dependent defect satisfies the two quantitative conditions above.

## 9. Remaining gap

The unresolved issue is automatic control of

\[
\varepsilon_r(t)
\]

for arbitrary data near a hypothetical singular time.

A residual singularity must violate at least one of:

1. local projective smallness `epsilon_r<epsilon_0`;
2. axis-gradient rate `sqrt(epsilon_r)/r=O(1)`;
3. critical cross-vorticity integrability `epsilon_r E in L_t^2`.

These failure modes can now be intersected with the dyadic projective depletion and occupancy/sparseness channels.

Status: **ACTIVE LOCAL-COVARIANCE MILLER BRIDGE / OPEN AUTOMATIC DEFECT DECAY**.
