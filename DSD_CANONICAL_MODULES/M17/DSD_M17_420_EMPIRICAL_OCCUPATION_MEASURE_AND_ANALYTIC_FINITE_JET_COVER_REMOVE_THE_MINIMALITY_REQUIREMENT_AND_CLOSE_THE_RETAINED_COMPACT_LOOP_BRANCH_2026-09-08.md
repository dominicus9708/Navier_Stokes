# DSD M17-420 — Empirical occupation measure plus the analytic finite-jet cover removes the minimality requirement and closes the retained compact loop branch

Date: 2026-09-08  
Canonical ID: **M17-420**

Status: **ACTIVE COMPACT-LOOP OCCUPATION-MEASURE CLOSURE / MINIMALITY REQUIREMENT REMOVED / LOOP BRANCH COMPRESSION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-415--419 close the compact loop branch when the **entire omega-limit set is minimal**, by upgrading robust good states to syndetic occupancy and then eliminating all finite and infinite coefficient jet possibilities.

The minimality assumption is stronger than necessary.

A compact original loop orbit already carries empirical time-occupation measures. Analyticity gives a countable cover of the retained state space by finite-jet good sets. One member of that countable cover must carry positive occupation mass.

This is enough for the M17-414 raw-`H2` occupancy criterion.

## 2. Retained compact loop-state space

Let

\[
Z(\theta)
\]

be the original same-material exact CE-H loop-state orbit on the retained branch.

Assume its closure

\[
\boxed{
\mathcal K
:=
\overline{\{Z(\theta):\theta\ge\theta_0\}}
}
\]

is compact in a regular topology with uniform margins for:

- positive loop flux / retained positive-flux tube family;
- nonzero regular vorticity amplitude on the loop;
- parent-scale loop length;
- tubular reach or bounded-overlap segmentation at the true intrinsic scale;
- spatial analyticity and uniform finite-jet bounds on compact subsets;
- representation-safe parent-to-record scale/genealogy map;
- bounded-above/below normalized record-window lengths.

Failure of any one of these items is an explicit named exit and is not included in the retained compact branch.

## 3. Empirical time measures

Define

\[
\boxed{
\mu_T
:=
\frac1T
\int_0^T
\delta_{Z(\theta)}d\theta.
}
\]

Each `mu_T` is a probability measure on the compact metric space `K`.

By weak-* compactness of probability measures, there exists a sequence

\[
T_j\to\infty
\]

such that

\[
\boxed{
\mu_{T_j}\rightharpoonup\mu
}
\]

for a probability measure `mu` supported on `K`.

Standard averaging also shows that `mu` is invariant under the continuous semiflow, but invariance is not needed for the basic occupation argument below.

## 4. Continuous finite-jet observables

For each integer `p>=0`, define the loop jet magnitude

\[
M_p(Z)
:=
\max_{x\in\Gamma(Z)}
|D^p\kappa(x)|.
\]

For `p=0`, line constancy gives simply

\[
M_0(Z)=|\kappa_\Gamma(Z)|.
\]

On the retained compact regular topology, each `M_p` is continuous.

Compactness gives finite upper bounds

\[
M_p(Z)\le C_p<\infty.
\]

## 5. Every nontrivial retained loop state has a finite nonzero jet

Suppose a state `Z in K` satisfied

\[
M_p(Z)=0
\qquad\text{for every }p\ge0.
\]

Then every spatial derivative of `kappa` vanishes at every loop point.

M17-419 applies at any regular loop point and gives

\[
\Omega\equiv0
\]

globally, contradicting the retained nonzero positive-flux loop.

Therefore

\[
\boxed{
\forall Z\in\mathcal K,
\quad
\exists p<\infty
\text{ such that }
M_p(Z)>0.
}
\]

This is the key analytic finite-jet cover property.

## 6. Countable robust good-state cover

For integers `p>=0` and `n>=1`, define

\[
\boxed{
G_{p,n}
:=
\left\{
Z\in\mathcal K:
M_p(Z)>\frac1n
\right\}.
}
\]

These sets are relatively open by continuity of `M_p`.

Section 5 gives the countable cover

\[
\boxed{
\mathcal K
=
\bigcup_{p=0}^{\infty}
\bigcup_{n=1}^{\infty}
G_{p,n}.
}
\]

Since `mu(K)=1`, countable subadditivity implies that at least one pair `(p_*,n_*)` satisfies

\[
\boxed{
\mu(G_{p_*,n_*})>0.
}
\]

Otherwise the countable union would have zero `mu` measure.

## 7. Positive occupation of one finite-jet class

Let

\[
G_*:=G_{p_*,n_*}.
\]

Because `G_*` is open, Portmanteau gives

\[
\mu(G_*)
\le
\liminf_{j\to\infty}
\mu_{T_j}(G_*).
\]

Hence for all sufficiently large `j` along a subsequence,

\[
\boxed{
\frac1{T_j}
\left|
\{0\le\theta\le T_j:Z(\theta)\in G_*\}
\right|
\ge c_*>0.
}
\]

Thus the **original orbit itself** spends a positive total asymptotic time fraction in one fixed finite-jet class.

No minimality, recurrence-density theorem, or shadowing of a chosen minimal subset is needed.

## 8. Uniform spatial arc from the fixed jet margin

On `G_*`,

\[
M_{p_*}>1/n_*.
\]

