# Super-separated Zeno probes have automatic Bessel geometry

Date: 2026-08-15

Status: **DERIVED SCALE-SEPARATION/BESSEL LEMMA FOR ONE RESET-SELECTED PROBE PER SCALE / SUPER-SEPARATED ZENO IS NOT A FRAME-FAILURE BRANCH.**

This note refines the remaining bounded-distortion reset branch.

The vector-valued reset packing lemma assumed a uniform Bessel geometry for the material probes. For a reset-separated super-Zeno subsequence, geometric scale separation itself is enough to provide this Bessel property, under the already stated bounded-shape-distortion assumptions.

---

## 1. Physical scale in terms of `(W,R,q)`

At a coherent Reynolds-one crossing,

\[
\ell=\frac{R}{\sqrt W}.
\]

Define

\[
q=\frac{W}{R^{10}}.
\]

Since

\[
R=\ell\sqrt W,
\]

we have

\[
q
=\frac{1}{\ell^{10}W^4}.
\]

Equivalently,

\[
\boxed{
\ell=q^{-1/10}W^{-2/5}.
}
\]

---

## 2. Reset-separated amplitude sequence

Take a sequence of genuinely reset-separated coherent crossings such that the previous selected crossing lies no later than the automatic reset checkpoint for the next one.

Then the first-hitting amplitudes satisfy schematically

\[
\boxed{
\frac{W_j}{W_{j-1}}
\ge c q_j
}
\]

up to the fixed reset-threshold constants.

Since any super-separated sequence has `q_j->infinity`, choose an infinite subsequence on which `q_j` is nondecreasing.

Then

\[
\begin{aligned}
\frac{\ell_j}{\ell_{j-1}}
&=
\left(\frac{q_j}{q_{j-1}}\right)^{-1/10}
\left(\frac{W_j}{W_{j-1}}\right)^{-2/5}\\
&\lesssim
q_j^{-2/5}.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{\ell_j}{\ell_{j-1}}
\to0.
}
\]

In particular, after discarding finitely many terms,

\[
\boxed{
\ell_{j+1}\le\frac12\ell_j.
}
\]

Thus the physical reset probes become at least dyadically separated in scale, and in fact much more strongly separated when `q_j` is large.

---

## 3. Abstract one-probe-per-scale Bessel lemma

Let

\[
p_j(x)=\ell_j^{-3/2}P_j\left(\frac{x-a_j}{\ell_j}\right),
\]

where the centers `a_j` are arbitrary and the normalized shapes obey uniform bounds

\[
\|P_j\|_1+\|P_j\|_2+\|P_j\|_\infty\le C_P.
\]

Assume geometric scale separation

\[
\ell_k\le\theta^{k-j}\ell_j,
\qquad k>j,
\qquad 0<\theta<1.
\]

For `k>j`, use `L-infinity x L1`:

\[
\begin{aligned}
|\langle p_j,p_k\rangle|
&\le\|p_j\|_\infty\|p_k\|_1\\
&\lesssim
\ell_j^{-3/2}\ell_k^{3/2}\\
&=
C_P\left(\frac{\ell_k}{\ell_j}\right)^{3/2}.
\end{aligned}
\]

Therefore

\[
\boxed{
|\langle p_j,p_k\rangle|
\lesssim
\theta^{\frac32|k-j|}.
}
\]

The Gram matrix has uniformly summable rows and columns. Schur's test yields

\[
\boxed{
\sum_j|\langle g,p_j\rangle|^2
\le C_{P,\theta}\|g\|_2^2.
}
\]

Thus one smooth normalized probe per geometrically separated scale is automatically a Bessel family, independently of the motion of its center.

No mean-zero condition is needed for a single scale chain because the volume normalization already gives geometric off-diagonal decay.

---

## 4. Apply to the Laplacian probe family

For the material-flux reset lemma, the second normalized family is

\[
\boxed{
k_j=\ell_j^{3/2}\Delta\psi_j.}
\]

Under uniform bounded `C2` material-probe distortion, `k_j` has the same form

\[
k_j(x)=\ell_j^{-3/2}K_j((x-a_j)/\ell_j)
\]

with uniform `L1/L2/Linfinity` shape bounds.

Therefore the same Gram/Schur argument gives

\[
\boxed{
\sum_j|\langle g,k_j\rangle|^2
\le C\|g\|_2^2.
}
\]

Hence both Bessel hypotheses required by the vector-valued reset packing lemma are automatic on the scale-separated bounded-distortion subsequence.

---

## 5. Consequence for the final branch

A genuine super-separated reset subsequence has

\[
q_j\to\infty,
\qquad
\ell_{j+1}/\ell_j\to0.
\]

Therefore it cannot evade the vector reset packing estimate merely by claiming loss of probe-frame orthogonality.

On the bounded-distortion track,

\[
\boxed{
\sum_jq_j^{-1/2}<\infty
}
\]

is the real residual condition.

The remaining alternatives are now cleanly separated:

1. **super-separated summable Zeno**: scale geometry is good, reset costs shrink fast enough to be summable;
2. **material-probe derivative distortion**: normalized probe shapes themselves lose the bounded `C2/H2` class.

Generic interval overlap or center motion is no longer a third independent issue for a reset-selected one-probe-per-scale subsequence.

---

## 6. Limitation

The reduction uses a reset-separated subsequence with one genuinely new reset probe per physical scale chain. A highly branched multicore family requires the separate multicore aggregation / spatial packing arguments already present in the repository.

Most importantly, summability

\[
\sum_jq_j^{-1/2}<\infty
\]

is compatible with finite energy. The present lemma does not contradict it.

Status: **SUPER-SEPARATED ZENO AUTOMATICALLY HAS GOOD BESSEL FRAME GEOMETRY / TRUE LAST BOUNDED-DISTORTION ESCAPE = SUMMABLE RESET COST.**