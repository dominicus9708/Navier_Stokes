# DSD M5-377 — Natural productive shell: source capacity, center-capacity split, and derivative occupancy

Date: 2026-08-31

Status: **A FIXED-FRACTION NATURAL-SCALE PRODUCTIVE BIOT--SAVART SHELL CANNOT BE A ONE-POINT OR ZERO-CAPACITY PARTNER / THE FIRST-HITTING CAP FORCES A POSITIVE-MEASURE MISALIGNED SOURCE SET IN THAT SHELL / AT A VORTICITY-MAXIMUM CENTER, EITHER THE CENTRAL HIGH-VORTICITY STATE HAS A FIXED NORMALIZED CONTINUITY RADIUS, IN WHICH CASE SOURCE/CENTER SEPARATION FORCES ORDER-ONE LOCAL NORMALIZED PALINSTROPHY, OR THE CONTINUITY RADIUS COLLAPSES AND THE NORMALIZED VORTICITY GRADIENT DIVERGES / THE NATURAL-PARTNER LEAF IS THEREFORE ABSORBED INTO THE DERIVATIVE-CAPACITY LEDGER, MODULO TEMPORAL/REMOTE LOSS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-376 reduced scale-tight productive angular action to a fixed-fraction shell at a physical radius comparable to the current viscous-vorticity scale.

The remaining label was

\[
P_{\rm angular,natural}.
\]

This note asks whether such a shell can remain an independent geometric terminal mechanism, or whether the fixed stretching contribution already forces a derivative/capacity event.

The main DSD audit point is that a pointwise maximum cannot be used as an `H^1` anchor: in three dimensions a single point has zero `H^1` capacity. We therefore split according to whether the maximum has a fixed normalized continuity core.

---

## 2. Maximum-point first-hitting action

Let

\[
W(t)=\|\omega(t)\|_\infty
\]

and let

\[
M(t)=\{x:|\omega(x,t)|=W(t)\}.
\]

On the smooth pre-singular interval, the exact magnitude equation gives at every spatial maximum

\[
D_t|\omega|\le \gamma |\omega|,
\qquad
\gamma=\xi^TS\xi.
\]

Hence the upper Dini derivative satisfies the sharper maximum-set form

\[
\boxed{
D^+\log W(t)
\le
G_M(t):=\sup_{x\in M(t)}\gamma^+(x,t).
}
\]

For a first-hitting stage

\[
W(t_{j+1})=qW(t_j),
\qquad q>1,
\]

we therefore have

\[
\boxed{
\int_{I_j}G_M(t)\,dt\ge\log q.
}
\]

Thus the productive source may be evaluated at an actual vorticity-maximum point; it is not necessary to move the center to an unrelated maximum of `gamma`.

On the bounded normalized-stage branch, there is a time `t_j^*` and a center `x_j^*\in M(t_j^*)` for which the normalized positive stretching is bounded below by a fixed constant.

---

## 3. Normalize at the event

Let

\[
W_*=W(t_j^*),
\qquad
r_*:=\sqrt{\frac\nu{W_*}}.
\]

Set

\[
Y=\frac{x-x_j^*}{r_*},
\qquad
\Omega(Y)=\frac{\omega(x_j^*+r_*Y,t_j^*)}{W_*}.
\]

Then

\[
\boxed{
|\Omega(Y)|\le1,
\qquad
|\Omega(0)|=1.
}
\]

Write

\[
\Xi(Y)=\frac{\Omega(Y)}{|\Omega(Y)|}
\]

only on the nonzero-vorticity set.

Assume the M5-376 scale-tight alternative selects one productive dyadic shell

\[
A=\{c_1\le |Y|\le c_2\},
\qquad 0<c_1<c_2<\infty,
\]

whose signed normalized longitudinal contribution obeys

\[
\boxed{
a_A\ge a_0>0.}
\]

Here `a0,c1,c2` are independent of the late first-hitting index.

---

## 4. A fixed productive shell forces positive source capacity

On the fixed normalized shell, the angular Biot--Savart integrand has the form

\[
F(Y)
=C\,|Y|^{-3}
D(\widehat Y,\Xi(Y),\Xi(0))
|\Omega(Y)|,
\]

with

