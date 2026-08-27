# DSD M5-120 — Renormalized Cubic Core–Tail Cocycle

Date: 2026-08-27

Status: **FINITE-TIME CRITICAL MOMENT BALANCE RENORMALIZED AGAINST THE CANONICAL TAIL / THE INTEGRATED CORE PRESSURE-OVERPAY EQUALS A BOUNDED RENORMALIZED-CUBIC COBoundary PLUS THE ACTUAL BACKWARD-GENEALOGY CUBIC CHARGE STORED IN ONE FINITE LOG-RADIUS WINDOW / THE INVARIANT `R3/6` ANOMALY IS RECOVERED AS THE MEAN OF THIS COCYCLE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why a finite-time cocycle is needed

M5-107 proved the invariant-mean identity

\[
\langle X_3\rangle
=\frac{\mathscr R_3}{6},
\]

where `X_3` is the critical pressure-overpay channel.

M5-118 identified

\[
\mathscr R_3
=\int\mathfrak c(T)d\nu(T)
\]

as the stationary cubic density of the canonical tail log-cylinder.

An invariant-average equality does not yet tell us how one finite core interval creates one finite piece of tail memory.  The present note derives that finite-time relation.

---

## 2. The `p>3` moment ledger

For

\[
p=3+\varepsilon,
\qquad\varepsilon>0,
\]

let

\[
M_p(V):=\int_{\mathbb R^3}|V|^p dY.
\]

Use the M5-107 notation

\[
\boxed{
X_p
:=(p-2)\Pi_p-\nu\mathcal D_p.
}
\]

The exact Leray moment identity is

\[
\boxed{
X_p
=\frac1p\frac d{ds}M_p
+\frac{p-3}{2p}M_p.
}
\]

Integrating along one W1 orbit from `0` to `h` gives

\[
\boxed{
\int_0^hX_p(S_sV)ds
=\frac1p\bigl[M_p(S_hV)-M_p(V)\bigr]
+\frac{\varepsilon}{2p}
\int_0^hM_p(S_sV)ds.
}
\]

No recurrence has been used.

---

## 3. Renormalized cubic charge after tail subtraction

Let `T_V` be the canonical tail and define

\[
\boxed{
\mathcal K(V)
:=
\int_{|Y|\le1}|V|^3dY
+
\int_{|Y|>1}
\bigl(|V|^3-|T_V|^3\bigr)dY.
}
\]

This integral is finite.

Indeed on a dyadic shell `A_R`, canonical-tail approximation gives

\[
\|V-T_V\|_{L^3(A_R)}\le CR^{-1/2},
\]

while both `V` and `T_V` have uniformly bounded critical shell `L3` norm.  Hence

\[
\int_{A_R}
\bigl||V|^3-|T_V|^3\bigr|dY
\lesssim R^{-1/2}.
\]

Summing over dyadic radii converges.

The same estimate, combined with the Type-I `Linf` shell bound, gives a uniform summable majorant for

\[
|V|^{3+\varepsilon}-|T_V|^{3+\varepsilon}
\]

for small `epsilon>=0`.  Therefore

\[
\boxed{
\mathcal K_{3+\varepsilon}(V)
\to\mathcal K(V)
}
\]

uniformly on the compact W1 class, where

\[
\mathcal K_p(V)
:=M_p(V)-I_p(T_V),
\]

and

\[
I_p(T)
:=\int_{|Y|>1}|T(Y)|^p dY.
\]

Continuity of the canonical tail factor then makes `mathcal K` a bounded continuous function on `M`.

---

## 4. Exact shift of the tail `p`-moment

Let

\[
a:=h/2.
\]

On the log cylinder,

\[
\Phi_{T_{S_hV}}(\rho,\theta)
=\Phi_{T_V}(\rho-a,\theta).
\]

Define

\[
c_{p,T}(\rho)
:=\int_{S^2}|\Phi_T(\rho,\theta)|^p d\theta.
\]

Then

\[
I_{3+\varepsilon}(T)
=\int_0^\infty
 e^{-\varepsilon\rho}
c_{3+\varepsilon,T}(\rho)d\rho.
\]

A direct change of variables gives

\[
\boxed{
\begin{aligned}
I_{3+\varepsilon}(D_hT)-I_{3+\varepsilon}(T)
&=(e^{-\varepsilon a}-1)I_{3+\varepsilon}(T)\\
&\quad
+e^{-\varepsilon a}
\int_{-a}^0e^{-\varepsilon\rho}
c_{3+\varepsilon,T}(\rho)d\rho.
\end{aligned}
}
\]

---

## 5. Critical limit on an ergodic component

Fix an ergodic component with positive residue

\[
\mathscr R_3>0.
\]

For `nu`-almost every tail state, the log-translation Cesaro mean equals `mathscr R_3`; hence its Abel mean also satisfies

\[
\boxed{
\varepsilon I_{3+\varepsilon}(T)
\to\mathscr R_3.
}
\]

Therefore

\[
(e^{-\varepsilon a}-1)I_{3+\varepsilon}(T)
\to-a\mathscr R_3,
\]

