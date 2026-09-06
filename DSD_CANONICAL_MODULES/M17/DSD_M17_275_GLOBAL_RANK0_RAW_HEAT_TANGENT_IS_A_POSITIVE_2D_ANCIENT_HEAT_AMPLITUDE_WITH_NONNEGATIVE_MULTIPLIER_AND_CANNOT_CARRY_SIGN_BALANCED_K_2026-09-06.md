# DSD M17-275 — A global Rank-0 raw heat tangent is a positive 2D ancient heat amplitude with nonnegative multiplier and cannot carry sign-balanced K

Date: 2026-09-06  
Canonical ID: **M17-275**

Status: **GLOBAL RANK-0 CLOSURE / M17-273 PRODUCES A RANK-0 DIRECTOR TANGENT WHEN BOTH DIRECTOR SINGULAR VALUES COLLAPSE. ON A CONNECTED GLOBAL RANK-0 ACTIVE TANGENT, `grad xi=0`, SO `xi=xi_0` IS A FIXED UNIT VECTOR AND `V=a xi_0` WITH `a=|V|>=0`. DIVERGENCE-FREE VORTICITY GIVES `D_{xi_0} a=0`, REDUCING THE AMPLITUDE TO TWO TRANSVERSE SPATIAL VARIABLES. THE RAW HEAT EQUATION BECOMES THE SCALAR 2D HEAT EQUATION `a_tau=Delta_perp a`, AND `K=a_tau/a`. FOR A NONTRIVIAL ENTIRE NONNEGATIVE ANCIENT HEAT SOLUTION, THE POSITIVE-ANCIENT REPRESENTATION THEOREM OF LIN--ZHANG (CPAM 72 (2019), 2006--2028, DOI 10.1002/cpa.21820; arXiv:1712.04091) REPRESENTS `a` AS A POSITIVE LAPLACE TRANSFORM OF POSITIVE EIGENFUNCTIONS `Delta h=s h`, `s>=0`. CONSEQUENTLY `a_tau>=0` AND `K>=0` WHERE `a>0`. THIS CONTRADICTS THE BOUNDED-SPIKE CRITICAL K SURVIVOR FROM M17-233/234/239, WHICH REQUIRES POSITIVE AND NEGATIVE K POPULATIONS AFTER THE SMALL-SIGNED-MEAN GATE. THUS A GLOBAL ENTIRE NONTRIVIAL RANK-0 RAW HEAT TANGENT CANNOT BE THAT SURVIVOR. LOCAL RANK-0 PATCHES REMAIN INTERFACE/EXTENSION PROBLEMS AND ARE NOT CLOSED BY THIS THEOREM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rank-0 director

Assume on the entire nonzero tangent component

\[
\boxed{D\xi=0.}
\]

Then

\[
\boxed{\xi\equiv\xi_0}
\]

for one constant unit vector.

Write

\[
\boxed{V=a\xi_0,\qquad a=|V|\ge0.}
\]

On a nontrivial active component, the heat strong maximum principle makes the scalar amplitude positive after excluding the identically-zero solution.

---

## 2. Divergence-free reduction to two dimensions

Because the vorticity tangent is divergence free,

\[
0=\nabla\cdot V
=\xi_0\cdot\nabla a.
\]

Thus

\[
\boxed{D_{\xi_0}a=0.}
\]

Choose coordinates so that

\[
\xi_0=e_3.
\]

Then

\[
\boxed{a=a(x_1,x_2,\tau).}
\]

No dependence on `x_3` remains.

---

## 3. Scalar ancient heat equation

The raw tangent satisfies

\[
\partial_\tau V=\Delta V.
\]

Since `xi_0` is constant,

\[
\boxed{
\partial_\tau a
=\Delta_\perp a,
}
\]

where

\[
\Delta_\perp=\partial_1^2+\partial_2^2.
\]

The inherited CE-H relation

\[
\Delta V=K V
\]

becomes

\[
\boxed{
K=\frac{\Delta_\perp a}{a}
=\frac{\partial_\tau a}{a}
=\partial_\tau\log a.
}
\]

---

## 4. Positive ancient heat representation

For positive ancient solutions of the heat equation on Euclidean space, Lin and Zhang prove an explicit representation as a standard Laplace transform of positive solutions of the elliptic family

\[
\Delta h=s h,
\qquad s>0,
\]

with the stationary `s=0` component included in the limiting measure.

Reference:

F. Lin and Q. S. Zhang, *On Ancient Solutions of the Heat Equation*, Communications on Pure and Applied Mathematics **72** (2019), 2006--2028. DOI: `10.1002/cpa.21820`. arXiv: `1712.04091`.

Schematically the Euclidean representation has the form

\[
\boxed{
a(x,\tau)=\int_{[0,\infty)}e^{s\tau}h_s(x)\,d\mu(s),
\qquad h_s(x)>0,
\qquad \mu\ge0.
}
\]

The theorem is invoked only on the **global entire positive ancient** Rank-0 branch.

---

## 5. Time monotonicity

Differentiate the positive representation:

\[
\partial_\tau a
=
\int_{[0,\infty)}s e^{s\tau}h_s(x)\,d\mu(s).
\]

Every integrand is nonnegative.
Therefore

\[
\boxed{\partial_\tau a\ge0.}
\]

Since `a>0`,

\[
\boxed{K=\partial_\tau\log a\ge0.}
\]

This is a pointwise sign conclusion for the global Rank-0 positive ancient tangent.

---

## 6. Conflict with the critical sign-balanced K survivor

On the bounded-spike coefficient branch, M17-233 gives nonvanishing critical `|K|^(3/2)` occupancy after intrinsic scaling.

M17-234/239 add the small signed-mean and bounded-`K` information, forcing retained positive and negative multiplier populations rather than a one-sign nonnegative multiplier.

Thus the Rank-0 conclusion

\[
K\ge0
\]

is incompatible with that survivor.

Hence

\[
\boxed{
H_{global\ entire\ Rank0\ raw\ heat\ tangent}
\Longrightarrow\bot
}
\]

on the critical sign-balanced `K` branch.

---

## 7. Scope firewall

This theorem does **not** close a merely local Rank-0 patch.

If the Rank-0 component ends at a finite spatial boundary, rank interface, nodal set, or another tangent component, the global positive-ancient representation theorem cannot be applied across that boundary.

Therefore

\[
\boxed{
G_{local\ Rank0}
\Longrightarrow
G_{rank/interface/extension}
}
\]

unless global continuation is separately proved.

Likewise, a sign-changing scalar amplitude is not admitted by the polar definition `a=|V|`; orientation reversal passes through `V=0` and belongs to the nodal branch.

---

## 8. DSD audit

- The external positive-ancient representation theorem is used only under its global Euclidean positivity hypothesis.
- Rank-0 locality is not silently promoted to an entire solution.
- Divergence-free reduction to two dimensions is exact.
- The sign conclusion concerns `K=a_tau/a`, not the original unscaled physical multiplier outside the tangent limit.
- The contradiction uses the already retained sign-balanced bounded-spike `K` survivor.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
