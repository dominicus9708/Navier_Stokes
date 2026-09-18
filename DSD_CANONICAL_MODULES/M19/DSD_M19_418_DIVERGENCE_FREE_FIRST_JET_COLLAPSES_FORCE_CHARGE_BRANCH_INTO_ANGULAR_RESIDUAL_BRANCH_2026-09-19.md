# M19-418 — Divergence-free first jet collapses the force-charge branch into the angular residual branch

Date: 2026-09-19  
Canonical ID: **M19-418**  
Status: **MAJOR RESIDUAL-CHANNEL COUPLING / THE FIRST TERMINAL JET IS DIVERGENCE FREE / ITS SPHERICAL MEAN FORCE MODE IS THE LOG DERIVATIVE OF AN l=1 RADIAL MOMENT / BOUNDED RECURRENCE GIVES AN EXACT MEAN IDENTITY FORCING QUANTITATIVE MEAN-FREE ANGULAR RESIDUAL WHENEVER FORCE-CHARGE ACTION IS NONZERO / FORCE IS NOT AN INDEPENDENT TERMINAL CHANNEL / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. First terminal jet and incompressibility

M5-572 gives the first terminal expansion
\[
u(x,s)
=
r^{-1}A(q,\omega)
+
(-s)r^{-3}C(q,\omega)
+\cdots,
\qquad
q=\log r.
\]

Because the full velocity is divergence free at every time, every coefficient satisfies its homogeneity-adapted divergence constraint.

For the degree-minus-three coefficient \(C\),
\[
\boxed{
(\partial_q-1)C_r
+
\operatorname{div}_{S^2}C_T
=
0.
}
\]

This constraint was not used in M5-271's orthogonal force/angular norm split.

## 2. Define the first angular moment

Write
\[
C=C_r\omega+C_T,
\qquad
C_T\cdot\omega=0.
\]

Define
\[
\boxed{
M(q)
:=
\int_{S^2}
C_r(q,\omega)\,\omega\,d\omega,
}
\]
and
\[
T(q)
:=
\int_{S^2}C_T(q,\omega)d\omega.
\]

The total spherical mean is
\[
\boxed{
m(q)
:=
\int_{S^2}C(q,\omega)d\omega
=
M(q)+T(q).
}
\]

Up to the fixed sign convention, \(m\) is exactly the force-source mode in
\[
\mathcal F_A'(q)=-m(q).
\]

## 3. Exact moment identity from divergence freedom

Multiply
\[
(\partial_q-1)C_r
+
\operatorname{div}_{S^2}C_T
=
0
\]
by \(\omega\) and integrate over \(S^2\).

The first term gives
\[
M'-M.
\]

For the second term, embedded-sphere integration by parts gives
\[
\int_{S^2}
\omega\,
\operatorname{div}_{S^2}C_T
\,d\omega
=
-
\int_{S^2}C_Td\omega
=
-T.
\]

Therefore
\[
\boxed{
M'-M-T=0.
}
\]

Since
\[
m=M+T,
\]
we obtain the exact identity
\[
\boxed{
m(q)=M'(q).
}
\]

Thus the net spherical first-jet mean is itself a log-radius coboundary of an \(l=1\)-type radial moment.

## 4. Separate the constant spherical mean from the mean-free residual

Define
\[
\overline C(q)
=
\frac{m(q)}{4\pi},
\qquad
C^\perp(q,\omega)
=
C(q,\omega)-\overline C(q).
\]

Then
\[
\int_{S^2}C^\perp d\omega=0.
\]

The constant Cartesian vector \(\overline C\) contributes to \(M\) by
\[
\int_{S^2}
(\overline C\cdot\omega)\omega d\omega
=
\frac13m.
\]

Define the mean-free first angular moment
\[
\boxed{
E(q)
:=
\int_{S^2}
(C^\perp\cdot\omega)\omega d\omega.
}
\]

Hence
\[
\boxed{
M
=
\frac13m
+
E.
}
\]

Using
\[
m=M',
\]
we obtain
\[
\boxed{
M'-3M
=
-3E.
}
\]

This is the exact low-angular-mode ODE coupling force and angular residual channels.

## 5. Bounded recurrence gives a future-resolvent formula

On the compact recurrent terminal hull, \(M(q)\) is bounded.

Solve
\[
M'-3M=-3E.
\]

Multiplying by \(e^{-3q}\) and integrating to \(+\infty\) gives
\[
\boxed{
M(q)
=
3
\int_0^\infty
e^{-3\tau}
E(q+\tau)d\tau.
}
\]

Therefore the force moment is not autonomous.

It is the stable future resolvent of the mean-free angular first moment.

If
\[
C^\perp\equiv0,
\]
then
\[
E\equiv0,
\]
so bounded recurrence forces
\[
M\equiv0,
\qquad
m\equiv0.
\]

Hence a recurrent pure spherical-mean first jet is impossible.

## 6. Exact invariant-mean quadratic identity

Take the dot product of
\[
M'-3M=-3E
\]
with \(M\) and average in invariant log radius.

