# DSD W1 Amplitude-Level Cascade and Half-Power Audit

Date: 2026-08-26

Status: **POSITIVE W1 CRITICAL WORK RESOLVED INTO A FIXED AMPLITUDE-LEVEL NONLINEAR INFLUX / PHYSICAL SCALING SHOWS THIS INFLUX ALONE COSTS ONLY FINITE ENERGY NEAR THE PUTATIVE SINGULAR TIME / PURE AMPLITUDE-CASCADE CONTRADICTION PRUNED / GLOBAL REGULARITY UNPROVED.**

## 1. Signed nonlinear work density

Let

\[
L_s:=\mathbb P(\Omega\times U)
\]

and define

\[
\boxed{
g(Y,s):=-U(Y,s)\cdot L_s(Y,s).
}
\]

The nonlinear term does no total kinetic-energy work. With the W1 tail decay and a cutoff-limit justification,

\[
\boxed{
\int_{\mathbb R^3}g(Y,s)dY=0.
}
\]

The critical `p=3` source is

\[
\boxed{
F_\infty(s)=\int |U|g\,dY.
}
\]

Its invariant mean is

\[
\boxed{
\langle F_\infty\rangle_\mu=f_*>0.
}
\]

Thus `g` is a signed redistribution density with zero zeroth moment and positive amplitude-weighted first moment.

---

## 2. Layer-cake decomposition in velocity amplitude

Set

\[
a(Y,s):=|U(Y,s)|.
\]

For `lambda>0`, define the nonlinear influx into the velocity superlevel set

\[
\boxed{
\mathcal G(\lambda,s)
:=
\int_{\{a>\lambda\}}g(Y,s)dY.
}
\]

Using

\[
a=\int_0^\infty \mathbf 1_{\{a>\lambda\}}d\lambda,
\]

Fubini gives the exact layer-cake identity

\[
\boxed{
F_\infty(s)
=
\int_0^\infty
\mathcal G(\lambda,s)d\lambda.
}
\]

On the compact W1 class let

\[
\|U\|_\infty\le A_0.
\]

Then

\[
\boxed{
F_\infty(s)
=
\int_0^{A_0}
\mathcal G(\lambda,s)d\lambda.
}
\]

Averaging over the invariant measure,

\[
\boxed{
\int_0^{A_0}
\overline{\mathcal G}(\lambda)d\lambda
=f_*>0,
}
\]

where

\[
\overline{\mathcal G}(\lambda)
:=
\langle\mathcal G(\lambda,\cdot)\rangle_\mu.
\]

Therefore there exists at least one amplitude level

\[
\boxed{
\lambda_*\in(0,A_0)
}
\]

such that

\[
\boxed{
\overline{\mathcal G}(\lambda_*)
\ge
\frac{f_*}{A_0}>0.
}
\]

So a W1 survivor must have a fixed normalized velocity-amplitude threshold receiving positive mean nonlinear energy influx.

This is stronger than saying merely that the nonlinear term is active.

---

## 3. DSD interpretation: energy-neutral but amplitude-uphill transfer

Since

\[
\int g=0,
\]

all positive nonlinear work is compensated by negative nonlinear work elsewhere.

Yet

\[
\int a g>0.
\]

Thus the compensation is amplitude-asymmetric: on average the nonlinear term removes energy from lower-amplitude states and deposits it into higher-amplitude states.

The exact DSD statement is

\[
\boxed{
\text{zero total nonlinear work}
+
\text{positive first amplitude moment}
\Longrightarrow
\text{amplitude-uphill redistribution}.
}
\]

The level `lambda_*` gives a concrete state boundary witnessing this conversion.

---

## 4. Physical scaling of the level current

Under backward Leray scaling,

\[
u(x,t)=(T_*-t)^{-1/2}U(Y,s),
\]

and

\[
L_s^{phys}(x,t)
=(T_*-t)^{-3/2}L_s(Y,s).
\]

Therefore the physical nonlinear work density satisfies

\[
g_{phys}(x,t)
=-u\cdot L_s^{phys}
=(T_*-t)^{-2}g(Y,s).
\]

The Leray level `a>lambda_*` corresponds to the physical velocity level

\[
\boxed{
|u|>
\frac{\lambda_*}{\sqrt{T_*-t}}.
}
\]

Since `dx=(T_*-t)^(3/2)dY`, the physical nonlinear influx into this moving amplitude state is

\[
\boxed{
\mathcal G_{phys}(t)
=(T_*-t)^{-1/2}
\mathcal G(\lambda_*,s).
}
\]

---

## 5. The half-power barrier reappears exactly

Integrating the absolute scaling factor in physical time gives

\[
\int^{T_*}(T_*-t)^{-1/2}dt<\infty.
\]

Equivalently, because

\[
dt=(T_*-t)ds=e^{-s}ds,
\]

one normalized order-one amplitude-transfer event contributes physical energy work of size

\[
\boxed{
O(e^{-s/2}).
}
\]

Hence even positive-density recurrence of the fixed normalized level current is compatible with a finite physical kinetic-energy budget:

\[
\boxed{
\sum_j e^{-s_j/2}<\infty
}
\]

on a geometric Leray stage sequence.

Thus the amplitude-level cascade alone cannot close W1 by summing physical energy costs.

This is the same half-power obstruction encountered in earlier turnover/first-hitting ledgers, now derived directly from the final Lamb-force formulation.

---

## 6. Consequence for proof search

A proof based only on

\[
\overline{\mathcal G}(\lambda_*)>0
\]

cannot contradict finite energy.

The endpoint must use the simultaneous second fact already proved for the same solenoidal Lamb force:

\[
\boxed{
\left\langle
\int\Delta U\cdot L_s
\right\rangle_\mu>0.
}
\]

That is, the nonlinearity must simultaneously move energy

1. uphill in velocity amplitude, and
2. toward higher spatial frequency.

The remaining target is therefore genuinely **two-coordinate**:

\[
\boxed{
\text{amplitude cascade}
+
\text{frequency cascade}.
}
\]

Neither marginal current alone has a divergent physical budget that yields a contradiction.

---

## 7. Updated frontier

The surviving W1 mechanism is now constrained by

\[
\boxed{
\int g=0,
\qquad
\int |U|g=f_*>0,
\qquad
\left\langle\int\Delta U\cdot L_s\right\rangle_\mu>0.
}
\]

The first two statements define an amplitude-uphill signed transfer.
The third defines a high-frequency-uphill transfer.

A useful next theorem would construct a joint amplitude-frequency transfer measure or a Littlewood-Paley/amplitude-bin ledger and prove that recurrent positive drift in both coordinates forces either a finite-energy contradiction or a previously closed turnover/export mechanism.

The present note also prevents a false closure: the fixed amplitude-level influx is real, but its physical integrated cost decays by the `1/2` power and is summable.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
