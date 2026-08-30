# DSD M5-292 — Satellite Packing/Persistence Threshold for the Amplified Mixed-Norm Branch

Date: 2026-08-30

Parent: `DSD_M5_290_FORMATION_AXIOM_AND_AXIS_PROPERTY_PARALLEL_DECOMPOSITION_2026-08-30.md`

Status: **FORMATION-ENSEMBLE DESCRIPTOR QUANTIFIED / THE AMPLIFIED TYPE-II BRANCH REQUIRES A SPECIFIC SPACE-TIME PACKING OR PERSISTENCE GROWTH, NOT MERELY ONE LARGE-VORTICITY SATELLITE / THE SPARSE BRANCH IS THEREFORE CLEANLY SEPARATED FROM THE SEREGIN-AMPLIFIED BRANCH / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-290 corrected the conceptual split

\[
S_{iso}\quad\text{vs}\quad S_{amp}
\]

by treating both as the same local satellite object with a different collective packing observable.

This note computes that collective observable for a family of comparable natural packets.

The calculation is scale algebra.  Application of any external Type-II exclusion theorem still requires that theorem's full hypotheses, including the weighted energy/dissipation/pressure assumptions audited in M5-288.

---

## 2. One natural packet

Fix a natural satellite length

\[
\ell>0.
\]

A natural-strength velocity packet has the scaling

\[
|u|\sim \ell^{-1}
\]

on spatial volume

\[
\sim \ell^3
\]

for natural time

\[
\sim\ell^2.
\]

Let the outer observation radius be

\[
d=L\ell,
\qquad
L\gg1.
\]

Use scaled time

\[
\sigma=\frac{t-t_0}{\ell^2}.
\]

---

## 3. A family of comparable packets

At scaled time `sigma`, suppose there are

\[
N(\sigma)
\]

pairwise disjoint, or uniformly bounded-overlap, natural packets inside `B_d`.

Assume each retained packet carries a fixed amplitude lower bound

\[
|u|\ge c_0\ell^{-1}
\]

on a fixed fraction of one natural ball.

Then for every finite spatial exponent `s` in the retained mixed-norm range,

\[
\boxed{
\int_{B_d}|u|^s dx
\gtrsim
N(\sigma)\,\ell^{3-s}.
}
\]

Therefore

\[
\boxed{
\left(\int_{B_d}|u|^s dx\right)^{l/s}
\gtrsim
N(\sigma)^{l/s}
\ell^{l(3/s-1)}.
}
\]

---

## 4. Critical mixed-norm scaling

Use the standard scale exponent

\[
\boxed{
\kappa
=2+l\left(\frac3s-1\right).
}
\]

For a time interval corresponding to scaled interval `I_sigma`,

\[
dt=\ell^2d\sigma.
\]

Hence the normalized mixed quantity on the outer radius `d=L ell` satisfies

\[
\begin{aligned}
M_\kappa^{s,l}(u,d)
&\gtrsim
 d^{-\kappa}
\int
N(\sigma)^{l/s}
\ell^{l(3/s-1)}
\ell^2d\sigma\\
&=
L^{-\kappa}
\ell^{-\kappa+l(3/s-1)+2}
\int N(\sigma)^{l/s}d\sigma.
\end{aligned}
\]

By the definition of `kappa`, the power of `ell` cancels exactly.

Thus

\[
\boxed{
M_\kappa^{s,l}(u,d)
\gtrsim
L^{-\kappa}
\int_{I_\sigma}
N(\sigma)^{l/s}d\sigma.
}
\]

This is the desired Formation-ensemble formula.

---

## 5. Define the packing/persistence descriptor

Introduce

\[
\boxed{
\mathcal P_{s,l}
:=
\int_{I_\sigma}
N(\sigma)^{l/s}d\sigma.
}
\]

Then

\[
\boxed{
M_\kappa^{s,l}(u,d)
\gtrsim
L^{-\kappa}\mathcal P_{s,l}.
}
\]

The amplified Type-II observable is schematically

\[
\Pi_{pack}
=g(\ell)M_\kappa^{s,l}.
\]

Therefore crossing the amplified threshold

\[
\Pi_{pack}\ge\varepsilon_0
\]

requires

\[
\boxed{
\mathcal P_{s,l}
\gtrsim
\frac{\varepsilon_0}{g(\ell)}L^\kappa.
}
\]

Since

\[
g(\ell)\to0,
\]

this is a genuinely growing collective requirement.

---

## 6. Constant multiplicity over a persistence interval

Suppose approximately `N` comparable packets coexist for

\[
\Theta
\]

natural times.  Then

\[
\mathcal P_{s,l}
\asymp
\Theta N^{l/s}.
\]

Hence a necessary scaling for the amplified threshold is

\[
\boxed{
\Theta N^{l/s}
\gtrsim
\frac{\varepsilon_0}{g(\ell)}L^\kappa.
}
\]

Equivalently,

\[
\boxed{
N
\gtrsim
\left[
\frac{\varepsilon_0}{g(\ell)\Theta}
L^\kappa
\right]^{s/l}.
}
\]

Thus one natural-strength satellite with `N=1` and `Theta=O(1)` is far below the amplified requirement as `L -> infinity` and `g(ell) -> 0`.

This recovers the M5-289 firewall quantitatively.

---

## 7. Sequential rather than simultaneous packets

