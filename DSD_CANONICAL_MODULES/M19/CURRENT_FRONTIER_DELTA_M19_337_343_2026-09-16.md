# M19 Current Frontier Delta — M19-337 through M19-343

**Date:** 2026-09-16  
**Delta tip:** **M19-343**  
**Status:** ACTIVE CALCULATION / SPATIAL MIXED-SIGN CE-H BRANCH REDUCED TO MEASURE TRANSFER, SIGN-RESOLVED AMPLITUDE, ZERO-SWEEP, AND DIFFUSE BASELINE GEOMETRY / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. M19-337 — exact enstrophy-line to flux-line measure bridge

For the regular flux-line family,

\[
E=\int L_1d\nu,
\qquad
\Phi=\int d\nu,
\qquad
L_1(\lambda)=\int_{\Gamma_\lambda}\rho\,ds.
\]

With

\[
dp_\Phi=d\nu/\Phi,
\qquad
\bar L_1=E/\Phi,
\]

M19-323's enstrophy line probability satisfies the exact Radon--Nikodym relation

\[
\boxed{
 d\Pi
 =
 \frac{L_1}{\bar L_1}dp_\Phi.
}
\]

Thus M19-334's coefficient-population incidence gap is no longer vague. A fixed \(\Pi\)-population transfers to a fixed flux population unless normalized line residence \(L_1/\bar L_1\) concentrates.

New explicit exit:

\[
\boxed{G_{\rm line\text{-}residence\ segregation}.}
\]

## 2. M19-338 — sign-resolved flux currency

For the positive flux probability \(p_\Phi\), define

\[
\eta_\pm=p_\Phi\{\pm\kappa>0\},
\]

and conditional flux-weighted normalized amplitudes \(\mathfrak a_\pm\). Then

\[
\boxed{
\mathfrak a_\Phi
=
\eta_+\mathfrak a_+
+
\eta_-\mathfrak a_-
+
\eta_0\mathfrak a_0.
}
\]

M17-441 gives \(\sum_m\mathfrak a_{\Phi,m}<\infty\) on retained positive-flux/good-time records, hence separately

\[
\boxed{
\sum_m\eta_{+,m}\mathfrak a_{+,m}<\infty,
\qquad
\sum_m\eta_{-,m}\mathfrak a_{-,m}<\infty.
}
\]

If both sign flux fractions stay uniformly positive, then both sign amplitudes are summable and tend to zero. If a sign amplitude stays bounded below, its flux fraction must thin summably.

For M17-442's quadratic-payer probability,

\[
\boxed{
\widehat\eta_\pm
=
\frac{\eta_\pm\mathfrak a_\pm}{\mathfrak a_\Phi}.
}
\]

Therefore fixed enstrophy/payer sign fractions can coexist with vanishing absolute flux currency. Weighted heterogeneity alone does not give a contradiction.

## 3. M19-339 — exact sign-resolved dynamics

Let

\[
h=D_t\kappa,
\]

and define signed zero-crossing transfer currents

\[
C_0^\Phi
=\int\delta(\kappa)h\,d\Phi,
\qquad
C_0^Q
=\int\delta(\kappa)hq\,d\Phi.
\]

Then

\[
\boxed{
\dot\Phi_+
=
\nu\int_{\kappa>0}\kappa d\Phi+C_0^\Phi,
}
\]

\[
\boxed{
\dot\Phi_-
=
\nu\int_{\kappa<0}\kappa d\Phi-C_0^\Phi.
}
\]

The sign-resolved amplitude law is

\[
\boxed{
\begin{aligned}
\frac d{dt}\log\mathfrak a_+
={}&
\langle\sigma+2\nu\kappa\rangle_{\widehat p_+}
-
\nu\langle\kappa\rangle_{p_+}\\
&+
\frac{C_0^Q}{Q_+}
-
\frac{C_0^\Phi}{\Phi_+},
\end{aligned}
}
\]

with the opposite crossing signs for \(\mathfrak a_-\).

The crossing contribution is an amplitude-biased sign-transfer current. It cancels from total flux and total quadratic currency, so total M17-442 dynamics can hide large internal sign exchange.

Permanent firewall:

\[
\boxed{C_0^{\Phi,Q}\ne J_0}
\]

without an additional representation/coarea theorem.

## 4. M19-340 — zero-crossing sweep bridge

On a regular transverse section, exact CE-H gives transverse \(\nabla\kappa\). The material-relative zero-level speed is

\[
\boxed{
v_0=-h/|\nabla\kappa|.
}
\]

Coarea yields

\[
\boxed{
C_{0,A}^\Phi
=-\int_{Z_A}\rho v_0d\ell,
}
\]

and

\[
\boxed{
C_{0,A}^Q
=-r^2\int_{Z_A}\rho^2v_0d\ell.
}
\]

For

\[
j_{0,A}=\int_{Z_A}\rho^2|\nabla\kappa|d\ell,
\]

