# M19-434 — The terminal pressure-dipole acceleration is a q-invariant finite-dimensional minimal-set constant, not a freely switching recurrent channel

Date: 2026-09-19  
Canonical ID: **M19-434**  
Status: **PRESSURE-DIPOLE DYNAMIC REDUCTION / THE PURE DEGREE-minus-3 DIVERGENCE-FREE CURL-FREE POTENTIAL-DIPOLE COMPONENT OF THE FIRST TERMINAL JET CANNOT CARRY q-DEPENDENCE / ITS COEFFICIENT IS A CONTINUOUS TRANSLATION-INVARIANT THREE-VECTOR AND THEREFORE CONSTANT ON EACH COMPACT MINIMAL HARD COMPONENT / THE DIPOLE ESCAPE IS FINITE DIMENSIONAL AND FROZEN IN q, THOUGH NOT YET FORCED TO VANISH / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Potential-dipole basis

For a vector \(a\in\mathbb R^3\), define

\[
\boxed{
W_a(\omega)
:=
a-3(a\cdot\omega)\omega.
}
\]

Then

\[
r^{-3}W_a(\omega)
=
\nabla
\left(
\frac{a\cdot x}{|x|^3}
\right),
\]

so on \(\mathbb R^3\setminus\{0\}\),

\[
\nabla\cdot(r^{-3}W_a)=0,
\qquad
\nabla\times(r^{-3}W_a)=0.
\]

This is the three-dimensional harmonic pressure-dipole acceleration sector isolated in M19-433.

## 2. Allow a q-dependent coefficient and impose incompressibility

Consider a putative pure potential-dipole component of the first terminal jet,

\[
\boxed{
C_{dip}(q,\omega)
=
W_{a(q)}(\omega).
}
\]

Write

\[
Y_{a(q)}(\omega)
:=
a(q)\cdot\omega.
\]

Then

\[
(C_{dip})_r
=
-2Y_{a(q)},
\]

and

\[
(C_{dip})_T
=
\nabla_{S^2}Y_{a(q)}.
\]

The degree-minus-three incompressibility condition from M19-418 is

\[
\boxed{
(\partial_q-1)C_r
+
\operatorname{div}_{S^2}C_T
=
0.
}
\]

Since

\[
\Delta_{S^2}Y_a=-2Y_a,
\]

substitution gives

\[
(\partial_q-1)(-2Y_a)-2Y_a=0.
\]

Therefore

\[
-2\partial_qY_a=0.
\]

Hence

\[
\boxed{
a'(q)=0.
}
\]

Thus a pure divergence-free curl-free degree-minus-three potential dipole cannot oscillate in log radius.

## 3. The dipole coefficient is translation invariant

The canonical q-translation acts by

\[
(T_hC)(q,\omega)=C(q+h,\omega).
\]

Since the pure dipole coefficient is independent of q,

\[
\boxed{
a(T_hC)=a(C).
}
\]

Therefore the dipole coefficient is a translation-invariant observable on the terminal factor whenever the projection is defined.

It is not a phase variable.

## 4. Continuity on the compact terminal hull

The potential-dipole space

\[
\mathcal D
=
\{W_a:a\in\mathbb R^3\}
\]

is finite dimensional.

Projection onto \(\mathcal D\) is continuous in any retained local smooth/Sobolev topology on the sphere.

Hence

\[
\boxed{
C\mapsto a_{dip}(C)
}
\]

is a continuous finite-dimensional observable on the compact hard terminal hull.

## 5. Minimality forces one constant vector

Let \(\mathcal T\) be one compact minimal terminal component.

A continuous translation-invariant observable is constant on a minimal set.

Therefore there exists one vector

\[
\boxed{
a_*\in\mathbb R^3
}
\]

such that

\[
\boxed{
a_{dip}(T)=a_*
\qquad
\forall T\in\mathcal T.
}
\]

