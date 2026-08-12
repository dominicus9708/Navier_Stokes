# Off-diagonal channel overlap / segregation matrix

Date: 2026-08-12

Status: **DSD STATIC-AGGREGATION BRIDGE + EXACT SET/WEIGHT DECOMPOSITIONS + OPEN DYNAMIC SEGREGATION EXCLUSION**.

The residual singularity map repeatedly produces the same structural alternative: dangerous channels may become large, but their co-location can activate a regularizing mechanism, so a residual configuration may attempt to spatially segregate them.

This note makes that pattern an explicit off-diagonal DSD object.

## 1. Observation region and active-vorticity set

Fix a natural local ball

\[
B=B_r(x_0)
\]

and let

\[
W=\|\omega\|_\infty.
\]

For a fixed threshold `0<a<1`, define

\[
V_a
=
\{x\in B:|\omega(x)|\ge aW\}.
\]

Its occupancy is

\[
\rho_V
=
\frac{|V_a|}{|B|}.
\]

In a residual configuration evading the vorticity line-sparseness gate at a bad point, the earlier volume-to-line lemma supplies a positive lower occupancy requirement at the theorem scale.

## 2. Set-overlap matrix

For any typed danger sets `A_i subset B`, define

\[
\rho_i=\frac{|A_i|}{|B|}
\]

and

\[
\boxed{
\Theta_{ij}
=
\frac{|A_i\cap A_j|}{|B|}.
}
\]

The exact Frechet bounds are

\[
\boxed{
\max(0,\rho_i+\rho_j-1)
\le
\Theta_{ij}
\le
\min(\rho_i,\rho_j).
}
\]

Thus two high-occupancy danger channels cannot be perfectly segregated.

This is elementary measure theory; its role here is bookkeeping, not a new regularity theorem.

## 3. Weighted overlap: direction-gradient versus intense vorticity

The exact vorticity-magnitude equation contains the penalty

\[
-\nu|\omega||\nabla\xi|^2.
\]

Define

\[
G_\xi(B)
=
\int_B|\nabla\xi|^2dx
\]

and, when `G_xi(B)>0`,

\[
\boxed{
\Sigma_{\xi V}
=
\frac{
\int_{V_a}|\nabla\xi|^2dx
}{
\int_B|\nabla\xi|^2dx
}.
}
\]

Then

\[
\int_B
\frac{|\omega|}{W}|\nabla\xi|^2dx
\ge
\int_{V_a}
\frac{|\omega|}{W}|\nabla\xi|^2dx
\ge
\boxed{
a\Sigma_{\xi V}G_\xi(B).
}
\]

Therefore the direction-gradient channel has an exact two-branch decomposition.

### Direction-overlap branch

If

\[
\Sigma_{\xi V}\ge\theta,
\]

then at least the fraction `theta` of the direction-gradient energy lies inside the intense-vorticity region, and

\[
\boxed{
\int_B
\frac{|\omega|}{W}|\nabla\xi|^2dx
\ge
a\theta G_\xi(B).
}
\]

For `theta=1/2`, half or more of the direction-gradient channel directly contributes in a region where the vorticity weight is order one.

### Direction-segregation branch

If

\[
\Sigma_{\xi V}<\theta,
\]

then more than `1-theta` of the direction-gradient energy is carried by the complement

\[
B\setminus V_a,
\]

where vorticity magnitude is below `aW`.

This is the precise version of the residual **interface/segregation** mechanism: directional defects are displaced away from the most intense vorticity.

The present note does not show that this mechanism is impossible.

## 4. Weighted overlap: positive middle strain versus intense vorticity

For `q>=1`, define

\[
S_{2,q}(B)
=
\int_B(\lambda_2^+)^qdx
\]

and

\[
\boxed{
\Sigma_{2V}^{(q)}
=
\frac{
\int_{V_a}(\lambda_2^+)^qdx
}{
\int_B(\lambda_2^+)^qdx
}
}
\]

when the denominator is nonzero.

This distinguishes the two branches already identified in the middle-eigenvalue residual note:

- large `Sigma_2V`: positive middle strain is substantially co-located with intense vorticity;
- small `Sigma_2V`: the Miller-critical middle-strain budget is spatially separated from the intense-vorticity core.

The distinction between

\[
\Lambda_{2,M}
\quad\text{and}\quad
\Lambda_{2,\infty}
\]

is the pointwise extreme version of the same off-diagonal information.

## 5. Generic weighted overlap matrix

Let nonnegative typed intensities on `B` be

\[
f_1,f_2,\ldots,f_N.
\]

Examples include

\[
\frac{|\omega|}{W},
\qquad
r^2|\nabla\xi|^2,
\qquad
r^2\lambda_2^+,
\qquad
r^2\lambda_3a_3^2,
\qquad
\text{higher-derivative normalized amplitudes}.
\]

Define normalized first moments

\[
\mu_i=\int_B f_i dx
\]

and off-diagonal products

\[
\boxed{
\mathsf O_{ij}
=
\frac{
\int_B f_if_jdx
}{
(\int_B f_idx)(\int_B f_jdx)/|B|
}
}
\]

when denominators are nonzero.

`O_ij>1` signals positive spatial co-location relative to uniform mixing; `O_ij<1` signals segregation.  This statistic is descriptive only and is not itself a regularity criterion.

For proof work, the unnormalized overlap integrals should be retained alongside this normalized diagnostic.

## 6. DSD role

### Formation

Each intensity/set is typed.  In particular the direction-gradient channel is inapplicable where the chosen direction representation is undefined; it must not be zero-padded through vorticity zeros.

### 축 속성공리계

Alignment channels such as `a_3^2` and strain eigen-directions remain properties of the realized 3D axes, not new axes.

### Static Aggregation

The diagonal entries contain single-channel occupancy/energy.  The off-diagonal entries contain co-location/segregation information that is destroyed by separate scalar aggregation.

### Structural Reorganization Dynamics

Track

\[
\mathsf O_{ij}(t,r)
\]

through the moving observation window and across physical scales.

## 7. Residual singularity branch tree

The current residual class must repeatedly choose among the following.

### Vorticity direction

Either

\[
\Sigma_{\xi V}\text{ is not small},
\]

so direction-gradient diffusion acts substantially inside the intense core,

or

\[
\Sigma_{\xi V}\text{ is small},
\]

so the direction defects are spatially segregated into lower-vorticity regions.

### Middle strain

Either

\[
\Sigma_{2V}^{(q)}\text{ is not small},
\]

so the middle-strain critical budget is co-located with the intense core,

or it is small, forcing the global Miller-critical strain divergence to live elsewhere while the vorticity maximum is driven by the extensional-alignment branch.

Thus a residual singularity is increasingly characterized not just by large amplitudes but by a particular **spatial arrangement of channels**.

## 8. Why segregation may feed the higher-derivative branch

Spatially separating two large-amplitude structures requires transition layers.  It is plausible that persistent segregation of vorticity magnitude, direction, and strain should create a cost in higher spatial derivatives or interface geometry.

However this is not automatic: without a quantitative transition-width estimate, an overlap deficit does not by itself lower-bound a derivative norm.

Therefore the next rigorous target is

\[
\boxed{
\text{persistent channel segregation}
\Longrightarrow
\text{quantitative higher-derivative / interface cost}.
}
\]

This is precisely where the external higher-derivative sparseness framework and the DSD derivative generating-function block can be coupled.

Status: **OPEN SEGREGATION-TO-DERIVATIVE-COST ESTIMATE**.
