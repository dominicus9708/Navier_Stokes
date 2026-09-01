# DSD M5-531 — Invariant recurrence forces infinite first radial enstrophy moment almost everywhere on the nontrivial hard component

Date: 2026-09-01

Status: **RECURRENCE/MOMENT RIGIDITY / M5-526 SHOWS THAT A UNIFORM BOUND ON THE CRITICAL FIRST RADIAL ENSTROPHY MOMENT CONTROLS THE VELOCITY `L3` NORM, WHILE M5-527 IMPORTS THE ALBRITTON--BARKER ANCIENT LIOUVILLE THEOREM TO EXCLUDE ANY NONTRIVIAL MILD ANCIENT SOLUTION HAVING A BOUNDED `L3` BACKWARD SUBSEQUENCE / HENCE A NONTRIVIAL COMPLETE HARD-CORE ORBIT CANNOT HAVE A BACKWARD SUBSEQUENCE WITH BOUNDED FIRST RADIAL MOMENT / ON AN INVERTIBLE INVARIANT ERGODIC COMPONENT, POINCARE RECURRENCE WOULD FORCE SUCH A BACKWARD SUBSEQUENCE THROUGH ANY POSITIVE-MEASURE FINITE-MOMENT SUBLEVEL SET / THEREFORE THE HARD RECURRENT MEASURE IS CONCENTRATED ON STATES WITH INFINITE FIRST RADIAL ENSTROPHY MOMENT / THIS IS AN EXTENDED-MOMENT DEFECT, NOT A CONTRADICTION WITH GLOBAL SMOOTH `H^m` COMPACTNESS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Invariant hard component

Use the common similarity suspension/hull obtained in M5-485 and sharpened in M5-508--515.

Let

\[
(\widehat{\mathfrak H},\phi^\theta,\nu)
\]

be one nontrivial invariant ergodic component carrying the retained hard-core marks.

In particular,

\[
\nu\text{-a.e. orbit is complete for }\theta\in\mathbb R,
\]

and the component is nonzero because it carries positive ratchet/dual/production activity.

The flow is invertible and measure preserving:

\[
\boxed{
(\phi^\theta)_*\nu=\nu
\qquad
\forall\theta\in\mathbb R.
}
\]

---

## 2. Extended first radial moment

For a hull state `Y`, define

\[
\boxed{
\mathcal M_1(Y)
:=
\int_{\mathbb R^3}
|y|\,|W_Y(y)|^2dy
\in[0,\infty].
}
\]

This quantity may be infinite even though

\[
W_Y\in H^m(\mathbb R^3)
\qquad
\forall m<\infty.
\]

That distinction is essential: unweighted smoothness does not control a positive spatial moment.

---

## 3. Lower semicontinuity / measurability

For `R>0`, define the truncated moment

\[
\mathcal M_{1,R}(Y)
:=
\int
\min(|y|,R)
|W_Y(y)|^2dy.
\]

On the M5-508 global strong `L2` compact topology,

\[
\mathcal M_{1,R}
\]

is continuous for every finite `R`.

Moreover,

\[
\mathcal M_{1,R}(Y)
\uparrow
\mathcal M_1(Y)
\qquad
(R\to\infty).
\]

Hence

\[
\boxed{
\mathcal M_1
\text{ is Borel measurable and lower semicontinuous as an extended observable.}
}
\]

The sets

\[
A_K:=\{Y:\mathcal M_1(Y)\le K\}
\]

are therefore measurable.

---

## 4. Bounded first moment controls the velocity `L3` norm

M5-525--526 gave a dyadic critical Dirichlet sequence

\[
b_k
=R_k\int_{A_k^*}|\nabla U|^2dy
\]

and the packing inequality

\[
\|U\|_{L^3(|y|>R_0)}^3
\le
C\sum_{k\ge0}b_k^{3/2}.
\]

Also,

\[
\sum_{k\ge0}b_k
\lesssim
\int |y||\nabla U|^2dy.
\]

Since `|y|` is an `A_2` weight, the weighted Calderon--Zygmund estimate used in M5-529 gives

\[
\int |y||\nabla U|^2dy
\le
C
\int |y||W|^2dy
=C\mathcal M_1.
\]

Because for nonnegative sequences

\[
\sum b_k^{3/2}
\le
\left(\sum b_k\right)^{3/2},
\]

we obtain

\[
\boxed{
\mathcal M_1(Y)\le K
\Longrightarrow
\|U_Y\|_3
\le C_K,
}
\]

where the fixed interior ball contribution is uniformly bounded by global smooth compactness.

Thus a bounded first-moment subsequence is automatically a bounded `L3` subsequence.

---

## 5. Ancient Liouville firewall from M5-527

M5-527 imported the following external theorem of Albritton--Barker for mild ancient 3D Navier--Stokes solutions:

> if a mild ancient solution possesses a sequence of times tending to backward infinity on which its `L3` norm is uniformly bounded, then the ancient solution is identically zero.

