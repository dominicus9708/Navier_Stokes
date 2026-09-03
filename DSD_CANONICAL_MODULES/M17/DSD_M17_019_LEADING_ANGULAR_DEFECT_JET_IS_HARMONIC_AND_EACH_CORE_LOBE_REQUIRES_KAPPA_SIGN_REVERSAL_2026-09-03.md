# DSD M17-019 — The leading angular-defect jet is harmonic and every core-emergent lobe requires kappa sign reversal

Date: 2026-09-03
Canonical ID: **M17-019**

Status: **INTERNAL LOBE-RESOLVED PAYER GATE / BECAUSE `chi` VANISHES ON THE VERTICAL FILAMENT AND SATISFIES `Delta chi = kappa chi`, ITS FIRST NONZERO TRANSVERSE HOMOGENEOUS JET `P_m` MUST SATISFY `Delta_h P_m = 0`. HENCE `P_m = r^m(A cos mtheta + B sin mtheta)` AND HAS `2m` SIMPLE ANGULAR NODAL RAYS WITH ALTERNATING DEFECT SECTORS. ON THE POSITIVE-KAPPA CORE PHASES OF M17-012, EACH LOCAL DEFECT SECTOR ENTERS A GLOBAL CHI NODAL DOMAIN THROUGH A REGION WITH `kappa>0`; THE M17-018 NODAL-DOMAIN ENERGY IDENTITY FORCES THAT SAME GLOBAL DEFECT DOMAIN TO CONTAIN `kappa<0`, SO A CONTINUOUS PATH INSIDE THE LOBE CROSSES `kappa=0`. THE NUMBER `2m` COUNTS LOCAL SECTOR ENTRANCES, NOT NECESSARILY DISTINCT GLOBAL PAYER COMPONENTS BECAUSE SAME-SIGN SECTORS MAY RECONNECT AWAY FROM THE CORE. NON-AXISYMMETRY IS THEREFORE ATTACHED TO A LOBE-RESOLVED POSITIVE-TO-NEGATIVE KAPPA TRANSITION NETWORK / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Transverse Taylor order of the angular defect

Center a vertical regular filament on

\[
x_h=(x_1,x_2)=0.
\]

Because the rotation generator vanishes on the axis,

\[
\chi(0,x_3,\theta)=0
\]

for every axial point and time.

Fix a filament point and let `m` be the first nonzero transverse Taylor order:

\[
\boxed{
\chi(x_h,x_3)
=P_m(x_h;x_3)+O(r^{m+1}),
\qquad r=|x_h|,
}
\]

where `P_m` is a nonzero homogeneous polynomial of horizontal degree `m`.

For a non-scalar nodal Hessian, M17-017 gives

\[
m=2.
\]

For a conformal positive core separated from the axisymmetric firewall, M17-016 gives a finite order

\[
m=m_A\ge3.
\]

---

## 2. The leading transverse jet must be harmonic

The exact defect equation is

\[
\Delta\chi=\kappa\chi.
\]

The right-hand side begins at transverse order `m` because `kappa` is smooth at the regular filament.

On the left,

\[
\Delta\chi
=\Delta_hP_m
+\partial_3^2P_m
+\text{higher transverse orders}.
\]

The term

\[
\Delta_hP_m
\]

has transverse degree `m-2`, while `partial_3^2 P_m` retains degree `m`.
There is no degree `m-2` term on the right-hand side.
Therefore

\[
\boxed{
\Delta_hP_m=0.
}
\]

Thus the first nonzero transverse angular-defect jet is a two-dimensional homogeneous harmonic polynomial.

---

## 3. Canonical angular multipole form

Every nonzero real homogeneous harmonic polynomial of degree `m` in two variables has the form

\[
\boxed{
P_m(r,\vartheta)
=r^m\left(A\cos m\vartheta+B\sin m\vartheta\right).
}
\]

After an angular phase shift,

\[
\boxed{
P_m
=C_m r^m\cos(m(\vartheta-\vartheta_0)),
\qquad C_m\ne0.
}
\]

Hence its local nodal set consists of exactly

\[
\boxed{2m}
\]

simple angular rays through the filament, separating `2m` sectors with alternating signs of `chi`.

For the first-order nonconformal classes,

\[
m=2,
\]

so the leading non-axisymmetric core has four alternating angular sectors.

For the conformal/high-jet survivor,

\[
m\ge3,
\]

so there are at least six local sectors.

---

## 4. Persistence of the local sector pattern

Because the zeros of

\[
\cos(m(\vartheta-\vartheta_0))
\]

are simple in angle, the analytic remainder

\[
O(r^{m+1})
\]

does not erase the sector pattern at sufficiently small positive radius.

Thus each leading sector contains a smaller open wedge in which

\[
\boxed{
\operatorname{sgn}\chi
=\operatorname{sgn}P_m
}
\]

and `chi != 0`.

Each such local wedge belongs to some connected global nodal domain

\[
\Omega_j\subset\{\chi\ne0\}.
\]

Different local wedges may later reconnect into the same global nodal domain; therefore local sector count and global component count must be kept distinct.

---

## 5. Insert the positive-kappa core tube

M17-012 gives a positive-density set of recurrent nodal phases for which a fixed tube around the regular filament satisfies

\[
\boxed{
\kappa\ge\kappa_*>0.
}
\]

Choose the local angular wedges inside this tube.
Then every core-emergent defect sector contains points with

