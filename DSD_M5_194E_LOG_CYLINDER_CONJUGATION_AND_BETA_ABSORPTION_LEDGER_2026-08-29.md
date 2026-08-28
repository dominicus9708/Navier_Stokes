# DSD M5-194E — Log-Cylinder Conjugation and Beta-Absorption Ledger

Date: 2026-08-29

Parent: `DSD_M5_194D_BULK_TRANSPORT_STRAIN_POINTWISE_POSITIVITY_NO_GO_AUDIT_2026-08-29.md`

Status: **POSITIVE NORMALIZATION / IN LOG-RADIUS VARIABLES THE CRITICAL FIRST-ORDER COMMON TAIL BECOMES AN ORDER-ONE CYLINDER DRIFT, WHILE THE CRITICAL STRAIN BECOMES AN ORDER-ONE ZEROTH-ORDER MATRIX / IN A LIN--WANG-TYPE CARLEMAN NORM, LARGE `beta` CAN ABSORB BOUNDED CRITICAL STRAIN THROUGH THE `beta^2 |q|^2` CHANNEL, BUT DOES NOT BY ITSELF ABSORB A GENERIC ORDER-ONE CRITICAL DRIFT THROUGH THE GRADIENT CHANNEL / THE DIRECT ABSOLUTE-VALUE DRIFT THRESHOLD IS `beta`-INDEPENDENT / STRUCTURAL SKEWNESS, SMALL DIMENSIONLESS TAIL AMPLITUDE, EXTRA WEIGHT CURVATURE, OR A DIFFERENT ENDPOINT ESTIMATE IS REQUIRED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-194D closed universal pointwise positivity-by-cancellation for the scalar transport--strain block.

The remaining scalar possibility is **coercive domination** by the conjugated heat operator.

To audit that possibility without guessing powers of the Carleman parameter, this note puts the critical operator into logarithmic radial variables and compares each tail channel with the actual homogeneity of a Lin--Wang-type Carleman estimate.

This is a normalization audit, not a completed endpoint Carleman theorem.

---

## 2. Log-cylinder coordinates

Set

\[
y=-\log r,
\qquad r=e^{-y}.
\]

For a scalar or componentwise vector field `f`,

\[
\partial_r f=-\frac1r\partial_y f.
\]

In three dimensions,

\[
\Delta f
=
\partial_{rr}f+\frac2r\partial_r f+rac1{r^2}\Delta_{S^2}f.
\]

A direct calculation gives

\[
\boxed{
r^2\Delta
=
\partial_{yy}-\partial_y+\Delta_{S^2}.
}
\]

Thus the singular Euclidean radial scaling becomes a regular second-order operator on the log-cylinder.

---

## 3. Radial Carleman conjugation

Take a radial logarithmic weight

\[
\varphi=e^{\psi(y)}
\]

and define

\[
W=e^{\psi}q,
\qquad
q=e^{-\psi}W.
\]

Then

\[
\partial_y q
=e^{-\psi}(W_y-\psi'W),
\]

and

\[
\partial_{yy}q
=e^{-\psi}
\left[
W_{yy}-2\psi'W_y+igl((\psi')^2-\psi''\bigr)W
\right].
\]

Therefore

