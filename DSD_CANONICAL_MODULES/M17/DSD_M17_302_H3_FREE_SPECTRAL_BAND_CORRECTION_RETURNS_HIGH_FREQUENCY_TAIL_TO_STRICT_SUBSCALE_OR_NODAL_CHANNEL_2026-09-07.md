# DSD M17-302 — H3-free spectral-band correction returns the high-frequency tail to the strict-subscale or nodal channel

Date: 2026-09-07  
Canonical ID: **M17-302**

Status: **AUDIT CORRECTION TO M17-300/301 / M17-300 USED THE STATEMENT `M17-272 PLUS INTERIOR BOOTSTRAPPING GIVES A UNIFORM H3 BOUND` TO CUT OFF THE HIGH-FOURIER H2 TAIL. THE CITED M17-272 ACTUALLY GIVES FINITE-CYLINDER `W^{2,1}_p` AND SPATIAL `C^{1,alpha}` CONTROL FROM BOUNDED LOWER-ORDER COEFFICIENTS, AND DOES NOT BY ITSELF JUSTIFY A UNIFORM H3 BOUND WITHOUT ADDITIONAL COEFFICIENT DERIVATIVE CONTROL. THE H3 STEP IS THEREFORE RETRACTED. IT IS NOT NEEDED. ON THE SCALE-COMPARABLE M17-251/253 PACKET THERE IS A UNIFORM H2 CEILING AND A FIXED POSITIVE RAW-LAPLACIAN FLOOR. EITHER A FIXED HIGH-FREQUENCY H2 TAIL PERSISTS ALONG ARBITRARILY LARGE FOURIER RADII, IN WHICH CASE M17-253 IDENTIFIES A VANISHING-L2 HIGH-FREQUENCY MICROCARRIER AND RETURNS IT TO STRICT PHYSICAL SUBSCALE OR NODAL CONCENTRATION; OR THE HIGH-FREQUENCY H2 TAIL IS TIGHT, IN WHICH CASE ONE FIXED `lambda_+` REMOVES AT MOST ONE QUARTER OF THE RAW-LAPLACIAN CHARGE. THE LOW-FREQUENCY L2 BOUND REMOVES ANOTHER QUARTER, SO A FIXED ANNULUS CARRIES A POSITIVE BAND MASS WITHOUT H3. CONSEQUENTLY M17-300/301 SURVIVE ONLY WITH THE EXTRA EXPLICIT ALTERNATIVE `G_high-frequency/subscale/nodal`. GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. Audit finding

M17-300 localized the own-scale normalized packet by

\[
f_j:=\chi V_j
\]

and retained

\[
\boxed{\|f_j\|_2\le C_0}
\]

and

\[
\boxed{\|\Delta f_j\|_2^2\ge h_0>0.}
\]

It then invoked a uniform `H3` bound to estimate

\[
\int_{|\xi|>\lambda_+}|\xi|^4|\widehat f_j|^2
\le
\lambda_+^{-2}
\int|\xi|^6|\widehat f_j|^2.
\]

The cited input M17-272 yields parabolic `W^{2,1}_p` and `C^{1,alpha}` control on the compact payer-free lane, but no uniform third spatial derivative estimate is stated there under only bounded lower-order coefficients.

Therefore the implication

\[
\boxed{\text{M17-272}\Longrightarrow \sup_j\|f_j\|_{H^3}<\infty}
\]

is **not justified by the cited module** and is retracted from the canonical reasoning.

---

## 2. What is actually available

M17-251 supplies, on the retained scale-comparable packet branch, a uniform own-scale `H2` ceiling on an interior fixed rescaled region.

After placing the fixed cutoff `chi` strictly inside that region,

\[
\boxed{\sup_j\|f_j\|_{H^2(\mathbb R^3)}\le C_2.}
\]

The same packet construction retains a positive raw-Laplacian charge

