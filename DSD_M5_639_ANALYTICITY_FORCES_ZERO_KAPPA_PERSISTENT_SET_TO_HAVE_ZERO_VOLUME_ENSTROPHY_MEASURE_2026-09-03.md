# DSD M5-639 — Spatial analyticity forces the persistent zero-kappa set to have zero volume/enstrophy measure

Date: 2026-09-03

Status: **EXTERNAL-ANALYTICITY-DEPENDENT ZERO-SET RIGIDITY / ON CE-H, `kappa=0` WITH `W!=0` IMPLIES `Delta W=0`. AT EVERY FIXED ANCIENT TIME THE VORTICITY FIELD IS REAL ANALYTIC UNDER THE M5-599 ANALYTICITY CORRIDOR, SO `Delta W` IS REAL ANALYTIC. IF ITS ZERO SET HAD NONEMPTY OPEN INTERIOR, ANALYTIC CONTINUATION WOULD GIVE `Delta W identically 0`, AND THE WHOLE-SPACE L2 HARMONIC FIELD WOULD BE `W=0`, CONTRADICTING THE MARKED HARD COMPONENT. MOREOVER THE ZERO SET OF A NONTRIVIAL REAL-ANALYTIC COMPONENT HAS LEBESGUE MEASURE ZERO, SO `{W!=0,kappa=0}` HAS ZERO 3D VOLUME. CONSEQUENTLY THE PERSISTENT ZERO-KAPPA NETWORK IS NECESSARILY A LOWER-DIMENSIONAL FLUX SKELETON AND CARRIES ZERO ENSTROPHY MEASURE; ALL VOLUMETRIC ENSTROPHY/RAYLEIGH BUDGET LIVES IN THE NONZERO-KAPPA SHEATH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Zero kappa means zero Laplacian on the active set

The CE-H eigenvalue equation is

\[
\Delta W=\kappa W.
\]

Hence on

\[
Z_0:=\{y:W(y)\ne0,\ \kappa(y)=0\},
\]

we have

\[
\boxed{\Delta W=0.}
\]

No division by `W` is needed for this implication.

---

## 2. Spatial analyticity input

M5-599 explicitly imports the spatial analyticity of the smooth ancient Navier--Stokes state on every fixed time slice.

Therefore

\[
W(\cdot,\theta)
\]

and

\[
\Delta W(\cdot,\theta)
\]

are real analytic in `y`.

This note inherits that external-theorem dependency.

---

## 3. No open zero-kappa plateau

Suppose `Z_0` contained a nonempty open three-dimensional ball.

Then

\[
\Delta W=0
\]

on that ball.

Each component of `Delta W` is real analytic, so the real-analytic identity theorem gives

\[
\boxed{\Delta W\equiv0\quad\text{on }\mathbb R^3.}
\]

Since the state is in `L2`, a whole-space harmonic component is zero.

Therefore

\[
W\equiv0.
\]

This contradicts the persistent marked hard component.

Hence

\[
\boxed{Z_0\text{ has empty interior.}}
\]

---

## 4. Zero volume of the zero-kappa active set

Because `W` is nonzero, `Delta W` cannot vanish identically by the previous argument.

Therefore at least one scalar component

\[
(\Delta W)_j
\]

is a nontrivial real-analytic function.

The zero set of a nontrivial real-analytic scalar function in `R3` has three-dimensional Lebesgue measure zero.

Since

\[
Z_0\subset\{(\Delta W)_j=0\},
\]

we obtain

\[
\boxed{|Z_0|=0.}
\]

Thus

\[
\boxed{
\int_{Z_0}|W|^2dy=0.
}
\]

The zero-kappa set carries no volumetric enstrophy measure.

---

## 5. Consequence for the persistent c*=0 network

M5-636--638 retain a possible persistent synchronized flux skeleton with

\[
c_*\equiv0.
\]

M5-639 now shows that this skeleton cannot be a three-dimensional enstrophy-bearing population.

It is necessarily lower-dimensional from the viewpoint of Lebesgue/enstrophy measure.

Therefore

\[
\boxed{
\text{persistent zero-kappa flux skeleton}
\text{ carries zero direct }|W|^2dy\text{ budget}.
}
\]

---

## 6. Rayleigh budget must live off the skeleton

The global CE-H identity is

\[
\int\kappa|W|^2dy=-P<0.
\]

The zero-kappa set contributes exactly zero.

Hence

\[
\boxed{
\int_{\{\kappa\ne0\}}\kappa|W|^2dy=-P<0.
}
\]

Similarly all positive-volume enstrophy production/dissipation is carried by the nonzero-kappa surrounding population.

Thus the `c_*=0` persistent network cannot itself pay the volumetric Rayleigh budget through same-level covariance; there is no same-level volume measure to correlate.

---

## 7. Combine with M5-629 and M5-638

Under the relabeling ODE, distinct nonzero kappa levels ordered away from the persistent zero level cannot themselves become additional bounded nondegenerate persistent fixed-flux lineages without synchronizing to zero.

M5-638 also shows that a positive-thickness material band around the zero-level surface expands at rate `3/2` and therefore requires material turnover to remain a bounded Eulerian sheath.

Consequently the zero-level no-turnover skeleton is surrounded by

\[
\boxed{
\text{nonzero-kappa, positive-volume, materially renewing sheath}.
}
\]

All enstrophy-weighted negative kappa budget is in that sheath.

---

## 8. Updated relabeling conclusion

Combining M5-636 and M5-639,

\[
\boxed{
R_{relabel}
\Longrightarrow
\text{positive-density/high-amplitude turnover}
\quad\text{or}\quad
\text{measure-zero zero-kappa skeleton + volumetric sheath turnover}.
}
\]

Thus **every three-dimensional enstrophy-bearing relabeling survivor requires turnover**.

What remains persistent without turnover is at most a lower-dimensional material flux skeleton.

This is a substantial branch reduction but is not itself a contradiction.

---

## 9. Firewall

The measure-zero conclusion uses real analyticity and therefore inherits the external analyticity dependency already isolated in M5-599.

The geometry/topology of the zero set is not classified here; it may contain surfaces, curves, singular strata, or their analytic combinations.

Only its zero three-dimensional volume/enstrophy measure is used.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]