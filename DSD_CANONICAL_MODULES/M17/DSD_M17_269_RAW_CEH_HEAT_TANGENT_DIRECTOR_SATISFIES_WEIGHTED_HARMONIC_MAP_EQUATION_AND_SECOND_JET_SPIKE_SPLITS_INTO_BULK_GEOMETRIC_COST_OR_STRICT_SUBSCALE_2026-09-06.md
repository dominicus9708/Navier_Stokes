# DSD M17-269 — Raw CE-H heat-tangent director satisfies a weighted harmonic-map equation; a second-jet spike is bulk geometric cost or strict subscale

Date: 2026-09-06  
Canonical ID: **M17-269**

Status: **SECOND-JET AUDIT / M17-268 REDUCES UNBOUNDED FOLD MULTIPLICITY TO `s2 -> 0` OR A DIRECTOR SECOND-JET SPIKE. A DSD AUDIT SHOWS THAT `|D2 xi| -> infinity` MUST NOT BE IDENTIFIED DIRECTLY WITH `rho^2 |grad kappa|^2`: IN M17-145 THE DIRECTOR JETS ENTER COMMUTATORS MULTIPLIED BY MULTIPLIER/STRAIN DERIVATIVES. ON THE RAW CE-H HEAT TANGENT, HOWEVER, `V=a xi`, `Delta V=K V`, AND `partial_tau V=Delta V` GIVE AN EXACT WEIGHTED HARMONIC-MAP EQUATION FOR `xi`. INTERIOR ELLIPTIC CONTROL THEN SHOWS THAT AN `L2`-BULK SECOND-JET ESCALATION REQUIRES FIRST-JET METRIC ESCALATION, LOG-AMPLITUDE-GRADIENT ESCALATION, OR INTERFACE/NODAL FAILURE. IF THE `L-infinity` SECOND JET BLOWS UP WHILE ITS LOCAL `L2` MASS STAYS BOUNDED, THE SPIKE IS CONCENTRATED on a vanishing effective volume and is therefore a strict higher-derivative subscale, not a bulk fold currency. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Raw heat-tangent equations

Work on a connected active patch of the raw tangent from M17-250--264 where

\[
V=a\xi,
\qquad a=|V|>0,
\qquad |\xi|=1.
\]

The tangent satisfies

\[
\boxed{\partial_\tau V=\Delta V}
\]

and the inherited CE-H relation

\[
\boxed{\Delta V=K V.}
\]

Hence

\[
\boxed{\partial_\tau V=K V.}
\]

M17-260 already gives

\[
\partial_\tau\xi=0.
\]

---

## 2. Exact polar decomposition of the elliptic relation

Expand

\[
\Delta(a\xi)
=(\Delta a)\xi
+2\partial_i a\,\partial_i\xi
+a\Delta\xi.
\]

Dot with `xi`. Since

