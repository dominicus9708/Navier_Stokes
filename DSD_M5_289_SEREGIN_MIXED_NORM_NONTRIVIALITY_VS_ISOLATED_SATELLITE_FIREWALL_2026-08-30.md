# DSD M5-289 — Seregin Mixed-Norm Nontriviality versus Isolated Satellite Firewall

Date: 2026-08-30

Parent: `DSD_M5_288_SEREGIN_WEIGHTED_AED_TRANSLATION_AND_BORDERLINE_DISSIPATION_PRESSURE_GAP_2026-08-30.md`

External reference: Gregory Seregin, *On potential Type II blowups for the Navier--Stokes equations*, arXiv:2606.29468v1.

Status: **NONTRIVIALITY HYPOTHESIS AUDIT / A SINGLE NATURAL VORTICITY SATELLITE HAS ORDER-ONE SCALE-INVARIANT `M_kappa^{s,l}` AT ITS OWN NATURAL SCALE AND THEREFORE FAILS SEREGIN'S TYPE-II ASSUMPTION `g(r) M_kappa >= epsilon_0` WHEN `g(r)->0` / VIEWED FROM THE OUTER SEPARATION SCALE `d`, EVEN A SATELLITE PERSISTING THROUGH THE WHOLE AVAILABLE TIME HAS `bar M_kappa(d) ~ Theta L^{-kappa}`, SO AN ISOLATED REMOTE SATELLITE BECOMES INVISIBLE IN THE OUTER MIXED-NORM ZOOM / SEREGIN'S 2026 THEOREMS EXCLUDE SPECIFIC MIXED-NORM-MASS TYPE-II SCENARIOS, NOT THE POINT-PICKED SATELLITE CLASS BY ITSELF / GLOBAL REGULARITY UNPROVED.**

---

## 1. Seregin's mixed scale-invariant quantity

For numbers `s,l` in the admissible range, define

\[
\kappa
:=l\left(\frac3s+\frac2l-1\right)
=2+l\left(\frac3s-1\right)>0.
\]

Seregin uses

\[
\boxed{
M^{s,l}_{\kappa}(v,r)
=
\frac1{r^\kappa}
\int_{-r^2}^{0}
\left(\int_{B(r)}|v|^sdx\right)^{l/s}dt.
}
\]

One Type-II scenario assumes a function

\[
g(r)\to0
\]

and a sequence `r_k -> 0` for which

\[
\boxed{
g(r_k)M^{s,l}_{\kappa}(v,r_k)\ge\varepsilon_0>0.}
\]

Thus the mixed norm must grow at least like `1/g(r_k)`.

---

## 2. Natural satellite packet scaling

Consider one vorticity-natural satellite packet of scale

\[
\ell=q^{-1}
\]

with the standard natural velocity amplitude

\[
|u|\sim\ell^{-1}
\]

on spatial volume

\[
\sim\ell^3
\]

for one natural parabolic time

\[
\sim\ell^2.
\]

Then

\[
\int_{B(\ell)}|u|^sdx
\sim
\ell^{3-s}.
\]

Raising to `l/s` gives

\[
\left(\int|u|^s\right)^{l/s}
\sim
\ell^{\frac{3l}{s}-l}.
\]

Integrating through one natural time gives

\[
\ell^{2+\frac{3l}{s}-l}.
\]

But

\[
2+\frac{3l}{s}-l=\kappa.
\]

Hence

\[
\boxed{
M^{s,l}_{\kappa}(u,\ell)\sim1.
}
\]

This is precisely the expected scale invariance of a single natural packet.

---

## 3. A single natural satellite fails the `g`-amplified scenario

Because

\[
g(\ell)\to0,
\]

one obtains

\[
\boxed{
g(\ell)M^{s,l}_{\kappa}(u,\ell)\to0.}
\]

Therefore the point-picked condition

\[
|\omega(x,t)|\sim\ell^{-2}
\]

on one nondegenerate natural satellite does **not** imply Seregin's nontriviality condition.

To satisfy

\[
g(r)M_\kappa(r)\ge\varepsilon_0,
\]

the Type-II configuration must contain additional amplitude, multiplicity, persistence, or spatial extent sufficient to make

\[
M_\kappa(r)\gtrsim g(r)^{-1}\to\infty.
\]

---

## 4. Relation to Seregin's inner radius `r=lambda sqrt(f(lambda))`

In the Euler zoom of Section 2, Seregin chooses

\[
r_k=\lambda_k\sqrt{f(\lambda_k)}.
\]

For the satellite dictionary

\[
\lambda=d,
\qquad
f(d)=\chi=\frac a{d^2},
\]

this inner radius is

\[
\boxed{
r_k=d\sqrt\chi=\sqrt a.}
\]

On the critical clock branch

\[
\Theta=\frac a{\ell^2}\asymp1,
\]

we have

\[
\sqrt a\asymp\ell.
\]

Thus Seregin's inner mixed-norm scale coincides, up to constants, with the natural satellite scale in the `Theta~1` regime.

Even then, a single natural satellite gives only

\[
M_\kappa\sim1,
\]

not the required `1/g` amplification.

This confirms that the mismatch is not caused by choosing the wrong inner scale.

