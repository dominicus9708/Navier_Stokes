# DSD M5-541 — Adaptive radial moment yields a weighted `L3` endpoint but does not force weak-`L3`

Date: 2026-09-01

Status: **ADAPTIVE VELOCITY-ENDPOINT UPGRADE / THE M5-540 ALMOST-CRITICAL VORTICITY MOMENT CAN BE CHOSEN WITH AN `A2` RADIAL WEIGHT AND TRANSFERRED BY WEIGHTED CALDERON--ZYGMUND TO THE VELOCITY DIRICHLET FIELD / DYADIC POINCARE--SOBOLEV AND THE ANNULAR-MEAN TELESCOPE THEN GIVE A FINITE SPATIALLY WEIGHTED `L3` NORM `int |U|^3/L(r)^(3/2)` WHERE `L(r)=r/w_tilde(r)->infinity` GROWS MORE SLOWLY THAN EVERY POSITIVE POWER / THIS IS STRICTLY STRONGER THAN THE BARE INTERSECTION OF ALL `Lp`, `p>3`, BUT A SPARSE-SHELL COUNTERMODEL SHOWS THAT IT STILL DOES NOT FORCE `L^{3,infinity}` OR ANY FIXED LORENTZ ENDPOINT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-540

M5-540 gives an increasing radial weight `w_tilde(r)` such that

\[
\boxed{
 r^{1-\varepsilon}\ll \widetilde w(r)\ll r
 \qquad\forall\varepsilon>0,
}
\]

and on the invariant hard component

\[
\boxed{
\int_{\mathbb R^3}
\widetilde w(|y|)|W(y)|^2dy<\infty
\quad\text{for }\nu\text{-a.e. state.}
}
\]

Define the slowly varying endpoint loss

\[
\boxed{
L(r):=\frac{r}{\widetilde w(r)}.
}
\]

Then

\[
L(r)\to\infty,
\qquad
L(r)=o(r^\varepsilon)
\quad\forall\varepsilon>0.
\]

Thus `L` grows more slowly than every positive power.

---

## 2. `A2` audit for the adaptive weight

The smoothing freedom in M5-540 can be strengthened without changing its majorization property.

Choose the logarithmic deficit majorant so slowly that for large logarithmic radius `rho`,

\[
\left|\frac{d}{d\rho}\log\widetilde w(e^\rho)-1\right|
\le \frac14.
\]

Equivalently,

\[
\frac34
\le
\frac{d\log\widetilde w(r)}{d\log r}
\le
\frac54
\]

outside one fixed core.

A radial positive weight with logarithmic slope in a compact subinterval of `(-3,3)` is doubling and reverse-doubling with the exponents needed for the Muckenhoupt `A2` condition. The bounded-core regularization does not affect membership.

Hence

\[
\boxed{
\widetilde w\in A_2(\mathbb R^3).
}
\]

Therefore the Riesz transforms are bounded on `L2(w_tilde dy)` and, since `grad U` is a Calderon--Zygmund transform of vorticity,

\[
\boxed{
\int
\widetilde w(|y|)|\nabla U(y)|^2dy
\le C
\int
\widetilde w(|y|)|W(y)|^2dy<\infty.
}
\]

This is the weighted velocity-Dirichlet input.

---

## 3. Dyadic shell notation

Let

\[
R_k=2^kR_0
\]

and let `A_k` be the corresponding dyadic annulus, with `A_k^*` a fixed enlarged annulus of bounded overlap.

Set

\[
E_k:=\int_{A_k^*}|\nabla U|^2dy,
\]

\[
\boxed{
b_k:=R_kE_k,
}
\]

and

\[
\boxed{
m_k:=\widetilde w(R_k)E_k.
}
\]

Slow variation of `w_tilde` on dyadic shells gives

\[
\sum_km_k<\infty.
\]

Since

\[
L_k:=L(R_k)=\frac{R_k}{\widetilde w(R_k)},
\]

we have exactly

\[
\boxed{
b_k=L_km_k.
}
\]

---

## 4. Fluctuation part of the annular `L3` norm

Let

\[
c_k:=(U)_{A_k}
\]

be the annular mean.

After scaling `A_k` to a fixed unit annulus, Poincare--Sobolev gives

\[
\int_{A_k}|U-c_k|^3dy
\le Cb_k^{3/2}.
\]

Dividing by the endpoint loss,

\[
\boxed{
L_k^{-3/2}
\int_{A_k}|U-c_k|^3dy
\le Cm_k^{3/2}.
}
\]

Because `m in ell^1`,

\[
\sum_km_k^{3/2}<\infty.
\]

Thus the fluctuation contribution is summable in the adaptive weighted endpoint.

---

## 5. Annular mean telescope with the adaptive loss

M5-525--526 gave the exact dyadic mean estimate

\[
R_k|c_k|
\le
C\sum_{j\ge0}2^{-j}b_{k+j}^{1/2}.
\]

Divide by `L_k^(1/2)`:

\[
\frac{R_k|c_k|}{L_k^{1/2}}
\le
C\sum_{j\ge0}
2^{-j}
\left(\frac{L_{k+j}}{L_k}\right)^{1/2}
m_{k+j}^{1/2}.
\]

Since `L(r)=o(r^epsilon)` for every fixed `epsilon>0`, after increasing the bounded starting index if necessary one may fix an `eta<1` such that

\[
\frac{L_{k+j}}{L_k}
\le C2^{\eta j}
\]

uniformly for late shells.

Hence

