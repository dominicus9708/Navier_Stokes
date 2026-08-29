# DSD M5-269 — RG Flatness Certified by Exact Physical Terminal-Time Identification

Date: 2026-08-30

Parent: `DSD_M5_268_STATIONARY_TAIL_RG_CARLEMAN_CORE_CONTRADICTION_2026-08-30.md`

Status: **SCOPE-CERTIFICATION AUDIT / THE FLATNESS INPUT USED IN M5-268 DOES NOT RELY ON CONVERGENCE OF THE FORMAL RG TAYLOR SERIES / THE DESCENDANT RESCALING EXACTLY CANCELS THE LERAY SPATIAL RESCALING, SO AT FIXED DESCENDANT COORDINATE THE RG PARAMETER `rho=e^{-h}` IS THE PHYSICAL TERMINAL-TIME DEPTH AT ONE FIXED PUNCTURED PHYSICAL POSITION, UP TO THE HARMLESS BASE NORMALIZATION / M5-139'S PUNCTURED TERMINAL `C^infinity` REGULARITY THEREFORE GIVES ACTUAL `C^infinity` REGULARITY OF THE REALIZED RG PATH AT `rho=0` ON FIXED PUNCTURED COMPACTS / IF `F(T)=0`, THE EXACT RG DIFFERENTIAL RECURSION MAKES EVERY POSITIVE `rho` DERIVATIVE AT ZERO VANISH, AND ORDINARY TAYLOR REMAINDER ESTIMATES GIVE `O(rho^N)` FOR EVERY N / THUS THE ZERO-EXTENSION/CARLEMAN INPUT OF M5-268 IS GREEN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why this audit is needed

M5-240 explicitly warns that the formal series

\[
\mathscr R_\rho(T)\sim\sum_{n\ge0}\rho^nA_n
\]

need not converge.

Therefore the implication

\[
A_n=0\ \forall n\ge1
\quad\Longrightarrow\quad
\mathscr R_\rho(T)-T=O(\rho^N)\ \forall N
\]

would be invalid if based only on a formal expansion.

M5-268 instead needs **actual finite-order Taylor regularity** of the realized RG path at `rho=0` on every fixed punctured compact.

This note verifies that regularity directly from the physical meaning of the descendant variables.

---

## 2. Leray variables and physical terminal depth

Write

\[
\tau=T^*-t,
\qquad
s=-\log\tau,
\qquad
Y=\frac{x-x_*}{\sqrt\tau}.
\]

The Leray velocity is, up to the fixed normalization convention,

\[
V(Y,s)=\sqrt\tau\,u(x,t).
\]

Advance by a Leray time `h`:

\[
\tau_h=e^{-h}\tau_0,
\qquad
s_h=s_0+h.
\]

The descendant field is

\[
\mathcal D_h(Y)
=e^{h/2}V(e^{h/2}Y,s_0+h).
\]

Insert the physical representation of `V`:

\[
\begin{aligned}
\mathcal D_h(Y)
&=e^{h/2}\sqrt{\tau_h}\,
 u\!\left(x_*+\sqrt{\tau_h}\,e^{h/2}Y,
 T^*-\tau_h\right)\\
&=\sqrt{\tau_0}\,
 u\!\left(x_*+\sqrt{\tau_0}Y,
 T^*-\tau_0e^{-h}\right).
\end{aligned}
\]

Thus the spatial position

\[
\boxed{x=x_*+\sqrt{\tau_0}Y}
\]

is **independent of `h`**.

The only changing variable is terminal time depth

\[
\boxed{
T^*-t_h=\tau_0e^{-h}.
}
\]

---

## 3. Exact RG parameter is terminal-time depth

Set

\[
\rho=e^{-h}.
\]

Then

\[
\boxed{
\mathscr R_\rho(T)(Y)
=\sqrt{\tau_0}\,
 u\!\left(x_*+\sqrt{\tau_0}Y,
 T^*-\tau_0\rho\right).
}
\]

Therefore, on every fixed descendant compact

\[
K\Subset\mathbb R^3\setminus\{0\},
\]

`rho -> 0` is exactly the physical one-sided terminal-time limit at a fixed punctured spatial compact

\[
x_*+\sqrt{\tau_0}K.
\]

This is the same geometry as M5-139, where

\[
z=\frac{T^*-t}{|x-x_*|^2}.
\]

For fixed physical `x!=x_*`, `z` and `rho` differ only by a fixed positive spatial/base-normalization factor.

Hence `rho` and the realized integer Fuchsian terminal variable are not merely of the same asymptotic order; on a fixed descendant cell they are the same physical terminal-time coordinate up to a constant multiple.

---

## 4. Punctured terminal smoothness gives actual RG Taylor regularity