\[
|D|\le1,
\qquad
|\Omega|\le1,
\qquad
|Y|^{-3}\asymp1
\quad(Y\in A).
\]

Thus

\[
|F(Y)|\le C_A
\]

for a fixed shell constant `C_A`.

Since

\[
\int_A F(Y)\,dY\ge a_0,
\]

its positive part satisfies

\[
\int_A F_+\,dY\ge a_0.
\]

Choose

\[
\tau_0:=\frac{a_0}{2|A|}.
\]

Then

\[
a_0
\le
\tau_0|A|
+C_A|\{F_+>\tau_0\}|,
\]

so the productive source set

\[
E:=\{Y\in A:F(Y)>\tau_0\}
\]

obeys

\[
\boxed{
|E|\ge m_0:=\frac{a_0}{2C_A}>0.
}
\]

Hence a fixed-fraction natural shell cannot be supported by an arbitrarily small spatial set.

Moreover, on `E`,

\[
|\Omega(Y)|\,|D(\widehat Y,\Xi(Y),\Xi(0))|
\ge c(a_0,c_1,c_2)>0.
\]

Because both factors are at most one, there are constants

\[
\lambda_0>0,
\qquad
\delta_0>0
\]

such that for every `Y\in E`,

\[
\boxed{
|\Omega(Y)|\ge\lambda_0,
\qquad
|D(\widehat Y,\Xi(Y),\Xi(0))|\ge\delta_0.
}
\]

Since `|D|\le |\Xi(Y)\times\Xi(0)|`, this also gives a fixed projective-angle separation from both alignment and anti-alignment.

Consequently

\[
\boxed{
|\Omega(Y)-\Omega(0)|\ge d_0>0
\qquad(Y\in E)
}
\]

for a constant `d0=d0(lambda0,delta0)`.

This is the capacity upgrade missing from a merely pointwise partner statement.

---

## 5. Central continuity radius

Fix

\[
0<\varepsilon_0<d_0/4.
\]

Define the normalized continuity radius at the maximum center by

\[
\boxed{
\rho_j
:=
\sup\left\{0<\rho<c_1/4:
\sup_{|Y|\le\rho}
|\Omega(Y)-\Omega(0)|\le\varepsilon_0
\right\}.
}
\]

There are only two possibilities along any late-stage subsequence.

### A. Thick-center subsequence

There exists

\[
\rho_0>0
\]

such that

\[
\rho_j\ge\rho_0.
\]

Then the central ball

\[
B_{\rho_0}
\]

has fixed positive normalized volume and all its vorticity values stay within `epsilon0` of `Omega(0)`.

### B. Thin-center subsequence

\[
\rho_j\to0.
\]

By the definition of `rho_j`, for arbitrarily small enlargements of `rho_j` there is a point where the vector changes by at least `epsilon0`. The mean-value theorem therefore gives

\[
\boxed{
\|\nabla_Y\Omega\|_{L^\infty(B_{2\rho_j})}
\gtrsim
\frac{\varepsilon_0}{\rho_j}
\to\infty.
}
\]

Thus loss of central capacity is already a divergent normalized vorticity-gradient event:

\[
\boxed{H_{\rm der,\infty}.}
\]

---

## 6. Thick center plus productive shell forces local normalized palinstrophy

Assume Case A.

Choose a fixed ball `B_R`, with `R>c2+1`, containing both the central ball and the productive shell.

On

\[
F:=B_{\rho_0},
\]

we have

\[
|\Omega-\Omega(0)|\le\varepsilon_0,
\qquad
|F|\ge c\rho_0^3>0.
\]

On the productive set `E`,

\[
|\Omega-\Omega(0)|\ge d_0.
\]

Since `epsilon0<d0/4`, the vector values on `E` and `F` are separated by a fixed amount.

Therefore the vector variance over `B_R` has a uniform lower bound:

\[
\boxed{
\int_{B_R}|\Omega-\overline\Omega_{B_R}|^2dY
\ge c_*>0.
}
\]

The ordinary vector Poincare inequality yields

\[
\boxed{
\int_{B_R}|\nabla_Y\Omega|^2dY
\ge c_{P}>0.
}
\]

Thus a thick central maximum together with a fixed-fraction natural productive shell forces an order-one normalized local palinstrophy occupancy.

In physical variables,

