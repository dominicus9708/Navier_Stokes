# DSD M17-414 — A parent-length positive-flux loop defeats the cubic raw-`H2` discount exactly when its record-window occupancy fractions are nonsummable

Date: 2026-09-08  
Canonical ID: **M17-414**

Status: **ACTIVE OCCUPANCY CRITERION / LOOP-RESIDENCE SHARPENING / RECURRENCE-DENSITY FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-413

M17-413 proves conditionally that a parent-length, positive-flux, own-scale exact CE-H loop carries

- `O(R_m)` independent/bounded-overlap spatial segments;
- `O(R_m^2)` own-time blocks if it persists throughout an entire parent parabolic record interval;
- hence `O(R_m^3)` normalized raw-`H2` packets.

The M17-405 ancestry weight `R_m^{-3}` then leaves an order-one charge per record.

The full-parent-time assumption can be weakened to an exact occupancy fraction.

## 2. Define record-window occupancy

Let `J_m` be the parent parabolic record interval in parent-normalized time, with

\[
|J_m|\asymp1.
\]

Let

\[
G_m\subset J_m
\]

be the set of times for which all M17-413 retained-loop hypotheses hold simultaneously:

- exact CE-H coefficient scale `r_m\asymp R_m^{-1}`;
- parent-scale loop length bounded below;
- positive retained flux `Phi>=Phi_*`;
- tubular reach/bounded-overlap spatial segmentation;
- same genealogy/domain component.

Define

\[
\boxed{
\alpha_m
:=
\frac{|G_m|}{|J_m|}
\in[0,1].
}
\]

This is the **usable loop occupancy fraction** of record `m`.

## 3. Temporal multiplicity from partial occupancy

One descendant own-time has duration

\[
r_m^2\asymp R_m^{-2}.
\]

A measurable subset of parent time of measure `|G_m|\asymp alpha_m` contains, after standard interval selection with bounded overlap, on the order of

\[
\boxed{
N_{t,m}
\gtrsim
c\alpha_mR_m^2
}
\]

usable unit own-time blocks, modulo harmless endpoint losses.

If `G_m` is highly fragmented, one uses a Vitali-type selection of own-time intervals contained in density portions of `G_m`; failure to obtain this count is retained as an explicit temporal-fragmentation/interface exit rather than silently identifying measure with contiguous residence.

## 4. Spatial multiplicity remains linear

M17-313 gives

\[
D_\xi\kappa=0,
\]

and the M17-413 tubular-reach hypothesis gives

\[
\boxed{
N_{x,m}\gtrsim cR_m.
}
\]

Each space-time packet carries

\[
h_{m,j}^{norm}\gtrsim c\Phi_*^2.
\]

Therefore

\[
\boxed{
H_{m}^{norm}
\gtrsim
c\Phi_*^2
N_{x,m}N_{t,m}
\gtrsim
c\Phi_*^2\alpha_mR_m^3.
}
\]

## 5. Exact cancellation of the cubic ancestry discount

Apply the M17-405 ancestry factor:

\[
R_m^{-3}H_m^{norm}
\gtrsim
c\Phi_*^2\alpha_m.
\]

Thus the entire spatial/parabolic scaling cancels and the first-generation raw-`H2` ledger gives

\[
\boxed{
\sum_m\alpha_m<\infty
}
\]

for every retained family satisfying the other uniform hypotheses.

Equivalently, a contradiction follows if

\[
\boxed{
\sum_m\alpha_m=\infty.
}
\]

This is the exact loop-residence threshold.

## 6. Consequences

A uniform positive occupancy

\[
\alpha_m\ge\alpha_*>0
\]

on infinitely many records closes the branch immediately.

But much less is enough. For geometric records `R_m~q^m`, even

\[
\alpha_m\sim\frac1m
\]

is sufficient because

\[
\sum_m\frac1m=\infty.
\]

By contrast,

\[
\alpha_m\sim m^{-1-\varepsilon}
\]

or exponentially sparse occupation may remain compatible with the ancestor.

Thus the missing theorem is not full persistence; it is merely a **nonsummable record-window occupancy theorem**.

## 7. Topological recurrence is not yet enough

M17-360 proves that a compact nondegenerate closed-loop orbit contains a recurrent minimal subsystem in its omega-limit hull.

But M17-360 explicitly does not prove that the original orbit spends positive density of time near that minimal subsystem.

Therefore topological recurrence alone supplies no certified lower bound on `alpha_m`.

A recurrent orbit may have arbitrarily sparse return times at the level needed here unless additional dynamical structure is proved.

Hence

\[
\boxed{
\text{recurrent minimal hull}
\not\Rightarrow
\sum_m\alpha_m=\infty
}
\]

with the current theorem set.

## 8. Relation to M17-361

M17-361 proves a positive recurrent mean palinstrophy density on the retained positive-flux recurrent loop family.

That mean is taken on the recurrent hull/limit dynamics.

M17-414 identifies the missing transfer to the first-generation record ledger:

\[
\boxed{
\text{recurrent-hull positive payer}
+
\text{nonsummable original-record occupancy}
\Longrightarrow
\text{raw-`H2` contradiction under M17-413 geometry}.
}
\]

Without the occupancy transfer, recurrent mean and ancestral multiplicity remain distinct statements.

## 9. Exact revised loop branch

The late CE-H loop branch is now

\[
\boxed{
\begin{aligned}
H_{parent\text{-}length\ positive\text{-}flux\ own\text{-}scale\ loop}
\Longrightarrow{}&
H_{\sum_m\alpha_m=\infty\ \Rightarrow\ contradiction}\\
&\lor G_{\sum_m\alpha_m<\infty\ sparse\ record\ occupancy}\\
&\lor G_{temporal\ fragmentation}\\
&\lor G_{tubular\ reach/self\text{-}clustering}\\
&\lor G_{flux/coefficient/genealogy/interface\ loss}.
\end{aligned}
}
\]

This is much narrower than an unspecified recurrence escape.

## 10. DSD audit

The DSD role is to separate topological recurrence from quantitative occupation density.

The proof currency is the exact cancellation

\[
R_m^{-3}
\cdot R_m
\cdot \alpha_mR_m^2
=\alpha_m.
\]

No DSD hypothesis enters this calculation.

## 11. Audit verdict

**PASS — exact occupancy criterion.**

The loop raw-`H2` route is now reduced to proving that the usable positive-flux coefficient-scale loop occupies a nonsummable fraction of the first-generation record windows, or else classifying why that occupation becomes summably sparse.

The next high-value target is the dynamics of the omega-limit set: if the whole omega-limit set is minimal, asymptotic shadowing may upgrade topological recurrence to high occupancy; if not, the nonminimal decomposition must be treated as a separate genealogy/transition branch.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]