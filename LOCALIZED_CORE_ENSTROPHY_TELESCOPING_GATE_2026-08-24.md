# Localized-Core Enstrophy Telescoping Gate — 2026-08-24

Status: **LOCAL S-LEVEL ENSTROPHY CLOSURE THAT DOES NOT REQUIRE GLOBAL VORTICITY TIGHTNESS / GLOBAL REGULARITY NOT PROVED.**

This note is the direct anti-proof continuation of `FINITE_STAGE_TIGHT_ENSTROPHY_TELESCOPING_CLOSURE_2026-08-24.md`.

The global tightness closure is strong, but the audit correctly identified a possible escape: normalized enstrophy may spread to arbitrarily remote radii while the dangerous core remains local. It is therefore unsafe to assume a universal global tightness radius `R_Z`.

The present calculation localizes the same enstrophy mechanism to one tracked core packet. Remote passive enstrophy is allowed to exist. The only quantities that must stay quiet are the **local transition annulus**, the **localized strain-vorticity boundary defect**, and the **material/diffusive cutoff flux**.

---

## 1. Dynamically normalized vorticity equation

Use the running first-hitting normalization

\[
M(t)=\|\omega(t)\|_\infty
\]

on record-growth portions, with

\[
\frac{ds}{dt}=M(t),
\qquad
b(s)=\frac d{ds}\log M\ge0.
\]

In normalized coordinates the vorticity equation is

\[
\boxed{
\Omega_s
+V\cdot\nabla\Omega
+b\Omega
=\Sigma\Omega+
u\Delta\Omega,
}
\]

where

\[
V=U+\frac b2y,
\qquad
\nabla\cdot U=0,
\qquad
\nabla\cdot V=\frac{3b}{2}.
\]

The first-hitting cap gives

\[
\|\Omega\|_\infty\le1.
\]

Over one geometric stage,

\[
\boxed{
\int_{I_j}b(s)ds=\log q.
}
\]

---

## 2. One moving local-core cutoff

Let `a(s)` be a coherent normalized center. Choose a fixed-shape radial cutoff

\[
\psi_a(y,s)
=\Psi\!\left(\frac{y-a(s)}R\right),
\]

with

\[
0\le\psi\le1,
\qquad
\psi=1\text{ on }B_R(a),
\qquad
\psi=0\text{ outside }B_{LR}(a),
\]

where `L>1` is a free cutoff factor.

Set

\[
\boxed{\phi:=\psi^2.}
\]

This choice is important: the same cutoff simultaneously enters the exact local-enstrophy identity and the Dirichlet frequency estimate.

Choose the center speed `a_s` so that the transport velocity is measured relative to the coherent local frame. For example, one may use the weighted mean of `V` on the cutoff support. Only the relative velocity

\[
V-a_s
\]

appears below.

Define

\[
Z_\phi
:=\int\phi|\Omega|^2dy,
\qquad
Q_\phi
:=\int\phi|\nabla\Omega|^2dy,
\]

and

\[
P_\phi
:=\int\phi\,\Omega^T\Sigma\Omega\,dy.
\]

---

## 3. Exact moving local-enstrophy identity in the dynamic scaling

Let

\[
e=\frac12|\Omega|^2.
\]

From the normalized vorticity equation,

\[
e_s+V\cdot\nabla e+2be
=\Omega^T\Sigma\Omega+
u\Delta e-
u|\nabla\Omega|^2.
\]

Since

\[
\nabla\cdot V=\frac{3b}{2}
\]

and

\[
\phi_s=-a_s\cdot\nabla\phi,
\]

integration by parts gives

\[
\boxed{
\frac12Z_\phi'
+\frac b4Z_\phi
+\nu Q_\phi
=P_\phi+F_\phi,
}
\]

where the complete local boundary/material term is

\[
\boxed{
F_\phi
:=
\int e\,(V-a_s)\cdot\nabla\phi\,dy
+\nu\int e\,\Delta\phi\,dy.
}
\]

