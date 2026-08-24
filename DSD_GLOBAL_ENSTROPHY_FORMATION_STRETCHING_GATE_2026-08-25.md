# DSD global enstrophy formation / stretching gate

Date: 2026-08-25

Status: **BOUNDARY-TRANSFER ESCAPE REMOVED AT WHOLE-SPACE LEVEL / FIXED-GAP GLOBAL STRETCHING CHARGE PROVED ON BOUNDED-Z FIRST-HITTING BRANCH / TOTAL STRETCHING DIVERGENCE NECESSARY / NO FINITE STRETCHING BUDGET DERIVED / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_FIRST_HITTING_MATERIAL_FORMATION_RETURN_GATE_2026-08-25.md`. The material-cell gate left two positive supply channels for a newly formed high-vorticity cell: bulk stretching or viscous influx across the material boundary. The present calculation uses the bounded-Z global ceiling to remove the boundary-transfer alternative after a sufficiently large but finite first-hitting gap.

## 1. Normalized enstrophy channel

At first-hitting stage `j`, use

\[
\Omega_j(y)=\frac{\omega(X_j+r_jy,t_j)}{W_j},
\qquad
r_j=\left(\frac\nu{W_j}\right)^{1/2}.
\]

A change of variables gives

\[
\boxed{
\|\Omega_j\|_2^2
=\frac{r_j}{\nu^2}\|\omega(t_j)\|_2^2.
}
\]

On the bounded-Z branch assume

\[
\boxed{\|\Omega_j\|_2^2\le Z_*}
\]

for the late first-hitting sequence under consideration.

Hence

\[
\boxed{
\|\omega(t_j)\|_2^2
\le Z_*\frac{\nu^2}{r_j}.
}
\]

## 2. Analytic occupied core gives a normalized enstrophy floor

The first-hitting analytic occupied ball satisfies

\[
|\Omega_n(y)|\ge\frac12
\qquad(y\in B_{r_a}(0)).
\]

Therefore

\[
\boxed{
\|\Omega_n\|_2^2
\ge z_a,
\qquad
z_a:=\frac\pi3r_a^3>0.
}
\]

Equivalently,

\[
\boxed{
\|\omega(t_n)\|_2^2
\ge z_a\frac{\nu^2}{r_n}.
}
\]

This is a whole-space lower bound because the occupied ball is a subset of the whole space.

## 3. A finite generation gap makes the future core exceed the entire earlier enstrophy ceiling

Let

\[
n=j+k.
\]

Since

\[
W_n=q^kW_j,
\]

we have

\[
\boxed{r_j=q^{k/2}r_n.}
\]

The earlier global enstrophy ceiling becomes

\[
\|\omega(t_j)\|_2^2
\le
Z_*q^{-k/2}\frac{\nu^2}{r_n}.
\]

Choose a finite integer

\[
\boxed{
k_Z:=\min\left\{k\in\mathbb N:
Z_*q^{-k/2}\le\frac{z_a}{2}
\right\}.}
\]

Then for every late `j`, with `n=j+k_Z`,

\[
\boxed{
\|\omega(t_n)\|_2^2
-\|\omega(t_j)\|_2^2
\ge
\frac{z_a}{2}\frac{\nu^2}{r_n}.
}
\]

Thus after the fixed finite gap `k_Z`, the final analytic core alone carries more enstrophy than the bounded-Z ceiling permits for the entire earlier field.

No redistribution across a material boundary can explain this whole-space increase.

Status: **PROVED under the bounded-Z first-hitting hypotheses.**

## 4. Whole-space enstrophy identity removes boundary influx

For every smooth pre-singular interval,

\[
\boxed{
\frac12\frac d{dt}\|\omega(t)\|_2^2
+\nu\|\nabla\omega(t)\|_2^2
=
\int_{\mathbb R^3}\omega^TS\omega\,dx.
}
\]

Integrating from `t_j` to `t_n`,

\[
\begin{aligned}
\int_{t_j}^{t_n}\int\omega^TS\omega\,dxdt
={}&
\frac12\left(
\|\omega(t_n)\|_2^2-\|\omega(t_j)\|_2^2
\right)\\
&+\nu\int_{t_j}^{t_n}\|\nabla\omega(t)\|_2^2dt.
\end{aligned}
\]

The palinstrophy term is nonnegative. Therefore for the fixed gap `k_Z`,

\[
\boxed{
\mathcal S_{j,n}^{glob}
:=
\int_{t_j}^{t_n}\int_{\mathbb R^3}\omega^TS\omega\,dxdt
\ge
c_Z\frac{\nu^2}{r_n},
\qquad
c_Z:=\frac{z_a}{4}>0.
}
\]

This is a lower bound for the **signed** global vortex-stretching production, not merely its absolute value.

Hence the material-cell boundary-influx survivor is removed at the whole-space formation level:

\[
\boxed{
\text{bounded-Z first-hitting formation over }k_Z\text{ generations}
\Longrightarrow
\text{positive global vortex-stretching creation}.
}
\]

Status: **PROVED.**

## 5. Disjoint finite blocks force divergent total stretching toward a hypothetical singular time

Select disjoint generation blocks

\[
j_m=j_0+mk_Z,
\qquad
n_m=j_m+k_Z.
\]

Their physical time intervals

\[
[t_{j_m},t_{n_m}]
\]

are disjoint up to endpoints.

For each block,

\[
\mathcal S_m^{glob}
\ge
c_Z\frac{\nu^2}{r_{n_m}}.
\]

Since

\[
r_{n_m}
=r_{n_0}q^{-mk_Z/2},
\]

one has

\[
\sum_m\frac1{r_{n_m}}=\infty.
\]

Therefore any hypothetical singular branch satisfying the stated bounded-Z and analytic-core hypotheses must obey

\[
\boxed{
\int_{t_{j_0}}^{T^*}\int_{\mathbb R^3}\omega^TS\omega\,dxdt
=+\infty
}
\]

in the sense that its partial integrals over the disjoint first-hitting blocks diverge to `+infinity`.

Moreover the enstrophy identity shows that the integrated global palinstrophy may also diverge; no finiteness claim is made for it.

Status: **PROVED AS A NECESSARY CONSEQUENCE OF THE BRANCH HYPOTHESES.**

## 6. DSD interpretation

The previous material-cell gate classified positive boundary influx as a possible **reorganization/transfer** channel. At the whole-space base there is no finite boundary, so internal viscous transfer cancels from the global aggregation. What remains is a true **formation/source** channel:

\[
\boxed{\omega^TS\omega.}
\]

Thus the DSD hierarchy is now:

\[
\text{finite first-hitting formation witness}
\to
\text{material-cell stretching or transfer}
\to
\text{whole-space positive stretching creation}.
\]

This removes the auxiliary derivative ladder and the material-boundary transfer as primitive terminal survivors on the bounded-Z branch.

## 7. Why this is not yet a contradiction

The basic kinetic-energy inequality controls

\[
\int_0^{T^*}\|\nabla u(t)\|_2^2dt,
\]

but it does not supply a finite a-priori bound for

\[
\int_0^{T^*}\int\omega^TS\omega\,dxdt.
\]

Indeed the whole-space enstrophy identity allows the stretching integral and palinstrophy integral to diverge together near a hypothetical singularity.

The elementary estimate

\[
\left|\int\omega^TS\omega\right|
\lesssim
\int|\nabla u|^3
\]

returns to a critical cubic first-derivative channel. Re-entering the old derivative-persistence ladder from here would recreate the previously audited methodological loop without adding a new budget.

Therefore the next DSD step must **not** simply repeat the derivative-descent tree. It must test the stretching channel itself for a finite formation/aggregation constraint that is not equivalent to the already-used local concentration estimates.

## 8. New Budget-Closure Gate

The remaining bounded-Z proof obligation is now sharply reduced to:

\[
\boxed{
\text{Can positive global vortex-stretching production of size }
\nu^2/r_n
\text{ on every fixed-gap first-hitting block be globally recycled without violating another formed finite channel?}
}
\]

Call a non-circular estimate answering this the **Stretching Budget-Closure Gate (SBCG)**.

Current status:

\[
\boxed{\text{SBCG: NOT DERIVED.}}
\]

A valid SBCG cannot merely replace `omega^T S omega` by `|nabla u|^3` and then invoke the already-audited derivative ladder; that is the route from which the DSD audit has just exited.

## 9. Audit verdict

### PROVED

- normalized bounded-Z gives the physical global enstrophy ceiling `Z_* nu^2/r_j`;
- analytic first-hitting occupancy gives a fixed normalized enstrophy floor `z_a`;
- after a fixed finite gap `k_Z`, the future occupied core exceeds the entire earlier global enstrophy ceiling;
- whole-space boundary transfer therefore cannot account for the formation;
- each disjoint `k_Z`-generation block carries a positive signed global stretching charge `>= c_Z nu^2/r_n`;
- the sum of those required stretching charges diverges toward a hypothetical singular time.

### NOT DERIVED

- a finite a-priori global budget for vortex stretching;
- a non-circular SBCG;
- contradiction to the hypothetical singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