\[
\boxed{\|\Delta f_j\|_2^2\ge h_0>0.}
\]

No `H3` statement is needed below.

---

## 3. Define the high-frequency H2 tail

For `Lambda>0`, define

\[
\boxed{
\mathcal T_j(\Lambda)
:=
\int_{|\xi|>\Lambda}
|\xi|^4|\widehat f_j(\xi)|^2d\xi.
}
\]

The uniform `H2` ceiling gives

\[
0\le \mathcal T_j(\Lambda)\le C_2^2.
\]

There are two exhaustive alternatives.

---

## 4. Alternative A — high-frequency tightness

Suppose there exists a fixed `lambda_+<infinity` such that, after passing to a subsequence,

\[
\boxed{
\mathcal T_j(\lambda_+)\le h_0/4
}
\]

for all sufficiently large `j`.

For low frequencies,

\[
\int_{|\xi|<\lambda_-}
|\xi|^4|\widehat f_j|^2d\xi
\le
\lambda_-^4\|f_j\|_2^2
\le
\lambda_-^4C_0^2.
\]

Choose fixed `lambda_->0` so that

\[
\boxed{\lambda_-^4C_0^2\le h_0/4.}
\]

Then the fixed annulus

\[
\boxed{
\mathcal B:=\{\lambda_-\le |\xi|\le\lambda_+\}
}
\]

carries

\[
\begin{aligned}
\int_{\mathcal B}
|\xi|^4|\widehat f_j|^2d\xi
&\ge
\|\Delta f_j\|_2^2
-
\int_{|\xi|<\lambda_-}|\xi|^4|\widehat f_j|^2d\xi\\
&\qquad-
\int_{|\xi|>\lambda_+}|\xi|^4|\widehat f_j|^2d\xi\\
&\ge h_0/2.
\end{aligned}
\]

Since `|xi|<=lambda_+` on the band,

\[
\boxed{
\|P_{\mathcal B}f_j\|_2^2
\ge
\lambda_+^{-4}h_0/2
=:c_B^2>0.
}
\]

Thus the true fixed Fourier-band witness of M17-300 follows from **H2 tightness**, not H3 regularity.

---

## 5. Alternative B — persistent high-frequency H2 tail

Suppose Alternative A fails.

Then for every fixed `Lambda` there are arbitrarily large indices with

\[
\mathcal T_j(\Lambda)>h_0/4.
\]

Choose a sequence

\[
\Lambda_k\to\infty
\]

and a diagonal subsequence `j_k` such that

\[
\boxed{
\mathcal T_{j_k}(\Lambda_k)\ge h_0/4.
}
\]

The corresponding high-frequency piece has `L2` mass

\[
\begin{aligned}
\|P_{>\Lambda_k}f_{j_k}\|_2^2
&=
\int_{|\xi|>\Lambda_k}|\widehat f_{j_k}|^2d\xi\\
&\le
\Lambda_k^{-4}
\int_{|\xi|>\Lambda_k}
|\xi|^4|\widehat f_{j_k}|^2d\xi\\
&\le C_2^2\Lambda_k^{-4}
\to0.
\end{aligned}
\]

while its second-derivative charge stays bounded below:

\[
\boxed{
\|\Delta P_{>\Lambda_k}f_{j_k}\|_2^2
\ge h_0/4.
}
\]

Hence this is exactly a

\[
\boxed{
\text{vanishing-L2 / positive-H2 high-frequency microcarrier}.
}
\]

M17-253 already classifies this mechanism and returns it, via the raw-Laplacian physical re-extraction of M17-232/250, to

\[
\boxed{
G_{strict\ physical\ subscale}
\lor
G_{nodal\ concentration}.
}
\]

Therefore a non-tight high-frequency tail is not an untyped failure of the spectral-band argument.

---

## 6. Corrected M17-300 gate

The correct input-to-band statement is

