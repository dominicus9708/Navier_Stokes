# Localized Tightrope / Passive Remote-H Audit — 2026-08-23

Status: **EXACT LOCALIZED ALGEBRA + BRANCH PRUNING FRAMEWORK — GLOBAL REGULARITY NOT PROVED.**

This note addresses the passive part of `H_remote`. The whole-space smooth tightrope ledger uses global derivative norms, so derivative mass at very large normalized radius can change `P/E` and `H/P` even when it has negligible dynamical effect on the first-hitting core. The purpose here is to localize the ledger and identify exactly how exterior information can enter.

The result is an exact cutoff identity. A complete closure still requires quantitative bounds on the cutoff errors and far-field pressure/strain terms, but passive exterior derivative mass no longer enters as a naked whole-space norm.

## 1. Normalized strain equation

Use the smooth first-hitting normalization with fixed reference center `X0`:

\[
y=M^{1/2}(x-X_0),
\qquad
\frac{ds}{dt}=M,
\qquad
S=M\Sigma,
\qquad
u>0.
\]

With

\[
b=(\log M)_s,
\]

the normalized strain equation may be written

\[
\boxed{
\Sigma_s
+U\cdot\nabla\Sigma
+\frac b2 y\cdot\nabla\Sigma
+b\Sigma
-\nu\Delta\Sigma
=\mathcal R_0,
}
\]

where `R0` denotes the normalized non-transport strain forcing (quadratic velocity-gradient terms plus the pressure Hessian, in the usual trace-free strain equation).

The normalization coefficients are fixed by the exact global identities already recorded in `SMOOTH_FINITE_STAGE_TIGHTROPE_LEDGER_2026-08-20.md`.

## 2. Compact core packet

Choose a smooth time-independent cutoff in normalized coordinates

\[
\chi\in C_c^\infty(\mathbb R^3),
\qquad
0\le\chi\le1,
\]

with `chi=1` on a core ball and support in a slightly larger parent ball. Set

\[
\boxed{F=\chi\Sigma.}
\]

Then a direct product-rule calculation gives

\[
\boxed{
F_s
+U\cdot\nabla F
+\frac b2 y\cdot\nabla F
+bF
-\nu\Delta F
=
\chi\mathcal R_0+\mathcal C_\chi,
}
\]

where the entire cutoff commutator is

\[
\boxed{
\mathcal C_\chi
=
\left(U+\frac b2y\right)\cdot\nabla\chi\,\Sigma
-
u\left[
2\nabla\chi\cdot\nabla\Sigma
+(\Delta\chi)\Sigma
\right].
}
\]

Thus `C_chi` is supported only where `grad chi` or `Delta chi` is nonzero: the parent-buffer annulus.

## 3. Local L2 ledger

Define

\[
E_\chi=\|F\|_2^2,
\qquad
P_\chi=\|\nabla F\|_2^2,
\qquad
H_\chi=\|\Delta F\|_2^2.
\]

Because `div U=0` and `F` is compactly supported,

\[
\langle U\cdot\nabla F,F\rangle=0.
\]

Also

\[
\left\langle y\cdot\nabla F,F\right\rangle
=-\frac32E_\chi.
\]

Therefore

\[
\boxed{
\frac12(E_\chi)_s
+\frac14bE_\chi
+\nu P_\chi
=A_\chi+e_{0,\chi},
}
\]

where

\[
A_\chi
:=\langle\chi\mathcal R_0,F\rangle,
\qquad
 e_{0,\chi}
:=\langle\mathcal C_\chi,F\rangle.
\]

The `b/4` coefficient is exactly the global first-hitting L2 coefficient; localization changes only the explicit annular commutator.

## 4. Local H1 ledger

Multiply the packet equation by `-Delta F` and integrate. For the dilation term,

\[
\langle y\cdot\nabla F,-\Delta F\rangle
=-\frac12P_\chi.
\]

The divergence-free transport is no longer zero at H1 order and belongs to the H1 production. Define

\[
N_\chi
:=
\left\langle
\chi\mathcal R_0-U\cdot\nabla F,
-\Delta F
\right\rangle,
\]

and

\[
e_{1,\chi}
:=
\langle\mathcal C_\chi,-\Delta F\rangle.
\]

Then

\[
\boxed{
\frac12(P_\chi)_s
+\frac34bP_\chi
+\nu H_\chi
=N_\chi+e_{1,\chi}.
}
\]

Again the scaling coefficient `3b/4` is the same as in the whole-space smooth ledger.

## 5. Exact localized cross-order identity

Assume `E_chi>0` and `P_chi>0`. Subtract the logarithmic L2 ledger from the logarithmic H1 ledger. With

\[
\chi_{loc}:=P_\chi/E_\chi,
\]

one obtains

