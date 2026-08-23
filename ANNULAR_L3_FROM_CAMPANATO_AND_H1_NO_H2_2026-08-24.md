# Annular L3 Tail from Relative Campanato + Critical H1, without H2 — 2026-08-24

Status: **H2CRIT REMOVED FROM THE L3-LIOUVILLE ROUTE / GLOBAL REGULARITY NOT PROVED.**

The annular H2 bridge is useful when one wants the pointwise spatial Type-I bound

\[
|V(Y,s)|\lesssim |Y|^{-1}
\]

needed by certain one-slice/RSS/RDSS criteria.

It is **not** necessary for the separate endgame that aims only to place a recurrent ancient state in global `L3`.

For the cubic tail, a scale-invariant annular interpolation uses only

1. relative velocity variance, and
2. first derivative energy.

Thus a large `H2crit_tail` caused by tiny-amplitude high-frequency oscillations need not be treated as a final obstruction to the `L3` route.

---

## 1. Annular quantities

Let

\[
A_R=\{R<|Y|<2R\},
\]

and let `A_R^*` be a fixed enlargement.

Set

\[
m_R=\fint_{A_R^*}VdY,
\]

\[
\boxed{
\mathfrak C_A(R)
:=
R^{-1}
\int_{A_R^*}|V-m_R|^2dY,
}
\]

and

\[
\boxed{
\mathfrak E_1(R)
:=
R\int_{A_R^*}|\nabla V|^2dY.
}
\]

Both are scale invariant under the Navier--Stokes critical scaling.

---

## 2. Local Sobolev estimate

On the fixed-shape annulus, scaling the standard Sobolev/Poincare inequality gives

\[
\boxed{
\|V-m_R\|_{L^6(A_R)}
\le
C
\left[
\|\nabla V\|_{L^2(A_R^*)}
+
R^{-1}\|V-m_R\|_{L^2(A_R^*)}
\right].
}
\]

In critical variables,

\[
\boxed{
\|V-m_R\|_{L^6(A_R)}
\le
C R^{-1/2}
\left[
\mathfrak E_1(R)^{1/2}
+
\mathfrak C_A(R)^{1/2}
\right].
}
\]

Also

\[
\|V-m_R\|_2
=R^{1/2}\mathfrak C_A(R)^{1/2}.
\]

---

## 3. Interpolate directly to L3

Interpolation gives

\[
\|f\|_3
\le
\|f\|_2^{1/2}\|f\|_6^{1/2}.
\]

Therefore

\[
\begin{aligned}
\int_{A_R}|V-m_R|^3
&=\|V-m_R\|_3^3\\
&\le
\|V-m_R\|_2^{3/2}
\|V-m_R\|_6^{3/2}.
\end{aligned}
\]

Substituting the scale-normalized bounds yields

\[
\boxed{
\int_{A_R}|V-m_R|^3dY
\le
C
\mathfrak C_A(R)^{3/4}
\left[
\mathfrak E_1(R)^{1/2}
+
\mathfrak C_A(R)^{1/2}
\right]^{3/2}.
}
\]

Equivalently,

\[
\boxed{
\int_{A_R}|V-m_R|^3dY
\le
C
\mathfrak C_A(R)^{3/4}
\bigl(
\mathfrak E_1(R)+\mathfrak C_A(R)
\bigr)^{3/4}.
}
\]

No second derivative appears.

---

## 4. Mean term from finite-energy/Campanato telescoping

For first-hitting prelimit fields, finite energy fixes the mean at infinity. The same dyadic mean estimate used in

`FINITE_ENERGY_RELATIVE_CAMPANATO_TO_MORREY_2026-08-24.md`

gives

\[
|m_R|
\le
C\sum_{k\ge0}
\frac{
\mathcal C_{2^kR}^{1/2}
}{2^kR}
\]

for ball means, with equivalent fixed-annulus versions after changing constants.

Hence the dimensionless mean amplitude obeys

\[
\boxed{
R|m_R|
\le
C
\sum_{k\ge0}
2^{-k}
\mathcal C_{2^kR}^{1/2}.
}
\]

Therefore

\[
\boxed{
\int_{A_R}|m_R|^3dY
\le
C
\left[
\sum_{k\ge0}
2^{-k}
\mathcal C_{2^kR}^{1/2}
\right]^3.
}
\]

Combining mean and mean-free parts gives a complete annular cubic ledger involving only relative Campanato and critical H1 shell energy.

---

## 5. Full annular cubic estimate

Up to fixed enlargement constants,

\[
\boxed{
\begin{aligned}
M_3(R)
:=\int_{A_R}|V|^3dY
\lesssim{}&
\mathfrak C_A(R)^{3/4}
(\mathfrak E_1(R)+\mathfrak C_A(R))^{3/4}\\
&+
\left[
\sum_{k\ge0}2^{-k}
\mathcal C_{2^kR}^{1/2}
\right]^3.
\end{aligned}
}
\]

This is the appropriate tail functional for the global-L3 endgame.

---

## 6. H2crit is route-specific, not universally terminal

A shell may have

\[
R^3\int_{A_R}|\nabla^2V|^2\gg1
\]

because of a very small-amplitude high-frequency packet.

Such a packet may obstruct a pointwise `H2 -> L-infinity` estimate while contributing negligibly to

\[
\int_{A_R}|V|^3.
\]

Therefore

\[
\boxed{
H_{2,crit}^{tail}
\text{ is a failure branch of the pointwise spatial-Type-I route,}
}
\]

but it is **not automatically a failure branch of the L3-Liouville route**.

This distinction prevents another DSD bookkeeping overreach.

---

## 7. New L3 tail target

For dyadic radii `R_k=2^kR0`, a sufficient condition for global L3 is now

\[
\boxed{
\sum_k
\mathfrak C_A(R_k)^{3/4}
(\mathfrak E_1(R_k)+\mathfrak C_A(R_k))^{3/4}
<\infty
}
\]

plus summability of the dyadic mean term.

Thus the remaining L3-tail problem is reduced to the **joint distribution across logarithmic scales** of

\[
\boxed{
\mathfrak C_A(R_k),
\qquad
\mathfrak E_1(R_k),
}
\]

rather than any H2 norm.

The existing result

\[
H_{1,crit}^{tail}
\Longrightarrow
\text{Campanato escalation}\lor H_{2,crit}^{tail}
\]

remains useful for the pointwise Type-I route, but the L3 route should instead work directly with the cubic ledger above.

---

## 8. Next quantitative question

The most direct remaining theorem is now:

\[
\boxed{
\text{does no-replenishment / no-turnover force the dyadic cubic series above to be summable on a recurrent-state time-translation limit?}
}
\]

If yes, the recurrent state lies in global `L3` and the standard ancient Liouville/backward-uniqueness endgame becomes available.

If no, the nonsummable sequence identifies the exact logarithmic scales on which historical replenishment or Campanato escalation must be charged.

Status: **SECOND DERIVATIVES ARE NOT NEEDED TO CONTROL THE CUBIC TAIL. THE GLOBAL-L3 ENDGAME DEPENDS ONLY ON RELATIVE CAMPANATO, CRITICAL FIRST-DERIVATIVE SHELL ENERGY, AND THE DYADIC MEAN. H2CRIT REMAINS RELEVANT ONLY TO THE STRONGER POINTWISE SPATIAL-TYPE-I ROUTE. GLOBAL REGULARITY REMAINS UNPROVED.**