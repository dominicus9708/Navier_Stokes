# M19 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M19-035**  
**Status:** ACTIVE CALCULATION / ROOT RECOMPRESSION / EXPLICIT THEOREM FRONTIERS

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase policy

M18 is frozen as the analysis/audit family.
M19 is the active calculation family.
M19 may use M18 statements only at the certification level actually established there.

\[
\boxed{
\text{M18 certified analysis}
\Longrightarrow
\text{M19 calculation}
\Longrightarrow
\text{closure or an explicit theorem frontier}.
}
\]

## 2. M19-001--004 — CE-H finite population current

The finite material-population current was decomposed as

\[
\bar j
=
\bar G B^T\bar V
+r^{pump}+\bar r^{mode}+\bar r^{src}.
\]

Weighted graph Hodge projection shows that a nonzero conservative cycle cannot be supported by the symmetric conductance gradient alone.

The residuals descend to known continuum structures:

- pump \(\to\) strain/connector geometry;
- boundary mode \(\to\) palinstrophy/interface gradients;
- bulk source \(\to\) CE-H coefficient + normalized diffusion.

Thus the graph current is not an independent CE-H currency.

## 3. M19-005--012 and M19-034 — R-AC

The clock has the exact discounted coboundary

\[
L_j=\Theta_j-q^{-1}\Theta_{j+1},
\qquad
\sum_jq^{-j}L_j=\Theta_0,
\]

so signed clock bookkeeping does not erase ancestry discount.

For age ratio

\[
K=q^{k/2},
\]

one natural return episode carries the ancestor-time fraction

\[
K^{-2}.
\]

A sufficient temporal-return threshold requires order

\[
K^2J_k^{1/2}
\]

effective episodes unless residence is enhanced.

M19-033 adds the spatial eccentricity threshold: a shell at distance \(d=Kr\) needs order

\[
K
\]

comparable first-hitting packets to form an order-one critical Morrey shell.

M19-034 shows that the same child event has joint parent space-time fraction

\[
\boxed{K^{-1}K^{-2}=K^{-3}.}
\]

Hence spatial and temporal marginal ledgers cannot be naively multiplied into a stronger ancestry payer.

The exposed R-AC theorem is now explicitly a same-event correlation theorem:

\[
\boxed{
\mathcal T_{AC}^{corr}:
\text{cubic-mass-bearing lineage}
\Rightarrow
\text{jointly aligned shell occupancy + ancestral return}
\lor
\text{typed replacement/export/deformation exit}.
}
\]

No further unsigned scaling rearrangement currently improves this frontier.

## 4. M19-013--019 and M19-035 — R-critical

The critical velocity tail is represented by the parent kinetic Morrey density

\[
\mathcal M_u(x,r,t)
=\frac1r\int_{B_r(x)}|u|^2dx.
\]

On the passive spectator branch,

\[
U_Y(y,\theta)
=
\frac1{|y|}
A_Y\left(\log|y|-\frac\theta2,\frac y{|y|}\right)
+O(|y|^{-3}),
\]

with translation covariance

\[
A_{\sigma_tY}(q)=A_Y(q-t/2).
\]

A nontrivial translation-invariant recurrent factor cannot be supported on finite global \(L^p(\mathbb R_q\times S^2)\) scattering data; in particular it is genuinely weak-critical rather than strong \(L^3\).

M19-035 calculates why one more local asymptotic order does not close this branch. For

\[
U_0=r^{-1}A(q,\omega),
\qquad
q=\log r-\theta/2,
\]

the similarity transport operator satisfies

\[
\mathcal L_{sim}U_0=0
\]

for arbitrary sufficiently regular \(A\).

The first Navier--Stokes residual is \(O(r^{-3})\), while

\[
\mathcal L_{sim}[r^{-3}B]=-r^{-3}B.
\]

Thus the first residual is generically absorbed by the \(r^{-3}\) correction rather than imposing a solvability condition on \(A\).

The unique resonant sector is the leading \(r^{-1}\) datum itself.

Therefore the general R-critical frontier remains

\[
\boxed{
\mathcal T_{critical}:
\text{global }q\text{-translation/cocycle rigidity for the resonant weak-critical datum}.
}
\]

## 5. M19-020--029 — strong remote / Type-II source

For remote source ratio \(K_j\),

\[
R_j=K_jr_j,
\qquad
U_j^E=\frac{\nu K_j}{r_j},
\qquad
\varepsilon_j=K_j^{-2}.
\]

Define

