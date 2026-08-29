# DSD M5-230 — Scale-Invariant `rW` Relative Energy and Negative Critical Balance

Date: 2026-08-30

Parent: `DSD_M5_228_SAME_POINT_FORCE_DILATE_DIFFERENCE_RELATIVE_STATIONARY_ENERGY_GATE_2026-08-30.md`

Status: **POSITIVE LARGE-DATA REDUCTION / MULTIPLYING THE SAME-POINT-FORCE RELATIVE STATIONARY EQUATION BY `r W_h` PRODUCES A LOG-RADIUS TRANSLATION-INVARIANT IDENTITY / AFTER LONG LOG-AVERAGING, THE VISCOUS PART IS THE NONNEGATIVE CYLINDER FORM `nu<|partial_y Psi_h|^2+|grad_S Psi_h|^2>` / THE M5-219 FINITE-DILATE SEPARATION PLUS SOLENOIDALITY FORCES THIS FORM TO HAVE A STRICT POSITIVE LOWER DENSITY / THEREFORE EVERY LARGE NONHOMOGENEOUS STATIONARY SURVIVOR MUST CARRY A STRICTLY NEGATIVE MEAN CRITICAL NONVISCOUS BALANCE TO CANCEL VISCOSITY / THIS IS A NECESSARY LARGE-DATA INSTABILITY CERTIFICATE, NOT YET A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Same-force relative equation

Fix the M5-219 no-short-return dilation shift

\[
h_*>0.
\]

Let

\[
U:=D_{h_*}T,
\qquad
V:=T,
\qquad
W:=U-V,
\qquad
q:=P_U-P_V.
\]

M5-227 gives the same point force for `U` and `V`, so M5-228 gives

\[
\boxed{
-\nu\Delta W
+(U\cdot\nabla)W
+(W\cdot\nabla)V
+\nabla q
=0,
\qquad
\nabla\cdot W=0.
}
\]

All equations are distributionally unforced after subtraction.

---

## 2. Use the scale-invariant multiplier `rW`

Let

\[
r=|x|.
\]

On a finite annulus

\[
A_{R_1,R_2}:=\{R_1<r<R_2\},
\]

pair the relative equation with

\[
\boxed{rW.}
\]

This multiplier is distinguished because each bulk term becomes scale invariant for a critical `1/r` field.

---

## 3. Diffusion term

Integration by parts gives

\[
\begin{aligned}
\int_A(-\Delta W)\cdot(rW)
&=
\int_A r|\nabla W|^2
+\frac12\int_A\nabla r\cdot\nabla|W|^2
+\text{radial boundary}\\
&=
\int_A
\left(
r|\nabla W|^2
-\frac{|W|^2}{r}
\right)dx
+\text{radial boundary},
\end{aligned}
\]

because in three dimensions

\[
\boxed{\Delta r=\frac2r.}
\]

Therefore the viscous bulk term is

\[
\boxed{
\nu\int_A
\left(
r|\nabla W|^2
-\frac{|W|^2}{r}
\right)dx.
}
\]

---

## 4. Transport, strain, and pressure bulk terms

Since `div U=0`,

\[
\begin{aligned}
\int_A
(U\cdot\nabla W)\cdot(rW)
&=
\frac12\int_A rU\cdot\nabla|W|^2\\
&=
-\frac12\int_A|W|^2U\cdot\nabla r
+\text{radial boundary}.
\end{aligned}
\]

Thus its bulk part is

\[
\boxed{
-\frac12\int_A|W|^2U_r\,dx.
}
\]

The cross term is

\[
\boxed{
\int_A rW^TS_VW\,dx,
}
\]

where `S_V` is the symmetric strain of `V`.

For pressure,

\[
\begin{aligned}
\int_A rW\cdot\nabla q
&=
-\int_Aq\,\nabla\cdot(rW)dx
+\text{radial boundary}\\
&=
-\int_AqW_rdx
+\text{radial boundary}.
\end{aligned}
\]

Thus the pressure bulk part is

