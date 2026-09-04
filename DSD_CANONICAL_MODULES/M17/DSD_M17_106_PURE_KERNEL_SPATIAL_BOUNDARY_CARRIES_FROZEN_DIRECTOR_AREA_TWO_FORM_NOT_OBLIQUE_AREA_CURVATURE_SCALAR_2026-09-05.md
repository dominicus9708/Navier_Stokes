# DSD M17-106 — Pure-kernel spatial boundary carries the frozen director-area two-form, not the oblique area-curvature scalar

Date: 2026-09-05
Canonical ID: **M17-106**

Status: **INTERNAL RANK-2 SPATIAL CARRIER-BOUNDARY AUDIT / THE SOURCE-FREE SCALAR `Q=|j_xi||b|` OF M17-034 BELONGS TO THE `j_xi != 0` OBLIQUE BRANCH AND VANISHES IDENTICALLY ON THE CURRENT PURE-TRANSVERSE-KERNEL HARD SURVIVOR `j_xi=0`, `J_xi!=0`. IT MUST NOT BE IMPORTED INTO THE PURE-KERNEL BOUNDARY LEDGER. THE CORRECT CARRIER OBJECT IS THE CLOSED FROZEN TWO-FORM `beta_xi=i_{J_xi}dV`. FOR ANY FIXED OPEN SPATIAL SURFACE `S`, ITS DIRECTOR-AREA FLUX OBEYS THE EXACT EDGE-TRANSPORT LAW `d/dtheta int_S beta_xi = -int_{partial S} i_B beta_xi = int_{partial S}(B x J_xi)·dl`. FOR A CLOSED SPATIAL BOUNDARY `partial Omega`, THE SIGNED DIRECTOR-AREA FLUX IS IDENTICALLY ZERO BECAUSE `div J_xi=0`. THIS IS NOT A STATEMENT THAT MATERIAL TUBE TURNOVER VANISHES: `J_xi·n` MEASURES ORIENTED DIRECTOR-AREA LINE FLUX, WHILE MATERIAL ENTRY/EXIT IS CONTROLLED BY THE MOTION OF THE FROZEN TUBES UNDER `B`. THERE IS NO CANONICAL POSITIVE VOLUME DENSITY OF PURE-KERNEL DIRECTOR-AREA CARRIERS DERIVED HERE. THUS THE SPATIAL BOUNDARY PROBLEM REACHES A TWO-FORM/SECTION FIREWALL RATHER THAN A ONE-SIDED CHARGE COST. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scope correction: M17-034 does not apply to the pure-kernel survivor

M17-034 defines, on the oblique branch,

\[
Q:=|j_\xi|\,|b|,
\qquad
j_\xi:=J_\xi\cdot\xi,
\]

and derives

\[
\partial_\theta Q+\nabla\cdot(BQ)=0.
\]

That calculation explicitly assumes

\[
j_\xi\neq0.
\]

The current intrinsic Rank-2 hard survivor is instead

\[
\boxed{
j_\xi=0,
\qquad
J_\xi=|J_\xi|k\neq0,
\qquad
D_k\xi=0.
}
\]

Therefore

\[
Q\equiv0
\]

on the present branch.

Hence the M17-034 positive scalar turnover ledger cannot be used as a boundary inventory for the pure-kernel survivor.

This is a scope correction, not a loss of the M17-034 result on its original branch.

---

## 2. Correct pure-kernel carrier object

M17-026 gives

\[
\boxed{\nabla\cdot J_\xi=0}
\]

and

\[
\boxed{
D_BJ_\xi
=(\nabla B)J_\xi-\frac32J_\xi.
}
\]

With

\[
\nabla\cdot B=\frac32,
\]

define the director-area two-form

\[
\boxed{
\beta_\xi:=\iota_{J_\xi}dV.
}
\]

Then

\[
\boxed{d\beta_\xi=0}
\]

and the Cauchy law is equivalent to

\[
\boxed{
(\partial_\theta+\mathcal L_B)\beta_\xi=0.
}
\]

Thus `beta_xi` is the exact frozen carrier descriptor on the pure-kernel branch.

---

## 3. Fixed open-surface flux law

Let `S` be a fixed oriented spatial surface in similarity coordinates.
Define

\[
\Phi_J(S,\theta)
:=\int_S\beta_\xi
=\int_S J_\xi\cdot n_S\,dA.
\]

Since `S` is fixed,

\[
\frac d{d\theta}\Phi_J(S,\theta)
=\int_S\partial_\theta\beta_\xi.
\]

Use the frozen law:

\[
\partial_\theta\beta_\xi
=-\mathcal L_B\beta_\xi.
\]

Cartan's identity gives

\[
\mathcal L_B\beta_\xi
=d(\iota_B\beta_\xi)
+\iota_B(d\beta_\xi).
\]

Because `d beta_xi=0`,

\[
\boxed{
\frac d{d\theta}\Phi_J(S,\theta)
=-\int_{\partial S}\iota_B\beta_\xi.
}
\]

In Euclidean vector notation,

\[
\iota_B\beta_\xi
=(J_\xi\times B)^\flat,
\]

so

\[
\boxed{
\frac d{d\theta}
\int_SJ_\xi\cdot n_S\,dA
=
\oint_{\partial S}(B\times J_\xi)\cdot d\ell.
}
\]

This is the exact open-section transport law.

