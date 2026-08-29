# DSD M5-194V — Leray Shape-Speed Four-Channel PDE Ledger

Date: 2026-08-29

Parent: `DSD_M5_194U_FINITE_DESCRIPTOR_OBSERVABILITY_NO_GO_AND_PDE_TANGENT_REDUCTION_AUDIT_2026-08-29.md`

Status: **POSITIVE PDE CHANNEL REDUCTION / A UNIFORMLY POSITIVE ROTATION-ORTHOGONAL SHAPE SPEED ON THE FIXED SIMILARITY CORE FORCES A UNIFORMLY POSITIVE CONTRIBUTION FROM AT LEAST ONE OF FOUR ACTUAL LERAY CHANNELS: DIFFUSION/CURVATURE, SPATIAL HOMOGENEITY DEFECT, NONLINEAR TRANSPORT, OR PRESSURE / THIS IS AN EXACT TRIANGLE-INEQUALITY FORK AFTER LOCALIZATION, NOT YET A CONTRADICTION / DIFFUSION IS AN H-TYPE DERIVATIVE CHANNEL; THE OTHER THREE REQUIRE FURTHER ROUTING / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input shape branch

From M5-194T, on a positive-density set of similarity times, or on the entire surviving shape-dominant subbranch after taking a subsequence, suppose

\[
\boxed{
\|V_s^{shape}(s)\|_{L^2(B_R)}
\ge \sigma_{sh}>0.
}
\]

Here

\[
V_s^{shape}
=(I-P_{rot})V_s,
\]

where `P_rot` is the local `L2(B_R)` orthogonal projection onto the instantaneous rotational tangent span.

Since orthogonal projection is contractive,

\[
\boxed{
\|V_s^{shape}\|_{L^2(B_R)}
\le
\|V_s\|_{L^2(B_R)}.
}
\]

Therefore every shape-speed lower bound is also a lower bound on the full local Leray vector-field magnitude.

---

## 2. Leray equation

The backward similarity equation is

\[
V_s
=
\Delta V
-\frac12V
-\frac12(Y\cdot\nabla)V
-(V\cdot\nabla)V
-\nabla P.
\]

Define the spatial degree-`-1` homogeneity defect

\[
\boxed{
\mathcal G_x[V]
:=
V+(Y\cdot\nabla)V.
}
\]

Then

\[
\boxed{
V_s
=
\Delta V
-\frac12\mathcal G_x[V]
-(V\cdot\nabla)V
-\nabla P.
}
\]

This equation is exact.

---

## 3. Fixed core cutoff

Choose

\[
\chi\in C_c^\infty(B_{2R}),
\qquad
\chi\equiv1\text{ on }B_R.
\]

Because the shape speed is measured on `B_R`,

\[
\sigma_{sh}
\le
\|\chi V_s\|_{L^2(\mathbb R^3)}.
\]

Use the equation:

\[
\chi V_s
=
\chi\Delta V
-\frac12\chi\mathcal G_x[V]
-\chi(V\cdot\nabla)V
-\chi\nabla P.
\]

Hence by the triangle inequality,

\[
\boxed{
\sigma_{sh}
\le
D_R
+\frac12H_R
+N_R
+P_R,
}
\]

where

\[
\boxed{
D_R:=\|\chi\Delta V\|_2,
}
\]

\[
\boxed{
H_R:=\|\chi\mathcal G_x[V]\|_2,
}
\]

\[
\boxed{
N_R:=\|\chi(V\cdot\nabla)V\|_2,
}
\]

and

\[
\boxed{
P_R:=\|\chi\nabla P\|_2.
}
\]

No term has been discarded or assigned a sign.

---

## 4. Four-channel quantitative fork

If all four channels satisfied

\[
D_R<\frac{\sigma_{sh}}4,
\]

\[
\frac12H_R<\frac{\sigma_{sh}}4,
\]

\[
N_R<\frac{\sigma_{sh}}4,
\]

and

\[
P_R<\frac{\sigma_{sh}}4,
\]

then their sum would be strictly below `sigma_sh`, contradiction.

Therefore at every shape-dominant time at least one of

\[
\boxed{
D_R\ge\frac{\sigma_{sh}}4,
}
\]

\[
\boxed{
H_R\ge\frac{\sigma_{sh}}2,
}
\]

\[
\boxed{
N_R\ge\frac{\sigma_{sh}}4,
}
\]

or

\[
\boxed{
P_R\ge\frac{\sigma_{sh}}4
}
\]

must occur.

Thus persistent shape motion is no longer an untyped infinite-dimensional phenomenon. It has a finite PDE-generated witness at every such time.

---

## 5. Positive-density channel selection

Let `E_shape` be a positive-density set supplied by M5-194T.

Partition it into the four measurable channel sets

\[
E_D,\quad E_H,\quad E_N,\quad E_P
\]

according to which threshold above is met, using a deterministic tie-breaking rule.

Since

\[
E_{shape}=E_D\cup E_H\cup E_N\cup E_P,
\]

at least one channel has at least one fourth of the lower time density of the shape set:

\[
\boxed{
\underline d(E_*)
\ge
\frac14\underline d(E_{shape})>0
}
\]

along a suitable long-time sequence.

Hence one actual Leray mechanism must recur with positive time density.

---

## 6. Diffusion channel is a direct derivative witness

If

