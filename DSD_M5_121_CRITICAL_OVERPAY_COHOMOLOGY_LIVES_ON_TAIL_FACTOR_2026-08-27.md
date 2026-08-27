# DSD M5-121 — Critical Overpay Cohomology Lives on the Tail Factor

Date: 2026-08-27

Status: **THE FINITE-TIME CORE-TAIL COCYCLE IS DIFFERENTIATED IN THE DYNAMICAL SENSE / CRITICAL PRESSURE OVERPAY SPLITS INTO A RENORMALIZED-CUBIC COBoundary PLUS ONE-SIXTH OF THE CANONICAL TAIL CUBIC SLICE DENSITY / SAME-TAIL FIBERS CAN MODIFY THE OVERPAY ONLY BY AN EXACT BOUNDED COBoundary / GLOBAL REGULARITY UNPROVED.**

---

## 1. Start from the audited finite-time identity

M5-120 gives, for every fixed `h>0` on a positive-residue ergodic W1 component,

\[
\boxed{
\int_0^hX_3(S_sV)ds
=
\frac13[\mathcal K(S_hV)-\mathcal K(V)]
+
\frac13\int_{-h/2}^0\mathfrak c_\rho(T_V)d\rho.
}
\]

All quantities in this identity have already been independently formed:

- `X_3` is the critical pressure-overpay channel;
- `mathcal K` is the bounded renormalized cubic charge after canonical-tail subtraction;
- `mathfrak c_rho` is the cubic density on the canonical tail log cylinder.

No new limit is introduced below.

---

## 2. Absolute continuity of the renormalized cubic charge along the orbit

The left-hand side is absolutely continuous in `h`.

The tail-window term

\[
\int_{-h/2}^0\mathfrak c_\rho(T_V)d\rho
\]

is also absolutely continuous because the canonical log-cylinder density is locally integrable and uniformly bounded by the Type-I tail envelope.

Therefore the difference

\[
\mathcal K(S_hV)-\mathcal K(V)
\]

is absolutely continuous in `h` along almost every orbit.

Define its dynamical derivative

\[
\boxed{
\mathcal L\mathcal K(V)
:=\frac d{dh}\mathcal K(S_hV)\bigg|_{h=0}
}
\]

where it exists; the finite-time identity shows it exists for almost every orbit time in the usual absolutely-continuous sense.

---

## 3. Differentiate the tail window

Let

\[
F(h):=\int_{-h/2}^0\mathfrak c_\rho(T_V)d\rho.
\]

For almost every `h`,

\[
F'(h)
=\frac12\mathfrak c_{-h/2}(T_V).
\]

At `h=0`, in the a.e./Lebesgue-point sense,

