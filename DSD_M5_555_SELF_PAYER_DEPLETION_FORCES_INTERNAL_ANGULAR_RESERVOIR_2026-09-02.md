# DSD M5-555 — Self-payer depletion forces a recurrent internal angular reservoir and returns to the active-bridge/separator cost

Date: 2026-09-02

Status: **SELF-PAYER REDUCTION / IF THE M5-553 ORDERED PAYER EDGE IS A SELF-EDGE, THE PARENT LINEAGE CANNOT GENERATE ITS POSITIVE AXIAL STRAIN FROM A SOURCE EVERYWHERE PARALLEL TO THE PARENT DIRECTION: THE CLASSICAL/M5-454 DIRECTIONAL-DEPLETION KERNEL ANNIHILATES THE PARALLEL COMPONENT EXACTLY / UNIFORM DIRECTION SMOOTHNESS MAKES THE VERY-NEAR MARKER CONTRIBUTION SMALL, AND M5-534 MAKES THE REMOTE CONTRIBUTION SMALL / THEREFORE A FIXED INTERMEDIATE SOURCE ANNULUS INSIDE THE SAME LINEAGE CARRIES A FIXED TRANSVERSE VORTICITY AMOUNT / COMPACT DERIVATIVE BOUNDS THICKEN THIS INTO A FIXED-AMPLITUDE COHERENT INTERNAL SUBPACKET WITH ORDER-ONE ANGULAR SEPARATION / THE SELF-PAYER BRANCH IS THUS A RECURRENT INTERNAL DUAL-GEOMETRY BRANCH; M5-492 THEN FORCES EITHER ACTIVE-BRIDGE DIRECTION ENERGY OR LOW-VORTICITY-SEPARATOR MAGNITUDE-GRADIENT ENERGY / THIS IS A REAL PALINSTROPHY COST BUT, AS ALREADY AUDITED, IT CAN RECUR WITH POSITIVE MEAN AND IS NOT BY ITSELF A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Self-payer hypothesis

Take the recurrent ordered payer edge from M5-553 and suppose

\[
\boxed{b=a.}
\]

At the productive marker `x_a` with unit vorticity direction

\[
e:=\xi_a(x_a),
\]

the lineage-assigned source contributes

\[
\boxed{
q_{a\leftarrow a}
=e^T\mathcal R_{strain}[W_a](x_a)e
\ge q_{pay}>0
}
\]

at positive recurrence frequency.

The goal is to identify what geometry inside the same lineage is necessary for this self-stretching contribution.

---

## 2. Exact directional depletion of the axial strain

The axial stretching factor admits the classical directional representation, used structurally in M5-454,

\[
\boxed{
 e^T\Sigma(x_a)e
 =c\,\operatorname{p.v.}
 \int
 D(\widehat y,\xi(x_a+y),e)
 |W(x_a+y)|\frac{dy}{|y|^3},
}
\]

with

\[
D(n,b,e)
=(n\cdot e)\det(n,b,e).
\]

In particular,

\[
\boxed{
D(n,\pm e,e)=0.
}
\]

Moreover

\[
|D(n,b,e)|
\le C|b\times e|.
\]

Therefore an exactly parallel or antiparallel vorticity source does not contribute to the parent axial stretching factor.

---

## 3. Apply the formula to the self-lineage source piece

Because the strain operator is linear, the self-attributed scalar can be written schematically as

\[
q_{a\leftarrow a}
=c\,\operatorname{p.v.}
\int
D(\widehat y,\xi_a(x_a+y),e)
|W_a(x_a+y)|\frac{dy}{|y|^3}
\]

plus harmless smooth cutoff terms from the fixed genealogical partition.

Those cutoff terms remain uniformly controlled and can be absorbed into the fixed residual threshold used in M5-553.

Thus a positive fixed self-payer mark requires a fixed nonparallel contribution from the lineage-assigned vorticity source.

---

## 4. Very-near source contribution is uniformly small

On the globally smooth compact hull, in an active neighborhood of the marker,

\[
|\xi(x_a+y)-e|
\le C_\xi|y|.
\]

Hence

\[
|D(\widehat y,\xi(x_a+y),e)|
\le C C_\xi |y|.
\]

Also

\[
|W|\le M_*.
\]

Therefore the absolute contribution from `|y|<r` satisfies

\[
\begin{aligned}
|q_{near}(r)|
&\le C M_*
\int_{|y|<r}\frac{|y|}{|y|^3}dy\\
&\le C M_* r.
\end{aligned}
\]

Choose a fixed `r_0>0` so small that

\[
\boxed{|q_{near}(r_0)|\le q_{pay}/8.}
\]

Thus the positive self-payer contribution cannot be hidden arbitrarily close to an exactly aligned marker.

---

## 5. Remote source contribution is also small

Choose the active-core radius `R_core` from M5-543 sufficiently large.

M5-534/552 give

\[
\boxed{|q_{remote}(R_{core})|\le q_{pay}/8.}
\]

Therefore the middle source region

\[
\boxed{
A_{mid}
:=
\{r_0<|y-x_a|<R_{core}\}
}
\]

must carry a fixed part of the positive self-payer contribution.

After absorbing the fixed cutoff/residual errors,

\[
\boxed{
|q_{mid}|
\ge c q_{pay}>0.
}
\]

---

## 6. Middle contribution forces transverse vorticity mass

On the fixed annulus `A_mid`, the kernel weight is nonsingular and bounded above by constants depending only on the retained compact scales.

Using

\[
|D|\le C|\xi\times e|
\]

and

\[
|\xi\times e|\,|W|
=|(I-e\otimes e)W|,
\]

