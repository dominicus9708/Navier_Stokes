# DSD W1 Scaling-Budget Exponent Taxonomy

Date: 2026-08-26

Status: **GENERAL SCALING AUDIT / EXPLAINS WHY ENERGY-LEVEL FIXED-ACTION EVENTS CAN REPEAT TO A FINITE SINGULAR TIME / RESTRICTS FUTURE CLOSURE ATTEMPTS TO SCALE-CRITICAL OR SCALE-BREAKING INFORMATION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

Many previously derived W1 events have a fixed positive size in normalized Leray variables, yet their physical costs remain summable as `t -> T_*`.

This note isolates the common reason and prevents further false closure attempts of the same type.

---

## 2. Geometric singular scales

Let the physical scale of a recurrent event be

\[
r_j\sim q^{-j/2},
\qquad q>1.
\]

Suppose a positive physical event cost `C_j` scales like

\[
\boxed{
C_j\asymp r_j^{\beta}
}
\]

for a normalized order-one event.

Then

\[
\sum_j C_j
\asymp
\sum_j q^{-j\beta/2}.
\]

Hence:

\[
\boxed{
\beta>0
\Longrightarrow
\sum_j C_j<\infty,
}
\]

whereas

\[
\boxed{
\beta=0
\Longrightarrow
\text{fixed positive event density forces divergence}.
}
\]

For `beta<0`, even a single late fixed normalized event becomes increasingly expensive.

---

## 3. Interpretation

This gives three DSD budget classes.

### Subcritical parent budget

\[
\boxed{\beta>0.}
\]

A geometric sequence of normalized recurrent events can be paid with finite total physical cost.

Such a budget cannot by itself exclude W1 recurrence.

### Critical budget

\[
\boxed{\beta=0.}
\]

A fixed positive event repeated with positive density in Leray time produces a nonsummable physical cost.

This is the correct scale class for a possible final contradiction.

### Supercritical penalty

\[
\boxed{\beta<0.}
\]

Late normalized events become more expensive as the singular scale shrinks.

A finite global parent bound of this type would be even stronger.

---

## 4. Examples already encountered

### Kinetic energy in a shrinking critical shell

For a `1/r` velocity shell of physical radius `r`,

\[
E_{shell}\sim r.
\]

Thus

\[
\beta=1.
\]

This explains why infinitely many critical shells are compatible with finite total kinetic energy.

### Ordinary viscous dissipation over one self-similar stage

A normalized enstrophy of order one corresponds to physical enstrophy of order `r^{-1}`, while a stage lasts order `r^2`.

Hence the stage dissipation is order

\[
r.
\]

Again

\[
\beta=1.
\]

### Lamb `L_t^2 L_x^1` energy-level budget

The spatial `L1` norm of `u x omega` is scale invariant, but physical time contributes `r^2`.

Thus one fixed normalized episode has cost

\[
r^2,
\]

so

\[
\beta=2.
\]

### Critical `D3` spacetime action

\[
D_{3,phys}
=
\int |u||\nabla u|^2dx+
\text{directional term}
\]

scales like `r^{-2}` while a stage lasts `r^2`.

Therefore

\[
\boxed{\beta=0.}
\]

This is why positive recurrent `D3` produces logarithmic divergence.

### Streamline-amplitude critical norm

The quantity

\[
e=u\cdot\nabla|u|
\]

has critical spacetime norm

\[
\|e\|_{L_t^2L_x^{3/2}}.
\]

Its squared stage action is scale invariant, hence again

\[
\boxed{\beta=0.}
\]

and W1 recurrence forces its divergence.

---

## 5. Consequence for proof search

A proposed closure of the form

\[
\text{fixed normalized W1 event}
\Longrightarrow
\text{positive physical cost}
\]

is insufficient unless the cost has `beta <= 0` or unless an additional nonshrinking parent scale changes the scaling.

Therefore future proof search should not spend effort on new additive energy-level costs with `beta>0`.

The viable targets are:

1. a finite **scale-critical** parent budget (`beta=0`);
2. a sign-definite critical monotonicity quantity;
3. a topological/integer obstruction that does not shrink with scale;
4. or a parent--core interface theorem that introduces a fixed physical scale and thereby breaks self-similar homogeneity.

---

## 6. Current critical obstruction

The present W1 survivor already forces several `beta=0` quantities to remain nontrivial:

\[
\boxed{
\int D_{3,phys}dt=\infty,
}
\]

\[
\boxed{
\int
\|u\cdot\nabla|u|\|_{3/2}^2dt
=\infty,
}
\]

and the Bernoulli/vorticity scale currents remain positive in the invariant/log-scale sense.

These facts are necessary certificates of a singular survivor, not contradictions, because no finite unconditional critical parent budget for them is presently available.

---

## 7. DSD conclusion

The repeated failure of energy, turnover-energy, ordinary enstrophy, or raw Lamb budgets is not a collection of unrelated accidents.

They all belong to the same structural class:

\[
\boxed{
\text{subcritical additive budget}
+\text{geometric scale contraction}
\Longrightarrow
\text{summable repeated cost}.
}
\]

The final proof obligation must therefore live at the critical clock

\[
\boxed{
ds=dt/(T_*-t)
}
\]

or must break that scaling by a fixed parent/interface structure.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
