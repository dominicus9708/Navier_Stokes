# DSD M5-307 — General Growth Visibility Ratio and Energy-Shield Law

Date: 2026-08-30

Parent: `DSD_M5_306_DETACHED_ANCIENT_POLYNOMIAL_GROWTH_DESCRIPTOR_AND_GENERAL_ENERGY_VISIBILITY_SHIELD_2026-08-30.md`

Status: **ANCESTRY GEOMETRY GENERALIZATION / THE POINT-PICKING WINDOW CAN EXCLUDE AN `R^alpha` DETACHED GROWTH MODE EXACTLY WHEN `Xi_alpha := qd/(qE0)^{1/(2alpha+3)} -> infinity`; IF THIS FAILS, THE SURVIVOR MUST OBEY THE GENERAL ENERGY-SHIELD LAW `q^{2alpha+2} d^{2alpha+3} <= C E0`, EQUIVALENT FOR `alpha>-1` TO `ell >= c E0^{-1/(2alpha+2)} d^{(2alpha+3)/(2alpha+2)}` / THE AFFINE `5/4` LAW IS THE CASE `alpha=1` / GLOBAL REGULARITY UNPROVED.**

---

## 1. Available point-picking radius

For a remote satellite with vorticity frequency

\[
q=|\omega|^{1/2},
\]

natural length

\[
\ell=q^{-1},
\]

and physical distance `d` from the tracked main core, M5-281 gives a point-picking window parameter `A` satisfying

\[
1\ll A\ll qd
\]

whenever `qd->infinity`.

Thus the largest available normalized spatial radius before the main core enters the satellite frame is of order

\[
\boxed{L_{sep}=qd=d/\ell.}
\]

---

## 2. Growth visibility radius

M5-306 shows that an order-one detached growth mode

\[
|U-c|\sim R^\alpha
\]

through radius `R` consumes scaled kinetic energy

\[
\sim R^{2\alpha+3}.
\]

The prelimit scaled energy budget is `qE0`, hence the visibility radius is

\[
\boxed{
R_\alpha=(qE_0)^{1/(2\alpha+3)}.
}
\]

---

## 3. General visibility ratio

Define

\[
\boxed{
\Xi_\alpha
:=
\frac{qd}{(qE_0)^{1/(2\alpha+3)}}.
}
\]

If

\[
\boxed{\Xi_\alpha\to\infty,}
\]

one may choose the point-picking radius `A_n` so that

\[
R_\alpha\ll A_n\ll q_nd_n.
\]

Then the prelimit finite-energy field cannot approximate a nonzero order-one `R^alpha` detached profile throughout `B_{A_n}`.

Therefore

\[
\boxed{
\Xi_\alpha\to\infty
\Longrightarrow
\text{exclusion of persistent visible }\alpha\text{-growth}.
}
\]

This is a direct scale comparison.

---

## 4. Energy-shield inequality

If an `alpha`-growth detached profile survives without becoming visible to finite energy, then `Xi_alpha` must remain bounded along the relevant subsequence:

\[
qd
\lesssim
(qE_0)^{1/(2\alpha+3)}.
\]

Raise to the power `2alpha+3`:

\[
q^{2\alpha+3}d^{2\alpha+3}
\lesssim
qE_0.
\]

Thus

\[
\boxed{
q^{2\alpha+2}d^{2\alpha+3}
\lesssim
E_0.
}
\]

This is the general energy-shield law.

---

## 5. Natural-length form

With

\[
q=\ell^{-1},
\]

the shield is

\[
\boxed{
\frac{d^{2\alpha+3}}{\ell^{2\alpha+2}}
\lesssim E_0.
}
\]

For

\[
\alpha>-1
\]

this gives

\[
\boxed{
\ell
\gtrsim
E_0^{-1/(2\alpha+2)}
\,d^{\frac{2\alpha+3}{2\alpha+2}}.
}
\]

Define