\[
\boxed{
\begin{aligned}
\frac12(\log\chi_{loc})_s
+\frac12b
+\nu\left(
\frac{H_\chi}{P_\chi}
-
\frac{P_\chi}{E_\chi}
\right)
&=
\frac{N_\chi}{P_\chi}
-
\frac{A_\chi}{E_\chi}\\
&\quad+
\frac{e_{1,\chi}}{P_\chi}
-
\frac{e_{0,\chi}}{E_\chi}.
\end{aligned}
}
\]

Since `F` is compactly supported,

\[
P_\chi^2
=\langle-\Delta F,F\rangle^2
\le E_\chi H_\chi,
\]

so

\[
\boxed{
\frac{H_\chi}{P_\chi}
-
\frac{P_\chi}{E_\chi}
\ge0.
}
\]

Thus the favorable viscous spectral-gap sign survives localization exactly.

## 6. What exterior derivative mass can and cannot do

The naked exterior quantity

\[
\int_{|y|\gg1}|\nabla\Omega|^2dy
\]

does **not** occur anywhere in the localized identity.

Exterior information can enter the core packet only through four typed channels:

1. **annular material/advection flux** in
   \[
   (U\cdot\nabla\chi)\Sigma;
   \]
2. **annular scale-drift flux** in
   \[
   \frac b2(y\cdot\nabla\chi)\Sigma;
   \]
3. **annular viscous derivative leakage** in
   \[
   -\nu[2\nabla\chi\cdot\nabla\Sigma+(\Delta\chi)\Sigma];
   \]
4. **actual nonlocal influence inside the core**, principally far-field strain/velocity and harmonic pressure Hessian contained in the local values entering `R0` and `U`.

The first three are explicit cutoff-buffer terms. A fixed positive amount of them is a material/boundary/derivative leakage event and belongs to the existing `T/H` bookkeeping.

The fourth is not passive: if far-field vorticity supplies fixed positive core strain action, it belongs to the **active remote-H** lane quantified in `REMOTE_H_ACTIVE_STRAIN_ENSTROPHY_AMPLIFICATION_2026-08-23.md`; far harmonic pressure is already subject to the finite parent-pressure escalation gate.

## 7. Passive remote-H pruning statement

Define a remote derivative reservoir to be **passive relative to the chosen core packet** when, on a stage,

- its induced far-field strain/velocity contribution to the local production is below the chosen small interaction threshold;
- its far harmonic pressure contribution is below the pressure threshold;
- the cutoff-buffer errors satisfy the low-turnover/leakage threshold.

Then arbitrarily large derivative mass outside the parent support has no direct term in the localized cross-order equation.

Consequently

\[
\boxed{
H_{remote}^{passive}
\text{ is not an independent obstruction to the localized tightrope ledger.}
}
\]

If such a reservoir changes the local proof by an order-one amount, by definition it has ceased to be passive and must enter one of the explicit interaction channels above.

This is a proof-tree pruning statement, not a proof that passive derivative mass cannot exist in the full solution.

## 8. Finite-stage integrated form

On one geometric stage, `int b ds=log q`, so

\[
\boxed{
\begin{aligned}
&\frac12\log\frac{\chi_{loc}(s_1)}{\chi_{loc}(s_0)}
+\frac12\log q\\
&\quad+
\nu\int_I
\left(
\frac{H_\chi}{P_\chi}
-
\frac{P_\chi}{E_\chi}
\right)ds\\
&=
\int_I
\left(
\frac{N_\chi}{P_\chi}
-
\frac{A_\chi}{E_\chi}
\right)ds
+
\int_I
\left(
\frac{e_{1,\chi}}{P_\chi}
-
\frac{e_{0,\chi}}{E_\chi}
\right)ds.
\end{aligned}
}
\]

The next quantitative target is to choose the cutoff buffer from the existing moving-ball / parent-core geometry and bound the last integral by the same explicit `T/H/pressure` thresholds already used elsewhere in the repository.

## 9. Updated System-I interpretation

After combining this localized identity with the active-strain amplification lemma:

\[
\boxed{
H_{remote}
\Longrightarrow
\begin{cases}
\text{passive exterior mass: removable from the local ledger},\\
\text{active remote strain: }R^{7/5}\text{ enstrophy amplification},\\
\text{large annular commutator: }T/H,\\
\text{large far pressure: finite parent-pressure routing}.
\end{cases}
}
\]

The remaining genuinely new `H_remote` survivor is therefore a **contracting dynamically active halo** whose physical radius approaches the first-hitting point rapidly enough to evade the global energy packing threshold while avoiding explicit shell turnover.

Status: **PASSIVE REMOTE DERIVATIVE MASS IS REMOVED AS A NAKED WHOLE-SPACE-NORM OBSTRUCTION BY AN EXACT LOCALIZED CROSS-ORDER LEDGER. THE ONLY NEW REMOTE-H SURVIVOR IS A RAPIDLY CONTRACTING, DYNAMICALLY ACTIVE HALO, MODULO QUANTITATIVE CUTOFF-ERROR MATCHING. GLOBAL REGULARITY IS NOT PROVED.**
