# Low-order physical factorization of the critical projective scale-migration forcing

Date: 2026-08-18

Status: **DERIVED PHYSICAL LOW-ORDER CONSEQUENCE OF THE CRITICALIZED DYNAMIC-RADIUS PROJECTIVE INEQUALITY. IF THE REQUIRED SCALE-CRITICAL FACTORIAL FORCING IS NOT CARRIED BY HIGHER DERIVATIVE ORDERS, PROJECTIVELY ROUGH FREQUENCY MIGRATION FORCES A PRODUCT OF CRITICAL L_t^2 L_x^3 STRAIN ACTION AND CRITICAL SCALE-WEIGHTED MAGNITUDE-GRADIENT ACTION GROWING LIKE LOG^2(K1/K0). GLOBAL REGULARITY NOT PROVED.**

## 1. Critical projective migration requirement

The dynamic-radius cross-index inequality gives, for a projectively rough critical component with

\[
\mathfrak P_\ell\ge p_0>0
\]

while the active physical frequency moves from `K0` to `K1`,

\[
\boxed{
\int\mathfrak F_{\rm crit}dt
\gtrsim
c\sqrt{p_0}\log\frac{K_1}{K_0}
-O(1).
}
\]

Here

\[
\mathfrak F_{\rm crit}
=\ell^{1/2}
\left(\sum_{m\ge0}(F_m^\#)^2\right)^{1/2}.
\]

## 2. Zeroth derivative forcing

At derivative order `m=0`, the differentiated-vorticity forcing is simply the stretching source

\[
F_0=S\omega
\]

(up to the chosen forced band/localized decomposition; projection/moving-band terms are typed separately in the total forcing).

Thus

\[
\|F_0\|_2
\le
\|S\|_3\|\omega\|_6.
\]

The scalar Sobolev estimate for the vorticity magnitude gives

\[
\|\omega\|_6
=\||\omega|\|_6
\lesssim
\|\nabla|\omega|\|_2
=P_{\rm mag}^{1/2}.
\]

Therefore

\[
\boxed{
\ell^{1/2}\|F_0\|_2
\lesssim
\|S\|_3(\ell P_{\rm mag})^{1/2}.
}
\]

## 3. Time factorization

Cauchy--Schwarz in time gives

\[
\boxed{
\int_I\ell^{1/2}\|F_0\|_2dt
\lesssim
\left(\int_I\|S\|_3^2dt\right)^{1/2}
\left(\int_I\ell P_{\rm mag}dt\right)^{1/2}.
}
\]

Both factors are scale critical:

- `int ||S||_3^2 dt` has `2/2+3/3=2` strain-critical scaling;
- `int ell P_mag dt` is invariant because `P_mag` scales like inverse length cubed, `ell` like length, and `dt` like length squared.

## 4. Low-order / high-order forcing split

Split the critical factorial forcing into

\[
\mathfrak F_{\rm crit}
\le
\ell^{1/2}\|F_0\|_2
+\mathfrak F_{\rm crit}^{\ge1}.
\]

If at least a fixed fraction of the migration lower bound is carried by `m=0`, then

\[
\left(\int_I\|S\|_3^2dt\right)^{1/2}
\left(\int_I\ell P_{\rm mag}dt\right)^{1/2}
\gtrsim
\sqrt{p_0}\log\frac{K_1}{K_0}.
\]

Hence

\[
\boxed{
\left(\int_I\|S\|_3^2dt\right)
\left(\int_I\ell P_{\rm mag}dt\right)
\gtrsim
p_0\left(\log\frac{K_1}{K_0}\right)^2.
}
\]

If this fails, then the higher-order factorial forcing must satisfy

\[
\boxed{
\int_I\mathfrak F_{\rm crit}^{\ge1}dt
\gtrsim
\sqrt{p_0}\log\frac{K_1}{K_0},
}
\]

which is the derivative-order concentration / analytic-radius forcing branch.

## 5. Interpretation

A projectively rough cascade cannot migrate through many physical scales by using only a mild low-order source.  It must pay either

\[
\boxed{
\text{critical strain action}
\times
\text{critical magnitude-interface action}
}
\]

with a logarithmic-square lower bound, or it must move the forcing into higher derivative orders.

This explicitly couples the DSD projective channel to the established strain and magnitude-gradient ledgers.

## 6. Limitation

Neither critical factor has an a-priori finite global bound near a hypothetical singularity.  The product lower bound therefore does not prove regularity.  It identifies a narrower simultaneous-saturation requirement.

Status: **ROUGH SCALE MIGRATION -> LOG^2 CRITICAL STRAIN x MAGNITUDE-GRADIENT PRODUCT OR HIGHER-DERIVATIVE FACTORIAL FORCING / GLOBAL REGULARITY NOT PROVED.**