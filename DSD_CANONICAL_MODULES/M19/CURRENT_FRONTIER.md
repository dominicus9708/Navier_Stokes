# M19 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M19-019**  
**Status:** ACTIVE CALCULATION / THREE-ROOT CLOSURE LINE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase boundary

M18 is frozen as the analysis/audit family.
M19 is the active calculation family.
M19 may use M18 results only at the certification level actually established there.

\[
\boxed{
\text{M18 certified analysis}
\Longrightarrow
\text{M19 calculation}
\Longrightarrow
\text{closure or a precisely exposed theorem frontier}.
}
\]

## 2. M19-001--004 — finite CE-H population-current calculation

The material-population current is reduced by Dirichlet-to-Neumann decomposition and weighted graph Hodge projection to

\[
\bar j
=
\bar G B^T\bar V
+r^{pump}+\bar r^{mode}+\bar r^{src}.
\]

A fixed symmetric conductance gradient cannot support a nonzero conservative cycle.
Every fixed cycle must pay a non-gradient defect.

The defects descend as follows:

\[
G_{boundary\ mode}
\to G_{palinstrophy/interface},
\]

\[
\Delta u_p
=\rho^p(\kappa+G_p),
\qquad
G_p=(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2,
\]

and conductance pumping satisfies

\[
G'
=\int_C\nabla h\cdot A'\nabla h,
\qquad
A'=JF^{-1}\left(\frac12I-2\Sigma\right)F^{-T}.
\]

Hence the finite graph current introduces no independent CE-H currency.

## 3. M19-005--012 — R-AC calculation frontier

### Signed candidates

The first-hitting clock satisfies the exact discounted coboundary

\[
L_j=\Theta_j-q^{-1}\Theta_{j+1},
\qquad
\sum_jq^{-j}L_j=\Theta_0.
\]

Thus it cannot remove the ancestry discount.

Material vorticity flux is scale critical, but bounded recurrent flux permits sign-reversing variation and no finite original-parent total-variation budget is certified.
A scaling calculation rules out scale-free control of that variation by standard kinetic-energy dissipation.
The present signed-budget shortcuts are therefore exhausted.

### Direct return-weight kinematics

For age ratio

\[
K_k=q^{k/2},
\]

a plain return episode pays only

\[
K_k^{-2}
\]

in ancestor-normalized dwell.
The sufficient ancestry threshold requires

\[
M_k\gtrsim K_k^2J_k^{1/2}
\]

plain episodes unless there is enhanced trapping/residence.

Parabolic transport supplies order

\[
K_k^2
\]

descendant time slots in an order-one parent window, so the obstacle is occupancy rather than a shortage of kinematic opportunities.

On a fixed parent annulus, similarity-time occupation and descendant parabolic-slot occupation are uniformly equivalent. Thus no logarithmic-time Jacobian loss remains.

### EVENT-ALIGN reduction

Finite lineage saturation reduces the quiet branch to one persistent lineage carrying divergent represented cubic shell mass while aligned ancestry-return occupancy or incidence becomes too small.

Positive production on another lineage does not force transfer, because recurrent node balance depends on the net surplus

\[
S_{p,i}=A_{p,i}-D_{p,i}-c_pM_{p,i},
\]

not on production alone.

Hence the exposed R-AC theorem frontier is

\[
\boxed{
\mathcal T_{AC}:
\text{lineage-shell incidence / aligned occupancy / node-surplus correlation theorem}.
}
\]

Further rearrangement of existing budget, graph, or recurrence arguments does not close this frontier.

## 4. M19-013--019 — R-critical calculation frontier

### Physical critical-tail normal form

The normalized critical tail is exactly the parent kinetic Morrey density

\[
\mathcal M_u(x,r,t)
=\frac1r\int_{B_r(x)}|u|^2dx,
\]

or annular version

\[
\mathcal A_u(x,r,t)
=\frac1r\int_{r<|z-x|<2r}|u|^2dz.
\]

Order-one critical shells cost only physical energy \(O(r)\), so even infinitely many geometric shells and positive log-density critical stacks are compatible with finite physical energy and ordinary dissipation.

### Spectral/scattering reduction

A critical annulus splits into normalized infrared \(\dot H^{-1}\) mass or high relative frequency, with a localization firewall on the Fourier formulation.

On the passive spectator branch, the sharper M5-567 scattering representation is used:

\[
U_Y(y,\theta)
=\frac1{|y|}
A_Y\left(\log|y|-\frac\theta2,\frac y{|y|}\right)
+O(|y|^{-3}).
\]

The Morrey charge is a fixed-length local \(L^2\) mass of \(A\) in log radius.
Strong \(L^3\) corresponds to

\[
A\in L^3(\mathbb R_q\times S^2).
\]

A translation-invariant probability measure supported on finite \(L^p(\mathbb R_q\times S^2)\), \(1\le p<\infty\), is concentrated at zero. Hence a nontrivial recurrent scattering factor cannot be globally strong \(L^3\).

On a nonzero ergodic weak-critical factor, critical Morrey annuli occur with positive log-density, but their physical energy remains geometrically summable.

### Stress firewall

Along the outward characteristic,

\[
\partial_\tau V
=R_0^{-2}e^{-\tau}\mathcal R[V,P],
\]

so stress/nonlinearity is an integrable subleading residual relative to the leading log-translation dynamics.
Stationary stress/point-force rigidity therefore does not automatically extend to aperiodic recurrent scattering.

The exposed general R-critical theorem frontier is

\[
\boxed{
\mathcal T_{critical}:
\text{aperiodic weak-critical scattering }q\text{-cocycle / rigidity theorem}.
}
\]

### Conditional CE-H harmonic subbranch

Under the additional M17-349--350 coefficient-compact harmonic-exterior hypotheses, the weak-critical obstruction is the toroidal dipole

\[
\Omega(x)=\frac{a\times x}{|x|^3}+O(|x|^{-3}),
\qquad a\ne0.
\]

M19-019 proves away from the axis

\[
L_{annulus}\gtrsim R^2,
\qquad
N_{wind}(R)\gtrsim R,
\qquad
\Phi_{through}(R)\lesssim R^{-1}.
\]

The resulting tube volume saturates the \(R^3\) annular scaling rather than contradicting it.
The conditional frontier is winding/reuse, bounded toroidal topology, or axial/lower-order escape.

## 5. Active root now: R-remote / Type-II

R-AC and R-critical have been reduced to explicit new theorem frontiers. The next calculation complex is

\[
\boxed{\mathcal R_{remote}}.
\]

M18 already identifies the principal remote/Type-II branches as:

- Euler-scale compact ancient profile;
- Euler-scale noncompact source;
- iterated remote/historical recycling;
- scale descent or spatial export;
- remote/high-frequency behavior.

M19 should now recover the exact Type-II/Euler rescaling, determine which quantities survive viscosity loss, and test whether the remote cascade can be reduced to already exposed R-critical/R-AC frontiers or a genuinely independent Euler ancient-profile rigidity problem.

## 6. Final integration still required

Even if the three root complexes were closed, the repository would still require:

1. arbitrary-singularity entry certification;
2. historical branch completeness beyond the active indexes;
3. a full beginning-to-end independent audit of the combined proof chain.

No global-regularity conclusion is currently justified.

## 7. Permanent firewalls

\[
\boxed{\text{CE-H internal closure}\neq\text{global NS closure}},
\]

\[
\boxed{\text{own-scale payment}\neq\text{fixed-parent ancestry payment}},
\]

\[
\boxed{\text{rerecording}\neq\text{multiplicity}},
\]

\[
\boxed{\text{high-frequency control}\neq\text{low-frequency tightness}},
\]

\[
\boxed{\text{positive recurrence density}\neq\text{divergent physical parent cost}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-019; NEXT = R-REMOTE / TYPE-II CALCULATION.}}
\]
