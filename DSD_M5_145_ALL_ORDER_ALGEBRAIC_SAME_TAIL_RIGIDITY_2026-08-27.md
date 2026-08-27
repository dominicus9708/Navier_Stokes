# DSD M5-145 — All-Order Algebraic Same-Tail Rigidity

Date: 2026-08-27

Status: **P1_A CLOSED AT EVERY FINITE ALGEBRAIC ORDER / TWO STATES IN THE SAME COMPACT MINIMAL W1 SET WITH THE SAME CANONICAL TAIL HAVE IDENTICAL INTEGER FUCHSIAN/THE TERMINAL TAYLOR COEFFICIENTS TO EVERY FINITE ORDER / THE ONLY REMAINING SAME-TAIL FREEDOM IS FUCHSIAN-FLAT AT `z=0` / THIS DOES NOT PROVE TAIL-FACTOR INJECTIVITY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Use the exact M5-136 variables

\[
z=r^{-2},\qquad \eta=\log r-\frac s2,
\]

and write the realized integer-sector finite jets

\[
H(z,\eta,\theta)
=\sum_{j=0}^{N}z^jH_j(\eta,\theta)+O(z^{N+1}),
\]

\[
\Pi(z,\eta,\theta)
=\sum_{j=0}^{N}z^j\Pi_j(\eta,\theta)+O(z^{N+1}).
\]

M5-139 justifies the integer terminal/Taylor sector for every finite order in an actual W1 realization: half-integer powers are excluded by punctured terminal smoothness.

Let `V,W` be two states in the same compact minimal W1 set `M` with

\[
T_V=T_W.
\]

Then their leading velocity factors agree:

\[
H_0^V=H_0^W=\Phi.
\]

M5-134 and M5-144 also give equality of the realized leading pressure coefficient, including the critical dipole:

\[
\Pi_0^V=\Pi_0^W.
\]

---

## 2. Degree bookkeeping in the exact Fuchsian system

Recall

\[
D=\partial_\eta-2z\partial_z.
\]

For a coefficient `z^j f_j`,

\[
D(z^jf_j)=z^j(\partial_\eta-2j)f_j.
\]

Hence `D`, `D^2`, angular derivatives, and the pressure Poisson operator preserve `z` degree.

The velocity equation is

\[
H_z
=
-\nu(D^2-D+\Delta_{S^2})H
+\mathcal B_D(H)
+\theta(D\Pi-2\Pi)
+\nabla_{S^2}\Pi.
\]

Its coefficient at degree `z^(n-1)` has the triangular form

\[
\boxed{
 nH_n
 =
 \mathcal F_{n-1}
 \bigl(H_0,\ldots,H_{n-1},\Pi_{n-1}\bigr),
}
\]

where `mathcal F_(n-1)` contains viscous terms built from `H_(n-1)`, quadratic terms `H_i,H_j` with `i+j=n-1`, and the pressure coefficient `Pi_(n-1)`.

Crucially, `H_n` does not occur on the right at this degree.  The nonzero scalar divisor `n` is the M5-135 velocity nonresonance.

---

## 3. Pressure source is one order lower and triangular

The exact pressure equation is

\[
-\left(D^2-3D+2+\Delta_{S^2}\right)\Pi
=\mathcal Q_D[H].
\]

Because `mathcal Q_D` is quadratic in scaled first derivatives of `H` and `D` preserves degree, the coefficient `Q_(n-1)` of `z^(n-1)` depends only on

\[
H_0,\ldots,H_{n-1}.
\]

Therefore if

\[
H_j^V=H_j^W\qquad(0\le j\le n-1),
\]

then

\[
Q_{n-1}^V=Q_{n-1}^W.
\]

The pressure difference

\[
\delta\Pi_{n-1}:=\Pi_{n-1}^V-\Pi_{n-1}^W
\]

therefore solves the homogeneous order-`n-1` pressure equation.

---

## 4. The only bounded homogeneous pressure difference is the realized odd resonance

M5-137, with the M5-138/M5-139 scope correction, gives for the actual integer sector:

\[
\ker_{\mathrm{bounded},n-1}
=\mathcal H_{2n-1}(S^2),
\]

with the kernel coefficient independent of `eta`.

Hence

\[
\delta\Pi_{n-1}
=\sum_m c_{n-1,m}Y_{2n-1,m}(\theta).
\]

But M5-144 proves every realized coefficient in this odd pressure resonance tower is a continuous flow-invariant functional and is therefore constant on the entire compact minimal set `M`.

Since `V,W in M`,

\[
\boxed{
 c_{n-1,m}=0\quad\forall m.
}
\]

