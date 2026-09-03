# DSD M17-012 — Positive-density nodal phases force a finite-radius positive-kappa sheath and a compensating negative payer

Date: 2026-09-03
Canonical ID: **M17-012**

Status: **INTERNAL JET-TO-SHEATH TRANSFER / UNDER THE SAME UNIFORMLY REGULAR RECURRENT-JACOBIAN ASSUMPTIONS USED IN M17-010, PLUS THE COMPACT `C^m` HARD-HULL BOUNDS ALREADY USED IN M17-009, THE MEAN LAW `⟨kappa_0⟩_nodal = 3/2` FORCES A POSITIVE TIME-DENSITY SET OF PHASES ON WHICH `kappa_0` IS UNIFORMLY POSITIVE. THE JACOBIAN LOWER BOUND AND UNIFORM SECOND-DERIVATIVE CONTROL THEN GIVE A UNIFORM TUBULAR NEIGHBORHOOD WHERE `|W|` GROWS AT LEAST LINEARLY AWAY FROM THE FILAMENT, WHILE UNIFORM `C^1` CONTROL OF `kappa` KEEPS `kappa` POSITIVE. EACH SUCH PHASE THEREFORE CARRIES A FIXED POSITIVE `∫ kappa|W|^2` SHEATH CHARGE. THE GLOBAL IDENTITY `∫ kappa|W|^2=-P<0` THEN FORCES A COMPENSATING NEGATIVE-KAPPA PAYER OF AT LEAST THE SAME FIXED SIZE. THIS CLOSES THE PURE MEASURE-ZERO ESCAPE AND BRIDGES THE M17 WINDING BRANCH BACK TO THE M5 ZERO-LEVEL / HYSTERESIS CONVEYOR; IT IS NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-010 and M17-011

Let `Gamma(theta)` be a uniformly recurrent regular material winding filament in the M17 rank-one great-circle branch.
Along the marked material nodal trajectory, M17-010 gives

\[
\boxed{
\langle\kappa_0\rangle=\frac32,
}
\]

where

\[
\kappa_0(\theta):=\kappa(\Gamma(\theta),\theta).
\]

The same branch assumes a uniformly nondegenerate horizontal nodal Jacobian:

\[
\boxed{
0<c_G\le |\det G_h(\theta)|
}
\]

with

\[
G_h=\partial_{(y_1,y_2)}(W_1,W_2)
\]

in the canonical great-circle frame.

M17-011 showed that the infinitesimal `|W|^2` weight alone is too thin to produce a contradiction and identified the correct first-jet descriptor.

The present step asks whether compactness turns that first-jet information into a **uniform nonzero-radius sheath statement**.

---

## 2. Uniform compact-hull constants

The compact smooth/analytic hard hull used in M17-009 gives finite bounds on every fixed spatial derivative order on the marked finite core.
Fix constants

\[
\boxed{
\|G_h\|_{op}\le M_1,
\qquad
|\nabla^2W|\le M_2,
\qquad
|\nabla\kappa|\le L_\kappa,
\qquad
\kappa_0\le K_\kappa<\infty.
}
\]

Because

\[
|\det G_h|=\sigma_{max}(G_h)\sigma_{min}(G_h)
\]

and

\[
\sigma_{max}(G_h)\le M_1,
\]

we obtain the uniform smallest-singular-value lower bound

\[
\boxed{
a_0:=\frac{c_G}{M_1}>0,
\qquad
\sigma_{min}(G_h)\ge a_0.
}
\]

Thus the first transverse jet cannot become arbitrarily weak on the retained recurrent branch.

---

## 3. Positive mean implies positive-density strongly positive phases

Choose any threshold

\[
0<\eta<\frac32.
\]

Let

\[
E_\eta:=\{\theta:\kappa_0(\theta)\ge\eta\}.
\]

Write its lower asymptotic time density as `d_eta`.
Since `kappa_0 <= K_kappa`,

\[
\langle\kappa_0\rangle
\le
 d_\eta K_\kappa+(1-d_\eta)\eta.
\]

Using

\[
\langle\kappa_0\rangle=\frac32
\]

gives

\[
\boxed{
d_\eta
\ge
\frac{\frac32-\eta}{K_\kappa-\eta}
>0
}
\]

whenever `K_kappa > eta`.

A convenient fixed choice is

\[
\eta=\frac34,
\]

for which

\[
\boxed{
d_{3/4}
\ge
\frac{3/4}{K_\kappa-3/4}>0.
}
\]

If `K_kappa=3/2`, the mean identity is even more rigid: `kappa_0=3/2` almost everywhere on the recurrent average.

Thus the positive nodal mean cannot be concentrated into a zero-density sequence of arbitrarily large spikes.

---

## 4. Uniform tubular linear growth of vorticity

At a phase `theta in E_eta`, center local tubular coordinates `(s,z)` on the marked filament point, with `z` transverse.
At the center,

\[
W=0,
\qquad
\sigma_{min}(G_h)\ge a_0.
\]

