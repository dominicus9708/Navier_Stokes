# DSD M5-286 — Seregin Type-II Euler Zoom versus Satellite `5/4` Scaling Audit

Date: 2026-08-30

Parent: `DSD_M5_285_SATELLITE_RECENTERING_AFFINE_FIXED_POINT_ANTI_MODEL_2026-08-30.md`

External reference: Gregory Seregin, *On potential Type II blowups for the Navier--Stokes equations*, arXiv:2606.29468v1 (2026-06-28).

Status: **VARIABLE-MATCH AUDIT / THE `5/4` EXPONENT FROM M5-282 IS NOT SEREGIN'S `alpha` / SEREGIN'S `f(lambda)` IS A TIME-TO-SPATIAL-SQUARE COMPRESSION FACTOR IN AN EULER ZOOM, WHILE THE M5-282 LAW RELATES SATELLITE NATURAL VORTICITY LENGTH TO CORE-SEPARATION LENGTH / THE CORRECT COMMON COORDINATE IS `chi=(T*-t)/d^2` / IF THE SATELLITE HAS ORDER-ONE NATURAL LIFETIME `Theta=q^2(T*-t)~1`, THEN THE ENERGY-SHIELD BOUNDARY `ell~d^(5/4)` CORRESPONDS EXACTLY TO SEREGIN'S BORDERLINE `alpha=3/2`, NOT TO HIS EXCLUDED `alpha>3/2` REGIME / WITHOUT A TIME-ACTIVITY BRIDGE OR SEREGIN'S WEIGHTED `A_f/E_f/D_f` HYPOTHESES, HIS THEOREM DOES NOT CLOSE THE CURRENT SATELLITE FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Seregin's Type-II scaling

Seregin considers a suitable weak Navier--Stokes solution near a candidate singular point and introduces a function

\[
f:(0,1]\to(0,1],
\qquad
f(\lambda)\to0
\quad(\lambda\to0).
\]

The Euler-type zoom is

\[
\boxed{
v^\lambda(y,\tau)
=\lambda f(\lambda)v(x,t),
}
\]

with

\[
\boxed{
x=\lambda y,
\qquad
t=\lambda^2f(\lambda)\tau.
}
\]

Thus `lambda` is the spatial observation scale, whereas

\[
\boxed{
f(\lambda)=
\frac{\text{chosen time scale}}{\lambda^2}}
\]

is a dimensionless time-compression factor relative to parabolic scaling.

Seregin's scenario also assumes weighted scale bounds

\[
A_f(v,r)+E_f(v,r)+D_f(q,r)\le M_1,
\]

where schematically

\[
E_f\sim \frac{f(r)}r\int_{Q(r)}|\nabla v|^2,
\]

\[
A_f\sim \frac{f(r)^2}r\sup_t\int_{B(r)}|v|^2,
\]

and

\[
D_f\sim \frac{f(r)^2}{r^2}\int_{Q(r)}|q|^{3/2}.
\]

These are substantive hypotheses, not consequences of the scaling definition alone.

---

## 2. Seregin's power family

A model family in the 2026 paper is

\[
\boxed{
f(\lambda)
=\frac{\lambda^{\alpha-1}}
{\log^\gamma(e/\lambda)},
\qquad1<\alpha<2.
}
\]

Ignoring the logarithmic modifier for exponent bookkeeping, the time scale is

\[
\lambda^2f(\lambda)
\sim
\lambda^{\alpha+1}.
\]

The limiting Euler energy estimate contains

\[
\frac{F(a)^2}{a}=a^{2\alpha-3}.
\]

Therefore the simple decay argument forces the limiting Euler profile to vanish if

\[
\boxed{\alpha>\frac32.}
\]

The paper consequently restricts the potentially surviving power regime to

\[
\boxed{\alpha\le\frac32.}
\]

This is only one part of Seregin's full scenario theorem, which also contains the `g`-weighted growth condition.

---

## 3. Our satellite variables

For a satellite observed at physical time `t<T*`, define

\[
a:=T^*-t>0,
\]

\[
q:=|\omega(x,t)|^{1/2},
\qquad
\ell:=q^{-1},
\]

and let

\[
d
\]

be its spatial separation from the tracked main core/candidate singular center in the same physical variables.

The remote-satellite condition is

\[
\boxed{L:=qd=\frac d\ell\to\infty.}
\]

Introduce the scale-invariant natural-time activity ratio

\[
\boxed{\Theta:=q^2a=\frac a{\ell^2}.}
\]

Finally define the distance-based parabolic ratio

\[
\boxed{\chi:=\frac a{d^2}.}
\]

These satisfy the exact identity

\[
\boxed{\chi=\frac{\Theta}{L^2}.}
\]

---

## 4. Correct identification with Seregin's `f`

If one chooses the Seregin spatial zoom parameter to be the satellite separation scale

\[
\lambda=d,
\]

then his time-compression factor is represented by

\[
\boxed{
f(d)\leftrightarrow\frac a{d^2}=\chi.}
\]

By contrast,

\[
\frac\ell d=L^{-1}
\]

is a ratio of **two spatial lengths**.

Therefore

\[
\boxed{
\frac\ell d
\neq f(d)
}
\]

in general.

This immediately blocks the naive identification

\[
\text{M5-282 exponent }5/4
=\text{Seregin exponent }\alpha.
\]

The axes are different.

---

## 5. Add the order-one activity bridge

Suppose now, conditionally, that the satellite has an order-one amount of its own natural parabolic lifetime remaining:

\[
\boxed{0<c_\Theta\le\Theta\le C_\Theta<\infty.}
\]

Then

\[
a\asymp\ell^2.
\]

On the M5-282 energy-shield boundary,

