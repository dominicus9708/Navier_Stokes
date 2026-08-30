# DSD M5-309 — Affine-Campanato Excess, First-Break Radius, and the `L^{1/5}` Transition Gate

Date: 2026-08-30

Parent: `DSD_M5_308_PARENT_MORREY_LOCAL_ENERGY_VISIBILITY_RADIUS_AND_REDUCED_EXPANDING_WINDOW_TARGET_2026-08-30.md`

Status: **FORMATION STOPPING-RADIUS REFORMULATION / A NONZERO AFFINE DETACHED MODE CANNOT REMAIN BOTH AMPLITUDE-COHERENT AND AFFINE-CAMPANATO-COHERENT THROUGH RADII BEYOND THE PARENT-MORREY VISIBILITY SCALE `~L^{1/5}` / THEREFORE EVERY SHIELDED AFFINE SEQUENCE HAS A FIRST TRANSITION RADIUS `R_br <= C L^{1/5}` WHERE EITHER THE BEST AFFINE GRADIENT CHANGES BY ORDER ONE OR THE NORMALIZED NONAFFINE EXCESS BECOMES ORDER ONE / THE EXCESS BRANCH FORCES A SCALE-INVARIANT GRADIENT-VARIANCE WITNESS ON THAT INTERMEDIATE SHELL / THIS REPLACES AN UNSPECIFIED EXPANDING-WINDOW FAILURE BY A CONCRETE MOVING TRANSITION SHELL, BUT DOES NOT YET CONTRADICT NAVIER–STOKES / GLOBAL REGULARITY UNPROVED.**

---

## 1. Motivation

M5-308 identified the affine energy visibility scale

\[
R\sim L^{1/5}
\]

under parent Morrey control, but fixed-radius compactness does not imply convergence on this growing window.

Instead of asking for full convergence, this note measures directly whether the prelimit field remains affine-like as the radius grows.

This is a Formation-style change of descriptor, not a new proof rule.

---

## 2. Best divergence-free affine fit

In the satellite-normalized variables, fix a time slice and center the selected satellite at the origin.

For `R>=1`, define

\[
\boxed{
\mathcal Q_R(c,M)
:=
\int_{B_R}|U(y)-c-My|^2dy,
\qquad \operatorname{tr}M=0.
}
\]

Let `(c_R,M_R)` be a minimizer.

The trace-free condition matches incompressible affine fields.

Define the normalized affine excess

\[
\boxed{
\mathfrak E_{aff}(R)
:=
R^{-5}\mathcal Q_R(c_R,M_R).
}
\]

The `R^{-5}` normalization is natural because a linear field of order-one gradient has kinetic energy `~R^5`.

---

## 3. Affine amplitude and direction descriptors

Define

\[
\boxed{a_R:=|M_R|_F.}
\]

When `a_R>0`, define its normalized matrix direction

\[
\boxed{\widehat M_R:=M_R/a_R.}
\]

A nonzero affine detached limit `U=M_*y+c_*` has

\[
\mathfrak E_{aff}(R)=0,
\qquad
M_R=M_*
\]

for every `R` in the exact model.

For a convergent prelimit sequence, these properties hold on every fixed `R`, but not necessarily on a growing window.

---

## 4. Orthogonality of the best affine fit

The minimizer satisfies the normal equations

\[
\int_{B_R}(U-c_R-M_Ry)dy=0
\]

and orthogonality to trace-free linear fields.

Because the ball is centered,

\[
\int_{B_R}y\,dy=0,
\]

and

\[
\int_{B_R} y\otimes y\,dy
=c_2R^5I
\]

for a universal `c_2>0`.

Thus the linear affine component has energy

\[
\boxed{
\int_{B_R}|M_Ry|^2dy
=c_A R^5|M_R|_F^2
}
\]

with universal `c_A>0`, and the best-fit residual is `L2`-orthogonal to the fitted linear subspace.

Consequently

\[
\boxed{
\inf_c\int_{B_R}|U-c|^2dy
\ge
c_AR^5a_R^2.
}
\]

In fact the full orthogonal decomposition gives the affine energy plus the residual excess.

---

## 5. Parent Morrey energy ceiling

M5-308 gives, for every

\[
R\le cL,
\]

a satellite-frame local energy ceiling of the form

\[
\boxed{
\inf_c\int_{B_R}|U-c|^2dy
\le
C_MM_*L
}
\]

on the no-Campanato-turnover corridor, after choosing the compatible parent relative-velocity gauge.

Combining with the affine lower bound,

\[
\boxed{
a_R^2R^5\lesssim M_*L.}
\]

Therefore

\[
\boxed{
a_R\lesssim M_*^{1/2}L^{1/2}R^{-5/2}.}
\]

---

## 6. Affine amplitude cannot survive beyond `L^{1/5}`

Fix a nonzero target affine amplitude `a_*>0` inherited from the detached fixed-radius limit.

If

\[
a_R\ge a_*/2,
\]

then the preceding inequality forces

\[
\boxed{
R\le
C(a_*,M_*)L^{1/5}.
}
\]

Hence a nonzero affine gradient cannot remain the best-fit gradient with order-one amplitude through radii much larger than `L^{1/5}`.

