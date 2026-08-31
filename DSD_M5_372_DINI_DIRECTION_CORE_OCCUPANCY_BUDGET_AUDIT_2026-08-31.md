# DSD M5-372 — Dini-direction core split, occupancy reconnection, and budget audit

Date: 2026-08-31

Status: **THE `H_Dini/dir` SOURCE FROM M5-371 IS RECONNECTED TO THE EXISTING DERIVATIVE-OCCUPANCY AND ANGULAR-MULTISCALE LEDGERS / HIGH-VORTICITY CORE LOSS IS AN AMPLITUDE-DERIVATIVE EVENT, CORE DIRECTION TURNING IS A NORMALIZED DERIVATIVE OR MULTISCALE ANGULAR EVENT / NESTED-SCALE ENERGY CHARGING CANNOT BE SUMMED WITHOUT DOUBLE COUNTING / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-371 reduced the similarity-gradient escape to

\[
H_{\nabla,\rm sim}
\Longrightarrow
H_{\omega}
\lor H_{\rm Dini/dir}
\lor H_{\rm angular,multiscale}
\lor T_{\rm remote}.
\]

The open point was whether repeated Dini/directional events can be charged to a finite regularity budget.

This note does two things.

1. It separates full-vorticity Dini roughness into amplitude and direction channels without ever evaluating the vorticity direction where vorticity vanishes.
2. It audits the tempting energy-budget argument and shows exactly where nested-scale double counting or a one-derivative upgrade would enter.

The goal is source reduction, not a claim of global regularity.

## 2. Smooth pre-singular Dini control is already a derivative statement

Let

\[
\Omega=\nabla\times V
\]

be a smooth vorticity field at a pre-singular similarity time and define

\[
m_\Omega(x,r)
:=\sup_{|h|\le r}|\Omega(x+h)-\Omega(x)|.
\]

For every ball on which `Omega` is smooth,

\[
m_\Omega(x,r)
\le
r\,\|\nabla\Omega\|_{L^\infty(B_r(x))}.
\]

Hence

\[
\boxed{
\int_0^\rho \frac{m_\Omega(x,r)}{r}\,dr
\le
\int_0^\rho
\|\nabla\Omega\|_{L^\infty(B_r(x))}\,dr
\le
\rho\,\|\nabla\Omega\|_{L^\infty(B_\rho(x))}.
}
\]

Thus a large near-field Dini term at a smooth time is not a derivative-free phenomenon.

If the cutoff `rho` is fixed, divergence of the Dini term forces divergence of a vorticity-gradient norm.

If the cutoff shrinks with the singular scale, the scale-normalized quantity to track is

\[
\boxed{
h_1(x,\rho)
:=
\frac{\rho\,\|\nabla\Omega\|_{L^\infty(B_\rho(x))}}
{|\Omega(x)|}.
}
\]

This is the same structural type as the normalized first-vorticity-derivative witness already treated in the derivative-occupancy descent.

## 3. Amplitude-direction factorization on an intense-vorticity core

Write

\[
a(x)=|\Omega(x)|.
\]

Where `a>0`, define the direction

\[
\xi(x)=\frac{\Omega(x)}{|\Omega(x)|}.
\]

Let `x_*` be a point with

\[
a(x_*)=W>0,
\]

and fix

\[
0<\eta<1.
\]

Define the intense-vorticity core

\[
G_\eta
:=
\{x:a(x)\ge\eta W\}.
\]

This prevents the DSD-invalid operation of assigning a direction at `Omega=0`.

For `x_*+h\in G_eta`, the elementary normalized-vector inequality gives

\[
\boxed{
|\xi(x_*+h)-\xi(x_*)|
\le
\frac{2}{\eta W}
|\Omega(x_*+h)-\Omega(x_*)|.
}
\]

Also

\[
\boxed{
|a(x_*+h)-a(x_*)|
\le
|\Omega(x_*+h)-\Omega(x_*)|.
}
\]

Therefore, inside the intense core, full-vector roughness is resolved into amplitude and direction roughness with no undefined direction variable.

