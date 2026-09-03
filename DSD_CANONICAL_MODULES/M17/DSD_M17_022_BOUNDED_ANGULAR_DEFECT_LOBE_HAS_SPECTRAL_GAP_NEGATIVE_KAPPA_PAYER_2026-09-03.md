# DSD M17-022 — Every bounded angular-defect lobe has a spectral-gap negative-kappa payer

Date: 2026-09-03
Canonical ID: **M17-022**

Status: **INTERNAL QUANTITATIVE PAYER UPGRADE / ON A BOUNDED CHI NODAL DOMAIN `Omega`, THE EXACT IDENTITY `int_Omega kappa chi^2 = -int_Omega |grad chi|^2` COMBINED WITH THE DIRICHLET POINCARE INEQUALITY GIVES `(<kappa>)_{chi^2,Omega} <= -lambda_1(Omega) < 0`. FABER-KRAHN THEN GIVES `lambda_1(Omega) >= C_FK |Omega|^{-2/3}` IN THREE DIMENSIONS. THEREFORE A BOUNDED RECURRENT LOBE WITH UNIFORMLY BOUNDED VOLUME CANNOT MAKE ITS DEFECT-WEIGHTED NEGATIVE KAPPA BUDGET ARBITRARILY WEAK. ON A COMPACT BRANCH UNIFORMLY SEPARATED FROM THE AXISYMMETRIC FIREWALL, THE FINITE ANGULAR-JET FLOOR ALSO GIVES A NONZERO CHI-MASS FLOOR, SO THE NEGATIVE DEFECT PAYER HAS A FIXED ABSOLUTE LOWER BOUND. THIS STRENGTHENS M17-018/020 FROM SIGN TO QUANTITATIVE COERCIVITY BUT STILL DOES NOT EXCLUDE A REGULAR TURNOVER CYCLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Bounded defect lobe

Let `Omega` be a bounded connected nodal domain of `chi` at a fixed similarity time:

\[
\chi\ne0\quad\text{in }\Omega,
\qquad
\chi=0\quad\text{on }\partial\Omega.
\]

M17-018 gives

\[
\boxed{
\int_\Omega\kappa\chi^2
=-\int_\Omega|\nabla\chi|^2.
}
\]

---

## 2. Dirichlet spectral gap

Because `chi` vanishes on the lobe boundary,

\[
\chi\in H_0^1(\Omega)
\]

under the retained regularity assumptions.
Let `lambda_1(Omega)` be the first Dirichlet eigenvalue of `-Delta` on `Omega`.
Then

\[
\boxed{
\int_\Omega|\nabla\chi|^2
\ge
\lambda_1(\Omega)
\int_\Omega\chi^2.
}
\]

Therefore

\[
\boxed{
\int_\Omega\kappa\chi^2
\le
-\lambda_1(\Omega)
\int_\Omega\chi^2.
}
\]

Equivalently, the defect-weighted lobe mean satisfies

\[
\boxed{
\langle\kappa\rangle_{\chi^2,\Omega}
:=
\frac{\int_\Omega\kappa\chi^2}
{\int_\Omega\chi^2}
\le
-\lambda_1(\Omega)<0.
}
\]

Thus a bounded lobe has a strict spectral negative bias, not merely a sign-changing potential.

---

## 3. Positive/negative charge form

Using the M17-018 notation,

\[
D_{-,\Omega}-D_{+,\Omega}
=\int_\Omega|\nabla\chi|^2.
\]

Hence

\[
\boxed{
D_{-,\Omega}-D_{+,\Omega}
\ge
\lambda_1(\Omega)
\|\chi\|_{L^2(\Omega)}^2.
}
\]

In particular,

\[
\boxed{
D_{-,\Omega}
\ge
D_{+,\Omega}
+\lambda_1(\Omega)\|\chi\|_2^2.
}
\]

The negative side must exceed the positive side by a coercive gap.

---

## 4. Faber-Krahn geometric lower bound

In three dimensions, the Faber-Krahn inequality gives

\[
\boxed{
\lambda_1(\Omega)
\ge
C_{FK}|\Omega|^{-2/3},
}
\]

where `C_FK` is the universal constant attained by a ball of the same volume.

Therefore

\[
\boxed{
\langle\kappa\rangle_{\chi^2,\Omega}
\le
-C_{FK}|\Omega|^{-2/3}.
}
\]

For a recurrent bounded-lobe class with

\[
|\Omega(\theta)|\le V_{max}<\infty,
\]

we obtain the uniform estimate

\[
\boxed{
\langle\kappa\rangle_{\chi^2,\Omega(\theta)}
\le
-C_{FK}V_{max}^{-2/3}<0.
}
\]

Thus bounded recurrence cannot weaken the defect-weighted negative bias to zero by slowly flattening `kappa`.

---

## 5. Maximum-point consequence

Let `x_*` be an interior point where `|chi|` attains its maximum in a bounded lobe.
After replacing `chi` by `-chi` if necessary, assume

\[
\chi(x_*)>0.
\]

Then

\[
\nabla\chi(x_*)=0,
\qquad
\Delta\chi(x_*)\le0.
\]

Since

\[
\Delta\chi=\kappa\chi,
\]

