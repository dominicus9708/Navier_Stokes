# DSD M17-112 — Global turnover assembly is block-diagonal in carriers with nonlocal pressure and kappa coupling

Date: 2026-09-05
Canonical ID: **M17-112**

Status: **INTERNAL GLOBAL TURNOVER ASSEMBLY GATE / M17-111 SHOWS THAT ACTIVE RANK-ONE (`J_xi=0`) AND RANK-TWO (`J_xi!=0`) MATERIAL LABELS DO NOT CONVERT INTO EACH OTHER ON A FINITE REGULAR CE-H INTERVAL. CONSEQUENTLY THEIR TURNOVER MEASURES CANNOT BE ADDED AS THOUGH ONE CARRIER CHARGE PAYS THE OTHER'S DEFICIT. THE CORRECT ASSEMBLY IS BLOCK-DIAGONAL AT THE CARRIER LEVEL. OFF-DIAGONAL COUPLING STILL EXISTS THROUGH ACTUAL PDE FIELDS: THE PRESSURE POISSON SOURCE `S_P=|Sigma|^2-rho^2/2` IS GLOBAL, SO THE RANK-ONE STF `l=3` PRESSURE LOCK RECEIVES SOURCE CONTRIBUTIONS FROM ALL SPATIAL STRATA; THE RANK-TWO MARGIN RECHARGE CONTAINS STRAIN AND `kappa` DERIVATIVES THAT ARE LIKEWISE NONLOCAL THROUGH THE VELOCITY/PRESSURE SYSTEM. THE GLOBAL SIGNED IDENTITY `int kappa rho^2=-int|grad W|^2` ALSO DECOMPOSES ADDITIVELY ACROSS STRATA BUT DOES NOT FIX THE SIGN OF EACH BLOCK. THUS THE CURRENT PROOF FRONTIER IS AN EXPLICIT TWO-BLOCK SYSTEM WITH NONLOCAL FIELD COUPLING, NOT A SINGLE CONSERVED-CHARGE CONTRADICTION. CLOSURE REQUIRES EITHER A RANK-ONE LOCAL-TO-GLOBAL PRESSURE COVARIANCE ESTIMATE OR A RANK-TWO UPPER/OPPOSITE-SIGN BOUND ON THE THREE-HALVES RECHARGE, PLUS THE FINAL EXHAUSTIVENESS ASSEMBLY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material carrier blocks

On the active domain `rho>0`, define

\[
\boxed{
\mathcal S_1:=\{J_\xi=0\},
\qquad
\mathcal S_2:=\{J_\xi\neq0\}.
}
\]

M17-111 gives material invariance of both strata on every finite regular CE-H interval.

Therefore the carrier measures remain structurally distinct:

### Rank-1 block

M5/Rank-1 uses base-label, lobe, and pressure descriptors such as

\[
d\mu_0,
\quad
h=D_B\kappa,
\quad
\chi,
\quad
\mathcal H_{333}.
\]

### Rank-2 block

The pure-kernel hard survivor uses

\[
d\Phi_J,
\quad
N_{R2}=|a|\mathcal M_{R2},
\quad
Z_\nu.
\]

There is no regular finite-time carrier map

\[
d\Phi_J\longleftrightarrow d\mu_0
\]

produced by Rank conversion.

---

## 2. Rank-1 recurrence ledger

For the vertical nonaxis branch, M17-095--096 give the local M5 crossing bias

\[
\boxed{
\overline{
\int
 a\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)\,d\mu_0
}>0.
}
\]

The same branch obeys the global axial STF pressure lock

\[
\boxed{
V_V
=-\frac12\mathcal H_{333}.
}
\]

The missing Rank-1 theorem remains a relation between this label-space crossing bias and the global spatial pressure architecture.

For slanted Rank-1, the same structural issue appears in the principal/oblique `l=3` locks and covariance firewalls.

---

## 3. Rank-2 recurrence ledger

For a spatially restricted clean transverse positive-margin population, M17-108 gives

