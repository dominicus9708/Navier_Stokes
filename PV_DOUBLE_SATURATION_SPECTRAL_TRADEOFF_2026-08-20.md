# Double-Saturation Spectral Tradeoff — 2026-08-20

Overall status: **NEW SPECTRAL INCOMPATIBILITY FOR THE FINAL P_V BRANCH — GLOBAL REGULARITY NOT PROVED.**

This note compares the two different geometries that the remaining `P_V` branch tries to approach:

1. the static H1/max-mid covariance ceiling;
2. the vorticity-gradient non-normality/Bottcher--Wenzel ceiling.

The two ceilings prefer opposite strain spectra.

---

## 1. Exact non-normality density in the strain eigenframe

Let

\[
G=\nabla\omega.
\]

The exact global identity is

\[
N
=\frac12\int S:(G^TG-GG^T)dx.
\]

At a point, rotate into the strain eigenframe

\[
S=\operatorname{diag}(s_1,s_2,s_3),
\qquad
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0.
\]

Then

\[
\boxed{
S:(G^TG-GG^T)
=\sum_{a,b}(s_b-s_a)|G_{ab}|^2.
}
\]

Therefore the corresponding non-normality density satisfies

\[
\boxed{
q_{NN}
\le
\frac12(s_3-s_1)|G|^2.
}
\]

Positive production is carried by matrix entries that transfer vorticity-gradient weight from lower-strain directions toward higher-strain directions. The largest coefficient is the extreme spectral gap `s3-s1`.

---

## 2. Exact middle-eigenvalue tax

Let

\[
r=s_3-s_1.
\]

Since the trace is zero,

\[
|S|^2=\frac12(r^2+3s_2^2).
\]

Hence

\[
\boxed{
\sqrt2|S|-r
=
\frac{3s_2^2}{\sqrt2|S|+r}
\ge0.
}
\]

Thus

\[
\boxed{
q_{NN}
\le
\frac1{\sqrt2}|S||G|^2
-
\frac12
\frac{3s_2^2}{\sqrt2|S|+(s_3-s_1)}
|G|^2.
}
\]

The Bottcher--Wenzel/range ceiling is saturated only when

\[
\boxed{s_2=0.}
\]

So non-normality saturation prefers the middle-zero spectrum

\[
(-a,0,a).
\]

---

## 3. Positive-middle parameterization

On the positive-middle branch write

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\]

with

\[
m>0,
\qquad
0\le d\le m.
\]

Set

\[
x=d/m\in[0,1].
\]

Then

\[
|S|=m\sqrt{6+2x^2},
\qquad
s_3-s_1=m(3+x).
\]

The fractional efficiency relative to the absolute non-normality range ceiling is therefore

\[
\boxed{
\Theta_{NN}(x)
=
\frac{s_3-s_1}{\sqrt2|S|}
=
\frac{3+x}{2\sqrt{3+x^2}}.
}
\]

It increases monotonically from

\[
\Theta_{NN}(0)=\frac{\sqrt3}{2}
\approx0.8660254
\]

to

\[
\Theta_{NN}(1)=1.
\]

Thus exact max-mid strain pays a `13.4%` algebraic loss in the non-normality ceiling.

---

## 4. Static H1 efficiency prefers the opposite endpoint

The previously derived sharp fixed-gap H1 efficiency factor is

\[
\boxed{
\Theta_{st}(x)
=
\frac12+
\frac1{2\sqrt{1+x^2/3}}.
}
\]

It decreases monotonically from

\[
\Theta_{st}(0)=1
\]

toward

\[
\Theta_{st}(1)
=
\frac12+rac{\sqrt3}{4}
\approx0.9330127.
\]

Thus the static H1 ceiling prefers

\[
\boxed{x=0}
\]

which is exact max-mid strain, while the non-normality ceiling prefers

\[
\boxed{x=1}
\]

which is middle-zero strain.

---

## 5. Exact crossing and universal spectral tradeoff

