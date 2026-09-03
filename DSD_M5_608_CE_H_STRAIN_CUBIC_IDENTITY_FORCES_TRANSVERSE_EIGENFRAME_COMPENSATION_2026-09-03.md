# DSD M5-608 — CE-H strain cubic identity forces transverse eigenframe compensation

Date: 2026-09-03

Status: **GLOBAL STRAIN-EIGENFRAME CONSTRAINT / THE WHOLE-SPACE NAVIER--STOKES STRAIN/VORTICITY IDENTITY `int tr(Sigma^3) = -(3/4) int W·Sigma W` COMBINES WITH THE CE-H ALIGNMENT `Sigma W = sigma W` / WRITING THE OTHER TWO TRACE-FREE STRAIN EIGENVALUES AS `-sigma/2 ± delta` YIELDS THE EXACT SIGNED IDENTITY `int sigma[(sigma^2+|W|^2)/4-delta^2]=0` / THEREFORE POSITIVE AXIAL VORTEX STRETCHING CANNOT LIVE IN A LOCALLY AXISYMMETRIC TWO-COMPRESSION EIGENFRAME WITHOUT COMPENSATION; IT REQUIRES SUFFICIENT TRANSVERSE SADDLE ANISOTROPY OR NEGATIVE-SIGMA REGIONS / THIS ADDS AN INDEPENDENT EIGENFRAME PAYER TO THE CE-H KAPPA CONSTRAINTS BUT IS NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Global strain-vorticity cubic identity

For a smooth whole-space incompressible Navier--Stokes solution, let

\[
\Sigma=\frac12(\nabla U+\nabla U^T).
\]

The global strain equation and vorticity equation, together with

\[
\|\Sigma\|_2^2=\frac12\|W\|_2^2,
\qquad
\|\nabla\Sigma\|_2^2=\frac12\|\nabla W\|_2^2,
\]

give the standard exact identity

\[
\boxed{
\int_{\mathbb R^3}\operatorname{tr}(\Sigma^3)dy
=
-\frac34
\int_{\mathbb R^3}W\cdot\Sigma W\,dy.
}
\]

This is a whole-space identity; no pointwise sign assumption is made.

---

## 2. CE-H eigenframe

On CE-H,

\[
\boxed{\Sigma W=\sigma W.}
\]

Where `W != 0`, choose an orthonormal strain eigenframe with first direction

\[
\xi=W/|W|.
\]

Because `tr Sigma = 0`, write the three eigenvalues as

\[
\boxed{
\lambda_1=\sigma,
\qquad
\lambda_2=-\frac\sigma2+\delta,
\qquad
\lambda_3=-\frac\sigma2-\delta.
}
\]

The scalar `delta` measures the splitting of the two transverse strain eigenvalues.

---

## 3. Cubic invariant in the CE-H frame

For three numbers with zero sum,

\[
\lambda_1^3+\lambda_2^3+\lambda_3^3
=3\lambda_1\lambda_2\lambda_3.
\]

Hence

\[
\operatorname{tr}(\Sigma^3)
=3\sigma\left(\frac{\sigma^2}{4}-\delta^2\right).
\]

Also

\[
W\cdot\Sigma W
=\sigma|W|^2.
\]

Substitute into the global cubic identity:

\[
3\int\sigma\left(\frac{\sigma^2}{4}-\delta^2\right)
=-\frac34\int\sigma|W|^2.
\]

Divide by `3` and rearrange:

\[
\boxed{
\int
\sigma
\left[
\frac{\sigma^2+|W|^2}{4}-\delta^2
\right]dy
=0.
}
\]

Equivalently,

\[
\boxed{
\int\sigma\delta^2dy
=
\frac14
\int\sigma(\sigma^2+|W|^2)dy.
}
\]

The second form is signed because `sigma` may change sign.

---

## 4. Positive-stretching region

On a region where

\[
\sigma>0,
\]

if the two transverse eigenvalues are both compressive and nearly equal, then

\[
\delta^2\lesssim\sigma^2/4
\]

and therefore

\[
\frac{\sigma^2+|W|^2}{4}-\delta^2
\]

is strictly positive whenever `W != 0`.

Thus such a region contributes positively to the cubic identity.

Since the global integral is zero, recurrent positive axial stretching must be compensated by at least one of:

1. sufficiently large transverse eigenvalue splitting `delta^2` on positive-`sigma` regions;
2. regions with `sigma < 0`;
3. both.

Hence

\[
\boxed{
\text{positive CE-H axial stretching}
\Longrightarrow
\text{transverse saddle anisotropy}
\lor
\text{negative-sigma compensation}.
}
\]

---

## 5. Relation to the production core

The finite-depth production shell from M5-587--591 has positive recurrent stretching surplus and is represented by the finite persistent lineage network.

Therefore the CE-H component cannot maintain that production in a globally axisymmetric strain eigenframe of the form

\[
(\sigma,-\sigma/2,-\sigma/2)
\]

with `sigma > 0` on all active vorticity.

A nontrivial survivor requires recurrent transverse saddle structure or recurrent compressive axial regions elsewhere in the finite core.

---

## 6. Relation to kappa constraints

The CE-H hard core now has two independent signed spatial structures:

\[
\boxed{
\int\kappa|W|^2=-P<0,
\qquad
\int(y\cdot\nabla\kappa)|W|^2=2P>0,
}
\]

and

\[
\boxed{
\int
\sigma
\left[
\frac{\sigma^2+|W|^2}{4}-\delta^2
\right]=0.
}
\]

The first pair constrains the viscous eigenvalue landscape transverse to vortex lines.

The cubic identity constrains the full strain eigenframe around those same vortex lines.

Any final CE-H survivor must satisfy both simultaneously.

---

## 7. Audit firewall

This note does not assert that `sigma > 0` pointwise, nor that `delta^2` has a one-sided global lower bound independent of the negative-`sigma` set.

Therefore the cubic identity is a structural compensation law, not yet a Liouville contradiction.

The next useful target is to localize these compensation channels on the same finite persistent production network and test whether they can coexist with the zero-mean material-flux `kappa` cocycle from M5-603.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
