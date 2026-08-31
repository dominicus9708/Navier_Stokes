# DSD M5-421 — Diffuse remote-shell critical duality efficiency law

Date: 2026-08-31

Status: **THE M5-416 QUADRATIC REMOTE-EFFICIENCY LOSS IS NOT LIMITED TO FORMED FIXED-FLUX CARRIERS / A SMOOTHED BIOT--SAVART STRAIN FUNCTIONAL ON AN ANNULUS OF RADIUS `R` HAS `dot H^{1/2}` TEST NORM `O(R^-2)`, SO DUALITY GIVES `|S_R| <= C R^-2 ||omega_R||_{dot H^-1/2}` / FOR A FIRST-HITTING TARGET OF NATURAL SCALE `s`, A REMOTE SHELL AT `R=L s` CAN SUPPLY A FIXED FRACTION OF THE NATURAL STRAIN ONLY IF ITS LOCALIZED CRITICAL VORTICITY NORM IS AT LEAST `c nu L^2`, HENCE THE GLOBAL CRITICAL NORM IS AT LEAST `c nu^2 L^4` UP TO UNIFORM LOCALIZATION CONSTANTS / THIS EXTENDS SOURCE INEFFICIENCY TO DIFFUSE SHELLS AND QUANTIFIES THE COST OF GROWING-WINDOW SOURCING / THE COST MAY STILL DIVERGE IN A HYPOTHETICAL SINGULARITY, SO GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-416 proves a formed-carrier efficiency law

\[
\eta\lesssim\frac{s^2r}{(d+r)^3}
\]

and shows that remote formed sources are optimally only `O((s/d)^2)` efficient.

Its explicit firewall leaves open a completely diffuse remote source that is not decomposed into fixed-flux carriers.

The present note removes that limitation by treating the remote strain as a linear functional on the full critical vorticity space `dot H^{-1/2}`.

---

## 2. Remote annular strain functional

Fix a target point `x_*` and a remote radius `R` larger than a fixed multiple of the target natural scale.

Let `chi` be a fixed smooth annular cutoff supported in

\[
\{1/2<|z|<2\}
\]

and equal to one on a retained annulus.

Define

\[
\chi_R(y)=\chi\left(\frac{y-x_*}{R}\right).
\]

Let `K` denote one component of the Biot--Savart strain kernel, homogeneous of degree `-3`.

The retained remote-shell contribution is

\[
\boxed{
S_R(x_*)
=
\int K(x_*-y)\chi_R(y)\omega(y)dy
}
\]

componentwise/tensorially.

There is no principal-value issue because the retained shell stays a positive distance from `x_*`.

---

## 3. Scale of the test function

Define the shell test tensor/vector

\[
\Phi_R(y)
:=
K(x_*-y)\chi_R(y).
\]

By homogeneity,

\[
\Phi_R(y)
=
R^{-3}
\Phi_1\left(\frac{y-x_*}{R}\right)
\]

for a fixed smooth compactly supported annular profile `Phi_1`.

For homogeneous Sobolev scaling in three dimensions,

\[
\|A f(\cdot/R)\|_{\dot H^s}
=
|A|R^{3/2-s}\|f\|_{\dot H^s}.
\]

At `s=1/2` and `A=R^-3`,

\[
\boxed{
\|\Phi_R\|_{\dot H^{1/2}}
=
C_\Phi R^{-2}.
}
\]

This `R^-2` is the critical source-efficiency exponent.

---

## 4. Critical duality bound

Let `widetilde chi_R` be a slightly larger annular cutoff equal to one on the support of `Phi_R`, and set

\[
\omega_R=\widetilde\chi_R\omega.
\]

Then

\[
S_R(x_*)
=\langle\omega_R,\Phi_R\rangle.
\]

By `dot H^{-1/2}`--`dot H^{1/2}` duality,

\[
\boxed{
|S_R(x_*)|
\le
C R^{-2}
\|\omega_R\|_{\dot H^{-1/2}}.
}
\]

No formed packet, sign, topology, or pointwise source-amplitude hypothesis is used.

---

## 5. Normalize by the target natural strain

Let the target first-hitting natural scale be

\[
s=\sqrt{\nu/W},
\]

so

\[
S_{nat}\asymp\frac{\nu}{s^2}.
\]

Set

\[
L=\frac Rs.
\]

Then

\[
\boxed{
\frac{|S_R(x_*)|}{\nu/s^2}
\le
C
L^{-2}
\frac{\|\omega_R\|_{\dot H^{-1/2}}}{\nu}.
}
\]

This is the diffuse-shell analogue of the optimized M5-416 formed-carrier law.

---

## 6. Fixed remote strain fraction forces quadratic critical norm growth

Suppose one retained remote shell supplies a fixed fraction `epsilon>0` of the target natural strain:

\[
|S_R(x_*)|
\ge
\epsilon\frac{\nu}{s^2}.
\]

Then

\[
\boxed{
\|\omega_R\|_{\dot H^{-1/2}}
\ge
c\epsilon\nu L^2.
}
\]

Squaring,

\[
\boxed{
\|\omega_R\|_{\dot H^{-1/2}}^2
\ge
c\epsilon^2\nu^2L^4.
}
\]

Thus remote diffuse sourcing has the same quadratic efficiency loss in distance as the optimal formed source, and a quartic critical-mass cost after squaring the norm.

---

## 7. Localized shell norm versus global critical norm

Multiplication by a fixed smooth cutoff is bounded on `dot H^{-1/2}` in the retained homogeneous class, with operator norm invariant under translation and dilation of the cutoff.

Hence