Uniform compact bounds on the next spatial derivative give a uniform continuity modulus along the loop.

Therefore every state in a slightly smaller robust class contains a loop arc of fixed parent-normalized length

\[
\boxed{\ell_*>0}
\]

on which the relevant `p_*`-jet remains bounded below by a fixed positive constant.

For `p_*=0`, this is the M17-416 away-zero loop case.

For `p_*=1`, it is the M17-417 regular zero-gradient case after restricting to the zero-loop subbranch.

For `p_*>=2`, it is the M17-418 finite higher-jet case.

In every case, the true jet scale supplies `O(R_m)` bounded-overlap own-scale spatial segments on the representation-safe record branch.

## 9. Uniform raw-H2 lower bound on the occupied class

M17-413/417/418 give, according to `p_*`, a fixed normalized raw-`H2` lower bound per own-scale spatial segment per unit own-time:

\[
\boxed{h_*^{norm}>0.}
\]

All constants are uniform on the fixed robust class because `p_*` and `n_*` are now fixed and the state space is compact.

Thus the positive occupation measure found in Section 7 is not spread over ever-higher jet orders with vanishing constants; one concrete finite jet class carries positive time mass.

## 10. Occupation measure directly yields nonsummable record occupancy

Let the bounded-length record windows `J_m` partition/cover the sufficiently late retained tail with uniformly bounded overlap.

Let

\[
\alpha_m
:=
\frac{|J_m\cap\{Z\in G_*\}|}{|J_m|}.
\]

Positive asymptotic time density of `G_*` and uniform upper/lower bounds on `|J_m|` imply

\[
\boxed{
\sum_m\alpha_m=\infty.
}
\]

Indeed, if the sum were finite, the total late good-state time would be finite up to uniform window constants, contradicting the positive time-density subsequence from Section 7.

## 11. Correction to the temporal-fragmentation concern

M17-414 retained a possible temporal-fragmentation exit when interpreting `alpha_m` as a count of complete own-time intervals.

For the present raw-`H2` route that extra exit is unnecessary once a **pointwise-in-time spatial raw-`H2` lower bound** is available on `G_*`.

One integrates the snapshot lower bound directly over the measurable good-time set.

Thus no contiguous own-time block is required:

\[
\boxed{
\text{measurable good-time occupation is enough}.
}
\]

The factor `alpha_m R_m^2` is a normalized time measure, not necessarily a literal count of disjoint full intervals.

This supersedes the temporal-fragmentation caution of M17-414 for these pointwise loop/corridor lower bounds.

## 12. Raw-H2 ancestral contradiction

For record `m`, the fixed parent-length good arc provides the linear spatial factor `R_m`, while good-time measure provides `alpha_mR_m^2` normalized temporal measure.

Therefore

\[
\boxed{
H_m^{norm}
\gtrsim
c h_*\alpha_mR_m^3.
}
\]

Apply M17-405:

\[
R_m^{-3}H_m^{norm}
\gtrsim
c h_*\alpha_m.
\]

Summing and using

\[
\sum_m\alpha_m=\infty
\]

gives

\[
\sum_mR_m^{-3}H_m^{norm}=\infty,
\]

contradicting the finite first-generation raw-`H2` ancestral ledger.

## 13. Main theorem

Under the retained compact regular geometry and representation-safe record map,

\[
\boxed{
\text{a precompact positive-flux exact CE-H closed-loop orbit cannot persist.}
}
\]

Minimality of the omega-limit set is **not required**.

The proof uses only:

1. compact empirical occupation measures;
2. the countable finite analytic-jet cover;
3. fixed-jet own-scale raw-`H2` lower bounds;
4. the exact M17-405 cubic ancestry weight.

## 14. Revised loop exits

The closed-loop CE-H branch is now reduced to explicit failures of the retained hypotheses:

\[
\boxed{
\begin{aligned}
G_{loop\ state\ decompactification},\\
G_{positive\ flux\ thinning/loss},\\
G_{nodal/amplitude\ loss},\\
G_{tubular\ reach/self\text{-}clustering},\\
G_{jet\text{-}scale/record\text{-}scale\ mismatch},\\
G_{parent\text{-}to\text{-}record\ genealogy/scale\text{-}map\ failure},\\
G_{interface/rank/domain\ loss}.
\end{aligned}
}
\]

The former separate `nonminimal omega-limit` escape is no longer needed on the retained compact branch.

## 15. Relation to M17-415--419

M17-415--419 remain valid and useful as a transparent minimal-dynamics subroute.

M17-420 strictly strengthens the navigation result by showing that occupation-measure compactness already selects a positive-mass finite-jet class even when the omega-limit set is nonminimal.

Thus future frontier files should treat M17-420 as the authoritative compact-loop closure under the stated hypotheses.

## 16. DSD audit

The DSD role is an exhaustive countable state-class audit.

The key logical point is that a compact trajectory cannot spend all its time among finite-jet states while giving every fixed jet class zero occupation mass: countable additivity forbids it.

All analytic and measure arguments are standard mathematics.

## 17. Audit verdict

**PASS — retained compact closed-loop CE-H branch closed without a minimality assumption.**

The late CE-H frontier now moves away from recurrent loop dynamics toward the explicit decompactification, scale-map/genealogy, tubular/self-clustering, flux/amplitude, and interface/rank/domain exits.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]