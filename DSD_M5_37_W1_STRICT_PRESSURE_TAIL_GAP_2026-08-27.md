# DSD M5-37 — W1 Strict Pressure-Tail Gap at a Positive Defect First Hit

Date: 2026-08-27

Status: **DERIVED W1-SPECIFIC STRICT GAP / A POSITIVE DEFECT FIRST HIT FORCES THE PRESSURE-TAIL DENSITY A FIXED ADDITIVE AMOUNT BEYOND THE MINIMAL VISCOUS THRESHOLD / NOT YET A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

## 1. Threshold notation

For a regular amplitude level `lambda`, let

\[
\Sigma_\lambda=\{|V|=\lambda\},
\qquad a=|V|.
\]

Write the nonsmooth threshold dissipation as

\[
\boxed{
D_\lambda^{surf}
=A(\lambda)+\lambda B(\lambda),
}
\]

where

\[
A(\lambda)
:=
\int_{a>\lambda}|\nabla V|^2dz,
\]

and

\[
B(\lambda)
:=
\int_{\Sigma_\lambda}|\nabla a|dS.
\]

Define the pressure tail

\[
Q_P(\lambda)
:=
\int_{a>\lambda}|\Pi|^2dz.
\]

## 2. Sharper surface Cauchy--Schwarz

On `Sigma_lambda`, `|V|=lambda`. Keep the crossing angle rather than discarding it:

\[
J_P(\lambda)
=
\int_{\Sigma_\lambda}
\Pi\,V\cdot n_\lambda\,dS.
\]

Then

\[
\begin{aligned}
|J_P(\lambda)|^2
&\le
\left(
\int_{\Sigma_\lambda}
\frac{|\Pi|^2}{|\nabla a|}dS
\right)
\left(
\int_{\Sigma_\lambda}
(V\cdot n_\lambda)^2|\nabla a|dS
\right)\\
&\le
[-Q_P'(\lambda)]
\lambda^2B(\lambda).
\end{aligned}
\]

Since

\[
\lambda B(\lambda)
=D_\lambda^{surf}-A(\lambda),
\]

we obtain

\[
\boxed{
|J_P(\lambda)|^2
\le
\lambda[-Q_P'(\lambda)]
\left(
D_\lambda^{surf}-A(\lambda)
\right).
}
\]

This is sharper than the M5-34 estimate because it retains the positive bulk active-set gradient term `A(lambda)` outside the surface payer.

## 3. Positive active bulk-gradient floor from a defect first hit

On the normalized W1 first-hit class, the high-amplitude excess is supported in a fixed phase cell and has a fixed positive entropy/excess size.

Let

\[
g=(a-\lambda)_+.
\]

The fixed amplitude ceiling and fixed support volume convert a positive threshold-excess lower bound into

\[
\|g\|_{L^2}\ge c_g>0.
\]

Since `g` vanishes outside the fixed active cell, Poincare/Sobolev gives

\[
\int|\nabla g|^2dz
\ge c_A>0.
\]

But on `a>lambda`,

\[
|\nabla g|=|\nabla a|
\le |\nabla V|.
\]

Hence

\[
\boxed{
A(\lambda)
\ge A_*>0
}
\]

uniformly on the fixed positive defect first-hit class.

The constant depends on the fixed first-hit excess level and the retained W1 phase-cell compactness data, not on the physical threshold scale.

## 4. First-hit pressure-tail gap

At a first hit of the threshold entropy,

\[
\partial_tE_\lambda\ge0.
\]

The threshold ledger therefore gives

\[
J_P(\lambda)
\ge
\nu D_\lambda^{surf}.
\]

Combining with the sharper Cauchy estimate,

\[
\nu^2(D_\lambda^{surf})^2
\le
\lambda[-Q_P'(\lambda)]
(D_\lambda^{surf}-A(\lambda)).
\]

Thus

\[
\lambda[-Q_P'(\lambda)]
\ge
\nu^2
\frac{(D_\lambda^{surf})^2}
{D_\lambda^{surf}-A(\lambda)}.
\]

Use the algebraic identity

\[
\frac{D^2}{D-A}
=D+A+\frac{A^2}{D-A}
\ge D+A.
\]

Therefore

\[
\boxed{
\lambda[-Q_P'(\lambda)]
\ge
\nu^2D_\lambda^{surf}
+
\nu^2A(\lambda)
\ge
\nu^2D_\lambda^{surf}
+
\nu^2A_*.
}
\]

## 5. Meaning of the strict gap

M5-34 gave the minimal condition

\[
\lambda[-Q_P']
\gtrsim
\nu^2D_\lambda^{surf}
\]

for pressure work to compete with viscosity.

M5-37 shows that a **fixed positive W1 defect first hit cannot merely sit at this minimal threshold**. The positive bulk gradient content forces an additive excess:

\[
\boxed{
\text{pressure-tail density}
\ge
\text{minimal viscous threshold}
+
\text{fixed W1 margin}.
}
\]

This is a genuinely W1-specific strengthening of the generic pressure--velocity criterion.

## 6. DSD interpretation

The amplitude-state boundary payer and the interior active-set structure cannot be completely decoupled. A positive defect carries nonzero interior gradient formation, and that interior amount removes part of the surface dissipation from the pressure-flux Cauchy payer.

Consequently the pressure tail must overcompensate not only viscosity but also the interior formation floor.

## 7. What this does not yet prove

The quantity

\[
\lambda[-Q_P'(\lambda)]
\]

is itself scale critical. The classical finite-energy inequality does not provide a finite spacetime budget for a fixed normalized amount at infinitely many nested thresholds.

Thus the strict additive gap is not yet a contradiction.

A closing theorem would need to show that such fixed-gap pressure-tail first hits cannot recur through arbitrarily large physical thresholds, or that the W1 pressure-Poisson geometry forces a smaller pressure tail than the new lower bound.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
