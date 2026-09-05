# DSD M17-182 — Zero-loop pressure variance has an exact signed transport law with crossing slip; it is not a new dissipative budget

Date: 2026-09-06  
Canonical ID: **M17-182**

Status: **PRESSURE-VARIANCE TRANSPORT AUDIT / FOR A REGULAR `kappa=0` LOOP IN THE REDUCED `(q,x_3)` PLANE, CHOOSE THE LOOP-TRACKING VELOCITY `W_Gamma=V_L-(h/|grad kappa|) n_kappa`, WHICH PRESERVES THE ZERO LEVEL WHILE RETAINING THE MATERIAL TANGENTIAL SPEED. THEN `D_Gamma H_V = Pi_V^prod+Pi_V^rel-(h/|grad kappa|) partial_n H_V`. THE COAREA MEASURE `dnu=ds/|grad kappa|` EVOLVES WITH `Lambda_Gamma=div W_Gamma=-div[(h/|grad kappa|)n_kappa]` BECAUSE `div V_L=kappa=0` ON THE LOOP. FOR `u=H_V-bar H_Gamma`, THE EXACT VARIANCE LAW IS `V_H'=2 int u[Pi_V^prod+Pi_V^rel-(h/|grad kappa|)partial_n H_V]dnu + int u^2 Lambda_Gamma dnu`. EVERY TERM IS SIGNED. AN EXPLICIT REDUCED ANNULAR MODEL CAN PRESERVE NONZERO PRESSURE VARIANCE BY PURE TANGENTIAL TRANSPORT EVEN WITH NONZERO MATERIAL CROSSING SLIP AND ZERO PRESSURE FORCING. THEREFORE M17-177'S SPATIAL HIGHER-JET OCCUPANCY DOES NOT BY ITSELF CREATE A NEW MONOTONE/SCALE-CRITICAL DISSIPATION BUDGET. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Moving regular zero loop

Let

\[
\Gamma(\theta)=\{(q,z):\kappa(q,z,\theta)=0\}
\]

be a smooth closed regular component with

\[
\boxed{g:=|\nabla\kappa|>0.}
\]

Define

\[
n:=\frac{\nabla\kappa}{g}
\]

and let the reduced material velocity be

\[
V_L=(\mathscr H,K).
\]

M17-013 gives

\[
\boxed{\nabla\cdot V_L=\kappa.}
\]

The material crossing rate is

\[
\boxed{
h=D_L\kappa
=\partial_\theta\kappa+V_L\cdot\nabla\kappa.
}
\]

---

## 2. Canonical zero-loop tracking velocity

Define

\[
\boxed{
c:=\frac{h}{g}}
\]

and

\[
\boxed{
W_\Gamma:=V_L-cn.
}
\]

Then

\[
\begin{aligned}
(\partial_\theta+W_\Gamma\cdot\nabla)\kappa
&=h-cg\\
&=0.
\end{aligned}
\]

Thus

\[
\boxed{D_\Gamma\kappa=0}
\]

for

\[
D_\Gamma:=\partial_\theta+W_\Gamma\cdot\nabla.
\]

This choice removes only the material **normal slip** through the zero level; it retains the material tangential component and therefore fixes the tangential gauge naturally.

---

## 3. Pressure-coordinate transport along the zero loop

On the vertical branch, M17-082 gives along the material reduced trajectory

\[
\boxed{
D_LH_V
=\Pi_V^{prod}+\Pi_V^{rel}.
}
\]

Since

\[
D_L=D_\Gamma+c\partial_n,
\]

we obtain the exact zero-loop transport

\[
\boxed{
D_\Gamma H_V
=\Pi_V^{prod}+\Pi_V^{rel}
-\frac{h}{g}\partial_nH_V.
}
\]

The extra term is the pressure gradient sampled by the material/zero-set crossing slip.

---

## 4. Exact evolution of the coarea measure

Use

\[
\boxed{d\nu:=\frac{ds}{g}.}
\]

For a plane curve transported by an ambient velocity `W_Gamma`, the line element obeys

\[
D_\Gamma ds
=(t\cdot\nabla W_\Gamma\,t)ds.
\]

Because `D_Gamma kappa=0`,

\[
D_\Gamma\nabla\kappa
=-(\nabla W_\Gamma)^T\nabla\kappa.
\]

Therefore

\[
D_\Gamma g
=-g\,n\cdot\nabla W_\Gamma\,n.
\]

Combining the two factors,

\[
\boxed{
D_\Gamma(d\nu)
=(\nabla\cdot W_\Gamma)d\nu.
}
\]

On the zero level,

\[
\nabla\cdot V_L=\kappa=0.
\]

