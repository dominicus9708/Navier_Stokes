# M19-056 — Angular momentum sees the toroidal critical datum, but its leading R^3 balance is pure similarity transport and the first stress torque is absorbed at R order by the invertible r^-3 correction

**Date:** 2026-09-12  
**Status:** CALCULATION / R-CRITICAL TOROIDAL MOMENT TEST / ANGULAR-MOMENTUM FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-055 showed that the scalar finite-radius energy balance is tautological at leading order for the resonant critical tail

\[
U_0(r\omega,\theta)=r^{-1}A(q,\omega),
\qquad q=\log r-\theta/2.
\]

Because scalar energy does not distinguish the toroidal channel well, the next natural observable is localized angular momentum.  This module derives its exact similarity balance and checks whether the toroidal datum acquires a new leading constraint.

The answer is negative at the first two asymptotic orders.  The leading \(O(R^3)\) angular-momentum balance is exact similarity transport for arbitrary \(A\), while the first genuine stress torque is \(O(R)\), exactly the same order as the angular-momentum contribution of the freely solvable \(r^{-3}B\) correction from M19-035.

## 2. Similarity momentum equation in stress form

Use

\[
\partial_\theta U
+\frac12 U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
+\nabla P
=\nu\Delta U,
\qquad \nabla\cdot U=0.
\]

Define the symmetric Navier--Stokes stress

\[
\boxed{
T
:=
U\otimes U+PI-2\nu D(U),
\qquad
D(U):=\frac12(\nabla U+\nabla U^T).
}
\]

Since \(\nabla\cdot U=0\),

\[
\nabla\cdot T
=(U\cdot\nabla)U+\nabla P-\nu\Delta U.
\]

Thus

\[
\boxed{
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+\nabla\cdot T=0.
}
\]

## 3. Exact local angular-momentum equation

Set

\[
\ell:=y\times U.
\]

Because

\[
(y\cdot\nabla)(y\times U)
=
y\times U+y\times (y\cdot\nabla U),
\]

we have

\[
y\times\left[
\frac12U+\frac12(y\cdot\nabla)U
\right]
=\frac12(y\cdot\nabla)\ell.
\]

Also, since \(T\) is symmetric,

\[
\boxed{
y\times(\nabla\cdot T)
=\nabla\cdot\mathcal T,
}
\]

where the torque-flux tensor is defined componentwise by

\[
\mathcal T_{kj}
:=\varepsilon_{k\alpha\beta}y_\alpha T_{\beta j}.
\]

The possible algebraic torque term vanishes exactly because

\[
\varepsilon_{k\alpha\beta}T_{\beta\alpha}=0.
\]

Therefore

\[
\partial_\theta\ell
+\frac12(y\cdot\nabla)\ell
+\nabla\cdot\mathcal T=0.
\]

Using

\[
\frac12(y\cdot\nabla)\ell
=
\frac12\nabla\cdot(y\otimes\ell)
-\frac32\ell,
\]

we obtain

\[
\boxed{
\partial_\theta\ell
-\frac32\ell
+\nabla\cdot
\left(
\frac12y\otimes\ell+\mathcal T
\right)=0.
}
\]

This is the exact similarity angular-momentum balance.

## 4. Annular balance

On the fixed-ratio annulus

\[
\mathcal A_R:=\{R<r<\lambda R\},
\qquad 1<\lambda<\infty,
\]

define

\[
L_R(\theta)
:=\int_{\mathcal A_R}\ell\,dy.
\]

Then

\[
\boxed{
L_R'
-\frac32L_R
+\mathcal J_{\lambda R}
-\mathcal J_R
=0,
}
\]

where the outward angular-momentum flux through \(S_r\) is

\[
\boxed{
\mathcal J_r
:=
\int_{S_r}
\left[
\frac12r\ell
+y\times(Tn)
\right]dS.
}
\]

On a sphere \(n=\omega\), the pressure torque vanishes identically:

\[
\boxed{
y\times(Pn)=0.}
\]

Thus the genuine stress torque sees only convective and viscous contributions.

## 5. Leading critical angular momentum

For

\[
U_0=r^{-1}A(q,\omega),
\]

we have

\[
\ell_0
=y\times U_0
=\omega\times A(q,\omega).
\]

Define

\[
\boxed{
N(q)
:=
\int_{S^2}\omega\times A(q,\omega)\,d\omega.
}
\]

Then

\[
\boxed{
L_R^{(0)}
=
\int_R^{\lambda R}r^2N(q)\,dr
=O(R^3).
}
\]

Unlike scalar energy, \(N(q)\) directly sees the toroidal part of \(A\).  In particular a purely toroidal datum need not have \(N=0\).

## 6. Exact leading similarity-transport cancellation

Since \(q=\log r-\theta/2\),

\[
(L_R^{(0)})'
=-\frac12\int_R^{\lambda R}r^2N_q(q)\,dr.
\]

But

\[
\frac d{dr}\bigl(r^3N(q)\bigr)
=r^2\bigl(3N+N_q\bigr),
\]

hence

