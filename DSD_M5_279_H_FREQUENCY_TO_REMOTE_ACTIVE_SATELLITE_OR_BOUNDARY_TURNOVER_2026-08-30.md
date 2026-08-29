# DSD M5-279 — H-Frequency Escalation to Remote Active Satellite or Boundary Turnover

Date: 2026-08-30

Parent: `DSD_M5_278_ALBRITTON_BARKER_CONTRAPOSITIVE_H_FREQUENCY_SATURATION_2026-08-30.md`

Status: **H GEOMETRIZATION / ON THE NON-CAMPANATO-TURNOVER CORRIDOR, LARGE CRITICAL SHELL H1 ENERGY CANNOT BE AN ABSTRACT STRAIN/FREQUENCY NUMBER ONLY / SOLENOIDAL LOCALIZATION CONVERTS IT TO LARGE ACTUAL VORTICITY ENERGY UNLESS CUTOFF/BOGOVSKII BOUNDARY ACTION IS LARGE / CONSEQUENTLY `R^2 sup_{A_R}|Omega|` DIVERGES AND THE SHELL CONTAINS A VORTICITY POINT WHOSE NATURAL SCALE IS ASYMPTOTICALLY MUCH SMALLER THAN ITS DISTANCE FROM THE TRACKED CORE / H IS REDUCED TO REMOTE ACTIVE SATELLITES OR TYPED BOUNDARY TURNOVER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

At one normalized W1/ancient time, let `A_R` be a fixed-shape annulus of radius `R` and define

\[
E_1(R)
:=
R\int_{A_R^*}|\nabla U|^2.
\]

Let

\[
f_R=\chi_RU-b_R
\]

be the standard Bogovskii-corrected shell localization, so

\[
\nabla\cdot f_R=0,
\]

`f_R=U` on the retained inner annulus, and `f_R` is compactly supported in a fixed enlargement.

On the M5-278 H-only survivor, for every sufficiently old epoch one can choose `R` with

\[
E_1(R)\gg1.
\]

---

## 2. Solenoidal identity converts gradient energy to localized vorticity energy

For a compactly supported divergence-free vector field,

\[
\boxed{
\int_{\mathbb R^3}|\nabla f_R|^2
=
\int_{\mathbb R^3}|\nabla\times f_R|^2.
}
\]

The curl of the localized packet is

\[
\boxed{
\nabla\times f_R
=
\chi_R\Omega
+
\nabla\chi_R\times U
-
\nabla\times b_R.
}
\]

Thus the only difference between localized gradient energy and true shell vorticity energy is carried by the transition-buffer/correction terms.

---

## 3. Boundary correction scale

The cutoff obeys

\[
|\nabla\chi_R|\lesssim R^{-1}.
\]

After subtracting the shell mean in the standard Campanato localization convention,

\[
\|\nabla\chi_R\times(U-(U)_{A_R^*})\|_2^2
\lesssim
R^{-2}
\|U-(U)_{A_R^*}\|_{L^2(A_R^*)}^2.
\]

Since

\[
\mathfrak C_A(R)
=R^{-1}
\|U-(U)_{A_R^*}\|_2^2,
\]

we obtain

\[
\boxed{
R\,
\|\nabla\chi_R\times(U-(U)_{A_R^*})\|_2^2
\lesssim
\mathfrak C_A(R).
}
\]

The Bogovskii correction has the same fixed-shape estimate:

\[
\boxed{
R\|\nabla\times b_R\|_2^2
\lesssim
C\,\mathfrak C_A(R)
}
\]

provided the usual mean/drift term is kept in the previously typed shell-boundary/center channel.

If those transition terms exceed this quiet scale, the event is already a boundary/material/center localization turnover `T`.

Hence on the non-T Campanato/boundary corridor

\[
\boxed{
R\|\text{localization curl corrections}\|_2^2
\le C C_T.
}
\]

---

## 4. Large E1 forces true annular vorticity energy

The existing localization estimate in the weak-`L^3` routing gives, in the genuinely escalating regime,

\[
\|\nabla f_R\|_2^2
\gtrsim
\int_{A_R}|\nabla U|^2
-
CR^{-2}\|U-(U)_{A_R^*}\|_2^2.
\]

Multiply by `R`:

\[
R\|\nabla f_R\|_2^2
\gtrsim
E_1(R)-C\mathfrak C_A(R).
\]

Use the solenoidal curl identity and the boundary estimates.  There are fixed constants `c,C>0` such that

\[
\boxed{
R\int_{A_R^{ret}}|\Omega|^2
\ge
cE_1(R)-CC_T
}
\]

unless a localization/boundary T event occurs.

Therefore along the H escalation sequence

\[
E_1(R)\to\infty
\]

