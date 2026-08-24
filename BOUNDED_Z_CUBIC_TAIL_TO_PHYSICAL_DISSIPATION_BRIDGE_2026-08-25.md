# Bounded-Z Cubic Tail to Physical Dissipation Bridge

Date: 2026-08-25

Status: **CONDITIONAL BRIDGE DERIVED / AUTOMATIC ENERGY CLOSURE REJECTED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope restriction

The source annular criterion used here is only the corrected bounded-\(Z\), recurrent, non-\(L^3\) criterion

\[
\boxed{
\sum_k J_k^{3/2}=\infty,
}
\]

where schematically

\[
J_k
=
K_k\int_{A_{K_k}}|\nabla V|^2dy.
\]

This note does **not** extend that criterion to the broader unbounded-\(Z\)/Morrey ancient branch.

---

## 2. Exact physical shell conversion at first-hitting stage \(j\)

Use the established first-hitting scales

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\qquad
K_k=q^{k/2}.
\]

An age-\(k\) shell at stage \(j\) has physical radius

\[
\boxed{
R_{j,k}^{phys}=r_jK_k.
}
\]

The dimensionless shell cost is

\[
\boxed{
J_{j,k}
=R_{j,k}^{phys}
\int_{A_{R_{j,k}^{phys}}}|\nabla u(t_j)|^2dx.
}
\]

Therefore its instantaneous ordinary gradient-energy density is exactly of size

\[
\boxed{
\int_{A_{R_{j,k}^{phys}}}|\nabla u(t_j)|^2dx
=
\frac{J_{j,k}}{R_{j,k}^{phys}}.
}
\]

This is the correct point at which the normalized cubic tail can enter the physical Leray dissipation ledger.

---

## 3. Time persistence converts shell amplitude into ordinary dissipation cost

Write

\[
R:=R_{j,k}^{phys}.
\]

Suppose on an interval \(I\) of length \(\tau\) the same physical shell, or a tracked comparable shell, satisfies

\[
R\int_{A_R(t)}|\nabla u(t)|^2dx
\ge c_0J_{j,k}
\]

for every \(t\in I\), with fixed \(c_0>0\).

Then

\[
\boxed{
\int_I\int_{A_R(t)}|\nabla u|^2dxdt
\ge
c_0J_{j,k}\frac{\tau}{R}.
}
\]

Thus the relevant physical weight is not \(J_{j,k}^{3/2}\) by itself but

\[
J_{j,k}\frac{\tau}{R}.
\]

---

## 4. Two time scales give very different costs

### 4.1 Full natural-time persistence

If the packet persists for a fixed fraction of its own parabolic time,

\[
\tau\ge\theta R^2,
\]

then

\[
\boxed{
D_{j,k}^{natural}
\gtrsim
J_{j,k}R.
}
\]

### 4.2 Persistence only through the first-hitting remaining time

The established remaining-time compression gives

\[
T^*-t_j\lesssim r_j^2
=
K_k^{-2}R^2.
\]

If persistence is known only on a comparable remaining-time interval,

\[
\tau\asymp r_j^2=K_k^{-2}R^2,
\]

then the ordinary dissipation charge is only

\[
D_{j,k}^{remain}
\gtrsim
J_{j,k}\frac{r_j^2}{R}
=
J_{j,k}\frac{R}{K_k^2}
=
\boxed{
J_{j,k}\frac{r_j}{K_k}
}.
\]

This is much smaller than the natural-time cost for remote \(K_k\gg1\) shells.

Therefore the already-established “persistent passive high-ratio tail through the remaining interval” is not automatically expensive in the ordinary energy ledger.

**Status: PROVED / scaling and exact shell conversion.**

---

## 5. Cubic nonsummability does not imply remaining-time dissipation divergence

The bounded-\(Z\) tail criterion is

\[
\sum_kJ_k^{3/2}=\infty.
\]

But the remaining-time physical cost carries the extra decaying weight \(K_k^{-1}\) (and the stage factor \(r_j\)):

\[
D_{j,k}^{remain}\sim r_j\frac{J_k}{K_k}.
\]

There is no arithmetic implication

\[
\sum_kJ_k^{3/2}=\infty
\Longrightarrow
\sum_k\frac{J_k}{K_k}=\infty.
\]

For example, take

\[
J_k=k^{-2/3}.
\]

Then

\[
\sum_kJ_k^{3/2}
=
\sum_k\frac1k
=
\infty,
\]

while for geometric \(K_k=q^{k/2}\),

\[
\sum_k\frac{J_k}{K_k}<\infty.
\]

Hence the cubic tail ledger alone cannot be converted into an ordinary-energy contradiction over the short remaining windows.

