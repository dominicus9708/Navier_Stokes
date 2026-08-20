# Two-Residual Alignment Geometry of the Remaining P_V Branch — 2026-08-20

Overall status: **P_V BRANCH REPARAMETERIZED — GLOBAL REGULARITY NOT PROVED.**

This note rewrites the final full-Navier--Stokes projective branch in coordinates adapted to two existing strain model decompositions. The result is an exact one-scalar-plus-orthogonal decomposition of the advection action relative to the algebraic vorticity--strain projective action.

---

## 1. The two projective terms

Let

\[
\mathcal A=P_{st}((u\cdot\nabla)S),
\]

and

\[
\mathcal V=P_{st}\left(\frac13S^2+\frac14\omega\otimes\omega\right).
\]

The residual relative to the strain self-amplification model is

\[
\boxed{
\mathcal R_{SA}=\mathcal A+\mathcal V.
}
\]

There is a second natural residual, obtained by viewing full Navier--Stokes as a perturbation of the globally regular strain--vorticity interaction model:

\[
\mathcal R_{VI}
=P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right).
\]

Since

\[
3\mathcal V
=P_{st}\left(S^2+\frac34\omega\otimes\omega\right),
\]

we have the exact relation

\[
\boxed{
\mathcal R_{VI}=\mathcal A+3\mathcal V.
}
\]

Therefore

\[
\boxed{
\mathcal R_{VI}-\mathcal R_{SA}=2\mathcal V.
}
\]

The two model residuals can never both be small when `V` is projectively active.

---

## 2. Alignment coordinate alpha

Whenever `V != 0`, define

\[
\alpha
=-\frac{\langle\mathcal A,\mathcal V\rangle}{\|\mathcal V\|_2^2}.
\]

Set

\[
\mathcal A_{\perp}=\mathcal A+\alpha\mathcal V.
\]

Then

\[
\langle\mathcal A_{\perp},\mathcal V\rangle=0,
\]

and

\[
\boxed{
\mathcal A=-\alpha\mathcal V+\mathcal A_{\perp}.
}
\]

Thus the two residuals become

\[
\boxed{
\mathcal R_{SA}=(1-\alpha)\mathcal V+\mathcal A_{\perp},
}
\]

\[
\boxed{
\mathcal R_{VI}=(3-\alpha)\mathcal V+\mathcal A_{\perp}.
}
\]

By orthogonality,

\[
\boxed{
\|\mathcal R_{SA}\|_2^2
=(1-\alpha)^2\|\mathcal V\|_2^2
+\|\mathcal A_{\perp}\|_2^2,
}
\]

\[
\boxed{
\|\mathcal R_{VI}\|_2^2
=(3-\alpha)^2\|\mathcal V\|_2^2
+\|\mathcal A_{\perp}\|_2^2.
}
\]

The exact difference is

\[
\boxed{
\|\mathcal R_{VI}\|_2^2
-\|\mathcal R_{SA}\|_2^2
=4(2-\alpha)\|\mathcal V\|_2^2.
}
\]

---

## 3. Interpretation of the two cancellation centers

### alpha = 1

\[
\mathcal A\approx-\mathcal V
\]

makes `R_SA` small. This is the cancellation required for the full equation to track the strain self-amplification model. Earlier in the proof route, projection-visible occupied middle strain plus a small `R_SA` forced large advection and hence a derivative cost unless the quadratic stress entered the projection-invisibility branch `G_Q`; the max-mid and near-max-mid subbranches of `G_Q` were then reduced further.

### alpha = 3

\[
\mathcal A\approx-3\mathcal V
\]

makes `R_VI` small. The strain--vorticity interaction model obtained by removing `R_VI` is globally regular, and the existing perturbative regularity criteria use the size of `R_VI` relative to derivative norms. Hence this is the regularizing cancellation center.

### alpha = 2

At the midpoint,

\[
\|R_{VI}\|_2=\|R_{SA}\|_2
\]

when measured with the same orthogonal component. Thus `alpha=2` is the exact algebraic separator between which model residual is smaller.

---

## 4. Existing regularity constraint in these coordinates

A known strain--vorticity perturbative criterion implies that finite-time blowup requires, along times approaching the putative blowup time,

\[
\limsup
\frac{\|\mathcal R_{VI}\|_2}{\|\Delta S\|_2}
\ge1.
\]

In the present coordinates this is

\[
\boxed{
\limsup
\frac{
\sqrt{(3-\alpha)^2\|\mathcal V\|_2^2+\|\mathcal A_{\perp}\|_2^2}
}{\|\Delta S\|_2}
\ge1.
}
\]

Thus a singular branch cannot remain eventually in a sufficiently small neighborhood of the regularizing center `alpha=3` with small orthogonal advection relative to the derivative scale.

There is also a scale-critical integral criterion involving the same `R_VI` residual; finite-time blowup forces divergence of that critical residual/derivative action.

---

## 5. Relation to the present proof tree

The final `P_V` branch should no longer be treated as one undifferentiated projective action. It splits into:

1. `SA-lock`: `alpha` near 1 and `A_perp` small;
2. `VI-lock`: `alpha` near 3 and `A_perp` small;
3. `transverse-advection`: `A_perp` non-negligible;
4. `intermediate-alignment`: `alpha` stays away from both 1 and 3.

The first has already been strongly constrained by the `G_Q`, max-mid, determinant-defect, and derivative-cancellation calculations. The second is constrained by the known strain--vorticity regularity criterion. The genuinely new remaining projective dynamics are therefore the transverse-advection and intermediate-alignment sectors.

---

## 6. Next target

Derive an evolution/packing estimate for `alpha` and `A_perp`, or show that persistent `A_perp` is necessarily a material/derivative reorganization cost. In self-similar logarithmic variables the `P_V` action is scale invariant, so these coordinates should pass naturally to the restricted Type-I ancient orbit.

Status: **THE FINAL P_V BRANCH HAS TWO EXACT CANCELLATION CENTERS: alpha=1 (SELF-AMPLIFICATION LOCK) AND alpha=3 (STRAIN--VORTICITY REGULARIZING LOCK). A SINGULAR SURVIVOR MUST AVOID THE REGULARIZING CENTER OFTEN ENOUGH WHILE ALSO AVOIDING THE DERIVATIVE COST ALREADY ASSOCIATED WITH THE SELF-AMPLIFICATION CENTER.**