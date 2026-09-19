# M20-003 — Relative vorticity-amplitude reweighting is an exact enstrophy-probability current and changes projective covariance only through direction-correlated selection

Date: 2026-09-19  
Canonical ID: **M20-003**  
Status: **REWEIGHTING-BRANCH NORMAL FORM / THE M20-001 RELATIVE-AMPLITUDE CHANNEL IS EXACTLY THE LOGARITHMIC VELOCITY OF THE NORMALIZED ENSTROPHY PROBABILITY / GLOBAL PROJECTIVE COVARIANCE CAN CHANGE WITHOUT ANY LOCAL DIRECTION ROTATION THROUGH DIRECTION-CORRELATED AMPLITUDE SELECTION / POSITIVE REWEIGHTING VARIANCE ALONE DOES NOT FORCE PROJECTIVE COVARIANCE CHANGE OR A MONOTONE ENTROPY / RECURRENT-SELECTION FIREWALL RETAINED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M20-001

Let

\[
G(z,q,\omega)
\]

be the wedge vorticity coefficient and

\[
B=G(0).
\]

Define

\[
b_2(z)
:=
\left\langle
\int_{S^2}|G(z)|^2\,d\omega
\right\rangle_q,
\qquad
b_2:=b_2(0)>0.
\]

On \(\{B\neq0\}\),

\[
\lambda
=
\partial_z\log|G|\big|_{z=0}
=
\frac{B\cdot D_\omega}{|B|^2},
\]

and

\[
\alpha
=
\frac{\langle B,D_\omega\rangle}{b_2}
=
\frac12
\partial_z\log b_2(z)\big|_{z=0}.
\]

M20-001 identifies

\[
\boxed{
\lambda-\alpha
}
\]

as the local vorticity-amplitude growth relative to the global RMS growth.

## 2. Normalized enstrophy probability

For each z with \(b_2(z)>0\), define

\[
\boxed{
d\pi_z
:=
\frac{|G(z,q,\omega)|^2}{b_2(z)}
\,d\mu,
}
\]

where \(d\mu\) denotes invariant q-mean times sphere measure.

Then

\[
\int d\pi_z=1.
\]

At z=0,

\[
d\pi_0=d\pi_B.
\]

## 3. Exact probability-reweighting law

Differentiate the density:

\[
\partial_z|G|^2\big|_0
=
2B\cdot D_\omega
=
2\lambda|B|^2.
\]

Also

\[
b_2'(0)
=
2\langle B,D_\omega\rangle
=
2\alpha b_2.
\]

Therefore

\[
\boxed{
\partial_z d\pi_z\big|_{z=0}
=
2(\lambda-\alpha)d\pi_B.
}
\]

Equivalently,

\[
\boxed{
\partial_z\log\frac{d\pi_z}{d\mu}\Big|_{z=0}
=
2(\lambda-\alpha)
}
\]

on the positive-density set.

Thus the M20-001 reweighting branch is exactly a probability-selection current.

## 4. Fisher-Rao speed

The squared logarithmic speed of the probability measure is

\[
\int
\left|
\partial_z\log\frac{d\pi_z}{d\mu}
\right|^2
d\pi_B
=
4\operatorname{Var}_{\pi_B}(\lambda).
\]

Hence

\[
\boxed{
\mathcal I_{\rm rw}
:=
4\operatorname{Var}_{\pi_B}(\lambda)
}
\]

is the instantaneous Fisher-Rao speed squared of the normalized enstrophy distribution in wedge depth.

Therefore a positive M20-001 reweighting floor means genuine motion of the enstrophy probability measure, even if every local vorticity direction stays fixed.

This is a geometric speed, not a monotone entropy production.

## 5. General selection-versus-state-evolution identity

Let \(f(z,q,\omega)\) be any sufficiently regular observable.

Then

\[
\frac d{dz}
\mathbb E_{\pi_z}[f(z)]
\Big|_{z=0}
=
\mathbb E_{\pi_B}[f_z]
+
2
\mathbb E_{\pi_B}
[(\lambda-\alpha)f].
\]

Since