---

## 4. Material cross-sections

More generally, let `S(theta)` move with velocity `V`.
Then

\[
\frac d{d\theta}\int_{S(\theta)}\beta_\xi
=
\int_{S(\theta)}
(\partial_\theta+\mathcal L_V)\beta_\xi.
\]

Using the frozen law,

\[
\boxed{
\frac d{d\theta}\int_{S(\theta)}\beta_\xi
=
\int_{S(\theta)}\mathcal L_{V-B}\beta_\xi.
}
\]

If the section is material,

\[
V=B,
\]

then

\[
\boxed{
\frac d{d\theta}\int_{S(\theta)}\beta_\xi=0.
}
\]

Thus the inherited tube weight `dPhi_J` of M17-097 is precisely the flux of this frozen two-form through a material tube cross-section.

---

## 5. Closed spatial boundary

Let `Omega` be a bounded spatial region with closed boundary `partial Omega`.
Because

\[
\nabla\cdot J_\xi=0,
\]

the divergence theorem gives at every regular time

\[
\boxed{
\int_{\partial\Omega}
J_\xi\cdot n\,dA
=0.
}
\]

This identity is instantaneous and does not require time recurrence.

It means that a divergence-free director-area line field has zero **net oriented line flux** through a closed surface.

---

## 6. Why this is not a material entry/exit rate

A tempting but incorrect interpretation is

\[
\int_{\partial\Omega}J_\xi\cdot n\,dA=0
\quad\Longrightarrow\quad
\text{no director-area carrier turnover through }\partial\Omega.
\]

This is false.

`J_xi·n dA` counts oriented director-area field-line flux through the spatial surface.
The material flux tubes themselves are transported by `B` because `beta_xi` is frozen into the `B` flow.

A tube may enter `Omega` at one boundary point and leave at another; the two oriented intersections cancel in the closed-surface integral while the tube still passes through the region.

Therefore

\[
\boxed{
\text{oriented }J_\xi\text{ boundary flux}
\neq
\text{material tube-label crossing rate}.
}
\]

The latter requires a section/tube-label construction such as M17-097, not the closed-surface divergence theorem alone.

---

## 7. No canonical positive volume carrier density has been derived

On the `j_xi!=0` oblique branch, M17-034 supplied a positive scalar density `Q` with a source-free volume continuity law.

On the pure-kernel branch,

\[
j_\xi=0,
\]

so that density disappears.

The remaining exact object is a two-form/flux measure.
There is currently no derived positive scalar `q_carrier` satisfying

\[
\partial_\theta q_{carrier}
+\nabla\cdot(Bq_{carrier})=0
\]

whose volume integral counts pure-kernel director-area tubes in `Omega`.

Inventing one would mix a two-dimensional flux descriptor with a three-dimensional volume descriptor.

---

## 8. Consequence for the boundary-cost route

The spatial carrier-boundary problem therefore splits into two distinct ledgers:

1. **section flux:**
   \[
   d\Phi_J=\beta_\xi|_{S},
   \]
   materially conserved on a tube cross-section;
2. **peak compensation:**
   \[
   \mathcal M^{(\nu)}>0,
   \]
   defined on the moving line-peak/critical network.

No current theorem supplies a canonical positive volume measure that multiplies these two descriptors over a fixed spatial core.

Hence a one-sided inequality of the form

\[
\text{outgoing carrier charge}
>\text{incoming carrier charge}
\]

cannot be justified from the frozen two-form alone.

---

## 9. DSD analysis

This gate exposes a descriptor-rank mismatch:

\[
\boxed{
\text{director-area carrier}
=\text{2-form / cross-section flux},
}
\]

whereas

\[
\boxed{
\text{Eulerian core inventory}
=\text{3-volume quantity}.
}
\]

The oblique scalar `Q` previously bridged that mismatch on `j_xi!=0`.
It is absent on the pure-kernel survivor.

Therefore the correct next object, if one exists, must be derived from a canonical tube-label cross-section or from a new PDE identity; it cannot be obtained by reusing the oblique volume density.

---

## 10. DSD audit

### Audit A — importing M17-034 into j_xi=0
Rejected.

### Audit B — treating `int_{partial Omega} J_xi·n=0` as no turnover
Rejected.

### Audit C — replacing signed flux by absolute flux without a theorem
Rejected.

### Audit D — treating the compact analytic hard hull as a physical spatial region
Rejected. Spatial boundary formulas apply only to an explicitly defined similarity-coordinate region `Omega`. Compactness of the state/jet hard hull is used only to supply uniform regularity bounds.

### Audit E — proof status
The pure-kernel boundary route reaches an exact two-form/section firewall. No contradiction is obtained.

---

## 11. Updated Rank-2 boundary frontier

The current boundary hierarchy is

\[
\boxed{
\text{frozen material tube flux }d\Phi_J
\to
\text{open-section edge transport}
\to
\text{peak compensation on tube intersections}.
}
\]

Clean finite interior genealogy remains recyclable by M17-098--103.
Finite-time `J_xi=0` and `rho=0` same-marker exits remain excluded by M17-104--105.

The next useful question is whether the positive peak margin can be integrated directly over the **tube-label measure `dPhi_J`** on a chosen recurrent cross-section, thereby avoiding any fictitious volume carrier density.

This is the **Director-Area-Weighted Margin Section Gate (DAWMSG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
