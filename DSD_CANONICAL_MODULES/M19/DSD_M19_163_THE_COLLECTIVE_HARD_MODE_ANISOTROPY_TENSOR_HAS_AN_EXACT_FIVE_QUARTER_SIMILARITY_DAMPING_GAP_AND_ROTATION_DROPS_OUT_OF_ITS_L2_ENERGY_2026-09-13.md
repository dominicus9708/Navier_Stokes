# DSD M19-163 — The collective hard-mode anisotropy tensor has an exact five-quarter similarity damping gap and rotation drops out of its L2 energy

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / TENSOR-ANISOTROPY EVOLUTION + 5/4 GAP / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-162 showed that the trace of local strain compensation over a family of hard modes depends only on the collective traceless tensor

\[
Q_E
=
\Gamma_E-\frac{\rho_E}{3}I.
\]

The present module derives the evolution equation for `Gamma_E` and `Q_E` from the exact linearized vorticity equation.

A new coercive feature appears:

\[
\boxed{
Q_E\text{ has a bare }5/4\text{ similarity damping gap in }L^2.
}
\]

This is substantially stronger than the `1/4` gap for a single linearized vorticity.

## 2. Linearized vorticity family

Let

\[
\eta_a=\nabla\times W_a,
\qquad
a=1,\ldots,m,
\]

be a family of linearized perturbations transported by the same background `U`.

They satisfy

\[
\begin{aligned}
\partial_s\eta_a
={}&
\nu\Delta\eta_a
-
\eta_a
-
\frac12(y\cdot\nabla)\eta_a
-
(U\cdot\nabla)\eta_a\\
&+
(\nabla U)\eta_a
+
F_a,
\end{aligned}
\]

where

\[
\boxed{
F_a
:=
(\Omega\cdot\nabla)W_a
-
(W_a\cdot\nabla)\Omega.
}
\]

## 3. Collective tensor

Define

\[
\boxed{
\Gamma
:=
\sum_{a=1}^m
\eta_a\otimes\eta_a.
}
\]

Also define the gradient tensor

\[
\boxed{
\mathcal G
:=
\sum_{a=1}^m\sum_{k=1}^3
(\partial_k\eta_a)
\otimes
(\partial_k\eta_a).
}
\]

and the nonlocal forcing tensor

\[
\boxed{
\mathcal F
:=
\sum_{a=1}^m
\left(
F_a\otimes\eta_a
+
\eta_a\otimes F_a
\right).
}
\]

Using

\[
\Delta(\eta\otimes\eta)
=
(\Delta\eta)\otimes\eta
+
\eta\otimes(\Delta\eta)
+
2\sum_k
\partial_k\eta\otimes\partial_k\eta,
\]

we obtain the exact tensor equation

\[
\boxed{
\begin{aligned}
\partial_s\Gamma
={}&
\nu\Delta\Gamma
-
2\nu\mathcal G
-
2\Gamma
-
\frac12(y\cdot\nabla)\Gamma
-
(U\cdot\nabla)\Gamma\\
&+
(\nabla U)\Gamma
+
\Gamma(\nabla U)^T
+
\mathcal F.
\end{aligned}
}
\]

## 4. Strain/rotation decomposition

Write

\[
\nabla U
=
S+R,
\]

with

\[
S^T=S,
\qquad
R^T=-R.
\]

Then

\[
(\nabla U)\Gamma
+
\Gamma(\nabla U)^T
=
S\Gamma+\Gamma S
+
R\Gamma-\Gamma R.
\]

The final term is a commutator.

## 5. Scalar density and traceless anisotropy

Define

\[
\rho
:=
\operatorname{tr}\Gamma
=
\sum_a|\eta_a|^2,
\]

and

\[
\boxed{
Q
:=
\Gamma-\frac\rho3I,
\qquad
\operatorname{tr}Q=0.
}
\]

Likewise let

\[
\mathcal G^\circ
:=
\mathcal G-
\frac{\operatorname{tr}\mathcal G}{3}I,
\]

and

\[
\mathcal F^\circ
:=
\mathcal F-
\frac{\operatorname{tr}\mathcal F}{3}I.
\]

Because `tr S=0`, the traceless equation becomes

\[
\boxed{
\begin{aligned}
\partial_sQ
={}&
\nu\Delta Q
-
2Q
-
\frac12(y\cdot\nabla)Q
-
(U\cdot\nabla)Q\\
&-
2\nu\mathcal G^\circ
+
\frac{2\rho}{3}S\\
&+
(SQ+QS)^\circ
+
[R,Q]
+
\mathcal F^\circ.
\end{aligned}
}
\]

where

\[
[R,Q]:=RQ-QR.
\]

This is the exact collective anisotropy equation.

## 6. L2 anisotropy energy

Take the Frobenius `L2` pairing with `Q`.

The divergence-free transport term satisfies

\[
\int Q:(U\cdot\nabla)Q=0.
\]

The similarity drift gives

\[
-\frac12
\int
Q:(y\cdot\nabla)Q
=
\frac34\|Q\|_2^2.
\]

Combined with the reaction `-2Q`, this yields

\[
-2+\frac34
=-\frac54.
\]

