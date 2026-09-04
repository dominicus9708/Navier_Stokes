# DSD M17-102 — Adjacent finite critical types share one director-area tube measure and a clean type boundary is a chart change

Date: 2026-09-05
Canonical ID: **M17-102**

Status: **INTERNAL RANK-2 STRATIFIED TYPE-BOUNDARY FLUX-MATCHING GATE / M17-101 SHOWS THAT EACH FIXED FINITE DEGENERATE TYPE `nu` HAS A REGULAR TOP-JET SHEET `Psi_nu=D_xi^(nu-1)g=0` WITH `D_xi Psi_nu=H_nu!=0`, AND WHERE THIS SHEET IS TRANSVERSE TO `J_xi` ITS PEAK POPULATION INHERITS THE DIRECTOR-AREA FLUX. THE KEY AUDIT IS THAT THIS FLUX IS NOT CREATED BY THE TOP-JET SHEET: IT IS THE PREEXISTING FROZEN FLUX OF THE SAME DIRECTOR-AREA TUBE. THEREFORE TWO ADJACENT FINITE TYPE CHARTS `nu` AND `nu'` DO NOT CARRY DISTINCT MEASURES. IF THE SAME REGULAR DIRECTOR-AREA TUBE LABEL AND THE SAME PEAK GENEALOGY CONTINUE THROUGH `H_nu=0` INTO TYPE `nu'`, THEN THE PULLBACKS OF `J_xi·n_nu dA_nu` AND `J_xi·n_nu' dA_nu'` TO TUBE-LABEL SPACE ARE EXACTLY THE SAME `dPhi_J(lambda)`. A CLEAN TYPE BOUNDARY IS THUS A CHANGE OF DEFINING JET CHART, NOT A FLUX SOURCE. IF ONE TOP-JET SHEET BECOMES TANGENT, THE ALGEBRAIC INTERSECTION DEGREE OF M17-100/101 STILL REMOVES REGULAR TANGENCY AS A SIGNED-FLUX COST. A GENUINE SOURCE REQUIRES FAILURE OF THE SHARED CARRIER OR ITS GENEALOGY: `J_xi=0`, ENDPOINT/DOMAIN EXIT, NONMATCHABLE PEAK BRANCHING, OR CHART/INTERFACE FAILURE NOT RESOLVED BY THE FINITE JET ATLAS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The primary carrier is the director-area tube

On the retained pure-transverse-kernel Rank-2 branch,

\[
J_\xi=|J_\xi|k\neq0
\]

and

\[
\beta_\xi:=\iota_{J_\xi}dV
\]

is frozen into the similarity material flow.

Hence every regular tube label `lambda` carries one conserved infinitesimal flux

\[
\boxed{d\Phi_J(\lambda).}
\]

This object exists before any peak or critical-type chart is chosen.

Therefore the hierarchy is

\[
\boxed{
\text{director-area tube flux}
\to
\text{peak intersection}
\to
\text{critical-type chart}.
}
\]

The type chart is not the source of the measure.

---

## 2. Fixed finite type charts

For a finite type `nu`, define

\[
\Psi_\nu:=D_\xi^{\nu-1}g,
\qquad
g=D_\xi\log\rho.
\]

On the type-`nu` maximum,

\[
\Psi_\nu=0,
\qquad
H_\nu:=D_\xi^\nu g<0.
\]

Therefore

\[
D_\xi\Psi_\nu=H_\nu\neq0
\]

and

\[
S_\nu^{top}:=\{\Psi_\nu=0\}
\]

is a regular local surface.

If

\[
D_k\Psi_\nu\neq0,
\]

then the director-area tube is transverse to this chart and the sheet representation of its flux is

\[
\boxed{
d\Phi_{J,\nu}^{sheet}
:=J_\xi\cdot n_\nu\,dA_\nu.
}
\]

---

## 3. Pull back to tube-label space

Let

