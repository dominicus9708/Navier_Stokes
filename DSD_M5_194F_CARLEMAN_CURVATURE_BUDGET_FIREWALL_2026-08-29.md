# DSD M5-194F — Carleman Curvature-Budget Firewall

Date: 2026-08-29

Parent: `DSD_M5_194E_LOG_CYLINDER_CONJUGATION_AND_BETA_ABSORPTION_LEDGER_2026-08-29.md`

Status: **NEGATIVE GLOBAL CURVATURE-ONLY FIREWALL / IF THE CARLEMAN SLOPE IS KEPT IN A FIXED COMPARABILITY BAND `beta/2 <= psi' <= 2 beta`, THEN A UNIFORM POSITIVE LOWER BOUND ON `psi''` CAN ONLY BE MAINTAINED OVER A FINITE LOG-RADIAL LENGTH FOR EACH FIXED `beta` / THEREFORE EXTRA CURVATURE CANNOT BY ITSELF PROVIDE A SINGLE GLOBAL UNIFORM ABSORPTION MARGIN FOR AN ARBITRARY NON-SMALL CRITICAL `1/r` DRIFT ON AN UNBOUNDED CYLINDER / SMALL-TAIL, FINITE-WINDOW, SUPPORT-DEPENDENT-WEIGHT, SKEWNESS, PDE-RIGIDITY, AND MATRIX/SYMMETRIZER BRANCHES REMAIN OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-194E

At the coefficient-ledger level, direct absolute-value absorption of the critical first-order tail requires a strict inequality of the schematic form

\[
C_{\rm Carl}|\Phi(y,\theta)|^2
<1+\psi''(y).
\]

The question is whether the right side can be made uniformly large simply by increasing the curvature of the logarithmic Carleman phase.

Assume the usual slope comparability band

\[
\boxed{
\frac12\beta\le\psi'(y)\le2\beta.
}
\]

This note audits the finite amount of positive curvature compatible with that band.

---

## 2. Finite slope budget

Take a log-radius interval

\[
I=[y_0,y_1],
\qquad
L:=y_1-y_0>0.
\]

If

\[
\psi''(y)\ge K>0
\qquad\text{for all }y\in I,
\]

then integration gives

\[
\psi'(y_1)-\psi'(y_0)
=
\int_{y_0}^{y_1}\psi''(y)\,dy
\ge KL.
\]

But the slope band implies

\[
\psi'(y_1)-\psi'(y_0)
\le
2\beta-\frac12\beta
=rac32\beta.
\]

Hence necessarily

\[
\boxed{
KL\le\frac32\beta.
}
\]

Equivalently,

\[
\boxed{
L\le\frac{3\beta}{2K}.
}
\]

This is the curvature-budget inequality.

---

## 3. Consequence for a non-small critical drift

Suppose the audited common tail obeys a lower-amplitude condition on the entire interval,

\[
|\Phi(y,\theta)|\ge M
\]

at least somewhere on every `y`-slice in a way that forces the direct pointwise absorption condition to use

\[
1+\psi''(y)
>
C_{\rm Carl}M^2.
\]

If

\[
C_{\rm Carl}M^2>1,
\]

then a sufficient uniform curvature requirement is

\[
\psi''(y)\ge K_M,
\qquad
K_M:=C_{\rm Carl}M^2-1>0.
\]

The curvature budget then yields

\[
\boxed{
L
<
\frac{3\beta}
{2(C_{\rm Carl}M^2-1)}.
}
\]

Thus, for each fixed `beta`, positive curvature strong enough to compensate for a non-small order-one tail can cover only a finite logarithmic radial length while the slope remains in the stated band.

---

## 4. Unbounded-cylinder firewall

Let the relevant endpoint geometry require one scalar weight with

\[
\frac12\beta\le\psi'\le2\beta
\]

on an unbounded interval in `y`.

If direct absorption of the tail requires a uniform positive curvature floor

\[
\psi''\ge K>0
\]

throughout that interval, then

\[
KL\le\frac32\beta
\]

fails as

\[
L\to\infty.
\]

Therefore

\[
\boxed{
\text{fixed slope band}
+
\text{unbounded log-cylinder}
+
\text{uniform non-small critical drift}
\not\Rightarrow
\text{global absorption by positive curvature alone}.
}
\]

More strongly: under these assumptions, a single scalar phase cannot maintain the required positive curvature floor for all log-radii.

---

## 5. The small-tail branch is qualitatively different

If

\[
C_{\rm Carl}\|\Phi\|_{L^\infty}^2<1,
\]

then the baseline `1` in

\[
1+\psi''
\]

may already supply the required strict margin, even with

\[
\psi''=0.
\]