while the finite-window term converges to

\[
\int_{-a}^0c_{3,T}(\rho)d\rho
=\int_{-h/2}^0\mathfrak c_\rho(T)d\rho.
\]

Thus

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\bigl[
I_{3+\varepsilon}(D_hT)-I_{3+\varepsilon}(T)
\bigr]
=
\int_{-h/2}^0\mathfrak c_\rho(T)d\rho
-\frac h2\mathscr R_3.
}
\]

---

## 6. The dilation term supplies the missing mean

For fixed finite `h`, the same Abel residue is invariant along the tail translation orbit.  Hence

\[
\frac{\varepsilon}{2(3+\varepsilon)}
\int_0^hM_{3+\varepsilon}(S_sV)ds
\to
\frac h6\mathscr R_3.
\]

The mean contribution

\[
-\frac1{3}\frac h2\mathscr R_3
=-\frac h6\mathscr R_3
\]

coming from the shifted exterior tail is canceled exactly by this Leray dilation term.

This cancellation is structural and is the reason the final finite-time formula contains an actual finite log window rather than an additional `R3` term.

---

## 7. The exact critical core-tail cocycle

Pass to `epsilon downarrow0` in the integrated `p>3` ledger, using the critical convergence package already audited in M5-107.

For `mu`-almost every state on the chosen ergodic component and every fixed `h>0`, obtain

\[
\boxed{
\int_0^hX_3(S_sV)ds
=
\frac13\bigl[
\mathcal K(S_hV)-\mathcal K(V)
\bigr]
+
\frac13
\int_{-h/2}^0
\mathfrak c_\rho(T_V)d\rho.
}
\]

This is the central identity.

The first term is a bounded coboundary on the compact W1 state space.

The second term is nonnegative and is exactly the cubic charge stored in the length-`h/2` backward-genealogy window of the current canonical tail.

---

## 8. Invariant mean check

Average the cocycle under `mu`.

Invariance kills the coboundary:

\[
\int
[\mathcal K(S_hV)-\mathcal K(V)]d\mu=0.
\]

Translation invariance of `nu` gives

\[
\int
\int_{-h/2}^0\mathfrak c_\rho(T)d\rho d\nu
=\frac h2\mathscr R_3.
\]

Hence

\[
\boxed{
\int\int_0^hX_3(S_sV)dsd\mu
=\frac h6\mathscr R_3,
}
\]

or

\[
\boxed{
\langle X_3\rangle=\mathscr R_3/6,
}
\]

exactly recovering M5-107.

This consistency check confirms that no extra critical resource has been introduced.

---

## 9. Recurrent-return form

Suppose `h_n` is a return sequence with

\[
S_{h_n}V\to V.
\]

Continuity of `mathcal K` yields

\[
\mathcal K(S_{h_n}V)-\mathcal K(V)\to0.
\]

Therefore

\[
\boxed{
\int_0^{h_n}X_3(S_sV)ds
=
\frac13
\int_{-h_n/2}^0
\mathfrak c_\rho(T_V)d\rho
+o(1).
}
\]

For a generic state in a positive-residue ergodic component, the right-hand side grows like

\[
\frac{h_n}{6}\mathscr R_3.
\]

Thus the long-time critical pressure overpay is exactly the amount of backward cubic genealogy stored in the corresponding logarithmic tail window, up to a bounded state coboundary.

---

## 10. DSD four-chain audit

### Formation — GREEN

`mathcal K` is formed only after subtracting the already constructed canonical tail.  The divergent critical tail and finite strong-critical quotient are not conflated.

### Axis — GREEN

Leray time length `h` maps to log-radius genealogy length `h/2` exactly.

### Static aggregation — GREEN

The `R3` mean appearing in the shifted tail and the Leray dilation term cancel; they are not counted as two costs.

### Dynamics — GREEN

The finite-time identity precedes recurrence.  Recurrence is used only afterward to make the bounded coboundary small on return times.

### Cross-audit — GREEN

The identity recovers the previously proved invariant mean instead of using that mean to justify itself.

---

## 11. What this closes

The old statement

\[
\text{core payer and tail memory are merely correlated in invariant average}
\]

is replaced by the stronger same-trajectory identity

\[
\boxed{
\text{integrated critical core overpay}
=
\text{bounded cubic coboundary}
+
\text{actual finite backward tail-memory window}.
}
\]

This is the first exact dynamic bridge between the recurrent finite core and the canonical critical tail.

---

## 12. What remains open

The cocycle itself is not a contradiction.  A positive translation density can support a linearly growing cocycle on an infinite Leray-time orbit.

The next target is to combine M5-108's pointwise residual inequality

\[
\mathcal E_3\ge2\nu X_3
\]

with the present finite-time cocycle, and then determine whether the resulting pressure-strain residual action is itself a tail-factor cocycle or necessarily contains a nontrivial strong-critical fiber-production term.

That is the next `P0/P1` split from M5-119 in a dynamic, rather than purely conditional, form.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
