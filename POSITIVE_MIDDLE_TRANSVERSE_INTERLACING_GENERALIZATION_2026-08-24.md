# Positive-Middle Transverse Interlacing Generalization — 2026-08-24

Status: **ALIGNMENT-FREE TRANSVERSE RIBBON ACTION LEMMA / GLOBAL REGULARITY NOT PROVED.**

This note removes the alignment assumption `xi ~= e3` from the positive-middle transverse-ribbon mechanism.

## 1. Strain relative to an arbitrary vorticity direction

Let `S` be a symmetric trace-free `3 x 3` matrix with ordered eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3.
\]

Let `xi` be an arbitrary unit vector and define

\[
\gamma=\xi^TS\xi.
\]

Let

\[
P=I-\xi\otimes\xi
\]

and consider the compression of `S` to the transverse plane

\[
C=P S P|_{\xi^\perp}.
\]

Let its eigenvalues be

\[
\mu_1\le\mu_2.
\]

Because `tr S=0`,

\[
\boxed{
\mu_1+\mu_2
=\operatorname{tr}_{\xi^\perp}C
=-\gamma.
}
\]

Thus positive vorticity stretching `gamma>0` means the transverse area contracts instantaneously at rate `gamma`.

## 2. Cauchy interlacing on the positive-middle branch

For a symmetric matrix and its compression to a codimension-one subspace, Cauchy interlacing gives

\[
\boxed{
\lambda_1
\le\mu_1
\le\lambda_2
\le\mu_2
\le\lambda_3.
}
\]

Assume the positive-middle condition

\[
\boxed{\lambda_2\ge0.}
\]

Then automatically

\[
\boxed{\mu_2\ge0.}
\]

Since

\[
\mu_1=-\gamma-\mu_2,
\]

we get

\[
\boxed{
\mu_2-\mu_1
=\gamma+2\mu_2
\ge\gamma.
}
\]

This is the alignment-free ribbon inequality.

## 3. Transverse trace-free strain floor

Write

\[
C=-\frac\gamma2 I_{\xi^\perp}+D,
\]

where `D` is the transverse symmetric trace-free part of the full strain relative to `xi`.

Its eigenvalues are `+-d`, with

\[
d=\frac{\mu_2-\mu_1}{2}.
\]

Therefore

\[
|D|_F=\sqrt2\,d
=\frac{\mu_2-\mu_1}{\sqrt2}.
\]

The interlacing estimate gives

\[
\boxed{
|D|_F
\ge
\frac\gamma{\sqrt2}
}
\]

at every point satisfying

\[
\gamma>0,
\qquad
\lambda_2\ge0.
\]

No vorticity/strain eigenvector alignment is assumed.

## 4. Material geometric interpretation

For two infinitesimal transverse material directions, the instantaneous principal metric rates inside `xi^perp` are the eigenvalues `mu1,mu2` modulo rotation of the transverse frame.

Their area rate is

\[
\mu_1+\mu_2=-\gamma,
\]

while the instantaneous logarithmic aspect-ratio production is

\[
\mu_2-\mu_1.
\]

Hence

\[
\boxed{
\text{aspect-ratio production}
\ge
-\text{area log-rate}
}
\]

on every positive-middle source-active point, exactly as in the previously aligned calculation.

If the transverse eigendirections rotate rapidly enough to prevent accumulated ribbonization, that rotation is projective/eigenframe action. If the material packet is replaced, that is turnover. If spatial non-affinity destroys the local plane description, it enters the existing derivative/residual lane.

## 5. Source-active quantitative floor

Suppose on a cell

\[
q=W^TSW=|W|^2\gamma\ge q_0>0
\]

and

\[
|W|\le M_+.
\]

Then

\[
\gamma\ge\frac{q_0}{M_+^2}.
\]

On the positive-middle part of that cell,

\[
\boxed{
|D|_F
\ge
\frac{q_0}{\sqrt2\,M_+^2}
=:
D_0>0.
}
\]

Thus a positive-density population of source-active positive-middle cells automatically supplies a positive-density transverse `D` action floor.

This is precisely the input needed by the covariance/projective-action bridge.

## 6. Recurrent consequence

`RECURRENT_MAX_BETCHOV_POSITIVE_MIDDLE_ROUTING_2026-08-24.md` shows that every residual-quiet nonzero recurrent core enters source-active positive-middle cells at positive time density.

The present lemma therefore upgrades that statement to

\[
\boxed{
\text{recurrent residual-quiet core}
\Longrightarrow
\text{positive-density transverse trace-free action}
}
\]

without any alignment hypothesis.

The transverse covariance identity

\[
E_\perp'=2q_\perp D+\mathcal R_\perp
\]

can now be applied with a genuine action floor obtained directly from the source-active stretching, rather than from an assumed `xi ~= e3` spectral lane.

## 7. Relation to the earlier aligned formula

If `xi=e3` is exactly the largest-strain eigenvector, then

\[
\mu_1=\lambda_1,
\qquad
\mu_2=\lambda_2,
\qquad
\gamma=\lambda_3,
\]

and the general inequality becomes

\[
\lambda_2-\lambda_1
\ge\lambda_3,
\]

which is exactly the original positive-middle ribbon estimate.

Thus the old aligned result is a special case of the interlacing lemma.

Status: **POSITIVE-MIDDLE RIBBONIZATION DOES NOT REQUIRE VORTICITY TO ALIGN WITH THE MOST EXTENSIONAL STRAIN EIGENVECTOR. FOR ANY VORTICITY DIRECTION WITH POSITIVE STRETCHING, `lambda2>=0` FORCES TRANSVERSE ANISOTROPY RATE AT LEAST THE STRETCHING RATE AND `|D|>=gamma/sqrt(2)`. THIS SUPPLIES THE MISSING ALIGNMENT-FREE ACTION FLOOR FOR THE RECURRENT COVARIANCE/PROJECTIVE ROUTE.**