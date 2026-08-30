# DSD M5-357 — Circulation Descendant / Finite-Memory Energy-Packet Gate

Date: 2026-08-30

Status: **CIRCULATION TREE CONVERTED INTO A SCALE-INDEPENDENT ENERGY-OCCUPANCY COUNT / QUIET EXPELLED DESCENDANTS EACH COST `Gamma^2 d ~ O(1)` / FINITE TOTAL ENERGY FORCES POSITIVE-FREQUENCY DESCENDANT LOSS/REFORMATION / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the affine shield

For the saturated affine branch,

\[
\boxed{
\Gamma_j\asymp r_j^{-2/5},
\qquad
 d_j\asymp r_j^{4/5}.
}
\]

Thus

\[
\boxed{
\Gamma_j^2d_j\asymp1.
}
\]

M5-351 and M5-356 show that on a no-H corridor, the next shield cannot obtain its larger circulation from the same material population without either fixed-fraction turnover or divergent viscous palinstrophy.

Hence repeated no-H shield growth produces expelled/replaced material flux populations.

## 2. Quiet coherent descendant

Call an expelled material population a **quiet coherent descendant** if, at a later common time,

1. it remains a connected/comparable vortex bundle;
2. its signed material circulation is still comparable to its exit value `Gamma_j`;
3. its longitudinal and transverse dimensions remain comparable to `d_j` up to fixed constants;
4. there is no strong opposite-sign cancellation inside the bundle;
5. its velocity field on a positive fraction of the bundle remains compatible with the circulation scale `|u-c| ~ Gamma_j/d_j`.

Failure of any of these is assigned to one of the already typed channels:

- viscous circulation loss -> `H_visc`;
- large elongation/aspect-ratio change -> `T_spatial/H_shape`;
- fragmentation -> `T_fragment`;
- opposite-sign mixing/cancellation -> `T_mix/H_gradient`;
- re-entry into a later core -> `T_return`.

## 3. Energy lower bound from circulation

On a regular bundle of diameter/length `~d`, average the circulation over a fixed positive family of comparable cross-sectional loops. Cauchy--Schwarz on the loop family and Fubini over the longitudinal parameter give the standard dimensional lower bound

\[
\boxed{
\int_{\mathcal B}|u-c|^2dx
\ge c_{geom}\,\Gamma^2 d.
}
\]

The constant depends only on the fixed bundle regularity/occupancy parameters.

This estimate may fail for arbitrarily thin/long or violently cancelled bundles; those failures are precisely retained as shape/mixing `H/T` exits rather than ignored.

## 4. Apply to one expelled affine generation

For a quiet descendant of the stage-`j` shield,

\[
E_j^{desc}
\gtrsim
\Gamma_j^2d_j.
\]

Using the affine shield exponents,

\[
\boxed{
E_j^{desc}\ge e_*>0
}
\]

with `e_*` independent of `j` along the comparable saturated corridor.

This is the key difference from the ordinary packet dissipation ledger: the descendant energy occupancy does **not** decay geometrically with the natural scale.

## 5. Material disjointness

Take expelled populations from different turnover generations, with re-used/re-entered material classified separately as `T_return`.

The incompressible Lagrangian flow map is one-to-one. Therefore distinct material populations remain spatially disjoint at every common later time.

Hence their kinetic energies are additive over their current material images:

\[
\int_{\cup_{m=1}^N A_m(t)}|u-c_m|^2dx
=
\sum_{m=1}^N\int_{A_m(t)}|u-c_m|^2dx.
\]

A common Galilean constant is not required: the lower bound is formulated in each bundle relative to its own mean/translation. Passing to absolute kinetic energy costs only the standard mean-motion alternative; if that dominates, it is a momentum/transport turnover channel already audited in M5-261--266.

On the quiet bundle corridor one obtains a uniform absolute-energy occupancy after this mean-motion split.

## 6. Finite-memory count

Let `E0` be the global kinetic-energy bound and `e_*` the scale-independent quiet-descendant energy floor. Then the number of simultaneously surviving quiet descendants satisfies

\[
\boxed{
N_{quiet}(t)
\le
N_E
:=
\left\lfloor\frac{E_0}{c e_*}\right\rfloor.
}
\]

The exact constant includes the relative/mean-motion comparison from the previous section.

Thus an infinite sequence of fixed-fraction turnover events cannot leave every expelled circulation packet quietly persistent.

## 7. Positive-frequency descendant loss

Suppose one new distinct circulation descendant is expelled on each sufficiently late first-hitting generation.

After at most `N_E+1` generations, at least one older descendant must cease to satisfy the quiet-persistence hypotheses.

Therefore every block of at most `N_E+1` late generations contains an event of type

\[
\boxed{
H_{visc/gradient}
\lor
T_{spatial/fragment/mix/return}.
}
\]

Equivalently, descendant loss/reformation has positive lower generation density

\[
\boxed{
d_{loss}\ge (N_E+1)^{-1}>0.}
\]

## 8. Relation to the older finite-memory theorem

Earlier finite-memory audits bounded the number of coherent material populations that can coexist in a bounded natural core.

The present argument is different in emphasis:

- the descendants may have left the current core;
- the energy floor comes from the growing circulation `Gamma_j` and shrinking scale `d_j` through the scale-independent product `Gamma_j^2d_j`;
- the resulting memory count applies to **quiet expelled circulation descendants** in the whole physical flow, not only simultaneous populations stored inside one normalized core.

Thus circulation gives a whole-flow finite-memory mechanism.

## 9. What this still does not close

A positive generation density of H/T events is not yet a contradiction.

Each loss event may itself have a scale-critical physical cost that is summable over generations.

The new gain is narrower: repeated affine turnover cannot hide all old material descendants in a passive zero-cost reservoir. Some secondary H/T reformation must occur with uniformly positive generation frequency.

## 10. Next target

The next audit should ask whether positive-density descendant loss creates branching fast enough to overwhelm geometric scale decay.

A useful tree descriptor is

\[
\mathcal N_k
:=
\#\{\text{active or recently lost descendants at generation }k\},
\]

and a candidate Carleson cost is

\[
\sum_k\mathcal N_k r_k^\beta.
\]

The question is whether material replacement/circulation conservation forces a growth exponent for `N_k` larger than the decay exponent `beta` of the relevant H/T physical cost.

## 11. Firewall

Do not sum relative energies over overlapping spatial sets. The argument uses distinct material populations, hence disjoint images, plus a mean-motion split.

Do not assume quiet descendants stay geometrically comparable forever. Failure of comparability is exactly the descendant-loss event being counted.

Do not claim positive event density is itself a global contradiction.

## 12. Audit verdict

### PROVED ON THE QUIET-DESCENDANT CORRIDOR

- regular vortex bundle energy floor `E >= c Gamma^2 d`;
- affine exponents give a scale-independent energy floor;
- finite total energy bounds the number of simultaneous quiet descendants;
- infinite turnover forces positive-frequency descendant loss/reformation.

### OPEN

- branching/Carleson contradiction from positive-frequency loss;
- cost of cancellation/re-entry branches;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]