Thus

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}\|Q\|_2^2
+
\nu\|\nabla Q\|_2^2
+
\frac54\|Q\|_2^2
={}&
-2\nu\int Q:\mathcal G^\circ\\
&+
\frac23\int \rho\,Q:S\\
&+
\int Q:(SQ+QS)^\circ\\
&+
\int Q:[R,Q]\\
&+
\int Q:\mathcal F^\circ.
\end{aligned}
}
\]

## 7. Rotation commutator cancels exactly

Because `Q` is symmetric and `R` is skew,

\[
\begin{aligned}
Q:[R,Q]
&=
\operatorname{tr}\left(Q(RQ-QR)\right)\\
&=
\operatorname{tr}(QRQ)
-
\operatorname{tr}(Q^2R)\\
&=
\operatorname{tr}(RQ^2)
-
\operatorname{tr}(Q^2R)\\
&=0.
\end{aligned}
\]

Hence

\[
\boxed{
\int Q:[R,Q]=0.
}
\]

Local rigid rotation does not pay or amplify the `L2` collective-anisotropy energy.

## 8. Exact five-quarter gap

The bare part of the anisotropy equation therefore has coercivity

\[
\boxed{
\frac12\frac d{ds}\|Q\|_2^2
+
\nu\|\nabla Q\|_2^2
+
\frac54\|Q\|_2^2
=
\text{anisotropy sources}.
}
\]

Compare this with the single-vorticity quarter-gap

\[
\frac12\frac d{ds}\|\eta\|_2^2
+
\nu\|\nabla\eta\|_2^2
+
\frac14\|\eta\|_2^2
=
\text{compensation}.
\]

Thus the collective traceless tensor carries an additional unit of similarity damping:

\[
\boxed{
5/4-1/4=1.
}
\]

This is a genuinely new positive structural margin.

## 9. Sources of collective anisotropy

The right-hand side contains four nontrivial source classes:

1. **gradient anisotropy**
   \[
   -2\nu\mathcal G^\circ;
   \]

2. **scalar-density to strain conversion**
   \[
   \frac{2\rho}{3}S;
   \]

3. **strain acting on existing anisotropy**
   \[
   (SQ+QS)^\circ;
   \]

4. **nonlocal background-vorticity forcing**
   \[
   \mathcal F^\circ.
   \]

Therefore the `5/4` gap is not by itself a contradiction. A persistent multi-channel neutral block must continuously regenerate `Q` through these sources.

## 10. Period-averaged necessary condition

For a relative-periodic hard family whose collective tensor returns up to orthogonal rotation, the `L2` norm of `Q` returns exactly after one period.

Hence

\[
\boxed{
\begin{aligned}
\nu\int_0^S\|\nabla Q\|_2^2ds
+
\frac54\int_0^S\|Q\|_2^2ds
={}&
-2\nu\int_0^S\!\int Q:\mathcal G^\circ\\
&+
\frac23\int_0^S\!\int \rho\,Q:S\\
&+
\int_0^S\!\int Q:(SQ+QS)^\circ\\
&+
\int_0^S\!\int Q:\mathcal F^\circ.
\end{aligned}
}
\]

Any persistent collective anisotropy must therefore pay an average source budget at least `5/4` per `Q`-mass, plus diffusion.

## 11. Relation to kernel multiplicity

M19-159 showed that an extra kernel direction forces an additional superthreshold compensation eigenchannel.
M19-162 showed that multiple channels force a collective anisotropy tensor `Q`.

The present module adds:

\[
\boxed{
\text{persistent }Q\neq0
\Longrightarrow
\text{sources must overcome a }5/4\text{ tensor gap}.
}
\]

Thus a many-channel kernel is more expensive than the scalar `1/4` bookkeeping suggests.

## 12. What does not close automatically

The diffusion-defect tensor `G^circ` has no fixed sign.

Likewise

\[
\rho Q:S,
\qquad
Q:(SQ+QS)^\circ,
\qquad
Q:\mathcal F^\circ
\]

can all have either sign.

Therefore no universal decay of `Q` is claimed yet.

The new task is to show that these sources cannot jointly sustain the `5/4` gap for a nonsymmetry superthreshold family beyond the exact symmetry block.

## 13. Audit verdict

### Proved

1. Exact evolution equation for the collective hard-mode tensor `Gamma`.
2. Exact traceless anisotropy equation for `Q`.
3. Exact cancellation of local rigid rotation in the `Q`-energy.
4. Exact bare `5/4` similarity damping gap for collective anisotropy.

### Not proved

1. That the anisotropy source terms are below the `5/4` threshold.
2. Kernel rigidity.
3. Irrational elliptic exclusion.
4. Global regularity.

## 14. Next target

M19-164 should estimate each anisotropy source against

\[
\nu\|\nabla Q\|_2^2
+
\frac54\|Q\|_2^2
\]

and determine whether the new unit-sized margin can absorb the gradient-anisotropy and nonlocal terms under the existing compact-corridor bounds.

Even a conditional inequality of the form

\[
\text{anisotropy-source operator norm}<5/4
\]

would eliminate all collective nonsymmetry compensation blocks on that subcorridor.
