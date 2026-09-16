# DSD M19-348 — Sparse sign flux with high line residence has a sharp Markov-saturating scaling witness compatible with the diffuse baseline

Date: 2026-09-16  
Canonical ID: **M19-348**

Status: **ACTIVE SHARP SCALING WITNESS / SPARSE-RESIDENCE FEASIBILITY / SNAPSHOT NO-GO**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-344--347

On the retained compact mixed-sign CE-H good-time branch,

\[
K_+
=\Phi_+\bar L_+\bar\kappa_{+,L},
\qquad
K_-
=\Phi_-\bar L_-\bar\kappa_{-,L}.
\]

M19-345 shows that compact coefficient bounds, bounded enstrophy, and nontrivial sign moments imply

\[
0<c_\kappa
\le
\bar\kappa_{\pm,L}
\le
C_\kappa<\infty.
\]

Therefore sign-flux thinning is paid by line-residence growth.

M19-343 imports the parent-length diffuse baseline

\[
\ell_R\sim R,
\qquad
\mathfrak A_R\sim R,
\qquad
\rho_{flux}\sim R^{-1},
\qquad
\Phi\sim1,
\]

at the level of scaling audit.

The present module asks whether sparse sign flux plus high residence is already impossible from these snapshot constraints.

## 2. One-parameter sparse-residence ansatz

Fix

\[
0\le p\le1.
\]

Consider a sign-positive subpopulation with flux fraction

\[
\boxed{\eta_+(R)\sim R^{-p}.}
\]

To retain an order-one sign enstrophy mass and sign moment, take

\[
\boxed{\bar L_+(R)\sim R^p,}
\]

and

\[
\boxed{\bar\kappa_{+,L}\sim1.}
\]

Then

\[
E_+
=\Phi\eta_+\bar L_+
\sim1,
\]

and

\[
K_+
=E_+\bar\kappa_{+,L}
\sim1.
\]

Thus M17-458 near-perfect sign cancellation can remain compatible with a vanishing plus-sign material-flux fraction.

## 3. Realization on a parent-length line

Suppose the sign-positive lines have the baseline parent-length scale

\[
\ell_+\sim R.
\]

Choose their flux-weighted arclength amplitude scale as

\[
\boxed{\rho_+(R)\sim R^{p-1}.}
\]

Then

\[
L_+
\sim
\rho_+\ell_+
\sim
R^{p-1}R
=R^p,
\]

exactly as required.

For \(0\le p\le1\), this amplitude never exceeds an order-one normalized amplitude ceiling.

The endpoint cases are informative:

- \(p=0\): order-one sign flux with the ordinary diffuse amplitude \(R^{-1}\);
- \(p=1\): flux fraction \(R^{-1}\) carried at order-one amplitude along a parent-length arc.

The whole interval interpolates continuously between them.

## 4. Cross-sectional area required by the sign flux

At a representative section, the positive sign flux scales as

\[
\Phi_+
\sim
\eta_+\Phi
\sim
R^{-p}.
\]

If its typical amplitude is \(\rho_+\sim R^{p-1}\), the required transverse area is

\[
\boxed{
\mathfrak A_+
\sim
\frac{\Phi_+}{\rho_+}
\sim
R^{1-2p}.
}
\]

This may become sub-own-scale in area for \(p>1/2\), but area alone does not produce a contradiction because coefficient-sign support need not be an amplitude support with a Dirichlet boundary. Any attempt to turn this small area into a gradient cost requires an additional interface, Poincare, Morrey, or amplitude-connectivity theorem.

That firewall is exactly the lesson of M17-446--447.

## 5. Diffuse quadratic currency is exactly preserved

The sign-positive contribution to the flux-weighted normalized amplitude is

\[
\eta_+\rho_+
\sim
R^{-p}R^{p-1}
=R^{-1}.
\]

Therefore

\[
\boxed{
\eta_+\mathfrak a_+
\sim R^{-1}
}
\]

independently of \(p\).

If the negative population contributes at the same or smaller order, then the total satisfies