\[
\boxed{-\int_AqW_rdx.}
\]

---

## 5. Exact finite-annulus weighted identity

Collecting the terms,

\[
\boxed{
\begin{aligned}
&\nu\int_A
\left(
r|\nabla W|^2-\frac{|W|^2}{r}
\right)dx\\
&\quad+
\int_A
\left[
rW^TS_VW
-\frac12|W|^2U_r
-qW_r
\right]dx
=
\mathcal J(R_1)-\mathcal J(R_2),
\end{aligned}}
\]

where `mathcal J(R)` is the complete radial boundary current produced by diffusion, transport, and pressure.

For critical fields every term in `mathcal J(R)` is dimensionless/bounded in log radius.

---

## 6. Log-cylinder representation

Write

\[
V=r^{-1}\Phi(y,\theta),
\]

\[
U=r^{-1}\Phi_h(y,\theta),
\qquad
\Phi_h(y,\theta)=\Phi(y-h_*/2,\theta),
\]

and

\[
\boxed{
W=r^{-1}\Psi(y,\theta),
\qquad
\Psi:=\Phi_h-\Phi.
}
\]

Also write

\[
q=r^{-2}\pi(y,\theta).
\]

Then the viscous integrand becomes exactly

\[
\left(
r|\nabla W|^2-rac{|W|^2}{r}
\right)dx
=
\left[
|\Psi_y|^2
-2\Psi\cdot\Psi_y
+|\nabla_{S^2}\Psi|^2
\right]dy\,d\theta,
\]

with the standard vector-spherical derivative understood componentwise in a fixed Cartesian frame.

The remaining bulk terms are also translation-invariant functions of

\[
(\Phi,\Phi_h,\Psi,\pi)
\]

on the log cylinder.

---

## 7. Long log-average removes the exact derivative

Integrate over

\[
-L<y<L
\]

and divide by `2L`.

The cross term is

\[
-2\Psi\cdot\Psi_y
=-\partial_y|\Psi|^2.
\]

The compact tail hull gives a uniform bound on `Psi`, so

\[
\frac1{2L}
\int_{-L}^{L}
\partial_y|\Psi|^2dy
\to0.
\]

The radial boundary current likewise contributes only

\[
\frac{\mathcal J(e^{-L})-\mathcal J(e^L)}{2L}
\to0
\]

along the bounded recurrent hull.

Therefore every invariant/long-time log mean satisfies

\[
\boxed{
\nu\left\langle
\int_{S^2}
\left(
|\Psi_y|^2+|\nabla_{S^2}\Psi|^2
\right)d\theta
\right\rangle
+
\langle\mathcal N_{crit}\rangle
=0,
}
\]

where

\[
\boxed{
\mathcal N_{crit}(y)
:=
\int_{S^2}
\left[
\Psi^T\mathcal S_\Phi\Psi
-\frac12|\Psi|^2(\Phi_h\cdot\theta)
-\pi(\Psi\cdot\theta)
\right]d\theta.
}
\]

Here `mathcal S_Phi` is the scale-normalized strain tensor of `V`.

---

## 8. Solenoidal cylinder coercivity on a fixed cell

The diffusion form

\[
\int_C
\left(
|\Psi_y|^2+|\nabla_{S^2}\Psi|^2
\right)
\]

has constants as its ordinary scalar/vector kernel.

But a nonzero constant Cartesian vector `c` would correspond to

\[
W(x)=\frac c{|x|},
\]

which is not divergence free:

\[
\nabla\cdot\left(\frac c r\right)
=-\frac{c\cdot\theta}{r^2}\ne0.
\]

Therefore the intersection of the constant kernel with the exact solenoidal critical cylinder constraint is `{0}`.

On every fixed compact log cell `C=J times S2`, a contradiction/Rellich argument yields a geometric constant

\[
\boxed{c_{sol}(J)>0}
\]

such that every critical profile difference satisfying the divergence constraint obeys

\[
\boxed{
\int_C
\left(
|\Psi_y|^2+|\nabla_{S^2}\Psi|^2
\right)
\ge
c_{sol}
\int_C|\Psi|^2.
}
\]

