# Solenoidal Hardy Gap and the Sliding-History Reduction — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — PERSISTENT PASSIVE HISTORICAL TOWER REDUCED TO FLUX/TURNOVER; SLIDING-HISTORY SURVIVOR REMAINS — GLOBAL REGULARITY NOT PROVED.**

This note continues `HISTORICAL_SHELL_LOG_RADIAL_CRITICAL_LEDGER_2026-08-23.md`.

The previous note found the positive scale-critical shell-counting quantity

\[
\mathfrak D_{\log}^{rad}
=
\int |x|\,|\partial_ru|^2dx
\]

and proved, on the bounded Type-I historical envelope `|ru|<=A`,

\[
\mathfrak D_{\log}^{rad}
\ge
A^{-1}\|u\|_{L^3(\text{tower})}^3-4\pi A^2.
\]

The question left open was whether this logarithmic derivative cost can be routed into the existing turnover/derivative branches.

A sharp solenoidal Hardy--Leray gap provides the next bridge.

---

## 1. Sharp weighted Hardy--Leray inequality at the exact historical weight

For three-dimensional solenoidal vector fields, the sharp Hardy--Leray inequality has the form

\[
C_\gamma
\int_{\mathbb R^3}
\frac{|u|^2}{|x|^2}|x|^{2\gamma}dx
\le
\int_{\mathbb R^3}|\nabla u|^2|x|^{2\gamma}dx.
\]

At

\[
\gamma=\frac12,
\]

the weights become exactly

\[
\frac{|u|^2}{|x|}
\qquad\text{and}\qquad
|x||\nabla u|^2.
\]

The sharp three-dimensional solenoidal constant is

\[
C_{1/2}
=
\left(\frac12+\frac12\right)^2
\frac{4+(\frac12-\frac32)^2}{2+(\frac12-\frac32)^2}
=
\boxed{\frac53}.
\]

Hence

\[
\boxed{
\frac53
\int\frac{|u|^2}{|x|}dx
\le
\int|x||\nabla u|^2dx.
}
\]

This is a genuine incompressibility gain. For unconstrained vector fields the corresponding scalar Hardy constant at this weight is `1`; the formal scalar extremal shape is `1/r`. The divergence-free condition removes that exact saturation and opens a strict gap.

External anchor: the sharp Hardy--Leray inequality for three-dimensional solenoidal fields, established without axial-symmetry restriction in the modern sharp results of Hamamoto and collaborators.

---

## 2. Weighted kinetic-energy identity

Let

\[
e=\frac12|u|^2.
\]

For a fixed center, the local energy equation of a smooth solution is

\[
\partial_te
+\nabla\cdot((e+p)u)
=
\nu\Delta e
-\nu|\nabla u|^2.
\]

Formally multiply by `r=|x|` and integrate. Since in three dimensions

\[
\Delta r=\frac2r,
\]

we obtain

\[
\boxed{
\nu(D_1-H_1)
=-\frac{d}{dt}M_1+F_1,
}
\]

where

\[
D_1
:=
\int r|\nabla u|^2dx,
\]

\[
H_1
:=
\int\frac{|u|^2}{r}dx,
\]

\[
M_1
:=
\frac12\int r|u|^2dx,
\]

and

\[
F_1
:=
\int
\left(\frac{|u|^2}{2}+p\right)
 u\cdot\widehat r\,dx.
\]

For the proof program this identity must ultimately be used with smooth inner/outer cutoffs and the moving coherent center. Those operations create cutoff, center-motion, and divergence-correction terms; they are not suppressed here and must be audited as `T`/drift/boundary channels.

---

## 3. Solenoidal gap leaves at least 2/5 of the weighted derivative cost

The sharp constant gives

\[
H_1\le\frac35D_1.
\]

Therefore

\[
\boxed{
D_1-H_1
\ge
\frac25D_1.
}
\]

Since

\[
D_1
\ge
\int r|\partial_ru|^2dx
=
\mathfrak D_{\log}^{rad},
\]

we obtain the conditional whole-space bridge

\[
\boxed{
-\frac{d}{dt}M_1+F_1
\ge
\frac{2\nu}{5}
\mathfrak D_{\log}^{rad}.
}
\]

