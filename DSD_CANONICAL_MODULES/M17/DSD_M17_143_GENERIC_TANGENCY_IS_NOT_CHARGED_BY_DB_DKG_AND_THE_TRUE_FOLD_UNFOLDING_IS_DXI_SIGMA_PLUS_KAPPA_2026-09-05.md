# DSD M17-143 — Generic tangency is not charged by `D_B(D_k g)`; the true fold unfolding is `D_xi(sigma+kappa)`

Date: 2026-09-05  
Canonical ID: **M17-143**

Status: **TRANSITION-COST AUDIT / M17-142 FORCES ALMOST-ALL REMOTE COMPACT-RIBBON CARRIERS, ON A QUIET CRITICAL SPACETIME BLOCK, TO LEAVE THE COMPACT BOUNDED-`J_xi` RIBBON CLASS WITHIN UNIFORMLY BOUNDED LOG-RADIUS DISTANCE. A NATURAL NEXT ATTEMPT IS TO CHARGE EACH PHYSICAL TYPE TRANSITION BY THE MATERIAL VARIATION OF `a:=D_k g`. THIS MODULE SHOWS THAT THIS IS NOT VALID FOR THE GENERIC DIRECTOR-AREA/PEAK FOLD. THE EXACT COMMUTATOR GIVES `D_B a=D_kD_xi(sigma+kappa)-(D_k sigma)g-(sigma+sigma_k+1)a`, SO AT A TANGENCY `g=a=0`, `D_B a=D_kD_xi(sigma+kappa)`. HOWEVER, THE GENERIC FOLD NORMAL FORM `g=A_T tau+(1/2)C_k eta^2+...` CAN HAVE `D_B a=0` AT THE CONTACT WHILE STILL CREATING/DESTROYING TWO TRANSVERSE INTERSECTIONS. THE TRUE FIRST TIME-UNFOLDING COEFFICIENT IS `A_T=D_B g=D_xi(sigma+kappa)`, WITH `C_k=D_k^2g` THE SPATIAL CURVATURE COEFFICIENT. THEREFORE A POSITIVE `L^2` COST FOR `D_B a` CANNOT BE USED TO EXCLUDE GENERIC FOLD TURNOVER. THE FOLD REMAINS A ZERO-NET-SIGNED-DIRECTOR-FLUX GEOMETRY-TRANSITION FIREWALL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Starting point from M17-142

On the quiet critical spacetime branch, M17-142 gives

\[
\boxed{
R_{2,\rm ribbon}^{remote}
\Longrightarrow
G_{\rm frequent}^{almost\ all\ flux}
}
\]

except for a vanishing director-flux/volume fraction, unless the critical spacetime shell bound fails.

The next task is not to prove that a chart label changes. One must identify a **physical discriminant** and then determine whether crossing it carries a cost controlled by an already available Navier--Stokes budget.

On the transverse peak-sheet branch the first physical discriminant is

\[
\boxed{a:=D_k g=0},
\qquad
\boxed{g:=D_\xi\log\rho}.
\]

M17-099 identifies this as the kernel/vortex curvature resonance

\[
D_k g=0
\iff
\gamma_k=q.
\]

---

## 2. Exact material commutator along `k`

M17-097 gives the frozen director-area Cauchy law

\[
D_BJ_\xi=(\nabla B)J_\xi-\frac32J_\xi,
\qquad
J_\xi=|J_\xi|k.
\]

Resolving magnitude and direction gives

\[
D_B\log|J_\xi|=\sigma_k-1
\]

and, equivalently to M17-115,

\[
D_Bk=\Omega n.
\]

For any scalar `f`,

\[
\boxed{
D_B(D_kf)
=
D_k(D_Bf)
-\left(\sigma_k+\frac12\right)D_kf.
}
\]

This formula already includes the rotation of the material `k` frame; there is no omitted `D_Bk` term.

---

## 3. Exact material law for `a=D_k g`

M17-040/M17-097 give

\[
\boxed{
D_Bg
=
D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g.
}
\]

Set

\[
S:=\sigma+\kappa.
\]

Then

\[
\begin{aligned}
D_Ba
&=D_B(D_kg)\\
&=D_k(D_Bg)
-\left(\sigma_k+\frac12\right)a\\
&=D_kD_\xi S
-D_k\left[\left(\sigma+\frac12\right)g\right]
-\left(\sigma_k+\frac12\right)a.
\end{aligned}
\]

Therefore

\[
\boxed{
D_Ba
=
D_kD_\xi(\sigma+\kappa)
-(D_k\sigma)g
-(\sigma+\sigma_k+1)a.
}
\]

On a peak `g=0`,

\[
\boxed{
D_Ba
=
D_kD_\xi(\sigma+\kappa)
-(\sigma+\sigma_k+1)a.
}
\]

At a tangency `g=a=0`,

\[
\boxed{
D_Ba
=
D_kD_\xi(\sigma+\kappa).
}
\]

This identity is exact.

---

## 4. Why this does **not** produce the desired transition cost

The director-area tangency is not a material zero of the scalar `a` that must be followed continuously through a sign change on one surviving peak branch.

M17-099 restricts the peak equation to one frozen director-area tube and gives, near a quadratic tangency,

\[
\boxed{
\mathfrak g(\eta,\tau)
=
A_T\tau
+\frac12C_k\eta^2
+\text{higher order},
}
\]

with

\[
\boxed{
A_T=D_Bg=D_\xi(\sigma+\kappa),
}
\]

and

