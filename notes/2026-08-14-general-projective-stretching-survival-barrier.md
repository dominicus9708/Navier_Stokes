# General projective stretching survival barrier

Date: 2026-08-14

Status: **DERIVED FOR THE FULL TRANSVERSE STRETCHING PROJECTIVE SOURCE. THIS IS WEAKER THAN THE SPECIAL QUADRATIC-CORE `Ab` BARRIER BUT APPLIES TO THE GENERAL PROJECTIVE LANE. GLOBAL REGULARITY NOT PROVED.**

## 1. Projective fractions

Let

\[
V_\omega
=\int\gamma|\delta\Omega|^2,
\qquad
\Theta=\frac{V_\omega}{B}.
\]

Relative to the Gaussian mean-vorticity axis `e`, write

\[
\delta\Omega=\alpha e+\beta,
\qquad
\beta\perp e,
\]

and define

\[
V_\perp
=\int\gamma|\beta|^2.
\]

The projective share of the vorticity variance is

\[
\boxed{
\Pi
:=
\frac{V_\perp}{V_\omega}
\in[0,1].
}
\]

Hence

\[
V_\perp
=\Theta\Pi B.
\]

## 2. General transverse stretching source

The general transverse stretching source is

\[
J_\perp
=
\int\gamma\,\delta S\,\beta.
\]

Cauchy--Schwarz gives

\[
|J_\perp|
\le
\sqrt{V_SV_\perp}.
\]

Since

\[
V_S\le B,
\]

we obtain

\[
\boxed{
|J_\perp|
\le
B\sqrt{\Theta\Pi}.
}
\]

This is the correct general-projective analogue of the typed source estimate.

For comparison, the special quadratic-core constant-shift lane satisfies the stronger estimate

\[
|J_{Ab}|
\lesssim \Theta B,
\]

but that improvement does not hold for arbitrary `J_perp`.

## 3. Fixed endpoint action forces B-mass

Let a responsible interval `I` carry a fixed projective endpoint source action `rho>0`, and suppose on that interval

\[
\Theta(t)\le\theta,
\qquad
\Pi(t)\le\pi.
\]

Then

\[
\rho
\lesssim
\int_I|J_\perp|dt
\le
\sqrt{\theta\pi}
\int_IB(t)dt.
\]

Therefore

\[
\boxed{
\int_IB(t)dt
\gtrsim
\frac{\rho}{\sqrt{\theta\pi}}.
}
\]

## 4. Rearrangement and physical dissipation

Let

\[
m=\sup_IB.
\]

The Gaussian-volume bathtub lemma gives

\[
\int_I\tau^{3/2}B(\tau)d\tau
\gtrsim
\left(\frac{\rho}{\sqrt{\theta\pi}}\right)^{5/2}
 m^{-3/2}.
\]

Thus

\[
D_{\rm phys}^{\perp}(I)
\gtrsim
W^{-1/2}
 m^{-3/2}
(\theta\pi)^{-5/4}.
\]

On a surviving intermediate pulse,

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\]

so the `W` factors cancel:

\[
\boxed{
D_{\rm phys}^{\perp}(I)
\gtrsim
\Lambda^{-3/2}
(\theta\pi)^{-5/4}.
}
\]

Equivalently,

\[
\boxed{
D_{\rm phys}^{\perp}(I)
\gtrsim
(\Lambda^{6/5}\theta\pi)^{-5/4}.
}
\]

## 5. Necessary condition for an infinite disjoint projective cascade

If infinitely many disjoint first-hitting intervals have this general transverse-projective lane carrying a fixed fraction of the endpoint source action, finite total kinetic-energy dissipation requires the individual lower bounds to tend to zero.

Therefore necessarily

\[
\boxed{
\Lambda^{6/5}\theta\pi\to\infty.
}
\]

After dyadic localization of both projective parameters this becomes

\[
\boxed{
\Lambda^{6/5}\Theta\Pi\to\infty.
}
\]

Thus a surviving general projective route requires not only vorticity variance but a quantitatively non-negligible **transverse fraction** of that variance.

## 6. Relation to source efficiency

The natural typed source scale is

\[
B\sqrt\Theta.
\]

If the transverse source has efficiency

\[
\mathcal E_\perp
:=
\frac{|J_\perp|}{B\sqrt\Theta},
\]

then

\[
\boxed{
\mathcal E_\perp\le\sqrt\Pi.
}
\]

Hence an efficient projective source automatically forces a lower bound on projective share:

\[
\Pi\ge\mathcal E_\perp^2.
\]

The previously derived source-efficiency survival condition

\[
\mathcal E H^{3/5}\to\infty,
\qquad
H=\Lambda\Theta^{5/6},
\]

is consistent with the present condition, since squaring the projective efficiency form gives the same natural combination

\[
\Lambda^{6/5}\Theta\Pi.
\]

## 7. Curvature consequence on a dyadically localized branch

Let

\[
\delta=\frac{K-B}{B}
\]

be the Hermite curvature surplus.

On a responsible projective set where

\[
\Theta\asymp\theta,
\qquad
\Pi\asymp\pi,
\]

if

\[
\delta\gtrsim\Theta\Pi,
\]

then the projective survival condition implies

\[
\boxed{
\delta\Lambda^{6/5}\to\infty.
}
\]

The complementary regime

\[
\delta\ll\Theta\Pi
\]

is a projectively near-first-Hermite branch and is the natural regime in which the quadratic-core approximation should dominate. On the strict mesoscopic band, the quadratic-core trace lane has already been excluded by the second-chaos telescoping barrier, leaving the special projective `Ab` lane or a failure of the low-Hermite approximation.

Status: **GENERAL TRANSVERSE PROJECTIVE SURVIVAL REQUIRES `Lambda^(6/5) Theta Pi -> infinity`; LOW-HERMITE PROJECTIVE BRANCH IS FUNNELED TOWARD THE QUADRATIC-CORE `Ab` ROUTE, WHILE THE COMPLEMENT IS CHARGED TO HERMITE CURVATURE / GLOBAL REGULARITY NOT PROVED.**