\[
\ell\asymp d^{5/4}
\]

(up to the fixed energy dimensional constant).

Therefore

\[
a\asymp\ell^2
\asymp d^{5/2}.
\]

Hence

\[
\boxed{
\chi=\frac a{d^2}
\asymp d^{1/2}.
}
\]

Comparing with Seregin's power model

\[
f(d)\sim d^{\alpha-1},
\]

gives

\[
\boxed{\alpha-1=\frac12,}
\]

so

\[
\boxed{\alpha=\frac32.}
\]

Thus the `5/4` spatial shield exponent, **after adding `Theta~1`**, corresponds exactly to Seregin's power borderline.

---

## 6. Which side corresponds to Seregin's simple exclusion?

Under the same order-one activity assumption,

\[
\ell\sim d^\beta
\]

implies

\[
a\sim d^{2\beta},
\]

and hence

\[
f(d)\sim\chi\sim d^{2\beta-2}.
\]

Therefore

\[
\alpha-1=2\beta-2,
\]

or

\[
\boxed{\alpha=2\beta-1.}
\]

Seregin's simple excluded side

\[
\alpha>\frac32
\]

corresponds to

\[
\boxed{\beta>\frac54.}
\]

For small `d`, a larger power `beta` means a **smaller** satellite natural length.

Thus the Seregin-excluded side corresponds schematically to

\[
\ell\ll d^{5/4}.
\]

But the M5-282 energy-shielded branch requires

\[
\boxed{\ell\gtrsim E_0^{-1/4}d^{5/4}.}
\]

Hence, under `Theta~1`, the finite-energy shield places the survivor on the borderline or on the opposite side from the easy Seregin exclusion.

This is a structural consistency, not a proof.

---

## 7. Why the current H/T branch does not provide `Theta~1`

The continuous backward Type-I vorticity estimate previously derived in the repository relied on bounded recurrent stage durations

\[
0<L_-\le L_j\le L_+<\infty.
\]

That is a restricted no-H/no-T Type-I corridor.

The current branch is precisely the complement in which H/T escalation is occurring.

Therefore one may **not** import the old Type-I estimate to assert

\[
\Theta=q^2(T^*-t)=O(1)
\]

for the remote satellite.

The satellite may instead lie in any of the regimes

\[
\Theta\ll1,
\qquad
\Theta\asymp1,
\qquad
\Theta\gg1.
\]

Hence the `5/4 -> alpha=3/2` dictionary is conditional on a new activity bridge.

---

## 8. Seregin's hypotheses are stronger than the variable dictionary

Even if one proves

\[
\chi\sim f(d),
\]

Seregin's theorem does not follow from this relation alone.

His Type-II scenario requires, among other things,

\[
\sup_r
\{A_f(v,r)+E_f(v,r)+D_f(q,r)\}<\infty
\]

and a specified `g`-weighted growth/nontriviality condition for

\[
M^{s,l}_\kappa.
\]

The current satellite ledgers have not established these exact weighted quantities with a common function `f`.

Thus

\[
\boxed{
\text{matching an exponent}
\not\Rightarrow
\text{matching Seregin's Type-II scenario}.
}
\]

---

## 9. What Seregin's result contributes to the DSD tree

The 2026 theorem supplies an external model for what a successful Type-II closure should look like:

1. identify a spatial zoom scale;
2. identify a non-parabolic time-compression factor `f`;
3. prove weighted local energy/dissipation/pressure control adapted to `f`;
4. obtain an Euler ancient limit;
5. apply an Euler Liouville theorem.

The current satellite analysis has already isolated the natural candidate for step 2:

\[
\boxed{
\chi=\frac{T^*-t}{d^2}
=\frac{\Theta}{L^2}.
}
\]

The missing work is to control `Theta` and establish weighted `A_f/E_f/D_f` estimates.

---

## 10. Updated Type-II coordinates

The minimal satellite state should henceforth be recorded using the pair

\[
\boxed{(L,\Theta)}
\]

rather than a single spatial exponent:

\[
L=qd=\frac d\ell,
\]

\[
\Theta=q^2(T^*-t)=\frac{T^*-t}{\ell^2}.
\]

Then

\[
\boxed{
\chi=\frac{T^*-t}{d^2}
=\frac{\Theta}{L^2}.
}
\]

This separates:

- spatial remoteness (`L`);
- remaining natural-time activity (`Theta`);
- Euler-vs-parabolic time compression (`chi`).

The old `5/4` law constrains only the spatial geometry and cannot replace this two-coordinate description.

---

## 11. DSD verdict

### PROVED / EXACT VARIABLE MATCH

- Seregin's `f(lambda)` is a time/spatial-square ratio, not a spatial length ratio;
- for `lambda=d`, the correct analogue is
  \[
  f(d)\leftrightarrow\chi=(T^*-t)/d^2;
  \]
- the satellite variables obey
  \[
  \chi=\Theta/L^2;
  \]
- conditional on `Theta~1`, the M5-282 boundary `ell~d^(5/4)` maps to the Seregin power borderline `alpha=3/2`;
- conditional on the same bridge, Seregin's simple `alpha>3/2` exclusion lies on the `ell<<d^(5/4)` side, which the energy-shield survivor does not occupy.

### FIREWALL

- `5/4` is not directly Seregin's `alpha`;
- the old no-H/no-T Type-I clock bound cannot be imported into the current H/T branch;
- exponent matching alone does not establish Seregin's weighted Type-II hypotheses.

### NEXT TARGET

Audit the activity coordinate

\[
\Theta=q^2(T^*-t)
\]

and derive an exhaustive passive/critical/hyperactive Type-II clock split. Then test whether any regime supplies the `f`-weighted `A_f/E_f/D_f` structure required by Seregin's theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]