# Zero angular palinstrophy is rigid: compact nontrivial divergence-free families have an angular gap

Date: 2026-08-13

Status: **EXACT ZERO-ANGULAR RIGIDITY + COMPACT-FAMILY ANGULAR GAP**.

The canonical sharp-GN source estimate contains the exact angular reserve

\[
P_{\rm ang}
=P-\|\nabla|\Omega|\|_2^2.
\]

This reserve cannot vanish for a nonzero finite-enstrophy divergence-free field.  On a strongly compact nontrivial family with uniformly bounded total palinstrophy, it therefore has a positive uniform lower bound and a positive angular fraction.

---

## 1. Exact pointwise split

Let

\[
\rho=|\Omega|.
\]

On the nonzero set write

\[
\Omega=\rho\xi,
\qquad |\xi|=1.
\]

Then

\[
\boxed{
|\nabla\Omega|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
}
\]

Define globally

\[
\boxed{
P_{\rm ang}
=\|\nabla\Omega\|_2^2
-\|\nabla|\Omega|\|_2^2
\ge0.
}
\]

On the nonzero set this equals

\[
\int\rho^2|\nabla\xi|^2.
\]

---

## 2. If `P_ang=0`, every positive component has constant direction

Assume

\[
P_{\rm ang}=0.
\]

Then

\[
\rho^2|\nabla\xi|^2=0
\]

almost everywhere, so the direction is constant on every Sobolev-connected positive-vorticity component:

\[
\boxed{
\Omega=\rho n
}
\]

with one constant unit vector `n` on that component.

---

## 3. Divergence-free forbids a finite-energy one-axis positive component

Inside such a component,

\[
0=\nabla\cdot\Omega
=n\cdot\nabla\rho.
\]

Rotate coordinates so `n=e3`.  Then

\[
\partial_3\rho=0
\]

where `rho>0`.

Use the absolutely-continuous-on-lines property of `H1` functions.  For almost every transverse point `x_perp`,

\[
g(s)=\rho(x_\perp+sn)
\]

belongs to `H1(R)` and satisfies

\[
g'(s)=0
\]

for almost every `s` such that `g(s)>0`.

A nonnegative `H1(R)` function cannot have a positive finite interval on which it is a nonzero constant and then join continuously to zero at the interval endpoints while its derivative vanishes on the positive set.  Thus each positive level interval must either be absent or extend along the whole line.

If it extends along the whole line with positive value, its `L2(R)` norm is infinite.

Since

\[
\Omega\in L^2(\mathbb R^3),
\]

this is impossible on a positive-measure family of lines.

Therefore

\[
\boxed{
P_{\rm ang}=0,
\quad
\Omega\in H^1\cap L^2,
\quad
\nabla\cdot\Omega=0
\Longrightarrow
\Omega\equiv0.
}
\]

This generalizes the earlier global fixed-axis rigidity: even piecewise one-axis direction separated through zero-vorticity regions cannot produce a nonzero finite-energy `H1` field with zero angular palinstrophy.

---

## 4. Compact-family positive gap

Let `Omega_j` be a sequence with

\[
\boxed{
\|\Omega_j\|_{H^1}\le M
}
\]

and assume, after a subsequence,

\[
\Omega_j\to\Omega_\infty
\quad\text{strongly in }H^1_{\rm loc}
\]

with a nontrivial local lower bound

\[
\boxed{
\|\Omega_\infty\|_{L^2(B_1)}\ge c_0>0.
}
\]

Also assume the global `L2` norms stay uniformly bounded so that the local limit belongs to the global weak `L2` limit and is finite enstrophy.

Suppose for contradiction

\[
P_{{\rm ang},j}\to0.
\]

Then on every fixed ball the angular defect tends to zero.  Strong local `H1` convergence and continuity of the Sobolev modulus composition imply the limit has

\[
P_{{\rm ang},\infty}=0
\]

locally, and hence globally by exhaustion.

The exact rigidity above gives

\[
\Omega_\infty\equiv0,
\]

contradicting the nontrivial local mass.

Therefore

\[
\boxed{
\liminf_j P_{{\rm ang},j}>0.
}
\]

---

## 5. Positive angular fraction on the first-hitting bounded branch

The first-hitting V2 bootstrap gives, on the bounded normalized-enstrophy branch and terminal subwindow,

\[
\boxed{
P_j=\|\nabla\Omega_j\|_2^2
\le M_P.
}
\]

Combining with the compact-family lower gap gives

\[
\boxed{
\eta_{{\rm ang},j}
=\frac{P_{{\rm ang},j}}{P_j}
\ge
\eta_0>0
}

along the compact nontrivial subsequence.

Hence the canonical sharp-GN source factor satisfies

\[
\boxed{
(1-\eta_{{\rm ang},j})^{3/4}
\le
(1-\eta_0)^{3/4}<1.
}

This is a genuine compactness-rigidity coefficient gap that survives the sharp-GN audit correction.

---

## 6. Relation to projective covariance

`P_ang` measures spatial change of the vorticity direction weighted by magnitude.  Projective covariance `J` measures directional dispersion across a region even when different directions are spatially separated.

They are complementary rather than identical.

The present rigidity says a nonzero finite-enstrophy divergence-free field cannot make **all** angular change disappear.  The multicore covariance identity says spatially separated axis differences also create a positive aggregate projective channel.

Together they prevent a compact nontrivial residual family from collapsing every direction-related descriptor simultaneously.

---

## 7. Claim boundary

The positive constants `a0,eta0` are family/compactness dependent; no universal numerical value is claimed here.

The result is used on the bounded normalized-enstrophy first-hitting branch, where the strong local compactness and terminal palinstrophy upper bound have already been derived.

Status: **ANGULAR FRACTION CANNOT VANISH ON THE COMPACT NONTRIVIAL BOUNDED BRANCH**.
