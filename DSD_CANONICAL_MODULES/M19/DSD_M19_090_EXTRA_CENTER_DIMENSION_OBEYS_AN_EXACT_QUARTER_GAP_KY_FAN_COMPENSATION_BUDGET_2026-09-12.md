# DSD M19-090 — Extra-center dimension obeys an exact quarter-gap Ky-Fan compensation budget

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / FINITE-DIMENSIONAL CENTER TRACE IDENTITY / QUARTER-GAP COMPENSATION BUDGET / KY-FAN CRITERION FOR EXCLUDING EXTRA CENTER / CURRENT CORRIDOR DOES NOT YET SUPPLY THE REQUIRED STRICT NUMERICAL BOUND / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Assume the M19-088 quasi-compactness bookkeeping has been completed so that, after quotienting exact rotations, the center bundle is finite-dimensional.

Write

\[
E^c_q
=\operatorname{span}\{\partial_\theta U\}
\oplus E^c_{extra}.
\]

Let

\[
m:=\dim E^c_{extra}.
\]

The objective is to derive a necessary quantitative condition for `m>=1`.

---

## 2. Vorticity quadratic form

For a perturbation velocity `W` with vorticity

\[
\eta=\nabla\times W,
\]

M19-087 gives

\[
\frac12\frac d{d\theta}\|\eta\|_2^2
= -\nu\|\nabla\eta\|_2^2
-\frac14\|\eta\|_2^2
+\mathcal C_U[W].
\]

On the vorticity Hilbert space define the symmetric compensation quadratic form

\[
\boxed{
\mathfrak k_U(\eta)
:=\mathcal C_U[\mathcal K_{BS}\eta],
}
\]

where `K_BS` reconstructs the divergence-free velocity perturbation from its vorticity.

Only the symmetric part of the linearized background operator contributes to this quadratic form.

---

## 3. Moving orthonormal frame in the extra center

Choose an `L^2`-orthonormal frame

\[
\eta_1(\theta),\ldots,\eta_m(\theta)
\]

for `E^c_extra(theta)`.

The frame may be maintained by a skew connection; the connection has zero trace and therefore does not alter the logarithmic growth of the `m`-volume.

The sum of the `m` center Lyapunov exponents is therefore the long-time average of the trace of the symmetric generator on this frame.

Since every direction lies in the zero center,

\[
\lambda_1+\cdots+\lambda_m=0.
\]

---

## 4. Exact center-volume budget

Summing the M19-087 identity over the orthonormal frame gives

\[
\begin{aligned}
0
={}&
-\frac m4
-\nu\left\langle
\sum_{j=1}^m\|\nabla\eta_j\|_2^2
\right\rangle\\
&+
\left\langle
\sum_{j=1}^m\mathfrak k_U(\eta_j)
\right\rangle.
\end{aligned}
\]

Hence

\[
\boxed{
\left\langle
\sum_{j=1}^m\mathfrak k_U(\eta_j)
\right\rangle
=
\frac m4
+\nu\left\langle
\sum_{j=1}^m\|\nabla\eta_j\|_2^2
\right\rangle
\ge\frac m4.
}
\]

Thus every extra center dimension costs at least one quarter-unit of persistent average compensation, before paying any perturbation palinstrophy.

---

## 5. Transverse Ky-Fan envelope

Let `K_U^s(theta)` denote the symmetric operator/form associated with `k_U`, restricted to the symmetry-transverse vorticity fiber after time/rotation modulation.

Let

\[
\kappa_1^\perp(\theta)
\ge
\kappa_2^\perp(\theta)
\ge\cdots
\]

be its positive discrete eigenvalues when the compact-core realization is used. More generally, interpret their partial sums as the Ky-Fan variational values of the symmetry-transverse form.

For every orthonormal `m`-frame,

\[
\sum_{j=1}^m\mathfrak k_U(\eta_j)
\le
\sum_{j=1}^m\kappa_j^\perp(\theta).
\]

Therefore existence of an `m`-dimensional extra center requires

\[
\boxed{
\left\langle
\sum_{j=1}^m\kappa_j^\perp
\right\rangle
\ge
\frac m4
+\nu\left\langle
\sum_{j=1}^m\|\nabla\eta_j\|_2^2
\right\rangle.
}
\]

In particular,

\[
\boxed{
E^c_{extra}\neq0
\Longrightarrow
\left\langle\kappa_1^\perp\right\rangle\ge\frac14
}
\]

up to the additional positive perturbation-palinstrophy term.

---

## 6. A sufficient exclusion criterion

A direct sufficient criterion for factor rigidity is therefore

\[
\boxed{
\left\langle\kappa_1^\perp\right\rangle<\frac14.
}
\]

More sharply, if for every transverse complete projective trajectory

\[
\left\langle
\mathfrak k_U(\eta)
-\nu\|\nabla\eta\|_2^2
\right\rangle
<\frac14,
\]

then no extra zero center exists.

Combined with M19-089,

\[
\boxed{
\text{transverse compensation below the quarter-gap}
\Longrightarrow
E^c_{extra}=0
\Longrightarrow
\text{no aperiodic weak-critical factor}.
}
\]

---

## 7. Relation to M19-071 and M19-080

M19-071 attempted a two-volume estimate before the far-field center had been reduced to a finite-dimensional core-observable bundle. It could not exploit a fixed finite-dimensional spectral trace and gained no cancellation.

M19-080 showed that trace-free strain alone cannot prevent two perturbations from receiving positive work.

M19-090 does not contradict those results.

It replaces pointwise strain-sign heuristics by a finite-dimensional spectral budget:

\[
\boxed{
\text{extra center dimension}
\Longrightarrow
\text{large positive transverse compensation spectrum}.
}
\]

---

## 8. Crude norm bound and why it is not yet enough

The compensation form can be estimated schematically by

\[
|\mathfrak k_U(\eta)|
\lesssim
\|S_U\|_{\mathcal X}\|\eta\|_2^2
+\|\Omega\|_{\mathcal Y}\|\eta\|_2^2
+\|\nabla\Omega\|_{L^3}\|\eta\|_2^2
\]

for appropriate retained smooth-corridor norms `X,Y`.

The present W1/compact corridor gives finiteness of these quantities, not a universal strict bound below `1/4` on the symmetry-transverse Ky-Fan value.

Therefore the module yields an exact target but not analytic closure.

---

## 9. New precise theorem target

The dominant analytic question can now be written as

\[
\boxed{
\mathcal T_{quarter}:
\left\langle\kappa_1^\perp\right\rangle<\frac14
\quad\text{on every nontrivial recurrent controlled survivor}.
}
\]

Any proof may use more structure than a crude operator norm: CE-H geometry where applicable, recurrence identities, alignment information, sign cancellation, or an exact compact-core trace formula.

Conversely, if the inequality can fail, the failure identifies an explicit interior spectral object carrying the aperiodic factor.

---

## 10. Firewall

The base enstrophy identity

\[
\frac{\langle\int\Omega\cdot S\Omega\rangle}{\langle\|\Omega\|_2^2\rangle}
\ge\frac14
\]

is not the same as

\[
\langle\kappa_1^\perp\rangle\ge\frac14.
\]

The first concerns the base vorticity direction; the second concerns the largest symmetry-transverse linearized compensation direction.

They must not be identified.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
