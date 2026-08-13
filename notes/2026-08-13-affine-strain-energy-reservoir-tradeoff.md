# Rotation-independent affine amplification tradeoff using only strain energy: `J × precursor >= c nu q`

Date: 2026-08-13

Status: **DERIVED GENERAL LINEAR AFFINE ENERGY TRADEOFF / REMOVES POINTWISE AFFINE-RATE ASSUMPTION**.

The rotation-independent affine diffusion estimate can be strengthened substantially.  No pointwise bound

\[
\|\operatorname{sym}L(t)\|\le M
\]

is needed.

The only affine deformation cost required is the time-integrated squared strain rate

\[
\boxed{
J=\int_0^T
\|\operatorname{sym}L(t)\|_{op}^2dt.
}
\]

A final stretch factor `q` then forces a two-dimensional heat covariance large enough to give the product tradeoff

\[
\boxed{
J
\|\omega_0\|_{L^\infty L^2_{\rm transverse}}^2
\gtrsim
\nu q
}
\]

for a genuine `q`-size amplification.

Thus arbitrary time intermittency and arbitrary eigenaxis rotation do not create a free affine escape.  The affine branch is reduced to a direct **strain-energy versus precursor-reservoir** competition.

This is a theorem for the linear affine advection--stretch--diffusion model.  Nonlinear perturbative transfer to Navier--Stokes remains open.

---

## 1. General affine flow

Consider

\[
\partial_t\omega
+(L(t)x)\cdot\nabla\omega
=L(t)\omega+\nu\Delta\omega,
\]

with

\[
\operatorname{tr}L(t)=0.
\]

Let

\[
S(t)=\operatorname{sym}L(t)
\]

and define

\[
\boxed{h(t)=\|S(t)\|_{op}.}
\]

Let

\[
F'=LF,
\qquad F(0)=I,
\qquad \det F=1.
\]

Define final largest singular stretch

\[
\boxed{q=\|F(T)\|_{op}>1.}
\]

The exact affine transform gives

\[
\omega(x,t)=F(t)v(F(t)^{-1}x,t)
\]

with

\[
\partial_tv
=\nu\nabla\cdot(A(t)\nabla v),
\qquad
A=F^{-1}F^{-T}.
\]

The accumulated heat matrix is

\[
\boxed{C_T=\int_0^T A(s)ds.}
\]

---

## 2. Backward singular-value comparison with an integrated strain function

Define

\[
\boxed{
H(s)=\int_s^T h(\tau)d\tau.
}
\]

The affine transition map from `s` to `T` has singular values between

\[
e^{-H(s)}
\quad\text{and}\quad
e^{H(s)}.
\]

Therefore, exactly as in the bounded-rate proof,

\[
\boxed{
A(s)
\succeq
e^{-2H(s)}A(T).
}
\]

Hence

\[
\boxed{
C_T
\succeq
c_H A(T),
\qquad
c_H=\int_0^T e^{-2H(s)}ds.
}
\]

---

## 3. Lower bound `c_H` using only the `L2_t` strain cost

Define

\[
\boxed{
K=\int_0^T h(s)ds,
\qquad
J=\int_0^T h(s)^2ds.
}
\]

Since

\[
H'(s)=-h(s),
\]

we have

\[
\frac d{ds}e^{-H(s)}
=h(s)e^{-H(s)}.
\]

Therefore

\[
\boxed{
\int_0^T
h(s)e^{-H(s)}ds
=1-e^{-K}.
}
\]

Cauchy--Schwarz gives

\[
\begin{aligned}
(1-e^{-K})^2
&\le
\left(\int_0^T h(s)^2ds\right)
\left(\int_0^T e^{-2H(s)}ds\right)\\
&=Jc_H.
\end{aligned}
\]

Hence

\[
\boxed{
c_H
\ge
\frac{(1-e^{-K})^2}{J}.}
\]

---

## 4. Replace total strain variation by the final stretch

The largest singular value of `F` grows at rate at most `h`, so

\[
q\le e^K.
\]

Thus

\[
e^{-K}\le q^{-1}.
\]

Therefore

\[
\boxed{
1-e^{-K}
\ge
1-q^{-1}.
}
\]

Combining,

\[
\boxed{
C_T
\succeq
c_{J,q}A(T),
\qquad
c_{J,q}
=\frac{(1-q^{-1})^2}{J}.
}
\]

No pointwise rate bound and no fixed eigendirection have been used.

---

## 5. Rotation-independent two-dimensional heat area

Let

\[
\sigma_1=q\ge\sigma_2\ge\sigma_3
\]

be the final singular values of `F(T)`.  Because

\[
\sigma_1\sigma_2\sigma_3=1,
\]

