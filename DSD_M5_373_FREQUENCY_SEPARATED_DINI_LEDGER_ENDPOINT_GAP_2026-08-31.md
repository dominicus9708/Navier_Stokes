# DSD M5-373 — Frequency-separated Dini ledger: the scale-summability endpoint gap

Date: 2026-08-31

Status: **LITTLEWOOD-PALEY/FREQUENCY SEPARATION REMOVES THE MOST OBVIOUS NESTED-SPATIAL DOUBLE COUNTING, BUT BARE ENERGY STILL DOES NOT CONTROL A Dini-TYPE LINEAR SCALE ACCUMULATION / THE OBSTRUCTION IS AN `ell^2`-TO-`ell^1` ENDPOINT GAP, WITH AN ADDITIONAL SPATIAL-CAPACITY GAP FOR POINTWISE DIRECTION EVENTS / POSITIVE DERIVATIVE WEIGHT REPAIRS SCALE SUMMABILITY BUT RETURNS TO THE PALINSTROPHY/HIGHER-REGULARITY LEDGER / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-372 identified the exact remaining budget obligation for the Dini/angular branch:

- event costs must not reuse the same nested spatial mass;
- the total cost must be finite from an already available a-priori ledger;
- the cost cannot assume palinstrophy or another regularity quantity equivalent to the desired conclusion.

A natural candidate is frequency separation.

Dyadic Fourier blocks are orthogonal in `L2`, so they avoid the most obvious nested-ball double counting.

This note tests whether that alone is enough.

The answer is no: it exposes an endpoint summability gap.

## 2. Dyadic vorticity energy ledger

Let

\[
\omega=\sum_{k\in\mathbb Z}\omega_k,
\qquad
\omega_k=P_k\omega,
\]

be a standard Littlewood-Paley decomposition into dyadic frequency shells.

For smooth finite-energy fields, Plancherel and almost orthogonality give schematically

\[
\boxed{
\|\omega\|_2^2
\asymp
\sum_k\|\omega_k\|_2^2.
}
\]

For Leray-Hopf solutions,

\[
\nu\int_0^T\|\omega(t)\|_2^2dt<\infty,
\]

hence

\[
\boxed{
\nu\int_0^T
\sum_k\|\omega_k(t)\|_2^2dt
<\infty.
}
\]

This is a genuine non-double-counted scale ledger.

The issue is what type of scale sum a Dini event asks us to control.

## 3. Dini accumulation is linear in scale contributions

A modulus-of-continuity Dini quantity has the form

\[
\int_0^\rho\frac{m(r)}{r}dr.
\]

On dyadic radii

\[
r_k=2^{-k}\rho,
\]

monotonicity of the modulus gives the standard comparison

\[
\boxed{
\int_0^\rho\frac{m(r)}{r}dr
\asymp
\sum_{k\ge0}m(r_k)
}
\]

up to universal constants when the sum/integral is interpreted on the same finite or infinite scale range.

Thus Dini roughness is a **linear accumulation across scales**.

Frequency energy, in contrast, is a quadratic accumulation.

This distinction survives even under ideal orthogonality.

## 4. Finite-scale endpoint counter-audit

Suppose optimistically that after all spatial localization and high-vorticity occupancy issues have been solved, the normalized event amplitude on each active scale is represented by a nonnegative number `a_k` and that the energy ledger controls

\[
\sum_{k=1}^N a_k^2.
\]

A Dini-type burden would require control of

\[
\sum_{k=1}^N a_k.
\]

There is no uniform bound of the latter by the former independent of the number of active scales.

Indeed take

\[
a_k=N^{-1/2},
\qquad 1\le k\le N.
\]

Then

\[
\boxed{
\sum_{k=1}^N a_k^2=1,
}
\]

while

\[
\boxed{
\sum_{k=1}^N a_k=\sqrt N\to\infty.
}
\]

Therefore even **perfect frequency orthogonality plus a fixed quadratic energy budget** does not bound a linear Dini accumulation when the number of active scales grows.

This is not a Navier-Stokes counterexample.

It is a counterexample to the proposed abstract ledger inequality

\[
\ell^2_{\rm scale}\Longrightarrow\ell^1_{\rm scale}
\]

with a scale-independent constant.

## 5. Infinite-scale version

The same obstruction persists on infinitely many scales.

Choose for example

\[
a_k=\frac1k,
\qquad k\ge1.
\]

Then

\[
\sum_{k=1}^\infty a_k^2<\infty,
\]

but

\[
\sum_{k=1}^\infty a_k=\infty.
\]

