# M19-398 — Critical current reversal requires exponential line-residence collapse at the seed amplification rate

Date: 2026-09-18

Status: **NEW CRITICAL SCALING REFINEMENT / M19-389 GIVES EXACT RESIDENCE RATIOS ON A POSITIVE KAPPA EXCURSION. WHEN A LONG COMPLETE EXCURSION HAS THE M19-365 CRITICAL ACTION `I_+=(3/2+o(1))T`, CURRENT CANCELLATION/REVERSAL FORCES `R_d/R_u<=exp(-3T+o(T))` FOR `R=L_rho/Phi`, AND `L_d/L_u<=exp(-3T/2+o(T))`. THUS THE REVERSAL ESCAPE IS NOT A MILD PHASE BIAS: IT REQUIRES EXPONENTIAL COLLAPSE OF THE MATERIAL LINE-RESIDENCE WEIGHT AT EXACTLY THE SAME 3/2 RATE AS THE CRITICAL SEED FLUX/ENSTROPHY AMPLIFICATION. A COHERENT COMPACT LINE SEGMENT CANNOT DO BOTH WITHOUT A MACROSCOPIC COMPRESSIVE COUNTERPHASE, AMPLITUDE/LENGTH DEGENERATION, OR PACKET/GENEALOGY REPLACEMENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Long critical positive excursion

Let

\[
E_T=[\theta_u,\theta_d]
\]

be a complete positive-kappa excursion of duration

\[
T=\theta_d-\theta_u\to\infty.
\]

Assume the critical seed phase dominates so that

\[
\boxed{
I_+
:=
\int_{E_T}\kappa\,d\theta
=
\left(\frac32+o(1)\right)T.
}
\]

Then the material flux amplification is

\[
\boxed{
\frac{\Phi_d}{\Phi_u}
=
e^{I_+}
=
\exp\left[
\left(\frac32+o(1)\right)T
\right].
}
\]

---

## 2. Relative residence collapse

M19-389--390 show that residence-current cancellation or reversal requires

\[
J_+\le-2I_+,
\]

where

\[
J_+
=
\log\frac{R_d}{R_u},
\qquad
R=\frac{L_\rho}{\Phi}.
\]

Therefore

\[
\boxed{
\frac{R_d}{R_u}
\le
e^{-2I_+}
=
\exp\left[
(-3+o(1))T
\right].
}
\]

So the enstrophy-residence weight relative to material flux must collapse at asymptotic rate at least \(3\).

---

## 3. Absolute line-residence collapse

Since

\[
L_\rho=\Phi R,
\]

we have

\[
\frac{L_d}{L_u}
=
\frac{\Phi_d}{\Phi_u}
\frac{R_d}{R_u}.
\]

Using the previous estimates,

\[
\frac{L_d}{L_u}
\le
e^{I_+}e^{-2I_+}
=
e^{-I_+}.
\]

Hence

\[
\boxed{
\frac{L_d}{L_u}
\le
\exp\left[
\left(-\frac32+o(1)\right)T
\right].
}
\]

Thus current reversal demands an exponentially strong collapse of

\[
L_\rho
=
\int_\Gamma\rho\,ds.
\]

---

## 4. Tube enstrophy stays nonincreasing

For the material tube enstrophy

\[
dE_{tube}=L_\rho d\Phi,
\]

the same relations give

\[
\frac{E_{tube,d}}{E_{tube,u}}
=
\frac{L_d}{L_u}
\frac{\Phi_d}{\Phi_u}
\le1.
\]

Therefore

\[
\boxed{
E_{tube,d}\le E_{tube,u}.
}
\]

The exponential line-residence loss exactly offsets the critical exponential flux gain.

This is the scaling form of M19-397.

---

## 5. Compare with the coherent critical seed lock

At the coherent pointwise M19-365 lock

\[
\kappa\approx\frac32,
\qquad
\sigma\approx-\frac12,
\]

one has

\[
D_B\log\rho
=
\sigma+\kappa-1
\approx0,
\]

and

\[
D_B\log ds
=
\sigma+\frac12
\approx0.
\]

Therefore a coherent material line element obeys

\[
D_B\log(\rho ds)
\approx0.
\]

Consequently a represented line segment that remains uniformly in the coherent critical lock has

\[
\boxed{
L_\rho(\theta_d)
=
e^{o(T)}
L_\rho(\theta_u),
}
\]

not

\[
L_d/L_u
\le
e^{-3T/2+o(T)}.
\]

Hence a uniformly coherent critical line cannot itself realize current reversal.

---

## 6. Required escape mechanisms

To obtain the required exponential collapse, at least one of the following must occur.

### A. Macroscopic compressive counterphase

A non-negligible fraction of the positive excursion leaves the \((3/2,-1/2)\) lock and produces sufficiently negative

\[
2\bar\sigma_\rho-\frac12
\]

to accumulate

\[
J_+\le-3T+o(T).
\]

An \(o(T)\) transition layer cannot provide this under compact bounded strain.

### B. Amplitude collapse

The residence integral falls because

\[
\rho
\]

becomes exponentially small on the represented line population.

This is an amplitude/nodal/decompactification exit.

### C. Longitudinal length collapse or line replacement

The represented material line length shrinks exponentially, or the line segment carrying the residence measure is replaced/re-referenced.

This is a line/genealogy/representation exit.

### D. Packet-to-current population segregation

The residence-weighted current is carried by a different material population from the critical seed amplifier.

This is the incidence survivor isolated in M19-397.

---

## 7. Quantitative counterphase duration

Let the compact hull give

\[
\left|
2\bar\sigma_\rho-\frac12
\right|
\le S_R^*.
\]

Suppose a critical subinterval of length

\[
T_c=T-o(T)
\]

has

\[
2\bar\sigma_\rho-\frac12
=
-\frac32+o(1)
\]

(the coherent \(\sigma=-1/2\) value).

Its contribution to \(J_+\) is only

\[
-\frac32T_c+o(T).
\]

Current reversal needs

\[
J_+\le-3T+o(T).
\]

Therefore the complementary counterphase must supply an additional negative action of order

\[
\frac32T.
\]

With bounded rate \(S_R^*\), its duration must be

\[
\boxed{
T_{counter}
\gtrsim
c_*T
}
\]

for some compactness-dependent \(c_*>0\).

Thus a sublinear endpoint transition cannot rescue the coherent critical seed.

---

## 8. Canonical critical reversal split

The long critical branch refines to

\[
\boxed{
G_{seed}^{3/2}
+
G_{current}^{reversal}
\Longrightarrow
G_{macroscopic\ compressive\ counterphase}
\lor
G_{amplitude/line\ collapse}
\lor
G_{packet/current\ segregation}
\lor
G_{genealogy/representation\ loss}.
}
\]

The same-packet, uniformly coherent, short-transition branch is closed.

---

## 9. Relation to the stationary seed witness

M19-364 showed that a critical \(3/2\) dormant seed reservoir can be stationary with finite instantaneous resource.

M19-398 does not contradict that scaling witness by itself.

It shows instead that **adding residence-current reversal to the same coherent seed history destroys the simple stationary critical profile** unless an additional macroscopic counterphase or material-population exchange is inserted.

Therefore the stationary survivor is more structured than the original age-only witness:

\[
\boxed{
\text{critical amplification}
+
\text{large compensating residence collapse/transfer}.
}
\]

---

\[
\boxed{\text{M19-398 COMPLETE; CRITICAL CURRENT REVERSAL REQUIRES EXPONENTIAL LINE-RESIDENCE COLLAPSE OR A MACROSCOPIC/GENEALOGICAL ESCAPE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
