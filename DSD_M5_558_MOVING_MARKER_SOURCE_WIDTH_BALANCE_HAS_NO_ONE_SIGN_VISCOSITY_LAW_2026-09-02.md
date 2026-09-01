# DSD M5-558 — Moving-marker source-width balance: viscosity does not give a one-sign recurrence obstruction for the separated satellite geometry

Date: 2026-09-02

Status: **SOURCE-WIDTH LYAPUNOV AUDIT / M5-557 REDUCES THE TWO-LINEAGE COMPRESSION EXCEPTION TO A RECURRENT MULTI-CENTER SOURCE ARCHITECTURE, SUGGESTING THAT VISCOSITY MIGHT FORCE MONOTONE SPREAD OF A LINEAGE SOURCE AROUND ITS MATERIAL MARKER / THE EXACT LOCAL SIMILARITY ENSTROPHY EQUATION SHOWS THIS SHORTCUT IS FALSE FOR THE NATURAL L2 VORTICITY-WIDTH OBSERVABLE / FOR ANY SMOOTH BOUNDED MARKER-CENTERED WEIGHT `psi(y-Y(theta))`, ITS WEIGHTED ENSTROPHY SATISFIES AN EXACT BALANCE WITH MATERIAL-RELATIVE TRANSPORT, WEIGHT LAPLACIAN, STRETCHING PRODUCTION, AND WEIGHTED PALINSTROPHY / EVEN FOR A QUADRATIC WIDTH INSIDE A FIXED CORE, THE DIFFUSIVE TERMS `+6 E` AND `-2 int |z|^2 |grad W|^2` HAVE COMPETING SIGNS, WHILE STRAIN/TRANSPORT CAN RECYCLE THE WIDTH / NORMALIZING BY LOCAL ENSTROPHY DOES NOT REMOVE THESE COVARIANCE TERMS / THEREFORE THE SEPARATED SATELLITE DOES NOT YET CREATE A STRICT SOURCE-WIDTH LYAPUNOV FUNCTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Local similarity enstrophy equation

Write

\[
h:=|W|^2,
\qquad
p:=|\nabla W|^2,
\qquad
q:=W\cdot\Sigma W,
\]

and

\[
B:=U+\frac12y.
\]

The exact local similarity enstrophy equation used in M5-529 is

\[
\boxed{
\partial_\theta h
+\frac12h
+\nabla\cdot(Bh-\nabla h)
=2q-2p.
}
\]

Integrating with weight one recovers

\[
\frac12E'+\frac14E+P=Q.
\]

---

## 2. Marker-centered moving weight

Let `Y(theta)` be a retained material marker, so

