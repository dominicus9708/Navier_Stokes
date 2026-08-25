# DSD Scale-Invariant Flux Replacement Routing

Date: 2026-08-25

Status: **NATURAL CORE FLUX SHOWN SCALE INVARIANT / POSITIVE-MIDDLE FIXED-FRACTION REPLACEMENT RECAST AS FLUX REPLACEMENT / QUIET REPLACEMENT ROUTED TO VISCOUS FLUX CHANGE, MATERIAL EXPORT, MULTIFLUX COEXISTENCE, OR PROJECTIVE REORGANIZATION / NO GLOBAL MULTIPLICITY CLOSURE YET / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The remaining geometric turnover branch from

`DSD_CAUCHY_GEOMETRIC_REPLACEMENT_CRITICAL_SATURATION_2026-08-25.md`

is exactly scale critical:

\[
\|F\|\sim q^k,
\qquad
s_{min}(F)\sim q^{-k/2},
\]

and the transverse compressed scale lands at the descendant natural radius.

Therefore ordinary volume is not a useful accumulating quantity: the natural core volume shrinks like `r_j^3`.

The correct transverse quantity is signed vorticity flux, because its natural first-hitting scale is invariant.

---

## 2. Natural first-hitting flux has no scale loss

At first-hitting stage `j`,

\[
W_j=q^jW_0,
\qquad
r_j=\sqrt{\frac\nu{W_j}}.
\]

A natural transverse disk has area of order

\[
r_j^2=\frac\nu{W_j}.
\]

If its directed vorticity is of order `W_j`, its physical signed vorticity flux is of order

\[
\boxed{
W_jr_j^2=\nu.
}
\]

Thus the natural circulation/flux scale is independent of `j`.

The existing Taylor-thick cylinder makes this quantitative. In normalized coordinates it supplies a fixed signed flux

\[
\Phi_*
\ge
\frac{3\pi}{16}r_0^2>0,
\]

and first-hitting parabolic rescaling preserves that physical flux.

Status: **PROVED / IMPORTED.**

---

## 3. One-stage positive-middle ribbonization

On the coherent positive-middle lane,

\[
s_1<0\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0.
\]

If the same material flux population produces one geometric amplification step `W -> qW`, its transverse area contracts by approximately `q^{-1}` while its transverse aspect ratio grows by at least `q` unless the eigenframe is reorganized.

For the standard `q=2` benchmark, the existing exact disk/ellipse geometry gives a maximum old-material coverage fraction

\[
F_2
=\frac12+\frac1\pi
\approx0.8183098862.
\]

Hence the uncovered target fraction is

\[
\boxed{
\delta_{rep}
:=1-F_2
=\frac12-\frac1\pi
\approx0.1816901138.
}
\]

This is the fixed one-stage material replacement fraction already proved on the coherent-affine positive-middle benchmark.

Status: **IMPORTED.**

---

## 4. Replacement fraction is also a fixed flux fraction on a thick target

At the next first-hitting thick core, the Taylor cylinder has a directed-vorticity lower bound on the target transverse disk.

Therefore an uncovered target-area fraction `delta_rep` is not merely geometric area. It carries a fixed positive amount of signed target flux.

Schematically, if the target disk flux is at least `Phi_*`, then the new-label portion carries

\[
\boxed{
\Phi_{new}
\ge
c_{thick}\,\delta_{rep}\,\Phi_*
=: \eta_{rep}\Phi_*,
}
\]

where `c_thick>0` is the fixed Taylor-thickness ratio from the directed-vorticity lower bound.

Thus fixed-fraction material replacement is a fixed-fraction **scale-invariant flux replacement**.

The exact numerical value of `eta_rep` depends on matching the chosen old-image/target cutoff geometry; only its strict positivity is used here.

Status: **PROVED on the same coherent thick-core geometry, with constants inherited from the Taylor lower bound.**

---

## 5. Material flux cannot quietly disappear

For a material transverse surface, the repository's exact viscous flux identity shows that its signed vorticity flux is conserved in the Euler limit and changes in Navier-Stokes only through the viscous flux-defect term.

Therefore an old material flux population carrying order `Phi_*` has only two possibilities during one stage:

1. it pays a robust viscous flux change;
2. a fixed fraction of its old material flux survives.

The first branch is already quantified by

`SMOOTH_THICK_CORE_FLUX_ENSTROPHY_GATE_2026-08-21.md`,

which gives a normalized palinstrophy lower bound and an explicit minimum stage duration `L_{Phi,min}` for robust flux change under bounded deformation.

Status: **IMPORTED.**

---

## 6. If old flux survives while target flux is replaced

Assume the viscous flux-change branch is below its fixed threshold.

Then a fixed portion of old material flux survives on the old material image.

If simultaneously the next thick target requires at least `eta_rep Phi_*` of new-label flux, the stage contains two distinct material flux contributions:

- surviving old-label flux;
- new-label target flux.

Because the new-label part is, by definition, outside the relevant old material image on the target cross-section, these cannot be identified as the same material surface population.

Thus quiet fixed-fraction replacement implies

\[
\boxed{
\text{surviving old flux}
+\text{new target flux}.
}
\]

What happens to the surviving old flux gives the next exact routing.

---

## 7. Export versus multiflux coexistence

Choose a common moving mesoscopic observation region containing the target thick core.

The surviving old material flux either:

### A. remains in the observation region

Then old and new material flux populations coexist at the same time.

This is a genuine

\[
\boxed{T_{multi-flux}}
\]

state rather than a vague packet multiplicity statement.