\[
\Lambda_j:=K_j^5r_j.
\]

Finite physical energy gives

\[
K_j^5r_j\lesssim1,
\qquad
R_j\lesssim r_j^{4/5}\to0.
\]

On \(\Lambda_j\ge\Lambda_->0\), the original inertial frame supplies global source-scale \(L^2\) control. Together with the Euler-scaled vorticity cap, pressure-free weak formulation, and Aubin--Lions, this yields a nontrivial finite-energy ancient Euler limit.

The same branch forces fixed physical kinetic energy into balls of radius \(R_j\to0\), hence a terminal energy-measure atom unless the strong left \(L^2\) trace fails.

More directly, M19-029 uses the M5-443 source oscillation floor and finite-measure Lorentz embedding to obtain

\[
\boxed{
\|u(t_j)\|_{L^{3,\infty}}
\gtrsim
\nu K_j^2.
}
\]

Therefore

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
G_{weak-L^3\ escalation}.
}
\]

Strong remote/Type-II throughput is not an independent quiet root inside bounded W1.

## 6. M19-026--027 — dilute harmonic-strain halo

On \(\Lambda_j\to0\), bounded Euler-scaled vorticity implies that any local velocity-variance divergence is carried by a curl-free harmonic strain component.

A Biot--Savart shell split gives the logarithmic ceiling

\[
\boxed{
|S_{harm,j}|
\lesssim
C(1+q|\log\Lambda_j|),
}
\]

and

\[
E_j^E(D)
\lesssim
C(1+|\log\Lambda_j|^2).
\]

Thus the physical energy of the main dilute source tends to zero and the noncompactness is an intermediate-scale logarithmic halo rather than a fixed-energy source atom.

## 7. M19-030--033 — residual weak remote recursion

M5-402 and M5-405 combined with M19-029 show that, under bounded weak-\(L^3\), a remote branch cannot terminate quietly:

\[
\boxed{
\text{remote activity + no typed exit}
\Longrightarrow
\text{infinite weak remote/shell-H recursion}.
}
\]

Restore one common physical frame. If

\[
r_{m+1}=r_m\ell_m,
\qquad
|x_{m+1}-x_m|=r_mD_m,
\qquad
K_m=D_m/\ell_m,
\]

then

\[
\boxed{
|x_{m+1}-x_m|=K_mr_{m+1}.
}
\]

Hence bounded physical jumps force physical scale descent; no scale descent forces large physical export.

If the centers converge to \(x_\infty\), define eccentricity

\[
\eta_m=\frac{|x_m-x_\infty|}{r_m}.
\]

A first-hitting velocity-variance floor yields

\[
\frac1{\rho_m}
\inf_c\int_{B_{\rho_m}(x_\infty)}|u-c|^2dx
\gtrsim
\frac{\nu^2}{\eta_m+C},
\qquad
\rho_m=r_m(\eta_m+C).
\]

Thus bounded eccentricity produces R-critical Morrey activity.

For off-center packets with \(\eta=d/r\gg1\), one packet contributes only order \(\eta^{-1}\) of the common-center critical shell scale. Order \(\eta\) comparable packets are needed for a critical shell.

Therefore

\[
\boxed{
G_{off-center\ remote}
\Longrightarrow
\mathcal R_{critical}
\lor
\mathcal R_{AC}
\lor
G_{typed\ common-mode/export}.
}
\]

The independent R-remote root has consequently been reduced to a narrow representation bridge between common-frame nested/wandering events and the already exposed R-AC/R-critical event classes.

## 8. Current root picture

The active calculation now exposes essentially two major new mathematical theorem frontiers plus one representation bridge:

\[
\boxed{
\mathcal T_{AC}^{corr}
}
\]

for same-lineage space-time ancestry correlation,

\[
\boxed{
\mathcal T_{critical}
}
\]

for aperiodic weak-critical scattering rigidity,

and

\[
\boxed{
\mathcal B_{remote\to AC/critical}
}
\]

for final event-class identification of the residual weak remote recursion.

Strong remote throughput itself has been routed to weak-\(L^3\) escalation and is no longer an independent quiet root.

## 9. Final integration still required

Even if the three displayed frontiers are closed, the repository still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness beyond active indexes;
3. a full beginning-to-end independent audit of the combined proof chain.

No global-regularity conclusion is currently justified.

## 10. Permanent firewalls

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
\boxed{\text{marginal spatial and temporal occupancy}\neq\text{joint same-event incidence}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-035.}}
\]
