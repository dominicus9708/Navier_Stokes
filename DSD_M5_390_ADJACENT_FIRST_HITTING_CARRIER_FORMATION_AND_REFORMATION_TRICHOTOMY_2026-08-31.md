# DSD M5-390 — Adjacent first-hitting carrier formation and reformation trichotomy

Date: 2026-08-31

Status: **THE `T_dyn^unformed` LABEL INTRODUCED IN M5-389 IS TOO BROAD ON THE SMOOTH FIRST-HITTING TRACK / EVERY FIRST-HITTING ENDPOINT HAS A UNIFORM NATURAL-SCALE ANALYTIC/TAYLOR VORTICITY CARRIER, AND ITS MATERIAL IMAGE CAN ALWAYS BE COMPARED WITH THE NEXT ENDPOINT CARRIER / FOR ONE ADJACENT GENERATION THE EXACT ALTERNATIVES ARE FIXED-LAG STRAIN/LIPSCHITZ/DIFFUSION EXPOSURE, POSITIVE MATERIAL CONTACT, OR A FIXED-FRACTION PACKET REPLACEMENT / THUS FAILURE TO FORM ANY CARRIER IS NOT AN INDEPENDENT T MECHANISM; THE REAL DYNAMIC FRONTIER IS A QUANTITATIVE REFORMATION ACTION OR FORMED CONTACT/REPLACEMENT / THIS IS A STRUCTURAL REDUCTION, NOT A GLOBAL CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-389 compressed the remaining tree to

\[
 H_{\rm micro/freq/cap}
 \lor
 T_{dyn}^{unformed}.
\]

The second label was intentionally conservative: it represented turnover so rapid that no stable center/packet/ancestry carrier seemed available for the finite-memory genealogy machinery.

However, the older stage-wide first-hitting analyticity and fixed-lag packet-identity theorem provide more structure than that label acknowledges.

On the smooth pre-singular first-hitting track, a natural-scale carrier can be constructed at **every endpoint**, independently of whether later material ancestry remains quiet.

The correct question is therefore not whether a carrier exists, but what it pays while being transported to the next endpoint.

---

## 2. Stage-wide first-hitting analyticity is uniform in the parent normalization

Let

\[
 W_{j+1}=qW_j,
 \qquad
 r_j=\sqrt{\frac\nu{W_j}}.
\]

For every

\[
 t\in[t_j,t_{j+1}),
\]

the first-hitting definition gives

\[
 \|\omega(t)\|_\infty<W_{j+1}=qW_j.
\]

The short-time vorticity analyticity restart used in the fixed-lag packet theorem therefore supplies, after rescaling by `r_j,W_j`, a fixed analytic radius and for every fixed derivative order `m`

\[
 \boxed{
 \sup_{t\in[t_j,t_{j+1})}
 \|\nabla_y^m\Omega_j(\cdot,t)\|_\infty
 \le C_{m,stage}(q,\nu,m)<\infty
 }
\]

for all sufficiently late stages.

This is an important scope point:

- natural-scale central carrier formation does not require an extra no-H hypothesis;
- the high-frequency H frontier concerns sub-natural/remote/reformed structures, not failure of ordinary smooth analyticity at one first-hitting endpoint.

---

## 3. Every endpoint has a thick signed natural carrier

At a record endpoint choose a maximum point `X_j` and define

\[
 \Omega_j(y)=\frac{\omega(X_j+r_jy,t_j)}{W_j},
 \qquad
 |\Omega_j(0)|=1.
\]

Let

\[
 \xi_j=\Omega_j(0).
\]

Using the uniform normalized Hessian bound from stage-wide analyticity and the maximum condition

\[
 \nabla(\xi_j\cdot\Omega_j)(0)=0,
\]

Taylor gives a fixed radius `a_0>0`, independent of `j`, such that on a cylinder of normalized radius/height comparable to `a_0`,

\[
 \boxed{
 \xi_j\cdot\Omega_j\ge c_0>0.
 }
\]

Consequently each transverse disk carries a fixed normalized signed flux

\[
 \Phi_*\ge c_\Phi a_0^2>0.
\]

In physical variables,

\[
 \boxed{
 \Phi_j^{phys}
 \asymp
 W_jr_j^2\Phi_*
 =
 \nu\Phi_*.
 }
\]

Thus every first-hitting endpoint contains a scale-invariant material-flux seed.

There is no late-stage loss of this endpoint carrier unless the standard smooth first-hitting analyticity input itself fails, which is outside the retained smooth pre-singular track.

---

## 4. Assign a material identity immediately

Inside the stage-`j` Taylor cylinder choose a smaller transverse disk/short cylinder

\[
 A_j^0
\]

whose vorticity has a fixed directed lower bound and whose signed flux is at least

\[
 \Phi_0:=c\nu>0.
\]

Transport it by the incompressible Lagrangian flow:

