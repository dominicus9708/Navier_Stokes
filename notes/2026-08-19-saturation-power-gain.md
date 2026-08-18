# Near-saturation power gain: local Betchov defect -> enstrophy/palinstrophy blow-up alternative

Date: 2026-08-19

Status: **DERIVED CONDITIONAL POWER-GAIN LEMMA / GLOBAL REGULARITY NOT PROVED**.

This note continues the reduced `M/H/T` endgame. It converts near-saturation of the middle-strain determinant bound into a strict power cost in global enstrophy-palinstrophy, unless the local Betchov shell flux is already large.

---

## 1. Local production and saturation defect

Let

\[
f=\lambda_2^+,
\]

and choose a nonnegative compactly supported cutoff `phi`.

Define

\[
\mathcal P_\phi
=\int \phi\,\omega\cdot S\omega,
\]

\[
A_\phi
=\int \phi f|S|^2,
\qquad
Q_\phi
=\int \phi f^3.
\]

The localized Betchov estimate from the previous note is

\[
\boxed{
\mathcal P_\phi+4Q_\phi
\le
2A_\phi+\mathcal F_{B,\phi,c},
}
\]

where `F_{B,phi,c}` is the exact translation-relative cubic shell flux.

Assume a fresh local stretching pulse satisfies

\[
\mathcal P_\phi\ge P_0>0,
\]

and the shell term is subdominant,

\[
|\mathcal F_{B,\phi,c}|
\le
\eta P_0,
\qquad 0\le\eta<1.
\]

Then

\[
\boxed{
A_\phi
\ge
\frac{1-\eta}{2}P_0.
}
\]

Define the local determinant-saturation defect ratio

\[
\boxed{
\delta_\phi
=\frac{Q_\phi}{A_\phi}
}
\]

whenever `A_phi>0`.

---

## 2. Production-weighted concentration of the planar regime

On the productive set define

\[
x=\frac{f}{|S|}.
\]

Using the probability measure

\[
d\mu_\phi
=\frac{\phi f|S|^2}{A_\phi}\,dx,
\]

we have exactly

\[
\int x^2d\mu_\phi
=\delta_\phi.
\]

For any `kappa>0`, Markov gives

\[
\mu_\phi\{x>\kappa\}
\le
\frac{\delta_\phi}{\kappa^2}.
\]

Choose

\[
\boxed{
\kappa=2\sqrt{\delta_\phi}.
}
\]

Then

\[
\mu_\phi\{x>\kappa\}\le\frac14,
\]

so the good near-planar set

\[
G_\kappa=\{x\le\kappa\}
\]

carries at least three quarters of `A_phi`:

\[
A_{\phi,G}
\ge
\frac34A_\phi
\ge
\frac{3(1-\eta)}8P_0.
\]

On `G_kappa`,

\[
f|S|^2\le\kappa|S|^3.
\]

Therefore

\[
\boxed{
\int \phi|S|^3
\ge
\frac{3(1-\eta)}{16}
P_0\,\delta_\phi^{-1/2}.
}
\]

Thus increasingly precise determinant saturation forces a genuine `L^3` strain-amplitude gain unless the shell flux is already order one.

---

## 3. Convert the local L3 gain to H/T cost

The whole-space Gagliardo--Nirenberg estimate gives

\[
\|S\|_3^3
\le
C_{GN}\|S\|_2^{3/2}\|\nabla S\|_2^{3/2}.
\]

Using the exact Fourier identities

\[
\|S\|_2^2=\frac12E_\omega,
\qquad
\|\nabla S\|_2^2=\frac12P_\omega,
\]

we obtain

\[
\|S\|_3^3
\le
C_*(E_\omega P_\omega)^{3/4}.
\]

Combining with the previous lower bound yields

\[
\boxed{
E_\omega P_\omega
\ge
c_*(1-\eta)^{4/3}
P_0^{4/3}
\delta_\phi^{-2/3}.
}
\]

Equivalently,

\[
\boxed{
\max\{E_\omega,P_\omega\}
\ge
c_*^{1/2}(1-\eta)^{2/3}
P_0^{2/3}
\delta_\phi^{-1/3}.
}
\]

This is the strict power gain sought in the late-frontier target.

---

## 4. First-hitting interpretation

In the normalized first-hitting variables,

\[
\|\Omega\|_\infty\le1.
\]

Therefore a sequence with

\[
E_\Omega\to\infty
\]

cannot remain spatially tight in any fixed bounded region.

On the other hand,

\[
P_\Omega\to\infty
\]

is precisely a higher-derivative/palinstrophy escalation and is routed to `H`.

Hence, for an order-one fresh local stretching pulse `P0` and subdominant shell flux,

\[
\boxed{
\delta_\phi\to0
\Longrightarrow
H\ \text{or}\ T.
}
\]

If the shell flux is not subdominant, the branch is already `T`.

Thus the nearly determinant-saturated `M` branch is no longer an independent compact low-derivative escape route.

---

## 5. Revised M/H/T trichotomy

For a fresh local production pulse, one now has the conditional reduction

\[
\boxed{
\text{fresh production}
\Longrightarrow
\begin{cases}
\text{non-negligible determinant defect / critical }M\text{ excess},\\
H\text{ via palinstrophy/derivative escalation},\\
T\text{ via shell flux or spatial non-tightness}.
\end{cases}
}
\]

The genuinely unresolved `M` subbranch is therefore the one in which `delta_phi` stays bounded away from zero while the critical middle-strain channel repeatedly remains active.

The final global issue is still whether such non-saturated `M` episodes can occur on infinitely many first-hitting intervals without violating the established critical middle-eigenvalue regularity criteria or forcing an unsummable derivative/transport cost.

Status: **STRICT DELTA^(-1/3) SIZE GAIN OBTAINED FOR NEAR-SATURATED M; NEAR-SATURATED COMPACT M REDUCED TO H/T; NON-SATURATED CRITICAL M REPETITION REMAINS OPEN**.