Thus square-summable scale energy is compatible with a non-summable linear scale burden.

The DSD meaning is direct:

**removing spatial double counting is necessary, but it is not sufficient.**

A second mechanism must control the number or strength of active scales.

## 6. Why one positive derivative repairs the scale sum

Let

\[
a_k=\|P_k\omega\|_2.
\]

A palinstrophy-level quantity has the dyadic form

\[
\|\nabla\omega\|_2^2
\asymp
\sum_k2^{2k}a_k^2.
\]

On high frequencies `k>=K`, Cauchy-Schwarz gives

\[
\begin{aligned}
\sum_{k\ge K}a_k
&=
\sum_{k\ge K}2^{-k}(2^ka_k)\\
&\le
\left(\sum_{k\ge K}2^{-2k}\right)^{1/2}
\left(\sum_{k\ge K}2^{2k}a_k^2\right)^{1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{k\ge K}\|P_k\omega\|_2
\lesssim
2^{-K}\|\nabla\omega\|_2.
}
\]

More generally, any positive Sobolev derivative `s>0` supplies a geometric weight `2^{-sk}` and repairs the bare `ell^2 -> ell^1` scale-summability failure at high frequencies.

This exactly matches M5-372:

- palinstrophy controls an `L2` Dini proxy;
- the control works because the derivative supplies the missing summability weight;
- but global palinstrophy is not an available a-priori finite ledger through a hypothetical singularity.

Thus the frequency calculation does not remove the circularity; it explains it.

## 7. Pointwise direction events have a second, spatial-capacity gap

The actual M5-371/M5-372 event is not merely an `L2` scale amplitude.

It concerns vorticity direction near a high-vorticity point.

On a core where

\[
|\omega|\ge\Lambda>0,
\]

M5-372 proved

\[
|\delta_h\xi|
\le
\frac{2}{\Lambda}|\delta_h\omega|.
\]

However a pointwise or very small-set direction turn need not force an order-one **global** `L2` increment unless the event occupies enough spatial measure.

If an event set `E` satisfies

\[
|\delta_h\xi|\ge\delta>0,
\qquad
|\omega(x)|,|\omega(x+h)|\ge\Lambda
\]

on `E`, then the reverse consequence is

\[
|\delta_h\omega|
\ge
\frac{\Lambda\delta}{2}
\]

on `E`, so

\[
\boxed{
\|\delta_h\omega\|_2^2
\ge
\frac{\Lambda^2\delta^2}{4}|E|.
}
\]

Thus a frequency-energy charge requires a lower bound on the measure/capacity of `E`.

Without such an occupancy bridge, a highly localized pointwise direction event can be invisible to the global quadratic ledger.

Therefore the frequency candidate exposes **two independent endpoint deficits**:

1. spatial deficit: pointwise/capacity information must be converted to `L2` mass;
2. scale deficit: linear Dini accumulation must be converted to a quadratic/additive scale budget.

## 8. Difference multipliers show why raw increments still reuse high frequencies

For a translation difference

\[
\delta_h\omega(x)=\omega(x+h)-\omega(x),
\]

its Fourier multiplier is

\[
e^{ih\cdot\zeta}-1.
\]

On dyadic block `q`, its magnitude is bounded schematically by

\[
\min\{1,|h|2^q\}.
\]

Consequently

\[
\boxed{
\|\delta_h\omega\|_2^2
\lesssim
\sum_q
\min\{1,(|h|2^q)^2\}
\|P_q\omega\|_2^2.
}
\]

If `|h|~2^{-k}`, then every much higher frequency `q>>k` enters with weight of order one.

Thus raw spatial increments at many coarse scales can still be generated by the same high-frequency block.

Frequency decomposition makes this reuse visible, but does not automatically assign each direction event to a unique band.

A stopping-time or Carleson-type assignment would be needed to obtain a genuinely non-reused event ledger.

## 9. Besov interpretation of the endpoint gap

At the schematic `L2` scale level,

\[
\left(\sum_k\|P_k\omega\|_2^2\right)^{1/2}
\]

is the `B^0_{2,2}` / `L2` type quantity supplied by energy.

A linear frequency sum

\[
\sum_k\|P_k\omega\|_2
\]

is of `B^0_{2,1}` type.

The strict scale-summability distinction

\[
\boxed{
\ell^2\not\subset\ell^1
}
\]

is exactly the obstruction found above.

For the true pointwise Dini modulus the spatial norm is stronger still; one cannot silently replace the pointwise direction problem by the easier `B^0_{2,1}` proxy.

