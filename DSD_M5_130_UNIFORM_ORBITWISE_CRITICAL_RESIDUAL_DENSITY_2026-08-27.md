# DSD M5-130 — Uniform Orbitwise Critical Residual Density

Date: 2026-08-27

Status: **W1-CONDITIONAL / COMBINES THE EXACT CORE–TAIL COCYCLE WITH THE TRACE-FREE RESIDUAL FLOOR AND MINIMAL TAIL-FACTOR DENSITY / EVERY NONTRIVIAL W1 SURVIVOR ORBIT CARRIES A STRICTLY POSITIVE LONG-TIME MEAN CRITICAL PRESSURE–STRAIN RESIDUAL / NO INVARIANT-MEASURE EXCEPTION REMAINS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inputs

Use the M5-120 exact cocycle

\[
\int_0^h X_3(S_sV)\,ds
=
\frac13\bigl[\mathcal K(S_hV)-\mathcal K(V)\bigr]
+
\frac13\int_{-h/2}^{0}\mathfrak c_\rho(T_V)\,d\rho,
\]

with bounded continuous renormalized cubic charge `K` on the compact W1 set.

Use the M5-108 pointwise residual inequality

\[
\boxed{\mathcal E_3\ge 2\nu X_3.}
\]

Use the M5-127 minimal tail-factor consequence: for every nonzero tail state there are constants

\[
r_*>0,\qquad C_*>0
\]

uniform on the compact minimal tail factor such that

\[
\boxed{
\int_{-L}^{0}\mathfrak c_\rho(T)\,d\rho
\ge r_*L-C_*
\qquad\forall L\ge0.
}
\]

The precise constants depend on the chosen continuous one-log-cell cubic observable and the syndetic return bound, not on the individual state.

---

## 2. Integrate the residual inequality

Integrating `E_3 >= 2 nu X_3` from `0` to `h` gives

\[
\int_0^h\mathcal E_3(S_sV)\,ds
\ge
2\nu\int_0^hX_3(S_sV)\,ds.
\]

Insert M5-120:

\[
\boxed{
\begin{aligned}
\int_0^h\mathcal E_3(S_sV)\,ds
&\ge
\frac{2\nu}{3}
\bigl[\mathcal K(S_hV)-\mathcal K(V)\bigr]\\
&\quad+
\frac{2\nu}{3}
\int_{-h/2}^{0}\mathfrak c_\rho(T_V)\,d\rho.
\end{aligned}
}
\]

This is statewise and does not average over any invariant measure.

---

## 3. Uniform lower growth

Since `K` is bounded on the compact W1 set, let

\[
K_*:=\sup_M|\mathcal K|<\infty.
\]

Then

\[
\mathcal K(S_hV)-\mathcal K(V)\ge-2K_*.
\]

With `L=h/2`, the uniform tail-density estimate gives

\[
\int_{-h/2}^{0}\mathfrak c_\rho(T_V)\,d\rho
\ge
\frac{r_*}{2}h-C_*.
\]

Therefore

\[
\boxed{
\int_0^h\mathcal E_3(S_sV)\,ds
\ge
\frac{\nu r_*}{3}h
-
\frac{4\nu K_*}{3}
-
\frac{2\nu C_*}{3}.
}
\]

Hence for every W1 state `V`,

\[
\boxed{
\liminf_{h\to\infty}
\frac1h
\int_0^h\mathcal E_3(S_sV)\,ds
\ge
\frac{\nu r_*}{3}>0.
}
\]

---

## 4. From positive mean to recurrent residual bursts

`E_3` is continuous on the audited regularized/critical W1 class after the M5-96 branch-mean treatment and M5-108 critical passage.

If `E_3` were identically zero on the minimal set, the time mean above would vanish. Therefore there exists a state `V_*` and `epsilon_*>0` such that

\[
\mathcal E_3(V_*)>2\epsilon_*.
\]

By continuity, the open set

\[
\mathcal U_*:=\{V:\mathcal E_3(V)>\epsilon_*\}
\]

is nonempty.

Minimality implies returns to every nonempty open set are syndetic. Thus every W1 orbit enters `U_*` with bounded Leray-time gaps.

After shrinking `U_*` if necessary and using local time continuity, one obtains uniform positive-width intervals on which

\[
\boxed{\mathcal E_3\ge \epsilon_*/2.}
\]

Hence critical pressure–strain mismatch bursts are syndetic on every survivor orbit.

---

## 5. DSD four-chain audit

### Formation — GREEN

The residual `E_3` is the already formed componentwise pressure–strain mismatch. No new resource is invented.

### Axis — GREEN

The Leray-time window `h` and backward log-radius genealogy window `h/2` remain distinct but exactly related.

### Static aggregation — GREEN

`R_3`, tail cubic density, `X_3`, and `E_3` are not added as independent budgets. The only inequality used is `E_3 >= 2 nu X_3`, followed by the exact M5-120 cocycle.

### Dynamics — GREEN

Minimality is used only after the statewise lower-growth formula has been established.

### Cross-audit — GREEN

No invariant mean is used to prove the orbitwise bound. Invariant means become consistency checks only.

---

## 6. What this strengthens

The previous statement

\[
\langle\mathcal E_3\rangle_\mu>0
\]

for positive-residue invariant measures is upgraded to

\[
\boxed{
\text{every nontrivial W1 survivor orbit has a uniform positive long-time residual density.}
}
\]

There is therefore no exceptional orbit on the same minimal survivor set that can hide in the exact pressure endpoint for arbitrarily long times.

---

## 7. Limitation / RED firewall

The action

\[
\int_0^h\mathcal E_3\,ds
\]

is critical and is allowed to grow linearly in Leray time.

No finite physical-time budget for this action has been proved.

Therefore the positive orbitwise density is a rigidity input, not yet a contradiction.

The next gate is NSE-specific: determine what repeated order-one core residual bursts force on the canonical-tail residual / strong quotient coupling.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]