## 4. Leaving the intense core is already a derivative witness

Suppose instead that for some `h`,

\[
x_*+h\notin G_\eta.
\]

Then

\[
a(x_*+h)<\eta W,
\]

so

\[
|a(x_*+h)-a(x_*)|
>(1-\eta)W.
\]

By the mean-value theorem along the segment from `x_*` to `x_*+h`,

\[
\boxed{
\sup_{[x_*,x_*+h]}|\nabla a|
\ge
\frac{(1-\eta)W}{|h|}.
}
\]

At points where `a>0`,

\[
|\nabla a|\le |\nabla\Omega|,
\]

hence

\[
\boxed{
\frac{|h|}{W}
\sup_{[x_*,x_*+h]}|\nabla\Omega|
\ge
1-\eta.
}
\]

Thus loss of the high-vorticity core on scale `|h|` is not a new terminal mechanism.

It is an order-one normalized derivative event on that scale.

## 5. A finite direction turn inside the core is also a derivative witness

Assume `x_*+h\in G_eta` and define

\[
\delta_\xi(h)
:=
|\xi(x_*+h)-\xi(x_*)|.
\]

The inequality of Section 3 implies

\[
|\Omega(x_*+h)-\Omega(x_*)|
\ge
\frac{\eta W}{2}\delta_\xi(h).
\]

Another mean-value estimate yields

\[
\boxed{
\frac{|h|}{W}
\|\nabla\Omega\|_{L^\infty(B_{|h|}(x_*))}
\ge
\frac{\eta}{2}\delta_\xi(h).
}
\]

Hence an order-one direction turn on one scale is already an order-one normalized derivative witness.

This reconnects the single-scale part of `H_Dini/dir` to the derivative-occupancy ledger.

## 6. Dyadic Dini accumulation: one large derivative witness or many scale witnesses

Let

\[
r_k=2^{-k}\rho,
\qquad k=0,1,2,\ldots
\]

and define the intense-core direction modulus

\[
d_k
:=
\sup_{\substack{|h|\le r_k\\x_*+h\in G_\eta}}
|\xi(x_*+h)-\xi(x_*)|.
\]

Let

\[
G_k
:=
\|\nabla\Omega\|_{L^\infty(B_{r_k}(x_*))}.
\]

Then

\[
\boxed{
d_k\le \frac{2r_kG_k}{\eta W}.}
\]

The Dini integral is equivalent, up to universal logarithmic constants, to a dyadic sum of moduli. Therefore a large direction-Dini burden has only two typed possibilities:

1. one or more scales carry an order-one normalized derivative witness `r_k G_k/W`;
2. no single scale is large, but many small direction/derivative increments accumulate over an increasing number of scales.

The first returns to the derivative-occupancy branch.

The second is a genuinely multiscale angular/critical-tail branch and must be charged scale by scale without duplicating the same spatial mass.

Accordingly,

\[
\boxed{
H_{\rm Dini/dir}
\Longrightarrow
H_{\rm der/occ}
\lor
H_{\rm angular,multiscale}
\lor
T_{\rm core/window},
}
\]

where `T_core/window` denotes loss of a common local core/window during the comparison rather than a new analytic singularity type.

## 7. Reconnection to the existing occupancy-sparseness bridge

Return now to the original Navier-Stokes variables and let

\[
W(t)=\|\omega(t)\|_\infty.
\]

Use the viscous vorticity scale

\[
\boxed{
r=b\sqrt{\frac{\nu}{W(t)}}}
\]

with fixed dimensionless `b>0`.

Inside `B_r(x_*)`, let the intense core be

\[
G_\eta(t)=\{x:|\omega(x,t)|\ge\eta W(t)\}
\]

and define its volume occupancy

\[
\theta_r
:=
\frac{|G_\eta(t)\cap B_r(x_*)|}{|B_r|}.
\]

Define the viscosity-normalized critical local enstrophy

