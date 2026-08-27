# DSD M5-108 — Critical Trace-Free Residual Floor

Date: 2026-08-27

Status: **W1-CONDITIONAL CRITICAL RIGIDITY / THE p=3 TRACE-FREE STRAIN INEQUALITY FORCES EVERY POSITIVE CRITICAL PRESSURE OVERPAY TO CARRY A QUANTITATIVE COMPONENTWISE PRESSURE-STRAIN RESIDUAL / INVARIANT MEAN RESIDUAL IS AT LEAST nu R3/3 / THE CUBIC DEFECT CANNOT BE STORED IN THE EXACT MINIMAL-PAYER ENDPOINT / NO FINITE GLOBAL BUDGET FOR THIS RESIDUAL IS CLAIMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Critical M5 variables

Use the critical weight

\[
w(a)=1.
\]

Then

\[
W_<(a)=a.
\]

Define

\[
A_3:=\int a|\nabla U|^2dY,
\]

\[
T_3:=\int a b^2dY,
\]

\[
G_3:=\int \frac{|U\times\nabla a|^2}{a}dY,
\]

and

\[
B_3:=A_3+G_3.
\]

Since

\[
C_3=T_3+G_3,
\]

the critical viscous term is

\[
\boxed{
D_3=A_3+C_3=B_3+T_3.
}
\]

Let the componentwise centered pressure be

\[
f:=P-m_k(a,s)
\]

on each regular superlevel branch.

The critical pressure work is

\[
J_3:=\int a f b\,dY.
\]

Define the instantaneous critical overpay

\[
\boxed{
X_3:=J_3-\nu D_3.
}
\]

M5-107 gives

\[
\boxed{
\langle X_3\rangle_\mu
=\frac{\mathscr R_3}{6}>0.
}
\]

---

## 2. Exact critical residual

The M5-83 completed-square identity extends to `w=1` through the p-down-to-3 limiting construction and the branch-mean audit M5-96.

Define

\[
\boxed{
\mathcal E_3
:=
\int a\,|f-2\nu b|^2dY.
}
\]

Then

\[
\boxed{
\mathcal E_3
=
S_{comp,3}
-4\nu^2B_3
-4\nu X_3,
}
\]

where

\[
S_{comp,3}:=\int a|f|^2dY.
\]

Cauchy gives

\[
J_3^2\le S_{comp,3}T_3.
\]

If `T_3=0`, then `J_3=0` and therefore

\[
X_3=-\nu D_3\le0.
\]

Hence only `T_3>0` needs analysis for a positive overpay.

---

## 3. Trace-free strain at the critical weight

M5-88 proved pointwise

\[
b=e^TSe,
\qquad
|\nabla U|^2\ge\frac32b^2.
\]

Multiplying by `a` gives

\[
\boxed{
A_3\ge\frac32T_3.
}
\]

Therefore

\[
\boxed{
B_3\ge\frac32T_3.
}
\]

This is exactly the critical `alpha=1` endpoint of the Mellin-weight inequality.

---

## 4. Lower bound the residual by the overpay

For `T_3>0`, Cauchy and the exact residual identity give

\[
\mathcal E_3
\ge
\frac{J_3^2}{T_3}
-4\nu^2B_3
-4\nu X_3.
\]

Since

\[
J_3=X_3+\nu(B_3+T_3),
\]

we obtain exactly

\[
\boxed{
\mathcal E_3
\ge
\frac{\bigl[X_3+\nu(B_3-T_3)\bigr]^2}{T_3}.
}
\]

Set

\[
x:=\frac{X_3}{\nu T_3},
\qquad
y:=\frac{B_3}{T_3}.
\]

For `X_3>=0`, one has `x>=0` and `y>=3/2`, so

\[
\frac{\mathcal E_3}{\nu^2T_3}
\ge
(x+y-1)^2.
\]

By

\[
(x+d)^2\ge4xd
\qquad(x,d\ge0)
\]

with `d=y-1>=1/2`,

\[
\mathcal E_3
\ge
4\nu X_3(y-1)
\ge
\boxed{2\nu X_3}.
\]

If `X_3<0`, then `E_3>=0>=2nu X_3`.

Hence for every state,

\[
\boxed{
\mathcal E_3\ge2\nu X_3.
}
\]

The right side is informative precisely on positive-overpay states.

---

## 5. Invariant mean floor

Average over the invariant W1 measure.

M5-107 gives

\[
\langle X_3\rangle_\mu
=\frac{\mathscr R_3}{6}.
\]

Therefore

\[
\boxed{
\langle\mathcal E_3\rangle_\mu
\ge
2\nu\langle X_3\rangle_\mu
=
\frac{\nu}{3}\mathscr R_3.
}
\]

Thus every surviving nonzero cubic residue forces a nonzero mean squared distance from the componentwise minimal-payer relation

\[
P-m_k=2\nu b.
\]

---

## 6. Exact endpoint is a downstroke at critical weight

If at one state

\[
\mathcal E_3=0,
\]

then

\[
f=2\nu b
\]

on the active weighted region.

Hence

\[
J_3=2\nu T_3
\]

and

\[
X_3
=2\nu T_3-\nu(B_3+T_3)
=\nu(T_3-B_3).
\]

Since

\[
B_3\ge\frac32T_3,
\]

we get

\[
\boxed{
X_3\le-\frac\nu2T_3\le0.
}
\]

Therefore the exact critical endpoint cannot itself carry the positive invariant anomaly.

Any zero-residual state is a nonpositive critical-overpay state.

---

## 7. DSD four-chain audit

### Formation

The residual is formed from the actual componentwise pressure mean and the actual longitudinal strain.

### Axis

`b` is the velocity-direction longitudinal strain; `G_3` remains the transverse amplitude channel; the two are not merged.

### Static aggregation

`R_3`, `X_3`, and `E_3` are linked by inequalities and identities; they are not added as independent resources.

### Dynamics

Only the already-formed invariant mean `X_3` is averaged. No recurrence conclusion is inferred from the residual floor.

### Cross-audit

The result is forward-only:

\[
\mathscr R_3>0
\to
\langle X_3\rangle>0
\to
\langle\mathcal E_3\rangle>0.
\]

No reverse arrow is used.

---

## 8. What this removes

The narrow-band R1/R2 exact-endpoint geometry is no longer the only place where the critical survivor can hide.

At the true critical weight, the positive anomaly is forced into the complement of the exact endpoint:

\[
\boxed{
\text{critical cubic defect}
\Rightarrow
\text{persistent pressure--strain mismatch}.
}
\]

Thus the principal remaining question is not whether `P-m=2nu b` can hold recurrently.

It is whether a weak-critical W1 orbit can support the nonzero critical residual required by

\[
\langle\mathcal E_3\rangle
\ge\nu\mathscr R_3/3
\]

without violating a standard Navier--Stokes critical regularity bound.

---

## 9. Limitation / RED firewall

No finite physical-time budget for

\[
\int \mathcal E_3\,dt
\]

has been proved.

The critical scaling audit M5-106 applies: finite terminal time does not imply finite critical residual action.

Therefore repeated positive residual cannot be summed into a contradiction unless an independent finite critical budget is proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