This conclusion does **not** require convergence on the whole growing ball.

---

## 7. First-break radius

Choose small fixed tolerances

\[
0<\delta_a,\delta_E,\delta_\theta\ll1.
\]

Take a reference radius `R_0=O(1)` on which fixed-radius convergence to the nonzero affine limit gives

\[
a_{R_0}\ge a_*,
\qquad
\mathfrak E_{aff}(R_0)\le\delta_E,
\]

and a reference direction `\widehat M_*`.

Define the first affine-coherence break radius

\[
\boxed{
R_{br}
:=
\inf\Big\{R\ge R_0:
\begin{array}{l}
a_R<(1-\delta_a)a_*\\
\text{or }|\widehat M_R-\widehat M_*|>\delta_\theta\\
\text{or }\mathfrak E_{aff}(R)>\delta_E
\end{array}
\Big\}.
}
\]

By the amplitude visibility estimate,

\[
\boxed{
R_{br}\le C(a_*,M_*,\delta_a)L^{1/5}.
}
\]

Thus every shielded affine sequence produces a concrete moving transition radius no later than the fifth-root scale.

---

## 8. Three transition mechanisms

At `R_br`, at least one of the following occurs.

### A. Affine amplitude drop

\[
\boxed{a_R<(1-\delta_a)a_*.}
\]

The order-one affine gradient visible near the satellite core has been lost by the time radius `R_br` is reached.

### B. Affine axis/matrix rotation

\[
\boxed{|\widehat M_R-\widehat M_*|>\delta_\theta.}
\]

The large-scale affine strain/rotation direction has reorganized by an order-one projective amount.

### C. Nonaffine excess creation

\[
\boxed{\mathfrak E_{aff}(R)>\delta_E.}
\]

The field is no longer well represented by one affine incompressible map on that scale.

These are Formation-distinct transition modes.

---

## 9. Excess implies a gradient-variance witness

Let

\[
w=U-c_R-M_Ry.
\]

The mean and first affine moments of `w` vanish by optimality.

A scale-`R` Poincare/Korn estimate gives

\[
\boxed{
\int_{B_R}|w|^2
\le
CR^2
\int_{B_R}|\nabla U-M_R|^2
}
\]

(up to the standard use of a slightly enlarged ball/cutoff if needed).

Therefore

\[
\mathfrak E_{aff}(R)>\delta_E
\]

forces

\[
\boxed{
R^{-3}
\int_{B_R}|\nabla U-M_R|^2dy
\ge c\delta_E.
}
\]

This is a scale-invariant gradient-variance witness on the transition scale.

It is not yet an unbounded `H` event; it is a fixed positive nonaffinity certificate.

---

## 10. Shell localization of the transition

Compare two nested radii, for example `R` and `2R`.

If the best affine matrices differ by a fixed amount,

\[
|M_{2R}-M_R|\ge\delta,
\]

or the affine excess rises by a fixed amount, then at least one annular block between the two scales carries a corresponding fixed normalized gradient-variance/relative-energy contribution.

Thus the first break can be localized to a dyadic transition shell

\[
\boxed{
A_{R\sim R_{br}}.
}
\]

This is the appropriate object for subsequent H/T or satellite reselection analysis.

---

## 11. Relation to the affine fixed-point firewall

The exact affine anti-model `U=M_*y` has no first-break radius: `R_br=infinity`.

The parent-Morrey energy ceiling forbids this behavior in the prelimit beyond `O(L^{1/5})`.

Therefore the finite-energy/Morrey ancestry does not immediately kill the local affine limit, but it **forces a transition shell separating the affine-looking core from the finite-energy exterior**.

This is the precise structure hidden by the abstract expanding-window failure.

---

## 12. What remains to close the affine branch

The next question is now concrete:

> what can an exact Navier–Stokes solution do on the transition shell where an order-one affine core loses amplitude/direction or develops order-one nonaffine gradient variance?

Possible routings are:

\[
\boxed{
H_{derivative/strain}
\lor T_{projective}
\lor T_{material/pressure}
\lor S_{secondary-satellite}.
}
\]

A purely static Campanato argument does not yet decide among them.

The key gain is that the shell radius satisfies

\[
\boxed{R_{br}=O(L^{1/5}),}
\]

far inside the separation scale `L`.

---

## 13. DSD audit firewall

One must not relabel the fixed positive gradient-variance witness from Section 9 as an immediate contradiction.

The cutoff affine countermodel shows that a field may transition from affine behavior to finite-energy decay through such a shell without any static impossibility.

The Navier–Stokes **time evolution** of that shell is still required for closure.

---

## 14. Audit verdict

### PROVED / VARIATIONAL

- best affine-fit energy lower bound `~a_R^2R^5`;
- parent Morrey forces order-one affine amplitude to break by `O(L^{1/5})`;
- affine excess gives a scale-invariant gradient-variance witness.

### STRUCTURAL REDUCTION

The vague expanding-window ancestry failure becomes a concrete first transition shell before the fifth-root scale.

### OPEN

- dynamic classification/closure of the transition shell;
- whether it necessarily produces H/T or a secondary satellite;
- critical `1/R` detached endpoint;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]