\[
\boxed{
 e^{\psi}r^2\Delta(e^{-\psi}W)
=
W_{yy}
-(2\psi'+1)W_y
+\Delta_{S^2}W
+igl((\psi')^2+\psi'-\psi''\bigr)W.
}
\]

Equivalently, for the heat operator,

\[
\boxed{
 e^{\psi}r^2(\partial_t-\Delta)(e^{-\psi}W)
=
r^2W_t
-W_{yy}
+(2\psi'+1)W_y
-\Delta_{S^2}W
-igl((\psi')^2+\psi'-\psi''\bigr)W.
}
\]

The large formal pieces include

\[
(\psi')^2W\sim\beta^2W,
\qquad
2\psi'W_y\sim\beta W_y,
\]

when `psi' ~ beta`.

However, these pieces do not individually equal a positive coercivity margin; the Carleman estimate is produced after the symmetric/skew interaction is organized. One must therefore compare against the final Carleman norm rather than infer positivity from the `beta^2` potential alone.

---

## 4. Critical common-tail operator on the cylinder

Write the Type-I critical common tail as

\[
B_T(r,y,\theta)
=
\frac1r
\left(
\Phi_r(y,\theta)e_r+\Phi_\tau(y,\theta)
\right).
\]

Since

\[
\nabla
=
\frac1r
\left(-e_r\partial_y+\nabla_{S^2}\right),
\]

we obtain

\[
\boxed{
r^2B_T\cdot\nabla
=
-\Phi_r\partial_y
+
\Phi_\tau\cdot\nabla_{S^2}.
}
\]

Thus the physical `1/r` drift is exactly an **order-one first-order coefficient** on the log-cylinder.

For a radial weight,

\[
\boxed{
 e^{\psi}r^2B_T\cdot\nabla(e^{-\psi}W)
=
-\Phi_r W_y
+\Phi_\tau\cdot\nabla_{S^2}W
+\psi'\Phi_r W.
}
\]

This reproduces the M5-194A bulk radial residual in dimensionless form:

\[
\psi'\Phi_r W\sim\beta\Phi_r W.
\]

The critical strain has the form

\[
S_{B_T}=r^{-2}\Sigma_T(y,\theta),
\]

so

\[
\boxed{
r^2 S_{B_T}W=\Sigma_TW.}
\]

Hence the log-cylinder ledger is

\[
\boxed{
\begin{array}{c|c}
\text{channel}&\text{dimensionless cylinder size}\\
\hline
B_T\cdot\nabla&\Phi\cdot D_{\rm cyl}\\
\text{weighted radial drift potential}&\psi'\Phi_r\sim\beta\Phi_r\\
S_{B_T}&\Sigma_T
\end{array}
}
\]

---

## 5. Carleman normalization from the Lin--Wang estimate

Lin and Wang use a spatial weight

\[
\varphi(r)=e^{\psi(-\log r)}
\]

with

\[
\frac12\beta\le\psi'\le2\beta
\]

and establish a spatial Carleman estimate whose principal left-hand norm contains

\[
\boxed{
\int
\varphi^2(1+\psi'')
\left[
 r^4|\nabla q|^2
+
\beta^2r^2|q|^2
\right].
}
\]

For the present audit, only the homogeneity of these two coercive channels is used.

Since

\[
r^4|\nabla q|^2
=
r^2
\left(
|q_y|^2+|\nabla_{S^2}q|^2
\right),
\]

both sides can be compared after factoring the same physical `r^2` weight.

The vorticity equation has no pressure unknown, so this coefficient ledger is simpler than the generalized Stokes system for which the cited estimate was proved. Nevertheless, importing the full endpoint theorem would require a separate proof and is not assumed here.

---

## 6. Direct absolute-value absorption of the critical drift

Before conjugation, the dimensionless critical drift is

\[
r^2B_T\cdot\nabla q
=
-\Phi_r q_y
+
\Phi_\tau\cdot\nabla_{S^2}q.
\]

Therefore

\[
\left|r^2B_T\cdot\nabla q\right|^2
\le
|\Phi|^2
\left(
|q_y|^2+|\nabla_{S^2}q|^2
\right).
\]

In a Lin--Wang-type right-hand norm this contributes, up to a universal Carleman constant,

\[
\boxed{
\int
\varphi^2 r^2 |\Phi|^2
\left(
|q_y|^2+|\nabla_{S^2}q|^2
\right).
}
\]

The gradient coercivity available on the left is

\[
\boxed{
\int
\varphi^2 r^2(1+\psi'')
\left(
|q_y|^2+|\nabla_{S^2}q|^2
\right).
}
\]

Consequently, the direct perturbative absorption condition has the schematic form

\[
\boxed{
C_{\rm Carl}|\Phi|^2
<
1+\psi''
}
\]

with a strict margin.

Most importantly, **`beta` does not appear as a favorable factor in this comparison.**

Thus

\[
\boxed{
\beta\to\infty
\quad\text{does not by itself absorb a generic order-one critical first-order tail.}
}
\]

This is the precise endpoint manifestation of losing the subcritical spatial factor `r^epsilon`.

---

## 7. Cross-check after conjugation

The same result appears in the weighted variable.

The radial part creates

\[
\psi'\Phi_r W\sim\beta\Phi_r W.
\]

Squaring gives a zeroth-order contribution of size

\[
\beta^2\Phi_r^2|W|^2.
\]

The zeroth-order Carleman norm is itself of size

\[
\beta^2(1+\psi'')|W|^2.
\]

Therefore the `beta^2` factors cancel in the absorption ratio.

Likewise, the derivative part

\[
-\Phi_rW_y+\Phi_\tau\cdot\nabla_{S^2}W
\]

competes directly with the gradient coercivity without a favorable `beta` power.

This confirms the unweighted-variable calculation.

---

## 8. Critical strain is quantitatively less severe in this norm

For the critical zeroth-order strain,

\[
r^2 S_{B_T}q=\Sigma_Tq.
\]

Its squared contribution is

\[
\int
\varphi^2 r^2
|\Sigma_Tq|^2
\le
\|\Sigma_T\|_{\rm op}^2
\int
\varphi^2r^2|q|^2.
\]

The corresponding Carleman coercive term is

\[
\beta^2
\int
\varphi^2r^2(1+\psi'')|q|^2.
\]

Hence the direct absorption condition is only

\[
\boxed{
C_{\rm Carl}\|\Sigma_T\|_{\rm op}^2
<
\beta^2(1+\psi'').
}
\]

For a bounded dimensionless strain matrix, this can be forced by taking `beta` sufficiently large, provided the endpoint Carleman estimate itself is available.

Therefore the quantitative priority changes:

\[
\boxed{
\text{generic critical first-order drift}
\quad>\quad
\text{bounded critical zeroth-order strain}
}
\]

as an **absolute-value absorption** problem.

This does not invalidate M5-194D; that audit concerned positivity-by-structural-cancellation. M5-194E shows that if one abandons cancellation and uses the final Carleman coercive norm, bounded strain is the easier of the two channels.

---

## 9. Radial versus tangential tail after this normalization

The direct absolute-value estimate treats

\[
|\Phi|^2=|\Phi_r|^2+|\Phi_\tau|^2
\]

as the critical coefficient.

Thus M5-194A's radial-component obstruction is not the whole endpoint if one controls drift by squaring its magnitude.

Even when

\[
\Phi_r=0,
\]

the tangential derivative term

\[
\Phi_\tau\cdot\nabla_{S^2}q
\]

remains at the same derivative scale as the Carleman gradient norm.

However, the purely tangential divergence-free branch has additional structure. The full divergence condition is

\[
\boxed{
\Phi_r-\partial_y\Phi_r
+
\operatorname{div}_{S^2}\Phi_\tau=0.
}
\]

If

\[
\Phi_r=0,
\]

then

\[
\operatorname{div}_{S^2}\Phi_\tau=0.
\]

Therefore the tangential transport is skew-adjoint on each sphere with respect to the unweighted spherical measure, and a radial Carleman weight is constant along that angular flow.

This creates a surviving **structural-skewness branch** that may avoid paying the full `|Phi_tau|^2` absolute-value threshold.

It is not proved here that the complete conjugated parabolic estimate preserves enough of that skew structure.

---

## 10. Relation to the subcritical `epsilon` architecture

For a first-order coefficient satisfying

\[
|A(x,t)|\lesssim r^{-1+\epsilon},
\]

the dimensionless cylinder coefficient is

\[
|rA|\lesssim r^\epsilon.
\]

As `r -> 0`, this produces a genuine small factor.

At the Type-I endpoint,

\[
|A|\sim r^{-1},
\]

so

\[
|rA|\sim O(1).
\]

The direct absorption condition therefore loses its spatial small parameter exactly at `epsilon=0`.

This gives a sharper formulation of the M5-194 epsilon-loss firewall:

\[
\boxed{
\text{subcritical: }rA\to0,
\qquad
\text{critical: }rA=\Phi=O(1).
}
\]

---

## 11. DSD verdict

### ESTABLISHED AT THE COEFFICIENT-LEDGER LEVEL

1. The critical `1/r` drift is an order-one first-order coefficient on the log-cylinder.
2. A radial Carleman conjugation creates the expected `beta Phi_r` zeroth-order term, but this does not yield a favorable `beta` ratio after squaring against the final Carleman norm.
3. Generic direct absorption of the critical drift needs a strict coefficient margin of the form
   \[
   C|\Phi|^2<1+\psi''.
   \]
4. Bounded critical strain is a zeroth-order channel and can, at this homogeneity level, be absorbed for sufficiently large `beta`.
5. Therefore the first-order common tail, not bounded strain, is the principal generic scalar endpoint.

### NOT YET ESTABLISHED

- an actual endpoint vorticity Carleman estimate with all required temporal and spatial boundary terms;
- a theorem-level value of the absorption constant;
- uniform smallness of `Phi` for the canonical Type-I common tail;
- sufficient skew cancellation for a purely tangential tail;
- a weight-curvature design that gives a globally adequate margin without violating the slope/geometry requirements;
- a matrix/symmetrizer estimate for non-small generic tails.

---

## 12. Next audit target

The next scalar question is now sharply defined:

\[
\boxed{
\text{Can }1+\psi''
\text{ be made uniformly large enough to dominate }C|\Phi|^2
\text{ on the entire endpoint cylinder while keeping }
\psi'\asymp\beta?
}
\]

Because `psi''` is the derivative of `psi'`, any attempt to maintain a large positive curvature over a long log-radius interval spends a finite slope budget.

The next audit should therefore derive the **Carleman curvature-budget inequality** and determine whether curvature alone can handle an arbitrary bounded critical tail on an unbounded log-cylinder.
