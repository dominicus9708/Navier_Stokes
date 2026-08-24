# DSD first-hitting renormalization transition gate

Date: 2026-08-25

Status: **EXACT TRANSITION IDENTITY PROVED / ZERO-GAP SAME-PROFILE RECURRENCE EXCLUDED / GENERAL POSITIVE-GAP RECURRENCE NOT CLOSED / CENTER-TIME-STATE DRIFT TRICHOTOMY SHARPENED / GLOBAL REGULARITY UNPROVED.**

This note continues the DSD-internal audit without identifying the previously recorded corridor symbol `L_j` with a first-hitting time gap. The exact definition of `L_j` must be recovered separately. Everything below uses only explicitly defined quantities.

## 1. Full first-hitting rescaling

Let

\[
W_j=q^jW_0,
\qquad
r_j=\left(\frac\nu{W_j}\right)^{1/2},
\qquad q>1.
\]

At the first-hitting time `t_j`, choose a maximum point `X_j`. Define the full normalized vorticity solution around that base by

\[
\boxed{
\Omega_j(y,s)
:=
\frac{r_j^2}{\nu}
\omega\left(
X_j+r_jy,
\,t_j+\frac{r_j^2}{\nu}s
\right).
}
\]

Thus

\[
\|\Omega_j(\cdot,0)\|_\infty=1.
\]

Set

\[
\boxed{
\lambda:=\frac{r_j}{r_{j+1}}=\sqrt q>1,
}
\]

\[
\boxed{
a_j:=\frac{X_{j+1}-X_j}{r_j},}
\]

and

\[
\boxed{
\tau_j:=\frac{\nu(t_{j+1}-t_j)}{r_j^2}>0.
}
\]

These are definitions. No bound on `a_j` or `tau_j` is assumed.

## 2. Exact consecutive transition identity

Because

\[
r_{j+1}=\frac{r_j}{\lambda},
\qquad
\frac{r_{j+1}^2}{\nu}
=\frac{r_j^2}{\nu\lambda^2},
\]

we compute directly:

\[
\begin{aligned}
\Omega_{j+1}(y,s)
&=
\frac{r_{j+1}^2}{\nu}
\omega\left(
X_{j+1}+r_{j+1}y,
\,t_{j+1}+\frac{r_{j+1}^2}{\nu}s
\right)\\
&=
\lambda^{-2}
\Omega_j\left(
\frac{X_{j+1}-X_j}{r_j}+rac y\lambda,
\frac{\nu(t_{j+1}-t_j)}{r_j^2}+rac{s}{\lambda^2}
\right).
\end{aligned}
\]

Hence

\[
\boxed{
\Omega_{j+1}(y,s)
=
\lambda^{-2}
\Omega_j\left(
a_j+\frac y\lambda,
\tau_j+\frac{s}{\lambda^2}
\right).
}
\]

Status: **PROVED EXACTLY.**

This is coordinate algebra, not a recurrence assumption.

## 3. Backward-time form avoids any positive-time compactness assumption

Choose

\[
s=-\lambda^2\tau_j.
\]

Then the time argument on the right is zero, so

\[
\boxed{
\Omega_{j+1}
\left(y,-\lambda^2\tau_j\right)
=
\lambda^{-2}
\Omega_j\left(a_j+\frac y\lambda,0\right).
}
\]

Thus the comparison between stage `j` at its first-hitting time and stage `j+1` requires only a negative normalized time in the later rescaling.

Status: **PROVED EXACTLY.**

## 4. Global L2 norm relation at the same physical time

Translations do not change `L2`. From the backward-time identity,

\[
\begin{aligned}
\left\|\Omega_{j+1}
(\cdot,-\lambda^2\tau_j)\right\|_2^2
&=
\lambda^{-4}
\int_{\mathbb R^3}
\left|\Omega_j(a_j+y/\lambda,0)\right|^2dy\\
&=
\lambda^{-1}\|\Omega_j(\cdot,0)\|_2^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\left\|\Omega_{j+1}
(\cdot,-\lambda^2\tau_j)\right\|_2
=
\lambda^{-1/2}
\|\Omega_j(\cdot,0)\|_2.
}
\]

This is not a contradiction. It is simply the exact change of normalized base for the same physical state at time `t_j`.

Status: **PROVED / NO CONTRADICTION CLAIMED.**

## 5. Joint compact subsequence with tight transition parameters

Suppose along a subsequence `j_n` one has

\[
a_{j_n}\to a_*,
\qquad
\tau_{j_n}\to\tau_*<\infty,
\]

and suppose the two neighboring normalized solution families converge on the required common compact spacetime windows:

\[
\Omega_{j_n}\to\Omega^-,
\qquad
\Omega_{j_n+1}\to\Omega^+.
\]

Passing to the exact backward-time identity gives

\[
\boxed{
\Omega^+
(y,-\lambda^2\tau_*)
=
\lambda^{-2}
\Omega^-
\left(a_*+\frac y\lambda,0\right).
}
\]

Status: **PROVED CONDITIONAL ON THE STATED JOINT COMPACTNESS/TIGHTNESS.**

