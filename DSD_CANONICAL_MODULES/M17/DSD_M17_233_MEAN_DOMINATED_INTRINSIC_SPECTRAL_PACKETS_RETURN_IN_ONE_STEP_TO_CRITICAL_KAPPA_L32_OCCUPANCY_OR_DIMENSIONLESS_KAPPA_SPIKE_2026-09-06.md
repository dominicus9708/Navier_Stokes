# DSD M17-233 — Mean-dominated intrinsic spectral packets return in one step to critical kappa L3/2 occupancy or a dimensionless kappa spike

Date: 2026-09-06  
Canonical ID: **M17-233**

Status: **ONE-STEP SCALE-RETURN GATE TO THE COEFFICIENT CHANNEL / AT THE ROOT INTRINSIC BUFFER THE HIGH `H2/L2` RATIO IS STILL THE ORIGINAL CE-H RATIO `int kappa^2|W|^2 / int |W|^2`. SPLIT `W=c+w` INTO ITS BUFFER MEAN AND MEAN-ZERO FLUCTUATION. IF THE FLUCTUATION CARRIES A FIXED MASS FRACTION, M17-228 GIVES PHYSICAL PALINSTROPHY. IF THE BUFFER IS MEAN-DOMINATED, FIX A DIMENSIONLESS POTENTIAL CEILING `ell^2||kappa||_infty<=K0`. CHEBYSHEV SHOWS THAT ONLY `O(theta)` OF THE `W`-MASS CAN LIE WHERE `|w|>|c|/2`; UNDER THE POTENTIAL CEILING THAT SMALL SET CAN CARRY ONLY `O(K0^2 theta)` OF THE RAW `kappa^2|W|^2` CHARGE. CHOOSING `theta<<K0^-2`, A FIXED FRACTION OF THE SPECTRAL CHARGE LIES WHERE `W` IS COMPARABLE TO THE NONZERO MEAN. THERE THE WEIGHT CAN BE REMOVED, GIVING `int_B kappa^2 >= c ell^-1`; THE `L-infinity` CEILING THEN YIELDS THE SCALE-CRITICAL AMPLITUDE-INDEPENDENT LOWER BOUND `int_B |kappa|^(3/2) >= c(K0,A)>0`. IF THE CEILING FAILS, `ell^2||kappa||_infty>K0` IS ITSELF A DIMENSIONLESS COEFFICIENT-SPIKE EXIT. THUS THE RELATIVE-AMPLITUDE MICROCARRIER LADDER IS NOT NEEDED AS AN INDEPENDENT ROOT SPECTRAL SURVIVOR: IT RETURNS IN ONE STEP TO PALINSTROPHY OR AN AMPLITUDE-INDEPENDENT COEFFICIENT CHANNEL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Root intrinsic CE-H packet

Let `B` be an M17-224 root intrinsic buffer of radius

\[
\boxed{r=A\ell}
\]

for one fixed geometric constant `A>1`, with inner raw-Laplacian core `K subset B`.

Set

\[
M:=\int_B|W|^2dy,
\qquad
H:=\int_K|\Delta W|^2dy.
\]

Define the root intrinsic scale by

\[
\boxed{
\ell:=\left(\frac{M}{H}\right)^{1/4}.
}
\]

Thus

\[
\boxed{
H=\ell^{-4}M.
}
\]

On the CE-H active set,

\[
\Delta W=\kappa W,
\]

so on `K`

\[
\boxed{
H=\int_K\kappa^2|W|^2dy.
}
\]

This section uses the original `W`, not a mean-subtracted descendant.

---

## 2. Mean/fluctuation decomposition

Write

\[
\boxed{
W=c+w,
\qquad
c:=\frac1{|B|}\int_BWdy,
\qquad
\int_Bwdy=0.
}
\]

Set

\[
V:=\int_B|w|^2dy.
\]

Orthogonality gives

