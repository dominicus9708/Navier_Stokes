# DSD M5-395 — Target-volume replacement forces fixed target-flux replacement

Date: 2026-08-31

Status: **THE LOW-CONTACT / TARGET-REPLACEMENT BRANCH OF M5-390 IS STRONGER THAN A VOLUME-COEXISTENCE STATEMENT / BECAUSE THE CURRENT FIRST-HITTING TAYLOR CYLINDER HAS A UNIFORM DIRECTED VORTICITY LOWER BOUND THROUGHOUT ITS VOLUME, ANY FIXED FRACTION OF CURRENT CARRIER VOLUME NOT OCCUPIED BY THE PREVIOUS MATERIAL CARRIER FORCES, BY FUBINI, A TRANSVERSE SLICE ON WHICH THE NON-PARENT MATERIAL OCCUPIES A FIXED FRACTION OF AREA / THAT SLICE CARRIES A FIXED DIRECTED VORTICITY FLUX OF PHYSICAL ORDER `W r^2 = nu` / THUS ORDINARY TARGET-VOLUME REPLACEMENT AUTOMATICALLY ENTERS THE FIXED-FLUX GENEALOGY LEDGER, WITHOUT THE POSITIVE-MIDDLE AFFINE GEOMETRY PREVIOUSLY USED TO CREATE A REPLACEMENT FLUX FRACTION / THIS DOES NOT BY ITSELF CLOSE REPLACEMENT, BUT IT REMOVES THE GAP BETWEEN VOLUME REPLACEMENT AND FLUX REPLACEMENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-390 gives an adjacent-stage trichotomy

\[
\text{stage }j\to j+1
\Longrightarrow
\mathcal R_j^{form}
\lor
R_j^{contact}
\lor
T_j^{replacement}.
\]

On the quiet replacement branch, the next first-hitting Taylor carrier contains a fixed positive volume of material that is not contained in the previous carrier image.

The older scale-invariant flux-replacement theorem obtained a fixed replacement flux fraction in a more specialized coherent positive-middle geometry.

The present question is simpler and more general:

> Does a fixed target-volume replacement inside the ordinary first-hitting Taylor carrier already force a fixed target-flux replacement?

The answer is yes.

The only ingredients are:

1. the uniform directed vorticity lower bound throughout the current Taylor cylinder;
2. a fixed uncovered target-volume fraction;
3. Fubini on transverse slices;
4. the first-hitting identity `W r^2 = nu`.

---

## 2. Current Taylor cylinder

At the next first-hitting endpoint `t_{j+1}`, let

\[
W_{j+1}=qW_j,
\qquad
r_{j+1}=\sqrt{\frac{\nu}{W_{j+1}}}.
\]

By the stage-wide analyticity/Taylor carrier theorem, choose a cylinder

\[
C_{j+1}
=
\left\{
X_{j+1}+z\xi_{j+1}+y:
|z|<h r_{j+1},
\ y\perp\xi_{j+1},
\ |y|<a r_{j+1}
\right\}
\]

with fixed `a,h>0`, independent of the late stage index, such that

\[
\boxed{
\xi_{j+1}\cdot\omega(x,t_{j+1})
\ge c_0W_{j+1}
\qquad
(x\in C_{j+1})
}
\]

for a fixed `c_0>0`.

Let

\[
D_z
:=
\left\{
X_{j+1}+z\xi_{j+1}+y:
 y\perp\xi_{j+1},
 |y|<a r_{j+1}
\right\}
\]

be the transverse disk at axial coordinate `z`.

Its area is

\[
|D_z|=\pi a^2r_{j+1}^2.
\]

The cylinder volume is

\[
|C_{j+1}|
=2hr_{j+1}|D_z|
\asymp r_{j+1}^3.
\]

---

## 3. Previous material carrier and target coverage

Let

\[
A_j(t_{j+1})
\]

be the material image at `t_{j+1}` of the previous stage carrier selected in M5-390.

Define the target coverage fraction

\[
\boxed{
\alpha_j
:=
\frac{|C_{j+1}\cap A_j(t_{j+1})|}
{|C_{j+1}|}.
}
\]

Fix

\[
0<\delta<1.
\]

The fixed target-volume replacement branch is

\[
\boxed{
\alpha_j\le1-\delta.
}
\]

Equivalently, the non-parent target set

\[
N_j
:=
C_{j+1}\setminus A_j(t_{j+1})
\]

satisfies

\[
\boxed{
|N_j|
\ge
\delta |C_{j+1}|.
}
\]

The label `non-parent` is deliberate.

The material in `N_j` need not be newly created physical material and need not be young.

It simply does not belong to the selected stage-`j` parent carrier.