\[
D_R
=\|\chi\Delta V\|_2
\ge\frac{\sigma_{sh}}4
\]

on a positive-density set, then the fixed core carries a positive recurrent second-derivative amplitude.

In vorticity/strain variables this is one derivative above the normalized first-gradient scale and is directly of the same structural type as the repository's palinstrophy/hyperpalinstrophy `H` channels.

At the minimal level,

\[
\boxed{
E_D\text{ is already a formed local derivative-cost branch.}
}
\]

Turning its pointwise-in-time lower bound into the exact existing `H1/H2` integrated charge requires only the standard positive-density time integration and the previously used local elliptic/curl-div estimates.

No new topology is needed for this branch.

---

## 7. Homogeneity-defect channel

If

\[
H_R
=\|\chi(V+Y\cdot\nabla V)\|_2
\ge\frac{\sigma_{sh}}2,
\]

then the core remains uniformly separated from a spatially degree-`-1` state in the local `L2` topology.

This is a genuine **scale-shape defect**, distinct from the temporal scaling generator `V_s`.

It means the active core cannot pay its perpetual time motion while simultaneously becoming spatially homogeneous.

This channel is closely related to the `M5-194P/Q/R` homogeneity-defect ledgers, but those notes concern the large-radius critical halo. The present `H_R` is a finite-core defect and must not be conflated with a tail defect.

It is therefore retained as a potentially new core-shape channel until linked to variance/projective/first-hitting geometry.

---

## 8. Nonlinear transport channel

If

\[
N_R
=\|\chi(V\cdot\nabla V)\|_2
\ge\frac{\sigma_{sh}}4,
\]

then nonlinear advection is quantitatively active on the fixed similarity core.

This is compatible with several existing DSD mechanisms:

- material replacement/turnover;
- projective strain reorganization;
- internal stretching without center replacement.

But a norm lower bound on `V·nabla V` alone does not identify which mechanism occurs.

For example, a steady or periodic coherent vortex can have order-one advection without material replacement.

Therefore

\[
\boxed{
N_R\text{ large}
\not\Rightarrow T\text{ directly}.
}
\]

A material/contact or strain-action pairing is still required.

---

## 9. Pressure channel

If

\[
P_R
=\|\chi\nabla P\|_2
\ge\frac{\sigma_{sh}}4,
\]

then nonlocal pressure redistribution is quantitatively active on the core.

Pressure is not independent of velocity: globally,

\[
-\Delta P
=\partial_i\partial_j(V_iV_j).
\]

However localization introduces a near/far split.

The near pressure is tied to local nonlinear velocity products by Calderon--Zygmund estimates.

The far pressure is harmonic on the core and is controlled by multipole/tail data rather than local advection alone.

Thus the pressure branch naturally divides into

\[
\boxed{
P_{near}\quad\lor\quad P_{far}.
}

The near branch should merge with `N_R`; the far branch reconnects to the remote-tail/pressure genealogy and is a possible formed nonlocal escape channel.

This split is the next pressure-specific sublemma, not assumed here.

---

## 10. Relation to rotation projection

The four-channel inequality was derived for the full `V_s`, whereas the input lower bound came from `V_s^{shape}`.

This is legitimate because

\[
\|V_s\|_2\ge\|V_s^{shape}\|_2.
\]

But it is not yet sharp: a large PDE channel could primarily generate rotational tangent motion while the shape component is produced by cancellations between channels.

A sharper projected identity would apply `I-P_rot` to every term:

\[
V_s^{shape}
=(I-P_{rot})
\left[
\Delta V
-\frac12\mathcal G_x[V]
-(V\cdot\nabla)V
-\nabla P
\right].
\]

Because `P_rot` depends on `V(s)` but is an instantaneous bounded orthogonal projection, the same triangle inequality gives an analogous four-channel split with each term replaced by its rotation-orthogonal projection.

The unprojected thresholds above are conservative upper witnesses and remain valid.

---

## 11. DSD verdict

### PROVED

Persistent positive shape speed forces positive-density recurrence of at least one of four formed PDE channels:

\[
\boxed{
D\lor H_x\lor N\lor P.
}
\]

### ALREADY ROUTED

- `D`: local derivative/palinstrophy-type `H` cost.

### PARTIALLY ROUTED

- `P_near`: expected to merge with nonlinear transport;
- `P_far`: remote pressure/tail channel.

### GENUINELY REMAINING CORE CHANNELS

- finite-core spatial homogeneity defect `H_x`;
- nonlinear transport that remains coherent without triggering replacement/projective cost.

These are now the two principal shape channels after derivative and far-pressure exits are removed.

---

## 12. Next audit target

The next calculation should pair the nonlinear transport and homogeneity defect with the local velocity itself and with the first-hitting vorticity/strain geometry.

Two useful exact identities are:

\[
\int_{B_R}(V\cdot\nabla V)\cdot V
\]

which reduces to a boundary kinetic-energy flux for divergence-free `V`, and

\[
\int_{B_R}
(V+Y\cdot\nabla V)\cdot V,
\]

which reduces to a bulk/boundary scaling balance.

If the core cutoff boundary flux is small on the pure no-turnover corridor, these pairings may show that large `N_R` or `H_R` cannot remain invisible: they must either pay boundary/material flux or act in a direction orthogonal to `V`, which can then be compared with projective/shape rotation.
