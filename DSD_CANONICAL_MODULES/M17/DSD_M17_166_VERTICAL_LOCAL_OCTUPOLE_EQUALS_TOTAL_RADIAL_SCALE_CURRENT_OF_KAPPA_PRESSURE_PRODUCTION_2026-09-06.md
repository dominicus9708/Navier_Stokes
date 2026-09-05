# DSD M17-166 — The vertical local octupole equals the total signed radial scale current of the `-kappa rho^2` axial pressure-production channel

Date: 2026-09-06  
Canonical ID: **M17-166**

Status: **RADIAL SCALE-CURRENT BRIDGE / M17-164 IDENTIFIES THE SMALL-CORE ASYMPTOTIC `P(R)/R^2 -> (3/7)O_V` FOR A SHARP BALL, WHERE `P(R)` IS THE CUMULATIVE AXIAL KAPPA-PRODUCTION INSIDE RADIUS `R`. IF THE FULL KAPPA-PRODUCTION MOMENT IS FINITE, THEN `P(R)` HAS A FINITE LIMIT AS `R->infinity`, SO THE SCALE-NORMALIZED CUMULATIVE `A(R)=R^-2 P(R)` TENDS TO ZERO. CONSEQUENTLY THE LOG-RADIAL DERIVATIVE `J_rad(s)=partial_s A(e^s)` HAS THE EXACT SUM RULE `int_{-infinity}^{infinity} J_rad(s) ds = -(3/7)O_V`. THUS THE PREVIOUSLY UNTYPED 'OUTER CANCELLATION' IS REPLACED BY A SIGNED RADIAL l=3 SCALE-TRANSPORT LEDGER: EVERY NONZERO LOCAL OCTUPOLE REQUIRES AN OPPOSITELY SIGNED TOTAL CHANGE OF THE NORMALIZED KAPPA-PRODUCTION ACROSS SPATIAL SCALES. THIS IS A STRUCTURAL SUM RULE, NOT YET A DISSIPATIVE COST. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Sharp cumulative kappa-production

Fix a marked vertical crossing core `Y` and set `z=Y-y`.
Define

\[
\boxed{
P_Y(R)
:=-\int_{|z|<R}
\kappa(y)\rho(y)^2
\mathcal K_{333}(z)dy.
}
\]

This is the cumulative part of

\[
\Pi_{V,\kappa}^{prod}(Y)
=-\langle\kappa\rho^2,\mathcal K_{333}(Y-\cdot)\rangle
\]

inside radius `R`.

Define the scale-normalized cumulative

\[
\boxed{
A_Y(R):=R^{-2}P_Y(R).
}
\]

The exponent `2` is forced by the cubic-source / degree-`-4` kernel scaling of M17-164.

---

## 2. Small-scale endpoint

M17-164 gives for the sharp ball

\[
P_Y(R)
=\frac37R^2O_V(Y)+O(R^3).
\]

Therefore

\[
\boxed{
\lim_{R\downarrow0}A_Y(R)
=\frac37O_V(Y).
}
\]

This endpoint is local and depends only on the vertical cubic payer octupole.

---

## 3. Large-scale endpoint

Assume the full kappa-production moment is finite at the marked core:

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=\lim_{R\to\infty}P_Y(R)
\in\mathbb R.
}
\]

Then automatically

\[
\boxed{
\lim_{R\to\infty}A_Y(R)=0
}
\]

because of the explicit `R^-2` normalization.

No sign of the full global moment is required.

---

## 4. Log-radial scale current

Set

\[
\boxed{s:=\log R}
\]

and define

\[
\boxed{
\mathscr J_{rad,Y}(s)
:=\partial_sA_Y(e^s).
}
\]

Then by the fundamental theorem of calculus,

\[
\int_{-\infty}^{\infty}\mathscr J_{rad,Y}(s)ds
=A_Y(\infty)-A_Y(0).
\]

Using Sections 2--3,

\[
\boxed{
\int_{-\infty}^{\infty}
\mathscr J_{rad,Y}(s)ds
=-\frac37O_V(Y).
}
\]

Equivalently,

\[
\boxed{
O_V(Y)
=-\frac73
\int_{-\infty}^{\infty}
\mathscr J_{rad,Y}(s)ds.
}
\]

This is the canonical radial scale-current identity.

---

## 5. Explicit shell formula

Differentiate

\[
A(R)=R^{-2}P(R).
\]

Then

