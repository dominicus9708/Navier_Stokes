# DSD M17-046 — The far cubic pressure tensor has an exact source-production / shell-turnover / relative-transport law

Date: 2026-09-04
Canonical ID: **M17-046**

Status: **INTERNAL FAR-PRESSURE MOMENT DYNAMICS / THE DEGREE-THREE FAR PRESSURE COEFFICIENT USED BY M17-045 IS NOT THE SAME OBJECT AS THE TERMINAL ODD FUCHSIAN MULTIPOLE OF M5-142--144. FOR A MATERIAL CORE CENTER `Y'=B(Y)`, A SMOOTH MOVING NEAR/FAR CUTOFF GIVES AN EXACT NEWTONIAN REPRESENTATION OF THE FAR CUBIC TENSOR `C^{far}=nabla^3 P_far(Y)`. ITS MATERIAL-CENTER DERIVATIVE SPLITS EXACTLY INTO THREE CHANNELS: PRESSURE-SOURCE PRODUCTION `D_B S_P+(3/2)S_P`, ANNULAR CUTOFF/SHELL TURNOVER, AND RELATIVE TRANSPORT BY `B(y)-B(Y)` AGAINST THE ORDER-THREE NEWTONIAN KERNEL. THUS THE CUBIC ORIENTATION IS NOT KINEMATICALLY FROZEN; PERSISTENT DSAIG LOCKING REQUIRES A RECURRENT BALANCE OF THESE THREE GLOBAL CHANNELS WITH THE LOCAL VISCOUS/NEAR-PRESSURE TENSOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pressure source

M17-045 gives

\[
-\Delta P=S_P,
\qquad
S_P:=|\Sigma|^2-\frac12\rho^2.
\]

Let `Y(theta)` be the marked material nodal-core center,

