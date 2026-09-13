# M19-222 — The natural vorticity cross-enstrophy pairing is exactly the linearization of the unsigned enstrophy balance and has no sign

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / SIGNED-PAIRING TEST + NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Candidate signed pairing

Let \(U\) be a retained smooth recurrent similarity solution and let \(W\) be a hard linearized solution, in particular a candidate zero-q invariant section from M19-219--221.

Write

\[
\Omega:=\nabla\times U,
\qquad
\eta:=\nabla\times W.
\]

A zero-q critical velocity tail has \(W=O(r^{-1})\), so \(\eta=O(r^{-2})\). On the retained finite-enstrophy lane the natural unweighted cross-enstrophy

\[
\boxed{
C(s):=\int_{\mathbb R^3}\eta(y,s)\cdot\Omega(y,s)\,dy
}
\]

is therefore a legitimate first signed scalar to test.

## 2. Background similarity-vorticity equation

Using the repository similarity convention

\[
\partial_sU
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
+\nabla P
=\nu\Delta U,
\]

curl gives

\[
\boxed{
\partial_s\Omega
=
\nu\Delta\Omega
-\Omega
-\frac12(y\cdot\nabla)\Omega
-(U\cdot\nabla)\Omega
+(\Omega\cdot\nabla)U.
}
\]

The coefficient \(-\Omega\) is the sum of the velocity similarity amplitude term and the curl of the dilation term.

## 3. Linearized vorticity equation

Linearizing about \(U\) gives

\[
\boxed{
\begin{aligned}
\partial_s\eta
={}&
u\Delta\eta
-\eta
-\frac12(y\cdot\nabla)\eta
-(U\cdot\nabla)\eta
-(W\cdot\nabla)\Omega\\
&+(\eta\cdot\nabla)U
+(\Omega\cdot\nabla)W.
\end{aligned}
}
\]

All four vector fields \(U,W,\Omega,\eta\) are divergence free.

## 4. Exact derivative of the cross-enstrophy

Differentiate

\[
C=\langle\eta,\Omega\rangle_{L^2}.
\]

The two viscous terms give

\[
-2\nu\int\nabla\eta:\nabla\Omega.
\]

For the two similarity amplitude/dilation terms,

\[
-2C
-\frac12\int y\cdot\nabla(\eta\cdot\Omega)
=
-2C+\frac32C
=-\frac12C.
\]

The background transport terms cancel by incompressibility:

\[
-\int (U\cdot\nabla)(\eta\cdot\Omega)=0.
\]

The tangent-advection term also vanishes:

\[
-\int ((W\cdot\nabla)\Omega)\cdot\Omega
=-\frac12\int W\cdot\nabla|\Omega|^2=0.
\]

The remaining terms are the stretching terms.

## 5. Stretching terms combine into a symmetric-strain form

Let

\[
S_U:=\frac12(\nabla U+\nabla U^T),
\qquad
S_W:=\frac12(\nabla W+\nabla W^T).
\]

The two terms containing \(\nabla U\) are

\[
\int ((\eta\cdot\nabla)U)\cdot\Omega
+
\int \eta\cdot((\Omega\cdot\nabla)U).
\]

Their sum is

\[
\boxed{
2\int\Omega^TS_U\eta.
}
\]

The remaining tangent-strain term is

\[
\int ((\Omega\cdot\nabla)W)\cdot\Omega
=
\boxed{
\int\Omega^TS_W\Omega
}
\]

because the antisymmetric part of \(\nabla W\) has zero quadratic form on \(\Omega\).

Therefore the exact cross-enstrophy identity is

\[
\boxed{
\frac{dC}{ds}
+2\nu\int\nabla\eta:\nabla\Omega
+\frac12C
=
2\int\Omega^TS_U\eta
+
\int\Omega^TS_W\Omega.
}
\]

## 6. This is precisely the tangent of the background enstrophy balance

The background enstrophy identity is

\[
\boxed{
\frac12\frac d{ds}\|\Omega\|_2^2
+\nu\|\nabla\Omega\|_2^2
+\frac14\|\Omega\|_2^2
=
\int\Omega^TS_U\Omega.
}
\]

Differentiate this identity along a family \(U+\varepsilon W\) at \(\varepsilon=0\).

The variation of the left side is exactly

\[
\frac{dC}{ds}
+2\nu\int\nabla\eta:\nabla\Omega
+\frac12C,
\]

while the variation of the stretching term is

\[
2\int\Omega^TS_U\eta
+
\int\Omega^TS_W\Omega.
\]

Hence

\[
\boxed{
\text{cross-enstrophy identity}
=
D(\text{ordinary enstrophy balance})[W].
}
\]

It is not a new independent signed conservation law.

## 7. No sign survives

Neither term

\[
2\int\Omega^TS_U\eta
\]

nor

\[
\int\Omega^TS_W\Omega
\]

has a fixed sign for a general divergence-free hard tangent.

Likewise the cross-gradient term

\[
\int\nabla\eta:\nabla\Omega
\]

is bilinear rather than positive.

Changing \(W\) to \(-W\) reverses every term in the identity, including \(C\). Therefore no one-sided inequality can follow from this scalar pairing without an additional orientation/normalization structure that itself breaks the \(W\mapsto-W\) symmetry.

Thus

\[
\boxed{
C=\langle\eta,\Omega\rangle
\text{ does not supply the missing zero-q signed coercivity.}
}
\]

## 8. Period/RDSS averaging does not repair the sign

For a fixed-moduli relative-periodic kernel, \(U\) and \(W\) return modulo the same physical rotation. Since the L2 pairing is rotation invariant,

\[
C(s+S)=C(s).
\]

Averaging the exact identity over one period removes only the total derivative:

\[
\boxed{
2\nu\left\langle\int\nabla\eta:\nabla\Omega\right\rangle
+\frac12\langle C\rangle
=
2\left\langle\int\Omega^TS_U\eta\right\rangle
+
\left\langle\int\Omega^TS_W\Omega\right\rangle.
}
\]

The remaining terms are still signed bilinear/trilinear quantities. Periodicity supplies no positivity.

## 9. Consequence for M19-221

M19-221 suggested testing a signed bilinear background-section pairing in the irrational \(m=0\) sector.

The most natural vorticity pairing fails for a structural reason: it is merely the first variation of an already unsigned balance.

Permanent firewall:

\[
\boxed{
\text{linearizing an unsigned energy/enstrophy identity}
\neq
\text{creating a signed kernel obstruction}.
}
\]

A successful pairing must therefore use additional geometric information not already contained in the scalar enstrophy functional, for example an orientation-sensitive helicity/current form, an adjoint mode not identical to the background, or a profile-specific Fredholm functional.

## 10. Next target

The immediate next pairing candidate should not be another first variation of a positive scalar norm. A sharper route is to inspect the adjoint hard bundle and ask whether the zero-q invariant section admits a canonical adjoint covector whose period pairing has a PDE-determined sign or nonzero topological value.

This is distinct from the same-vector Melnikov pairing already ruled out by M19-212.

---

\[
\boxed{
\text{M19-222: NATURAL CROSS-ENSTROPHY IS SIGN-INDEFINITE AND DOES NOT CLOSE THE ZERO-Q INVARIANT SECTION.}
}
\]
