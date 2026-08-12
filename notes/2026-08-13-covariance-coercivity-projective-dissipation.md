# Covariance coercivity: next-order projective dissipation controls the current defect quadratically

Date: 2026-08-13

Status: **DERIVED SHARP-ORDER COVARIANCE COERCIVITY + STRENGTHENED PROJECTIVE DISSIPATION / GLOBAL REGULARITY NOT PROVED**.

This note proves a purely finite-dimensional matrix inequality that removes an important degeneracy from the energy-weighted projective dissipation law.

For any two positive semidefinite trace-one `3 x 3` covariance matrices `C` and `D`, the combination

\[
J(D)+\|D-C\|_F^2
\]

controls the square of the projective defect of `C`.

## 1. Notation

Let

\[
C\succeq0,
\qquad
\operatorname{tr}C=1,
\]

with eigenvalues

\[
\mu_1\ge\mu_2\ge\mu_3\ge0.
\]

Define

\[
\Pi=1-\mu_1=\mu_2+\mu_3,
\]

and

\[
J(C)=1-\operatorname{tr}(C^2).
\]

Let `D` be any other positive semidefinite trace-one matrix and define

\[
J(D)=1-\operatorname{tr}(D^2),
\qquad
\Delta^2=\|D-C\|_F^2.
\]

## 2. First lower bound: optimize over the next covariance

Expand

\[
\begin{aligned}
J(D)+\Delta^2
&=1-\operatorname{tr}(D^2)
+\operatorname{tr}(D^2)+\operatorname{tr}(C^2)
-2\operatorname{tr}(CD)\\
&=1+\operatorname{tr}(C^2)-2\operatorname{tr}(CD).
\end{aligned}
\]

Because `D` is positive semidefinite with trace one,

\[
\operatorname{tr}(CD)\le\mu_1(C).
\]

The maximum is attained by the rank-one projector onto a principal eigenvector of `C`.

Therefore

\[
\boxed{
J(D)+\|D-C\|_F^2
\ge
1+\operatorname{tr}(C^2)-2\mu_1.
}
\]

Since

\[
\operatorname{tr}(C^2)=1-J(C),
\qquad
\mu_1=1-\Pi,
\]

this becomes

\[
\boxed{
J(D)+\|D-C\|_F^2
\ge
2\Pi-J(C).
}
\]

This first bound is exact with respect to the optimization over `D`.

## 3. Lower bound by the square of the current projective defect

Write

\[
q=\mu_2\mu_3.
\]

Because

\[
\mu_2+\mu_3=\Pi,
\]

we have

\[
q\le\frac{\Pi^2}{4}.
\]

Also

\[
J(C)
=2\Pi(1-\Pi)+2q.
\]

Hence

\[
\begin{aligned}
2\Pi-J(C)
&=2\Pi^2-2q\\
&\ge2\Pi^2-\frac12\Pi^2\\
&=\frac32\Pi^2.
\end{aligned}
\]

The elementary bound

\[
J(C)\le2\Pi
\]

then gives

\[
\Pi^2\ge\frac14J(C)^2.
\]

Therefore

\[
\boxed{
2\Pi-J(C)
\ge
\frac38J(C)^2.
}
\]

Combining the steps,

\[
\boxed{
J(D)+\|D-C\|_F^2
\ge
2\Pi-J(C)
\ge
\frac38J(C)^2.
}
\]

The coefficient `3/8` has the correct small-defect sharp order: for spectra approaching `(1-epsilon, epsilon/2, epsilon/2)`, the ratio of the left optimized defect to `J(C)^2` approaches `3/8`.

## 4. Apply to the derivative covariance chain

Set

\[
C=C_k,
\qquad
D=C_{k+1}.
\]

Then

\[
\boxed{
J_{k+1}+\Delta_k^2
\ge
\frac38J_k^2.
}
\]

The energy-weighted projective identity was

\[
\dot D_k
+2\nu E_{k+1}
(J_{k+1}+\Delta_k^2)
\le
2\sqrt5\sqrt{D_k}\mathcal F_k,
\]

with

\[
D_k=E_kJ_k.
\]

Therefore

\[
\boxed{
\dot D_k
+\frac{3\nu}{4}E_{k+1}J_k^2
\le
2\sqrt5\sqrt{D_k}\mathcal F_k.
}
\]

This lower bound depends only on the **current** projective defect `J_k`; no favorable assumption on the next covariance is required.

## 5. Square-root form

Where `D_k>0`, divide by `2 sqrt(D_k)`:

\[
\boxed{
\frac d{dt}\sqrt{D_k}
+
\frac{3\nu}{8}
\frac{E_{k+1}J_k^2}{\sqrt{D_k}}
\le
\sqrt5\mathcal F_k.
}
\]

Since

\[
D_k=E_kJ_k,
\qquad
r_k=E_{k+1}/E_k,
\]

we can rewrite the damping term as

\[
\frac{E_{k+1}J_k^2}{\sqrt{D_k}}
=r_kJ_k\sqrt{D_k}.
\]

Thus

\[
\boxed{
\frac d{dt}\sqrt{D_k}
+
\frac{3\nu}{8}r_kJ_k\sqrt{D_k}
\le
\sqrt5\mathcal F_k.
}
\]

The natural damping rate is therefore

\[
\boxed{\nu r_kJ_k.}
\]

After factorial normalization,

\[
r_k=(k+1)^2\rho_k,
\]

so the rate becomes

\[
\boxed{
\nu(k+1)^2\rho_kJ_k.
}
\]

## 6. What this removes

Previously, the projective viscous term appeared to depend on whether `C_{k+1}` happened to be sufficiently multi-axis or sufficiently different from `C_k`.

The coercivity estimate shows that these possibilities cannot jointly suppress dissipation below quadratic order in `J_k`.

If `C_{k+1}` becomes nearly rank one to make `J_{k+1}` small, it must approach the best rank-one approximation of `C_k`; the mismatch term then pays the remaining geometric cost.

Thus

\[
\boxed{
J_k>0
\Longrightarrow
\text{strict projective viscous cost at order }E_{k+1}J_k^2.
}
\]

## 7. What remains open

The coercive term degenerates quadratically as `J_k -> 0`, while the nonlinear source bound degenerates only like `sqrt(J_k)` through `sqrt(D_k)`.

Therefore the small-projective-defect regime still needs a separate mechanism. At `k=0`, the external locally anisotropic vorticity criterion can exploit sufficiently strong one-axis behavior. At `k>=1`, a direct transfer from high-derivative covariance alignment to a known regularity criterion has not yet been established.

The next target is to combine

\[
\frac{3\nu}{4}E_{k+1}J_k^2
\]

with the factorial forcing convolution and, at base order, with the local pairwise projective geometry of vortex stretching.

Status: **OPEN SMALL-J / NONLINEAR SOURCE CLOSURE**.
