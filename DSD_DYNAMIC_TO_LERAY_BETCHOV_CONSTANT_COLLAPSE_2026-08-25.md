# DSD Dynamic-to-Leray Betchov Constant Collapse

Date: 2026-08-25

Status: **EXACT DYNAMIC/LERAY SCALING OF `Z` AND HESSIAN CEILINGS DERIVED / ANALYTIC-THICKNESS BETCHOV CERTIFICATE REDUCED TO DYNAMIC PARAMETERS / ENDPOINT AMPLITUDE OBSTRUCTION IDENTIFIED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The previous analytic-thickness Betchov certificate is

\[
\mathcal B_{AZ}
:=
C_T^{-2/7}K_{2,L}^{3/7}Z_{L,+}^{2/7}
+
\frac{32}{729\pi^4}\frac{Z_{L,+}^2}{\nu^3}
<\frac12,
\]

where

\[
C_T=\frac{64\sqrt2\pi}{105},
\qquad
C_T^{-2/7}\approx0.7522879923.
\]

The repository still carries most analytic constants in the continuously dynamically normalized first-hitting coordinates. This note converts the certificate exactly into those coordinates and audits whether the resulting envelope can actually be small.

---

## 2. Dynamic and Leray coordinates

Let `M_D` be the running physical vorticity maximum along a dynamic first-hitting window and let

\[
\widetilde\Omega(z,s_D)
:=M_D^{-1}\Omega_{phys}(x,t),
\qquad
z=\sqrt{M_D}(x-x_c).
\]

Let

\[
T:=T^*-t>0
\]

and use standard Leray variables

\[
Y=\frac{x-x_c}{\sqrt T},
\qquad
W(Y,s_L)=T\Omega_{phys}(x,t).
\]

Define the dimensionless clock-amplitude factor

\[
\boxed{\mu:=TM_D.}
\]

Then

\[
\boxed{z=\sqrt\mu\,Y}
\]

(up to the common moving center) and

\[
\boxed{W(Y,s_L)=\mu\,\widetilde\Omega(z,s_D).}
\]

On the terminal analytic corridor the existing clock conversion gives

\[
0<\mu_-\le\mu\le\mu_+<\infty.
\]

---

## 3. Exact enstrophy scaling

Because

\[
dY=\mu^{-3/2}dz,
\]

we have

\[
\begin{aligned}
Z_L
&:=\int_{\mathbb R^3}|W|^2dY\\
&=\mu^2\mu^{-3/2}
\int|\widetilde\Omega|^2dz.
\end{aligned}
\]

Hence, with

\[
Z_D:=\|\widetilde\Omega\|_2^2,
\]

one obtains the exact identity

\[
\boxed{Z_L=\mu^{1/2}Z_D.}
\]

Therefore a uniform dynamic ceiling `Z_D<=Z_{D,+}` gives

\[
\boxed{Z_{L,+}\le\mu_+^{1/2}Z_{D,+}.}
\]

This improves the cruder replacement of the clock factor by a global Type-I supremum whenever `mu_+` is sharper.

Status: **PROVED.**

---

## 4. Exact Hessian scaling

Since

\[
W(Y)=\mu\widetilde\Omega(\sqrt\mu Y),
\]

one derivative contributes a factor `sqrt(mu)` and two derivatives contribute `mu`. Thus

\[
\boxed{
\nabla_Y^2W
=\mu^2\nabla_z^2\widetilde\Omega.
}
\]

Consequently, if the dynamic first-hitting analytic corridor satisfies

\[
\|\nabla_z^2\widetilde\Omega\|_\infty
\le K_{2,+},
\]

then

\[
\boxed{K_{2,L}\le\mu_+^2K_{2,+}.}
\]

Status: **PROVED.**

---

## 5. Collapse of the analytic Betchov certificate

Insert

\[
K_{2,L}\le\mu_+^2K_{2,+},
\qquad
Z_{L,+}\le\mu_+^{1/2}Z_{D,+}
\]

into the previous certificate.

The analytic-thickness term becomes

\[
\begin{aligned}
C_T^{-2/7}
K_{2,L}^{3/7}Z_{L,+}^{2/7}
&\le
C_T^{-2/7}
(\mu_+^2K_{2,+})^{3/7}
(\mu_+^{1/2}Z_{D,+})^{2/7}\\
&=
\mu_+
C_T^{-2/7}
K_{2,+}^{3/7}Z_{D,+}^{2/7}.
\end{aligned}
\]

The Betchov residual term becomes

\[
\frac{32}{729\pi^4}
\frac{Z_{L,+}^2}{\nu^3}
\le
\mu_+
\frac{32}{729\pi^4}
\frac{Z_{D,+}^2}{\nu^3}.
\]

Therefore the whole sufficient certificate reduces to

\[
\boxed{
\mu_+
\left[
C_T^{-2/7}K_{2,+}^{3/7}Z_{D,+}^{2/7}
+
\frac{32}{729\pi^4}\frac{Z_{D,+}^2}{\nu^3}
\right]
<\frac12.
}
\]

Numerically,

\[
\boxed{
\mu_+
\left[
0.7522879923\,K_{2,+}^{3/7}Z_{D,+}^{2/7}
+
0.000450632966\,\frac{Z_{D,+}^2}{\nu^3}
\right]
<\frac12.
}
\]