This section is an interpretation of the ledger structure, not an assertion that the original direction-Dini quantity equals a global `B^0_{2,1}` norm.

## 10. DSD analysis: two axes must remain separate

The candidate frequency ledger clarifies two different descriptive axes.

### Spatial support/capacity axis

How much physical region carries the high-vorticity directional event?

This is handled by the occupancy/sparseness ledger.

### Scale multiplicity/summability axis

How many independent frequency scales carry productive directional increments, and how are their costs summed?

This is not answered by occupancy alone.

Combining the two into one vague statement such as `many rough scales cost energy` would hide the missing implication.

DSD therefore requires the state to retain at least

\[
(\text{event amplitude},\text{occupied capacity},\text{frequency scale},\text{time interval},\text{productive angle}).
\]

## 11. Axis-property audit: only productive angular increments matter

The vortex-stretching branch isolated earlier contains a relative-angle factor.

Therefore the scale event to be charged cannot be every oscillation of `xi`.

It must be a **productive angular increment** that contributes to the longitudinal strain/vorticity amplification channel.

This can only reduce the event set; it cannot repair the `ell^2 -> ell^1` failure by itself unless a cancellation, sign, orthogonality, or packing theorem is derived from the Navier-Stokes dynamics.

Accordingly, a future angular ledger must distinguish

\[
\boxed{
\text{geometric direction roughness}
\neq
\text{productive stretching contribution}.
}
\]

## 12. What frequency separation accomplishes and what it does not

### It accomplishes

- an additive quadratic scale-energy identity;
- explicit visibility of which frequencies are being reused by a spatial increment;
- a possible framework for a stopping-time or Carleson packing argument;
- a precise location for the missing scale-summability estimate.

### It does not accomplish

- conversion of pointwise direction turning to positive-measure `L2` occupancy;
- a uniform `ell^1` Dini bound from an `ell^2` energy budget;
- exclusion of infinitely many weak active scales;
- a finite palinstrophy budget;
- global regularity.

## 13. Updated remaining obligation

The `Q_j` sought in M5-372 must now overcome both endpoint gaps.

A viable closure quantity would need a bound of the schematic form

\[
\boxed{
\sum_{\text{productive events }e}Q_e
\le
C(u_0,\nu)
}
\]

while each singular first-hitting stage forces

\[
\sum_{e\in\text{stage }j}Q_e\ge c_q>0.
\]

To avoid the present no-go, `Q_e` cannot be merely the square root of a dyadic energy contribution summed linearly over unrestricted scales.

At least one additional dynamical property is needed, for example:

1. a Carleson/packing bound on active scale-time boxes;
2. lacunarity of productive angular scales;
3. sign/cancellation that makes productive angular contributions square-summable rather than absolutely summable;
4. a scale-time occupancy theorem that assigns disjoint positive capacity to each new event;
5. an endpoint estimate generated directly by the vortex-stretching structure rather than by generic Dini control.

These are candidate obligations, not derived facts.

## 14. Proof-tree consequence

M5-373 does not create a new singular mechanism.

It closes one proposed **closure strategy**:

\[
\boxed{
\text{bare frequency orthogonality}
+
\text{Leray energy}
\not\Rightarrow
\text{uniform Dini/angular scale budget}.
}
\]

The surviving route is therefore narrower:

\[
\boxed{
H_{\rm angular,multiscale}
\to
\text{productive angular packing/cancellation problem}
}
\]

rather than a generic energy-per-frequency argument.

## 15. DSD audit verdict

### PROVED / STANDARD HARMONIC-ANALYSIS ACCOUNTING

- dyadic `L2` energy is square-summable across frequency shells;
- linear scale accumulation cannot be bounded uniformly by that square sum as the number of active scales grows;
- explicit finite and infinite sequence witnesses demonstrate the `ell^2/ell^1` gap;
- a positive derivative weight repairs high-frequency linear summability;
- spatial direction events require an occupancy/capacity lower bound before they can be charged to global `L2` energy;
- raw translation differences reuse all higher frequencies and therefore are not themselves a unique-band ledger.

### AUDIT CLOSURE

- the naive `Littlewood-Paley orthogonality alone will make the Dini budget finite` strategy is closed;
- nested spatial double counting can be exposed by frequency separation, but scale summability remains open.

### OPEN

- a non-circular productive-angular Carleson/packing estimate;
- a dynamical lacunarity or cancellation law for active angular scales;
- a scale-time capacity assignment with a finite Leray-level total budget;
- exclusion of the angular/multiscale and turnover survivors;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