Suppose at most one comparable packet is present at a time, but `K` essentially disjoint natural-time episodes occur.

Then

\[
N(\sigma)\in\{0,1\}
\]

and

\[
\mathcal P_{s,l}\asymp K.
\]

Therefore the amplified threshold requires

\[
\boxed{
K
\gtrsim
\frac{\varepsilon_0}{g(\ell)}L^\kappa.
}
\]

So temporal persistence/repetition can replace spatial multiplicity, but only at the same large scale-dependent cost.

---

## 8. Geometric packing ceiling

For disjoint natural balls of radius comparable to `ell` inside `B_d`, one has the trivial geometric ceiling

\[
\boxed{
N(\sigma)\lesssim L^3.
}
\]

If a fixed fraction `phi` of the available packing capacity is occupied,

\[
N(\sigma)\sim\phi L^3,
\qquad
0\le\phi\lesssim1.
\]

For persistence `Theta`, the mixed quantity scales as

\[
M_\kappa
\sim
\Theta
\phi^{l/s}
L^{3l/s-\kappa}.
\]

Since

\[
3l/s-\kappa
=l-2,
\]

we obtain the compact formula

\[
\boxed{
M_\kappa
\sim
\Theta\,\phi^{l/s}L^{l-2}.
}
\]

Thus the amplified observable behaves like

\[
\boxed{
\Pi_{pack}
\sim
g(\ell)\Theta\phi^{l/s}L^{l-2}.
}
\]

This formula makes clear exactly how spatial filling, time persistence, scale separation, and the Type-II gain function compete.

---

## 9. Consequences by temporal exponent

For any admissible exponent pair `(s,l)` to which the external theorem applies:

### If `l<2`

Even maximal geometric packing with bounded `Theta` gives

\[
M_\kappa\lesssim L^{l-2}\to0.
\]

Multiplication by `g(ell)->0` only strengthens the decay.

Hence a bounded-clock amplified scenario cannot be generated by a single-scale disjoint packing in this exponent range.

### If `l=2`

Maximal packing gives at most

\[
M_\kappa\sim \Theta\phi^{2/s},
\]

so `g(ell)->0` again suppresses the amplified observable unless `Theta` or another retained quantity diverges.

### If `l>2`

Spatial multiplicity may in principle compensate the remote factor `L^{-kappa}`.  The required occupancy fraction is

\[
\boxed{
\phi
\gtrsim
\left[
\frac{\varepsilon_0}
{g(\ell)\Theta L^{l-2}}
\right]^{s/l}.
}
\]

This is the natural high-multiplicity lane for further Type-II comparison.

These statements are only scaling consequences.  They do not assert that every exponent range is admissible in a particular external theorem.

---

## 10. Physical kinetic-energy ceiling

At one physical time, one natural packet carries kinetic energy of order

\[
\sim\ell
\]

under the natural-strength scaling.

Thus if all `N` packets are inherited from a solution with physical kinetic-energy bound `E0`, then schematically

\[
\boxed{
N\ell\lesssim E_0.
}
\]

Hence

\[
\boxed{
N\lesssim\frac{E_0}{\ell}.
}
\]

This is another packing ceiling, complementary to `N lesssim L^3`.

However, as emphasized in M5-283, this physical-energy ceiling is not uniform under arbitrary ancient diagonalization and cannot by itself be promoted to a limit-space Liouville condition.

It is therefore retained only as a prelimit capacity constraint.

---

## 11. Updated Formation split

The satellite family can now be partitioned by one quantitative descriptor rather than by informal labels:

\[
\boxed{
\mathscr P_{satellite}
\Longrightarrow
\begin{cases}
\mathcal P_{s,l}
\gtrsim
\varepsilon_0g(\ell)^{-1}L^\kappa,
&\text{amplified packing/persistence lane},\\[2mm]
\mathcal P_{s,l}
\ll
\varepsilon_0g(\ell)^{-1}L^\kappa,
&\text{sparse ancestry lane}.
\end{cases}
}
\]

The first lane may be compared with external Type-II exclusion results once their weighted `A/E/D` hypotheses are independently verified.

The second lane cannot be closed by such a mixed-norm theorem and returns to the detached affine/ancestry problem identified in M5-291.

---

## 12. Audit verdict

### PROVED AS SCALE ALGEBRA UNDER THE PACKET MODEL

For comparable disjoint/bounded-overlap natural packets,

\[
\boxed{
M_\kappa^{s,l}
\gtrsim
L^{-\kappa}
\int N(\sigma)^{l/s}d\sigma.
}
\]

Consequently an amplified scenario requires a quantitatively large space-time packet count/persistence.

### IMPORTANT INTERPRETATION

`S_amp` is not a different local satellite solution class.  It is a collective state of the same satellite atoms satisfying a packing threshold.

### REMAINING BRANCHES

The new parallel-analysis frontier is

\[
\boxed{
\text{hypothetical singularity}
\Longrightarrow
T_{physical/descriptor}
\lor
\mathscr P_{amplified}
\lor
A_{sparse/affine\ ancestry}.
}
\]

The next highest-value step is to compare the packing lower bound with existing finite-memory/turnover capacity bounds.  If a packet family large enough to satisfy the amplified threshold necessarily exceeds the finite coherent storage capacity, then the amplified branch routes to positive-frequency turnover; otherwise it remains a genuine Type-II collective branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
