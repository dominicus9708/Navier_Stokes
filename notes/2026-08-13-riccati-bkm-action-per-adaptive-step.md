# Riccati-to-BKM action lower bound on each bounded-affine adaptive step

Date: 2026-08-13

Status: **DERIVED SCALE-INVARIANT ACTION LOWER BOUND / CONSISTENT WITH BKM BLOW-UP NECESSITY**.

The bounded-affine Riccati barrier gives more than a duration lower bound.  It forces a logarithmic amount of the scale-invariant Beale--Kato--Majda vorticity action on every large adaptive first-hitting step.

This is not a contradiction: a finite-time singularity would already require divergence of this action.  The result identifies the remaining bounded-affine route as a BKM-critical saturation branch.

---

## 1. Riccati envelope

On a terminal-normalized first-hitting interval, let

\[
M(s)=\|\Omega(s)\|_\infty.
\]

The bounded-affine Gaussian residual estimate gives

\[
M(t)
\le a+C_K\int_{s_0}^tM(s)^2ds,
\qquad
a=\frac{K_F}{q}.
\]

Define

\[
Y(t)=a+C_K\int_{s_0}^tM(s)^2ds.
\]

Then

\[
M(t)\le Y(t),
\qquad
Y'(t)=C_KM(t)^2.
\]

At the terminal checkpoint `M(T)=1`, hence `Y(T)>=1`.

---

## 2. Integrate the amplitude action

On intervals where `M>0`,

\[
M(s)ds
=\frac{1}{C_KM(s)}dY(s).
\]

Since

\[
M(s)\le Y(s),
\]

we have

\[
\frac1{M(s)}\ge\frac1{Y(s)}.
\]

Therefore

\[
\begin{aligned}
\int_{s_0}^TM(s)ds
&\ge
\frac1{C_K}
\int_{Y(s_0)}^{Y(T)}\frac{dY}{Y}\\
&\ge
\frac1{C_K}\log\frac1a.
\end{aligned}
\]

Thus, for `q>K_F`,

\[
\boxed{
\int_{s_0}^TM(s)ds
\ge
c_K\log\frac{q}{K_F}.
}
\]

---

## 3. Scaling back to physical variables

At terminal vorticity scale `W`,

\[
\Omega=r^2\omega,
\qquad
r=W^{-1/2},
\qquad
ds=Wdt.
\]

Hence

\[
M(s)=W^{-1}\|\omega(t)\|_\infty.
\]

Therefore exactly

\[
\boxed{
M(s)ds
=\|\omega(t)\|_\infty dt.
}
\]

The normalized action is the physical BKM action.

Consequently each bounded-affine adaptive step obeys

\[
\boxed{
\int_{t_-}^{T}
\|\omega(t)\|_\infty dt
\ge
c_K\log\frac{q}{K_F}.
}
\]

---

## 4. Recursive adaptive sequence

For the checkpoint rule

\[
q_j=W_j^{1/3+2\varepsilon},
\]

up to the indexing convention of the previous/terminal levels,

\[
\log q_j
\asymp\log W_j.
\]

Thus if infinitely many adaptive steps remain in the same bounded-affine class, the cumulative BKM action necessarily diverges.

This is entirely consistent with the standard blow-up necessity and is not a contradiction.

---

## 5. Meaning for the proof route

The remaining bounded-affine singular scenario is now more rigid:

\[
\boxed{
\text{large adaptive amplification}
\Longrightarrow
\text{previous-natural-time duration}
+\text{logarithmic BKM action}.
}
\]

Therefore the next proof-producing task is not to prove BKM divergence; that is already compatible with a singularity.  It is to show that this BKM action cannot be realized indefinitely while simultaneously avoiding

- projective/coherence regularity gates;
- angular-palinstrophy depletion;
- the non-affine mesoscopic residual packing bounds;
- affine compression-diffusion/precursor constraints;
- pressure-Hessian/eigenframe costs.

In DSD language, the scalar BKM action must be decomposed into its active structural channels rather than treated as an undifferentiated global norm.

Status: **BOUNDED-AFFINE LONG STEP IDENTIFIED AS BKM-CRITICAL SATURATION / STRUCTURAL DEPLETION OF THAT ACTION REMAINS OPEN**.
