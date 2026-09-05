# DSD M17-175 — A uniformly nondegenerate `(kappa,F_3)` hodograph admits exact M5-type flux hysteresis; label-plane geometry alone cannot close Rank-1

Date: 2026-09-06  
Canonical ID: **M17-175**

Status: **ANTI-SHORTCUT COUNTERMODEL / A SMOOTH TWO-DIMENSIONAL REDUCED LABEL FLOW CAN SATISFY `div V_L=kappa`, HAVE A CONSTANT NONDEGENERATE SEMILINEAR HESSIAN/HODOGRAPH `det Hess F !=0`, CARRY A NONZERO CONSTANT MIXED COMPONENT `F_q3` AND THEREFORE NONZERO LOCAL OCTUPOLE, AND STILL REALIZE AN EXACT PERIODIC M5 HYSTERESIS CYCLE WITH ZERO BASE CROSSING CURRENT BUT STRICTLY NEGATIVE AMPLIFICATION-WEIGHTED CROSSING CURRENT. AN EXPLICIT MODEL USES A QUADRATIC `F` SO `(u,v)=(kappa,F_3)` IS A FIXED LINEAR HODOGRAPH, AND A POLAR FLOW WITH `r=1` PERIODIC, `u=cos theta`, `div V=u`; ALONG THE ORBIT `a=exp(sin theta)` MAKES THE DOWNWARD ZERO CROSSING FLUX-HEAVY AND THE UPWARD CROSSING FLUX-LIGHT. THIS IS NOT A NAVIER--STOKES SOLUTION; IT IS A FIREWALL SHOWING THAT M17-013/169/170/174 LABEL-PLANE KINEMATICS PLUS HODOGRAPH NONDEGENERACY DO NOT THEMSELVES CONTRADICT M5-685 HYSTERESIS. ANY CLOSURE MUST USE ADDITIONAL CE-H/NS PRESSURE, PALINSTROPHY, OR TRANSPORT STRUCTURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M17-174 splits the vertical regular branch into

\[
J_\Xi\neq0
\quad\text{or}\quad
J_\Xi=0,
\]

where

\[
J_\Xi
=\det\nabla^2_{(q,3)}F.
\]

It is tempting to hope that recurrent M5 hysteresis forces repeated hodograph degeneration.

M17-175 tests that implication at the level of the reduced semilinear label geometry.

The conclusion is negative.

---

## 2. Choose a constant nondegenerate semilinear Hessian

Let

\[
\boxed{
F(q,z)
=\frac12q^2+bqz+\frac12cz^2,
}
\]

where

\[
\boxed{b\neq0,\qquad d:=c-b^2\neq0.}
\]

Then

\[
\kappa=F_q=q+bz,
\]

and

\[
F_3=bq+cz.
\]

Define

\[
\boxed{
(u,v):=(\kappa,F_3).
}
\]

The hodograph matrix is constant:

\[
\boxed{
A:=\nabla^2F
=\begin{pmatrix}1&b\\b&c\end{pmatrix},
\qquad
\det A=d\neq0.
}
\]

Thus `(q,z)<->(u,v)` is a global linear diffeomorphism.

At a vertical crossing the mixed Hessian component is

\[
F_{q3}=b\neq0,
\]

so in the M17-169 normalization

\[
O_V=-\frac15|Q|_F^2b
\]

is nonzero if the external nodal factor `|Q|_F` is nonzero.

---

## 3. Construct a smooth flow with divergence exactly `u`

Work first in the hodograph `(u,v)` plane and use polar coordinates

\[
u=r\cos\vartheta,
\qquad
v=r\sin\vartheta.
\]

Define

\[
\boxed{
\dot r
=\frac{r^3-1}{3r}\cos\vartheta,
\qquad
\dot\vartheta=1.
}
\]

The polar velocity components are

\[
V_r=\frac{r^3-1}{3r}\cos\vartheta,
\qquad
V_\vartheta=r.
\]

The planar divergence is

\[
\operatorname{div}V
=\frac1r\partial_r(rV_r)
+\frac1r\partial_\vartheta V_\vartheta.
\]

Since

\[
rV_r=\frac{r^3-1}{3}\cos\vartheta,
\]

we get

\[
\frac1r\partial_r(rV_r)
=r\cos\vartheta=u,
\]

and

\[
\partial_\vartheta V_\vartheta=0.
\]

Therefore

\[
\boxed{\operatorname{div}_{(u,v)}V=u.}
\]

---

## 4. Pull back to the semilinear label plane

Because `(u,v)=A(q,z)` is linear and invertible, define

\[
\boxed{
V_L(q,z):=A^{-1}V(A(q,z)).
}
\]

The derivative matrices are conjugate:

\[
DV_L=A^{-1}(DV)A.
\]

Hence their traces are equal:

\[
\operatorname{div}_{(q,z)}V_L
=\operatorname{div}_{(u,v)}V.
\]

Thus