\[
\boxed{F'(0)=\frac12\mathfrak c(T_V).}
\]

Hence differentiating M5-120 gives

\[
\boxed{
X_3(V)
=
\frac13\mathcal L\mathcal K(V)
+
\frac16\mathfrak c(T_V)
}
\]

for almost every state-time under the invariant measure.

Equivalently,

\[
\boxed{
X_3-rac16\mathfrak c\circ\pi
=
\frac13\mathcal L\mathcal K.
}
\]

---

## 4. Dynamical-cohomology interpretation

In additive cocycle notation, two observables differ by a coboundary when their difference is the derivative of a bounded state function along the flow.

Therefore

\[
\boxed{
[X_3]
=
\left[\frac16\mathfrak c\circ\pi\right]
}
\]

as a dynamical cohomology class on the W1 compact system.

The non-exact critical part of the pressure-overpay channel is thus entirely carried by the canonical tail factor.

The renormalized strong-critical quotient contributes only the bounded coboundary `L K/3`.

---

## 5. Same-tail fiber cancellation

Let `V,W` satisfy

\[
T_V=T_W.
\]

Factor equivariance preserves this relation forward:

\[
T_{S_sV}
=D_sT_V
=D_sT_W
=T_{S_sW}.
\]

Subtract the cohomological identities:

\[
\boxed{
X_3(V)-X_3(W)
=
\frac13
\bigl[
\mathcal L\mathcal K(V)-\mathcal L\mathcal K(W)
\bigr].
}
\]

Integrated over `[0,h]`,

\[
\boxed{
\int_0^h
[X_3(S_sV)-X_3(S_sW)]ds
=
\frac13
\Bigl[
\Delta\mathcal K_h-\Delta\mathcal K_0
\Bigr],
}
\]

where

\[
\Delta\mathcal K_h
:=\mathcal K(S_hV)-\mathcal K(S_hW).
\]

Since `mathcal K` is bounded on compact `M`, the right-hand side is uniformly bounded in `h`.

Therefore

\[
\boxed{
\lim_{h\to\infty}
\frac1h
\int_0^h
[X_3(S_sV)-X_3(S_sW)]ds
=0
}
\]

whenever the long-time average is taken along complete same-tail trajectories.

Same-tail fibers cannot carry an independent linear critical-overpay drift.

---

## 6. Relation to M5-115 fiber residue

M5-115 already showed that same-tail differences lie in

\[
L^2\cap L^3
\]

and carry zero cubic Abel residue.

The present calculation is the dynamical strengthening:

\[
\boxed{
\text{zero fiber residue}
\quad\Longrightarrow\quad
\text{zero fiber critical-overpay cohomology}.
}
\]

Thus both the critical mass defect and the non-exact critical pressure-work defect descend to the same canonical tail factor.

---

## 7. Insert the exact pressure-strain residual inequality

M5-108 gives the pointwise critical estimate

\[
\boxed{
\mathcal E_3\ge2\nu X_3.
}
\]

Using the cohomology identity,

\[
\boxed{
\mathcal E_3
\ge
\frac{2\nu}{3}\mathcal L\mathcal K
+
\frac\nu3\mathfrak c\circ\pi.
}
\]

Equivalently,

\[
\boxed{
\mathcal E_3
-
\frac{2\nu}{3}\mathcal L\mathcal K
\ge
\frac\nu3\mathfrak c\circ\pi.
}
\]

This is a statewise/a.e. lower bound for the pressure-strain mismatch after removal of one bounded strong-critical coboundary.

It does not make `E_3` itself a tail observable.

---

## 8. Return-time form

For a return sequence `h_n` with

\[
S_{h_n}V\to V,
\]

M5-120 gives

\[
\int_0^{h_n}X_3ds
=
\frac13\int_{-h_n/2}^0\mathfrak c_\rho(T_V)d\rho
+o(1).
\]

Hence

\[
\boxed{
\int_0^{h_n}\mathcal E_3(S_sV)ds
\ge
\frac{2\nu}{3}
\int_{-h_n/2}^0\mathfrak c_\rho(T_V)d\rho
+o(1).
}
\]

On a positive-residue ergodic trajectory this grows asymptotically at least like

\[
\boxed{
\frac{\nu\mathscr R_3}{3}h_n.
}
\]

This reproduces the invariant mean lower bound without introducing a finite-budget claim.

---

## 9. DSD four-chain audit

### Formation — GREEN

The coboundary is defined from the already finite renormalized cubic charge.  No divergent `L3` quantity is differentiated directly.

### Axis — GREEN

Fiber direction and tail-factor translation direction are kept distinct.

### Static aggregation — GREEN

Tail cubic density and fiber coboundary are not counted as two positive costs.  The coboundary is signed.

### Dynamics — GREEN

The cohomology identity is derived from the finite-time forward cocycle, not from an invariant average.

### Cross-audit — GREEN

M5-107's invariant anomaly is recovered by integrating this identity; it is not used as an input to prove the identity.

---

## 10. Updated P0/P1 frontier

The earlier P0/P1 split concerned whether the **nonnegative finite-core residual payer** `H_R` descends to the tail factor.

For the signed critical-overpay channel `X_3`, that question is now settled:

\[
\boxed{
X_3\text{ descends modulo a bounded coboundary.}
}
\]

Therefore the only genuinely unresolved fiber question is no longer the anomaly itself.  It is whether same-tail strong-critical fibers can modulate the **nonnegative residual** `E_3` while their signed overpay modulation remains exact.

The next calculation should derive the relative pressure-strain residual identity for two same-tail states and determine whether persistent fiber variance in `E_3` requires a positive relative-gradient/frequency production channel.

That is the remaining P1 mechanism.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
