# M19-246 — A distance-to-wall moment forces linear-in-R poloidal pressure work for a radial-free returning shell

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / LOCALIZED SHELL-WORK CURRENCY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-245 shows that the \(\nu/R\) no-slip layer is a passive dissipative impedance. On the radial-free branch of M19-244, leading critical background transport cannot replenish it.

The remaining question is how much radial/poloidal pressure work is required for an outer velocity shell to survive an \(O(1)\) relative period.

This module derives a localized radial moment whose similarity-drift term is order \(R\) on a boundary shell.

## 2. Weighted velocity identity

The primal linearized equation is

\[
\partial_sw
=\nu\Delta w
-\left(\frac y2+U\right)\cdot\nabla w
-\frac12w
-(w\cdot\nabla)U
-\nabla\pi,
\]

with

\[
\nabla\cdot w=0,
\qquad
w|_{S_R}=0.
\]

Let \(a=a(r)\) be radial. Multiplication by \(aw\), integration over \(B_R\), incompressibility, and the no-slip boundary condition give

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}\int a|w|^2
={}&-\nu\int a|\nabla w|^2
+\frac\nu2\int(\Delta a)|w|^2\\
&+\frac14\int a|w|^2
+\frac14\int(y\cdot\nabla a)|w|^2\\
&+\frac12\int(U\cdot\nabla a)|w|^2
-\int a\,w^TS_Uw\\
&+\int\pi\,w\cdot\nabla a.
\end{aligned}}
\]

Unlike the global unweighted energy, the localized pressure term does not vanish. It measures pressure transfer across the radial localization.

## 3. Concave distance-to-wall detector

Let

\[
d=R-r
\]

and choose

\[
\boxed{
a_D(d)=D\left(1-e^{-d/D}\right),}
\]

with \(D>0\) and \(D=o(R)\) on an expanding-cavity sequence.

Then

\[
a_D'(d)=e^{-d/D}>0,
\qquad
a_D''(d)=-\frac1D e^{-d/D}<0.
\]