---

## 5. Truncated-time mixed norm at the outer separation scale

Seregin's Section 3 also uses

\[
\boxed{
\overline M^{s,l}_{\kappa}(v,d)
=
\frac1{d^\kappa}
\int_{-d^2f(d)}^0
\left(\int_{B(d)}|v|^sdx\right)^{l/s}dt.
}
\]

With the satellite clock

\[
f(d)=\chi,
\]

the integration interval has length

\[
d^2\chi=a=\Theta\ell^2.
\]

Suppose, as a maximal persistence model, that one natural satellite of amplitude `ell^-1` remains coherent throughout this entire interval.

Then the time integral gains a factor `Theta` relative to one natural lifetime, and

\[
\overline M_\kappa(d)
\sim
\frac{\Theta\ell^\kappa}{d^\kappa}.
\]

Since

\[
L=\frac d\ell,
\]

we get

\[
\boxed{
\overline M_\kappa(d)
\sim
\Theta L^{-\kappa}.
}
\]

For a remote satellite

\[
L\to\infty.
\]

Thus for bounded `Theta`, or even for `Theta=o(L^kappa)`, the outer-scale mixed norm tends to zero.

The satellite becomes invisible at the separation scale.

---

## 6. Required amplification for Seregin's Section-3 scenario

The shortened-time Type-II scenario uses a factor `g(d)` related to `f(d)` and requires

\[
\boxed{
g(d)\overline M_\kappa(d)\ge\varepsilon_0.}
\]

For an isolated persistent satellite, the scaling above gives only

\[
g(d)\Theta L^{-\kappa}.
\]

Hence the scenario requires schematically

\[
\boxed{
\Theta
\gtrsim
\frac{L^\kappa}{g(d)}
}
\]

unless additional simultaneous packet multiplicity or larger-than-natural amplitude contributes.

This is much stronger than the mere remote-satellite condition

\[
L\to\infty.
\]

---

## 7. Multiplicity interpretation

If there are many comparable natural packets in the outer ball/time slab, the mixed norm can increase.

The exact exponent depends on whether packets overlap in time and on the `l/s` power, so no universal linear counting formula should be asserted without an occupancy model.

What is robust is:

\[
\boxed{
\text{one natural packet}
\Rightarrow
M_\kappa=O(1),
}
\]

whereas Seregin's Type-II nontriviality requires

\[
\boxed{
M_\kappa\to\infty
\text{ at a prescribed }1/g\text{ rate}.
}
\]

Therefore his scenario is a **mass/multiplicity/persistence enhancement** of the point-picked satellite class.

---

## 8. Consequence for the `5/4` comparison

M5-286 showed that, on `Theta~1`, the spatial energy-shield boundary maps to Seregin's power exponent `alpha=3/2` at the level of the time-compression function.

The present note adds a second independent requirement:

\[
\boxed{
\text{clock/exponent match}
\not\Rightarrow
\text{mixed-norm nontriviality match}.
}
\]

Even exactly at the `alpha=3/2` clock boundary, an isolated satellite is too small in the `M_\kappa` sense to enter Seregin's Type-II scenario.

---

## 9. What Seregin can still eliminate inside the DSD tree

Suppose a Type-II H/T branch can be upgraded from isolated satellites to a coherent family satisfying simultaneously:

1. a function `f` represented by `chi`;
2. bounded weighted `A_f/E_f/D_f`;
3. the required `g M_\kappa >= epsilon_0` amplification.

Then Seregin's theorem can exclude parameter regimes satisfying his relation between `f` and `g`, and in the power example the easy Euler-energy argument excludes `alpha>3/2`.

Thus the paper supplies a **conditional pruning theorem for amplified Type-II satellite clusters**, not a universal isolated-satellite theorem.

---

## 10. Updated Type-II split

The satellite frontier should now be split into

\[
\boxed{
S_{iso}:
\text{isolated/natural packet strength},
}
\]

and

\[
\boxed{
S_{amp}:
\text{mixed-norm amplified packet family}.
}
\]

`S_amp` may be tested against Seregin's `f/g` theorem after the weighted `A/E/D` bridge.

`S_iso` remains governed by ancestry, restart coherence, persistence/turnover, and detached ancient-profile rigidity.

---

## 11. DSD verdict

### PROVED BY SCALING

- one natural packet has `M_kappa(ell)=O(1)`;
- therefore `g(ell) M_kappa -> 0` whenever `g -> 0`;
- with `f(d)=chi`, Seregin's inner radius is `sqrt(a)`, which equals `ell` on `Theta~1`;
- even a packet persisting throughout the shortened outer time has
  \[
  \overline M_\kappa(d)\sim\Theta L^{-\kappa};
  \]
- isolated remote satellites do not automatically satisfy Seregin's nontriviality hypothesis.

### CONDITIONAL EXTERNAL PRUNING

Seregin's theorem becomes relevant only after the satellite branch is shown to be **mixed-norm amplified** and to satisfy the weighted local bounds.

### OPEN

- isolated satellite ancestry/rigidity;
- amplified-family weighted dissipation and pressure;
- multiplicity/persistence bridge to the `g` condition;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]