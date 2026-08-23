# Active Remote Contraction `2/5` Correction — 2026-08-23

Status: **CORRECTION / STRENGTHENING OF EARLIER TURNOVER GATE — GLOBAL REGULARITY NOT PROVED.**

This note supersedes the weaker contraction exponents and corrects one geometric over-identification in `CONTRACTING_ACTIVE_REMOTE_H_TURNOVER_GATE_2026-08-23.md`.

---

## 1. Strongest current physical-radius bound

The relative-Campanato remote-strain gate gives, for an order-one active remote strain at normalized radius `R`,

\[
R\lesssim W^{1/10}.
\]

Since the first-hitting physical length is

\[
r=W^{-1/2},
\]

the physical active radius

\[
\ell=Rr
\]

satisfies

\[
\boxed{\ell\lesssim W^{-2/5}.}
\]

This is stronger than the earlier intermediate bounds

\[
\ell=o(W^{-1/7})
\]

and

\[
\ell=O(W^{-1/3}).
\]

Those earlier estimates remain valid as weaker consequences of their respective assumptions, but they are no longer the best active-radius ledger.

---

## 2. Stagewise logarithmic contraction requirement

Let

\[
W_j=q^jW_0,
\qquad q>1.
\]

Suppose a persistently tracked active source has physical radius `ell_j` satisfying the strongest bound for all sufficiently late stages. Then

\[
\ell_j\lesssim W_j^{-2/5}
\]

implies

\[
\log\frac{\ell_0}{\ell_J}
\ge
\frac25J\log q-O(1).
\]

Define positive contraction action

\[
a_j
:=
\left[\log\frac{\ell_j}{\ell_{j+1}}\right]_+.
\]

Then the asymptotic average cannot remain below `(2/5) log q`. In particular, infinitely many stages satisfy the weaker fixed threshold

\[
\boxed{
a_j\ge \frac15\log q.
}
\]

Equivalently,

\[
\boxed{
\frac{\ell_{j+1}}{\ell_j}\le q^{-1/5}
}
\]

on infinitely many stages.

For `q=2`, this is a contraction by at least

\[
1-2^{-1/5}\approx0.12945,
\]

about `12.9%` in those stages.

---

## 3. Correction: source radius is not automatically a material-line length

The earlier contracting-active-halo note used a material-line length inequality too quickly.

If both `x(t)` and `X(t)` are material trajectories, then

\[
\frac d{dt}(x-X)
=u(x,t)-u(X,t)
\]

and along the segment joining them,

\[
\frac d{dt}\log|x-X|
\le
\sup_{segment}\|S\|.
\]

The antisymmetric rotation does not change length.

However, the project’s moving weighted-mean center is not automatically material. In general,

\[
\frac d{dt}(x-X)
=u(x,t)-\dot X(t)
\]

contains the additional mismatch

\[
\boxed{\dot X-u(X,t).}
\]

Therefore contraction of distance to the tracked center cannot be identified with material-line contraction without a material-center lemma.

---

## 4. Corrected turnover split

The strong contraction requirement must therefore be divided into three cases.

### Case A: same material source + material center

If the active source is materially tracked and the center is a material trajectory, then

\[
\log\frac{\ell_j}{\ell_{j+1}}
\le
\int_{I_j}\|\Sigma\|_\infty ds.
\]

If the non-`H` corridor has

\[
\|\Sigma\|_\infty\le B_+
\]

in normalized time, then every strong-contraction stage satisfies

\[
\boxed{
L_j
\ge
\frac{\log q}{5B_+}.
}
\]

This is stronger than the previous `1/14` coefficient, but applies only in the material-center subcase.

### Case B: center drift

If

\[
\dot X-u(X,t)
\]

is not negligible at the relevant scale, then the radius change is paid by center motion rather than pure material strain. This is a genuine `T_center` candidate and appears explicitly in the moving-relative-variance ledger.

### Case C: source replacement

If the active source at stage `j+1` is not the same material reservoir as at stage `j`, then no material-line contraction estimate is applicable. The proof must instead charge the replacement to material boundary flux, pressure work, viscous leakage, or a change of coherent relative-energy reservoir.

These are exactly the terms in `MOVING_RELATIVE_VARIANCE_TURNOVER_LEDGER_2026-08-23.md`.

---

## 5. Revised finite-stage target

The safe statement is now

\[
\boxed{
\text{persistent active remote influence}
\Longrightarrow
\begin{cases}
\text{same-material/material-center strong contraction},\\
T_{center},\\
\text{source replacement / boundary turnover}.
\end{cases}
}
\]

Only the first line directly yields the time lower bound

\[
L_j\ge\frac{\log q}{5B_+}.
\]

The other two must be closed with the exact moving-relative-variance identity rather than by a material-line argument.

---

## 6. Current status

This correction strengthens the radius exponent while narrowing the scope of the material-line argument. It removes an overclaim and makes the remaining proof obligation cleaner.

Status: **THE STRONGEST ACTIVE-RADIUS SCALING IS `ell = O(W^{-2/5})`. A FIXED LOGARITHMIC CONTRACTION OCCURS INFINITELY OFTEN FOR A PERSISTENT ACTIVE SOURCE, BUT DIRECT STRAIN-TIME CONTROL APPLIES ONLY WHEN BOTH SOURCE AND CENTER ARE MATERIALLY TRACKED. CENTER DRIFT AND SOURCE REPLACEMENT REMAIN TURNOVER TERMS TO BE CLOSED BY THE RELATIVE-VARIANCE LEDGER.**