By the uniform `M_2` bound and quantitative continuity of the transverse Jacobian, there exists a hard-hull-uniform tubular chart with some axial half-length `ell_0>0` and transverse radius `r_G>0` such that

\[
\sigma_{min}A(s)\ge\frac{a_0}{2}
\]

throughout that chart.

Taylor expansion in the transverse variable gives

\[
W(s,z)=A(s)z+R(s,z),
\qquad
|R(s,z)|\le\frac{M_2}{2}|z|^2.
\]

Choose

\[
r_G\le\frac{a_0}{2M_2}.
\]

Then for `|z|<=r_G`,

\[
|W|
\ge
\frac{a_0}{2}|z|-
\frac{M_2}{2}|z|^2
\ge
\boxed{
\frac{a_0}{4}|z|.
}
\]

Hence the nodal first-jet floor becomes a uniform finite-radius lower bound on vorticity magnitude.

---

## 5. Uniform positivity radius for kappa

At the marked point of a phase in `E_eta`,

\[
\kappa_0\ge\eta.
\]

The uniform spatial Lipschitz bound gives

\[
|\kappa(x)-\kappa_0|
\le L_\kappa |x-x_0|.
\]

Therefore there exists a uniform geometric radius

\[
R_\kappa
:=
\begin{cases}
\eta/(2L_\kappa),&L_\kappa>0,\\
+\infty,&L_\kappa=0,
\end{cases}
\]

such that inside `B_{R_kappa}(x_0)`,

\[
\boxed{
\kappa\ge\frac\eta2>0.
}
\]

Shrink the tubular chart, if necessary, so that its cylinder is contained in this ball.
Define final uniform dimensions

\[
\boxed{
r_*:=\min(r_G,r_\kappa,r_{geo})>0,
\qquad
\ell_*:=\min(\ell_0,\ell_\kappa,\ell_{geo})>0,
}
\]

where the geometric constants only guarantee a regular tubular coordinate Jacobian.

---

## 6. Fixed positive sheath charge

On the uniform tube

\[
\mathcal T_*
=
\{|s|<\ell_*,\ |z|<r_*\},
\]

we have

\[
\kappa\ge\frac\eta2,
\qquad
|W|^2\ge\frac{a_0^2}{16}|z|^2.
\]

For a sufficiently small uniform tubular chart, let the coordinate Jacobian satisfy

\[
J_{geo}\ge c_{geo}>0.
\]

Then

\[
\begin{aligned}
\int_{\mathcal T_*}\kappa|W|^2dx
&\ge
c_{geo}
\frac{\eta a_0^2}{32}
\int_{-\ell_*}^{\ell_*}
\int_{|z|<r_*}|z|^2\,dz\,ds\\
&=
 c_{geo}
\frac{\pi\eta a_0^2}{32}
\ell_*r_*^4.
\end{aligned}
\]

Define

\[
\boxed{
Q_*
:=
 c_{geo}
\frac{\pi\eta a_0^2}{32}
\ell_*r_*^4
>0.
}
\]

Therefore every strongly positive nodal phase in `E_eta` carries a fixed positive three-dimensional sheath charge:

\[
\boxed{
\int_{\kappa>0}\kappa|W|^2dx
\ge Q_*.
}
\]

This is the desired jet-to-sheath transfer.

The regular winding skeleton can no longer evade the bulk measure purely by being codimension two.

---

## 7. Global identity forces a fixed negative payer

Split the global signed weighted integral into

\[
Q_+(\theta)
:=
\int_{\kappa>0}\kappa|W|^2dx,
\]

and

\[
Q_-(\theta)
:=
\int_{\kappa<0}(-\kappa)|W|^2dx.
\]

The CE-H identity is

\[
Q_+-Q_-=-P,
\qquad P>0.
\]

Thus

\[
\boxed{
Q_-=P+Q_+.
}
\]

On every phase in `E_eta`,

\[
Q_+\ge Q_*,
\]

so

\[
\boxed{
Q_-\ge P+Q_*\ge Q_*.
}
\]

Hence a uniformly recurrent regular winding filament forces, with positive time density, a **coherent finite negative-kappa payer** somewhere in the active bulk.

The negative payer cannot disappear into a measure-zero set because its weighted integral is bounded below by the fixed constant `Q_*` on those phases.

---

## 8. Consequence for the zero-kappa transition set

At a strongly positive nodal phase there is an open positive-`kappa` tube, while the negative-payer identity gives active points with `kappa<0`.

Whenever these regions lie in the same connected `kappa`-defined active component, continuity forces at least one intervening zero crossing:

\[
\boxed{
\kappa>0
\quad\leadsto\quad
\kappa=0
\quad\leadsto\quad
\kappa<0.
}
\]

This statement by itself does **not** guarantee that the zero set is a regular codimension-one sheet.
A singular zero level, critical point, or domain-separation event remains possible and must be classified separately.

If the zero level is regular and persistent under the synchronized relabeling assumptions of M5-638, then its positive-thickness material sheath cannot remain bounded without label turnover because

