# DSD W1: Barker--Prange -> positive-density critical shell recovery

Date: 2026-08-25

Status: **POSITIVE-DENSITY SHELL RECOVERY PROVED CONDITIONAL ON W1 FULL-TIME WEAK-L3 AND THE EXTERNAL BARKER--PRANGE TYPE-I THEOREM / NO DIRECT CONTRADICTION CLAIMED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose and correction discipline

An earlier audit correctly withdrew the false claim that the Barker--Prange lower bound contradicts the logarithmic upper growth available under a uniform weak-`L3` bound.

The actual Theorem A lower bound is on the cubic integral,

\[
\int_{|x|<R}|u(x,t)|^3dx
\ge c_{BP}(M)
\log\frac{R^2}{C_{BP}(M)(T^*-t)},
\]

for radii in the theorem's Type-I range.

That growth is endpoint-compatible with a `1/r` tail. The present note does **not** reinstate the withdrawn contradiction.

Instead, W1 supplies a new ingredient not used in that false comparison: a uniform upper bound on the cubic mass of each dyadic shell. The logarithmic total lower bound then forces a positive density of shells with a fixed positive cubic mass.

## 2. W1 shell upper bound

Fix dyadic normalized annuli

\[
A_k=\{R_k<|Y|<2R_k\},
\qquad R_k=2^kR_0.
\]

Let `c_k` be the annular mean and let `f_k` denote the standard divergence-free localized fluctuation packet. On W1 assume

\[
\mathfrak C_k
:=R_k^{-1}\|f_k\|_2^2
\le C_C,
\]

and

\[
\Gamma_k
:=\frac{R_k\|\nabla f_k\|_2}{\|f_k\|_2}
\le\Gamma_*.
\]

Then

\[
\|f_k\|_2
\le C_C^{1/2}R_k^{1/2},
\]

and

\[
\|\nabla f_k\|_2
\le\Gamma_*C_C^{1/2}R_k^{-1/2}.
\]

Sobolev gives

\[
\|f_k\|_6
\le C_S\Gamma_*C_C^{1/2}R_k^{-1/2}.
\]

Interpolating `L2` and `L6`,

\[
\|f_k\|_3
\le\|f_k\|_2^{1/2}\|f_k\|_6^{1/2},
\]

so

\[
\boxed{
\|f_k\|_3^3
\le
(C_S\Gamma_*)^{3/2}C_C^{3/2}.
}
\]

The annular mean obeys the already used Campanato telescoping bound

\[
|c_k|\lesssim C_C^{1/2}R_k^{-1}
\]

on the tail, using the global `Lp`, `p>3`, decay to fix the constant at infinity. Therefore

\[
\int_{A_k}|c_k|^3dY
\lesssim C_C^{3/2}.
\]

Thus the complete shell cubic mass

\[
m_k:=\int_{A_k}|U|^3dY
\]

has a stage- and age-independent ceiling

\[
\boxed{
m_k\le M_A<\infty,}
\]

where `M_A` depends only on the W1 Campanato/frequency/localization constants.

## 3. Convert the Barker--Prange radius to normalized radius

On the first-hitting Type-I corridor,

\[
r(t)\asymp\sqrt{T^*-t}
\]

up to fixed viscosity and remaining-time factors.

Choose a fixed `delta>0` and a physical radius

\[
\mathcal R(t)=(T^*-t)^{1/2-\delta}
\]

multiplied, if needed, by one fixed constant so that it lies in the Barker--Prange admissible interval for all sufficiently late times.

The corresponding normalized radius is

\[
K(t):=\frac{\mathcal R(t)}{r(t)}
\asymp (T^*-t)^{-\delta}.
\]

Therefore

\[
\boxed{
\log K(t)
=\delta\log\frac1{T^*-t}+O(1).
}
\]

The cubic integral is scale invariant, modulo the fixed viscosity normalization in this repository. Hence Theorem A gives

\[
\boxed{
\int_{|Y|<K(t)}|U(Y,s)|^3dY
\ge c_1(M,\nu)\log K(t)-C_1(M,\nu).
}
\]

No power mismatch is asserted: both sides are logarithmic.

## 4. Positive average cubic mass per log shell

Let `N=N(t)` be the number of dyadic annuli between the fixed core radius `R0` and `K(t)`. Then

\[
N=\frac{\log K(t)}{\log2}+O(1).
\]

The fixed core contributes only `O(1)` cubic mass because of local analyticity. Therefore, for all sufficiently late times,

\[
\sum_{k=0}^{N-1}m_k
\ge a_0N
\]

for one fixed

\[
\boxed{a_0=a_0(M,\nu)>0.}
\]

Thus W1 cannot realize the Barker--Prange lower bound through an arbitrarily sparse or vanishing-average collection of shells.

## 5. Positive-density selection

Since every shell obeys

\[
0\le m_k\le M_A,
\]

let

\[
G_N:=\{0\le k<N:m_k\ge a_0/2\}.
\]

If `g_N=|G_N|`, then

\[
a_0N
\le\sum_{k<N}m_k
\le g_NM_A+(N-g_N)\frac{a_0}{2}.
\]

Hence

\[
\boxed{
\frac{g_N}{N}
\ge
\rho_*
:=
\frac{a_0}{2M_A-a_0}>0.
}
\]

Therefore

\[
\boxed{
\text{a fixed positive fraction of late dyadic shells satisfies }
\int_{A_k}|U|^3dY\ge a_0/2.
}
\]

This is the positive-density occupied-shell property previously used conditionally in the historical-shell calculations.

## 6. Immediate historical consequence

Because `N(t)->infinity`, at each sufficiently late time there exists an occupied shell whose age is at least a fixed positive fraction of `N(t)`.
Thus its scale ratio to the current core satisfies

\[
K_{old}\to\infty.
\]

The existing sliding-history remaining-time lemma then applies on the non-H/non-T/pressure-quiet lane: an old occupied natural-frequency packet cannot be strongly forgotten in the `O(K_old^{-2})` fraction of its own natural time left before `T*`.

Accordingly the **sliding/forgetful** W1 tail is routed to

\[
\boxed{
H\lor T\lor\text{pressure/localization residual}.
}
\]

This is now fed by a theorem-level positive-density shell input rather than by a separate positive-density hypothesis.

## 7. What remains

The argument does not eliminate the genuinely persistent passive history in which the positive-density old shells remain present rather than being forgotten.
A `1/r` or DSS-like log-periodic tail can saturate simultaneously

\[
\text{constant cubic mass per log shell},
\]

\[
\text{finite total enstrophy},
\]

and

\[
\text{critical physical/normalized energy scaling}.
\]

Indeed Barker--Prange explicitly note optimal logarithmic behavior for a class of potential backward DSS solutions.

Thus the updated W1 tail split is

\[
\boxed{
W_1
\Longrightarrow
H/T/\text{forgetting exit}
\lor
\text{persistent positive-density passive history}.
}
\]

Combined with the minimal-set note, the persistent endpoint remains tied to the long-period DSS or aperiodic recurrent-core rigidity problem.

## 8. External theorem used

T. Barker and C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Commun. Math. Phys. 385 (2021), Theorem A. The theorem assumes a full-time Type-I `L_t^infty L_x^{3,infty}` bound and gives the explicit logarithmic lower bound for the local cubic integral.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