\[
 \boxed{
 A_j(t)=\Phi_{t_j,t}(A_j^0).
 }
\]

This material identity exists for every smooth pre-singular time, regardless of later geometric distortion.

Therefore later loss of a simple packet shape is not a failure of material ancestry to exist; it is a quantitative deformation/diffusion event of that already-defined carrier.

This removes the semantic loophole in which a difficult geometry is called `unformed` merely because a preferred Eulerian packet label is lost.

---

## 5. Adjacent-stage quiet exposure quantities

Compare the stage-`j` material carrier to the next endpoint at `t_{j+1}`.

Define scale-invariant one-stage exposure quantities of the same type used in the fixed-lag genealogy bridge:

\[
 \boxed{
 \Sigma_j
 :=
 \int_{t_j}^{t_{j+1}}
 \sup_{A_j(t)}|S|\,dt,
 }
\]

\[
 \boxed{
 \Lambda_j
 :=
 \int_{t_j}^{t_{j+1}}
 \sup_{H_j(t)}|\nabla u|\,dt,
 }
\]

where `H_j(t)` is the retained material hull/tube needed for distance control, and

\[
 \boxed{
 \mathcal D_j
 :=
 \frac\nu{W_j}
 \int_{t_j}^{t_{j+1}}
 \sup_{A_j(t)}|\Delta\omega|\,dt.
 }
\]

All three are dimensionless under the first-hitting scaling.

Fix finite thresholds

\[
 L_S,
 \quad L_\Lambda,
 \quad L_D>0.
\]

If one threshold is exceeded, record the stage as a **reformation exposure event**

\[
 \boxed{
 \mathcal R_j^{form}
 :=
 \max\left\{
 \Sigma_j/L_S,
 \Lambda_j/L_\Lambda,
 \mathcal D_j/L_D
 \right\}
 \ge1.
 }
\]

This is a concrete PDE descriptor, not a purely semantic T label.

---

## 6. Quiet transport preserves a coherent ancestor packet

Assume instead

\[
 \Sigma_j\le L_S,
 \qquad
 \Lambda_j\le L_\Lambda,
 \qquad
 \mathcal D_j\le L_D
\]

with the diffusion threshold chosen as in the imported amplitude-location genealogy bridge.

Then the transported material carrier retains:

1. a material inner ball/tube of radius comparable to `r_j`;
2. vorticity magnitude between fixed positive multiples of `W_j`;
3. bounded deformation relative to the one-stage natural scale.

Schematically,

\[
 \boxed{
 B_{\theta r_j}(z_j(t_{j+1}))
 \subset A_j(t_{j+1}),
 \qquad
 c_-W_j\le|\omega|\le c_+W_j.
 }
\]

Here `theta,c_-,c_+>0` depend only on the fixed exposure thresholds and standard first-hitting constants, not on `j`.

Thus in the quiet case the ancestor is a fully **formed material packet** at the next endpoint time.

---

## 7. The next endpoint also has a coherent current packet

At `t_{j+1}`, stage-wide analyticity/Taylor gives a current packet

\[
 C_{j+1}
\]

of radius

\[
 \asymp r_{j+1}=q^{-1/2}r_j
\]

and vorticity

\[
 |\omega|\ge c_EW_{j+1}=c_EqW_j.
\]

Since `q` is fixed, both the ancestor packet and current packet belong to one fixed finite natural-scale class when measured in units of `r_j`.

Hence they can be compared at the same physical time without any all-age compactness limit.

---

## 8. Contact / replacement split

Define the same-time normalized contact fraction

\[
 \boxed{
 \chi_j
 :=
 \frac{|C_{j+1}\cap A_j(t_{j+1})|}{r_j^3}.
 }
\]

The current packet has fixed positive normalized volume

\[
 |C_{j+1}|/r_j^3=V_C>0.
\]

Choose

\[
 0<\chi_0<V_C.
\]

There are exactly two quiet alternatives.

### A. Positive material contact

If

\[
 \chi_j\ge\chi_0,
\]

then a fixed fraction of the next high-vorticity packet is literally old stage-`j` material.

This is a formed **bounded-age return/contact** event.

### B. Packet replacement

If

\[
 \chi_j<\chi_0,
\]

then

\[
 \boxed{
 |C_{j+1}\setminus A_j(t_{j+1})|
 \ge c_Vr_j^3,
 \qquad
 |\omega|\ge c_EqW_j.
 }
\]

At the same time the quiet ancestor packet still contains a fixed high-vorticity old-material population.

Thus there are two non-identical formed material populations at one comparable natural scale:

\[
 \boxed{
 \text{surviving old carrier}
 +
 \text{new current carrier}.
 }
\]

This is a rigorous packet replacement/multicore event.

---

## 9. Adjacent first-hitting master trichotomy

Combining Sections 5--8 gives for every sufficiently late adjacent stage

