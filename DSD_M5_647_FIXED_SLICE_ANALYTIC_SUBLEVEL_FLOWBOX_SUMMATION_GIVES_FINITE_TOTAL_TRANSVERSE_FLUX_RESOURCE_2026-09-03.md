# DSD M5-647 — Fixed-slice analytic sublevel / flow-box summation gives a finite total transverse-flux resource

Date: 2026-09-03

Status: **CONDITIONAL-ON-STANDARD-REAL-ANALYTIC-GEOMETRY LEMMA / ON ONE FIXED BASE SIMILARITY TIME, THE NONTRIVIAL ANALYTIC VORTICITY FIELD HAS A POWER-LAW SMALL-AMPLITUDE SUBLEVEL VOLUME BOUND ON EVERY FIXED COMPACT RESERVOIR; COMBINED WITH A QUANTITATIVE FLOW-BOX RADIUS PROPORTIONAL TO THE LOCAL VORTICITY AMPLITUDE, A DYADIC AMPLITUDE DECOMPOSITION PRODUCES A COUNTABLE COMPLETE TRANSVERSE ATLAS WHOSE TOTAL ABSOLUTE VORTICITY-FLUX MASS IS FINITE / NO UNIFORM LOJASIEWICZ EXPONENT OVER THE WHOLE HULL IS CLAIMED OR NEEDED / THIS REMOVES THE ANALYTIC ZERO SET AS AN INFINITE-FLUX-RESOURCE ESCAPE FOR THE FIXED BASE SLICE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why only one fixed slice is needed

M5-642 showed that for a sufficiently large fixed radius `R_out`, the similarity material velocity

\[
B=U+\frac12 y
\]

has strictly outward normal component on `S_{R_out}`.

Therefore every material label that participates in a future retained-core packet is already contained, at one chosen base time `theta_0`, in the fixed reservoir

\[
K:=\overline{B_{R_{out}}}.
\]

Hence the flux-resource question can be asked entirely on the single field

\[
W_0(y):=W(y,\theta_0).
\]

No uniform real-analytic geometry over the entire recurrent hull is required.

---

## 2. Analytic input

For `theta_0` in the smooth ancient CE-H branch, `W_0` is real analytic in space.

Let

\[
f(y):=|W_0(y)|^2.
\]

The marked component is nontrivial, so `f` is not identically zero.

Let

\[
Z:=\{y\in K:W_0(y)=0\}=\{f=0\}\cap K.
\]

A standard Lojasiewicz distance inequality for a real-analytic function on a compact set gives finite constants `m>=1`, `c_L>0` such that locally around the zero set, after a finite compact cover,

\[
\boxed{
 f(y)\ge c_L\,\operatorname{dist}(y,Z)^m.
}
\]

Equivalently,

\[
|W_0(y)|\le \varepsilon
\quad\Longrightarrow\quad
\operatorname{dist}(y,Z)
\le C_L\varepsilon^{2/m}.
\]

The real-analytic zero set is locally subanalytic and has dimension at most two unless `f` vanishes identically.

A finite stratification/tubular-neighborhood estimate on the fixed compact set therefore yields some `beta>0` with

\[
\big|\{\operatorname{dist}(y,Z)<r\}\cap K\big|
\le C_Z r^\beta
\]

for sufficiently small `r`.

Combining the two estimates gives

\[
\boxed{
\left|\{|W_0|\le\varepsilon\}\cap K\right|
\le C\varepsilon^\alpha
}
\]

for some fixed `alpha>0` depending on this base slice and reservoir.

Only existence of a positive exponent is used below.

---

## 3. Firewall: no uniform exponent over the hull

The compact smooth hull does not by itself give a uniform Lojasiewicz exponent for all states.

That stronger assertion is neither proved nor needed.

All future labels are pulled back to the same fixed base field `W_0`, so one fixed-slice exponent `alpha>0` suffices.

---

## 4. Dyadic amplitude shells

For all sufficiently large integers `n`, define

\[
\boxed{
K_n:=\left\{
2^{-n-1}<|W_0|\le2^{-n}
\right\}\cap K.
}
\]

Then

\[
|K_n|\le C2^{-\alpha n}.
\]

Let

\[
M_1:=\|\nabla W_0\|_{L^\infty(K)}<\infty.
\]

Choose the quantitative flow-box scale

\[
\boxed{
r_n:=c_0\frac{2^{-n}}{1+M_1}
}
\]

with `c_0` sufficiently small.

If `y_n\in K_n`, then on `B(y_n,r_n)` the Lipschitz bound gives

\[
|W_0(y)|\asymp2^{-n}
\]

and the vorticity direction varies only by a fixed controlled angle.

Thus each such ball admits a standard local flow box with a transverse disk of radius comparable to `r_n`.

