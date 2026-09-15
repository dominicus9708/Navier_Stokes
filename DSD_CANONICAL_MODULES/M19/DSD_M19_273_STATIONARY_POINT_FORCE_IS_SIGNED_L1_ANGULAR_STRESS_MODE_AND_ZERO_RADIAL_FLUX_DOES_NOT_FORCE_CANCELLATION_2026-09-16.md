# DSD M19-273 — Stationary point force is a signed l=1 angular stress mode; zero radial flux does not force cancellation

Date: 2026-09-16  
Canonical ID: **M19-273**  
Status: **ACTIVE ANGULAR DEFECT AUDIT / EXACT STRESS-FLUX FORMULA / MASS-FLUX CANCELLATION CERTIFIED / POINT-FORCE CANCELLATION NOT IMPLIED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-272 reduces the stationary terminal-defect problem to cancellation/rigidity at the critical weak-L3 endpoint.

Let

\[
v(x)=r^{-1}A(q,\omega),
\qquad
p(x)=r^{-2}P(q,\omega),
\qquad
q=\log r,
\]

with

\[
A=A_r e_r+A_T,
\qquad
A_T\cdot e_r=0.
\]

On the stationary branch

\[
C=0,
\]

so the sphere momentum-stress flux is independent of \(q\):

\[
\boxed{
\kappa
=
\int_{S^2}\mathbb T_A(q,\omega)e_r\,d\omega.
}
\]

The goal is to compute the angular content of this vector exactly.

---

## 2. Divergence-free constraint

For a degree-minus-one log profile,

\[
\boxed{
(\partial_q+1)A_r
+\operatorname{div}_{S^2}A_T
=0.
}
\]

Integrating over \(S^2\) gives

\[
\frac d{dq}
\int_{S^2}A_r\,d\omega
+
\int_{S^2}A_r\,d\omega
=0.
\]

Define

\[
m_0(q):=\int_{S^2}A_r\,d\omega.
\]

Then

