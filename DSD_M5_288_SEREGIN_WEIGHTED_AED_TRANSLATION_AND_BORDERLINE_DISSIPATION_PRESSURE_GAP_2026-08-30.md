# DSD M5-288 — Seregin Weighted `A/E/D` Translation and Borderline Dissipation--Pressure Gap

Date: 2026-08-30

Parent: `DSD_M5_287_SATELLITE_ACTIVITY_RATIO_AND_TYPEII_CLOCK_COORDINATE_2026-08-30.md`

External reference: Gregory Seregin, *On potential Type II blowups for the Navier--Stokes equations*, arXiv:2606.29468v1.

Status: **HYPOTHESIS TRANSLATION / WITH THE DISTANCE-BASED EULER-TIME FACTOR `f(d)=chi=(T*-t)/d^2`, SEREGIN'S WEIGHTED LOCAL QUANTITIES ARE EXACTLY `A_f=chi^2 A`, `E_f=chi E`, AND `D_f=chi^2 D` / ON THE CRITICAL-CLOCK ENERGY-SHIELD BORDERLINE `chi~d^(1/2)`, THE VELOCITY-ENERGY CONDITION `d A(d)<=C` IS AUTOMATIC FROM GLOBAL FINITE KINETIC ENERGY, WHILE THE NONTRIVIAL MISSING CONDITIONS ARE `d^(1/2) E(d)<=C` AND `d D(d)<=C` / THUS THE SEREGIN BRIDGE REDUCES TO A WEIGHTED DISSIPATION/PRESSURE PROBLEM PLUS HIS SEPARATE `g`-NONTRIVIALITY CONDITION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Standard CKN quantities

At spatial radius `r` around the candidate singular center, write

\[
A(v,r)
:=\sup_{-r^2<t<0}
\frac1r\int_{B(r)}|v(x,t)|^2dx,
\]

\[
E(v,r)
:=\frac1r\int_{Q(r)}|\nabla v|^2dz,
\]

and

\[
D(q,r)
:=\frac1{r^2}\int_{Q(r)}|q|^{3/2}dz.
\]

These are the usual scale-invariant local energy, dissipation, and pressure quantities.

---

## 2. Seregin's weighted quantities are simple multipliers

The 2026 paper defines

\[
E_f(v,r)
=\frac{f(r)}r\int_{Q(r)}|\nabla v|^2dz,
\]

\[
A_f(v,r)
=\sup_{-r^2<t<0}
\frac{f(r)^2}{r}
\int_{B(r)}|v|^2dx,
\]

\[
D_f(q,r)
=\frac{f(r)^2}{r^2}
\int_{Q(r)}|q|^{3/2}dz.
\]

Therefore, exactly,

\[
\boxed{
A_f(r)=f(r)^2A(r),
}
\]

\[
\boxed{
E_f(r)=f(r)E(r),
}
\]

and

\[
\boxed{
D_f(r)=f(r)^2D(r).
}
\]

No approximation is involved.

---

## 3. Insert the satellite clock factor

M5-286--287 identify the satellite analogue of Seregin's time-compression factor at the separation scale `d` as

\[
\boxed{
f(d)=\chi:=\frac{T^*-t}{d^2}.}
\]

Hence the Seregin weighted local quantities become

\[
\boxed{
A_\chi(d)=\chi^2A(d),
}
\]

\[
\boxed{
E_\chi(d)=\chi E(d),
}
\]

\[
\boxed{
D_\chi(d)=\chi^2D(d).
}
\]

Thus the relevant weighted boundedness hypothesis is

\[
\boxed{
\sup_d
\{\chi(d)^2A(d)+\chi(d)E(d)+\chi(d)^2D(d)\}<\infty
}
\]

along a coherent scale function/sequence.

---

## 4. Critical-clock `5/4` boundary

Suppose

\[
\Theta\asymp1
\]

and the satellite lies on the M5-282 energy-shield boundary

\[
\ell\asymp d^{5/4}.
\]

Then M5-286 gives

\[
\boxed{\chi\asymp d^{1/2}.}
\]

Therefore

\[
\boxed{
A_\chi(d)\asymp dA(d),
}
\]

\[
\boxed{
E_\chi(d)\asymp d^{1/2}E(d),
}
\]

and

\[
\boxed{
D_\chi(d)\asymp dD(d).
}
\]

The Seregin weighted corridor at the borderline is thus

\[
\boxed{
dA(d)+d^{1/2}E(d)+dD(d)\lesssim1.}
\]

---

## 5. The weighted velocity-energy condition is automatic

Let

\[
\|u(t)\|_2^2\le E_0
\]

be the global Leray--Hopf kinetic-energy bound.

Then

