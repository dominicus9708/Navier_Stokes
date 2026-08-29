# DSD M5-226 — Stationary Critical-Tail Dilation-Pohozaev and Torque-Flux Firewall

Date: 2026-08-30

Parent: `DSD_M5_223_STATIONARY_CRITICAL_TAIL_LOG_RADIUS_ENERGY_AND_STRESS_FLUX_AUDIT_2026-08-30.md`

Status: **EXACT STRESS-MOMENT IDENTITIES / THE SYMMETRIC STATIONARY MOMENTUM STRESS GENERATES CONSTANT FORCE AND TORQUE CHARGES AND A DILATION CURRENT WHOSE LOG-RADIUS COEFFICIENT SATISFIES A FIRST-ORDER FORCED ODE / THE SOURCE `|T|^2+3P` HAS NO SIGN, SO BOUNDED PERIODIC OR APERIODIC RECURRENT LOG PROFILES ARE COMPATIBLE WITH THE POHOZAEV LAW / NO SCALE-MELLIN MONOTONICITY CONTROLLING THE POSITIVE HOMOGENEITY-DEFECT RESIDUE IS OBTAINED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Symmetric stationary momentum stress

For the stationary tail

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=0,
\qquad
\nabla\cdot T=0,
\]

define

\[
\boxed{
\mathbb S
:=
-\nu(\nabla T+\nabla T^T)
+T\otimes T
+PI.
}
\]

Since

\[
\nabla\cdot(\nabla T+\nabla T^T)
=\Delta T
\]

for divergence-free `T`, and

\[
\nabla\cdot(T\otimes T)
=(T\cdot\nabla)T,
\]

one has

\[
\boxed{\nabla\cdot\mathbb S=0.}
\]

The tensor is symmetric.

---

## 2. Constant force charge

Define

\[
\boxed{
b(r):=\int_{|x|=r}\mathbb S n\,dS.}
\]

By the divergence theorem,

\[
\boxed{b(r)=b}
\]

is independent of `r`.

This is the standard force/stress charge that labels the Landau leading profile in the small exterior theory.

For a critical tail `mathbb S=O(r^-2)`, the charge is scale invariant.

---

## 3. Constant torque charge

Because `mathbb S` is symmetric, angular momentum has another divergence-free current.

For each fixed vector `a`, consider

\[
K_a(x)
:=
(a\times x)\cdot\mathbb S.
\]

Equivalently use the vector torque flux

\[
\boxed{
\tau(r)
:=
\int_{|x|=r}x\times(\mathbb S n)\,dS.
}
\]

The antisymmetric derivative of `x` contracts with the symmetric stress and vanishes, while `div mathbb S=0`.

Hence

\[
\boxed{
\tau(r)=\tau
}
\]

is independent of `r`.

For a `1/r` critical field, `x times mathbb S` scales like `r^-1`; after integration over `S_r`, the raw torque scales like `r` unless cancellation occurs. Exact constancy therefore imposes nontrivial angular cancellation on the critical profile, but it remains only a finite-dimensional charge constraint.

---

## 4. Dilation current

Contract the stress with the dilation vector field `x`.

Define

\[
\boxed{
J_D
:=
\mathbb S x.
}
\]

Because `mathbb S` is symmetric, the choice of left/right contraction is immaterial.

Then

\[
\begin{aligned}
\nabla\cdot J_D
&=\partial_j(S_{ji}x_i)\\
&=(\partial_jS_{ji})x_i+S_{ji}\delta_{ji}\\
&=\operatorname{tr}\mathbb S.
\end{aligned}
\]

The viscous part is trace free because `div T=0`, so

\[
\boxed{
\operatorname{tr}\mathbb S
=|T|^2+3P.
}
\]

Therefore

\[
\boxed{
\nabla\cdot(\mathbb Sx)
=|T|^2+3P.
}
\]

This is the stationary dilation/Pohozaev-type identity.

---

## 5. Radial dilation flux law

Define

\[
\boxed{
D(r)
:=
\int_{|x|=r}
(\mathbb Sx)\cdot n\,dS
=
\int_{|x|=r}
x\cdot\mathbb S n\,dS.
}
\]

Then

\[
\boxed{
D(R)-D(r)
=
\int_{r<|x|<R}
(|T|^2+3P)dx.
}
\]

Differentiating,

\[
\boxed{
D'(r)
=
\int_{|x|=r}(|T|^2+3P)dS.
}
\]

There is no definite sign because of the pressure term.

---

## 6. Critical log-radius form

Write

\[
T=r^{-1}\Phi(y,\theta),
\qquad
P=r^{-2}\Pi(y,\theta),
\qquad y=\log r.
\]

