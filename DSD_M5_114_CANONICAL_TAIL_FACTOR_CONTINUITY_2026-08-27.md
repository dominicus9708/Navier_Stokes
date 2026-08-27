# DSD M5-114 — Canonical Tail Factor Continuity

Date: 2026-08-27

Status: **W1-CONDITIONAL TAIL COMPACTIFICATION / THE CANONICAL PASSIVE TAIL MAP V -> T_V IS CONTINUOUS FROM THE COMPACT MINIMAL W1 SET INTO LOCAL L3 ON THE PUNCTURED SPACE / EXACT COVARIANCE MAKES ITS COMPACT IMAGE A GENUINE DYNAMICAL FACTOR / THE M5-113 MOVING-RADIUS DIAGONAL PROBLEM IS THEREFORE CLOSED AT THE TAIL-FACTOR LEVEL, BUT INJECTIVITY OF THE FACTOR IS NOT CLAIMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Existing inputs

Let `M` be the compact minimal W1 set and `S(tau)` its Leray flow.

For every `V in M`, the canonical tail constructed previously is

\[
T_V(Y)=\lim_{h\to\infty}e^{h/2}(S(h)V)(e^{h/2}Y)
\]

on compact subsets of `R^3\{0}`.

The tail has exact covariance

\[
\boxed{
T_{S(\tau)V}(Y)
=e^{-\tau/2}T_V(e^{-\tau/2}Y).
}
\]

On every sufficiently remote annulus

\[
A_R=\{R<|Y|<2R\}
\]

we have the uniform approximation

\[
\boxed{
\|V-T_V\|_{L^3(A_R)}\le C R^{-1/2}
}
\]

with one constant on the compact W1 class.

---

## 2. Goal

Take a sequence

\[
V_n\to V
\]

in the retained W1 topology.

We prove for every fixed compact annulus

\[
K=\{r_0<|Y|<2r_0\},\qquad r_0>0,
\]

that

\[
\boxed{
T_{V_n}\to T_V
\quad\text{in }L^3(K).
}
\]

No moving-radius convergence of `V_n` is assumed.

---

## 3. Move the observation by the exact factor covariance

Fix `tau>0` and put

\[
R_\tau=e^{\tau/2}r_0.
\]

From covariance,

\[
T_V(Y)
=e^{\tau/2}T_{S(\tau)V}(e^{\tau/2}Y).
\]

Since `L^3` is exactly invariant under this critical scaling,

\[
\boxed{
\|T_{V_n}-T_V\|_{L^3(K)}
=
\|T_{S(\tau)V_n}-T_{S(\tau)V}\|_{L^3(A_{R_\tau})}.
}
\]

Thus a fixed inner tail comparison is converted into a remote-tail comparison **after** applying a fixed finite flow time.

---

## 4. Insert the actual W1 states only at fixed radius

By the uniform remote-tail estimate,

\[
\begin{aligned}
&\|T_{S(\tau)V_n}-T_{S(\tau)V}\|_{L^3(A_{R_\tau})}\\
&\le
\|T_{S(\tau)V_n}-S(\tau)V_n\|_{L^3(A_{R_\tau})}
+
\|S(\tau)V_n-S(\tau)V\|_{L^3(A_{R_\tau})}\\
&\qquad+
\|S(\tau)V-T_{S(\tau)V}\|_{L^3(A_{R_\tau})}\\
&\le
2C R_\tau^{-1/2}
+
\|S(\tau)V_n-S(\tau)V\|_{L^3(A_{R_\tau})}.
\end{aligned}
\]

For this step `tau` is fixed. Hence `A_{R_tau}` is one fixed finite annulus.

Continuity of the W1 flow and local smooth convergence imply

\[
\|S(\tau)V_n-S(\tau)V\|_{L^3(A_{R_\tau})}
\to0
\]

as `n->infinity`.

Therefore

\[
\limsup_{n\to\infty}
\|T_{V_n}-T_V\|_{L^3(K)}
\le
2C r_0^{-1/2}e^{-\tau/4}.
\]

Now let

\[
\tau\to\infty.
\]

The right-hand side tends to zero, proving

