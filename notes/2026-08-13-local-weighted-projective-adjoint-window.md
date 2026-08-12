# Local weighted projective defect and the adjoint observation window

Date: 2026-08-13

Status: **DERIVED LOCAL PROJECTIVE IDENTITY + ADJOINT-WINDOW CANCELLATION / OPEN NONLINEAR LOCAL CLOSURE**.

This note localizes the energy-weighted projective covariance inequality without discarding transport/cutoff terms. The correct window error turns out to be multiplicative in the projective defect, and it vanishes completely for an adjoint drift--diffusion observation kernel.

This is the most direct bridge so far between the original moving-sphere DSD picture and the projective covariance route.

## 1. Positive time-dependent observation weight

Let

\[
\phi(x,t)>0
\]

be smooth with sufficient decay. Define

\[
\boxed{
\Psi_\phi
=
\partial_t\phi
+u\cdot\nabla\phi
+\nu\Delta\phi.
}
\]

The strict positivity assumption is convenient for relative window estimates. Compactly supported cutoffs can still be used in the exact identity, but the relative bound `|Psi|<=Lambda phi` may fail near a zero boundary.

## 2. Local weighted covariance tensors

Define

\[
E_\phi
=\int\phi|\omega|^2dx,
\]

\[
N_\phi
=\int\phi\omega\otimes\omega dx,
\]

and, when `E_phi>0`,

\[
C_\phi=N_\phi/E_\phi,
\qquad
J_\phi=1-\operatorname{tr}(C_\phi^2),
\]

\[
\boxed{
D_\phi=E_\phi J_\phi.
}
\]

Also define

\[
A_\phi
=\int\phi(S\omega)\otimes\omega dx,
\]

\[
H_\phi
=\sum_m\int\phi(\partial_m\omega)\otimes(\partial_m\omega)dx,
\]

and the window tensor

\[
\boxed{
R_\phi
=\int\Psi_\phi\,\omega\otimes\omega dx.
}
\]

Let

\[
Q_\phi=\operatorname{tr}A_\phi,
\qquad
P_\phi=\operatorname{tr}H_\phi,
\qquad
R_{0,\phi}=\operatorname{tr}R_\phi.
\]

## 3. Exact weighted second-moment evolution

Multiply the vorticity equation

\[
\partial_t\omega+(u\cdot\nabla)\omega
=S\omega+\nu\Delta\omega
\]

by the tensor weight `phi omega`.

The divergence-free transport term transfers onto the weight. For viscosity,

\[
\int\phi
[(\Delta\omega)\otimes\omega
+\omega\otimes(\Delta\omega)]
=-2H_\phi
+\int(\Delta\phi)\omega\otimes\omega.
\]

Therefore

\[
\boxed{
\dot N_\phi
=A_\phi+A_\phi^T
-2\nu H_\phi
+R_\phi.
}
\]

Taking the trace,

\[
\boxed{
\dot E_\phi
=2Q_\phi-2\nu P_\phi+R_{0,\phi}.
}
\]

## 4. Exact local energy-weighted projective identity

When `P_phi>0`, define

\[
C_{1,\phi}=H_\phi/P_\phi,
\]

\[
J_{1,\phi}=1-\operatorname{tr}(C_{1,\phi}^2),
\]

and

\[
\Delta_\phi
=\|C_{1,\phi}-C_\phi\|_F.
\]

The same normalized covariance algebra as in the global case gives

\[
\boxed{
\begin{aligned}
\dot D_\phi
&+2\nu P_\phi
(J_{1,\phi}+\Delta_\phi^2)\\
&=2Q_\phi J_\phi
+4E_\phi M_{N,\phi}
+W_\phi,
\end{aligned}
}
\]

where

\[
M_{N,\phi}
=q_\phi(1-J_\phi)
-\operatorname{tr}(C_\phi B_\phi),
\]

\[
B_\phi=A_\phi/E_\phi,
\qquad
q_\phi=Q_\phi/E_\phi,
\]

and the complete observation-window term is

\[
\boxed{
W_\phi
=R_{0,\phi}(2-J_\phi)
-2\operatorname{tr}(C_\phi R_\phi).
}
\]

If `P_phi=0`, the viscous covariance is typed as undefined/inapplicable and the entire gradient tensor vanishes; the identity is understood by dropping that term.

## 5. Nonlinear source bound

Define the weighted forcing norm

\[
\boxed{
F_\phi
=\left(
\int\phi|S\omega|^2dx
\right)^{1/2}.
}
\]

The same covariance-eigenbasis Cauchy argument gives

\[
\boxed{
2Q_\phi J_\phi
+4E_\phi M_{N,\phi}
\le
2\sqrt5\sqrt{D_\phi}\,F_\phi.
}
\]

