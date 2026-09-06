# DSD M17-298 — Exponentially tiny packets carrying nonsummable shell H2 charge have a logarithmic scale floor

Date: 2026-09-06  
Canonical ID: **M17-298**

Status: **EXPONENTIAL-PACKING GATE / M17-296--297 LEAVE SCALE-`r` PACKETS WITH ABSOLUTE AMPLITUDE AS SMALL AS `exp(-c/r^2)`. A SCALE-COMPARABLE PACKET OF AMPLITUDE `a` HAS RAW SECOND-DERIVATIVE CHARGE `H_packet ~ a^2 r^(-1)`, WHILE AT MOST `O(R^3/r^3)` DISJOINT SCALE-`r` PACKETS FIT IN A REMOTE SHELL OF RADIUS `R`. HENCE ALL SUCH EXPONENTIALLY TINY PACKETS AT SCALE `r` CARRY AT MOST `C R^3 exp(-2c/r^2) r^(-4)` RAW H2 CHARGE. ON THE NONSUMMABLE M17-207 SHELL SUBFAMILY, `sum b_k^(3/2)=infinity` IMPLIES THAT FOR EVERY EPSILON>0, INFINITELY MANY DYADIC INDICES SATISFY `b_k >= k^(-2/3-epsilon)`; SINCE THE SPECTRAL RATIO EVENTUALLY EXCEEDS ONE, `H_k>=E_k=b_k/R_k`. COMPARISON SHOWS THAT A FIXED FRACTION OF THIS SHELL CHARGE CANNOT BE CARRIED BY PACKETS WITH `r=o((log R)^(-1/2))`. THUS ANY SHELL-RELEVANT EXPONENTIAL MICROcarrier HAS A LOGARITHMIC SPATIAL SCALE FLOOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One exponentially tiny scale-comparable packet

Let a packet have physical similarity scale `r` and characteristic absolute amplitude `a`.

On a scale-comparable packet,

\[
H_{pkt}\asymp\frac{m}{r^4},
\qquad
m\asymp a^2r^3.
\]

Therefore

\[
\boxed{
H_{pkt}\asymp a^2r^{-1}.}
\]

On the M17-296 exponential survivor,

\[
\boxed{a\le C_a e^{-c_a/r^2}.}
\]

Hence

\[
\boxed{
H_{pkt}
\le C e^{-2c_a/r^2}r^{-1}.}
\]

---

## 2. Geometric multiplicity at one scale

A remote shell/enlarged shell of radius `R` has geometric volume `O(R^3)`.

A disjoint/Vitali scale-`r` family therefore contains at most

\[
\boxed{
N_r\le C_{pack}\frac{R^3}{r^3}
}
\]

packets.

Thus the total raw `H2` charge of the entire exponential scale bin is bounded by

\[
\boxed{
H_{bin}(r)
\le
C R^3e^{-2c_a/r^2}r^{-4}.
}
\]

The same estimate holds for a bounded-overlap family after changing the constant.

---

## 3. Lower shell mass on a nonsummable subsequence

Recall

\[
b_k:=R_kE_k^{sh}
\]

and M17-207's nonsummable critical packing

\[
\boxed{
\sum_k b_k^{3/2}=\infty.
}
\]

Fix any

\[
\varepsilon>0.
\]

If eventually

\[
b_k<k^{-2/3-\varepsilon},
\]

then

\[
b_k^{3/2}<k^{-1-3\varepsilon/2}
\]

and the series would converge.

Therefore there are infinitely many indices with

\[
\boxed{
b_k\ge k^{-2/3-\varepsilon}.}
\]

For dyadic radii

\[
R_k\asymp2^k,
\]

this is

\[
\boxed{
E_k^{sh}
=\frac{b_k}{R_k}
\gtrsim
R_k^{-1}(\log R_k)^{-2/3-\varepsilon}
}
\]

up to fixed logarithmic constants.

---

## 4. Lower raw H2 shell charge on the spectral branch

On the shell spectral branch

\[
\frac{H_k^{sh}}{E_k^{sh}}\to\infty.
\]

Hence for sufficiently large selected indices,

\[
\frac{H_k^{sh}}{E_k^{sh}}\ge1.
\]

Thus

\[
\boxed{
H_k^{sh}
\ge E_k^{sh}
\gtrsim
R_k^{-1}(\log R_k)^{-2/3-\varepsilon}.
}
\]

---

## 5. Exclude scales much smaller than 1/sqrt(log R)

Suppose all exponential packets carrying a fixed fraction of the shell numerator have scales

\[
r\le r_*(R)
\]

with `r_*` sufficiently small.

For small `r`, the function

\[
e^{-2c_a/r^2}r^{-4}
\]

is increasing with `r`.

Therefore all such small-scale packets together carry at most

\[
\boxed{
H_{small}
\le
C R^3
 e^{-2c_a/r_*^2}
r_*^{-4}.
}
\]

Choose

\[
\boxed{
r_*(R)=\frac{A}{\sqrt{\log R}}}
\]

with a fixed sufficiently small `A>0`.

Then

\[
e^{-2c_a/r_*^2}
=R^{-2c_a/A^2}
\]

and

\[
r_*^{-4}
asymp(\log R)^2.
\]

Hence

\[
H_{small}
\le
C
R^{3-2c_a/A^2}
(\log R)^2.
\]

Choose `A` so small that

\[
\boxed{
\frac{2c_a}{A^2}>4.
}
\]

Then

\[
H_{small}
=o\!\left(R^{-1}(\log R)^{-M}\right)
\]

for every fixed logarithmic exponent `M` after strengthening `A` slightly if needed.

This is smaller than the lower shell charge of Section 4 on the nonsummable subsequence.

Therefore such packets cannot carry a fixed numerator fraction.

---

## 6. Logarithmic scale floor

Consequently, on infinitely many nonsummable spectral shells, any exponential packet family carrying a fixed fraction of `H_k^sh` must include scales satisfying

\[
\boxed{
r\ge\frac{c_*}{\sqrt{\log R_k}}.}
\]

Equivalently,

\[
\boxed{
\frac1{r^2}
\lesssim
\log R.
}
\]

Thus shell-relevant heat-scale exponential microcarriers cannot descend to arbitrarily faster-than-logarithmic spatial frequencies.

---

## 7. New interpretation

The M17-296 survivor

\[
a\lesssim e^{-c/r^2}
\]

combined with shell packing is now restricted to a regime in which

\[
r^{-2}=O(\log R).
\]

Hence its natural heat damping/amplification over a fixed `O(1)` similarity time is only polynomial in the remote shell radius:

\[
e^{T/r^2}
\le R^{C_T}.
\]

This converts the formerly beyond-all-orders local defect into a shell-scale **polynomial-rate genealogy problem**.

That is the next useful bridge.

---

## 8. DSD audit

- The lower bound on `b_k` is asserted only on an infinite subsequence forced by nonsummability.
- The spectral ratio is used only after it exceeds one; no specific divergence rate is assumed.
- The scale-bin packing uses absolute raw `H2` charge, not normalized ratios.
- Exponential packets outside the carrier family may exist but are irrelevant if they carry negligible shell numerator.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
