# M19-403 — Pure radial annularization of the nested GMS floor can produce only logarithmic scale multiplicity, far below the linear palinstrophy threshold

Date: 2026-09-18

Status: **NEW GMS NO-GO / M19-317 SHOWS THAT THE M17-307 INVERSE-RECORD WEIGHT REQUIRES EFFECTIVELY LINEAR MULTIPLICITY \`N_R\gtrsim R\` OR EQUIVALENT SUPERCRITICAL PER-EVENT GAIN. A NESTED GMS FLOOR HOLDS AT EVERY SMALL RADIUS, BUT AFTER CONVERTING IT INTO PAIRWISE NONOVERLAPPING FIXED-RATIO PARABOLIC ANNULI BETWEEN SCALES \`r\` AND \`Rr\`, THE NUMBER OF DISJOINT RADIAL SCALE SLOTS IS ONLY \`O(log R)\`. THEREFORE A PURE DYADIC/LOG-RADIAL NONREUSE THEOREM CANNOT BY ITSELF DEFEAT THE PALINSTROPHY ANCESTRY DISCOUNT. ANY SUCCESSFUL GMS ROUTE MUST CREATE SAME-SCALE SPATIAL/TEMPORAL/ANGULAR MULTIPLICITY OF ORDER R, OR A SUPERCRITICAL PER-ANNULUS PAYMENT, OR A DIFFERENT SUBCRITICAL PHYSICAL GAIN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M19-317

For a second-generation record factor \(R_m\),

\[
\sum_m R_m^{-1}p_m<\infty.
\]

If record \(m\) contains \(N_m\) genuinely disjoint palinstrophy payments with fixed normalized size,

\[
p_{m,k}\ge c_*>0,
\]

then

\[
p_m\ge c_*N_m.
\]

Hence a contradiction requires

\[
\boxed{
\sum_m\frac{N_m}{R_m}=\infty.
}
\]

For geometric records,

\[
R_m\asymp q^{m/2},
\]

the natural threshold is

\[
\boxed{
N_m\gtrsim R_m
}
\]

on a sufficiently persistent set of records.

---

## 2. Fixed-ratio parabolic annuli

Let the candidate singular point be \(z_*=(X_*,T^*)\) and use the parabolic radius

\[
\rho_*(x,t)
=
\max\{|x-X_*|,\sqrt{T^*-t}\}.
\]

Fix constants

\[
0<c<C<\infty.
\]

For a scale \(\rho>0\), define a fixed-ratio annular region schematically by

\[
\mathcal A(\rho)
=
\{c\rho<\rho_*(x,t)<C\rho\}.
\]

Two such annuli can be pairwise disjoint only if their scales are separated by a fixed multiplicative factor.

Choose

\[
\Lambda>\frac{C}{c}.
\]

Then a disjoint geometric family has scales

\[
\rho_n=\rho_0\Lambda^n.
\]

---

## 3. Count the available radial scale slots

Suppose one record spans composite radii between

\[
\rho_{\min}=r
\]

and

\[
\rho_{\max}=Rr.
\]

The number \(N_{\rm rad}(R)\) of pairwise disjoint fixed-ratio annuli satisfies

\[
\rho_0\Lambda^{N_{\rm rad}-1}
\lesssim
R\rho_0.
\]

Thus

\[
\Lambda^{N_{\rm rad}-1}
\lesssim R,
\]

and therefore

\[
\boxed{
N_{\rm rad}(R)
\le
C_0+C_1\log R.
}
\]

Hence the continuum of nested radii provides only logarithmically many **disjoint** fixed-ratio radial scale cells.

---

## 4. Consequence for the M17-307 ledger

Even under the optimistic hypothesis that every disjoint annulus carries a fixed normalized palinstrophy payment

\[
p_{m,k}\ge c_*>0,
\]

pure radial scale separation yields at most

\[
p_m
\gtrsim
c_*\log R_m
\]

from this counting mechanism.

The M17-307 contribution is then

\[
\frac{p_m}{R_m}
\gtrsim
c_*
\frac{\log R_m}{R_m}.
\]

For geometric

\[
R_m\asymp q^{m/2},
\]

one has

\[
\boxed{
\sum_m
\frac{\log R_m}{R_m}
<\infty.
}
\]

Therefore

\[
\boxed{
\text{fixed payment on every disjoint radial GMS annulus}
\not\Rightarrow
\text{M17-307 contradiction}.
}
\]

---

## 5. Continuum-radii version gives the same logarithm

One might try to avoid dyadic discretization and integrate over all logarithmic scales.

But the natural scale measure is

\[
d\log\rho=\frac{d\rho}{\rho}.
\]

Across the range

\[
r\le\rho\le Rr,
\]

its total size is

\[
\int_r^{Rr}\frac{d\rho}{\rho}
=
\log R.
\]

Thus even an idealized scale-density payment of order one per unit log scale produces only

\[
O(\log R)
\]

total radial scale multiplicity.

The obstruction is geometric, not an artifact of dyadic sampling.

---

## 6. Relation to the nested GMS floor

M19-254 gives a singular lower floor at every sufficiently small nested radius.

M19-315 correctly warns that the same central concentration may pay many nested scales.

Suppose a future localization theorem removes that reuse completely and assigns each logarithmically separated radius to a distinct annular derivative packet.

M19-403 shows that **even this ideal radial nonreuse is still insufficient** for the palinstrophy ancestry ledger.

The missing factor is not another \(\log R\).

It is essentially

\[
\boxed{
\frac{R}{\log R}.
}
\]

---

## 7. What kind of multiplicity could still work

A successful multiplicity mechanism must therefore be non-radial.

Examples include:

### A. Same-scale spatial multiplicity

At one composite radius \(\rho\), force

\[
N_{\rm spatial}(\rho)\gtrsim R
\]

genuinely disjoint derivative packets.

### B. Same-scale temporal multiplicity

Within one parent/record epoch, force \(O(R)\) disjoint own-scale time episodes carrying fixed palinstrophy charge.

### C. Angular / topological multiplicity

Force \(O(R)\) independent coherent sectors, tubes, sheets, or interfaces at comparable scale with bounded derivative-measure overlap.

### D. Per-event amplification

Avoid multiplicity and prove one event has

\[
p_m\gtrsim \frac{R_m}{m^\alpha}
\]

or any rate \(a_m\) with

\[
\sum_m \frac{a_m}{R_m}=\infty.
\]

### E. Subcritical physical transfer

Obtain an extra positive power of the physical scale so the restored cost is better than

\[
\rho^{-1}.
\]

---

## 8. Relation to M19-318--321

M19-318 already certifies one annular palinstrophy payer.

M19-319--321 show the canonical record carrier has only order-one total normalized

\[
q_1
\]

and a fixed own-scale spectral band.

Therefore any proposed \(O(R)\) same-record fixed-cost multiplicity would immediately force a dramatic change from the current canonical carrier structure.

It cannot be obtained by merely partitioning the already-certified order-one payer.

It would require genuinely additional independent carrier structure.

---

## 9. Permanent firewall

Do not use

\[
\text{GMS floor at every radius}
\]

as though it automatically supplied

\[
N_R\sim R
\]

independent payers.

Even under perfect annular nonreuse,

\[
\boxed{
N_{\rm radial}(R)=O(\log R).
}
\]

Thus

\[
\boxed{
\mathcal T_{GMS}^{pal/mult}
}
\]

must now be understood as a **same-scale multiplicity / supercritical-payment / subcritical-transfer theorem**, not merely a better dyadic annularization theorem.

---

\[
\boxed{\text{M19-403 COMPLETE; PURE RADIAL GMS NONREUSE IS LOGARITHMIC AND CANNOT MEET THE LINEAR PALINSTROPHY MULTIPLICITY THRESHOLD.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
