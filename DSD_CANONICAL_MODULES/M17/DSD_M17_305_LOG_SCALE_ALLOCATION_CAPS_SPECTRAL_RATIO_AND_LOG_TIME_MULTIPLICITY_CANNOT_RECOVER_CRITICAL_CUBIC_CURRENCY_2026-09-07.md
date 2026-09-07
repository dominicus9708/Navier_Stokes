# DSD M17-305 — Log-scale allocation caps the shell spectral ratio and logarithmic time multiplicity cannot recover the critical cubic currency

Date: 2026-09-07  
Canonical ID: **M17-305**

Status: **MULTIPLICITY-DEFICIT / CRITICAL-CURRENCY AUDIT, CONDITIONAL ON THE STILL-OPEN M17-298 CROSS-SCALE ALLOCATION THEOREM. IF A BOUNDED-OVERLAP FAMILY OF SCALE-COMPARABLE PACKETS CARRIES A FIXED FRACTION OF THE SHELL RAW `H2` NUMERATOR AND EVERY SHELL-RELEVANT PACKET OBEYS THE M17-298 LOGARITHMIC FLOOR `r^2 >= c/log R`, THEN SCALE COMPARABILITY AND BOUNDED PACKET-MASS OVERLAP FORCE THE SHELL SPECTRAL RATIO `Lambda=Hsh/Esh` TO SATISFY `Lambda <= C (log R)^2`. THUS THE SPECTRAL RATIO CANNOT GROW FAST ENOUGH TO COMPENSATE THE `R^-1` LOSS IN THE M17-207 CRITICAL CURRENCY. MORE PRECISELY, TO CONVERT GRADIENT-INTERFACE PAYMENTS INTO THE DIVERGENT CUBIC SHELL CHARGE `b_k^(3/2)` ONE WOULD NEED `M_k Lambda_k >= c R_k b_k^(1/2)(log R_k)^2`, WHERE `M_k` IS THE NUMBER OF EFFECTIVE DISJOINT PAYING SWEEPS. THE LOGARITHMIC DUHAMEL LOOKBACK PROVIDES AT MOST `M_k=O(log R_k)`, WHILE THE ALLOCATION CAP GIVES `Lambda_k=O((log R_k)^2)`. ON THE M17-298 NONSUMMABLE SUBSEQUENCE THIS MISSES THE REQUIRED SIZE BY AN ESSENTIALLY LINEAR FACTOR IN `R_k`. THE MASS-INTERFACE CHANNEL HAS ONE ADDITIONAL `r^2` LOSS AND IS EVEN FARTHER FROM CRITICAL CONVERSION. THIS DOES NOT PROVE THE ACTUAL PAYMENT SUMS CONVERGE; IT PROVES THAT GEOMETRIC PACKING + LOGARITHMIC TIME MULTIPLICITY + THE CURRENT SCALE FLOOR CANNOT, BY THEMSELVES, FORCE THE NONSUMMABLE PAYMENT NEEDED TO CONTRADICT THE FINITE M17-304 LEDGERS. A NEW MECHANISM MUST USE STRICT SCALE DESCENT, CROSS-SHELL ANCESTRY, TRUE MATERIAL/FLUX REPLACEMENT, OR A SIGNED/MONOTONE COEFFICIENT RESOURCE. GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.**

---

## 1. Conditional shell allocation hypothesis

This module explicitly assumes the missing M17-298 cross-scale allocation theorem in the following form.

Fix a remote shell `C_R` at one similarity time and write

\[
E^{sh}:=\int_{C_R}|W|^2dy,
\qquad
H^{sh}:=\int_{C_R}|\Delta W|^2dy.
\]

Assume there is a bounded-overlap family of scale-comparable packets `P_i` satisfying

\[
\boxed{
\sum_iH_i\ge\eta_HH^{sh}
}
\]

for a fixed `eta_H>0`, where

\[
H_i:=\int_{P_i^{core}}|\Delta W|^2dy,
\qquad
m_i:=\int_{P_i}|W|^2dy,
\]