\[
X_\nu:\Lambda\to S_\nu^{top}
\]

map a tube label to its locally unique transverse intersection with the type-`nu` top-jet sheet.

The sheet flux pulled back by this intersection map is precisely the flux assigned to that tube label:

\[
\boxed{
X_\nu^*(J_\xi\cdot n_\nu\,dA_\nu)
=d\Phi_J(\lambda).
}
\]

This equality is the geometric meaning of using a flux cross-section.

It is not a new conservation theorem; it is the same frozen two-form `beta_xi` evaluated on a different cross-section of the same tube bundle.

---

## 4. Adjacent type boundary

Suppose the type-`nu` top jet tends to zero,

\[
\boxed{H_\nu\to0,}
\]

and the peak continues into another finite type `nu'` with

\[
\boxed{H_{\nu'}\neq0.}
\]

The new regular defining function is

\[
\Psi_{\nu'}:=D_\xi^{\nu'-1}g.
\]

Assume through the boundary:

1. `J_xi!=0`;
2. the same frozen tube label continues;
3. the same local peak genealogy can be matched through the event;
4. no endpoint/domain/chart interface is crossed;
5. each side admits a regular top-jet chart, possibly after passing through an isolated tangency.

Then there are two local cross-section maps

\[
X_\nu,
\qquad
X_{\nu'}
\]

for the same tube-label family.

---

## 5. Exact measure matching

Each chart pulls back its sheet flux to the same primary tube measure:

\[
X_\nu^*(J_\xi\cdot n_\nu\,dA_\nu)
=d\Phi_J,
\]

\[
X_{\nu'}^*(J_\xi\cdot n_{\nu'}\,dA_{\nu'})
=d\Phi_J.
\]

Therefore

\[
\boxed{
X_\nu^*d\Phi_{J,\nu}^{sheet}
=
X_{\nu'}^*d\Phi_{J,\nu'}^{sheet}
=
d\Phi_J.
}
\]

Hence a clean finite critical-type boundary does not create a Jacobian mismatch or an independent flux source.

It is a change of sheet chart over the same carrier measure.

---

## 6. Type ledgers share one measure space

Instead of writing each finite type on an unrelated measure space, use the common tube-label measure

\[
\boxed{(\Lambda,d\Phi_J).}
\]

For any type-dependent descriptor `Y_nu`, define

\[
F_\nu^J(y,\theta)
=\int_{\Lambda_\nu(\theta)}
\delta(y-Y_\nu(\lambda,\theta))
\,d\Phi_J(\lambda).
\]

At a clean type switch

\[
\nu\to\nu',
\]

the tube label moves from `Lambda_nu` to `Lambda_nu'`, but its measure element does not change.

Thus the integrated type-source terms cancel:

\[
\boxed{
\int\mathcal B_\nu^Jdy
=-\dot\Phi_{switch},
\qquad
\int\mathcal B_{\nu'}^Jdy
=+\dot\Phi_{switch}.
}
\]

This recovers M17-098 without requiring the lowest-order `g=0` sheet itself to remain regular.

---

## 7. Tangency during chart transition

If either top-jet sheet becomes tangent to `J_xi`, then

\[
D_k\Psi_\nu=0
\]

or

\[
D_k\Psi_{\nu'}=0.
\]

The sheet is still regular as long as its top line derivative is nonzero on that side.

M17-100/101 then give the algebraic intersection-degree law with the corresponding `Psi` as defining function.

Therefore isolated regular top-jet tangency changes unsigned intersection genealogy but not signed tube flux.

Hence

\[
\boxed{
\text{type boundary + regular tangency}
\not\Rightarrow
\text{director-area flux loss}.
}
\]

---

## 8. What a genuine type-boundary source would require

A noncancelling source at a type boundary requires failure of the shared-carrier identification.

The explicit possibilities are

\[
\boxed{
\begin{aligned}
&J_\xi\to0
&&\text{director-area/rank degeneration},\\
&\text{no unique/matchable continuation of the peak genealogy}
&&\text{branching event beyond simple chart change},\\
&\text{peak crosses a retained tube endpoint}
&&\text{endpoint source},\\
&\text{the finite jet atlas leaves the retained domain}
&&\text{chart/interface source},\\
&\nu\to\infty
&&\text{unbounded-order exit}.
\end{aligned}
}
\]

On the compact analytic hard hull, M17-088 excludes the last option absent endpoint/rank/chart degeneration.

---

## 9. Refined finite-type atlas

The finite critical-type family is therefore better viewed as a stratified atlas over one tube-flux measure space:

\[
\boxed{
(\Lambda,d\Phi_J)
\supset
\Lambda_1\cup\Lambda_3\cup\cdots\cup\Lambda_{\nu_*}.
}
\]

Each `Lambda_nu` uses its own regular top-jet defining function `Psi_nu`, but all carry the same inherited measure element.

The type label is a chart/state descriptor.
The flux tube is the persistent carrier.

---

## 10. DSD interpretation

This resolves a potential measure substitution error.

The quantities

\[
J_\xi\cdot n_\nu\,dA_\nu
\]

and

\[
J_\xi\cdot n_{\nu'}\,dA_{\nu'}
\]

look like different surface measures in physical space.

They must **not** be compared pointwise as densities on different sheets.

After pullback to the same tube-label space, they are the same object:

\[
\boxed{d\Phi_J.}
\]

Thus the correct comparison is carrier-based, not density-based.

---

## 11. Consequence for the candidate nonrecyclable set

M17-101 left the finite critical-type boundary as a possible remaining event.

M17-102 removes a **clean matched finite type boundary** from the nonrecyclable list.

On the compact finite-order hard hull, the candidate set is refined to

\[
\boxed{
E_{nonrecyclable}^{R2}
\subset
E_{endpoint}
\cup
E_{J_\xi=0}
\cup
E_{nonmatchable\ peak\ branching}
\cup
E_{chart/interface}.
}
\]

Regular tangency, finite degeneracy, and clean finite type switching are now all internal recyclable events at the signed director-area-flux level.

---

## 12. DSD audit

### Audit A — treating each top-jet sheet measure as an independent conserved quantity
Rejected. Each is a cross-section representation of the same tube flux.

### Audit B — comparing `J·n dA` pointwise across different type sheets
Rejected. The correct comparison is after pullback to tube-label space.

### Audit C — assuming type transition automatically preserves genealogy
Not assumed. The result is conditional on a matchable continuation of the same peak carrier.

### Audit D — treating regular tangency during the switch as a source
Rejected by the algebraic intersection-degree law.

### Audit E — claiming all type-boundary events are harmless
Rejected. Nonmatchable branching, rank loss, endpoint, or interface exits remain explicit.

### Audit F — proof status
The clean finite-type boundary is reduced to a chart change, but nonmatchable genealogy and carrier exits remain open.

---

## 13. Updated Rank-2 finite-type frontier

Within the compact finite-order pure-kernel peak hull,

\[
\boxed{
\text{regular tangency}
\cup
\text{finite }\nabla g=0\text{ degeneracy}
\cup
\text{clean finite type switch}
\Longrightarrow
\text{recyclable internal genealogy}.
}
\]

Therefore the remaining genuinely structural Rank-2 events are

\[
\boxed{
E_{endpoint},
\qquad
E_{J_\xi=0},
\qquad
E_{nonmatchable\ peak\ branching},
\qquad
E_{chart/interface}.
}
\]

The next high-value gate is the **nonmatchable peak-branching gate**: determine whether finite analytic peak genealogy can ever fail to match tube labels without passing through one of the already explicit endpoint/rank/interface exits, or whether branching itself is again only a higher-codimension internal rearrangement with conserved algebraic flux.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
