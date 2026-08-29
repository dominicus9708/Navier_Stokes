# DSD M5-194X — Leray Vorticity Enstrophy and Periodic Stretching-Payment Audit

Date: 2026-08-29

Parent: `DSD_M5_194W_LOCAL_LERAY_ENERGY_PAIRING_AND_ORTHOGONAL_SHAPE_FIREWALL_2026-08-29.md`

Status: **POSITIVE VORTICITY LEDGER / THE LOCAL LERAY VORTICITY EQUATION SEPARATES ADVECTIVE BOUNDARY TRANSPORT FROM INTERIOR VORTEX STRETCHING / ON A PERIODIC SPATIAL-TYPE-I PROFILE WITH SUFFICIENT DERIVATIVE DECAY TO REMOVE THE LARGE-SPHERE TERMS, PERIOD AVERAGING FORCES STRICTLY POSITIVE MEAN STRETCHING EQUAL TO PALINSTROPHY PLUS ONE QUARTER OF ENSTROPHY / THUS A NONZERO PERIODIC SURVIVOR MUST PAY A RECURRENT BETCHOV/STRAIN-STRETCHING COST EVEN IF ITS VELOCITY ENERGY AND MATERIAL FLUX ARE CRITICALLY BALANCED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Curl of the Leray equation

The velocity equation is

\[
V_s-\Delta V
+\frac12V
+\frac12(Y\cdot\nabla)V
+(V\cdot\nabla)V
+\nabla P=0,
\qquad
\nabla\cdot V=0.
\]

Let

\[
\Omega=\nabla\times V.
\]

Taking curl gives

\[
\boxed{
\Omega_s
-\Delta\Omega
+\Omega
+\frac12(Y\cdot\nabla)\Omega
+(V\cdot\nabla)\Omega
-(\Omega\cdot\nabla)V
=0.
}
\]

The coefficient of `Omega` is one because curl of the similarity scaling operator gains one homogeneity degree.

---

## 2. Local enstrophy pairing

Set

\[
Z_R(s):=\int_{B_R}|\Omega|^2dY,
\]

\[
Q_R(s):=\int_{B_R}|\nabla\Omega|^2dY.
\]

Dot the vorticity equation with `Omega` and integrate over `B_R`.

The diffusion term gives

\[
\int_{B_R}(-\Delta\Omega)\cdot\Omega
=
Q_R
-
\int_{\partial B_R}\partial_n\Omega\cdot\Omega\,dS.
\]

The linear vorticity term contributes `Z_R`.

For the similarity drift,

\[
\frac12\int(Y\cdot\nabla\Omega)\cdot\Omega
=
\frac14R\int_{\partial B_R}|\Omega|^2dS
-
\frac34Z_R.
\]

Thus the two linear terms combine to

\[
\boxed{
\frac14Z_R
+
\frac R4\int_{\partial B_R}|\Omega|^2dS.
}
\]

---

## 3. Advection is a boundary term

By incompressibility,

\[
\int_{B_R}
(V\cdot\nabla\Omega)\cdot\Omega
=
\frac12
\int_{\partial B_R}
|\Omega|^2(V\cdot n)dS.
\]

Therefore ordinary advective transport creates no interior enstrophy production.

It is a boundary/turnover channel.

---

## 4. Stretching survives in the bulk

The stretching term is

\[
-\int_{B_R}
(\Omega\cdot\nabla V)\cdot\Omega\,dY.
\]

Write

\[
\nabla V=S+A,
\]

with `S` symmetric and `A` antisymmetric.

Since

\[
\Omega^TA\Omega=0,
\]

we have

\[
\boxed{
(\Omega\cdot\nabla V)\cdot\Omega
=
\Omega^TS\Omega.
}
\]

Define the local stretching production

\[
\boxed{
\mathcal B_R(s)
:=
\int_{B_R}
\Omega^TS\Omega\,dY.
}
\]

This is the genuine interior nonlinear vorticity-production channel.

---

## 5. Exact local enstrophy identity

Combining all terms gives

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}Z_R
+Q_R
+\frac14Z_R
-\mathcal B_R\\
+
\int_{\partial B_R}
\left[
-\partial_n\Omega\cdot\Omega
+\frac R4|\Omega|^2
+\frac12|\Omega|^2(V\cdot n)
\right]dS
=0.
\end{aligned}
}
\]

Unlike the velocity-energy identity, there is no pressure term.

This is the principal advantage of the vorticity probe for the remaining shape dynamics.

---

## 6. Spatial-Type-I tail makes enstrophy integrable at infinity

Assume the periodic profile is on the spatial-Type-I derivative corridor, schematically

\[
|V(Y,s)|\lesssim r^{-1},
\]

\[
|\Omega(Y,s)|\lesssim r^{-2},
\]

and

\[
|\nabla\Omega(Y,s)|\lesssim r^{-3}
\]

uniformly in periodic phase for large `r`.

Then

\[
\int_{r>R}|\Omega|^2dY
\lesssim
\int_R^\infty r^2r^{-4}dr
\lesssim R^{-1}.
\]

Hence

\[
\boxed{
\Omega(s)\in L^2(\mathbb R^3)
}
\]

uniformly in the periodic phase.

Similarly,

\[
\nabla\Omega(s)\in L^2(\mathbb R^3).
\]