and

\[
\boxed{
c_0\le r_i^4\frac{H_i}{m_i}\le C_0.}
\]

Assume also the M17-298 logarithmic shell-relevant floor

\[
\boxed{
r_i^2\ge\frac{c_r}{\log R}}
\]

for every packet retained in this fixed-fraction numerator family.

All conclusions below are conditional on this allocation package.  The package is precisely one of the current open bridges and is not silently declared proved here.

---

## 2. Bounded overlap plus the logarithmic floor caps the shell spectral ratio

Scale comparability gives

\[
m_i\ge c_0r_i^4H_i.
\]

Let

\[
r_*^2:=\frac{c_r}{\log R}.
\]

Then

\[
\sum_im_i
\ge
c_0r_*^4\sum_iH_i
\ge
c_0\eta_Hr_*^4H^{sh}.
\]

Because the packet family has uniformly bounded spatial overlap and each packet mass is sampled from the original `|W|^2`,

\[
\sum_im_i\le C_{ov}E^{sh}
\]

after using one fixed enlarged shell if necessary.

Therefore

\[
H^{sh}
\le
\frac{C_{ov}}{c_0\eta_H}r_*^{-4}E^{sh}.
\]

Define the shell spectral ratio

\[
\boxed{
\Lambda(R):=\frac{H^{sh}}{E^{sh}}.
}
\]

Since

\[
r_*^{-4}\asymp(\log R)^2,
\]

we obtain the conditional but exact consequence

\[
\boxed{
\Lambda(R)\le C_{spec}(\log R)^2.
}
\]

Thus, once a fixed fraction of raw shell `H2` has genuinely been allocated to bounded-overlap packets above the logarithmic scale floor, the same assumptions automatically prevent an arbitrarily faster shell spectral ratio.

This is an important consistency condition for any repair of M17-298.

---

## 3. Critical M17-207 shell currency

On the hard shell branch let

\[
\boxed{
b_k:=R_kE_k^{sh},
\qquad R_k\asymp2^k,}
\]

with

\[
\boxed{
\sum_kb_k^{3/2}=\infty.
}
\]

M17-207 further permits restriction to a globally tempered divergent subfamily.

M17-298 uses the elementary consequence that, for every fixed `epsilon>0`, infinitely many selected indices satisfy

\[
\boxed{
b_k\ge c k^{-2/3-\varepsilon}.}
\]

Since

\[
k\asymp\log R_k,
\]

this is

\[
\boxed{
b_k\ge c(\log R_k)^{-2/3-\varepsilon}}
\]

on an infinite selected subfamily.

The target critical charge per shell is `b_k^(3/2)`, not merely `E_k=b_k/R_k`.

---

## 4. Gradient-payment critical conversion condition

Suppose, optimistically, that at one effective paying sweep the fixed-fraction packet family of Section 1 is routed to the M17-301 gradient-interface channel.

M17-303/304 attach to the family the parent gradient weight

\[
\sum_im_i.
\]

Using scale comparability and the minimum packet scale,

\[
\sum_im_i
\ge
c r_*^4H_k^{sh}.
\]

Write

\[
H_k^{sh}
=\Lambda_kE_k^{sh}
=\Lambda_k\frac{b_k}{R_k}.
\]

Thus one such full shell-relevant sweep has the guaranteed current-information floor

\[
\boxed{
P_{k,1}^{grad}
\gtrsim
r_*^4\Lambda_k\frac{b_k}{R_k}.
}
\]

If `M_k` pairwise time-disjoint effective sweeps of this strength can be proved, then the corresponding floor is

\[
P_k^{grad}
\gtrsim
M_kr_*^4\Lambda_k\frac{b_k}{R_k}.
\]

To recover the M17-207 critical currency shell-by-shell it is sufficient to have

\[
P_k^{grad}\gtrsim b_k^{3/2}.
\]

This requires

