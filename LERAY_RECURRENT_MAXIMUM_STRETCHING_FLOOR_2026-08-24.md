# Leray Recurrent Maximum-Stretching Floor — 2026-08-24

Status: **EXACT MAXIMUM-PRINCIPLE ACTION FLOOR / PERIODIC AND RECURRENT CONSEQUENCES / GLOBAL REGULARITY NOT PROVED.**

## 1. Vorticity-magnitude equation

For the Leray vorticity equation

\[
W_s+W+\frac12Y\cdot\nabla W+V\cdot\nabla W
=SW+\nu\Delta W,
\]

write

\[
\rho=|W|,
\qquad
\xi=W/|W|
\]

where `W != 0`, and

\[
\gamma=\xi^TS\xi.
\]

The exact magnitude equation is

\[
\boxed{
\left(
\partial_s+(V+Y/2)\cdot\nabla-\nu\Delta
\right)\rho
=
\rho\left(
\gamma-1-\nu|\nabla\xi|^2
\right).
}
\]

Define

\[
M(s)=\|W(s)\|_\infty.
\]

At a spatial maximum point of `rho`,

\[
\nabla\rho=0,
\qquad
\Delta\rho\le0.
\]

Hence the upper Dini derivative satisfies

\[
\boxed{
D^+\log M(s)
\le
G(s)-1,
}
\]

where

\[
\boxed{
G(s)
:=
\sup_{Y\in\operatorname{Argmax}\rho(s)}
\left[
\gamma(Y,s)-\nu|\nabla\xi(Y,s)|^2
\right].
}
\]

Thus the Leray dilation contributes an exact unit decay rate which must be replenished by effective vortex stretching at the maximum set.

## 2. Periodic orbit: unit mean stretching floor

Suppose the Leray trajectory is nonzero and periodic with period `P`.

Then `M(s)>0` for all `s`. Otherwise `W=0` at one time; bounded divergence-free curl-free `V in L6` is zero, and uniqueness makes the whole orbit trivial.

Periodicity and continuity therefore give

\[
0<m_-\le M(s)\le m_+<\infty.
\]

Integrating the Dini inequality over one period and using

\[
M(s+P)=M(s)
\]

gives

\[
0
\le
\int_s^{s+P}(G(\sigma)-1)d\sigma.
\]

Therefore every nonzero periodic Leray orbit must satisfy

\[
\boxed{
\frac1P\int_s^{s+P}G(\sigma)d\sigma
\ge1.
}
\]

This is an exact action floor independent of the period.

## 3. Immediate strain-amplitude closure test

Since

\[
G(s)\le\|S(s)\|_\infty,
\]

any periodic survivor requires

\[
\boxed{
\frac1P\int_s^{s+P}\|S(\sigma)\|_\infty d\sigma
\ge1.
}
\]

In particular, a uniform strain ceiling

\[
\|S(s)\|_\infty\le B_+<1
\]

S-closes the periodic recurrent branch immediately.

Thus

\[
\boxed{B_+\ge1}
\]

is a necessary condition for every nonzero periodic survivor.

## 4. Positive-density high-stretching times

Assume the uniform ceiling

\[
G(s)\le B_+,
\qquad B_+>1.
\]

Fix `g0<1` and let

\[
E_{g0}=\{s\in[0,P]:G(s)>g_0\}.
\]

If

\[
\theta_{g0}=|E_{g0}|/P,
\]

then

\[
1
\le
\frac1P\int_0^PG\,ds
\le
\theta_{g0}B_++(1-\theta_{g0})g_0.
\]

Therefore

\[
\boxed{
\theta_{g0}
\ge
\frac{1-g_0}{B_+-g_0}.
}
\]

For example, at `g0=1/2`,

\[
\boxed{
\frac{|\{G>1/2\}|}{P}
\ge
\frac{1}{2B_+-1}.
}
\]

Thus a periodic orbit cannot hide the required stretching in a zero-density sequence of spikes when the analytic strain ceiling is finite.

## 5. Direction-strain split on the high-action set

At a maximum-vorticity point define the strain eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3
\]

and

\[
a_i=(\xi\cdot e_i)^2.
\]

The existing direction-strain gate gives, whenever

\[
g:=\gamma-\nu|\nabla\xi|^2>0,
\]

the alternative

\[
\boxed{
\lambda_2^+\ge g/2
\quad\lor\quad
\lambda_3a_3^2-\nu|\nabla\xi|^2\ge g/2.
}
\]

Hence the positive-density set `G>g0` splits into two measurable sublanes, and at least one occupies at least half of its measure.

Therefore every periodic survivor must carry positive-density action in at least one of:

1. positive-middle strain;
2. strongest-eigenvector alignment after paying the direction-gradient penalty.

These are already typed projective/geometric branches in the running proof tree.

## 6. Why periodicity also removes the temporal-thickness loophole

Because

\[
m_-:=\min_sM(s)>0
\]

and the orbit is uniformly smooth on the compact Leray-time circle, there are uniform spatial derivative bounds.

At every time choose a maximum point `Y_s`. Then for a fixed radius `r_*>0`, independent of `s`,

\[
|W(Y,s)|\ge m_-/2
\]

on a ball around `Y_s` of radius `r_*`.

If the no-`T` recurrent core keeps the maximum locations in a bounded similarity region, the transverse covariance packet is uniformly thick throughout the entire period.

Thus the previous loophole

\[
\text{remote/projective action occurs only while the packet is thin}
\]

is unavailable on a nonzero periodic orbit.

The periodic branch is therefore the cleanest setting in which to insert the covariance/projective/H1 tax without an additional endpoint-to-stage persistence argument.

## 7. Recurrent nonperiodic return version

Suppose a complete recurrent Leray trajectory has return times `T_n -> infinity` to a nonzero local state such that

\[
0<m_0\le M(0),M(T_n)\le M_+.
\]

Integrating the maximum inequality gives

\[
\log\frac{M(T_n)}{M(0)}
\le
\int_0^{T_n}(G-1)ds.
\]

The endpoint logarithm is `O(1)`, so

\[
\boxed{
\liminf_{n\to\infty}
\frac1{T_n}\int_0^{T_n}G(s)ds
\ge1.
}
\]

Thus the same unit mean effective-stretching floor holds along genuine nonzero recurrence returns, not only exact periodicity.

## 8. Current significance

The recurrent endgame is no longer allowed to have arbitrarily weak stretching. Every nonzero recurrent Leray core must replace the exact unit dilation loss at its vorticity maximum.

The next quantitative target is to combine

\[
\boxed{\text{mean }G\ge1}
\]

with the existing positive-middle/projective-frequency and H1 ledgers. If their maximum permitted recurrent production is strictly below this unit floor, the recurrent core is S-closed.

Status: **NONZERO PERIODIC OR GENUINELY RETURN-RECURRENT LERAY DYNAMICS MUST PAY AT LEAST ONE UNIT OF EFFECTIVE MAXIMUM-VORTICITY STRETCHING PER UNIT LERAY TIME ON AVERAGE. PERIODICITY ALSO MAKES THE THICK-CORE LOWER BOUND UNIFORM IN TIME. THIS ROUTES A POSITIVE-DENSITY FRACTION OF EVERY PERIOD INTO THE EXISTING POSITIVE-MIDDLE OR STRONGEST-EIGENVECTOR PROJECTIVE LANES. GLOBAL REGULARITY REMAINS UNPROVED.**