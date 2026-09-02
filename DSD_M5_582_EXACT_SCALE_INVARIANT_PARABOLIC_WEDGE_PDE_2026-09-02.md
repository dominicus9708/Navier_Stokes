# DSD M5-582 — Exact Scale-Invariant Parabolic-Wedge PDE

Date: 2026-09-02

Status: **THE TERMINAL JET RESUMS INTO AN EXACT COORDINATE FORMULATION OF THE ANCIENT FLOW ON A SCALE-INVARIANT HALF-CYLINDER. THE TERMINAL TRACE IS THE DEGENERATE z=0 BOUNDARY. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Exact wedge coordinates

For every physical point with

\[
s<0,
\qquad x\neq0,
\]

define

\[
\boxed{
q:=\log r,
\qquad
z:=\frac{-s}{r^2}>0,
\qquad
\omega:=x/r.
}
\]

Conversely,

\[
\boxed{
r=e^q,
\qquad
s=-ze^{2q},
\qquad
x=e^q\omega.
}
\]

Thus \((z,q,\omega)\in(0,\infty)\times\mathbb R\times S^2\) parametrizes the punctured ancient spacetime exactly.

Define

\[
\boxed{
F(z,q,\omega):=r\,u(x,s),
}
\]

and

\[
\boxed{
H(z,q,\omega):=r^2p(x,s).
}
\]

Then

\[
\boxed{
u(x,s)=r^{-1}F(z,q,\omega),
\qquad
p(x,s)=r^{-2}H(z,q,\omega).
}
\]

This is an exact coordinate transform; convergence of the formal terminal series is not required to define \(F\) for \(z>0\).

---

## 2. Terminal boundary and jet

At fixed \(x\neq0\),

\[
s\uparrow0
\Longleftrightarrow
z\downarrow0.
\]

Hence the terminal critical trace is simply the boundary value

\[
\boxed{F(0,q,\omega)=A(q,\omega).}
\]

If \(F\) is smooth/analytic enough in \(z\) at the boundary, then

\[
F(z,q,\omega)
=
\sum_{n\ge0}z^nA_n(q,\omega),
\]

with

\[
A_0=A,
\qquad
A_1=C,
\]

and M5-581 is the Taylor recursion of the exact wedge equation below.

---

## 3. Scale invariance

Under Navier-Stokes scaling

\[
u_\lambda(x,s)
=\lambda u(\lambda x,\lambda^2s),
\]

we have

\[
z\mapsto
\frac{-\lambda^2s}{|\lambda x|^2}=z,
\]

while

\[
q\mapsto q+\log\lambda.
\]

Therefore

\[
\boxed{z\text{ is exactly scale invariant}}
\]

and the scaling action becomes pure translation in \(q\):

\[
\boxed{F_\lambda(z,q,\omega)=F(z,q+\log\lambda,\omega).}
\]

This is the full-spacetime extension of the terminal log-radius process from M5-571/M5-580.

---

## 4. Natural radial differential operator

At fixed physical time \(s\), varying \(r\) changes both \(q\) and \(z\):

\[
r\partial_rq=1,
\qquad
r\partial_rz=-2z.
\]

Hence define

\[
\boxed{
\mathfrak D
:=
\partial_q-2z\partial_z.
}
\]

For a component \(f(z,q,\omega)\),

\[
\boxed{
r\partial_r f=\mathfrak Df.}
\]

---

## 5. Time derivative

At fixed \(x\),

\[
\partial_sz=-r^{-2}.
\]

Therefore

\[
\boxed{
\partial_su
=-r^{-3}\partial_zF.
}
\]

This immediately recovers

\[
\partial_su(x,0^-)
=-r^{-3}C
\]

when \(C=\partial_zF|_{z=0}\).

---

## 6. Laplacian

For a scalar/cartesian component \(f\), the ordinary homogeneous formula remains valid with \(\partial_q\) replaced by \(\mathfrak D\):

\[
\boxed{
\Delta\big(r^{-m}f\big)
=
r^{-m-2}
\left[
(\mathfrak D-m)(\mathfrak D-m+1)
+\Delta_{S^2}
\right]f.
}
\]

For velocity homogeneity \(m=1\), define

\[
\boxed{
\mathfrak L_1
:=(\mathfrak D-1)\mathfrak D+\Delta_{S^2}.
}
\]

Since

\[
\mathfrak D^2
=
\partial_q^2
-4z\partial_{qz}
+4z^2\partial_{zz}
+4z\partial_z,
\]

we have

