# Leray Betchov Positive-Middle Statistical Floor — 2026-08-24

Status: **EXACT KINEMATIC REDUCTION + POSITIVE-MIDDLE ACTION FLOOR / GLOBAL REGULARITY NOT PROVED.**

This note combines the recurrent Leray enstrophy balance with the Betchov kinematic identity.

## 1. Betchov identity on the Leray trajectory

Let

\[
A=\nabla V=S+\mathcal A,
\qquad
W=\nabla\times V.
\]

For a sufficiently decaying incompressible field, integration by parts gives the Betchov relation

\[
\boxed{
4\int_{\mathbb R^3}\operatorname{tr}(S^3)dY
=-3\int_{\mathbb R^3}W^TSW\,dY.
}
\]

The present Leray class has

\[
W\in L^2\cap L^\infty,
\]

hence `W in L3`; the Riesz relation gives `S in L3`, so the cubic terms are integrable and the identity is legitimate by cutoff approximation.

For a trace-free `3 x 3` matrix,

\[
\operatorname{tr}(S^3)=3\det S.
\]

Therefore, with

\[
\mathcal P(s)=\int W^TSW,
\]

\[
\boxed{
\mathcal P(s)=-4\int\det S(Y,s)dY.
}
\]

## 2. Insert the recurrent enstrophy balance

The exact Leray enstrophy identity is

\[
\frac12Z'+\frac14Z+\nu Q=\mathcal P,
\]

where

\[
Z=\|W\|_2^2,
\qquad
Q=\|\nabla W\|_2^2.
\]

Long-time averaging on a bounded recurrent orbit gives

\[
\boxed{
-4\overline{\int\det S}
=\frac14\overline Z+\nu\overline Q>0.
}
\]

Thus the recurrent survivor necessarily carries negative strain determinant on average.

For ordered trace-free strain eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3,
\]

negative determinant is exactly the positive-middle spectral sector

\[
\lambda_1<0<\lambda_2\le\lambda_3.
\]

Hence positive-middle strain is not an optional recurrent subcase: it is globally required on average.

## 3. Positive determinant-part floor

Define

\[
D_-(s)
:=
\int(-\det S)_+dY.
\]

Since

\[
D_-(s)\ge-\int\det S,
\]

time averaging gives

\[
\boxed{
\overline{D_-}
\ge
\frac1{16}\overline Z
+\frac\nu4\overline Q.
}
\]

Thus the positive-middle sector carries a strictly positive cubic strain budget on every nonzero recurrent statistical state.

## 4. Convert determinant action to a middle-eigenvalue action

On the positive-middle set,

\[
(-\det S)_+
=(-\lambda_1)\lambda_2\lambda_3.
\]

The algebraic estimate

\[
(-\lambda_1)\lambda_3
\le
\frac{\lambda_1^2+\lambda_3^2}{2}
\le\frac{|S|^2}{2}
\]

gives

\[
\boxed{
(-\det S)_+
\le
\frac12\lambda_2^+|S|^2.
}
\]

For divergence-free whole-space fields,

\[
\int|S|^2=\frac12Z.
\]

Let

\[
\Lambda_2(s)=\|\lambda_2^+(s)\|_\infty.
\]

Then

\[
D_-(s)
\le
\frac14\Lambda_2(s)Z(s).
\]

Consequently

\[
\boxed{
\overline{\Lambda_2 Z}
\ge
\frac14\overline Z+\nu\overline Q.
}
\]

Equivalently,

\[
\boxed{
\frac{\overline{\Lambda_2 Z}}{\overline Z}
\ge
\frac14
+\nu\frac{\overline Q}{\overline Z}.
}
\]

This is an exact recurrent positive-middle spectral floor.

## 5. Relation to the maximum-vorticity branch split

The maximum-vorticity magnitude equation gives a different alternative:

\[
\text{positive-middle at the maximum}
\quad\lor\quad
\text{strongest-eigenvector alignment}.
\]

The Betchov identity shows that even if the maximum-vorticity point uses the second route for long intervals, the flow as a whole must still generate a positive amount of positive-middle strain elsewhere.

Thus a recurrent survivor cannot be purely an extensional-alignment geometry globally.

The remaining issue is **co-location**:

\[
\boxed{
\text{does the Betchov-forced positive-middle action enter the same bounded active core that carries the recurrent vorticity?}
}
\]

If yes, it feeds directly into the existing positive-middle transverse-ribbon/projective-action closure. If not, the flow must maintain a spatially separated positive-middle payer, reviving the existing separation/remote-source branch.

## 6. Periodic orbit localization

For a smooth periodic Leray orbit, the maps

\[
s\mapsto S(s)
\]

form a compact family in `L3` over one period, provided the established `W in L2 cap Linfty` bounds are retained. Therefore the cubic strain tails are uniformly tight:

\[
\sup_{s\in[0,P]}
\int_{|Y|>R}|S(Y,s)|^3dY
\to0
\qquad(R\to\infty).
\]

Since

\[
|\det S|\le C|S|^3,
\]

the determinant payer cannot escape entirely to spatial infinity on a periodic survivor.

Hence for `R` sufficiently large a fixed bounded similarity ball carries a positive fraction of the time-averaged Betchov-required positive-middle determinant action.

This does not yet prove pointwise co-location with the vorticity maximum, but it rules out a purely infinite-radius determinant payer in the periodic case.

## 7. Current endgame split

The recurrent geometry is refined to

\[
\boxed{
\begin{aligned}
\text{recurrent survivor}
\Longrightarrow\;&
\text{positive-density maximum effective stretching}\\
&+\text{positive mean palinstrophy}\\
&+\text{positive mean positive-middle determinant action}.
\end{aligned}
}
\]

A survivor must therefore keep three ledgers replenished at once.

The next target is a localized Betchov/co-location lemma showing that, on a no-`T/H` compact core, a fixed fraction of the determinant action must overlap the vorticity-carrying region or else pay a boundary/separation derivative cost.

Status: **THE RECURRENT STRETCHING BUDGET IS EXACTLY A NEGATIVE STRAIN-DETERMINANT BUDGET. NONZERO RECURRENCE FORCES A STRICTLY POSITIVE TIME-AVERAGED POSITIVE-MIDDLE STRAIN ACTION, WITH `overline(Lambda2 Z) >= (1/4) overline(Z)+nu overline(Q)`. THE LAST ISSUE IS LOCALIZATION/CO-LOCATION WITH THE RECURRENT VORTICITY CORE.**