\[
\boxed{
\operatorname{div}_{(q,z)}V_L
=u
=\kappa.
}
\]

So the exact M17-013 area-divergence law is satisfied.

Write

\[
V_L=(\mathscr H,K).
\]

Then one may define

\[
G:=K-\frac12z.
\]

The identity

\[
\partial_q\mathscr H+\partial_zK=\kappa
\]

is precisely the M17-013 compatibility

\[
\mathscr H_q=\kappa-G_3-\frac12.
\]

Thus the reduced scalar/label kinematics are internally consistent.

---

## 5. Exact periodic zero-crossing orbit

At

\[
r=1,
\]

we have

\[
\dot r=0.
\]

Therefore `r=1` is an exact periodic orbit with

\[
\vartheta(\tau)=\tau+\vartheta_0.
\]

Along this orbit,

\[
\boxed{
\kappa=u=\cos\vartheta.
}
\]

The two zero crossings per period are:

1. `vartheta=pi/2`, with
   \[
   h=\dot\kappa=-1;
   \]
2. `vartheta=3pi/2`, with
   \[
   h=\dot\kappa=+1.
   \]

Thus the unweighted crossing rates cancel exactly.

---

## 6. Amplification factor and M5 hysteresis

The M17-013/M5 amplification obeys

\[
\dot a=\kappa a.
\]

Along the orbit,

\[
\frac{d}{d\vartheta}\log a
=\cos\vartheta.
\]

Therefore

\[
\boxed{
a(\vartheta)=a_*e^{\sin\vartheta}.}
\]

At the downward crossing `vartheta=pi/2`,

\[
\boxed{a_-=a_*e.}
\]

At the upward crossing `vartheta=3pi/2`,

\[
\boxed{a_+=a_*e^{-1}.}
\]

Hence the period-summed base current is

\[
(-1)+(1)=0,
\]

while the amplification-weighted current is

\[
\boxed{
(-1)a_*e+(1)a_*e^{-1}
=a_*(e^{-1}-e)<0.
}
\]

This is exactly the sign structure required by M5-685:

\[
\boxed{
\overline G_0(0)=0,
\qquad
\overline G_\Phi(0)<0.
}
\]

---

## 7. Hodograph never degenerates

Throughout the model,

\[
\boxed{
J_\Xi=d=c-b^2
}
\]

is constant and nonzero.

There is no repeated `J_Xi=0` turnover.

The local mixed component

\[
F_{q3}=b
\]

is also constant and nonzero.

Thus a nonzero local octupole and exact M5 hysteresis coexist with a uniformly nondegenerate hodograph.

---

## 8. Relation to the pressure-square identity

The constant Hessian gives

\[
F_{qq}=1,
\qquad
H_V=F_{33}=c,
\qquad
F_{q3}^2=b^2.
\]

Therefore

\[
\boxed{
F_{qq}H_V-F_{q3}^2
=c-b^2=d=J_\Xi.
}
\]

The M17-170/174 square architecture is satisfied identically.

There is no contradiction between the positive square term and periodic hysteresis at the reduced-label level.

---

## 9. What this model does NOT claim

This construction is **not** asserted to reconstruct a three-dimensional Navier--Stokes or CE-H solution.

It does not enforce all of:

- pressure Poisson architecture;
- vorticity reconstruction and Biot--Savart compatibility;
- global palinstrophy budgets;
- the M17-082 pressure transport law;
- the complete nodal geometry.

Its role is narrower:

\[
\boxed{
\text{it is a countermodel to any attempted proof using only the reduced label-plane identities.}
}
\]

---

## 10. DSD audit consequence

The following shortcut is rejected:

\[
\boxed{
\text{M5 hysteresis}
+\text{uniform hodograph nondegeneracy}
\Longrightarrow\bot.
}
\]

It is false at the level of the exact reduced kinematics.

Therefore a successful Rank-1 closure must use genuinely additional information such as

1. the global pressure transport `Pi_V^{prod}+Pi_V^{rel}`;
2. the positive-palinstrophy representation of M17-167;
3. a spatial/temporal packing cost for the weighted palinstrophy tail of M17-168;
4. constitutive information from the full CE-H multiplier equation.

---

## 11. Updated Rank-1 branch split

The uniform hodograph branch is a genuine survivor of the current label geometry:

\[
\boxed{
G_{hod}^{uniform}
\not\Longrightarrow
G_{hod}^{turnover}.
}
\]

Thus the next highest-value route returns to the **PDE production/transport channels**, not further hodograph topology.

The most concrete target is to combine the positive-palinstrophy representation

\[
\Pi_{V,\kappa}^{prod}
=\langle|\nabla W|^2,K_{333}\rangle
\]

with the exact global recurrence

\[
\langle\Pi_V^{prod}+\Pi_V^{rel}\rangle=0
\]

and determine what the non-kappa production plus relative-transport channels must pay when the M5 crossing population has a persistent localized production bias.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