\[
\boxed{
\frac d{d\theta}\mathscr N_\Omega
=-\frac32\mathscr N_\Omega
+\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
+\mathscr B_N.
}
\]

M17-109 identifies the generic tangency part of `B_N` as

\[
\boxed{
\mathscr B_F
=2\int
\varepsilon_FN_F
\delta(\theta-\tau_F)
\,d\Phi_J.
}
\]

Therefore a recurrent positive Rank-2 inventory must satisfy

\[
\boxed{
\left\langle
\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
+\mathscr B_N
\right\rangle
=
\frac32\left\langle\mathscr N_\Omega\right\rangle>0.
}
\]

The missing Rank-2 theorem is an upper/opposite-sign/coercive bound on the full recharge side.

---

## 4. Pressure is a true off-diagonal field coupling

Pressure satisfies

\[
\boxed{
-\Delta P
=S_P,
\qquad
S_P:=|\Sigma|^2-\frac12\rho^2.
}
\]

At a Rank-1 core centered at `Y`, the axial STF cubic moment has the Newtonian representation

\[
\boxed{
\mathcal H_{333}(Y)
=\int_{\mathbb R^3}
S_P(x)\,\mathcal K_{333}(Y-x)\,dx
}
\]

with the sign-changing kernel of M17-089.

Partition the spatial source by the material strata:

\[
S_P
=S_P\mathbf 1_{\mathcal S_1}
+S_P\mathbf 1_{\mathcal S_2}
+S_P\mathbf 1_{\mathcal S_0},
\]

where `S_0` denotes the remaining/nodal chart region when needed.
Then exactly

\[
\boxed{
\mathcal H_{333}
=
\mathcal H_{333}^{(1)}
+
\mathcal H_{333}^{(2)}
+
\mathcal H_{333}^{(0)}.
}
\]

Thus Rank-2 spatial structure may influence a Rank-1 pressure lock **without any Rank-2 carrier becoming Rank 1**.

This is genuine PDE coupling rather than charge transfer.

---

## 5. Consequence for the Rank-1 covariance firewall

The local Rank-1 crossing functional is supported on the Rank-1 label genealogy, whereas

\[
\mathcal H_{333}^{(2)}
\]

can be produced by Rank-2 spatial source architecture.

Therefore a putative inequality of the form

\[
\operatorname{sgn}(\mathcal C_V)
\Longrightarrow
\operatorname{sgn}(\mathcal H_{333})
\]

cannot be proved merely by tracking the Rank-1 local payer.

One must either

1. bound the off-stratum pressure contributions, or
2. prove a global covariance estimate including them.

This sharpens the vertical Rank-1 firewall.

---

## 6. Kappa energy identity is a second shared scalar coupling

Where

\[
\Delta W=\kappa W
\]

and the retained finite-energy/decay hypotheses justify integration by parts,

\[
\boxed{
\int_{\mathbb R^3}
\kappa\rho^2\,dx
=-\int_{\mathbb R^3}|\nabla W|^2\,dx
<0
}
\]

for a nonzero state.

Partition the active spatial domain:

\[
\boxed{
\int_{\mathcal S_1}\kappa\rho^2\,dx
+
\int_{\mathcal S_2}\kappa\rho^2\,dx
=-\int|\nabla W|^2\,dx.
}
\]

This is a legitimate common scalar ledger because both terms use the same spatial measure and the same global field `W`.

However it does not imply a sign for either stratum separately.

Thus one block can spatially carry more of the negative-kappa payer while the other supports positive recurrent phases, without material carrier conversion.

---

## 7. Rank-2 recharge is also globally field-coupled

M17-080's recharge contains terms such as

\[
D_\xi^2(\sigma+\kappa),
\qquad
D_nD_\xi(\sigma+\kappa),
\qquad
D_k(\sigma_n-\sigma),
\]

and strain/frame derivatives.

The strain field comes from the global velocity gradient and its evolution contains the pressure Hessian.
Therefore the Rank-2 recharge cannot in general be declared intrinsic to the local Rank-2 carrier population.

