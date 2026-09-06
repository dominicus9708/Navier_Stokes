# DSD M17-301 — Logarithmic growing-lag Duhamel gate returns to a local forcing payment or parent-ceiling exit

Date: 2026-09-06  
Canonical ID: **M17-301**

Status: **GROWING-LAG REDUCTION GATE / M17-300 DOES NOT ACTUALLY REQUIRE COMPACTNESS TO APPLY DUHAMEL AT A LAG `T_j` DEPENDING ON `j`: FOR EACH FINITE `T_j`, THE LOCALIZED EQUATION GIVES AN EXACT BAND DUHAMEL IDENTITY. ON THE M17-299 SHELL-RELEVANT SUBSEQUENCE, `a_j >= c R_j^-2 (log R_j)^(-beta) (log log R_j)^(-1/2)`. IF THE M17-296 PARENT FIRST-HITTING ABSOLUTE AMPLITUDE CEILING `|W_j|<=C0` AND THE PARENT-TO-M17 SCALE MAP REMAIN VALID THROUGH THE BACKWARD INTERVAL, THEN `||f_j(-T_j)||_2 <= C/a_j <= C R_j^2 polylog(R_j)`. CHOOSING `T_j=A log R_j` WITH `A lambda_-^2>2`, THE NO-RECHARGE ANCESTOR ALTERNATIVE FROM M17-300 WOULD REQUIRE `||P_B f_j(-T_j)||_2 >= c R_j^(A lambda_-^2)`, WHICH EVENTUALLY EXCEEDS THE PARENT CEILING. HENCE EITHER THE PARENT CEILING/SCALE MAP EXITS BEFORE THE LOGARITHMIC LAG, OR THE WEIGHTED BAND FORCING ACTION IS AT LEAST A FIXED POSITIVE CONSTANT. THE EXPONENTIAL HEAT KERNEL THEN LOCALIZES THIS ACTION TO AT LEAST ONE RESCALED UNIT WINDOW WITH A FIXED UNWEIGHTED PROJECTED-FORCING ACTION. SPLITTING THE EXACT LOCALIZED FORCING RETURNS THIS TO COEFFICIENT/NONLINEAR RECHARGE, GRADIENT-INTERFACE LEAKAGE, OR MASS-INTERFACE LEAKAGE. THIS REMOVES GROWING-LAG COMPACTNESS AS AN INDEPENDENT OBSTRUCTION; THE NEXT FRONTIER IS TO CHARGE THESE LOCAL PAYMENTS TO A NONSUMMABLE GLOBAL/Genealogical BUDGET OR SHOW THAT REPEATED PAYMENTS CREATE A STRICT SUBSCALE/ANCESTOR GENEALOGY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs retained from M17-299 and M17-300

Let `R_j -> infinity` be the shell-relevant subsequence from M17-299.

For the selected scale-comparable packet, write its physical amplitude normalization as

\[
W_j=a_jV_j.
\]

M17-299 gives, for arbitrary fixed `epsilon>0`,

\[
\boxed{
a_j
\ge
c_aR_j^{-2}
(\log R_j)^{-\beta}
(\log\log R_j)^{-1/2},
}
\]

where

\[
\boxed{\beta=\frac43+\frac{\varepsilon}{2}.}
\]

M17-300 chooses a fixed compactly supported cutoff `chi` in the own-scale variable and sets

\[
\boxed{f_j=\chi V_j.}
\]

At the present rescaled time `tau=0`, a fixed Fourier annulus

\[
\mathcal B=\{\lambda_-\le |\xi|\le\lambda_+\}
\]

carries a fixed nonzero mass

\[
\boxed{
\|P_{\mathcal B}f_j(0)\|_2\ge c_B>0.
}
\]

The localized equation is exactly

\[
\boxed{
\partial_\tau f_j-\Delta f_j=F_j,
}
\]

with

\[
\boxed{
F_j
=\chi\mathcal N_j
-2\nabla\chi\cdot\nabla V_j
-(\Delta\chi)V_j.
}
\]

No cutoff or interface term is discarded.

---

## 2. Duhamel is exact for a `j`-dependent finite lag

M17-300 stated the band dichotomy first for fixed `T` because its surrounding compactness discussion was fixed-cylinder.

However the Duhamel identity itself has no fixed-`T` compactness requirement.

For every `j` and every finite backward lag `T_j>0` for which the same rescaled packet equation is defined,