Thus all clock conversion losses collapse to one linear factor `mu_+`.

Status: **PROVED.**

---

## 6. Tightness reduction of `Z_{D,+}`

The existing recurrent-class tightness reduction gives, under dynamic first-hitting normalization `|widetilde Omega|<=1`,

\[
\int_{B_{R_Z}}|\widetilde\Omega|^2
\ge(1-\varepsilon_Z)Z_D.
\]

Therefore

\[
\boxed{
Z_{D,+}
\le
Z_{tight}
:=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Hence a fully reduced sufficient condition is

\[
\boxed{
\mu_+
\left[
C_T^{-2/7}K_{2,+}^{3/7}Z_{tight}^{2/7}
+
\frac{32}{729\pi^4}\frac{Z_{tight}^2}{\nu^3}
\right]
<\frac12.
}
\]

At this point the surviving quantitative inputs are only the clock amplitude `mu_+`, dynamic analytic curvature `K_{2,+}`, tightness data `(R_Z,epsilon_Z)`, and viscosity.

No global velocity-tail norm enters.

---

## 7. Endpoint nontriviality creates a structural lower bound

At every dynamic first-hitting endpoint,

\[
\|\widetilde\Omega\|_\infty=1.
\]

Apply the same exact Taylor-thickness lemma in the dynamic coordinates with Hessian ceiling `K_{2,+}`. It gives

\[
\boxed{
Z_D
\ge
C_TK_{2,+}^{-3/2}.
}
\]

Therefore any uniform dynamic enstrophy ceiling valid at the endpoint obeys

\[
Z_{D,+}
\ge
C_TK_{2,+}^{-3/2}.
\]

Substituting this lower bound into the first bracketed term gives

\[
\begin{aligned}
C_T^{-2/7}K_{2,+}^{3/7}Z_{D,+}^{2/7}
&\ge
C_T^{-2/7}K_{2,+}^{3/7}
(C_TK_{2,+}^{-3/2})^{2/7}\\
&=1.
\end{aligned}
\]

Hence the envelope certificate necessarily satisfies

\[
\boxed{
\mathcal B_{AZ}^{env}\ge\mu_+.
}
\]

Since the viscous/Betchov residual term is also nonnegative, the sufficient closure condition can hold only if

\[
\boxed{\mu_+<\frac12.}
\]

This is not a numerical accident. It is the exact cancellation between the Taylor-thickness upper estimate for amplitude and the Taylor-thickness lower estimate forced by the normalized endpoint maximum.

Status: **PROVED NECESSARY CONDITION FOR THIS ENVELOPE-BASED CLOSURE CERTIFICATE.**

---

## 8. Relation to the old coarse `K_I` obstruction

The earlier Betchov closure used the coarse all-time Type-I amplitude supremum

\[
K_I=\frac{L_+q^2}{q-1}.
\]

The dynamic-to-Leray terminal conversion instead gives

\[
\mu_+
=
\frac{L_+q}{q-1}
+
\delta_De^{B_+\delta_D},
\qquad
\delta_D=
\frac1{4(2B_++3\nu K_{2,+})}.
\]

Thus the new necessary small-amplitude requirement is potentially weaker than `K_I<1/2`, especially because the geometric factor is `q/(q-1)` rather than `q^2/(q-1)`.

However the repository currently proves only finiteness of the surviving stage/analytic constants, not the universal inequality `mu_+<1/2`.

Therefore no unconditional closure is obtained here.

---

## 9. Why uniform-envelope improvement has reached its limit

The preceding cancellation shows that replacing the actual weighted amplitude

\[
\overline M_Z
=
\frac{\langle M_LZ_L\rangle}{\langle Z_L\rangle}
\]

by a product of independent uniform ceilings `K2_L` and `Z_L,+` cannot by itself beat the endpoint Type-I amplitude scale.

In particular, further improvements of the same form

\[
M_L
\le
C K_{2,L}^{3/7}Z_L^{2/7}
\]

followed immediately by

\[
K_{2,L}\le K_{2,L,+},
\qquad
Z_L\le Z_{L,+}
\]

will retain this obstruction.

The next higher-leverage target must therefore keep temporal correlation information instead of taking both suprema separately.

The natural quantity is still

\[
\boxed{
\overline M_Z
=
\frac{\langle M_LZ_L\rangle}{\langle Z_L\rangle},
}
\]

with one of the following refinements:

1. estimate `M_L` by the actual instantaneous `Z_L` and `K2_L(s)` and average before taking ceilings;
2. exploit the exact first-hitting clock observable `Theta_j`/`mu(s)` and its recurrence law;
3. show high `M_L` and high `Z_L` cannot occupy the same positive-density recurrent times without paying the existing `H/T/projective` costs.

---

## 10. Updated frontier

The analytic-thickness route has now been audited to its uniform-envelope endpoint:

\[
\boxed{
\text{uniform analytic thickness}
\Longrightarrow
\mathcal B_{AZ}^{env}
\ge\mu_+.
}
\]

Therefore the next calculation should not merely seek smaller standalone values of `K_{2,+}` and `Z_{D,+}`.

It should attack the correlation-sensitive recurrent quantity

\[
\boxed{\langle M_LZ_L\rangle}
\]

directly, preferably using the exact first-hitting/Leray clock recursion and the already derived positive-density active-core frequency floor.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
