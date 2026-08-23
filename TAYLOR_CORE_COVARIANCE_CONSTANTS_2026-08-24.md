# Taylor Thick-Core Covariance Constants — 2026-08-24

Status: **EXPLICIT ENDPOINT COVARIANCE CONSTANTS / STAGE-PERSISTENCE BRIDGE STILL REQUIRED / GLOBAL REGULARITY NOT PROVED.**

This note supplies concrete values for the new transverse covariance ratio appearing in `TRANSVERSE_COVARIANCE_TO_PROJECTIVE_TAX_2026-08-24.md` from the already-derived Taylor thick core.

---

## 1. A general bounded-density cylinder lemma

Let `C` be a cylinder centered at the origin whose transverse cross-section is the disk

\[
|y_\perp|\le a.
\]

Let a nonnegative density `rho` satisfy on the whole cylinder

\[
0<c\le\rho\le C_0.
\]

Set

\[
\beta:=c/C_0\in(0,1].
\]

Normalize `rho dy` to a probability measure and let `Q_perp` be its centered transverse covariance.

Write

\[
\rho=c+(\rho-c).
\]

The constant part is a uniform cylindrical measure with transverse covariance

\[
\frac{a^2}{4}I_2.
\]

Its mass fraction in the normalized measure is at least `beta`, because

\[
\frac{c|C|}{\int_C\rho}
\ge\frac c{C_0}=\beta.
\]

The covariance-of-a-mixture formula is positive-semidefinite in each component, so

\[
\boxed{
\lambda_{min}(Q_\perp)
\ge
\frac{\beta a^2}{4}.
}
\]

For any transverse unit vector `v`, centering can only reduce the second moment about the origin. The uniform component contributes `a^2/4`, while every remaining point satisfies `|v dot y| <= a`. Hence

\[
\boxed{
\lambda_{max}(Q_\perp)
\le
a^2\left(1-\frac{3\beta}{4}\right).
}
\]

Let

\[
q_\perp=\frac12\operatorname{tr}Q_\perp,
\qquad
E_\perp=Q_\perp-q_\perp I_2.
\]

Then

\[
\boxed{
q_\perp\ge q_-:=\frac{\beta a^2}{4},
}
\]

and, because a transverse trace-free `2 x 2` covariance has eigenvalues `+/- delta`,

\[
\boxed{
|E_\perp|_F
\le
E_+:=\frac{(1-\beta)a^2}{\sqrt2}.
}
\]

Therefore

\[
\boxed{
\frac{q_-}{E_+}
\ge
\frac{\beta}{2\sqrt2(1-\beta)}.
}
\]

This ratio is scale-free: the cylinder radius cancels.

---

## 2. Insert the existing Taylor cylinder

At a first-hitting endpoint, the existing Taylor estimate gives, with

\[
r_0=K_{2,+}^{-1/2},
\]

on

\[
|z|\le\frac{r_0}{2},
\qquad
|y_\perp|\le\frac{r_0}{2},
\]

that

\[
\xi\cdot\Omega\ge\frac34.
\]

Hence

\[
|\Omega|\ge\frac34,
\qquad
\frac{9}{32}\le e=\frac12|\Omega|^2\le\frac12.
\]

Thus

\[
\boxed{
\beta=\frac{9}{16},
\qquad
a=\frac{r_0}{2}.
}
\]

The general lemma yields

\[
\boxed{
q_-
\ge
\frac{9}{256}r_0^2,
}
\]

and

\[
\boxed{
E_+
\le
\frac{7}{64\sqrt2}r_0^2.
}
\]

Therefore

\[
\boxed{
\frac{q_-}{E_+}
\ge
\frac{9}{14\sqrt2}
\approx0.4545686450.
}
\]

For the ideal `q=2` positive-middle action floor

\[
a_D=\frac{\log2}{\sqrt2}\approx0.4901290717,
\]

the covariance ratio from the preceding note obeys

\[
\boxed{
\Xi_\perp
:=\frac{E_+}{q_-a_D}
\le
\frac{14\sqrt2}{9a_D}
\approx4.488384572.
}
\]

Thus `Xi_perp` is not an arbitrary infinite parameter at a Taylor-thick endpoint.

---

