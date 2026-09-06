# DSD M17-299 — Shell-relevant logarithmic-scale carriers have a polynomial remote-amplitude floor

Date: 2026-09-06  
Canonical ID: **M17-299**

Status: **AMPLITUDE-EXTRACTION GATE / M17-298 SHOWS THAT EXPONENTIALLY TINY PACKETS CARRYING A FIXED FRACTION OF THE NONSUMMABLE SHELL H2 NUMERATOR MUST LIVE AT SCALES `r>=c/(log R)^(1/2)` ON AN INFINITE SHELL SUBFAMILY. DECOMPOSE THE REMAINING SCALE RANGE INTO DYADIC BINS. THERE ARE ONLY `O(log log R)` BINS BETWEEN THE LOGARITHMIC FLOOR AND A FIXED MACROSCOPIC INTRINSIC CEILING. IF THE EXPONENTIAL-CARRIER FAMILY CARRIES A FIXED FRACTION OF `Hsh`, ONE BIN CARRIES AT LEAST A `1/O(log log R)` FRACTION. PACKING IN THAT BIN GIVES A PACKET WITH `H_i >= c Hsh r^3/(R^3 log log R)`. SCALE COMPARABILITY `H_i~a_i^2/r` THEN YIELDS `a_i^2 >= c Hsh r^4/(R^3 log log R)`. ON THE M17-207 NONSUMMABLE SUBSEQUENCE, `Hsh>=R^-1(log R)^(-2/3-epsilon)`, AND WITH `r^2>=c/(log R)` THIS GIVES A POLYNOMIAL REMOTE LOWER BOUND `a_i >= c R^-2 (log R)^(-4/3-epsilon/2)(log log R)^(-1/2)`. THUS A SHELL-RELEVANT EXPONENTIAL CARRIER IS NOT ARBITRARILY BEYOND-ALL-ORDERS IN THE REMOTE RADIUS; AT LEAST ONE REPRESENTATIVE PACKET HAS ONLY POLYNOMIAL-IN-R SMALLNESS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Shell-relevant exponential carrier family

Fix one remote shell radius `R` from the infinite M17-207 nonsummable subfamily.

Let

\[
E^{sh}:=\int_{C_R}|W|^2,
\qquad
H^{sh}:=\int_{C_R}|\Delta W|^2.
\]

Assume a family `F_exp` of scale-comparable exponential packets carries a fixed numerator fraction

\[
\boxed{
\sum_{P_i\in\mathcal F_{exp}}H_i
\ge\eta_H H^{sh}
}
\]

with fixed `eta_H>0`.

By M17-298, after discarding a negligible-H2 subfamily, the shell-relevant packet scales satisfy

\[
\boxed{
r_i\ge r_{min}(R):=c_*/\sqrt{\log R}.}
\]

Take a fixed upper intrinsic scale `r_max=O(1)` inside the shell-local packet corridor.

---

## 2. Number of dyadic scale bins

Partition

\[
[r_{min}(R),r_{max}]
\]

into dyadic bins

\[
\mathcal B_j:=\{r:2^{-j-1}r_{max}<r\le2^{-j}r_{max}\}.
\]

The number of nonempty bins is at most

\[
\boxed{
N_{bin}(R)
\le C\log\!\left(\frac{r_{max}}{r_{min}(R)}\right)
\le C\log\log R.
}
\]

Therefore one bin, with representative scale `r`, satisfies

\[
\boxed{
\sum_{i\in\mathcal B}H_i
\ge
\frac{c\eta_H}{\log\log R}H^{sh}.
}
\]

All radii in this bin are comparable to `r` by a fixed factor.

---

## 3. Packing within the selected scale bin

After Vitali selection/bounded-overlap normalization, the number of scale-`r` packets in the shell is bounded by

\[
\boxed{
N_r
\le C_{pack}\frac{R^3}{r^3}.
}
\]

Hence at least one packet `P_*` in the selected bin obeys

\[
\begin{aligned}
H_*
&\ge
\frac{1}{N_r}
\sum_{i\in\mathcal B}H_i\\
&\ge
c
\frac{H^{sh}}{\log\log R}
\frac{r^3}{R^3}.
\end{aligned}
\]

