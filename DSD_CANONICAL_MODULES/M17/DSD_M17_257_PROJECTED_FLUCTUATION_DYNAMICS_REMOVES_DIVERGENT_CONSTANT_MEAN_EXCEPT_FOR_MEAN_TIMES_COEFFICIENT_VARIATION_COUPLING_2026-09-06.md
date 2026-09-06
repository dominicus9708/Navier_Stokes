# DSD M17-257 — Projected fluctuation dynamics removes the divergent constant mean except for mean-times-coefficient-variation coupling

Date: 2026-09-06  
Canonical ID: **M17-257**

Status: **COHERENT-MEAN DYNAMIC AUDIT / M17-256 SHOWS THAT NORMALIZED MASS DECOMPACTIFICATION ON A PALINSTROPHY-QUIET BRANCH MUST BE ALMOST CONSTANT ON EACH FIXED OWN-SCALE BALL. HOWEVER THE SIMPLE PARAMETER `r_j^2|c_j|` IS NOT BY ITSELF THE CORRECT FLUCTUATION-DYNAMIC SIZE, BECAUSE THE NORMALIZED MEAN `c_j/a_j` MAY DIVERGE. SUBTRACT THE SPATIAL MEAN ON A FIXED RESCALED BALL AND PROJECT THE RESCALED PDE AGAINST MEAN-ZERO TEST FUNCTIONS. ALL SPATIALLY CONSTANT BACKGROUND TERMS, INCLUDING THE LINEAR `-r_j^2 I` REACTION ACTING ON THE MEAN AND THE TIME DERIVATIVE OF THE CHOSEN MEAN, DROP OUT OF THE PROJECTED EQUATION. THE DIVERGENT MEAN REENTERS ONLY THROUGH SPATIAL VARIATION OF THE ZERO-ORDER COEFFICIENT, QUANTIFIED BY `Gamma_j = |bar V_j| osc(C_j)`. IF THIS COUPLING VANISHES AND THE ORDINARY SCALED COEFFICIENTS VANISH, THE MEAN-ZERO FLUCTUATION HAS THE SAME HEAT TANGENT LIMIT. IF IT DOES NOT, THE COHERENT BACKGROUND RETURNS TO AN EXPLICIT AMBIENT COEFFICIENT-INHOMOGENEITY PAYER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rescaled equation on a fixed ball

On one fixed rescaled ball

\[
B_K\subset\mathbb R^3,
\]

write the M17-255 equation

\[
\boxed{
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j.
}
\]

Here

\[
A_j
=r_j[B(q_j+r_jz)-B(q_j)],
\]

and

\[
C_j
=r_j^2\Sigma_j-r_j^2I.
\]

On the normalized mass-decompactifying coherent-mean branch,

\[
\int_{B_K}|V_j|^2\to\infty
\]

may hold even though the derivative packet normalization remains fixed.

---

## 2. Spatial mean and fluctuation

Define

\[
\boxed{
\bar V_{j,K}(\tau)
:=
\frac1{|B_K|}
\int_{B_K}V_j(z,\tau)dz
}
\]

and

\[
\boxed{
F_{j,K}(z,\tau)
:=V_j(z,\tau)-\bar V_{j,K}(\tau).
}
\]

Then

\[
\boxed{
\int_{B_K}F_{j,K}(z,\tau)dz=0.
}
\]

Spatial derivatives are unchanged:

\[
\nabla F_{j,K}=\nabla V_j,
\qquad
\Delta F_{j,K}=\Delta V_j.
\]

---

## 3. Palinstrophy quietness bounds the normalized fluctuation mass

Mean-zero Poincare on `B_K` gives

\[
\|F_{j,K}\|_{L^2(B_K)}^2
\le
C_PK^2
\|\nabla V_j\|_{L^2(B_K)}^2.
\]

In original variables,

\[
\|\nabla_zV_j\|_2^2
=
\frac{r_j^2}{E_j}
\int_{B_{Kr_j}}|\nabla W_j|^2dy
\]

up to the fixed normalization constants.

Therefore if the normalized surrounding palinstrophy obeys

\[
\boxed{
\frac{r_j^2}{E_j}
\int_{B_{Kr_j}}|\nabla W_j|^2dy
\le P_K<\infty,
}
\]

then

\[
\boxed{
\|F_{j,K}\|_{L^2(B_K)}^2
\le C_KP_K.
}
\]

Thus even when the full normalized vorticity decompactifies through a large constant mean, the mean-zero fluctuation remains locally `L2` bounded on the palinstrophy-quiet branch.

---

## 4. Weak projected equation

Let

\[
\phi\in C_c^\infty(B_K\times(-T,0);\mathbb R^3)
\]

be a test function satisfying at every time

\[
\boxed{
\int_{B_K}\phi(z,\tau)dz=0.
}
\]

Because `bar V_{j,K}` is spatially constant,

\[
\nabla V_j=\nabla F_{j,K}.
\]

Also

\[
\int \bar V_{j,K}'(\tau)\cdot\phi\,dz=0.
\]

Hence subtracting the time-dependent mean creates no term in the projected weak equation.

The diffusion of a spatial constant also vanishes.

Therefore the projected fluctuation equation is

\[
\boxed{
\langle\partial_\tau F_{j,K},\phi\rangle
+
\int\nabla F_{j,K}:\nabla\phi
=
\int\left[-A_j\cdot\nabla F_{j,K}+C_jF_{j,K}+C_j\bar V_{j,K}\right]\cdot\phi.
}
\]

