# Fixed positive-volume material core exclusion

Date: 2026-08-13

Status: **DERIVED CONDITIONAL EXCLUSION + EXTERNAL BKM CONTINUATION CRITERION / OPEN MATERIAL-TURNOVER CLOSURE**.

This note rules out one important residual geometry: the same positive-volume material tube cannot remain, all the way to a finite singular time, a natural-area intense oriented-vorticity core with uniformly nontrivial signed flux.

The argument is conditional on a controlled tube foliation stated below.  It is not a proof of global regularity.

---

## 1. Material tube and fixed volume

Let `T*<infinity` be a hypothetical first singular time and let

\[
\mathcal T(t)=X(\mathcal T_0,t)
\]

be the image of one fixed material tube under the incompressible flow map.

Because

\[
\det D_aX=1,
\]

its volume is constant:

\[
\boxed{
|\mathcal T(t)|=V_0>0.
}
\]

Assume the tube admits a regular axial foliation by cross-sections `D_s(t)` with arclength coordinate `s` and a geometric Jacobian bounded above and below by fixed constants.  In the clean straight-tube model,

\[
dx=dA\,ds.
\]

To keep constants explicit below, write the comparability as

\[
K_g^{-1}\int A(s,t)ds
\le V_0\le
K_g\int A(s,t)ds,
\qquad K_g\ge1.
\]

---

## 2. Natural-area hypothesis

Let

\[
W(t)=\|\omega(t)\|_\infty.
\]

Assume every relevant cross-section satisfies

\[
\boxed{
A(s,t)\le\frac{C_A}{W(t)}
}
\]

for fixed `C_A>0`.

This is exactly the area scale corresponding to a natural vorticity radius

\[
r(t)\asymp W(t)^{-1/2}.
\]

The volume constraint then forces the tube length to grow:

\[
V_0
\le K_g A_{\max}(t)L(t)
\le K_g\frac{C_A}{W(t)}L(t).
\]

Hence

\[
\boxed{
L(t)
\ge
\frac{V_0}{K_gC_A}W(t).
}
\]

Thus a fixed positive-volume material object cannot become natural-radius thin without becoming proportionally long.

---

## 3. Robust signed-flux hypothesis

Assume the same orientation of vorticity crosses every section with

\[
\boxed{
|\Phi(s,t)|
=
\left|\int_{D_s(t)}\omega\cdot n_s\,dA\right|
\ge\Gamma_0>0
}
\]

for a fixed `Gamma_0`.

At the natural area scale this is the natural order of magnitude, because

\[
W A\sim1.
\]

By Cauchy--Schwarz on each section,

\[
\int_{D_s(t)}|\omega|^2dA
\ge
\frac{\Phi(s,t)^2}{A(s,t)}
\ge
\frac{\Gamma_0^2}{C_A}W(t).
\]

Integrating axially and using the geometric lower comparison gives

\[
\begin{aligned}
E_\omega(t)
=\int_{\mathbb R^3}|\omega|^2dx
&\ge
\int_{\mathcal T(t)}|\omega|^2dx\\
&\ge
K_g^{-1}
\frac{\Gamma_0^2}{C_A}W(t)L(t).
\end{aligned}
\]

Substituting the length lower bound,

\[
\boxed{
E_\omega(t)
\ge
\frac{\Gamma_0^2V_0}{K_g^2C_A^2}
W(t)^2.
}
\]

This is the core estimate.

---

## 4. Global viscous budget forces `W in L^2_t`

For a smooth finite-energy whole-space solution on `[0,T*)`,

\[
\nu\int_0^{T^*}E_\omega(t)dt
\le
\frac12\|u_0\|_2^2.
\]

Therefore the fixed-material-core estimate implies

\[
\boxed{
\int_0^{T^*}W(t)^2dt
\le
\frac{K_g^2C_A^2}{\Gamma_0^2V_0}
\frac{\|u_0\|_2^2}{2\nu}
<\infty.
}
\]

Since `T*<infinity`, Cauchy--Schwarz gives

\[
\boxed{
\int_0^{T^*}W(t)dt<\infty.
}
\]

---

## 5. External continuation criterion

The classical Beale--Kato--Majda continuation criterion for 3D Navier--Stokes states that finiteness of

\[
\int_0^{T^*}\|\omega(t)\|_\infty dt
\]

precludes breakdown of regularity at `T*`.

A primary modern source explicitly recording the Navier--Stokes criterion is:

- Xiaoyutao Luo, *A Beale-Kato-Majda criterion with optimal frequency and temporal localization*, arXiv:1803.05569, eq. (1.2).

Thus the hypotheses above contradict `T*` being a finite singular time.

We obtain the conditional exclusion:

\[
\boxed{
\begin{gathered}
V_0>0\text{ fixed material tube},\\
A(s,t)\lesssim W(t)^{-1},\\
|\Phi(s,t)|\ge\Gamma_0>0\text{ on all sections}
\end{gathered}
\quad\Longrightarrow\quad
\text{no finite-time singularity while these persist.}
}
\]

---

## 6. What this actually removes

This excludes a picture in which one fixed positive amount of fluid/vorticity-supporting material is continuously squeezed to the natural transverse scale while retaining an order-one oriented vorticity flux.

The exclusion uses only:

1. incompressible material-volume preservation;
2. natural-area geometry;
3. signed-flux persistence;
4. the global enstrophy dissipation budget;
5. the external BKM continuation criterion.

No pressure estimate is needed.

---

## 7. Residual escape routes

A hypothetical singular core must therefore violate at least one hypothesis.  The meaningful possibilities are:

### M1. Material turnover

The material occupying the dangerous core is continually replaced, so no fixed positive `V_0` survives in the core.

### M2. Viscous flux erosion/recreation

The signed material flux is repeatedly destroyed and recreated; this is charged to the material-flux erosion / palinstrophy channel.

### M3. Loss of natural-area tube geometry

The intense set ceases to admit the assumed natural-area cross-sectional foliation.  Then occupancy/sparseness/projective geometry must be used instead.

### M4. Strong tube distortion

The foliation Jacobian constant `K_g` becomes large.  This returns to the Lagrangian deformation / strain channel.

Hence the genuinely new residual branch is **material turnover of the intense core**.

---

## 8. DSD channel interpretation

The material identity of the core should now be typed separately from its instantaneous geometry.

Define a material-retention channel

\[
\boxed{
\mathcal R_{\rm mat}(t_0,t)
=
\frac{
|\mathcal C(t)\cap X(\mathcal C(t_0),t;t_0)|
}{
|\mathcal C(t)|
},
}
\]

for a chosen dangerous core `C(t)`.

- `R_mat near 1`: the same material persists;
- `R_mat small`: strong material turnover.

The fixed-material-core exclusion says that a residual singular cascade cannot keep a positive-volume material subset with retention bounded away from zero forever while also maintaining the robust natural-area/flux hypotheses.

---

## 9. Principal next target

Quantify the cost of repeatedly replacing the material inside a shrinking dangerous core.

A useful next object is the symmetric-difference turnover rate between

\[
\mathcal C(t+dt)
\]

and the material image

\[
X(\mathcal C(t),t+dt;t).
\]

If high turnover is caused by relative motion of the threshold boundary rather than by material advection, the vorticity equation should charge it to

- diffusion across the threshold boundary;
- strain-driven magnitude growth across the threshold;
- or threshold-level geometric area.

Status: **OPEN MATERIAL-TURNOVER / THRESHOLD-FLUX CLOSURE**.
