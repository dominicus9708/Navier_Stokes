# DSD M17-101 — Finite degenerate peak singularity regularizes on the top-jet sheet with inherited director-area flux

Date: 2026-09-05
Canonical ID: **M17-101**

Status: **INTERNAL RANK-2 FINITE-DEGENERACY JET-LIFT GATE / M17-100 LEAVES `grad g=0` AS A POSSIBLE FAILURE OF THE ORDINARY PEAK-SHEET INTERSECTION DEGREE. M17-087, HOWEVER, SHOWS THAT A FIXED FINITE DEGENERATE MAXIMUM OF TYPE `nu>=3` HAS `G_j=D_xi^j g=0` FOR `0<=j<=nu-1` BUT `H_nu=D_xi^nu g<0`. THEREFORE THE TOP VANISHING JET `Psi_nu:=G_{nu-1}` HAS `D_xi Psi_nu=H_nu!=0`, SO ITS ZERO SET IS A REGULAR SURFACE EVEN WHEN THE LOWEST PEAK LEVEL `g=0` IS SINGULAR. ON A PERSISTENT FIXED-TYPE BRANCH THE LOWER VANISHING JETS ARE LOCKED TO ZERO, SO THE ACTUAL DEGENERATE PEAK SHEET CAN BE REPRESENTED LOCALLY BY THIS REGULAR TOP-JET SURFACE TOGETHER WITH THE LOWER-JET STRATUM CONDITIONS. DIRECTOR-AREA FLUX IS TRANSVERSE TO THE TOP-JET SHEET IFF `D_k Psi_nu!=0`, EQUIVALENT TO A NONZERO K-DIRECTION HIGHER-JET TILT `Theta_{nu,k}`. THIS RESTORES A CANONICAL INHERITED FLUX WEIGHT FOR FINITE DEGENERATE PEAKS. IF `D_k Psi_nu=0`, THE EVENT IS ONLY A REGULAR HIGHER-JET TANGENCY AND THE ALGEBRAIC INTERSECTION DEGREE OF M17-100 APPLIES WITH `Psi_nu` IN PLACE OF `g`, SO IT IS SIGNED-FLUX NEUTRAL. CONSEQUENTLY `grad g=0` BY ITSELF IS NOT A NONRECYCLABLE EVENT. THE TRUE DESCRIPTOR FAILURE OCCURS ONLY WHEN THE TOP JET ALSO VANISHES, `H_nu->0`, I.E. CRITICAL-ORDER TRANSITION, OR WHEN RANK/ENDPOINT/INTERFACE CONDITIONS FAIL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed finite degenerate maximum

Let

\[
g:=D_\xi\log\rho.
\]

For a fixed finite degenerate maximum type

\[
\nu=2r-1\ge3,
\]

M17-087 gives

\[
\boxed{
G_j:=D_\xi^jg=0
\qquad(0\le j\le\nu-1),
}
\]

and the first nonzero top jet

\[
\boxed{
H_\nu:=D_\xi^\nu g<0.
}
\]

Because `G_0=g` and `G_1=D_xi g` vanish, the ordinary level set `g=0` may fail to be a regular peak sheet when its transverse derivatives also vanish.

This is precisely the `grad g=0` event left explicit in M17-100.

---

## 2. Define the top vanishing jet

Set

\[
\boxed{
\Psi_\nu
:=G_{\nu-1}
=D_\xi^{\nu-1}g.
}
\]

At the type-`nu` maximum,

\[
\Psi_\nu=0.
\]

But its xi derivative is

\[
D_\xi\Psi_\nu
=D_\xi^\nu g
=H_\nu.
\]

Therefore

\[
\boxed{
D_\xi\Psi_\nu=H_\nu<0.
}
\]

In particular,

\[
\boxed{
\nabla\Psi_\nu\neq0.
}
\]

Hence the zero set

\[
\boxed{
S_\nu^{top}:=\{\Psi_\nu=0\}
}
\]

is a regular local surface by the implicit function theorem.

The ordinary `g=0` sheet may be singular, but the finite-degeneracy top-jet sheet is regular.

---

## 3. Lower-jet stratum locks

A fixed type is not defined by `Psi_nu=0` alone.
The lower jets must also vanish:

\[
G_0=\cdots=G_{\nu-2}=0.
\]

M17-087 gives the transverse persistence hierarchy

\[
\boxed{
D_nG_j=0,
\qquad
D_kG_j=0
\qquad(0\le j\le\nu-2).
}
\]