\[
\boxed{Y'=B(Y,\theta).}
\]

Set

\[
z:=y-Y(\theta).
\]

Take a smooth bounded weight

\[
\psi(z)
\]

with bounded first and second derivatives; compact support is sufficient for every integration by parts below.

Define

\[
\boxed{
M_\psi(\theta)
:=
\int_{\mathbb R^3}
\psi(y-Y(\theta))
|W(y,\theta)|^2dy.
}
\]

This is a local source-width/shape observable around the material marker.

---

## 3. Exact time derivative of the moving weight

Because

\[
\partial_\theta\psi(y-Y)
=-Y'\cdot\nabla\psi
=-B(Y)\cdot\nabla\psi,
\]

we have

\[
\begin{aligned}
M_\psi'
={}&
\int
[-B(Y)\cdot\nabla\psi]h\,dy
+\int\psi\,\partial_\theta h\,dy.
\end{aligned}
\]

Insert the local enstrophy equation.

Integration by parts gives

\[
-\int\psi\,\nabla\cdot(Bh)\,dy
=
\int B\cdot\nabla\psi\,h\,dy,
\]

and

\[
\int\psi\,\Delta h\,dy
=
\int\Delta\psi\,h\,dy.
\]

Therefore

\[
\boxed{
\begin{aligned}
M_\psi'
={}&
\int
\left[
(B(y)-B(Y))\cdot\nabla\psi
+\Delta\psi
-\frac12\psi
\right]|W|^2dy\\
&+2\int\psi\,W\cdot\Sigma W\,dy
-2\int\psi|\nabla W|^2dy.
\end{aligned}
}
\]

This identity is exact for every admissible marker-centered weight.

---

## 4. Separate explicit similarity dilation from physical velocity difference

Since

\[
B(y)-B(Y)
=U(y)-U(Y)+\frac12z,
\]

we may rewrite the transport coefficient as

\[
(U(y)-U(Y))\cdot\nabla\psi
+\frac12z\cdot\nabla\psi
-\frac12\psi.
\]

Thus

\[
\boxed{
\begin{aligned}
M_\psi'
={}&
\int
\left[
(U(y)-U(Y))\cdot\nabla\psi
+\frac12(z\cdot\nabla\psi-\psi)
+\Delta\psi
\right]h\,dy\\
&+2Q_\psi-2P_\psi,
\end{aligned}
}
\]

where

\[
Q_\psi:=\int\psi q,
\qquad
P_\psi:=\int\psi p.
\]

The source-shape balance is therefore another exact similarity ledger.

---

## 5. Quadratic width in the region where the cutoff is one

Take a smooth cutoff `chi` and let

\[
\psi_R(z)
=|z|^2\chi(|z|/R),
\]

with `chi=1` on a fixed inner source region containing the marker and its recurrent satellite.

Inside the region where `chi=1`,

\[
\nabla\psi_R=2z,
\qquad
\Delta\psi_R=6,
\]

and

\[
\frac12(z\cdot\nabla\psi_R-\psi_R)
=\frac12|z|^2.
\]

Ignoring only the explicitly recorded cutoff-annulus terms, the interior quadratic-width contribution is

\[
\boxed{
\begin{aligned}
M_{2}'
={}&
\frac12M_2
+6E_{loc}
+2\int z\cdot(U(y)-U(Y))|W|^2dy\\
&+2Q_2
-2P_2
+\mathcal B_R,
\end{aligned}
}
\]

where

\[
Q_2=\int |z|^2W\cdot\Sigma W,
\]

\[
P_2=\int |z|^2|\nabla W|^2,
\]

and `B_R` contains the bounded cutoff-annulus commutators.

---

## 6. Diffusion alone is not one-sign for L2 source width

The two diffusion-generated terms in the quadratic identity are

\[
\boxed{
6E_{loc}-2P_2.
}
\]

They have opposite signs.

A broad slowly varying source can have the positive `6E` term dominate, while a sharply varying source can have the negative weighted-palinstrophy term dominate.

Thus the L2 vorticity second moment is not a monotone diffusion-spreading quantity even before stretching and nonlinear transport are included.

This differs from the second moment of a positive conserved heat density; enstrophy is itself dissipated and is not a conserved positive mass.

---

## 7. Physical relative transport is also sign-indefinite

The marker-relative transport term is

\[
\boxed{
T_2
:=
2\int
z\cdot(U(y)-U(Y))|W|^2dy.
}
\]

By the fundamental theorem of calculus,

\[
U(y)-U(Y)
=\int_0^1\nabla U(Y+s z)z\,ds.
\]

Hence

\[
T_2
=2\int
\left[
\int_0^1z^T\Sigma(Y+s z)z\,ds
\right]|W|^2dy.
\]

The antisymmetric velocity-gradient part cancels.

This term can be positive or negative depending on the local strain geometry.

Therefore material centering removes translation but does not remove deformation of source width.

---

## 8. Stretching production can recycle source width

The weighted production term is

\[
\boxed{
2Q_2
=2\int |z|^2W\cdot\Sigma W\,dy.
}
\]

It is sign-indefinite and is generated by the same finite-core strain field that already pays the ordinary enstrophy/palinstrophy ledgers.

There is no inequality from the current hard-core hypotheses forcing

\[
Q_2\le0
\]

or making it smaller than the favorable weighted-palinstrophy term.

Thus recurrent vortex stretching can regenerate off-center enstrophy while viscosity removes gradients.

---

## 9. Similarity scaling itself expands the quadratic width

The explicit linear contribution is

\[
\boxed{+\frac12M_2.}
\]

This is expected: a fixed physical length expands like `e^(theta/2)` in backward-similarity coordinates.

A recurrent similarity source shape must therefore continuously counter this explicit expansion using negative relative strain and/or diffusion.

M5-554's connector compression `-1/2` is the two-marker analogue of exactly this requirement.

Again this is a balance condition, not an inconsistency.

---

## 10. Cutoff terms are not automatically negligible in a weighted width audit

One might try to move `R` to the remote spectator tail and discard `B_R` by unweighted `L2` tightness.

That shortcut is unsafe because derivatives of a quadratic cutoff can carry factors of order `R` or `R^2`, while M5-531 proves that the critical first radial moment is infinite on the hard component.

Unweighted tail smallness does not automatically imply weighted cutoff-error smallness.

Therefore M5-558 uses a fixed active-core width observable and keeps `B_R` explicit rather than silently sending `R to infinity`.

---

## 11. Normalizing by local enstrophy does not restore monotonicity

Suppose one defines a local normalized width

\[
\mathcal V
:=
\frac{M_2}{E_{loc}}.
\]

Then

\[
\mathcal V'
=\frac{M_2'}{E_{loc}}
-\frac{M_2 E_{loc}'}{E_{loc}^2}.
\]

The local enstrophy derivative contains its own production, dissipation, and boundary terms.

Consequently `V'` contains covariances between spatial radius and stretching/dissipation rather than a one-sign variance-production law.

No cancellation established in the present proof stack turns this quotient into a Lyapunov function.

---

## 12. DSD verdict on the separated-satellite idea

The M5-557 satellite is a genuine structural cost: the source cannot remain point-like.

But the natural width observable has the exact channel split

\[
\boxed{
\text{similarity expansion}
+\text{relative strain transport}
+\text{weight diffusion}
+\text{vortex-stretching production}
-\text{weighted palinstrophy}.
}
\]

All five channels can recur with signed cancellation.

Thus

\[
\boxed{
\text{separated satellite}
\not\Rightarrow
\text{strict viscous width drift}.
}
\]

---

## 13. What remains genuinely new

The source-shape architecture must be attacked through a relation that couples **different geometric channels**, not through scalar width alone.

The two best retained exact relations are now

\[
\boxed{
q_{a\leftarrow b}>0
}
\]

for recurrent cross stretching, and

\[
\boxed{
\langle n^TS_{ab}n\rangle=-1/2
}
\]

for material connector compression.

M5-556 further shows these are different leading kernel modes.

Any next rigidity mechanism must use their simultaneous realization by one finite source-shape field.

---

## 14. Highest-value next target

There are two viable directions.

1. **Localized ancient rigidity:** use M5-542--544 to ask whether the dynamically decoupled endpoint spectator tail can be removed from the hypotheses of the Albritton--Barker `L3` ancient Liouville mechanism, replacing global `L3` by bounded local-core `L3` plus quantitative far-field pressure/strain decoupling.
2. **Tensor source shape:** replace scalar width by a matrix-valued marker-centered second moment and determine whether its determinant/eigenvalue ratios acquire a stricter deformation law when combined with the recurrent connector-compression and cross-stretch marks.

Neither closure is assumed here.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
