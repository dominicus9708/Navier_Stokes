# Global L3-Tail Necessity for the Restricted Ancient Survivor — 2026-08-20

Overall status: **NEW GLOBAL NECESSARY CONDITION — GLOBAL REGULARITY NOT PROVED.**

This note combines the restricted Type-I ancient limit with the Albritton--Barker Liouville theorem for ancient solutions bounded in global `L^3` along a backward sequence. It shows that any nontrivial ancient survivor in the present proof route must retain a genuinely global, scale-critical, backward-growing `L^3` tail. The local natural core alone cannot supply this requirement under the non-`H/T` compact-core hypotheses.

---

## 1. External Liouville input

Albritton--Barker prove that if a mild ancient Navier--Stokes solution satisfies

\[
\sup_k\|U(\cdot,\tau_k)\|_{L^3(\mathbb R^3)}<\infty
\]

for some sequence

\[
\tau_k\downarrow-\infty,
\]

then

\[
U\equiv0.
\]

Therefore any **nontrivial** mild ancient solution must fail every such bounded backward sequence. Equivalently, whenever the global `L^3` norm is finite at individual times,

\[
\boxed{
\liminf_{\tau\to-\infty}\|U(\tau)\|_3=\infty.
}
\]

The present first-hitting ancient candidate is nontrivial because the normalized vorticity equals one at a bounded point at the terminal rescaled time.

---

## 2. Natural Type-I core contributes only critical O(1) L3 mass

At backward first-hitting scale `R=sqrt(|tau|)`, the natural Type-I scaling is

\[
|U|\sim R^{-1},
\qquad
\text{core radius}\sim R.
\]

Hence

\[
\int_{B_{cR}}|U|^3dx
\sim
R^{-3}R^3
=O(1).
\]

Under the non-`H/T` natural-profile control developed in the main route, the rescaled unit core is uniformly controlled, so this `O(1)` critical core contribution does not grow merely because the backward scale `R` grows.

Therefore the backward divergence required by the Liouville theorem cannot be supplied by one uniformly controlled natural core alone.

---

## 3. Necessary global tail

Let `R(tau) ~ sqrt(|tau|)` be the natural core radius and split

\[
\|U(\tau)\|_3^3
=
\int_{|x|\le CR(\tau)}|U|^3
+
\int_{|x|>CR(\tau)}|U|^3.
\]

If the first term remains uniformly bounded on the non-`H/T` natural core, nontriviality forces

\[
\boxed{
\int_{|x|>CR(\tau)}|U(x,\tau)|^3dx\to\infty
\quad\text{along every sufficiently remote backward sequence}
}
\]

in the sense required to prevent a bounded global `L^3` subsequence.

Thus the restricted ancient survivor must contain a **global critical L3 tail** outside the active Type-I core.

---

## 4. Compatibility with the passive-halo reduction

This conclusion does not contradict the earlier aggregate halo result. A velocity tail may carry critical `L^3` mass while its vorticity/strain influence on the tracked core is summably small.

The previous aggregate quadrupole estimate gives, for vorticity outside normalized radius `R_0`,

\[
|S_{\ge R_0}(0)|^2
\lesssim R_0^{-1}P_{\Omega,\ge R_0}.
\]

Hence on the non-`H` branch the remote tail becomes dynamically passive at the core as `R_0 -> infinity`, even though a velocity `L^3` tail may still be needed globally to avoid the ancient `L^3` Liouville theorem.

The final ancient picture is therefore necessarily two-sector:

\[
\boxed{
\text{active bounded Type-I core}
\quad+\quad
\text{global L3-critical dynamically passive tail}.
}
\]

---

## 5. Critical-shell interpretation

A model Type-I shell of radius `R` and velocity amplitude `R^{-1}` contributes

\[
\int_{A_R}|U|^3\sim O(1)
\]

independently of `R`. Thus a non-summable sequence of geometrically separated critical shells can make the global `L^3` norm diverge while each shell is individually critical rather than supercritical.

At the same time its kinetic-energy contribution is of order

\[
\int_{A_R}|U|^2\sim R.
\]

When pulled back to a physical first-hitting scale `r_j`, this costs physical energy of order `r_jR`. A geometric stack extending only to a fixed physical outer scale can therefore remain compatible with finite initial energy because its energy sum is dominated by the largest shell.

This explains why the global `L^3` non-tight tail can coexist with finite physical energy and why the earlier energy-only stage-packing argument could not remove it.

---

## 6. New global target

A nontrivial non-`H/T` ancient survivor must now satisfy all of:

1. a tight active Type-I core carrying the `P_V` recurrence;
2. continuous backward Type-I vorticity control;
3. a global `L^3` norm that cannot remain bounded along any backward sequence;
4. a remote critical tail whose direct strain coupling to the active core is asymptotically passive unless it pays `H`.

The next global rigidity target is therefore not to eliminate the tail by energy alone. It is to show that a dynamically passive `L^3`-critical tail cannot continually coexist with the recurrent active core without causing either material exchange (`T`), derivative coupling (`H`), or loss of the required projective `P_V` replenishment.

Status: **ANY NONTRIVIAL RESTRICTED TYPE-I ANCIENT SURVIVOR MUST CARRY A BACKWARD-DIVERGENT GLOBAL L3 TAIL OUTSIDE ITS UNIFORMLY CONTROLLED ACTIVE CORE. THIS TAIL MAY BE ENERGY-COMPATIBLE BUT MUST REMAIN DYNAMICALLY PASSIVE ON THE NON-H BRANCH.**