\[
\boxed{
\mathcal E_r(x_*,t)
:=
\frac{r}{\nu^2}
\int_{B_r(x_*)}|\omega(x,t)|^2dx.
}
\]

On the intense core,

\[
|\omega|\ge\eta W,
\]

so

\[
\mathcal E_r
\ge
\frac{r}{\nu^2}
\eta^2W^2\theta_r|B_r|.
\]

Since

\[
r=b\sqrt{\nu/W},
\]

we obtain the scale-free lower bound

\[
\boxed{
\mathcal E_r(x_*,t)
\ge
\frac{4\pi}{3}\eta^2 b^4\theta_r.
}
\]

Therefore avoiding strong sparseness at the natural vorticity scale forces an order-one critical local-enstrophy occupancy.

This is exactly the type of quantity already isolated in the 2026-08-12 vorticity occupancy-to-line-sparseness bridge.

## 8. Why the finite kinetic-energy dissipation ledger still does not close this branch

For Leray-Hopf solutions,

\[
\frac12\|u(t)\|_2^2
+
\nu\int_0^t\|\nabla u(s)\|_2^2ds
\le
\frac12\|u_0\|_2^2.
\]

For divergence-free whole-space fields,

\[
\|\nabla u\|_2^2=\|\omega\|_2^2.
\]

Thus the finite global budget is the time integral of enstrophy, not palinstrophy.

At the natural scale,

\[
\int_{B_r}|\omega|^2dx
\gtrsim
\eta^2\theta_r W^2r^3
\asymp
\eta^2\theta_r\nu^{3/2}W^{1/2}.
\]

Even if one grants persistence for one viscous-scale time

\[
\tau_r\asymp\frac{r^2}{\nu}\asymp\frac1W,
\]

the corresponding minimum kinetic-dissipation charge scales only like

\[
\nu\tau_r
\int_{B_r}|\omega|^2dx
\gtrsim
C(\eta,b,\theta_r,\nu)W^{-1/2}.
\]

For geometrically increasing first-hitting levels

\[
W_j=q^jW_0,
\qquad q>1,
\]

the series

\[
\sum_j W_j^{-1/2}
\]

is convergent.

Therefore a one-natural-scale occupancy event per first-hitting stage is compatible with a finite kinetic-energy dissipation ledger.

This is a structural reason that occupancy alone does not close global regularity.

## 9. Palinstrophy does control an `L2` Dini proxy, but that charge is circular for the global problem

On the high-vorticity set where both endpoints satisfy

\[
|\omega(x)|,|\omega(x+h)|\ge\Lambda>0,
\]

the normalized-vector inequality gives

\[
|\xi(x+h)-\xi(x)|
\le
\frac{2}{\Lambda}|\omega(x+h)-\omega(x)|.
\]

For smooth fields,

\[
\|\omega(\cdot+h)-\omega\|_2
\le
|h|\|\nabla\omega\|_2.
\]

Hence

\[
\boxed{
\|\delta_h\xi\|_{L^2(\text{high-vorticity overlap})}
\le
\frac{2|h|}{\Lambda}\|\nabla\omega\|_2.
}
\]

A dyadic `L2` Dini proxy can therefore be controlled by palinstrophy.

But the global regularity problem does not provide the a-priori finite budget

\[
\int_0^T\|\nabla\omega(t)\|_2^2dt<\infty
\]

through a hypothetical singular time.

This agrees with the 2026-08-25 derivative-occupancy descent: palinstrophy is a legitimate formed channel, but not a finite global contradiction budget.

Thus

\[
\boxed{
\text{Dini direction} \to \text{palinstrophy control}
}
\]

is mathematically useful but cannot be used as an unconditional closure step.

## 10. DSD no-double-counting audit for nested scales

A tempting argument is to assign an order-one critical local-enstrophy cost to every active dyadic scale and then sum over all scales.

This is not valid for nested balls.

The regions

\[
B_{r_0}(x_*)\supset B_{r_1}(x_*)\supset B_{r_2}(x_*)\supset\cdots
\]

contain the same vorticity mass repeatedly.