\[
\boxed{Y'=B(Y,\theta).}
\]

Choose a smooth radial cutoff `chi_R(z)` with

\[
\chi_R=1\quad\text{for }|z|\le R,
\qquad
\chi_R=0\quad\text{for }|z|\ge 2R,
\]

and set

\[
\boxed{w_R(y,Y):=1-\chi_R(y-Y).}
\]

Define the far pressure by

\[
\boxed{
P_{far}(x)
:=(-\Delta)^{-1}(w_R S_P)(x).
}
\]

Because `w_R=0` in a neighborhood of `Y`,

\[
\Delta P_{far}=0
\]

near the marked core.

---

## 2. Cubic tensor

Let

\[
G(z)=\frac1{4\pi|z|}
\]

be the Newtonian kernel for `-Delta`.
Define

\[
\boxed{
K^{(3)}_{ijk}(z):=\partial_{z_i z_j z_k}G(z).
}
\]

Then the far cubic pressure tensor at the material center is

\[
\boxed{
C^{far}_{ijk}(\theta)
:=\partial_{ijk}P_{far}(Y(\theta),\theta)
=\int_{\mathbb R^3}
 w_R(y,Y)S_P(y,\theta)
 K^{(3)}_{ijk}(Y-y)\,dy.
}
\]

It is fully symmetric.
Harmonicity near `Y` gives the trace constraints

\[
\boxed{C^{far}_{iik}=0}
\]

for each remaining index `k`.

The kernel scales as

\[
|K^{(3)}(z)|\lesssim |z|^{-4}.
\]

---

## 3. Differentiate along the material center

Let

\[
\mathcal D_Y:=\partial_\theta+B(Y,\theta)\cdot\nabla_Y.
\]

Since `Y'=B(Y)`, this is the derivative of the coefficient observed at the material core.
Differentiate the moment representation:

\[
\begin{aligned}
\mathcal D_Y C^{far}
={}&\int w_R(\partial_\theta S_P)K^{(3)}\,dy\\
&+\int [B(Y)\cdot\nabla_Y w_R]S_PK^{(3)}\,dy\\
&+\int w_RS_P[B(Y)\cdot\nabla_YK^{(3)}]\,dy.
\end{aligned}
\]

Now use

\[
\partial_\theta S_P=D_BS_P-B(y)\cdot\nabla_yS_P.
\]

Integrate the transport term by parts in `y`.
Because

\[
\nabla\cdot B=\frac32,
\qquad
\nabla_yK^{(3)}(Y-y)=-\nabla_YK^{(3)}(Y-y),
\]

and

\[
\nabla_Yw_R=-\nabla_yw_R,
\]

all terms group into three exact channels.

---

## 4. Exact far-cubic transport identity

The result is

\[
\boxed{
\begin{aligned}
\mathcal D_Y C^{far}_{ijk}
={}&\int w_R
\left(D_BS_P+\frac32S_P\right)
K^{(3)}_{ijk}(Y-y)\,dy\\
&+\int S_P
\big(B(y)-B(Y)\big)\cdot\nabla_yw_R
\,K^{(3)}_{ijk}(Y-y)\,dy\\
&+\int w_RS_P
\big(B(Y)-B(y)\big)\cdot\nabla_YK^{(3)}_{ijk}(Y-y)\,dy.
\end{aligned}
}
\]

Call the three terms

\[
\boxed{
\mathcal P_3^{far}
+\mathcal T_3^{shell}
+\mathcal R_3^{rel}.
}
\]

Thus

\[
\boxed{
\mathcal D_Y C^{far}
=\mathcal P_3^{far}
+\mathcal T_3^{shell}
+\mathcal R_3^{rel}.
}
\]

---

## 5. Interpretation of the three channels

### 5.1 Source-production channel

\[
\boxed{
\mathcal P_3^{far}
=
\int w_R
\left(D_BS_P+\frac32S_P\right)K^{(3)}\,dy.
}
\]

This is the genuine evolution of the pressure-Poisson source, corrected by the exact similarity material-volume rate `3/2`.

### 5.2 Shell-turnover channel

\[
\boxed{
\mathcal T_3^{shell}
=
\int S_P
(B(y)-B(Y))\cdot\nabla_yw_R
\,K^{(3)}\,dy.
}
\]

Since `grad w_R` is supported only on the annulus

\[
R\lesssim|y-Y|\lesssim2R,
\]

this term is the exact turnover of source material across the moving near/far partition.

### 5.3 Relative-transport channel

\[
\boxed{
\mathcal R_3^{rel}
=
\int w_RS_P
(B(Y)-B(y))\cdot\nabla_YK^{(3)}\,dy.
}
\]

Because

\[
|\nabla K^{(3)}(z)|\lesssim|z|^{-5},
\]

this is the deformation of the cubic moment caused by relative motion of the far source with respect to the marked core.

---

## 6. Explicit source-production formula

The pressure source is

\[
S_P=|\Sigma|^2-\frac12\rho^2.
\]

M17-044 gives

\[
D_B\Sigma
=\Delta\Sigma-\Sigma-\Sigma^2-\Omega^2-\nabla^2P.
\]

On the CE-H branch,

\[
D_B\rho=(\sigma+\kappa-1)\rho.
\]

Therefore

\[
\boxed{
\begin{aligned}
D_BS_P
={}&2\Sigma:\Delta\Sigma
-2|\Sigma|^2
-2\operatorname{tr}(\Sigma^3)
-2\Sigma:\Omega^2\\
&-2\Sigma:\nabla^2P
-(\sigma+\kappa-1)\rho^2.
\end{aligned}
}
\]

Hence the source-production density entering the cubic moment is

\[
\boxed{
\begin{aligned}
D_BS_P+\frac32S_P
={}&2\Sigma:\Delta\Sigma
-\frac12|\Sigma|^2
-2\operatorname{tr}(\Sigma^3)
-2\Sigma:\Omega^2\\
&-2\Sigma:\nabla^2P
-\left(\sigma+\kappa-\frac14\right)\rho^2.
\end{aligned}
}
\]

No sign is fixed.

---

## 7. The DSAIG-visible cubic contraction

M17-045 uses the horizontal trace-free contraction

\[
\boxed{
T_p^{far}
:=TF_h\big[p_\ell C^{far}_{\ell\alpha\beta}\big],
\qquad \alpha,\beta\in\{1,2\}.
}
\]

The slant direction obeys

\[
D_Bp=3\lambda p,
\]

so its normalized direction is materially frozen.
The nodal anisotropy tensor obeys

\[
D_BQ_0=(\kappa-3/2)Q_0,
\]

so its normalized tensor direction is also frozen.

Therefore any change of the **orientation** of `T_p^{far}` relative to the fixed material tensor line `span(Q_0)` must come from the cubic-moment dynamics above, not from rotation of `p` or `Q_0`.

---

## 8. Important distinction from M5 odd resonant multipoles

M5-142 interprets the terminal odd pressure multipoles as renormalized center-supported stress moments.
M5-144 shows realized resonant coefficients are invariant on the compact minimal W1 set.

The present object

\[
C^{far}_{ijk}(\theta)
=\nabla^3P_{far}(Y(\theta),\theta)
\]

is different:

1. it is an instantaneous local harmonic coefficient generated by the current far source;
2. its center `Y(theta)` moves materially;
3. its near/far partition moves;
4. its exact derivative has source-production, shell-turnover, and relative-transport terms.

Hence

\[
\boxed{
\text{M5 terminal odd-multipole invariance}
\not\Rightarrow
D_B C^{far}=0.
}
\]

This prevents a descriptor substitution error.

---

## 9. DSD audit

### Audit A — treating the cubic far tensor as frozen
Rejected by the exact transport identity.

### Audit B — identifying it with the M5 terminal resonant octupole
Rejected; they are different descriptors with different centers and limiting procedures.

### Audit C — ignoring moving-cutoff turnover
Rejected; `T_3^{shell}` is an explicit annular source-exchange term.

### Audit D — treating far dynamics as pure source time derivative
Rejected; relative motion against the moment kernel contributes independently.

### Audit E — using boundedness as a sign contradiction
Rejected; all three channels are signed.

---

## 10. Updated pressure-alignment frontier

The slanted DSAIG condition of M17-045 now requires a recurrent cancellation involving a cubic far tensor whose evolution is itself constrained by

\[
\boxed{
\mathcal D_Y C^{far}
=\mathcal P_3^{far}
+\mathcal T_3^{shell}
+\mathcal R_3^{rel}.
}
\]

Thus persistent slanted alignment cannot be achieved by choosing one static far cubic orientation once and for all.
It requires the global pressure-source architecture, annular turnover, and relative transport to keep regenerating the required tensor orientation.

---

## 11. Next target — cubic locking derivative gate

Differentiate the full DSAIG alignment

\[
P_{Q_0}^{\perp}
\left(V_p-N_p^{near}-T_p^{far}-N_{p,\ge4}^{far}\right)=0
\]

along the material nodal core.
Because the directions of `p` and `Q_0` are frozen, any nonzero perpendicular derivative must be cancelled by the next higher viscous/pressure moments.

The next calculation should determine whether the resulting condition is an automatic consequence of the Navier--Stokes equations or a genuinely new fifth-jet / quartic-pressure compatibility requirement.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
