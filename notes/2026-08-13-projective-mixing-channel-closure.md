# Projective mixing-channel closure inequalities

Date: 2026-08-13

Status: **DERIVED MIXING-CHANNEL BOUNDS / OPEN SPACETIME CLOSURE**.

This note bounds the two exact projective-dispersion production channels

\[
\dot{\mathcal J}=4\mathcal M_S+4\nu\mathcal M_\nu
\]

by previously tracked strain/alignment and palinstrophy/covariance-mismatch quantities.

No global regularity conclusion is claimed.

## 1. Setup

Let

\[
E=\|\omega\|_2^2,
\qquad
C=\frac1E\int\omega\otimes\omega dx,
\qquad
\mathcal J=1-\operatorname{tr}(C^2).
\]

Let

\[
A=\int(S\omega)\otimes\omega dx,
\qquad
B=A/E,
\qquad
q=\operatorname{tr}B,
\]

and

\[
H=\sum_k\int(\partial_k\omega)\otimes(\partial_k\omega)dx,
\qquad
P=\operatorname{tr}H,
\qquad
G=H/E,
\qquad
p=P/E.
\]

The exact channels are

\[
\mathcal M_S
=q\operatorname{tr}(C^2)-\operatorname{tr}(CB),
\]

\[
\mathcal M_\nu
=\operatorname{tr}(CG)-p\operatorname{tr}(C^2).
\]

## 2. Strain-mixing bound

Diagonalize the covariance matrix:

\[
C e_i=\mu_i e_i,
\qquad
\mu_i\ge0,
\qquad
\sum_i\mu_i=1.
\]

Set

\[
s=\operatorname{tr}(C^2)=1-\mathcal J,
\]

\[
\beta_i=e_i^TBe_i
=\frac1E\int(e_i\cdot S\omega)(e_i\cdot\omega)dx,
\]

and

\[
L_i^2
=\frac1E\int(e_i\cdot S\omega)^2dx.
\]

Then

\[
|\beta_i|\le\sqrt{\mu_i}L_i,
\qquad
\sum_iL_i^2
=\frac1E\int|S\omega|^2dx.
\]

Define the enstrophy-weighted RMS strain exposure

\[
\boxed{
\mathcal L_S
=
\left(
\frac1E\int|S\omega|^2dx
\right)^{1/2}.
}
\]

Since

\[
\mathcal M_S
=\sum_i(s-\mu_i)\beta_i,
\]

Cauchy--Schwarz gives

\[
|\mathcal M_S|
\le
\left[
\sum_i\mu_i(s-\mu_i)^2
\right]^{1/2}
\mathcal L_S.
\]

The covariance factor is

\[
\sum_i\mu_i(s-\mu_i)^2
=\operatorname{tr}(C^3)-s^2.
\]

Because `0<=mu_i<=1`,

\[
\operatorname{tr}(C^3)\le\operatorname{tr}(C^2)=s,
\]

hence

\[
\operatorname{tr}(C^3)-s^2
\le s(1-s)
=\mathcal J(1-\mathcal J).
\]

Therefore

\[
\boxed{
|\mathcal M_S|
\le
\sqrt{\mathcal J(1-\mathcal J)}\,\mathcal L_S.
}
\]

This is axis-choice-free and vanishes at least like `sqrt(J)` as the covariance approaches a one-axis state.

## 3. What `L_S` contains

Where `omega!=0`, write

\[
\xi=\omega/|\omega|,
\qquad
\gamma=\xi^TS\xi.
\]

The orthogonal decomposition

\[
S\xi
=\gamma\xi+P_{\xi^\perp}S\xi
\]

gives

\[
\boxed{
\mathcal L_S^2
=
\frac1E\int|\omega|^2
\left[
\gamma^2+
|P_{\xi^\perp}S\xi|^2
\right]dx.
}
\]

Thus large strain-driven projective mixing requires an enstrophy-weighted combination of

1. large vorticity-magnitude stretching rate `gamma`, and/or
2. large pointwise vorticity-axis conversion `|P_{xi^perp} S xi|`.

In the strain eigenframe,

\[
|P_{\xi^\perp}S\xi|^2
=\sum_{i<j}a_i a_j(\lambda_i-\lambda_j)^2,
\qquad
a_i=(\xi\cdot e_i)^2.
\]

Hence the strain-mixing channel feeds directly into the already tracked magnitude-growth and strain-gap/alignment branches.

## 4. Viscous mixing = palinstrophy rate times covariance mismatch

If `P>0`, define the normalized gradient covariance

