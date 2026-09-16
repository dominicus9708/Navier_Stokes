# M19-328 — Normalized log-kappa entropy removes mean amplitude growth and exposes coefficient-growth covariance as the internal signed channel

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / EXACT NORMALIZED ENTROPY IDENTITY / SIGNED COVARIANCE CHANNEL / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M19-326--327 reduce the spatial CE-H coefficient-variance branch to positive log-kappa diffusion plus already typed source/interface channels. M17-394's materially integrated identity contains an apparently independent amplitude-growth entropy term

\[
2\int\chi\rho^2(\sigma+\kappa)\log|\kappa|dx.
\]

This module normalizes by the material packet enstrophy and shows that the mean amplitude-growth part cancels exactly. The surviving internal signed term is a covariance between coefficient phase and amplitude growth.

## 2. Material packet probability

Work on a sign-preserving CE-H material carrier with smooth material cutoff

\[
D_t\chi=0.
\]

Set

\[
z:=\log|\kappa|,
\qquad
g:=\sigma+\kappa.
\]

The vorticity amplitude obeys

\[
D_t\rho=g\rho,
\qquad
D_t\rho^2=2g\rho^2.
\]

Define packet mass

\[
M(t):=\int\chi\rho^2dx,
\]

and the normalized material probability

\[
\boxed{
d\pi_t=\frac{\chi\rho^2}{M(t)}dx.}
\]

Then

\[
\boxed{
\frac{M'}{M}=2\langle g\rangle_{\pi_t}.
}
\]

## 3. Normalized centered log coefficient

Define

\[
H(t):=\int\chi\rho^2z\,dx,
\qquad
h(t):=\frac{H(t)}{M(t)}=\langle z\rangle_{\pi_t}.
\]

M17-394 gives

\[
\begin{aligned}
H'
={}&
\int\chi\rho^2|\nabla z|^2dx\\
&-
\int\rho^2\nabla\chi\cdot\nabla z\,dx\\
&+
\int\chi\rho^2
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}dx\\
&+
2\int\chi\rho^2gz\,dx.
\end{aligned}
\]

Divide by \(M\) and use

\[
h'=\frac{H'}M-h\frac{M'}M.
\]

The amplitude term becomes

\[
2\langle gz\rangle_\pi
-2\langle g\rangle_\pi\langle z\rangle_\pi
=
2\operatorname{Cov}_\pi(g,z).
\]

Therefore

\[
\boxed{
\begin{aligned}
h'
={}&
D_z
+S_{interface}
+S_{force}
+2C_{gz},
\end{aligned}
}
\]

where

\[
\boxed{
D_z:=\langle|\nabla z|^2\rangle_\pi\ge0,
}
\]

\[
S_{interface}
:=-\frac1M
\int\rho^2\nabla\chi\cdot\nabla z\,dx,
\]

\[
S_{force}
:=
\left\langle
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}
\right\rangle_\pi,
\]

and

\[
\boxed{
C_{gz}:=\operatorname{Cov}_\pi(g,z).
}
\]

## 4. Exact cancellation of mean amplitude growth

The identity proves

\[
\boxed{
\text{mean packet growth }\langle g\rangle_\pi
\text{ is not an independent entropy payer.}
}
\]

Only differential growth correlated with coefficient phase survives:

\[
\boxed{
\text{internal signed amplitude channel}
=
2\operatorname{Cov}_\pi(\sigma+\kappa,\log|\kappa|).
}
\]

Thus uniform multiplication of all packet amplitudes changes \(M\) but not the normalized coefficient entropy \(h\).

## 5. Recurrent invariant-mean law

On a compact recurrent sign-preserving branch, \(h\) is a bounded state observable after intrinsic centering if needed. Therefore its invariant mean derivative vanishes:

\[
\langle h'\rangle=0.
\]

Hence

\[
\boxed{
\langle D_z\rangle
+
\langle S_{interface}\rangle
+
\langle S_{force}\rangle
+
2\langle C_{gz}\rangle
=0.
}
\]

If M19-326 supplies

\[
\langle D_z\rangle\ge d_*>0,
\]

then at least one compensating signed mean must be nonzero and negative:

\[
\boxed{
\langle S_{interface}\rangle<0
\quad\lor\quad
\langle S_{force}\rangle<0
\quad\lor\quad
\langle C_{gz}\rangle<0
}
\]

quantitatively, one channel has magnitude at least a fixed fraction of \(d_*\).

## 6. Closed-carrier simplification

If one can choose a genuinely closed material carrier with no coefficient flux through the cutoff region, then

\[
S_{interface}=0.
\]

The identity becomes

\[
\boxed{
\langle D_z\rangle
+
\langle S_{force}\rangle
+
2\langle C_{gz}\rangle=0.
}
\]

Therefore positive coefficient diffusion must be sustained by normalized strain/geometric forcing and/or a negative coefficient-growth covariance.

Failure to construct such a closed carrier remains an explicit interface/genealogy exit and must not be silently removed.

## 7. Covariance interpretation

Because

\[
g=\sigma+\kappa,
\qquad
z=\log|\kappa|,
\]

\[
C_{gz}
=
\operatorname{Cov}_\pi(\sigma,\log|\kappa|)
+
\operatorname{Cov}_\pi(\kappa,\log|\kappa|).
\]

The second covariance has a definite monotone-function sign on each fixed-sign coefficient branch:

- if \(\kappa>0\), both \(\kappa\) and \(\log\kappa\) are increasing, so
  \[
  \operatorname{Cov}_\pi(\kappa,\log\kappa)\ge0;
  \]
- if \(\kappa<0\), \(\log|\kappa|\) decreases as \(\kappa\) increases, so
  \[
  \operatorname{Cov}_\pi(\kappa,\log|\kappa|)\le0.
  \]

Thus the negative-kappa branch possesses an intrinsic negative coefficient self-covariance capable of recycling positive log diffusion. This is a genuine structural mechanism, not automatically a contradiction.

## 8. Quantitative covariance bound

Cauchy--Schwarz gives

\[
|C_{gz}|
\le
\operatorname{Var}_\pi(g)^{1/2}
\operatorname{Var}_\pi(z)^{1/2}.
\]

Hence if coefficient variance is fixed while the forcing/interface channels are small, a fixed diffusion payment forces nontrivial spatial variance in the local growth rate \(g=\sigma+\kappa\).

This produces a new conditional route:

\[
\boxed{
D_z^+ + \text{small force/interface}
\Longrightarrow
\operatorname{Var}_\pi(\sigma+\kappa)>0.
}
\]

It is a phase-segregation statement, not yet a finite-budget contradiction.

## 9. Relation to M19-325 temporal breathing

M19-325 shows that the temporal coefficient branch is effective-frequency breathing. M19-328 shows that on the spatial branch the normalized entropy return is serviced by coefficient-growth covariance.

Thus both branches are recurrent phase phenomena:

\[
\boxed{
\text{temporal }P/E\text{ breathing}
\quad\text{or}\quad
\text{spatial coefficient-growth covariance circulation}.
}
\]

A closure theorem must break this recurrent phase recycling, not merely identify another positive local derivative norm.

## 10. Accumulation firewall

The covariance is signed and can have nonzero invariant mean, but it is not a one-way bounded scalar drift. A stationary recurrent distribution can sustain a nonzero covariance indefinitely.

Therefore

\[
\boxed{
\langle C_{gz}\rangle\ne0
\not\Rightarrow
\text{finite exhaustion}.
}
\]

The next useful calculation is to determine whether the exact CE-H relation and trace-free strain constraints force the required negative covariance into already saturated palinstrophy/raw-H2 channels, or whether it represents a genuine independent recurrent factor.

## 11. Conclusion

Normalizing the M17-394 entropy by the material packet mass removes the apparent mean amplitude-growth payer exactly. The surviving internal signed channel is

\[
\boxed{
2\operatorname{Cov}_\pi(\sigma+\kappa,\log|\kappa|).
}
\]

Hence the spatial coefficient-current problem has been reduced from four apparent compensators to interface/forcing plus one intrinsic signed covariance.

\[
\boxed{
\text{M19-328 COMPLETE; NEXT TARGET: DECOMPOSE THE REQUIRED NEGATIVE COVARIANCE USING CE-H STRAIN/COEFFICIENT GEOMETRY.}
}
\]
