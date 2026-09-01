# DSD M5-482 — Bounded critical Dirichlet tail generates a complete dilation genealogy

Date: 2026-09-01

Status: **TERMINAL-TAIL COMPACTIFICATION / IF THE M5-481 CRITICAL DIRICHLET TAIL AVOIDS UNBOUNDED TERMINAL `L3` AMPLITUDE AND UNBOUNDED CRITICAL DIRICHLET FREQUENCY, THE RECORD-SCALE TERMINAL BLOW-DOWNS ARE PRECOMPACT ON EVERY PUNCTURED ANNULUS / THE EXACT IDENTITY `U_(m+1)=D_(lambda_m) U_m` PASSES TO A COMPLETE DISCRETE DILATION GENEALOGY WITH STEP FACTORS BOUNDED AWAY FROM ONE AND INFINITY / THE DIRICHLET LOWER MARK MAKES THE HULL NONCONSTANT / THIS IS THE TERMINAL LOG-SCALE HARD OBJECT; IT MAY BE PERIODIC/DSS OR APERIODIC AND IS NOT YET EXCLUDED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Record-scale terminal states

Let `R_m -> infinity` be the M5-478 backward-record radii and define

\[
\boxed{
U_m(y):=R_mV(R_my,0).
}
\]

For every fixed punctured annulus

\[
A_{a,b}=\{a<|y|<b\},
\]

assume the bounded terminal-tail lane:

\[
\boxed{
\sup_m\|U_m\|_{L^3(A_{a,b})}<\infty,
}
\]

\[
\boxed{
\sup_m\|\nabla U_m\|_{L^2(A_{a,b})}<\infty.
}
\]

If either bound fails, the sequence is already in a genuine strong terminal amplitude/frequency branch.

M5-481 gives on at least one annulus a positive lower Dirichlet mark:

\[
\boxed{
\limsup_m
\|\nabla U_m\|_{L^2(A_{a_0,b_0})}
\ge g_0>0.
}
\]

---

## 2. Local H1 compactness modulo no extra Galilean choice

On a fixed annulus, Poincare gives

\[
\|U_m-(U_m)_A\|_{L^6(A)}
\le C_A\|\nabla U_m\|_2.
\]

The `L3` bound controls the mean:

\[
|(U_m)_A|
\le |A|^{-1/3}\|U_m\|_{L^3(A)}.
\]

Hence

\[
\boxed{
\sup_m\|U_m\|_{H^1(A)}<\infty
}
\]

for each fixed annulus.

By Rellich,

\[
U_m\to T
\]

strongly in `Lp(A)` for every `p<6` and weakly in `H1(A)` along a subsequence.

Using a diagonal sequence over rational annuli produces a divergence-free terminal tail state

\[
\boxed{
T\in H^1_{loc}(\mathbb R^3\setminus\{0\})
}
\]

with local `L3` control.

The lower Dirichlet mark can be preserved by choosing the subsequence on which the limsup is realized, so the resulting hull contains a nonconstant state.

---

## 3. Consecutive record-scale ratios

Let the backward first-hitting times be

\[
T_m=R_m^2\asymp q^m.
\]

The inherited first-hitting stage lengths satisfy

\[
0<L_-\le L_j\le L_+<\infty.
\]

Since the newly added oldest stage has duration comparable to `q^(m+1)` while the previous accumulated backward time is comparable to `q^m`, there exist constants

\[
1<\Lambda_-\le\Lambda_+<\infty
\]

such that

\[
\boxed{
\Lambda_-
\le
\frac{T_{m+1}}{T_m}
\le
\Lambda_+.
}
\]

Therefore the spatial record ratio

\[
\boxed{
\lambda_m:=\frac{R_{m+1}}{R_m}
}
\]

satisfies

\[
\boxed{
1<\lambda_-\le\lambda_m\le\lambda_+<\infty.
}
\]

---

## 4. Exact dilation genealogy before taking limits

Define the Navier--Stokes critical dilation operator

\[
\boxed{
(D_\lambda f)(y)
:=\lambda f(\lambda y).
}
\]

Then exactly

\[
\begin{aligned}
D_{\lambda_m}U_m(y)
&=
\lambda_mR_mV(R_m\lambda_my,0)\\
&=R_{m+1}V(R_{m+1}y,0)\\
&=U_{m+1}(y).
\end{aligned}
\]