\[
\boxed{
C_\nabla=\frac HP.
}
\]

Then

\[
C_\nabla\succeq0,
\qquad
\operatorname{tr}C_\nabla=1,
\]

and

\[
G=\frac PE C_\nabla=pC_\nabla.
\]

Therefore

\[
\boxed{
\mathcal M_\nu
=p\left[
\operatorname{tr}(CC_\nabla)
-\operatorname{tr}(C^2)
\right].
}
\]

Define the covariance mismatch

\[
\boxed{
\Delta_\nu
=\|C_\nabla-C\|_F.
}
\]

Then

\[
\begin{aligned}
|\mathcal M_\nu|
&=p|\operatorname{tr}[C(C_\nabla-C)]|\\
&\le p\|C\|_F\Delta_\nu\\
&=p\sqrt{1-\mathcal J}\,\Delta_\nu.
\end{aligned}
\]

Thus

\[
\boxed{
|\mathcal M_\nu|
\le
\frac PE
\sqrt{1-\mathcal J}\,\Delta_\nu.
}
\]

If `P=0`, then `H=0` and `M_nu=0`; `C_nabla` is typed as undefined/inapplicable.

## 5. Physical interpretation of the viscous sign

The viscous term is not universally negative for the **normalized directional dispersion** `J`.

- If gradient energy is concentrated more strongly in the dominant vorticity direction than the vorticity covariance itself, viscosity preferentially removes that dominant component and can increase `J`.
- If gradient energy is concentrated in off-axis directions, viscosity preferentially removes the off-axis component and can decrease `J`.
- If

\[
C_\nabla=C,
\]

then

\[
\boxed{\mathcal M_\nu=0}
\]

exactly: viscosity changes total enstrophy but not the normalized directional covariance to first order.

## 6. Combined growth inequality

Using the exact budget,

\[
\dot{\mathcal J}=4\mathcal M_S+4\nu\mathcal M_\nu,
\]

we obtain

\[
\boxed{
\dot{\mathcal J}
\le
4\sqrt{1-\mathcal J}
\left[
\sqrt{\mathcal J}\,\mathcal L_S
+
\nu\frac PE\Delta_\nu
\right].
}
\]

Therefore growth or sustained regeneration of multi-axis vorticity dispersion requires at least one of two mechanisms:

\[
\boxed{
\textbf{S-branch:}
\quad
\sqrt{\mathcal J}\,\mathcal L_S
\text{ is large},
}
\]

or

\[
\boxed{
\textbf{V-branch:}
\quad
\nu(P/E)\Delta_\nu
\text{ is large}.
}
\]

This is the desired first mixing-channel closure dichotomy.

## 7. Strain-only regeneration cost when viscosity does not help

On any time interval on which

\[
\mathcal M_\nu\le0,
\]

one has

\[
\dot{\mathcal J}
\le
4\sqrt{\mathcal J(1-\mathcal J)}\,\mathcal L_S.
\]

Whenever `0<J<1`,

\[
\frac d{dt}\arcsin\sqrt{\mathcal J}
=
\frac{\dot{\mathcal J}}{2\sqrt{\mathcal J(1-\mathcal J)}}.
\]

Hence

\[
\boxed{
\frac d{dt}\arcsin\sqrt{\mathcal J}
\le2\mathcal L_S
\qquad
(\mathcal M_\nu\le0).
}
\]

So raising the projective dispersion from `J0` to `J1>J0` without positive viscous mixing requires the finite strain-exposure cost

\[
\boxed{
\int_s^t\mathcal L_S(\tau)d\tau
\ge
\frac12
\left[
\arcsin\sqrt{\mathcal J_1}
-
\arcsin\sqrt{\mathcal J_0}
\right].
}
\]

This is a regeneration-cost statement, not a contradiction, because no general finite bound for the required `L_S` time integral has been established.

## 8. Residual-class update

A hypothetical singular cascade that must retain large `E J` can no longer treat multi-axisity as a free geometric label.

It must repeatedly pay through at least one of:

1. **strain exposure:** magnitude stretching and/or strain-gap axis conversion;
2. **viscous covariance mismatch:** high palinstrophy-to-enstrophy ratio together with a mismatch between gradient and vorticity directional covariances.

These are already connected to the existing middle-eigenvalue, extensional-alignment, palinstrophy, segregation, and higher-derivative channels.

The next target is to determine whether the V-branch can be iterated into the higher-derivative covariance chain, while the S-branch is intersected with the existing strain/alignment regularity gates.

Status: **OPEN S/V BRANCH INTERSECTION**.
