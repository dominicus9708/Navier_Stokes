# DSD M17-108 — Spatially restricted director-area-weighted margin has an exact boundary import/export ledger

Date: 2026-09-05
Canonical ID: **M17-108**

Status: **INTERNAL PURE-KERNEL SPATIAL BOUNDARY MARGIN GATE / M17-107 DEFINES A POSITIVE MARGIN INVENTORY DIRECTLY ON THE FROZEN DIRECTOR-AREA TUBE MEASURE `dPhi_J`, AVOIDING THE NONEXISTENT PURE-KERNEL VOLUME CARRIER DENSITY. TO REINTRODUCE A FIXED SPATIAL CORE `Omega`, MARK WHETHER THE CANONICAL PEAK INTERSECTION `x_*(lambda,theta)` OF EACH TRANSVERSE TUBE LIES INSIDE `Omega`. THE INTERSECTION MOVES WITH EXACT VELOCITY `V_*=B+alpha_J k`, `alpha_J=-D_xi(sigma+kappa)/D_k g`. FOR `Omega={phi<0}`, THE RESTRICTED INVENTORY `N_Omega=int H(-phi(x_*)) N_R2 dPhi_J` OBEYS `dN_Omega/dtheta=-(3/2)N_Omega+P_Omega+S_Omega-F_boundary`, WHERE `F_boundary=int delta(phi(x_*)) N_R2 V_*·grad phi dPhi_J` IS THE SIGNED OUTWARD MARGIN FLUX. SPLITTING POSITIVE/NEGATIVE NORMAL VELOCITY GIVES THE EXACT RECURRENT PAYMENT `mean(P_Omega+S_Omega+F_in-F_out)=(3/2)mean N_Omega>0` ON CLEAN TRANSVERSE POPULATIONS. THUS SPATIAL TURNOVER IS NOW AN EXPLICIT INHERITED-MEASURE LEDGER, BUT NO CURRENT IDENTITY FORCES `F_out>=F_in` OR BOUNDS THE INTERNAL RECHARGE, SO BOUNDARY REENTRY REMAINS A REAL RECYCLING FIREWALL RATHER THAN A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed spatial core and tube-labelled peak intersection

Let `Omega` be a fixed bounded region in similarity-coordinate space.
Choose a smooth defining function

\[
\boxed{
\Omega=\{x:\phi(x)<0\},
\qquad
\partial\Omega=\{\phi=0\},
}
\]

with

\[
\nabla\phi\neq0
\]

near the boundary.

Work first on the clean transverse peak population of M17-107:

\[
\boxed{
g=0,
\quad C=D_\xi g<0,
\quad D_kg\neq0,
\quad \mathcal M_{R2}>0.
}
\]

For every frozen director-area tube label `lambda`, let

\[
\boxed{x_*(\lambda,\theta)}
\]

be its selected regular peak intersection.

---

## 2. Exact peak-intersection velocity

M17-097 gives the canonical slide along the same frozen director-area tube:

\[
\boxed{
\alpha_J
=-\frac{D_\xi(\sigma+\kappa)}{D_kg}.
}
\]

Therefore the selected intersection moves in physical similarity space with

\[
\boxed{
V_*:=B+\alpha_Jk.
}
\]

For any fixed spatial scalar `f(x)`, its derivative along the tube-labelled intersection is

\[
\boxed{
D_J^*f
=V_*\cdot\nabla f.
}
\]

In particular,

\[
\boxed{
D_J^*\phi(x_*)
=V_*\cdot\nabla\phi.
}
\]

---

## 3. Spatially restricted positive margin inventory

Define the positive weighted margin

\[
N:=N_{R2}=|a|\mathcal M_{R2}>0.
\]

The inherited flux measure is the frozen tube-label measure

\[
d\Phi_J.
\]

Define

\[
\boxed{
\mathscr N_\Omega(\theta)
:=\int_\Lambda
H(-\phi(x_*(\lambda,\theta)))
N(\lambda,\theta)
\,d\Phi_J(\lambda),
}
\]

where `H` is the Heaviside function.

This counts positive margin only on tube-labelled peak intersections presently lying inside `Omega`.

No spatial volume carrier density is introduced.

---

## 4. Differentiate the spatial indicator

Distributionally,

\[
D_J^*H(-\phi(x_*))
=-\delta(\phi(x_*))D_J^*\phi(x_*).
\]

Hence

\[
\boxed{
D_J^*H(-\phi(x_*))
=-\delta(\phi(x_*))
V_*\cdot\nabla\phi.
}
\]

A positive value of

\[
V_*\cdot\nabla\phi
\]

corresponds to outward crossing for the convention `phi<0` inside.

---

## 5. Insert the M17-107 margin law

M17-107 gives

\[
\boxed{
D_J^*N
=-\frac32N
+|a|\mathcal R_{R2}
+\alpha_JD_kN.
}
\]

Define the restricted internal terms

\[
\boxed{
\mathscr P_\Omega
:=\int_\Lambda
H(-\phi(x_*))
|a|\mathcal R_{R2}
\,d\Phi_J,
}
\]

and

\[
\boxed{
\mathscr S_\Omega
:=\int_\Lambda
H(-\phi(x_*))
\alpha_JD_kN
\,d\Phi_J.
}
\]

---

## 6. Exact signed spatial boundary flux

Differentiate `mathscr N_Omega`.
Because `dPhi_J` is fixed on the frozen tube labels,

\[
\begin{aligned}
\frac d{d\theta}\mathscr N_\Omega
={}&
\int H(-\phi)D_J^*N\,d\Phi_J\\
&+
\int N D_J^*H(-\phi)\,d\Phi_J.
\end{aligned}
\]