\[
\boxed{
M_k\Lambda_k
\gtrsim
\frac{R_kb_k^{1/2}}{r_*^4}.
}
\]

Using `r_*^-4 asymp (log R_k)^2`,

\[
\boxed{
M_k\Lambda_k
\gtrsim
R_kb_k^{1/2}(\log R_k)^2.
}
\]

This is the exact multiplicity--spectral-ratio deficit relation for the current gradient-payment strategy.

It is a requirement for this particular critical-currency conversion, not a universal necessary condition for every possible proof.

---

## 5. Available logarithmic time multiplicity is far too small

M17-301 uses the own-scale backward lag

\[
\boxed{T_k=A\log R_k.}
\]

A pairwise disjoint collection of unit own-scale time windows inside this lag can contain at most

\[
\boxed{M_k\le C_T\log R_k.}
\]

This is only an absolute counting ceiling; M17-301 itself proves at least one paying unit window, not payment on all such windows.

Combine this maximal possible logarithmic count with the allocation cap from Section 2:

\[
\boxed{
M_k\Lambda_k
\le
C(\log R_k)^3
}
\]

within the present log-scale allocation model.

By contrast, Section 4 requires

\[
M_k\Lambda_k
\gtrsim
R_kb_k^{1/2}(\log R_k)^2.
\]

On the infinite M17-298 selected subfamily,

\[
b_k^{1/2}
\gtrsim
(\log R_k)^{-1/3-\varepsilon/2}.
\]

Hence the required product is at least

\[
\boxed{
R_k
(\log R_k)^{5/3-\varepsilon/2}.
}
\]

whereas the log-scale model can furnish at most a polylogarithmic product `O((log R_k)^3)`.

The ratio between the required scale and the maximal log-scale product is therefore at least

\[
\boxed{
\frac{R_k}
{(\log R_k)^{4/3+\varepsilon/2}}
\to\infty.
}
\]

Thus logarithmic time multiplicity cannot repair the critical `R_k^-1` loss within this allocation strategy.

Again, this is an insufficiency theorem for the present lower-bound mechanism; it does not upper-bound the unknown actual parent gradient ledger generated by the solution.

---

## 6. Equivalent form after using the spectral cap first

Because

\[
\Lambda_k\le C(\log R_k)^2,
\]

the gradient conversion requirement implies

\[
M_k
\gtrsim
R_kb_k^{1/2}.
\]

Thus on the selected nonsummable subfamily,

\[
\boxed{
M_k
\gtrsim
R_k
(\log R_k)^{-1/3-\varepsilon/2}.
}
\]

But the available logarithmic ancestry interval contains only

\[
O(\log R_k)
\]

disjoint unit windows.

The required paying-sweep multiplicity is therefore essentially **linear in the remote radius**, while the available lookback multiplicity is only logarithmic in that radius.

This is the main quantitative conclusion of M17-305.

---

## 7. Mass-interface channel has an additional scale loss

For a shell-relevant packet,

\[
m_ir_i^2\asymp H_ir_i^6.
\]

Therefore one fixed-fraction mass-interface sweep has floor

\[
P_{k,1}^{mass}
\gtrsim
r_*^6H_k^{sh}
=r_*^6\Lambda_k\frac{b_k}{R_k}.
\]

To reach `b_k^(3/2)` after `M_k` sweeps requires

\[
\boxed{
M_k\Lambda_k
\gtrsim
\frac{R_kb_k^{1/2}}{r_*^6}.
}
\]

Since

\[
r_*^{-6}\asymp(\log R_k)^3,
\]

this becomes

\[
\boxed{
M_k\Lambda_k
\gtrsim
R_kb_k^{1/2}(\log R_k)^3.
}
\]

Using the spectral cap `Lambda_k<=C(log R_k)^2`, one would need

\[
\boxed{
M_k
\gtrsim
R_kb_k^{1/2}\log R_k.
}
\]

On the selected subsequence,

