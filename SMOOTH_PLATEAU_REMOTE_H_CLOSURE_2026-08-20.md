# Smooth Plateau / Remote-H Closure — 2026-08-20

Status: **S-LEVEL FINITE-TIME PLATEAU CLOSURE CRITERION. GLOBAL REGULARITY NOT PROVED.**

This note combines the smooth tightrope identity, the spectral-gap/radius uncertainty bound, and the instantaneous Hardy--Biot--Savart production ceiling. It shows that a positive-middle plateau can remain a `P_V` survival interval only if the derivative radius is sufficiently large.

## 1. Plateau equation

On a plateau of the running vorticity envelope,

\[
b=0.
\]

The smooth cross-order ledger is

\[
\boxed{
\frac12(\log\lambda)_s
+\nu\mathcal G
=\mathcal X,
}
\]

where

\[
\lambda=\frac PE,
\]

\[
\mathcal G=\frac HP-\frac PE,
\]

and

\[
\mathcal X=\frac NP-\frac AE.
\]

On the positive-middle determinant lane,

\[
A\ge0,
\]

so

\[
\boxed{
\mathcal X
\le
\frac NP.
}
\]

## 2. Instantaneous production ceiling

The Hardy--Biot--Savart estimate gives at every smooth time

\[
\boxed{
\frac NP
\le
C_P K_2^{1/5}Q^{2/5},
\qquad
C_P=\frac{15}{4}\pi^{-2/5},
}
\]

where

\[
K_2=\|\nabla^2\Omega\|_\infty,
\qquad
Q=\|\nabla\Omega\|_2^2.
\]

Thus

\[
\boxed{
\mathcal X
\le
X_{max}
:=
C_P K_2^{1/5}Q^{2/5}.
}
\]

## 3. Derivative tightness forces a viscous gap

From `SMOOTH_SPECTRAL_GAP_RADIUS_UNCERTAINTY_2026-08-20.md`,

\[
\boxed{
\mathcal G
\ge
\left(
R_D+rac{3}{2\sqrt\lambda}
\right)^{-2},
}
\]

where

\[
R_D^2
=
\frac1P
\int|x-X|^2|\nabla\Sigma|^2dx
\]

for the optimally chosen center.

Therefore

\[
\frac12(\log\lambda)_s
\le
X_{max}
-
\nu
\left(
R_D+rac{3}{2\sqrt\lambda}
\right)^{-2}.
\]

## 4. Direct plateau closure criterion

If at a plateau time

\[
\boxed{
\nu
\left(
R_D+rac{3}{2\sqrt\lambda}
\right)^{-2}
>
C_P K_2^{1/5}Q^{2/5},
}
\]

then

\[
\boxed{(\log\lambda)_s<0.}
\]

Thus the normalized derivative frequency decreases strictly while the vorticity record is not increasing.

Such an interval cannot be a stationary `P_V` survival/equality lane. It is a frequency-decay/viscous-reset interval.

## 5. Failure of plateau closure forces radius growth

Conversely, a plateau that avoids forced frequency decrease must satisfy

\[
\nu
\left(
R_D+rac{3}{2\sqrt\lambda}
\right)^{-2}
\le
X_{max}.
\]

Hence

\[
\boxed{
R_D
\ge
\left[
\sqrt{\frac{\nu}{C_P K_2^{1/5}Q^{2/5}}}
-
\frac{3}{2\sqrt\lambda}
\right]_+.
}
\]

Therefore survival of a positive-middle plateau has an explicit derivative-radius price.

If the right side becomes large along late first-hitting stages, the plateau automatically enters `H_remote`.

## 6. Replace Q by finite-stage derivative tightness data

Suppose on a smooth non-H stage there is a parent radius `R_P` and tail fraction `epsilon_H` such that

\[
\int_{|y-X|>R_P}|\nabla\Omega|^2dy
\le
\varepsilon_H Q.
\]

Let

\[
K_1=\|\nabla\Omega\|_\infty.
\]

Then

\[
(1-\varepsilon_H)Q
\le
K_1^2|B_{R_P}|,
\]

so

\[
\boxed{
Q
\le
\frac{4\pi}{3(1-\varepsilon_H)}
K_1^2R_P^3.
}
\]

Consequently

\[
\boxed{
X_{max}
\le
C_P
\left[
\frac{4\pi}{3(1-\varepsilon_H)}
\right]^{2/5}
K_2^{1/5}K_1^{4/5}R_P^{6/5}.
}
\]

This expresses the maximum plateau production entirely through finite-time analytic derivative bounds and a derivative-tight parent radius.

## 7. Clay-data analyticity specialization

On the smooth rapidly-decaying first-hitting track, if the complex vorticity bound is `M0` in a strip of radius `rho0`, one-dimensional Cauchy estimates along real directions give schematically

\[
K_1\le\frac{M_0}{\rho_0},
\qquad
K_2\le\frac{2M_0}{\rho_0^2}.
\]

Therefore

\[
K_2^{1/5}K_1^{4/5}
\le
2^{1/5}M_0\rho_0^{-6/5}.
\]

Hence

\[
\boxed{
X_{max}
\le
C_P2^{1/5}M_0
\left[
\frac{4\pi}{3(1-\varepsilon_H)}
\right]^{2/5}
\left(
\frac{R_P}{\rho_0}
\right)^{6/5}.
}
\]

All quantities are dimensionless in first-hitting coordinates.

## 8. Interpretation

The plateau branch now has no free low-cost limit.

- If derivative radius remains small, the viscous spectral gap is positive and can dominate the maximum available `P_V` cross-order production.
- If production remains strong enough to avoid frequency decay, the derivative radius must increase according to the explicit inequality.
- If the derivative radius increases without bound across stages, the state is in `H_remote`.

Thus the plateau side of the temporal gate and the remote-derivative side of System I are two descriptions of the same remaining corridor.

Status: **A POSITIVE-MIDDLE PLATEAU CAN AVOID VISCOSITY-DRIVEN FREQUENCY DECAY ONLY BY SATISFYING AN EXPLICIT LOWER BOUND ON THE DERIVATIVE RMS RADIUS. PLATEAU SURVIVAL IS THEREFORE QUANTITATIVELY COUPLED TO `H_remote`.**