# M19 Current Frontier

**Date:** 2026-09-11  
**Status:** ACTIVE CALCULATION / CLOSURE LINE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase boundary

M18 is frozen as the analysis/audit family.

M19 is the active calculation family.

M19 may use M18 results only at the certification level actually established there.

The standing workflow is

\[
\boxed{
\text{M18 certified analysis}
\Longrightarrow
\text{M19 calculation}
\Longrightarrow
\text{closure or a precisely exposed new defect}.
}
\]

## 2. First calculation complex

The first M19 calculation complex is the compact CE-H finite-population redistribution problem.

M18 provides, for a material population interface \(S_{ij}\),

\[
 e_{ij}^{(p)}
 =
 \int_{S_{ij}}
 \rho^{p-1}\partial_{n_i}\rho\,dS
 =
 \int_{S_{ij}}
 \partial_{n_i}u_p\,dS,
 \qquad
 u_p:=\frac{\rho^p}{p}.
\]

It also provides antisymmetry

\[
 e_{ij}^{(p)}=-e_{ji}^{(p)}.
\]

The continuum mechanism is gradient diffusion, but the finite lineage graph can carry a cycle-space current after coarse graining.

The immediate task is to calculate exactly what part of the coarse current is a symmetric conductance gradient and what part requires unresolved boundary modes, bulk forcing, or geometry loss.

## 3. M19-001 target

On a controlled connector collar between two persistent populations, construct the Laplace/Poisson Dirichlet-to-Neumann decomposition

\[
\boxed{
 j_{ij}
 =
 G_{ij}(V_i-V_j)
 +r_{ij}^{mode}
 +r_{ij}^{src},
}
\]

with

\[
G_{ij}=G_{ji}>0.
\]

Then prove that a divergence-free finite-network current cannot be supported solely by the conductance-gradient part.

## 4. M19-002 target

Use weighted discrete Hodge orthogonality to prove a quantitative defect floor:

\[
\boxed{
\|j_{cycle}\|_{G^{-1}}
\le
\|r\|_{G^{-1}}.
}
\]

Thus any fixed nonzero conservative cycle forces a fixed non-gradient defect.

## 5. Later calculation complexes

After the CE-H current-cycle calculation, M19 must return to the three M18 upstream roots:

\[
\mathcal R_{remote},
\qquad
\mathcal R_{critical},
\qquad
\mathcal R_{AC}.
\]

The downstream CE-H calculation is not a substitute for those root closures.

## 6. Permanent firewalls

M19 inherits all M18 firewalls, in particular:

\[
\boxed{\text{CE-H internal closure}\neq\text{global NS closure}},
\]

\[
\boxed{\text{own-scale payment}\neq\text{fixed-parent ancestry payment}},
\]

\[
\boxed{\text{rerecording}\neq\text{multiplicity}}.
\]

---

\[
\boxed{\text{M19 ACTIVE CALCULATION LINE STARTED.}}
\]
