# DSD M17-040 — Orthogonal-stretch line extrema have an exact material-relative velocity and a cross-aligned jet frame

Date: 2026-09-04
Canonical ID: **M17-040**

Status: **INTERNAL OSCILLATORY-TAIL CRITICAL-POINT DYNAMICS / ON THE ORTHOGONAL PURE-KERNEL BRANCH, `D_xi d=-E D_xi log rho`, SO LINEWISE CRITICAL POINTS OF VORTICITY AMPLITUDE AND SIGNED STRETCH DEFECT COINCIDE EXACTLY. WRITING `g=D_xi log rho=-div xi`, COMMUTING `D_B` WITH THE MATERIALLY FROZEN DIRECTION `xi` GIVES `D_B g=D_xi(sigma+kappa)-(sigma+1/2)g`. THEREFORE A NONDEGENERATE LINEWISE EXTREMUM `g=0`, `D_xi g!=0` MOVES RELATIVE TO THE MATERIAL VORTEX LABEL WITH EXACT SIGNED SPEED `v_rel=-D_xi(sigma+kappa)/(D_xi g)`. A MATERIAL-STATIONARY EXTREMUM REQUIRES `D_xi(sigma+kappa)=0`. AT EVERY SUCH CRITICAL POINT, `div xi=0` FORCES THE `n` COMPONENT OF `a=(n·grad)xi` TO VANISH; ORTHOGONALITY `a·b=0` THEN FORCES THE `k` COMPONENT OF `b=(xi·grad)xi` TO VANISH. HENCE `a` IS PARALLEL TO `k` AND `b` IS PARALLEL TO `n`, SO THE CRITICAL JET FRAME HAS THE SAME CROSS-ALIGNED FORM AS THE CONFORMAL CLASS BUT WITH UNEQUAL MAGNITUDES. OSCILLATORY TAILS MUST THEREFORE BE BUILT FROM A MOVING NETWORK OF CROSS-ALIGNED CRITICAL JETS RATHER THAN ARBITRARY AMPLITUDE OSCILLATIONS. THIS IS A KINEMATIC CLASSIFICATION, NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Coincidence of amplitude and stretch critical points

M17-038 gives

\[
D_\xi d=-E D_\xi\log\rho,
\qquad E>0.
\]

Therefore

\[
\boxed{
D_\xi d=0
\iff
D_\xi\rho=0
}
\]

on the active branch.

Define

\[
\boxed{
g:=D_\xi\log\rho.}
\]

Then

\[
\boxed{g=-\nabla\cdot\xi}
\]

by `div(rho xi)=0`.

Thus the common line-critical set is

\[
\boxed{g=0.}
\]

---

## 2. Material commutator with D_xi

Because

\[
D_B\xi=0,
\]

for any scalar `f`,

\[
D_B(D_\xi f)
=D_\xi(D_B f)
-\big((\xi\cdot\nabla)B\big)\cdot\nabla f.
\]

CE-H gives

\[
(\xi\cdot\nabla)B
=\left(\sigma+\frac12\right)\xi.
\]

Hence

\[
\boxed{
D_B(D_\xi f)
=D_\xi(D_Bf)
-\left(\sigma+\frac12\right)D_\xi f.
}
\]

---

## 3. Exact evolution of the line-amplitude derivative

Use

\[
D_B\log\rho
=\sigma+\kappa-1.
\]

With `f=log rho`, Section 2 gives

\[
\boxed{
D_Bg
=D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g.
}
\]

At a linewise critical point `g=0`,

\[
\boxed{
D_Bg
=D_\xi(\sigma+\kappa).
}
\]

Thus a material label located at a critical point remains critical instantaneously only if

\[
\boxed{
D_\xi(\sigma+\kappa)=0.
}
\]

---

## 4. Material-relative velocity of a nondegenerate extremum

Assume

\[
g=0,
\qquad
D_\xi g\ne0.
\]

Let the critical point move relative to the material flow by signed line speed `v_rel` in the `xi` direction.
The derivative along the moving critical point is

\[
D_Bg+v_{rel}D_\xi g=0.
\]

Therefore

\[
\boxed{
 v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{D_\xi g}.
}
\]

This is the exact analogue, on a vortex line, of the zero-level relative-velocity formulas used earlier for `kappa` and `chi` surfaces.

---

## 5. The same velocity moves stretch extrema

Since

\[
D_\xi d=-Eg,
\]

at `g=0`,

\[
D_\xi^2d=-E D_\xi g.
\]

Also

\[
D_B(D_\xi d)
=-E D_\xi(\sigma+\kappa)
\]

at the critical point, because all terms proportional to `g` vanish.

Thus the relative velocity obtained from the `d` critical equation is

\[
-\frac{D_B(D_\xi d)}{D_\xi^2d}
=-\frac{D_\xi(\sigma+\kappa)}{D_\xi g},
\]

exactly the same `v_rel`.

Hence amplitude and stretch extrema are one moving critical network, not two merely coincident point sets.

---

## 6. Canonical jet alignment at every common critical point

