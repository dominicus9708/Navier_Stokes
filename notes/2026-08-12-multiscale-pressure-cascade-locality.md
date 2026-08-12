# Multiscale pressure-tail locality and the cascade block

Date: 2026-08-12

Status: **DERIVED REMOTE-PRESSURE DECAY + DSD MULTISCALE BRIDGE + OPEN CASCADE EXCLUSION**.

This note refines the affine-free harmonic tail left by the one-step weighted channel closure.

## 1. Genuinely remote pressure component

Fix a moving center `X=X_ell(t)` and a small scale `ell`.  Let the canonical whole-space pressure kernel be `K_ij`, homogeneous of degree `-3`, and define a genuinely remote component schematically by

\[
p_{\rm rem}(x)
=
\int_{|z-X|\ge 8\ell}
K_{ij}(x-z)u_i(z)u_j(z)\,dz.
\]

The exact numerical factor `8` is not important; it only separates the inner/transition region from the remote region.

For `x in B_{2 ell}(X)`, subtract the affine Taylor polynomial at the moving center,

\[
L_Xp_{\rm rem}(x)
=p_{\rm rem}(X)
+\nabla p_{\rm rem}(X)\cdot(x-X).
\]

Since the second spatial derivatives of the pressure kernel are homogeneous of degree `-5`, Taylor's theorem gives

\[
\boxed{
|p_{\rm rem}(x)-L_Xp_{\rm rem}(x)|
\lesssim
|x-X|^2
\int_{|z-X|\ge8\ell}
\frac{|u(z)|^2}{|z-X|^5}\,dz.
}
\]

The affine polynomial is dynamically irrelevant to the weighted variance pressure work because

\[
\int\varphi_\ell v\,dx=0,
\qquad
\nabla\cdot v=0.
\]

## 2. Scale-critical remote-tail channel

Taking the `L^{3/2}` norm over a ball of radius comparable to `ell` contributes another factor `ell^2`.  Define

\[
\boxed{
\mathfrak H_\ell(X,t)
=
\ell^4
\int_{|z-X|\ge8\ell}
\frac{|u(z,t)|^2}{|z-X|^5}\,dz.
}
\]

Then

\[
\|p_{\rm rem}-L_Xp_{\rm rem}\|_{L^{3/2}(B_{2\ell}(X))}
\lesssim
\mathfrak H_\ell.
\]

`mathfrak H_ell` is Navier--Stokes scale invariant.

The corresponding normalized pressure-work contribution obeys

\[
P_{\rm rem}
\lesssim
\mathfrak H_\ell
(C_RE_R)^{1/4}
\]

with a fixed parent radius `R` large enough to contain the support of the local cutoff.

## 3. Dyadic shell decomposition

Define the critical local kinetic-energy channel in the original inertial frame,

\[
M_R(X,t)
=
R^{-1}
\int_{B_R(X)}|u(x,t)|^2dx.
\]

For dyadic shells

\[
A_j
=
\{2^j\ell\le|z-X|<2^{j+1}\ell\},
\qquad j\ge3,
\]

we have

\[
\begin{aligned}
\mathfrak H_\ell
&\lesssim
\ell^4
\sum_{j\ge3}
(2^j\ell)^{-5}
\int_{A_j}|u|^2dz\\
&\lesssim
\sum_{j\ge3}
2^{-4j}
M_{2^{j+1}\ell}(X,t).
\end{aligned}
\]

Therefore

\[
\boxed{
\mathfrak H_\ell
\lesssim
\sum_{j\ge3}
2^{-4j}
M_{2^{j+1}\ell}.
}
\]

The crucial feature is the geometric weight `2^{-4j}`.

## 4. Macroscopically remote sources vanish at a singular scale

Let the total kinetic energy satisfy

\[
E_0=\int_{\mathbb R^3}|u(x,t)|^2dx<\infty.
\]

Then

\[
M_R(X,t)\le E_0/R.
\]

Fix a physical distance `L>0`, and choose `J` so that

\[
2^J\ell\simeq L.
\]

The contribution to `mathfrak H_ell` from scales larger than `L` satisfies

\[
\begin{aligned}
\sum_{j\ge J}
2^{-4j}M_{2^{j+1}\ell}
&\lesssim
\frac{E_0}{\ell}
\sum_{j\ge J}2^{-5j}\\
&\lesssim
E_0\frac{\ell^4}{L^5}.
\end{aligned}
\]

Hence

\[
\boxed{
\text{for fixed }L>0,
\qquad
\mathfrak H_{\ell,\,|z-X|\ge L}
=O(\ell^4)
\to0
\quad(\ell\to0).
}
\]

Thus a possible singularity cannot be maintained by a direct pressure injection from a region that stays a fixed positive distance away.

This is a locality statement about the **affine-free remote pressure contribution**, not a finite propagation-speed statement.  Incompressible pressure remains elliptically nonlocal.

## 5. What remains in the pressure channel

After this split, pressure has three structurally different parts.

1. **Near pressure**: generated inside a fixed parent multiple of `ell`; already controlled by the same cubic oscillation--dissipation block as relative advection.
2. **Transition pressure**: generated in the fixed annulus between the near and remote cutoffs; it belongs to the same finite-parent-scale block after enlarging the parent radius.
3. **Genuinely remote pressure**: represented by `mathfrak H_ell` and geometrically suppressed across distant dyadic scales.

Therefore pressure nonlocality does not supply an independent direct small-scale source from arbitrarily remote distances.

## 6. DSD multiscale cascade block

Use dyadic or fixed-ratio scales

\[
\ell_k=2^{-k}\ell_0
\]

(or a ratio matched to the chosen parent cutoff), and define the scale-indexed state

\[
\boxed{
\mathcal K_k(t)
=
\bigl(
C_k,
E_k,
\mathfrak H_k,
\lambda_{2,k}^+,
\Gamma_{\omega,k},
\text{cross}_k,
\ldots
\bigr).
}
\]

The one-step inequality supplies a directed relation

\[
\mathcal K_{k-1}
\longrightarrow
\mathcal K_k.
\]

The remote-pressure estimate shows that very distant scales enter this relation only with rapidly decaying weights.

This is the first point where the Channel-Indexed Static Aggregation viewpoint becomes genuinely multiscale: **radius/scale itself is an index over structural channels**, and the dynamics is a transfer relation between adjacent scale blocks.

## 7. Consequence for any hypothetical singularity

Combined with the pressure-free epsilon-regularity certificate, a hypothetical singular endpoint must support an arbitrarily long chain of small scales on which the internal oscillation/dissipation product remains non-small.

The present result adds:

\[
\boxed{
\text{that chain must be locally sustained in scale.}
}
\]

A macroscopically remote pressure source cannot jump directly to arbitrarily small scales with order-one affine-free strength.

This still does **not** exclude the cascade.  Critical profiles can carry only `O(ell)` kinetic energy at scale `ell`, so the global finite-energy bound alone is compatible with infinitely many nested critical scales.

## 8. Next proof obligation

The remaining question is whether an arbitrarily long locally sustained critical cascade is compatible with all of

- incompressibility;
- finite total energy and dissipation;
- strain/vorticity geometry;
- off-diagonal nonlinear couplings;
- the moving mean-zero oscillation budget.

The next tests should therefore add **occupancy/sparseness and directional-alignment channels** to `mathcal K_k` rather than introduce another pressure scalar.

Status: **OPEN CASCADE EXCLUSION**.
