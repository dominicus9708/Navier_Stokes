# Scope Correction for the Solenoidal Radius Barrier — 2026-08-20

Overall status: **RIGOR AUDIT / SCOPE CORRECTION — GLOBAL REGULARITY NOT PROVED.**

This note corrects an over-strong interpretation in `FRONTIER_SOLENOIDAL_UNCERTAINTY_RADIUS_2026-08-20.md` and in the immediately preceding similarity-radius discussion.

The global solenoidal uncertainty estimate remains valid under its stated integrability hypotheses, but its rms radius is the radius of the **whole vorticity field**, not automatically the radius of the bounded active `P_V` core.

---

## 1. What remains valid

For a divergence-free whole-space vorticity field with

\[
Z=\|\omega\|_2^2<\infty,
\qquad
M_\omega=\int|x-X|^2|\omega|^2dx<\infty,
\qquad
D=\|\Delta\omega\|_2^2<\infty,
\]

Hamamoto's sharp 3D solenoidal uncertainty inequality gives

\[
M_\omega\|\nabla\omega\|_2^2
\ge\frac{25}{4}Z^2.
\]

Together with

\[
\|\nabla\omega\|_2^4\le ZD
\]

and the vorticity-Hessian production estimate

\[
\eta_{VI}
\le
\sqrt{\frac32}\,\|\omega\|_\infty\sqrt{\frac ZD},
\]

this yields

\[
\boxed{
\eta_{VI}
\le
\frac{2\sqrt6}{25}
\|\omega\|_\infty R_{\omega,\mathrm{global}}^2,
}
\]

where

\[
R_{\omega,\mathrm{global}}^2=M_\omega/Z.
\]

Thus, when the whole-space second moment is finite, a first-hitting threshold satisfies

\[
R_{\omega,\mathrm{global}}
\ge2.259005\sqrt\nu.
\]

This mathematical statement is retained.

---

## 2. What cannot yet be inferred

The non-`T` Type-I tower provides tightness of the **active threshold packet** in similarity variables. Its upper radius constant `c_+` controls the active/core sector.

The global rms radius above can instead be enlarged by a weak remote vorticity tail. Therefore

\[
R_{\omega,\mathrm{global}}
\ge2.259005\sqrt\nu
\]

does **not** imply

\[
R_{\omega,\mathrm{core}}
\ge2.259005\sqrt\nu.
\]

Consequently the previous proposed direct comparison

\[
c_+<2.259005\sqrt\nu
\]

is not by itself a contradiction unless one first proves global/core moment comparability.

Likewise, the earlier phrase that the active similarity orbit has a lower radius edge supplied directly by the global rms inequality is too strong without a tail-control lemma.

---

## 3. The ancient-limit issue is stronger

The restricted ancient limit is only known locally in the Type-I compactness topology together with a globally necessary low-vorticity critical tail.

Even when every finite first-hitting approximation has a finite weighted moment, the ancient limit need not inherit a uniform finite global second moment after rescaling.

Hence the correct global dichotomy is

\[
\boxed{
M_\Omega(\tau)<\infty
\quad\text{with a global radius barrier},
\qquad\text{or}\qquad
M_\Omega(\tau)=\infty
\quad\text{and the global barrier is vacuous}.
}
\]

An infinite or tail-dominated global moment is not automatically `H` or `T`, because a very remote low-vorticity tail can carry a large moment while remaining weak in direct core strain.

---

## 4. Local divergence-free replacement

A cutoff `chi_R omega` is not divergence-free. To recover the solenoidal improvement locally, choose a radial cutoff with

\[
\chi_R=1\text{ on }B_R,
\qquad
\chi_R=0\text{ outside }B_{2R},
\qquad
|\nabla\chi_R|\le c_\chi/R.
\]

On the annulus

\[
A_R=B_{2R}\setminus B_R,
\]

let `b_R` be a Bogovskii correction satisfying

\[
\nabla\cdot b_R
=\nabla\chi_R\cdot\omega,
\]

with zero trace on the annulus boundary and the scale-invariant estimates

\[
\|b_R\|_2
\le C_B c_\chi\|\omega\|_{L^2(A_R)},
\]

\[
\|\nabla b_R\|_2
\le
C_B c_\chi R^{-1}\|\omega\|_{L^2(A_R)}.
\]

Define

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

Hamamoto's inequality applied to `v_R` gives, because its support lies in `B_{2R}`,

\[
\boxed{
\|\nabla v_R\|_2^2
\ge
\frac{25}{16R^2}\|v_R\|_2^2
\ge
\frac{25}{16R^2}
\|\omega\|_{L^2(B_R)}^2.
}
\]

On the other hand,

\[
\|\nabla v_R\|_2
\le
\|\nabla\omega\|_{L^2(B_{2R})}
+C_{loc}R^{-1}\|\omega\|_{L^2(A_R)},
\]

where `C_loc` depends only on the fixed cutoff and the unit-annulus Bogovskii constant.

Therefore the localized solenoidal gate is

\[
\boxed{
\|\nabla\omega\|_{L^2(B_{2R})}
+C_{loc}R^{-1}\|\omega\|_{L^2(A_R)}
\ge
\frac5{4R}\|\omega\|_{L^2(B_R)}.
}
\]

Equivalently, if the annular leakage ratio is small,

\[
\frac{\|\omega\|_{L^2(A_R)}}
{\|\omega\|_{L^2(B_R)}}\le\varepsilon,
\]

then

\[
\boxed{
\|\nabla\omega\|_{L^2(B_{2R})}
\ge
\left(\frac54-C_{loc}\varepsilon\right)
\frac1R
\|\omega\|_{L^2(B_R)}.
}
\]

This is the correct local use of the solenoidal structure.

---

## 5. Updated branch structure

The radius argument now splits into three honest branches.

### A. Whole-space finite-moment branch

The global uncertainty barrier applies, and the stronger second-order solenoidal spectral estimate developed in the next note can be used.

### B. Tail-dominated or infinite-moment branch

The global radius lower bound is not useful. The task becomes proving that the tail is dynamically passive not only in direct strain but also in the vorticity-Hessian H1 production ledger.

### C. Localized active-core branch

Use the Bogovskii-corrected field `v_R`. Failure of the localized solenoidal inequality to be close to the whole-space constant must appear as either annular vorticity leakage or derivative cost. These are quantities that can be compared directly with the existing `T/H` bookkeeping.

---

## 6. Correct next target

The decisive radius target is therefore no longer simply to compute a numerical `c_+`.

The next required lemma is a **core-tail moment/production decoupling lemma** of one of the forms

\[
M_{tail}\le C M_{core},
\]

or

\[
|N_{tail}|\le\varepsilon(R)H,
\qquad
\varepsilon(R)\to0,
\]

or a localized Bogovskii inequality strong enough to route failure into `H/T`.

Only after such a bridge is established may a global radius lower bound be compared directly with the active-core upper radius.

---

Status: **THE SOLENOIDAL UNCERTAINTY CALCULATION IS RETAINED, BUT ITS `2.259005*sqrt(nu)` RADIUS IS A WHOLE-FIELD FINITE-MOMENT STATEMENT. DIRECT COMPARISON WITH THE ACTIVE-CORE `c_+` IS WITHDRAWN UNTIL GLOBAL/CORE MOMENT OR PRODUCTION DECOUPLING IS PROVED. A BOGOVSKII-CORRECTED LOCAL SOLENOIDAL GATE IS NOW THE RIGOROUS LOCAL REPLACEMENT.**