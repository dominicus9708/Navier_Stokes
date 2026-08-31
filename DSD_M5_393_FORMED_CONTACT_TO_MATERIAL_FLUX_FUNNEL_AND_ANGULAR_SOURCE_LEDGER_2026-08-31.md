# DSD M5-393 — Formed contact: material-flux funnel and angular-source routing

Date: 2026-08-31

Status: **POSITIVE MATERIAL VOLUME CONTACT IS NOT THE SAME THING AS PERSISTENT VORTICITY-FLUX ANCESTRY / A FORMED CONTACT STAGE THEREFORE SPLITS INTO FLUX-IDENTITY LOSS/REPLACEMENT OR A GENUINE MATERIAL-FLUX DESCENDANT / A GENUINE FIXED-FRACTION FLUX DESCENDANT ACROSS MANY FIRST-HITTING GENERATIONS FORCES MATERIAL CROSS-SECTIONAL AREA CONTRACTION OF ORDER `q^{-L}` AND HENCE COMPLEMENTARY DEFORMATION/STRETCHING OF ORDER `q^L` BY INCOMPRESSIBILITY / IF THE FUNNEL AXIS REORGANIZES THIS IS PROJECTIVE/CAPACITY ACTION; IF IT STAYS COHERENT, THE REQUIRED LONGITUDINAL STRETCHING CANNOT BE SELF-SUPPLIED BY A PERFECTLY ALIGNED FINITE-ENERGY CORE AND MUST COME FROM THE MISALIGNED BIOT--SAVART SOURCE NETWORK OF M5-362, WHICH M5-376--377 AND M5-392 ROUTE TO CRITICAL LOCAL OCCUPANCY OR REMOTE/NONLOCAL STRAIN / THUS `R_contact^formed` IS NOT AN INDEPENDENT QUIET TERMINAL, BUT THE REMAINING H/REMOTE LEDGER IS STILL OPEN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

After M5-390--392, the late smooth first-hitting frontier is

\[
H_{\rm crit\,mass/occupancy}
\lor
H_{\rm remote\,relative-frequency/nonlocal\,strain}
\lor
R_{\rm contact}^{formed}
\lor
T_{\rm replacement/export}^{formed}.
\]

The most dangerous interpretation of

\[
R_{\rm contact}^{formed}
\]

would be to say that positive overlap with old material is itself impossible.

That is false.

Classical vortex stretching is precisely compatible with the same material vortex population being compressed transversely while its vorticity grows longitudinally.

The correct question is more precise:

> Does formed volume contact carry an actual fixed-fraction **material vorticity-flux ancestry**, and if so, what deformation/source action is forced by that ancestry?

This note separates volume contact from flux contact and then prices the genuine flux-contact branch.

---

## 2. First-hitting carriers and the volume-contact variable

Let

\[
W_{j+1}=qW_j,
\qquad
r_j=\sqrt{\frac{\nu}{W_j}},
\qquad q>1.
\]

M5-390 constructs at every late first-hitting endpoint a Taylor carrier

\[
C_j
\]

with natural diameter comparable to `r_j`, positive normalized volume, and a directed signed vorticity flux

\[
\boxed{
\Phi_j\asymp W_jr_j^2\asymp\nu.
}
\]

Let

\[
A_j(t)=\Phi_{t_j,t}(C_j)
\]

be its material image under the incompressible flow map.

At the next endpoint, M5-390 defines a volume contact fraction of the form

\[
\chi_j
=
\frac{|C_{j+1}\cap A_j(t_{j+1})|}{r_j^3}.
\]

A positive lower bound on `chi_j` means that a definite part of the next high-vorticity core consists of old material.

It does **not** yet mean that the old vorticity flux itself survives through the same material cross-section.

---

## 3. DSD distinction: material identity, flux identity, and geometric axis

Three descriptors must remain separate.

### A. Material identity

A particle label is transported exactly by the flow map.

This survives as long as the solution is smooth.

### B. Vorticity-flux identity

Vorticity is not a passive material scalar in Navier--Stokes.

Viscosity changes vorticity flux through a material surface.

Therefore old material can occupy a new high-vorticity core while the relevant signed flux has been created, destroyed, or reorganized diffusively.

### C. Geometric/axis identity

Even if a material cross-section survives and carries comparable flux, its transported normal/stretching axis may rotate relative to the current vorticity direction.

