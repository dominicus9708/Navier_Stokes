# DSD M5-510 — Global smooth vorticity compactness does not force spatial Type-I velocity decay

Date: 2026-09-01

Status: **SPATIAL-DECAY FIREWALL / THE M5-508 HULL IS GLOBALLY COMPACT IN EVERY UNWEIGHTED SOBOLEV ORDER AND ITS CANONICAL VELOCITIES FORM A COMPACT SUBSET OF `L6`, BUT THESE FACTS DO NOT FORCE THE CRITICAL POINTWISE DECAY `|U(y)| <= C/(1+|y|)` / A FIXED SMOOTH DIVERGENCE-FREE FIELD CAN HAVE FINITE ALL-ORDER SOBOLEV NORMS, TIGHT VORTICITY, AND YET CONTAIN SPARSE REMOTE BUMPS FOR WHICH `|y||U(y)| -> infinity` / THEREFORE THE STRONGER SPATIAL TYPE-I HYPOTHESIS USED BY RECENT ONE-SLICE APPROXIMATE-SELF-SIMILARITY CRITERIA IS NOT AUTOMATICALLY INHERITED / THE COMPACT BRANCH SPLITS FURTHER INTO A SPATIAL TYPE-I SUBBRANCH OR AN EXPLICIT REMOTE VELOCITY-DECAY DEFECT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Question left by M5-509

M5-509 showed that on the M5-508 globally smooth compact marked branch the recurrent states are uniformly nonstationary on one fixed ball.

A much stronger external regularity route would become available if the corresponding similarity velocity satisfied a uniform critical spatial decay

\[
\boxed{
|U(y,\theta)|
\le
\frac{C_I}{1+|y|}.
}
\]

In physical variables this is the local spatial Type-I form

\[
|u(x,t)|
\lesssim
\frac1{\sqrt{-t}+|x|}.
\]

M5-510 audits whether this follows from the already proved global smooth compactness of the vorticity hull.

---

## 2. What M5-508 does imply for velocity

Use the canonical Biot--Savart representative

\[
U
=\nabla\times(-\Delta)^{-1}W.
\]

For every state,

\[
\|U\|_6
\le C\|W\|_2.
\]

Since the M5-508 vorticity hull is compact in `L2`, its image under the bounded Biot--Savart map is compact in `L6`.

Therefore the velocity family is uniformly `L6`-tight:

\[
\boxed{
\eta_6(R)
:=
\sup_{Y\in\widehat{\mathfrak H}}
\|U_Y\|_{L^6(|y|>R)}
\longrightarrow0.
}
\]

Similarly, Calderon--Zygmund maps the compact vorticity set to a compact set of velocity gradients in every corresponding Sobolev norm.

Thus the compact branch has strong integral tail control.

---

## 3. Integral tail control is weaker than `1/r` pointwise decay

The desired spatial Type-I statement is

\[
\sup_Y\sup_y
(1+|y|)|U_Y(y)|<\infty.
\]

Neither `L6` integrability nor all-order unweighted Sobolev boundedness gives such a weighted pointwise estimate.

Unweighted compactness controls the *amount* of remote mass, not the rate at which the pointwise amplitude must decay relative to the distance of that mass from the origin.

A sparse packet may have very small total norm while still being too large compared with `1/|y|` at its remote center.

---

## 4. Explicit smooth divergence-free function-space witness

Choose one nonzero divergence-free field

\[
\psi\in C_c^\infty(B_1(0);\mathbb R^3),
\qquad
\nabla\cdot\psi=0,
\]

with

\[
\psi(0)\ne0.
\]

Choose remote centers

\[
y_n=R_ne_1,
\qquad
R_n=4^n,
\]

so that the translated unit balls are disjoint.

Set amplitudes

\[
a_n=R_n^{-1/2}
\]

and define

\[
\boxed{
U(y)
:=
\sum_{n=1}^\infty
 a_n\psi(y-y_n).
}
\]

The supports are disjoint, so for every integer `m>=0`,

\[
\|U\|_{H^m}^2
=
\|\psi\|_{H^m}^2
\sum_{n=1}^\infty a_n^2.
\]

Since

\[
\sum_na_n^2
=
\sum_nR_n^{-1}
<\infty,
\]

we have

\[
\boxed{
U\in H^m(\mathbb R^3)
\quad\text{for every finite }m.
}
\]

The vorticity

\[
W=\nabla\times U
\]

also lies in every finite Sobolev space.

The singleton set

\[
\{W\}
\]

is trivially globally compact and tight in every Sobolev topology.

Nevertheless, at the remote centers,

\[
|U(y_n)|
=a_n|\psi(0)|
=R_n^{-1/2}|\psi(0)|.
\]

Hence

