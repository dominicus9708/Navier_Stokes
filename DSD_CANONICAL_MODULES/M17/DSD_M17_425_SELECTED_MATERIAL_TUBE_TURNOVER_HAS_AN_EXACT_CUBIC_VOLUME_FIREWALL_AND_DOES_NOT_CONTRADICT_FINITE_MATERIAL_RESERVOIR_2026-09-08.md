# DSD M17-425 — Selected material-tube turnover has an exact cubic volume firewall and does not contradict a finite material reservoir

Date: 2026-09-08  
Canonical ID: **M17-425**

Status: **ACTIVE MATERIAL-LABEL TURNOVER AUDIT / CUBIC VOLUME FIREWALL / NO-GO**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-424

M17-424 proves that one fixed positive-volume material tube cannot remain bounded in similarity space forever.

The natural escape is to let the proof-selected activity-carrying tube band change with record generation.

The present module asks whether infinitely many such selected bands automatically exhaust a finite material volume reservoir.

They do not.

The exact volume cost is cubic in the inverse record scale and is therefore summable on geometric records.

## 2. Physical/similarity scale dictionary

Let the physical similarity scale at record `m` be

\[
r_m:=\sqrt{-t_m}.
\]

Write the growing inverse scale as

\[
R_m:=r_m^{-1}.
\]

Hence

\[
-t_m=r_m^2=R_m^{-2}.
\]

Assume the selected loop has bounded normalized similarity length

\[
0<\ell_*\le\ell_{sim,m}\le\ell^*<\infty.
\]

Then its physical length satisfies

\[
\boxed{
\ell_{ph,m}
=r_m\ell_{sim,m}
\asymp R_m^{-1}.
}
\]

## 3. Normalized amplitude ceiling

Let

\[
W_m=r_m^2\Omega_{ph}
\]

be the similarity/normalized vorticity.

On the retained compact amplitude branch assume

\[
|W_m|\le M_W.
\]

Therefore the physical vorticity ceiling at record `m` is

\[
\boxed{
|\Omega_{ph}|
\le
M_WR_m^2.
}
\]

This growing physical amplitude is the correct scale conversion; a fixed physical amplitude ceiling must not be inserted here.

## 4. Positive flux forces a cubic minimum material volume

Let `T_m` be a regular selected material tube band at record `m`, carrying oriented physical vortex flux

\[
\Phi_m\ge\Phi_*>0.
\]

Let `A_{ph,m}` be a representative cross-sectional area. From the physical vorticity ceiling,

\[
\Phi_m
\le
M_WR_m^2 A_{ph,m}.
\]

Hence

\[
\boxed{
A_{ph,m}
\ge
\frac{\Phi_*}{M_W}R_m^{-2}.
}
\]

Under the regular tube-chart comparability used in the loop branch,

\[
V_m^{ph}
\asymp
\ell_{ph,m}A_{ph,m}.
\]

Thus

\[
\boxed{
V_m^{ph}
\gtrsim
c\frac{\Phi_*}{M_W}R_m^{-3}.
}
\]

The exponent is exactly three.

## 5. The same result from similarity volume

A selected tube that remains `O(1)` in all three normalized similarity dimensions has normalized volume of order one.

Since

\[
dx=r_m^3dy=R_m^{-3}dy,
\]

its physical material volume is automatically

\[
V_m^{ph}\sim R_m^{-3}V_m^{sim}.
\]

Thus the cubic volume scale in Section 4 is also the direct Jacobian scale of the similarity map.

## 6. Infinite disjoint turnover is compatible with finite material volume

Suppose the selected tube bands are pairwise disjoint in material labels and each pays the minimum volume scale

\[
V_m^{ph}\gtrsim cR_m^{-3}.
\]

For geometric record growth

\[
R_m\ge c_0q^m,
\qquad q>1,
\]

we have

\[
\boxed{
\sum_mR_m^{-3}<\infty.
}
\]