\[
P_{\mathcal B}f_j(0)
=
e^{T_j\Delta}P_{\mathcal B}f_j(-T_j)
+
\int_{-T_j}^{0}
e^{-s\Delta}P_{\mathcal B}F_j(s)\,ds.
\]

On `mathcal B`,

\[
\|e^{T_j\Delta}P_{\mathcal B}g\|_2
\le
e^{-\lambda_-^2T_j}\|P_{\mathcal B}g\|_2.
\]

Define

\[
\boxed{
\mathfrak L_j(T_j)
:=
\int_{-T_j}^{0}
e^{-\lambda_-^2(-s)}
\|P_{\mathcal B}F_j(s)\|_2\,ds.
}
\]

Therefore

\[
c_B
\le
 e^{-\lambda_-^2T_j}
\|P_{\mathcal B}f_j(-T_j)\|_2
+
\mathfrak L_j(T_j).
\]

Hence for every finite `T_j`, either

\[
\boxed{
\mathfrak L_j(T_j)\ge\frac{c_B}{2},
}
\]

or

\[
\boxed{
\|P_{\mathcal B}f_j(-T_j)\|_2
\ge
\frac{c_B}{2}e^{\lambda_-^2T_j}.
}
\]

This dichotomy is an exact finite-`j` identity estimate, not a compactness statement.

---

## 3. Parent absolute-amplitude ceiling gives an ancestor norm ceiling

On the M17-296 parent first-hitting/analytic corridor, assume the same parent-to-M17 scale map remains valid and the absolute vorticity ceiling holds through the required backward interval:

\[
\boxed{|W_j(y,\theta)|\le C_0.}
\]

Because

\[
V_j=\frac{W_j}{a_j},
\qquad
f_j=\chi V_j,
\]

and `chi` has fixed compact support in the rescaled variable,

\[
\begin{aligned}
\|f_j(-T_j)\|_2
&\le
\|\chi\|_2\frac{C_0}{a_j}\\
&=:C_\chi\frac{C_0}{a_j}.
\end{aligned}
\]

Thus

\[
\boxed{
\|P_{\mathcal B}f_j(-T_j)\|_2
\le
C_*a_j^{-1},
}
\]

where `C_*:=C_chi C_0` is independent of `j`.

If the parent ceiling or the scale map fails before `-T_j`, record the explicit branch

\[
\boxed{G_{parent\ ceiling/scale\text{-}map\ exit}.}
\]

No ancestor ceiling is used beyond that branch.

---

## 4. Insert the M17-299 polynomial amplitude floor

From M17-299,

\[
a_j^{-1}
\le
C
R_j^2
(\log R_j)^{\beta}
(\log\log R_j)^{1/2}.
\]

Therefore, while the parent ceiling corridor remains valid,

\[
\boxed{
\|P_{\mathcal B}f_j(-T_j)\|_2
\le
C
R_j^2
(\log R_j)^{\beta}
(\log\log R_j)^{1/2}.
}
\]

The permitted normalized ancestor size is polynomial in the remote shell radius, up to polylogarithmic factors.

---

## 5. Choose the logarithmic lag

Fix a constant

\[
\boxed{A>\frac{2}{\lambda_-^2}.}
\]

Set

\[
\boxed{T_j:=A\log R_j.}
\]

Then the no-recharge ancestor alternative would give

\[
\begin{aligned}
\|P_{\mathcal B}f_j(-T_j)\|_2
&\ge
\frac{c_B}{2}
 e^{\lambda_-^2A\log R_j}\\
&=
\frac{c_B}{2}
R_j^{A\lambda_-^2}.
\end{aligned}
\]

But

\[
A\lambda_-^2>2,
\]

so

\[
R_j^{A\lambda_-^2}
\gg
R_j^2(\log R_j)^\beta(\log\log R_j)^{1/2}.
\]

Hence, for all sufficiently large `j`, the ancestor alternative contradicts the parent absolute-amplitude ceiling.

Therefore

\[
\boxed{
G_{parent\ ceiling/scale\text{-}map\ exit}
\ \lor\ 
\mathfrak L_j(T_j)\ge c_B/2.
}
\]

This is the logarithmic growing-lag reduction.

---

## 6. Physical-time translation and its audit

The rescaled lag

\[
T_j=A\log R_j
\]

corresponds to original similarity-time length