\[
D_B\log(dA_0d_\perp)=\frac32.
\]

Thus the M17 winding branch is now directly connected to the M5 zero-level/sheath-turnover mechanism.

---

## 9. Bridge to M5-685 hysteresis

M5-685 showed that a surviving current-flux conveyor cannot have a net base-label current across `kappa=0`, but must have a strictly negative **flux-weighted** current there:

\[
\overline G_0(0)=0,
\qquad
\overline G_\Phi(0)<0.
\]

Equivalently, downward `kappa` crossings must be systematically more heavily current-flux weighted than upward crossings.

M17-012 supplies a new source of recurrent positive-side charge:

\[
\boxed{
\text{regular winding core}
\Longrightarrow
\text{positive-density finite positive-}kappa\text{ sheath}
\Longrightarrow
\text{finite negative payer}.
}
\]

Therefore any non-axisymmetric recurrent rank-one survivor that repeatedly reuses the same broad material population must realize the M5-685 constitutive hysteresis, or else discharge the burden through one of the already isolated turnover/degeneration exits.

This is a cross-module closure, not yet a contradiction.

---

## 10. DSD analysis

### 10.1 Descriptor transfer
M17-011 changed descriptors from `W` to `G=∇W` at the zero.
M17-012 now transfers the nondegenerate `G` descriptor back to a nonzero-volume `W` sheath using compact derivative bounds.

Thus the chain is

\[
\boxed{
W=0
\to
G\neq0
\to
|W|\gtrsim |z|
\to
\int_{tube}\kappa|W|^2\ge Q_*>0.
}
\]

### 10.2 Measure restoration
The codimension-two skeleton was suppressed by the `|W|^2` measure.
Uniform regularity plus compactness restores a fixed three-dimensional measure contribution on a positive-density set of times.

### 10.3 Remaining structural alternatives
The payer can still be handled by

1. persistent zero-level sheath turnover;
2. finite-jet nodal degeneration/reconnection;
3. axisymmetric/no-swirl regular geometry;
4. a genuinely non-axisymmetric recurrent CE-H hysteresis cycle.

No other measure-zero escape remains on the uniformly regular recurrent-filament subbranch.

---

## 11. DSD audit

### Audit A — time-average spike loophole
Closed under compactness.
The upper bound `K_kappa` converts mean `3/2` into a positive-density threshold set.

### Audit B — shrinking-radius loophole
Closed on the uniformly regular branch.
The Jacobian lower bound, second-derivative upper bound, and `kappa` Lipschitz upper bound produce fixed positive `r_*` and `ell_*`.

### Audit C — zero-dimensional/measure-zero payer
Closed.
The negative payer has weighted mass at least `Q_*>0` on every strongly positive phase.

### Audit D — automatic regular zero sheet
Not claimed.
Continuity only forces a zero crossing in a connected `kappa`-defined component; regular-sheet structure needs the hypotheses of M5-638 or a separate singular-level audit.

### Audit E — axisymmetric firewall
Preserved.
M17-008 remains an exact known-regular model, so finite positive/negative `kappa` separation is not itself contradictory.

### Audit F — global proof status
No contradiction with recurrence has yet been established.
Global regularity remains open.

---

## 12. Updated frontier

The uniformly regular recurrent rank-one winding branch now satisfies

\[
\boxed{
R_{nodal}^{uniform}
\Longrightarrow
P_{tube}^{+}
\Longrightarrow
N_{bulk}^{-}
\Longrightarrow
Z_\kappa
\ \lor\ 
D_\kappa^{sing}
\ \lor\ 
G_{axis/no\text{-}swirl}
\ \lor\ 
H_{CE-H}^{nonaxis}.
}
\]

where

- `P_tube^+` is the positive-density finite-radius positive-`kappa` sheath;
- `N_bulk^-` is the fixed-size negative weighted payer;
- `Z_kappa` is a regular zero-level/sheath-turnover channel;
- `D_kappa^{sing}` is a singular/critical zero-level or degeneration channel;
- `G_axis/no-swirl` is the known regular firewall;
- `H_CE-H^{nonaxis}` is the surviving constitutive hysteresis problem.

---

## 13. Next target

The next highest-value calculation is to test whether the **non-axisymmetric** recurrent branch can sustain the required payer cycle while preserving the great-circle director and the M17-010 nodal multiplier laws.

Concretely, combine

\[
\boxed{
\langle\kappa_0\rangle_{nodal}=\frac32,
\qquad
Q_-\ge Q_*>0
}
\]

with the M5-685 zero-crossing constitutive law

\[
\boxed{
h
=L_\rho\kappa+L_\rho\sigma+\mathcal R_{geom}
\qquad(\kappa=0),
}
\]

and ask whether a recurrent non-axisymmetric great-circle geometry can generate the required negative flux-weighted crossing bias without either

\[
\boxed{
\text{rank loss}
\ \lor\ 
\text{finite-jet turnover}
\ \lor\ 
\text{axisymmetric reduction}.
}
\]

This is now the principal M17/M5 bridge.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
