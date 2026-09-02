# DSD M5-581 — Full Parabolic Terminal-Jet Recursion

Date: 2026-09-02

Status: **THE ENTIRE FAR-FIELD TERMINAL JET OBEYS AN EXACT TRIANGULAR RECURSION WITH A 1/(n+1) FACTOR. NONZERO FIRST RESIDUAL DOES NOT BY ITSELF FORCE FACTORIAL GROWTH. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. General terminal expansion

Write

\[
a=-s>0,
\qquad q=\log r.
\]

The natural parabolic terminal expansion is

\[
\boxed{
u(x,s)
=
\sum_{n=0}^{\infty}
a^n r^{-(2n+1)}A_n(q,\omega),
}
\]

and

\[
\boxed{
p(x,s)
=
\sum_{n=0}^{\infty}
a^n r^{-(2n+2)}P_n(q,\omega).
}
\]

The first coefficients are

\[
A_0=A,
\qquad
A_1=C.
\]

The expansion parameter is

\[
\boxed{z:=a/r^2=(-s)/r^2.}
\]

---

## 2. Homogeneous log-spherical Laplacian

For any scalar/cartesian component \(f(q,\omega)\) and exponent \(m\),

\[
\boxed{
\Delta\big(r^{-m}f\big)
=
r^{-m-2}\mathcal L_mf,
}
\]

where

\[
\boxed{
\mathcal L_m
:=(\partial_q-m)(\partial_q-m+1)+\Delta_{S^2}.
}
\]

For \(m=1\), this recovers M5-572:

\[
\mathcal L_1
=\partial_q(\partial_q-1)+\Delta_{S^2}.
\]

---

## 3. Pressure-gradient operator

For

\[
p_n=r^{-(2n+2)}P_n,
\]

we have

\[
\boxed{
\nabla p_n
=
r^{-(2n+3)}\mathcal G_{2n+2}P_n,
}
\]

with

\[
\boxed{
\mathcal G_mP
:=
e_r(\partial_q-m)P+\nabla_{S^2}P.
}
\]

---

## 4. Time derivative

Because

\[
\partial_sa^n=-na^{n-1},
\]

the coefficient at order

\[
a^nr^{-(2n+3)}
\]

coming from the time derivative is supplied by \(A_{n+1}\):

\[
\boxed{
\partial_s
\left(a^{n+1}r^{-(2n+3)}A_{n+1}\right)
=-(n+1)a^nr^{-(2n+3)}A_{n+1}.
}
\]

---

## 5. Nonlinear order matching

The interaction of

\[
a^ir^{-(2i+1)}A_i
\]

with the gradient of

\[
a^jr^{-(2j+1)}A_j
\]

has order

\[
a^{i+j}r^{-(2(i+j)+3)}.
\]

Therefore at jet order \(n\), all and only pairs

\[
i+j=n
\]

contribute.

Let

\[
\mathcal N_{i,j}(A_i,A_j)
\]

denote the corresponding log-spherical bilinear coefficient, including the radial homogeneity \(2j+1\) of the differentiated factor.

---

## 6. Exact triangular recursion

At coefficient

\[
a^nr^{-(2n+3)},
\]

the Navier-Stokes equation gives

\[
-(n+1)A_{n+1}
+
\sum_{i+j=n}\mathcal N_{i,j}(A_i,A_j)
=
-\mathcal G_{2n+2}P_n
+
\mathcal L_{2n+1}A_n.
\]

Hence

\[
\boxed{
(n+1)A_{n+1}
=
-\mathcal L_{2n+1}A_n
+
\sum_{i+j=n}\mathcal N_{i,j}(A_i,A_j)
+
\mathcal G_{2n+2}P_n.
}
\]

Equivalently,

\[
\boxed{
A_{n+1}
=
\frac1{n+1}
\left[
-\mathcal L_{2n+1}A_n
+
\sum_{i+j=n}\mathcal N_{i,j}(A_i,A_j)
+
\mathcal G_{2n+2}P_n
\right].
}
\]

For \(n=0\), this is exactly M5-572:

\[
A_1=C
=-\mathcal L_1A_0
+\mathcal N_{0,0}(A_0,A_0)
+\mathcal G_2P_0.
\]

---

## 7. Divergence constraint at every order

For

\[
r^{-(2n+1)}A_n,
\]

the divergence-free condition is

\[
\boxed{
(\partial_q+1-2n)(A_n)_r
+\operatorname{div}_{S^2}(A_n)_T
=0.
}
\]

Thus every coefficient lies in its own homogeneity-adapted solenoidal subspace.

Pressure \(P_n\) is fixed, up to the usual harmonic/gauge freedom, by imposing this constraint on the recursion.

---

## 8. Scaling covariance of every jet coefficient

Under

\[
u_\lambda(x,s)=\lambda u(\lambda x,\lambda^2s),
\]

each term transforms as

\[
\lambda
(\lambda^2a)^n
(\lambda r)^{-(2n+1)}
=
a^nr^{-(2n+1)}.
\]

Therefore there is no coefficient amplitude factor:

\[
\boxed{
(A_n)_\lambda(q,\omega)
=
A_n(q+\log\lambda,\omega)
\quad\text{for every }n.
}
\]

Hence every nonzero coefficient can in principle be promoted to the same stationary log-radius factor used for \(A\) and \(C\).

---

## 9. Anti-proof: no automatic factorial explosion

The first dynamic residual \(C=A_1\) has positive log-density on the J branch by M5-580.

A tempting route is to claim that each residual forces a still larger next jet coefficient, eventually causing factorial growth.

The exact recursion shows the opposite structural feature:

\[
\boxed{
A_{n+1}
\text{ carries an explicit factor }
\frac1{n+1}.
}
\]

This is compatible with ordinary time analyticity in the parameter \(a=-s\), at least away from the singular core.

Derivative operators \(\mathcal L_{2n+1}\) contain coefficients growing with \(n\), so no convergence theorem follows automatically; however, **nonzero \(C\) alone does not imply factorial divergence.**

Any growth argument must estimate the full competition between:

- the \(n\)-dependent homogeneous derivatives;
- the quadratic convolution over \(i+j=n\);
- the pressure solve;
- the divisor \(n+1\).

---

## 10. Natural resummation

The expansion suggests defining

\[
\boxed{
F(z,q,\omega)
:=
\sum_{n\ge0}z^nA_n(q,\omega),
}
\]

and

\[
\boxed{
H(z,q,\omega)
:=
\sum_{n\ge0}z^nP_n(q,\omega),
}
\]

so that

\[
\boxed{
u(x,s)=r^{-1}F((-s)/r^2,\log r,\omega),}
\]

\[
\boxed{
p(x,s)=r^{-2}H((-s)/r^2,\log r,\omega).}
\]

The infinite terminal jet is therefore more naturally viewed as one **parabolic wedge profile** \(F(z,q,\omega)\), with the terminal trace at

\[
z=0.
\]

The next target is to derive the exact Navier-Stokes PDE for \(F\) in \((z,q,\omega)\). That formulation may reveal a monotone/elliptic structure hidden by the coefficient recursion.

Status: **THE TERMINAL-JET HIERARCHY IS TRIANGULAR AND SCALE-COVARIANT, BUT IT DOES NOT AUTOMATICALLY BLOW UP. THE CORRECT NEXT OBJECT IS THE RESUMMED PARABOLIC WEDGE PROFILE F(z,q,omega). GLOBAL REGULARITY REMAINS UNPROVED.**