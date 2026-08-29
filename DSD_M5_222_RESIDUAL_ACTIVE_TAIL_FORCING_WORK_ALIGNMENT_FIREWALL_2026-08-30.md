# DSD M5-222 — Residual-Active Tail Forcing / Work-Alignment Firewall

Date: 2026-08-30

Parent: `DSD_M5_220_TAIL_HOMOGENEITY_DEFECT_TO_RESIDUAL_OR_STATIONARY_CRITICAL_PROFILE_FORK_2026-08-30.md`

Status: **RESIDUAL-WORK AUDIT / THE FINITE-ENERGY QUOTIENT HAS AN EXACT FORCED RELATIVE-ENERGY IDENTITY, BUT A POSITIVE H^-1 NORM OF THE CRITICAL TAIL RESIDUAL DOES NOT FORCE POSITIVE ENERGY WORK / A LINEAR RECURRENT FORCED PARABOLIC ANTI-MODEL SHOWS THAT ORDER-ONE RECURRENT FORCING CAN SUSTAIN A BOUNDED RECURRENT RESPONSE WITHOUT VIOLATING A FINITE ENERGY LEDGER / THE RESIDUAL-ACTIVE BRANCH THEREFORE REQUIRES RESPONSE ALIGNMENT OR A NONCRITICAL GAIN, NOT JUST FORCING SIZE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Quotient setup

Choose a fixed large cutoff radius `R0` and construct the divergence-free canonical-tail background

\[
B_T
\]

as in the general W1 tail theorem.

For a W1 state

\[
V=B_T+Q,
\]

the quotient satisfies

\[
\boxed{
Q\in L^2(\mathbb R^3)\cap L^3(\mathbb R^3),
\qquad
\nabla\cdot Q=0.
}
\]

Its Leray equation has the form

\[
\boxed{
\mathcal LQ
+
\mathbb P\nabla\cdot
\left(
Q\otimes Q
+B_T\otimes Q
+Q\otimes B_T
\right)
=
\mathcal F_{B_T},
}
\]

where

\[
\mathcal L
=
\partial_s-\nu\Delta
+\frac12+rac12Y\cdot\nabla.
\]

Outside the cutoff transition region,

\[
\mathcal F_{B_T}=F_T
\]

with

\[
F_T
=
\nu\Delta T
-
\mathbb P\nabla\cdot(T\otimes T).
\]

---

## 2. Exact quotient L2 energy identity

Pair the quotient equation with `Q` in `L2`.

The pure quotient transport vanishes:

\[
\int Q\cdot(Q\cdot\nabla Q)=0.
\]

The background transport also vanishes because `div B_T=0`:

\[
\int Q\cdot(B_T\cdot\nabla Q)=0.
\]

The remaining mixed term is the background strain form:

\[
\int Q\cdot(Q\cdot\nabla B_T)
=
\int Q^TS_{B_T}Q.
\]

The Leray linear terms give

\[
\int Q\cdot
\left(
\frac12Q+rac12Y\cdot\nabla Q
\right)
=
-\frac14\|Q\|_2^2.
\]

Therefore

\[
\boxed{
\frac12\frac d{ds}\|Q\|_2^2
+
\nu\|\nabla Q\|_2^2
-
\frac14\|Q\|_2^2
+
\int Q^TS_{B_T}Q
=
\langle\mathcal F_{B_T},Q\rangle.
}
\]

The sign convention for `F` is fixed by the displayed quotient equation.

This is the exact forced energy ledger.

---

## 3. Recurrent time-average identity

On a compact recurrent quotient class, the `L2` energy is uniformly bounded.

Along a long-time sequence for which endpoint energy increments are negligible after division by length,

\[
\frac1S
\left[
\|Q(S)\|_2^2-
\|Q(0)\|_2^2
\right]
\to0.
\]

Hence the recurrent mean obeys

\[
\boxed{
\nu\langle\|\nabla Q\|_2^2\rangle
-
\frac14\langle\|Q\|_2^2\rangle
+
\left\langle
\int Q^TS_{B_T}Q
\right\rangle
=
\langle
\langle\mathcal F_{B_T},Q\rangle
\rangle.
}
\]

Thus a nonzero recurrent tail residual must be balanced by some combination of

- actual work on the quotient;
- the background critical strain form;
- the Leray scaling term;
- quotient Dirichlet dissipation.

No term is sign-free except the Dirichlet contribution.

---

## 4. Positive residual norm does not imply positive work

The residual-active branch from M5-220 supplies, on a positive-density family of cells/times,

\[
\boxed{
\|F_T\|_{H^{-1}(A)}
\ge\varepsilon_F>0.
}
\]

But duality gives only the upper estimate

\[
|\langle F_T,Q\rangle|
\le
\|F_T\|_{H^{-1}}
\|Q\|_{H^1_0(A)}.
\]

There is no reverse estimate of the form

\[
|\langle F_T,Q\rangle|
\ge
c\|F_T\|_{H^{-1}}^2
\]