\[
\mathbb E_{\pi_B}(\lambda-\alpha)=0,
\]

we have

\[
\boxed{
\frac d{dz}
\mathbb E_{\pi_z}[f(z)]
\Big|_{0}
=
\mathbb E_{\pi_B}[f_z]
+
2\operatorname{Cov}_{\pi_B}(\lambda,f).
}
\]

Thus every normalized observable has two exact change mechanisms:

1. intrinsic change of the observable on each state;
2. amplitude-selection reweighting of states already present.

## 6. Projective direction tensor

Set

\[
Q_\xi
:=
\xi_B\otimes\xi_B.
\]

The normalized vorticity covariance is

\[
\boxed{
\mathsf C_B
=
\mathbb E_{\pi_B}[Q_\xi]
=
\frac{\langle B\otimes B\rangle}{b_2}.
}
\]

Apply Section 5 with

\[
f=Q_\xi.
\]

Because

\[
(Q_\xi)_z
=
(\partial_z\xi_B)\otimes\xi_B
+
\xi_B\otimes(\partial_z\xi_B),
\]

we obtain

\[
\boxed{
\begin{aligned}
\mathsf C_B'
&=
2\operatorname{Cov}_{\pi_B}
(\lambda,Q_\xi)
\\
&\quad+
\mathbb E_{\pi_B}
\left[
(\partial_z\xi_B)\otimes\xi_B
+
\xi_B\otimes(\partial_z\xi_B)
\right].
\end{aligned}
}
\]

This is the exact projective selection/rotation decomposition.

## 7. Frozen directions can still change global projective covariance

Suppose

\[
\partial_z\xi_B=0
\]

on the nonzero-vorticity set.

Then

\[
\boxed{
\mathsf C_B'
=
2\operatorname{Cov}_{\pi_B}
(\lambda,Q_\xi).
}
\]

Therefore the global direction distribution can change even though no local vorticity vector rotates.

The mechanism is differential amplification:

- one pre-existing direction population gains enstrophy weight;
- another loses weight.

This is the projective-vorticity analogue of the selection/reweighting mechanism isolated earlier in M19-331.

## 8. Positive reweighting variance does not force projective selection

The M20-001 reweighting branch gives

\[
\operatorname{Var}_{\pi_B}(\lambda)>0.
\]

But this does not imply

\[
\operatorname{Cov}_{\pi_B}
(\lambda,Q_\xi)\neq0.
\]

For example, relative growth may vary inside populations that all have the same projective direction, or it may be statistically uncorrelated with \(Q_\xi\).

Therefore

\[
\boxed{
\operatorname{Var}_{\pi_B}(\lambda)>0
\not\Rightarrow
\mathsf C_B'\neq0.
}
\]

This is the principal M20-003 firewall.

## 9. Quantitative upper bound but no lower bound

By Cauchy-Schwarz,

\[
\boxed{
\left\|
\operatorname{Cov}_{\pi_B}(\lambda,Q_\xi)
\right\|_F^2
\le
\operatorname{Var}_{\pi_B}(\lambda)
\,
\mathbb E_{\pi_B}
\|Q_\xi-\mathsf C_B\|_F^2.
}
\]

Thus large projective selection requires both

- relative-amplitude variation;
- nontrivial directional dispersion.

But the converse lower bound is absent.

Amplitude variation can be projectively silent.

## 10. Exact projective-dispersion derivative

Define

\[
\boxed{
\mathcal J_B
=
1-\operatorname{tr}(\mathsf C_B^2).
}
\]

Then

