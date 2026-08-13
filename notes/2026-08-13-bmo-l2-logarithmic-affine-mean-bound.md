# BMO + `L2` gives logarithmic control of the first-hitting affine mean strain

Date: 2026-08-13

Status: **DERIVED BMO/L2 MEAN BOUND + LOCAL SOURCE COROLLARY / DOES NOT CLOSE GLOBAL ENSTROPHY GROWTH**.

The first-hitting normalization gives

\[
\|\Omega\|_\infty\le1,
\]

and the strain is a zero-order Calderon--Zygmund transform of vorticity. Hence

\[
\|S\|_{BMO}\le C.
\]

BMO does not control additive constants, so the local affine mean `S_B` may still be large.  However, the global finite-`L2` strain condition fixes the additive constant at large scales.  Comparing nested averages gives a logarithmic upper bound on the local mean.

---

## 1. General nested-average estimate

Let

\[
f\in BMO(\mathbb R^3)\cap L^2(\mathbb R^3).
\]

For a ball `B_r=B_r(x0)` and dyadic enlargement

\[
B_{2^Nr},
\]

standard BMO mean comparison gives

\[
\boxed{
|f_{B_r}-f_{B_{2^Nr}}|
\le C N\|f\|_{BMO}.
}
\]

The large-ball mean satisfies

\[
\boxed{
|f_{B_R}|
\le |B_R|^{-1/2}\|f\|_2
\le C R^{-3/2}\|f\|_2.
}
\]

Therefore

\[
|f_{B_r}|
\le
C\|f\|_{BMO}\log\frac Rr
+C R^{-3/2}\|f\|_2
\]

for dyadic-comparable `R>=2r`.

---

## 2. Optimize the outer radius

Let

\[
B=\|f\|_{BMO}.
\]

When `B>0`, choose `R` so that the large-ball term is comparable to `B`, schematically

\[
R^{3/2}
\sim
\frac{\|f\|_2}{B},
\]

subject to `R>=2r`.

This yields

\[
\boxed{
|f_{B_r}|
\le
C B
\left[
1+
\log^+
\left(
\frac{\|f\|_2}
{B r^{3/2}}
\right)
\right].
}
\]

If `B=0`, then `f` is almost everywhere constant; `f in L2(R3)` forces that constant to be zero, so the same conclusion is trivial.

---

## 3. Apply to normalized strain

For the first-hitting strain,

\[
\|S\|_{BMO}
\le C\|\Omega\|_\infty
\le C.
\]

Also globally for divergence-free velocity,

\[
\boxed{
\|S\|_2^2
=\frac12\|\Omega\|_2^2.
}
\]

Hence on a fixed normalized ball,

\[
\boxed{
|S_{B_r}|
\le
C_r
\left[
1+\log^+(1+\|\Omega\|_2)
\right].
}
\]

For a unit normalized ball the radius dependence is absorbed into the constant:

\[
\boxed{
|S_B|
\lesssim
1+\log(1+\|\Omega\|_2).
}
\]

Thus the coherent local affine mean cannot grow faster than logarithmically in the global normalized vorticity `L2` norm while the normalized vorticity amplitude remains bounded by one.

---

## 4. Local stretching-source corollary

The previous BMO source reduction gives

\[
Q_B
=E_B\operatorname{tr}(S_BC_B)+R_B,
\qquad
|R_B|\le C|B|.
\]

Since

\[
E_B\le|B|\|\Omega\|_\infty^2\le|B|
\]

and

\[
\operatorname{tr}(S_BC_B)
\le\lambda_{\max}(S_B)
\le|S_B|,
\]

we obtain

\[
\boxed{
|Q_B|
\le
C|B|
\left[
1+\log(1+\|\Omega\|_2)
\right].
}
\]

A sharper version may replace `|S_B|` by the exact affine-covariance coupling envelope using `J_B` and the strain eigenvalues.

---

## 5. Inverse interpretation

If

\[
|S_B|\ge A\gg1,
\]

then the logarithmic estimate implies schematically

\[
\boxed{
\|\Omega\|_2
\gtrsim
\exp(cA)
}
\]

up to dimension/operator/radius constants.

Thus a very large coherent affine mean requires an exponentially larger normalized global enstrophy reservoir.

This is a genuine nonlocal price, although it is not by itself a contradiction because normalized global enstrophy may increase along a hypothetical singular sequence.

---

## 6. Time-integrated Jensen corollary

If the same estimate holds on a normalized time interval `I` of length `T`, then

\[
\|\Omega(s)\|_2
\gtrsim
\exp(c|S_B(s)|)-1.
\]

Convexity gives schematically

\[
\boxed{
\int_I\|\Omega(s)\|_2^2ds
\gtrsim
T\left[
\exp\left(
\frac{c}{T}
\int_I|S_B(s)|ds
\right)-1
\right].
}
\]

This converts accumulated affine deformation into a normalized global-enstrophy-time cost.

The physical kinetic-energy dissipation budget multiplies this normalized quantity by the appropriate natural-scale factor.  Because that factor shrinks as `W^{-1/2}`, this estimate alone does not yet make the sum over all amplification levels divergent.

---

## 7. Claim boundary

This logarithmic estimate does not restore global normalized enstrophy as a prerequisite for local compactness.  Local compactness still follows from first-hitting amplitude plus bounded affine/coefficient channels on fixed windows.

Its role is different:

\[
\boxed{
\text{large local affine mean}
\Longrightarrow
\text{large global normalized enstrophy reservoir}.
}
\]

The remaining proof question is whether repeated first-hitting amplification can pay this reservoir cost indefinitely while respecting the physical energy-dissipation and Cauchy I/V ledgers.

Status: **AFFINE-MEAN GROWTH LOGARITHMICALLY TIED TO GLOBAL ENSTROPHY / SUMMABILITY CLOSURE OPEN**.
