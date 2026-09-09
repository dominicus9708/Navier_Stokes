# M17-471 — Zero-level strain trace collapses to raw-H2 plus palinstrophy under the shared zero-tube/trace compactness package

**Date:** 2026-09-10  
**Status:** ACTIVE TRACE ABSORPTION / RAW-H2 + PALINSTROPHY REDUCTION

## 1. Scope

M17-460 isolated the zero-level strain trace
\[
C_{0\sigma}
=
\int_{\{\kappa=0\}}\rho^2\partial_n\sigma\,dS
\]
and proved, under its record-uniform finite-jet trace-thickening hypothesis,
\[
\boxed{
2|C_{0\sigma}|
\le
\varepsilon J_0+C_\varepsilon P.
}
\]

M17-470 independently proved that under a record-uniform zero-tube level-current stability and coefficient-gradient ceiling,
\[
\boxed{
J_0
\le
C_0 H_{\rm raw},
\qquad
C_0:=\frac{3G_*^2}{2c_0\delta_0^3}.
}
\]

This module combines only those two certified inequalities.

## 2. Pointwise trace absorption

Substitution gives
\[
2|C_{0\sigma}|
\le
\varepsilon C_0H_{\rm raw}
+C_\varepsilon P.
\]
Therefore
\[
\boxed{
|C_{0\sigma}|
\le
\frac{\varepsilon C_0}{2}H_{\rm raw}
+\frac{C_\varepsilon}{2}P.
}
\]

Thus, on a record family where the M17-460 and M17-470 compactness packages hold simultaneously, the codimension-one zero-level strain trace is not an independent payer.

It is absorbed by the two already-certified bulk ledgers:
\[
\boxed{
G_{C_{0\sigma}}
\subseteq
G_{\rm raw\text{-}H^2}
\lor
G_{\rm palinstrophy}.
}
\]

## 3. Spacetime version

For any interval \(I\),
\[
\boxed{
\int_I|C_{0\sigma}|dt
\le
\frac{\varepsilon C_0}{2}
\int_IH_{\rm raw}dt
+
\frac{C_\varepsilon}{2}
\int_IPdt.
}
\]

The first term belongs to the raw second-derivative ledger, and the second to the palinstrophy ledger
\[
P=\|\nabla\Omega\|_2^2.
\]

## 4. Ancestry audit

The certified record scalings are
\[
\sum_mR_m^{-3}
\int_IH_{{\rm raw},m}ds<\infty,
\]
\[
\sum_mR_m^{-1}
\int_IP_mds<\infty.
\]

Therefore the trace absorption does **not** create a contradiction merely by assigning a fixed normalized cost at every geometric record scale. Both ancestry weights are summable.

The point of this reduction is branch compression, not closure of global regularity.

## 5. Shared compactness package and exact exits

The reduction requires two independent quantitative packages.

### 5.1 Zero-tube package from M17-470

There must exist record-uniform
\[
\delta_0>0,
\qquad
c_0>0,
\qquad
G_*<\infty
\]
such that
\[
F(s)\ge c_0F(0)
\quad(|s|\le\delta_0),
\qquad
|\nabla\kappa|\le G_*.
\]

Failure gives
\[
G_{\rm zero\text{-}tube/level\text{-}flux\ collapse}
\lor
G_{\nabla\kappa\text{-}high\text{-}jet}.
\]

### 5.2 Trace package from M17-460

The zero-level normal strain derivative must admit the record-uniform trace thickening needed for
\[
2|C_{0\sigma}|\le\varepsilon J_0+C_\varepsilon P.
\]

Failure gives
\[
G_{\rm strain\ trace/high\text{-}jet}
\lor
G_{\rm zero\text{-}tube/chart\ degeneration}.
\]

Combining the two packages yields the exact dichotomy
\[
\boxed{
\begin{aligned}
G_{C_{0\sigma}}
\Longrightarrow{}&
G_{\rm raw\text{-}H^2}
\lor
G_{\rm palinstrophy}\\
&\lor
G_{\nabla\kappa\text{-}high\text{-}jet}\\
&\lor
G_{\rm strain\ trace/high\text{-}jet}\\
&\lor
G_{\rm zero\text{-}tube/level\text{-}flux/chart\ collapse}.
\end{aligned}
}
\]

## 6. No circular absorption claim

The parameter \(\varepsilon\) in M17-460 may be chosen small, but M17-471 does not use that smallness to absorb an unknown copy of \(C_{0\sigma}\) back into itself. It simply substitutes the independently obtained M17-470 estimate for \(J_0\).

Accordingly the argument is a payer classification, not a bootstrap closure.

## 7. Consequence for the A-balance

Recall
\[
\dot A+2J_0
=-2C_{0\sigma}+2G_{\rm cm}+2S_A+2\Delta Q.
\]

Under the shared compactness package:

- \(J_0\) is raw-H2 by M17-470;
- \(C_{0\sigma}\) is raw-H2 plus palinstrophy by M17-471;
- \(S_A\) is raw-H2-controlled under the M17-462 amplitude/enstrophy hypotheses;
- \(\Delta Q\) is raw-H2 by M17-468.

Thus, apart from endpoints and the explicitly listed compactness failures, every non-geometry term in the common-mode balance has now been assigned to raw-H2 or palinstrophy.

## 8. Audit status

Reduced/closed here:

- zero-level strain trace as an independent payer on compact zero-tube/trace record families.

Still OPEN:

- whether those compactness hypotheses hold uniformly across the retained genealogy;
- endpoint raw-H2 temporal thickening from M17-469;
- non-summable exploitation of raw-H2 or palinstrophy;
- termwise provenance of \(\mathcal R_{\rm geom}\);
- remote compensation, diffuse-carrier exits, genealogy/interface/domain exits;
- ROOT-CERT and non-CE-H roots.

## 9. Next target

Use M17-466, M17-468--471, and the certified ancestry ledgers to state the full common-mode source-return no-go: under bounded enstrophy/amplitude and the zero-tube/trace compactness package, the source-return mechanism pays only ancestry-summable raw-H2/palinstrophy plus an endpoint temporal-thickening debt. Therefore a contradiction requires a genuinely non-summable duration/multiplicity/allocation theorem or failure of one of those compactness hypotheses.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
