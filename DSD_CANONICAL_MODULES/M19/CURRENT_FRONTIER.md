# M19 Current Frontier

**Date:** 2026-09-15  
**Current tip:** **M19-259**  
**Status:** ACTIVE CALCULATION / WHOLE-SPACE TRANSPARENT MOVING-SPHERE + GALILEAN WEIGHTED-PAYER FRONTIER / LOG-SCALE DENSITY + SPACETIME INCIDENCE + REPRESENTATION/ROOT GATES OPEN / APERIODIC SIGNED FRONTIER OPEN / FINAL ROOT-PROOF CERTIFICATION OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical policy

M18 remains the frozen audit/reduction family. M19 is the active calculation/closure family. Historical modules remain preserved; corrected later modules and this frontier determine the current canonical interpretation.

## 2. Global proof tree remains open

`ROOT-CERT` is unfinished. Historical non-CE-H roots

\[
CP\!-\!E,\quad CP\!-\!S,\quad CE\!-\!T,\quad Migration
\]

remain unresolved, together with parent-to-late-branch alignment/nonreuse and final beginning-to-end independent audit.

The aperiodic recurrent-hard target

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

also remains OPEN.

## 3. Historical no-slip cavity branch — M19-211--252

M19-211--252 remain valid auxiliary analyses under their stated cavity hypotheses. M19-253 permanently corrected the whole-space interpretation:

\[
\boxed{\text{no-slip cavity exclusion}\not\Rightarrow\text{whole-space transparent-sphere exclusion}.}
\]

Wall shear, \(\nu/R\) layers, wall impedance and no-slip determinant calculations are not direct Clay-(A) closure conditions.

## 4. M19-253 — transparent moving observation sphere and Galilean epsilon floor

The physical observation region is

\[
\Omega_R(t)=B_R(X(t))\subset\mathbb R^3,
\qquad S_R(t)=\partial B_R(X(t)),
\]

with no material wall condition. For \(e=|u|^2/2\),

\[
\frac d{dt}\int_{\Omega_R(t)}e
+\nu\int_{\Omega_R(t)}|\nabla u|^2
=
-\int_{S_R(t)}
\left[e(u-\dot X)\cdot n+p\,u\cdot n-\nu\partial_ne\right]dS.
\]

For the constant-velocity Galilean cylinder

\[
Q_r^V(z_0)=\{t_0-r^2<t<t_0,\ |x-x_0-V(t-t_0)|<r\},
\]

standard one-scale epsilon regularity plus Galilean covariance gives

\[
\boxed{
z_0\text{ singular}
\Longrightarrow
\forall V,\ \forall r\ll1,
\quad C_V(r)+D_V(r)\ge\varepsilon_*.
}
\]

## 5. M19-254 — logarithmically divergent critical payer

Finite-energy interpolation yields the usual \(u\in L^{10/3}_{x,t}\), \(p\in L^{5/3}_{x,t}\), but the unweighted scale costs remain summable.

With

\[
\rho_V(x,t)=\max(|x-x_0-V(t-t_0)|,\sqrt{t_0-t}),
\]

Tonelli converts the scale-invariant epsilon floor into the necessary singularity condition

\[
\boxed{
\mathcal P_{GMS}^{log}(V)
:=
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}{\rho_V^{5/3}}\,dxdt
=\infty
}
\]

for every fixed constant \(V\).

## 6. Corrected M19-255 — derivative threshold

If on the required physical neighborhood

\[
u\in L_t^\infty L_x^2,
\qquad D^m u\in L_t^2L_x^2,
\]

Gagliardo--Nirenberg with direct time integration gives

\[
\boxed{s=2+\frac{4m}{3}},
\qquad u\in L^s_{x,t}.
\]

At the raw-H2 level \(m=3\),

\[
\boxed{D^3u\in L^2_{x,t}\Longrightarrow u\in L^6_{x,t}.}
\]

The canonical pressure then satisfies

\[
\boxed{p\in L^3_{x,t}.}
\]

Since the parabolic dimension is five,

\[
\rho_V^{-5/3}\in L^q_{loc}\quad(q<3).
\]