Bounded recurrence gives
\[
\langle M\cdot M'\rangle_q
=
\frac12
\langle(|M|^2)'\rangle_q
=
0.
\]

Therefore
\[
\boxed{
\langle|M|^2\rangle
=
\langle M\cdot E\rangle.
}
\]

Also
\[
m=M'=3(M-E).
\]

Hence
\[
\begin{aligned}
\langle|m|^2\rangle
&=
9
\langle|M-E|^2\rangle
\\
&=
9
\left(
\langle|E|^2\rangle
-
\langle|M|^2\rangle
\right).
\end{aligned}
\]

Thus
\[
\boxed{
\langle|E|^2\rangle
=
\langle|M|^2\rangle
+
\frac19
\langle|m|^2\rangle.
}
\]

In particular,
\[
\boxed{
\langle|E|^2\rangle
\ge
\frac19
\langle|m|^2\rangle.
}
\]

This is an exact quantitative coupling.

## 7. Convert the first moment into an angular-residual lower bound

By Cauchy--Schwarz,
\[
\begin{aligned}
|E|^2
&=
\left|
\int_{S^2}
\omega(\omega\cdot C^\perp)d\omega
\right|^2
\\
&\le
4\pi
\int_{S^2}|C^\perp|^2d\omega.
\end{aligned}
\]

Therefore
\[
\boxed{
\left\langle
\int_{S^2}|C^\perp|^2d\omega
\right\rangle
\ge
\frac{1}{36\pi}
\langle|m|^2\rangle.
}
\]

Since every Cartesian component of \(C^\perp\) has zero spherical mean, the first nonzero spherical eigenvalue gives
\[
\int_{S^2}
|\nabla_{S^2}C^\perp|^2d\omega
\ge
2
\int_{S^2}|C^\perp|^2d\omega.
\]

Hence
\[
\boxed{
\left\langle
\int_{S^2}
|\nabla_{S^2}C^\perp|^2d\omega
\right\rangle
\ge
\frac{1}{18\pi}
\langle|m|^2\rangle.
}
\]

Thus any positive mean-square force-charge activity forces quantitative angular residual activity.

## 8. Combine with M19-417 syndeticity

M19-417 says that one fixed residual channel/cell is syndetic on every minimal-hull orbit.

If the selected channel is already angular, nothing more is needed.

If the selected channel is force-charge, the syndetic fixed lower action gives
\[
\boxed{
\langle|m|^2\rangle
>0.
}
\]

Section 7 then gives
\[
\boxed{
\left\langle
\|\nabla_{S^2}C^\perp\|_2^2
\right\rangle
>0.
}
\]

Therefore there exists a state with a strict angular-residual event.

By continuity this event persists on a nonempty open neighborhood of the compact minimal hull.

Minimality then applies again: returns to that angular-event neighborhood are syndetic on every orbit.

Hence, **regardless of which channel M19-417 initially selects**,
\[
\boxed{
A_{res}^{syndetic}
}
\]
is mandatory on every nontrivial retained minimal hard hull.

## 9. Force-charge is demoted from an independent endpoint

The previous frontier
\[
F_{charge}^{syndetic,critical}
\lor
A_{res}^{syndetic,critical}
\]
collapses to
\[
\boxed{
A_{res}^{syndetic,critical}
}
\]
with possible force-charge activity as a subordinate projection.

The M19-415--416 stress-flux non-Cauchy/annular-acceleration defect remains a valid structural consequence when \(m\neq0\).

But it is no longer an independent escape route because
\[
\boxed{
F_{charge}
\Longrightarrow
A_{res}.
}
\]

Thus any closure of the angular residual branch automatically closes the force branch as well.

## 10. Relation to M19-414

M19-414 showed that direct conversion of angular residual activity into unsigned raw-H2 ancestry yields only critical \(R^{-3}\) physical weight with \(O(\log R)\) multiplicity.

M19-418 does not change that scaling firewall.

Instead it simplifies the topology of the proof tree:

\[
\boxed{
\text{all mandatory residual activity can be routed through the mean-free angular first jet.}
}
\]

Therefore the next calculation should stop treating force and angular residual as parallel terminal roots.

The sole residual structural target is now to extract **noncritical information** from
\[
C^\perp,
\qquad
\nabla_{S^2}C^\perp.
\]

## 11. Immediate next target

The most promising new leverage is that \(C^\perp\) is not an arbitrary mean-free field.

It simultaneously satisfies

1. the homogeneity-adapted divergence constraint;
2. the first-jet stationary-residual formula
   \[
   C=\mathcal R_{stat}[A,P];
   \]
3. the pressure-Poisson relation inherited from \(A\);
4. syndetic positive angular activity from M19-417--418.

The next calculation should project the exact residual formula onto spherical harmonics and determine whether the mandatory mean-free activity can remain entirely in the lowest \(l=1\) sector.

If the \(l=1\) sector is a pure coboundary/translation mode, the residual must leak to \(l\ge2\), producing a stronger angular spectral gap than the generic Poincare constant.

\[
\boxed{\text{M19-418 COMPLETE; FORCE-CHARGE IS NOT AN INDEPENDENT RESIDUAL CHANNEL.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
