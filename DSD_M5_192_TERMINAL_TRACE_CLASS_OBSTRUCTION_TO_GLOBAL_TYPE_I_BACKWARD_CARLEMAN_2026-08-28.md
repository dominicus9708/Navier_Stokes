# DSD M5-192 — Terminal Trace-Class Obstruction to a Global Type-I Backward Carleman

Date: 2026-08-28

Status: **T1 GLOBAL BACKWARD-CARLEMAN ROUTE: YELLOW / CRITICAL COEFFICIENT ABSORPTION IS NOT THE MAIN OBSTRUCTION; THE SAME-TAIL PHYSICAL DIFFERENCE APPROACHES ZERO ONLY THROUGH THE SIMILARITY `L2` SCALING FACTOR, SO THE TERMINAL-BLOWING WEIGHTS REQUIRED BY A STANDARD BACKWARD CARLEMAN DO NOT HAVE A VANISHING TERMINAL TRACE ON A NONZERO RECURRENT NORMALIZED FIBER / USING SUCH A CARLEMAN WOULD SILENTLY ASSUME THE DESIRED NORMALIZED FIBER COLLAPSE / ROUTE T3 (EXACT FUCHSIAN COMPLETE-ORBIT UNIQUENESS) IS RESTORED AS THE PRIMARY P1_B ROUTE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact physical-normalized relation

For a same-tail normalized difference `Z`, the physical difference is

\[
z(x,t)
=
\tau^{-1/2}
Z\left(\frac{x-x_*}{\sqrt\tau},s\right),
\qquad
\tau:=T_*-t,
\qquad
s=-\log\tau+\text{const}.
\]

Therefore

\[
\boxed{
\|z(t)\|_2^2
=
\tau^{1/2}\|Z(s)\|_2^2.
}
\]

On a nonzero compact recurrent fiber, `||Z(s)||_2` may remain order one.

Hence

\[
\|z(t)\|_2\to0
\]

is an automatic similarity scaling collapse and does not mean the normalized state is approaching zero.

---

## 2. Why standard terminal weights are dangerous here

A genuine backward Carleman estimate normally introduces a terminal-singular parameter through a factor schematically of the form

\[
\tau^{-\gamma}
\]

or a stronger terminal exponential.

The terminal trace contributed by the same-tail difference then scales as

\[
\boxed{
\tau^{-\gamma}\|z(t)\|_2^2
=
\tau^{1/2-\gamma}\|Z(s)\|_2^2.
}
\]

For any

\[
\gamma>\frac12,
\]

this does not tend to zero on a nontrivial recurrent normalized fiber.

Thus the unweighted terminal condition

\[
z(T_*)=0\quad\text{in }L^2
\]

does **not** justify the vanishing weighted endpoint term required by a large-parameter terminal Carleman.

---

## 3. Why a large terminal parameter is precisely what the Type-I lower order needs

The physical relative equation has

\[
|a(x,t)|\lesssim \rho^{-1},
\qquad
|B(x,t)|\lesssim \rho^{-2},
\qquad
\rho^2=r^2+\tau.
\]

In the parabolic core `r \lesssim sqrt(tau)`, this becomes

\[
|a|\lesssim\tau^{-1/2},
\qquad
|B|\lesssim\tau^{-1}.
\]

A terminal Carleman must therefore generate gradient and zeroth-order channels at least comparable to

\[
\tau^{-1}|\nabla z|^2,
\qquad
\tau^{-2}|z|^2,
\]

with sufficiently large coefficients to absorb the arbitrary finite W1 Type-I ceiling.

This is exactly the regime in which the terminal parameter cannot be kept below `1/2` merely to preserve the physical `L2` endpoint trace.

Thus the conflict is structural:

\[
\boxed{
\text{strong enough terminal weight for critical absorption}
\quad\text{vs}\quad
\text{weak enough terminal weight for the known }L^2\text{ trace}.
}
\]

---

## 4. Spatial subquadratic convexification does not remove the trace problem

A natural ESS-type weight has a spatial component in the self-similar variable

\[
y=\frac{x-x_*}{\sqrt\tau},
\]

for example a strictly subquadratic convex profile

\[
e^{s\langle y\rangle^\alpha},
\qquad 1<\alpha<2.
\]

On Branch `P1_B^S`, M5-177 supplies enough Gaussian normal decay to make every fixed such spatial exponential integrable.

This helps the **spatial infinity** part of the Carleman estimate.

It does not alter the core scaling

\[
\|z(t)\|_2^2\sim\tau^{1/2}\|Z(s)\|_2^2.
\]

At `|y|=O(1)`, the spatial weight is only a finite factor.  The terminal trace obstruction remains.

---

## 5. Why importing bounded-mild backward uniqueness is circular

The recent whole-space Navier--Stokes backward-uniqueness theorem of Lei--Yang--Yuan assumes bounded mild solutions (and bounded vorticity in the main theorem).

The W1 physical realization allows

\[
\|u(t)\|_\infty\sim\tau^{-1/2},
\qquad
\|\omega(t)\|_\infty\sim\tau^{-1}.
\]

Hence the theorem does not apply directly.

To force the same-tail difference into its bounded terminal class one would need to prove precisely the normalized fiber collapse that is currently at issue.

Therefore

\[
\boxed{
\text{bounded-mild BU theorem}
\not\Rightarrow
P1_B\text{ closure}
}

under the existing W1 hypotheses.

---

## 6. Relation to M5-188--190

M5-188--190 remain GREEN and useful:

- critical lower-order coefficient absorption is locally possible;
- pressure can be removed through vorticity plus elliptic Stokes recovery;
- divergence-source forcing has a correct endpoint scale-local Carleman estimate.

M5-192 says only that these **local coercivity modules cannot be upgraded to the global terminal conclusion by a standard terminal-singular weight using the present endpoint trace class**.

The obstruction is dynamic, not local power counting.

---

## 7. DSD audit

### Formation — GREEN

Physical `L2` zero and normalized-state zero are kept as different objects.

### Axis — GREEN

Terminal weight strength, Type-I coefficient strength, and similarity amplitude are separate axes.

### Static aggregation — GREEN

The similarity factor `tau^{1/2}` is not counted as dissipative decay of the normalized fiber.

### Dynamics — GREEN

No terminal Carleman endpoint is assumed before checking that its weighted trace actually vanishes.

### Cross-audit — GREEN

This blocks the circular implication

\[
\text{physical scaling zero}
\to
\text{weighted terminal zero}
\to
\text{normalized fiber zero}.
\]

---

## 8. Route decision

Route `T1` is not declared impossible in principle, but it no longer has priority under the current trace class.

The primary route returns to `T3`:

\[
\boxed{
\text{same-tail all-orders flatness}
+\text{compact complete/recurrent normalized dynamics}
+\text{exact Fuchsian fast--slow equation}
\Longrightarrow ?
}
\]

The next calculation should therefore use the **complete-orbit/invariant-pair structure directly**, rather than trying to manufacture stronger physical terminal data through a Carleman weight.

In particular, M5-128's exact relative-energy ledger should be re-audited together with M5-145 flatness and M5-174--180 spectral/Fuchsian information.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
