# DSD M5-04 — Critical Compactness and the Infrared Dilation Defect

Date: 2026-08-26

Status: **M5 SUBSTEP / EXPLICIT DIVERGENCE-FREE DILATION SEQUENCE SHOWS THAT THE CURRENT `Lp`, `p>3`, COMPACTNESS AND EVEN VANISHING `H1`/`D3` COST DO NOT CONTROL THE `K` DEFECT / M5 IS AN ENDPOINT CRITICAL-COMPACTNESS PROBLEM / GLOBAL REGULARITY UNPROVED.**

## 1. Question

The canonical stack currently has global/precompact control in `Lp`, `p>3`, on the W1 lane, while the unresolved boundary coordinate is

\[
K(U;\lambda)
=\frac\lambda2\int (|U|^2-\lambda^2)_+dY.
\]

Does stronger use of the already available supercritical compactness automatically control `K` as `lambda downarrow 0`?

The answer is no.

---

## 2. Exact divergence-free critical dilation sequence

Fix a nonzero divergence-free

\[
\phi\in C_c^\infty(\mathbb R^3;\mathbb R^3).
\]

For `R>=1`, define

\[
\boxed{
U_R(Y)=R^{-1}\phi(Y/R).
}
\]

This is exactly the Navier--Stokes critical spatial dilation with scale `lambda_NS=1/R`.

For every `p>3`,

\[
\boxed{
\|U_R\|_p^p
=R^{3-p}\|\phi\|_p^p
\longrightarrow0.
}
\]

Thus `U_R -> 0` strongly in every fixed `Lp`, `p>3`.

---

## 3. Even derivative costs vanish

A direct calculation gives

\[
\nabla U_R(Y)=R^{-2}(\nabla\phi)(Y/R),
\]

hence

\[
\boxed{
\|\nabla U_R\|_2^2
=R^{-1}\|\nabla\phi\|_2^2
\longrightarrow0.
}
\]

Likewise the cubic viscous quantity scales as

\[
\boxed{
D_3(U_R)=R^{-2}D_3(\phi)
\longrightarrow0.
}
\]

Therefore neither small `H1` cost nor small `D3` cost at one state sees the critical boundary mode.

---

## 4. The `K` defect survives exactly

Choose a fixed `theta>0` below `||phi||_infinity` and set

\[
\lambda_R=\theta/R.
\]

Then

\[
\begin{aligned}
K(U_R;\lambda_R)
&=\frac{\theta}{2R}
\int
\left(R^{-2}|\phi(Y/R)|^2-\theta^2R^{-2}\right)_+dY\\
&=\boxed{
\frac\theta2
\int (|\phi(z)|^2-\theta^2)_+dz
}.
\end{aligned}
\]

The right-hand side is a positive constant independent of `R` when the chosen level intersects the nonzero profile.

Thus

\[
\boxed{
U_R\to0\text{ strongly in every }L^p,\ p>3,
\quad
\|\nabla U_R\|_2\to0,
\quad
D_3(U_R)\to0,
}
\]

while simultaneously

\[
\boxed{
K(U_R;\lambda_R)\not\to0,
\qquad
\lambda_R\downarrow0.
}
\]

This is the exact joint-boundary defect.

---

## 5. Critical spaces detect the mode

For the same sequence,

\[
\|U_R\|_3=\|\phi\|_3,
\]

and

\[
\|U_R\|_{\dot H^{1/2}}
=\|\phi\|_{\dot H^{1/2}}.
\]

Hence the escaping mode is invisible to `p>3` compactness but remains order one in standard critical spaces.

This gives the correct endpoint interpretation:

\[
\boxed{
M5=\text{upgrade from supercritical compactness to defect-aware critical compactness}.
}
\]

A particularly clean sufficient condition is late-orbit precompactness in `L3`.

Indeed

\[
K(U;\lambda)
\le \frac12\int_{|U|>\lambda}|U|^3dY.
\]

For a compact subset of `L3`, the right-hand side tends to zero uniformly as `lambda downarrow 0`. Therefore

\[
\boxed{
\text{late precompactness in }L^3
\Longrightarrow
\lim_{\lambda\downarrow0}\sup_sK(U(s);\lambda)=0
\Longrightarrow
M5\text{ closes}.
}
\]

The repository does not currently prove this critical precompactness.

---

## 6. DSD interpretation

The defect lives on the coupled projective boundary

\[
\lambda R=O(1).
\]

The sequence above realizes it by simultaneously sending

\[
R\to\infty,
\qquad
\lambda\to0.
\]

It is therefore inaccurate to describe the mode as either

- a purely spatial tail, or
- a purely zero-amplitude defect.

It is one joint critical state-boundary mode.

In Fourier variables the dilation moves the characteristic frequency toward zero as `R -> infinity`. This is an **infrared mode in Leray coordinates**. It must not automatically be interpreted as a physical inverse energy cascade: the Leray dilation itself shifts fixed physical scales toward larger normalized radii / lower normalized frequencies.

---

## 7. Consequence for the M5 search

M5-01 ruled out ordinary energy/dissipation as sufficient for uniform tail control.

M5-02 ruled out scale-invariant parabolic persistence as sufficiently long.

M5-03 ruled out instantaneous norm-only pressure absorption as non-circular.

M5-04 now rules out the idea that the already established `Lp`, `p>3`, compactness plus local derivative control automatically upgrades to the critical boundary.

The next nonredundant question is therefore:

\[
\boxed{
\textbf{can the Navier--Stokes time dynamics prevent this critical dilation mode from being generated/maintained along the prelimit history?}
}
\]

Equivalently, one needs a **dynamic inter-scale lineage theorem** or another mechanism producing actual critical `L3`/`K` compactness.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