No boundary condition in `y` is needed because the only zero-gradient mode is excluded by solenoidality.

---

## 9. M5-219 separation forces positive viscous scale-action

M5-219 gives, on one of finitely many fixed cells at every tail time and on one selected cell with positive logarithmic density,

\[
\boxed{
\|\Psi\|_{L^3(C)}
\ge c_*>0.
}
\]

The compact tail hull also gives a uniform `L-infinity` bound

\[
\|\Psi\|_{L^\infty(C)}
\le M_*.
\]

Hence

\[
\int_C|\Psi|^2
\ge
\frac1{M_*}
\int_C|\Psi|^3
\ge
\frac{c_*^3}{M_*}.
\]

The solenoidal coercivity then gives

\[
\boxed{
\int_C
\left(
|\Psi_y|^2+|\nabla_{S^2}\Psi|^2
\right)
\ge
c_D^*>0
}
\]

on a positive-density family of translated cells.

Consequently the long log mean obeys

\[
\boxed{
\left\langle
\int_{S^2}
(|\Psi_y|^2+|\nabla_{S^2}\Psi|^2)d\theta
\right\rangle
\ge d_D^*>0.
}
\]

---

## 10. Strict negative critical nonviscous balance

Insert the positive viscous lower mean into the exact averaged identity.

Then

\[
\boxed{
\langle\mathcal N_{crit}\rangle
\le
-\nu d_D^*<0.
}
\]

Thus every nonhomogeneous large stationary minimal tail must create a **strictly negative mean critical balance** from the combined

- background strain;
- radial transport;
- pressure coupling

in the finite-dilate zero-force mode.

This is a necessary condition, not an optional mechanism.

---

## 11. Interpretation

The large stationary branch can no longer be described merely as a failure of smallness.

It must have a genuine critical direction in which the nonviscous part of the scale-weighted relative form overcomes a strictly positive viscous scale-phase cost.

Schematically,

\[
\boxed{
\text{nonhomogeneous fixed-force scaling orbit}
\Longrightarrow
\text{strict negative critical relative balance}.
}
\]

This is the precise large-data certificate suggested by M5-229.

---

## 12. What this does not prove

A negative direction of a non-self-adjoint/pressure-coupled critical form is not by itself a contradiction.

Stationary Navier--Stokes at large Reynolds amplitude may support indefinite quadratic forms.

The identity also does not prove dynamical linear instability of the time-dependent Navier--Stokes flow; the multiplier and topology are scale-weighted and stationary.

Therefore the implications

\[
\langle\mathcal N_{crit}\rangle<0
\Rightarrow
\text{bifurcation}
\]

or

\[
\langle\mathcal N_{crit}\rangle<0
\Rightarrow
\text{singular instability}
\]

are not asserted.

---

## 13. Updated stationary endpoint

The surviving large stationary point-force branch must now satisfy

\[
\boxed{
\begin{cases}
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=b\delta_0,\\
\underline{\mathscr R}_H>0,\\
\mathcal H_T\text{ is a nonzero fixed-force linearized zero mode},\\
\tau=0,\\
\langle\mathcal N_{crit}\rangle\le-\nu d_D^*<0,\\
\text{compact minimal dilation hull}.
\end{cases}}
\]

This is much more restrictive than generic arbitrary-amplitude stationary nonuniqueness.

---

## 14. Next target

The negative balance has three components:

\[
\Psi^T\mathcal S_\Phi\Psi,
\qquad
-\frac12|\Psi|^2\Phi_{h,r},
\qquad
-\pi\Psi_r.
\]

The next audit should separate them using

- zero spherical flux;
- fixed point-force/stress charge;
- pressure Poisson structure;
- the existing positive-middle-strain/Betchov ledgers.

If radial transport and pressure have zero or bounded mean contribution, the entire negative payment would be forced into the strain quadratic form, providing a direct bridge to the projective/positive-middle-strain machinery.

No such cancellation is assumed yet.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]