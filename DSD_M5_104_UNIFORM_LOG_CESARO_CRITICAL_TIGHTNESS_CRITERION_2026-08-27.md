# DSD M5-104 — Uniform Log-Cesaro Critical Tightness Criterion

Date: 2026-08-27

Status: **EXACT REFORMULATION OF THE MELLIN LIMIT-INTERCHANGE GAP / THE W1 CUBIC RESIDUE IS A LOG-SCALE ABEL MEAN OF THE CRITICAL DISTRIBUTION COORDINATE / UNIFORM ABEL VANISHING IS EQUIVALENT, UP TO UNIVERSAL CONSTANTS, TO UNIFORM LOG-CESARO VANISHING FOR THE NONNEGATIVE TAIL PROFILE / THIS IS WEAKER THAN POINTWISE UNIFORM K-TAIL TIGHTNESS AND WOULD ALREADY KILL `R3` / WHETHER NAVIER--STOKES ANCESTRY FORCES IT REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Distribution coordinate

For one normalized prelimit/W1 state `U`, define

\[
N_U(\lambda)
:=|\{Y:|U(Y)|>\lambda\}|,
\]

and the critical distribution coordinate

\[
\boxed{
q_U(\lambda)
:=\lambda^3N_U(\lambda)\ge0.
}
\]

For the small-amplitude boundary put

\[
\lambda=e^{-x},
\qquad x\ge0,
\]

and define

\[
\boxed{
Q_U(x)
:=q_U(e^{-x})
=e^{-3x}N_U(e^{-x}).
}
\]

Thus large `x` is the low-amplitude/spatial-infinity boundary.

---

# 2. Mellin moment in log-amplitude coordinates

Layer cake gives

\[
\int |U|^{3+\varepsilon}dY
=(3+\varepsilon)
\int_0^\infty
\lambda^{2+\varepsilon}N_U(\lambda)d\lambda.
\]

On `0<lambda<1`, substitute

\[
q_U(\lambda)=\lambda^3N_U(\lambda).
\]

Then

\[
\lambda^{2+\varepsilon}N_U(\lambda)d\lambda
=\lambda^{\varepsilon-1}q_U(\lambda)d\lambda.
\]

With `lambda=e^{-x}`,

\[
\boxed{
\varepsilon
\int_0^1
\lambda^{2+\varepsilon}N_U(\lambda)d\lambda
=
\varepsilon
\int_0^\infty
e^{-\varepsilon x}Q_U(x)dx.
}
\]

The high-amplitude part `lambda>=1` is harmless in the retained W1 `L^{3+delta}` class after multiplying by `epsilon`.

Hence the cubic residue is exactly controlled by the low-amplitude Abel mean

\[
\boxed{
\mathcal A_\varepsilon[Q]
:=\varepsilon\int_0^\infty e^{-\varepsilon x}Q(x)dx.
}
\]

---

# 3. Uniform Abel tightness

For a family of finite-stage normalized states `U_j`, define

\[
Q_j(x)=Q_{U_j}(x).
\]

The direct limit-interchange condition is

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\sup_j
\varepsilon\int_0^\infty e^{-\varepsilon x}Q_j(x)dx
=0.
}
\]

Call this **uniform Abel critical tightness**.

If it holds, then every subsequential W1 limit has zero Abel/Mellin cubic residue:

\[
\boxed{\mathscr R_3=0.}
\]

Therefore it is sufficient to exclude the retained positive-`R3` W1 endpoint.

---

# 4. Equivalent uniform logarithmic Cesaro condition

Define the log-Cesaro mean

\[
\boxed{
\mathcal C_L[Q_j]
:=\frac1L\int_0^LQ_j(x)dx.
}
\]

The proposed weaker-looking condition is

\[
\boxed{
\lim_{L\to\infty}
\sup_j
\mathcal C_L[Q_j]
=0.
}
\]

Because `Q_j>=0`, this condition and uniform Abel tightness are equivalent up to universal comparison constants.