\[
\boxed{
M=V+|B||c|^2.
}
\]

Fix a threshold `0<theta<1`.

If

\[
V\ge\theta M,
\]

then M17-228 gives the genuine cutoff-independent palinstrophy return

\[
\boxed{
\int_B|\nabla W|^2dy
\ge c_P\theta r^{-2}M.
}
\]

Therefore only the mean-dominated branch

\[
\boxed{V<\theta M}
\]

needs a coefficient audit.

---

## 3. Dimensionless kappa-spike alternative

Fix one constant

\[
K_0>1.
\]

If

\[
\boxed{
\ell^2\|\kappa\|_{L^\infty(K)}>K_0,
}
\]

retain the explicit coefficient-spike branch

\[
\boxed{G_{\kappa\text{-}spike}^{intrinsic}.}
\]

This is already scale invariant because `kappa` has inverse-length-squared scaling.

For the remaining branch assume

\[
\boxed{
\|\kappa\|_{L^\infty(K)}
\le K_0\ell^{-2}.
}
\]

No claim is made that `K0` is small.

---

## 4. The cancellation set has small W-mass

Define

\[
E:=\{y\in B:|w(y)|>|c|/2\}.
\]

Since

\[
|B||c|^2=M-V>(1-\theta)M,
\]

Chebyshev gives

\[
|E|
\le\frac{4V}{|c|^2}.
\]

On `E`,

\[
|W|^2=|c+w|^2
\le2|c|^2+2|w|^2.
\]

Therefore

\[
\begin{aligned}
\int_E|W|^2dy
&\le2|c|^2|E|+2V\\
&\le10V.
\end{aligned}
\]

Hence on the mean-dominated branch

\[
\boxed{
\int_E|W|^2dy
\le10\theta M.
}
\]

The complement

\[
G:=K\setminus E
\]

is the region where the original vorticity remains comparable to its local coherent mean.

---

## 5. A bounded dimensionless potential prevents the bad set from carrying the spectral charge

On the bounded-coefficient branch,

\[
\begin{aligned}
\int_{K\cap E}\kappa^2|W|^2dy
&\le K_0^2\ell^{-4}
\int_E|W|^2dy\\
&\le10K_0^2\theta\ell^{-4}M\\
&=10K_0^2\theta H.
\end{aligned}
\]

Choose once and for all

\[
\boxed{
0<\theta\le\frac1{20K_0^2}.
}
\]

Then

\[
\boxed{
\int_G\kappa^2|W|^2dy
\ge\frac12H.
}
\]

Thus the high spectral charge cannot hide entirely in the small cancellation set unless the dimensionless `kappa` ceiling fails.

---

## 6. Remove the amplitude weight on the good set

On `G`,

\[
|w|\le|c|/2,
\]

so

\[
|W|\le\frac32|c|.
\]

Therefore

\[
\frac12H
\le
\frac94|c|^2\int_G\kappa^2dy.
\]

Hence

\[
\int_G\kappa^2dy
\ge\frac{2}{9}\frac{H}{|c|^2}.
\]

Since

\[
|c|^2\le\frac{M}{|B|},
\]

we obtain

\[
\boxed{
\int_B\kappa^2dy
\ge
c_A\frac{H|B|}{M}.
}
\]

Now

\[
\frac{H}{M}=\ell^{-4}
\]

and

\[
|B|=c_3A^3\ell^3.
\]

Therefore

\[
\boxed{
\int_B\kappa^2dy
\ge c_A\ell^{-1}.
}
\]

This lower bound is independent of the packet amplitude `M`.

---

## 7. Critical L3/2 coefficient occupancy

From

\[
|\kappa|^2
\le
\|\kappa\|_\infty^{1/2}|\kappa|^{3/2},
\]

we have

\[
\int_B|\kappa|^{3/2}dy
\ge
\frac{\int_B\kappa^2dy}
{\|\kappa\|_\infty^{1/2}}.
\]

