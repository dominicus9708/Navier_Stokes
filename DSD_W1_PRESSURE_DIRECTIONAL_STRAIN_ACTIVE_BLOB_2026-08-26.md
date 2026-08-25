# DSD W1 Pressure--Directional-Strain Active Blob

Date: 2026-08-26

Status: **POSITIVE FINITE-PARENT P3 PRESSURE WORK CONVERTED INTO A FIXED-VOLUME LOCAL WITNESS WHERE AMPLITUDE, PRESSURE, AND VELOCITY-DIRECTION STRAIN ARE ALL NONDEGENERATE WITH MATCHED SIGN / GLOBAL REGULARITY UNPROVED.**

## 1. Finite-parent pressure-work event

From the finite-parent weak-L3 gate, after choosing a sufficiently large but fixed parent radius `RP`, the recurrent W1 class has pressure-amplitude events for which

\[
\boxed{
\int_{B_{R_P}}P\,e\,dY
\ge c_P>0,
}
\]

up to already absorbed tail/localization errors, where

\[
e=U\cdot\nabla|U|.
\]

The pressure gauge is fixed by the existing W1 gauge repair/local finite-parent convention.

---

## 2. Uniform local ceilings

Because the W1 minimal set is compact in the local smooth topology, on the fixed ball `B_RP` there are finite constants

\[
A_P,
\qquad
S_P,
\qquad
P_P
\]

such that

\[
\|U\|_\infty\le A_P,
\qquad
\|S\|_\infty\le S_P,
\qquad
\|P\|_\infty\le P_P.
\]

Consequently

\[
|e|
=
|U\cdot\nabla|U||
\le
A_PS_P
=:E_P,
\]

and

\[
|Pe|
\le
P_PE_P
=:K_P.
\]

---

## 3. Positive integral forces a positive-volume active set

Let

\[
V_P=|B_{R_P}|
\]

and define

\[
\eta_P
:=
\frac{c_P}{2V_P}.
\]

Let

\[
A_{act}
:=
\{Y\in B_{R_P}:P(Y)e(Y)\ge\eta_P\}.
\]

If `|A_act|` were too small, then

\[
\int(Pe)_+
\le
K_P|A_{act}|+\eta_PV_P.
\]

Since the signed integral is at least `c_P`, the positive part is also at least `c_P`. Hence

\[
K_P|A_{act}|+rac{c_P}{2}
\ge c_P.
\]

Therefore

\[
\boxed{
|A_{act}|
\ge
\frac{c_P}{2K_P}
=:v_{act}>0.
}
\]

Thus the critical work cannot be concentrated into a vanishing normalized set.

---

## 4. Directional-strain form of e

Write

\[
U=a n,
\qquad
a=|U|,
\qquad |n|=1.
\]

Then

\[
\boxed{
e
=a\,n^TSn.
}
\]

On `A_act`,

\[
|Pe|
\ge
\eta_P.
\]

Using the local ceilings gives three lower bounds.

First,

\[
|e|
\ge
\frac{\eta_P}{P_P}
=:e_*.
\]

Since

\[
|e|
\le
|U|S_P,
\]

we get

\[
\boxed{
|U|
\ge
\frac{e_*}{S_P}
=:a_1>0.
}
\]

Since

\[
|e|
=|U|\,|n^TSn|
\le
A_P|n^TSn|,
\]

we obtain

\[
\boxed{
|n^TSn|
\ge
\frac{e_*}{A_P}
=:alpha_1>0.
}
\]

Finally, because

\[
|e|
\le E_P,
\]

we also have

\[
\boxed{
|P|
\ge
\frac{\eta_P}{E_P}
=:p_1>0.
}
\]

---

## 5. Matched sign

On the active set,

\[
Pe
=
P|U|n^TSn>0.
\]

Since `|U|>0`,

\[
\boxed{
P\,n^TSn>0
\qquad\text{on }A_{act}.
}
\]

Thus pressure and extensional/compressional strain measured along the velocity direction have the same sign on a fixed-volume recurrent region.

---

## 6. Recurrent event statement

The finite-parent pressure-work superlevel is an open condition on the compact smooth W1 class after fixing the ball and gauge.

Minimality therefore yields bounded return times to such events.

Consequently a nontrivial W1 survivor must syndetically reproduce a core region with

\[
\boxed{
|A_{act}|\ge v_{act}>0,
}

on which simultaneously

\[
\boxed{
|U|\ge a_1,
\qquad
|n^TSn|\ge alpha_1,
\qquad
|P|\ge p_1,
\qquad
P\,n^TSn>0.
}
\]

---

## 7. Physical scaling

At physical scale

\[
r(t)=\sqrt{T_*-t},
\]

the active set has volume order

\[
r(t)^3v_{act},
\]

velocity amplitude order

\[
r(t)^{-1}a_1,
\]

strain order

\[
r(t)^{-2}alpha_1,
\]

and pressure order

\[
r(t)^{-2}p_1.
\]

The pressure-amplitude work over one self-similar time event is therefore scale critical, while the kinetic-energy cost of the blob remains order `r(t)`.

This is consistent with the scaling-budget audit.

---

## 8. Updated local survivor certificate

The unresolved large weak-critical W1 branch now requires a recurrent finite core containing

\[
\boxed{
\text{high amplitude}
+
\text{nonzero velocity-direction strain}
+
\text{nonzero pressure}
+
\text{matched pressure/strain sign}
}
\]

on a fixed normalized volume.

This local witness must coexist with the positive vorticity-stretching/middle-strain gates already derived.

Whether those two recurrent core certificates can be forced to overlap, or whether their mandatory alternation yields a new transition cost, remains open.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
