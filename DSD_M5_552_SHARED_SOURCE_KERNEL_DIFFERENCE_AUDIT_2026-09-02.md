# DSD M5-552 — Shared-source kernel-difference audit: the remote tail is negligible in pair strain difference, but arbitrary dual flux packets do not force cross-strain coercivity

Date: 2026-09-02

Status: **SHARED-SOURCE AUDIT / THE STRAIN DIFFERENCE OF TWO PERSISTENT CARRIER POINTS IS AN EXACT DIFFERENCE OF ONE BIOT--SAVART SINGULAR INTEGRAL / ON THE REMOTE TAIL THE DIFFERENCE KERNEL GAINS ONE POWER, GIVING AN `O(d R^{-5/2} E_tail^{1/2})` BOUND, SO THE SPECTATOR TAIL CANNOT DECOUPLE THE TWO LINEAGE STRAINS / HOWEVER THE TWO LOCAL CARRIER SELF-FIELDS AND THE FINITE RESIDUAL CORE REMAIN ORDER-ONE AND SIGN-INDEFINITE / FIXED NONZERO FLUX AND NONCOLLINEARITY ALONE DO NOT IMPLY A UNIVERSAL POSITIVE CROSS-STRAIN LOWER BOUND / THEREFORE THE NAIVE SHARED-SOURCE RIGIDITY SHORTCUT FAILS / THE NEXT STEP MUST USE THE M5-455 FORMATION RELATION THAT PRODUCTIVE LONGITUDINAL STRAIN FORCES TRANSVERSE VORTICITY IN THE SAME BOUNDED WINDOW, NOT MERELY THE LATER EXISTENCE OF TWO FLUX PACKETS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Persistent pair geometry

Work on the compact finite-core component from M5-543--551.

Let

\[
x_a(\theta),\qquad x_b(\theta)
\]

be the representative active points of a recurrent persistent dual pair, with

\[
d(\theta):=|x_a-x_b|\le d_*<\infty.
\]

Their local coherent directions satisfy a fixed noncollinearity mark at recurrent events,

\[
1-(\xi_a\cdot\xi_b)^2\ge s_0^2>0,
\]

and their material-flux sizes satisfy

\[
|\Phi_a|,|\Phi_b|\ge\phi_0>0.
\]

M5-491 already established that the two packets generally sample different strain tensors.

---

## 2. One common strain source

For divergence-free vorticity `W`, write the symmetric velocity gradient as the Calderon--Zygmund transform

\[
\boxed{
\Sigma(x)
=
\operatorname{p.v.}\int_{\mathbb R^3}K_S(x-z)W(z)\,dz,
}
\]

where the matrix-valued kernel is homogeneous of degree `-3`:

\[
|K_S(y)|\le C|y|^{-3},
\qquad
|\nabla K_S(y)|\le C|y|^{-4}.
\]

Therefore

\[
\boxed{
\Sigma(x_a)-\Sigma(x_b)
=
\operatorname{p.v.}\int
\bigl[K_S(x_a-z)-K_S(x_b-z)\bigr]W(z)\,dz.
}
\]

This is the exact shared-source relation left by M5-551.

---

## 3. Four-way source decomposition

Choose a fixed carrier radius `r_c>0` supplied by the analytic coherent-packet construction, small enough that the two selected carrier neighborhoods can be treated separately at the recurrent dual event.

Let

\[
B_a:=B_{r_c}(x_a),
\qquad
B_b:=B_{r_c}(x_b).
\]

Choose a large finite core radius `R` containing both packets and set

\[
\mathcal C_R:=B_R\setminus(B_a\cup B_b).
\]

Split

\[
W=W_a+W_b+W_{res}+W_{tail}
\]

with smooth cutoffs adapted respectively to

\[
B_a,\quad B_b,\quad \mathcal C_R,\quad \{|z|>R\}.
\]

By linearity,

\[
\Sigma_a-\Sigma_b
=I_a+I_b+I_{res}+I_{tail},
\]

where each term is the kernel difference acting on the corresponding source piece.

---

## 4. Remote kernel difference gains one power

Take `R` so large that

\[
R\ge 4(1+|x_a|+|x_b|)
\]

throughout the fixed active core window.

For `|z|>R`, the segment joining `x_a-z` and `x_b-z` stays at distance comparable to `|z|` from the origin.

The mean-value theorem and the kernel derivative bound give

\[
\boxed{
|K_S(x_a-z)-K_S(x_b-z)|
\le
C\frac{d}{|z|^4}.
}
\]

Hence by Cauchy--Schwarz,

\[
\begin{aligned}
|I_{tail}|
&\le
Cd
\left(\int_{|z|>R}|z|^{-8}\,dz\right)^{1/2}
\|W\|_{L^2(|z|>R)}\\
&\le
CdR^{-5/2}E_{tail}(R)^{1/2}.
\end{aligned}
\]

Thus

\[
\boxed{
|I_{tail}|
\le
CdR^{-5/2}E_{tail}(R)^{1/2}
\longrightarrow0
}
\]

uniformly on the compact hull.

This is one power of `R` stronger than the individual far-strain estimate from M5-534.

---

## 5. Generation-integrated remote difference also vanishes

The similarity roof lengths are uniformly bounded on the retained generation hull.

Therefore M5-542 and the preceding pointwise estimate imply

\[
\boxed{
\sup_j
\int_{I_j}|I_{tail}(\theta)|\,d\theta
\to0
\qquad(R\to\infty).
}
\]

