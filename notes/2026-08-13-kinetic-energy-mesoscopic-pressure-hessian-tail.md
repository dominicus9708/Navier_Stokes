# Finite kinetic energy confines pressure-Hessian variation to a mesoscopic neighborhood

Date: 2026-08-13

Status: **DERIVED FAR-FIELD PRESSURE-KERNEL TAIL + SCALING AUDIT / MESOSCOPIC PRESSURE PACKING OPEN**.

The local pressure-Hessian residual self-closure leaves only a harmonic parent-scale pressure tail.  Finite kinetic energy shows that the genuinely distinguishable part of this tail cannot come from arbitrarily remote physical distances.

The important object is pressure-Hessian **variation across the dangerous core**, not a spatially constant Hessian representative.

---

## 1. Far pressure kernel

For a smooth decaying incompressible velocity,

\[
P=R_iR_j(U_iU_j)
\]

(up to the standard sign convention).  Away from the singularity, the pressure kernel is homogeneous of degree `-3`.

Therefore its Hessian kernel has degree `-5`, and one more spatial derivative has degree `-6`.

In physical variables, if the source region is at distance at least `R_phys` from a tracked point `x_*`, then

\[
\boxed{
|\nabla^2p_{\rm far}(x_*)|
\le
C R_{\rm phys}^{-5}\|u(t)\|_2^2
\le
C R_{\rm phys}^{-5}\|u_0\|_2^2.
}
\]

More importantly, for `|x-x_*|<=r_core` and a separated far source,

\[
\boxed{
|\nabla^2p_{\rm far}(x)-\nabla^2p_{\rm far}(x_*)|
\le
C r_{\rm core}R_{\rm phys}^{-6}\|u_0\|_2^2.
}
\]

No pressure principal-value issue occurs in this separated far region.

---

## 2. Terminal first-hitting scaling

Let

\[
r=W^{-1/2},
\qquad
y=(x-x_*)/r,
\qquad
P^{\rm norm}(y)=r^2p(x_*+ry).
\]

Then

\[
\nabla_y^2P^{\rm norm}=r^4\nabla_x^2p.
\]

Take a normalized parent radius `R`, corresponding physically to

\[
R_{\rm phys}=rR.
\]

Across the unit normalized dangerous core, the physical spatial separation is of order `r`.  Hence the far Hessian oscillation becomes

\[
\begin{aligned}
\operatorname{osc}_{B_1}
\nabla_y^2P_{\rm far}^{\rm norm}
&\le
Cr^4\,r\,(rR)^{-6}\|u_0\|_2^2\\
&=
Cr^{-1}R^{-6}\|u_0\|_2^2.
\end{aligned}
\]

Since `r^{-1}=W^{1/2}`,

\[
\boxed{
\operatorname{osc}_{B_1}
\nabla_y^2P_{\rm far}^{\rm norm}
\le
C W^{1/2}\|u_0\|_2^2R^{-6}.
}
\]

---

## 3. Mesoscopic cutoff exponent

Choose

\[
R(W)=W^\theta.
\]

Then

\[
W^{1/2}R(W)^{-6}
=W^{1/2-6\theta}.
\]

Therefore

\[
\boxed{
\theta>\frac1{12}
\Longrightarrow
\operatorname{osc}_{B_1}
\nabla_y^2P_{\rm far}^{\rm norm}
\to0.
}
\]

At the same time the corresponding physical parent radius is

\[
rR(W)=W^{-1/2+\theta}.
\]

For any

\[
\frac1{12}<\theta<\frac12,
\]

this physical radius still tends to zero.

Thus all pressure-Hessian variation capable of affecting the unit dangerous core at order one must be generated inside a physical neighborhood that shrinks to the candidate singular point.

---

## 4. Absolute far Hessian versus distinguishable variation

The absolute normalized far Hessian satisfies

\[
|\nabla_y^2P_{\rm far}^{\rm norm}|
\le
Cr^4(rR)^{-5}\|u_0\|_2^2
=
CW^{1/2}R^{-5}\|u_0\|_2^2.
\]

Thus absolute far Hessian becomes small for `theta>1/10`.

However a spatially constant Hessian is already part of the low-dimensional affine/pressure representative and does not contribute to the Gaussian pressure-Hessian variance.

For residual/eigenframe forcing, the relevant threshold is therefore the sharper variation exponent

\[
\boxed{\theta>1/12.}
\]

---

## 5. Pressure scale-escalation ladder is finite at each first-hitting level

Start from unit normalized scale and enlarge parent radii dyadically until

\[
R_N\asymp W^{1/12+\varepsilon}.
\]

The number of parent steps is

\[
\boxed{N=O(\log W).}
\]

Beyond this radius the pressure-Hessian variation from the remaining exterior is `o(1)`.

Therefore persistent child pressure forcing must be resolved on one of only `O(log W)` mesoscopic parent levels, rather than escaping to arbitrarily remote physical space.

This is not yet a contradiction: an `O(log W)` scale ladder can still be compatible with critical concentration.

---

## 6. Combined pressure route

Together with the local pressure-residual self-closure:

\[
\boxed{
\text{pressure-Hessian variation at child scale}
}
\]

must be either

\[
\boxed{
\text{generated locally by }L\times B+B\times B
}
\]

or

\[
\boxed{
\text{resolved at a mesoscopic parent scale}
}
\]

before normalized radius `W^(1/12+epsilon)`.

The fully remote exterior is negligible in pressure-Hessian variation by kinetic energy.

---

## 7. DSD interpretation

Pressure nonlocality does not force whole-space high-resolution bookkeeping.

At the resolution of a unit dangerous core, pressure information beyond the mesoscopic radius contributes only an almost common Hessian field.  Its distinguishable variation vanishes.

Thus the pressure search domain is reduced to a shrinking physical neighborhood with `O(log W)` parent resolutions.

Status: **REMOTE PRESSURE-HESSIAN VARIATION PRUNED / FINITE MESOSCOPIC SCALE-LADDER PACKING REMAINS OPEN**.
