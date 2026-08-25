# DSD W1: No-Short-Return Cone and Aperiodic Recurrence Reduction

Date: 2026-08-25

Status: **STATIONARY AND SUFFICIENTLY SHORT-RETURN W1 SUBCLASSES PRUNED / GENERIC RECURRENT W1 REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The endpoint survivor `W1` has now been upgraded to a compact subcritical orbit:

\[
U\in L_s^\infty L_Y^{3,\infty},
\qquad
U\in L_s^\infty L_Y^p\ \forall 3<p\le6,
\]

with global `L^p` precompactness, bounded normalized enstrophy, bounded shell derivative ratio, and a nonzero recurrent core.

The Pineau--Vicol one-slice approximate-self-similarity criterion, already used in the project, implies that a hypothetical singular survivor cannot have arbitrarily small self-similar-time velocity on the active core. Thus there exist a fixed ball `B_R` and

\[
\boxed{
\sigma_0>0
}
\]

such that for all sufficiently late Leray times,

\[
\boxed{
\|U_s(s)\|_{L^2(B_R)}\ge\sigma_0.
}
\]

This note combines that lower bound with local analytic regularity to obtain a quantitative no-short-return cone.

---

## 2. Uniform second time derivative on the core

The Leray equation is autonomous:

\[
U_s+\frac12U+\frac12Y\cdot\nabla U
+U\cdot\nabla U+\nabla P
=\nu\Delta U,
\qquad \nabla\cdot U=0.
\]

The recurrent W1 corridor has uniform local analytic spatial bounds on a slightly larger fixed ball. The pressure is controlled locally by the usual near/far decomposition and the bounded Type-I data.

Differentiating the equation once in `s` and using those uniform bounds gives

\[
\boxed{
\sup_{s\ge s_0}
\|U_{ss}(s)\|_{L^2(B_R)}
\le K_{ss}<\infty.
}
\]

No numerical value of `K_ss` is needed for the structural argument.

---

## 3. Taylor formula in state space

For `h>0`,

\[
U(s+h)-U(s)
=hU_s(s)
+\int_0^h(h-\tau)U_{ss}(s+\tau)\,d\tau.
\]

Therefore

\[
\begin{aligned}
\|U(s+h)-U(s)\|_{L^2(B_R)}
&\ge
h\|U_s(s)\|_{L^2(B_R)}
-
\frac12K_{ss}h^2\\
&\ge
\sigma_0h-rac12K_{ss}h^2.
\end{aligned}
\]

Set

\[
\boxed{
h_0:=\min\left\{1,\frac{\sigma_0}{K_{ss}}\right\}.}
\]

Then for every `0<h<=h0`,

\[
\boxed{
\|U(s+h)-U(s)\|_{L^2(B_R)}
\ge
\frac{\sigma_0}{2}h.
}
\]

The same estimate holds for negative sufficiently small `h` along a complete W1 omega-limit trajectory.

This is the **no-short-return cone**.

---

## 4. Immediate consequences

### 4.1 No stationary W1 survivor

If `U_s=0`, the Pineau--Vicol local speed lower bound is violated immediately. Thus

\[
\boxed{W1_{stationary}=\varnothing}
\]

inside the hypothetical singular corridor.

This is consistent with the classical stationary/backward-self-similar Liouville theorems, which in fact exclude stationary profiles under much weaker Lorentz/Morrey assumptions.

### 4.2 Exact periodic orbit has a minimum period

If

\[
U(s+S)=U(s)
\]

for all `s`, then the no-short-return cone implies

\[
\boxed{S>h_0.}
\]

Hence no exact W1 DSS profile can have arbitrarily small self-similar period.

Pineau--Vicol (2026) independently prove a stronger Type-I DSS theorem: for a Type-I upper bound, a backward DSS profile is trivial when the discrete scaling factor `lambda` is sufficiently close to one, equivalently when its period `S=2 log lambda` is sufficiently small. Their proof uses the small period essentially to make the temporal fluctuation of the profile `O(S)`.

### 4.3 Approximate returns must be at least linear in time

For every `0<h<=h0`,

\[
\boxed{
\operatorname{dist}_{L^2(B_R)}
(U(s+h),U(s))
\ge c_0h,
\qquad c_0=\sigma_0/2.
}
\]

Thus a short approximate recurrence with error `o(h)` is impossible.

This prevents an unjustified step from compact recurrence to local approximate stationarity.

---

## 5. Why compact recurrence does not finish the proof

Global `L^p` precompactness guarantees omega-limit recurrence after passing to a minimal invariant subset, but recurrence alone does not force a stationary or periodic point.

A compact smooth flow can support

- quasiperiodic motion;
- nonperiodic minimal recurrent sets;
- more complicated aperiodic dynamics;

while its vector field stays uniformly nonzero.

The no-short-return cone is fully compatible with such dynamics.

Therefore one must not infer

\[
\text{precompact + recurrent}
\Longrightarrow
\text{periodic/self-similar}.
\]

That inference would be a genuine dynamical-systems gap.

---

## 6. Audit of the 2026 DSS theorem

Pineau--Vicol's DSS proof does not extend automatically from exact short periodicity to generic recurrence.

For a profile of period `S`, they decompose

\[
U=\langle U\rangle_s+\widetilde U
\]

and use the Type-I derivative bounds plus exact periodicity to obtain

\[
|\widetilde U(y,s)|
\lesssim
\frac{S}{1+|y|},
\qquad
|\nabla\widetilde U(y,s)|
\lesssim
\frac{S}{1+|y|^2}.
\]

Thus small `S` makes the entire temporal fluctuation perturbative. Generic recurrent W1 motion has no such globally small period and can retain the positive core speed `sigma0`.

Hence the valid external pruning is

\[
\boxed{
\text{stationary / sufficiently short-period DSS}
\quad\text{excluded},
}
\]

not

\[
\text{all recurrent W1 excluded}.
\]

---

## 7. Refined final W1 class

After all current pruning, a genuine W1 survivor must be

\[
\boxed{
\begin{aligned}
&\text{nonzero and genuinely nonstationary},\\
&\text{globally precompact in every }L^p,\ 3<p\le6,\\
&\text{uniformly weak-}L^3,\\
&\text{bounded in global enstrophy},\\
&\text{bounded in shell derivative ratio},\\
&\|U_s\|_{L^2(B_R)}\ge\sigma_0,\\
&\text{with no recurrence period below }h_0,\\
&\text{and, if periodic at all, outside the known small-period DSS regime.}
\end{aligned}
}
\]

Thus the endpoint is no longer a generic ancient-solution problem. It is a **compact, genuinely moving recurrent Leray-flow rigidity problem**.

---

## 8. Next mathematical target

The remaining theorem can be stated sharply as:

\[
\boxed{
\text{There is no nonzero complete recurrent Leray trajectory in W1.}
}
\]

A successful proof now needs one genuinely dynamical ingredient, for example:

1. a strict Lyapunov/virial functional compatible with the `1/R` endpoint tail;
2. an extension of the weighted-L2 DSS machinery from exact periodicity to invariant/recurrent measures;
3. a tail quotient that leaves a finite-energy recurrent core and has strict dissipation;
4. or a recurrent-orbit Liouville theorem for the above precompact subcritical class.

### Status

**PROVED:** no-short-return cone; stationary exclusion; positive minimum return scale; exact description of why small-period DSS theorems do not yet close generic recurrence.

**OPEN:** genuinely aperiodic/large-period recurrent W1; final master closure; global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