Therefore

\[
\sum_k \mathcal E_{r_k}
\]

is not a physical additive energy ledger.

Even if one passes to disjoint annuli and assumes comparable amplitude on all of them, the raw volume costs scale geometrically like

\[
\sum_k W^2r_k^3,
\]

which is dominated by the largest occupied scale rather than growing linearly with the number of scales.

Consequently, an increasing Dini/logarithmic scale count cannot be converted into an increasing finite-energy price merely by summing nested occupancy estimates.

This is the principal DSD audit correction of the present checkpoint.

## 11. Formation-analysis interpretation

The Dini source is now typed by where the loss of regular description occurs.

### Amplitude formation loss

The intense-vorticity core terminates within the comparison scale.

Then the amplitude changes by order `W`, forcing a normalized derivative witness and potentially feeding the occupancy/sparseness channel.

### Directional formation loss

The intense core persists, but `xi` rotates within it.

A single finite turn forces a normalized derivative witness; many small turns feed the multiscale angular ledger.

### Window/ancestry loss

The required common local comparison window is not retained across the scales or times.

This is a turnover/compactness channel and must not be silently treated as direction roughness.

## 12. Axis-property interpretation

The direction field `xi` is not merely a regularity label.

The productive longitudinal vortex stretching isolated earlier contains the relative-angle factor represented schematically by

\[
\sin\theta.
\]

Therefore a surviving core-direction event must eventually be audited not only for roughness magnitude but for whether the turning produces the strain component that actually amplifies vorticity.

This prevents overcounting harmless directional oscillation as productive stretching.

## 13. Updated proof-tree reduction

Combining M5-371 with the present reconnection gives

\[
\boxed{
H_{\nabla,\rm sim}
\Longrightarrow
H_{\omega,\infty}
\lor
H_{\rm der/occ}
\lor
H_{\rm angular,multiscale}
\lor
T_{\rm remote/core}.
}
\]

The explicit `H_Dini/dir` label is no longer needed as an independent terminal leaf.

Its single-scale content is derivative occupancy; its diffuse content is multiscale angular accumulation; its loss-of-domain content is turnover.

## 14. Exact remaining budget obligation

To close the surviving direction/multiscale route one needs a quantity `Q_j` with all three properties:

1. **event lower bound** — every genuinely new productive angular/Dini event forces `Q_j >= c > 0` after normalization;
2. **non-overlap/additivity** — different scales or first-hitting stages cannot charge the same physical mass repeatedly;
3. **finite a-priori ledger** — `sum_j Q_j < infinity` follows from Leray-Hopf-level information or another already proved finite quantity, without importing palinstrophy or a regularity criterion equivalent to the desired conclusion.

No such `Q_j` has been derived here.

A natural next test is a frequency-separated angular-increment ledger, because Littlewood-Paley orthogonality is one possible way to avoid nested spatial double counting. It must still overcome localization and high-vorticity occupancy issues.

## 15. DSD audit verdict

### PROVED / ELEMENTARY

- smooth Dini modulus is bounded by a vorticity-gradient norm;
- high-vorticity core exit forces an order-one normalized derivative witness;
- finite direction turn inside the core forces a normalized derivative witness;
- natural-scale non-sparse occupancy forces an order-one critical local-enstrophy quantity;
- an `L2` direction-increment proxy is controlled by palinstrophy;
- nested spatial occupancy charges are not additive and cannot be summed naively.

### RECONNECTED TO EXISTING LEDGERS

- single-scale Dini/direction roughness -> derivative occupancy;
- low occupancy -> occupancy/sparseness geometry;
- diffuse many-scale direction turning -> angular/multiscale ledger;
- loss of a common core/window -> turnover/compactness ledger.

### NOT DERIVED

- a finite global palinstrophy budget;
- a non-overlapping energy-level charge for every multiscale direction event;
- an a-priori mechanism forcing natural-scale sparseness at every sufficiently late first hit;
- exclusion of the surviving angular/multiscale or turnover branches;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
