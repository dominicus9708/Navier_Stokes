# M19-055 — Finite-radius similarity energy balance is tautological at leading order and the first nontrivial flux lives in the invertible r^-3 correction sector

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL BOUNDARY-HISTORY AUDIT / LEADING ENERGY-COMPATIBILITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

After M19-054, the dominant analytic frontier is the global realizability/rigidity of the recurrent weak-critical scattering datum

\[
A(q,\omega),
\qquad
q=\log r-\theta/2.
\]

One natural candidate is a finite-radius boundary-history compatibility law obtained from the similarity local-energy identity.

The present module checks that route at the first two asymptotic orders.

The leading \(O(R)\) energy balance is an exact transport identity for arbitrary \(A\). The first nontrivial \(O(R^{-1})\) balance occurs at the same order as the invertible \(r^{-3}B\) correction of M19-035 and therefore is not an independent leading solvability condition on \(A\).

## 2. Similarity equation and local energy identity

Use the M5-567 / M19-035 sign convention

\[
\boxed{
\partial_\theta U
+\frac12 U
+\frac12 y\cdot\nabla U
+(U\cdot\nabla)U
+\nabla P
=\nu\Delta U,
\qquad
\nabla\cdot U=0.
}
\]

Let

\[
e:=\frac12|U|^2.
\]

Dotting the equation with \(U\) gives

\[
\partial_\theta e
+e
+\frac12y\cdot\nabla e
+\nabla\cdot((e+P)U)
=\nu\Delta e-\nu|\nabla U|^2.
\]

Since

\[
\frac12y\cdot\nabla e
=\frac12\nabla\cdot(ye)-\frac32e,
\]

we obtain

\[
\boxed{
\partial_\theta e
-\frac12e
+\nabla\cdot
\left(
\frac12ye+(e+P)U-\nu\nabla e
\right)
=-\nu|\nabla U|^2.
}
\]

## 3. Work on a remote fixed-ratio annulus

To avoid importing the asymptotic tail through the non-asymptotic core, fix

\[
1<\lambda<\infty
\]

and use

\[
\mathcal A_R:=\{R<r<\lambda R\}.
\]

Define

\[
E_R(\theta)
:=
\int_{\mathcal A_R}e(y,\theta)\,dy,
\]

\[
D_R(\theta)
:=
\int_{\mathcal A_R}|\nabla U|^2dy.
\]

Integrating the local-energy identity gives

\[
\boxed{
E_R'-\frac12E_R
+\mathcal F_{\lambda R}-\mathcal F_R
=-\nu D_R,
}
\]

where the outward radial flux through \(S_r\) is

\[
\boxed{
\mathcal F_r
:=
\int_{S_r}
\left[
\frac12 r e
+(e+P)U\cdot n
-\nu\partial_re
\right]dS.
}
\]

The inner boundary enters with the opposite orientation, hence the difference \(\mathcal F_{\lambda R}-\mathcal F_R\).

## 4. Leading critical field

Take

\[
\boxed{
U_0(r\omega,\theta)
=r^{-1}A(q,\omega),
\qquad
q=\log r-\theta/2.
}
\]

Set

\[
\boxed{
M(q):=\int_{S^2}|A(q,\omega)|^2d\omega.
}
\]

Then

\[
e_0=\frac12r^{-2}|A|^2,
\]

so the annular energy is

\[
\boxed{
E_R^{(0)}
=\frac12\int_R^{\lambda R}M\left(\log r-\frac\theta2\right)dr.
}
\]

Thus

\[
E_R^{(0)}=O(R).
\]

## 5. Exact leading cancellation for arbitrary A

Differentiate in \(\theta\):

\[
\partial_\theta M(q)
=-\frac12M_q(q).
\]

Hence

\[
(E_R^{(0)})'
=-\frac14
\int_R^{\lambda R}M_q(q)dr.
\]

Since

\[
\frac d{dr}\bigl(rM(q)\bigr)
=M(q)+M_q(q),
\]

we have

\[
\int_R^{\lambda R}M_q(q)dr
=
\left[rM(q)\right]_R^{\lambda R}
-
\int_R^{\lambda R}M(q)dr.
\]

Because

\[
E_R^{(0)}=\frac12\int_R^{\lambda R}M(q)dr,
\]

it follows that

\[
\boxed{
(E_R^{(0)})'
-\frac12E_R^{(0)}
=-\frac14
\left[rM(q)\right]_R^{\lambda R}.
}
\]

On the other hand the similarity-drift part of the boundary flux is

\[
\begin{aligned}
\mathcal F_r^{drift,(0)}
&=
\int_{S_r}\frac12re_0\,dS\\
&=
\frac14rM(q).
\end{aligned}
\]

Therefore

\[
\boxed{
(E_R^{(0)})'
-\frac12E_R^{(0)}
+\mathcal F_{\lambda R}^{drift,(0)}
-\mathcal F_R^{drift,(0)}
=0
}
\]

for **every sufficiently regular scattering datum \(A\)**.

This is exactly the energy-level manifestation of the M19-035 resonance

\[
\mathcal L_{sim}[r^{-1}A]=0.
\]

## 6. All genuinely Navier--Stokes terms are two orders smaller

For the critical field,

\[
U_0=O(r^{-1}),
\qquad
\nabla U_0=O(r^{-2}),
\qquad
P_0=r^{-2}\Pi(q,\omega).
\]

Therefore on \(S_r\),