Thus

\[
\boxed{
H_*
\ge
c\frac{H^{sh}r^3}{R^3\log\log R}.
}
\]

---

## 4. Convert H2 charge to packet RMS amplitude

For a scale-comparable packet,

\[
H_*\asymp\frac{m_*}{r^4}.
\]

Define its RMS amplitude by

\[
\boxed{
a_*^2:=\frac{m_*}{r^3}.}
\]

Then

\[
H_*\asymp a_*^2r^{-1}.
\]

Therefore Section 3 gives

\[
\boxed{
a_*^2
\ge
c\frac{H^{sh}r^4}{R^3\log\log R}.}
\]

Equivalently,

\[
\boxed{
a_*
\ge
c\frac{r^2(H^{sh})^{1/2}}{R^{3/2}(\log\log R)^{1/2}}.}
\]

---

## 5. Nonsummable shell lower bound

M17-207 gives

\[
\sum_k b_k^{3/2}=\infty,
\qquad
b_k:=R_kE_k^{sh}.
\]

Fix arbitrary

\[
\varepsilon>0.
\]

As recorded in M17-298, infinitely many dyadic shell indices satisfy

\[
\boxed{
b_k\ge k^{-2/3-\varepsilon}.}
\]

Since the spectral ratio eventually exceeds one,

\[
H_k^{sh}\ge E_k^{sh}=\frac{b_k}{R_k}.
\]

Thus on an infinite selected subsequence,

\[
\boxed{
H^{sh}
\ge
cR^{-1}(\log R)^{-2/3-\varepsilon}.}
\]

---

## 6. Use the logarithmic scale floor

M17-298 gives

\[
\boxed{
r^2\ge\frac{c_*^2}{\log R}.}
\]

Insert Sections 5 and 6 into the amplitude estimate:

\[
\begin{aligned}
a_*
&\ge
c\frac{r^2}{R^{3/2}(\log\log R)^{1/2}}
R^{-1/2}(\log R)^{-1/3-\varepsilon/2}\\
&\ge
cR^{-2}
(\log R)^{-4/3-\varepsilon/2}
(\log\log R)^{-1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
a_*
\ge
cR^{-2}
(\log R)^{-4/3-\varepsilon/2}
(\log\log R)^{-1/2}.}
\]

The precise logarithmic exponent is not the conceptual point.
The key is that the representative shell-relevant packet is only **polynomially small in the remote shell radius**.

---

## 7. What this changes

M17-296 allowed one isolated packet to have absolute amplitude

\[
a\lesssim e^{-c/r^2}.
\]

M17-299 shows that, once such packets are required to carry a fixed fraction of the nonsummable shell numerator, at least one packet on infinitely many shells obeys both

\[
\boxed{
r^{-2}=O(\log R)}
\]

and

\[
\boxed{a\ge R^{-2}\times\operatorname{polylog}(R)^{-1}.}
\]

Thus the shell-relevant survivor is no longer beyond-all-orders in `R`.
It becomes a **polynomial-rate ancestor/genealogy problem**.

---

## 8. What is not yet proved

A present amplitude lower bound does not imply that the same packet or spectral component grows backward by the free heat factor

\[
e^{T/r^2}.
\]

`H2/L2` localization alone is not an exact Fourier-band or eigenmode localization.
Cancellation and multiscale reorganization may occur.

Therefore the next missing theorem is a **Logarithmic Ancestor Gate (LAG)** that would separate:

1. persistent scale-`r` spectral band / coherent ancestor;
2. spectral-band leakage or cancellation;
3. coefficient/interface/replenishment payment.

No backward heat amplification is claimed before that gate is proved.

---

## 9. DSD audit

- The fixed shell numerator-fraction hypothesis is explicit.
- The `O(log log R)` bin count uses the M17-298 logarithmic lower scale and a fixed upper packet scale.
- The amplitude is an RMS packet amplitude, not a pointwise minimum.
- The shell lower bound is asserted only on the infinite nonsummable subsequence.
- No backward mode persistence is inferred from a single-time `H2/L2` ratio.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
