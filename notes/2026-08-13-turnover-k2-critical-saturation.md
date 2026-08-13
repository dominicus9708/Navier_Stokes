# Material-turnover `k=2` cost versus Sobolev critical scaling

Date: 2026-08-13

Status: **DERIVED SCALING DIAGNOSTIC / NO SUPERCRITICAL GAIN CLAIMED**.

The Cauchy-vorticity turnover lemma forces, under bounded recent deformation and order-one natural-volume recruitment,

\[
\int_I\|\Delta\omega\|_2^2dt
\gtrsim W_0^{3/2}.
\]

This note compares that lower bound with the standard 3D Sobolev/Gagliardo--Nirenberg scaling.  The purpose is to locate the true critical wall and avoid mistaking scale-critical saturation for a proof-producing exponent gain.

---

## 1. `H^2` to `L^infinity` interpolation

For a sufficiently smooth decaying vector field in `R^3`,

\[
\boxed{
\|\omega\|_\infty
\le
C_{GN}
\|\omega\|_2^{1/4}
\|\nabla^2\omega\|_2^{3/4}.
}
\]

Fourier algebra gives equivalence (indeed equality for the full Frobenius Hessian convention)

\[
\|\nabla^2\omega\|_2^2
\asymp
\|\Delta\omega\|_2^2.
\]

Let

\[
E_0=\|\omega\|_2^2,
\qquad
E_2=\|\nabla^2\omega\|_2^2,
\qquad
W=\|\omega\|_\infty.
\]

Then

\[
W
\lesssim
E_0^{1/8}E_2^{3/8},
\]

so

\[
\boxed{
E_2
\gtrsim
W^{8/3}E_0^{-1/3}.
}
\]

---

## 2. Dimensionless enstrophy occupancy ratio

At the natural vorticity scale define

\[
\boxed{
\mathfrak e
=\frac{E_0}{\sqrt W}.
}
\]

This is scale invariant:

- `E_0 -> lambda E_0`;
- `sqrt W -> lambda sqrt W`.

Substituting

\[
E_0=\mathfrak e\sqrt W
\]

into the interpolation lower bound yields

\[
\boxed{
E_2
\gtrsim
\mathfrak e^{-1/3}W^{5/2}.
}
\]

Over one natural time

\[
\tau\asymp W^{-1},
\]

a comparable-in-time `E_2` level would therefore correspond to

\[
\boxed{
\int_I E_2dt
\gtrsim
\mathfrak e^{-1/3}W^{3/2}.
}
\]

This last display is a scaling comparison, not an unconditional time lower bound, because `E_0,E_2,W` can vary within the window.

---

## 3. Compare with the turnover lower bound

The material-recruitment lemma gives the genuinely dynamical/geometric estimate

\[
\boxed{
\int_I E_2dt
\gtrsim
c_{\rm turn}W^{3/2}
}
\]

under its stated turnover and bounded-deformation hypotheses.

The exponent is the same natural exponent as the `H^2 -> L^infinity` critical scaling.

Therefore the turnover route does **not** produce a better power of `W` by itself.

This is important: an apparent gain at the level of raw derivative size would be an artifact unless some additional geometric small parameter is used.

---

## 4. Where a genuine gain can still occur

The two estimates differ in their coefficients and geometry.

The generic interpolation relation weakens when

\[
\mathfrak e=E_0/\sqrt W
\]

is large, through the factor

\[
\mathfrak e^{-1/3}.
\]

The turnover lower bound does not contain this weakening: replacing a fixed fraction of one natural material volume still costs an order-one `W^(3/2)` amount, independent of how much enstrophy exists elsewhere.

Thus for large `mathfrak e`, material turnover can impose a stronger **coefficient-level** derivative burden than generic interpolation.

The possible proof gain is therefore not an exponent gain but a structural one involving combinations such as

\[
\boxed{
\text{turnover fraction}
\times
\text{projective alignment}
\times
\text{occupancy/sparseness}
\times
\mathfrak e^{1/3}.
}
\]

---

## 5. Interpretation of the critical wall

The current route has reached the scaling expected at a potential singularity:

- natural length `r~W^-1/2`;
- natural time `tau~W^-1`;
- natural integrated second-vorticity-derivative cost `W^(3/2)`.

Therefore continuing by dimensional estimates alone cannot solve the problem.

Any proof-producing closure must exploit at least one non-scaling ingredient:

1. a strict geometric deficit (sparseness / projective alignment / polarity);
2. an exact cancellation;
3. a summable material-retention gain;
4. a monotonic/telescoping channel across derivative order;
5. or an incompatibility among several critical conditions.

---

## 6. Residual target

The most concrete remaining target is now:

\[
\boxed{
\text{show that repeated order-one turnover at critical }k=2\text{ cost}
\text{ cannot coexist with all projective/sparseness gates at every late natural window.}
}
\]

Equivalently, seek a strict coefficient gain that becomes summable when the residual geometry is simultaneously

- intense;
- non-sparse;
- projectively almost one-axis;
- sign-oriented;
- and repeatedly material-replacing.

Status: **OPEN STRICT-GAIN / CRITICAL-SATURATION CLOSURE**.