Using Sections 3 and 6,

\[
\|\kappa\|_\infty^{1/2}
\le K_0^{1/2}\ell^{-1},
\]

and hence

\[
\boxed{
\int_B|\kappa|^{3/2}dy
\ge
c_AK_0^{-1/2}>0.
}
\]

The exponent `3/2` is the scale-critical Lebesgue exponent for a potential with scaling `length^-2` in three dimensions.

Indeed, after `y=q+ell z`,

\[
\int_{B_{A\ell}}|\kappa(y)|^{3/2}dy
=
\int_{B_A}|\ell^2\kappa(q+\ell z)|^{3/2}dz.
\]

Thus the lower bound is dimensionless and amplitude independent.

For completeness, the same coefficient ceiling gives the finite upper bound

\[
\int_B|\kappa|^{3/2}dy
\le C_AK_0^{3/2}.
\]

Hence the bounded-spike branch is a genuinely **critical potential-occupancy packet**, neither vanishing nor diverging after intrinsic rescaling.

---

## 8. One-step Scale-Return Gate

Combining Sections 2--7 gives, at the root intrinsic spectral packet,

\[
\boxed{
G_{intrinsic\ H2/L2\ spectral}
\Longrightarrow
H_{intrinsic\ palinstrophy}
\lor
G_{dimensionless\ \kappa\ spike}
\lor
H_{critical\ \kappa\ L^{3/2}\ occupancy}.
}
\]

This is a Scale-Return Gate in the sense of M17-229 because the output is reached after one uniformly bounded number of steps and the coefficient charge does not shrink with microcarrier mass.

Therefore the relative-amplitude finite scale ladder need not remain an independent **root spectral** terminal branch.

The ladder of M17-232 remains mathematically valid as a concentration description, but the original root CE-H packet has already returned to an amplitude-independent coefficient channel before that ladder is needed for canonical branch bookkeeping.

---

## 9. Relation to M17-210

M17-210 identifies

\[
\frac{\int\kappa^2|W|^2}{\int|W|^2}
\]

with the weighted `H2/L2` spectral ratio.

M17-233 adds a new distinction:

- the old spectral ratio is **amplitude weighted**;
- the new `L3/2` coefficient occupancy is **unweighted and amplitude independent**.

Thus the new branch is not merely the old weighted spectral ratio under a different name.

It is a scale-critical coefficient-space return obtained from mean domination plus the original CE-H identity.

---

## 10. Scope and nodal caveat

The coefficient identity is used on the CE-H active region.

If `kappa` cannot be continued across a relevant nodal/interface set with the regularity assumed in the packet calculation, retain

\[
G_{nodal/interface}
\]

explicitly.

No division by `|W|` is performed in the proof.

The amplitude weight is removed only on the good set where `W` is comparable to the nonzero mean.

---

## 11. What remains open

M17-233 closes the **scale-return problem**, not the Navier--Stokes problem.

The surviving coefficient alternatives are

\[
\boxed{
G_{dimensionless\ \kappa\ spike}
\lor
H_{critical\ \kappa\ L^{3/2}\ occupancy}.
}
\]

What is not yet known is whether the CE-H scalar multiplier possesses an independent spacetime/genealogy budget, a compactness/Liouville theorem, or a return to an already finite Navier--Stokes energy/enstrophy ledger.

Therefore the next canonical target is the **coefficient-channel audit**, not another microcarrier scale descent.

---

## 12. DSD audit

- The one-step SRG is applied only at the root packet where the denominator is the original `W` mass.
- No homogeneous CE-H equation is assigned to a mean-subtracted descendant.
- The cancellation set is controlled in `W`-mass, not merely in Lebesgue volume.
- The potential ceiling is dimensionless and its failure remains an explicit spike branch.
- The `L3/2` lower bound is unweighted and independent of carrier amplitude.
- This is a coefficient return, not yet a finite physical energy budget.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
