# DSD M5-109 — Tail-to-Core Critical Payer Transfer

Date: 2026-08-27

Status: **W1-CONDITIONAL TAIL/CORE COUPLING / THE CRITICAL PRESSURE-STRAIN RESIDUAL HAS UNIFORMLY O(R^-2) FAR-TAIL CONTENT / NONZERO CUBIC RESIDUE THEREFORE FORCES A POSITIVE COMPONENT-FREE PAYER INSIDE ONE FIXED LERAY CORE / LOCAL SMOOTH CONTINUITY AND MINIMALITY MAKE ROBUST CORE-PAYER EVENTS SYNDETIC / NO FINITE CRITICAL ACTION BUDGET IS CLAIMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-108

The critical componentwise residual is

\[
\mathcal E_3
=
\int a\,|P-m_k(a,s)-2\nu b|^2dY.
\]

M5-108 gives

\[
\boxed{
\langle\mathcal E_3\rangle_\mu
\ge
\frac\nu3\mathscr R_3
>0.
}
\]

This residual is a necessary carrier of the W1 cubic anomaly.

The next question is whether that residual can live only in the passive remote `1/r` memory.

---

## 2. Uniform remote W1 bounds

On the retained W1 class, the critical tail and pressure localization give uniformly for sufficiently large `r=|Y|`

\[
|U(Y,s)|\le \frac{C_U}{r},
\]

\[
|\nabla U(Y,s)|+|\nabla a(Y,s)|\le\frac{C_1}{r^2},
\]

and, in the canonical decaying pressure gauge,

\[
|P(Y,s)|\le\frac{C_P}{r^2}.
\]

Since

\[
|b|
=|U\cdot\nabla\log a|
\le|\nabla a|,
\]

we also have

\[
\boxed{|b(Y,s)|\le C_b r^{-2}.}
\]

For a small-amplitude tail component, its componentwise pressure mean is bounded by the same pressure scale, so

\[
|P-m_k(a,s)|\lesssim r^{-2}
\]

on the remote regular levels.

---

## 3. The exact residual tail is summable

Hence on `r>R`,

\[
a|P-m_k-2\nu b|^2
\lesssim
r^{-1}r^{-4}
=r^{-5}.
\]

Therefore

\[
\boxed{
\mathcal E_{3,>R}
:=
\int_{|Y|>R}
a|P-m_k-2\nu b|^2dY
\le
\frac{C_E}{R^2}.
}
\]

The bound is uniform on the compact W1 class.

Thus the residual required by `R_3` is not itself a logarithmically distributed tail quantity.

It is spatially summable and becomes core-localized.

---

## 4. Replace branch-dependent residual by a component-free payer

For recurrence transport it is useful to avoid branch labels.

Define

\[
S_3:=\int a|P|^2dY
\]

in the canonical pressure gauge and

\[
T_3:=\int a b^2dY.
\]

The componentwise pressure variance satisfies

\[
S_{comp,3}\le S_3.
\]

Also

\[
|x-y|^2\le2|x|^2+2|y|^2.
\]

Therefore

\[
\begin{aligned}
\mathcal E_3
&\le
2S_{comp,3}+8\nu^2T_3\\
&\le
2S_3+8\nu^2T_3.
\end{aligned}
\]

Define the component-free critical payer

\[
\boxed{
\mathcal H_3
:=
S_3+4\nu^2T_3.
}
\]

Then

\[
\boxed{
\mathcal H_3\ge\frac12\mathcal E_3.
}
\]

Consequently

\[
\boxed{
\langle\mathcal H_3\rangle_\mu
\ge
\frac\nu6\mathscr R_3.
}
\]

---

## 5. Remote part of the component-free payer also vanishes

From the W1 tail bounds,

\[
aP^2\lesssim r^{-5},
\qquad
a b^2\lesssim r^{-5}.
\]

Hence

\[
\boxed{
\mathcal H_{3,>R}
\le
\frac{C_H}{R^2}
}
\]

uniformly in the W1 recurrent class.

Choose one fixed normalized radius `R_*` such that

\[
\frac{C_H}{R_*^2}
\le
\frac{\nu\mathscr R_3}{12}.
\]