\[
\boxed{
\mathfrak a_{\Phi,R}
\sim R^{-1},
}
\]

which is exactly the M17-450--452 diffuse baseline.

Hence sign-flux thinning can be completely hidden inside a compensating increase in sign-specific residence/amplitude while leaving the total canonical amplitude scaling unchanged.

## 6. Markov saturation

M17-452 gives a flux-arclength probability \(\mu_R\) with

\[
\mathbb E_{\mu_R}[\rho]
\lesssim R^{-1}.
\]

The present witness places probability mass

\[
\sim R^{-p}
\]

at amplitude scale

\[
\sim R^{p-1}.
\]

Their product is

\[
R^{-p}R^{p-1}=R^{-1}.
\]

Thus the family exactly saturates the first-moment/Markov scaling.

Equivalently, if one tests the threshold

\[
a_R:=R^{p-1},
\]

Markov permits probability of order

\[
\frac{R^{-1}}{a_R}
=R^{-p},
\]

which is exactly the sparse sign fraction of the witness.

Therefore

\[
\boxed{
\text{M17-452 first-moment control alone cannot exclude the sparse-residence branch.}
}
\]

## 7. Compatibility with snapshot derivative ledgers

On exact CE-H with compact coefficient magnitude \(|\kappa|\sim1\),

\[
|\Delta\Omega|^2
=\kappa^2|\Omega|^2.
\]

Since the sign-positive enstrophy mass remains order one,

\[
H_{raw,+}^{snap}\sim1.
\]

This is compatible with the M19-319 / M17-453 critical raw-H2 snapshot scale and does not create any additional ancestry gain.

Likewise the existence of a small coefficient-sign cross-sectional area does not by itself force order-one additional palinstrophy because the sign boundary is a \(\kappa\)-interface, not a zero boundary for \(\Omega\). Low-amplitude transition corridors can hide coefficient gradients unless an amplitude-connected coercivity theorem is supplied.

Thus no currently certified snapshot resource rules out the witness.

## 8. What the witness does and does not mean

This construction is a **scaling witness**, not an exact Navier--Stokes or CE-H solution.

It proves only the following no-go statement:

\[
\boxed{
\text{near-perfect sign cancellation}
+
\text{bounded enstrophy/coefficient}
+
\text{diffuse first-moment amplitude control}
\not\Rightarrow
\text{sign-flux non-thinning}.
}
\]

Any genuine rigidity theorem must use information absent from this snapshot algebra, such as

1. a superlinear moment bound on line residence;
2. a geometric upper bound on sign-specific line length;
3. amplitude-connected interface coercivity;
4. temporal zero-crossing/current constraints;
5. genealogy/nonreuse constraints;
6. terminal dilation-hull structure.

## 9. Sharp residence tail interpretation

The witness has

\[
\eta_+\sim R^{-p},
\qquad
\bar L_+\sim R^p,
\]

so

\[
\boxed{
\eta_+\bar L_+\sim1.
}
\]

This is the exact critical product needed to keep an order-one enstrophy/sign moment inside a vanishing flux population.

It suggests that the correct next object is not the mean residence itself but the **integrability class of the residence distribution**. A finite first moment is critical and permits the witness; any uniform superlinear moment may forbid it.

## 10. Audit verdict

**PASS AS A SHARP NO-GO WITNESS.**

The sparse-residence branch is genuinely compatible with all currently used snapshot first-moment constraints. For every \(0\le p\le1\), the scaling

\[
\boxed{
\eta_+\sim R^{-p},
\quad
\bar L_+\sim R^p,
\quad
\rho_+\sim R^{p-1}
}
\]

keeps the sign enstrophy/moment order one while exactly saturating the canonical \(R^{-1}\) diffuse amplitude budget.

The next target is therefore a line-residence integrability theorem: determine whether the CE-H/Navier--Stokes structure supplies any uniform \(L^{1+\varepsilon}\) control of \(L_1\), or an equivalent geometric/time derivative estimate. Such a gain would eliminate sign-flux thinning immediately.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