No explicit `bar V_j'` term remains.

---

## 5. Constant part of C_j acting on the mean also disappears

Let

\[
\boxed{
\bar C_{j,K}(\tau)
:=
\frac1{|B_K|}
\int_{B_K}C_j(z,\tau)dz.
}
\]

Then

\[
C_j\bar V_{j,K}
=
(C_j-\bar C_{j,K})\bar V_{j,K}
+
\bar C_{j,K}\bar V_{j,K}.
\]

The second term is spatially constant, so

\[
\int
\bar C_{j,K}\bar V_{j,K}\cdot\phi\,dz
=0.
\]

Thus the divergent mean reenters only through

\[
\boxed{
(C_j-\bar C_{j,K})\bar V_{j,K}.
}
\]

In particular the linear reaction part

\[
-r_j^2I
\]

is spatially constant and cancels exactly from this mean-background coupling.

---

## 6. Correct coherent-mean coupling parameter

Define

\[
\boxed{
\Gamma_j(K,T)
:=
\sup_{-T\le\tau\le0}
|̄V_{j,K}(\tau)|
\,
\|C_j-\bar C_{j,K}\|_{L^\infty(B_K)}.
}
\]

Since

\[
C_j=r_j^2\Sigma_j-r_j^2I,
\]

the constant reaction cancels and

\[
\boxed{
\Gamma_j(K,T)
=
\sup_\tau
|̄V_{j,K}(\tau)|
\,
r_j^2
\|\Sigma_j-\bar\Sigma_{j,K}\|_{L^\infty(B_K)}.
}
\]

This is the correct normalized mean-times-coefficient-variation coupling.

It replaces the insufficient diagnostic

\[
r_j^2|c_j|.
\]

A physically small mean can still be dynamically relevant after packet normalization if its normalized size multiplies a coefficient variation that does not decay fast enough.

---

## 7. Fluctuation heat limit under vanishing coupling

Assume on every fixed `K,T`:

\[
\boxed{
\|A_j\|_\infty
+
\|C_j\|_\infty
\to0,
}
\]

and

\[
\boxed{
\Gamma_j(K,T)\to0.
}
\]

Assume also the normalized palinstrophy bound of Section 3, so `F_{j,K}` is locally `L2` bounded.

The same Caccioppoli/Aubin--Lions argument as M17-255 gives a subsequence

\[
F_{j,K}\to F_K
\]

strongly in local spacetime `L2`.

In the projected weak equation:

- `A_j grad F_j ->0`;
- `C_jF_j->0`;
- `(C_j-bar C_j)bar V_j->0` by `Gamma_j->0`.

Hence

\[
\boxed{
\partial_\tau F_K=\Delta F_K
}
\]

in the mean-zero projected sense on the fixed ball.

Equivalently, after adding back an arbitrary spatially constant caloric gauge, the fluctuation is a genuine local heat solution.

---

## 8. Failure returns to an ambient-coefficient payer

If

\[
\Gamma_j(K,T)\not\to0,
\]

then the coherent mean is not dynamically harmless.

The surviving quantity is

\[
\boxed{
|̄V_{j,K}|
\,
r_j^2
\operatorname{osc}_{B_K}\Sigma_j.
}
\]

This is an explicit ambient strain-inhomogeneity coupling.

It belongs to the scaled ambient/coefficient branch rather than to a separate mass-decompactification branch.

Thus

\[
\boxed{
G_{coherent\ mean\ dominance}
\Longrightarrow
H_{projected\ heat\ fluctuation}
\lor
G_{mean\text{-}shear\ coupling}.
}
\]

---

## 9. Relation to M17-256

M17-256 introduced

\[
\beta_{j,K}=r_j^2|c_{j,K}|
\]

as a first diagnostic of ambient-mean dynamical size.

M17-257 corrects and refines that diagnostic for the **packet-normalized fluctuation equation**.

The correct coupling is not the physical mean alone.

It is the normalized mean multiplied by the spatially varying part of the scaled zero-order coefficient:

\[
\boxed{
\Gamma_j
\sim
\frac{|c_j|}{a_j}
\,
 r_j^2\operatorname{osc}\Sigma_j.
}
\]

Therefore `beta_j->0` is neither necessary nor sufficient by itself for fluctuation decoupling.

This correction is additive and should be used in future frontier bookkeeping.

---

## 10. New residual after mean projection

The raw normalized-field decompactification has now been replaced by

\[
\boxed{
H_{bounded\ mean\text{-}zero\ fluctuation}
\lor
H_{normalized\ palinstrophy}
\lor
G_{mean\text{-}shear\ coupling}.
}
\]

On the first branch, the divergent constant background no longer prevents local compactness.

The next question is whether the projected fluctuation can be given enough global gradient/derivative control to invoke an ancient heat Liouville theorem modulo constants.

---

## 11. DSD audit

- The coherent mean is subtracted only after writing the full rescaled dynamic equation.
- Time dependence of the mean is not ignored; it cancels only against mean-zero test functions.
- Constant zero-order background terms are separated from coefficient variation.
- The linear reaction term acting on the mean cancels exactly in the projected equation.
- `r_j^2|c_j|` is explicitly downgraded from a sufficient criterion.
- The new coupling `Gamma_j` is dimensionless in the packet-normalized equation.
- Failure of mean decoupling is returned to an ambient coefficient-inhomogeneity branch.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