Since \(\partial_ra_D=-a_D'(d)\),

\[
\boxed{
y\cdot\nabla a_D=-r e^{-d/D}.}
\]

Moreover, away from an exponentially negligible center regularization,

\[
\Delta a_D
=a_D''(d)-\frac2r a_D'(d)
=-e^{-d/D}\left(\frac1D+\frac2r\right)\le0.
\]

Thus the localization itself introduces no positive diffusion error.

A smooth modification inside \(r\le R/2\) can make the radial weight regular at the origin; all resulting terms are \(O(e^{-R/(2D)})\) and vanish when \(D=o(R)\).

## 4. Shell mass detected by the moment

Define the one-period exponentially weighted shell mass

\[
\boxed{
M_D(R)
:=
\int_0^S\int_{B_R}e^{-(R-r)/D}|w|^2\,dy\,ds.
}
\]

The normalization is

\[
\int_0^S\|w(s)\|_2^2ds=1.
\]

Also

\[
0\le a_D\le D.
\]

Because the detector is exponentially concentrated in \(d\lesssim D\),

\[
\int_0^S\int r e^{-d/D}|w|^2
\ge
\frac R2 M_D(R)-o(1)
\]

for \(D=o(R)\), with the \(o(1)\) term coming from the exponentially small detector inside \(r<R/2\).

## 5. Exact pressure-work variable

For this weight,

\[
\nabla a_D=-e^{-d/D}\omega.
\]

Hence

\[
\int\pi w\cdot\nabla a_D
=-\int e^{-d/D}\pi w_r.
\]

Define the signed one-period poloidal pressure work

\[
\boxed{
\mathcal W_{P,D}(R)
:=-\int_0^S\int_{B_R}e^{-d/D}\pi w_r\,dy\,ds.
}
\]

The sign convention is chosen so that positive \(\mathcal W_{P,D}\) replenishes the similarity-drift loss.

## 6. Period integration

The radial weight is invariant under the closing spatial rotation, so the weighted moment has equal endpoint values for a relative-periodic mode. Integrating over one period gives

\[
\begin{aligned}
\mathcal W_{P,D}(R)
={}&
\nu\int_0^S\int a_D|\nabla w|^2
-\frac\nu2\int_0^S\int(\Delta a_D)|w|^2\\
&-\frac14\int_0^S\int a_D|w|^2
+\frac14\int_0^S\int r e^{-d/D}|w|^2\\
&-\frac12\int_0^S\int(U\cdot\nabla a_D)|w|^2
+\int_0^S\int a_D w^TS_Uw.
\end{aligned}
\]

The first two terms are nonnegative because \(a_D\ge0\) and \(\Delta a_D\le0\).

Therefore

\[
\boxed{
\mathcal W_{P,D}(R)
\ge
\frac14\int_0^S\int r e^{-d/D}|w|^2
-\frac D4
-\mathcal E_U(R,D),
}
\]

where

\[
\mathcal E_U(R,D)
:=
\left|\frac12\int_0^S\int(U\cdot\nabla a_D)|w|^2\right|
+
\left|\int_0^S\int a_D w^TS_Uw\right|.
\]

## 7. Radial-free background makes the coefficient error lower order

On the leading radial-free critical branch of M19-244,

\[
U_r=O(R^{-3}),
\qquad
S_U=O(R^{-2})
\]

on a remote shell, under the retained next-order tail expansion.

Because

\[
U\cdot\nabla a_D=-U_r e^{-d/D},
\qquad
0\le a_D\le D,
\]

we obtain

\[
\boxed{
\mathcal E_U(R,D)
\lesssim
CR^{-3}M_D(R)+CDR^{-2}.
}
\]

In the exact radial-free case \(U_r\equiv0\), the first term vanishes identically.

## 8. Linear-in-R pressure-work lower bound

Combining the preceding estimates,

\[
\boxed{
\mathcal W_{P,D}(R)
\ge
\frac R8 M_D(R)
-\frac D4
-o(1)
-\mathcal E_U(R,D).
}
\]

Hence if an escaping weak-zero shell carries a fixed positive detected fraction

\[
\boxed{
M_D(R)\ge m_*>0
}
\]

for some \(D=o(R)\), then

\[
\boxed{
\mathcal W_{P,D}(R)
\ge
\frac{m_*}{8}R-o(R).
}
\]

In particular,

\[
\boxed{
\mathcal W_{P,D}(R)=\Omega(R).
}
\]

Thus an \(O(1)\)-period radial-free returning shell requires a **linear-in-cavity-radius signed poloidal pressure-work currency**.

## 9. Interpretation

The thin no-slip layer of M19-245 is passive. The distance-to-wall moment now shows that a shell which keeps a positive fraction of the normalized velocity mass near the wall loses order \(R\) through the similarity drift in this first radial moment.

The only leading signed term capable of replenishing that loss on the radial-free branch is the localized pressure transfer

\[
-\int e^{-d/D}\pi w_r.
\]

Therefore the vague phrase “poloidal boundary coupling” is sharpened to a quantitative theorem obligation:

\[
\boxed{
\mathcal T_{shell}^{P,R}:
\text{decide whether the pressure system can produce }\Omega(R)\text{ signed shell work under the fixed }H^1\text{ currency and no-slip constraints.}
}
\]

## 10. Scope firewalls

The linear pressure-work lower bound is conditional on a positive detected shell mass \(M_D\ge m_*\) for some \(D=o(R)\). If no such sublinear thickness captures a positive mass fraction, the sequence belongs to a broader diffuse/mesoscopic shell or scaled-decompactification branch and must be analyzed separately.

Also,

\[
\boxed{
\text{large localized pressure work}
\neq
\text{large global pressure work},
}
\]

because global pressure work is zero in unweighted incompressible \(L^2\). The localized \(\Omega(R)\) work must be balanced by radial pressure transfer elsewhere.

The next calculation is therefore to compare this required \(\Omega(R)\) pressure currency with the pressure Poisson equation and the no-slip boundary momentum law.