Thus the scale-growth term `b Z_phi/4` survives localization exactly. Absolute translational drift is absent when the center is followed coherently.

---

## 4. Local strain-vorticity identity and its boundary defect

Let

\[
A=\nabla U,
\qquad
\Sigma=\frac12(A+A^T).
\]

For divergence-free `U`,

\[
\operatorname{tr}(A^2)
=|\Sigma|^2-\frac12|\Omega|^2
=\partial_iU_j\,\partial_jU_i.
\]

Moreover

\[
\partial_iU_j\,\partial_jU_i
=\partial_i(U_j\partial_jU_i).
\]

Therefore, for any constant vector `c`,

\[
\boxed{
\int\phi|\Sigma|^2
=\frac12Z_\phi+B_\phi,
}
\]

with the translation-invariant boundary defect

\[
\boxed{
B_\phi
:=-\int(\partial_i\phi)
(U_j-c_j)\partial_jU_i\,dy.
}
\]

The subtraction of `c` is legitimate because the corresponding constant term integrates to zero by incompressibility.

A direct buffer estimate is

\[
\boxed{
|B_\phi|
\lesssim
\|\nabla\phi\|_\infty
\|U-c\|_{L^2(A_{tr})}
\|\nabla U\|_{L^2(A_{tr})},
}
\]

where `A_tr` is the cutoff transition annulus.

Thus a large `B_phi` is a concrete relative-velocity/strain buffer defect, not a hidden global term.

---

## 5. Local trace-free production coefficient

Assume the quiet localized-strain boundary condition

\[
\boxed{
|B_\phi|
\le\beta_S Z_\phi
}
\]

with fixed `beta_S>=0`.

Then

\[
\int\phi|\Sigma|^2
\le
\left(\frac12+\beta_S\right)Z_\phi.
\]

For every symmetric trace-free strain matrix,

\[
\lambda_{max}(\Sigma)
\le\sqrt{\frac23}|\Sigma|.
\]

Since `||Omega||_infinity<=1`,

\[
\begin{aligned}
P_\phi
&\le
\sqrt{\frac23}
\int\phi|\Sigma||\Omega|^2\\
&\le
\sqrt{\frac23}
\left(\int\phi|\Sigma|^2\right)^{1/2}
Z_\phi^{1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
P_\phi
\le
C_{prod}(\beta_S)Z_\phi,
}
\]

where

\[
\boxed{
C_{prod}(\beta_S)
:=
\sqrt{\frac{1+2\beta_S}{3}}.
}
\]

At zero boundary defect this recovers the global sharp coefficient

\[
C_{prod}(0)=1/\sqrt3.
\]

---

## 6. Local Dirichlet frequency floor from only the transition annulus

Because `phi=psi^2`,

\[
Z_\phi=\|\psi\Omega\|_2^2.
\]

Let the transition-annulus vorticity mass satisfy

\[
\boxed{
Z_{tr}
:=
\int_{\operatorname{supp}\nabla\psi}|\Omega|^2dy
\le
\varepsilon_b Z_\phi.
}
\]

This is **local buffer quietness**, not global vorticity tightness. Vorticity arbitrarily far outside `B_{LR}` is unrestricted.

Choose

\[
|\nabla\psi|
\le\frac1{(L-1)R}.
\]

Since `psi Omega in H_0^1(B_{LR})`, the first Dirichlet eigenvalue of the three-dimensional ball gives

\[
Z_\phi
\le
\frac{L^2R^2}{\pi^2}
\|\nabla(\psi\Omega)\|_2^2.
\]

For every `eta>0`,

\[
\|\nabla(\psi\Omega)\|_2^2
\le
(1+\eta)Q_\phi
+
(1+\eta^{-1})
\frac{\varepsilon_b Z_\phi}{(L-1)^2R^2}.
\]

Thus