Thus, on a persistent fixed-type branch, the lower-jet equations are locked along the retained degenerate sheet.

The top equation

\[
\Psi_\nu=0
\]

is the first level with a nonzero xi derivative and therefore supplies the regular local defining function for the sheet.

The correct local descriptor is therefore

\[
\boxed{
\text{lower-jet stratum}
+
\text{regular top-jet sheet }S_\nu^{top}.
}
\]

---

## 4. Top-jet surface normal

The top-jet normal is

\[
\boxed{
n_\nu
=\frac{\nabla\Psi_\nu}{|\nabla\Psi_\nu|}.
}
\]

Because

\[
D_\xi\Psi_\nu=H_\nu\neq0,
\]

this normal is well-defined even at

\[
\nabla g=0.
\]

Thus the loss of the lowest-order peak normal does not destroy the finite-order critical geometry.

It only forces a change of descriptor resolution from `g` to `Psi_nu`.

---

## 5. Director-area transversality at finite degeneracy

On the pure-transverse-kernel branch,

\[
J_\xi=|J_\xi|k\neq0.
\]

The director-area current crosses the regular top-jet sheet iff

\[
J_\xi\cdot n_\nu\neq0.
\]

Equivalently,

\[
\boxed{
D_k\Psi_\nu\neq0.
}
\]

When this holds, the inherited director-area flux measure is

\[
\boxed{
d\Phi_{J,\nu}
:=J_\xi\cdot n_\nu\,dA.
}
\]

Therefore a canonical peak weight exists for the finite-degenerate type after lifting from the singular `g` sheet to the regular top-jet sheet.

No arbitrary point-counting measure is required.

---

## 6. Exact relation to the higher-jet k tilt

M17-087 defines the k-direction top-order sheet tilt by

\[
\boxed{
\Theta_{\nu,k}
=-\frac{D_kD_\xi^{\nu-1}g}{D_\xi^\nu g}.
}
\]

Using

\[
\Psi_\nu=D_\xi^{\nu-1}g,
\qquad
H_\nu=D_\xi^\nu g,
\]

this is

\[
\boxed{
\Theta_{\nu,k}
=-\frac{D_k\Psi_\nu}{H_\nu}.
}
\]

Since `H_nu!=0`,

\[
\boxed{
D_k\Psi_\nu\neq0
\iff
\Theta_{\nu,k}\neq0.
}
\]

Thus director-area transversality is exactly the nonzero higher-jet k-tilt condition.

Conversely,

\[
\boxed{
D_k\Psi_\nu=0
\iff
\Theta_{\nu,k}=0
}
\]

is a higher-jet director-area tangency.

---

## 7. Flux-labelled finite-degenerate peak population

On a fixed-type interval with

\[
H_\nu<0,
\qquad
D_k\Psi_\nu\neq0,
\]

one may label the degenerate peaks by frozen director-area flux tubes exactly as in M17-097, but using the top-jet sheet.

For a tube-label family `Lambda_nu`, any type descriptor `Y_nu` defined on the fixed-degenerate branch may therefore be distributed with the inherited measure

\[
\boxed{
F_{\nu}^{J,top}(y,\theta)
:=\int_{\Lambda_\nu}
\delta(y-Y_\nu(\lambda,\theta))
\,d\Phi_{J,\nu}(\lambda).
}
\]

This does not yet assign a sign to its state-space current.
It only closes the measure problem at fixed finite degeneracy.

---

## 8. Higher-jet tangency is again algebraically neutral

Suppose instead

\[
D_k\Psi_\nu=0
\]

while

\[
H_\nu\neq0,
\qquad
J_\xi\neq0.
\]

The top-jet surface remains regular because its xi derivative is nonzero.
Only the flux line is tangent to that regular surface.

Therefore the one-dimensional intersection-degree argument of M17-100 applies with

\[
g
\quad\mapsto\quad
\Psi_\nu.
\]

For an oriented tube segment whose endpoints remain off `Psi_nu=0`, define

\[
\boxed{
I_{\lambda,\nu}^{top}
:=
\sum_{\Psi_\nu=0}
\operatorname{sgn}(D_k\Psi_\nu).
}
\]

Then

\[
\boxed{
I_{\lambda,\nu}^{top}
=
\frac{
\operatorname{sgn}\Psi_\nu(s_+)
-
\operatorname{sgn}\Psi_\nu(s_-)
}{2}.
}
\]

Hence regular higher-jet tangencies are signed-flux neutral.

---

## 9. `grad g=0` is a descriptor-resolution event, not necessarily genealogy loss

