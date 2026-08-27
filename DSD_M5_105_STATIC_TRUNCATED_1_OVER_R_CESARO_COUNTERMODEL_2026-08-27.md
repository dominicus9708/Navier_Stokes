# DSD M5-105 — Static Truncated 1/r Cesaro Countermodel

Date: 2026-08-27

Status: **STATIC NO-GO AUDIT / A SMOOTH DIVERGENCE-FREE TRUNCATED `1/r` SWIRL FAMILY HAS FINITE ENERGY AT EVERY STAGE, UNIFORM ENSTROPHY, UNIFORM `L^p` FOR EVERY FIXED `p>3`, AND FIXED-CORE SMOOTHNESS, YET FAILS UNIFORM LOG-CESARO CRITICAL TIGHTNESS / THEREFORE THE CURRENT STATIC W1 BOUNDS CANNOT COMMUTE THE CRITICAL MELLIN LIMIT BY THEMSELVES / THIS FAMILY IS NOT A NAVIER--STOKES TRAJECTORY / DYNAMIC PDE GENEALOGY IS REQUIRED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-104 reduced the critical defect to the target

\[
\lim_{L\to\infty}
\sup_j
\frac1L\int_0^LQ_j(x)dx=0,
\]

where

\[
Q_j(x)
=e^{-3x}|\{|U_j|>e^{-x}\}|.
\]

The present audit tests whether this follows merely from the already available **static** controls:

- finite energy for every prelimit state;
- uniform normalized enstrophy;
- uniform `L^p`, `p>3`, control;
- fixed-core smoothness;
- a critical `1/r` envelope.

The answer is no.

---

# 2. Divergence-free truncated swirl

Fix a nonzero constant vector `a` and write

\[
B(x)
:=\frac{a\times x}{|x|^2}.
\]

For `x!=0`,

\[
|B(x)|\sim\frac{\sin\theta}{|x|},
\]

and

\[
\nabla\cdot B=0.
\]

Indeed `B` is tangent to every sphere centered at the origin.

Choose smooth radial cutoffs `chi_in`, `chi_out` satisfying

\[
\chi_{in}(r)=0\quad(r\le1),
\qquad
\chi_{in}(r)=1\quad(r\ge2),
\]

and

\[
\chi_{out}(s)=1\quad(s\le1),
\qquad
\chi_{out}(s)=0\quad(s\ge2).
\]

Let

\[
R_j\to\infty
\]

and define

\[
\boxed{
U_j(x)
:=
\chi_{in}(|x|)
\chi_{out}(|x|/R_j)
\frac{a\times x}{|x|^2}.
}
\]

Because the cutoff gradients are radial while `B` is tangential,

\[
\nabla\chi\cdot B=0.
\]

Hence

\[
\boxed{\nabla\cdot U_j=0.}
\]

The inner cutoff removes the origin singularity, so every `U_j` is smooth and compactly supported.

This is a kinematic divergence-free family, **not** a claimed Navier--Stokes solution family.

---

# 3. Finite energy at every stage

On the annulus

\[
2<r<R_j,
\]

we have `|U_j|~1/r` away from a fixed polar sector.
Therefore

\[
\int |U_j|^2dx
\sim
\int_2^{R_j}r^{-2}r^2dr
\sim R_j.
\]

Thus

\[
\boxed{\|U_j\|_2<\infty\quad\text{for every fixed }j,}
\]

while the normalized energy is allowed to grow with stage depth.

This is exactly the type of growth that physical finite energy permits after blow-up normalization: finite parent energy does not give a uniform normalized `L^2` ceiling as the natural scale shrinks.

---

# 4. Uniform enstrophy

In the critical annulus,

\[
|\nabla U_j|\sim r^{-2}.
\]

Hence

\[
\int_{2<r<R_j}|\nabla U_j|^2dx
\lesssim
\int_2^{R_j}r^{-4}r^2dr
\le C.
\]

The inner cutoff contributes one fixed amount.
The outer cutoff occurs on `r~R_j`; both the derivative of the base field and the cutoff derivative contribute only `O(R_j^{-1})` to the squared-gradient integral.

Therefore

\[
\boxed{
\sup_j\|\nabla U_j\|_2<\infty.
}
\]

