# DSD Explicit Strain Interpolation and Active-Density Collapse

Date: 2026-08-25

Status: **EXPLICIT ENDPOINT-RIESZ-SAFE STRAIN CONSTANT DERIVED / B+ AND K2+ REDUCED TO ANALYTIC-STRIP AND TIGHTNESS DATA / DIRECT-AGMON SURVIVAL FLOOR COLLAPSED TO A SMALLER PARAMETER SET / GLOBAL REGULARITY UNPROVED.**

## 1. Explicit strain kernel bound

For divergence-free velocity in `R^3`, write the Biot-Savart law in vorticity form. Differentiating and taking the symmetric part removes the local antisymmetric distribution term. The strain is therefore a principal-value singular integral

\[
S(x)=\operatorname{p.v.}\int K(z)\omega(x-z)\,dz
\]

with spherical mean zero and a pointwise operator bound

\[
\boxed{
|K(z)|_{op,F}\le C_K|z|^{-3},
\qquad
C_K:=\frac{\sqrt3}{2\pi}.
}
\]

A safe derivation is obtained from the differentiated Biot-Savart tensor

\[
\frac1{4\pi}|z|^{-3}\epsilon_{ijk}(\delta_{j\ell}-3n_jn_\ell),
\qquad n=z/|z|,
\]

whose full tensor Frobenius norm is `sqrt(12)/(4pi)=sqrt(3)/(2pi)`; symmetrization cannot increase the norm.

## 2. Near/far split

Let

\[
K_1:=\|\nabla\omega\|_\infty,
\qquad
Z:=\|\omega\|_2^2.
\]

For `|z|<R`, spherical cancellation permits subtraction of the constant `omega(x)`. Thus

\[
\begin{aligned}
|S_{near}(x)|
&\le
C_KK_1\int_{|z|<R}|z|^{-2}dz\\
&=4\pi C_KK_1R.
\end{aligned}
\]

For `|z|>R`, Cauchy-Schwarz gives

\[
\begin{aligned}
|S_{far}(x)|
&\le
C_K Z^{1/2}
\left(\int_{|z|>R}|z|^{-6}dz\right)^{1/2}\\
&=C_K\left(\frac{4\pi}{3}\right)^{1/2}
Z^{1/2}R^{-3/2}.
\end{aligned}
\]

Hence

\[
\|S\|_\infty
\le
C_K\left[
4\pi K_1R
+
\left(\frac{4\pi}{3}\right)^{1/2}Z^{1/2}R^{-3/2}
\right].
\]

Optimizing in `R` gives

\[
\boxed{
\|S\|_\infty
\le
C_I K_1^{3/5}Z^{1/5},
}
\]

where

\[
\boxed{
C_I
=
\frac{5\sqrt3}{3}
6^{1/5}\pi^{-1/5}
\approx3.2855618909.
}
\]

Status: **PROVED with an explicit safe kernel constant.**

## 3. Cauchy bounds from the terminal analytic strip

The existing terminal restart-analyticity result supplies universal strip data `rho_0,M_0` on every terminal analytic window:

\[
\sup_{|\operatorname{Im}y|<\rho_0}|\Omega(y)|\le M_0.
\]

For every real unit direction `h`, one-variable Cauchy applied to

\[
z\mapsto\Omega(y+zh)
\]

gives the directional bounds

\[
\boxed{
\|D_h\Omega\|_\infty\le\frac{M_0}{\rho_0},
}
\]

and

\[
\boxed{
\|D_h^2\Omega\|_\infty\le\frac{2M_0}{\rho_0^2}.
}
\]

Thus the admissible first- and pure-second-derivative ceilings are

\[
\boxed{
K_{1,+}\le\frac{M_0}{\rho_0},
\qquad
K_{2,+}\le\frac{2M_0}{\rho_0^2}.
}
\]

Only these directional/pure-coordinate bounds are needed in the terminal thick-window argument.

## 4. Remove B+ using tightness

On the recurrent bounded dynamic-enstrophy corridor,

\[
Z_D\le Z_{D,+}.
\]

The non-T tightness reduction gives

