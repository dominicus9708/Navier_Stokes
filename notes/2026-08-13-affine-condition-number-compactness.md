# Affine-background compactness needs only bounded deformation condition number

Date: 2026-08-13

Status: **EXACT AFFINE CANCELLATION + UNIFORMLY ELLIPTIC LOCAL VORTICITY SYSTEM / SHARPER THAN `int |S_aff|` SUFFICIENT CONDITION**.

The previous bounded-affine local bootstrap used

\[
\int|S_{\rm aff}(s)|ds\le K
\]

as a sufficient condition.  That is stronger than necessary.  A rapidly varying affine strain can have a large absolute time integral while its net deformation remains bounded.  The correct geometric state variable is the affine flow-gradient condition number.

---

## 1. Affine plus residual decomposition

After removing a common translation, write the normalized local velocity as

\[
\boxed{
U(y,s)=L(s)y+v(y,s),
\qquad
\operatorname{tr}L(s)=0.
}

Then

\[
\nabla U=L+\nabla v.
\]

The normalized vorticity equation is

\[
\partial_s\Omega
+U\cdot\nabla_y\Omega
=
\Omega\cdot\nabla_yU
+\nu\Delta_y\Omega.
\]

---

## 2. Affine flow map

Let

\[
\boxed{
F'(s)=L(s)F(s),
\qquad
F(s_0)=I.
}
\]

Since `tr L=0`,

\[
\boxed{
\det F(s)=1.
}
\]

Introduce affine coordinates

\[
\boxed{y=F(s)z.}
\]

Transform the vorticity as a vector:

\[
\boxed{
\Omega(F(s)z,s)=F(s)W(z,s).
}
\]

Define the residual velocity

\[
\boxed{
\widetilde v(z,s)
=F(s)^{-1}v(F(s)z,s).
}
\]

---

## 3. Exact cancellation of affine advection and stretching

At fixed `y`,

\[
\partial_s z
=-F^{-1}LFz.
\]

Differentiating `Omega=FW` gives a term

\[
F'W=LFW
\]

and a coordinate-motion term

\[
-F(F^{-1}LFz\cdot\nabla_zW).
\]

Meanwhile the affine advection contributes

\[
(Ly\cdot\nabla_y)\Omega
=F(F^{-1}LFz\cdot\nabla_zW)
\]

and affine stretching contributes

\[
(\Omega\cdot\nabla)(Ly)
=L\Omega=LFW.
\]

Hence the affine transport and affine stretching cancel **exactly** in the transformed material-linear frame.

---

## 4. Residual nonlinear terms retain the vorticity form

Because

\[
\nabla_z\widetilde v
=F^{-1}(\nabla_yv)F,
\]

we obtain

\[
F^{-1}(v\cdot\nabla_y\Omega)
=\widetilde v\cdot\nabla_zW,
\]

and

\[
F^{-1}(\Omega\cdot\nabla_yv)
=W\cdot\nabla_z\widetilde v.
\]

Moreover

\[
\nabla_z\cdot\widetilde v=0,
\qquad
\nabla_z\cdot W=0.
\]

---

## 5. Anisotropic diffusion metric

Since `F` is spatially constant,

\[
\Delta_y(FW)
=F\,\nabla_z\cdot(A(s)\nabla_zW),
\]

where

\[
\boxed{
A(s)=F(s)^{-1}F(s)^{-T}.
}
\]

Thus the exact transformed vorticity equation is

\[
\boxed{
\partial_sW
+\widetilde v\cdot\nabla_zW
=
W\cdot\nabla_z\widetilde v
+\nu\nabla_z\cdot(A(s)\nabla_zW).
}
\]

This is a uniformly parabolic vorticity system whenever `F` and `F^-1` remain bounded.

---

## 6. Condition-number channel

Define

\[
\boxed{
\mathcal K_F
=\sup_{s\in I}
\max\{\|F(s)\|_{op},\|F(s)^{-1}\|_{op}\}.
}
\]

If

\[
\mathcal K_F\le K,
\]

then

\[
\boxed{
K^{-2}I
\le A(s)\le
K^2I.
}
\]

Hence the diffusion remains uniformly elliptic.

This condition is weaker than an `L1_t` bound on the absolute affine strain.  Indeed

\[
\mathcal K_F
\le
\exp\left(
\int|S_{\rm aff}|ds
\right),
\]

but the reverse need not hold because time-dependent strain can partly reverse/cancel.

---

## 7. `H1` derivative energy does not require `A'(s)`

Differentiate the transformed PDE in a spatial coordinate `z_k` and test against `partial_k W`.

The diffusion contribution is

\[
-\nu
\int
\nabla\partial_kW
:\,A(s)\,
\nabla\partial_kW\,dz.
\]

Since `A` depends only on time, no spatial derivative lands on `A`, and because the energy used is the ordinary Euclidean

\[
\|\nabla W\|_2^2,
\]

no time derivative `A'` appears either.

Uniform ellipticity gives

\[
\boxed{
\nu
\int
\nabla\partial_kW:A\nabla\partial_kW
\ge
\nu K^{-2}
\|\nabla\partial_kW\|_2^2.
}
\]

Thus arbitrary temporal oscillation of the affine background is harmless to the derivative-energy estimate as long as the deformation condition number remains bounded.

---

## 8. Local V2 bootstrap on the bounded-condition branch

The first-hitting amplitude cap gives, on fixed transformed balls comparable under `K`, uniform finite-`Lp` bounds for `W` and the residual local vorticity.

The near singular-integral estimates for `grad v_tilde` inherit constants depending on `K` and the fixed buffer.

Using nested cutoffs exactly as in the bounded-affine bootstrap gives

\[
\boxed{
\mathcal P'(s)
+c_{\nu,K}\mathcal Z(s)
\le
C_{K,R,\nu}
[1+\mathcal P(s)].
}
\]

A localized enstrophy estimate on an earlier subinterval supplies a good `H1` slice, and Gronwall yields on the terminal subwindow

\[
\boxed{
\sup\|\nabla W\|_2^2
+
\int\|\nabla^2W\|_2^2ds
\le
C(K,R,\nu,\delta).
}
\]

Transforming back gives equivalent local `H1/V2` control for `Omega`, with constants depending on `K`.

---

## 9. Compactness dichotomy sharpened

The local first-hitting proof no longer needs either

1. bounded global normalized enstrophy; or
2. bounded `int |S_aff|`.

The sharper split is

\[
\boxed{
\mathcal K_F\to\infty
}
\]

or

\[
\boxed{
\mathcal K_F\le K
\Longrightarrow
\text{uniformly parabolic local system}
\Longrightarrow
\text{terminal local }H^1/V2\text{ compactness}.
}
\]

Thus the genuine affine escape route is **degeneration of the mesoscopic affine deformation**, not merely a large instantaneous/background strain norm.

---

## 10. Relation to Cauchy I/V channels

The same `F` is the affine component of the material deformation used in the Cauchy amplification formula.

If

\[
\mathcal K_F\to\infty,
\]

then at least one singular value of `F` or `F^-1` diverges.  Since `det F=1`, this means strong anisotropic stretching/compression.

For material directions,

\[
\frac d{ds}\log|Fv|
=e^TS_{\rm aff}e.
\]

Hence condition-number blowup requires an unbounded accumulated directional-strain excursion along some sequence of material directions.

This feeds directly into the existing strain/deformation lane rather than defining a separate unrelated failure.

---

## 11. DSD interpretation

A complicated remote/intermediate field is reduced, at the tracked core scale, to a finite-dimensional deformation matrix `F(s)` plus small non-affine remainder.

The criterion for whether this background must be resolved further is simply whether its **observable geometric action** degenerates:

\[
\boxed{
\text{bounded }F,F^{-1}
\Rightarrow
\text{background absorbed into coefficients},
}

\[
\boxed{
\text{unbounded condition number}
\Rightarrow
\text{follow the affine-deformation IC branch}.
}

This is a sharper implementation of adaptive describability than tracking the absolute remote strain at every instant.

Status: **BOUNDED-CONDITION LOCAL COMPACTNESS CLOSED / CONDITION-NUMBER CASCADE IS THE AFFINE RESIDUAL**.