This is compatible with a velocity tail which is not globally `L^3`.

---

## 7. Large-sphere boundary terms vanish

Under the same asymptotic rates,

### Diffusive boundary term

\[
\int_{S_R}
|\partial_n\Omega||\Omega|dS
\lesssim
R^2R^{-3}R^{-2}
=R^{-3}\to0.
\]

### Similarity-vorticity boundary term

\[
R\int_{S_R}|\Omega|^2dS
\lesssim
R\,R^2R^{-4}
=R^{-1}\to0.
\]

### Advective boundary term

\[
\int_{S_R}|\Omega|^2|V|dS
\lesssim
R^2R^{-4}R^{-1}
=R^{-3}\to0.
\]

Therefore the local identity passes to the whole space.

---

## 8. Global similarity enstrophy identity

Define

\[
Z(s):=\|\Omega(s)\|_2^2,
\qquad
Q(s):=\|\nabla\Omega(s)\|_2^2,
\]

and

\[
\mathcal B(s)
:=
\int_{\mathbb R^3}
\Omega^TS\Omega\,dY.
\]

Then

\[
\boxed{
\frac12Z'(s)
+Q(s)
+\frac14Z(s)
=
\mathcal B(s).
}
\]

This identity is exact on the stated decay/regularity branch.

---

## 9. Period average forces positive stretching payment

If

\[
V(s+S)=V(s),
\]

then

\[
Z(s+S)=Z(s).
\]

Integrating the global enstrophy identity over one period gives

\[
\boxed{
\frac1S
\int_0^S\mathcal B(s)ds
=
\frac1S
\int_0^S Q(s)ds
+
\frac1{4S}
\int_0^S Z(s)ds.
}
\]

For a nonzero profile,

\[
\int_0^S Z(s)ds>0.
\]

Therefore

\[
\boxed{
\langle\mathcal B\rangle_S
>
0.
}
\]

Indeed the lower bound is explicit:

\[
\boxed{
\langle\mathcal B\rangle_S
\ge
\frac14\langle Z\rangle_S.
}
\]

This is the periodic stretching-payment identity.

---

## 10. Checkpoint nontriviality prevents vanishing average enstrophy

M5-194L gives a nonzero vorticity witness in one fixed similarity ball for checkpoint alpha-limits.

Under the strong local vorticity compactness and periodic regularity, continuity supplies a positive spacetime neighborhood on which `|Omega|` remains nonzero.

Consequently

\[
\boxed{
\langle Z\rangle_S>0
}
\]

with a profile-dependent positive value.

Obtaining a universal numerical lower bound from the checkpoint witness would require explicit local derivative constants and is not claimed here.

---

## 11. Relation to Betchov/projective channels

The production

\[
\mathcal B
=
\int\Omega^TS\Omega
\]

is exactly the vortex-stretching channel appearing in the ordinary enstrophy equation and in the repository's strain/vorticity geometry ledgers.

Thus a periodic survivor cannot be supported purely by

- coordinate similarity flux;
- passive `1/r` velocity tail;
- pressure redistribution;
- or boundary advection.

It must maintain positive mean interior stretching sufficient to pay both

\[
Q
\]

and

\[
\frac14Z.
\]

This directly reconnects the periodic alpha-limit to the existing Betchov/projective/derivative cost tree.

---

## 12. A simple positive-density consequence

Suppose `Z(s)` and `Q(s)` are bounded above on the compact periodic orbit, so `mathcal B(s)` is also bounded in the smooth class.

Since

\[
\langle\mathcal B\rangle_S>0,
\]

there exists a positive threshold `b_*>0` such that the set

\[
\boxed{
E_B
:=\{s\in[0,S]:\mathcal B(s)\ge b_*\}
}
\]

has positive measure.

Repeating periodically gives a positive-density recurrent stretching set on the whole similarity-time line.

Thus the periodic branch supplies exactly the recurrence frequency needed by finite-stage cost ledgers, provided those ledgers pass to the alpha-limit/core localization.

---

## 13. DSD verdict

### PROVED ON THE SPATIAL-TYPE-I DERIVATIVE CORRIDOR

- global enstrophy and palinstrophy are finite despite the possible non-`L3` velocity tail;
- all large-sphere vorticity boundary terms vanish;
- exact global Leray enstrophy identity;
- every nonzero periodic alpha-limit pays strictly positive mean interior vortex stretching;
- positive mean stretching yields a positive-density stretching recurrence set.

### NOT YET A CONTRADICTION

Positive stretching can balance palinstrophy and similarity damping on a periodic orbit. The identity is a payment law, not a sign contradiction.

### NEXT REDUCTION

The remaining question is whether the already established finite-stage Betchov/projective/H ledgers impose a strictly smaller long-time stretching budget than

\[
\langle Q+Z/4\rangle.
\]

If yes, the periodic alpha-limit closes.

If not, the residual compatible stretching regime becomes the precise finite scalar frontier.

---

## 14. Next audit target

Retrieve the existing recurrent Betchov mean-production ceiling and compare it directly with

\[
\boxed{
\langle\mathcal B\rangle
=
\langle Q\rangle+rac14\langle Z\rangle.
}
\]

The desired closure is a constant inequality.

If the repository only bounds a different Betchov scalar, derive the exact conversion between that scalar and `int Omega^T S Omega` before comparing constants.
