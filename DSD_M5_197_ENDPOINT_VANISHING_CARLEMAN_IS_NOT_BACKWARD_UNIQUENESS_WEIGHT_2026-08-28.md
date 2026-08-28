# DSD M5-197 — Endpoint-Vanishing Carleman Is Not a Backward-Uniqueness Weight

Date: 2026-08-28

Status: **DYNAMIC-AXIS CORRECTION / THE SINGULAR-TIME LINEARIZED-NS PHASE USED BY CHOULLI–IMANUVILOV–PUEL–YAMAMOTO HAS `alpha<0` AND `exp(2s alpha)->0` AT BOTH TEMPORAL ENDPOINTS; ITS SINGULARITY IS DESIGNED TO ERASE TIME-BOUNDARY TERMS IN CONTROL/INVERSE PROBLEMS, NOT TO AMPLIFY A KNOWN ZERO FINAL TRACE AND PROPAGATE IT BACKWARD / M5-196'S COEFFICIENT-ORDER DOMINATION REMAINS TRUE BUT DOES NOT BY ITSELF ADVANCE BACKWARD UNIQUENESS / ANY ATTEMPT TO USE THE ENDPOINT-VANISHING WEIGHT AS A TERMINAL-ZERO PROPAGATOR IS RED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Sign of the actual singular phase

The singular linearized-NS Carleman uses

\[
\phi(x,t)=\frac{e^{\lambda\eta(x)}}{\ell(t)^8}>0,
\]

and

\[
\boxed{
\alpha(x,t)
=
\frac{e^{\lambda\eta(x)}-e^{2\lambda\|\eta\|_\infty}}
{\ell(t)^8}<0.
}
\]

Since

\[
\ell(t)\to0
\]

at either temporal endpoint,

\[
\boxed{
\alpha(x,t)\to-\infty,
\qquad
e^{2s\alpha(x,t)}\to0.
}
\]

---

## 2. What this singularity actually does

The vanishing exponential weight suppresses all endpoint contributions produced by time integration by parts.

This is extremely useful for:

- null controllability;
- inverse-source estimates around an interior time;
- eliminating unknown temporal boundary terms from a Carleman identity.

But it also means that information at the terminal face has **zero Carleman weight**.

Thus the estimate does not distinguish between

\[
Z(T_*)=0
\]

and an arbitrary finite terminal trace by making the known zero dominant.

---

## 3. Why coefficient-order domination is not enough

M5-196 correctly observed

\[
\phi\sim t^{-8}
\]

and therefore

\[
|A|^2\sim t^{-1}\ll s\phi,
\qquad
|\nabla A|^2\sim t^{-2}\ll s^2\phi^2.
\]

This proves that the **algebraic size** of W1 Type-I coefficients is subordinate to the singular Carleman coefficients.

However the same exponential factor satisfies

\[
e^{2s\alpha}\to0
\]

so the estimate can be perfectly compatible with a nonzero solution carrying arbitrary earlier-time data.

A coefficient can be absorbable while the estimate still has no backward-time uniqueness content.

Therefore

\[
\boxed{
\text{coefficient absorption}
\not\Rightarrow
\text{terminal backward propagation}.
}
\]

---

## 4. Generic parabolic sanity check

A homogeneous heat equation has many nonzero solutions on `(0,T)`.

An endpoint-vanishing Carleman estimate can hold for all of them because it is an a priori weighted inequality; it does not assert that zero/no endpoint contribution implies the solution is zero.

If one combined it with spatial cutoffs and concluded that any decaying homogeneous solution must vanish, that would contradict ordinary heat evolution.

This sanity check is an explicit RED firewall against overusing phase-gap arguments.

---

## 5. What a genuine backward-uniqueness weight must do

The backward-uniqueness mechanism used by Escauriaza–Seregin–Šverák or Lei–Yang–Yuan has a different orientation.

After reversing time so that the known final trace becomes an initial trace at `t=0`, the weight becomes singular in a way that **penalizes nonzero behavior approaching the known-zero face**, for example powers comparable to

\[
t^{-2a}
\]

in the Lei–Yang–Yuan estimate.

The zero initial trace is essential in justifying this singular weight.

Thus the next required estimate must simultaneously have:

1. **backward-uniqueness orientation** at the terminal face;
2. pressure/Stokes compatibility;
3. a large-parameter gradient coercivity capable of absorbing arbitrary Type-I strain.

None of M5-193, M5-195, or M5-196 individually has all three.

---

## 6. Updated three-way comparison

### Lei–Yang–Yuan polynomial/CZ weight

- backward orientation: GREEN;
- pressure compatibility: GREEN;
- large-parameter gradient gain: **NO**;
- arbitrary Type-I strain: YELLOW/obstructed by M5-194.

### Imanuvilov–Lorenzi–Yamamoto regular Stokes Carleman

- pressure compatibility: GREEN;
- large-parameter gradient gain: GREEN;
- backward terminal orientation: **NO** (interior regular phase).

### Choulli–Imanuvilov–Puel–Yamamoto endpoint-singular control weight

- pressure/curl-Stokes compatibility: GREEN;
- Type-I coefficient-order domination: GREEN;
- backward terminal orientation: **NO** because the exponential vanishes at the endpoint.

The missing object is therefore sharply identified.

---

## 7. DSD audit

### Formation — GREEN

The sign of `alpha` and endpoint behavior are read from the actual theorem weight.

### Axis — GREEN

Coefficient singularity strength and temporal propagation orientation are separate axes.

### Static aggregation — GREEN

A large coefficient `phi~t^-8` is not counted as a positive backward-information budget.

### Dynamics — RED for the attempted backward use

The control/inverse singular weight does not propagate terminal zero backward by itself.

### Cross-audit — GREEN

This correction prevents M5-196 from being fed downstream as if it had solved M5-194's dynamic gate.

---

## 8. Next gate

Construct or locate a **hybrid backward Stokes Carleman** with:

\[
\boxed{
\text{terminal-zero singularity}
+
 s\times\text{gradient coercivity}
+
\text{pressure/Leray compatibility}.
}
\]

A natural route is to modify the Lei–Yang–Yuan time-singular conjugation while adding a spatially pseudoconvex phase, rather than reversing the sign of the Choulli control weight without proof.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
