# M19-374 — Multi-sheet relabeling static geometry reduces to a positive-rate dynamic triad

**Date:** 2026-09-18  
**Status:** HISTORICAL-REIMPORT SYNTHESIS / M5-651--665 CANONICAL REDUCTION / STATIC SILENT MULTI-SHEET GEOMETRY EXHAUSTED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Starting point

M19-373 corrected the overstrong M19-372 reading and retained

\[
\boxed{
F_{cross\text{-}level}^{\mathfrak A\ne0}
\lor
R_{multi\text{-}sheet/patching}.
}
\]

The present module reimports M5-651--665 to determine how much of the second branch is already classified.

Write

\[
\rho=|W|,
\qquad
h=D_B\kappa.
\]

## 2. Every persistent lineage has a same-amplitude-component negative payer

M5-656--657 use the CE-H parallel amplitude equation

\[
\Delta\rho=(\kappa+|\nabla\xi|^2)\rho
\]

with a fixed superlevel component \(C_L\subset\{\rho>a_0\}\) containing a persistent fixed-flux lineage.

For

\[
w_L=\rho(\rho-a_0),
\]

the exact component identity is

\[
\boxed{
\int_{C_L}\kappa w_L\,dy
=
-\int_{C_L}|\nabla\rho|^2dy
-\int_{C_L}\rho(\rho-a_0)|\nabla\xi|^2dy.
}
\]

The fixed carrier amplitude ball gives a uniform Dirichlet floor, hence a fixed strongly-negative coherent packet

\[
\boxed{
P_L^-\subset C_L,
\qquad
\rho\ge a_-/2,
\qquad
\kappa\le-\kappa_-/2,
\qquad
|\Phi_-|\ge\phi_->0.
}
\]

Thus payer outsourcing cannot be remote or purely low-amplitude. It must occur inside one connected high-amplitude component.

## 3. Regular silent patching cannot change the scalar law

On a regular high-amplitude corridor,

\[
\rho>a_0,
\qquad
\nabla\kappa\ne0,
\qquad
\nabla\kappa\times\nabla h=0,
\]

M5-658 shows that

\[
h=f(\kappa,\theta)
\]

continues uniquely along any connected regular path.

Therefore a genuine sheet change must meet either

\[
\boxed{
\nabla\kappa\times\nabla h\ne0
}
\]

or

\[
\boxed{
\nabla\kappa=0.
}
\]

The quotient-free regular event is

\[
\mathfrak A
=a^5\big[\nabla\kappa\times\nabla(D_B\kappa)\big],
\qquad a=|W|^2.
\]

## 4. Critical patching is finite-order

At an active critical point,

\[
W\cdot\nabla\kappa=0
\]

implies

\[
(\nabla^2\kappa)W=0.
\]

M5-659 eliminates a nondegenerate transverse Morse point as a silent multi-sheet branch. A genuinely silent branch therefore requires transverse Hessian degeneracy.

M5-663 then uses spatial analyticity and compactness to exclude infinite-order flatness. There are constants

\[
\boxed{m_*<\infty,
\qquad c_*>0}
\]

such that every retained active critical point has some finite order \(m\le m_*\) with

\[
|\nabla^m\kappa|\ge c_*.
\]

## 5. Finite-order critical hypersurfaces have an exact crossing law

For a smooth critical hypersurface with first nonzero normal coefficient jet

\[
\partial_n^j\kappa=0\quad(1\le j<m),
\qquad
\partial_n^m\kappa\ne0,
\]

M5-664 gives

\[
\boxed{
(B-V_\Sigma)\cdot n
=
\frac{
\partial_n^{m-1}(h-h_\Sigma)
}{
\partial_n^m\kappa
}.
}
\]

Hence either

\[
\boxed{
C_{crit}^{(m-1)}:
\partial_n^{m-1}(h-h_\Sigma)\ne0
}
\]

is a genuine higher-jet crossing/creation event, or the critical face is a material-normal barrier.

## 6. Silent material barriers cannot form a static recurrent network

For a material-normal critical face,

\[
(B-V_\Sigma)\cdot n=0.
\]

If a closed collection of such faces bounds a material cell \(\Omega\), then

\[
\nabla\cdot B=\frac32
\]

gives

\[
\boxed{
|\Omega(\theta)|
=|\Omega(\theta_0)|
\exp\left[\frac32(\theta-\theta_0)\right].
}
\]

A positive-volume cell therefore cannot remain indefinitely inside the fixed bounded recurrent similarity core.

If the cell meets the fixed amplitude boundary \(\rho=a_0\), M5-662 gives a positive-rate material sheath turnover through that boundary.

Analytic stratification plus the finite-order crossing law yields the M5-665 conclusion: lower-dimensional junction strata do not create an additional turnover-free static network.

## 7. Uniform event-free lifetime

If a retained sheet cell contains the fixed coherent carrier ball, then

\[
|\Omega_L|\ge v_0>0.
\]

Let \(V_{core}<\infty\) be the fixed storage volume. A turnover-free material cell can persist at most

\[
\boxed{
T_{cell}^{max}
\le
\frac23\log\frac{V_{core}}{v_0}.
}
\]

Thus a recurrent surviving architecture must produce a dynamic event with a uniformly bounded gap in the retained similarity dynamics.

## 8. Canonical reduction

The broad M19-373 multi-sheet branch therefore sharpens to

\[
\boxed{
R_{persistent\ relabeling}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{higher\text{-}jet}
\lor
T_{sheath}^{\rho=a_0}.
}
\]

where

1. \(C_{rot}^{force}\) is regular generalized-\(\kappa\)-force rotation;
2. \(C_{crit}^{higher\text{-}jet}\) is a finite-order critical crossing/creation event;
3. \(T_{sheath}^{\rho=a_0}\) is material turnover through a fixed amplitude threshold.

There is no independent static silent multi-sheet survivor under the retained analytic/high-amplitude compactness hypotheses.

## 9. Scope firewall

This is a branch reduction, not a contradiction.

The three dynamic mechanisms may recur on a compact state space. M5-665 does not provide a finite cumulative resource exhausted by their repetition.

If the analytic/high-amplitude compactness, fixed carrier ball, stratification, representation, or bounded-core hypotheses fail, that failure remains an explicit decompactification/interface/domain exit.

## 10. Next target

The next problem is no longer topology classification. It is a resource question:

\[
\boxed{
\mathcal T_{dyn}^{nonreuse}:
\text{does positive-rate activity in }
C_{rot}^{force}
\lor C_{crit}^{higher\text{-}jet}
\lor T_{sheath}^{\rho=a_0}
\text{ consume a nonrecyclable critical resource?}
}
\]

M5-666--688 and M17-186--190 provide the relevant stationary amplitude/\(\kappa\)-space payer ledgers and must be audited next.

---

\[
\boxed{\text{M19-374 COMPLETE; STATIC MULTI-SHEET GEOMETRY IS REDUCED TO A POSITIVE-RATE DYNAMIC TRIAD.}}
\]