That is a projective/geometric action, not ordinary quiet contact.

Hence the implication

\[
\boxed{
\text{positive material volume contact}
\not\Longrightarrow
\text{persistent material vorticity-flux contact}
}
\]

is mandatory in the DSD ledger.

---

## 4. Exact material-surface vorticity-flux equation

Let

\[
X(a,t)
\]

be the flow map and

\[
F(a,t)=D_aX(a,t)
\]

its deformation gradient.

For incompressible flow,

\[
\det F=1.
\]

Let `S_0` be an oriented material surface with initial unit normal `n_0` and let

\[
S(t)=X(S_0,t).
\]

The oriented area vector transforms as

\[
n(t)dA_t
=
\operatorname{cof}F\,n_0dA_0
=
F^{-T}n_0dA_0.
\]

The vorticity equation is

\[
D_t\omega
=(\nabla u)\omega+\nu\Delta\omega.
\]

Since

\[
\frac{d}{dt}F^{-T}
=-(\nabla u)^TF^{-T},
\]

the stretching terms cancel in the derivative of the flux pairing:

\[
\frac d{dt}
\left[
\omega(X(a,t),t)\cdot F^{-T}(a,t)n_0
\right]
=
\nu\Delta\omega(X(a,t),t)
\cdot F^{-T}(a,t)n_0.
\]

Therefore the signed vorticity flux through a material surface obeys the exact identity

\[
\boxed{
\frac d{dt}
\int_{S(t)}\omega\cdot n\,dA
=
\nu
\int_{S(t)}\Delta\omega\cdot n\,dA.
}
\]

For Euler, the right-hand side vanishes and material vorticity flux is conserved.

For Navier--Stokes, any change of flux ancestry must be paid by the viscous flux term.

This is the correct flux-level analogue of the Kelvin/circulation ledger used earlier.

---

## 5. Definition of a genuine material-flux descendant

Fix a flux fraction

\[
0<\phi_0<1.
\]

A stage-`j` carrier is said to have a genuine material-flux descendant at stage `j+L` if there exists a material sub-surface

\[
S_j^0\subset C_j
\]

such that:

1. at formation,
   \[
   \left|\int_{S_j^0}\omega(t_j)\cdot n\,dA\right|
   \ge \phi_0\nu;
   \]
2. its material image
   \[
   S_j^L=X(S_j^0,t_{j+L})
   \]
   lies inside the retained current carrier geometry at stage `j+L`;
3. its signed flux at `t_{j+L}` still satisfies
   \[
   \left|\int_{S_j^L}\omega(t_{j+L})\cdot n\,dA\right|
   \ge c_\phi\nu
   \]
   for a fixed `c_phi>0`.

This definition is deliberately stronger than positive volume contact.

If no such surface can be retained, then the old/new overlap is not a persistent flux genealogy and must be typed as flux-identity loss, projective reorganization, or replacement.

---

## 6. Failure of flux ancestry is already a costed branch

Suppose the stage has positive material volume contact but every candidate old material cross-section loses a fixed fraction of its initial signed flux before it can represent the later carrier.

By the exact material-surface flux equation,

\[
\left|
\Phi(t_{j+L})-\Phi(t_j)
\right|
\le
\nu
\int_{t_j}^{t_{j+L}}
\left|
\int_{S(t)}\Delta\omega\cdot n\,dA
\right|dt.
\]

Thus a fixed-fraction loss of order `nu` is a genuine viscous flux-change event.

If instead the old material still carries comparable flux but no transported old surface represents the new directed carrier, then the carrier axis/cross-section has undergone a projective or replacement reorganization.

Therefore

\[
\boxed{
\text{volume contact without flux ancestry}
\Longrightarrow
H_{\rm viscous\ flux}
\lor
T_{\rm projective/flux\ replacement}.
}
\]

This does not assert a contradiction.

It only prevents positive volume overlap from being counted as a free quiet terminal.

---

## 7. Persistent flux ancestry forces cross-sectional area contraction

Now assume a genuine material-flux descendant survives from stage `j` to stage `j+L`.

At the initial stage the first-hitting amplitude cap gives

\[
|\omega(t_j)|\le C_WW_j.
\]

Since the initial material surface carries at least `phi_0 nu` flux,

\[
\phi_0\nu
\le
C_WW_j|S_j^0|.
\]

Because

\[
W_jr_j^2=\nu,
\]

