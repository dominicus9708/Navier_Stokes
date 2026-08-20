# Smooth Finite-Stage Tightrope Ledger — 2026-08-20

Status: **S-LEVEL IDENTITY ON THE ORIGINAL SMOOTH NAVIER--STOKES SOLUTION. GLOBAL REGULARITY NOT PROVED.**

This note deliberately leaves the ancient-limit/recurrent-profile mainline. All identities below are stated on a finite smooth lifespan interval `t < T*` and on a finite geometric first-hitting stage.

## 1. Running first-hitting envelope

Let

\[
M(t)=\max\left\{M(t_0),\sup_{t_0\le\tau\le t}\|\omega(\tau)\|_\infty\right\}.
\]

On a geometric stage `[t0,t1]`, assume

\[
M(t_1)=qM(t_0),\qquad q>1.
\]

Set

\[
\lambda(t)=M(t)^{1/2},
\qquad
\frac{ds}{dt}=M(t),
\]

and use a fixed spatial reference center `X0`:

\[
y=\lambda(t)(x-X_0).
\]

Define normalized strain by

\[
S(x,t)=M(t)\Sigma(y,s).
\]

No limiting profile is introduced.

At almost every time where the monotone envelope is differentiable define

\[
\boxed{b(s)=\frac{d}{ds}\log M=\frac{M'(t)}{M(t)^2}\ge0.}
\]

Since the stage amplifies by `q`,

\[
\boxed{\int_{I_j}b(s)ds=\log q.}
\]

## 2. Normalized strain norms

Write

\[
E=\|\Sigma\|_2^2,
\qquad
P=\|\nabla\Sigma\|_2^2,
\qquad
H=\|\Delta\Sigma\|_2^2.
\]

The corresponding physical quantities scale as

\[
E_{phys}=M^{1/2}E,
\qquad
P_{phys}=M^{3/2}P,
\qquad
H_{phys}=M^{5/2}H.
\]

Define the normalized L2 strain production

\[
A=-2\int_{\mathbb R^3}\det\Sigma\,dy,
\]

and normalized H1 production

\[
N=-\langle\mathcal R_{VI}^{norm},-\Delta\Sigma\rangle.
\]

Their physical versions scale respectively like `M^(3/2)` and `M^(5/2)`.

## 3. Exact finite-stage L2 ledger

The physical strain identity is

\[
\frac12\frac d{dt}\|S\|_2^2
+\nu\|\nabla S\|_2^2
=-2\int\det S.
\]

Substitution of the running first-hitting normalization gives, exactly on the smooth interval,

\[
\boxed{
\frac12E_s+rac14bE+\nu P=A.
}
\]

Since a nonzero finite-energy strain cannot have `E=0`, division by `E` gives

\[
\boxed{
\frac12(\log E)_s+rac14b+\nu\frac PE=\frac AE.
}
\]

## 4. Exact finite-stage H1 ledger

The physical H1 identity is

\[
\frac12\frac d{dt}\|\nabla S\|_2^2
+\nu\|\Delta S\|_2^2
=N_{phys}.
\]

After normalization,

\[
\boxed{
\frac12P_s+rac34bP+\nu H=N.
}
\]

For a nontrivial finite-energy field `P>0`, so

\[
\boxed{
\frac12(\log P)_s+rac34b+\nu\frac HP=\frac NP.
}
\]

This is the smooth finite-stage origin of the scale-damping term. No ancient self-similar profile and no recurrence hypothesis is required.

## 5. Cross-order tightrope identity

Subtract the L2 log ledger from the H1 log ledger. Define

\[
\chi=\frac PE.
\]

Then

\[
\boxed{
\frac12(\log\chi)_s
+\frac12b
+\nu\left(\frac HP-\frac PE\right)
=
\frac NP-\frac AE.
}
\]

By Cauchy--Schwarz,

\[
P^2
=\langle-\Delta\Sigma,\Sigma\rangle^2
\le EH,
\]

therefore

\[
\boxed{
\frac HP-\frac PE\ge0.
}
\]

The viscous term in the cross-order ledger has the favorable sign.

## 6. Exact geometric-stage identity

Integrating from the first hitting of `M_j` to the first hitting of `qM_j` gives

\[
\boxed{
\begin{aligned}
&\frac12\log\frac{\chi_1}{\chi_0}
+\frac12\log q\\
&\quad+
\nu\int_{I_j}
\left(\frac HP-\frac PE\right)ds
=
\int_{I_j}
\left(\frac NP-\frac AE\right)ds.
\end{aligned}
}
\]

This is the central smooth-only tightrope equation.

Interpretation: every finite geometric vorticity amplification stage must pay a cross-order production excess of at least one half-logarithmic scale unit, modulo the finite endpoint change of the normalized frequency `chi` and with an additional nonnegative viscous spectral-gap cost.

## 7. Repeated stages without a limit object

For consecutive stages `j=0,...,J-1`, telescoping gives

\[
\boxed{
\begin{aligned}
&\frac12\log\frac{\chi_J}{\chi_0}
+\frac J2\log q\\
&\quad+
\nu\int_{s_0}^{s_J}
\left(\frac HP-\frac PE\right)ds
=
\int_{s_0}^{s_J}
\left(\frac NP-\frac AE\right)ds.
\end{aligned}
}
\]

This statement remains entirely on the original smooth solution for every finite `J`.

If a pruned non-H/T lane supplies finite constants

\[
0<\chi_-\le\chi_j\le\chi_+<\infty
\]

at its first-hitting checkpoints, then

\[
\frac1J
\int_{s_0}^{s_J}
\left(\frac NP-\frac AE\right)ds
\ge
\frac12\log q
-
\frac1{2J}\log\frac{\chi_+}{\chi_-}.
\]

Thus the cross-order excess cannot disappear asymptotically on a smooth bounded-frequency lane.

## 8. Two-sided tightrope interpretation

The identity also shows why overproduction is not free.

If on many stages

\[
\int_{I_j}\left(\frac NP-\frac AE\right)ds
\]

substantially exceeds

\[
\frac12\log q
+\nu\int_{I_j}
\left(\frac HP-\frac PE\right)ds,
\]

then `chi=P/E` grows geometrically and the lane exits the bounded normalized derivative-frequency class. That is an `H`-type exit.

If the cross-order excess is substantially smaller than `1/2 log q`, `chi` decreases geometrically and a fixed natural-scale derivative core cannot persist. That is a tightness/turnover exit.

Hence the surviving smooth lane must balance on the finite-stage equality itself:

\[
\boxed{
\text{too little cross-order production}\to T,
\qquad
\text{too much}\to H,
\qquad
\text{survival}\to\text{narrow balance}.
}
\]

## 9. Status discipline

This identity is `S-level`: it holds directly for the original smooth solution before any singular time.

Ancient limits may still be used to discover candidate estimates for the integrand

\[
\frac NP-\frac AE,
\]

but a candidate estimate is promoted to the main proof only after it is rewritten uniformly on the finite first-hitting stages above.

Status: **THE MAINLINE NOW HAS AN EXACT SMOOTH FINITE-STAGE TIGHTROPE IDENTITY. THE NEXT DIRECT TARGET IS A UNIFORM ESTIMATE OF THE CROSS-ORDER PRODUCTION EXCESS `N/P - A/E` ON THE PRUNED SINGLE-CORE P_V LANE.**