\[
\boxed{
\Delta\theta_j
=A r_j^2\log R_j.
}
\]

M17-299 only gives

\[
r_j^2\gtrsim(\log R_j)^{-1},
\]

so `Delta theta_j` need not tend to zero.

It may remain order one or grow.

Therefore the parent first-hitting ceiling and parent-to-M17 scale map must genuinely persist on this whole interval; this persistence is not inferred from fixed-cylinder compactness.

If it fails, that failure is retained as the explicit parent-corridor exit branch above.

---

## 7. The exponentially weighted action forces one unit-window action

Assume the parent corridor does not exit, so

\[
\mathfrak L_j(T_j)\ge c_B/2.
\]

Partition the backward rescaled interval into unit windows

\[
I_{j,n}:=[-(n+1),-n]
\]

for integers `n>=0` lying inside `[-T_j,0]`, with one possible final partial interval.

Define the unweighted projected forcing action

\[
\boxed{
A_{j,n}
:=
\int_{I_{j,n}}
\|P_{\mathcal B}F_j(s)\|_2\,ds.
}
\]

For `s in I_{j,n}`,

\[
e^{-\lambda_-^2(-s)}\le e^{-\lambda_-^2 n}.
\]

Hence

\[
\mathfrak L_j(T_j)
\le
\sum_{n\ge0}
e^{-\lambda_-^2n}A_{j,n}.
\]

If every unit-window action satisfied `A_{j,n}<delta_F`, then

\[
\mathfrak L_j(T_j)
<
\frac{\delta_F}{1-e^{-\lambda_-^2}}.
\]

Choose

\[
\boxed{
\delta_F
:=
\frac{c_B}{2}
\left(1-e^{-\lambda_-^2}\right).
}
\]

Therefore there must exist at least one index `n_j` such that

\[
\boxed{
A_{j,n_j}
\ge
\delta_F>0.
}
\]

Thus a logarithmically long weighted history cannot hide the recharge in infinitely many individually vanishing windows.

It returns to a fixed positive projected forcing action on one rescaled unit window.

---

## 8. Split the exact forcing on the payment window

Recall

\[
F_j
=\chi\mathcal N_j
-2\nabla\chi\cdot\nabla V_j
-(\Delta\chi)V_j.
\]

Since the Fourier projection is an `L2` contraction,

\[
\begin{aligned}
A_{j,n_j}
\le{}&
\int_{I_{j,n_j}}\|\chi\mathcal N_j\|_2\,ds\\
&+2\int_{I_{j,n_j}}
\|\nabla\chi\cdot\nabla V_j\|_2\,ds\\
&+\int_{I_{j,n_j}}
\|(\Delta\chi)V_j\|_2\,ds.
\end{aligned}
\]

Hence at least one of the following carries a fixed fraction of `delta_F`:

1. **coefficient/non-heat recharge**
   \[
   \boxed{
   \int_{I_{j,n_j}}\|\chi\mathcal N_j\|_2\,ds
   \ge\delta_F/3;
   }
   \]

2. **gradient-interface leakage**
   \[
   \boxed{
   2\int_{I_{j,n_j}}
   \|\nabla\chi\cdot\nabla V_j\|_2\,ds
   \ge\delta_F/3;
   }
   \]

3. **mass-interface leakage**
   \[
   \boxed{
   \int_{I_{j,n_j}}
   \|(\Delta\chi)V_j\|_2\,ds
   \ge\delta_F/3.
   }
   \]

These are typed payments, not an unclassified failure of compactness.

---

## 9. Convert interface action to positive spacetime cost

The unit-window length is at most one.

For the gradient-interface branch, Cauchy--Schwarz gives

\[
\int_{I_{j,n_j}}
\|\nabla\chi\cdot\nabla V_j\|_2\,ds
\le
\|\nabla\chi\|_\infty
\left(
\int_{I_{j,n_j}}
\int_{supp\nabla\chi}|\nabla V_j|^2
\right)^{1/2}.
\]

Therefore a fixed gradient-interface action forces

\[
\boxed{
\int_{I_{j,n_j}}
\int_{supp\nabla\chi}|\nabla V_j|^2
\ge c_{grad}>0.
}
\]

Likewise, the mass-interface branch forces

\[
\boxed{
\int_{I_{j,n_j}}
\int_{supp\Delta\chi}|V_j|^2
\ge c_{mass}>0.
}
\]