\[
\boxed{
T_{V_n}\to T_V
\text{ in }L^3(K).
}
\]

The order of limits is essential:

1. fix `tau`;
2. take `n->infinity` on one fixed annulus;
3. only then send `tau->infinity`.

This avoids the M5-113 moving-radius diagonal shortcut.

---

## 5. Local punctured topology

Choose a countable annular exhaustion of the punctured space, for example

\[
K_m=\{2^{-m}<|Y|<2^m\},\qquad m\ge1.
\]

Define

\[
\boxed{
 d_{tail}(T_1,T_2)
 =
 \sum_{m=1}^\infty
 2^{-m}
 \min\left(1,\|T_1-T_2\|_{L^3(K_m)}\right).
}
\]

Then `d_tail` metrizes local `L^3` convergence on `R^3\{0}`.

The preceding argument gives

\[
\boxed{
\mathfrak T:M\to\mathcal X_{tail},
\qquad
\mathfrak T(V):=T_V,
}
\]

as a continuous map.

Since `M` is compact, the image

\[
\boxed{
\mathcal T:=\mathfrak T(M)
}
\]

is compact in `X_tail`.

---

## 6. Exact factor dynamics

Define the dilation flow on tails by

\[
\boxed{
(D_\tau T)(Y)
:=e^{-\tau/2}T(e^{-\tau/2}Y).
}
\]

Canonical covariance becomes

\[
\boxed{
\mathfrak T(S(\tau)V)
=D_\tau\mathfrak T(V).
}
\]

Thus

\[
\boxed{
(M,S)
\xrightarrow{\ \mathfrak T\ }
(\mathcal T,D)
}
\]

is a genuine continuous dynamical factor.

This is the rigorous `tail compactification/factor` that was missing in M5-113.

---

## 7. What is and is not recovered

### Proved

The full canonical tail field is a continuous factor of the W1 minimal dynamics.

Moving-radius shell sequences may now be interpreted through this already-defined compact tail space instead of through a fictional pointwise `O_infinity`.

### Not proved

The map

\[
\mathfrak T:M\to\mathcal T
\]

need not be injective.

The passive tail satisfies only the dilation transport law plus divergence-free constraints. No spatial elliptic/analytic equation for `T_V` has been proved that would allow unique continuation from one tail annulus to the full W1 state.

Therefore

\[
T_V=T_W
\]

does **not** presently imply

\[
V=W.
\]

---

## 8. Fiber formation

Define the tail equivalence relation

\[
\boxed{
V\sim_T W
\iff
T_V=T_W.
}
\]

Continuity makes each fiber

\[
\mathfrak T^{-1}(T)
\]

compact.

Covariance makes the relation dynamically compatible:

\[
V\sim_TW
\Longrightarrow
S(\tau)V\sim_T S(\tau)W.
\]

Thus noninjectivity, if present, is an honest **internal fiber dynamics over one passive critical tail**, not an ill-defined moving-radius limit.

---

## 9. DSD four-chain audit

### Formation

The tail field `T_V` exists before the factor space is defined.

### Axis

Core state, tail state, and finite-radius shell observation remain distinct objects.

### Static aggregation

The tail approximation error is used exactly twice in the triangle inequality and is not counted later as a new cost.

### Dynamics

Covariance is used to move a fixed comparison to a remote annulus only after a finite flow time has been fixed.

### Cross-audit RED firewall

We do not use

\[
V_n\to V,\ R_n\to\infty
\]

to infer convergence on `A_{R_n}`.

Instead every `n->infinity` passage occurs at a fixed finite annulus.

---

## 10. Updated frontier

M5-113's diagonal problem is now resolved at the correct level:

\[
\boxed{
\text{W1 minimal dynamics}
\to
\text{compact canonical-tail factor}
}
\]

is rigorous.

The next split is exact:

1. **tail factor injective:** the passive tail is a complete topological code of the W1 state;
2. **tail factor noninjective:** distinct W1 states live in a compact invariant fiber above the same tail.

The next calculation should analyze the noninjective fiber using the already proved fact that differences from the common tail are in `L^2 cap L^3`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
