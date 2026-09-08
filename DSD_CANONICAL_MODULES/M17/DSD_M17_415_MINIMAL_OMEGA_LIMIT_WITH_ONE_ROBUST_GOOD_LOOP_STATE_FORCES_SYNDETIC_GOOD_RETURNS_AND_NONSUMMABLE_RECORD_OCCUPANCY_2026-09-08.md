# DSD M17-415 — A minimal omega-limit set with one robust good loop state forces syndetic good returns and nonsummable record occupancy

Date: 2026-09-08  
Canonical ID: **M17-415**

Status: **ACTIVE COMPACT-DYNAMICS OCCUPANCY THEOREM / CONDITIONAL LOOP-BRANCH CLOSURE / SYNDETIC RETURN UPGRADE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input and objective

M17-360 gives a compact nondegenerate closed-loop orbit and a recurrent minimal subset inside its omega-limit set, but explicitly does not give positive-density shadowing by the original orbit.

M17-414 shows that the raw-`H2` loop route closes once the usable record-window occupancies `alpha_m` satisfy

\[
\sum_m\alpha_m=\infty.
\]

The present module identifies a standard compact-dynamics condition under which this occupancy is automatic:

\[
\boxed{\text{the whole omega-limit set is minimal}.}
\]

Together with one robust good loop state, minimality upgrades recurrence to bounded-gap good returns.

## 2. Compact loop-state semiflow

Let

\[
Z(\theta)
\]

be the compact regular loop-state trajectory from M17-360, with compact orbit closure `K` and continuous semiflow `S_t`.

Let

\[
\Omega_\omega:=\omega(Z)
\]

be its omega-limit set.

Assume the present branch satisfies

\[
\boxed{\Omega_\omega\text{ is minimal}.}
\]

Thus every forward orbit in `Omega_omega` is dense in `Omega_omega`.

## 3. Robust good-state set

Assume there is a state

\[
z_g\in\Omega_\omega
\]

at which the M17-413 usable-loop conditions hold with strict margins, including the representation-normalized versions of:

- positive loop flux;
- parent-scale/nondegenerate loop length;
- coefficient separated from zero and in the desired intrinsic scale window;
- tubular reach/bounded-overlap segmentation;
- no interface/rank/domain loss.

By continuity, these strict inequalities persist on a relative open neighborhood

\[
U\subset\Omega_\omega
\]

of `z_g`.

Choose a smaller nonempty open set

\[
U_0
\]

with

\[
\overline{U_0}\subset U.
\]

The gap between `U_0` and the complement of `U` supplies robustness for a uniform dwell interval.

## 4. Minimality gives a uniform hitting-time bound

For every `z in Omega_omega`, density of its forward orbit implies that there exists a time `t_z>=0` with

\[
S_{t_z}z\in U_0.
\]

By continuity, there is a neighborhood `V_z` of `z` such that

\[
S_{t_z}V_z\subset U_0.
\]

The family `V_z` covers the compact set `Omega_omega`.

Choose a finite subcover

\[
V_{z_1},\dots,V_{z_N}
\]

and define

\[
\boxed{L_*:=\max_i t_{z_i}<\infty.}
\]

Then every point of `Omega_omega` hits `U_0` within forward time at most `L_*`.

By invariance, the same statement applies after every starting time.

Therefore good returns are **syndetic**: the gap between successive hits is uniformly bounded.

## 5. Uniform dwell time inside the good set

Since

\[
\overline{U_0}\subset U
\]

and the semiflow is uniformly continuous on the compact set

\[
\overline{U_0}\times[0,\delta]
\]

for sufficiently small fixed `delta>0`, one can choose

\[
\boxed{\delta_*>0}
\]

such that

\[
z\in U_0
\quad\Longrightarrow\quad
S_tz\in U
\quad\text{for }0\le t\le\delta_*.
\]

Hence every syndetic return contains a uniform positive-duration good-loop interval.

The minimal orbit therefore has a positive lower time-density in `U`, quantitatively at least a constant of order

\[
\boxed{
\underline d(U)
\gtrsim
\frac{\delta_*}{L_*+\delta_*}
>0.
}
\]