\[
\boxed{
\chi\ne0,
\qquad
\kappa>0.
}
\]

Therefore the corresponding global defect nodal domain `Omega_j` has strictly positive defect-weighted kappa content in a neighborhood of the core.

---

## 6. The same defect lobe must contain negative kappa

M17-018 gives on every nontrivial global `chi` nodal domain

\[
\boxed{
\int_{\Omega_j}\kappa\chi^2
=-\int_{\Omega_j}|\nabla\chi|^2<0.
}
\]

But `Omega_j` already contains a positive-kappa core portion.
Therefore it cannot have

\[
\kappa\ge0
\]

everywhere.
There must exist a point in the same global defect domain with

\[
\boxed{
\kappa<0.
}
\]

Hence every global defect domain that emerges from a positive core sector contains both signs of `kappa`.

---

## 7. Same-lobe zero crossing

A nodal domain `Omega_j` is connected.
Choose

\[
x_+\in\Omega_j,
\qquad
\kappa(x_+)>0,
\]

near the core, and

\[
x_-\in\Omega_j,
\qquad
\kappa(x_-)<0.
\]

There exists a continuous path

\[
\gamma_j\subset\Omega_j
\]

joining them.
By continuity of `kappa`, some point on the path satisfies

\[
\boxed{
\kappa=0.
}
\]

Thus

\[
\boxed{
\text{positive core}\n\xrightarrow[\text{inside same chi lobe}]{}\n\kappa=0\n\xrightarrow{}\n\text{negative defect payer}.
}
\]

The zero crossing is not merely somewhere in the bulk; it lies on a connected non-axisymmetric defect channel issuing from the winding core.

---

## 8. What the factor 2m does and does not count

The leading jet provides `2m` alternating **local sector entrances** at the filament.

It is safe to conclude:

\[
\boxed{
\text{every local sector belongs to a defect domain that requires a negative-kappa payer.}
}
\]

It is **not** yet safe to conclude that there are `2m` distinct global payer components or `2m` distinct connected `kappa=0` sheets.
Same-sign sectors may reconnect away from the core, and one zero-level component may intersect several defect lobes.

This distinction is part of the DSD audit.

---

## 9. Quantitative compact-hull upgrade

On a compact branch uniformly separated from the axisymmetric firewall, M17-016 supplies

1. a finite upper bound on the first nonzero angular order;
2. a nonzero jet floor.

Combined with uniform higher-derivative bounds, this gives a fixed small radius on which the leading harmonic sector pattern has a uniform amplitude floor.

Consequently the positive core portion of at least one defect lobe has a nonzero lower bound on its local Dirichlet energy.
Through

\[
D_{-,\Omega}
=D_{+,\Omega}
+\int_\Omega|\nabla\chi|^2,
\]

the corresponding negative defect payer cannot vanish continuously while the branch remains uniformly separated from the firewall.

A fully explicit universal constant is not fixed here because it depends on the retained compact-hull derivative bounds and angular-jet normalization.

---

## 10. DSD interpretation

### 10.1 Finite structural channel count
The non-axisymmetric core does not radiate arbitrary angular complexity at leading order.
Its first visible descriptor is a finite harmonic multipole `m`.

### 10.2 Same-channel payer coupling
Positive winding-core amplification and negative `kappa` compensation are connected inside the same non-axisymmetric defect domain.
This is stronger than a global sign budget.

### 10.3 Descriptor hierarchy
The chain is now

\[
\boxed{
\text{nodal core}
\to
\text{finite angular jet }P_m
\to
\text{chi lobe}
\to
\kappa=0
\to
\text{negative defect payer}.
}
\]

---

## 11. DSD audit

### Audit A — arbitrary leading angular geometry
Closed.
The first nonzero transverse jet is harmonic and has the fixed multipole form.

### Audit B — claiming 2m distinct global payer components
Rejected.
`2m` is a local sector count only.

### Audit C — payer in a different defect lobe
Closed at the global nodal-domain level.
Each nodal domain separately has negative weighted `kappa` mean.

### Audit D — automatic regularity of the kappa=0 crossing
Not claimed.
The crossing may occur at a regular zero level or a critical/singular zero-level point.

### Audit E — proof status
The lobe sign reversal is a structural constraint, not yet a contradiction.

---

## 12. Updated non-axisymmetric geometry

At every strongly positive recurrent core phase,

\[
\boxed{
P_m\ne0
\Longrightarrow
2m\text{ local defect sectors}
}
\]

and for every global defect domain reached by those sectors,

\[
\boxed{
\kappa>0\text{ near the core}
\Longrightarrow
\kappa=0\text{ somewhere in the lobe}
\Longrightarrow
\kappa<0\text{ in the same lobe}.
}
\]

Thus a recurrent non-axisymmetric winding survivor must carry a **lobe-resolved kappa sign-reversal network**.

---

## 13. Next target — material fate of the lobe crossing

The next problem is dynamical rather than elliptic:

Does the same material defect lobe recurrently preserve its positive-to-negative `kappa` architecture, or must the `kappa=0` crossing undergo

\[
\boxed{
\text{cross-lobe turnover}
\ \lor\ 
\text{critical zero-level degeneration}
\ \lor\ 
\text{finite-jet nodal reconfiguration}
\ \lor\ 
\text{axisymmetric firewall approach}?
}
\]

The M5-685 flux-weighted hysteresis law must now be imposed **within this lobe-resolved geometry**.

This is the **Lobe Hysteresis Compatibility Gate (LHCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