Use Sections 4--5:

\[
\boxed{
\frac d{d\theta}\mathscr N_\Omega
=-\frac32\mathscr N_\Omega
+\mathscr P_\Omega
+\mathscr S_\Omega
-\mathscr F_{\partial\Omega},
}
\]

where

\[
\boxed{
\mathscr F_{\partial\Omega}
:=\int_\Lambda
\delta(\phi(x_*))
N
\,V_*\cdot\nabla\phi
\,d\Phi_J.
}
\]

This is the exact signed margin-weighted spatial boundary current on the tube-label measure.

---

## 7. Inward and outward parts

If `phi` is chosen as signed distance near `partial Omega`, then

\[
n=\nabla\phi
\]

on the boundary.

Define

\[
\boxed{
\mathscr F_{out}
:=\int
\delta(\phi(x_*))
N\,[V_*\cdot n]_+
\,d\Phi_J,
}
\]

and

\[
\boxed{
\mathscr F_{in}
:=\int
\delta(\phi(x_*))
N\,[-V_*\cdot n]_+
\,d\Phi_J.
}
\]

Both are nonnegative and

\[
\boxed{
\mathscr F_{\partial\Omega}
=\mathscr F_{out}-\mathscr F_{in}.
}
\]

Hence

\[
\boxed{
\frac d{d\theta}\mathscr N_\Omega
=-\frac32\mathscr N_\Omega
+\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}.
}
\]

---

## 8. Recurrent spatial-core payment

Assume the clean spatially restricted tube-labelled peak population is recurrent with zero long-time mean drift of `mathscr N_Omega`.
Then

\[
\boxed{
\left\langle
\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
\right\rangle
=
\frac32
\left\langle
\mathscr N_\Omega
\right\rangle.
}
\]

If the recurrent core carries a positive director-area flux mass with a positive margin floor, then

\[
\boxed{
\left\langle
\mathscr N_\Omega
\right\rangle>0
}
\]

and therefore

\[
\boxed{
\left\langle
\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
\right\rangle>0.
}
\]

This is the exact Rank-2 spatial carrier/recharge budget on the inherited measure.

---

## 9. What the boundary law does and does not say

The law does not imply

\[
\mathscr F_{out}\ge\mathscr F_{in}
\]

or its reverse.

A recurrent Eulerian core may import high-margin tube intersections and export lower-margin ones.
Likewise, the internal higher-jet term `P_Omega` and section-slide term `S_Omega` remain signed.

Thus the boundary can participate in a **margin conveyor**:

\[
\boxed{
\text{lower-margin export}
\quad+\quad
\text{higher-margin import}
}
\]

without violating conservation of the underlying director-area tube flux.

No current theorem forbids this sorting.

---

## 10. Relation to unweighted carrier flux

M17-106 shows that for a closed spatial boundary

\[
\int_{\partial\Omega}J_\xi\cdot n\,dA=0.
\]

This does not force

\[
\mathscr F_{out}=\mathscr F_{in}
\]

in the present ledger because the two quantities measure different objects:

- `J_xi·n` is oriented director-area line flux through a spatial surface;
- `mathscr F_in/out` is the time rate at which **peak intersections carried by frozen tube labels** cross the spatial boundary, weighted by positive margin `N`.

Conflating them would mix field-line orientation with tube-label transport.

---

## 11. Event terms

The present derivation assumes `D_k g!=0` and a clean selected peak branch.
If a tangency, peak birth/death, finite-type chart event, or intersection genealogy event occurs, add the explicit margin event source

\[
\boxed{\mathscr B_N.}
\]

Then

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

Unweighted director-area flux neutrality does not imply `mathscr B_N=0`.

---

## 12. DSD analysis

The spatial boundary ledger now lives entirely on one descriptor measure:

\[
\boxed{
d\Phi_J.
}
\]

The roles are separated as

\[
\boxed{
\text{carrier measure}
\to
\text{positive margin state}
\to
\text{internal recharge}
\to
\text{spatial import/export}.
}
\]

This removes the previous two-form/volume mismatch without pretending that the spatial core itself is material.

---

## 13. DSD audit

### Audit A — integrating pure-kernel carriers with a fictitious volume density
Rejected.

### Audit B — using `B·n` alone as the peak-boundary speed
Rejected. The selected tube-labelled peak moves with `B+alpha_J k`.

### Audit C — treating zero signed `J_xi` flux through a closed boundary as equal margin import/export
Rejected.

### Audit D — dropping tangency/branch events
Rejected; they enter through `mathscr B_N`.

### Audit E — claiming recurrence is contradictory
Rejected. The exact budget is compatible with a margin-sorting conveyor unless an independent sign/coercivity estimate is added.

### Audit F — proof status
The spatial boundary turnover is now explicit and measure-correct, but remains sign-indefinite.

---

## 14. Updated Rank-2 spatial frontier

The clean recurrent pure-kernel peak population must satisfy

\[
\boxed{
\left\langle
\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
\right\rangle
=
\frac32
\left\langle
\mathscr N_\Omega
\right\rangle>0.
}
\]

Therefore the remaining possible services of the three-halves damping are exactly

\[
\boxed{
\text{PDE/higher-jet recharge}
\ \lor\
\text{same-tube spatial slide}
\ \lor\
\text{high-margin boundary import}
\ \lor\
\text{margin-weighted event hysteresis}.
}
\]

The next gate should determine whether the event term `mathscr B_N` is recyclable or has a signed hysteresis law at generic director-area/peak tangencies.

This is the **Margin-Weighted Tangency Hysteresis Gate (MWTHG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