M5-139 records that on every fixed punctured physical compact, the W1 physical realization is `C^infinity` in one-sided terminal time.

By Section 3, this gives for every fixed punctured descendant compact `K` and every finite spatial derivative order `k`:

\[
\boxed{
\rho\mapsto\mathscr R_\rho(T)
\in C^\infty\bigl([0,\rho_0];C^k(K)\bigr).
}
\]

In particular, all finite `rho` derivatives at zero are actual derivatives, not formal coefficients.

The same holds for the pressure gradient after fixing the canonical additive pressure gauge.

---

## 5. Exact RG equation determines the actual derivatives

The realized path satisfies

\[
\partial_\rho\mathscr R
=-\mathcal F(\mathscr R).
\]

At `rho=0`,

\[
\partial_\rho\mathscr R(0)
=-\mathcal F(T).
\]

If

\[
\mathcal F(T)=0,
\]

then

\[
\partial_\rho\mathscr R(0)=0.
\]

Differentiate the exact RG equation repeatedly. Every higher derivative is a finite multilinear expression in derivatives of `mathcal F` at `T` and lower positive `rho` derivatives of `mathscr R`.

For example,

\[
\partial_\rho^2\mathscr R(0)
=-D\mathcal F_T[\partial_\rho\mathscr R(0)]=0.
\]

Inductively, if

\[
\partial_\rho^j\mathscr R(0)=0
\quad(1\le j\le n),
\]

then every term in the differentiated equation for order `n+1` contains at least one positive-order derivative and vanishes.

Therefore

\[
\boxed{
\partial_\rho^n\mathscr R(0)=0
\qquad\forall n\ge1.
}
\]

This is the differential version of the M5-240 triangular recursion, now justified at the level of the actual realized path.

---

## 6. Taylor remainder gives genuine infinite-order flatness

Fix `N` and a punctured compact `K`.

Since

\[
\mathscr R\in C^N([0,\rho_0];C^k(K))
\]

and all derivatives of orders `1,...,N-1` vanish at zero, the Banach-valued Taylor theorem gives

\[
\mathscr R_\rho(T)-T
=\frac{\rho^N}{(N-1)!}
\int_0^1(1-\theta)^{N-1}
\partial_\rho^N\mathscr R_{\theta\rho}(T)\,d\theta.
\]

The `Nth` derivative is bounded on a sufficiently small compact `rho` interval by punctured terminal smoothness.

Hence

\[
\boxed{
\|\mathscr R_\rho(T)-T\|_{C^k(K)}
\le C_{K,k,N}\rho^N.
}
\]

Since `N` is arbitrary,

\[
\boxed{
\mathscr R_\rho(T)-T
\text{ is genuinely flat to every algebraic order at }\rho=0.
}
\]

No Taylor-series convergence or analyticity is used.

---

## 7. Pressure flatness

On a fixed punctured domain the pressure difference is determined, after gauge fixing, by the elliptic equation obtained from the RG/Navier--Stokes difference:

\[
-\Delta q
=(\partial_iU_j)(\partial_jW_i)
+(\partial_iW_j)(\partial_jT_i).
\]

Here

\[
W=\mathscr R_\rho(T)-T.
\]

Because `W` and all required derivatives are `O(rho^N)` for every `N`, standard local elliptic estimates give, after fixing the spatial mean of `q`,

\[
\boxed{
\|q(\rho)\|_{C^k(K)}
=O_{K,k,N}(\rho^N)
\qquad\forall N.
}
\]

Thus the pressure zero extension used in M5-268 is also justified.

---

## 8. Consequence for M5-268

The only delicate extra input of M5-268 was the actual all-order flatness required to zero-extend the realized RG/stationary difference through `tau=0`.

Sections 2--7 establish precisely that input.

Therefore the M5-268 Carleman argument does **not** depend on an unproved convergent RG Taylor series.

Its logic is instead

\[
\boxed{
\text{punctured terminal }C^\infty
+\text{exact RG equation}
+F(T)=0
\Longrightarrow
\text{actual infinite-order RG flatness}
\Longrightarrow
\text{M5-217 local Carleman closure}.
}
\]

---

## 9. DSD verdict

### GREEN

- exact physical interpretation of descendant `rho`;
- actual Banach-valued terminal Taylor regularity on punctured compacts;
- stationarity kills every actual positive `rho` derivative;
- Taylor remainder produces genuine `O(rho^N)` flatness;
- pressure flatness follows elliptically.

### CONFIRMED

\[
\boxed{
\text{M5-268 stationary-tail closure remains valid on the audited realized W1 corridor.}
}
\]

### STILL OPEN

\[
\boxed{
\text{residual-active realized minimal tail hull}.}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
