# DSD M5-118 — Canonical Tail Log-Cylinder Factor and Cubic Residue

Date: 2026-08-27

Status: **CANONICAL TAIL FACTOR REWRITTEN AS A LOG-CYLINDER TRANSLATION SYSTEM / THE CUBIC ABEL-MELLIN RESIDUE BECOMES AN ORDINARY ONE-SLICE CUBIC DENSITY UNDER THE PUSHFORWARD INVARIANT MEASURE / NO DUPLICATE CORE-TAIL COST IS INTRODUCED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input and DSD formation rule

Let `M` be the compact minimal W1 set and

\[
\mathfrak T:M\to\mathcal T,
\qquad
V\mapsto T_V
\]

be the continuous canonical passive-tail factor from M5-114.

For one tail state `T`, define cylindrical coordinates

\[
Y=e^\rho\theta,
\qquad
\rho\in\mathbb R,
\qquad
\theta\in S^2,
\]

and the critical-amplitude cylinder field

\[
\boxed{
\Phi_T(\rho,\theta)
:=e^\rho T(e^\rho\theta).
}
\]

This is a change of representation of an already formed tail object.  No new physical field is inserted.

---

## 2. Axial chain: dilation becomes translation

The tail factor flow is

\[
(D_\tau T)(Y)
=e^{-\tau/2}T(e^{-\tau/2}Y).
\]

Therefore

\[
\begin{aligned}
\Phi_{D_\tau T}(\rho,\theta)
&=e^\rho e^{-\tau/2}
T(e^{\rho-\tau/2}\theta)\\
&=\Phi_T(\rho-\tau/2,\theta).
\end{aligned}
\]

Hence

\[
\boxed{
D_\tau
\quad\longleftrightarrow\quad
\mathsf S_{\tau/2}:\Phi(\rho,\theta)\mapsto
\Phi(\rho-\tau/2,\theta).
}
\]

The W1 dynamical time on the tail factor is thus ordinary translation in logarithmic radius.

---

## 3. Divergence-free cylinder constraint

Decompose

\[
\Phi=\Phi_r\theta+\Phi_\tau,
\qquad
\Phi_\tau\cdot\theta=0.
\]

Since

\[
T(Y)=|Y|^{-1}\Phi(\log|Y|,Y/|Y|),
\]

the condition `div T=0` becomes

\[
\boxed{
\partial_\rho\Phi_r
+\Phi_r
+\operatorname{div}_{S^2}\Phi_\tau
=0.
}
\]

The zero spherical-flux property of the canonical tail gives

\[
\boxed{
\int_{S^2}\Phi_r(\rho,\theta)d\theta=0
}
\]

for every regular logarithmic radius, hence distributionally in `rho`.

Thus the log-cylinder factor retains both incompressibility and the zero-source condition.  It is not an arbitrary translation process.

---

## 4. Static aggregation: cubic mass is flat in log radius

For every interval `[a,b]`,

\[
\begin{aligned}
\int_{e^a<|Y|<e^b}|T(Y)|^3dY
&=
\int_a^b\int_{S^2}
|\Phi_T(\rho,\theta)|^3
\,d\theta\,d\rho.
\end{aligned}
\]

Therefore

\[
\boxed{
|T|^3dY
=|\Phi_T|^3d\rho d\theta.
}
\]

Define the one-slice cubic observable

\[
\boxed{
\mathfrak c(T)
:=\int_{S^2}|\Phi_T(0,\theta)|^3d\theta.
}
\]

More generally,

\[
\mathfrak c_\rho(T)
:=\int_{S^2}|\Phi_T(\rho,\theta)|^3d\theta
=\mathfrak c(D_{2\rho}T).
\]

The critical cubic tail density is therefore an ordinary continuous/local observable transported by the factor flow.

---

## 5. The exterior `3+epsilon` moment

For `epsilon>0` and exterior radius one,

\[
\begin{aligned}
\int_{|Y|>1}|T(Y)|^{3+\varepsilon}dY
&=
\int_0^\infty
 e^{-\varepsilon\rho}
\int_{S^2}|\Phi_T(\rho,\theta)|^{3+\varepsilon}
 d\theta d\rho.
\end{aligned}
\]

The Type-I tail bound gives a uniform bound on `Phi`, so

\[
|\Phi|^{3+\varepsilon}\to|\Phi|^3
\]

uniformly on the bounded amplitude range as `epsilon downarrow 0`.

Thus the only noncompact feature is the logarithmic half-line itself.

---

## 6. Push forward the invariant measure

Let `mu` be an invariant probability measure on the compact W1 minimal set and define

\[
\boxed{
\nu:=\mathfrak T_\#\mu.
}
\]

