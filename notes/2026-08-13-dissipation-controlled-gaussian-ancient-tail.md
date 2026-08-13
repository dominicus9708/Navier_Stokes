# Dissipation-controlled Gaussian ancient tail and the `W^(1/6)` active-scale ceiling

Date: 2026-08-13

Status: **DERIVED BOUNDED-AFFINE RESIDUAL-TAIL IMPROVEMENT / GLOBAL REGULARITY NOT PROVED**.

The earlier kinetic-energy far-past estimate gave a `tau^(-5/4)` decay but did not uniformly truncate the ancient tail at a fixed normalized time because the normalized kinetic energy grows like `W^(1/2)` in squared norm.

The sharpened mean-vorticity cancellation changes the residual source from `sqrt(B_gamma)` to `B_gamma`.  Combining this with the physical energy-dissipation budget produces a substantially stronger mesoscopic tail cutoff.

---

## 1. Linear residual source

On the self-consistent Gaussian affine window,

\[
\left|
\int\gamma_s f_r
\right|
\le
C
[1+\sqrt{\kappa(\Sigma(s))}]
\mathcal B_\gamma(s),
\]

where

\[
\mathcal B_\gamma
=\int\gamma|\nabla U-L|^2.
\]

Assume on the branch under consideration that

\[
\|F(T,s)\|_{op}\le K_F,
\qquad
\kappa(\Sigma(s))\le K_\Sigma.
\]

If either bound fails, the route is typed as affine deformation / affine heat anisotropy rather than the bounded-affine residual branch.

Then

\[
\boxed{
\mathfrak R_{\gamma,J}
\le
C_K\int_J\mathcal B_\gamma(s)ds
}
\]

for every time subset `J`.

---

## 2. Gaussian variance is bounded by Gaussian-weighted dissipation

Since `L` is the Gaussian mean of `grad U`,

\[
\mathcal B_\gamma
=P_\Sigma|\nabla U|^2-|P_\Sigma\nabla U|^2
\le
P_\Sigma|\nabla U|^2.
\]

Let the Gaussian volume radius be

\[
R_\gamma=(\det\Sigma)^{1/6}.
\]

Then

\[
\|\gamma_\Sigma\|_\infty
=(2\pi)^{-3/2}(\det\Sigma)^{-1/2}
=C R_\gamma^{-3}.
\]

Therefore

\[
\boxed{
\mathcal B_\gamma(s)
\le
C R_\gamma(s)^{-3}
\|\nabla U(s)\|_2^2.
}
\]

No vorticity `L2` bound beyond the energy dissipation identity is assumed.

---

## 3. Total normalized dissipation budget

At a terminal first-hitting level

\[
W=\|\omega(T)\|_\infty,
\qquad
r=W^{-1/2},
\]

use

\[
U(y,s)=r u(x_*+ry,T+r^2s).
\]

Then

\[
\|\nabla U(s)\|_2^2
=r\|\nabla u(t)\|_2^2,
\qquad
ds=r^{-2}dt.
\]

Hence

\[
\boxed{
\int\|\nabla U(s)\|_2^2ds
=r^{-1}
\int\|\nabla u(t)\|_2^2dt
=W^{1/2}
\int\|\nabla u(t)\|_2^2dt.
}
\]

The kinetic-energy identity yields

\[
\int_0^T\|\nabla u(t)\|_2^2dt
\le
\frac{\|u_0\|_2^2}{2\nu}.
\]

Thus

\[
\boxed{
\int\|\nabla U(s)\|_2^2ds
\le
C(u_0,\nu)W^{1/2}.
}
\]

---

## 4. Residual tail beyond a Gaussian parent scale

Fix `R0>0` and let

\[
J_{R_0}=\{s:R_\gamma(s)\ge R_0\}.
\]

Then

\[
\begin{aligned}
\mathfrak R_{\gamma,J_{R_0}}
&\le
C_K\int_{J_{R_0}}\mathcal B_\gamma(s)ds\\
&\le
C_K R_0^{-3}
\int\|\nabla U(s)\|_2^2ds.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathfrak R_{\gamma,\,R_\gamma\ge R_0}
\le
C(K,u_0,\nu)
W^{1/2}R_0^{-3}.
}
\]

---

## 5. The `1/6` cutoff exponent

Set

\[
R_0=W^{1/6+\varepsilon}.
\]

Then

\[
W^{1/2}R_0^{-3}
=W^{1/2-(1/2+3\varepsilon)}
=W^{-3\varepsilon}.
\]

Hence

\[
\boxed{
\mathfrak R_{\gamma,\,R_\gamma\ge W^{1/6+\varepsilon}}
\to0
}
\]

on every bounded-affine/controlled-Gaussian branch.

The corresponding physical radius is

\[
rR_0
=W^{-1/2}W^{1/6+\varepsilon}
=W^{-1/3+\varepsilon},
\]

which tends to zero for `epsilon<1/3`.

Thus the non-affine endpoint residual relevant to a hypothetical blow-up is confined to a physical mesoscopic neighborhood shrinking like `W^(-1/3+epsilon)`.

---

## 6. Compare the active-scale ceilings

The current kinetic-energy scale audits give

\[
\boxed{
\begin{array}{c|c}
\text{channel} & \text{normalized parent-scale ceiling}\\
\hline
\text{far pressure-Hessian variation} & W^{1/12+\varepsilon}\\
\text{Gaussian affine mean} & W^{1/10+\varepsilon}\\
\text{non-affine Gaussian residual} & W^{1/6+\varepsilon}
\end{array}
}
\]

Hence the residual channel determines the largest currently active mesoscopic ladder.

---

## 7. DSD interpretation

The adaptive search no longer needs the full ancient normalized domain on the bounded-affine branch.

At terminal level `W`, the endpoint-relevant unresolved history may be compressed to

\[
\boxed{
1\lesssim R_\gamma
\lesssim W^{1/6+\varepsilon}.
}
\]

Information at larger Gaussian resolution contributes vanishingly to the endpoint residual unless affine deformation/anisotropy itself leaves the bounded branch.

Thus the search graph splits cleanly:

1. **bounded affine geometry:** residual history is mesoscopically truncated by dissipation;
2. **unbounded affine geometry:** return to the affine deformation/compression-diffusion branch.

---

## 8. Limitation

The active ladder still contains `O(log W)` dyadic scales.  The estimate does not show contraction inside that ladder.  Order-one residual action can still move between scales in a scale-critical fashion.

The next target is to combine

- the scale-ladder ANOVA identity;
- the Gaussian residual semigroup square function;
- and the finite total normalized dissipation

into a packing or contraction statement for the remaining `R <= W^(1/6+epsilon)` scales.

Status: **ANCIENT RESIDUAL TAIL PRUNED TO THE `W^(1/6)` MESOSCOPIC LADDER / INTERNAL SCALE PACKING REMAINS OPEN**.