At a finite degenerate peak one may have

\[
\boxed{
\nabla g=0
}
\]

while simultaneously

\[
\boxed{
\nabla\Psi_\nu\neq0.
}
\]

Therefore

\[
\boxed{
\nabla g=0
\not\Rightarrow
\text{loss of finite-order peak carrier}.
}
\]

The correct interpretation is

\[
\boxed{
\text{lowest-order peak descriptor singular}
\Longrightarrow
\text{lift to finite top-jet descriptor}.
}
\]

This is a DSD resolution change, not automatically a physical or topological turnover.

---

## 10. True failure of the top-jet chart

The top-jet surface loses its guaranteed xi transversality only if

\[
\boxed{
H_\nu=D_\xi^\nu g\to0.
}
\]

But this is exactly the critical-type boundary identified by M17-092--093:

\[
\boxed{
Z_\nu\to0
}
\]

while `b!=0`.

Thus the finite-degenerate singularity hierarchy terminates not at `grad g=0`, but at critical-order transition.

If the next finite type exists, the descriptor can be lifted again to its next top jet.
If the order becomes unbounded or `b`, `J_xi`, endpoints, or charts fail, those are separate exits.

---

## 11. Consequence for the nonrecyclable event list

M17-100 left

\[
E_{endpoint}
\cup E_{\nabla g=0}
\cup E_{J_\xi=0}
\cup E_{chart/interface}
\]

as possible algebraic-flux failure classes.

M17-101 removes ordinary finite-order `grad g=0` from that list whenever the fixed type `nu` remains finite and `H_nu!=0`.

The refined list is

\[
\boxed{
E_{nonrecyclable}^{R2}
\subset
E_{endpoint}
\cup
E_{H_\nu=0\,\mathrm{type\ boundary}}
\cup
E_{J_\xi=0}
\cup
E_{chart/interface}
\cup
E_{unbounded\ order}.
}
\]

M17-088 already excludes unbounded critical order on the compact analytic peak-floor hull absent endpoint/rank/chart degeneration.

Therefore, on that hull, the genuinely unresolved classes reduce further to

\[
\boxed{
E_{endpoint}
\cup
E_{type\ boundary}
\cup
E_{J_\xi=0}
\cup
E_{chart/interface}.
}
\]

---

## 12. DSD analysis

Finite degeneracy forms a descriptor tower

\[
\boxed{
G_0
\to G_1
\to\cdots\to
G_{\nu-1}
\to H_\nu.
}
\]

The first levels may all vanish and fail to define a regular surface.
The first nonzero derivative `H_nu` certifies that the immediately preceding top vanishing jet `G_{nu-1}` is a valid regular defining function.

Thus finite critical order is precisely what prevents a complete loss of local describability.

---

## 13. DSD audit

### Audit A — treating `grad g=0` as a singular physical event
Rejected for fixed finite type. The top-jet sheet is regular.

### Audit B — using `Psi_nu=0` without lower-jet constraints
Rejected. The actual type-`nu` branch also requires `G_0=...=G_{nu-2}=0`.

### Audit C — assuming top-jet director-area transversality
Not assumed. It splits into `D_k Psi_nu!=0` versus higher-jet tangency.

### Audit D — counting higher-jet tangency as charge loss
Rejected by the algebraic intersection-degree argument.

### Audit E — claiming `H_nu=0` is itself a contradiction
Rejected. It is a critical-order transition and must be matched to the neighboring finite type or a genuine exit.

### Audit F — proof status
Finite-degenerate peak singularity is regularized by a higher-jet chart, but type-boundary/rank/endpoint/interface assembly remains open.

---

## 14. Updated Rank-2 peak frontier

On the compact finite-order hard hull,

\[
\boxed{
R_{2,peak}
\Longrightarrow
\bigcup_{\nu\le\nu_*}
\left(
R_{\nu}^{top\text{-}J\ transverse}
\ \lor\
T_{\nu}^{top\text{-}J\ tangent}
\ \lor\
B_{\nu\to\nu'}^{type}
\right)
\ \lor\
E_{endpoint/rank/interface}.
}
\]

The first branch has an inherited director-area flux weight.
The second is signed-flux neutral while the top-jet surface remains regular.
The third is the finite critical-type boundary.

The next high-value gate is therefore the **stratified type-boundary flux-matching gate**: determine whether the inherited top-jet flux measures on adjacent finite critical types can be canonically matched through `H_nu=0`, or whether a genuine source survives only there.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
