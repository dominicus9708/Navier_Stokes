# DSD M19-142 — The Pineau--Vicol velocity Type-I and fixed physical pressure-annulus hypotheses follow on the uniformly smooth passive critical-tail lane, but not from primitive W1 alone

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL-THEOREM APPLICABILITY AUDIT / PRIMITIVE W1 GIVES A GLOBAL-IN-SPACE SUPNORM TYPE-I BOUND BUT NOT BY ITSELF THE REQUIRED 1/(SQRT(TAU)+R) SPATIAL PROFILE / ON THE CERTIFIED SMOOTH PASSIVE CRITICAL-TAIL LANE, UNIFORM U=O(1/R) AND P=O(1/R^2) BOUNDS SCALE BACK EXACTLY TO THE PINEAU--VICOL VELOCITY TYPE-I AND FIXED PHYSICAL PRESSURE-ANNULUS CONDITIONS / THE BRIDGE IS CLOSED ON THIS SUBBRANCH SUBJECT TO THE POINTWISE TAIL-NORM AND PRESSURE-NORMALIZATION GATES / GLOBAL ROOT ENTRY REMAINS OPEN.**

---

## 1. The external application target

The Pineau--Vicol one-slice regularity criterion is used in M19-096--097 only on a physical cylinder around a candidate singular point `x_*`, after shifting the putative blow-up time to `T_*`.

The relevant structural hypotheses are of the form

\[
\boxed{
|u(x,t)|
\le
\frac{C_u}{\sqrt{T_*-t}+|x-x_*|}
}
\]

and a bounded pressure on a fixed physical annulus around `x_*`, after the standard pressure normalization.

The present module audits whether the repository actually supplies these conditions.

---

## 2. Primitive W1 is not enough by itself

M18-042 records the primitive Type-I condition as the vorticity-amplitude bound

\[
(T_*-t)\|\omega(t)\|_\infty\le K_I.
\]

Together with bounded normalized enstrophy `Z_D<=Z_+`, the bounded-Z Type-I calculation gives

\[
\boxed{
\|u(t)\|_\infty
\lesssim
(T_*-t)^{-1/2}.
}
\]

This is the standard global supnorm Type-I velocity estimate.

However

\[
\|u(t)\|_\infty\lesssim (T_*-t)^{-1/2}
\]

does **not** imply the stronger spatial profile

\[
|u(x,t)|\lesssim
(\sqrt{T_*-t}+|x-x_*|)^{-1}.
\]

Therefore

\[
\boxed{
\text{primitive W1 Type-I}
\not\Rightarrow
\text{Pineau--Vicol spatial Type-I by itself}.
}
\]

This is an important hypothesis-matching firewall.

---

## 3. Similarity variables on the passive critical-tail lane

Set

\[
\tau:=T_*-t>0,
\qquad
s:=-\log\tau,
\qquad
y:=\frac{x-x_*}{\sqrt\tau}.
\]

Use the backward similarity normalization

\[
\boxed{
u(x,t)=\tau^{-1/2}U(y,s)}
\]

and the pressure normalization

\[
\boxed{
p(x,t)=\tau^{-1}P(y,s)}
\]

up to the harmless time-dependent pressure gauge, fixed by the whole-space/Riesz or retained spectator normalization.

---

## 4. Uniform smooth critical-tail bounds

The active passive-spectator M19 corridor uses the smooth critical-tail estimates

\[
\boxed{
|U(y,s)|
\le
\frac{C_U}{1+|y|},
}
\]

and

\[
\boxed{
|P(y,s)|
\le
\frac{C_P}{1+|y|^2},
}
\]

uniformly in the relevant late/recurrent similarity-time corridor.

These are stronger pointwise versions of the scattering asymptotics

\[
U
=
r^{-1}A(\log r-s/2,\omega)+O(r^{-3}),
\]

\[
P
=
r^{-2}\Pi(\log r-s/2,\omega)+\text{faster terms},
\]

combined with the smooth compact-core bounds.

**Application gate:** if the retained spectator norm only supplies an annular `H1` estimate and not a pointwise Sobolev/analytic bound, this step must not be used until the stronger pointwise tail bound is certified. The current late M19 hard corridor explicitly retains the smooth pointwise critical-tail bounds used in the quasi-compactness calculation.

