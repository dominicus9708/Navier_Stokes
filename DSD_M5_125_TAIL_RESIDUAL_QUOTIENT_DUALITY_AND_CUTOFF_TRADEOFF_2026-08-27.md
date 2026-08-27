# DSD M5-125 — Tail-Residual / Quotient Duality and the Cutoff Tradeoff

Date: 2026-08-27

Status: **CANONICAL-TAIL RESIDUAL PAIRED WITH THE STRONG QUOTIENT IS SPATIALLY SUMMABLE AND VANISHES AS THE TAIL CUTOFF IS MOVED OUTWARD / HOWEVER THE QUOTIENT `L2` SIZE GROWS WITH THE SAME CUTOFF BECAUSE MORE CRITICAL TAIL IS RECLASSIFIED AS QUOTIENT / THE NEAR-UNFORCED-QUOTIENT SHORTCUT IS THEREFORE INVALID / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Fix a large cutoff radius `R0` in the canonical construction of M5-170/M5-117.

Let

\[
B_{R_0}
\]

be the divergence-free cutoff canonical tail, equal to zero inside `R0` and equal to `T` outside `2R0`, and define

\[
\boxed{
Q_{R_0}:=V-B_{R_0}.
}
\]

Then

\[
Q_{R_0}\in L^2\cap L^3.
\]

Its forced Leray equation contains

- the exterior canonical-tail residual `F_T`;
- transition-annulus cutoff/Bogovskii forcing;
- cross coupling with `B_R0`.

The question is whether these terms provide a new scale-critical non-summable resource.

---

## 2. Exterior residual / quotient pairing on one shell

For a dyadic shell

\[
A_R=\{R<|Y|<2R\},
\qquad R\ge2R_0,
\]

we have

\[
Q_{R_0}=V-T.
\]

Define scaled fields on the unit annulus

\[
\widehat F_R(z):=R^3F_T(Rz),
\qquad
\widehat Q_R(z):=RQ_{R_0}(Rz).
\]

The canonical-tail residual estimate gives

\[
\boxed{
\|\widehat F_R\|_{H^{-1}(A)}\le C.
}
\]

The W1 shell bounds give uniform scaled `H1` bounds for both `V` and `T`, hence

\[
\boxed{
\|\widehat Q_R\|_{H^1(A)}\le C.
}
\]

Changing variables,

\[
\begin{aligned}
\left|
\int_{A_R}F_T\cdot Q_{R_0}dY
\right|
&=
R^{-1}
\left|
\langle\widehat F_R,\widehat Q_R\rangle
\right|\\
&\le CR^{-1}.
\end{aligned}
\]

Therefore

\[
\boxed{
\left|
\int_{A_R}F_T\cdot Q_{R_0}dY
\right|
\le CR^{-1}.
}
\]

---

## 3. Dyadic summation

Sum over

\[
R=2^kR_0,
\qquad k\ge1.
\]

Then

\[
\sum_{k\ge1}(2^kR_0)^{-1}
\lesssim R_0^{-1}.
\]

Thus the whole exterior tail residual satisfies

\[
\boxed{
\left|
\langle F_T,Q_{R_0}\rangle_{|Y|>2R_0}
\right|
\le CR_0^{-1}.
}
\]

The exterior canonical residual is therefore spatially **subcritical when paired against the strong quotient**.

It cannot produce one order-one independent payment per logarithmic shell.

---

## 4. Transition-annulus forcing

On the transition annulus

\[
R_0<|Y|<2R_0,
\]

the tail and cutoff/Bogovskii fields have the natural critical sizes

\[
|B_{R_0}|\lesssim R_0^{-1},
\qquad
|\nabla B_{R_0}|\lesssim R_0^{-2},
\]

and the induced forcing has size

\[
|\mathcal F_{trans}|\sim R_0^{-3}
\]

in the scale-invariant fixed-annulus distributional norm.

The scaled quotient

\[
R_0Q_{R_0}(R_0\cdot)
\]

has a uniform `H1` bound.

Therefore the same dual scaling gives

