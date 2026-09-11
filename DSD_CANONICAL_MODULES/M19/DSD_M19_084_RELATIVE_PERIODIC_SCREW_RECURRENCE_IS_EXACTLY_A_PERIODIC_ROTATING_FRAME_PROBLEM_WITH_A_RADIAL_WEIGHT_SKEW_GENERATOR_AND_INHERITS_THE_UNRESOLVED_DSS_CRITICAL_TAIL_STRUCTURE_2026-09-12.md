# DSD M19-084 — Relative-periodic screw recurrence is exactly a periodic rotating-frame problem with a radial-weight skew generator and inherits the unresolved DSS critical-tail structure

**Date:** 2026-09-12  
**Status:** RELATIVE-PERIODIC BRANCH CONSOLIDATION / ROTATION DOES NOT CREATE A NEW SCALAR ENERGY PAYER OR CLOSE THE DSS TAIL / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-076 isolated the relative-periodic branch

\[
\boxed{
\sigma_TY=R\cdot Y,
\qquad
R\in SO(3).
}
\]

It must not be discarded by quotienting rotations.

M5-566 already analyzed the exact periodic/DSS branch and showed that any unresolved nontrivial DSS survivor on the passive spectator lane must carry a nonzero log-periodic critical tail.

The present module determines whether relative periodicity is a genuinely new analytic root or a rotating-frame extension of the same unresolved DSS structure.

It is the latter.

## 2. Relative-periodic similarity state

Assume

\[
\boxed{
U(y,\theta+T)
=R\,U(R^{-1}y,\theta),
}
\tag{1}
\]

with \(T>0\).

Choose a skew-symmetric matrix

\[
K\in\mathfrak{so}(3)
\]

such that

\[
\boxed{e^{TK}=R.}
\]

Every rotation admits such a logarithm after choosing an axis and an angle representative.

Set

\[
S_\theta:=e^{\theta K}.
\]

Define the rotating-frame velocity

\[
\boxed{
V(y,\theta)
:=S_\theta^{-1}U(S_\theta y,\theta).
}
\tag{2}
\]

## 3. The rotating-frame state is exactly periodic

Using (1),

\[
\begin{aligned}
V(y,\theta+T)
&=S_{\theta+T}^{-1}
U(S_{\theta+T}y,\theta+T)\\
&=S_\theta^{-1}R^{-1}
R\,U(R^{-1}RS_\theta y,\theta)\\
&=S_\theta^{-1}U(S_\theta y,\theta).
\end{aligned}
\]

Therefore

\[
\boxed{
V(y,\theta+T)=V(y,\theta).
}
\tag{3}
\]

Relative periodicity has become ordinary time periodicity.

## 4. Exact rotating-frame PDE

Differentiate (2):

\[
\partial_\theta V
=-KV
+S_\theta^{-1}(\partial_\theta U)(S_\theta y,\theta)
+(Ky)\cdot\nabla V.
\]

Hence

\[
S_\theta^{-1}\partial_\theta U
=
\partial_\theta V
+KV
-(Ky)\cdot\nabla V.
\]

Rotation covariance preserves the Laplacian, divergence, pressure gradient, and nonlinear transport. Therefore \(V\) solves

\[
\boxed{
\partial_\theta V
+\frac12V
+\frac12(y\cdot\nabla)V
+(V\cdot\nabla)V
+\mathcal J_KV
=-\nabla P+\nu\Delta V,
}
\tag{4}
\]

where

\[
\boxed{
\mathcal J_KV
:=KV-(Ky)\cdot\nabla V.
}
\tag{5}
\]

Also

\[
\nabla\cdot V=0.
\]

Thus the only change from the ordinary periodic similarity equation is the constant infinitesimal rotation generator \(\mathcal J_K\).

## 5. The rotation generator is skew in every radial weighted L2 space

Let

\[
w(y)=w(|y|)
\]

be any radial weight.

First,

\[
V\cdot KV=0
\]

pointwise because \(K\) is skew-symmetric.

Second,

\[
\begin{aligned}
-\int V\cdot((Ky)\cdot\nabla V)w\,dy
&=-\frac12\int (Ky)\cdot\nabla(|V|^2)w\,dy\\
&=\frac12\int |V|^2\nabla\cdot(wKy)\,dy.
\end{aligned}
\]

But

\[
\nabla\cdot(Ky)=\operatorname{tr}K=0
\]

and, since \(w\) is radial,

\[
(Ky)\cdot\nabla w=0.
\]

Therefore

\[
\boxed{
\int V\cdot\mathcal J_KV\,w\,dy=0.
}
\tag{6}
\]

The same identity holds for any vector field in the domain of the generator.

Hence \(\mathcal J_K\) is skew with respect to the radial weighted kinetic inner product.

## 6. Vorticity/enstrophy scalar ledgers are also unchanged by the rotation term

Let

\[
\Omega_V:=\nabla\times V.
\]

Rotations commute with curl, so the rotating-frame vorticity equation contains the same generator

\[
\mathcal J_K\Omega_V.
\]

Consequently, for radial weights,

\[
\boxed{
\int \Omega_V\cdot\mathcal J_K\Omega_V\,w\,dy=0.
}
\tag{7}
\]

Thus the rotation correction creates no scalar enstrophy source or sink.

Any M5/M18/M19 scalar identity derived from radial weighted kinetic energy or enstrophy retains the same sign structure after moving to the rotating frame.

## 7. Leading far-field equation acquires only angular skew transport

Write

\[
r=e^\rho,
\qquad
F(\rho,\omega,\theta)
:=e^\rho V(e^\rho\omega,\theta).
\]