Thus the family has a uniform normalized enstrophy-type bound.

---

# 5. Uniform Lp above the critical endpoint

For every fixed `p>3`,

\[
\int_{2<r<R_j}|U_j|^pdx
\lesssim
\int_2^{R_j}r^{2-p}dr
\le C_p.
\]

Hence

\[
\boxed{
\sup_j\|U_j\|_{L^p}<\infty
\qquad\forall p>3.
}
\]

The family therefore reproduces the decisive static feature of W1:

\[
L^p\text{ is uniformly controlled for every }p>3,
\]

while the `p=3` endpoint remains logarithmic.

On every fixed ball, the family is eventually independent of `j`, so it also has trivial fixed-core smooth compactness.

---

# 6. Critical distribution plateau

Choose one angular belt on which

\[
|a\times x|\ge c|a||x|.
\]

For amplitudes in the range

\[
C/R_j\lesssim\lambda\lesssim c_0,
\]

the superlevel set contains a fixed angular fraction of the ball

\[
r\lesssim c/\lambda.
\]

Thus

\[
N_j(\lambda)
\gtrsim c\lambda^{-3}.
\]

The reverse estimate follows from the global `1/r` envelope:

\[
N_j(\lambda)
\lesssim C\lambda^{-3}.
\]

Therefore on a logarithmic amplitude interval of length

\[
\sim\log R_j,
\]

we have

\[
\boxed{
0<c_1
\le
\lambda^3N_j(\lambda)
\le c_2<\infty.
}
\]

Equivalently,

\[
Q_j(x)
\]

has an order-one plateau for

\[
O(1)\lesssim x\lesssim\log R_j-O(1).
\]

---

# 7. Failure of uniform log-Cesaro tightness

Take

\[
L_j\sim\frac12\log R_j.
\]

Then the interval `[0,L_j]` contains an order-one fraction of the plateau for large `j`.
Hence

\[
\boxed{
\frac1{L_j}\int_0^{L_j}Q_j(x)dx
\ge c_*>0.
}
\]

Therefore

\[
\boxed{
\lim_{L\to\infty}
\sup_j
\frac1L\int_0^LQ_j(x)dx
\ne0.
}
\]

The M5-104 critical compactness criterion fails despite all the static bounds listed above.

---

# 8. DSD four-chain audit

## Formation

Each prelimit state is a perfectly formed smooth finite-energy divergence-free object.
The growing normalized `L^2` mass comes from a longer critical annulus, not from an undefined boundary object.

**GREEN.**

## Axis

The log-amplitude coordinate and radial support depth grow together as expected for a `1/r` corridor.
No physical-time interpretation is attached to the radial plateau.

**GREEN.**

## Static aggregation

Uniform `L^p`, `p>3`, and uniform enstrophy do not penalize adding more logarithmic `1/r` shells.
Their shell costs are summable above the endpoint while the critical distribution mean stays order one.

**GREEN no-go.**

## Dynamics

The model contains no Navier--Stokes evolution, pressure Poisson history, or same-trajectory first-hit genealogy.
Therefore it cannot refute a PDE-specific dynamic closure theorem.

**NOT INVOKED / next required input.**

---

# 9. Permanent RED conclusion

The following implication is rejected:

\[
\boxed{
\text{finite energy per stage}
+\text{uniform enstrophy}
+\bigcap_{p>3}\text{uniform }L^p
+\text{fixed-core smoothness}
\Rightarrow
\text{uniform critical log-Cesaro tightness}.
}
\]

It is false at the level of smooth divergence-free static fields.

Thus no future proof may close Issue #2 by recombining only these already-audited static bounds under new notation.

---

# 10. What must enter next

Any successful M5-104 closure must use a genuinely **dynamic Navier--Stokes-specific** property absent from this model, for example:

1. pressure-Poisson coupling across the growing critical corridor;
2. first-hit temporal genealogy linking adjacent log shells;
3. a same-trajectory transport/reformation constraint;
4. a dynamic restriction on how fast the outer truncation radius can migrate in normalized variables;
5. or a defect-aware local-energy theorem that is not implied by the static norms above.

This locates the next computation in the dynamic DSD chain rather than the static chain.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