we have

\[
\boxed{
R\int_{A_R^{ret}}|\Omega|^2\to\infty.
}
\]

This is a genuine vorticity statement, not merely a velocity-strain estimate.

---

## 5. Pointwise active-satellite parameter

The retained annulus has volume

\[
|A_R^{ret}|\asymp R^3.
\]

Let

\[
m_R:=\|\Omega\|_{L^\infty(A_R^{ret})}.
\]

Then

\[
\int_{A_R^{ret}}|\Omega|^2
\le
C R^3 m_R^2.
\]

Combining with Section 4 yields

\[
R\cdot C R^3m_R^2
\ge
cE_1(R)-CC_T.
\]

Hence

\[
\boxed{
R^2m_R
\ge
c_0\sqrt{E_1(R)-C_0C_T}.
}
\]

Define the dimensionless active-satellite parameter

\[
\boxed{
\Lambda_R
:=R^2m_R.
}
\]

Then on the H-only escalation corridor

\[
\boxed{
\Lambda_R\to\infty.
}
\]

---

## 6. Natural scale of the remote vorticity point

Choose a point `Y_R in A_R^{ret}` with

\[
|\Omega(Y_R)|\ge m_R/2.
\]

Its vorticity-natural normalized scale is

\[
\boxed{
\ell_R:=m_R^{-1/2}.
}
\]

Since

\[
m_R=\Lambda_RR^{-2},
\]

we have

\[
\boxed{
\ell_R
=
\frac{R}{\sqrt{\Lambda_R}}.
}
\]

Therefore

\[
\boxed{
\frac{R}{\ell_R}
=
\sqrt{\Lambda_R}
\to\infty.
}
\]

Thus the H shell contains a vorticity point whose own natural scale is asymptotically much smaller than its distance from the tracked core.

This is the precise meaning of a **remote active satellite**.

---

## 7. Compatibility with the first-hitting cap

The current first-hitting normalization gives a global vorticity upper cap on the relevant backward interval.

Hence

\[
m_R\le K_I
\]

(up to the fixed normalization of the selected W1/RG time).

Therefore `ell_R` does not collapse for the trivial reason `m_R -> infinity` at fixed normalized radius.  Rather, the divergence is geometric:

\[
R/\ell_R\to\infty.
\]

The satellite is far away in units of its own active scale.

For an ideal historical critical shell one would have

\[
m_R\sim R^{-2},
\qquad
\Lambda_R\sim1.
\]

Thus

\[
\Lambda_R\gg1
\]

is exactly a departure from passive ancestor scaling.

---

## 8. H branch is now a satellite/turnover fork

Combining the preceding sections:

\[
\boxed{
H_{freq}\text{ with }E_1\gg1
\Longrightarrow
\begin{cases}
T_{boundary/localization},\\
\text{or}\\
\Lambda_R=R^2\|\Omega\|_{L^\infty(A_R)}\gg1.
\end{cases}
}
\]

Along the M5-278 eventual H-saturation survivor, if T remains excluded then

\[
\boxed{
\sup_R\Lambda_R(h)\to\infty
\qquad(h\to-\infty).
}
\]

So every sufficiently old epoch contains an increasingly scale-separated active satellite.

---

## 9. What is not yet proved

A large `Lambda_R` point is not automatically a coherent material vortex tube or a separately nested first-hitting lineage.

The current audit does **not** yet prove:

\[
\Lambda_R\gg1
\Longrightarrow T_{center}.
\]

High derivatives may make the region of comparable vorticity very small, and the satellite may be created/destroyed locally rather than persist as a material core.

The correct next gate is therefore local and dynamical:

> starting from a point with vorticity amplitude `m_R` at distance `R` and natural scale `ell_R=m_R^{-1/2} << R`, trace a backward parabolic cylinder of radius/time `ell_R, ell_R^2`.  Either a comparable local vorticity core persists long enough to form a satellite first-hitting block, or its appearance/disappearance requires a boundary/nonlinear/derivative replenishment event that is already H/T.

---

## 10. DSD verdict

### PROVED

- large shell derivative energy cannot remain purely irrotational after solenoidal localization;
- on quiet Campanato/boundary localization, it forces large actual annular vorticity energy;
- large annular vorticity energy forces `Lambda_R=R^2 sup|Omega|` large;
- `Lambda_R` is exactly the squared separation between shell radius and the satellite's vorticity-natural scale.

### CURRENT H FRONTIER

\[
\boxed{
H_{freq}
\Longrightarrow
T_{boundary}
\lor
\text{remote active satellite with }R/\ell_R\to\infty.
}
\]

The next task is to convert the latter satellite into a typed center/material turnover or a re-centered first-hitting tower.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
