# DSD M5-179 — Ultragenealogical Channel Selection at Spectral Infinity

Date: 2026-08-28

Status: **P1_B^S SPECTRAL-INFINITY CHANNEL PRUNING / EXACT FROZEN ROOT GEOMETRY SHOWS THAT ANGULAR HIGH FREQUENCY IS ALWAYS MORE STRONGLY DAMPED THAN THE `z`-WEIGHTED FIRST-ORDER TRANSFER AT SMALL NORMAL DEPTH / ONLY THE GENEALOGICAL FREQUENCY CHANNEL CAN COMPETE, AND COMPETITION STARTS NO EARLIER THAN `|omega| ~ z^-3` / CONSEQUENTLY ANY SURVIVING EXACT FLAT FIBER MUST ENTER AN ULTRAGENEALOGICAL REGIME WHOSE UNIFORM TIME-ANALYTIC ENVELOPE IS OF SIZE `exp(-c z^-3)=exp(-c r^6)` / THIS IS A NECESSARY CHANNEL SELECTION, NOT YET A COMPLETE UNIQUENESS THEOREM / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact damping symbol

Use the M5-173 frozen stable damping

\[
\Gamma_z(\omega,\ell)
=\frac{u-1}{8\nu z},
\]

with

\[
\sqrt D=u+iv.
\]

The variable transport/stretching channel enters the forward `tau` evolution with coefficient `z` and has cross-section differential order one.

Thus at cross frequency `(omega,ell)` its raw transfer scale is

\[
\boxed{
\mathfrak T_z(\omega,\ell)
\lesssim
z\bigl(1+|\omega|+\ell\bigr),
}
\]

up to uniform W1 coefficient constants.

This is a transfer scale; the top transport derivative is energy-skew, so this is deliberately a conservative upper size.

---

## 2. Angular high-frequency asymptotic

Let

\[
m=\ell(\ell+1).
\]

For angular-dominant frequency with `m->infinity`, the real part of the discriminant obeys

\[
d
=1+12\nu z+4\nu^2z^2+16\nu^2z^2m.
\]

Hence

\[
u\ge\sqrt d
\]

up to the harmless square-root convention, and for

\[
z\ell\gg1
\]

we have

\[
\boxed{
\Gamma_z
\ge
c\ell-Cz^{-1}
\sim c\ell.
}
\]

The first-order angular transfer is only

\[
\mathfrak T_z^{ang}\lesssim z\ell.
\]

Therefore

\[
\boxed{
\frac{\mathfrak T_z^{ang}}{\Gamma_z}
\lesssim z
\to0.
}
\]

Thus arbitrarily large angular frequency cannot become a transfer-dominated stable channel at small `z`.

The moderate angular region `z ell=O(1)` is already contained in the finite/parabolic analysis M5-174--176.

---

## 3. Genealogical high-frequency asymptotic

For genealogical-dominant frequency, the imaginary part of the discriminant is

\[
16\nu z\omega.
\]

When

\[
|\omega|\gg z^{-1},
\]

this term dominates the bounded real low-frequency part.  The principal square-root geometry gives

\[
 u
\sim
c(\nu z|\omega|)^{1/2}.
\]

Hence

\[
\boxed{
\Gamma_z^{gen}
\sim
c_\nu z^{-1/2}|\omega|^{1/2}.
}
\]

The first-order genealogical transfer scale is

\[
\boxed{
\mathfrak T_z^{gen}
\lesssim z|\omega|.
}
\]

Their ratio is

\[
\boxed{
\frac{\mathfrak T_z^{gen}}{\Gamma_z^{gen}}
\lesssim
C_\nu z^{3/2}|\omega|^{1/2}.
}
\]

Therefore transfer cannot compete with principal damping while

\[
|\omega|\ll z^{-3}.
\]

The first scale at which order-one competition is even possible is

\[
\boxed{|\omega|\asymp z^{-3}.}
\]

---

## 4. Necessary channel selection

M5-176 already proves that a survivor must leave every fixed parabolic mean corridor.

Sections 2--3 sharpen the spectral-infinity mechanism: the angular channel cannot furnish the required nonuniformity, and genealogical modes below `z^-3` remain principal-damping dominated.

Thus any remaining spectral-infinity entrance must place a non-negligible part of the distinguishability in the ultragenealogical regime

\[
\boxed{
|\omega|\gtrsim c z^{-3}
}

along arbitrarily small normal depths.

This is a necessary condition.  It does not claim that such a regime can actually be sustained.

---

## 5. Analytic amplitude consequence

M5-155 supplies a uniform positive analytic radius in the pair-flow time direction.  Hence genealogical spectral coefficients satisfy

\[
\|P_{|G|\ge\Omega}F\|
\le
M e^{-\delta\Omega}
\]

in a fixed reduced analytic norm.

At the necessary scale

\[
\Omega\gtrsim cz^{-3},
\]

we obtain

\[
\boxed{
\|P_{|G|\gtrsim z^{-3}}F\|
\le
M\exp(-c_1z^{-3}).
}
\]

Since

\[
z=r^{-2},
\]

this is

\[
\boxed{
\exp(-c_1r^6).
}
\]

Thus the only remaining spectral-infinity channel lives at an amplitude far smaller than the Gaussian floor obtained in M5-177.

---

## 6. Why this is stronger than M5-177 but not yet closure

M5-177 forced the **total pair energy** of any flat survivor below a fixed Gaussian-in-radius scale.

M5-179 says the specific modes capable of defeating principal damping must lie in a genealogical analytic tail of order

\[
e^{-cr^6}.
\]

However a homogeneous linear system can in principle amplify an extremely small high-frequency seed while transferring it to lower modes.  Therefore the amplitude estimate alone is not yet declared a contradiction.

The remaining task is to compare:

\[
\boxed{
\text{available amplification/transfer from }|\omega|\gtrsim z^{-3}
}
\]

against

\[
\boxed{
\text{analytic seed }e^{-c z^{-3}}.
}
\]

using the exact M5-169 fast kernel and stable-root damping.

---

## 7. DSD audit

### Formation — GREEN

Both damping and transfer scales come from the actual stable same-tail equation.

### Axis — GREEN

Angular and genealogical spectral channels are treated separately instead of being collapsed into one scalar frequency prematurely.

### Static aggregation — GREEN / NECESSARY-CHANNEL STATEMENT

No claim is made that the full spectral measure is supported at `z^-3`; only a surviving entrance mechanism must use that channel.

### Dynamics — GREEN at order-comparison level / YELLOW for full uniqueness

The channel threshold follows from the exact root asymptotics and the audited first-order differential order.  Whether the tiny analytic seed can be amplified into a nonzero core state remains open.

### Cross-audit — GREEN

The conclusion does not contradict the M5-173 mean-support firewall and does not reintroduce the invalid factorial path estimate of the original M5-161.

---

## 8. Updated frontier

The surviving statistical flat branch has been reduced to

\[
\boxed{
\text{ultragenealogical spectral entrance at }|G|\gtrsim z^{-3}
\text{ with seed size }\lesssim e^{-c z^{-3}}.
}
\]

The next calculation is an amplification-capacity estimate for that exact regime.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
