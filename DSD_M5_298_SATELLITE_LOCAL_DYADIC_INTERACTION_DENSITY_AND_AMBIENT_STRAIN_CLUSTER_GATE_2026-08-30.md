# DSD M5-298 — Satellite-Local Dyadic Interaction Density and Ambient-Strain Cluster Gate

Date: 2026-08-30

Parent: `DSD_M5_297_MORREY_SPARSE_CLOUD_MAIN_CORE_FAR_STRAIN_DECAY_AND_ANGULAR_CANCELLATION_SCOPE_CORRECTION_2026-08-30.md`

Status: **FORMATION LOCAL-INTERACTION DESCRIPTOR / MAIN-CORE FAR STRAIN DECAYS, BUT SATELLITE-LOCAL NEIGHBOR INTERACTIONS ARE CRITICAL / THE NATURAL DYADIC INTERACTION DENSITY IS `I_loc = sum 2^{-3k} N_k`; NONCANCELLING DIVERGENCE ROUTES TO `H_sat-local`, WHILE BOUNDED INTERACTION DENSITY IS THE CORRECT AMBIENT-STRAIN INPUT FOR DETACHED ANCIENT COMPACTNESS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why the observation center must change

M5-297 shows that a Morrey-sparse cloud at distance `d=L ell` has negligible aggregate strain at the original main core.

This does **not** imply that one satellite sees negligible strain from the other satellites.

At a chosen satellite center `y_0`, neighboring packets may lie at distances comparable to only a few multiples of `ell`.

Therefore the relevant Formation descriptor is local interaction density around each satellite, not the total cloud count alone.

---

## 2. Dyadic neighbor shells

Fix an occupied natural satellite of scale `ell` centered at `y_0`.

For `k>=0`, define the dyadic neighbor shell

\[
\mathcal A_k
=
\{y:2^k\ell\le|y-y_0|<2^{k+1}\ell\}.
\]

Let

\[
N_k
:=
\#\{\text{comparable occupied satellite centers in }\mathcal A_k\}.
\]

Pure geometry gives

\[
N_k\lesssim 2^{3k}
\]

for disjoint fixed-shape packet cores.

---

## 3. Far strain from one neighbor

For a comparable natural packet at distance

\[
r_k\simeq2^k\ell,
\]

M5-294 gives

\[
|S_i(y_0)|\lesssim\frac\ell{r_k^3}.
\]

Relative to the selected satellite natural strain scale `ell^{-2}`,

\[
\boxed{
\frac{|S_i(y_0)|}{\ell^{-2}}
\lesssim2^{-3k}.
}
\]

Therefore the absolute contribution of the entire `k`-th neighbor shell obeys

\[
\boxed{
\frac{|S_k(y_0)|}{\ell^{-2}}
\lesssim
2^{-3k}N_k
}
\]

without using angular cancellation.

---

## 4. Local interaction-density descriptor

Define

\[
\boxed{
\mathscr I_{loc}(y_0)
:=
\sum_{k\ge0}2^{-3k}N_k.
}
\]

This is the discrete interaction density naturally paired with the degree-`-3` strain kernel.

Then

\[
\boxed{
|S_{neighbors}(y_0)|
\lesssim
\ell^{-2}\mathscr I_{loc}(y_0)
}
\]

at the absolute-value level, plus next-multipole/background terms.

Pure geometric saturation `N_k~2^{3k}` contributes order one **per dyadic layer**, so `K` saturated layers give

\[
\mathscr I_{loc}\sim K.
\]

Thus the critical local-cluster growth is only logarithmic in outer cluster radius, exactly as expected for the `|x|^{-3}` kernel in three dimensions.

---

## 5. Angular tensor refinement

Let the leading normalized tensor of neighbor `i` be

\[
\mathcal K_i
=\mathcal K(n_i,m_i)
\]

from M5-294.

Define the dyadic tensor order parameter

\[
\boxed{
\mathfrak A_k
:=
\frac1{N_k}\sum_{i\in\mathcal A_k}\mathcal K_i
}
\]

when `N_k>0`.

Then the signed leading strain is schematically

\[
\boxed{
\ell^2S_{neighbors}(y_0)
\simeq
C\sum_k2^{-3k}N_k\mathfrak A_k
+\text{higher multipoles}.
}
\]

