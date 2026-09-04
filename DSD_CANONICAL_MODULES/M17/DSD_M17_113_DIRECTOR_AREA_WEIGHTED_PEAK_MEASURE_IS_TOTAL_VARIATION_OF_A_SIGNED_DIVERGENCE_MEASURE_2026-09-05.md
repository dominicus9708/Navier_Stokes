# DSD M17-113 — Director-area-weighted peak measure is the total variation of a signed divergence measure

Date: 2026-09-05
Canonical ID: **M17-113**

Status: **INTERNAL PURE-KERNEL PEAK-MEASURE COAREA / DIVERGENCE GATE / ON A TRANSVERSE PURE-KERNEL PEAK SET `g=D_xi log rho=0`, `J_xi=|J_xi|k` AND `D_k g!=0`, THE FROZEN TUBE-FLUX MEASURE OF M17-097 HAS AN EXACT SPATIAL REPRESENTATION `dmu_peak^J=delta(g)|J_xi·grad g|dV`. THE ORIENTATION-SIGNED VERSION IS `dnu_peak^J=delta(g)J_xi·grad g dV`, AND BECAUSE `div J_xi=0`, DISTRIBUTIONALLY `delta(g)J_xi·grad g=div(H(g)J_xi)`. THUS THE POSITIVE PEAK COUNT/FLUX MEASURE IS THE TOTAL-VARIATION VERSION OF A SIGNED DIVERGENCE MEASURE. FOR A FIXED REGION `Omega`, THE SIGNED PEAK FLUX IS A PURE BOUNDARY TERM `int_Omega dnu=int_partialOmega H(g)J_xi·n dA`, WHILE THE POSITIVE TOTAL VARIATION IS NOT CONTROLLED BY THAT SIGNED BOUNDARY FLUX AND CAN INCREASE THROUGH FOLD PAIR CREATION. RESTRICTING TO `C=D_xi g<0` GIVES A CANONICAL SPATIAL FORM OF THE POSITIVE MAXIMUM-MARGIN INVENTORY `int N 1_{C<0} delta(g)|J_xi·grad g|dV`, EQUIVALENT TO THE TUBE-LABEL INTEGRAL ON CLEAN TRANSVERSE SHEETS. THIS SHARPENS THE POSITIVITY-VERSUS-CONSERVATION FIREWALL AND PROVIDES A COMMON SPATIAL REPRESENTATION FOR FUTURE COERCIVE ESTIMATES. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pure-kernel transverse peak geometry

Work on

\[
\boxed{
J_\xi=|J_\xi|k\neq0,
\qquad
D_k\xi=0.
}
\]

Define

\[
\boxed{g:=D_\xi\log\rho.}
\]

On a regular transverse critical sheet,

\[
\boxed{
g=0,
\qquad
D_kg\neq0.}
\]

Because `J_xi=|J_xi|k`,

\[
\boxed{
J_\xi\cdot\nabla g
=|J_\xi|D_kg.
}
\]

---

## 2. Tube-coordinate coarea identity

Take local flux-tube coordinates `(lambda_1,lambda_2,s)` where `s` runs along the oriented `k` direction and `dPhi_J(lambda)` is the director-area flux carried by the tube bundle.

Flux conservation along a tube gives the local volume relation

\[
\boxed{
|J_\xi|\,dV
=d\Phi_J\,ds
}
\]

for the corresponding oriented flux coordinates.

For a test function `f`, the one-dimensional root identity gives

\[
\int f\,\delta(g)|D_kg|\,ds
=\sum_{s_i:g(s_i)=0}f(s_i)
\]

on transverse roots.

Therefore

\[
\boxed{
\int
f\,\delta(g)|J_\xi\cdot\nabla g|\,dV
=
\int d\Phi_J
\sum_{g=0}f.
}
\]

Thus the spatial measure

\[
\boxed{
d\mu_{peak}^J
:=\delta(g)|J_\xi\cdot\nabla g|\,dV
}
\]

is exactly the inherited director-area tube flux counted once per transverse peak/critical intersection.

---

## 3. Orientation-signed peak measure

Define instead

\[
\boxed{
d\nu_{peak}^J
:=\delta(g)
J_\xi\cdot\nabla g\,dV.
}
\]

This weights each transverse intersection by

\[
\operatorname{sgn}(D_kg)
\]

relative to the fixed orientation of `J_xi`.

It is the spatial distribution corresponding to the algebraic tube-intersection number of M17-100/103.

---

## 4. Exact divergence representation

Since

\[
\nabla\cdot J_\xi=0,
\]

and distributionally

\[
\nabla H(g)=\delta(g)\nabla g,
\]

we have

\[
\begin{aligned}
\nabla\cdot(H(g)J_\xi)
&=H(g)\nabla\cdot J_\xi
+J_\xi\cdot\nabla H(g)\\
&=\delta(g)J_\xi\cdot\nabla g.
\end{aligned}
\]

Hence

\[
\boxed{
\delta(g)J_\xi\cdot\nabla g
=\nabla\cdot(H(g)J_\xi)
}
\]

distributionally.

This identity remains meaningful across finite critical degeneracies in the distributional/BV sense, even when the simple-root coarea formula must be interpreted by limiting charts.

---

## 5. Signed peak flux is a boundary quantity

For a fixed bounded spatial region `Omega`,