\[
\boxed{
\frac{R_k|c_k|}{L_k^{1/2}}
\le
C\sum_{j\ge0}2^{-(1-\eta/2)j}m_{k+j}^{1/2}.
}
\]

The kernel is in `ell^1`.

Discrete Young convolution therefore gives

\[
\sum_k
\left(
\frac{R_k|c_k|}{L_k^{1/2}}
\right)^3
<\infty.
\]

Since

\[
|A_k||c_k|^3\asymp R_k^3|c_k|^3,
\]

we obtain

\[
\boxed{
\sum_kL_k^{-3/2}
\int_{A_k}|c_k|^3dy<\infty.
}
\]

---

## 6. Adaptive weighted `L3` endpoint

Combining fluctuation and mean terms,

\[
\boxed{
\sum_k
L_k^{-3/2}
\int_{A_k}|U(y)|^3dy<\infty.
}
\]

By dyadic comparability of `L`, this is equivalent, up to constants, to

\[
\boxed{
\int_{|y|>R_0}
\frac{|U(y)|^3}{L(|y|)^{3/2}}dy<\infty.
}
\]

The bounded core is harmless, so

\[
\boxed{
\int_{\mathbb R^3}
\frac{|U(y)|^3}{L(e+|y|)^{3/2}}dy<\infty.
}
\]

This is the natural velocity-side image of the M5-540 adaptive vorticity moment.

---

## 7. Why this is stronger than all fixed `Lp`, `p>3`

For every fixed `epsilon>0`,

\[
L(r)=o(r^\epsilon).
\]

Hence the spatial loss `L(r)^(3/2)` grows more slowly than every positive power of `r`.

Thus the weighted `L3` statement lies strictly closer to the endpoint than any estimate obtained by replacing `3` with a fixed `p>3`.

It packages all of the power-subcritical radial information into one adaptive near-critical velocity norm.

---

## 8. Sparse-shell countermodel against weak-`L3`

The preceding estimate still does **not** imply

\[
U\in L^{3,\infty}.
\]

This can be seen at the same dyadic scaling level.

Because `L_k -> infinity`, choose a sparse sequence `k_n -> infinity` so rapidly that

\[
L_{k_n}\ge n^2 2^{2n}.
\]

Set

\[
m_{k_n}:=\frac{n}{L_{k_n}},
\qquad
m_k:=0
\quad\text{off the selected shells}.
\]

Then

\[
\sum_nm_{k_n}
\le
\sum_n\frac1{n2^{2n}}<\infty,
\]

but the critical shell amplitudes are

\[
\boxed{
b_{k_n}=L_{k_n}m_{k_n}=n\to\infty.
}
\]

Realize this sequence by smooth divergence-free shell bumps whose scale-normalized velocity amplitude on `A_(k_n)` is comparable to

\[
A_n:=b_{k_n}^{1/2}=n^{1/2}.
\]

The physical amplitude is `A_n/R_(k_n)` and the shell volume is `asymp R_(k_n)^3`.

At level

\[
\lambda_n\asymp\frac{A_n}{R_{k_n}},
\]

the weak-`L3` quantity obeys

\[
\lambda_n^3
|\{|U|>c\lambda_n\}|
\gtrsim
A_n^3
=n^{3/2}\to\infty.
\]

Thus the weak-`L3` quasi-norm diverges.

By choosing the radii still more sparsely, the same model can satisfy every fixed `Lp`, `p>3`, all fixed Sobolev tail requirements, and the adaptive weighted Dirichlet summability.

Therefore

\[
\boxed{
\text{adaptive weighted }L3
\not\Rightarrow
L^{3,\infty}.
}
\]

This is a function-space audit, not a Navier--Stokes counterexample.

---

## 9. Updated endpoint package

On the recurrent hard component we now have

\[
\boxed{
U\in\bigcap_{p>3}L^p,
}
\]

\[
\boxed{
U\notin L^3
\quad\nu\text{-a.e.},
}
\]

and additionally

\[
\boxed{
\int
\frac{|U(y)|^3}{L(e+|y|)^{3/2}}dy<\infty
}
\]

for one actual slowly varying loss `L` determined by the far-field modulus.

Thus the endpoint defect is narrower than the full class

\[
\bigcap_{p>3}L^p\setminus L^3,
\]

but it is still not a standard Lorentz endpoint.

---

## 10. DSD audit

Three implications must remain distinct:

1. M5-540 controls a weighted **vorticity moment**.
2. The `A2` audit and weighted Calderon--Zygmund transfer it to a weighted **Dirichlet velocity** estimate.
3. Dyadic Poincare and annular-mean control produce a weighted **velocity `L3`** estimate.

None of these steps converts the spatially varying loss `L(|y|)` into an amplitude-only Lorentz gauge.

The sparse-shell model shows why such a conversion would be false without additional PDE dynamics.

---

## 11. Highest-value next target

Since pure function-space improvement stops short of weak-`L3`, the next target should use the actual Navier--Stokes dynamics.

The remote dust already has vanishing instantaneous core velocity/strain influence by M5-534--535.

Because each generation/suspension roof has uniformly bounded similarity duration, the next calculation should integrate the remote Biot--Savart influence over one complete generation and prove

\[
\boxed{
\text{remote dust cumulative core action per generation}\to0
\quad(R\to\infty).
}
\]

If successful, all positive dual/ratchet/production marks can be localized to one finite-radius active core, leaving the adaptive endpoint tail as a dynamically passive spectator rather than a payer of the singular mechanism.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]