\[
 \boxed{
 \text{stage }j\to j+1
 \Longrightarrow
 \mathcal R_j^{form}
 \lor
 R_j^{contact}
 \lor
 T_j^{replacement}.
 }
\]

where

\[
 \mathcal R_j^{form}
 =
 \text{fixed-lag strain/Lipschitz/diffusion exposure},
\]

\[
 R_j^{contact}
 =
 \text{positive old-material contact with the new core},
\]

and

\[
 T_j^{replacement}
 =
 \text{formed old/new packet coexistence}.
\]

There is no fourth option

\[
 \boxed{
 \text{``no carrier can be formed.''}
 }
\]

on the smooth first-hitting track.

---

## 10. Relation to natural scale-invariant flux replacement

Each endpoint carrier has signed flux of physical order

\[
 W_jr_j^2\asymp\nu.
\]

Therefore once the quiet replacement branch additionally lies in the coherent directed-flux geometry used by the scale-invariant flux-replacement theorem, the old/new packet replacement is a fixed absolute flux replacement.

It then routes to

\[
 \boxed{
 \text{viscous flux change}
 \lor
 \text{projective reorganization}
 \lor
 T_{export}
 \lor
 T_{multi-flux}
 \lor
 H_{coherence\ loss}.
 }
\]

The finite-memory replacement theorem removes indefinite local `T_multi-flux` storage on positive-density fixed-lag recurrence and forces a positive-frequency costed exit.

M5-385--388 then reduce old return/export on the formed no-H corridor to H or the complete weak-critical Liouville endpoint.

This later machinery is **conditional on entering its directed/coherent recurrence hypotheses**; M5-390 does not silently assert those hypotheses for every arbitrary contact/replacement stage.

---

## 11. What M5-390 actually removes

M5-390 removes the overly broad final label

\[
 T_{dyn}^{unformed}
\]

as a description of failure to construct any finite-scale carrier.

The correct dynamic difficulty is instead explicit:

\[
 \boxed{
 \mathcal R_{form}
 \lor
 R_{contact}
 \lor
 T_{replacement}.
 }
\]

The last two are formed genealogy objects.

The first is an actual PDE action, not a failure of notation.

Thus the remaining global problem is to price or route `R_form`, and to show that recurrent contact/replacement enters the already-developed fixed-flux/genealogy closures often enough.

---

## 12. DSD audit

### Valid

- endpoint carrier comes from standard smooth first-hitting analyticity/Taylor thickness;
- material identity is assigned by the exact flow map immediately at formation;
- later geometric loss is measured by exposure instead of erasing the carrier label;
- comparison is at one adjacent fixed lag, avoiding all-age ancestry assumptions;
- low contact is a same-time coexistence statement, not a claim of contradiction.

### Firewall

- Large `Sigma_j`, `Lambda_j`, or `D_j` is not automatically a globally contradictory H budget; it is the common reformation action to analyze next.
- Contact may dominate indefinitely; positive contact alone is not a contradiction.
- Packet replacement does not automatically satisfy the positive-middle directed-flux hypotheses; those must be verified before invoking the flux-replacement theorem.
- The stage-wide analytic constants control natural-scale derivatives but do not rule out remote/sub-natural H elsewhere.

---

## 13. Updated frontier

The post-M5-389 frontier should therefore be refined from

\[
 H_{micro/freq/cap}
 \lor
 T_{dyn}^{unformed}
\]

to

\[
 \boxed{
 H_{micro/freq/cap}
 \lor
 \mathcal R_{form}
 \lor
 R_{contact}
 \lor
 T_{replacement}.
 }
\]

Here `contact` and `replacement` are formed adjacent-stage genealogy events, not untyped T.

On recurrent coherent subcorridors they reconnect to the existing fixed-lag flux/finite-memory/export machinery.

The next highest-value target is the common exposure action

\[
 \boxed{
 \mathcal R_{form}
 =
 \text{strain/Lipschitz/diffusion needed to destroy one natural carrier before the next stage}.
 }
\]

The question is whether positive-density `R_form` can be converted to `H_micro/freq/cap`, or to a nonsummable critical action already forced by first-hitting growth.

---

## 14. Audit verdict

### NEW STRUCTURAL REDUCTION

\[
 \boxed{
 \text{adjacent first-hitting evolution}
 \Longrightarrow
 \mathcal R_{form}
 \lor
 R_{contact}
 \lor
 T_{replacement}.
 }
\]

### REMOVED AS AN INDEPENDENT FINAL CONCEPT

`T_dyn^unformed` interpreted as absence of any formable natural-scale material carrier.

### STILL OPEN

- recurrent fixed-lag exposure/reformation action;
- contact-dominated genealogy outside already closed coherent corridors;
- replacement without the directed positive-middle hypotheses;
- `H_micro/freq/cap` itself;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