Hence the endpoint spectator tail cannot create an order-one relative-strain drift between the two persistent lineages either instantaneously or after one full generation.

The shared-source obstruction is entirely a finite-core problem.

---

## 6. The residual core is bounded but not small by kernel structure alone

On the residual core away from the singular carrier balls, the kernel difference is smooth.

If the residual support stays a fixed distance `r_0>0` from both marker points, then

\[
|K_S(x_a-z)-K_S(x_b-z)|
\le C(d_*,r_0,R).
\]

Consequently

\[
|I_{res}|
\le C\|W_{res}\|_{L^2(\mathcal C_R)}.
\]

The right-hand side is uniformly bounded by compactness, but no smallness or sign follows merely from the global enstrophy cap.

Thus the finite residual core can remain an order-one shared source.

---

## 7. Local self-blocks also remain order one

The contribution of `W_a` to `Sigma(x_a)` contains the principal-value singular integral on its own coherent carrier neighborhood.

The contribution of `W_a` to `Sigma(x_b)` is nonsingular if the carrier balls are separated.

Therefore the difference block

\[
I_a
=
\mathcal R_S[W_a](x_a)-\mathcal R_S[W_a](x_b)
\]

need not be small.

The same is true for `I_b`.

Their signs and tensor directions depend on the internal geometry of the coherent packets, not only on total directed flux and a central direction label.

---

## 8. Flux and noncollinearity do not determine the strain tensor

The retained pair data

\[
(\Phi_a,\Phi_b,\xi_a,\xi_b)
\]

contain only a finite set of scale-critical integral/directional marks.

The Biot--Savart strain at a point depends on the full spatial vorticity distribution through a degree `-3` singular kernel.

Consequently the presently retained data do not determine

\[
e_a^T\Sigma_b(x_a)e_a,
\qquad
P_{e_a^\perp}\Sigma_b(x_a)e_a,
\]

or the analogous quantities with `a,b` reversed.

In particular, no estimate of the form

\[
|\Phi_b|\ge\phi_0,
\quad
\sin\angle(\xi_a,\xi_b)\ge s_0
\quad\Longrightarrow\quad
|e_a^T\Sigma_b(x_a)e_a|\ge c(\phi_0,s_0)>0
\]

has been established, and it does not follow from flux/noncollinearity data alone.

This is a data-sufficiency audit, not a construction of a global Navier--Stokes counterexample.

---

## 9. Why the naive shared-source shortcut fails

The hoped-for shortcut was

\[
\text{same global }W
+\text{persistent noncollinear pair}
\Rightarrow
\text{forced cross-strain incompatibility}.
\]

M5-552 shows that this implication is not available from the current marks.

The remote part is rigidly negligible, but inside the finite core we still have

\[
\boxed{
I_a+I_b+I_{res}
}
\]

with three order-one, sign-indefinite blocks.

Thus common sourcing by itself is not yet coercive.

---

## 10. The missing information is the formation relation

M5-455 contains stronger information than M5-490's later pair mark.

At a productive first-hitting block there is a principal direction `e_*` and a fixed longitudinal strain action.

After analytic thickening, the productive window has a fixed longitudinal-strain lower mark, and M5-454 gives the directional-depletion inequality

\[
\boxed{
\|e_*^T\Sigma e_*\|_{L^2(B_R)}
\le
C_\kappa
\|(I-e_*\otimes e_*)W\|_{L^2(B_R^*)}.
}
\]

Hence productive axial strain cannot occur without a fixed amount of transverse vorticity in the same bounded source window.

The companion packet is extracted from this forced transverse source.

This is a **generative relation**, not merely coexistence of two flux packets.

---

## 11. New correct target: source attribution

The finite persistent-lineage saturation should now be applied before forgetting the M5-455 formation mechanism.

At each recurrent productive event, decompose the transverse source responsible for

\[
e_*^T\Sigma e_*
\]

among

1. the local principal lineage;
2. the finitely many other persistent lineage packets;
3. a residual bounded-core source;
4. the already negligible remote tail.

If the residual source repeatedly carries a fixed share, M5-497's local-payer saturation machinery should extract it as another coherent persistent payer/replacement branch.

On the saturated no-new-payer branch, one of the finite retained lineages must therefore repeatedly carry a fixed share of the productive Biot--Savart source.

That statement is stronger than arbitrary dual-pair recurrence and is the next useful shared-source object.

---

## 12. Updated shared-source frontier

The current logic is

\[
\boxed{
\begin{aligned}
&\text{persistent dual flux + noncollinearity}\n&\qquad\not\Rightarrow\text{universal cross-strain floor},\\[1mm]
&\text{M5-455 productive formation}\n&\qquad\Rightarrow\text{fixed transverse source in the same bounded window}.
\end{aligned}
}
\]

Therefore the final rigidity problem should be formulated using a recurrent **parent--payer relation** rather than an arbitrary pair-interaction matrix.

---

## 13. Highest-value next target

Construct a finite source-attribution decomposition at each productive event.

The desired conclusion is a dichotomy

\[
\boxed{
\text{productive parent strain}
\Longrightarrow
\text{recurrent ordered parent--payer lineage edge}
\lor
\text{new residual payer/reformation exit}.
}
\]

On the saturated compact branch, the second alternative is already costed by finite memory.

One should then extract a fixed ordered pair `(a,b)` recurring with positive frequency such that lineage `b` makes a quantitatively nonzero contribution to the productive axial strain of lineage `a`.

Only after obtaining this formation-linked interaction edge is it meaningful to search for reciprocity or cycle rigidity in the common Biot--Savart source.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
