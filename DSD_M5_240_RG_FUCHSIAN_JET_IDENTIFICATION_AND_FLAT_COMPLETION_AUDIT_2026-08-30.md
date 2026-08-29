# DSD M5-240 — RG/Fuchsian Jet Identification and Flat-Completion Audit

Date: 2026-08-30

Parent: `DSD_M5_239_RG_RECONSTRUCTION_COVARIANCE_AND_TAIL_INVERSE_SEMIDIRECT_STRUCTURE_2026-08-30.md`

Status: **STRUCTURAL UNIFICATION / THE `rho=e^{-h}=R^{-2}` RG EXPANSION OBEYS A TRIANGULAR RECURSION IDENTICAL IN ORDER STRUCTURE TO THE PREVIOUS INTEGER FUCHSIAN DESCENDANT HIERARCHY / THE CANONICAL TAIL FIXES EVERY FINITE RG JET / M5-217 REMOVES SAME-TAIL FLAT NONUNIQUENESS INSIDE THE REALIZED W1 CLASS / THIS GIVES PDE-QUASIANALYTIC UNIQUENESS OF THE REALIZED COMPLETION WITHOUT ASSERTING CONVERGENCE OF THE FORMAL RG TAYLOR SERIES / GLOBAL REGULARITY UNPROVED.**

---

## 1. RG variable and the old Fuchsian variable

M5-237 introduces

\[
\rho=e^{-h}=R^{-2}.
\]

The earlier physical/Fuchsian analysis uses the dimensionless parabolic ratio

\[
z\sim \frac{T_*-t}{|x-x_*|^2}.
\]

On a descendant observation at normalized radius `R`, these are the same scale order:

\[
\boxed{
\rho\sim z\sim R^{-2}.
}
\]

Thus the RG boundary `rho=0` and the Fuchsian boundary `z=0` are two descriptions of the same scale-infinity/terminal-puncture limit.

---

## 2. Bilinear stationary operator

Write

\[
\mathcal F(U)
=\nu\Delta U-\mathcal B(U,U),
\]

where

\[
\mathcal B(U,V)
:=
\mathbb P\nabla\cdot(U\otimes V)
\]

is bilinear.

The RG reconstruction equation is

\[
\boxed{
\partial_\rho\mathscr R
=-\nu\Delta\mathscr R
+\mathcal B(\mathscr R,\mathscr R).
}
\]

---

## 3. Formal RG series

Write formally

\[
\boxed{
\mathscr R_\rho(T)
=\sum_{n=0}^\infty\rho^nA_n,
\qquad
A_0=T.
}
\]

Then

\[
\partial_\rho\mathscr R
=
\sum_{n=0}^\infty(n+1)\rho^nA_{n+1}.
\]

The right-hand side is

\[
-\nu\sum_{n\ge0}\rho^n\Delta A_n
+
\sum_{n\ge0}\rho^n
\sum_{i+j=n}\mathcal B(A_i,A_j).
\]

Therefore each coefficient satisfies the exact triangular recursion

\[
\boxed{
(n+1)A_{n+1}
=
-\nu\Delta A_n
+
\sum_{i+j=n}\mathcal B(A_i,A_j).
}
\]

The right side contains only coefficients of order at most `n`.

There is no positive-order resonance in the velocity coefficient because the divisor `n+1` never vanishes.

---

## 4. First coefficients

For `n=0`,

\[
A_1
=
-\nu\Delta T
+\mathcal B(T,T)
=-\mathcal F(T).
\]

Thus

\[
\boxed{A_1=-F_T.}
\]

This reproduces M5-237:

\[
\mathscr R_\rho
=T-\rho F_T+o(\rho).
\]

For `n=1`,

\[
2A_2
=
-\nu\Delta A_1
+\mathcal B(T,A_1)
+\mathcal B(A_1,T).
\]

Since `A1=-F_T`,

\[
\boxed{
A_2
=\frac12D\mathcal F_T[F_T].
}
\]

The same pattern continues recursively.

---