speed/gradient compactness gives

\[
\boxed{
|C_{0,A}^Q|
\le
r^2\frac{V_*}{g_*}j_{0,A}.
}
\]

The unweighted flux-transfer current additionally requires a zero-level amplitude floor:

\[
\boxed{
|C_{0,A}^\Phi|
\le
\frac{V_*}{\rho_*g_*}j_{0,A}.
}
\]

Thus the exact residual is a low-amplitude zero corridor or zero-speed/gradient/high-jet/chart degeneration.

## 5. M19-341 — robust low-amplitude separator returns to palinstrophy

M17-446 permits coefficient contrast to hide in low-amplitude regions, but M17-447 shows that a robust finite-thickness low-amplitude separator inside a uniformly Poincare cross-section with substantial higher-amplitude populations pays an order-one palinstrophy packet.

If such states occupy parent-time fraction \(\beta_R\), then

\[
\boxed{
\mathcal P_{anc,R}^{bot}
\gtrsim
c\beta_RR.
}
\]

Hence persistent positive parent-time occupancy is impossible.

The surviving low-amplitude branch must therefore be sign-wide amplitude dilution, transverse neck/Poincare degeneration, flux participation thinning, time/longitudinal sparsity, or chart/genealogy loss.

## 6. M19-342 — conditional longitudinal coercivity

For a bounded-length represented tube with fixed tube enstrophy and positive flux, reference cross-sectional amplitude collapse forces longitudinal amplitude derivative and hence palinstrophy.

The key inequality is

\[
\boxed{
P_{\mathcal T}
\ge
\frac{\Phi}{M_qL_*^3}
\left(
\frac{E_{\mathcal T}}{\Phi}
-L_*\mathfrak a_{\Phi,0}
\right)_+^2.
}
\]

This is valid and useful for bounded-length productive subcarriers.

## 7. M19-343 scope correction — parent-length diffuse geometry is the baseline

M17-450 proves that the canonical retained positive-flux loop already has

\[
\ell_R\gtrsim R,
\]

\[
\mathfrak A_{H,R}\gtrsim R,
\]

and

\[
\boxed{
\overline{\mathfrak a}_{\Phi,R}
\lesssim
C/R.
}
\]

Thus the line-length escape from M19-342 is not pathological on the canonical full loop. It is the certified parent-length diffuse baseline.

Since geometric records satisfy

\[
\sum_mR_m^{-1}<\infty,
\]

record-inverse amplitude dilution is compatible with M17-441 ancestry summability.

If the represented tube also carries a fixed enstrophy lower bound and has length \(\asymp R\), then

\[
\boxed{
\overline{\mathfrak a}_{\Phi,R}\asymp R^{-1}.
}
\]

Define the excess-dilution variable

\[
\boxed{
\mathfrak b_{\Phi,R}
:=R\overline{\mathfrak a}_{\Phi,R}.
}
\]

The new dilution frontier is \(\mathfrak b_{\Phi,R}\to0\), not merely \(\mathfrak a_{\Phi,R}\to0\).

## 8. Current spatial mixed-sign branch

The M19-336 spatial branch is now compressed to

\[
\boxed{
\begin{aligned}
H_{\rm productive\ spatial\ mixed\text{-}sign}
\Longrightarrow{}&
G_{\rm line\text{-}residence\ segregation}\\
&\lor G_{\rm sign\ flux\ thinning}\\
&\lor H_{\rm parent\text{-}length\ baseline\ dilution}\\
&\lor G_{\rm excess\ sign\text{-}dependent\ dilution}\\
&\lor G_{\rm amplitude\text{-}biased\ zero\text{-}crossing\ transfer}\\
&\lor G_{\rm neck/Poincare/time\ degeneration}\\
&\lor G_{\rm zero\text{-}level\ speed/high\text{-}jet}\\
&\lor G_{\rm tube\ enstrophy\ incidence\ loss}\\
&\lor G_{\rm remote/interface/genealogy\ loss}.
\end{aligned}
}
\]

The simple robust separator and the simple bounded-length amplitude-collapse routes are no longer independent hard cores.

## 9. Immediate next target

Do not try to close the branch by treating \(\mathfrak a_\Phi\to0\) itself as anomalous. On the canonical parent-length diffuse carrier, \(\mathfrak a_\Phi\sim R^{-1}\) is natural.

The preferred next quantities are the sign-resolved baseline-normalized amplitudes

\[
\boxed{
R\mathfrak a_{+,R},
\qquad
R\mathfrak a_{-,R},
}
\]

and the carrier-to-productive-tube enstrophy incidence.

Determine whether M17-458 near-perfect sign cancellation plus M19-321--323 coefficient variance permits both sign populations to remain on the same \(R^{-1}\) diffuse baseline, or forces sign-dependent excess dilution, residence segregation, or zero-transfer activity.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