Thus the curvature-budget obstruction does **not** apply to a sufficiently small dimensionless critical tail.

This sharpens the branch structure:

\[
\boxed{
\begin{array}{c|c}
\text{tail regime}&\text{direct scalar absorption status}\\
\hline
C|\Phi|^2<1&\text{potentially baseline-absorbable}\\
C|\Phi|^2>1&\text{needs extra curvature or structure}\\
\text{non-small on unbounded }y&\text{curvature-only global strategy fails under fixed slope band}
\end{array}
}
\]

The exact numerical threshold is theorem-dependent and has not been derived.

---

## 6. Why `beta -> infinity` does not erase the firewall automatically

For any fixed finite interval `L`, the budget

\[
KL\le\frac32\beta
\]

can be satisfied by choosing `beta` sufficiently large.

Therefore this note does **not** close finite-window Carleman arguments.

But for a single fixed `beta`, no finite value of `beta` permits a strictly positive curvature floor over an actually unbounded interval.

A proof may try to let the support window grow while also sending `beta` to infinity. That is a distinct two-parameter limiting architecture. It must control all constants and shell terms uniformly and is **not** ruled out here.

Hence the precise conclusion is a firewall against a **single global curvature-only weight**, not a no-go theorem for every support-dependent Carleman family.

---

## 7. Positive-curvature integral budget without pointwise monotonicity assumptions

The preceding estimate assumed the required lower bound

\[
\psi''\ge K>0
\]

throughout the target interval.

More generally, if one only tracks the net increase of the slope on any subinterval where `psi''` is nonnegative, then the total uncompensated positive curvature that can be accumulated without leaving the band is bounded by the same slope range.

However, large positive and negative oscillations of `psi''` could have a large positive part while keeping `psi'` bounded.

Such oscillation does not automatically help the present absorption problem because the direct margin is pointwise:

\[
1+\psi''(y)>C|\Phi(y,\theta)|^2.
\]

Where `psi''` becomes strongly negative, the coercive factor itself deteriorates and may even cease to be positive.

Therefore positive/negative curvature cancellation cannot satisfy a uniform positive lower-bound requirement.

---

## 8. Interaction with the structural branches

### Purely tangential divergence-free tail

If

\[
\Phi_r=0,
\]

then radial conjugation does not create the `beta Phi_r` potential, and incompressibility gives

\[
\operatorname{div}_{S^2}\Phi_\tau=0.
\]

The angular drift is then skew-adjoint on each sphere before the remaining commutators are considered.

If that skew structure can be retained in the full parabolic Carleman calculation, the direct absolute-value requirement

\[
C|\Phi_\tau|^2<1+\psi''
\]

may be unnecessarily strong.

Thus the curvature firewall increases the importance of the skewness branch rather than closing it.

### PDE-specific tail rigidity

If the canonical Type-I common tail can be shown to become small, tangential, or otherwise structured on the relevant cylinder, the non-small generic firewall may never be reached.

### Matrix/symmetrizer route

A matrix weight can potentially redistribute first-order drift and strain between components rather than asking one scalar curvature factor to dominate the entire operator norm.

That branch remains logically open.

---

## 9. DSD verdict

### CLOSED AT THIS LAYER

The following universal shortcut is closed:

\[
\boxed{
\text{Take an arbitrarily large positive }\psi''
\text{ everywhere and absorb any bounded critical drift,}
}
\]

while simultaneously keeping

\[
\frac12\beta\le\psi'\le2\beta
\]

on an unbounded log-radius interval for a fixed scalar weight.

The slope band gives a finite curvature budget.

### STILL OPEN

- sufficiently small dimensionless critical tail;
- finite log-radius windows with `beta` chosen relative to the window length;
- a two-parameter limit in which the support window and `beta` grow together with uniform constants;
- purely tangential/skew critical transport;
- nonradial approximate adaptation with a controlled residual;
- PDE-specific canonical-tail rigidity;
- matrix/vector symmetrization;
- a different endpoint backward-uniqueness theorem whose first-order coefficient class is genuinely critical without smallness.

---

## 10. Next audit target

The most economical surviving scalar branch is now the tangential/skew case.

The next calculation should assume

\[
\Phi_r=0,
\qquad
\operatorname{div}_{S^2}\Phi_\tau=0,
\]

retain the angular transport **without squaring it as an error**, and compute its exact commutator with the conjugated log-cylinder heat operator.

The decisive question is whether

\[
\Phi_\tau\cdot\nabla_{S^2}
\]

remains sufficiently skew after the Carleman symmetric/skew decomposition, or whether derivatives of `Phi_tau` recreate an order-one symmetric first-order obstruction.