\[
\boxed{
\|\omega_R\|_{\dot H^{-1/2}}
\le
C_{loc}
\|\omega\|_{\dot H^{-1/2}}.
}
\]

Using

\[
\|\omega\|_{\dot H^{-1/2}}
\asymp
\|u\|_{\dot H^{1/2}},
\]

a fixed remote strain fraction implies the global lower bound

\[
\boxed{
X(t)
:=
\|u(t)\|_{\dot H^{1/2}}^2
\ge
c\epsilon^2\nu^2L^4.
}
\]

Equivalently, for a given critical size `X(t)`, any single annular source that provides a fixed fraction of natural target strain must satisfy

\[
\boxed{
L
\lesssim
\epsilon^{-1/2}
\left(\frac{X(t)}{\nu^2}\right)^{1/4}.
}
\]

This is a critical visibility radius for source efficiency.

---

## 8. Relation to M5-400--402

M5-400--402 route large nonlocal/ambient strain to growing enstrophy and remote satellites.

The present estimate gives a direct critical-space version:

\[
\boxed{
\text{remote strain at normalized distance }L
\Longrightarrow
X\gtrsim\nu^2L^4
}
\]

when that shell alone carries a fixed strain fraction.

Thus remote strain is not merely associated with some abstract critical growth; its critical cost grows quantitatively with source separation.

---

## 9. Relation to M5-416

For one natural-strength formed carrier of radius `r` and distance `d`, M5-416 gives

\[
\eta\lesssim\frac{s^2r}{(d+r)^3}.
\]

Optimizing over `r` at fixed remote `d` gives

\[
\eta_{max}\lesssim (s/d)^2.
\]

The present shell duality bound gives exactly the same exponent without any formed-carrier model:

\[
\boxed{
\eta_{shell}
\lesssim
(s/R)^2
\times
\text{critical shell amplitude}.
}
\]

Therefore the quadratic remote inefficiency is a property of the critical Biot--Savart mapping itself, not an artifact of packet discretization.

---

## 10. Distributed remote source across many shells

If no single remote shell carries a fixed fraction, decompose into dyadic radii

\[
R_k=2^ks.
\]

Then schematically

\[
\boxed{
\frac{|S_{remote}|}{\nu/s^2}
\lesssim
\sum_{k\ge K}
2^{-2k}
\frac{\|\omega_{R_k}\|_{\dot H^{-1/2}}}{\nu}.
}
\]

This weighted shell throughput is the correct continuum scale-space ledger for diffuse remote sourcing.

One must not automatically replace the right side by an unweighted square sum of localized norms: `dot H^{-1/2}` is nonlocal, and cross-shell orthogonality requires a separate wavelet/Bessel implementation.

Thus the no-double-counting firewall remains explicit.

---

## 11. Consequence for `C_mass accum`

M5-420 shows that a fixed parent-natural cluster has bounded critical mass.

The present estimate shows that exterior critical mass at large normalized radius is increasingly inefficient at feeding the current target unless its localized critical norm grows at least quadratically in radius.

Hence

\[
\boxed{
C_{mass\,accum}
}

must be interpreted as a genuinely expensive delocalized reservoir:

- it cannot hide in the fixed main/companion cluster;
- if it directly drives current stretching from radius `L`, it pays `~L^4` critical mass;
- if it does not drive the current core, it is passive throughput content that must later be transported, reselected, or dissipated.

---

## 12. Near-balanced critical element interpretation

For the M5-419 `C_bal` branch, a near-minimal active element has no incentive to source a fixed fraction of its stretching from arbitrarily remote shells because the critical cost per unit strain diverges like `L^2` in norm.

Thus both the formed and diffuse source calculations support the same variational localization:

\[
\boxed{
\text{near-efficient / near-minimal active critical element}
\Longrightarrow
\text{source support concentrated in a bounded natural window.}
}
\]

The exterior reservoir may still exist, but its direct coupling to the active element becomes quantitatively weak unless it carries correspondingly huge critical mass.

---

## 13. Firewall

The lower bound

\[
X\gtrsim\nu^2L^4
\]

is not a contradiction because a hypothetical singularity may have unbounded critical norm.

The estimate concerns a fixed shell contribution. A source spread over many shells must be treated with the weighted ledger of Section 10 rather than assigning the total strain to one shell without proof.

The localized critical norm is defined through a smooth annular cutoff; hard characteristic cutoffs are not used in the Sobolev multiplier statement.

---

## 14. Next target

The critical frontier is now naturally separated into

\[
\boxed{
\text{compact near-balanced natural element}
+
\text{delocalized critical reservoir with quadratic coupling loss}.
}
\]

The next high-value question is whether the delocalized reservoir can replenish the compact element often enough to sustain the M5-419 near-balance without either:

1. forcing the quartic critical-mass growth to accelerate beyond the allowed near-balanced regime; or
2. producing fresh natural-scale source atoms and returning to the nonreuse ledger.

This is the first direct bridge between `C_mass accum` and `C_bal`.

---

## 15. Audit verdict

### DERIVED

\[
\boxed{
|S_R|
\lesssim
R^{-2}\|\omega_R\|_{\dot H^{-1/2}}.
}
\]

Hence

\[
\boxed{
\text{fixed strain fraction at }R=Ls
\Longrightarrow
\|\omega_R\|_{\dot H^{-1/2}}
\gtrsim\nu L^2,
\quad
X\gtrsim\nu^2L^4.
}
\]

### REMAINING

- multi-shell no-double-counting implementation;
- replenishment rate from the delocalized reservoir;
- near-balanced critical-element rigidity;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