\[
\boxed{
(\mathfrak D-1)\mathfrak D
=
\partial_q^2-\partial_q
-4z\partial_{qz}
+4z^2\partial_{zz}
+6z\partial_z.
}
\]

The coefficient of \(\partial_{zz}\) is \(4z^2\), so the second normal derivative degenerates quadratically at the terminal boundary \(z=0\).

---

## 7. Pressure and nonlinear operators

Define

\[
\boxed{
\mathfrak G_2H
:=
e_r(\mathfrak D-2)H+\nabla_{S^2}H,
}
\]

so that

\[
\nabla p
=r^{-3}\mathfrak G_2H.
\]

Define geometrically

\[
\boxed{
\mathfrak N(F,F)
:=
r^3
\big[(r^{-1}F)\cdot\nabla\big](r^{-1}F),
}
\]

which depends only on \(F\), \(\mathfrak D F\), and angular derivatives on \(S^2\).

---

## 8. Exact wedge Navier-Stokes PDE

Insert the transformed quantities into

\[
\partial_su+(u\cdot\nabla)u
=-\nabla p+\Delta u.
\]

After multiplying by \(r^3\),

\[
-\partial_zF+\mathfrak N(F,F)
=-\mathfrak G_2H+\mathfrak L_1F.
\]

Thus

\[
\boxed{
\partial_zF
=
-\mathfrak L_1F
+\mathfrak N(F,F)
+\mathfrak G_2H.
}
\]

Because \(\mathfrak L_1\) itself contains \(z\partial_z\) and \(z^2\partial_{zz}\), this is not an ordinary first-order evolution equation in \(z\). It is a degenerate mixed elliptic/parabolic equation on the half-cylinder.

---

## 9. Exact incompressibility constraint

For

\[
u=r^{-1}F,
\]

incompressibility becomes

\[
\boxed{
(\mathfrak D+1)F_r
+\operatorname{div}_{S^2}F_T
=0.
}
\]

At \(z=0\), this reduces to M5-569's terminal condition

\[
(\partial_q+1)A_r+\operatorname{div}_{S^2}A_T=0.
\]

---

## 10. Relation to similarity variables

Since

\[
y=x/\sqrt{-s},
\]

we have

\[
\boxed{z=|y|^{-2}.}
\]

Also

\[
q
=
\log r
=
\log|y|-\frac\theta2.
\]

Therefore

\[
\boxed{
U(y,\theta)
=
|y|^{-1}
F\!\left(|y|^{-2},\log|y|-\frac\theta2,\omega\right).
}
\]

The regions correspond as follows:

- \(z\downarrow0\): remote similarity tail / terminal physical trace;
- \(z=O(1)\): Type-I similarity core scale;
- \(z\to\infty\): deep interior \(|y|\to0\).

Thus the wedge profile joins the terminal tail and the recurrent similarity core in one object.

---

## 11. Type-I bound in wedge form

A Type-I velocity bound

\[
|u(x,s)|\lesssim(-s)^{-1/2}
\]

gives

\[
|F|=r|u|\lesssim\frac r{\sqrt{-s}}
=\boxed{z^{-1/2}}.
\]

Equivalently,

\[
\boxed{\sqrt z\,|F(z,q,\omega)|\lesssim1.}
\]

The terminal branch has the stronger boundary regularity

\[
F(z,q,\omega)\to A(q,\omega)
\]

as \(z\downarrow0\).

---

## 12. Structural significance

The old hard core was described by two apparently separate structures:

1. a recurrent Type-I similarity core;
2. a critical terminal \(1/r\) tail.

The exact wedge transform shows that they are sections of one scale-invariant field:

\[
\boxed{F(z,q,\omega).}
\]

Similarity recurrence/scaling acts only by translation in \(q\), while \(z\) labels the scale-invariant parabolic depth.

Therefore a compact two-sided similarity hull can be pushed to a stationary ergodic process

\[
q\mapsto F(z,q,\cdot)
\]

for every fixed \(z>0\), not only at the terminal boundary \(z=0\).

This opens a new route: derive balances in \(z\) after taking the invariant \(q\)-mean. All total \(q\)-derivatives then disappear, potentially reducing the full PDE to a one-dimensional scale-depth system.

Status: **THE FULL ANCIENT HARD CORE HAS BEEN REPARAMETRIZED AS AN EXACT SCALE-INVARIANT WEDGE PDE. THE NEXT HIGH-VALUE STEP IS ERGODIC q-AVERAGING OF THIS PDE/ITS ENERGY-VORTICITY IDENTITIES TO OBTAIN z-DEPENDENT BALANCE LAWS. GLOBAL REGULARITY REMAINS UNPROVED.**