Choosing \(q=9/4\) and \(q'=9/5\), one has

\[
|u-V|^{10/3},\ |p|^{5/3}\in L^{9/5},
\]

so Hölder gives

\[
\boxed{D^3u\in L^2\text{ physically}\Longrightarrow\mathcal P_{GMS}^{log}(V)<\infty.}
\]

Thus low-frequency and pressure are not independent analytic gates once the physical raw-H2 transfer is available.

## 7. M19-256 — exact ancestry scaling match

For

\[
\omega^{(r)}(y,s)=r^2\omega(x_0+ry,t_0+r^2s),
\]

one has exactly

\[
\boxed{
\int_{Q_r}|D_x^k\omega|^2dxdt
=
r^{1-2k}
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dyds.
}
\]

Therefore the M17 ancestry factors are exactly the physical parabolic derivative factors:

\[
k=1:r^{-1},\qquad k=2:r^{-3},\qquad k=3:r^{-5}.
\]

The relevant raw-H2 case is \(k=2\) on vorticity because \(D^2\omega\simeq D^3u\). Hence there is no exponent mismatch between the certified M17 \(r^{-3}\) ledger and the physical derivative level needed by M19-255.

For moving record centers \(X_m(t)\), define

\[
\Theta_m(V)=r_m^{-1}\sup_{t\in I_m}|X_m(t)-x_0-V(t-t_0)|.
\]

Failure of every fixed frame is the explicit exit

\[
\boxed{
\mathcal E_{track}:
\forall V,\quad\limsup_{m\to\infty}\Theta_m(V)=\infty.
}
\]

More generally, transfer failure is typed as

\[
\boxed{
\mathcal E_{track}
\lor\mathcal E_{domain}
\lor\mathcal E_{coverage}
\lor\mathcal E_{overlap}
\lor\mathcal E_{genealogy}
\lor\mathcal E_{interface}.
}
\]

## 8. M19-257 — explicit record-to-physical transfer contract

Let \(r_j=2^{-j}r_0\) be physical GMS scales and let \(\mathcal M(j)\) be the records assigned to physical shell \(j\). A sufficient algebraic transfer contract is:

\[
\Lambda^{-1}r_j\le R_m\le\Lambda r_j
\qquad(m\in\mathcal M(j)),
\]

physical shell cost domination by the assigned record costs, and uniformly bounded reuse

\[
\#\{j:m\in\mathcal M(j)\}\le N.
\]

Then the matching \(R^{-3}\) weight and bounded reuse convert the M17 record ledger into the required physical raw-H2 ledger. Thus exponent matching alone is not enough; scale-comparable coverage and reuse control are the actual combinatorial bridge.

M19-257 also separated the upstream root/genealogy eligibility gate from the analytic transfer itself.

## 9. M19-258 — whole-space field and pressure gates collapse

For an untruncated whole-space divergence-free record field,

\[
\widehat\omega=i\xi\times\widehat u,
\qquad \xi\cdot\widehat u=0,
\]

so

\[
\boxed{
\|\omega\|_{\dot H^2}^2
=\|u\|_{\dot H^3}^2,
\qquad
\|\Delta\omega\|_2^2
=\|(-\Delta)^{3/2}u\|_2^2.
}
\]

Therefore, if an assigned M17 record is the same untruncated whole-space rescaled field as the physical GMS record, no separate localized Biot--Savart derivative loss occurs. Once the physical H3 transfer is achieved, M19-255 and Calderón--Zygmund give

\[
u\in L^6_{x,t},
\qquad p\in L^3_{x,t},
\qquad \mathcal P_{GMS}^{log}(V)<\infty.
\]

If the M17 record variable is actually cutoff/truncated at the relevant step, the local field/interface gate reopens and the conservative M19-257 formulation applies.

## 10. M19-259 — dyadic scale comparability removes bounded reuse as an independent gate

Define

\[
a_m=-\log_2(R_m/r_0),
\qquad r_j=2^{-j}r_0.
\]

Then

\[
\Lambda^{-1}r_j\le R_m\le\Lambda r_j
\iff
|a_m-j|\le\log_2\Lambda.
\]

For a fixed record \(m\), the number of dyadic shell indices satisfying this is at most

\[
\boxed{N_\Lambda=2\lceil\log_2\Lambda\rceil+1.}
\]

Thus uniform scale comparability automatically supplies bounded shell-index reuse.

The actual radius-coverage condition is logarithmic relative density:

\[
\boxed{
\mathcal T_{GMS}^{scale-density}:
\forall j\gg1\quad\exists m:\ |a_m-j|\le L.
}
\]

For an ordered cofinal record sequence, a sufficient form is

\[
\boxed{
\sup_m\log_2\frac{R_m}{R_{m+1}}<\infty.
}
\]

Cofinality \(R_m\to0\) and record-window bounded overlap do not imply this. The abstract sequence \(R_m=2^{-2^m}r_0\) is a counterexample. This does not assert that the actual M17 records are sparse; it identifies what must be checked.

Scale density still does not give space-time/center coverage. Therefore

\[
\boxed{
\mathcal T_{GMS}^{cover}
=
\mathcal T_{GMS}^{scale-density}
+\mathcal T_{GMS}^{incidence}.
}
\]

## 11. Updated conditional closure

Under the same-field whole-space representation, the current entered-branch transfer complex is

\[
\boxed{
\mathcal T_{GMS}^{scale-density}
+\mathcal T_{GMS}^{incidence}
+\mathcal T_{GMS}^{repr}
+\mathcal T_{GMS}^{root}.
}
\]

If these hold, the M17 \(R^{-3}\) raw-H2 ledger transfers to the physical GMS neighborhood, M19-255/258 give \(\mathcal P_{GMS}^{log}(V)<\infty\), and M19-254 gives a contradiction.

This is conditional branch closure, not global regularity.

## 12. Permanent firewalls through M19-259

\[
\boxed{\text{unweighted finite integrability}\not\Rightarrow\text{finite critical GMS payer}},
\]
\[
\boxed{\text{exact scaling-exponent match}\not\Rightarrow\text{domain/scale coverage}},
\]
\[
\boxed{\text{record scales cofinal at }0\not\Rightarrow\text{bounded logarithmic scale gaps}},
\]
\[
\boxed{\text{bounded record-window overlap}\not\Rightarrow\text{log-scale density}},
\]
\[
\boxed{\text{log-scale density}\not\Rightarrow\text{space-time incidence}},
\]
\[
\boxed{\text{global Fourier velocity-vorticity identity}\not\Rightarrow\text{record-to-physical representation coherence}},
\]
\[
\boxed{\text{conditional GMS branch closure}\not\Rightarrow\text{ROOT-CERT or non-CE-H closure}}.
\]

## 13. Immediate next target

Audit the actual M17 record-selection/first-hitting rule for a bounded logarithmic scale-gap theorem or equivalent relative-density statement.

If scale density is certified, the next gate is

\[
\boxed{\mathcal T_{GMS}^{incidence}}
\]

— whether the comparable-scale record windows cover the actual candidate singular point's physical parabolic shells in one fixed Galilean frame.

If no scale-density theorem exists, retain the explicit survivor

\[
\boxed{\mathcal E_{scale-gap}}
\]

unless another record-selection mechanism fills the skipped scales.

Global regularity remains unproved.