\[
\boxed{
\beta(\alpha)
:=
\frac{2\alpha+3}{2\alpha+2}
=1+\frac1{2\alpha+2}.
}
\]

Then the shield is

\[
\ell\gtrsim d^{\beta(\alpha)}
\]

up to the energy constant.

---

## 6. Examples

### Affine growth `alpha=1`

\[
\beta(1)=\frac54,
\]

so

\[
\boxed{
ell\gtrsim E_0^{-1/4}d^{5/4}.}
\]

This is exactly M5-282.

### Bounded mean-free growth `alpha=0`

\[
\beta(0)=\frac32,
\]

so a bounded-order detached component that remains energy-shielded must satisfy

\[
\boxed{
ell\gtrsim E_0^{-1/2}d^{3/2}.}
\]

### As `alpha -> infinity`

\[
\beta(\alpha)\downarrow1.
\]

Faster polynomial growth becomes visible on a comparatively smaller fraction of the separation scale.

### As `alpha -> -1^+`

\[
\beta(\alpha)\to\infty.
\]

The critical decaying `1/R` class is not efficiently constrained by this polynomial-energy visibility mechanism, consistent with the need for weak-`L3`/Besov information instead.

---

## 7. Formation meaning

The detached ancestry problem is now a two-coordinate comparison:

\[
\boxed{
\text{available separation window }qd
\quad\text{vs}\quad
\text{growth visibility radius }R_\alpha.
}
\]

A growth class is either:

1. **visible** — finite energy excludes it;
2. **shielded** — geometry/compactness prevents observation before the main core enters the window.

Thus

\[
\boxed{
A_\alpha
\Longrightarrow
A_{\alpha,visible}^{\emptyset}
\lor A_{\alpha,shielded}.
}
\]

---

## 8. Connection with Type-II satellite variables

Recall

\[
L=qd=d/\ell,
\qquad
\Theta=(T^*-t)|\omega|.
\]

The visibility ratio is

\[
\Xi_\alpha
=
\frac{L}{(qE_0)^{1/(2\alpha+3)}}.
\]

Thus shielded polynomial growth requires a specific coupling between:

- scale separation `L`;
- vorticity amplitude `q^2`;
- physical finite-energy budget.

This can be compared independently with the Type-II clock `Theta` and Seregin amplification constraints.

No such comparison is asserted automatically here.

---

## 9. Scope firewall

The visibility argument requires the detached profile to exhibit its `R^alpha` growth coherently throughout radii comparable to the chosen expanding window.

A highly intermittent growth profile can evade a simple ball-energy lower bound even if its pointwise limsup is large.

Therefore the appropriate rigorous growth descriptor is the mean-free ball energy `E(R)` from M5-306, not a pointwise supremum alone.

---

## 10. Updated ancestry target

The first practical target remains `alpha=1` because it removes the exact affine/solid-rotation/affine-strain countermodels responsible for the main local Liouville firewall.

The required quantitative bridge is precisely

\[
\boxed{
\Xi_1
=
\frac{qd}{(qE_0)^{1/5}}
\to\infty.
}
\]

If this can be forced on every detached satellite subsequence, the entire nonzero affine blow-down class disappears.

If not, the branch is restricted by the explicit fifth-root shield geometry.

---

## 11. Audit verdict

### PROVED

General visibility ratio

\[
\boxed{
\Xi_\alpha
=qd/(qE_0)^{1/(2\alpha+3)}.
}
\]

### DERIVED

General shield law

\[
\boxed{
q^{2\alpha+2}d^{2\alpha+3}\lesssim E_0.
}
\]

For `alpha>-1`,

\[
\boxed{
ell\gtrsim E_0^{-1/(2\alpha+2)}d^{(2\alpha+3)/(2\alpha+2)}.}
\]

### OPEN

- forcing `Xi_1 -> infinity`;
- shielded affine branch;
- sublinear general-3D rigidity;
- dynamic turnover;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]