we obtain

\[
|q_{mid}|
\le C_{mid}
\int_{A_{mid}}
|(I-e\otimes e)W_a|\,dy.
\]

Hence

\[
\boxed{
\int_{A_{mid}}
|(I-e\otimes e)W_a|\,dy
\ge c_T>0.
}
\]

Since `A_mid` has fixed finite volume,

\[
\boxed{
\|(I-e\otimes e)W_a\|_{L^2(A_{mid})}
\ge c_{T,2}>0.
}
\]

This is the internal transverse reservoir required by self-payer stretching.

---

## 7. Extract a coherent internal transverse subpacket

The compact hull gives a uniform bound on the spatial derivatives of `W`.

The fixed transverse `L2` lower bound therefore implies a point `z_a` in the middle source region such that

\[
|(I-e\otimes e)W_a(z_a)|\ge c_1>0.
\]

Since

\[
|W|\le M_*,
\]

the direction at that point satisfies a fixed angular separation

\[
\boxed{
\sin\angle(\xi(z_a),e)
\ge s_{self}>0.
}
\]

After fixed shrinking, analyticity produces a coherent ball

\[
B_{r_{self}}(z_a)
\]

with fixed amplitude and direction cone separated from `e`.

Thus one genealogical lineage contains two recurrent active directional regions:

1. the productive marker region near `x_a`;
2. an internal transverse source packet near `z_a`.

---

## 8. The internal source packet carries fixed directed flux

On a sufficiently small disk normal to its coherent direction, the extracted packet has fixed positive directed vorticity flux magnitude

\[
\boxed{
|\Phi_{self,T}|\ge\phi_{self}>0.
}
\]

The packet remains assigned to the same broad material genealogy in the self-payer branch.

If its material ancestry is instead independent enough to require a separate fixed-flux label, the branch is refined back into the cross-lineage payer/finite-memory network rather than remaining a true self-edge.

Hence the genuine self branch is precisely an internally nontrivial material lineage with a recurrent angularly separated flux-carrying substructure.

---

## 9. Apply the M5-492 active bridge/separator dichotomy internally

Take the two active subregions inside the same lineage representation.

For a fixed active threshold `eta`, there are two cases.

### A. Uniform active bridge

A quantitatively thick path/tube inside

\[
\{\rho\ge\eta\}
\]

connects the marker region to the internal transverse packet.

The order-one direction change then gives

\[
\boxed{
\int_{bridge}
\rho^2|\nabla\xi|^2dy
\ge c_{dir}>0.
}
\]

### B. Low-vorticity separator / thin neck

Every connection crosses a low-amplitude or quantitatively thin region.

M5-492's coarea/isoperimetric argument then gives a magnitude-gradient cost

\[
\boxed{
\int_{sep}|\nabla\rho|^2dy
\ge c_{mag}>0
}
\]

or routes the event to the already typed thin-neck/frequency defect.

Thus in every clean self-payer event,

\[
\boxed{
P_{loc}
=\int|\nabla W|^2
\ge p_{self}>0.
}
\]

---

## 10. Positive recurrence thickens the self-payer cost in time

The self-payer edge occurs with positive log-scale frequency by M5-553.

The local derivative bounds thicken each spatial cost into a fixed similarity-time interval exactly as in M5-493.

Therefore

\[
\boxed{
\langle P_{self}\rangle>0.
}
\]

This is a recurrent internal-curvature/directional-variation cost attached to one material lineage.

---

## 11. Why this is not yet a contradiction

M5-493--507 already showed that positive recurrent palinstrophy and even all-order derivative charges can coexist with the compact similarity balance provided the stretching/nonlinear production pays them.

The self-payer geometry therefore does not create a new finite-total budget.

It refines the surviving mechanism:

\[
\boxed{
\text{self axial stretching}
\Rightarrow
\text{persistent internal angular reservoir}
\Rightarrow
\text{positive recurrent palinstrophy}.
}
\]

This is a genuine structural restriction but remains recyclable by the existing production ledger.

---

## 12. Self-payer verdict

The self-edge is not an independent zero-cost exception.

It is exactly a recurrent internal dual-geometry state of one material lineage.

However the already established similarity enstrophy/palinstrophy identities allow such a state in principle.

Therefore

\[
\boxed{
\mathcal E_{self}^{pay}
\Longrightarrow
\mathcal E_{internal-dual}^{lineage}
}
\]

with a fixed positive recurrent derivative cost, not a contradiction.

---

## 13. Updated final active branches

After M5-553--555, the shared-source hard core reduces to

\[
\boxed{
\mathcal E_{cross}^{pay}
\lor
\mathcal E_{internal-dual}^{lineage}.
}
\]

The second branch is now fully typed by existing active-bridge/separator and derivative ledgers.

The first branch carries the additional universal connector-compression condition from M5-554.

Thus the **genuinely new** remaining rigidity problem is concentrated on the cross-lineage payer branch.

---

## 14. Highest-value next target

For the cross-payer branch, combine

\[
q_{a\leftarrow b}>0
\]

with the exact material connector equation

\[
r'=(\tfrac12I+G_{ab})r
\]

and the anchored/migration alternatives of both lineages.

The next question is whether persistent positive cross-stretching plus mean connector compression `-1/2` forces a third independent persistent source/marker.

If a third independent material marker is forced, the finite shape matrix becomes available and the exact similarity material-volume law

\[
\nabla\cdot B=\frac32
\]

may provide a determinant obstruction stronger than any scalar energy ledger.

If no third marker is forced, the survivor is a genuinely two-lineage recurrent cross-stretching system and must be attacked directly as such.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
