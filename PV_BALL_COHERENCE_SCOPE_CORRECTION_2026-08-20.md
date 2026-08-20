# Scope Correction for the Ball Coherence Formula — 2026-08-20

Overall status: **RIGOR AUDIT / LOCALIZATION CONDITION ADDED — GLOBAL REGULARITY NOT PROVED.**

This note corrects the scope of `PV_EXPLICIT_BALL_COHERENCE_CONSTANT_2026-08-20.md`.

The formula

\[
C_{coh}^{ball}
=\frac{36}{\pi^2}\frac{R^2P_\infty}{g_-^2}
\]

is a valid Poincare/eigenaxis-bending conversion **once a fixed-axis compatibility cap is available on the same localized object**.

However, the exact

\[
\lambda_{max}(\mathbb C)\le\frac23
\]

proved in `PV_GLOBAL_COMPATIBILITY_COVARIANCE_CAP_2026-08-20.md` is a whole-space statement for a globally compatible incompressible strain field. It cannot be inserted into an arbitrary raw core ball without localization error, because multiplication by a cutoff destroys exact strain compatibility/divergence-free structure.

Therefore the ball formula is to be read conditionally until the local compatibility projection is completed.

---

## Correct local target

Construct a divergence-free localized velocity `u_R` such that

- `u_R=u` on `B_R`;
- `u_R` is supported in `B_{2R}`;
- the correction is supported in the annulus `A_R=B_{2R}\\B_R`.

Set

\[
S_R=\operatorname{sym}\nabla u_R.
\]

The global compatibility cap then applies exactly to `S_R`:

\[
\lambda_{max}(\mathbb C[S_R])\le\frac23.
\]

Expanding `S_R` back into the original core plus correction terms must yield

\[
\boxed{
\text{core covariance alignment}
\le
\frac23
+
\mathcal E_{ann}(R),
}
\]

where `E_ann` depends only on annular velocity/strain/derivative leakage and localization derivatives.

If `E_ann` is small on the non-T/non-H branch, the `2/3` cap transfers to the core. If it is not small, the annulus itself supplies the required turnover/derivative defect.

---

## Status of the previous numerical examples

The example values of

\[
\delta_{cov}^{ball}(\chi)
\]

remain correct **conditional evaluations** of the coherence formula after a local compatibility cap has been established with sufficiently small annular error.

They are not yet unconditional local Navier--Stokes bounds.

---

Status: **WHOLE-SPACE `2/3` COMPATIBILITY IS RIGOROUS. THE BALL COHERENCE CONSTANT FORMULA IS RIGOROUS AS A POINCARE/BENDING STEP BUT ITS USE AS A LOCAL COVARIANCE GAP AWAITS A DIVERGENCE-FREE LOCALIZATION LEMMA WITH EXPLICIT ANNULAR ERROR.**