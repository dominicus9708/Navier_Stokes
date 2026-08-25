# DSD W1 Critical Lorentz Endpoint Saturation

Date: 2026-08-26

Status: **W1 SURVIVOR SHOWN TO SATURATE WEAK-TIME CRITICAL ENDPOINTS FOR STREAMLINE-AMPLITUDE FLOW AND D3 / STRONG CRITICAL NORMS DIVERGE BY MINIMAL RECURRENCE / THIS IDENTIFIES THE EXACT STRONG-VS-WEAK ENDPOINT GAP, NOT A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

## 1. Streamline-amplitude variable

Set in physical variables

\[
e_{phys}:=u\cdot\nabla|u|.
\]

In Leray variables,

\[
e:=U\cdot\nabla|U|.
\]

The scaling is

\[
\boxed{
e_{phys}(x,t)
=\tau^{-3/2}e(Y,s),
\qquad
\tau=T_*-t=e^{-s}.
}
\]

Hence

\[
\boxed{
\|e_{phys}(t)\|_{L_x^{3/2}}
=\tau^{-1/2}
\|e(s)\|_{L_Y^{3/2}}.
}
\]

Therefore

\[
\boxed{
\|e_{phys}\|_{L_t^2L_x^{3/2}}^2
=
\int^{\infty}
\|e(s)\|_{3/2}^2ds.
}
\]

The strong `L_t^2 L_x^(3/2)` norm is exactly the unweighted Leray clock.

---

## 2. Type-I/W1 upper bound gives weak-L2 time control

By Hölder and Sobolev,

\[
\|e(s)\|_{3/2}
\le
\|U(s)\|_6\|\nabla U(s)\|_2
\le
C\|\nabla U(s)\|_2^2.
\]

On the compact W1 corridor the rescaled enstrophy is uniformly bounded:

\[
\|\nabla U(s)\|_2^2\le Z_*.
\]

Thus

\[
\boxed{
\|e_{phys}(t)\|_{3/2}
\le
C Z_*\tau^{-1/2}.
}
\]

The scalar time profile `tau^(-1/2)` belongs to weak `L2` but not strong `L2` at the endpoint. Therefore

\[
\boxed{
e_{phys}
\in
L_t^{2,\infty}L_x^{3/2}
}
\]

on the W1 Type-I corridor, with a norm controlled by the normalized W1 ceiling.

---

## 3. Invariant Bernoulli endpoint forces a positive normalized amplitude-flow event

The critical Gaussian/Bernoulli ledger gives a strictly positive invariant mean source. After the previously established localization of the tail contribution, one obtains a positive lower bound of the form

\[
\boxed{
\int_M\|e(U)\|_{3/2}d\mu(U)
\ge c_e>0.
}
\]

Equivalently, there exists a nonempty open subset of the compact minimal set on which

\[
\|e(U)\|_{3/2}>c_0>0.
\]

Minimality implies syndetic recurrence to that open set.

By continuity on the compact smooth W1 class, each visit contains a normalized interval of fixed positive duration `delta_s` on which, after reducing the threshold if needed,

\[
\boxed{
\|e(s)\|_{3/2}\ge c_1>0.
}
\]

---

## 4. Each recurrent event pays fixed critical action

For each such Leray interval `J_k`, the physical critical action satisfies

\[
\begin{aligned}
\int_{t(J_k)}
\|e_{phys}(t)\|_{3/2}^2dt
&=
\int_{J_k}\|e(s)\|_{3/2}^2ds\\
&\ge
c_1^2\delta_s.
\end{aligned}
\]

Since the events recur with bounded gaps in `s`, infinitely many disjoint such intervals exist.

Hence

\[
\boxed{
\int^{T_*}
\|u\cdot\nabla|u|\|_{3/2}^2dt
=\infty.
}
\]

Thus the W1 survivor occupies precisely the weak-time endpoint:

\[
\boxed{
 u\cdot\nabla|u|
\in
L_t^{2,\infty}L_x^{3/2}
\setminus
L_t^2L_x^{3/2}.
}
\]

This statement is conditional on the W1 Type-I/compact bounds used above.

---

## 5. The same phenomenon for D3

The physical endpoint dissipation density satisfies

\[
D_{3,phys}(t)
=
\tau^{-1}D_3(U(s)).
\]

Compact W1 bounds give a normalized upper ceiling

\[
D_3(U(s))\le D_{3,*}^{up}.
\]

Therefore

\[
D_{3,phys}(t)
\lesssim
\tau^{-1},
\]

which is the weak-`L1` endpoint in time.

The invariant W1 measure has

\[
\langle D_3\rangle_\mu>0.
\]

Minimal recurrence therefore yields fixed positive `D3` action on infinitely many Leray intervals, and

\[
\boxed{
\int^{T_*}D_{3,phys}(t)dt
=\infty.
}
\]

Thus schematically

\[
\boxed{
D_{3,phys}
\in L_t^{1,\infty}\setminus L_t^1.
}
\]

---

## 6. Relation to known conditional regularity criteria

The variable

\[
u\cdot\nabla|u|^\lambda
\]

is precisely the energy-flow variable studied in velocity-direction/energy-flow regularity criteria.

For `lambda=1`,

\[
 u\cdot\nabla|u|
\]

has the scale-critical mixed norm `L_t^2 L_x^(3/2)`.

The W1 calculation shows that a hypothetical singular survivor cannot lie in that strong critical class; instead it is forced to saturate the corresponding weak-time endpoint.

Similarly, the D3 criterion is forced to the weak-`L1`/non-`L1` boundary.

Thus the remaining gap is not a generic lack of integrability. It is the exact strong-critical versus weak-critical endpoint.

---

## 7. DSD interpretation

The structural chain can be written

\[
\boxed{
\text{recurrent core deformation}
\to
\text{fixed normalized amplitude-flow action}
\to
\text{critical physical action per log-time event}
\to
\text{weak-Lorentz saturation}.
}
\]

Subcritical budgets allow the events to be geometrically summable.

Strong critical budgets would exclude them.

W1 therefore survives only on the boundary where the critical quantity is weak-Lorentz controlled but its strong norm diverges.

A final closure theorem may target:

- smallness/improvement of the weak endpoint;
- a logarithmic improvement converting weak critical control to strong critical control;
- or a parent/interface mechanism forcing the weak-endpoint coefficient to decay.

No such unconditional improvement is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