The two efficiency curves cross when

\[
\Theta_{st}(x_*)=\Theta_{NN}(x_*).
\]

Solving exactly gives

\[
\boxed{
x_*
=\frac{3(\sqrt3-1)}4
\approx0.549038106.
}
\]

The common value is

\[
\boxed{
\Theta_*
=
\frac{15+6\sqrt3}{26}
\approx0.9766271094.
}
\]

Therefore every positive-middle strain spectrum satisfies

\[
\boxed{
\min\{\Theta_{st}(x),\Theta_{NN}(x)\}
\le
\Theta_*
<1.
}
\]

Equivalently, every spectral shape pays at least

\[
\boxed{
1-\Theta_*
=
\frac{11-6\sqrt3}{26}
\approx0.0233728906
}
\]

of the ceiling in at least one of the two saturation channels.

This is the first explicit algebraic double-saturation gap between the max-mid and non-normality geometries.

---

## 6. Scope of the 2.337% number

The static H1 density and the non-normality density are two different local representations whose **integrals** agree after integration by parts. They are not identical pointwise; their difference contains divergence/transport terms.

Therefore the number

\[
1-\Theta_*\approx2.337\%
\]

must **not** yet be inserted directly as a universal global reduction of the H1 production constant.

Its rigorous meaning at this stage is:

> no pointwise positive-middle strain spectrum can be simultaneously closer than `2.337%` to both required algebraic saturation geometries.

To convert it into a global H1 threshold gap one must control the divergence transfer between the two density representations or use compactness/localization to prevent the two saturation geometries from segregating into different regions.

---

## 7. Relation to the new Fourier compatibility cap

The tradeoff is even sharper when static saturation also approaches its required one-dimensional derivative geometry.

Static near-saturation drives

- the derivative direction toward a fixed axis `n`;
- derivative matrices toward the max-mid line `Q_n`.

But `PV_GLOBAL_COMPATIBILITY_COVARIANCE_CAP_2026-08-20.md` proves

\[
\operatorname{dist}(Q_n,\mathcal V_k)\ge\frac12
\]

for every compatible Fourier strain mode, and exact one-dimensionality `k parallel n` makes the two spaces orthogonal.

Thus the static endpoint `x=0` is not merely inefficient for non-normality: its full derivative saturation geometry is incompatible with an incompressible strain field unless additional angular-frequency spread, interface structure, or higher derivative activity appears.

---

## 8. New routing of the recurrent survivor

A recurrent non-H/T `P_V` profile that tries to maintain near-threshold H1 production has three options.

### A. Stay near max-mid (`x << 1`)

Then

\[
\Theta_{NN}\lesssim\sqrt3/2
\]

and strong vorticity-gradient non-normality efficiency is lost. If it also approaches one-dimensional covariance saturation, Fourier strain compatibility forces angular-frequency spread or a compatibility/interface defect.

### B. Move toward middle-zero (`x -> 1`)

Then non-normality becomes efficient, but the static H1/max-mid bound pays the explicit fixed-gap loss and the determinant/max-mid branch loses its saturation geometry.

### C. Remain near the crossing (`x approx x_*`)

Then both channels are bounded by

\[
\Theta_*\approx0.9766271.
\]

Thus no spectral choice removes both taxes simultaneously.

The next task is to turn this algebraic tradeoff plus the exact `2/3` global compatibility covariance cap into a class-level quantitative reduction of the Leray recurrence threshold.

Status: **MAX-MID STATIC SATURATION AND VORTICITY-GRADIENT NON-NORMALITY SATURATION PREFER OPPOSITE STRAIN SPECTRA. THEIR OPTIMAL COMPROMISE STILL LOSES AT LEAST `2.337%` IN ONE CHANNEL, AND THE FULL ONE-DIMENSIONAL MAX-MID ENDPOINT IS FURTHER BLOCKED BY FOURIER STRAIN COMPATIBILITY.**