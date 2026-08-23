# Recurrent Pressure-Affine Threshold Optimization — 2026-08-24

Status: **SYMBOLIC OPTIMIZATION OF THE CONDITIONAL AFFINE-INTERFACE CLOSURE TEST / GLOBAL REGULARITY NOT PROVED.**

The pressure-affine interface note produced the lower time-density estimate

\[
\delta_G(g)
\ge
\frac{1-g}{B_+-g},
\qquad 0<g<1,
\]

from the recurrent effective-growth average `G_bar >= 1` and ceiling `G <= B_+`, together with the affine-interface tax

\[
P_S\ge \frac{c_{aff}}2 g^2
\]

on the positive-middle affine-coherent part of the high-growth set.

Ignoring only the separately typed loss fraction into Betchov/residual channels, the resulting average palinstrophy lower bound is proportional to

\[
\boxed{
F_B(g):=rac{g^2(1-g)}{B-g},
\qquad B=B_+>1.
}
\]

---

## 1. Exact optimizer

Differentiation gives

\[
F_B'(g)
=
\frac{g\,[2g^2-(3B+1)g+2B]}{(B-g)^2}.
\]

The unique interior maximizer is the smaller root

\[
\boxed{
g_*(B)
=
\frac{3B+1-\sqrt{9B^2-10B+1}}4.
}
\]

For `B>1`, this lies in `(0,1)`. As `B -> infinity`,

\[
\boxed{g_*(B)\to\frac23.}
\]

Thus the efficient recurrent threshold is naturally of order `2/3`, not arbitrarily close to zero or one.

---

## 2. Optimized average interface tax

Let `eta_pm in [0,1]` denote the fraction of the high-growth time density that remains in the positive-middle affine-coherent lane after removing already typed Betchov/residual/pressure-fluctuation events.

Then

\[
\boxed{
\overline P_S
\ge
\eta_{pm}\frac{c_{aff}}2
F_B(g_*(B)).
}
\]

The recurrent H1 average upper budget is

\[
\boxed{
\overline P_S
\le
\frac{E_+}{\nu}
\left(\sqrt2B_+-\frac34\right)_+.
}
\]

Therefore the affine-pressure recurrent lane is excluded whenever

\[
\boxed{
\eta_{pm}\frac{c_{aff}}2
F_{B_+}(g_*(B_+))
>
\frac{E_+}{\nu}
\left(\sqrt2B_+-\frac34\right)_+.
}
\]

This removes the free threshold `g0` from the closure certificate.

---

## 3. Interpretation

If the optimized inequality fails, the remaining freedom is no longer the arbitrary choice of a growth threshold. It is concentrated in the physically meaningful quantities

\[
\boxed{
B_+,
\quad E_+,
\quad c_{aff},
\quad \eta_{pm}.
}
\]

Here `c_aff` measures the size/weight of the affine-coherent whole-space core and `eta_pm` measures how much recurrent source activity escapes to the already typed Betchov/residual/pressure-fluctuation alternatives.

Status: **THE RECURRENT PRESSURE-AFFINE CLOSURE TEST NO LONGER CONTAINS AN ARBITRARY EFFECTIVE-GROWTH THRESHOLD. THE OPTIMAL THRESHOLD IS EXPLICIT, LEAVING ONLY THE CORE-GEOMETRY, STRAIN-CEILING, ENSTROPHY, AND BRANCH-DENSITY PARAMETERS. GLOBAL REGULARITY REMAINS UNPROVED.**