without a response-alignment/coercivity theorem.

In particular `Q` may be nearly orthogonal, in the dual pairing, to the dominant residual direction.

Therefore

\[
\boxed{
\|F_T\|_{H^{-1}}\ge\varepsilon_F
\not\Rightarrow
\text{positive fixed energy-work payment}.
}
\]

---

## 5. Linear recurrent forcing anti-model

The failure is not specific to pressure or Navier--Stokes geometry.

Let `H` be a Hilbert space and let `A` be a positive self-adjoint operator with one normalized eigenvector `e`:

\[
Ae=\lambda e,
\qquad
\lambda>0.
\]

Consider

\[
\boxed{
q_s+Aq=f(s),
}
\]

with periodic forcing

\[
f(s)=\varepsilon
\left(
\cos s\,e_1+\sin s\,e_2
\right)
\]

in a two-dimensional eigenspace of `A`.

There is a unique bounded periodic response

\[
q_{per}(s)
\]

of size `O(epsilon)`.

The forcing norm satisfies

\[
\|f(s)\|=\varepsilon
\]

at every time, while the work

\[
\langle f,q_{per}\rangle
\]

oscillates and its sign/phase depends on the resolvent response.

The exact periodic energy identity balances forcing work and dissipation with no contradiction.

Hence

\[
\boxed{
\text{persistent nonzero forcing}
+
\text{bounded recurrent response}
}
\]

is entirely compatible with a dissipative parabolic system.

A Navier--Stokes contradiction must use additional structure of `F_T`, not generic parabolic dissipation.

---

## 6. Critical shell scaling makes the naive total-work sum even weaker

On a radius-`R` tail shell,

\[
F_T\sim R^{-3}
\]

in the critical distributional sense.

The shell `H^-1` norm scales as

\[
\boxed{
\|F_T\|_{H^{-1}(A_R)}
\lesssim R^{-1/2}.
}
\]

Indeed the normalized quantity

\[
R^3F_T(R\cdot)
\]

is bounded in fixed-cell `H^-1`, while an `H^1` test function rescales with the `R^{-1/2}` factor.

Thus on geometric shells `R_k=q^{k/2}` one has

\[
\sum_k
\|F_T\|_{H^{-1}(A_{R_k})}^2
\lesssim
\sum_kR_k^{-1}
<\infty.
\]

Therefore even a positive-density family of scale-critical residual cells can be globally square-summable in the natural exterior `H^-1` topology.

This is the forcing analogue of the previous critical energy-tail compatibility.

---

## 7. What would make the residual branch close

At least one genuinely stronger estimate is needed.

### Alignment/coercivity

A lower response estimate such as

\[
\boxed{
|\langle F_T,Q\rangle|
\ge
c_F\|F_T\|_{H^{-1}}^2
}
\]

on a positive-density set.

### Noncritical spatial gain

An improved shell estimate

\[
\boxed{
\|F_T\|_{H^{-1}(A_R)}
\gtrsim R^{-1/2+\delta}
}
\]

for some `delta>0` on a sufficiently rich shell family, so that the corresponding square sum loses critical summability.

### Derivative descent

A residual lower bound that forces an already finite-budget higher-derivative or turnover charge with a noncritical exponent.

None of these is presently proved in the generic residual-active branch.

---

## 8. Relation to tail injectivity

M5-217/M5-218 say that the tail uniquely determines the W1 state and quotient response.

Thus the recurrent response is not arbitrary: there is a single graph map

\[
T\mapsto Q_T.
\]

However topological uniqueness of this response does not imply energetic alignment:

\[
\boxed{
\text{unique response}
\not\Rightarrow
\langle F_T,Q_T\rangle
\text{ has a fixed sign or lower bound}.
}
\]

A quantitative differentiable/coercive property of the graph map would be needed.

---

## 9. DSD verdict

The residual-active branch is now typed as

\[
\boxed{
R_{tail}
=
\text{critical recurrent forcing with an unresolved response-alignment problem}.
}
\]

The forbidden shortcut is

\[
\boxed{
\text{forcing norm}
\Rightarrow
\text{energy work}
}
\]

without a dual-angle/coercivity lemma.

Thus M5-220's two endpoints remain honest:

\[
\boxed{
A_{min}^{aper}
\Longrightarrow
R_{tail}^{align/open}
\lor
S_{crit,large}^{nonhom}.
}
\]

---

## 10. Next useful calculation

The most promising residual-specific quantity is not `Q` itself but the **linearized response in the tail-translation direction**.

Because

\[
T_s=-\frac12\mathcal H_T,
\]

and the W1 state is uniquely coded by `T`, differentiating the tail-to-core graph formally would produce a tangent response

\[
\dot Q
=
D\mathcal Q_T[T_s].
\]

The next audit should determine whether this derivative exists on the compact smooth W1 class and whether the differentiated quotient equation yields a signed/coercive pairing with the residual derivative.

If differentiability fails, that failure itself becomes a quantitative instability branch rather than being hidden under topological injectivity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]