\[
\boxed{
|y_n|\,|U(y_n)|
=R_n^{1/2}|\psi(0)|
\longrightarrow\infty.
}
\]

Thus

\[
\boxed{
\sup_y(1+|y|)|U(y)|=\infty.
}
\]

This is a direct counterexample to the functional implication

\[
\text{all-order smooth compactness/tightness}
\Longrightarrow
1/r\text{ velocity decay}.
\]

The witness is not claimed to solve Navier--Stokes.  Its role is precisely to show that the desired decay cannot be extracted from the M5-508 function-space information alone; additional PDE/genealogy structure would be required.

---

## 5. Annular mean audit

Let

\[
A_R=\{R<|y|<2R\},
\qquad
c_R=(U)_{A_R}.
\]

Holder gives

\[
|c_R|
\le
|A_R|^{-1/6}
\|U\|_{L^6(A_R)}.
\]

Since

\[
|A_R|\asymp R^3,
\]

we obtain

\[
\boxed{
|c_R|
\le
C R^{-1/2}
\|U\|_{L^6(A_R)}.
}
\]

For the compact velocity family,

\[
\sup_Y|c_R(Y)|
\le
C R^{-1/2}\eta_6(R)
=o(R^{-1/2}).
\]

This is still not a uniform `O(R^{-1})` estimate because `eta_6(R)` may tend to zero arbitrarily slowly.

Moreover, the sparse-bump witness shows that even small annular means cannot rule out localized pointwise decay defects.

Thus neither shell means nor global `L6` tightness alone close the gap.

---

## 6. Define the missing decay channel

Define the critical spatial-velocity observable

\[
\boxed{
\mathcal V_1(Y)
:=
\sup_{y\in\mathbb R^3}
(1+|y|)|U_Y(y)|.
}
\]

The spatial Type-I subbranch is

\[
\boxed{
\sup_{Y\in\widehat{\mathfrak H}}
\mathcal V_1(Y)
<\infty.
}
\]

The complementary defect is

\[
\boxed{
H_{decay}^{U,1}
:
\quad
\sup_{Y\in\widehat{\mathfrak H}}
\mathcal V_1(Y)
=\infty.
}
\]

Therefore

\[
\boxed{
\mathcal C_{smooth}^{global}
\Longrightarrow
H_{decay}^{U,1}
\lor
\mathcal C_{spatial-Type-I}^{U}.
}
\]

This is a genuine new concentration/decay split rather than a restatement of `remote-E`.

---

## 7. Why `H_decay^(U,1)` is distinct from remote enstrophy escape

The M5-508 compact branch has uniformly tight vorticity `L2` mass.

Yet the function-space witness above has tight vorticity and still violates `1/r` velocity decay.

Thus

\[
\boxed{
H_{decay}^{U,1}
\not\equiv
H_{tail}^{remote-E}.
}
\]

The new defect is weighted pointwise/geometric rather than an unweighted mass-tightness failure.

It measures how small remote packets compare with their radius, not whether the total remote vorticity mass vanishes.

---

## 8. External-theorem firewall

Pineau--Vicol 2026 prove one-slice approximate-self-similarity and local-enstrophy regularity criteria under a spatial Type-I assumption of the form

\[
|u(x,t)|
\le
\frac{C_u}{\sqrt{-t}+|x|}
\]

plus suitable local pressure/solution hypotheses.

M5-510 shows that M5-508 does not by itself verify the spatial Type-I hypothesis.

Therefore those stronger external criteria may be used only on the explicitly separated subbranch

\[
\mathcal C_{spatial-Type-I}^{U},
\]

not on the whole globally smooth compact hull.

No external theorem closes `H_decay^(U,1)` here.

---

## 9. Updated frontier

Combining M5-508--510,

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-Sob}
\lor
H_{tail}^{remote-E}
\lor
H_{decay}^{U,1}
\lor
\mathcal C_{spatial-Type-I}^{U}\cap
\mathcal C_{dyn}^{uniform-marked}.
}
\]

The first two branches are unweighted spatial/frequency escapes.

The third is a weighted velocity-decay defect despite smooth compact vorticity.

The final branch is the cleanest dynamically recurrent critical class and is the only branch on which stronger spatial Type-I regularity criteria can even be audited.

---

## 10. Highest-value next target

There are now two high-value directions:

1. use the Navier--Stokes similarity equation, pressure representation, and finite-lineage genealogy to determine whether `H_decay^(U,1)` can actually persist dynamically, rather than merely in abstract function space;
2. on the spatial-Type-I subbranch, audit the exact hypotheses and consequences of current one-slice approximate-self-similarity criteria without conflating regularity of the ancient limit with regularity of the original hypothetical singular tower.

The second route is an external-theorem audit; the first remains an internal DSD calculation.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
