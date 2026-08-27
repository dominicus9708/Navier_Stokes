# DSD M5-99 — R1 Topology-Only Coercivity No-Go

Date: 2026-08-27

Status: **R1 FIRST AUDIT / SAME-SURFACE SIGN REVERSAL ALONE DOES NOT CONTROL THE NORMAL CROSSING BY THE ANGULAR CHANNEL / A THIN TRANSITION STRIP CAN KEEP NORMAL L2 CROSSING ORDER ONE WHILE ANGULAR MASS TENDS TO ZERO / THE MISSING PAYMENT MOVES INTO TANGENTIAL DERIVATIVE FORMATION / THIS IS A STRUCTURAL COUNTERMODEL, NOT A NAVIER–STOKES SOLUTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. R1 input

On one connected regular amplitude surface `Gamma` with

\[
a=|U|=\lambda>0,
\]

write

\[
U=q n+v,
\qquad v\cdot n=0,
\qquad q^2+|v|^2=\lambda^2.
\]

R1 means that `q` takes both signs on the same connected surface.
By continuity it crosses

\[
q=0,
\]

and at the zero set

\[
|v|=\lambda.
\]

M5-94 correctly identified this as pointwise angular-channel activation.
The present audit asks whether the pointwise statement alone gives an integrated lower bound for `G`.

---

# 2. Formation chain

Take a smooth two-sphere as a model regular level surface and an equatorial coordinate `s` measuring signed geodesic distance from the equator.

For `epsilon>0`, choose a smooth odd transition profile `c_epsilon(s)` such that

\[
c_\varepsilon=+1
\quad\text{for }s\ge \varepsilon,
\]

\[
c_\varepsilon=-1
\quad\text{for }s\le-\varepsilon,
\]

and `|c_epsilon|<=1` in the transition strip.

Set

\[
q_\varepsilon=\lambda c_\varepsilon.
\]

On the equatorial strip choose a smooth unit tangential direction `tau` and put

\[
v_\varepsilon
=\lambda\sqrt{1-c_\varepsilon^2}\,\tau,
\]

with `v_epsilon=0` outside the strip.

This is a smooth formed surface field satisfying

\[
q_\varepsilon^2+|v_\varepsilon|^2=\lambda^2.
\]

It is only a kinematic surface model. It is **not** asserted to extend to a divergence-free three-dimensional Navier--Stokes state.

---

# 3. Axial chain

The normal channel occupies almost the entire surface:

\[
q_\varepsilon^2\to\lambda^2
\]

away from a strip of area `O(epsilon)`.
Hence for any fixed smooth positive surface weight `h` bounded above and below,

\[
\int_\Gamma h q_\varepsilon^2\,dS
\to
\lambda^2\int_\Gamma h\,dS>0.
\]

The tangential channel is supported only in the transition strip, so

\[
\int_\Gamma h|v_\varepsilon|^2\,dS
=O(\varepsilon).
\]

Therefore

\[
\boxed{
\frac{\int h q_\varepsilon^2}
{\int h|v_\varepsilon|^2}
\to\infty.
}
\]

Thus the exact pointwise event `q=0 => |v|=lambda` has no geometry-free positive-area consequence.

---

# 4. Static aggregation verdict

For the M5 coarea weight

\[
h=\frac{|\nabla a|}{\lambda},
\]

a regular surface with a uniform nondegeneracy margin gives the same conclusion.

Hence no universal estimate of the form

\[
T_{R1}\le C G_{R1}
\]

can be derived from sign reversal and `q^2+|v|^2=lambda^2` alone.

In particular, the stronger desired coefficient-one estimate cannot be a purely topological theorem.

---

# 5. Where the missing cost goes

The transition becomes steep:

\[
|\nabla_\Gamma q_\varepsilon|
\sim\frac{\lambda}{\varepsilon}
\]

inside a strip of area `O(epsilon)`.
Consequently

\[
\boxed{
\int_\Gamma
|\nabla_\Gamma q_\varepsilon|^2dS
\sim\frac{\lambda^2}{\varepsilon}
\to\infty.
}
\]

Thus the thin-strip escape does not remove the reconnection payment. It transfers it from angular mass to derivative formation.

The correct R1 payer must therefore involve some combination of

\[
\boxed{
G
+\text{tangential derivative formation}
}
\]

rather than `G` alone.

---

# 6. DSD four-chain audit

## Formation

A same-surface sign-changing state is formable with an arbitrarily thin transition strip.

**GREEN.**

## Axis

Normal and tangential channels remain exactly separated by

\[
q^2+|v|^2=\lambda^2.
\]

**GREEN.**

## Static aggregation

A pointwise full-tangential crossing does not imply a positive measure angular reservoir.
The angular integral can vanish while the normal L2 reservoir remains order one.

**GREEN no-go result.**

## Dynamics

No recurrence or time evolution is used in this countermodel.
Therefore no later dynamical hypothesis may be used retroactively to claim that topology alone supplied the missing bound.

**GREEN / not invoked.**

---

# 7. Cross-audit and RED firewall

The following implication is permanently rejected:

\[
\boxed{
q\text{ changes sign on }\Gamma
\ \not\Rightarrow\ 
G_\Gamma\ge c T_\Gamma
}
\]

without an independent quantitative regularity/derivative hypothesis.

The surface model is not a Navier--Stokes counterexample; it is a counterexample to the **logical sufficiency** of topology-only R1 coercivity.

---

# 8. Next route

There are two legitimate continuations.

1. Add the derivative formation channel and seek a genuine R1 coercivity theorem under W1 regularity margins.
2. Use the M5-88 amplitude-weight freedom to ask whether the exact endpoint can be bypassed before R1/R2 by a weight whose cumulative growth never enters the forbidden `chi_w>0` zone.

The second route is cheaper logically and is audited next. It does not use this no-go result as a proof input beyond ruling out the topology-only shortcut.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
