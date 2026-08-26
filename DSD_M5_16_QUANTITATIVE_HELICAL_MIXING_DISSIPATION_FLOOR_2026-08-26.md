# DSD M5-16 — Quantitative Helical Mixing Dissipation Floor

Date: 2026-08-26

Status: **DERIVED PRELIMIT CRITICAL MIXING ESTIMATE / POSITIVE CRITICAL CASCADE FORCES BOTH HELICITY SECTORS TO PARTICIPATE IN H^{3/2} DISSIPATION / THIS IS NOT YET A GLOBAL W1 CLOSURE / GLOBAL REGULARITY UNPROVED.**

## 1. Setting

Work at one smooth finite prelimit time where the homogeneous Sobolev quantities below are finite.

Use helical projectors `P_+`, `P_-` and write

\[
u=u_++u_-.
\]

Define

\[
X_\pm:=\frac12\|\Lambda^{1/2}u_\pm\|_2^2,
\qquad
Y_\pm:=\|\Lambda^{3/2}u_\pm\|_2^2.
\]

Let

\[
N:=\mathbb P(u\cdot\nabla u).
\]

The critical sector equations are

\[
X_\pm' + \nu Y_\pm = T_\pm,
\qquad
T_\pm:=-\langle N,\Lambda u_\pm\rangle.
\]

## 2. Exact helicity constraint on the nonlinear transfer

The Euler nonlinearity conserves helicity.
Since helicity is proportional to `X_+-X_-`, its nonlinear contribution vanishes:

\[
\boxed{T_+-T_-=0.}
\]

Hence

\[
\boxed{T_+=T_-}
\]

and the total critical Sobolev source is

\[
T_{crit}:=T_++T_-=2T_-=2T_+.
\]

This identity is exact at the finite prelimit level.

## 3. Standard H^{-1/2} nonlinear estimate

Sobolev embedding gives

\[
\dot H^{1/2}(\mathbb R^3)\hookrightarrow L^3,
\qquad
\dot H^{1/2}\ni \nabla u \hookrightarrow L^3
\]

when `u in dot H^{3/2}`.
Therefore

\[
\|u\cdot\nabla u\|_{L^{3/2}}
\le
\|u\|_3\|\nabla u\|_3
\lesssim
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}.
\]

By dual Sobolev embedding `L^{3/2} -> dot H^{-1/2}` and boundedness of the Leray projector,

\[
\boxed{
\|N\|_{\dot H^{-1/2}}
\le
C
\|u\|_{\dot H^{1/2}}
\|u\|_{\dot H^{3/2}}.
}
\]

## 4. Minority-sector degeneration

Pairing with the minus sector,

\[
|T_-|
=
|\langle \Lambda^{-1/2}N,\Lambda^{3/2}u_-\rangle|
\le
\|N\|_{\dot H^{-1/2}}\,Y_-^{1/2}.
\]

Hence, with

\[
X:=X_++X_-,
\qquad
Y:=Y_++Y_-,
\]

we get

\[
|T_-|
\le
C X^{1/2}Y^{1/2}Y_-^{1/2}.
\]

The identical argument with the plus sector gives

\[
|T_+|
\le
C X^{1/2}Y^{1/2}Y_+^{1/2}.
\]

Since `Tcrit=2T_-=2T_+`,

\[
\boxed{
|T_{crit}|
\le
C X^{1/2}Y^{1/2}
\min\{Y_+^{1/2},Y_-^{1/2}\}.
}
\]

Thus the total critical nonlinear source degenerates quantitatively when either helical sector loses `dot H^{3/2}` participation.

## 5. Quantitative two-sector floor under active cascade

Suppose at a given time the nonlinear critical source overcomes a fixed fraction of viscous critical dissipation:

\[
T_{crit}\ge \theta\nu Y,
\qquad \theta>0.
\]

Then the previous estimate implies

\[
\theta\nu Y
\le
C X^{1/2}Y^{1/2}
\min\{Y_+^{1/2},Y_-^{1/2}\}.
\]

If `Y>0`, after squaring and dividing,

\[
\boxed{
\min\{Y_+,Y_-\}
\ge
c\frac{\theta^2\nu^2}{X}\,Y.
}
\]

Therefore a genuinely active large critical cascade cannot be supported by an arbitrarily homochiral **dissipation** state unless the total critical `dot H^{1/2}` size `X` simultaneously becomes arbitrarily large.

## 6. Relation to M5-15

M5-15 gave only the qualitative statement

\[
\text{positive critical transfer}
\Longrightarrow
\text{two-helicity participation}.
\]

M5-16 strengthens this to a quantitative dissipation-sector floor.

However the floor weakens like `1/X`. A cross-radius `1/r` corridor can make the global prelimit `dot H^{1/2}` size grow logarithmically, so this estimate alone does not produce a uniform positive fraction at arbitrarily late times.

This is a crucial limitation.

## 7. Domain audit

The identities above are used on finite smooth prelimit states.

The W1 `1/r` corridor may fail to belong globally to `dot H^{1/2}`, so `X_\pm` are not automatically finite on the omega-limit state. Consequently the estimate must not be promoted directly to a global W1 invariant statement without localization/truncation and control of the corresponding boundary fluxes.

## 8. Updated M5 target

The helical route has now reduced to a sharper question:

> Can one localize the quantitative minority-sector estimate to a scale-critical spectral or physical window **without introducing an uncontrolled boundary transfer**, and obtain a scale-uniform two-helicity floor?

If yes, the full W1 corridor would require persistent cross-helical mixing on every active critical window.
If no, the localization boundary flux itself becomes the next critical transport object.

No contradiction is claimed here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