\[
\nabla_Y\Omega
=
\frac{r_*}{W_*}\nabla_x\omega,
\]

so

\[
\boxed{
\frac{r_*^3}{\nu^2}
\int_{B_{Rr_*}(x_j^*)}
|\nabla_x\omega|^2dx
\ge c_P.
}
\]

Equivalently,

\[
\boxed{
\int_{B_{Rr_*}(x_j^*)}
|\nabla_x\omega|^2dx
\gtrsim
\frac{\nu^2}{r_*^3}.
}
\]

This is precisely a derivative-occupancy event, not a new projective terminal state.

---

## 7. Natural-partner collapse

Combining Sections 5 and 6 gives

\[
\boxed{
P_{\rm angular,natural}
\Longrightarrow
H_{\rm der,\infty}
\lor
H_{\rm pal,local/occ},
}
\]

provided the productive shell remains at a common natural-scale event center.

Together with M5-376,

\[
\boxed{
H_{\rm angular,multiscale}
\lor
P_{\rm angular,natural}
\Longrightarrow
H_{\rm der/occ}
\lor
T_{\rm remote/core},
}
\]

where the remote/core term retains loss of the common source window or escape of productive mass to large normalized radius.

Thus `P_angular,natural` no longer needs to be carried as an independent final leaf.

---

## 8. Relation to the older projective-partner and reach-collapse lemmas

The older pairwise-projective result showed that a bounded-geometry partner network with order-one source must carry positive projective variance and therefore angular/magnitude-gradient cost.

The present result is complementary and slightly more primitive:

- it starts directly from one fixed-fraction **signed productive shell**;
- it derives positive spatial measure of the misaligned source from the first-hitting amplitude cap;
- it does not assume a pre-existing discrete packet decomposition;
- the only additional split is whether the central maximum has nonvanishing normalized capacity.

If shell geometry itself collapses or source localization leaves the fixed annulus, the event is routed back to the existing reach/remote/shape channels rather than silently inserted into the Poincare estimate.

---

## 9. Why this is not a global contradiction

The new local palinstrophy lower bound is strong in normalized variables, but the global Leray-Hopf finite budget controls

\[
\nu\int\|\omega\|_2^2dt,
\]

not

\[
\int\|\nabla\omega\|_2^2dt.
\]

Therefore infinitely many local normalized palinstrophy events are not excluded by the energy inequality alone.

Similarly, the thin-center alternative explicitly becomes a high-derivative escape rather than a contradiction.

The gain is a reduction in the number of independent geometric terminals, not a proof of regularity.

---

## 10. DSD audit

### Valid distinctions

- vorticity direction is used only where `|Omega|>0`;
- the central maximum point is **not** treated as an `H^1`-positive-capacity set;
- positive source capacity is derived from the bounded shell integrand and fixed signed shell action;
- Poincare is invoked only after both central and source sets have fixed positive normalized measure;
- collapse of the central continuity radius is retained as a derivative escape.

### Forbidden inference

Do **not** infer from

\[
|\Omega(Y)-\Omega(0)|\ge d_0
\]

at one source point that

\[
\int|\nabla\Omega|^2\ge c.
\]

A point anchor has zero `H^1` capacity in dimension three. The thick-center/thin-center split is essential.

---

## 11. Updated frontier

After M5-377 the angular source subtree is

\[
\boxed{
\text{productive angular source}
\Longrightarrow
H_{\rm der/occ}
\lor
T_{\rm remote/core/shape}.
}
\]

The next task is therefore no longer to analyze generic angular roughness. It is to determine whether the derivative-occupancy branch can be forced into a finite additive charge, or whether all no-derivative subsequences must migrate into dynamic turnover/remote escape.

---

## 12. Audit verdict

### DERIVED

- maximum-set first-hitting action may be centered at an actual vorticity maximum;
- fixed natural productive shell action forces a positive-measure misaligned source set;
- fixed central continuity radius + productive source capacity forces order-one normalized local palinstrophy;
- collapse of central continuity radius forces divergent normalized `L^infty` vorticity gradient;
- natural productive partner is absorbed into the derivative-capacity ledger.

### OPEN

- a finite global additive budget for the derivative-occupancy events;
- exclusion of temporal/remote/common-window loss;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
