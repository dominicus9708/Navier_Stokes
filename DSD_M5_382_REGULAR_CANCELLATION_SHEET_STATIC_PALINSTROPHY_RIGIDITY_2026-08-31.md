# DSD M5-382 — Regular coherent cancellation sheet has unavoidable divergent normalized palinstrophy

Date: 2026-08-31

Status: **M5-379'S VOLUME-VARIANCE BOUND AND A NEW NORMAL-FIBER INTERFACE BOUND COMPLEMENT EACH OTHER / FOR A REGULAR OPPOSITE-SIGNED RESERVOIR OF TRANSVERSE AREA O(d^2) AND EFFECTIVE THICKNESS h, NORMALIZED PALINSTROPHY OBEYS P_hat >= c max{h/r, d^2/(r h)} >= c d/r / SINCE d/r ~ r^(-1/5) -> infinity, NO CHOICE OF REGULAR THICKNESS BETWEEN SUB-NATURAL AND SHIELD SCALE CAN KEEP THE CANCELLATION RESERVOIR ON A NO-H CORRIDOR / THE PREVIOUS REGULAR SHEET T LEAF IS THEREFORE REABSORBED INTO H / ONLY LOSS OF REGULAR TUBULAR GEOMETRY, UNBOUNDED FRAGMENTATION/MICROSHAPE, OR SPATIAL/NON-TIGHT DESCRIPTION LOSS REMAINS AS T / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-379 derived, for a coherent opposite-sign cancellation reservoir of thickness `h_j`, the static normalized palinstrophy lower bound

\[
\mathfrak P_j
\gtrsim
\frac{h_j}{r_j}.
\]

This is strong for `h_j >> r_j`, but by itself allows the borderline `h_j=O(r_j)` thin-sheet geometry.

M5-380 then showed that if such a thin sheet actually destroys a fixed fraction of the old material circulation, the **spacetime** palinstrophy diverges.

The present note asks an even simpler static question:

\[
\boxed{
\text{Can a regular high-vorticity sheet of width }d_j\text{ and thickness }h_j
\text{ exist at one time without paying H?}
}
\]

The normal transition across the sheet boundary supplies the missing reciprocal-in-thickness estimate.

---

## 2. Scales

Use

\[
W_j\asymp\frac\nu{r_j^2},
\qquad
 d_j\asymp r_j^{4/5},
\qquad
\frac{d_j}{r_j}\asymp r_j^{-1/5}\to\infty.
\]

A fixed-fraction cancellation reservoir must carry transverse flux area

\[
\boxed{
A_j\gtrsim d_j^2
}
\]

by M5-379 and the first-hitting amplitude cap.

---

## 3. Regular coherent sheet model

Assume the cancellation reservoir admits a regular tubular description around a surface patch `Sigma_j` with

\[
|\Sigma_j|\gtrsim d_j^2.
\]

Let `s` be the signed normal coordinate and let `h_j` be the effective coherent thickness.

On a fixed positive fraction of the surface patch, assume the inner reservoir contains opposite-signed high vorticity

\[
|\omega(y,s_{in})|\ge c_1W_j.
\]

By the definition of **effective thickness**, at an outer point a normal distance `O(h_j)` away, at least one of the following occurs:

- the magnitude drops by a fixed fraction;
- the signed direction changes by a fixed amount;
- the field enters the old descendant/opposite environment and differs as a vector by a fixed fraction of `W_j`.

Thus on a positive fraction of normal fibers,

\[
\boxed{
|\omega(y,s_{out})-\omega(y,s_{in})|
\ge c_2W_j.
}
\]

If no such boundary contrast exists, the reservoir remains coherent beyond `h_j`, so `h_j` was not its effective thickness and must be enlarged. Hence the split is exhaustive within the regular tubular model.

---

## 4. One-dimensional normal-fiber cost

For each retained normal fiber, the fundamental theorem of calculus and Cauchy--Schwarz give

\[
 c_2W_j
\le
\int_{s_{in}}^{s_{out}}|\partial_s\omega|ds
\le
h_j^{1/2}
\left(
\int_{s_{in}}^{s_{out}}|\partial_s\omega|^2ds
\right)^{1/2}.
\]

Therefore

\[
\boxed{
\int_{s_{in}}^{s_{out}}|\partial_s\omega|^2ds
\gtrsim
\frac{W_j^2}{h_j}.
}
\]

Integrating over a surface subset of area `>= c d_j^2` and using bounded tubular Jacobian distortion gives

\[
\boxed{
\int_{N_j}|\nabla\omega|^2dx
\gtrsim
\frac{W_j^2d_j^2}{h_j}.
}
\]

This is the reciprocal-thickness interface cost.

---

## 5. Normalize the interface cost

Define, as before,

\[
\mathfrak P_j(N_j)
:=
\frac{r_j^3}{\nu^2}
\int_{N_j}|\nabla\omega|^2dx.
\]

Since

\[
W_j\asymp\frac\nu{r_j^2},
\]

Section 4 yields

\[
\boxed{
\mathfrak P_j(N_j)
\gtrsim
\frac{d_j^2}{r_jh_j}.
}
\]

Equivalently,

\[
\boxed{
\mathfrak P_j
\gtrsim
\left(\frac{d_j}{r_j}\right)^2
\frac{r_j}{h_j}.
}
\]

For a natural-thickness sheet `h_j ~ r_j`, this already gives

\[
\mathfrak P_j
\gtrsim
\left(\frac{d_j}{r_j}\right)^2
\asymp
r_j^{-2/5}.
\]

---

## 6. Combine with the volume-variance bound

