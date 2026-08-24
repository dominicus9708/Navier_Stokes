# Local Material-Flux Relative-Mean / Dilation Reduction — 2026-08-24

Status: **REDUCES THE LOCALIZED ENSTROPHY MATERIAL-FLUX ERROR TO RELATIVE VELOCITY VARIANCE + ANNULAR VORTICITY MASS / GLOBAL REGULARITY NOT PROVED.**

This note strengthens the material term in `LOCAL_ENSTROPHY_IMS_DIFFUSION_SHARPENING_2026-08-24.md`.

The dynamically normalized transport field is

\[
V=U+\frac b2y.
\]

A naive moving cutoff can mix three unrelated motions:

1. absolute translational drift;
2. the deterministic similarity dilation `b y/2`;
3. genuine relative material crossing.

The correct center choice separates them. The similarity dilation has a favorable sign for a radial decreasing cutoff and therefore does not need to be paid as an error.

## 1. Radial cutoff and adapted center

Let

\[
\phi_a(y,s)=\Phi\!\left(\frac{|y-a(s)|}{R}\right)
\]

with `Phi'<=0`. Let `bar U_phi` be a local weighted mean velocity associated with the cutoff region. Choose the center equation

\[
\boxed{
a_s
=\bar U_\phi+\frac b2a.
}
\]

Then

\[
\boxed{
V-a_s
=(U-\bar U_\phi)
+\frac b2(y-a).
}
\]

The local material term in the enstrophy identity is

\[
F_{mat}
=\frac12
\int|\Omega|^2(V-a_s)\cdot\nabla\phi\,dy.
\]

## 2. Similarity dilation has the favorable sign

Because `phi` is radial and decreasing,

\[
(y-a)\cdot\nabla\phi\le0.
\]

Since `b>=0` on the running first-hitting envelope,

\[
\boxed{
\frac b4
\int|\Omega|^2(y-a)\cdot\nabla\phi\,dy
\le0.
}
\]

Therefore

\[
\boxed{
F_{mat}
\le
\frac12
\int|\Omega|^2
(U-\bar U_\phi)\cdot\nabla\phi\,dy.
}
\]

Thus the deterministic scale dilation cannot be the positive boundary injection that defeats the local enstrophy telescope.

## 3. Relative-velocity crossing bound

Let `A_tr=supp grad phi` and define

\[
Z_{tr}:=\int_{A_{tr}}|\Omega|^2dy,
\]

\[
V_{rel,tr}:=
\int_{A_{tr}}|U-\bar U_\phi|^2dy.
\]

The first-hitting cap `|Omega|<=1` gives

\[
\int_{A_{tr}}|\Omega|^2|U-\bar U_\phi|^2
\le V_{rel,tr}.
\]

Hence Cauchy--Schwarz yields

\[
\boxed{
F_{mat}
\le
\frac12\|\nabla\phi\|_\infty
\sqrt{Z_{tr}V_{rel,tr}}.
}
\]

For `phi=psi^2` with

\[
|\nabla\psi|\le[(L-1)R]^{-1},
\]

one has

\[
|\nabla\phi|\le\frac2{(L-1)R},
\]

and therefore

\[
\boxed{
F_{mat}
\le
\frac1{(L-1)R}
\sqrt{Z_{tr}V_{rel,tr}}.
}
\]

## 4. Insert the local buffer-mass ratio

If

\[
Z_{tr}\le\varepsilon_bZ_\phi,
\]

then

\[
\boxed{
\frac{F_{mat}}{Z_\phi}
\le
\frac{\sqrt{\varepsilon_b}}{(L-1)R}
\left(
\frac{V_{rel,tr}}{Z_\phi}
\right)^{1/2}.
}
\]

If the retained packet gives `Z_phi>=z_->0` and the low-turnover moving-variance corridor gives

\[
V_{rel,tr}\le V_{tr,+},
\]

then the previously abstract coefficient `f_mat` can be taken as

\[
\boxed{
f_{mat}
\le
\frac{\sqrt{\varepsilon_bV_{tr,+}/z_-}}
{(L-1)R}.
}
\]

Conversely, if `F_mat/Z_phi` exceeds a chosen threshold while `Z_tr/Z_phi` is small, then the relative velocity variance must satisfy the explicit lower bound

\[
\boxed{
V_{rel,tr}
\ge
\frac{(L-1)^2R^2}{\varepsilon_b}
\left(
\frac{F_{mat}}{Z_\phi}
\right)^2
Z_\phi.
}
\]

Thus large material injection is quantitatively a local relative-velocity/turnover event unless the annular vorticity mass is itself large.

## 5. Combined IMS local coefficient

Using the exact IMS frequency constant

\[
\lambda_{IMS}
=\frac1{R^2}
\left[
\frac{\pi^2}{L^2}
-
\frac{\varepsilon_b}{(L-1)^2}
\right],
\]

the quiet relative-mean corridor obeys

\[
\boxed{
\frac12(\log Z_\phi)'
+\frac b4
\le
C_{prod}(\beta_S)
+
\frac{\sqrt{\varepsilon_bV_{tr,+}/z_-}}
{(L-1)R}
-
\nu\lambda_{IMS}.
}
\]

No independent positive diffusion-flux parameter remains, and absolute center drift does not appear.

## 6. Corrected complement

The material-flux part of the local proof tree now has only

\[
\boxed{
\text{large }F_{mat}
\Longrightarrow
\text{large annular vorticity mass}
\lor
\text{large relative velocity variance}.
}
\]

The first enters the one-step annular plateau trichotomy. The second is the existing moving-variance/material-turnover branch.

Status: **WITH THE DILATION-ADAPTED RELATIVE-MEAN CENTER, THE SIMILARITY DILATION CONTRIBUTION TO LOCAL ENSTROPHY FLUX HAS FAVORABLE SIGN. POSITIVE MATERIAL INJECTION IS CONTROLLED SOLELY BY THE PRODUCT OF TRANSITION-ANNULUS VORTICITY MASS AND RELATIVE VELOCITY VARIANCE. THUS THE ABSTRACT MATERIAL-FLUX ERROR REDUCES TO THE ALREADY TRACKED ANNULAR-MASS OR MOVING-VARIANCE BRANCHES. GLOBAL REGULARITY REMAINS UNPROVED.**