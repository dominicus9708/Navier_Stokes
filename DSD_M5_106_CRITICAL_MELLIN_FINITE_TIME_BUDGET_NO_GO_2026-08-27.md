# DSD M5-106 — Critical Mellin Finite-Time Budget No-Go

Date: 2026-08-27

Status: **DYNAMIC BUDGET FIREWALL / THE `alpha->1` MELLIN PAYER IS SPACETIME-CRITICAL, SO A FINITE STANDARD-CELL TIME INTERVAL DOES NOT GIVE A FINITE TOTAL CRITICAL SURPLUS BUDGET / THE LINEAR-IN-LERAY-TIME LOWER BOUND FROM M5-103 IS COMPATIBLE WITH LOGARITHMIC TERMINAL ACCUMULATION / THIS ROUTE CANNOT CLOSE W1 BY FINITE-TIME COUNTING ALONE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why this audit is necessary

M5-103 proved for a fixed Leray shift `h` that

\[
\liminf_{\varepsilon\downarrow0}
\left\langle
\int_0^{\sigma_h}
\mathcal E_\varepsilon d\sigma
\right\rangle_\mu
\ge
\frac{\nu h\mathscr R_3}{6}.
\]

Since

\[
\sigma_h=\sigma_*(1-e^{-h})<\sigma_*
\]

and `sigma_h -> sigma_*` as `h->infinity`, it would be tempting to argue that a finite terminal time cannot support a quantity growing linearly in `h`.

That inference is false at the critical scaling.

---

# 2. Critical instantaneous scaling

At `alpha=1`, the homogeneous payer has schematic form

\[
S_1[V]
\sim
\int |V||P_V|^2dz.
\]

Use the inverse-Leray representation

\[
V(z,\sigma)
=\tau^{-1/2}U(Y,\eta),
\qquad
P_V(z,\sigma)=\tau^{-1}P(Y,\eta),
\]

with

\[
\tau:=\sigma_*-\sigma,
\qquad
z=\sqrt\tau Y.
\]

Then

\[
dz=\tau^{3/2}dY.
\]

Therefore

\[
\boxed{
S_1[V(\sigma)]
=\tau^{-1}
\mathcal W[U(\eta)],
}
\]

where

\[
\mathcal W[U]
:=\int |U||P|^2dY
\]

is the M5-54 critical W1 pressure payer.

The same `tau^{-1}` scaling applies to the critical limit of the surplus.

---

# 3. Cell time versus Leray time

By definition

\[
\eta=\log\frac{\sigma_*}{\tau},
\]

so

\[
\boxed{d\sigma=\tau d\eta.}
\]

Consequently

\[
S_1[V]d\sigma
=\mathcal W[U(\eta)]d\eta.
\]

Thus the terminal singular factor cancels the shrinking physical/cell-time interval exactly.

Hence

\[
\boxed{
\int_0^{\sigma_h}S_1[V]d\sigma
=
\int_0^h\mathcal W[U(\eta)]d\eta.
}
\]

A bounded positive invariant mean of `W` therefore produces growth proportional to `h`, even though the standard-cell time remains bounded by `sigma_*`.

---

# 4. Compatibility with M5-103

M5-103's lower bound

\[
\frac{\nu h\mathscr R_3}{6}
\]

has exactly the same logarithmic terminal scaling.

Thus it is dimensionally and dynamically compatible with a recurrent W1 cell carrying a nonzero critical pressure action per unit Leray time.

No contradiction follows from

\[
h\to\infty
\]

inside a finite terminal cell-time interval.

---

# 5. DSD four-chain audit

## Formation

The critical payer is a formed spacetime action, but its density becomes singular at the terminal boundary.

**GREEN.**

## Axis

`eta` is logarithmic similarity time while `sigma` is standard Navier--Stokes cell time.
They are related by a singular Jacobian and must not be aggregated as if they had comparable interval lengths.

**GREEN.**

## Static aggregation

An order-one critical cost per unit `eta` is not an independent cost per fixed amount of `sigma`.
The Jacobian converts the same critical channel between the two descriptions.

**GREEN.**

## Dynamics

Recurrence can sustain a positive invariant critical action over arbitrarily long Leray time while physical/cell intervals shrink geometrically.

**GREEN.**

---

# 6. RED firewall

The following implication is permanently rejected for the Mellin route:

\[
\boxed{
\sigma_*<\infty
+\int_0^{\sigma_h}\mathcal E_1\sim h
\ \not\Rightarrow\ 
\text{contradiction}.
}
\]

A separate initial-data-controlled finite **critical** action bound would be required.
No such bound is supplied by the ordinary energy inequality.

This is the same scaling obstruction identified abstractly in M5-61, now written explicitly in the new Mellin variables.

---

# 7. Updated live target

After M5-105 and the present budget audit, the critical Mellin route has only two legitimate ways forward:

1. derive uniform log-Cesaro tightness from a genuinely dynamic PDE-specific genealogy/pressure constraint; or
2. derive a direct statewise absorption/rigidity theorem showing that the critical pressure payer required by a nonzero Cesaro residue cannot be realized by an unforced smooth finite-energy ancestry.

Simple static norms and simple finite-terminal-time accumulation are both closed as shortcuts.

The next calculation should therefore examine the **same-trajectory pressure/momentum flux associated with a long truncated `1/r` corridor**, rather than another norm-only estimate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
