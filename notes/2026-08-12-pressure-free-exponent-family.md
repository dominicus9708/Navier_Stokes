# Pressure-free epsilon-regularity exponent family for the moving sphere

Date: 2026-08-12

Status: **DERIVED INTERPOLATION FAMILY + EXTERNAL PRESSURE-FREE REGULARITY ANCHOR + OPEN SMALLNESS OBLIGATION**.

## 1. External target exponent

A pressure-free one-scale epsilon-regularity theorem for suitable weak solutions states that for every

\[
\delta>0
\]

there exists a sufficiently small threshold such that small

\[
\int_{Q(1)}|u|^{5/2+\delta}dxdt
\]

implies boundedness in a smaller cylinder.

Thus the proof track is not restricted to the cubic exponent `p=3`.

Set

\[
p=\frac52+\delta,
\qquad
\frac52<p\le3.
\]

## 2. Moving mean-sphere interpolation

In the mean-flow moving sphere, the translated velocity `v` has zero spatial mean on `B_ell` at each time.

Interpolate

\[
\|v\|_p
\le
\|v\|_2^{\theta}
\|v\|_6^{1-\theta},
\]

where

\[
\frac1p=\frac\theta2+\frac{1-\theta}{6}.
\]

Hence

\[
\theta=\frac3p-\frac12.
\]

Using

\[
\|v\|_2^2=\ell C_{\rm sph},
\]

and

\[
\|v\|_6
\le C\left(\frac{E_{\rm sph}}{\ell}\right)^{1/2},
\]

we obtain

\[
\boxed{
\int_{B_\ell}|v|^pdx
\le
C\ell^{3-p}
C_{\rm sph}^{\alpha(p)}
E_{\rm sph}^{\beta(p)}
}
\]

with

\[
\boxed{
\alpha(p)=\frac{6-p}{4},
\qquad
\beta(p)=\frac{3(p-2)}{4}.
}
\]

## 3. Parabolic critical quantity

Define

\[
A_p
=
\ell^{p-5}
\int_{t_0}^{t_0+\ell^2}
\int_{B_\ell}|v|^pdxdt.
\]

This is invariant under Navier--Stokes scaling.

Because `beta(p)<1` for the whole range used here, Jensen/Hölder gives

\[
\boxed{
A_p
\le
C
\left(\sup_t C_{\rm sph}(t)\right)^{\alpha(p)}
\left(\mathfrak E_{\rm sph}\right)^{\beta(p)}.
}
\]

## 4. Representative exponents

For `p=3`:

\[
\alpha=\frac34,
\qquad
\beta=\frac34.
\]

For the concrete pressure-free choice

\[
p=\frac{11}{4}
\quad(\delta=\tfrac14),
\]

we obtain

\[
\boxed{
A_{11/4}
\le
C
(\sup C_{\rm sph})^{13/16}
(\mathfrak E_{\rm sph})^{9/16}.
}
\]

As

\[
p\downarrow\frac52,
\]

the powers approach

\[
\boxed{
\alpha\to\frac78,
\qquad
\beta\to\frac38.
}
\]

Thus lower pressure-free exponents put more weight on **internal velocity oscillation** and less weight on the local-dissipation channel.

## 5. DSD consequence

This is useful specifically for the DSD formulation because `C_sph` is the channel most directly aligned with a local 기술가능성 difference after coherent motion is removed.

The route can therefore test a family of gates rather than only

\[
(C_{\rm sph}\mathfrak E_{\rm sph})^{3/4}.
\]

For example, if structural dynamics can suppress internal oscillation strongly while allowing a relatively larger gradient-energy channel, a choice closer to `p=5/2` is formally more favorable.

However, the epsilon threshold depends on the chosen exponent. One must not optimize over `p` while pretending that the threshold constant is uniform.

## 6. Necessary concentration condition for a candidate singularity

Once the moving-frame/suitable-solution bridge is rigorous, failure of the pressure-free epsilon criterion at a candidate singularity implies that at arbitrarily small scales the channel product cannot be too small:

\[
(\sup C_{\rm sph})^{\alpha(p)}
(\mathfrak E_{\rm sph})^{\beta(p)}
\gtrsim
\varepsilon_p/C.
\]

This is not a contradiction. It is a **necessary critical concentration certificate** that any singularity must satisfy in the moving-sphere description.

The next proof task is to show that DSD-resolved transport, strain, or cross-channel constraints make such persistent simultaneous concentration impossible.

Status: **OPEN PROOF OBLIGATION**.