Repeated replacement without old-flux destruction or export increases the number/amount of distinguishable material flux populations that must be stored in the mesoscopic region.

### B. leaves the observation region

Then the old material population crosses the moving boundary.

This is exactly a material-turnover/export action of the type entering the existing moving relative-variance ledger through

\[
\mathcal T_{mat}.
\]

Hence

\[
\boxed{
\text{quiet flux replacement}
\Longrightarrow
T_{multi-flux}
\lor
T_{export}.
}
\]

Status: **PROVED AS A MATERIAL CONSERVATION ROUTING; no global cost for repeated multiflux storage is asserted yet.**

---

## 8. Projective reorganization is the replacement-avoidance branch

The only coherent positive-middle way to avoid the fixed replacement fraction is to reorganize the transverse eigenframe/material frame sufficiently rapidly.

The existing transverse-axis-swap gate gives

\[
\boxed{
\frac{L_I}{2}
+\mathscr A_{shape}
\ge
\frac\pi2.
}
\]

On the pure projective lane, the existing projective-speed estimate converts this action to a frequency integral and hence to a viscous `H1` tax.

Thus the no-replacement coherent branch is already typed as

\[
\boxed{T_{proj}/H1\text{ tax}.}
\]

Status: **IMPORTED.**

---

## 9. Full one-stage flux turnover routing

Combining the previous sections, a thick positive-middle first-hitting stage satisfies the structural routing

\[
\boxed{
\begin{aligned}
\text{critical geometric continuation}
\Longrightarrow{}&
\text{robust viscous flux change}\\
&\lor\ 
\text{projective anti-ribbon action}\\
&\lor\
\text{material flux export}\\
&\lor\
\text{multiflux coexistence}\\
&\lor\
\text{loss of coherent/thick positive-middle hypotheses}.
\end{aligned}
}
\]

The last loss is already routed in the repository to derivative/localization/Betchov residual channels.

Therefore the formerly broad `T` branch is reduced to four finite typed payers plus already known complement exits.

---

## 10. Why flux is better than volume for multistage turnover

Natural core volume scales as

\[
r_j^3\sim W_j^{-3/2}
\]

and therefore vanishes geometrically.

A fixed replacement fraction of volume can consequently be summable over stages and gives no direct contradiction.

By contrast, natural signed vorticity flux scales as

\[
W_jr_j^2=\nu,
\]

so a fixed replacement fraction corresponds to a fixed absolute scale-invariant flux amount on every stage.

Therefore repeated `T_multi-flux` events cannot be dismissed merely because the physical core volume shrinks.

The remaining problem is to convert storage of many fixed-flux material populations into a coercive quantity such as enstrophy, palinstrophy, relative variance, or boundary action without double counting folded/reconnected geometry.

---

## 11. Connection to the smooth flux and projective closures

Two of the four routes already have explicit finite-stage taxes:

### Viscous flux change

The smooth thick-core flux/enstrophy gate gives

\[
L_j\ge L_{\Phi,min}
\]

for a robust fixed-fraction flux change, under its stated tightness/deformation assumptions.

### Projective anti-ribbon action

The smooth projective-action closure gives a positive frequency integral

\[
\int_{I_j}\lambda ds
\ge
K_P^{-4/3}Z_+^{-2/3}
L_j^{-1/3}A(L_j)^{4/3}
\]

and inserts it directly into the `H1` ledger.

Thus the genuinely unresolved turnover mechanisms are narrowed to

\[
\boxed{T_{export}\lor T_{multi-flux}.}
\]

---

## 12. Relation to the R / historical-tail branch

If exported old flux is transported outward through successive first-hitting similarity scales and remains globally recurrent, it becomes a historical-replenishment problem already routed to

\[
H_{remote}\lor T.
\]

If instead it escapes to similarity infinity without replenishment, it merges with the locally recurrent core plus escaping passive critical-tail topology.

Therefore `T_export` is not entirely independent of the previously audited R/critical-halo branch.

The sharp remaining local turnover question is consequently `T_multi-flux`.

---

## 13. Updated frontier

After the material-mean diffusion and Cauchy corrections, the main proof tree can be organized as

\[
\boxed{
D_{mean}
\lor
T_{viscous\ flux}
\lor
T_{projective}
\lor
T_{export}
\lor
T_{multi-flux}
\lor
\text{escaping critical tail/complement exits}.
}
\]

Here

- `D_mean` has the new quadratic hyperpalinstrophy charge `~q^{-k/2}`;
- `T_viscous flux` has an explicit finite-stage palinstrophy/time floor;
- `T_projective` has an explicit projective-action/H1 frequency tax;
- `T_export` reconnects to historical/remote-tail routing;
- `T_multi-flux` is now the cleanest unresolved local turnover object.

The next efficient calculation is therefore to derive a **multiplicity-to-enstrophy or multiplicity-to-palinstrophy inequality for several distinguishable fixed-flux material tubes inside one bounded normalized region**.

---

## 14. Audit verdict

### PROVED / IMPORTED

- natural first-hitting signed flux is scale invariant;
- coherent positive-middle continuation forces fixed-fraction replacement unless projective reorganization occurs;
- fixed-fraction replacement on a thick target carries a fixed positive flux fraction;
- old material flux cannot disappear without a viscous flux-defect payment;
- surviving old flux plus new target flux yields export or material multiflux coexistence;
- viscous-flux and projective branches already have explicit finite-stage taxes.

### NOT DERIVED

- a coercive global bound excluding indefinite `T_multi-flux` storage;
- a no-double-counting theorem for folded/interlinked material flux tubes;
- closure of `T_export` on the nonrecurrent escaping-tail branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
