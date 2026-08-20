# Local Second-Order Solenoidal Gate — 2026-08-20

Status: **LOCAL CORE/TAIL BRIDGE STEP — GLOBAL REGULARITY NOT PROVED.**

This note combines the Bogovskii localization from `RADIUS_BARRIER_SCOPE_CORRECTION_2026-08-20.md` with the direct second-order solenoidal constant from `SECOND_ORDER_SOLENOIDAL_TEMPLE_BOUND_2026-08-20.md`.

Let `chi_R` equal one on `B_R`, vanish outside `B_{2R}`, and satisfy the usual derivative bounds

\[
|\nabla\chi_R|\lesssim R^{-1},
\qquad
|\nabla^2\chi_R|\lesssim R^{-2}.
\]

Let `b_R` be an annular Bogovskii correction and set

\[
v_R=\chi_R\omega-b_R.
\]

Then

\[
\nabla\cdot v_R=0,
\qquad
v_R=\omega\text{ on }B_R,
\qquad
\operatorname{supp}v_R\subset B_{2R}.
\]

## 1. Direct second-order uncertainty on the corrected core

For every compactly supported divergence-free field covered by the second-order estimate,

\[
M(v_R)\sqrt{D(v_R)}
\ge
\mathcal C_{2,sol}\,Z(v_R)^{3/2},
\]

where

\[
Z(v_R)=\|v_R\|_2^2,
\qquad
D(v_R)=\|\Delta v_R\|_2^2,
\]

and the rigorous explicit constant satisfies

\[
\mathcal C_{2,sol}\ge6.7199874273.
\]

Since `v_R` is supported in `B_{2R}`,

\[
M(v_R)\le4R^2 Z(v_R).
\]

Therefore

\[
4R^2Z(v_R)\sqrt{D(v_R)}
\ge
\mathcal C_{2,sol}Z(v_R)^{3/2}.
\]

Hence

\[
\boxed{
\|\Delta v_R\|_2
\ge
\frac{\mathcal C_{2,sol}}{4R^2}\|v_R\|_2.
}
\]

Because `v_R=omega` on `B_R`,

\[
\|v_R\|_2
\ge
\|\omega\|_{L^2(B_R)}.
\]

Thus

\[
\boxed{
\|\Delta v_R\|_2
\ge
\frac{1.6799968568}{R^2}
\|\omega\|_{L^2(B_R)}.
}
\]

## 2. Return to the original vorticity

The scale-invariant annular `W^{2,2}` Bogovskii estimate gives

\[
\|\Delta b_R\|_2
\le
C_B^{(2)}
\left(
R^{-1}\|\nabla\omega\|_{L^2(A_R)}
+R^{-2}\|\omega\|_{L^2(A_R)}
\right),
\]

where

\[
A_R=B_{2R}\setminus B_R.
\]

Expanding `Delta(chi_R omega)` gives

\[
\|\Delta(\chi_R\omega)\|_2
\le
\|\Delta\omega\|_{L^2(B_{2R})}
+C_\chi
\left(
R^{-1}\|\nabla\omega\|_{L^2(A_R)}
+R^{-2}\|\omega\|_{L^2(A_R)}
\right).
\]

Therefore, for one fixed localization constant `C_loc^(2)`,

\[
\boxed{
\|\Delta\omega\|_{L^2(B_{2R})}
+C_{loc}^{(2)}
\left(
R^{-1}\|\nabla\omega\|_{L^2(A_R)}
+R^{-2}\|\omega\|_{L^2(A_R)}
\right)
\ge
\frac{1.6799968568}{R^2}
\|\omega\|_{L^2(B_R)}.
}
\]

This is the localized second-order solenoidal gate.

## 3. H/T interpretation

Define normalized leakage ratios

\[
\varepsilon_0(R)
=
\frac{\|\omega\|_{L^2(A_R)}}
{\|\omega\|_{L^2(B_R)}},
\]

\[
\varepsilon_1(R)
=
R\frac{\|\nabla\omega\|_{L^2(A_R)}}
{\|\omega\|_{L^2(B_R)}}.
\]

Then

\[
R^2
\frac{\|\Delta\omega\|_{L^2(B_{2R})}}
{\|\omega\|_{L^2(B_R)}}
\ge
1.6799968568
-C_{loc}^{(2)}(\varepsilon_0+\varepsilon_1).
\]

Therefore a small-radius active core cannot simultaneously have

- negligible annular vorticity leakage;
- negligible annular derivative leakage;
- negligible normalized second-derivative cost.

In the existing proof tree these alternatives naturally map to

\[
\boxed{
\text{annular/core replacement leakage}\to T,
\qquad
\text{second-derivative leakage/concentration}\to H.
}
\]

The only non-`H/T` possibility is a compact core carrying a definite normalized second-order derivative cost.

## 4. Compact-core radius consequence

Suppose on a quantitative non-`H/T` compact class one has

\[
\|\Delta\omega\|_{L^2(B_{2R})}
\le
K_2\|\omega\|_{L^2(B_R)}
\]

and

\[
C_{loc}^{(2)}(\varepsilon_0+\varepsilon_1)\le\delta<1.6799968568.
\]

Then

\[
\boxed{
R^2
\ge
\frac{1.6799968568-\delta}{K_2}.
}
\]

Thus the active-core radius now has a genuine local lower bound depending only on the quantitative non-`H/T` derivative and leakage constants. No global vorticity second moment is required.

## 5. Next target

The next step is to obtain `K_2` and `delta` from the already established first-hitting analyticity and non-turnover parent-ball estimates. If those constants can be made explicit, the local radius floor above becomes numerical and can finally be compared with the active-core upper radius without any whole-field moment ambiguity.

Status: **A BOGOVSKII-CORRECTED ACTIVE CORE SATISFIES A SECOND-ORDER SOLENOIDAL GATE WITH EXPLICIT MAIN COEFFICIENT `1.6799968568/R^2`. A SMALL CORE MUST PAY THROUGH LOCAL SECOND-DERIVATIVE COST OR ANNULAR LEAKAGE, LINKING THE NEW UNCERTAINTY ESTIMATE DIRECTLY TO THE EXISTING `H/T` BRANCHES.**