The constants depend only on the fixed cutoff and `c_B,lambda_-`, not on `j`.

Thus the band recharge is accompanied by a genuine local normalized spacetime cost unless the non-heat/coefficient term itself pays.

---

## 10. Correct logical upgrade of M17-300

The fixed-lag statement of M17-300 can therefore be sharpened on the M17-299 shell-relevant subsequence to

\[
\boxed{
H_{present\ fixed\ band}
\Longrightarrow
G_{parent\ ceiling/scale\text{-}map\ exit}
\lor
H_{unit\text{-}window\ coefficient/recharge\ payment}
\lor
H_{unit\text{-}window\ gradient\ interface\ payment}
\lor
H_{unit\text{-}window\ mass\ interface\ payment}.
}
\]

The exponentially larger ancestor branch is eliminated whenever the parent absolute-amplitude ceiling remains valid over the logarithmic lookback.

Crucially, this conclusion does **not** use compactness on a cylinder whose time length tends to infinity.

---

## 11. What has and has not been closed

### Closed as an independent obstruction

The statement

\[
\boxed{
\text{`T_j -> infinity prevents using the band Duhamel gate'}
}
\]

is no longer an independent obstruction.

Each `T_j=A log R_j` is finite, so the exact localized PDE identity applies directly.

### Still open

The resulting fixed local payment must still be connected to a globally finite or genealogically nonrepeatable quantity.

In particular, one still must prove at least one of:

1. repeated coefficient/non-heat recharge consumes a nonsummable global budget;
2. repeated gradient-interface payments consume physical palinstrophy/dissipation with nonsummable weights;
3. repeated mass-interface payments force strict packet migration, a smaller intrinsic scale, or a new ancestor node;
4. the parent ceiling/scale-map exit itself belongs to an already controlled payer family.

Without one of these, the payment can recur at different ancestor windows without immediate contradiction.

---

## 12. DSD analysis

### State separation

The present spectral witness, the parent absolute ceiling, and the historical forcing action are kept as distinct objects.

No single-time spectral statement is promoted to a history statement without Duhamel.

### Scale separation

Three scales/times are explicit:

- present own-scale packet radius `r_j`;
- remote shell radius `R_j`;
- logarithmic rescaled history `T_j=A log R_j`, corresponding to physical similarity time `A r_j^2 log R_j`.

### Payment typing

The surviving forcing is decomposed into coefficient/recharge, gradient-interface, and mass-interface components before any global-budget claim.

### Quantifier order

The constant `A` is chosen once with

\[
A\lambda_-^2>2,
\]

and only then `j -> infinity` is taken.

No `A=A_j` or hidden shell-dependent constant is used.

---

## 13. DSD audit

- **PASS:** the band Duhamel identity is valid for every finite `T_j`; no growing-cylinder compactness theorem is required for the identity itself.
- **PASS:** the M17-299 lower amplitude floor turns the parent normalized amplitude ceiling into `R_j^2 polylog(R_j)` growth.
- **PASS:** choosing fixed `A lambda_-^2>2` makes the no-recharge ancestor lower bound dominate that ceiling.
- **PASS:** the exponential kernel converts a fixed weighted history action into a fixed action on at least one unit rescaled window.
- **PASS:** cutoff/interface terms remain explicit and yield positive normalized spacetime costs when they carry the action.
- **CONDITIONAL:** eliminating the ancestor branch requires the M17-296 parent absolute-amplitude ceiling and parent-to-M17 scale map to remain valid throughout the physical lookback `A r_j^2 log R_j`.
- **OPEN:** a fixed normalized local payment has not yet been proved to consume a nonsummable **physical** global budget.
- **OPEN:** mass-interface payment may represent packet migration rather than dissipation and therefore needs a genealogy/return theorem.
- **OPEN:** coefficient/non-heat recharge must be matched to the exact M17 coefficient ledger before it can be globally charged.
- **NO CLAIM:** no unconditional global regularity theorem follows from M17-301.

---

## 14. Next canonical target

The next module should audit the repeated unit-window payer produced above.

A natural target is:

\[
\boxed{
\text{local projected-forcing payment}
\Longrightarrow
\text{physical budget payment}
\lor
\text{strict scale descent}
\lor
\text{ancestor migration with bounded multiplicity}.
}
\]

The required audit must preserve physical weights; normalized payments cannot simply be counted, in accordance with regression test R21.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