\[
\frac{Q_\phi}{Z_\phi}
\ge
\frac1{R^2}
\frac{
\pi^2L^{-2}
-(1+\eta^{-1})\varepsilon_b(L-1)^{-2}
}{1+\eta}.
\]

Optimize first in `eta` and then in `L`. Exactly as in the global-tightness calculation, but now without the factor `(1-epsilon)`, the result is

\[
\boxed{
\frac{Q_\phi}{Z_\phi}
\ge
\lambda_{loc}
:=
\frac{\Lambda_{loc}(\varepsilon_b)}{R^2},
}
\]

where

\[
\boxed{
\Lambda_{loc}(\varepsilon_b)
=
\left(
\sqrt\pi-\varepsilon_b^{1/4}
\right)^4.
}
\]

Useful benchmarks are

\[
\boxed{
\Lambda_{loc}(1/4)
\approx1.2881441415,
}
\]

\[
\boxed{
\Lambda_{loc}(1/2)
\approx0.7530755486,
}
\]

and even

\[
\boxed{
\Lambda_{loc}(1)
\approx0.3560329317.
}
\]

Thus the local frequency floor can remain positive even when the transition annulus carries vorticity mass comparable with the weighted core packet.

---

## 7. Quiet boundary-flux parameterization

The exact cutoff flux need only be controlled from above. Assume

\[
\boxed{
F_\phi
\le
f_bZ_\phi
+\eta_b\nu Q_\phi,
\qquad
0\le\eta_b<1.
}
\]

Here

- `f_b` measures normalized material/dilation/diffusive boundary injection proportional to the packet mass;
- `eta_b` measures the fraction of interior viscous dissipation that can be cancelled by boundary transfer.

Failure of this inequality is an explicit local material/diffusive turnover event; it is not discarded as an error.

Insert the production and frequency estimates into the exact identity. Wherever `Z_phi>0`,

\[
\boxed{
\frac12(\log Z_\phi)'
+\frac b4
+(1-\eta_b)\nu\lambda_{loc}
\le
C_{prod}(\beta_S)+f_b.
}
\]

Define the effective local growth ceiling

\[
\boxed{
C_{loc}^{eff}
:=
C_{prod}(\beta_S)+f_b
-(1-\eta_b)\nu
\frac{\Lambda_{loc}(\varepsilon_b)}{R^2}.
}
\]

Then

\[
\boxed{
\frac12(\log Z_\phi)'
+\frac b4
\le
C_{loc}^{eff}.
}
\]

---

## 8. One-stage and multistage telescope

Integrating one geometric first-hitting stage gives

\[
\boxed{
\frac12\log\frac{Z_{\phi,1}}{Z_{\phi,0}}
+\frac14\log q
\le
C_{loc}^{eff}L_j.
}
\]

To telescope many stages, use the retained local packet chain supplied by `RELATIVE_MEAN_PATH_LOCAL_ENSTROPHY_TRACKING_2026-08-24.md`.

On the pure retained-packet corridor assume fixed endpoint bounds

\[
\boxed{
0<z_-\le Z_{\phi,j}\le z_+<\infty.
}
\]

The lower bound comes from terminal Taylor/analytic core mass propagated through the quiet packet-retention lane. The upper bound follows from `||Omega||_infinity<=1` and the fixed normalized support volume.

Summing `N` consecutive stages,

\[
\frac12\log\frac{Z_{\phi,N}}{Z_{\phi,0}}
+\frac N4\log q
\le
C_{loc}^{eff}\sum_{j=0}^{N-1}L_j.
\]

If

\[
L_j\le L_{stage,+},
\]

then any infinite quiet retained-packet corridor must satisfy

\[
\boxed{
\frac14\log q
\le
C_{loc}^{eff}L_{stage,+}.
}
\]

Therefore the local corridor is S-closed whenever

