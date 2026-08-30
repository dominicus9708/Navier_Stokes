# DSD M5-287 — Satellite Activity Ratio and Type-II Clock Coordinate

Date: 2026-08-30

Parent: `DSD_M5_286_SEREGIN_TYPEII_EULER_ZOOM_VS_SATELLITE_5_4_SCALING_AUDIT_2026-08-30.md`

Status: **DYNAMIC COORDINATE REFINEMENT / THE NATURAL SATELLITE ACTIVITY VARIABLE IS EXACTLY `Theta=(T*-t)|omega(x,t)|` / TOGETHER WITH THE REMOTENESS `L=d sqrt(|omega|)` IT COMPLETELY DETERMINES THE DISTANCE-BASED EULER-TIME RATIO `chi=(T*-t)/d^2=Theta/L^2` / THIS SEPARATES SUB-TYPE-I PASSIVE SATELLITES, TYPE-I-STRENGTH SATELLITES, AND GENUINELY TYPE-II-STRENGTH SATELLITES / THE ENERGY-SHIELD `5/4` LAW CONSTRAINS THE SPATIAL COORDINATE BUT DOES NOT CONTROL `Theta` / SEREGIN'S EULER-ZOOM REGIME REQUIRES CONTROL OF `chi`, NOT `Theta` OR `L` ALONE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Physical satellite variables

At a satellite point `(x,t)` with `t<T*`, write

\[
a:=T^*-t,
\]

\[
m:=|\omega(x,t)|,
\]

\[
q:=m^{1/2},
\qquad
\ell:=q^{-1}=m^{-1/2},
\]

and let `d` be the distance from the tracked main core/candidate singular center.

The remote-satellite parameter is

\[
\boxed{L:=qd=\frac d\ell.}
\]

The satellite frontier has

\[
L\to\infty.
\]

---

## 2. The activity coordinate is the local Type-I product

Define

\[
\boxed{\Theta:=q^2a.}
\]

Since

\[
q^2=m=|\omega(x,t)|,
\]

this is exactly

\[
\boxed{
\Theta
=(T^*-t)|\omega(x,t)|.
}
\]

Thus `Theta` is not merely a convenient normalization. It is the local vorticity Type-I product at the selected satellite.

The global vorticity maximum `W(t)=||omega(t)||_infinity` satisfies

\[
\boxed{
(T^*-t)W(t)\ge\Theta.
}
\]

Therefore any sequence with

\[
\Theta_n\to\infty
\]

forces genuine global vorticity Type-II escalation:

\[
\boxed{
(T^*-t_n)\|\omega(t_n)\|_\infty\to\infty.
}
\]

---

## 3. The distance-based clock

Define

\[
\boxed{\chi:=\frac a{d^2}.}
\]

Because

\[
d=L\ell
\]

and

\[
a=\Theta\ell^2,
\]

we have the exact identity

\[
\boxed{
\chi=\frac{\Theta}{L^2}.
}
\]

Equivalently,

\[
\boxed{
a=\Theta\frac{d^2}{L^2}.}
\]

This is the key two-coordinate relation.

---

## 4. Three natural-time regimes

### P — clock-passive/sub-Type-I satellite

\[
\boxed{\Theta\to0.}
\]

Then

\[
a\ll\ell^2.
\]

Only a vanishing fraction of one satellite natural parabolic time remains before `T*`.

A natural-band packet cannot be strongly erased over this interval by order-one natural-scale forcing: the heat semigroup changes it only by `O(Theta)`, and an order-one fractional forgetting requires normalized forcing action of order one over a time interval of length `Theta`.

Thus, under a fixed quiet forcing ceiling, a `Theta -> 0` satellite is **persistent/passive** rather than dynamically rebuilt.

If it is nevertheless forgotten/rebuilt by a fixed fraction, the required instantaneous normalized forcing must scale at least schematically like

\[
\boxed{\Theta^{-1},}
\]

routing to a dynamic H/T/pressure/localization exit.

This is the satellite analogue of the historical `K^{-2}` compressed-time forgetting gate.

### C — critical Type-I-strength satellite

\[
\boxed{0<c\le\Theta\le C<\infty.}
\]

Then

\[
a\asymp\ell^2.
\]

No small or large natural-time parameter is available.

This is the true scale-critical clock regime. The M5-286 dictionary between the `5/4` shield and Seregin's `alpha=3/2` boundary lives here.

### II — local Type-II-strength satellite

\[
\boxed{\Theta\to\infty.}
\]

Then

\[
a\gg\ell^2.
\]

The satellite is observed with many of its own natural parabolic times remaining before `T*`.

This regime is not a contradiction: diffusion may erase a satellite during such a long interval unless nonlinear stretching/replenishment keeps it active.

However it is a genuine Type-II marker because

\[
(T^*-t)\|\omega(t)\|_\infty\ge\Theta\to\infty.
\]

Thus any survivor in this branch must be treated as a true Type-II blowup scenario, not with the old Type-I clock estimates.

---

## 5. Euler-time compression is controlled by `Theta/L^2`

Seregin's Euler zoom uses a factor

\[
f(\lambda)
=\frac{\text{time scale}}{\lambda^2}.
\]

With spatial scale `lambda=d`, the satellite analogue is