Insert the previous historical-shell coercivity estimate:

\[
\boxed{
-\frac{d}{dt}M_1+F_1
\ge
\frac{2\nu}{5}
\left[
A^{-1}\|u\|_{L^3(\text{tower})}^3
-4\pi A^2
\right].
}
\]

Thus if

\[
\|u\|_{L^3(\text{tower})}^3
\ge
c_0\log K-O(1),
\]

then

\[
\boxed{
-\frac{d}{dt}M_1+F_1
\ge
\frac{2\nu c_0}{5A}\log K-O_\nu(A^2+1).
}
\]

The historical tail is therefore not merely paying an abstract critical derivative tax. In the weighted energy equation the tax must emerge as either

1. radial kinetic/pressure energy flux `F_1`, or
2. rapid decrease of the weighted kinetic moment `M_1`.

---

## 4. Persistent historical tower

Consider the ideal historical tower in physical variables occupying

\[
r_j<r<R_*,
\]

with a fixed positive outer physical radius `R_*` and critical amplitude `|u|~1/r`.

Its cubic mass behaves as

\[
\|u\|_3^3
\sim
c\log\frac{R_*}{r_j}.
\]

Its weighted kinetic moment behaves instead as

\[
M_1
\sim
c_2
\int_{r_j}^{R_*}r\,dr
=
\frac{c_2}{2}(R_*^2-r_j^2).
\]

Hence, as `r_j -> 0`, the persistent tower does **not** obtain a logarithmically large negative `M_1'` from merely adding smaller critical shells. In the ideal scale-stationary picture `M_1` approaches a finite outer-scale value from below.

The Hardy-gap balance therefore requires