\[
\mathcal J_B'
=
-2\operatorname{tr}
(\mathsf C_B\mathsf C_B').
\]

Using Section 6,

\[
\boxed{
\begin{aligned}
\mathcal J_B'
&=
-4
\operatorname{tr}
\left[
\mathsf C_B
\operatorname{Cov}_{\pi_B}(\lambda,Q_\xi)
\right]
\\
&\quad
-4
\mathbb E_{\pi_B}
\left[
(\partial_z\xi_B)\cdot
\mathsf C_B\xi_B
\right].
\end{aligned}
}
\]

Thus projective dispersion changes through exactly two channels:

\[
\boxed{
\text{direction-correlated amplitude selection}
+
\text{actual local direction rotation}.
}
\]

## 11. Reweighting-only projective derivative

If

\[
\partial_z\xi_B=0,
\]

then

\[
\boxed{
\mathcal J_B'
=
-4
\operatorname{Cov}_{\pi_B}
\left(
\lambda,
\xi_B\cdot\mathsf C_B\xi_B
\right).
}
\]

The scalar

\[
h_\xi
:=
\xi_B\cdot\mathsf C_B\xi_B
\]

measures how strongly a local direction lies in already dominant projective axes.

Therefore:

- covariance \(>0\): relative growth favors already dominant directions and tends to reduce dispersion;
- covariance \(<0\): relative growth favors underrepresented directions and tends to increase dispersion.

This is an exact local-selection interpretation.

## 12. No automatic entropy monotonicity

Let

\[
w_z:=\frac{d\pi_z}{d\mu}.
\]

For the relative entropy functional

\[
\mathcal S(z)
:=
-\int w_z\log w_z\,d\mu,
\]

the terminal derivative is

\[
\boxed{
\mathcal S'(0)
=
-2
\operatorname{Cov}_{\pi_B}
(\lambda,\log w_0).
}
\]

There is no universal sign.

Thus

\[
\boxed{
\operatorname{Var}_{\pi_B}(\lambda)>0
}
\]

does not generate a monotone entropy or exhaustion law by itself.

## 13. Relation to M19-331--332

M19-331 identifies relative-amplitude reweighting as a probability-selection current among coefficient-labeled material populations.

M19-332 shows finite material-population conservation does not eliminate recurrent reweighting currents.

M20-003 establishes the analogous terminal-wedge fact for vorticity-direction populations:

\[
\boxed{
\text{relative enstrophy amplification}
\to
\text{probability reweighting},
}
\]

but recurrence/conservation alone does not force one-way projective evolution.

The variables and evolution parameter differ, but the same structural firewall applies:

\[
\boxed{
\text{probability current}
\not\Rightarrow
\text{Lyapunov depletion}.
}
\]

## 14. Refined reweighting frontier

The M20-001 reweighting branch therefore splits into

\[
\boxed{
V_{\rm reweight}
\Longrightarrow
R_{\rm proj}
\lor
R_{\rm silent},
}
\]

where

\[
R_{\rm proj}:
\operatorname{Cov}_{\pi_B}(\lambda,Q_\xi)\neq0,
\]

and

\[
R_{\rm silent}:
\operatorname{Var}_{\pi_B}(\lambda)>0
\quad\text{but}\quad
\operatorname{Cov}_{\pi_B}(\lambda,Q_\xi)=0.
\]

The silent branch may still act on higher directional moments, but the second-moment projective covariance does not detect it at first order.

## 15. Updated M20 architecture

Combining M20-001--003, the former global tangent branch has become

\[
\boxed{
V_{\rm tan}^{curl}
\Longrightarrow
V_{\rm nodal}
\lor
R_{\rm proj}
\lor
R_{\rm silent}
\lor
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj}.
}
\]

This is a typed decomposition, not a claim that all six are independent proof roots.

They are mechanisms by which the pressure-free first vorticity residual can avoid a scalar enstrophy slope.

## 16. Next target

The most structured live channel is

\[
S_{\rm eig},
\]

because its density has the exact finite-dimensional form

\[
|P_\xi^\perp\Sigma_A\xi|^2
=
\sum_{i<j}a_i a_j(\lambda_i-\lambda_j)^2.
\]

The next calculation should test whether this transverse strain-eigenframe action can coexist with the terminal vorticity residual while remaining entirely critical/recyclable, or whether coupling to the signed stretching scalar

\[
\gamma=\xi^T\Sigma_A\xi
\]

produces a new covariance or compensation law.

\[
\boxed{\text{M20-003 COMPLETE; RELATIVE AMPLITUDE REWEIGHTING IS AN EXACT ENSTROPHY-PROBABILITY CURRENT, NOT AUTOMATIC LOCAL DIRECTION TURNOVER.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