Thus the statement is about ancestry replacement relative to that parent, not spontaneous creation of matter or vorticity.

---

## 4. Fubini extracts a fixed-area replacement slice

For each axial coordinate `z`, define

\[
N_{j,z}:=N_j\cap D_z.
\]

By Fubini,

\[
|N_j|
=
\int_{-hr_{j+1}}^{hr_{j+1}}
|N_{j,z}|\,dz.
\]

If every slice obeyed

\[
|N_{j,z}|<\delta |D_z|,
\]

then

\[
|N_j|
<
2hr_{j+1}\delta|D_z|
=
\delta|C_{j+1}|,
\]

contradicting Section 3.

Hence there exists at least one slice `z=z_*` such that

\[
\boxed{
|N_{j,z_*}|
\ge
\delta |D_{z_*}|.
}
\]

Thus fixed three-dimensional target replacement forces a fixed two-dimensional replacement fraction on at least one transverse current-carrier slice.

No connectedness assumption is required.

---

## 5. The replacement slice carries fixed directed flux

On the whole current Taylor cylinder,

\[
\xi_{j+1}\cdot\omega
\ge c_0W_{j+1}.
\]

Therefore on the measurable non-parent surface patch `N_{j,z_*}`,

\[
\begin{aligned}
\Phi_{j+1}^{nonparent}
&:=
\int_{N_{j,z_*}}
\omega(x,t_{j+1})\cdot\xi_{j+1}\,dA\\
&\ge
c_0W_{j+1}|N_{j,z_*}|\\
&\ge
c_0\delta W_{j+1}|D_{z_*}|.
\end{aligned}
\]

Since

\[
|D_{z_*}|
=\pi a^2r_{j+1}^2,
\]

we obtain

\[
\boxed{
\Phi_{j+1}^{nonparent}
\ge
c_0\delta\pi a^2
W_{j+1}r_{j+1}^2.
}
\]

Using

\[
W_{j+1}r_{j+1}^2=\nu,
\]

this becomes

\[
\boxed{
\Phi_{j+1}^{nonparent}
\ge
c_{rep}\nu,
\qquad
c_{rep}:=c_0\delta\pi a^2>0.
}
\]

Thus target-volume replacement automatically contains a fixed absolute directed replacement flux.

---

## 6. The old part of the same slice is also well typed

The complementary old-parent part is

\[
O_{j,z_*}
:=
D_{z_*}\cap A_j(t_{j+1}).
\]

Because the whole disk has the same directed lower bound,

\[
\int_{O_{j,z_*}}
\omega\cdot\xi_{j+1}\,dA
\ge
c_0W_{j+1}|O_{j,z_*}|.
\]

The theorem does not require the old part to carry a fixed fraction.

Two subcases are possible:

1. the old part also has fixed area/flux, producing simultaneous old/new current flux populations;
2. the old part is small, in which case the current carrier is overwhelmingly non-parent flux.

Both are stronger genealogy statements than a mere volume replacement label.

---

## 7. Material identity of the non-parent flux patch

Although `N_{j,z_*}` need not be connected or contain an open planar disk, it is a measurable subset of the smooth transverse disk `D_{z_*}`.

Because the flow is a smooth diffeomorphism on the pre-singular interval, every point of this patch has a unique material label.

Parameterize the current disk by a smooth planar parameter domain and pull `N_{j,z_*}` back by the flow map to an earlier comparison time.

The material-surface flux identity of M5-393 is pointwise in the surface parameters before integration, so it can be integrated over a measurable parameter subset.

Therefore no artificial connectedness assumption is needed to assign a material flux ancestry to the replacement patch.

If desired for later smooth geometric arguments, one may approximate the measurable patch in area/flux while retaining a fixed fraction of `c_rep nu`; such regularization is a later technical step and is not needed for the present flux lower bound.

---

## 8. Generic target-flux replacement theorem

Combining Sections 3--7 gives

\[
\boxed{
\alpha_j\le1-\delta
\Longrightarrow
\Phi_{j+1}^{nonparent}
\ge c_{rep}\nu.
}
\]

Equivalently,

\[
\boxed{
T_{\rm target\ volume\ replacement}
\Longrightarrow
T_{\rm fixed\ target\ flux\ replacement}.
}
\]

The constant `c_rep` depends only on the fixed Taylor-cylinder constants and the selected replacement fraction `delta`, not on the late first-hitting stage.

This is scale invariant.

---

## 9. Relation to the older positive-middle flux replacement theorem

The older scale-invariant flux replacement theorem obtained a fixed replacement flux fraction from a more specialized coherent positive-middle / ribbon geometry.

The present lemma is logically different.

