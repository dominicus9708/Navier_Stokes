# Smooth Record-Point Growth / H1 Production Tradeoff — 2026-08-20

Status: **S-LEVEL POINTWISE LEMMA ON THE ORIGINAL SMOOTH SOLUTION. GLOBAL REGULARITY NOT PROVED.**

This note works only at finite smooth first-hitting times. It quantifies a direct incompatibility between efficient growth of the running vorticity maximum and strong local `P_V` H1 production at the same spatial point.

## 1. Record-growth point

Use the running first-hitting envelope `M(t)` from `SMOOTH_FINITE_STAGE_TIGHTROPE_LEDGER_2026-08-20.md`.

At almost every time where

\[
M'(t)>0,
\]

the current vorticity supremum equals the running envelope. Choose a maximizing point `x_*` and set

\[
|\omega(x_*,t)|=M(t),
\qquad
\xi=\frac{\omega}{M},
\qquad |\xi|=1.
\]

Use the running normalization

\[
\Omega=M^{-1}\omega,
\qquad
\Sigma=M^{-1}S,
\qquad
y=M^{1/2}(x-X_0).
\]

Let

\[
G=\nabla_y\Omega.
\]

At the maximum,

\[
\nabla_y|\Omega|^2=0,
\]

hence

\[
\boxed{G\xi=0.}
\]

This is an exact first-hitting constraint on the vorticity-gradient matrix.

## 2. Record growth has an exact viscous loss

The vorticity magnitude identity is

\[
\frac12(\partial_t+u\cdot\nabla)|\omega|^2
=
\omega\cdot S\omega
+\nu\left(
\frac12\Delta|\omega|^2-|\nabla\omega|^2
\right).
\]

At a spatial maximum of `|omega|`,

\[
\Delta|\omega|^2\le0.
\]

Therefore the upper Dini derivative of the running maximum satisfies

\[
M M'
\le
M^2\,\xi^TS\xi
-\nu|\nabla_x\omega|^2.
\]

Since

\[
|\nabla_x\omega|^2=M^3|G|^2,
\]

and

\[
b=\frac{M'}{M^2},
\]

we get the exact normalized inequality

\[
\boxed{
b+\nu|G|^2\le\xi^T\Sigma\xi.}
\]

If `s3` is the largest eigenvalue of `Sigma`, define the alignment defect

\[
\boxed{
\delta_{align}=s_3-\xi^T\Sigma\xi\ge0.
}
\]

Then

\[
\boxed{
\nu|G|^2
\le
s_3-b-\delta_{align}.
}
\]

Thus inefficient record amplification has only two local sources:

1. vorticity is not aligned with the strongest extensional strain direction;
2. vorticity-gradient diffusion is non-negligible.

## 3. Exact local H1 production density

The vorticity-gradient representation of H1 production has density

\[
\boxed{
n_{H1}
=\frac12\Sigma:(G^TG-GG^T).
}
\]

Bottcher--Wenzel gives

\[
|G^TG-GG^T|
\le\sqrt2|G|^2,
\]

therefore

\[
\boxed{
(n_{H1})^+
\le
\frac{|\Sigma|}{\sqrt2}|G|^2.
}
\]

Combining with the record-growth inequality yields the universal record-point tradeoff

\[
\boxed{
(n_{H1})^+
\le
\frac{|\Sigma|}{\sqrt2\nu}
\left(
 s_3-b-\delta_{align}
\right).
}
\]

This is a direct smooth first-hitting statement.

If record amplification approaches the local extensional ceiling,

\[
b\to s_3,
\qquad
\delta_{align}\to0,
\]

then necessarily

\[
(n_{H1})^+\to0
\]

at the same record point.

## 4. Sharpening under exact extensional alignment

Assume now

\[
\xi=e_3
\]

is exactly the largest-strain eigenvector and write

\[
\Sigma=\operatorname{diag}(s_1,s_2,s_3),
\qquad
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0.
\]

Because `G xi = 0` and `tr G=0`, in this eigenframe

\[
G=
\begin{pmatrix}
a&c_{12}&0\\
c_{21}&-a&0\\
c_{31}&c_{32}&0
\end{pmatrix}.
\]

A direct calculation gives

\[
\boxed{
\begin{aligned}
2n_{H1}
={}&(s_1-s_2)c_{21}^2
+(s_2-s_1)c_{12}^2\\
&+(s_1-s_3)c_{31}^2
+(s_2-s_3)c_{32}^2.
\end{aligned}
}
\]

Every coefficient except the `c12` coefficient is nonpositive. Hence

\[
\boxed{
(n_{H1})^+
\le
\frac12(s_2-s_1)c_{12}^2
\le
\frac12(s_2-s_1)|G|^2.
}
\]

Combining with record growth,

\[
\boxed{
(n_{H1})^+
\le
\frac{s_2-s_1}{2\nu}(s_3-b).
}
\]

## 5. Positive-middle spectral parameter

Write

\[
(s_1,s_2,s_3)
=(-2m,m-d,m+d),
\qquad
x=d/m\in[0,1].
\]

Then

\[
s_2-s_1=m(3-x),
\qquad
s_3=m(1+x).
\]

Thus

\[
\boxed{
(n_{H1})^+
\le
\frac{3-x}{2(1+x)}
\frac{s_3(s_3-b)}{\nu}.
}
\]

At the middle-zero endpoint `x=1`,

\[
\boxed{
(n_{H1})^+
\le
\frac{s_3(s_3-b)}{2\nu}.
}
\]

So the very spectrum previously favored by the nonnormality branch has a strong same-point growth/production incompatibility: if `b` is close to `s3`, local H1 production collapses.

## 6. Smooth branch routing

This yields a finite-solution trichotomy at a record point.

### R1 — efficient record amplification

If

\[
s_3-b\ll1
\]

and alignment is good, then

\[
(n_{H1})^+\ll1.
\]

A globally significant `P_V` production packet must therefore sit away from the record point. On the single-core mainline, this becomes a spatial-overlap/turnover question rather than a new local equality regime.

### R2 — strong local P_V production at the record point

If `(n_H1)^+` is order one, then

\[
s_3-b-\delta_{align}
\]

is order one as well. The record core pays a definite vorticity-gradient diffusion cost.

This feeds the derivative/H channel directly.

### R3 — extensional misalignment

If

\[
\delta_{align}
\]

is not small, vorticity is not aligned with the strongest extensional strain axis. This feeds the already tracked projective/covariance/turnover deficit.

Hence the record maximum cannot simultaneously be

- spectrally efficient for vorticity amplification;
- diffusion-light;
- and a strong local H1 nonnormality producer.

At least one role must be surrendered.

## 7. What remains before S-closing a branch

The pointwise lemma does not yet say that global `N` is concentrated at the vorticity record point.

The next smooth-only step is therefore an overlap lemma. For each finite stage, define a record tube around the maximizing trajectory and quantify the fraction of the global vorticity-gradient production measure contained in that tube.

Then:

- small overlap routes to spatial separation / turnover;
- large overlap allows the pointwise tradeoff above to control a fixed fraction of global `N`;
- large diffusion slack routes to `H`.

No compact limit is required for this program.

Status: **AT A SMOOTH VORTICITY RECORD POINT, EFFICIENT VORTICITY AMPLIFICATION AND STRONG LOCAL P_V H1 PRODUCTION ARE QUANTITATIVELY INCOMPATIBLE. NEXT = FINITE-STAGE RECORD-TUBE OVERLAP LEMMA.**