Then for the fixed-core payer

\[
\mathcal H_{3,R_*}
:=
\int_{|Y|\le R_*}
\left(aP^2+4\nu^2ab^2\right)dY,
\]

we have

\[
\boxed{
\langle\mathcal H_{3,R_*}\rangle_\mu
\ge
\frac{\nu\mathscr R_3}{12}>0.
}
\]

Thus a positive tail residue forces positive mean payer inside one finite normalized core.

---

## 6. Local continuity

On the fixed ball `B_{R_*}`, the W1 class is locally smooth/analytic with uniform finite derivative bounds.

The canonical pressure gauge has locally smooth dependence through the Navier--Stokes pressure decomposition.

Therefore

\[
U\mapsto\mathcal H_{3,R_*}(U)
\]

is continuous in the retained local W1 topology.

Since the minimal W1 set is compact,

\[
\mathcal H_{3,R_*}\le H_*<\infty
\]

uniformly.

---

## 7. A robust positive payer state exists

Let

\[
h_*:=\frac{\nu\mathscr R_3}{24}.
\]

If every state satisfied

\[
\mathcal H_{3,R_*}<h_*,
\]

the invariant average would be smaller than `h_*`, contradicting Section 5.

Hence there exists a state `U_*` in the minimal W1 set with

\[
\boxed{
\mathcal H_{3,R_*}(U_*)\ge h_*.
}
\]

By continuity there is an open W1 neighborhood `O_*` on which, after shrinking if needed,

\[
\boxed{
\mathcal H_{3,R_*}\ge h_*/2>0.
}
\]

---

## 8. Minimal recurrence makes the core payer syndetic

Every nonempty open set in a compact minimal flow has syndetic return times.

Therefore the W1 trajectory returns to `O_*` with bounded gaps in Leray time.

Thus there is a syndetic sequence of intervals/states on which

\[
\boxed{
\mathcal H_{3,R_*}
\ge
\frac{\nu\mathscr R_3}{48}.
}
\]

This is a genuine tail-to-core dynamical coupling:

\[
\boxed{
\text{nonzero critical log-tail residue}
\Longrightarrow
\text{recurrent finite-core pressure/longitudinal-strain payer}.
}
\]

The remote tail can be kinematically passive, but its anomaly cannot be dynamically disconnected from the core.

---

## 9. Static split of the payer

At every robust core-payer event,

\[
S_{3,R_*}+4\nu^2T_{3,R_*}
\ge h_*/2.
\]

Therefore at least one of the two channels satisfies

\[
\boxed{
S_{3,R_*}
\ge\frac{h_*}{4}
}
\]

or

\[
\boxed{
\nu^2T_{3,R_*}
\ge\frac{h_*}{16}.
}
\]

So the core event has two honest subbranches:

1. pressure-oscillation payer;
2. longitudinal-strain payer.

They may coexist.

No cancellation between them is allowed because both are nonnegative static channels.

---

## 10. DSD four-chain audit

### Formation

The tail residue is formed through the `p>3 -> 3+` limit; the core payer is formed only after the uniform remote estimate is proved.

### Axis

Pressure variance and longitudinal strain are retained as separate channels.

### Static aggregation

The remote residual is not counted again after it is bounded and removed. The core lower bound is the remainder of the same anomaly, not a second copy of it.

### Dynamics

Minimal recurrence is invoked only after the fixed-core payer is shown to be a continuous state observable.

### Cross-audit

The dependency remains acyclic:

\[
\mathscr R_3
\to
\langle\mathcal E_3\rangle
\to
\langle\mathcal H_{3,R_*}\rangle
\to
\text{one robust core payer state}
\to
\text{syndetic returns}.
\]

---

## 11. What this does not prove

The core payer is scale-critical under the terminal recurrence.

No initial-data-controlled finite total action for its infinitely many physical copies is known.

Therefore syndetic recurrence of the payer is not itself a contradiction.

The next gate is to compare this forced finite-core payer with known or derivable **local critical regularity criteria**, especially the boundary between finite-index Lorentz `L^{3,q}`, `q<infinity`, and the unresolved large weak-`L3` endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