\[
\boxed{
M_k
\gtrsim
R_k
(\log R_k)^{2/3-\varepsilon/2},
}
\]

which is even farther from the available `O(log R_k)` unit-window count.

Thus mass-interface multiplicity is strictly weaker than gradient-interface multiplicity for direct critical-currency recovery.

---

## 8. Why spatial packet multiplicity does not add another R^3 here

The family in Section 1 already aggregates **all spatial packets** carrying the fixed shell `H2` fraction at one effective sweep.

The estimate

\[
\sum_im_i\ge cr_*^4\sum_iH_i
\]

and the bounded-overlap inequality

\[
\sum_im_i\le CE^{sh}
\]

have already incorporated spatial packet multiplicity.

Therefore multiplying Section 4 again by a geometric packet count `R^3/r^3` would double-count the same shell population and is forbidden.

The only multiplicity left in the present conversion is independent time/genealogy reuse of shell-level paying populations.

This is an R21/R27 audit firewall.

---

## 9. Relation to M17-205/207 fixed-lag genealogy

M17-205 controls material shell enstrophy over every **fixed** similarity lag, and M17-207 removes the fixed-lag shell-neighbor circularity by globally tempered extraction.

The present logarithmic lag grows like

\[
T_k\asymp\log R_k.
\]

Thus M17-205 cannot simply be inserted with one uniform fixed-lag constant: its shell displacement and amplitude-comparison constants depend on the lag.

M17-305 does not claim a growing-lag extension of M17-205.

Failure to maintain the required parent-to-M17 packet/shell genealogy over the logarithmic interval remains the explicit branch

\[
\boxed{G_{parent\text{-}to\text{-}M17\ scale\text{-}map/domain/genealogy}.}
\]

If such a growing-lag genealogy theorem is later proved, the quantitative deficit above shows that **mere logarithmic reuse count is still insufficient**; that theorem must supply a stronger mechanism than unit-window multiplicity.

---

## 10. What this closes

The following candidate strategy is now retired, even after granting the unresolved cross-scale allocation theorem:

\[
\boxed{
\text{logarithmic packet scale floor}
+\text{bounded-overlap shell packing}
+\text{O(log R) paying windows}
\Longrightarrow
\text{critical nonsummable interface budget}.
}
\]

The missing factor is essentially one power of the remote radius `R`.

Thus the M17-304 finite resource cannot be contradicted by the currently available geometric/logarithmic multiplicity information alone.

---

## 11. New narrow frontier

After M17-305, a successful continuation must introduce a mechanism not already present in the naive multiplicity ledger.  The most concrete options are:

1. **strict intrinsic scale descent** whose infinite continuation ends in the already typed nodal channel;
2. **cross-shell ancestry/reassignment** that transfers the M17-207 cubic currency without the `R^-1` loss;
3. **true material/flux replacement** with a finite-memory theorem at packet/surface level, respecting M17-238;
4. **signed/monotone coefficient ledger** for the CE-H multiplier `kappa` or amplitude exposure;
5. **a new critical-resource conversion** producing an event charge directly comparable to `b_k^(3/2)` instead of `E_k=b_k/R_k`.

The coefficient branch from M17-233--238 is therefore a natural next place to search, but its amplitude-independent critical `kappa` occupancy still needs a global spacetime/genealogy budget.

---

## 12. DSD audit

- Every conclusion using the logarithmic packet floor is explicitly conditional on the unresolved M17-298 cross-scale allocation theorem.
- Spatial packet multiplicity is counted exactly once through the fixed-fraction shell allocation.
- `M_k<=C log R_k` is an upper count of disjoint unit windows, not a lower payment multiplicity theorem.
- A summable/insufficient lower-bound mechanism is not confused with an upper bound on the actual unknown solution cost.
- The spectral-ratio cap follows from packet mass overlap and scale comparability; it is not an external regularity theorem.
- M17-205 remains a fixed-lag result and is not silently promoted to a logarithmic-lag theorem.
- Mass-interface migration remains distinct from dissipation.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