Thus

\[
\boxed{
\Pi_{n-1}^V=\Pi_{n-1}^W.
}
\]

---

## 5. Velocity coefficient follows uniquely

Subtract the degree-`z^(n-1)` velocity equations.

All lower velocity coefficients agree by the induction hypothesis, and the pressure coefficient just proved equal. Therefore

\[
n(H_n^V-H_n^W)=0.
\]

Since `n>=1`,

\[
\boxed{
H_n^V=H_n^W.
}
\]

There is no velocity resonance at positive integer Fuchsian order.

The divergence-free constraint introduces no new free coefficient: both realized solutions satisfy it, and once the velocity coefficient difference is zero its order-`n` difference is identically satisfied.

---

## 6. Induction

### Base

Same tail gives

\[
H_0^V=H_0^W.
\]

The realized leading pressure factor also agrees by M5-134/M5-144:

\[
\Pi_0^V=\Pi_0^W.
\]

The degree-zero velocity recursion therefore gives

\[
H_1^V=H_1^W.
\]

### Step

Assume

\[
H_j^V=H_j^W\quad(0\le j\le n-1).
\]

Then:

1. the order-`n-1` pressure sources are equal;
2. the pressure difference is only the degree `2n-1` harmonic resonance;
3. M5-144 forces that realized resonance coefficient equal on `M`;
4. hence `Pi_(n-1)` agrees;
5. the nonresonant velocity recursion gives `H_n^V=H_n^W`.

Thus the induction closes for every finite `n`.

---

## 7. All-order algebraic rigidity

For every finite `N`,

\[
\boxed{
H_j^V=H_j^W,
\qquad
\Pi_j^V=\Pi_j^W,
\qquad
0\le j\le N.
}
\]

Equivalently, the same-tail difference has no algebraic Fuchsian/Taylor jet:

\[
\boxed{
H^V-H^W=O(z^N)
\quad\text{for every finite }N
}
\]

on each fixed compact `(eta,theta)` window, with analogous statements for pressure and finite derivatives allowed by the punctured terminal regularity package.

This is a **flatness statement**, not convergence of the formal Taylor series.

No analyticity is assumed.

---

## 8. Physical interpretation

M5-139 gives

\[
z=\frac{T_*-t}{|x-x_*|^2}
\]

at fixed punctured physical position.

Therefore two same-tail W1 realizations have physical difference `w=u_V-u_W` satisfying, for every fixed punctured compact set `K` and every `N`,

\[
\boxed{
\|w(t)\|_{C^k(K)}
=O_K\bigl((T_*-t)^N\bigr)
}
\]

for each fixed finite derivative order `k` after choosing the corresponding finite terminal jet order.

Thus the difference vanishes to infinite order in terminal time away from the singular center.

---

## 9. DSD four-chain audit

### Formation — GREEN

Only realized finite-order jets supplied by punctured terminal smoothness are used.  No formal convergent series is assumed.

### Axis — GREEN

Taylor/Fuchsian order, genealogical coordinate, and spherical harmonic rank are kept separate.

### Static aggregation — GREEN

A pressure harmonic resonance is not counted as an independent fiber variable once M5-144 has shown its realized coefficient is a minimal-set invariant.

### Dynamics — GREEN

Minimality is used only on already continuous realized resonance coefficients; the velocity recursion itself is purely local/algebraic in Fuchsian order.

### Cross-audit — GREEN

The proof is triangular and forward-only:

\[
\text{equal lower velocity data}
\to
\text{equal pressure source}
\to
\text{resonance only}
\to
\text{minimality removes resonance difference}
\to
\text{equal next velocity coefficient}.
\]

No higher coefficient is used to justify a lower one.

---

## 10. What P1 becomes

The algebraic fiber gate `P1_A` is closed inside the audited W1 minimal class.

Any remaining noninjective same-tail pair must satisfy

\[
\boxed{
H^V-H^W\text{ is Fuchsian-flat at }z=0.
}
\]

Thus

\[
\boxed{
P1\ \longrightarrow\ P1_B:
\text{flat boundary-to-core nonuniqueness only}.
}
\]

This is substantially narrower than a generic strong-`L3` same-tail difference.

---

## 11. Remaining limitation

A `C^infinity` function can be flat at `z=0` without vanishing identically.  Therefore all-order jet equality does not imply

\[
V=W.
\]

Closing `P1_B` requires a genuine flat-boundary uniqueness theorem for the degenerate Fuchsian/physical backward problem, or an independent W1 recurrence argument that excludes flat core-localized modes.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]