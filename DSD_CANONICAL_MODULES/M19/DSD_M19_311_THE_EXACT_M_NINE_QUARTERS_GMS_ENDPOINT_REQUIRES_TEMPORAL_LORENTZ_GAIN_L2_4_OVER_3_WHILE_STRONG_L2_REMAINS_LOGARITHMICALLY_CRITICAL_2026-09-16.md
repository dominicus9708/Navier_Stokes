# M19-311 — The exact m=9/4 GMS endpoint requires temporal Lorentz gain L_t^{2,4/3}; strong L_t^2 remains logarithmically critical

**Date:** 2026-09-16  
**Status:** ACTIVE GMS ENDPOINT REFINEMENT / LORENTZ THRESHOLD / STRONG-ENDPOINT NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Strong fractional threshold from M19-310

M19-310 showed that

\[
D^m u\in L_t^2L_x^2,
\qquad
u\in L_t^\infty L_x^2
\]

implies

\[
u\in L^{s}_{x,t},
\qquad
s=2+\frac{4m}{3}.
\]

Strong Hölder closes the GMS logarithmic kernel whenever

\[
s>5,
\]

i.e.

\[
\boxed{m>9/4.}
\]

At `m=9/4`, one has exactly `s=5` and the isotropic parabolic Hölder argument is logarithmically critical.

## 2. Separate space and time at the endpoint

Set

\[
\tau=t_0-t>0
\]

and, after a fixed Galilean translation, write

\[
\rho(x,t)=\max\{|x|,\sqrt\tau\}.
\]

At fixed positive `tau`, on a bounded spatial ball,

\[
\begin{aligned}
\|\rho^{-5/3}\|_{L_x^3}^3
&\asymp
\int_0^{\sqrt\tau}\tau^{-5/2}r^2dr
+
\int_{\sqrt\tau}^{R}r^{-5}r^2dr\\
&\asymp
\tau^{-1}.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\rho^{-5/3}\|_{L_x^3}
\asymp
\tau^{-1/3}.
}
\]

## 3. Velocity contribution reduces to a one-dimensional time endpoint

At each time, spatial Hölder gives

\[
\int |u|^{10/3}\rho^{-5/3}dx
\lesssim
\|u(t)\|_{L_x^5}^{10/3}
\tau^{-1/3}.
\]

Thus the endpoint weighted payer reduces to

\[
\boxed{
\int_0^{\tau_0}
G(\tau)^{10/3}\tau^{-1/3}d\tau,
\qquad
G(t):=\|u(t)\|_{L_x^5}.
}
\]

The time weight

\[
\tau^{-1/3}
\]

belongs to weak Lorentz

\[
\boxed{L_t^{3,\infty}}
\]

and not strong `L3` at the endpoint.

## 4. What ordinary D^{9/4} L2 gives

At each time the endpoint Gagliardo--Nirenberg inequality is

\[
\boxed{
\|u(t)\|_5
\lesssim
\|u(t)\|_2^{3/5}
\|D^{9/4}u(t)\|_2^{2/5}.
}
\]

Let

\[
h(t):=\|D^{9/4}u(t)\|_2.
\]

With bounded energy,

\[
G(t)\lesssim C_E h(t)^{2/5}.
\]

If only

\[
h\in L_t^2=L_t^{2,2},
\]

then the power rule for Lorentz spaces gives only

\[
G\in L_t^{5,5}=L_t^5.
\]

Consequently

\[
G^{10/3}\in L_t^{3/2,3/2}.
\]

This is not enough to pair with the weak endpoint weight `L^{3,infinity}` via the sharp Lorentz Holder pairing, which requires the first factor in `L^{3/2,1}`.

Thus

\[
\boxed{
D^{9/4}u\in L_t^2L_x^2
\text{ alone remains logarithmically critical.}
}
\]

## 5. Sufficient temporal Lorentz improvement

Suppose instead

\[
\boxed{
h\in L_t^{2,4/3}.}
\]

Since `G lesssim h^{2/5}`, the Lorentz power rule gives

\[
G
\in
L_t^{5,(5/2)(4/3)}
=
L_t^{5,10/3}.
\]

Hence

\[
G^{10/3}
\in
L_t^{3/2,1}.
\]

Lorentz Holder then yields

\[
L^{3/2,1}\cdot L^{3,\infty}
\subset L^1.
\]

Therefore

\[
\boxed{
D^{9/4}u\in L_t^{2,4/3}L_x^2
\Longrightarrow
\int |u|^{10/3}\rho^{-5/3}dxdt<\infty.
}
\]

## 6. Pressure has the same endpoint

At fixed time, Riesz-transform boundedness gives

\[
\|p(t)\|_{5/2}
\lesssim
\|u(t)\|_5^2.
\]

Therefore

\[
\int |p|^{5/3}\rho^{-5/3}dx
\lesssim
\|p(t)\|_{5/2}^{5/3}\tau^{-1/3}
\lesssim
G(t)^{10/3}\tau^{-1/3}.
\]

Thus the pressure contribution is closed by exactly the same temporal Lorentz condition.

## 7. Endpoint theorem template

The analytic GMS endpoint can therefore be stated as

\[
\boxed{
\begin{aligned}
&u\in L_t^\infty L_x^2,
\\
&D^{9/4}u\in L_t^{2,4/3}L_x^2
\\
&\qquad\Longrightarrow\qquad
\mathcal P_{GMS}^{log}(V)<\infty
\end{aligned}
}
\]

on the relevant finite physical cylinder, with the standard canonical pressure gauge.

This contradicts M19-254 at a singular point.

## 8. New GMS alternatives

There are now two analytic closure lanes:

\[
\boxed{
\text{Lane A: }m>9/4
\text{ with strong }L_t^2L_x^2,
}
\]

or

\[
\boxed{
\text{Lane B: }m=9/4
\text{ with temporal Lorentz gain }L_t^{2,4/3}.
}
\]

Lane B is exactly critical in derivative order but subcritical in temporal concentration.

## 9. Relation to the ancient ledgers

The current M17 palinstrophy/raw-H2 interpolation certifies only ordinary spacetime `L2` control at fractional order and critical Type-I tail scaling.

It does not automatically provide the stronger temporal Lorentz index `4/3` after physical transfer.

Thus the new endpoint gain is a genuine additional concentration theorem, not a reformulation of existing `L2` finiteness.

## 10. Updated missing theorem

The GMS route can now close by either

\[
\boxed{
\mathcal T_{GMS}^{m>9/4,subcrit}
}
\]

or the sharper endpoint

\[
\boxed{
\mathcal T_{GMS}^{9/4,Lorentz}:
D^{9/4}u
\text{ gains }L_t^{2,4/3}
\text{ concentration control in physical variables.}
}
\]

The second formulation identifies precisely what is missing at the logarithmic derivative endpoint.

---

\[
\boxed{\text{M19-311 COMPLETE; THE EXACT }9/4\text{ ENDPOINT IS A TEMPORAL CONCENTRATION PROBLEM, NOT A SPATIAL DERIVATIVE-ORDER PROBLEM.}}
\]