\[
\boxed{m_0'+m_0=0.}
\]

Hence

\[
m_0(q)=ce^{-q}.
\]

A two-sided bounded recurrent log profile cannot contain the exponentially growing/decaying mode \(ce^{-q}\) unless \(c=0\). Therefore

\[
\boxed{
\int_{S^2}A_r(q,\omega)d\omega=0
\quad\text{for every }q.
}
\]

Thus the stationary recurrent critical tail has zero net scalar radial mass flux.

---

## 3. Exact symmetric-gradient traction

For Cartesian-valued \(A\),

\[
(\nabla v)e_r
=r^{-2}(\partial_qA-A).
\]

Also

\[
(\nabla v)^Te_r
=
 r^{-2}
\left[
(\partial_qA_r-A_r)e_r
+\nabla_{S^2}A_r
-A_T
\right].
\]

The nonlinear and pressure tractions are

\[
(v\otimes v)e_r
=r^{-2}A_rA,
\]

and

\[
pe_r=r^{-2}Pe_r.
\]

Therefore the scale-normalized stress traction

\[
K_A:=r^2\mathbb T e_r
\]

splits into radial and tangential parts

\[
\boxed{
(K_A)_r
=
2(\partial_q-1)A_r
-A_r^2
-P,
}
\]

\[
\boxed{
(K_A)_T
=
\partial_qA_T
-(2+A_r)A_T
+\nabla_{S^2}A_r.
}
\]

Hence

\[
\boxed{
\kappa
=
\int_{S^2}
\left[
(K_A)_re_r+(K_A)_T
\right]d\omega.
}
\]

---

## 4. A useful vector moment identity

Define

\[
M(q)
:=
\int_{S^2}A_r e_r\,d\omega,
\]

and

\[
T(q)
:=
\int_{S^2}A_T\,d\omega.
\]

Multiply the divergence-free constraint by \(e_r=\omega\) and integrate over the sphere.

Using

\[
\int_{S^2}
 e_r\operatorname{div}_{S^2}A_T\,d\omega
=
-\int_{S^2}A_T\,d\omega,
\]

one obtains

\[
\boxed{
M'+M-T=0,
}
\]

or

\[
\boxed{T=M'+M.}
\]

Let

\[
N(q):=
\int_{S^2}A\,d\omega.
\]

Then

\[
\boxed{
N=M+T=M'+2M.
}
\]

These are exact low-angular-mode constraints inherited only from incompressibility.

---

## 5. Integrated viscous traction simplifies

The embedded-sphere integration identity

\[
\boxed{
\int_{S^2}\nabla_{S^2}f\,d\omega
=
2\int_{S^2}f e_r\,d\omega
}
\]

holds for smooth scalar \(f\).

Using this and the relation \(M'+M-T=0\), the sphere integral of the transpose-gradient traction vanishes:

\[
\int_{S^2}
\left[
(\partial_qA_r-A_r)e_r
+\nabla_{S^2}A_r
-A_T
\right]d\omega
=0.
\]

Therefore the total point-force coefficient reduces to

\[
\boxed{
\kappa
=
N'(q)-N(q)
-
\int_{S^2}A_rA\,d\omega
-
\int_{S^2}P e_r\,d\omega.
}
\]

This identity is valid at every \(q\) on the stationary branch, and its left side is independent of \(q\).

---

## 6. Invariant-mean force formula

On the recurrent compact log factor, boundedness gives

\[
\langle N'\rangle_q=0.
\]

Hence

\[
\boxed{
\kappa
=
-
\left\langle N\right\rangle_q
-
\left\langle
\int_{S^2}
\left(A_rA+Pe_r\right)d\omega
\right\rangle_q.
}
\]

Thus force cancellation is the signed vector condition

\[
\boxed{
\left\langle N\right\rangle_q
+
\left\langle
\int_{S^2}(A_rA+Pe_r)d\omega
\right\rangle_q
=0.
}
\]

It is not a consequence of any scalar positive density currently available.

---

## 7. Why zero radial flux is insufficient

We have already proved

\[
\int_{S^2}A_r\,d\omega=0.
\]

But \(\kappa\) depends on

\[
\int A\,d\omega,
\qquad
\int A_rA\,d\omega,
\qquad
\int Pe_r\,d\omega,
\]

which are vector first-angular-moment quantities.

Therefore

\[
\boxed{
\int A_r=0
\not\Rightarrow
\kappa=0.
}
\]

The scalar no-source/no-sink condition removes only the \(l=0\) radial mass channel. The point force lives in a signed vector \(l=1\)-type stress projection.

---

## 8. Positive hard-tail densities do not determine the force sign

The hard ergodic branch has

\[
\left\langle\int|A|^3\right\rangle=c_3>0,
\]

and

\[
\left\langle\int|B_A|^2\right\rangle=c_\omega>0.
\]

These are scalar nonnegative observables.

They contain no sign information sufficient to determine

\[
\left\langle N\right\rangle,
\quad
\left\langle\int A_rA\right\rangle,
\quad
\left\langle\int Pe_r\right\rangle.
\]

Hence

\[
\boxed{
 c_3>0,\ c_\omega>0
\not\Rightarrow
\kappa\neq0,
}
\]

and equally

\[
\boxed{
 c_3>0,\ c_\omega>0
\not\Rightarrow
\kappa=0.
}
\]

The point-force problem is intrinsically signed/angular.

---

## 9. Example of a sufficient cancellation symmetry

If a stationary profile happened to satisfy the antipodal odd symmetry

\[
A(q,-\omega)=-A(q,\omega),
\]

with the corresponding even pressure symmetry

\[
P(q,-\omega)=P(q,\omega),
\]

then

\[
N=0,
\]

while \(A_r\) is even and the vectors

\[
A_rA,
\qquad
Pe_r
\]

are odd on the sphere. Therefore

\[
\boxed{\kappa=0.}
\]

No such antipodal symmetry is presently inherited by the hard branch; this is only an explicit demonstration that force cancellation is angular, not amplitude-based.

---

## 10. Literature-scope firewall on stationary log profiles

Classical classification shows that continuously homogeneous smooth degree-minus-one stationary profiles are Landau solutions.

The larger class

\[
A=A(q,\omega)
\]

with bounded recurrent/log-periodic dependence in \(q\) is substantially broader.

Existing work on stationary discretely self-similar/log-periodic profiles does not provide a general classification sufficient to collapse every such recurrent profile to Landau. In particular, restricted bifurcation analyses around Landau profiles do not constitute a global rigidity theorem for the present class.

Therefore the implication

\[
\boxed{
C=0
\Longrightarrow
\partial_qA=0
}
\]

must remain unproved unless a new theorem is supplied.

---

## 11. Refined stationary endpoint

The stationary hard branch now decomposes cleanly into

\[
\boxed{
S_{force}:
\kappa\neq0,
}
\]

or

\[
\boxed{
S_{zero-force}:
\kappa=0,\quad A\neq0,\quad A\in L^{3,\infty}_{crit},\quad C=0.
}
\]

The first branch is an explicit terminal point-defect branch.

The second is an endpoint stationary rigidity/removability problem.

No scalar unsigned payer distinguishes them.

---

## 12. Updated closure targets

The stationary route is now reduced to two theorem-level targets:

### Target S1 — signed force cancellation/exclusion

Prove

\[
\boxed{
\kappa=0
}
\]

from a genuine signed angular identity inherited from the original solution, or prove that \(\kappa\neq0\) is incompatible with a stronger terminal defect-measure condition.

### Target S2 — zero-force endpoint rigidity

Assuming

\[
\kappa=0,
\]

prove that a bounded recurrent critical stationary log profile must improve to

\[
L^3
\quad\text{or}\quad
o(1/r),
\]

or vanish directly.

This is the exact stationary analogue of M19-271's demand for a non-coboundary object on the dynamic branch.

---

## 13. Immediate next target

Do not seek another scalar positive tail norm.

The highest-value next tests are:

1. inspect whether the original finite-energy/first-hitting centering or zero-total-vorticity identities impose any signed \(l=1\) moment on \(A,P\);
2. audit whether \(\kappa=0\) plus recurrence allows a stationary log-profile energy/pressure identity that forces strong-L3 improvement;
3. otherwise return to the dynamic branch and search for a genuine non-coboundary finite-lag defect/index quantity.

Global 3D Navier--Stokes regularity remains unproved.