M5-379 proved on the same coherent reservoir corridor

\[
\boxed{
\mathfrak P_j
\gtrsim
\frac{h_j}{r_j}.
}
\]

Hence every regular coherent reservoir satisfies the two-sided thickness constraint

\[
\boxed{
\mathfrak P_j
\gtrsim
\max\left\{
\frac{h_j}{r_j},
\frac{d_j^2}{r_jh_j}
\right\}.
}
\]

Set

\[
a_j:=\frac{h_j}{r_j},
\qquad
D_j:=\frac{d_j}{r_j}.
\]

Then

\[
\mathfrak P_j
\gtrsim
\max\{a_j,D_j^2/a_j\}.
\]

For every `a_j>0`,

\[
\max\{a_j,D_j^2/a_j\}
\ge D_j
\]

because the geometric mean of the two terms is exactly `D_j`.

Therefore

\[
\boxed{
\mathfrak P_j
\gtrsim
\frac{d_j}{r_j}.
}
\]

Using the saturated shield exponent,

\[
\boxed{
\mathfrak P_j
\gtrsim
r_j^{-1/5}
\to\infty.
}
\]

This is independent of the choice of regular thickness.

---

## 7. Optimal thickness does not save the sheet

The lower envelope of the two costs occurs when

\[
a_j\asymp D_j,
\]

i.e.

\[
h_j\asymp d_j.
\]

At that formally optimal thickness,

\[
\mathfrak P_j\gtrsim D_j=d_j/r_j\to\infty.
\]

Thus:

- very thin sheets pay the interface-gradient term;
- thick reservoirs pay the volume/vector-variance term;
- intermediate thicknesses pay at least the geometric-mean barrier.

There is no regular-thickness minimizer with bounded normalized palinstrophy.

---

## 8. Sub-natural thickness

If

\[
h_j\ll r_j,
\]

then even before using the combined estimate, the reservoir has sub-natural reach and belongs to

\[
H_{\rm high-freq/der}
\lor
T_{\rm microshape/reach}.
\]

If the tubular geometry remains regular enough for the normal-fiber calculation, the interface bound becomes even larger.

Thus sub-natural thickness is not a quiet escape.

---

## 9. Consequence for M5-379's sheet T

M5-379 concluded that no-H forces a cancellation reservoir toward `O(r_j)` thickness and therefore sheet-like anisotropy.

M5-382 sharpens this:

\[
\boxed{
\text{regular coherent cancellation sheet}
\Longrightarrow
H_{\rm pal/der}.
}
\]

The regular sheet itself should therefore no longer be carried as an independent T leaf.

To remain T rather than H, the cancellation structure must lose at least one regular-sheet property:

- no regular tubular normal field at the needed area scale;
- unbounded curvature/reach degeneration;
- unbounded fragmentation into microcomponents;
- absence of a common shield-scale window;
- loss of coherent high-vorticity occupancy;
- purely descriptive/eulerian cancellation while material charge persists elsewhere.

These are genuine compactness/ancestry/geometry losses.

---

## 10. Relation to M5-380 dynamic destruction

The present static estimate and M5-380 are complementary.

M5-382 says:

\[
\boxed{
\text{a regular coherent opposite reservoir already has divergent instantaneous normalized palinstrophy.}
}
\]

M5-380 says:

\[
\boxed{
\text{if a regular thin layer actually destroys material circulation, its normalized spacetime palinstrophy also diverges.}
}
\]

Thus both the state and the dynamic charge-destruction process return to H under regular geometry.

---

## 11. DSD audit

### Derived

- normal-fiber interface lower bound
  \[
  \mathfrak P_j\gtrsim d_j^2/(r_jh_j);
  \]
- M5-379 volume lower bound
  \[
  \mathfrak P_j\gtrsim h_j/r_j;
  \]
- combined thickness-independent barrier
  \[
  \mathfrak P_j\gtrsim d_j/r_j\asymp r_j^{-1/5}\to\infty.
  \]

### Required regularity

The normal-fiber argument requires a tubular surface patch of area comparable to `d_j^2` with controlled Jacobian at thickness `h_j`.

Failure is **not** treated as zero cost. It is explicitly the remaining T geometry.

### Forbidden inference

Do not conclude that every arbitrary fractal/multifold vorticity set has a regular normal foliation. The result closes the regular-sheet corridor only.

---

## 12. Updated T frontier

After M5-382, no-H opposite-sign cancellation cannot survive as

- a thick coherent reservoir;
- a regular thin sheet;
- a regular material charge-destruction layer.

The cancellation-related T frontier is reduced to

\[
\boxed{
T_{\rm irregular\ reach/curvature}
\lor
T_{\rm fragmentation/microshape}
\lor
T_{\rm spatial/non-tight}
\lor
T_{\rm descriptive\ mix\ with\ material\ charge\ preserved}.
}
\]

The next useful target is to determine whether repeated positive-density `T_irregular/microshape` itself implies high-frequency capacity H, or whether only pure spatial export/return can remain genuinely independent.

---

## 13. Audit verdict

### NEW STATIC RIGIDITY

\[
\boxed{
\mathfrak P_j
\gtrsim
\max\left\{
\frac{h_j}{r_j},
\frac{d_j^2}{r_jh_j}
\right\}
\ge
\frac{d_j}{r_j}
\asymp r_j^{-1/5}\to\infty.
}
\]

### REMOVED AS INDEPENDENT T

Regular coherent cancellation sheet.

### STILL OPEN

- irregular/fractal reach loss;
- fragmentation/microshape without a regular tubular model;
- spatial export/non-tightness;
- material return/recycling;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