\[
\boxed{
C_k=D_k^2g.
}
\]

The generic fold conditions are

\[
\boxed{A_T\neq0,\qquad C_k\neq0.}
\]

The two transverse intersections satisfy to leading order

\[
\eta_\pm(\tau)
=\pm\sqrt{-\frac{2A_T}{C_k}\tau}
\]

on the side where the square root is real.

At those intersections,

\[
a_\pm
=D_kg
\sim
C_k\eta_\pm
=
\pm\sqrt{-2A_TC_k\tau}.
\]

The two branches terminate at the fold rather than forming one material `a`-trajectory that crosses smoothly through zero.

---

## 5. Explicit counterexample to a `D_B a`-cost theorem

Take the exact local normal form

\[
\boxed{
\mathfrak g(\eta,\tau)=\tau+\eta^2.
}
\]

Then

\[
A_T=1,
\qquad
C_k=2,
\]

so this is a nondegenerate generic fold.

But

\[
a=\partial_\eta\mathfrak g=2\eta,
\]

and at the contact point `(eta,tau)=(0,0)`,

\[
\boxed{
\partial_\tau a=0.
}
\]

Thus a generic fold can occur with

\[
\boxed{D_B(D_kg)=0}
\]

at the contact.

Therefore no theorem of the form

\[
\text{generic fold}
\Longrightarrow
\int|D_B(D_kg)|^2\,d\theta\ge c_*>0
\]

can hold on the basis of fold topology alone.

This invalidates the proposed direct `D_Ba` transition-charge route.

---

## 6. The correct local transition data

For the generic director-area/peak fold the physically relevant low-order data are

\[
\boxed{
(g,a;A_T,C_k)
=
\left(
0,0;
D_\xi(\sigma+\kappa),
D_k^2g
\right).
}
\]

The roles are different:

- `g=0` places the point on the peak sheet;
- `a=D_kg=0` gives tangency to the director-area tube;
- `A_T=D_Bg` unfolds the tangency in material time;
- `C_k=D_k^2g` gives the quadratic spatial curvature of the restricted zero set.

A cost theorem must therefore control `A_T`, `C_k`, or a higher finite jet when one of these vanishes. Charging only `D_Ba` misses the generic event.

---

## 7. Signed flux remains neutral at the generic fold

M17-099 already proves that the two transverse intersections born or destroyed at the fold have opposite signs of `D_kg`.

Hence the positive intersection population changes, while the net signed director-area intersection flux is zero.

Schematically,

\[
\boxed{
(+d\Phi_J)+(-d\Phi_J)=0.
}
\]

Therefore the inherited signed Cauchy flux does not penalize repeated generic pair turnover.

This is exactly why the M17-142 geometry-transition branch cannot be closed by signed flux conservation alone.

---

## 8. Physical discriminant versus chart discriminant

A pure coordinate-chart change between two descriptions of the same nondegenerate state carries no physical content and must be quotiented out.

The condition

\[
D_kg=0
\]

is different: it is a genuine loss of transversality between the peak sheet and the frozen director-area current.

However,

\[
\boxed{
\text{genuine physical discriminant}
\not\Rightarrow
\text{positive energetic cost}.
}
\]

M17-143 makes this distinction explicit.

---

## 9. Consequence for the M17-142 frontier

The M17-142 implication should now be refined as

\[
\boxed{
R_{2,\rm ribbon}^{remote}
\Longrightarrow
H_{1,crit}^{spacetime}
\ \lor
G_{\rm fold/type}^{almost\ all\ flux},
}
\]

where the quiet branch may be serviced by smooth finite-jet events such as

\[
\boxed{
\begin{aligned}
&D_kg=0\text{ generic fold/tangency},\\
&g\equiv0\text{ ribbon entry/exit},\\
&C_k=D_k^2g=0\text{ higher-order tangency},\\
&\text{top-jet/rank/endpoint/interface degeneracy}.
\end{aligned}
}
\]

The first of these is not eliminated by an `L^2` cost for `D_Ba`.

---

## 10. DSD audit

### Audit A — `D_k g=0` is only a bad chart

Rejected.
It is a genuine geometric tangency of the peak sheet and the frozen director-area current.

### Audit B — every genuine tangency forces positive `D_B(D_k g)`

Rejected by the normal form `g=tau+eta^2`.

### Audit C — a hard-cell variation bound on `a` can be integrated through the fold on one peak genealogy

Rejected.
The two transverse peak branches terminate at the fold; there is no single surviving peak-intersection genealogy across the event.

### Audit D — signed director-area flux forbids pair birth/death

Rejected.
The pair carries opposite signed intersection flux and has zero net signed charge.

### Audit E — the generic fold is therefore known to be dynamically realizable in full Navier--Stokes

Not established.
The result is only that the previously proposed `D_Ba`/signed-flux obstruction does not exclude it. Full coupled dynamics may still obstruct the event.

---

## 11. Highest-value next gate

The correct time-unfolding scalar is

\[
\boxed{A_T=D_\xi(\sigma+\kappa).}
\]

On the M17-142 quiet remote branch, ordinary strain is already small in an averaged spacetime sense. Under the retained compact finite-jet hypotheses, the next efficient calculation is therefore to determine whether the strain-gradient part of `A_T` also decays, leaving

\[
A_T\sim D_\xi\kappa.
\]

If so, dominant smooth fold turnover must be paid by a **scale-free CE-H multiplier-gradient mechanism**, not by ordinary strain recharge.

That is the next module.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