\[
\boxed{
\text{cubic annular nonsummability}
\not\Rightarrow
\text{physical Leray-dissipation divergence.}
}
\]

**Status: PROVED by explicit counterexample sequence.**

---

## 6. Quantitative return-count bridge

The missing quantity can be typed exactly.

For each shell label \(k\), suppose genealogy produces \(M_k\) physical return intervals \(I_{k,\ell}\) with physical shell radius \(\rho_k\), each satisfying

\[
|I_{k,\ell}|\ge\theta\rho_k^2
\]

and

\[
\rho_k
\int_{A_{k,\ell}(t)}|\nabla u(t)|^2dx
\ge c_0J_k
\]

throughout the interval.

Assume the whole collection of return intervals has time-overlap multiplicity at most \(Q\).

Each return costs at least

\[
c_0\theta J_k\rho_k
\]

in the ordinary dissipation ledger. Thus the Leray energy inequality yields

\[
\boxed{
\sum_kM_kJ_k\rho_k<\infty.
}
\]

More precisely, with \(E_0=\frac12\|u_0\|_2^2\),

\[
\sum_kM_kJ_k\rho_k
\le
\frac{QE_0}{c_0\theta}.
\]

**Status: PROVED CONDITIONAL on quantitative return, parabolic dwell, amplitude retention, and bounded time overlap.**

---

## 7. Exact sufficient condition for cubic-tail contradiction

If the same return genealogy also satisfies, on a subset carrying the divergent cubic mass,

\[
\boxed{
M_k\rho_k
\ge
c_1J_k^{1/2}
}
\]

for some fixed \(c_1>0\), then

\[
M_kJ_k\rho_k
\ge
c_1J_k^{3/2}.
\]

Therefore

\[
\sum_kJ_k^{3/2}=\infty
\]

would imply

\[
\sum_kM_kJ_k\rho_k=\infty,
\]

contradicting the finite-energy return-count gate.

Thus a precise sufficient genealogy target is

\[
\boxed{
M_k
\gtrsim
\frac{J_k^{1/2}}{\rho_k}.
}
\]

This converts the vague word “recurrent” into an explicit scale-amplitude return-count requirement.

---

## 8. Why qualitative recurrence is still insufficient

If only \(M_k=O(1)\) returns are known at each shrinking scale and \(\rho_k\) is geometric, then even order-one \(J_k\) gives

\[
\sum_kM_kJ_k\rho_k<\infty.
\]

So one or finitely many returns per logarithmic scale are not enough for an ordinary-energy contradiction.

Likewise, if return intervals have unbounded time overlap, the same physical dissipation may be counted repeatedly, and the summation is invalid.

Therefore a successful energy closure requires a genuinely quantitative recurrence statement: sufficiently many returns, sufficiently long dwell, and a bounded-overlap selection.

---

## 9. Diagonal ancient-limit audit

The finite-block diagonal transfer gives late stages \(j_n\) approximating arbitrarily large finite shell sets, with

\[
j_n-\max F_n\to\infty.
\]

But the physical radius of a transferred shell is

\[
R_{j_n,k}^{phys}=r_{j_n}K_k.
\]

As \(j_n-k\to\infty\), this physical radius tends to zero. Consequently an arbitrarily good ancient-profile approximation may occur at an arbitrarily small physical energy weight.

Without a quantitative convergence rate or a quantitative historical-return theorem, diagonal convergence by itself does not provide a lower bound on

\[
M_kR_{j_n,k}^{phys}.
\]

Thus the ancient cubic divergence cannot be pushed through the diagonal limit into a physical energy contradiction solely by choosing larger finite shell blocks.

**Status: PROVED as an audit of the current diagonal argument; quantitative bridge NOT DERIVED.**

---

## 10. Updated bounded-Z frontier

The bounded-\(Z\), recurrent, non-\(L^3\) route now has the sharper form

\[
\boxed{
\sum_kJ_k^{3/2}=\infty
\Longrightarrow
\begin{cases}
\text{quantitative return genealogy with }M_k\rho_k\gtrsim J_k^{1/2}
\Rightarrow\text{energy contradiction},\\[2mm]
\text{or insufficient physical return weight / persistent passive tail}.
\end{cases}
}
\]

The first implication is now explicit and rigorous under its hypotheses. The second branch is the actual survivor.

The highest-value next theorem is therefore not another unweighted shell selection. It is one of:

1. derive the return-count lower bound \(M_k\rho_k\gtrsim J_k^{1/2}\) on a cubic-divergent subset;
2. derive a stronger common finite ledger whose per-return cost removes the extra physical-radius factor;
3. bypass physical return counting with a tail-decoupling or local/quotient Liouville theorem.

Global regularity remains unproved.