\[
\int_R^{\lambda R}r^2N_q\,dr
=
\left[r^3N\right]_R^{\lambda R}
-3L_R^{(0)}.
\]

Therefore

\[
\boxed{
(L_R^{(0)})'
-\frac32L_R^{(0)}
=-\frac12
\left[r^3N(q)\right]_R^{\lambda R}.
}
\]

The similarity-drift contribution to the boundary flux is

\[
\mathcal J_r^{drift,(0)}
=
\int_{S_r}\frac12r\ell_0\,dS
=
\frac12r^3N(q).
\]

Thus

\[
\boxed{
(L_R^{(0)})'
-\frac32L_R^{(0)}
+\mathcal J_{\lambda R}^{drift,(0)}
-\mathcal J_R^{drift,(0)}
=0
}
\]

for every sufficiently regular scattering datum \(A\).

Hence angular momentum does detect the toroidal channel, but its leading \(O(R^3)\) law is still only the resonant similarity translation already encoded by \(q\).

## 7. Genuine stress torque is two powers lower

For the leading critical field,

\[
U_0=O(r^{-1}),
\qquad
D(U_0)=O(r^{-2}).
\]

The convective torque density on \(S_r\) is

\[
y\times\bigl[(U_0\otimes U_0)n\bigr]
=(U_0\cdot n)(y\times U_0)
=O(r^{-1}).
\]

After integration over area \(r^2\),

\[
\boxed{
\mathcal J_r^{conv,(0)}=O(r).
}
\]

Likewise

\[
y\times\bigl[-2\nu D(U_0)n\bigr]=O(r^{-1}),
\]

so

\[
\boxed{
\mathcal J_r^{visc,(0)}=O(r).
}
\]

As noted above, pressure gives zero spherical torque exactly.

Therefore every genuine Navier--Stokes stress torque first appears at

\[
\boxed{O(R),}
\]

two powers below the leading \(O(R^3)\) storage/drift balance.

## 8. The r^-3 correction contributes angular momentum at exactly O(R)

M19-035 gives

\[
U_1=r^{-3}B(q,\omega),
\qquad
\mathcal L_{sim}U_1=-r^{-3}B.
\]

Its angular-momentum density is

\[
\ell_1
=y\times U_1
=r^{-2}\omega\times B.
\]

Hence over \(\mathcal A_R\),

\[
\boxed{
L_R^{(1)}
=
\int_R^{\lambda R}r^2\,r^{-2}
\left(
\int_{S^2}\omega\times B\,d\omega
\right)dr
=O(R).
}
\]

The drift flux generated by \(U_1\) is also \(O(R)\).

Thus the first nontrivial stress-torque balance occurs at exactly the order at which the vector equation has the freely solvable \(r^{-3}B\) correction.

## 9. Consequence for toroidal rigidity

At order \(r^{-3}\), after solenoidal/pressure projection, M19-035 gives schematically

\[
-B+\mathbb P\mathcal F(A,\Pi)=0.
\]

The \(O(R)\) angular-momentum law is a moment of this same correction equation.  Therefore it does not independently force a closed condition on the leading toroidal scalar \(\psi(q,\omega)\).

In particular the M19-041 aperiodic toroidal leading anti-model is not excluded merely by imposing localized angular-momentum balance.

The valid result is

\[
\boxed{
\text{angular momentum sees the toroidal channel but supplies no new leading rigidity.}
}
\]

## 10. Stronger general lesson

M19-055 and M19-056 now show the same two-order structure for two different observables:

- scalar energy: leading storage/drift \(O(R)\), first NS flux/correction \(O(R^{-1})\);
- angular momentum: leading storage/drift \(O(R^3)\), first stress torque/correction \(O(R)\).

This suggests a general polynomial-moment firewall: multiplying momentum by a polynomial spatial weight raises both the leading transport storage and the first correction by the same number of powers of \(R\), leaving the two-order separation unchanged.

That statement should be proved rather than assumed.

## 11. Certified / not certified

### Certified

1. The exact local similarity angular-momentum balance.
2. The leading \(O(R^3)\) storage/drift cancellation for arbitrary regular \(A\).
3. Pressure torque vanishes exactly on centered spherical boundaries.
4. Convective and viscous torque first enter at \(O(R)\).
5. The \(r^{-3}B\) correction contributes angular-momentum storage/drift at the same \(O(R)\) order.
6. Therefore localized angular momentum does not supply an independent first solvability condition on the resonant toroidal datum.

### Not certified

1. Failure of every higher spherical/tensor moment.
2. Failure of nonlocal/global angular momentum pairings.
3. Global rigidity of recurrent weak-critical scattering.
4. Global 3D Navier--Stokes regularity.

## 12. Next calculation

M19-057 should prove or refute the suggested general polynomial momentum-moment rule.  If every fixed-degree local polynomial moment has leading resonant transport and its first genuine Navier--Stokes content at exactly the \(r^{-3}\) correction order, then an entire family of local moment shortcuts can be removed at once.

---

\[
\boxed{\text{M19-056 COMPLETE; LOCAL ANGULAR MOMENTUM DOES NOT CLOSE THE TOROIDAL RESONANT SCATTERING DATUM.}}
\]
