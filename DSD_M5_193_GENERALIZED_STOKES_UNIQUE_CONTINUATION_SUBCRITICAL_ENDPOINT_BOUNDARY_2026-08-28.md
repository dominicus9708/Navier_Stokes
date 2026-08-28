# DSD M5-193 — Generalized Stokes Unique Continuation: Subcritical Theorem / Critical Endpoint Boundary

Date: 2026-08-28

Status: **P1_B LITERATURE-ENDPOINT AUDIT / LIN--WANG PROVE QUANTITATIVE STRONG UNIQUE CONTINUATION FOR THE GENERALIZED NONSTATIONARY STOKES SYSTEM WITH PRESSURE AND SINGULAR LOWER-ORDER COEFFICIENTS `|A|<=lambda |x|^-1+eps`, `|B|<=lambda |x|^-2+eps`, BUT THEIR ASSUMPTION IS STRICTLY `eps>0` / THE W1 COMMON-TAIL LINEARIZATION SITS EXACTLY AT THE OMITTED `eps=0` SCALE-CRITICAL ENDPOINT / PRESSURE COMPATIBILITY IS THEREFORE KNOWN SUBCRITICALLY, WHILE THE ACTUAL W1 GATE IS A GENUINE ENDPOINT PROBLEM RATHER THAN A MISSING STANDARD STOKES CARLEMAN REFERENCE / GLOBAL REGULARITY UNPROVED.**

---

## 1. External generalized Stokes system

Lin--Wang study

\[
\boxed{
\partial_tu-\Delta u+A(t,x)\cdot\nabla u+B(t,x)u+\nabla p=0,
\qquad \nabla\cdot u=0.
}
\]

Their result is designed specifically to obtain quantitative vanishing-order / strong unique-continuation estimates for the **velocity field** despite the pressure coupling.

Thus the pressure/divergence-free architecture matches the structural form of the present same-tail relative equation.

---

## 2. Their singular coefficient class

The theorem assumes, near the spatial singular point,

\[
\boxed{
|A(t,x)|\le\lambda |x|^{-1+\varepsilon},
}
\]

and

\[
\boxed{
|B(t,x)|\le\lambda |x|^{-2+\varepsilon},
}
\]

for

\[
\boxed{0<\varepsilon<1.}
\]

Their proof reduces the Stokes system to a coupled parabolic vorticity equation plus elliptic velocity equation and derives Carleman / three-cylinder estimates.

This independently confirms the M5-183 architecture.

---

## 3. W1 is exactly the missing endpoint

M5-185/M5-190 give the actual W1 Type-I coefficient order

\[
|A_{W1}|\lesssim\rho^{-1},
\qquad
|B_{W1}|\lesssim\rho^{-2}.
\]

At a fixed time slice near the center this corresponds precisely to the spatial endpoint

\[
\boxed{
|A|\sim |x|^{-1},
\qquad
|B|\sim |x|^{-2},
}
\]

before the parabolic regularization by `rho^2=|x|^2+tau` is included.

Thus the external theorem reaches every strictly subcritical exponent but not

\[
\boxed{\varepsilon=0.}
\]

This is exactly the W1 Hardy-critical endpoint.

---

## 4. Consequence

The literature boundary changes the interpretation of the first large gate.

It is **not**:

\[
\text{`find any Carleman estimate that can handle Stokes pressure'}.
\]

Pressure-compatible generalized-Stokes Carleman estimates already exist.

The actual problem is:

\[
\boxed{
\text{extend the generalized-Stokes unique-continuation mechanism to the exact critical endpoint}
\quad
(|A|,|B|)\sim(|x|^{-1},|x|^{-2}),
}
\]

or exploit additional canonical-tail structure that makes this extension unnecessary.

---

## 5. Why epsilon->0 cannot simply be taken

A theorem with constants depending on `epsilon>0` does not imply the endpoint by a limiting argument.

Critical Hardy problems commonly lose coercivity or compactness exactly at `epsilon=0`.

M5-191 gives an explicit signed `r^-2` strain countermodel, while M5-192 gives a terminal-critical `1/tau` countermodel to generic backward injectivity.

Therefore

\[
\boxed{
\varepsilon>0\text{ theorem}
\not\Rightarrow
\varepsilon=0\text{ W1 endpoint}.
}

This is a permanent RED arrow unless uniform endpoint constants are independently proved.

---

## 6. Useful information imported from the theorem

Although it does not close W1, the theorem validates three structural choices:

1. curl/velocity parabolic--elliptic reduction is legitimate;
2. pressure can be handled without converting the whole problem into a scalar heat inequality;
3. the only genuinely new analytic difficulty is the **critical coefficient strength**, not the existence of a Stokes unique-continuation framework.

Hence M5-183 is retained, while M5-185 is correctly interpreted as an endpoint extension problem.

---

## 7. DSD audit

### Formation — GREEN

The external theorem and the W1 coefficient class are stated separately before comparison.

### Axis — GREEN

Subcritical `epsilon>0` and critical `epsilon=0` are not merged.

### Static aggregation — GREEN

No limiting theorem is asserted from nonuniform subcritical estimates.

### Dynamics — YELLOW ENDPOINT

Pressure-compatible UCP is known below the endpoint; the exact W1 endpoint remains open.

### Cross-audit — GREEN

This is consistent with M5-183, M5-190, M5-191, and the corrected M5-192.

---

## 8. Next calculation

The most informative next step is to inspect the Lin--Wang Carleman proof and identify **which single estimate uses `epsilon>0`**.

If the loss is only an integrability factor, test whether the canonical-tail properties

- divergence-free transport skewness;
- zero radial flux;
- exact common tail in both states;
- strong-`L3` perturbative quotient;

supply the missing endpoint cancellation.

If not, record the endpoint as a genuine new theorem requirement rather than disguising it as routine bookkeeping.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
