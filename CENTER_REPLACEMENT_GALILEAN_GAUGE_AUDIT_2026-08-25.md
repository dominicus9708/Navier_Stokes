# Center-Replacement Galilean Gauge Audit

Date: 2026-08-25

Status: **BARE INTER-TIME CENTER INCREMENT IS NOT GALILEAN INVARIANT / SAME-TIME RELATIVE CENTER SEPARATION IS INVARIANT / SOURCE-SPECIFIC FIXED-GAUGE CENTER BOUND REQUIRES SCOPE RETENTION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

A previous frontier note records a no-\(T\) center-replacement estimate of the schematic form

\[
|X_{j+1}-X_j|\lesssim r_j.
\]

Before importing such an estimate into the material genealogy argument, its coordinate dependence must be audited.

The issue is purely kinematic and independent of the detailed Navier–Stokes estimate that originally produced the bound.

---

## 2. Constant Galilean transformation

For a constant velocity \(c\in\mathbb R^3\), write

\[
x'=x-ct,
\qquad
u'(x',t)=u(x'+ct,t)-c.
\]

Then

\[
\omega'(x',t)=\omega(x'+ct,t).
\]

If \(X_j\) is a vorticity-maximum center at time \(t_j\), the corresponding center in the transformed inertial frame is

\[
\boxed{X_j'=X_j-ct_j.}
\]

Therefore

\[
\boxed{
X_{j+1}'-X_j'
=(X_{j+1}-X_j)-c(t_{j+1}-t_j).
}
\]

Consequently a bare estimate

\[
|X_{j+1}-X_j|\le Cr_j
\]

with universal \(C\) cannot be an invariant statement across all constant Galilean frames unless the gauge/reference frame is fixed as part of the hypotheses.

Indeed, for \(t_{j+1}\ne t_j\), choosing \(|c|\) arbitrarily large changes the left side by an arbitrarily large amount while \(r_j\), which depends on vorticity amplitude, is Galilean invariant.

**Status: PROVED.**

---

## 3. Correct interpretation of a fixed-gauge center bound

If the original center-replacement lemma was proved after fixing one inertial frame, then it may remain a valid estimate **inside that fixed gauge**.

What is invalid is the stronger import

\[
\text{fixed-gauge center estimate}
\Longrightarrow
\text{Galilean-invariant material genealogy constraint}.
\]

Hence until the exact source lemma and its reference-frame conventions are revalidated, the repository must treat the schematic estimate

\[
|X_{j+1}-X_j|\lesssim r_j
\]

as

\[
\boxed{\text{DO NOT USE AS AN INVARIANT CONTRADICTION MECHANISM}.}
\]

This audit does **not** declare the source estimate false in its original gauge.

---

## 4. Same-time relative separation is invariant

Let \(z_n(t)\) be the material image of an ancestor center. Under the same constant Galilean transformation,

\[
z_n'(t)=z_n(t)-ct.
\]

At the descendant time \(t_j\),

\[
\boxed{
X_j'-z_n'(t_j)
=X_j-z_n(t_j).
}
\]

Therefore the recently derived remote center-separation statement

\[
|X_j-z_n(t_j)|\ge \theta_Lr_n
\]

is Galilean invariant.

This is the correct type of positional genealogy statement: both positions are compared at the **same physical time**.

**Status: PROVED.**

---

## 5. Galilean-covariant reference paths

A useful non-material reference path may be defined by a local mean velocity, for example

\[
\dot Y_R(t)
=\fint_{B_{4R}(Y_R(t))}u(x,t)\,dx.
\]

Under a constant Galilean transformation, choosing

\[
Y_R'(t)=Y_R(t)-ct
\]

gives

\[
\dot Y_R'(t)=\dot Y_R(t)-c.
\]

Hence relative locations

\[
X_j-Y_R(t_j)
\]

and relative inter-stage increments

\[
\boxed{
[X_{j+1}-Y_R(t_{j+1})]
-[X_j-Y_R(t_j)]
}
\]

are invariant under constant Galilean boosts.

This is only a covariant choice of reference curve. A time-dependent translation is **not** being claimed as an exact symmetry of the Navier–Stokes equations; transforming the PDE into an accelerating frame would introduce inertial terms.

**Status: PROVED / SCOPE CLARIFIED.**

---

## 6. Consequence for summing center replacements

The formal telescope

\[
|X_j-X_{j-k}|
\le
\sum_{m=j-k}^{j-1}|X_{m+1}-X_m|
\lesssim
\sum_{m=j-k}^{j-1}r_m
\lesssim r_{j-k}
\]

may be algebraically valid in a fixed gauge if every one-step estimate is valid there.

However the resulting inter-time absolute displacement

\[
|X_j-X_{j-k}|
\]

is itself Galilean dependent:

\[
(X_j'-X_{j-k}')
=(X_j-X_{j-k})-c(t_j-t_{j-k}).
\]

Therefore this telescope cannot by itself identify the current maximum packet with the transported ancestor packet.

The material comparison must instead use

\[
X_j-z_{j-k}(t_j),
\]

or an equivalent same-time relative position.

**Status: PROVED.**

---

## 7. Updated positional genealogy rule

Admissible invariant positional statements:

\[
\boxed{
X_j-z_n(t_j),
\qquad
X_j-Y(t_j),
\qquad
[X_{j+1}-Y(t_{j+1})]-[X_j-Y(t_j)].
}
\]

Bare cross-time center differences:

\[
\boxed{
X_{j+1}-X_j,
\qquad
X_j-X_n
}
\]

must retain an explicit fixed-gauge qualification and cannot serve as invariant genealogy observables.

---

## 8. Audit table

| Statement | Status |
|---|---|
| Constant Galilean transform shifts \(X_j\) by \(-ct_j\) | PROVED |
| Bare inter-time center increment is Galilean invariant | FALSE |
| A universal gauge-free bound \(|X_{j+1}-X_j|\lesssim r_j\) can hold without a reference path | FALSE |
| Original source bound may remain valid in its fixed frame | POSSIBLE / SOURCE SCOPE MUST BE RETAINED |
| Same-time \(X_j-z_n(t_j)\) is Galilean invariant | PROVED |
| Local-mean reference path yields invariant relative increments | PROVED |
| Time-dependent moving frame is an exact NS symmetry | FALSE |
| Center telescope alone proves material packet identity | NOT DERIVED |
| Global regularity | UNPROVED |

---

## 9. Corrected frontier contribution

The center-switch branch cannot be closed through an absolute center-speed or absolute inter-time displacement argument.

The admissible route is

\[
\boxed{
\text{center switch}
\to
\text{same-time separation from transported ancestor/reference packet}
\to
\text{contact / multiplicity / dissipation ledger}.
}
\]

Thus the next calculation must charge packet persistence or switching through Galilean-invariant amplitudes, overlaps, relative transport, and time-integrated dissipation rather than bare center coordinates.