# Exact affine strain / vorticity-covariance coupling envelope at fixed projective dispersion

Date: 2026-08-13

Status: **EXACT FINITE-DIMENSIONAL OPTIMIZATION / IDENTIFIES BIAXIAL EXTENSIONAL-PLANE HARD BRANCH**.

The earlier trace-free Frobenius estimate

\[
|\operatorname{tr}(SC)|
\le |S|_F\sqrt{\frac23-J}
\]

is useful but is not always sharp once the covariance constraint

\[
C\succeq0,
\qquad \operatorname{tr}C=1
\]

is retained.

This note solves the positive affine-coupling optimization exactly at fixed covariance purity/projective dispersion and shows that the Betchov-optimal strain shape does **not** require one-axis vorticity alignment.  Its hardest branch is a two-dimensional extensional-plane covariance.

---

## 1. Setup

Let

\[
S=S^T,
\qquad
\operatorname{tr}S=0,
\]

with ordered eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3.
\]

Let

\[
C\succeq0,
\qquad
\operatorname{tr}C=1.
\]

Define purity

\[
p=\operatorname{tr}(C^2)
\in[1/3,1]
\]

and projective dispersion

\[
\boxed{J=1-p\in[0,2/3].}
\]

We seek

\[
\boxed{
M_S(p)
=\max
\{\operatorname{tr}(SC):C\succeq0,\operatorname{tr}C=1,\operatorname{tr}C^2=p\}.
}
\]

---

## 2. Eigenframes align at the maximizer

For fixed eigenvalues of `C`, von Neumann's trace inequality implies that the maximum of

\[
\operatorname{tr}(SC)
\]

is obtained when `C` and `S` commute and their ordered eigenvalues are paired in the same order.

Thus write

\[
C=\operatorname{diag}(c_1,c_2,c_3)
\]

in the strain eigenframe, with

\[
c_i\ge0,
\qquad
c_1+c_2+c_3=1,
\qquad
c_1^2+c_2^2+c_3^2=p.
\]

The problem becomes

\[
\max \sum_i\lambda_i c_i.
\]

---

## 3. Interior optimizer

Ignoring positivity temporarily, the intersection of

\[
\sum_i c_i=1
\]

with the purity sphere is centered at

\[
(1/3,1/3,1/3).
\]

Because

\[
\lambda_1+\lambda_2+\lambda_3=0,
\]

the maximizing direction in this plane is the eigenvalue vector itself.

Hence the interior candidate is

\[
\boxed{
c_i=\frac13+\alpha\lambda_i,}
\]

where

\[
\boxed{
\alpha
=\sqrt{
\frac{p-1/3}{|S|_F^2}
}.
}
\]

The corresponding maximum is

\[
\boxed{
M_S(p)
=|S|_F\sqrt{p-1/3}
=|S|_F\sqrt{\frac23-J}.
}
\]

This reproduces the previous Frobenius/projective bound, but only while all `c_i` remain nonnegative.

---

## 4. Positivity threshold

The first component to hit zero is `c_1`, because `lambda_1` is the smallest eigenvalue.

The interior solution is admissible while

\[
\frac13+\alpha\lambda_1\ge0.
\]

The threshold purity is therefore

\[
\boxed{
p_0
=\frac13+rac{|S|_F^2}{9\lambda_1^2}
}
\]

when `lambda_1<0`.

Equivalently,

\[
\boxed{
J_0
=1-p_0
=\frac23-rac{|S|_F^2}{9\lambda_1^2}.
}
\]

For

\[
p\le p_0
\quad (J\ge J_0),
\]

the Frobenius/projective formula is sharp.

---

## 5. Boundary optimizer after the compressive covariance eigenvalue vanishes

For

\[
p\ge p_0,
\]

the maximizer lies on

\[
c_1=0.
\]

Then

\[
c_2+c_3=1,
\qquad
c_2^2+c_3^2=p,
\]

so

\[
\boxed{
c_3=\frac{1+\sqrt{2p-1}}2,}
\]

\[
\boxed{
c_2=\frac{1-\sqrt{2p-1}}2.}
\]

Therefore

\[
\boxed{
M_S(p)
=\frac{\lambda_2+\lambda_3}{2}
+\frac{\lambda_3-\lambda_2}{2}
\sqrt{2p-1}.
}
\]

Since `tr S=0`,

