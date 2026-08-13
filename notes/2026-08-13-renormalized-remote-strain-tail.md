# Renormalized remote-strain tail under bounded normalized enstrophy

Date: 2026-08-13

Status: **DERIVED REMOTE-TAIL DECAY / BOUNDED-ENSTROPHY BRANCH LOCALIZATION**.

The local source-gap route leaves a far strain term.  After natural-window renormalization, the far strain and its spatial variation become uniformly small at large normalized radius whenever the normalized global enstrophy remains bounded.

---

## 1. Normalized global enstrophy

At checkpoint `j`, with

\[
r_j=W_j^{-1/2},
\]

the normalized vorticity is

\[
\Omega_j(y)=r_j^2\omega(x_j+r_jy).
\]

Hence

\[
\boxed{
\|\Omega_j\|_2^2
=r_j\|\omega(t_j)\|_2^2
=\frac{E_\omega(t_j)}{\sqrt{W_j}}.
}
\]

Define

\[
\boxed{
\mathfrak e_j
=\|\Omega_j\|_2^2.
}
\]

This is scale invariant under the natural checkpoint normalization.

Assume along the branch

\[
\boxed{
\mathfrak e_j\le M_E.
}
\]

---

## 2. Far strain at the dangerous center

The strain is a zero-order singular integral of vorticity with kernel satisfying

\[
|K(z)|\le C|z|^{-3}.
\]

Let `S_{>R}` denote the contribution from `|z|>R` in normalized coordinates.  Then

\[
|S_{>R}(0)|
\le
C\int_{|z|>R}|z|^{-3}|\Omega_j(z)|dz.
\]

By Cauchy--Schwarz,

\[
|S_{>R}(0)|
\le
C
\left(
\int_{|z|>R}|z|^{-6}dz
\right)^{1/2}
\|\Omega_j\|_2.
\]

In three dimensions,

\[
\int_{|z|>R}|z|^{-6}dz
\asymp R^{-3}.
\]

Therefore

\[
\boxed{
|S_{>R}(0)|
\le
C R^{-3/2}M_E^{1/2}.
}
\]

---

## 3. Far spatial variation

For `|y|<=1` and `R>=2`, the mean-value theorem for the kernel gives

\[
|K(y-z)-K(-z)|
\le
C|y||z|^{-4}
\le
C|z|^{-4}
\]

for `|z|>R`.

Hence

\[
|S_{>R}(y)-S_{>R}(0)|
\le
C\int_{|z|>R}|z|^{-4}|\Omega_j(z)|dz.
\]

Again by Cauchy--Schwarz,

\[
\int_{|z|>R}|z|^{-8}dz
\asymp R^{-5},
\]

so

\[
\boxed{
\sup_{|y|\le1}
|S_{>R}(y)-S_{>R}(0)|
\le
C R^{-5/2}M_E^{1/2}.
}
\]

Thus the far spatial variation has one extra inverse power of normalized distance compared with the far constant strain.

---

## 4. Uniform remote-source smallness

If the local unit-ball enstrophy is also bounded,

\[
E_{B_1,j}\le M_1,
\]

then the far source satisfies

\[
\left|
\int_{B_1}\Omega\cdot S_{>R}\Omega dy
\right|
\le
M_1
\sup_{B_1}|S_{>R}|.
\]

Therefore

\[
\boxed{
|Q_{>R,B_1}|
\le
C M_1M_E^{1/2}
\left(R^{-3/2}+R^{-5/2}\right).
}
\]

For every `epsilon>0`, one may choose one fixed normalized radius `R_epsilon` depending only on the bounded state block such that

\[
\boxed{
|Q_{>R_\varepsilon,B_1}|
\le\varepsilon
}
\]

uniformly along the subsequence.

---

## 5. Consequence for the source-gap program

On the branch

\[
\sup_j\mathfrak e_j<\infty,
\]

the dangerous source is asymptotically local after choosing a sufficiently large fixed normalized buffer.

Hence the strict coefficient deficits from

- angular palinstrophy;
- magnitude heterogeneity;
- projective covariance of the far *buffered constant* part

cannot be refilled by arbitrarily distant vorticity.

The remaining source-gap closure can therefore be performed on a fixed large normalized ball, up to an arbitrarily small remote error.

---

## 6. Complementary concentration branch

If

\[
\boxed{
\mathfrak e_j\to\infty,
}

then remote localization is not uniform from this estimate.  This is retained as a separate scale-invariant **global-enstrophy concentration** channel.

It means

\[
\|\omega(t_j)\|_2^2
\gg
\sqrt{W_j},
\]

so the total vorticity `L2` mass grows much faster than the minimum natural-core floor.

No contradiction is claimed from this fact alone.

---

## 7. Updated compactness dichotomy

The renormalized route now has the clean split

\[
\boxed{
\mathfrak e_j\to\infty
\quad\text{or}\quad
\sup_j\mathfrak e_j<\infty.
}
\]

- unbounded branch: typed global-enstrophy concentration;
- bounded branch: remote strain tail uniformly localizable, allowing the compactness/source-gap analysis on a fixed normalized ball.

Status: **REMOTE TAIL CLOSED ON THE BOUNDED NORMALIZED-ENSTROPHY BRANCH**.
