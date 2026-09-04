# DSD M17-098 — Director-area weight makes transverse critical-type switches internal flux redistributions, not charge loss

Date: 2026-09-05
Canonical ID: **M17-098**

Status: **INTERNAL RANK-2 TYPE-SWITCH AUDIT / M17-097 REPLACES ARBITRARY PEAK WEIGHTS BY THE CONSERVED DIRECTOR-AREA FLUX `dPhi_J` ON PEAK SHEETS TRANSVERSE TO `J_xi`. IF A SINGLE FROZEN DIRECTOR-AREA FLUX TUBE CONTINUES TO INTERSECT THE PEAK SHEET UNIQUELY WHILE THE CRITICAL ORDER CHANGES `nu -> nu'`, WITH `J_xi != 0`, `D_k g != 0`, AND NO PEAK BIRTH/DEATH OR CHART EXIT, THE SAME TUBE CARRIES THE SAME `dPhi_J` THROUGH THE TYPE-SWITCH EVENT. CONSEQUENTLY THE SOURCE IN THE OUTGOING `nu` LEDGER IS EXACTLY AN INTERNAL REDISTRIBUTION INTO THE INCOMING `nu'` LEDGER WHEN BOTH ARE DESCRIBED WITH THE SAME FLUX-TUBE LABEL. SUMMING OVER THE FINITE CRITICAL-TYPE FAMILY CONSERVES TOTAL TRANSVERSE PEAK FLUX; TYPE SWITCHING ALONE IS NOT A NONRECYCLABLE DIRECTOR-AREA COST. ONLY TANGENCY, RANK/CURVATURE LOSS, PEAK BIRTH/DEATH, MULTIPLE-INTERSECTION REARRANGEMENT, ENDPOINT, OR CHART/INTERFACE EVENTS CAN CHANGE THE TOTAL TRANSVERSE PEAK-FLUX POPULATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Flux-weighted type ledgers

M17-097 gives, on a peak sheet transverse to the director-area current,

\[
D_k g\neq0,
\qquad
J_\xi=|J_\xi|k\neq0,
\]

and the inherited flux measure

\[
\boxed{d\Phi_J=J_\xi\cdot n_S\,dA.}
\]

For each retained odd critical order

\[
\nu\in\{1,3,5,\ldots,\nu_*\},
\]

define the flux-weighted type distribution

\[
\boxed{
F_\nu^J(z,\theta)
=\int_{\Lambda_\nu(\theta)}
\delta(z-Z_\nu(\lambda,\theta))\,d\Phi_J(\lambda).
}
\]

Its integrated mass is simply the director-area flux carried by tube labels currently assigned type `nu`:

\[
\boxed{
M_\nu^J(\theta)
:=\int F_\nu^J(z,\theta)\,dz
=\int_{\Lambda_\nu(\theta)}d\Phi_J.
}
\]

---

## 2. A clean type-switch event

Consider a single tube label `lambda` for which the peak intersection persists smoothly through a time `theta_*` and changes critical order

\[
\boxed{\nu_-\longrightarrow\nu_+.}
\]

Assume through the event:

1. `J_xi != 0`;
2. `D_k g != 0`, so the tube remains transverse to the peak sheet;
3. the same tube has a unique locally continued peak intersection;
4. no peak is born or destroyed;
5. no rank, curvature, endpoint, interface, or chart exit occurs.

The frozen-in two-form law

\[
(\partial_\theta+\mathcal L_B)\beta_\xi=0,
\qquad
\beta_\xi=\iota_{J_\xi}dV,
\]

implies that the flux carried by this tube label is unchanged through the event.

Thus the same infinitesimal amount

\[
d\Phi_J(\lambda)
\]

leaves the old type class and enters the new type class.

---

## 3. Type source is an internal transfer

Write the flux-weighted continuity equation for each type as

\[
\boxed{
\partial_\theta F_\nu^J
+\partial_zG_\nu^J
=\mathcal B_\nu^J.
}
\]

At a clean switch `nu_- -> nu_+`, the event contributes a sink of size `dPhi_J` to the outgoing integrated source and a source of the same size to the incoming integrated source:

\[
\boxed{
\int \mathcal B_{\nu_-}^J\,dz
=-\dot\Phi_{switch},
}
\]