\[
\lambda_2+\lambda_3=-\lambda_1.
\]

In terms of projective dispersion,

\[
\boxed{
M_S(J)
=-\frac{\lambda_1}{2}
+\frac{\lambda_3-\lambda_2}{2}
\sqrt{1-2J}
}
\]

on the boundary branch.

At `J=0`, this gives

\[
M_S(0)=\lambda_3,
\]

as required by the elementary trace-one PSD bound.

---

## 6. Betchov-optimal strain shape

For positive Betchov stretching, the determinant-optimal trace-free eigenvalue shape is

\[
\boxed{
(\lambda_1,\lambda_2,\lambda_3)
=(-2a,a,a),
\qquad a>0.
}
\]

Then

\[
|S|_F=\sqrt6\,a,
\]

and

\[
p_0=1/2,
\qquad
J_0=1/2.
\]

For the interior branch `J>=1/2`,

\[
M_S(J)
=\sqrt6\,a\sqrt{\frac23-J}.
\]

For the boundary branch `0<=J<=1/2`, the two positive eigenvalues are degenerate:

\[
\lambda_2=\lambda_3=a.
\]

Hence

\[
\boxed{
M_S(J)=a
\qquad
0\le J\le1/2.
}
\]

Therefore **no further one-axis projective alignment is needed once the covariance is supported in the two-dimensional extensional plane**.

---

## 7. Direct extensional-plane formula

Let `e_1` be the compressive eigenvector for the Betchov shape and define

\[
c_1=e_1^TCe_1.
\]

Since the remaining plane has eigenvalue `a`,

\[
\begin{aligned}
\operatorname{tr}(SC)
&=-2a c_1+a(1-c_1)\\
&=a(1-3c_1).
\end{aligned}
\]

Thus exactly

\[
\boxed{
\operatorname{tr}(SC)
=a(1-3e_1^TCe_1).
}
\]

The affine coupling is maximal iff

\[
\boxed{e_1^TCe_1=0,}
\]

meaning the vorticity covariance is entirely contained in the extensional plane.

It can remain isotropic **within that plane**:

\[
C=\operatorname{diag}(0,1/2,1/2),
\]

for which

\[
J=1-(1/4+1/4)=1/2
\]

and yet

\[
\operatorname{tr}(SC)=a
\]

is already maximal.

---

## 8. Correction to the one-axis narrative

The implication

\[
\text{large affine source}
\Longrightarrow
J\to0
\]

is false for a biaxial extensional strain.

The correct hard geometry is

\[
\boxed{
\text{compressive-axis depletion}
+
\text{possible two-dimensional covariance inside the extensional plane}.
}
\]

Thus the projective scalar `J` alone does not resolve the affine near-extremizer geometry.

The state should retain at least

\[
\boxed{
(e_1^TCe_1,
\ c_2-c_3,
\ J,
\ \lambda_2/\lambda_3).
}
\]

---

## 9. Connection to the middle-eigenvalue branch

The Betchov-optimal shape has

\[
\lambda_2^+=\lambda_3=a.
\]

Therefore the hard affine near-extremizer is exactly a state with

- positive middle strain;
- two equal extensional eigenvalues;
- vorticity covariance depleted along the single compressive normal;
- no requirement that vorticity choose one axis inside the extensional plane.

This intersects directly with the existing middle-eigenvalue residual branch.

Repeated singular amplification can therefore try to survive through a **biaxial extensional-plane channel**, rather than through a one-axis projective channel.

---

## 10. Remaining target

The next rigidity problem is to determine whether a thick first-hitting core can repeatedly maintain

\[
\boxed{
\lambda_2\approx\lambda_3>0,
\qquad
\lambda_1\approx-2\lambda_3,
\qquad
 e_1^TC_Be_1\ll1
}
\]

while simultaneously satisfying

- the Cauchy I/V amplification ledger;
- local BMO residual-source bounds;
- finite viscosity/dissipation;
- derivative-covariance constraints;
- and spatial compatibility of the rotating extensional plane.

This is narrower than demanding arbitrary three-dimensional turbulence, but it is not yet excluded.

Status: **EXACT AFFINE-COVARIANCE ENVELOPE CLOSED / BIAXIAL EXTENSIONAL-PLANE BRANCH IDENTIFIED AS THE HARD AFFINE GEOMETRY**.