\[
\boxed{
\partial_sA(R)
=R^{-2}\left(RP'(R)-2P(R)\right).
}
\]

For regular radii,

\[
P'(R)
=-\int_{|z|=R}
\kappa(Y-z)\rho(Y-z)^2
\mathcal K_{333}(z)dA_z.
\]

Hence

\[
\boxed{
\mathscr J_{rad}(\log R)
= -R^{-1}
\int_{|z|=R}
\kappa\rho^2\mathcal K_{333}\,dA
-2R^{-2}P(R).
}
\]

Thus the scale current combines

1. the instantaneous `l=3` shell contribution at radius `R`;
2. the dilation subtraction required by the natural `R^2` local scaling.

---

## 6. Total variation lower bound

The signed sum rule immediately gives

\[
\boxed{
\int_{-\infty}^{\infty}
|\mathscr J_{rad,Y}(s)|ds
\ge\frac37|O_V(Y)|.
}
\]

Therefore every nonzero local octupole requires a nonzero amount of radial `l=3` scale variation.

This is positive as a spatial total-variation descriptor, but it is not yet a Navier--Stokes dissipation cost.

---

## 7. Interpretation of the old outer-cancellation firewall

M17-096 described the possibility that the local octupole orientation is canceled by mesoscopic/global source architecture.

M17-166 refines that statement:

\[
\boxed{
\text{outer cancellation}
\quad\equiv\quad
\text{radial transport of the normalized axial kappa-production }A(R).
}
\]

The cancellation cannot happen without changing `A(R)` across log scale, and the total signed change is fixed exactly by `O_V`.

Thus the outer freedom is not arbitrary. It is organized by one scale-current function `J_rad(s)`.

---

## 8. M5 crossing bias in scale-current language

M17-095 gives

\[
\overline{
\int a\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)d\mu_0
}>0.
\]

Insert the sum rule:

\[
O_V
=-\frac73\int\mathscr J_{rad}(s)ds.
\]

Formally, and rigorously under the compact/dominated crossing assumptions used in M17-165, Fubini gives

\[
\boxed{
\int_{-\infty}^{\infty}
\overline{
\int
 a\frac{r_V}{|Q|_F^2}
\mathscr J_{rad,\lambda}(s)
\delta(\kappa_\lambda)d\mu_0
}
ds
<0.
}
\]

Thus M5 hysteresis forces a negative **integrated radial scale-current bias** in the relative-speed-weighted crossing population.

This is a full-scale reformulation of the local crossing bias.

---

## 9. Existence of an active scale

Because the integrated weighted scale current is strictly negative, it cannot vanish at every scale.
Therefore there exists at least one log-radius set of positive measure on which

\[
\boxed{
\overline{
\int
 a\frac{r_V}{|Q|_F^2}
\mathscr J_{rad,\lambda}(s)
\delta(\kappa_\lambda)d\mu_0
}<0
}
\]

in the averaged sense.

This does not select a universal deterministic radius independent of the label population, but it proves that the M5 crossing bias must be serviced by a genuine radial `l=3` redistribution somewhere in scale space.

---

## 10. Why this is not yet a contradiction

The same radial architecture may recur.
A nonzero spatial total variation in `s` is not automatically a positive temporal dissipation or turnover cost.

Moreover the full vertical recurrence law contains:

\[
\Pi_V^{prod}
=\Pi_{V,\kappa}^{prod}
+\Pi_{V,other}^{prod}
\]

and the signed relative-transport channel

\[
\Pi_V^{rel}.
\]

Thus repeated scale redistribution in the kappa channel may in principle be balanced by other signed channels.

---

## 11. DSD audit

### Audit A — treating `R` as physical time
Rejected. `R` is an auxiliary spatial localization scale.

### Audit B — interpreting total radial variation as dissipation
Rejected. It is a structural scale-variation descriptor only.

### Audit C — assuming full kappa production has zero sign or zero mean
Not needed. Only finiteness of the endpoint is used.

### Audit D — ignoring measure mismatch
The scale identity is pointwise in each marked core; M5 is introduced only afterward under the original label measure.

### Audit E — proof status
The mesoscopic/global cancellation is converted to an exact radial scale-current sum rule, not eliminated.

---

## 12. Updated Rank-1 vertical frontier

Every retained regular crossing with `O_V != 0` carries

\[
\boxed{
O_V
=-\frac73\int\mathscr J_{rad}(s)ds.
}
\]

The M5 hysteresis condition forces a nontrivial signed bias of this scale current after weighting by `a r_V |Q|^-2 delta(kappa)dmu_0`.

The next target is no longer an undefined outer covariance. It is to determine whether the required recurrent radial `l=3` scale current can be realized with arbitrarily small temporal production/transport action, or whether its persistence forces one of the already typed pressure/turnover gates.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