\[
\boxed{
|\langle\mathcal F_{trans},Q_{R_0}\rangle|
\le CR_0^{-1}.
}
\]

Bogovskii correction terms have the same scaling because the correction is formed on one fixed-shape annulus after rescaling.

---

## 5. Cross-strain term

The quotient energy ledger contains

\[
\int Q_{R_0}^TS_{B_{R_0}}Q_{R_0}dY.
\]

On exterior dyadic shells,

\[
|S_T|\lesssim R^{-2}
\]

and the canonical quotient estimate gives

\[
\|Q_{R_0}\|_{L^2(A_R)}^2\lesssim R^{-1}.
\]

Hence

\[
\left|
\int_{A_R}Q^TS_TQdY
\right|
\lesssim R^{-3},
\]

which is dyadically summable.

The transition annulus gives the larger but still vanishing estimate

\[
\boxed{
\left|
\int Q^TS_BQdY
\right|
\lesssim R_0^{-1}.
}
\]

Thus every explicit tail/quotient interaction in the `L2` energy ledger can be made small by moving the decomposition radius outward.

---

## 6. Why this does not make the quotient uniformly near-unforced

The same change of cutoff changes the quotient itself.

Inside `R0`,

\[
B_{R_0}=0,
\qquad
Q_{R_0}=V.
\]

A critical `1/r` tail contributes ordinary `L2` mass proportional to radius:

\[
\int_{1<|Y|<R_0}|V|^2dY
\sim O(R_0)
\]

whenever the tail density is nontrivial.

Thus in general

\[
\boxed{
\|Q_{R_0}\|_2^2
\sim O(R_0)
}
\]

rather than remaining uniformly bounded as `R0 to infinity`.

The quotient energy ledger contains the Leray drift term

\[
-\frac14\|Q_{R_0}\|_2^2,
\]

whose scale therefore grows with `R0`.

Hence

\[
\boxed{
\text{tail forcing}\to0
\quad\text{but}\quad
\text{quotient state size}\to\infty.
}
\]

One cannot pass to an unforced finite-energy limit by sending the cutoff to infinity.

---

## 7. DSD interpretation

Moving `R0` is not deleting the tail.

It merely reclassifies more of the same formed critical field from the `tail` channel into the `quotient` channel.

Static aggregation therefore obeys the conservation-of-description rule:

\[
\boxed{
\text{smaller coupling}
\Longleftrightarrow
\text{larger quotient reservoir}.
}
\]

Treating only the vanishing coupling and ignoring the growing quotient would be a DSD channel-loss error.

---

## 8. Permanent RED route

The following shortcut is closed:

\[
\boxed{
R_0\to\infty
\Longrightarrow
\text{canonical quotient becomes an unforced uniformly finite-energy recurrent NSE state}.
}
\]

The premise fails because the quotient `L2` norm is not uniform in the cutoff.

Likewise the summability of

\[
\langle F_T,Q\rangle
\]

does not provide a finite budget for the separate critical cubic anomaly.

---

## 9. What remains useful

The result does establish one important negative fact:

\[
\boxed{
\text{the exterior residual/quotient duality is not the missing nonsummable critical payer.}
}
\]

Therefore the anomaly cannot be closed by summing canonical-tail forcing work over shells.

The viable information remains:

- the tail-factor cubic cocycle from M5-118--122;
- the finite-core pressure/strain residual;
- the strong-critical fiber dynamics;
- and the prelimit/scale-infinity realization problem.

---

## 10. New frontier

The next audit should return to the original finite-energy prelimit interface.

Unlike the internal W1 tail/quotient split, the original solution possesses one genuinely fixed global `L2` budget.  The question is whether the log-cylinder genealogy can be transferred to **growing but still shrinking-physical-radius windows** strongly enough to combine critical cubic depth with that fixed physical-energy structure.

A first target is a diagonal expanding-window lemma with

\[
R_n\to\infty,
\qquad
\sqrt{T-t_n}\,R_n\to0,
\]

on which the original normalized prelimit still converges to the W1 state.

This weaker interface is available from local compactness by diagonalization and should be audited before asking for the much stronger fixed-physical-radius EWG.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