\[
\boxed{
\int \mathcal B_{\nu_+}^J\,dz
=+\dot\Phi_{switch}.
}
\]

Hence

\[
\boxed{
\sum_\nu\int\mathcal B_\nu^J\,dz
=0
}
\]

for a collection of clean internal type-switch events.

This cancellation is justified only because the same conserved flux-tube label is continued through the switch.

---

## 4. Total transverse peak-flux population

Define

\[
\boxed{
M_{peak}^J(\theta)
:=\sum_{\nu\le\nu_*}M_\nu^J(\theta).
}
\]

If the entire peak population remains transverse, full rank, uniquely tube-labelled, and free of births/deaths/endpoints/interfaces, then internal critical-order switches do not change this total:

\[
\boxed{
\frac d{d\theta}M_{peak}^J=0.
}
\]

Thus the finite type hierarchy behaves as a set of internal states carried by one conserved director-area flux population.

---

## 5. What can change total peak flux

The cancellation in Section 4 fails only when the hypotheses needed to identify the same incoming and outgoing flux tube fail.

The explicit event classes are

\[
\boxed{
\begin{aligned}
&D_k g=0 &&\text{director-area / peak-sheet tangency},\\
&J_\xi\to0 &&\text{rank/director-area degeneration},\\
&b\to0 &&\text{curvature-normalization degeneration},\\
&\text{peak birth/death} &&\text{critical-set topology event},\\
&\text{multiple-intersection rearrangement} &&\text{tube/peak genealogy change},\\
&\text{finite/nondecaying endpoint} &&\text{coverage exit},\\
&\text{chart/interface exit} &&\text{descriptor-domain change}.
\end{aligned}
}
\]

Only these events can alter the total transverse peak-flux population without being a mere internal type relabeling.

---

## 6. Consequence for the hoped-for turnover cost

A tempting closure route was

\[
\text{critical type turnover}
\Longrightarrow
\text{director-area charge loss}.
\]

M17-098 rejects this shortcut.

Under clean transverse type switching,

\[
\boxed{
\text{critical-order change}
\Longrightarrow
\text{director-area flux redistribution only}.
}
\]

Therefore a nonrecyclable cost must come from a stronger event than `Z_nu -> 0` by itself.

---

## 7. Relation to Riccati compensation

The critical order and the Riccati compensation margin are distinct descriptors.

A clean type switch may preserve director-area flux while the new type still has to satisfy

\[
\boxed{\mathcal M^{(\nu_+)}>0.}
\]

Thus flux preservation does not automatically preserve a positive compensation margin.

The next useful joint question is whether a flux tube can recurrently cycle through critical types while keeping the compensation margin positive on every retained peak state.

This requires a joint `(Z_nu, margin)` ledger, but type switching by itself supplies no charge contradiction.

---

## 8. DSD analysis

The corrected descriptor hierarchy is

\[
\boxed{
\text{director-area flux tube}
\to
\text{peak intersection}
\to
\text{finite critical type }\nu
\to
\text{internal type switch}.
}
\]

The flux tube is the persistent carrier; `nu` is an internal state label.

This distinction prevents counting a change of state label as destruction of the carrier.

---

## 9. DSD audit

### Audit A — treating every `Z_nu=0` as flux loss
Rejected.

### Audit B — cancelling type-source terms without a shared carrier
Cancellation is allowed only for the same continued director-area flux-tube label.

### Audit C — ignoring tangency
Rejected. `D_k g=0` is precisely where the M17-097 inherited tube parametrization fails.

### Audit D — promoting total transverse peak-flux conservation through birth/death or rank loss
Rejected.

### Audit E — proof status
Internal critical-order turnover is recyclable at the director-area-flux level. The remaining obstruction must involve compensation failure or a genuine genealogy/interface event.

---

## 10. Updated Rank-2 frontier

On the transverse two-ended decaying pure-kernel branch, the finite type family is carried by a conserved director-area flux population.

Hence

\[
\boxed{
R_{2,peak}^{J\text{-}transverse}
\to
\left\{
\begin{array}{l}
\text{finite internal type cycling},\\
\mathcal M^{(\nu)}>0\text{ at every surviving state}
\end{array}
\right.
\ \lor\
T_{J/rank/peak/interface}.
}
\]

The next high-value gate is not type counting; it is the **joint flux-tube type–margin compatibility gate**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