Since `mathbb S=r^-2 Sigma_cyl`,

\[
D(r)
\]

has critical size `O(r)`.

Define

\[
\boxed{D(r)=r\,d(y).}
\]

Also define

\[
\boxed{
c_D(y)
:=
\int_{S^2}
(|\Phi(y,\theta)|^2+3\Pi(y,\theta))d\theta.
}
\]

Then

\[
D'(r)=d(y)+d'(y)
\]

while the sphere source is exactly `c_D(y)`.

Hence the log-radius Pohozaev law is

\[
\boxed{
d'(y)+d(y)=c_D(y).}
\]

---

## 7. Bounded recurrent source gives bounded recurrent dilation current

For any bounded complete source `c_D`, the unique solution bounded toward the appropriate direction can be written as an exponential convolution.

For example, imposing boundedness as `y->-infinity` gives

\[
\boxed{
d(y)
=
\int_{-\infty}^{y}
e^{-(y-z)}c_D(z)dz.
}
\]

Thus if `c_D` is periodic, almost-periodic, or belongs to a compact recurrent translation hull, the same is true of `d`.

A simple model

\[
c_D(y)=c_0+c_1\cos y
\]

gives

\[
d(y)
=c_0+\frac{c_1}{2}(\cos y+\sin y).
\]

Therefore

\[
\boxed{
\text{dilation/Pohozaev identity}
\not\Rightarrow
\text{constant log profile}.
}
\]

---

## 8. Why pressure prevents a sign argument

The source is

\[
c_D(y)
=
\int_{S^2}|\Phi|^2d\theta
+3\int_{S^2}\Pi d\theta.
\]

Although the first term is positive, the spherical pressure mean is not sign controlled by the stationary equations.

The pressure Poisson equation contains

\[
-\Delta P
=\partial_iT_j\partial_jT_i,
\]

whose source is also indefinite.

No derived identity supplies

\[
\int_{S^2}3\Pi
\ge -c\int_{S^2}|\Phi|^2
\]

with a coercive constant strong enough to make `c_D` one-signed on the arbitrary-amplitude branch.

Thus a Pohozaev monotonicity based on `D` is not available.

---

## 9. Relation to the homogeneity-defect residue

M5-224 gives

\[
\underline{\mathscr R}_H
=
\liminf_{\varepsilon\downarrow0}
\varepsilon
\int|T+x\cdot\nabla T|^3|x|^{-\varepsilon}dx
>0.
\]

The dilation identity instead controls only the scalar angular moment

\[
|T|^2+3P.
\]

There is no algebraic inequality connecting

\[
|T+x\cdot\nabla T|^3
\]

from below to a one-signed part of `|T|^2+3P`.

Therefore the new positive scale-phase residue is **not** priced by the elementary dilation current.

---

## 10. Force and torque charges remain finite-dimensional

The exact invariants

\[
b\in\mathbb R^3,
\qquad
\tau\in\mathbb R^3
\]

constrain only six scalar degrees of freedom.

The recurrent log-profile `Phi(y,theta)` is infinite dimensional.

Without a large-data rigidity theorem, constant force/torque cannot determine all higher spherical/logarithmic modes.

Consequently

\[
\boxed{
(b,\tau)\text{ fixed}
\not\Rightarrow
\partial_y\Phi=0.
}
\]

---

## 11. DSD verdict

### PROVED

- constant force charge;
- constant torque charge;
- exact dilation/Pohozaev identity;
- critical log-radius ODE
  \[
  d'+d=c_D.
  \]

### FIREWALL

The following route does not close the arbitrary-amplitude stationary branch:

\[
\boxed{
\text{force/torque conservation}
+
\text{Pohozaev identity}
\Longrightarrow
\text{homogeneity}.
}
\]

The pressure source has no sign and the first-order log ODE supports nonconstant recurrent solutions.

---

## 12. Updated stationary frontier

After M5-223, M5-224, and M5-226, any remaining large stationary critical tail must satisfy simultaneously

\[
\boxed{
\begin{cases}
F_T=0,\\
|T|\lesssim A_*/r,\quad A_*>\varepsilon_{KS},\\
\underline{\mathscr R}_H>0,\\
F_E(r)=r^{-1}f_E(\log r)\text{ monotone physically},\\
f_E'-f_E=-\nu A_D,\\
b\text{ constant},\\
\tau\text{ constant},\\
d'+d=c_D,\\
\text{compact minimal log-translation hull}.
\end{cases}}
\]

No elementary first-moment stress identity currently forces this class to collapse.

The next stationary closure would require a genuinely stronger large-data theorem or an identity controlling higher angular/log-radial modes.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]