we obtain

\[
\boxed{
|S_j^0|
\ge c_0r_j^2.
}
\]

At the later first-hitting stage, the retained current Taylor carrier has transverse area at most

\[
C_1r_{j+L}^2
=
C_1q^{-L}r_j^2.
\]

Since the material descendant lies inside that carrier geometry,

\[
\boxed{
|S_j^L|
\le C_1q^{-L}r_j^2.
}
\]

Hence

\[
\boxed{
\frac{|S_j^L|}{|S_j^0|}
\le C_2q^{-L}.
}
\]

Thus a persistent fixed-flux lineage is a genuine material funnel: its cross-sectional area contracts geometrically across the first-hitting tower.

---

## 8. Area contraction forces complementary deformation stretching

For an oriented material surface the local area Jacobian is

\[
J_2(a,t)
=
|F^{-T}(a,t)n_0(a)|.
\]

The area estimate gives

\[
\int_{S_j^0}J_2(a,t_{j+L})dA_0
\le
C_2q^{-L}|S_j^0|.
\]

Therefore there exists at least one point on the retained material surface for which

\[
\boxed{
|F^{-T}n_0|
\le C_2q^{-L}.
}
\]

Let

\[
\sigma_1(F)
\ge\sigma_2(F)
\ge\sigma_3(F)>0
\]

be the singular values.

Since

\[
\|F^{-T}n_0\|
\ge\sigma_{\min}(F^{-T})
=\sigma_1(F)^{-1},
\]

we get

\[
\boxed{
\sigma_1(F)
\ge c_2q^L.
}
\]

This is the complementary stretching forced by incompressible cross-sectional squeezing.

Moreover the deformation-gradient estimate

\[
\|F(t_{j+L})\|
\le
\exp
\left(
\int_{t_j}^{t_{j+L}}
\|\nabla u(t)\|_\infty dt
\right)
\]

gives

\[
\boxed{
\int_{t_j}^{t_{j+L}}
\|\nabla u(t)\|_\infty dt
\ge
L\log q-O(1).
}
\]

This lower bound is fully compatible with a hypothetical singularity.

It is not yet a contradiction.

Its value is that the formed contact branch is now tied to an actual same-material deformation mechanism rather than an abstract overlap label.

---

## 9. Relation to M5-340 first-hitting longitudinal stretching

M5-340 proves independently that each first-hitting stage pays

\[
\boxed{
\int_{t_j}^{t_{j+1}}
\|\gamma^+(t)\|_\infty dt
\ge\log q,
\qquad
\gamma=\xi^TS\xi.
}
\]

The material-funnel estimate is geometrically consistent with this required longitudinal stretching.

The new gain is that on the genuine contact branch the amplification can be realized as a **material cross-section contraction / complementary stretch** over the same flux lineage.

Thus there is no legitimate shortcut

\[
\text{same material}
\Longrightarrow
\text{impossible}.
\]

The correct next question is the source of the strain that drives the funnel.

---

## 10. Funnel-axis dichotomy

Let the retained flux funnel have a material normal/stretching-axis descriptor determined by the transported cross-section.

Across late generations there are two possibilities.

### A. Persistent projective reorganization

The transported material axis and the current high-vorticity carrier axis retain a fixed non-negligible angular mismatch or undergo repeated order-one reorientation.

Then the contact is not a quiet aligned funnel.

It lies in the existing projective/angular ledger:

\[
\boxed{
T_{\rm projective\ funnel}
\Longrightarrow
H_{\rm angular/capacity}
\lor
T_{\rm replacement/reorientation}.
}
\]

Under M5-376--377 and the M5-392 analyticity correction, a natural-scale productive angular defect is not an independent terminal; it becomes a fixed local normalized palinstrophy/capacity occupancy event.

### B. Coherent funnel axis

After passing to a subsequence, the funnel axis remains quantitatively coherent with the current high-vorticity direction over the active material core.

Then the active core is approximately an aligned material vortex funnel.

Such an aligned finite-energy whole-space core cannot self-supply all of its required longitudinal stretching through aligned vorticity alone.

M5-362 gives the exact angular Biot--Savart source requirement.

---

## 11. Stable aligned funnel requires an external/misaligned Biot--Savart source

M5-362 uses the longitudinal stretching representation

