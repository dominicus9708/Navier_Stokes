# DSD M5-135 — Nonresonant Subleading Tail-Correction Re-Audit

Date: 2026-08-27

Status: **F-GATE PRUNING / THE CANONICAL `r^-1` TAIL IS THE UNIQUE NEUTRAL DILATION ORDER, WHILE EVERY SUBLEADING `r^{-(1+2n)}` CORRECTION HAS A NONZERO LERAY-DILATION EIGENVALUE `-n` / THE `r^-3` NAVIER–STOKES TAIL RESIDUAL CAN THEREFORE BE ABSORBED BY A STRONG SUBLEADING CORRECTION WITHOUT A SOLVABILITY CONDITION / THIS RECONNECTS THE CURRENT FACTOR ANALYSIS TO THE EARLIER TERMINAL-TAYLOR NONRESONANCE AUDIT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why this re-audit is necessary

M5-133 and M5-134 make the leading tail velocity and pressure factor-level data and define the leading NSE tail residual

\[
F_T=r^{-3}\mathfrak F(\eta,\theta),
\qquad
\eta:=\rho-\frac s2.
\]

A tempting F-gate closure is

\[
\mathfrak F\ne0
\Rightarrow
\text{canonical tail incompatible with NSE}.
\]

The repository's earlier punctured-terminal/Taylor audit already warned that this is generally false. The present note rewrites that fact in the current log-factor language.

---

## 2. Passive Leray operator

Let

\[
\mathcal L_0
:=
\partial_s
+\frac12
+\frac12Y\cdot\nabla.
\]

For a correction of homogeneous log form

\[
Q_n(Y,s)
=
r^{-(1+2n)}G_n(\eta,\theta),
\qquad n\ge0,
\]

we have

\[
\partial_sG_n(\eta)=-\frac12\partial_\eta G_n,
\qquad
Y\cdot\nabla Q_n
=
r^{-(1+2n)}
\left[-(1+2n)G_n+\partial_\eta G_n\right].
\]

Therefore the `eta` derivatives cancel and

\[
\boxed{
\mathcal L_0Q_n
=
-n\,r^{-(1+2n)}G_n.
}
\]

---

## 3. Unique neutral order

For `n=0`,

\[
Q_0=r^{-1}\Phi(\eta,\theta),
\qquad
\mathcal L_0Q_0=0.
\]

This is exactly the canonical passive tail / log-radius conveyor.

For every `n>=1`,

\[
\boxed{-n\ne0.}
\]

Thus every subleading odd critical-parabolic order is algebraically nonresonant with respect to the similarity drift.

---

## 4. First residual correction

The leading tail's viscous, nonlinear, and pressure residual is of order

\[
r^{-3}.
\]

At that same order choose

\[
Q_1=r^{-3}G_1(\eta,\theta).
\]

Since

\[
\mathcal L_0Q_1=-r^{-3}G_1,
\]

one can choose `G_1` equal to the required signed residual coefficient according to the chosen Leray-equation convention so that

\[
\boxed{
\mathcal L_0Q_1
+
(\text{leading tail NSE residual})
=0
}
\]

at order `r^-3`.

No Fredholm condition, mean-zero condition, or periodicity assumption is required.

---

## 5. Higher orders

After inserting `Q_1`, the remaining residual begins at the next lower order, schematically `r^-5`.

At order

\[
r^{-(1+2n)},
\qquad n\ge1,
\]

the coefficient equation has the structure

\[
\boxed{
-nG_n=H_n
}
\]

in the co-moving tail coordinate, where `H_n` is determined by lower-order profiles and their derivatives.

Thus

\[
\boxed{
G_n=-\frac1nH_n
}
\]

at every finite order.

This is the log-cylinder version of the earlier coefficient equations of the type

\[
(\partial_s-n)G_n=H_n
\]

before passing to the co-moving coordinate.

---

## 6. Strong-critical character of the correction

The first correction is `r^-3`, so on remote shells

\[
\int_{A_R}|Q_1|^3dY
\sim R^{-6},
\]

and similarly it is square integrable at infinity.

Hence the residual-canceling correction naturally belongs to the strong tail quotient rather than creating another weak-`L3` critical tail.

This is consistent with

\[
V-T_V\in L^2\cap L^3.
\]

---

## 7. DSD four-chain audit

### Formation — GREEN

The correction is formed only after the leading canonical tail and its actual NSE residual are known.

### Axis — GREEN

The neutral `n=0` critical-tail channel and the damped `n>=1` correction channels are separated.

### Static aggregation — GREEN

The correction does not constitute a second critical tail resource. Its stronger decay places it in the strong quotient.

### Dynamics — GREEN

No recurrence assumption is used to invert the subleading operator. The inverse coefficient `1/n` is local to the similarity-drift spectrum.

### Cross-audit — GREEN

This matches the earlier physical terminal Taylor expansion in which the static trace residual is canceled by the first `O(T_*-t)` correction.

---

## 8. Major pruning

The following route is RED:

\[
\text{nonzero canonical-tail NSE residual}
\Rightarrow
\text{no W1 realization}.
\]

A nonzero residual can be absorbed by strong subleading corrections to every finite asymptotic order.

Similarly, a recurrent/log-aperiodic residual is not by itself a resonance obstruction because the similarity eigenvalue at each subleading order is nonzero.

---

## 9. What remains genuinely open

Finite-order tail asymptotics no longer provide an obstruction.

A real F-gate closure must therefore be **nonperturbative/global**, for example:

1. failure of the full correction series to converge or remain in the strong quotient;
2. a global center-to-tail matching obstruction;
3. a critical estimate on the exact quotient equation not visible at any finite asymptotic order;
4. or a finite-energy prelimit constraint on the complete realized factor/correction pair.

The local tail residual itself is not the obstruction.

---

## 10. Updated interpretation

The W1 endpoint has the asymptotic architecture

\[
\boxed{
\text{neutral `r^-1` canonical genealogy}
+
\text{nonresonant strong subleading correction hierarchy}.
}
\]

This architecture is formally and finitely-order consistent with NSE.

The remaining difficulty is the global realization of the entire hierarchy by one unforced finite-energy trajectory.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]