Rank-1 and Rank-0 spatial source architecture can influence it through the global PDE fields.

Again, this is off-diagonal **field coupling**, not carrier conversion.

---

## 8. Block form of the current recurrence problem

Schematically the remaining recurrent hard system has the form

\[
\boxed{
\begin{pmatrix}
\text{Rank-1 crossing / }l=3\text{ lock}\\
\text{Rank-2 positive-margin ledger}
\end{pmatrix}
=
\begin{pmatrix}
\mathcal L_{11}&\mathcal P_{12}\\
\mathcal P_{21}&\mathcal L_{22}
\end{pmatrix}
\begin{pmatrix}
\text{Rank-1 state}\\
\text{Rank-2 state}
\end{pmatrix}
+
\text{boundary/event terms}.
}
\]

Here

- `L_11`, `L_22` denote the within-stratum carrier ledgers;
- `P_12`, `P_21` denote nonlocal pressure/velocity/kappa field influence;
- no off-diagonal **carrier charge conversion** is present on a regular interval.

This is a structural diagram, not a new linearization of Navier--Stokes.

---

## 9. Why the two deficits cannot simply be added

The Rank-1 positive/negative crossing bias uses

\[
d\mu_0
\]

and related lobe/spatial measures.

The Rank-2 compensation uses

\[
d\Phi_J.
\]

There is no theorem identifying these measures.

Hence an expression such as

\[
\mathcal C_V
+\mathscr N_\Omega
\]

has no canonical conservation meaning.

A valid global contradiction must instead close **each branch of the disjunction**, while consistently retaining the shared PDE coupling.

---

## 10. Minimal missing closure statements

The assembly isolates three remaining theorem-level obligations.

### Rank-1 covariance closure

Derive a bound/sign/pushforward theorem connecting local Rank-1 crossing/hysteresis to the full global STF pressure architecture, including off-stratum pressure sources.

### Rank-2 recharge closure

Derive an estimate of the form

\[
\boxed{
\left\langle
\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
+\mathscr B_N
\right\rangle
<
\frac32\left\langle\mathscr N_\Omega\right\rangle
}
\]

or another incompatible sign/coercivity statement, under the retained recurrent hard hypotheses.

### Exhaustiveness closure

Verify that every hypothetical hard recurrent/blow-up survivor reaches one of the audited Rank-1 or Rank-2 blocks without an unaccounted regular chart/interface escape.

---

## 11. DSD analysis

The correct global architecture has two independent layers:

\[
\boxed{
\text{material carrier stratification}
}
\]

and

\[
\boxed{
\text{nonlocal PDE field coupling}.
}
\]

Mixing the two would create false charge-transfer arguments.
Keeping them separate exposes exactly where a true theorem is still missing.

---

## 12. DSD audit

### Audit A — summing Rank-1 and Rank-2 deficits into one conserved quantity
Rejected.

### Audit B — assuming material rank invariance means pressure decoupling
Rejected.

### Audit C — assigning the global negative-kappa identity to one stratum
Rejected without a sign theorem.

### Audit D — ignoring Rank-2 contributions to Rank-1 global pressure moments
Rejected.

### Audit E — treating the schematic block matrix as a literal linear PDE
Rejected. It is a ledger/descriptor architecture only.

### Audit F — proof status
The global turnover system is structurally assembled but both diagonal closure estimates remain open.

---

## 13. Updated global frontier

The proof tree is now

\[
\boxed{
B_{dir}
\Longrightarrow
R_1\lor R_2,
}
\]

with

\[
\boxed{
R_1
\to
\text{global }l=3\text{ covariance/pushforward gate},
}

and

\[
\boxed{
R_2
\to
\text{director-area-weighted }3/2\text{ recharge gate}.
}
\]

The two branches interact only through explicitly global PDE fields and spatial identities, not through material carrier conversion.

The next highest-value action is to seek a **coercive estimate** on one of these two remaining diagonal gates rather than creating further local genealogy descriptors.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
