# DSD M17-379 — Audit correction: logarithmic flux-evacuation exposure is a sum of true own-scale residence times across coefficient scales

Date: 2026-09-08  
Canonical ID: **M17-379**

Status: **ACTIVE AUDIT CORRECTION / CROSS-SCALE EXPOSURE LEDGER**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. What M17-378 correctly proved

M17-372 gives the negative-exposure lower bound

\[
\boxed{
\int
\overline{\kappa_-}_{\Phi,F}d\theta
\gtrsim
\log\frac1r.
}
\]

Under the global target-scale ceiling

\[
\kappa_-\le K r^{-2},
\]

M17-378 correctly deduced

\[
|E_r|\gtrsim r^2\log(1/r).
\]

This is a valid time-measure estimate.

## 2. Interpretation that must not be made silently

Dividing by `r^2` gives

\[
r^{-2}|E_r|\gtrsim\log(1/r).
\]

However, this does **not** by itself prove that the negative exposure occurred at intrinsic coefficient scale `r`.

An interval on which

\[
\kappa_-\sim s^{-2},
\qquad s\gg r,
\]

may be long compared with `r^2` while being only `O(1)` in its own natural parabolic time `s^2`.

Therefore the phrase "logarithmically long scale-`r` residence" is allowed only after a coefficient lower bound

\[
\kappa_-\gtrsim r^{-2}
\]

is localized on the same time population.

Without that localization, M17-378 should be read as a **target-`r` normalized time bound**, not an extracted scale-`r` tangent theorem.

## 3. Dyadic intrinsic coefficient scales

Define the intrinsic negative-coefficient scale formally by

\[
s\sim\kappa_-^{-1/2}.
\]

For a final target `r`, partition the exposure into dyadic scale classes

\[
\mathcal E_m
:=
\left\{
2^m r\lesssim s<2^{m+1}r
\right\},
\qquad m=0,1,2,\dots.
\]

Equivalently, on `E_m`,

\[
\kappa_-\asymp 4^{-m}r^{-2}
\]

up to fixed dyadic constants.

Let

\[
T_m:=|\mathcal E_m|
\]

be the similarity-time measure allocated to that scale class.

## 4. Exact scale-corrected residence variable

The natural own-scale time of class `m` is

\[
\boxed{
\tau_m^{own}
:=
\frac{T_m}{(2^m r)^2}
=
\frac{T_m}{4^m r^2}.
}
\]

The exposure contributed by class `m` is of order

\[
\kappa_-T_m
\asymp
4^{-m}r^{-2}T_m
=
\tau_m^{own}.
\]

Therefore the total M17-372 exposure lower bound becomes the scale-invariant ledger

\[
\boxed{
\sum_m\tau_m^{own}
\gtrsim
\log\frac1r.
}
\]

This is the correct interpretation of the logarithmic evacuation cost.

## 5. Two genuine alternatives

The ledger implies the following dichotomy.

### A. Concentrated scale residence

If the number of materially active coefficient scales is

\[
N_{scale}(r)=o(\log(1/r)),
\]

then by pigeonhole

\[
\boxed{
\max_m\tau_m^{own}
\gtrsim
\frac{\log(1/r)}{N_{scale}(r)}
\to\infty.
}
\]

Thus at least one actual intrinsic coefficient scale carries a diverging amount of its **own natural parabolic time**. This is the branch on which a long-time own-scale tangent extraction becomes plausible.

### B. Cross-scale exposure cascade

If every active scale carries only bounded own-scale residence,

\[
\tau_m^{own}\le C,
\]

then the ledger forces

\[
\boxed{
N_{scale}(r)\gtrsim\log\frac1r.
}
\]

Thus logarithmically many distinct coefficient scales must participate.

This is a genuine cross-scale allocation/cascade branch rather than one long-lived `r`-bubble.

## 6. Connection to the existing cross-scale barrier

The second branch has the same structural character as the unresolved M17-298 cross-scale raw-`H2` allocation problem:

\[
\text{fixed total critical requirement}
\quad\text{may be distributed over many nested scales.}
\]

The quantities are not identical, so M17-298 is not declared solved or equivalent.

But the present calculation shows that the nodal flux-evacuation branch reaches the **same type of cross-scale bookkeeping obstruction** unless the exposure localizes to fewer scales.

## 7. Corrected successor to M17-378

The safe statement is therefore

\[
\boxed{
H_{r^{5/2}\ flux\ evacuation}
\Longrightarrow
H_{diverging\ true\ own\text{-}scale\ residence}
\lor
H_{logarithmic\ multi\text{-}scale\ exposure\ cascade}
\lor
G_{coefficient/genealogy\ decompactification}.
}
\]

M17-378 remains valid as a coarse time-measure estimate, but its compactness opportunity must be used only on the first branch above.

## 8. DSD audit

This correction is exactly a scale-identity audit: measuring every episode in the final scale's clock can manufacture an apparent long residence that is not long in the episode's own clock.

The mathematical repair is the dyadic intrinsic-scale decomposition above; no DSD axiom enters the PDE argument.

## 9. Audit verdict

**PASS-CORRECTION.**

The evacuation cost is best represented by

\[
\boxed{
\sum_m\tau_m^{own}
\gtrsim\log\frac1r,
}
\]

not by an unconditional claim of one logarithmically long scale-`r` residence interval.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]