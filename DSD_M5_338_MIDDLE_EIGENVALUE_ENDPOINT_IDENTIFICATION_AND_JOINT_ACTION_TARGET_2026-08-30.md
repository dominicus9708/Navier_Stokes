# DSD M5-338 — Middle-Eigenvalue Endpoint Identification / Joint-Action Target

Date: 2026-08-30

Status: **KNOWN SHARP REGULARITY ENDPOINT IDENTIFIED / DIVERGENCE OF `L_t^2 L_x^3` POSITIVE MIDDLE STRAIN IS NOT A CONTRADICTION / NEW INFORMATION IS THE SIMULTANEOUS ATOM-FORCED COMPRESSIVE ACTION AND THE INTERFACE BETWEEN PRODUCTIVE AND COMPRESSIVE SPECTRAL GEOMETRIES / GLOBAL REGULARITY UNPROVED.**

## 1. Known endpoint

For the 3D incompressible Navier–Stokes equation, the known strain-eigenvalue regularity criterion based on the positive part of the middle strain eigenvalue includes the critical pair

\[
\boxed{
\lambda_2^+\in L_t^2L_x^3.
}
\]

Thus finite

\[
\int_0^{T_*}\|\lambda_2^+(t)\|_3^2dt
\]

is a regularity condition, and a hypothetical finite-time blow-up may necessarily have this integral diverge.

Reference: Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569.

## 2. Audit consequence

Therefore the branch

\[
\int^{T_*}\|\lambda_2^+\|_3^2dt=\infty
\]

must **not** be labeled a contradiction.

The repository had independently recovered the same critical quantity from the enstrophy/Betchov ledger. This agreement is useful validation, but not closure.

## 3. What the atom analysis adds

The energy-atom/Oseen transfer gives the additional independent requirement

\[
\boxed{
\int^{T_*}\|S_-(t)\|_3^2dt=\infty.
}
\]

Hence an atom-compatible singular branch must carry the joint critical action

\[
\boxed{
\mathcal A_{joint}
:=
\int^{T_*}
\left(
\|\lambda_2^+(t)\|_3^2
+\|S_-(t)\|_3^2
\right)dt
=\infty.
}
\]

This is strictly more structural information than the known positive-middle criterion alone.

## 4. Why the two terms are geometrically different

`lambda_2^+` measures two-positive/one-negative strain geometry responsible for positive determinant/enstrophy production.

`S_-` measures the compressive spectral directions selected by positive Oseen production from an endpoint energy atom.

Thus a singular atom branch simultaneously needs

\[
\boxed{
\text{productive extensional geometry}
+\text{nonintegrable compressive geometry}.
}
\]

The relation between the two is not captured by either norm separately.

## 5. Correct next target

M5-334--337 show that when the productive and compressive populations differ in sign-pattern or planar structure, keeping both inside a common bounded parent forces a `lambda_2` interface and hence spatial-gradient or material pressure-curvature action.

Therefore the new target is not another scalar norm bound but a **joint organization theorem**:

\[
\boxed{
\mathcal A_{joint}=\infty
\Longrightarrow
H_{interface}\lor T_{separation}\lor C_{same-sector}.
}
\]

Here `C_same-sector` is the case where atom compression and productive middle strain are carried by the same two-positive/one-negative spectral population.

That same-sector branch is the next hard geometry.

## 6. Scope

This audit prevents a false proof step: known critical-norm divergence is necessary for blow-up and cannot itself be used to disprove blow-up.

The genuine gain from the atom machinery is the **simultaneous opposite-role strain demand**, not the rediscovery of the positive-middle criterion.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
