# Amplification-time noncollapse under bounded renormalized channels

Date: 2026-08-13

Status: **DERIVED CONDITIONAL TIME-NONCOLLAPSE LEMMA / COMPACTNESS PREPARATION**.

The natural-window renormalization introduces the dimensionless duration between vorticity amplification checkpoints.  The Cauchy I/V two-lane bounds show that if all relevant normalized danger channels remain bounded, this duration cannot collapse to zero.

---

## 1. Amplification duration

Let

\[
W_1=qW_0,
\qquad q>1,
\]

and

\[
\tau=t_1-t_0.
\]

Define

\[
\boxed{
\sigma=W_0\tau.
}
\]

Since the natural time is `W0^-1`, `sigma` is exactly the duration measured in natural-time units.

---

## 2. I-lane normalized strain cost

Suppose the I-lane occupies at least half of a thick final natural core.  The Cauchy contribution lemma gives

\[
\int_I\int_{X(A_I,t)}|S|^2dxdt
\ge
\frac{|C_1|}{2\tau}
\left(\log\frac{bq}{2}\right)^2.
\]

For

\[
|C_1|\ge c(qW_0)^{-3/2},
\]

we obtain

\[
\int_I\int|S|^2
\ge
c q^{-3/2}
W_0^{-1/2}
\frac{(\log(bq/2))^2}{\sigma}.
\]

The scale-invariant normalized strain spacetime cost is

\[
\boxed{
\mathcal S_I
=W_0^{1/2}
\int_I\int_{X(A_I,t)}|S|^2dxdt.
}
\]

Hence

\[
\boxed{
\mathcal S_I
\ge
c q^{-3/2}
\frac{(\log(bq/2))^2}{\sigma}.
}
\]

Therefore a bounded normalized I-lane strain cost forces a positive lower bound on `sigma`.

---

## 3. V-lane normalized `k=2` cost

If instead the V-lane occupies at least half of the final core, then

\[
\int_I\int|\Delta\omega|^2
\ge
c
\frac{q^{1/2}}
{\nu^2K_+^2K_-^2\sigma}
W_0^{3/2}.
\]

Define the scale-invariant normalized cost

\[
\boxed{
\mathcal V_2
=W_0^{-3/2}
\int_I\int|\Delta\omega|^2dxdt.
}
\]

Then

\[
\boxed{
\mathcal V_2
\ge
c
\frac{q^{1/2}}
{\nu^2K_+^2K_-^2\sigma}.
}
\]

Thus, if the recent forward/inverse deformation bounds and `V2` channel are all uniformly bounded, `sigma` again has a positive lower bound.

If `K_+K_-` is unbounded, the deformation/condition-number channel itself is already unbounded and compactness in the full bounded-state block has failed for a typed reason.

---

## 4. Conditional time-noncollapse statement

Fix `q,b,nu` and assume `bq>2`.  Suppose along a sequence of amplification windows the following renormalized channels are uniformly bounded:

\[
\mathcal S_I\le M_S,
\qquad
\mathcal V_2\le M_2,
\qquad
K_+K_-\le M_K.
\]

At least one of the two Cauchy lanes occupies half of each final core.  Consequently there is

\[
\boxed{
\sigma_*=\sigma_*(q,b,\nu,M_S,M_2,M_K)>0
}
\]

such that

\[
\boxed{
\sigma_j\ge\sigma_*
}
\]

on every window in the bounded-channel sequence.

This is a conditional but exact structural consequence of the earlier lane estimates.

---

## 5. Compactness consequence

After natural rescaling, the amplification interval has normalized length `sigma_j`.

The time-noncollapse lemma means that a sequence for which all tracked critical channels remain bounded automatically contains a **nondegenerate fixed backward/forward time segment** after choosing a common subwindow of length less than `sigma_*`.

Hence a compactness attempt does not suffer from the observation windows collapsing instantaneously.

The remaining compactness requirements are spatial/local function-space bounds and pressure/time-derivative control; these are not proved automatically here.

---

## 6. Residual fast-amplification branch

If instead

\[
\sigma_j\to0,
\]

then at least one normalized channel must diverge:

\[
\boxed{
\mathcal S_I\to\infty,
\quad\text{or}\quad
\mathcal V_2\to\infty,
\quad\text{or}\quad
K_+K_-\to\infty.
}
\]

Thus fast amplification is no longer an untyped escape.  It is explicitly routed into

1. strain concentration;
2. second-vorticity-derivative concentration;
3. or material condition-number blowup.

Status: **FAST AMPLIFICATION TYPED / BOUNDED-CHANNEL TIME NONCOLLAPSE DERIVED**.
