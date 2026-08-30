# DSD M5-313 — Formation Second-Moment Cancellation No-Go and Source-Local Variance Routing

Date: 2026-08-30

Parent: `DSD_M5_312_VOLUME_FILLING_TRANSITION_CLOUD_MIXED_NORM_VS_WEIGHTED_DISSIPATION_AUDIT_2026-08-30.md`

Status: **FORMATION/AXIAL PARALLEL ANALYSIS / DECOMPOSITION-LEVEL SECOND-MOMENT POSITIVITY IS NOT A NAVIER–STOKES COERCIVE OBSERVABLE / EXACT FIRST-MOMENT STRAIN CANCELLATION CAN ALSO REMOVE THE LOCAL PRESSURE/BETCHOV RESPONSE BECAUSE THE PDE SEES THE TOTAL STRAIN, NOT THE ARTIFICIAL PACKET DECOMPOSITION / THE POSITIVE SECOND MOMENT BECOMES LEGITIMATE ONLY AFTER RETURNING TO SPATIALLY DISJOINT SOURCE CELLS, WHERE IT IS ALREADY REPRESENTED BY PACKETWISE KINETIC/DISSIPATIVE COSTS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Question

After M5-299--312, a dense cloud may have individual leading far-strain tensors

\[
K_i\in \mathrm{Sym}_0(3)
\]

with large absolute interaction

\[
\sum_i |K_i|\gg1
\]

but bounded total output because of tensor cancellation,

\[
\sum_iK_i\approx0.
\]

A tempting next step is to define the positive second moment

\[
\mathcal C_2:=\sum_i K_i\otimes K_i
\]

and argue that it must appear in pressure, Betchov, or another quadratic Navier--Stokes identity.

This note audits that shortcut.

---

## 2. Formation distinction: packet descriptors are not PDE state variables

The decomposition

\[
S_{far}=\sum_iK_i
\]

is a useful **formation descriptor** for resolving source populations.

But the Navier--Stokes equation at the observation point contains only the total field

\[
S_{tot},\quad \omega_{tot},\quad u_{tot},\quad p_{tot}.
\]

The labels `i` are not independent PDE fields.

Therefore any expression that depends on the chosen packet decomposition must be justified by a spatial orthogonality/localization argument before it can be used as a coercive Navier--Stokes quantity.

---

## 3. Pressure sees the total gradient

For incompressible Navier--Stokes,

\[
-\Delta p
=\partial_i u_j\,\partial_j u_i
=|S|^2-\frac12|\omega|^2.
\]

If

\[
S=\sum_iK_i,
\]

then

\[
|S|^2
=\left|\sum_iK_i\right|^2
=\sum_i|K_i|^2
+2\sum_{i<j}K_i:K_j.
\]

Thus exact tensor cancellation

\[
\sum_iK_i=0
\]

implies

\[
|S|^2=0
\]

at that observation point even though

\[
\sum_i|K_i|^2>0.
\]

The negative cross terms exactly cancel the decomposition-level second moment.

Hence

\[
\boxed{
\sum_iK_i=0,
\quad
\sum_iK_i\otimes K_i>0
\not\Rightarrow
\text{positive pressure-Hessian/source cost at the same point}.
}
\]

---

## 4. Betchov and vorticity stretching have the same firewall

The local stretching production is

\[
\omega^TS\omega,
\]

and the Betchov cubic structure is expressed through the **total** trace-free gradient/strain invariants.

Neither identity contains an intrinsic term

\[
\sum_i K_i\otimes K_i
\]

attached to an arbitrary source partition.

Therefore exact angular/source cancellation can hide the leading remote contribution from these local identities as well.

This does not say that dense cancellation is dynamically easy. It says only that the positivity of a decomposition-level covariance is not by itself a standard PDE coercivity argument.

---

## 5. Where the second moment becomes legitimate

Suppose instead that the packet sources occupy pairwise essentially disjoint natural cells `C_i`.

Then physical integrals decompose with nonnegative summands, for example

\[
\int_{\cup_iC_i}|\nabla u|^2
=\sum_i\int_{C_i}|\nabla u|^2
\]

up to bounded-overlap localization errors.

For an occupied natural packet of scale `ell`, the retained packet normalization supplies

\[
\int_{C_i}|u-c_i|^2\gtrsim \ell,
\]

and natural-frequency occupancy gives a corresponding derivative scale

\[
\int_{C_i}|\nabla u|^2\gtrsim \ell^{-1}
\]

in physical units, or order-one in the packet-normalized dimensionless ledger.

Thus packet multiplicity really does produce positive additive cost when measured **at the source cells themselves**.

This is exactly the mechanism already recorded in M5-296, M5-301, and M5-302.

---

## 6. Relation to the packet persistence budget

If `N` occupied packets persist for `Theta` natural times, M5-301 gives schematically

\[
E(d)\gtrsim \frac{N\Theta}{L},
\]

and with `f=Theta/L^2`,

\[
E_f(d)\gtrsim \frac{N\Theta^2}{L^3}.
\]

This is the correct positive second-moment analogue:

- not `sum K_i tensor K_i` at one observation point;
- but the sum of nonnegative packet-local derivative energies across disjoint source cells.

Therefore dense cancellation may hide the **far-field tensor sum**, but it cannot erase packetwise source-local dissipation if the packets are genuinely occupied and persistent.

---

## 7. Exact-symmetry firewall

A perfectly symmetric cloud can in principle satisfy

\[
\sum_i K_i=0
\]

for geometric reasons and can preserve this equality under a symmetry-compatible evolution.

One must therefore not argue from generic codimension or random-orientation intuition.

The admissible proof alternatives are instead:

\[
\boxed{
\text{dense cancelling cloud}
\Longrightarrow
\begin{cases}
\text{packet-local additive kinetic/dissipative cost},\\
\text{dynamic turnover/birth/death/boundary cost},\\
\text{or an exact/near-exact silent symmetry class requiring separate rigidity.}
\end{cases}
}
\]

---

## 8. Updated formation interpretation

The cloud has two different observable levels.

### Observation level

\[
\mathcal O_1=\sum_iK_i.
\]

This may cancel.

### Source level

\[
\mathcal O_{src}
=\sum_i\mathcal E_i,
\qquad
\mathcal E_i\ge0.
\]

This cannot cancel across disjoint cells.

The second level is the legitimate place to exploit multiplicity.

Thus the next useful branch is not an abstract tensor covariance branch but

\[
\boxed{
C_{dense,cancel}
\Longrightarrow
C_{silent/symmetric}
\lor
T_{dynamic}
\lor
\text{source-local packet budget saturation}.
}
\]

---

## 9. Audit verdict

### Proved / corrected

- decomposition-level second moment `sum K_i tensor K_i` is not an intrinsic local NSE observable;
- pressure and Betchov depend on the total field and may fully reflect first-order cancellation;
- spatially disjoint packet-local energy and dissipation are genuine nonnegative additive quantities;
- M5-301/302 already provide the correct positive multiplicity budget.

### Still open

- rigidity of exact/near-exact silent symmetric clouds;
- whether packet-local additive cost plus the existing global/weighted budgets closes all dense-cancelling persistence regimes;
- dynamic turnover when symmetry is maintained through packet birth/death or reorientation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