\[
\boxed{f(d)\leftrightarrow\chi=\Theta/L^2.}
\]

Therefore the condition for an Euler-fast-time regime is

\[
\boxed{\chi\to0}
\]

or equivalently

\[
\boxed{\Theta=o(L^2).}
\]

This includes all bounded-Theta satellites because `L->infinity`, but it may also include Type-II-strength satellites with

\[
1\ll\Theta\ll L^2.
\]

Conversely,

\[
\Theta\asymp L^2
\]

gives

\[
\chi\asymp1,
\]

and

\[
\Theta\gg L^2
\]

gives a time horizon longer than the distance-based parabolic scale.

Hence the local Type-II classification by `Theta` and the Euler-zoom classification by `chi` are different.

---

## 6. Energy-shield relation in `(L,Theta)` variables

M5-282's shield condition is

\[
q^4d^5\lesssim E_0.
\]

Since

\[
q=\frac Ld,
\]

we obtain the exact equivalent form

\[
\boxed{dL^4\lesssim E_0.}
\]

Therefore

\[
\boxed{d\lesssim E_0L^{-4}.}
\]

Using

\[
a=\Theta\frac{d^2}{L^2},
\]

one gets the conditional upper estimate

\[
\boxed{
a\lesssim
\Theta E_0^2L^{-10}.}
\]

This is exact up to the fixed shield constant.

It shows that, if `Theta` stays bounded, shielded remote satellites must occur extremely close to terminal time as `L -> infinity`.

But if `Theta` grows, that temporal gain may be canceled.

---

## 7. Recover the `5/4` / `alpha=3/2` boundary

On the critical clock branch

\[
\Theta\asymp1,
\]

one has

\[
a\asymp\ell^2.
\]

At the energy-shield boundary

\[
\ell\asymp d^{5/4},
\]

so

\[
a\asymp d^{5/2}.
\]

Therefore

\[
\chi=\frac a{d^2}\asymp d^{1/2}.
\]

This is precisely Seregin's power factor

\[
f(d)\sim d^{\alpha-1}
\]

with

\[
\boxed{\alpha=3/2.}
\]

Again: the identification is valid because `Theta~1` supplies the missing time relation.

---

## 8. What happens on the passive side

If

\[
\Theta\to0,
\]

then even on the spatial shield boundary

\[
\chi
=\frac{\Theta}{L^2}
\]

is smaller than the critical-clock value.

Thus a passive satellite may formally enter a faster Euler-time compression regime than the `alpha=3/2` power dictionary suggests.

But this does **not** automatically invoke Seregin's theorem, because his weighted `A_f/E_f/D_f` and `g` hypotheses have not been proved for the satellite family.

The correct DSD interpretation is:

\[
\boxed{
\Theta\to0
\Rightarrow
\text{compressed-time persistent-tail / forgetting problem},
}
\]

not an automatic Type-II Liouville contradiction.

---

## 9. What happens on the hyperactive side

If

\[
\Theta\to\infty,
\]

there are three subregimes:

\[
1\ll\Theta\ll L^2
\quad\Rightarrow\quad
\chi\to0,
\]

\[
\Theta\asymp L^2
\quad\Rightarrow\quad
\chi\asymp1,
\]

\[
\Theta\gg L^2
\quad\Rightarrow\quad
\chi\to\infty.
\]

Only the first is naturally comparable to an Euler-fast-time zoom.

The second and third are not described by a function `f(d)->0` of the Seregin type at that selected spatial separation scale.

Thus the Type-II satellite frontier cannot be described by one exponent.

---

## 10. Updated master coordinates

The appropriate satellite descriptor is now

\[
\boxed{
(L,\Theta,\chi),
\qquad
\chi=\Theta/L^2,
}
\]

with only two independent variables.

Interpretation:

- `L`: spatial scale separation from the main core;
- `Theta`: local natural-time activity / vorticity Type-I product;
- `chi`: time-to-distance-square ratio / Euler-time compression.

Any future Type-II theorem imported into the DSD tree should first be translated into these coordinates.

---

## 11. DSD verdict

### PROVED

- `Theta=(T*-t)|omega(x,t)|` exactly;
- `Theta->infinity` forces global vorticity Type-II escalation along the same sequence;
- `chi=Theta/L^2` exactly;
- the energy shield is `d L^4 <= C E_0`;
- under the shield, `a <= C Theta E_0^2 L^-10`;
- `Theta~1` recovers the `5/4 <-> alpha=3/2` boundary.

### STRUCTURAL ROUTING

\[
\Theta\to0:
\text{ passive/compressed-time persistence or large forgetting action},
\]

\[
\Theta\asymp1:
\text{ critical satellite},
\]

\[
\Theta\to\infty:
\text{ genuine local/global Type-II escalation}.
\]

### FIREWALL

- `Theta>>1` is not itself a contradiction;
- `chi->0` is not sufficient for Seregin's theorem without his weighted hypotheses;
- the old Type-I clock bounds are not available on the current H/T branch.

### NEXT TARGET

For each clock regime, audit whether the existing localized packet and local-energy ledgers yield the weighted quantities analogous to Seregin's

\[
A_f,\quad E_f,\quad D_f,
\]

with

\[
f(d)=\chi.
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]