the two largest eigenvalues of

\[
A(T)=F(T)^{-1}F(T)^{-T}
\]

have product exactly

\[
q^2.
\]

If

\[
0<\mu_1\le\mu_2\le\mu_3
\]

are the eigenvalues of `C_T`, then

\[
\boxed{
\mu_2\mu_3
\ge
c_{J,q}^2q^2
=\frac{(1-q^{-1})^4}{J^2}q^2.
}
\]

---

## 6. Mixed-norm affine heat estimate

Using the two strongest heat directions,

\[
\|e^{\nu C_T:D^2}f\|_\infty
\le
C[\nu^2\mu_2\mu_3]^{-1/4}
\|f\|_{L^\infty L^2_{\rm transverse}}.
\]

Since

\[
\omega(T)=F(T)e^{\nu C_T:D^2}\omega_0,
\]

we obtain

\[
\boxed{
\|\omega(T)\|_\infty
\le
C
\frac{q^{1/2}}{1-q^{-1}}
\left(\frac J\nu\right)^{1/2}
\|\omega_0\|_{L^\infty L^2_{\rm transverse}}.
}
\]

For `q>=2`,

\[
(1-q^{-1})^{-1}\le2,
\]

so

\[
\boxed{
\|\omega(T)\|_\infty
\lesssim
q^{1/2}
(J/\nu)^{1/2}
M_\Pi,
}
\]

where

\[
M_\Pi
=\|\omega_0\|_{L^\infty L^2_{\rm transverse}}.
\]

---

## 7. Strain-energy / precursor product tradeoff

Suppose a target amplification satisfies

\[
\|\omega(T)\|_\infty
\ge c_0q
\]

in the normalized linear model.

Then

\[
M_\Pi
\gtrsim
c_0q^{1/2}
(\nu/J)^{1/2}
\]

and therefore

\[
\boxed{
J M_\Pi^2
\gtrsim
c_0^2\nu q.
}
\]

This is the central affine tradeoff.

A large amplification must pay by

- large coherent strain-energy `J`,
- large transverse precursor reservoir `M_Pi^2`,
- or both.

There is no separate pointwise-rate or axis-rotation escape.

---

## 8. Trace bridge to enstrophy and directional palinstrophy

For the transverse mixed norm,

\[
M_\Pi^4
\le
4E_0P_{e_1},
\]

where `e1` is the remaining coordinate in the heat-covariance eigenbasis,

\[
E_0=\|\omega_0\|_2^2,
\qquad
P_{e_1}=\|\partial_{e_1}\omega_0\|_2^2.
\]

Thus the affine tradeoff implies

\[
\boxed{
J^2 E_0P_{e_1}
\gtrsim
\nu^2q^2.
}
\]

Equivalently,

\[
\boxed{
J(E_0P_{e_1})^{1/2}
\gtrsim
\nu q.
}
\]

This converts the precursor geometry into already typed derivative/enstrophy channels.

---

## 9. Adaptive-`q` consequence

If at a smooth checkpoint the relevant initial quantities `E0`, `P_e1` are finite and one imposes a finite affine strain-energy budget `J<=J0`, then the linear affine amplification ceiling is finite:

\[
\boxed{
q
\lesssim
\frac{J_0}{\nu}
(E_0P_{e_1})^{1/2}.
}
\]

Under a hypothetical blow-up one can choose a later first-hitting target above this ceiling.

Therefore a singular route cannot remain within a uniformly bounded affine-strain-energy and bounded-precursor class at every adaptively selected checkpoint.

The nonlinear flow must activate a residual/Cauchy-V/pressure/shell/high-derivative channel or increase the coherent strain-energy budget.

---

## 10. Why this is a cleaner DSD channel pair

The earlier four-way fixed-axis list

\[
\text{rate / rotation / residual / reservoir}
\]

is now replaced, for the exact linear affine dynamics, by

\[
\boxed{
\text{strain-energy }J
\quad\times\quad
\text{precursor reservoir }M_\Pi^2.
}
\]

All time intermittency and eigendirection rotation are already aggregated into these two invariant quantities through the accumulated heat matrix.

This is a much smaller state description.

---

## 11. Claim boundary

The affine tradeoff is exact for the whole-space linear affine advection--stretch--diffusion model.

The full Navier--Stokes velocity is not globally affine.  A proof still requires a local/perturbative transfer theorem showing that if the residual channels remain below chosen thresholds, the actual first-hitting amplification obeys a comparable tradeoff.

Status: **POINTWISE AFFINE RATE ASSUMPTION REMOVED / ROTATION-INDEPENDENT STRAIN-ENERGY–PRECURSOR TRADEOFF CLOSED / NONLINEAR TRANSFER OPEN**.