For the ordinary similarity equation, M5-566 used

\[
\left(\partial_\theta+\frac12\partial_\rho\right)F
=e^{-2\rho}\mathcal N[F,P].
\]

The rotating-frame equation becomes

\[
\boxed{
\left(
\partial_\theta
+\frac12\partial_\rho
+\mathfrak J_K
\right)F
=e^{-2\rho}\mathcal N_K[F,P],
}
\tag{8}
\]

where \(\mathfrak J_K\) is the induced angular/vector rotation generator on \(S^2\).

Its flow is unitary/isometric on every rotation-invariant angular norm.

Therefore one follows a combined dilation-plus-rotation characteristic rather than a pure dilation characteristic.

The right-hand side still carries the same geometrically integrable factor

\[
e^{-2\rho}.
\]

## 8. One-period defect remains O(r^-2) in the critical rescaled profile

Because \(V\) is exactly \(T\)-periodic and the homogeneous left-hand transport in (8) is an isometry along the combined characteristic, integration over one period gives the same defect size as M5-566:

\[
\boxed{
\|F(\rho+T/2,\text{rotated phase},\theta)
-F(\rho,\text{phase},\theta)\|_X
\le
Ce^{-2\rho}.
}
\tag{9}
\]

The only modification is the deterministic angular rotation accumulated during the period.

The radial defect remains geometrically summable.

Hence the tail converges to a critical rotating/log-periodic scattering amplitude.

## 9. Direct scattering relation recovers the screw law

In the original frame M19-076 found

\[
\boxed{
A(q-T/2,\omega)
=R\,A(q,R^{-1}\omega).
}
\tag{10}
\]

Equation (10) is exactly the scattering-space image of periodicity of \(V\) in the rotating frame.

Thus there are not two unrelated structures:

\[
\boxed{
\text{relative periodicity in }U
\Longleftrightarrow
\text{ordinary periodicity in the rotating frame}
\Longleftrightarrow
\text{screw-periodic critical tail in }A.
}
\]

## 10. Vanishing leading tail still routes to the existing L3 contradiction

Suppose the limiting critical rotating amplitude vanished.

The same geometrically summable defect as in M5-566 then improves the far-field velocity from critical \(r^{-1}\) to a subcritical tail, schematically

\[
V=O(r^{-3})
\]

in the retained annular norm.

Rotations preserve \(|U|\), so

\[
\|V(\theta)\|_{L^3}=\|U(\theta)\|_{L^3}.
\]

Hence the original relative-periodic state would enter the global \(L^3\) class.

The already retained recurrent/global-\(L^3\) Liouville gate then forces triviality, contradicting the nontrivial core mark.

Therefore any unresolved nontrivial relative-periodic survivor must carry

\[
\boxed{
A_{screw}\not\equiv0.
}
\]

It remains critical at order \(1/r\).

## 11. Why the skew term does not close the unresolved DSS problem

The key energy fact is precisely that

\[
\int V\cdot\mathcal J_KV\,w=0.
\]

Thus rotation contributes neither positive damping nor a monotone scalar payer.

The rotating-frame branch inherits the same fundamental M5-566 difficulty:

- a nonzero critical tail is compatible with finite enstrophy;
- the leading tail is controlled by homogeneous transport/rotation;
- genuine Navier--Stokes stress appears in the subleading correction;
- scalar radial-weight ledgers do not force the critical amplitude to vanish.

Therefore

\[
\boxed{
\text{relative-periodic screw}
\text{ is not a new scalar-energy root, but it is also not closed.}
}
\]

## 12. Branch consolidation

The periodic sector can now be organized as

\[
\boxed{
\mathcal R_{periodic}^{critical}
=
\begin{cases}
K=0:&\text{ordinary unresolved DSS tail of M5-566},\\
K\neq0:&\text{rotating-frame DSS / screw-periodic critical tail}.
\end{cases}
}
\]

Both share the same critical radial scaling and the same lack of a scalar damping obstruction.

The rotation parameter \(K\) should therefore be treated as a compact symmetry decoration of the periodic critical-tail complex, not as a fourth independent upstream root.

## 13. What is certified

M19-084 certifies:

1. exact conversion of relative periodicity to periodicity by a constant rotating frame;
2. the precise rotating-frame PDE;
3. skew-adjointness of the rotation generator in every radial weighted L2 energy;
4. preservation of the scalar enstrophy sign structure;
5. persistence of the M5-566 O(r^-2) rescaled-profile defect after following combined dilation/rotation characteristics;
6. nonzero critical tail requirement for every unresolved nontrivial relative-periodic survivor.

## 14. What remains open

M19-084 does not prove:

1. nonexistence of ordinary DSS critical tails;
2. nonexistence of rotating/screw DSS critical tails;
3. tail-to-core incompatibility;
4. center exhaustion by symmetry;
5. aperiodic factor rigidity;
6. global regularity.

## 15. Next target

The periodic and relative-periodic branches are now structurally consolidated.

The genuinely different survivor is the aperiodic center/factor branch, especially the deep-norm-degeneration case from M19-083 with diverging recovery gaps.

The next calculation should return there and ask whether the exact scattering translation law converts those diverging temporal recovery gaps into an equally explicit sequence of increasingly separated q-intervals whose local profiles must be regenerated from the same finite spectator core.

That is the natural place to test whether the new center recovery law can couple back to the historical replenishment mechanism of M5-563/M5-567.

---

\[
\boxed{\text{M19-084 COMPLETE.}}
\]
