# Taylor Thick-Core Covariance Constants — 2026-08-24

Status: **EXPLICIT ENDPOINT COVARIANCE CONSTANTS / REMOTE-ACTION PERSISTENCE AND DOMINANCE STILL REQUIRED / GLOBAL REGULARITY NOT PROVED.**

This note supplies concrete values for the transverse covariance ratio appearing in `TRANSVERSE_COVARIANCE_TO_PROJECTIVE_TAX_2026-08-24.md` from the already-derived Taylor thick core.

The covariance constants are geometric and apply independently of whether the driving transverse strain is remote or full. Any numerical substitution of `log 2 / sqrt(2)` for the transverse action, however, is only a **full-D / exactly remote-dominant benchmark**.

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

and

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

This ratio is scale-free.

---

## 2. Insert the existing Taylor cylinder

At a first-hitting endpoint, with

\[
r_0=K_{2,+}^{-1/2},
\]

the existing Taylor estimate gives on

\[
|z|\le\frac{r_0}{2},
\qquad
|y_\perp|\le\frac{r_0}{2}
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

This endpoint ratio is valid before any remote/full-strain dominance decision is made.

---

## 3. Insert a generic active remote-D floor

Let

\[
A_{{D,rem},j}\ge a_{D,rem}>0
\]

be the actual active remote transverse action threshold.

The dimensionless covariance/action ratio obeys

\[
\boxed{
\Xi_{\perp,rem}
:=\frac{E_+}{q_-a_{D,rem}}
\le
\frac{14\sqrt2}{9a_{D,rem}}.
}
\]

Thus the Taylor endpoint removes the shape part of the unknown constant. What remains is the genuine remote action floor `a_D,rem` and the remote-to-full dominance/cancellation fraction.

No `log 2 / sqrt(2)` value is inserted at this generic stage.

---

## 4. Full-D / exactly remote-dominant benchmark only

If, as a special benchmark,

1. the transverse affine strain under study is the full positive-middle transverse strain, or the remote component is exactly dominant with no compensating near component; and
2. a `q=2` flux-preserving stage gives

\[
a_D=\frac{\log2}{\sqrt2}
\approx0.4901290717,
\]

then

\[
\boxed{
\Xi_\perp
\le
\frac{14\sqrt2}{9a_D}
\approx4.488384572.
}
\]

On the further zero-residual / zero-compensation benchmark, the optimized covariance-to-projective estimate gives

\[
\boxed{
a_\theta^{opt}
\gtrsim0.06250538
\quad\text{radians per stage}.
}
\]

With

\[
c_0=\frac{\sqrt2}{4},
\]

this benchmark alone creates positive excess projective action over the baseline only when

\[
\boxed{
L_+\lesssim0.17679190.
}
\]

Using

\[
L_{max}(r)=0.7483880874r^2,
\]

this corresponds to

\[
\boxed{
r\lesssim0.48603523.
}
\]

This is **not** a new best closure radius and is **not** valid for a generic remote transverse field. It is only a consistency benchmark showing that the endpoint covariance constants are numerically finite once a legitimate transverse-action floor and dominance transfer are supplied.

---

## 5. Variable Taylor subradius

Let

\[
a=\theta r_0,
\qquad
0<\theta<1/\sqrt2.
\]

Since `|y|^2 <= 2a^2` in the cylinder,

\[
\xi\cdot\Omega
\ge
1-K_{2,+}a^2
=1-\theta^2.
\]

Therefore

\[
\boxed{
\beta(\theta)=(1-\theta^2)^2.
}
\]

and

\[
\boxed{
\frac{q_-}{E_+}
\ge
\frac{(1-\theta^2)^2}
{2\sqrt2\left[1-(1-\theta^2)^2\right]}.
}
\]

As `theta -> 0`, the local vorticity becomes nearly constant and this ratio improves strongly.

However shrinking the cylinder also magnifies cutoff/material/non-affine sensitivity. Those terms enter the covariance residual density `r_0`; furthermore the remote-to-full cancellation parameter `epsilon_D` remains separate.

Thus the correct small-cylinder tradeoff is

\[
\boxed{
\text{nearly isotropic Taylor core}
\quad\text{vs}\quad
\text{cutoff/material residual + near-field compensation}.
}
\]

---

## 6. Remaining issue: endpoint thickness versus remote-action-carrying thickness

The Taylor estimate is automatic at record first-hitting endpoints. The remote covariance block argument needs

\[
q_\perp(s)\ge q_->0
\]

on the times that actually carry

\[
|D_{\rm rem}|ds.
\]

The endpoint estimate by itself does not prove this overlap.

The repository already contains two relevant persistence mechanisms:

- terminal natural-block packet persistence versus I/V rebuild;
- oriented-flux persistence / flux-change budgets.

They suggest the following narrower next bridge:

\[
\boxed{
\text{remote-D action carried while the Taylor packet is thin}
\Longrightarrow
\text{packet rebuild / flux turnover / derivative or deformation cost}.
}
\]

If that implication is quantified, the complementary action must occur while the packet is thick enough for the covariance lower bound, and the corrected remote-to-full transfer note can be applied.

Status: **THE TAYLOR ENDPOINT GIVES THE EXPLICIT SHAPE RATIO `q_-/E_+ >= 9/(14 sqrt(2))` INDEPENDENTLY OF THE REMOTE/FULL-STRAIN SPLIT. THE GENERIC REMOTE BRANCH STILL NEEDS ITS OWN ACTION FLOOR, ACTION/T HICKNESS OVERLAP, AND A DOMINANCE-OR-COMPENSATION BUDGET. GLOBAL REGULARITY REMAINS UNPROVED.**