Therefore a finite material reservoir can contain infinitely many disjoint selected tube bands of record-cubic shrinking volume.

There is no contradiction from infinite turnover alone.

## 7. Multiplicity form

If record `m` requires `N_m` essentially disjoint selected material tube bands, then the material-volume demand is

\[
\sum_mN_mR_m^{-3}.
\]

A finite material reservoir implies only a bound of the schematic form

\[
\boxed{
\sum_m\frac{N_m}{R_m^3}
\lesssim V_{reservoir}.
}
\]

Therefore a material-volume contradiction requires

\[
\boxed{
\sum_m\frac{N_m}{R_m^3}=\infty.
}
\]

This is the same cubic multiplicity threshold as the M17-405 raw-`H2` ancestral ledger.

## 8. Nested/reused labels are even less contradictory

The selected bands need not be disjoint. They may be nested or repeatedly reuse part of the same material-label population.

In that case finite total material volume gives an even weaker restriction.

Thus neither

\[
N_{records}=\infty
\]

nor

\[
V_m^{ph}\to0
\]

is by itself evidence of a contradiction.

The proof must control material-label overlap/multiplicity, not merely count record times.

## 9. Relation to M17-404--405

The coincidence of cubic exponents is structural:

- material volume under 3D similarity scaling carries `R_m^{-3}`;
- raw-`H2` ancestry also carries `R_m^{-3}`.

Hence material-tube turnover does not produce a cheaper cross-generation currency than raw-`H2`.

Symbolically,

\[
\boxed{
G_{selected\ tube\ turnover}
\Longrightarrow
G_{cubic\ material\ volume\ firewall}
}
\]

unless an additional theorem supplies record-supercubic multiplicity or nonsummable label occupancy.

## 10. Exact correction to a tempting pigeonhole argument

The following inference is invalid:

\[
\text{infinitely many different positive-flux tubes}
\Rightarrow
\text{infinite material volume}.
\]

The correct statement is

\[
\text{positive-flux tube at scale }R_m
\Rightarrow
V_m^{ph}\gtrsim cR_m^{-3},
\]

and these minimum volumes are summable on geometric records.

This is a permanent firewall against a false volume pigeonhole closure.

## 11. What can beat the firewall

A contradiction from material-label turnover requires at least one of:

1. same-scale multiplicity `N_m` comparable to the cubic capacity;
2. positive lower density of tube-label volume independent of record scale;
3. a fixed positive-volume tube forced to remain selected, which M17-424 sends to similarity decompactification;
4. a recurrence/return theorem forcing repeated use of a nonshrinking material-label set;
5. another finite ancestral resource with a weaker ancestry discount.

None is currently certified for the general selected-tube turnover branch.

## 12. Revised tube-genealogy frontier

Combining M17-424--425:

\[
\boxed{
\begin{aligned}
H_{positive\ flux\ selected\ tube}
\Longrightarrow{}&
G_{fixed\ positive\ volume\ tube\ similarity\ decompactification}\\
&\lor G_{record\text{-}dependent\ label\ turnover\ with\ cubic\ volume\ firewall}\\
&\lor G_{flux/amplitude\ loss}\\
&\lor G_{chart/interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

## 13. Next target

The best remaining way to sharpen turnover is to study the **overlap multiplicity in material-label space**.

If the selected positive-flux sets are nested/reused, determine whether differentiation of the label measure forces a persistent material line/tube core and hence returns to M17-424. If they are essentially disjoint, the cubic firewall above is exact.

This label-overlap dichotomy is the target of M17-426.

## 14. DSD audit

The DSD role is to audit which measure is being counted. The mathematical result is ordinary similarity Jacobian scaling, flux-amplitude comparison, and finite-measure packing.

## 15. Audit verdict

**PASS-NO-GO.**

Selected material-tube turnover has an exact `R_m^{-3}` minimum volume scale. Infinite turnover remains compatible with a finite material reservoir on geometric records; a cubic multiplicity or persistent-label theorem is still required.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