\[
\boxed{
H_{scale\text{-}comparable\ raw\ H2\ packet}
\Longrightarrow
G_{strict\ subscale/nodal}
\lor
H_{fixed\ Fourier\ band}.
}
\]

On the second branch, the exact localized equation

\[
\partial_\tau f_j-\Delta f_j=F_j
\]

and the fixed-band Duhamel calculation of M17-300 remain unchanged.

Thus the corrected fixed-lag gate is

\[
\boxed{
H_{present\ packet}
\Longrightarrow
G_{strict\ subscale/nodal}
\lor
H_{fixed\text{-}lag\ band\ recharge/leakage}
\lor
H_{exponentially\ larger\ ancestor\ band}.
}
\]

---

## 7. Corrected M17-301 growing-lag gate

M17-301 eliminates the exponentially larger ancestor branch on the parent-ceiling corridor by choosing

\[
T_j=A\log R_j,
\qquad
A\lambda_-^2>2.
\]

That argument is unaffected once Alternative A supplies the fixed band.

Therefore the corrected M17-301 conclusion is

\[
\boxed{
H_{shell\text{-}relevant\ packet}
\Longrightarrow
G_{strict\ subscale/nodal}
\lor
G_{parent\ ceiling/scale\text{-}map\ exit}
\lor
H_{unit\text{-}window\ coefficient/recharge\ payment}
\lor
H_{unit\text{-}window\ gradient\ interface\ payment}
\lor
H_{unit\text{-}window\ mass\ interface\ payment}.
}
\]

No `H3` hypothesis is used.

---

## 8. Why this correction matters

The correction changes the logical status of the high-frequency branch.

Previously M17-300 silently suppressed it through an unsupported higher-regularity assertion.

The corrected proof tree does the opposite:

1. if high-frequency `H2` charge escapes, it is explicitly retained as the already-known strict-subscale/nodal branch;
2. only on the complementary `H2`-tight branch is a fixed Fourier annulus extracted;
3. the subsequent Duhamel/growing-lag argument is run only there.

This is consistent with the concentration-compactness firewall established by M17-253.

---

## 9. DSD analysis

### Resolution separation

`H2` charge at a fixed Fourier scale and `H2` charge escaping to infinite frequency are treated as different structural states.

### No derivative inflation

No third derivative is inferred from second-order parabolic control with merely bounded lower-order coefficients.

### Exhaustive branching

Failure of fixed-band extraction is not discarded. It is exactly the high-frequency microcarrier branch.

### Physical return

The Fourier high-frequency branch is not itself called a physical smaller packet; physical re-extraction is delegated to M17-253 -> M17-232/250.

---

## 10. DSD audit

- **FAIL/CORRECTED:** `M17-272 => uniform H3` was not justified by the cited assumptions.
- **PASS:** M17-251 provides the uniform `H2` ceiling required for the corrected dichotomy.
- **PASS:** low-frequency `H2` charge is uniformly small for sufficiently small fixed `lambda_-` by the `L2` ceiling.
- **PASS:** either one fixed `lambda_+` controls the high-frequency `H2` tail, or a diagonal high-frequency positive-`H2`/vanishing-`L2` carrier exists.
- **PASS:** the latter is precisely the M17-253 strict-subscale/nodal mechanism.
- **PASS:** on the fixed-band branch, all Duhamel estimates in M17-300/301 remain valid.
- **OPEN:** M17-301 still depends on persistence of the parent absolute-amplitude ceiling/scale map over the logarithmic physical lookback.
- **OPEN:** the local normalized payments produced by M17-301 are not yet converted into a nonsummable physical budget or a nonrepeatable genealogy.
- **NO CLAIM:** global regularity is not proved.

---

## 11. Canonical supersession note

For all future use:

- the `H3` sentence in M17-300 is **superseded by M17-302**;
- M17-300 is to be read with the additional `strict subscale/nodal` alternative;
- M17-301 is to be read with the same additional alternative before its parent-ceiling/payment split.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