Thus the pressure-dipole acceleration escape is not

\[
a=a(q)
\]

or a switching recurrent channel.

It is at most one fixed three-vector attached to the entire minimal component.

## 6. Relation to M5-134 and M5-144

M5-134 shows that the realized leading \(r^{-2},l=1\) pressure dipole is fixed on each velocity-tail fiber.

M5-144 strengthens the odd resonant pressure coefficients to minimal-set invariants.

M19-434 supplies the first-jet vector form of the same rigidity:

\[
\boxed{
\text{harmonic pressure dipole}
\Longleftrightarrow
\text{q-invariant potential-dipole acceleration coefficient}.
}
\]

The three descriptions are compatible and must not be counted as separate resources.

## 7. First angular moment detects the coefficient

For the basis field,

\[
W_a\cdot\omega
=
-2(a\cdot\omega).
\]

Define the radial first moment

\[
M_C
:=
\int_{S^2}
C_r\,\omega,d\omega.
\]

For the pure dipole,

\[
\begin{aligned}
M_{dip}
&=
-2
\int_{S^2}
(a\cdot\omega)\omega\,d\omega
\\
&=
\boxed{
-\frac{8\pi}{3}a.
}
\end{aligned}
\]

Thus

\[
\boxed{
a
=
-\frac{3}{8\pi}M_{dip}.
}
\]

The dipole is invisible to the spherical mean force,

\[
\int_{S^2}W_a,d\omega=0,
\]

but is exactly visible in the \(l=1\) radial first moment.

## 8. Compatibility with M19-418

M19-418 defines

\[
M(q)
=
\int C_r\omega,d\omega
\]

and proves

\[
m=M',
\qquad
M'-3M=-3E.
\]

For a pure potential dipole,

\[
m=0,
\]

and \(M\) is constant.

Hence

\[
E=M,
\]

which exactly satisfies

\[
-3M=-3E.
\]

Therefore the pressure dipole is not excluded by the first-jet force/angular coupling.

It lies in the mean-free angular residual branch with zero net force.

## 9. Consequence for the overlap proof tree

M19-433 introduced

\[
Z_{dip}
:
\text{vorticity-invisible harmonic pressure-dipole acceleration}.
\]

M19-434 reduces this to

\[
\boxed{
Z_{dip}
\Longrightarrow
a_*\neq0
\text{ for one fixed component-wide vector }a_*.
}
\]

This is much narrower than an arbitrary recurrent pressure history.

The branch has no q-phase entropy, no switching labels, and no infinite-dimensional freedom.

## 10. What remains open

Nothing here forces

\[
a_*=0.
\]

M5-143 already warns that finite energy and absence of external forcing do not annihilate general stress moments.

For the leading critical pressure dipole, the issue is even more delicate because every finite preterminal whole-space slice has faster far-pressure decay, while the terminal/blow-up limit may lose that tightness.

Thus the remaining question is not local PDE freedom.

It is a global noncommuting-limit question:

\[
\boxed{
\text{Can one finite-energy unforced ancestral sequence generate a nonzero fixed critical pressure-dipole coefficient }a_*\text{ in the terminal hard factor?}
}
\]

## 11. Next target

At every finite regular parent time, whole-space finite energy gives an integrable Reynolds stress and hence far pressure beginning at order \(r^{-3}\), not \(r^{-2}\).

Therefore a nonzero terminal \(r^{-2}\) dipole requires failure of uniform pressure/stress-moment tightness under the blow-up/terminal limit.

The next calculation should quantify exactly which stress moment must escape and determine its physical scaling.

This will decide whether \(a_*\neq0\) is

- another exact critical noncommuting-limit defect;
- or a subcritical/tightness violation that can be excluded.

\[
\boxed{\text{M19-434 COMPLETE; THE PRESSURE-DIPOLE ESCAPE IS A FROZEN THREE-DIMENSIONAL MINIMAL-SET CONSTANT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