It assumes the replacement has already been detected as a fixed target-volume fraction inside the standard first-hitting Taylor carrier.

Then the directed Taylor lower bound and Fubini alone create the fixed replacement flux.

Therefore the positive-middle affine geometry is **not required for the volume-to-flux upgrade itself**.

However, DSD scope discipline requires the following distinction:

- downstream arguments that use only `fixed old/new directed flux`, material transport, finite memory, export, or viscous flux loss may be reused after this lemma;
- any downstream step that uses the special positive-middle eigengeometry, ribbon orientation, or affine shield law must keep those hypotheses explicitly.

This note does not silently import positive-middle-specific conclusions into arbitrary Taylor replacement.

---

## 10. Consequence for the adjacent-stage trichotomy

M5-390 gave

\[
\text{stage }j\to j+1
\Longrightarrow
\mathcal R_j^{form}
\lor
R_j^{contact}
\lor
T_j^{replacement}.
\]

On every fixed low-coverage branch

\[
\alpha_j\le1-\delta,
\]

M5-395 sharpens the third term to

\[
\boxed{
T_j^{replacement}
\Longrightarrow
T_{j,\rm fixed\ flux}^{replacement}.
}
\]

Thus the only genuinely contact-dominated branch is the near-full target-coverage regime

\[
\boxed{
\alpha_j\to1
}
\]

or a subsequence on which the deficit tends to zero.

But M5-393 already audits positive/near-full material contact by separating volume identity from actual material-flux ancestry:

\[
\text{contact}
\Longrightarrow
H_{\rm viscous\ flux}
\lor
T_{\rm projective/replacement}
\lor
\text{genuine material-flux funnel}.
\]

Hence `contact` and `replacement` are now both flux-typed rather than purely volumetric labels.

---

## 11. Relation to M5-394 dual-flux formation

M5-394 shows that a natural productive Biot--Savart source contains a second formed flux carrier of physical size `~nu`.

M5-395 gives the complementary target-replacement fact:

- natural productive source -> formed companion flux;
- low target contact -> formed non-parent replacement flux.

Thus the local first-hitting genealogy can increasingly be written in terms of scale-invariant flux objects rather than unformed volume sets.

This is useful because the same material-surface flux equation can now audit both the main carrier and its companion/replacement carriers.

---

## 12. DSD audit

### Derived

- fixed target-volume deficit gives a fixed-area deficit on one transverse slice;
- the Taylor directed lower bound converts that area into fixed signed vorticity flux;
- the physical flux lower bound is scale invariant because `W r^2 = nu`;
- connectedness of the replacement subset is not required for the flux integral or material label assignment.

### Forbidden inference

Do not call every non-parent material patch `fresh material`.

It may come from an older different carrier.

Do not infer exponential genealogy width from simultaneous old/new flux populations.

Do not import positive-middle-specific geometry merely because a fixed replacement flux has now been obtained.

Do not call the fixed-flux replacement itself a contradiction.

---

## 13. Updated formed genealogy frontier

After M5-393--395, the adjacent formed branch can be written more precisely as

\[
\boxed{
H_{\rm reformation/nonlocal\ strain}
\lor
H_{\rm viscous\ flux}
\lor
T_{\rm fixed\ flux\ replacement/projective/export}
\lor
G_{\rm persistent\ material\ flux\ funnel}.
}
\]

On the coherent persistent-funnel branch, M5-393--394 further route the required stretching source to

\[
\boxed{
G_{\rm dual\,flux}^{formed}
\lor
H_{\rm remote\ relative-frequency/nonlocal\ strain}.
}
\]

Thus plain `volume replacement` is removed as an under-specified survivor.

---

## 14. Next target

The next unresolved local question is not whether a replacement carrier has fixed flux.

It does.

The next target is the **source-age / reuse ledger** for the dual-flux graph:

\[
\boxed{
\text{persistent reuse of an old companion flux carrier}
\quad\text{vs}\quad
\text{continual non-parent companion replacement}.
}
\]

Unlike the growing affine-shield circulation in M5-385, the natural carrier flux is scale invariant (`~nu`), so the old age-dilution estimate cannot be copied blindly.

That distinction must be audited next.

---

## 15. Audit verdict

### NEW RESULT

\[
\boxed{
\text{fixed target-volume replacement}
\Longrightarrow
\text{fixed target-flux replacement of order }\nu.
}
\]

### REMOVED AS UNDER-SPECIFIED TERMINAL

Pure target-volume replacement without a flux interpretation.

### STILL OPEN

- persistent old companion-source reuse at scale-invariant flux;
- continual fixed-flux source replacement;
- pricing the resulting dual-flux/source genealogy without double counting;
- remote/nonlocal strain;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
