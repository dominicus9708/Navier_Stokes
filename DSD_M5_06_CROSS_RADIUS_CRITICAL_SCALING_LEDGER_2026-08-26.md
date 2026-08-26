# DSD M5-06 — Cross-Radius Critical Scaling Ledger

Date: 2026-08-26

Status: **M5 SUBSTEP / A COHERENT CRITICAL RADIUS FAMILY PRODUCES LOGARITHMIC STRONG-L3 GROWTH WHILE REMAINING COMPATIBLE WITH FINITE KINETIC ENERGY AND FINITE TOTAL PHYSICAL DISSIPATION / THIS LOCKS THE ENDPOINT SCALING AND RULES OUT FURTHER SUBCRITICAL-BUDGET SHORTCUTS / GLOBAL REGULARITY UNPROVED.**

## 1. Cross-radius hypothesis

Assume that at a late physical time `t<T*` there is a dyadic family of radii

\[
r_j=2^{-j}r_0,
\qquad
r_*(t)\lesssim r_j\le r_0,
\]

such that the critical cubic shell mass satisfies

\[
\boxed{
\int_{r_j<|x-X_*|<2r_j}|u(x,t)|^3dx\ge m_*>0
}
\]

uniformly over the active shells.

This is the physical form of a coherent critical `1/r` family across characteristics.

---

## 2. Strong `L3` grows logarithmically

The number of active dyadic shells is

\[
N(t)
\sim
\frac{\log(r_0/r_*(t))}{\log2}.
\]

Therefore

\[
\boxed{
\|u(t)\|_3^3
\ge
m_*N(t)
\gtrsim
\log\frac{r_0}{r_*(t)}.
}
\]

For a Type-I inner scale

\[
r_*(t)\asymp \sqrt{T_*-t},
\]

this becomes

\[
\boxed{
\|u(t)\|_3^3
\gtrsim
\frac12\log\frac1{T_*-t}-C.
}
\]

Thus cross-radius coherence necessarily leaves the strong `L3` continuation class by logarithmic divergence.

This reproduces the critical cubic-memory picture in physical variables.

---

## 3. Kinetic energy remains finite

For a critical `1/r` shell, the kinetic-energy scaling is

\[
\int_{r<|x-X_*|<2r}|u|^2dx\sim r.
\]

More generally, under the W1 Type-I upper envelope `|u| <= A/r` on the critical corridor, cubic shell mass controls from below a linear-in-radius kinetic contribution of the same scaling, while the upper envelope gives the matching dimensional ceiling.

Hence the dyadic energy ledger has the form

\[
\sum_j O(r_j).
\]

Because

\[
\sum_{j\ge0}2^{-j}r_0<\infty,
\]

one obtains

\[
\boxed{
\text{critical cross-radius coherence is compatible with finite physical kinetic energy.}
}
\]

There is no energy contradiction.

---

## 4. Enstrophy has the Type-I half-power scaling

For the model critical profile

\[
|u|\sim r^{-1},
\qquad
|\nabla u|\sim r^{-2}.
\]

The enstrophy contribution of one dyadic shell is

\[
\int_{r<|x-X_*|<2r}|\nabla u|^2dx
\sim r^{-1}.
\]

Summing from `r_*(t)` to `r0` is dominated by the smallest radius:

\[
\boxed{
\|\nabla u(t)\|_2^2
\sim r_*(t)^{-1}.
}
\]

With `r_*(t) ~ sqrt(T*-t)`, this is

\[
\boxed{
\|\nabla u(t)\|_2^2
\sim (T_*-t)^{-1/2}.
}
\]

Therefore

\[
\int^{T_*}\|\nabla u(t)\|_2^2dt
\sim
\int^{T_*}(T_*-t)^{-1/2}dt
<\infty.
\]

So the total physical viscous budget also remains finite.

---

## 5. DSD interpretation

The coherent family separates three layers cleanly:

1. **critical cubic state density** — one order-one contribution per log radius, hence logarithmic accumulation;
2. **kinetic energy** — one `O(r)` contribution per radius shell, hence geometrically summable;
3. **ordinary enstrophy** — one `O(1/r)` contribution per shell, dominated by the smallest active radius and still time-integrable under Type-I scaling.

Thus

\[
\boxed{
\text{strong-}L^3\text{ fails critically while energy and total dissipation remain admissible.}
}
\]

This is not an inconsistency. It is the exact endpoint configuration M5 must exclude by additional structure.

---

## 6. Consequence for proof search

This ledger closes another family of shortcuts.

The following cannot by themselves exclude the cross-radius survivor:

- finite physical kinetic energy;
- finite total physical enstrophy dissipation;
- logarithmic strong-`L3` growth;
- Type-I half-power enstrophy growth.

Any M5 closure must therefore use information that couples different radius channels more strongly than these scalar budgets do.

The next useful target is a **radius-to-radius coherence identity/inequality** involving a genuinely signed or monotone quantity, or an endpoint compactness theorem that prevents the `1/r` family from remaining coherent down to `r=0`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