\[
\boxed{
\int_\Omega d\nu_{peak}^J
=
\int_{\partial\Omega}
H(g)J_\xi\cdot n\,dA.
}
\]

Thus the **signed algebraic peak flux** inside a region is fixed by the director-area flux through the part of the spatial boundary lying in the sign domain `g>0`.

This is the spatial divergence-theorem form of the endpoint-degree identity from M17-100.

---

## 6. Positive peak measure is total variation, not signed flux

The positive inherited measure is

\[
\boxed{
|d\nu_{peak}^J|
=d\mu_{peak}^J
=\delta(g)|J_\xi\cdot\nabla g|\,dV
}
\]

on the regular transverse set.

Therefore

\[
\boxed{
\text{positive peak measure}
=\text{total variation of the signed peak measure}.
}
\]

The divergence theorem controls the signed integral, not this total variation.

Consequently there is no estimate of the form

\[
\int_\Omega d\mu_{peak}^J
\le
\left|\int_{\partial\Omega}H(g)J_\xi\cdot n\,dA\right|
\]

in general.

Interior sign alternation may make the total variation arbitrarily larger than the signed boundary degree unless additional oscillation control is proved.

---

## 7. Generic fold interpretation

At a generic tangency fold, two transverse roots are born or die with opposite signs of

\[
J_\xi\cdot\nabla g.
\]

Therefore their signed contributions cancel in `dnu_peak^J`, while their positive contributions add in `dmu_peak^J`.

This is exactly M17-109's positivity-versus-conservation tradeoff written as a spatial measure identity.

At the degenerate instant itself the total variation may change discontinuously under the limiting root-count description even though the signed distribution has no delta charge creation.

---

## 8. Canonical maximum measure

A linewise amplitude maximum has

\[
\boxed{C:=D_\xi g<0.}
\]

Define the positive director-area-weighted maximum measure

\[
\boxed{
d\mu_{max}^J
:=\mathbf 1_{\{C<0\}}
\delta(g)|J_\xi\cdot\nabla g|\,dV.
}
\]

On a clean transverse maximum sheet this is exactly the tube-label measure `dPhi_J` counted once per maximum intersection.

Therefore the positive margin inventory has the spatial representation

\[
\boxed{
\mathscr N_\Omega
=
\int_\Omega
N_{R2}
\,d\mu_{max}^J
}
\]

when all retained maxima in the region are included and the finite tangency/degeneracy events are treated by the event convention of M17-109.

---

## 9. What this gains

M17-106 showed that there is no source-free positive **volume carrier density** on the pure-kernel branch analogous to M17-034's oblique `Q`.

The present measure is different:

\[
\boxed{
\delta(g)|J_\xi\cdot\nabla g|\,dV
}
\]

is a codimension-one critical-set measure represented in volume coordinates.

It is canonical and inherited from the director-area flux, but it is not materially conserved because its total variation changes at folds and critical-set topology events.

This is exactly the correct measure for the positive Riccati-margin burden.

---

## 10. Potential coercive route and its firewall

The spatial representation permits standard integral estimates to be attempted on

\[
\int
N_{R2}\,\mathbf 1_{\{C<0\}}
\delta(g)|J_\xi\cdot\nabla g|\,dV.
\]

However the only exact divergence identity available without absolute values is

\[
\delta(g)J_\xi\cdot\nabla g
=\nabla\cdot(H(g)J_\xi).
\]

Taking absolute value is precisely what restores positivity and destroys the cancellation.

Therefore any future coercive estimate must control the **oscillation/total variation** of the signed peak measure, not merely its boundary degree.

---

## 11. DSD analysis

The measure hierarchy is now explicit:

\[
\boxed{
\text{frozen tube flux }d\Phi_J
\leftrightarrow
\text{signed spatial peak measure }d\nu_{peak}^J
\to
\text{positive total variation }d\mu_{peak}^J.
}
\]

The first two retain orientation cancellation.
The last is the one needed for positive Riccati control.

This identifies the exact mathematical location where coercivity is lost.

---

## 12. DSD audit

### Audit A — calling `dmu_peak^J` a volume carrier density
Rejected. It is a codimension-one critical-set measure written using a delta distribution.

### Audit B — using the signed boundary degree to bound positive peak mass
Rejected without an oscillation theorem.

### Audit C — ignoring degenerate zeros in the delta formula
Avoided by restricting the simple-root formula to transverse sheets and using the distributional divergence identity / event limits at finite degeneracies.

### Audit D — treating total variation as conserved
Rejected. Generic folds change it.

### Audit E — proof status
A canonical spatial measure for the positive peak-margin burden is obtained, but no total-variation coercive estimate is yet available.

---

## 13. Updated Rank-2 coercivity frontier

The Rank-2 positive-margin quantity can now be written intrinsically as

\[
\boxed{
\mathscr N_\Omega
=
\int_\Omega
N_{R2}
\mathbf 1_{\{C<0\}}
\delta(g)|J_\xi\cdot\nabla g|\,dV.
}
\]

Its signed carrier skeleton is the divergence measure

\[
\boxed{
\nabla\cdot(H(g)J_\xi).
}
\]

Therefore the next possible coercive gate is an **oscillation/total-variation bound** for the director-area-weighted sign changes of `g` along kernel tubes.

Without such a bound, the positive margin inventory can be replenished by fold-generated total variation while the signed director-area degree remains fixed.

This is the **Director-Area Peak Oscillation Gate (DAPOG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