---

## 5. Scale back the velocity bound

Using

\[
|y|=\frac{|x-x_*|}{\sqrt\tau},
\]

we obtain

\[
\begin{aligned}
|u(x,t)|
&=
\tau^{-1/2}|U(y,s)|\\
&\le
C_U\tau^{-1/2}
\frac1{1+|x-x_*|/\sqrt\tau}\\
&=
\boxed{
\frac{C_U}{\sqrt\tau+|x-x_*|}.
}
\end{aligned}
\]

Thus the precise spatial Type-I form required by the external criterion is recovered:

\[
\boxed{
|u(x,t)|
\lesssim
\frac1{\sqrt{T_*-t}+|x-x_*|}.
}
\]

---

## 6. Scale back the pressure bound

Similarly,

\[
\begin{aligned}
|p(x,t)|
&=
\tau^{-1}|P(y,s)|\\
&\le
C_P\tau^{-1}
\frac1{1+|x-x_*|^2/\tau}\\
&=
\boxed{
\frac{C_P}{\tau+|x-x_*|^2}.
}
\end{aligned}
\]

Fix physical radii

\[
0<r_-<r_+<\infty.
\]

On the fixed physical annulus

\[
r_-<|x-x_*|<r_+,
\]

we get

\[
\boxed{
|p(x,t)|
\le
\frac{C_P}{r_-^2}
}
\]

uniformly as `t->T_*`.

After the local spatial normalization used by the external theorem, one may take for example the standard annulus

\[
1/2<|x|<3/4.
\]

Thus the required physical pressure-annulus `L-infinity` bound is certified on this passive critical-tail subbranch.

---

## 7. Compact core and the full local ball

For

\[
|y|\le R_{core},
\]

the retained recurrent/analytic compactness gives a uniform bound

\[
|U(y,s)|\le C_{core}.
\]

Hence in the physical core

\[
|x-x_*|\lesssim\sqrt\tau,
\]

we have

\[
|u(x,t)|\lesssim\tau^{-1/2},
\]

which is again bounded by

\[
C(\sqrt\tau+|x-x_*|)^{-1}.
\]

Combining compact core and critical tail gives the required Type-I profile on the whole local physical ball.

---

## 8. What is now certified

On the **uniformly smooth passive critical-tail lane**, the following implication is exact:

\[
\boxed{
\begin{aligned}
&|U(y,s)|\lesssim(1+|y|)^{-1},\\
&|P(y,s)|\lesssim(1+|y|^2)^{-1}
\end{aligned}
\Longrightarrow
\begin{aligned}
&|u(x,t)|\lesssim(\sqrt\tau+|x-x_*|)^{-1},\\
&|p(x,t)|\lesssim(\tau+|x-x_*|^2)^{-1}.
\end{aligned}
}
\]

Therefore the velocity-Type-I and fixed pressure-annulus hypotheses imported in M19-096/097 are matched on this subbranch.

---

## 9. What remains conditional

This does **not** show that every W1 or every hypothetical singularity satisfies the external theorem's hypotheses.
The following remain explicit gates:

1. entry into the smooth passive critical-tail corridor;
2. uniform pointwise tail control, rather than only annular `H1` control;
3. the chosen whole-space/local pressure normalization;
4. suitable smooth/local-energy solution regularity on the physical punctured cylinder;
5. the remaining one-slice derivative-smallness condition when the external regularity theorem is invoked.

Thus the correct scope is

\[
\boxed{
\text{Pineau--Vicol Type-I/pressure applicability}
\text{ is certified on the M19 passive critical-tail lane,}
}
\]

not on primitive W1 globally.

---

## 10. Effect on the M19 frontier

The former broad `external theorem applicability` item is reduced.
The Type-I velocity and pressure-annulus pieces are no longer independent unknowns **inside the smooth passive critical-tail hard core**.

The remaining external/application work is principally:

- certify that the actual branch being tested has reached this pointwise spectator lane;
- certify unique-continuation/scattering differentiability where used;
- preserve the original ROOT-CERT warning that arbitrary-singularity entry is still open.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