we have

\[
\boxed{
\kappa(x_*)\le0.
}
\]

Therefore the amplitude maximum of every bounded defect lobe lies on the nonpositive side of the kappa landscape.

If the maximum is nondegenerate in trace, then

\[
\kappa(x_*)<0.
\]

The exceptional flat case `kappa(x_*)=0` is a higher-jet maximum and belongs to a finite analytic jet classification rather than an unrestricted escape.

---

## 6. Compact non-axisymmetric branch gives an absolute payer floor

On a compact branch uniformly separated from the axisymmetric firewall, M17-016/019 give

1. a uniformly finite first nonzero angular order `m <= m_A^*`;
2. a nonzero angular-jet coefficient floor;
3. uniform higher-derivative bounds.

Therefore one can choose a fixed small core neighborhood in at least one core-emergent lobe where

\[
\boxed{
\int\chi^2
\ge M_{\chi,*}>0
}
\]

uniformly on the separated branch.

If the corresponding recurrent bounded global lobe also satisfies

\[
|\Omega|\le V_{max},
\]

then

\[
\boxed{
D_{-,\Omega}-D_{+,\Omega}
\ge
C_{FK}V_{max}^{-2/3}M_{\chi,*}
=:Q_{\chi,*}>0.
}
\]

Thus non-axisymmetry itself carries a fixed negative payer floor as long as the branch remains both localized and uniformly separated from the firewall.

---

## 7. Relation to M17-012

M17-012 supplied a fixed negative payer in the enstrophy measure

\[
|W|^2dx.
\]

M17-022 supplies, on bounded non-axisymmetric lobes, a fixed negative payer in the shape measure

\[
\chi^2dx.
\]

The two quantitative bounds need not be numerically equal.
But the survivor must support both simultaneously in

\[
\boxed{\{\kappa<0\}.}
\]

This removes the possibility that the angular defect uses only an arbitrarily weak negative tail while the enstrophy payer is carried elsewhere.
For a uniformly localized separated lobe, the shape payer itself remains finite and coercive.

---

## 8. Relation to lobe turnover

M17-020 gives for a recurrent bounded lobe

\[
\boxed{
\left\langle
s\int_{\partial\Omega_s}\frac{T}{|\nabla\chi|}
\right\rangle
=\frac32\langle|\Omega_s|\rangle.
}
\]

M17-022 adds the interior requirement

\[
\boxed{
\langle\kappa\rangle_{\chi^2,\Omega_s}
\le
-C_{FK}|\Omega_s|^{-2/3}.
}
\]

Thus a recurrent bounded lobe must simultaneously maintain

1. a strictly negative interior spectral budget;
2. a strictly signed boundary material-turnover budget.

The two requirements are independent and both coercive.

---

## 9. DSD interpretation

### 9.1 Geometry controls sign magnitude
The spatial size of a defect lobe controls how negative its `chi^2`-weighted multiplier must be.
This is a direct geometry-to-dynamics describability relation.

### 9.2 Firewall separation becomes quantitative
A branch that remains a fixed distance from `chi=0` in a compact jet topology cannot send its defect payer continuously to zero.
To lose the payer it must either

- approach the axisymmetric firewall;
- delocalize/unbound the lobe;
- lose regular nodal-domain geometry.

### 9.3 Interior and boundary budgets
The lobe now has both an interior coercive quantity and a boundary turnover current.
This gives a more rigid state description for the next recurrence audit.

---

## 10. DSD audit

### Audit A — using Poincare on unbounded lobes
Rejected.
The spectral-gap conclusion is for bounded Dirichlet nodal domains.

### Audit B — claiming a universal absolute payer without a chi-mass floor
Rejected.
The absolute constant `Q_chi,*` additionally uses uniform separation from the firewall and compact jet bounds.

### Audit C — maximum point implies strict kappa<0 in every case
Rejected.
A flat analytic maximum may have `kappa=0`; this is a finite higher-jet exception.

### Audit D — identifying the spectral gap with blow-up
Rejected.
It is a quantitative compatibility condition for a regular lobe.

### Audit E — proof status
Global regularity remains unproved.

---

## 11. Updated bounded-lobe survivor

A localized recurrent non-axisymmetric lobe separated from the firewall must satisfy

\[
\boxed{
\begin{aligned}
D_{-,\Omega}-D_{+,\Omega}
&\ge Q_{\chi,*}>0,\\
\left\langle
s\int_{\partial\Omega_s}\frac{T}{|\nabla\chi|}
\right\rangle
&=\frac32\langle|\Omega_s|\rangle>0.
\end{aligned}
}
\]

Thus neither its interior negative payer nor its boundary turnover can disappear in the recurrent limit.

---

## 12. Next target

The remaining question is whether the two persistent budgets can be sustained while the internal `kappa=0` transition remains uniformly transverse to the angular boundary.

The next useful geometric reduction is to exploit the fact that

\[
\kappa=F_q(q,x_3)
\]

so regular horizontal `kappa=0` sets are `q`-level curves, and double zeros `chi=kappa=0` acquire a direct radial-extremum interpretation.

This is the **Kappa-Contour Geometry Gate (KCGG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