The M5-478 hard ancient cell is smooth/mild on every finite negative interval and is nontrivial by the retained first-hitting carrier.

Therefore any nontrivial complete orbit satisfies

\[
\boxed{
\nexists\ \theta_n\to-\infty
\text{ with }
\sup_n\|U(\theta_n)\|_3<\infty.
}
\]

By Section 4,

\[
\boxed{
\nexists\ \theta_n\to-\infty
\text{ with }
\sup_n\mathcal M_1(\phi^{\theta_n}Y)<\infty.
}
\]

Equivalently, for every finite `K`, each nontrivial hard orbit can visit

\[
A_K
\]

only finitely many times in the sufficiently far backward direction.

---

## 6. Assume a finite-moment set has positive invariant measure

Suppose, for contradiction, that

\[
\nu(\mathcal M_1<\infty)>0.
\]

Since

\[
\{\mathcal M_1<\infty\}
=
\bigcup_{K=1}^\infty A_K,
\]

there exists some finite `K` with

\[
\boxed{
\nu(A_K)>0.
}
\]

---

## 7. Backward Poincare recurrence

Fix any nonzero time step `tau_0>0` and consider the invertible map

\[
T:=\phi^{-\tau_0}.
\]

Because `nu` is invariant under the full flow,

\[
T_*\nu=\nu.
\]

Poincare recurrence applied to `A_K` gives that for `nu`-almost every `Y in A_K`, there exist infinitely many integers

\[
n_j\to\infty
\]

such that

\[
T^{n_j}Y
=
\phi^{-n_j\tau_0}Y
\in A_K.
\]

Therefore

\[
\boxed{
\mathcal M_1(\phi^{-n_j\tau_0}Y)
\le K
}
\]

along a sequence with

\[
-n_j\tau_0\to-\infty.
\]

This is exactly the bounded backward first-moment subsequence excluded in Section 5.

Contradiction.

---

## 8. Main conclusion

Hence

\[
\boxed{
\nu(\mathcal M_1<\infty)=0.
}
\]

Equivalently,

\[
\boxed{
\mathcal M_1(Y)=\infty
\quad
\text{for }\nu\text{-almost every }Y
\text{ in the nontrivial recurrent hard component.}
}
\]

This is substantially stronger than the earlier orbitwise statement

\[
\mathcal M_1(\theta)\to\infty
\quad(\theta\to-\infty)
\]

whenever the moment happens to be finite.

The invariant hard measure itself is concentrated on the infinite-moment locus.

---

## 9. No contradiction with global smooth compactness

M5-508 gives, for every finite `m`,

\[
\sup_{Y\in\widehat{\mathfrak H}}
\|W_Y\|_{H^m}<\infty
\]

and global strong precompactness in every finite Sobolev norm.

M5-531 does not contradict this.

A sequence of arbitrarily small smooth packets placed at arbitrarily large radii can converge strongly in every unweighted `H^m` norm while carrying an infinite or divergent first spatial moment.

Thus the remaining defect is genuinely weighted/spatial:

\[
\boxed{
\text{unweighted all-order compactness}
+
\text{infinite critical first radial moment}.
}
\]

---

## 10. DSD interpretation

Before M5-531, the remote tail could still be described as an occasional backward escape.

After invariant recurrence is imposed, that description is no longer adequate.

The recurrent hard component must satisfy

\[
\boxed{
\text{finite unweighted critical mass}
\quad\text{but}\quad
\text{infinite weighted first moment almost everywhere}.
}
\]

Therefore the tail is not a transient accident of one orbit phase.

It is an invariant structural property of the surviving recurrent measure.

---

## 11. Log-radius formulation

By M5-530,

\[
\mathcal M_1(Y)
=
\int_{-\infty}^{\infty}
\mathfrak T(e^\rho,Y)d\rho.
\]

Hence M5-531 implies

\[
\boxed{
\int_{-\infty}^{\infty}
\mathfrak T(e^\rho,Y)d\rho
=\infty
\quad\text{for }\nu\text{-a.e. }Y.
}
\]

Because the unweighted enstrophy is finite and uniformly tight, this divergence must be produced by a sufficiently long/diffuse critical log-radius tail, not by infinite mass on one fixed shell.

---

## 12. Highest-value next target

The moving-tail equation from M5-530 is

\[
\left(\partial_\theta+\frac12\partial_\rho\right)
\mathfrak T
=
\mathcal S.
\]

Average this identity against the invariant measure `nu`.

The `theta` derivative should disappear by invariance, producing an exact radial ensemble balance

\[
\boxed{
\frac12\partial_\rho
\overline{\mathfrak T}(\rho)
=
\overline{\mathcal S}(\rho).
}
\]

Together with

\[
\int\overline{\mathfrak T}(\rho)d\rho=\infty,
\]

this would convert the abstract infinite-moment defect into an invariant **radial flux/source defect at infinity**.

That is the next calculation.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
