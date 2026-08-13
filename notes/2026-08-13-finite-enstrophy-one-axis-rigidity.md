# Finite-enstrophy one-axis rigidity and a compactness projective gap

Date: 2026-08-13

Status: **EXACT DIVERGENCE-FREE RIGIDITY + COMPACTNESS COROLLARY**.

An exactly one-axis divergence-free vorticity field cannot be both nonzero and square integrable on all of `R^3`.  This simple fact turns projective-axis collapse into a genuine contradiction on the bounded-normalized-enstrophy compactness branch.

---

## 1. Exact one-axis rigidity

Let

\[
\omega\in L^2(\mathbb R^3;\mathbb R^3)
\]

be divergence free and suppose there is one fixed unit vector `n` such that

\[
\boxed{
\omega(x)=\alpha(x)n
}
\]

almost everywhere.

Then

\[
0=\nabla\cdot\omega
=n\cdot\nabla\alpha
\]

in distributions.

After rotating coordinates so `n=e_3`,

\[
\partial_3\alpha=0.
\]

Hence

\[
\alpha(x_1,x_2,x_3)
=a(x_1,x_2)
\]

for some distribution/function `a`.

If `a` is nonzero on a set of positive two-dimensional measure, then

\[
\int_{\mathbb R^3}|\alpha|^2dx
=
\int_{\mathbb R^2}|a(x_1,x_2)|^2dx_1dx_2
\int_{\mathbb R}dx_3
=\infty.
\]

Since `omega in L2`, this is impossible.

Therefore

\[
\boxed{
\omega\in L^2,
\quad
\nabla\cdot\omega=0,
\quad
\omega\parallel n\text{ globally}
\Longrightarrow
\omega\equiv0.
}
\]

---

## 2. Fourier interpretation

The same rigidity can be read in Fourier space.  If

\[
\widehat\omega(\xi)=\widehat\alpha(\xi)n
\]

and

\[
\xi\cdot\widehat\omega(\xi)=0,
\]

then

\[
(\xi\cdot n)\widehat\alpha(\xi)=0.
\]

Thus a nonzero one-axis divergence-free field would have Fourier support in the plane

\[
\xi\cdot n=0,
\]

a measure-zero set.  An `L2` Fourier function supported there is zero almost everywhere.

This is the spectral version of the physical-space argument.

---

## 3. Compactness projective-gap corollary

Let `Omega_j` be normalized vorticity fields satisfying

\[
\boxed{
\|\Omega_j\|_{L^2(\mathbb R^3)}^2
\le M_E.
}
\]

Assume:

1. `div Omega_j=0`;
2. after a subsequence, `Omega_j -> Omega_infty` strongly in local `L2`;
3. the limit is nontrivial on a fixed ball:
   \[
   \|\Omega_\infty\|_{L^2(B_1)}>0;
   \]
4. `Pi_j` is the optimal global constant-axis covariance defect:
   \[
   \Pi_j
   =\min_{|n|=1}
   \frac{\|n\times\Omega_j\|_2^2}
   {\|\Omega_j\|_2^2}.
   \]

Suppose for contradiction

\[
\Pi_j\to0.
\]

Choose minimizing principal axes `n_j`.  Compactness of the unit sphere gives, after a subsequence,

\[
n_j\to n.
\]

Since

\[
\|n_j\times\Omega_j\|_2^2
\le M_E\Pi_j,
\]

we have

\[
n_j\times\Omega_j\to0
\quad\text{strongly in }L^2.
\]

Also

\[
\|(n-n_j)\times\Omega_j\|_2
\le
|n-n_j|M_E^{1/2}
\to0.
\]

Thus

\[
\boxed{
n\times\Omega_j\to0
\quad\text{strongly in }L^2.}
\]

The global `L2` bound gives a weak `L2` subsequence with limit `Omega_infty`; local strong convergence identifies the same limit.  Passing to the limit,

\[
\boxed{
n\times\Omega_\infty=0.}
\]

Divergence-free also passes to the limit.  The exact one-axis rigidity therefore gives

\[
\Omega_\infty=0,
\]

contradicting local nontriviality.

Hence

\[
\boxed{
\liminf_{j\to\infty}\Pi_j>0.
}
\]

---

## 4. Meaning for the normalized residual branch

On a sequence with

- bounded normalized global enstrophy;
- local strong vorticity compactness;
- persistent nontrivial local vorticity mass;

**global projective covariance cannot collapse to one axis.**

Thus the compact bounded branch has a genuine projective lower gap:

\[
\boxed{
\Pi_{\rm global}\ge\pi_0>0
}
\]

along a subsequence.

This complements the source estimate:

- global exact one-axis limit is impossible by finite enstrophy + divergence free;
- local near-one-axis stretching is depleted by the constant/variable-axis strain identities;
- any closure of a locally coherent finite-energy structure must create off-axis geometry somewhere at finite or escaping normalized distance.

---

## 5. Local versus global caveat

The corollary concerns the **global optimal constant-axis defect**.  A unit dangerous core can still be locally nearly one-axis while compensating/off-axis vorticity exists outside that core.

The current proof route handles that geometry using

1. finite shell escalation;
2. bounded normalized global enstrophy;
3. oriented-flux persistence/side-leakage;
4. remote-strain tail decay.

Therefore the result does not identify the exact radius at which projective roughness must appear.  It shows that on the compact finite-enstrophy branch such roughness **must appear somewhere** and cannot be pushed entirely out of the limiting state.

---

## 6. DSD interpretation

A globally one-axis projective state is not merely a special low-complexity channel assignment.  Under divergence-free and finite-enstrophy constraints it is the **zero state**.

Thus the DSD axis descriptor acquires a sharp admissibility rule on this application:

\[
\boxed{
\text{nonzero finite-enstrophy incompressible vorticity}
\Rightarrow
\text{nonzero global projective multi-axis defect}.
}
\]

For an individual field the defect may be arbitrarily small, so no universal numerical lower constant is claimed.  The positive lower gap arises only after adding compactness and nontriviality of a sequence.

Status: **EXACT RIGIDITY / COMPACT NONTRIVIAL GLOBAL-PROJECTIVE GAP DERIVED**.