\[
\boxed{
\left[
C_{prod}(\beta_S)+f_b
-(1-\eta_b)\nu
\frac{\Lambda_{loc}(\varepsilon_b)}{R^2}
\right]_+
L_{stage,+}
<
\frac14\log q.
}
\]

This is the main localized finite-stage certificate.

---

## 9. Timing-independent local closure

If the effective coefficient is nonpositive,

\[
\boxed{
(1-\eta_b)\nu
\frac{\Lambda_{loc}(\varepsilon_b)}{R^2}
\ge
C_{prod}(\beta_S)+f_b,
}
\]

then no infinite retained local packet corridor is possible, independent of the stage-length ceiling.

In the ideal quiet benchmark

\[
\beta_S=f_b=\eta_b=0,
\qquad
\varepsilon_b=\frac14,
\qquad
\nu=1,
\]

this becomes

\[
\frac{1.2881441415}{R^2}
\ge
\frac1{\sqrt3},
\]

or

\[
\boxed{
R\lesssim1.49369712.
}
\]

This benchmark is substantially larger than the corresponding global-quarter-tail timing-independent radius `1.1687`, because only the local transition annulus is charged rather than the entire global tail.

The benchmark does **not** by itself prove that `beta_S,f_b,eta_b` vanish; it only shows the strength available on the fully quiet local lane.

---

## 10. Exact failure branches

The local theorem does not classify every failure as `T` by definition. Its complement is explicitly

\[
\boxed{
\begin{aligned}
\text{local telescope fails quietly only if at least one of:}
\qquad&\\
\text{A. }Z_{tr}>\varepsilon_bZ_\phi
&\quad\text{(annular/multicore vorticity packet)},\\
\text{B. }|B_\phi|>\beta_SZ_\phi
&\quad\text{(strain-vorticity boundary defect)},\\
\text{C. }F_\phi>f_bZ_\phi+\eta_b\nu Q_\phi
&\quad\text{(material/diffusive boundary injection)},\\
\text{D. packet endpoint retention fails}
&\quad\text{(local rebuild/loss action)},\\
\text{E. }L_j>L_{stage,+}
&\quad\text{(long-stage/rate escape)}.
\end{aligned}
}
\]

The repository already has direct ledgers for B, C, and D in terms of relative Campanato, buffer gradient energy, material crossing, viscous leakage, or local derivative action.

Branch A is deliberately left as an **annular vorticity-mass escape**, not silently renamed turnover. This is the main anti-proof survivor after localization.

---

## 11. Global significance

The previous corrected global split was

\[
\text{stage-wide global vorticity tightness}
\lor
\text{global vorticity non-tightness}.
\]

The present calculation shows that global non-tightness is not automatically fatal to the main proof. A candidate with remote passive enstrophy can still be closed if one local tracked packet has

- a quiet transition annulus;
- a small localized strain-vorticity boundary defect;
- quiet material/diffusive cutoff flux;
- and retained endpoint mass.

Thus the new split is narrower:

\[
\boxed{
\text{singular survivor}
\Longrightarrow
\text{localized quiet-core certificate fails}
\quad\lor\quad
\text{one of the explicit A--E exits above}.
}
\]

Among those exits, A — repeated annular vorticity mass comparable with the core — is now the cleanest genuinely unresolved spatial branch.

Status: **THE TRACE-FREE ENSTROPHY TELESCOPE HAS BEEN LOCALIZED TO A MOVING CORE PACKET. GLOBAL VORTICITY TIGHTNESS AND THE REMOTE VELOCITY TAIL ARE NO LONGER REQUIRED ON THIS ROUTE. THE REMAINING NEW SPATIAL ESCAPE IS REPEATED COMPARABLE VORTICITY MASS IN THE CUTOFF TRANSITION ANNULUS; ALL OTHER FAILURES ARE ALREADY TYPED BY EXISTING LOCAL BUFFER/TRANSPORT/DERIVATIVE LEDGERS. GLOBAL REGULARITY REMAINS UNPROVED.**