\[
\boxed{
F_1
\gtrsim
c\nu\log(R_*/r_j)
}

up to the bounded/slow `M_1` variation and localization errors.

By coarea, `F_1` is a radial sum of kinetic-plus-pressure flux through the occupied scales. Thus a persistent tower cannot remain simultaneously

- logarithmically `L3`-occupied;
- bounded by the passive Type-I `1/r` envelope;
- and flux-quiet.

In the proof tree, a logarithmically growing radial energy/pressure flux is naturally a `T`-type turnover/influx event once the localization terms are quantified.

So the **persistent passive historical tower is no longer the main survivor**.

---

## 5. The only remaining quiet escape: sliding / forgetful history

A tail may attempt to avoid the persistent-tower conclusion by allowing its outer physical radius to shrink:

\[
R_j\to0,
\qquad
K_j:=\frac{R_j}{r_j}\to\infty.
\]

Then the normalized tower still contains more and more logarithmic scales while the whole historical packet collapses toward the singular point.

For geometric first-hitting scales

\[
r_j=r_0q^{-j/2},
\]

retain the latest `N_j` historical shells. The outer retained physical radius is

\[
\boxed{
R_j
=r_{j-N_j}
=r_jq^{N_j/2}.
}
\]

The normalized outer radius is

\[
\boxed{
K_j
=R_j/r_j
=q^{N_j/2}.
}

The ancient `L3` requirement demands

\[
N_j\to\infty.
\]

To avoid persistence at a fixed outer physical scale, one simultaneously needs

\[
j-N_j\to\infty.
\]

Hence the quiet survivor must satisfy the double condition

\[
\boxed{
N_j\to\infty,
\qquad
j-N_j\to\infty.
}
\]

This is a **sliding historical window**: the number of remembered critical shells diverges, but the oldest retained shell also moves to later and later stages.

A simple model is

\[
N_j\sim\alpha j,
\qquad
0<\alpha<1.
\]

Then

\[
K_j\sim q^{\alpha j/2}\to\infty,
\]

while

\[
R_j\sim r_0q^{-(1-\alpha)j/2}\to0.
\]

Thus

\[
\|u\|_3^3\sim c\alpha j\to\infty,
\]

but

\[
M_1\sim O(R_j^2)\to0.
\]

This collapsing weighted moment can in principle absorb the positive Hardy-gap term without requiring a logarithmically large persistent outer flux.

---

## 6. Meaning of the new reduction

The historical branch has therefore been narrowed from

> arbitrary passive `1/r` critical tail

into

> a sliding / forgetful critical history that continually loses its oldest physical shells while retaining a diverging number of newer shells.

This is much more restrictive.

In particular, if the old shells are materially retained at fixed physical radii, the sharp solenoidal Hardy gap forces `T`-type radial flux.

Therefore a non-`T` survivor must continually **erase, transport, cancel, or decorrelate old shells** fast enough that

\[
R_j\to0
\]

while still maintaining

\[
K_j\to\infty.
\]

That erasure mechanism is the next object to audit.

---

## 7. Why ordinary diffusion is exactly critical for this question

A historical shell born at physical scale `r_m` has natural diffusion time

\[
\tau_m\sim r_m^2/\nu.
\]

In a Type-I first-hitting sequence the remaining time to the putative singular time is also of order

\[
T^*-t_m\sim r_m^2.
\]

Therefore an old shell experiences only an order-one number of its own natural diffusion times before `T^*`.

At the linear scaling level the heat factor is consequently only

\[
\exp\left[-c\nu\frac{T^*-t_m}{r_m^2}\right]
\sim e^{-c\nu},
\]

an order-one attenuation rather than a scale-dependent factor tending to zero.

Thus geometric first-hitting scaling gives no automatic reason for older critical shells to disappear merely by viscosity.

This does **not** prove a lower bound for a nonlinear Navier--Stokes shell; cancellation and nonlinear redistribution remain possible. It does show that the sliding-history branch requires more than the naive statement "old shells diffuse away".

---

## 8. Updated final survivor

After the log-radial critical ledger and the solenoidal Hardy gap, the remaining historical-shell survivor is now:

\[
\boxed{
\text{SLIDING CRITICAL HISTORY}
}
\]

with all of the following features:

1. `N_j -> infinity`, so global ancient `L3` diverges;
2. `K_j -> infinity`, so the normalized tail reaches arbitrarily remote scales;
3. `R_j -> 0`, so the oldest retained physical shell moves inward;
4. the Type-I amplitude envelope remains `|u| <= A/r`;
5. persistent outer radial flux stays below the `T` threshold;
6. old shells are continually erased/replaced by a mechanism not attributable merely to linear diffusion.

The next theorem target is therefore no longer "remove an arbitrary weak-L3 historical tail".

It is the much narrower statement:

\[
\boxed{
\text{Diverging remembered history}
+
\text{continual old-shell forgetting}
\Longrightarrow
T\ \text{or}\ H\ \text{or projective failure}.
}
\]

---

## 9. Technical caveat required for theorem-level use

The sharp Hardy--Leray inequality is stated for globally solenoidal fields in the appropriate weighted completion (initially smooth compactly supported fields).

The proof program uses

- a moving core center;
- an inner singular-scale cutoff;
- a finite outer physical cutoff;
- and a whole-space velocity that need not have finite first weighted energy moment.

Therefore the next rigorous lemma must perform a **solenoidal localization**, e.g. cutoff plus divergence correction, and track all induced terms.

Those induced terms are not harmless by declaration. They must be bounded or explicitly routed into

- boundary/material flux `T`;
- remote derivative leakage `H`;
- coherent-frame drift;
- or pressure-gauge terms.

Until that localization lemma is complete, the Hardy-gap bridge remains a strong conditional reduction rather than a global regularity proof.

---

## 10. Current status

Two successive improvements are now available:

1. historical logarithmic `L3` occupancy forces

\[
\mathfrak D_{\log}^{rad}\gtrsim\log K;
\]

2. incompressibility opens the sharp `5/3` Hardy--Leray gap, giving formally

\[
-\dot M_1+F_1
\ge
\frac{2\nu}{5}\mathfrak D_{\log}^{rad}.
\]

Consequently a persistent flux-quiet historical tower is excluded at the model/conditional level. The only quiet survivor is a sliding historical window whose outer physical radius tends to zero while the number of remembered shells tends to infinity.

Status: **PERSISTENT PASSIVE HISTORY IS REDUCED TO `T` BY THE SOLENOIDAL HARDY GAP, SUBJECT TO THE LOCALIZATION AUDIT. THE MAIN SURVIVOR IS NOW A SLIDING/FORGETFUL HISTORY. GLOBAL REGULARITY IS NOT PROVED.**
