# M19 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M19-027**  
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

The three defects descend to already known continuum structures:

\[
G_{boundary\ mode}\to G_{palinstrophy/interface},
\]

\[
\Delta u_p=\rho^p(\kappa+G_p),
\qquad
G_p=(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2,
\]

and

\[
G'
=\int_C\nabla h\cdot A'\nabla h,
\qquad
A'=JF^{-1}\left(\frac12I-2\Sigma\right)F^{-T}.
\]

Hence finite graph current introduces no independent CE-H currency.

## 3. M19-005--012 — R-AC theorem frontier

The first-hitting clock has the exact discounted coboundary

\[
L_j=\Theta_j-q^{-1}\Theta_{j+1},
\qquad
\sum_jq^{-j}L_j=\Theta_0,
\]

so it cannot remove the ancestry discount.

Material vorticity flux is scale critical but recurrent total variation has no certified finite original-parent budget, and scaling rules out a scale-free control of that variation by standard kinetic-energy dissipation.

For age ratio

\[
K_k=q^{k/2},
\]

a plain return episode pays only \(K_k^{-2}\) in ancestor-normalized dwell. The sufficient threshold therefore requires

\[
M_k\gtrsim K_k^2J_k^{1/2}
\]

effective episodes unless residence is enhanced.

Parabolic transport itself supplies order \(K_k^2\) descendant time slots in one order-one parent window, so the missing ingredient is occupancy/alignment, not kinematic opportunity.

Finite-lineage saturation and node-balance analysis reduce the surviving quiet branch to

\[
\boxed{
\mathcal T_{AC}:
\text{lineage-shell incidence / aligned occupancy / node-surplus correlation theorem}.
}
\]

This is the exposed R-AC theorem frontier.

## 4. M19-013--019 — R-critical theorem frontier

The normalized critical tail is exactly the parent kinetic Morrey density

\[
\mathcal M_u(x,r,t)
=\frac1r\int_{B_r(x)}|u|^2dx.
\]

Order-one critical shells cost only physical energy \(O(r)\), so geometric recurrence and even positive log-density are compatible with finite parent energy.

On the passive spectator branch,

\[
U_Y(y,\theta)
=\frac1{|y|}
A_Y\left(\log|y|-\frac\theta2,\frac y{|y|}\right)
+O(|y|^{-3}).
\]

Translation-invariant probability cannot be supported on nonzero finite global \(L^p(\mathbb R_q\times S^2)\) data. Thus every nontrivial recurrent scattering factor is genuinely weak-critical, not strong \(L^3\).

The general R-critical theorem frontier is

\[
\boxed{
\mathcal T_{critical}:
\text{aperiodic weak-critical scattering }q\text{-cocycle / rigidity theorem}.
}
\]

On the conditional coefficient-compact CE-H harmonic branch, the toroidal dipole requires

\[
L_{annulus}\gtrsim R^2,
\qquad
N_{wind}(R)\gtrsim R,
\qquad
\Phi_{through}(R)\lesssim R^{-1},
\]

and saturates rather than exceeds the annular \(R^3\) volume scale.

## 5. M19-020--025 — nondegenerate R-remote branch

For the remote Type-II source,

\[
R_j=K_jr_j,
\qquad
U_j^E=\frac{\nu K_j}{r_j},
\qquad
\varepsilon_j=K_j^{-2},
\]

and define

\[
\boxed{\Lambda_j:=K_j^5r_j.}
\]

Finite physical kinetic energy plus the fixed normalized source oscillation gives

\[
\boxed{K_j^5r_j\lesssim1,}
\]

hence

\[
R_j\lesssim r_j^{4/5}\to0.
\]

Thus normalized remoteness does not imply physical macroscopic export.

If

\[
\Lambda_j\ge\Lambda_->0,
\]

then the original physical inertial frame gives uniform local and global source-scale \(L^2\) control:

\[
\|V_j(\tau)\|_2^2
=\frac{\|u(t_j+T_j^E\tau)\|_2^2}{\nu^2\Lambda_j}
\le \frac{E_0}{\nu^2\Lambda_-}.
\]

Together with the Euler-scaled vorticity cap and interior div--curl, this yields local \(H^1\) bounds.

In divergence-free weak form pressure disappears, and

\[
\partial_\tau V_j
\]

is uniformly bounded in a fixed negative Sobolev space. Aubin--Lions/Simon therefore gives strong local spacetime \(L^2\) compactness and a nontrivial ancient Euler limit.

The previously provisional coherent-Galilean-frame defect is removed on this nondegenerate branch by using the original physical inertial frame.

More strongly, M19-025 converts the source oscillation lower bound back to physical variables:

\[
\int_{D_{R_j}}|u(x,t_j)|^2dx
\gtrsim
\nu^2\Lambda_j.
\]

Thus \(\Lambda_j\ge\Lambda_->0\) forces fixed positive kinetic energy into regions of radius \(R_j\to0\). The pre-singular kinetic-energy measures therefore develop an atom at the singular point unless a strong left \(L^2\) terminal trace fails.

Hence

\[
\boxed{
\mathcal R_{remote}^{nondeg}
\to
\mathcal R_{critical}^{terminal\ trace/energy\ defect}.
}
\]

The nondegenerate remote branch is no longer an independent upstream root.

## 6. M19-026--027 — dilute R-remote branch

The genuinely remote residual is

\[
\boxed{\Lambda_j\to0.}
\]

Define local source variance

\[
E_j^E(D)
:=
\inf_b\int_D|V_j-b|^2dy.
\]

Because \(\|\Omega_j^E\|_\infty\le q\), a local Helmholtz decomposition shows that any divergence

\[
E_j^E(D)\to\infty
\]

must come from a curl-free harmonic velocity component

\[
H_j=\nabla\phi_j,
\qquad
\Delta\phi_j=0,
\]

with diverging trace-free strain. It is not vorticity-amplitude blowup.

A Biot--Savart shell split gives a logarithmic ceiling. Intermediate dyadic shells contribute at most \(O(q)\) each, while the far tail satisfies

\[
|S_{far}|
\lesssim
\|V_j\|_2L^{-5/2}
\lesssim
\Lambda_j^{-1/2}L^{-5/2}.
\]

Optimizing at

\[
L_j=\Lambda_j^{-1/5}
\]

gives

\[
\boxed{
|S_{harm,j}|
\lesssim
C\bigl(1+q|\log\Lambda_j|\bigr),
}
\]

and

\[
E_j^E(D)
\lesssim
C\bigl(1+|\log\Lambda_j|^2\bigr).
\]

Consequently the physical energy on the main dilute source scale obeys

\[
\boxed{
\Lambda_jE_j^E(D)\to0.
}
\]

The remote shells capable of producing this logarithmic harmonic strain lie, at worst, inside physical radius

\[
R_j\Lambda_j^{-1/5}=r_j^{4/5}\to0.
\]

Thus the remaining noncompact remote object is an intermediate-scale logarithmic harmonic-strain halo collapsing to the singular point.

## 7. Updated three-root status

### R-AC

Reduced to one explicit new theorem:

\[
\boxed{\mathcal T_{AC}}.
\]

### R-critical

Reduced to the aperiodic scattering rigidity theorem plus terminal-trace/energy-defect structure:

\[
\boxed{\mathcal T_{critical}}.
\]

The nondegenerate remote branch now feeds into this root.

### R-remote

The independent residual is now chiefly

\[
\boxed{
\Lambda_j\to0
+
\text{intermediate-scale harmonic-strain/source-tail halo}
}
\]

plus already typed derivative/frequency/domain noncompactness.

The next calculation should determine whether this logarithmic halo must pay sufficient strain action over time, or whether temporal sparsity simply converts it into an R-AC style occupancy defect.

## 8. Final integration still required

Even if the three root complexes are closed, the repository still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness beyond the active indexes;
3. a full beginning-to-end independent audit of the combined proof chain.

No global-regularity conclusion is currently justified.

## 9. Permanent firewalls

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
\boxed{\text{M19 ACTIVE TIP = M19-027; NEXT = DILUTE REMOTE HALO TEMPORAL-ACTION CALCULATION.}}
\]