Continuity and equivariance of `mathfrak T` imply that `nu` is invariant under the dilation flow `D_tau`, equivalently under every log translation `S_rho`.

Average the exterior `3+epsilon` tail moment:

\[
\begin{aligned}
&\varepsilon
\int_{\mathcal T}
\int_0^\infty e^{-\varepsilon\rho}
\int_{S^2}|\Phi_T(\rho,\theta)|^{3+\varepsilon}
 d\theta d\rho\,d\nu(T)\\
&=
\varepsilon\int_0^\infty e^{-\varepsilon\rho}d\rho
\int_{\mathcal T}
\int_{S^2}|\Phi_T(0,\theta)|^{3+\varepsilon}
 d\theta\,d\nu(T)\\
&=
\int_{\mathcal T}
\int_{S^2}|\Phi_T(0,\theta)|^{3+\varepsilon}
 d\theta\,d\nu(T).
\end{aligned}
\]

Here translation invariance of `nu` is the essential step.

Taking `epsilon downarrow 0` gives

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\varepsilon
\left\langle
\int_{|Y|>1}|T|^{3+\varepsilon}dY
\right\rangle_\nu
=
\int_{\mathcal T}\mathfrak c(T)d\nu(T).
}
\]

---

## 7. Identification with the W1 cubic residue

The canonical tail subtraction satisfies

\[
V-T_V\in L^3
\]

on the exterior, with uniformly summable dyadic error.  Interior bounded regions do not contribute to an `epsilon times (3+epsilon)` residue.

Therefore the W1 cubic residue from M5-103/M5-107 is entirely carried by the canonical tail factor:

\[
\boxed{
\mathscr R_3
=
\int_{\mathcal T}
\mathfrak c(T)d\nu(T)
=
\int_{\mathcal T}
\int_{S^2}|\Phi_T(0,\theta)|^3d\theta\,d\nu(T).
}
\]

Equivalently, for any fixed `rho`,

\[
\boxed{
\mathscr R_3
=
\int_{\mathcal T}
\int_{S^2}|\Phi_T(\rho,\theta)|^3d\theta\,d\nu(T).
}
\]

Thus the apparent Abel/Mellin anomaly is an ordinary stationary cubic density on the log-cylinder factor.

---

## 8. Cesaro form

For every tail trajectory for which the time/log-radius Cesaro mean exists,

\[
\frac1L\int_0^L\mathfrak c_\rho(T)d\rho
\]

is exactly the mean cubic charge per unit logarithmic radius.

Under an ergodic component of `nu`, Birkhoff gives for `nu`-almost every tail state

\[
\boxed{
\lim_{L\to\infty}
\frac1L\int_0^L
\int_{S^2}|\Phi_T(\rho,\theta)|^3d\theta d\rho
=
\mathscr R_3^{(erg)}.
}
\]

No pointwise tail limit and no finite Lorentz index is required.

---

## 9. DSD four-chain audit

### Formation — GREEN

`Phi_T` is only the cylindrical representation of the already constructed canonical tail.  No independent critical charge is formed.

### Axis — GREEN

The tail dilation axis becomes the translation axis `rho`; normal/tangential spherical components remain typed separately.

### Static aggregation — GREEN

Cubic tail mass is exactly Lebesgue mass on the log cylinder.  The quantity `mathscr R_3` is not added to this density; it is the invariant mean of this density.

### Dynamics — GREEN

Factor equivariance turns W1 time translation into log-radius translation and pushes every invariant W1 measure to a translation-invariant tail measure.

### Cross-audit — GREEN

There is no reverse implication from the tail density to W1 compactness or recurrence.  Compact recurrence is an upstream input used only to define the invariant factor measure.

---

## 10. Permanent RED firewall

The following are invalid:

1. counting `mathscr R_3` and the log-cylinder cubic density as two different critical resources;
2. treating one large log-radius slice as independent of the backward W1 history that generated it;
3. inferring injectivity of the tail factor from positivity of `mathscr R_3`;
4. using finite physical terminal time as a finite budget for the translation-invariant cubic density.

---

## 11. New frontier

The critical anomaly has now been completely moved onto a compact translation factor:

\[
\boxed{
\mathscr R_3>0
\Longleftrightarrow
\text{positive invariant cubic density on }(\mathcal T,D_\tau).
}
\]

M5-109 independently places a recurrent positive pressure/strain payer in one fixed W1 core.

The next task is therefore not another norm estimate.  It is to determine whether the finite-core payer descends to the tail factor, or whether its non-tail-measurable part lives entirely in the strong-critical fibers isolated in M5-115/M5-116.

This produces the exact next DSD split:

\[
\boxed{
\text{core payer}
=
\text{tail-factor component}
+\text{fiber component}.
}
\]

No claim is yet made that either component is contradictory.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