Hence

\[
\boxed{
\Lambda_\Gamma
:=\nabla\cdot W_\Gamma
=-\nabla\cdot(cn)
=-\nabla\cdot\left(
\frac{h}{g}n
\right).
}
\]

Thus

\[
\boxed{D_\Gamma(d\nu)=\Lambda_\Gamma d\nu.}
\]

---

## 5. Exact pressure-variance transport

Define

\[
M_\Gamma:=\int_\Gamma d\nu,
\]

\[
\bar H_\Gamma
:=M_\Gamma^{-1}\int_\Gamma H_Vd\nu,
\]

and

\[
\boxed{
V_H
:=\int_\Gamma(H_V-\bar H_\Gamma)^2d\nu.
}
\]

Set

\[
u:=H_V-\bar H_\Gamma.
\]

Since

\[
\int_\Gamma u\,d\nu=0,
\]

the derivative of the moving mean cancels from the variance derivative.

Using Sections 3--4,

\[
\boxed{
\begin{aligned}
V_H'
={}&2\int_\Gamma
u\left[
\Pi_V^{prod}+\Pi_V^{rel}
-\frac{h}{g}\partial_nH_V
\right]d\nu\\
&+\int_\Gamma
u^2\Lambda_\Gamma d\nu.
\end{aligned}
}
\]

This is the canonical zero-loop pressure-variance transport law.

---

## 6. No sign-definite production term

The three mechanisms are

1. global pressure source production `Pi_V^prod`;
2. global relative transport `Pi_V^rel`;
3. zero-level crossing slip `-(h/g) partial_n H_V`;
4. coarea-measure deformation `Lambda_Gamma`.

All are signed.

There is no term of the form

\[
-cV_H,
\qquad c>0,
\]

or another monotone positive cost supplied by the identity itself.

At best, Cauchy--Schwarz yields an occupancy estimate for the combined signed forcing.
It does not convert recurrence of `V_H` into a dissipation contradiction.

---

## 7. Explicit reduced transport firewall

To show that this absence of coercivity is structural rather than a missing algebraic step, consider an annulus around the unit circle in the reduced plane.

Let

\[
\kappa(r)=r-1.
\]

Choose a reduced velocity

\[
V_L=f(r)e_r+\Omega r e_\theta
\]

with `f` solving locally

\[
f'(r)+\frac{f(r)}r=r-1
\]

and choose the integration constant so that

\[
f(1)=c_0\neq0.
\]

Then

\[
\boxed{\nabla\cdot V_L=\kappa}
\]

on the annulus, and on the zero loop

\[
\boxed{h=c_0.}
\]

The canonical zero-loop velocity is

\[
W_\Gamma=\Omega e_\theta
\]

on `r=1`.

Now take a pressure-coordinate test state

\[
H_V(\theta,\varphi)
=\cos(\varphi-\Omega\theta)
\]

independent of the normal coordinate near the loop.

Then

\[
D_\Gamma H_V=0,
\qquad
\partial_nH_V=0,
\qquad
\Lambda_\Gamma=0.
\]

Thus the variance is positive and constant while

\[
\Pi_V^{prod}+\Pi_V^{rel}=0.
\]

The material crossing slip `h=c_0` is nonzero.

This reduced example is not a Navier--Stokes solution; it proves only that the zero-loop variance transport identity itself contains no hidden positive cost.

---

## 8. Consequence for M17-176--177

Even if one supplies the missing M5-to-nodal localization assumption and obtains

\[
\overline{V_H}>0,
\]

M17-177's derivative occupancy

\[
\overline{\|\partial_sH_V\|_{L^2(d\nu)}^2}>0
\]

does not automatically imply positive time-integrated pressure production or dissipation.

A recurrent profile may transport its spatial variance around the loop through signed relative transport and crossing geometry.

Therefore the pressure-variance route reaches the known signed pressure-transport firewall unless an additional PDE estimate controls

\[
\Pi_V^{rel},
\quad
\frac{h}{g}\partial_nH_V,
\quad
\Lambda_\Gamma
\]

by a finite nonrecyclable budget.

---

## 9. DSD audit

### Audit A — differentiating a fixed loop
Rejected. The `kappa=0` loop moves and is not material.

### Audit B — ignoring crossing slip
Rejected. `h/g` is exactly the material/zero-level normal slip.

### Audit C — treating coarea measure as invariant
Rejected. Its deformation is `Lambda_Gamma`.

### Audit D — calling positive spatial variance a dissipation cost
Rejected by the exact transport law and reduced firewall model.

### Audit E — proof status
The temporal pressure-variance route is structurally noncoercive without a new estimate.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