Use the M17-038 frame components

\[
b=p\,k+q\,n,
\]

\[
a=r\,k+t\,n.
\]

There

\[
\nabla\cdot\xi=t.
\]

At a line-amplitude critical point,

\[
g=0
\]

so

\[
\boxed{t=0.}
\]

Thus

\[
\boxed{a=rk.}
\]

Full rank two gives `a!=0`, so

\[
r\ne0.
\]

The orthogonal-stretch condition is

\[
a\cdot b=0.
\]

Therefore

\[
r p=0.
\]

Since `r!=0`,

\[
\boxed{p=0.}
\]

Hence

\[
\boxed{b=qn.}
\]

Full rank two also gives `q!=0`.

Thus every common critical point has the cross-aligned form

\[
\boxed{
D_k\xi=0,
\qquad
D_\xi\xi=q\,n,
\qquad
D_n\xi=r\,k,
}
\]

with

\[
|q|\ne|r|
\]

on the strictly anisotropic branch.

---

## 7. Relation to the closed conformal class

M17-035/M17-036 obtained exactly the same cross-aligned domain/target pattern on the conformal class, but with equal magnitudes

\[
|q|=|r|.
\]

Thus a critical point in the orthogonal anisotropic branch differs from the conformal geometry by **one signed stretch scalar only**:

\[
\boxed{
d=\frac{q^2-r^2}{2}.}
\]

This makes common critical points the natural interface locations for a possible approach to or crossing of the conformal class.

However, equality at one point does not invoke the M17-036 complete conformal contradiction, which requires persistence of the conformal structure on a component.

---

## 8. Maxima and minima

At a nondegenerate critical point,

\[
D_\xi g
=D_\xi^2\log\rho.
\]

Therefore

- linewise amplitude maximum: `D_xi g<0`;
- linewise amplitude minimum: `D_xi g>0`.

The signed drift law becomes

\[
\boxed{
 v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{D_\xi^2\log\rho}.
}
\]

Thus the sign of `D_xi(sigma+kappa)` determines whether each maximum/minimum moves forward or backward through the material vortex labels.

---

## 9. Oscillatory-tail consequence

A line tail that avoids eventual monotonicity by infinitely many alternating extrema must therefore carry an infinite sequence of cross-aligned rank-two jet events.

At each nondegenerate event the motion is controlled by the same local descriptor set

\[
\boxed{
(q,r,
D_\xi^2\log\rho,
D_\xi(\sigma+\kappa)).
}
\]

This removes the freedom to regard oscillatory tails as arbitrary scalar wiggles.
They are a geometrically coherent moving critical network.

---

## 10. Degenerate critical events

If

\[
g=0,
\qquad
D_\xi g=0,
\]

then the relative-velocity formula loses regularity.

Such an event is a linewise critical-point merger/splitting or higher-order flattening event.
It is the one-dimensional analogue of the finite-jet zero-set degenerations already isolated in M17-009 and M17-021.

No uniform finite-order theorem for this line-critical hierarchy is claimed here without an additional compactness argument adapted to the active tail.

---

## 11. DSD analysis

The scalar amplitude descriptor and the geometric stretch descriptor have now merged at the derivative level:

\[
D_\xi\rho=0
\iff
D_\xi d=0.
\]

At that merged event, a third descriptor—director-jet orientation—collapses to the cross-aligned canonical frame.

Thus a line extremum is simultaneously an amplitude, stretch, and frame-geometry event.

---

## 12. DSD audit

### Audit A — treating critical points as material labels
Rejected. Their exact material-relative speed is generally nonzero.

### Audit B — claiming every critical point is conformal
Rejected. Cross alignment is forced, but the magnitudes `|q|` and `|r|` may be unequal.

### Audit C — claiming infinitely many extrema imply singularity
Rejected. Nondegenerate extrema may move smoothly; only degeneracies require a separate audit.

### Audit D — importing M17-009 finite-jet bound automatically
Rejected. M17-009 concerns nodal zeros of the analytic vorticity field, not this directional critical hierarchy on a potentially remote tail.

### Audit E — proof status
The oscillatory-tail branch is classified but remains open.

---

## 13. Updated oscillatory-tail frontier

\[
\boxed{
R_{osc-tail}^{stretch}
\Longrightarrow
R_{crit}^{nondegenerate-cross-aligned}
\ \lor\ 
T_{crit}^{degenerate}.
}
\]

The nondegenerate branch is governed by the exact relative velocity above.
The degenerate branch requires a separate finite-jet/compactness audit.

---

## 14. Next target

At a cross-aligned nondegenerate critical point, the moving frame has exactly the same algebraic pattern as the M17-036 conformal frame but with unequal magnitudes `q` and `r`.

The next high-value calculation is to impose Euclidean flatness at this unequal-stretch critical frame and determine whether the ratio `|r/q|` can remain away from one along a recurrent critical network, or whether the flatness equations drive it toward the closed conformal Riccati geometry or a degenerate critical event.

This is the **Cross-Aligned Unequal-Stretch Flatness Gate (CUSFG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
