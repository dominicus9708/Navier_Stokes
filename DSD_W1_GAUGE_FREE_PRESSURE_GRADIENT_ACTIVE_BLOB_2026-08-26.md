# DSD W1 Gauge-Free Pressure-Gradient Active Blob

Date: 2026-08-26

Status: **GAUGE-INVARIANT REPLACEMENT FOR THE PRESSURE-SIGN ACTIVE-BLOB INTERPRETATION / POSITIVE P3 PRESSURE WORK FORCES A FIXED-VOLUME CORE REGION WHERE THE PRESSURE FORCE DOES POSITIVE AMPLITUDE-WEIGHTED WORK ALONG THE VELOCITY / GLOBAL REGULARITY UNPROVED.**

## 1. Gauge-free form of the endpoint pressure work

Let

\[
a=|U|,
\qquad
n=U/|U|
\]

on the nonzero set.

The pressure part of the `p=3` balance is

\[
F_P
=\int P\,U\cdot\nabla a\,dY.
\]

Because

\[
\nabla\cdot U=0
\]

and the endpoint cutoff/gauge audit justifies the global integration by parts after the boundary defect is retained separately,

\[
\boxed{
F_P
=-\int a\,U\cdot\nabla P\,dY
=-\int a^2\,n\cdot\nabla P\,dY.
}
\]

This representation is invariant under

\[
P\mapsto P+c(s).
\]

Therefore the physically meaningful local sign is the sign of the pressure gradient along the velocity direction, not the sign of `P` itself.

---

## 2. Finite-parent localization

The previously established pressure locality and far-tail estimates allow one to choose a fixed parent radius `R_P` so that the contribution to the endpoint work from outside the parent buffer is smaller than a prescribed fraction of the positive residue.

Hence recurrent W1 states contain events for which

\[
\boxed{
-\int_{B_{R_P}}a^2 n\cdot\nabla P\,dY
\ge c_{grad}>0.
}
\]

All constants below depend only on the compact W1 class and the fixed parent radius, not on the recurrence index.

---

## 3. Local smooth ceilings

Compact smoothness on `B_RP` supplies

\[
A_P
:=\sup_M\|U\|_{L^\infty(B_{R_P})}<\infty,
\]

and

\[
G_P
:=\sup_M\|\nabla P\|_{L^\infty(B_{R_P})}<\infty.
\]

Therefore

\[
0\le a^2|n\cdot\nabla P|
\le A_P^2G_P
=:K_{grad}.
\]

---

## 4. Positive work forces a fixed-volume downhill set

Let

\[
V_P=|B_{R_P}|
\]

and choose

\[
\eta_{grad}
:=\frac{c_{grad}}{2V_P}.
\]

Define

\[
A_{grad}
:=
\left\{
Y\in B_{R_P}:
-a^2 n\cdot\nabla P
\ge\eta_{grad}
\right\}.
\]

The same bounded-density argument used for the preceding active-blob extraction gives

\[
\boxed{
|A_{grad}|
\ge
\frac{c_{grad}}{2K_{grad}}
=:v_{grad}>0.
}
\]

Thus the pressure work cannot be concentrated into a vanishing normalized set.

---

## 5. Pointwise lower bounds on the active set

On `A_grad`,

\[
a^2(-n\cdot\nabla P)
\ge\eta_{grad}.
\]

Using

\[
-n\cdot\nabla P\le G_P
\]

gives

\[
\boxed{
a\ge
\left(\frac{\eta_{grad}}{G_P}\right)^{1/2}
=:a_{grad}>0.
}
\]

Using

\[
a\le A_P
\]

gives

\[
\boxed{
-n\cdot\nabla P
\ge
\frac{\eta_{grad}}{A_P^2}
=:g_{grad}>0.
}
\]

Hence on a fixed normalized volume,

\[
\boxed{
|U|\ge a_{grad},
\qquad
-n\cdot\nabla P\ge g_{grad}.
}
\]

The pressure force `-grad P` therefore has a strictly positive projection along the velocity direction.

---

## 6. Recurrent gauge-free core certificate

The finite-parent pressure-work superlevel is open in the compact local-smooth topology. Minimality therefore gives syndetic returns.

Thus every nontrivial W1 survivor must recurrently regenerate a fixed normalized core region satisfying

\[
\boxed{
|A_{grad}|\ge v_{grad}>0,
\quad
|U|\ge a_{grad}>0,
\quad
(-\nabla P)\cdot n\ge g_{grad}>0.
}
\]

This is the gauge-free replacement for statements based on the pointwise sign of `P`.

---

## 7. Relation to the older pressure--directional-strain blob

The identity

\[
F_P=\int P\,e
\]

remains globally gauge invariant because

\[
\int e=\int U\cdot\nabla|U|=0.
\]

However, after localization to a finite ball, a pointwise statement involving the sign of `P` depends on the selected pressure gauge.

Accordingly the earlier `P n^T S n>0` active-blob statement should be treated as a gauge-fixed bookkeeping representation, not as the preferred physical certificate.

The gauge-free terminal certificate is the pressure-gradient form above.

---

## 8. DSD interpretation

The recurrent large weak-critical core must contain a finite-volume region in which

\[
\boxed{
\text{pressure-force direction}
\text{ and velocity direction are positively aligned}.
}
\]

This pressure-downhill acceleration is one local realization of the global critical loop gain.

The remaining closure must combine this gauge-free pressure-force witness with the independent vorticity-stretching/middle-strain certificate, or show that their recurrent alternation forces an inadmissible critical action.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