\[
A(d)
=\sup_t\frac1d\int_{B_d}|u|^2
\le\frac{E_0}{d}.
\]

Hence

\[
\boxed{
dA(d)\le E_0.}
\]

Therefore, on the critical-clock `5/4` boundary,

\[
\boxed{A_\chi(d)\lesssim E_0}
\]

without any new local estimate.

This is a genuine simplification: the velocity-energy part of Seregin's weighted Type-II hypothesis is already compatible with the original finite-energy ancestry.

---

## 6. Global dissipation is too weak for the weighted dissipation condition

The global energy inequality gives only

\[
\int_0^{T^*}\int_{\mathbb R^3}|\nabla u|^2
\lesssim E_0
\]

in viscosity-normalized units.

Therefore

\[
E(d)
\lesssim\frac{E_0}{d}
\]

as a crude bound.

At the borderline,

\[
E_\chi(d)
\asymp d^{1/2}E(d)
\lesssim E_0d^{-1/2},
\]

which may diverge.

Thus finite total dissipation does **not** prove

\[
\boxed{d^{1/2}E(d)\lesssim1.}
\]

A genuinely stronger local Type-II dissipation estimate is required.

---

## 7. Pressure remains an independent weighted gap

Likewise the desired pressure condition is

\[
\boxed{dD(d)\lesssim1.}
\]

on the critical-clock `5/4` boundary.

The usual local pressure decomposition can estimate `D` from local velocity quantities plus far-field terms, but on the present H/T branch the strong scale-invariant bounds needed to make `dD` uniform have not yet been proved.

Therefore pressure cannot be declared automatic merely because `dA` is bounded.

The current nontrivial weighted pair is

\[
\boxed{
d^{1/2}E(d),
\qquad
dD(d).}
\]

---

## 8. Relation to the old H/T master tree

The standard Type-II definition is precisely that at least one of the unweighted quantities

\[
A(d),\quad E(d),\quad C(d)
\]

becomes unbounded as `d -> 0` in the relevant sense.

Seregin's weighted corridor permits controlled divergence.

At the `alpha=3/2` boundary, for example, it allows schematically

\[
A(d)=O(d^{-1}),
\]

\[
E(d)=O(d^{-1/2}),
\]

and analogous weighted pressure growth.

Thus a Type-II H/T branch need not be quiet in the old CKN variables to fit the Euler-zoom compactness class.

This is exactly why the weighted formulation is potentially useful here.

---

## 9. Passive and hyperactive clocks modify the weights

In general

\[
\chi=\frac{\Theta}{L^2}.
\]

Hence the weighted conditions are

\[
\boxed{
\frac{\Theta^2}{L^4}A(d)\lesssim1,
}
\]

\[
\boxed{
\frac{\Theta}{L^2}E(d)\lesssim1,
}
\]

\[
\boxed{
\frac{\Theta^2}{L^4}D(d)\lesssim1.
}
\]

A smaller `Theta` weakens the weighted requirements, while a larger `Theta` strengthens them.

This shows why the activity coordinate cannot be omitted from the Type-II audit.

---

## 10. Seregin's additional nontriviality condition remains separate

Even if

\[
A_\chi+E_\chi+D_\chi
\]

is uniformly bounded, Seregin's scenario theorem also assumes a scale-dependent nontriviality/growth condition expressed through

\[
M^{s,l}_\kappa
\]

or its shortened-time version

\[
\overline M^{s,l}_\kappa,
\]

with a function `g` related to `f`.

The remote-vorticity mark

\[
|\omega(x,t)|>0
\]

is not by itself the same as that spacetime mixed-norm lower bound.

Thus one still needs a packet/nontriviality bridge.

---

## 11. Updated Seregin bridge checklist

On the critical-clock `5/4` frontier:

### Already available

\[
\boxed{dA(d)\le E_0.}
\]

### Still required

\[
\boxed{d^{1/2}E(d)\le C,}
\]

\[
\boxed{dD(d)\le C,}
\]

and a compatible `g`-weighted mixed-norm lower bound for nontriviality.

Only after these are proved can the Seregin Euler-limit machinery be imported honestly.

---

## 12. DSD verdict

### PROVED

- exact translation
  \[
  A_f=f^2A,\quad E_f=fE,\quad D_f=f^2D;
  \]
- with `f(d)=chi`, these become `chi^2 A`, `chi E`, `chi^2 D`;
- on `Theta~1`, `ell~d^(5/4)`, the requirements are `dA`, `d^(1/2)E`, `dD` bounded;
- finite kinetic energy automatically controls `dA`.

### OPEN

- weighted local dissipation `d^(1/2)E`;
- weighted pressure `dD`;
- Seregin's `g`-nontriviality condition;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]