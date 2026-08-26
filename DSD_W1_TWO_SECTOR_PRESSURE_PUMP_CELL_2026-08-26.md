# DSD W1 Two-Sector Pressure-Pump Cell

Date: 2026-08-26

Status: **THE RECURRENT AMPLITUDE PUMP IS REFINED TO A FINITE-CORE TWO-SECTOR CELL WITH FIXED PRESSURE GAP, NON-TANGENTIAL AMPLITUDE-LEVEL CROSSING, AND FIXED NORMALIZED SPATIAL SEPARATION / GLOBAL REGULARITY UNPROVED.**

## 1. Band area budget

On the strict interior amplitude band

\[
I_*=[\lambda_-,\lambda_+],
\]

let

\[
\Sigma_\lambda=\{|U|=\lambda\}.
\]

Coarea gives

\[
\int_{I_*}|\Sigma_\lambda|d\lambda
=
\int_{\{\lambda_-<|U|<\lambda_+\}}|\nabla|U||dY.
\]

The W1 finite-parent compact smooth bounds imply

\[
\boxed{
\int_{I_*}|\Sigma_\lambda|d\lambda\le S_*<\infty.
}
\]

## 2. Gain per surface area

The recurrent band gain satisfies

\[
\int_{I_*}
\bigl[J_P(\lambda)-\nu D_\lambda\bigr]d\lambda
\ge g_I>0.
\]

Hence there exists a regular level `lambda_* in I_*` such that

\[
\boxed{
\frac{J_P(\lambda_*)-\nu D_{\lambda_*}}
{|\Sigma_{\lambda_*}|}
\ge
\frac{g_I}{S_*}
=:j_*>0.
}
\]

In particular,

\[
\boxed{
J_P(\lambda_*)\ge j_*|\Sigma_{\lambda_*}|.
}
\]

## 3. Equal inflow and outflow flux

Let

\[
n_\lambda=\nabla|U|/|\nabla|U||.
\]

Incompressibility gives equal amplitude-level crossing fluxes

\[
Q_+=Q_-=:Q_\lambda.
\]

The pressure work is

\[
J_P(\lambda)
=Q_\lambda(\bar P_{in}-\bar P_{out}).
\]

On the compact parent ball, choose a gauge-safe pressure oscillation ceiling

\[
\operatorname{osc}P\le 2P_*.
\]

Then

\[
J_P\le2P_*Q_\lambda,
\]

so at the pump level

\[
\boxed{
Q_{\lambda_*}
\ge
\frac{j_*}{2P_*}|\Sigma_{\lambda_*}|.
}
\]

## 4. Non-tangential crossing

Since `|U|=lambda_*<=lambda_+` on the level surface,

\[
2Q_{\lambda_*}
=
\int_{\Sigma_{\lambda_*}}|U\cdot n_{\lambda_*}|dS
\le
\lambda_+
\int_{\Sigma_{\lambda_*}}
|n\cdot n_{\lambda_*}|dS.
\]

Therefore

\[
\boxed{
\frac1{|\Sigma_{\lambda_*}|}
\int_{\Sigma_{\lambda_*}}
|n\cdot n_{\lambda_*}|dS
\ge
c_{cross}:=
\frac{j_*}{P_*\lambda_+}>0.
}
\]

Thus the velocity field cannot be asymptotically tangent to the active amplitude boundary.

## 5. Fixed pressure gap and spatial separation

The previous pump lemma gives

\[
\boxed{
\bar P_{in}-\bar P_{out}\ge\Delta P_*>0.
}
\]

Hence there exist points in the inflow and outflow sectors whose pressures differ by at least `Delta P_*`.

Compact smoothness gives

\[
\|\nabla P\|_{L^\infty(B_{R_*})}
\le G_*.
\]

Therefore those sectors cannot collapse to the same point:

\[
\boxed{
\operatorname{dist}(\Sigma_{in},\Sigma_{out})
\ge
\frac{\Delta P_*}{G_*}
=:d_{sep}>0
}
\]

for appropriately chosen witness points/sectors.

## 6. DSD cell

The recurrent endpoint therefore contains a finite normalized pressure-pump cell with

- a strict interior amplitude level;
- nonzero inflow and outflow through the same amplitude boundary;
- a fixed pressure advantage on inflow;
- a fixed non-tangential crossing fraction;
- a fixed normalized separation between pressure sectors.

This is a substantially stronger finite-core witness than a pointwise pressure-gradient sign condition.

## 7. Limitation

The cell remains compatible with conservative pressure redistribution: positive pressure work inside the high-amplitude region can be offset by pressure recovery elsewhere. Its physical energy cost is subcritical under blow-up scaling. A final closure therefore still requires a genuinely critical nonrepeatability / gain theorem, not merely the existence of this cell.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