\[
(e_0+P_0)U_0\cdot n
=O(r^{-3}),
\]

and after multiplying by area \(r^2\),

\[
\boxed{
\int_{S_r}(e_0+P_0)U_0\cdot n\,dS
=O(r^{-1}).
}
\]

Likewise

\[
\partial_re_0=O(r^{-3}),
\]

so

\[
\boxed{
\nu\int_{S_r}\partial_re_0\,dS
=O(r^{-1}).
}
\]

Finally

\[
|\nabla U_0|^2=O(r^{-4}),
\]

and hence over a fixed-ratio annulus

\[
\boxed{
D_R^{(0)}=O(R^{-1}).
}
\]

Thus the entire nonlinear/pressure/viscous content first enters the annular energy balance at order

\[
\boxed{R^{-1}}.
\]

## 7. The r^-3 velocity correction contributes at exactly the same order

M19-035 gives the first correction

\[
\boxed{
U_1=r^{-3}B(q,\omega)
}
\]

with

\[
\mathcal L_{sim}U_1=-r^{-3}B.
\]

The energy cross term is

\[
U_0\cdot U_1
=r^{-4}A\cdot B.
\]

After integrating over \(\mathcal A_R\),

\[
\int_R^{\lambda R}r^2r^{-4}dr
=O(R^{-1}).
\]

Hence

\[
\boxed{
E_R^{(01)}=O(R^{-1}).
}
\]

The drift boundary flux of this cross term is also \(O(R^{-1})\).

Therefore the first nontrivial local-energy compatibility occurs at exactly the order at which the vector Navier--Stokes equation has the freely solvable correction \(B\).

## 8. Why the O(R^-1) energy equation is not an independent solvability condition

At order \(r^{-3}\), M19-035 gives schematically

\[
\boxed{
-B
+\mathbb P\mathcal F(A,\Pi)=0
}
\]

after solenoidal/pressure projection, where \(\mathbb P\) is the Leray projection.

The scalar local-energy identity is obtained by dotting the same vector equation with the velocity and integrating by parts.

Consequently, once the order-\(r^{-3}\) vector correction equation is solved for \(B\) and the corresponding pressure correction, its order-\(R^{-1}\) energy balance is a consequence of that equation rather than an additional Fredholm condition on \(A\).

Thus the finite-radius energy identity does **not** remove the M19-035 invertibility firewall.

The valid conclusion is

\[
\boxed{
\text{leading boundary energy compatibility is tautological,}
}
\]

and

\[
\boxed{
\text{first nontrivial boundary-energy order belongs to the invertible }r^{-3}\text{ correction sector.}
}
\]

## 9. Boundary-history interpretation

M5-567 identifies

\[
q=\log R_{spec}-\theta_{cross}/2
\]

at a fixed spectator boundary.

Hence \(A(q,\omega)\) records the long similarity-time history at that boundary.

M19-055 shows that the ordinary finite-radius local-energy law does not constrain that history at leading order beyond the transport already built into

\[
q=\log r-\theta/2.
\]

The boundary can carry arbitrary leading recurrent translation history without violating the leading similarity energy bookkeeping.

Any genuine rigidity must use information finer than ordinary scalar energy balance.

## 10. What this rules out

The following proposed shortcut is invalid:

\[
\boxed{
\text{finite-radius local energy balance}
\Longrightarrow
\text{closed scalar evolution/monotonicity law for }A.
}
\]

At leading order it is an identity.
At first subleading order it mixes with \(B\), pressure, nonlinear stress, viscosity, and dissipation at exactly the invertible correction scale.

This is consistent with:

- M19-018: stress is outward-integrable/subleading;
- M19-035: no first \(r^{-3}\) solvability obstruction;
- M19-042: ordinary physical energy-flux/dissipation cost is integrable near \(T_*\).

## 11. Remaining promising boundary observables

A useful boundary law must avoid being merely a scalar consequence of the same local vector equation at an invertible correction order.

The next candidates are therefore more structured quantities, such as:

1. momentum or angular-momentum flux after subtracting transport storage;
2. tensor stress moments projected onto nontrivial spherical harmonics;
3. helicity-like signed boundary pairings;
4. a nonlocal pressure/core-tail pairing with a fixed spatial center;
5. a global cocycle/unique-continuation constraint linking the complete interior trajectory to the full boundary history.

Each candidate must be tested against the aperiodic toroidal leading anti-model before being promoted to a theorem target.

## 12. Status

Certified:

\[
\boxed{
\text{ordinary finite-radius similarity energy balance supplies no new leading constraint on }A.
}
\]

Not certified:

- absence of every possible tensor/signed boundary constraint;
- global rigidity of \(A\);
- global 3D Navier--Stokes regularity.

## 13. Next calculation

The lowest-cost next test is the **angular momentum / first spherical moment of momentum flux**, because unlike scalar energy it is sensitive to the toroidal channel.

The M19-041 anti-model is purely toroidal, so a successful observable must see

\[
\omega\times\nabla_{S^2}\psi.
\]

The next module should derive the scaling and similarity transport law for

\[
\int_{S_R} y\times T(U,P)n\,dS
\]

or an equivalent localized angular-momentum balance and determine whether its leading critical term is finite, conserved, integrable, or again absorbed by transport/storage.

---

\[
\boxed{\text{M19-055 COMPLETE; SCALAR FINITE-RADIUS ENERGY COMPATIBILITY DOES NOT CLOSE THE RESONANT SCATTERING DATUM.}}
\]