---

## 5. Cover number

Use a maximal disjoint family of balls `B(y_a,r_n/5)` centered in `K_n`.

The corresponding `B(y_a,r_n)` cover `K_n`.

Because the enlarged balls remain inside a comparable small-amplitude sublevel set,

\[
N_n r_n^3
\lesssim
\left|\{|W_0|\lesssim2^{-n}\}\cap K\right|
\lesssim2^{-\alpha n}.
\]

Since `r_n\asymp2^{-n}`,

\[
\boxed{
N_n\lesssim 2^{(3-\alpha)n}.
}
\]

---

## 6. Flux mass of one transverse disk

Let `D_{n,a}` be a transverse disk in one such flow box, chosen with its normal consistently oriented with `W_0`.

Then

\[
\int_{D_{n,a}}|W_0\cdot n|\,dA
\lesssim
2^{-n}r_n^2
\lesssim2^{-3n}.
\]

Therefore the full dyadic shell contributes at most

\[
\boxed{
\sum_{a=1}^{N_n}
\int_{D_{n,a}}|W_0\cdot n|\,dA
\lesssim
2^{-\alpha n}.
}
\]

The series converges:

\[
\sum_{n\ge n_0}2^{-\alpha n}<\infty.
\]

---

## 7. Moderate/high-amplitude region

On

\[
K_{hi}:=K\cap\{|W_0|\ge2^{-n_0-1}\},
\]

there is a fixed positive lower bound on `|W_0|`.

A finite flow-box cover exists by compactness.

The sum of the absolute flux masses of the finitely many associated transverse disks is finite.

Combining this finite part with the convergent dyadic low-amplitude sum gives a countable transverse atlas

\[
\mathcal T=\{D_a\}_{a\in\mathbb N}
\]

covering `K\setminus Z` by vortex flow boxes and satisfying

\[
\boxed{
\|\mu_{flux}\|(\mathcal T)
:=
\sum_a\int_{D_a}|W_0\cdot n_a|\,dA
<\infty.
}
\]

This is the required finite-total-flux resource.

---

## 8. Why the zero set itself carries no missing flux

On `Z`,

\[
W_0=0.
\]

Hence the vorticity flux density itself vanishes there.

The countable flow-box atlas approaches `Z` through dyadic shells with a summable total absolute flux cost.

Thus the analytic zero set cannot hide an infinite amount of transverse vorticity-flux resource on the fixed base slice.

---

## 9. Holonomy / chart overlap audit

M5-644--645 already showed that on regular Clebsch charts the transverse flux form is

\[
d\kappa\wedge d\psi
\]

and is invariant under chart transitions `psi_j=psi_i+F_{ij}(kappa)`.

M5-646 then removed `grad kappa=0` as an obstruction by using ordinary vortex flow boxes wherever `W_0!=0`.

The present construction does not require one global single-valued Clebsch potential.

Overlaps may overcount flux in the definition of `||mu_flux||(T)`, but overcounting only increases the finite upper resource bound and is therefore harmless for the later contradiction argument.

---

## 10. What this lemma does not yet prove

A finite complete transverse-flux resource alone does not imply that infinitely many future packet events are impossible.

One still needs to prove that each strongly-negative packet event consumes a fixed positive amount of this base-slice resource, in a way that cannot be recycled indefinitely by the same vortex leaves.

The natural mechanism is the CE-H negative-level material-flux law:

\[
\Phi'=\bar\kappa_\Phi\Phi.
\]

On the `kappa<0` relabeling population, flux is forward-monotone decreasing.

The next document should charge every time-thickened strongly-negative packet event against a fixed irreversible decrease of the finite base transversal measure.

---

## 11. External theorem dependencies

This note depends on standard results from real-analytic/subanalytic geometry:

1. the Lojasiewicz distance inequality for a nonzero real-analytic function on a fixed compact set;
2. finite stratification / tubular-neighborhood volume control for a fixed compact real-analytic zero set;
3. the ordinary local flow-box theorem, used quantitatively under a positive lower bound on `|W_0|` and a finite Lipschitz bound.

No Navier-Stokes regularity theorem beyond the already inherited spatial analyticity of the ancient smooth branch is introduced here.

---

## 12. Updated resource frontier

The previous obstruction

\[
\text{future packets may accumulate on }\{W_0=0\}
\]

is replaced by

\[
\boxed{
\text{all future retained-core vortex labels pull back into a fixed finite-total-flux transverse resource }\mathcal T.
}
\]

The remaining task is purely dynamical:

\[
\boxed{
\text{strongly-negative recurrent packet events}
\stackrel{?}{\Longrightarrow}
\text{fixed irreversible flux consumption per event}.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]