## 5. Match to the previous Fuchsian hierarchy

M5-135--145 derived, in the integer terminal/Fuchsian sector, triangular relations of the form

\[
\boxed{
 nH_n
=\mathcal F_{n-1}
(H_0,\ldots,H_{n-1},\Pi_{n-1}).
}
\]

Pressure at each order is solved from an elliptic equation whose realized resonance coefficients are fixed on the minimal tail fiber, and then the next velocity coefficient is divided by the nonzero integer order.

The RG recursion has exactly the same architecture:

\[
\boxed{
\text{known lower coefficients}
\to
\text{stationary NS source at current order}
\to
\text{pressure/Leray resolution}
\to
\text{divide by positive integer}
\to
\text{next coefficient}.
}
\]

Thus the earlier Fuchsian descendant hierarchy is not a separate algebraic artifact. It is the coefficient expansion of the exact RG reconstruction equation.

---

## 6. Every finite realized jet is fixed by the tail

M5-145 proved for two states in one canonical-tail fiber that every finite integer Fuchsian coefficient agrees.

M5-217 subsequently proved the tail fiber is actually a singleton.

Therefore, on the realized W1 class,

\[
\boxed{
T
\Longrightarrow
A_1,A_2,\ldots,A_N
\quad\text{uniquely for every finite }N.
}
\]

There is no hidden finite-order RG branch.

---

## 7. Flat completion and M5-217

A formal all-order equality does not imply series convergence.

One may have a schematic flat remainder such as

\[
e^{-1/\rho}
\]

which has zero Taylor coefficients at `rho=0`.

Therefore the implication

\[
\text{all RG jets fixed}
\Rightarrow
\text{convergent RG series}
\]

is RED.

However M5-217 supplies a different statement: **two realized W1 reconstructions with the same tail cannot differ by such a flat mode.**

Thus within the realized PDE class,

\[
\boxed{
\text{same tail}
+\text{same all-order RG jet}
\Longrightarrow
\text{same reconstructed W1 state}.
}
\]

This is a PDE unique-completion statement, not a Taylor-convergence statement.

---

## 8. PDE-quasianalyticity versus analytic series

It is useful to separate two notions.

### Analytic RG reconstruction

This would require bounds such as

\[
\|A_n\|_X
\le CR^n
\]

on a suitable punctured function space, giving an actually convergent Taylor series in `rho`.

This has **not** been proved.

### Realized PDE-quasianalyticity

M5-145 + M5-217 give:

\[
\boxed{
\text{no nonzero realized same-tail difference can be flat to every algebraic RG order}.
}
\]

This weaker notion is already available and is enough for injectivity.

The two statements must not be conflated.

---

## 9. Consequence for the residual-active branch

On the `R-gap` branch of M5-238,

\[
\mathbf F(T)\ge\varepsilon_{glob}>0.
\]

Hence

\[
A_1=-F_T
\]

is uniformly nontrivial in the global residual metric.

All higher coefficients are then recursively slaved to `T` and `F_T`.

Thus a residual-active minimal tail does not carry a free sequence of descendant corrections:

\[
\boxed{
T
\to
A_1
\to
A_2
\to\cdots
}
\]

is fixed at every finite order.

The only remaining issue is **existence/realizability** of the unique full completion, not coefficient selection.

---

## 10. DSD verdict

### CLOSED

- finite-order RG ambiguity;
- interpretation gap between Fuchsian descendants and RG corrections;
- same-tail flat branching inside the realized class.

### OPEN

- convergence/Gevrey growth of the RG series;
- characterization of tails for which the unique formal hierarchy has an actual W1 realization;
- exclusion of compact aperiodic minimal tails inside that realized range.

### UPDATED RESIDUAL-ACTIVE ENDPOINT

\[
\boxed{
\text{compact aperiodic minimal }T
+
\mathbf F(T)\ge\varepsilon_{glob}
+
\text{unique all-order RG hierarchy}
+
\text{one realized backward-RG completion}.
}
\]

This is considerably narrower than the original generic residual-forcing branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]