\[
\xi\cdot\partial_i\xi=0,
\qquad
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

we obtain

\[
\boxed{
\frac{\Delta a}{a}
=K+|\nabla\xi|^2.
}
\]

Project orthogonally to `xi`:

\[
\boxed{
\Delta\xi
+2\nabla\log a\cdot\nabla\xi
+|\nabla\xi|^2\xi
=0.
}
\]

Equivalently,

\[
\boxed{
a^{-2}\nabla\cdot(a^2\nabla\xi)
+|\nabla\xi|^2\xi=0.}
\]

Thus the time-frozen director is a weighted harmonic map into `S^2`.

---

## 3. Why this is the correct second-jet equation

M17-145 contains the commutator

\[
\mathcal C_\xi[f]
=-(\Delta\xi)\cdot\nabla f
-2(\partial_i\xi_j)\partial_{ij}f
+2(D_\xi\nabla\psi-D_{\nabla\psi}\xi)\cdot\nabla f,
\]

with `psi=log rho`.

Therefore a large director second jet is only one factor in the recharge law.
It does not by itself imply a large multiplier-gradient diffusion cost.

The weighted harmonic-map equation above supplies the independent elliptic relation needed to classify the director jet before coupling it back to M17-145.

---

## 4. Interior L2 elliptic estimate

Fix concentric rescaled balls

\[
B_{1/2}\Subset B_{3/4}\Subset B_1
\]

inside the active tangent patch.

Standard interior elliptic estimates give

\[
\boxed{
\|D^2\xi\|_{L^2(B_{1/2})}
\le
C\left(
\|\Delta\xi\|_{L^2(B_{3/4})}
+\|\nabla\xi\|_{L^2(B_{3/4})}
+1
\right).
}
\]

Using the weighted harmonic-map equation,

\[
|\Delta\xi|
\le
2|\nabla\log a|\,|\nabla\xi|
+|\nabla\xi|^2.
\]

Hence

\[
\boxed{
\begin{aligned}
\|D^2\xi\|_{L^2(B_{1/2})}
\le C\bigl(&
\|\nabla\log a\,\nabla\xi\|_{L^2(B_{3/4})}\\
&+\|\nabla\xi\|_{L^4(B_{3/4})}^2
+\|\nabla\xi\|_{L^2(B_{3/4})}
+1
\bigr).
\end{aligned}
}
\]

This is the bulk second-jet gate.

---

## 5. Bulk second-jet escalation

Suppose

\[
\|D^2\xi_j\|_{L^2(B_{1/2})}\to\infty.
\]

Then at least one of the following must occur:

\[
\boxed{
\|\nabla\xi_j\|_{L^4(B_{3/4})}\to\infty,
}
\]

or

\[
\boxed{
\|\nabla\log a_j\,\nabla\xi_j\|_{L^2(B_{3/4})}\to\infty,
}
\]

or the fixed active interior geometry fails through

\[
G_{nodal/amplitude\ degeneration}
\lor
G_{interface/domain}.
\]

Thus a bulk director second-jet spike is not an independent object.
It returns to first-jet metric concentration, log-amplitude coupling, or active-set failure.

---

## 6. Supremum spike with bounded L2 second-jet mass

Now suppose instead

\[
M_j:=\|D^2\xi_j\|_{L^\infty(B_{1/2})}\to\infty
\]

while

\[
\|D^2\xi_j\|_{L^2(B_{1/2})}\le C.
\]

Define the effective concentration volume

\[
\boxed{
\nu_j
:=
\frac{\|D^2\xi_j\|_{L^2(B_{1/2})}^2}{M_j^2}.
}
\]

Then

\[
\boxed{\nu_j\to0.}
\]

Its three-dimensional effective length is

\[
\boxed{
\varepsilon_j:=\nu_j^{1/3}\to0.
}
\]

On a transverse two-dimensional fold section the analogous effective area scale is

\[
\varepsilon_{j,\Sigma}
:=
\frac{\|D^2_\Sigma\xi_j\|_{L^2(\Sigma)} }{M_j}
\to0
\]

when the transverse `L2` mass remains bounded.

Thus the second-jet `L-infinity` blowup has collapsed onto a strictly smaller spatial scale.

This is exactly a higher-derivative microcarrier/subscale event.

---

## 7. Correct second-jet split

Combining Sections 5 and 6,

\[
\boxed{
G_{director\ second\text{-}jet\ spike}
\Longrightarrow
G_{director\ first\text{-}jet/metric\ concentration}
\lor
G_{log\text{-}amplitude\ coupling}
\lor
G_{strict\ higher\text{-}derivative\ subscale}
\lor
G_{nodal/interface}.
}
\]

This is the DSD-safe replacement for the unsupported shortcut

\[
D^2\xi\text{ spike}
\Rightarrow
\rho^2|\nabla\kappa|^2\text{ cost}.
\]

---

## 8. Relation to M17-268

M17-268 proves

\[
G_{fold\ multiplicity}
\Longrightarrow
G_{s_2\to0}
\lor
G_{D^2\xi\ spike}.
\]

The first branch is already rank/anisotropy degeneration.
The second now satisfies the split in Section 7.

Therefore pure fold multiplicity no longer creates a new untyped endpoint.

---

## 9. Relation to M17-145

Only after the Section-7 split should M17-145 be invoked.

If the surviving second-jet activity also has nontrivial multiplier/strain derivatives, then the explicit commutator/reformation term

\[
\mathcal F_\xi
\]

becomes a genuine recharge payer.

If those scalar derivatives are small, the director spike must instead be carried by the weighted-harmonic-map channels isolated above.

This prevents double counting director geometry and multiplier-gradient diffusion as independent costs.

---

## 10. DSD audit

- The exact raw tangent equation is used; no mean-subtracted field is assigned homogeneous CE-H.
- The unit-vector constraint is retained in the `|grad xi|^2 xi` term.
- Pointwise second-jet blowup is separated from bulk `L2` second-jet growth.
- Concentrated `L-infinity` blowup with bounded `L2` mass is recorded as a strict smaller-scale event, not as a bulk budget.
- M17-145 is used only after identifying the scalar derivative factor needed by its commutator.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