No ergodic theorem is needed for this lower bound.

## 6. Transfer from the omega-limit set to the original orbit

For a precompact trajectory,

\[
\boxed{
\operatorname{dist}(Z(\theta),\Omega_\omega)\to0
\qquad(\theta\to\infty).
}
\]

Otherwise there would exist `epsilon>0` and a late sequence staying at distance at least `epsilon`; precompactness would yield a subsequential limit belonging to the omega-limit set, a contradiction.

Because the hitting and dwell estimates above use strict open margins and only a bounded time horizon `L_*+delta_*`, uniform continuity of the semiflow transfers them to all sufficiently late original states lying close enough to `Omega_omega`.

Hence the **original loop orbit** also has asymptotically bounded gaps between usable good-loop intervals of duration comparable to `delta_*`.

Therefore its lower asymptotic good-time density is positive.

## 7. Convert syndetic similarity/record occupancy to `alpha_m`

Assume the parent-to-record map gives record windows whose normalized durations are bounded above and below,

\[
0<J_-\le |J_m|\le J_+<\infty,
\]

as in the retained geometric first-hitting corridor, and maps the robust good-state set to the M17-413 coefficient-scale loop conditions.

Since good intervals have bounded gaps and uniform dwell, a fixed positive proportion of sufficiently late record windows, or a uniformly bounded block of consecutive records, contains a fixed positive amount of good time.

Consequently there exist constants `c_*>0` and a positive-density set of record indices `M_good` such that

\[
\boxed{
\alpha_m\ge c_*
\qquad(m\in M_{good}).
}
\]

In particular,

\[
\boxed{
\sum_m\alpha_m=\infty.
}
\]

## 8. Apply M17-414

M17-414 gives

\[
R_m^{-3}H_m^{norm}
\gtrsim
c\Phi_*^2\alpha_m.
\]

Therefore

\[
\sum_m\alpha_m=\infty
\]

forces

\[
\sum_mR_m^{-3}H_m^{norm}=\infty,
\]

contradicting the M17-405 finite first-generation raw-`H2` ancestral ledger.

Hence the branch

\[
\boxed{
\begin{aligned}
&\omega(Z)\text{ minimal}\\
&+\text{one robust M17-413 good loop state}\\
&+\text{representation-safe bounded-length record windows}\\
&\Longrightarrow
\text{contradiction}.
\end{aligned}
}
\]

is closed.

## 9. What remains if the theorem cannot be applied

The retained loop branch must therefore escape through at least one of:

\[
\boxed{
\begin{aligned}
G_{nonminimal\ omega\text{-}limit},\\
G_{no\ robust\ away\text{-}zero\ coefficient\ loop\ state},\\
G_{tubular\ reach/self\text{-}clustering},\\
G_{flux/length\ decompactification},\\
G_{record\ scale\text{-}map/genealogy\ failure},\\
G_{interface/rank/domain\ loss}.
\end{aligned}
}
\]

This is strictly narrower than the previous generic sparse-recurrence exit.

## 10. Important scope firewall

M17-360 proves only that `omega(Z)` **contains** a minimal subset.

It does not prove

\[
\omega(Z)=\mathcal M.
\]

Therefore the present theorem must not be retroactively applied to all compact loop orbits.

The new decisive topological question is whether the full omega-limit set is minimal, or whether nonminimal omega-limit structure can be converted into another typed transition/genealogy mechanism.

## 11. DSD audit

The DSD role is to distinguish three notions:

1. recurrence of one limit point;
2. minimality of a compact invariant set;
3. quantitative occupation density of the original orbit.

Standard compact dynamics shows that (2), plus a robust open good set and full omega-limit identification, is strong enough to imply (3).

No DSD axiom is used.

## 12. Audit verdict

**PASS — conditional compact-dynamics closure.**

The minimal-full-omega-limit positive-flux loop branch is incompatible with the M17-405 finite raw-`H2` ancestor, provided one robust own-scale good loop state and the representation-safe record map persist.

The next target is the complementary case `omega(Z)` nonminimal: determine whether nested invariant subsets create a finite transition chain, a further compactness reduction, or an explicit genealogy/interface decompactification.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]