\[
\gamma(x)
=
\frac{3}{4\pi}
\operatorname{p.v.}
\int_{\mathbb R^3}
D(\widehat y,\xi(x+y),\xi(x))
\frac{|\omega(x+y)|}{|y|^3}dy,
\]

with

\[
|D|
\le
|\xi(x+y)\times\xi(x)|.
\]

If the source vorticity is perfectly aligned or anti-aligned with the core direction, its contribution to `gamma` vanishes.

Therefore the fixed first-hitting stretching action cannot be supplied by a perfectly aligned self-contained funnel.

A surviving coherent material-flux funnel must be accompanied by a nontrivial misaligned source at some scale.

Thus

\[
\boxed{
\text{coherent material-flux funnel}
\Longrightarrow
\text{misaligned natural source}
\lor
\text{multiscale source spread}
\lor
\text{remote/nonlocal source}.
}
\]

---

## 12. Insert the M5-376--377 and M5-392 source closures

The recent angular-source audit gives the following routing.

### Natural-scale source

A fixed-fraction productive natural shell has positive spatial source capacity.

M5-377 gives a center/source Poincare cost.

M5-392 removes the old thin-center pointwise derivative alternative because the first-hitting stage has a fixed normalized analytic radius.

Hence

\[
\boxed{
\text{natural productive source}
\Longrightarrow
H_{\rm crit\,mass/occupancy}.
}
\]

### Multiscale source spread

M5-376 removes indefinite diffuse natural-scale angular spreading as an independent leaf and routes scale loss to derivative/capacity or remote/non-tight structure.

With M5-392 this becomes

\[
\boxed{
\text{multiscale source}
\Longrightarrow
H_{\rm crit\,mass/occupancy}
\lor
H_{\rm remote\,relative-frequency/nonlocal\,strain}.
}
\]

### Remote source

If the source of the required stretching escapes to large normalized distance, the surviving mechanism is precisely the remote/nonlocal strain frontier:

\[
\boxed{
\text{remote source}
\Longrightarrow
H_{\rm remote\,relative-frequency/nonlocal\,strain}
\lor
T_{\rm remote/formed}.
}
\]

---

## 13. Formed-contact collapse

Combining Sections 6 and 10--12 gives the structural reduction

\[
\boxed{
R_{\rm contact}^{formed}
\Longrightarrow
H_{\rm viscous\ flux}
\lor
T_{\rm replacement/projective}
\lor
H_{\rm crit\,mass/occupancy}
\lor
H_{\rm remote\,relative-frequency/nonlocal\,strain}.
}
\]

On the late corridor where viscous flux replacement and projective replacement are already routed through the finite-memory/formed-replacement ledger, the independent quiet-contact leaf disappears:

\[
\boxed{
R_{\rm contact}^{formed}
\text{ is not an independent final terminal.}
}
\]

What remains is the common H/remote/replacement source ledger.

This is a proof-tree consolidation, not a global regularity theorem.

---

## 14. Why pairwise contact alone still cannot produce an immortal material population

A subtle ancestry firewall remains necessary.

Even if

\[
|C_{j+1}\cap A_j(t_{j+1})|
\approx|C_{j+1}|
\]

for every stage, one cannot infer that a fixed positive-volume subset of one early carrier survives every later generation.

The active volume shrinks like

\[
|C_j|\asymp r_j^3,
\qquad
\frac{|C_{j+1}|}{|C_j|}\asymp q^{-3/2}.
\]

A small subset of the old carrier can therefore populate essentially all of the next smaller carrier.

Successive stages can keep switching which old subset is selected.

Thus the present argument deliberately uses **material flux surfaces** when claiming a persistent funnel and otherwise routes the event to ancestry/replacement.

No immortal positive-volume particle population is assumed.

---

## 15. Why nested material patches are not summed as independent costs

The material flux descendants may be nested or may successively select smaller subpatches.

Therefore their areas, enstrophy, or palinstrophy cannot be added across generations as disjoint contributions.

The only stagewise statements retained here are:

1. geometric area contraction along a genuine flux lineage;
2. the associated deformation-gradient lower bound;
3. projective source routing;
4. the external/misaligned Biot--Savart source requirement.

No contradiction is obtained by summing nested material area or mass.

---

## 16. DSD formation analysis

### Formed objects

- endpoint Taylor carrier;
- exact material image under the flow map;
- material cross-section;
- signed vorticity flux;
- transported area-normal/stretching-axis descriptor.