## 3. Residual-free projective-action benchmark

The optimized zero-residual multistage estimate was

\[
a_\theta^{opt}
\ge
0.2805481691\,
\frac{q_-a_D}{E_+}.
\]

Using the Taylor-cylinder ratio gives

\[
\boxed{
a_\theta^{opt}
\gtrsim0.06250538
\quad\text{radians per stage}.
}
\]

The baseline in the explicit projective-speed inequality is

\[
c_0=\frac{\sqrt2}{4}\approx0.35355339.
\]

Therefore this crude Taylor-cylinder benchmark produces a strictly positive Sobolev frequency tax whenever the normalized stage ceiling obeys

\[
\boxed{
L_+
<
\frac{a_\theta^{opt}}{c_0}
\approx0.17679190.
}
\]

Using the broad pure moving-ball estimate

\[
L_{max}(r)=0.7483880874r^2,
\]

this benchmark condition is

\[
\boxed{
r\lesssim0.48603523.
}
\]

This narrow numerical window is **not** a new best closure radius: the existing anti-ribbon/projective-action closure is already much stronger on its own stated pure corridor. The significance here is different: the transverse covariance route no longer requires an unspecified shape constant at a Taylor-thick endpoint.

---

## 4. Variable Taylor subradius

The Taylor estimate can be used on a smaller cylinder. Let

\[
a=\theta r_0,
\qquad
0<\theta<1/\sqrt2.
\]

Since every point in the cylinder satisfies

\[
|y|^2\le2a^2,
\]

Taylor gives

\[
\xi\cdot\Omega
\ge
1-K_{2,+}a^2
=1-\theta^2.
\]

Therefore the enstrophy-density ratio is

\[
\boxed{
\beta(\theta)=(1-\theta^2)^2.
}
\]

The scale-free covariance ratio becomes

\[
\boxed{
\frac{q_-}{E_+}
\ge
\frac{(1-\theta^2)^2}
{2\sqrt2\left[1-(1-\theta^2)^2\right]}.
}
\]

As `theta -> 0`, the local vorticity becomes nearly constant and this ratio improves strongly.

However this does **not** give a free arbitrarily large projective-action bound: shrinking the cutoff increases sensitivity to material crossing, non-affine variation, and cutoff/viscous residual terms. Those contributions appear in `r_0` of the multistage covariance bridge.

Thus the small-cylinder limit exposes the correct tradeoff:

\[
\boxed{
\text{nearly isotropic Taylor core}
\quad\text{vs}\quad
\text{cutoff/material/non-affine residual action}.
}
\]

If the residual remains subcritical as the cylinder is reduced, the projective-action lower bound strengthens. If it does not, that growth is itself the `T/H/residual` exit.

---

## 5. Remaining issue: endpoint thickness versus stage-wide thickness

The Taylor estimate is automatic at record first-hitting endpoints and, more generally, at times where the normalized maximum and Hessian cap give the same local lower bound.

The covariance-to-projective block argument uses

\[
q_\perp(s)\ge q_->0
\]

on the portions of time carrying the transverse `D` action. The existing Taylor note by itself does not yet prove this lower bound uniformly over every instant of a whole stage.

Therefore the remaining bridge is precisely:

\[
\boxed{
\text{positive-middle D-action carrying time}
\Longrightarrow
\text{persistent Taylor/thick covariance}
\quad\lor\quad
T/H\text{ loss of persistence}.
}
\]

This is narrower than the previous vague transverse-affine obstruction.

A natural next calculation is to combine the temporal-enstrophy/analytic persistence estimates with the Taylor cylinder so that loss of `q_perp` during an action-carrying interval has an explicit flux/palinstrophy cost.

Status: **THE NEW THICK-CORE COVARIANCE RATIO IS EXPLICIT AT FIRST-HITTING ENDPOINTS: `q_-/E_+ >= 9/(14 sqrt(2))`. THE REMAINING OBSTRUCTION IS TEMPORAL PERSISTENCE OF THIS THICK COVARIANCE ON THE TIMES THAT CARRY TRANSVERSE STRAIN ACTION, NOT AN UNCONTROLLED ENDPOINT SHAPE PARAMETER. GLOBAL REGULARITY REMAINS UNPROVED.**