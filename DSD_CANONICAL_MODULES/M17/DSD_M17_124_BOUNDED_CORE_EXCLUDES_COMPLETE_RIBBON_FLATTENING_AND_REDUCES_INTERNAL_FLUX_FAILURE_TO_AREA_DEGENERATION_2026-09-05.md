# DSD M17-124 — Bounded core excludes complete-ribbon flattening and reduces internal flux failure to area degeneration

Date: 2026-09-05
Canonical ID: **M17-124**

Status: **EXACT BOUNDED-CORE GEOMETRIC REDUCTION / A COMPLETE CRITICAL-RIBBON FIBER IS A CIRCLE OF DIAMETER `2/|q|`. IF THE WHOLE MATERIAL LOOP IS CONTAINED IN A FIXED BOUNDED SIMILARITY CORE `Omega`, ITS DIAMETER CANNOT EXCEED `diam(Omega)`, SO `|q|>=2/diam(Omega)` AND ITS LENGTH IS AT MOST `pi diam(Omega)`. THEREFORE THE `q -> 0` FLATTENING ESCAPE OF M17-122 CANNOT OCCUR AS AN INTERNAL COMPLETE-RIBBON DEGENERATION. IT NECESSARILY BECOMES A RIBBON-COVER/BOUNDARY-TURNOVER EXIT. WITH NORMALIZED AMPLITUDE, INTERNAL COMPLETE-RIBBON FLUX-CAPTURE FAILURE IS REDUCED TO DIRECTOR-AREA DEGENERATION, WHICH M17-123 PUSHES TO FRESH-CARRIER RANK-ONE ACCUMULATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed bounded recurrent core

Let

\[
\Omega\subset\mathbb R^3
\]

be a fixed bounded similarity-coordinate core and define

\[
\boxed{D_\Omega:=\operatorname{diam}(\Omega)<\infty.}
\]

Consider a complete critical-ribbon kernel loop

\[
\Gamma_\lambda\subset\Omega.
\]

M17-114/M17-115 give

\[
D_kk=q\,n,
\qquad D_kq=0,
\]

so `Gamma_lambda` is a planar circle of radius

\[
R_\lambda=|q_\lambda|^{-1}.
\]

---

## 2. Exact curvature floor from boundedness

Two antipodal points of the circle are separated by

\[
2R_\lambda=\frac{2}{|q_\lambda|}.
\]

Both points belong to `Omega`, hence by the definition of diameter

\[
\frac{2}{|q_\lambda|}
\le D_\Omega.
\]

Therefore

\[
\boxed{
|q_\lambda|
\ge
\frac{2}{D_\Omega}.
}
\]

The loop length satisfies

\[
L_\lambda
=\frac{2\pi}{|q_\lambda|}
\le
\boxed{\pi D_\Omega}.
\]

Thus no sequence of complete critical-ribbon loops wholly contained in the same bounded core can have `q -> 0`.

---

## 3. Meaning of q-flattening

Suppose a critical-ribbon sequence has

\[
|q_n|\to0.
\]

Then its circle diameter diverges:

\[
\frac{2}{|q_n|}\to\infty.
\]

For any fixed bounded `Omega`, sufficiently large loops cannot satisfy

\[
\Gamma_n\subset\Omega.
\]

Hence

\[
\boxed{
q\to0
\Longrightarrow
\text{complete-ribbon cover exits the bounded core}.
}
\]

This is a spatial boundary/turnover phenomenon, not a new internal compact-ribbon geometry.

---

## 4. Improved upper flux-capture bound

M17-122 gives

\[
\mathcal W_J(\lambda)
=
\oint_{\Gamma_\lambda}
\frac{\rho^2}{|J_\xi|}ds.
\]

Assume normalized amplitude

\[
\rho\le C_\rho
\]

and a director-area lower bound on the complete loop

\[
|J_\xi|\ge c_J>0.
\]

Using `L_lambda<=pi D_Omega`,

\[
\boxed{
\mathcal W_J(\lambda)
\le
\frac{\pi D_\Omega C_\rho^2}{c_J}.
}
\]

Therefore for any complete-ribbon bundle wholly contained in `Omega`,

\[
\boxed{
E_T^\omega
\le
\frac{\pi D_\Omega C_\rho^2}{c_J}\Phi_T.
}
\]

No independent lower bound on `|q|` has to be assumed; bounded-core containment provides it geometrically.

---

## 5. Internal failure dichotomy

Within the class

\[
\boxed{
\text{complete critical ribbon}
+
\Gamma_\lambda\subset\Omega
+
\rho\le C_\rho,
}
\]

upper flux capture can fail only if there is no uniform positive lower bound for `|J_xi|`.

Thus

\[
\boxed{
F_{capture}^{failure,internal}
\Longrightarrow
\inf|J_\xi|\to0.
}
\]

If the relevant normalized vorticity remains nontrivial, M17-123 then yields

\[
\boxed{
F_{capture}^{failure,internal}
\Longrightarrow
A_{R1}^{fresh-carrier\ accumulation}.
}
\]

---

## 6. External-loop alternative

If a complete critical circle is not wholly contained in `Omega`, the core sees only an arc or a changing intersection set.
Then the correct object is not the closed-loop inventory of M17-116 but the boundary-crossing ledger of M17-108/M17-112.

Therefore

\[
\boxed{
q\text{-flattening}
\subset
T_{ribbon-cover/boundary}
}
\]

for a fixed bounded core.

The branch must be analyzed through entry/exit and physical genealogy rather than through an internal complete-loop recurrence law.

---

## 7. DSD audit

### Audit A — using bounded hard hull as a spatial diameter

Rejected. The diameter argument applies only to an explicitly fixed bounded spatial similarity-coordinate core `Omega`, not to abstract state/jet compactness.

### Audit B — assuming every ribbon loop lies wholly in Omega

Rejected. Loops crossing `partial Omega` remain as the boundary-turnover branch.

### Audit C — interpreting q -> 0 as Rank-1 degeneration

Rejected. `q` is kernel-line curvature here. Its vanishing means circle flattening/decompactification, not by itself `rank(d xi)<=1`.

### Audit D — proof status

The internal complete-ribbon flattening escape is removed. Boundary-crossing ribbons and fresh-carrier Rank-1 accumulation remain open.

---

## 8. Updated bounded-core ribbon frontier

For normalized Rank-2 critical ribbons in a fixed bounded recurrent core,

\[
\boxed{
R_2^{ribbon}(\Omega)
\Longrightarrow
F_{capture}^{nondeg}
\ \lor\
A_{R1}^{fresh-carrier}
\ \lor\
T_{boundary/ribbon-cover}.
}
\]

The next hard step is the physical return-density gate on the flux-captured branch, while the other two exits must be connected respectively to the existing Rank-1 pressure/firewall structure and the boundary turnover ledger.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