Thus all new localization difficulty is isolated in `W_phi`.

## 6. The window error is multiplicative in the projective defect

Assume

\[
\boxed{
|\Psi_\phi(x,t)|
\le
\Lambda(t)\phi(x,t)
}
\]

pointwise.

Diagonalize

\[
C_\phi e_i=\mu_i e_i.
\]

Set

\[
\beta_i
=\frac1{E_\phi}
e_i^TR_\phi e_i
=\frac1{E_\phi}
\int\Psi_\phi(e_i\cdot\omega)^2dx.
\]

Then

\[
|\beta_i|
\le\Lambda\mu_i.
\]

Moreover

\[
\frac{W_\phi}{E_\phi}
=\sum_i
(2-J_\phi-2\mu_i)\beta_i.
\]

For every trace-one positive covariance,

\[
2-J-2\mu_i
=1+\operatorname{tr}(C^2)-2\mu_i
\ge0.
\]

Also

\[
\sum_i
\mu_i(2-J-2\mu_i)
=J.
\]

Therefore

\[
\boxed{
|W_\phi|
\le
\Lambda E_\phi J_\phi
=\Lambda D_\phi.
}
\]

This is substantially better typed than a generic local enstrophy-window error: a nearly one-axis local covariance also suppresses the observation-window mixing error.

## 7. Local projective inequality

Combining the source and window bounds,

\[
\boxed{
\dot D_\phi
+2\nu P_\phi
(J_{1,\phi}+\Delta_\phi^2)
\le
2\sqrt5\sqrt{D_\phi}\,F_\phi
+\Lambda D_\phi.
}
\]

Using the finite-dimensional covariance coercivity

\[
J_{1,\phi}+\Delta_\phi^2
\ge\frac38J_\phi^2,
\]

we obtain

\[
\boxed{
\dot D_\phi
+\frac{3\nu}{4}P_\phi J_\phi^2
\le
2\sqrt5\sqrt{D_\phi}\,F_\phi
+\Lambda D_\phi.
}
\]

This is a fully localized counterpart of the global projective dissipation inequality.

## 8. Adjoint drift--diffusion observation window

Choose `phi` to solve

\[
\boxed{
\partial_t\phi
+u\cdot\nabla\phi
+\nu\Delta\phi
=0.
}
\]

Then

\[
\Psi_\phi=0,
\qquad
R_\phi=0,
\qquad
W_\phi=0.
\]

Hence the exact local projective inequality becomes

\[
\boxed{
\dot D_\phi
+2\nu P_\phi
(J_{1,\phi}+\Delta_\phi^2)
\le
2\sqrt5\sqrt{D_\phi}\,F_\phi.
}
\]

or, with covariance coercivity,

\[
\boxed{
\dot D_\phi
+\frac{3\nu}{4}P_\phi J_\phi^2
\le
2\sqrt5\sqrt{D_\phi}\,F_\phi.
}
\]

The window itself has absorbed transport and scalar diffusion exactly.

## 9. Terminal-value interpretation

The adjoint equation is naturally prescribed with a terminal observation profile at time `T`:

\[
\phi(x,T)=\phi_T(x)>0.
\]

Writing reverse time `tau=T-t` converts it to a forward parabolic drift--diffusion equation, so this is the standard adjoint orientation rather than a claim of forward anti-diffusion.

The mass of the window is preserved:

\[
\frac d{dt}\int\phi dx=0
\]

under sufficient decay and `div u=0`.

Thus one may choose a positive terminal kernel concentrated near a candidate singular point/scale and propagate the observation weight backward along the actual velocity field.

## 10. DSD interpretation

The original moving-sphere picture used a translating observation region. The adjoint window is a stronger typed version:

- center translation is no longer the only motion;
- the observation weight is advected by the 3D velocity field;
- scalar viscous spreading is included in the observation kernel itself;
- projective covariance is aggregated inside this dynamically compatible window.

No new physical force or propagation law is added to Navier--Stokes.

## 11. Remaining obstacle

The window/cutoff problem is no longer the principal obstruction if an adjoint weight is used.

The remaining local source is

\[
\sqrt{D_\phi}\,F_\phi
=
\sqrt{E_\phi J_\phi}
\left(
\int\phi|S\omega|^2
\right)^{1/2}.
\]

The active question is whether the dyadic pairwise projective depletion and occupancy/sparseness channels can bound this local nonlinear source strongly enough to integrate the resulting inequality on every candidate singular observation window.

Status: **OPEN LOCAL NONLINEAR PROJECTIVE SOURCE CLOSURE**.