### Not identified silently

- material volume contact is not flux contact;
- current vorticity direction is not automatically the transported old flux axis;
- current carrier is not automatically the same material surface as the old carrier;
- repeated pairwise contact is not a fixed positive-volume all-age descendant.

This separation is the main formation-level correction of the contact branch.

---

## 17. DSD axis-property analysis

The axis ledger now has three possibilities.

1. **Axis-stable flux funnel**
   \[
   \text{material transverse contraction}
   +
   \text{longitudinal stretch}
   +
   \text{external/misaligned source requirement}.
   \]

2. **Axis-changing flux funnel**
   \[
   \text{projective/angular action}
   \to
   H_{\rm capacity}
   \lor T_{\rm replacement}.
   \]

3. **Flux-axis identity loss**
   \[
   \text{viscous flux change}
   \lor
   \text{new carrier/replacement}.
   \]

Thus the contact branch has no axis-free silent survivor.

---

## 18. DSD audit firewall

The following inferences are forbidden.

### Forbidden 1

\[
\text{positive material overlap}
\Rightarrow
\text{same vortex flux tube}.
\]

False without a flux-identity argument.

### Forbidden 2

\[
\text{same material flux tube stretches}
\Rightarrow
\text{contradiction}.
\]

False; this is classical vortex stretching geometry.

### Forbidden 3

\[
\text{pairwise high contact}
\Rightarrow
\text{one fixed positive-volume population survives forever}.
\]

False because the active core volume shrinks geometrically and the selected subset can change.

### Forbidden 4

Treat material vorticity flux as exactly conserved in Navier--Stokes.

The exact viscous flux term must be retained.

### Forbidden 5

Infer parent-scale pointwise derivative blowup from funnel compression.

M5-392 already gives uniform fixed-order parent-normalized vorticity derivative bounds on each smooth first-hitting stage.

The surviving difficulty is critical occupancy/remote/nonlocal strain, not an arbitrarily sharp local cusp.

### Forbidden 6

Add nested descendant areas or derivative costs as if they were disjoint.

No such sum is used.

---

## 19. Updated frontier

The independent `R_contact^formed` leaf can now be absorbed into the source/replacement ledger.

A conservative updated late first-hitting frontier is

\[
\boxed{
H_{\rm crit\,mass/occupancy}
\lor
H_{\rm remote\,relative-frequency/nonlocal\,strain}
\lor
T_{\rm replacement/export/projective}^{formed}.
}
\]

The remaining decisive problem is no longer whether old material can stay in the core.

It can.

The decisive problem is whether the **critical source network that keeps feeding the material funnel** can be globally priced by a non-double-counted scale-time budget.

---

## 20. Next target

The most efficient next calculation is a scale-time source-packing theorem.

At each first-hitting stage the record growth supplies a fixed normalized longitudinal-stretching action.

M5-362 and the present note force that action into one of:

\[
\text{local productive source occupancy},
\qquad
\text{remote/nonlocal source},
\qquad
\text{projective replacement}.
\]

The next question is whether a positive-density sequence of such source events can be assigned a common Carleson/packing-type charge without counting the same spatial/frequency reservoir at infinitely many nested scales.

That is now the narrowest common bottleneck.

---

## 21. Audit verdict

### NEW STRUCTURAL REDUCTION

\[
\boxed{
\text{formed material volume contact}
\to
\text{flux-identity loss/replacement}
\lor
\text{genuine material-flux funnel}.
}
\]

### GENUINE FLUX FUNNEL COST

\[
\boxed{
|S_j^L|/|S_j^0|
\lesssim q^{-L},
\qquad
\sigma_1(F)\gtrsim q^L,
\qquad
\int\|\nabla u\|_\infty dt
\gtrsim L\log q-O(1).
}
\]

### SOURCE ROUTING

\[
\boxed{
\text{coherent funnel}
\to
H_{\rm crit\,mass/occupancy}
\lor
H_{\rm remote/nonlocal\,strain},
}
\]

modulo projective/viscous flux replacement.

### REMOVED AS INDEPENDENT QUIET LEAF

\[
\boxed{R_{\rm contact}^{formed}.}
\]

### STILL OPEN

- a global non-double-counted price for repeated critical source occupancy;
- remote relative-frequency/nonlocal-strain source closure;
- formed replacement/export/projective genealogy;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