## Cesaro -> Abel

Split the positive half-line into blocks of length `L=1/epsilon`.
If the long Cesaro means are uniformly small, summation against the exponentially decreasing block weights gives

\[
\sup_j
\varepsilon\int_0^\infty e^{-\varepsilon x}Q_j(x)dx
\to0.
\]

This is the standard Abelian implication for nonnegative locally integrable functions.

## Abel -> Cesaro

Set

\[
\varepsilon=1/L.
\]

On `0<=x<=L`,

\[
e^{-x/L}\ge e^{-1}.
\]

Therefore

\[
\begin{aligned}
\frac1L\int_0^LQ_j(x)dx
&\le
e\,\frac1L\int_0^L e^{-x/L}Q_j(x)dx\\
&\le
e\,\varepsilon
\int_0^\infty e^{-\varepsilon x}Q_j(x)dx.
\end{aligned}
\]

Hence

\[
\boxed{
\sup_j\mathcal C_L[Q_j]
\le
e\sup_j\mathcal A_{1/L}[Q_j].
}
\]

Thus uniform Abel vanishing implies uniform log-Cesaro vanishing.

Consequently the two conditions identify the same critical compactness obstruction.

---

# 5. Relation to the stronger pointwise tail target

Issue #2 uses stronger sufficient forms such as uniform `K`-tail tightness or uniform high weak-`L3` tail smallness.

Pointwise control of the critical distribution profile,

\[
\sup_j\sup_{x\ge L}Q_j(x)\to0,
\]

immediately implies log-Cesaro tightness.

But the converse need not hold: a family may have sparse log-scale spikes whose pointwise supremum stays large while their logarithmic density tends to zero.

Therefore

\[
\boxed{
\text{uniform log-Cesaro tightness}
}
\]

is a genuinely weaker sufficient target for killing the Abel/Mellin W1 residue.

It may not by itself imply the previously proved physical high-tail absorption lemma, but it would already contradict the retained W1 endpoint `R3>0`.

---

# 6. DSD four-chain audit

## Formation

`Q_j(x)` is the formed critical amplitude/spatial-boundary profile. It is nonnegative and does not require a pointwise asymptotic coefficient.

**GREEN.**

## Axis

The coordinate `x=-log lambda` is an amplitude-boundary/log-scale axis, not physical time and not material radius.

**GREEN.**

## Static aggregation

The Abel and Cesaro means aggregate the same nonnegative critical profile with different kernels. No shell is counted as an independent physical event.

**GREEN.**

## Dynamics

No recurrence is needed to prove the Abel/Cesaro equivalence. Dynamics enters only in the separate question of whether one physical ancestry can keep these means uniformly nonzero as `j->infinity`.

**GREEN.**

---

# 7. Circularity firewall

Uniform log-Cesaro tightness must be derived from an independent prelimit Navier--Stokes property.

It cannot be assumed in the disguised form

\[
\text{finite energy forbids a W1 boundary residue}
\]

because that statement is precisely the missing critical compactness theorem.

Likewise the existing `p>3` global precompactness does not imply this condition: the critical `1/r` profile belongs to every `L^p`, `p>3`, while maintaining a nonzero log-scale Cesaro mean at the `p=3` boundary.

---

# 8. New exact target

The weakest current mainline target can be written

\[
\boxed{
\lim_{L\to\infty}
\sup_j
\frac1L
\int_0^L
 e^{-3x}
 |\{|U_j|>e^{-x}\}|
 dx
=0.
}
\]

If proved for the normalized prelimit ancestry that generates W1, this commutes the critical Mellin limit and forces

\[
\mathscr R_3=0,
\]

closing the retained W1 endpoint.

The next audit must test whether the already available finite energy, normalized enstrophy, global `L^p (p>3)` tightness, and first-hit genealogy imply this Cesaro condition, or whether a countermodel survives all of those static bounds.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
