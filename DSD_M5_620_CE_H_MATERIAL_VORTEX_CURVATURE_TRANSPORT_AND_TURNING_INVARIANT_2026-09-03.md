# DSD M5-620 — CE-H material vortex-curvature transport and turning invariant

Date: 2026-09-03

Status: **INTERNAL EXACT GEOMETRIC LAW, CONDITIONAL ON THE M5-599 GLOBAL CE-H BRANCH / BECAUSE `D_B xi=0` AND THE MATERIAL VELOCITY GRADIENT MAPS THE VORTEX DIRECTION TO `(sigma+1/2) xi`, THE VORTEX-LINE CURVATURE VECTOR `K=(xi·nabla)xi` SATISFIES THE CLOSED MATERIAL ODE `D_B K=-(sigma+1/2)K` / THE PRODUCT OF CURVATURE WITH A MATERIAL ARCLENGTH ELEMENT IS EXACTLY INVARIANT / THIS TURNS THE M5-619 CURVATURE CHARGE INTO A TRUE MATERIAL-LINE OBSERVABLE, BUT DOES NOT BY ITSELF CONTRADICT RECURRENCE BECAUSE MATERIAL LINE LENGTH MAY EXPAND WHILE CURVATURE DECAYS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H inputs

On the global double-eigenline branch,

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

\[
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W,
\]

and the similarity material derivative

\[
D_B:=\partial_\theta+B\cdot\nabla,
\qquad
B=U+\frac12y
\]

obeys

\[
\boxed{D_B\xi=0.}
\]

Because the antisymmetric part of `nabla U` annihilates `xi`,

\[
(\nabla U)\xi=\sigma\xi.
\]

Hence

\[
\boxed{(\xi\cdot\nabla)B=(\nabla B)\xi=\left(\sigma+\frac12\right)\xi.}
\]

---

## 2. Define vortex-line curvature

Let

\[
\boxed{\mathcal K:=(\xi\cdot\nabla)\xi.}
\]

For a vortex line parametrized by arclength, `xi` is the unit tangent and `mathcal K` is the curvature vector.

Since `|xi|=1`,

\[
\mathcal K\perp\xi.
\]

---

## 3. Commutator of material and vortex-line derivatives

For any smooth scalar or vector field `f`,

\[
D_B\big((\xi\cdot\nabla)f\big)
-(\xi\cdot\nabla)(D_Bf)
=
\big(D_B\xi-(\xi\cdot\nabla)B\big)\cdot\nabla f.
\]

Using

\[
D_B\xi=0
\]

and

\[
(\xi\cdot\nabla)B
=\left(\sigma+\frac12\right)\xi,
\]

we obtain

\[
\boxed{
[D_B,\xi\cdot\nabla]
=-\left(\sigma+\frac12\right)(\xi\cdot\nabla).
}
\]

This identity is exact.

---

## 4. Exact material curvature equation

Apply the commutator to `f=xi`.

Since

\[
D_B\xi=0,
\]

we get

\[
D_B\mathcal K
=D_B\big((\xi\cdot\nabla)\xi\big)
=-\left(\sigma+\frac12\right)(\xi\cdot\nabla)\xi.
\]

Therefore

\[
\boxed{
D_B\mathcal K
=-\left(\sigma+\frac12\right)\mathcal K.
}
\]

Consequently, wherever `mathcal K` is nonzero,

\[
\boxed{
D_B\log|\mathcal K|
=-\sigma-\frac12.
}
\]

A material point with zero curvature remains zero-curvature as long as it remains in the CE-H branch.

---

## 5. Material arclength law

Let

\[
\ell=a_\parallel\xi
\]

be an infinitesimal material line element tangent to the vortex line.

Material line elements satisfy

\[
D_B\ell=(\nabla B)\ell.
\]

Hence

\[
\boxed{
D_B\log a_\parallel
=\sigma+\frac12.
}
\]

Combine this with the curvature law:

\[
D_B\log|\mathcal K|
=-\sigma-\frac12.
\]

Thus

\[
\boxed{
D_B\big(a_\parallel\mathcal K\big)=0.
}
\]

Equivalently,

\[
\boxed{
a_\parallel(\theta)\mathcal K(\theta)
=a_\parallel(\theta_0)\mathcal K(\theta_0)
}
\]

along every material vortex-line element.

This is the exact infinitesimal turning-vector invariant.

---

## 6. Geometric meaning

For a short material vortex-line segment,

\[
\delta\Theta
\approx
|\mathcal K|\,\delta s.
\]

The invariant

\[
a_\parallel\mathcal K=\text{constant}
\]

therefore says that the infinitesimal turning angle between neighboring material labels is frozen on CE-H.

The vortex line may stretch, but its material turning angle is not created or destroyed; stretching only dilutes curvature by the reciprocal arclength factor.

---

## 7. Relation to the M5-602 flux cocycle

M5-602 gives for an infinitesimal material vortex-tube flux

\[
\boxed{D_B\log|\phi|=\kappa.}
\]

Thus a curved material tube element simultaneously obeys

\[
D_B\log|\mathcal K|
=-\sigma-\frac12,
\]

\[
D_B\log|\phi|
=\kappa,
\]

and the vorticity amplitude obeys

\[
D_B\log\rho=\sigma+\kappa-1.
\]

These are three exact scalar drift laws attached to the same material geometry.

---

## 8. Coherent-return consequence

If the **same material line element** has nonzero curvature and returns recurrently with both

\[
0<K_-\le |\mathcal K(\theta_j)|\le K_+<\infty
\]

and

\[
0<a_-\le a_\parallel(\theta_j)\le a_+<\infty,
\]

then either recurrence condition yields

\[
\boxed{
\langle\sigma\rangle_{line}=-\frac12.
}
\]

This should be compared with the recurrent cross-sectional-area condition from M5-602,

\[
\langle\sigma\rangle_{area}=1.
\]

However these are not automatically the same material observable. A material tube may stretch longitudinally while expanding/contracting transversely, and M5-560 already showed that its positive material volume cannot remain recurrent in a bounded similarity core.

Therefore no contradiction is claimed from the two averages alone.

---

## 9. A stronger three-observable audit

Suppose one insists on a single material tube element for which

1. curvature remains nonzero and recurrent;
2. flux remains bounded and nondegenerate;
3. vorticity amplitude remains bounded and nondegenerate.

Then the return averages give

\[
\langle\sigma\rangle=-\frac12,
\qquad
\langle\kappa\rangle=0,
\]

while amplitude recurrence requires

\[
0
=
\langle\sigma+\kappa-1\rangle.
\]

The first two values make the right-hand side equal

\[
-\frac32,
\]

not zero.

Hence

\[
\boxed{
\text{same-material curved tube}
+\text{ recurrent flux}
+\text{ recurrent amplitude}
\Longrightarrow\bot.
}
\]

This is a genuine incompatibility, but its applicability requires that the same material tube/line element carries all three recurrent marks. Existing lineage bookkeeping still allows marker/tube migration, so this is a conditional closure rather than a global contradiction.

---

## 10. Whole-space curvature charge to study next

Define

\[
\boxed{
\mathcal C(\theta)
:=
\int_{\mathbb R^3}
\rho^2|\mathcal K|^2dy.
}
\]

Because M5-619 may force a uniform curvature channel, a whole-space evolution law for `mathcal C` avoids the same-marker identification problem.

The next step should derive this ledger and compare its `kappa` average with the negative global enstrophy-weighted `kappa` mean.

---

## 11. Firewall

The exact law

\[
D_B\mathcal K=-(\sigma+1/2)\mathcal K
\]

holds only on the CE-H branch where `D_B xi=0` globally.

A positive Eulerian curvature `L2` charge does not automatically identify one persistent material line segment carrying that charge forever.

No such identification is used here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
