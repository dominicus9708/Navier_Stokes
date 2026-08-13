# Projective coherence forces vortex-stretching collapse on a bounded `H1` state block

Date: 2026-08-13

Status: **DERIVED GLOBAL QUANTITATIVE COHERENCE DEPLETION / LOCAL BUFFERED VERSION VIA EXISTING TAIL CHANNELS**.

The rough branch carries coefficient deficits.  The complementary nearly-one-axis branch can be treated directly: for a fixed optimal projective axis, the exact constant-axis strain/off-axis identity implies that the vortex-stretching source tends to zero as the off-axis `L2` vorticity tends to zero, provided the `H1` state block remains bounded.

---

## 1. Constant-axis decomposition

Fix a constant unit vector `n` and write

\[
\boxed{
\omega=\alpha n+\beta,
\qquad
\alpha=n\cdot\omega,
\qquad
\beta=P_{n^\perp}\omega.
}
\]

Then

\[
|\beta|=|n\times\omega|.
\]

Let

\[
B=\|\beta\|_2.
\]

The already-derived exact Fourier identity gives

\[
\boxed{
2\|Sn\|_2=B.
}
\]

---

## 2. Split the vortex-stretching source

The enstrophy source is

\[
Q=\int\omega\cdot S\omega dx.
\]

Substitute the axis decomposition:

\[
\boxed{
Q
=
\int\alpha^2 n\cdot Sn
+2\int\alpha\,\beta\cdot Sn
+\int\beta\cdot S\beta.
}
\]

All three terms contain at least one off-axis/axis-strain factor.

---

## 3. Bounded `H1` block

Assume

\[
\boxed{
\|\omega\|_{H^1(\mathbb R^3)}\le M.
}
\]

Because `n` is constant,

\[
\|\alpha\|_{H^1}
+\|\beta\|_{H^1}
\le C M.
\]

Sobolev/interpolation gives

\[
\|\alpha\|_4^2\le C M^2,
\qquad
\|\alpha\|_6\le CM,
\]

\[
\|\beta\|_6\le CM,
\qquad
\|\beta\|_3
\le
\|\beta\|_2^{1/2}\|\beta\|_6^{1/2}
\le C M^{1/2}B^{1/2}.
\]

The strain is a zero-order singular integral of vorticity, so

\[
\|S\|_3\le C\|\omega\|_3\le CM.
\]

---

## 4. Bound the three source pieces

For the axial piece,

\[
\left|
\int\alpha^2 n\cdot Sn
\right|
\le
\|\alpha\|_4^2\|Sn\|_2
\le
C M^2 B.
\]

For the cross piece,

\[
\begin{aligned}
\left|
2\int\alpha\,\beta\cdot Sn
\right|
&\le
2\|\alpha\|_6
\|\beta\|_3
\|Sn\|_2\\
&\le
C M^{3/2}B^{3/2}.
\end{aligned}
\]

For the purely off-axis piece,

\[
\begin{aligned}
\left|
\int\beta\cdot S\beta
\right|
&\le
\|S\|_3\|\beta\|_3^2\\
&\le
C M^2B.
\end{aligned}
\]

Therefore

\[
\boxed{
|Q|
\le
C
\left[
M^2B
+M^{3/2}B^{3/2}
\right].
}
\]

For a uniformly bounded `M`, this implies

\[
\boxed{
B\to0
\Longrightarrow
Q\to0.
}
\]

---

## 5. Express `B` by the optimal covariance defect

Let

\[
C_\omega
=
\frac{\int\omega\otimes\omega dx}{E},
\qquad
E=\|\omega\|_2^2,
\]

and let `n` be a principal eigenvector with largest eigenvalue `mu1`.

Then

\[
\boxed{
B^2
=\|n\times\omega\|_2^2
=E(1-\mu_1)
=E\Pi.
}
\]

Hence

\[
\boxed{
|Q|
\le
C
\left[
M^2(E\Pi)^{1/2}
+M^{3/2}(E\Pi)^{3/4}
\right].
}
\]

If `E` and `M` are uniformly bounded,

\[
\boxed{
\Pi\to0
\Longrightarrow
Q\to0.
}
\]

Thus the exactly one-axis limit has zero vortex-stretching source, and near-one-axis states have quantitatively depleted source on the bounded `H1` block.

---

## 6. Complementarity with the rough branch

The current bounded-state geometry now has a direct dichotomy.

### Coherent branch

\[
\Pi\to0.
\]

Then

\[
Q\to0.
\]

### Rough branch

\[
\Pi\ge\pi_0>0
\]

or equivalently a comparable projective dispersion remains positive.  Then the projective Poincare / angular-palinstrophy / covariance-gap mechanisms supply strict coefficient depletion.

Therefore

\[
\boxed{
\text{projective coherence}
\Rightarrow
\text{stretching collapse},
}
\]

while

\[
\boxed{
\text{projective roughness}
\Rightarrow
\text{source coefficient deficits or derivative concentration}.
}
\]

This removes the misleading idea that perfect axis coherence might be the most dangerous stretching configuration.  For a globally constant axis it is instead a zero-stretching limit.

---

## 7. Local normalized use

The proof route is local rather than globally `H1` bounded.  On a fixed large normalized buffer:

1. use the local covariance axis on the dangerous cluster;
2. use the variable-axis commutator estimate for slow axis bending;
3. use the finite-shell selector to control cutoff leakage;
4. use bounded normalized global enstrophy to make the remote strain tail arbitrarily small.

The global estimate above is therefore the clean baseline for a buffered local coherence-depletion lemma.

The local commutator and far-tail errors must remain explicit; they are not set to zero.

---

## 8. Current rigidity consequence

On a compact bounded normalized sequence, a hypothetical source-active limiting profile cannot survive by driving projective defect to zero, because that collapses the stretching source.

If it keeps projective defect away from zero, the magnitude/direction/covariance strict-gap program becomes active.

Hence a residual source-saturating state has no neutral projective limit:

\[
\boxed{
\Pi\to0
\Rightarrow Q\to0,
\qquad
\Pi\not\to0
\Rightarrow \text{strict-gap branch}.
}
\]

Status: **GLOBAL COHERENCE DEPLETION DERIVED / LOCAL UNIFORMIZATION REMAINS**.