Importantly, compactness does not by itself imply

\[
\Omega^-\equiv\Omega^+.
\]

That would be a stronger same-profile recurrence statement and must be separately formed.

## 6. Zero-gap same-profile recurrence is impossible in finite global L2

Now assume the stronger finite DSD witness conditions:

1. `a_{j_n}->a_*`;
2. `tau_{j_n}->0`;
3. both neighboring sequences converge to the **same** time-zero global profile
   \[
   \Omega^-\equiv\Omega^+\equiv\Omega_*;
   \]
4. \(\Omega_*(\cdot,0)\in L^2(\mathbb R^3)\).

Then the limit identity becomes

\[
\boxed{
\Omega_*(y,0)
=
\lambda^{-2}
\Omega_*
\left(a_*+\frac y\lambda,0\right).
}
\]

Taking the global `L2` norm yields

\[
\|\Omega_*(0)\|_2^2
=
\lambda^{-1}
\|\Omega_*(0)\|_2^2.
\]

Since `lambda>1`,

\[
\boxed{
\Omega_*(\cdot,0)=0.
}
\]

But the first-hitting analytic core normalization supplies a nonzero point/ball witness, so the same profile cannot be zero.

Therefore

\[
\boxed{
\text{finite-L2 nonzero same-profile recurrence}
+\tau_j\to0
+\text{tight normalized center shift}
\Longrightarrow
\text{contradiction}.
}
\]

Status: **PROVED CONDITIONAL.**

This is stronger than merely saying that exact global discrete self-similarity is incompatible with bounded-Z: here only a one-step zero-time-gap fixed-profile limit is used.

## 7. Positive time gap does not close by the same norm argument

If

\[
\tau_*>0,
\]

then the limit relation is between two different times:

\[
\Omega^+
(y,-\lambda^2\tau_*)
=
\lambda^{-2}
\Omega^-
\left(a_*+\frac y\lambda,0\right).
\]

Even if `Omega^-=Omega^+=Omega_*`, this single two-time relation does **not** by itself give

\[
\Omega_*=\mathcal R\Omega_*
\]

for all times, nor does it automatically iterate to a full discretely self-similar ancient orbit.

Therefore

\[
\boxed{
\text{single positive-gap two-time scale relation}
\not\Rightarrow
\text{contradiction by bounded-Z alone}.
}
\]

Status: **ANTI-OVERCLAIM / PROVED AS A SCOPE LIMITATION.**

## 8. DSD transition typing

The exact transition identity exposes four genuinely different late behaviors:

### A. Normalized center/base escape

\[
|a_j|\to\infty
\quad\text{or is non-tight}.
\]

Then the neighboring first-hitting cores leave every common finite spatial base under the transition map.

This is a DSD **base/location non-tightness** branch. Because `a_j` is frame-dependent across different physical times, no energy cost is claimed from absolute translation alone.

### B. Normalized time-gap escape/non-tightness

\[
\tau_j\to\infty
\quad\text{or is otherwise non-tight}.
\]

Then adjacent first-hitting events cannot be compared on one fixed ancient time window without an additional timing theorem.

### C. Tight positive-gap renormalization-state drift

`a_j` and `tau_j` are tight, but joint subsequential limits satisfy

\[
\Omega^-\ne\Omega^+.
\]

Then successive normalized formed states do not settle to one recurring descriptor; a genuine DSD describability difference persists in the renormalization state space.

### D. Tight same-profile zero-gap recurrence

\[
a_j\to a_*,
\qquad
\tau_j\to0,
\qquad
\Omega^-\equiv\Omega^+.
\]

On the finite-global-L2 bounded-Z branch this is excluded by Section 6.

Thus the previously vague recurrence question becomes

\[
\boxed{
\text{center/base escape}
\lor
\text{time-gap non-tightness/positive dwell}
\lor
\text{renormalization-state drift}
\lor
\text{excluded zero-gap fixed profile}.
}
\]

## 9. Relation to the DSD formation sequence

This transition gate respects the finite-formation discipline:

- no singular-time value is assigned;
- no infinite derivative object is formed;
- no infinite tail is treated as one Stage-VII channel;
- every comparison uses two finite first-hitting bases;
- the exact difference between those bases is represented by the finite tuple
  \[
  (a_j,\tau_j,\Omega_j,\Omega_{j+1}).
  \]

The next proof obligation is therefore a finite transition problem, not an ancient-limit object problem.

## 10. Audit verdict

### PROVED

- exact consecutive first-hitting renormalization identity;
- exact backward-time version;
- exact global-L2 scaling relation for the same physical state represented in the next base;
- joint-limit transition formula under tight `a_j,tau_j`;
- finite-L2 nonzero same-profile zero-gap recurrence is impossible.

### NOT DERIVED

- uniform lower or upper bounds for `tau_j` from the unrecovered `L_j` corridor;
- Galilean-invariant tightness of the center parameter `a_j`;
- equality of neighboring subsequential limits;
- full discrete self-similarity from one positive-gap relation;
- contradiction on the positive-gap/state-drift/base-escape branches;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