\[
\boxed{
Z_{D,+}
\le
Z_{D,tight}
:=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Insert the Cauchy `K1` bound and `Z_D<=Z_{D,tight}` into the explicit strain interpolation:

\[
\boxed{
B_+
\le
B_0
:=
C_I
\left(\frac{M_0}{\rho_0}\right)^{3/5}
Z_{D,tight}^{1/5}.
}
\]

Hence `B_+` is not an independent survivor parameter.

## 5. Uniform lower bound for the terminal persistence duration

The terminal thick-window duration is

\[
\delta_D
=
\frac1{4(2B_++3\nu K_{2,+})}.
\]

Using the preceding upper bounds,

\[
\boxed{
\delta_D
\ge
\delta_0
:=
\frac1{
4\left(
2B_0+6\nu M_0\rho_0^{-2}
\right)
}.
}
\]

Thus the duration is reduced to tightness plus the universal restart-analyticity data.

## 6. A universal simplification of mu-

Recall

\[
\mu_-
=\frac{L_-}{q}e^{-B_+\delta_D}.
\]

But exactly

\[
B_+\delta_D
=
\frac{B_+}{4(2B_++3\nu K_{2,+})}
\le\frac18.
\]

Therefore

\[
\boxed{
\mu_-
\ge
\mu_{-,0}
:=
\frac{L_-}{q}e^{-1/8}.
}
\]

This lower bound no longer contains `B_+` or `K_{2,+}`.

## 7. Replace the old additive mu+ bound by the global Type-I clock ceiling

The continuous backward first-hitting estimate already gives, on the entire restricted ancient corridor,

\[
M_L(s)=T\|\Omega(s)\|_\infty
\le
K_I,
\]

where

\[
\boxed{
K_I=\frac{L_+q^2}{q-1}.
}
\]

On a terminal dynamic window, `mu=TM_D` is precisely this Leray maximum-amplitude variable. Hence one may safely take

\[
\boxed{
\mu_+\le K_I.
}
\]

Consequently

\[
\boxed{
\frac{\mu_-}{\mu_+}
\ge
\chi_0
:=
e^{-1/8}
\frac{L_-(q-1)}{L_+q^3}.
}
\]

This is stronger structurally than keeping the earlier additive upper bound `c_+ + delta_D exp(B_+delta_D)`.

## 8. Explicit lower bound for active Leray-time density

The checkpoint Leray-gap ceiling is

\[
\boxed{
G_L
=
\log\left[
q\frac{L_+q/(q-1)}{L_-/q}
\right].
}
\]

The active-window density satisfies

\[
d_L
=\min\left\{1,\frac{\delta_D}{\mu_+G_L}\right\}.
\]

Using `delta_D>=delta_0` and `mu_+<=K_I`,

\[
\boxed{
d_L
\ge
d_0
:=
\min\left\{
1,
\frac{\delta_0}{K_IG_L}
\right\}.
}
\]

Thus the active density is now explicitly bounded below using only

\[
q,L_-,L_+,R_Z,\varepsilon_Z,\nu,M_0,\rho_0
\]

and universal constants.

## 9. Insert into the direct-Agmon survival floor

The direct-Agmon note proved

\[
Z_{D,+}
\ge
\frac{\pi^2 3^{5/2}}{32}
 d_L^{3/16}
\nu^{3/2}
\left(\frac{\mu_-}{\mu_+}\right)^{1/2}.
\]

Therefore every recurrent survivor must satisfy the completely reduced necessary bound

\[
\boxed{
Z_{D,+}
\ge
Z_{D,red,-}
:=
\frac{\pi^2 3^{5/2}}{32}
 d_0^{3/16}
\nu^{3/2}
\chi_0^{1/2}.
}
\]

Equivalently,

\[
\boxed{
Z_{D,+}
\ge
4.8078720769
\,d_0^{3/16}
\nu^{3/2}
\left[
e^{-1/8}
\frac{L_-(q-1)}{L_+q^3}
\right]^{1/2}.
}
\]

Combined with tightness,

\[
\boxed{
Z_{D,red,-}
\le
Z_{D,+}
\le
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Hence the branch closes whenever

\[
\boxed{
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
<
Z_{D,red,-}.
}
\]

## 10. Parameter count after collapse

Before this note the survival floor involved

\[
q,L_-,L_+,B_+,K_{2,+},K_{3,+},R_Z,\varepsilon_Z,\nu.
\]

The direct-Agmon route already removed `K3+`. This note removes `B+` and `K2+` as independent variables.

The only solution-dependent geometric parameters left are

\[
\boxed{
q,L_-,L_+,R_Z,\varepsilon_Z
}
\]

plus viscosity and the universal restart-analyticity constants

\[
\boxed{M_0,\rho_0.}
\]

If one imports explicit numerical constants from a quantitative restart-analyticity theorem, even `M_0,rho_0` cease to be free parameters.

## 11. External analyticity audit

Classical and modern Navier-Stokes analyticity results do provide quantitative spatial derivative estimates and lower bounds on the spatial analyticity radius. The repository currently uses its already-imported restart formulation as the branch input; no stronger external numerical value for `M_0,rho_0` is asserted here.

Thus the logical status is:

- parameter reduction from `B+,K2+` to `M0,rho0,Z_tight`: **PROVED conditional on the existing restart-analyticity input**;
- a universal positive `d_0`: **PROVED on that corridor**;
- numerical universal evaluation of `M0,rho0`: **OPEN in the repository bookkeeping**.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]