Hence there are two distinct local cloud mechanisms:

1. **interaction-density escalation** — `I_loc` itself grows;
2. **angular coherence/cancellation** — `I_loc` may be large while the tensor sum stays bounded.

They must not be conflated.

---

## 6. Noncancelling local cluster route

Suppose along a satellite sequence

\[
\left|
\sum_k2^{-3k}N_k\mathfrak A_k
\right|
\to\infty.
\]

Then

\[
\boxed{
|S_{neighbors}(y_0)|/\ell^{-2}\to\infty,
}
\]

which is precisely

\[
\boxed{H_{sat-local}.}
\]

Thus any noncancelling increasingly dense local cloud re-enters the ambient-strain H branch.

---

## 7. Bounded local interaction branch

If

\[
\boxed{
\mathscr I_{loc}(y_0)\le C_I
}
\]

uniformly, then the occupied-neighbor contribution to ambient strain is automatically bounded at natural scale:

\[
|S_{neighbors}(y_0)|\lesssim C_I\ell^{-2}.
\]

Together with bounds on:

- near/self vorticity,
- diffuse/background harmonic strain,
- pressure/localization terms,

this is exactly the kind of ambient-strain hypothesis required by M5-281 for detached ancient compactness.

Therefore

\[
\boxed{
\mathscr I_{loc}=O(1)
\quad\text{is the natural occupied-cloud compactness lane.}
}
\]

---

## 8. Dense-but-cancelling branch

The difficult case is

\[
\mathscr I_{loc}\to\infty
\]

while

\[
\left|
\sum_k2^{-3k}N_k\mathfrak A_k
\right|=O(1).
\]

This requires increasing angular/multipole cancellation across scales.

The Formation description is

\[
\boxed{
C_{dense,cancel}
:
\text{large interaction mass but bounded tensor output}.
}
\]

This is where the axis-attribute dynamical constraints from M5-295 and the transverse covariance gate become relevant.

However large codimension alone is not a contradiction; statistically isotropic or symmetric clouds may cancel robustly.

---

## 9. Geometric packing does not close local interaction density

Although each dyadic layer has

\[
N_k\lesssim2^{3k},
\]

this gives only

\[
2^{-3k}N_k\lesssim1.
\]

Therefore geometry allows

\[
\mathscr I_{loc}\sim K
\]

over `K` filled dyadic scales.

The centered Morrey cap at the original main core does not by itself give a uniform Morrey estimate centered at every remote satellite.

Hence one must not claim

\[
\mathscr I_{loc}=O(1)
\]

from M5-296 alone.

This is an important firewall.

---

## 10. Updated local cloud frontier

The persistent occupied cloud now splits as

\[
\boxed{
\begin{aligned}
C_{occupied}
\Longrightarrow{}&
C_{I\text{-bounded}}\\
&\lor H_{sat-local}\\
&\lor C_{dense,cancel}\\
&\lor H/T_{background/diffuse}.
\end{aligned}
}
\]

The first lane feeds detached ancient compactness.

The second is already typed H.

The third is the genuine angular/axis cloud problem.

---

## 11. Next target

The next efficient calculation is not another raw packing count. It is to differentiate the dyadic angular tensor sum

\[
\mathscr T_{loc}
:=
\sum_k2^{-3k}N_k\mathfrak A_k
\]

along the cloud motion and determine whether maintaining

\[
\mathscr I_{loc}\gg1,
\qquad
\mathscr T_{loc}=O(1)
\]

forces one of:

- packet-axis turnover;
- radial-bin crossing;
- stretching-moment compensation;
- pressure/material replacement;
- an exact statistically isotropic invariant subclass.

---

## 12. Audit verdict

### PROVED / EXACT SCALING

\[
\boxed{
\mathscr I_{loc}
=\sum_k2^{-3k}N_k
}
\]

is the natural absolute interaction density for occupied comparable satellites.

### ROUTED

Noncancelling divergence of the weighted angular tensor sum gives `H_sat-local`.

### OPEN

- dense-but-cancelling local clouds;
- satellite-centered Morrey inheritance;
- diffuse/background strain;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]