Thus

\[
\boxed{
U_{m+1}=D_{\lambda_m}U_m.
}
\]

This is an exact identity, not an asymptotic ansatz.

---

## 5. Extract a complete discrete dilation orbit

Choose integers `m_k -> infinity`.

By compactness, for every fixed integer offset `n` and every fixed punctured annulus, extract diagonally so that

\[
U_{m_k+n}\to T_n
\]

locally strongly in `Lp`, `p<6`, and weakly in `H1`.

Since the step factors lie in a compact interval, also arrange

\[
\lambda_{m_k+n}\to\lambda_n
\in[\lambda_-,\lambda_+].
\]

Continuity of dilation on fixed annular Sobolev classes gives

\[
\boxed{
T_{n+1}=D_{\lambda_n}T_n,
\qquad n\in\mathbb Z.
}
\]

This is a complete two-sided discrete log-scale genealogy.

---

## 6. The genealogy is nontrivial

Choose the original subsequence so that the M5-481 Dirichlet lower mark is realized at offset zero:

\[
\|\nabla U_{m_k}\|_{L^2(A_{a_0,b_0})}
\ge g_0/2.
\]

Weak `H1` convergence alone gives only lower semicontinuity in the wrong direction for preserving a lower norm. To avoid an unjustified claim, use the following exact split:

1. if the gradient energy loses a fixed amount in the limit, that loss is a **scale-frequency compactness defect**, returned to the strong terminal-frequency branch;
2. on the no-defect compact lane, local `H1` convergence is strong and
   \[
   \boxed{
   \|\nabla T_0\|_{L^2(A_{a_0,b_0})}
   \ge g_0/2.
   }
   \]

Thus the genuinely compact dilation hull contains a nonconstant state.

---

## 7. Periodic and aperiodic realizations

If there exist `N>=1` and a product

\[
\Lambda
:=\prod_{n=0}^{N-1}\lambda_n>1
\]

such that

\[
T_N=T_0,
\]

then

\[
\boxed{
T_0=D_\Lambda T_0,
}
\]

so the terminal tail is discretely self-similar in space.

If no such return occurs, the closure of the genealogy in the local punctured topology may support an aperiodic compact dilation hull.

Compactness alone does not exclude the second possibility.

Thus the bounded terminal tail has the exact qualitative alternatives

\[
\boxed{
T_{DSS}^{terminal}
\lor
T_{aper}^{terminal}.
}
\]

---

## 8. Relation to the earlier W1 tail program

The older W1 analysis began with a global weak-critical orbit and constructed a canonical passive `1/r`-type tail.

M5-482 reaches a related log-scale object from a different direction:

\[
\text{first-hitting ratchet}
\to
\text{finite-enstrophy ancient element}
\to
\text{backward record blow-down}
\to
\text{forced terminal Dirichlet tail}
\to
\text{dilation genealogy}.
\]

Thus the W1 tail architecture is not being assumed; a terminal dilation structure is independently re-derived from the bounded ratchet corridor.

---

## 9. Firewall

The terminal tail states `T_n` are time-slice objects. M5-482 does not claim that they individually solve the stationary Navier--Stokes equations.

The relation

\[
T_{n+1}=D_{\lambda_n}T_n
\]

is a spatial dilation genealogy, not a time evolution equation.

To obtain further rigidity one must use the M5-478 ancient tail cells that connect these terminal states to coherent Navier--Stokes time evolution.

---

## 10. Updated bounded-ratchet frontier

Outside strong terminal amplitude/frequency and terminal suitable defects,

\[
\boxed{
E_{ratchet}^{ancient}
\Longrightarrow
\mathcal H_{dil}^{terminal},
}
\]

where `H_dil^terminal` is a nonconstant compact complete dilation genealogy on punctured space.

---

## 11. Highest-value next target

Lift the discrete terminal genealogy to the corresponding M5-478 space-time tail cells and determine whether the complete dilation hull is

1. dynamically coherent under Navier--Stokes;
2. forced to be DSS/periodic;
3. or capable of carrying a genuinely aperiodic ancient dilation dynamics.

A rigidity theorem at this lifted level would attack both periodic and aperiodic terminal tails simultaneously.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
