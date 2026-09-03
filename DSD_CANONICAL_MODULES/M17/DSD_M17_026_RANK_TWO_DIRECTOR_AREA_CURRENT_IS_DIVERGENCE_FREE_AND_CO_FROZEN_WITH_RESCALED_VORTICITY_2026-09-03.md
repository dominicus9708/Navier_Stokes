# DSD M17-026 — The rank-two director-area current is divergence-free and co-frozen with rescaled vorticity

Date: 2026-09-03
Canonical ID: **M17-026**

Status: **INTERNAL RANK-TWO CANONICAL CURRENT / THE PULLBACK OF THE `S^2` AREA FORM HAS THE HODGE-DUAL DIRECTOR-AREA CURRENT `J_xi^i = 1/2 epsilon^{ijk} xi dot(partial_j xi cross partial_k xi)`. IT IS IDENTICALLY DIVERGENCE-FREE, LIES IN THE KERNEL OF `d xi`, AND ITS COMPONENT ALONG `xi` IS EXACTLY THE EULERIAN TRANSVERSE DIRECTOR-AREA DENSITY `j_xi` OF M16-025. BECAUSE `D_B xi=0`, THE PULLBACK 2-FORM IS LIE-ADVECTED AND `J_xi` OBEYS THE FROZEN-IN VECTOR-DENSITY LAW `D_B J_xi=(J_xi dot grad)B-(3/2)J_xi`. VORTICITY OBEYS THE SAME LAW AFTER DIVIDING BY THE MATERIAL FLUX AMPLIFICATION `a'=kappa a`: `W_tilde=W/a` SATISFIES `D_B W_tilde=(W_tilde dot grad)B-(3/2)W_tilde`. THUS RANK-TWO DIRECTOR-AREA FLUX AND RESCALED VORTICITY FLUX SHARE THE SAME CAUCHY DEFORMATION MAP. THEIR LINEAR DEPENDENCE/INDEPENDENCE IS MATERIAL INVARIANT. THIS PROVIDES THE MISSING GLOBAL FLUX DESCRIPTOR FOR RANK TWO / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pullback area 2-form of the director

Let

\[
\xi:\mathbb R^3\to S^2,
\qquad |\xi|=1.
\]

Define the pulled-back sphere area 2-form

\[
\boxed{
\omega_{ij}
:=
\xi\cdot(\partial_i\xi\times\partial_j\xi).
}
\]

On a rank-two director region this 2-form is nonzero.

Its Euclidean Hodge dual is the vector field

\[
\boxed{
(J_\xi)^k
:=
\frac12\varepsilon^{kij}\omega_{ij}
=
\frac12\varepsilon^{kij}
\xi\cdot(\partial_i\xi\times\partial_j\xi).
}
\]

We call `J_xi` the **director-area current**.

---

## 2. Divergence-free identity

The area form on `S^2` is closed.
Therefore its pullback is closed:

\[
d\omega=0.
\]

In three dimensions this is exactly

\[
\boxed{
\nabla\cdot J_\xi=0.
}
\]

This identity is geometric and does not use the Navier-Stokes dynamics.

Thus director area is naturally organized into a divergence-free flux network.

---

## 3. The current is the kernel direction of d xi

At a rank-two point,

\[
\operatorname{rank}d\xi=2.
\]

Hence the kernel of

\[
d\xi:T_x\mathbb R^3\to T_\xi S^2
\]

is one-dimensional.

The Hodge-dual construction gives

\[
\boxed{
(J_\xi\cdot\nabla)\xi=0.
}
\]

Therefore `J_xi` points along the spatial direction in which the director does not change.

At rank two,

\[
\boxed{
\ker d\xi=\operatorname{span}\{J_\xi\}.
}
\]

This gives a canonical line field that was not explicit in M16-025.

---

## 4. Recover the M16-025 transverse area density

Take two infinitesimal material vectors `v_1,v_2` perpendicular to `xi`.
Their area vector is

\[
v_1\times v_2
=A_\perp\xi
\]

up to orientation.

The pulled-back director-area charge is

\[
\mathcal J_{mat}
=\omega(v_1,v_2)
=J_\xi\cdot(v_1\times v_2).
\]

Hence

\[
\mathcal J_{mat}
=A_\perp(J_\xi\cdot\xi).
\]

M16-025 defined

\[
j_\xi=\frac{\mathcal J_{mat}}{A_\perp}.
\]

Therefore

\[
\boxed{
j_\xi=J_\xi\cdot\xi.}
\]

The old scalar density is the vorticity-direction component of the new divergence-free current.

Rank-two **transverse** director deformation means

\[
\boxed{J_\xi\cdot\xi\ne0.}
\]

---

## 5. Lie advection of the director area form

CE-H gives

\[
\boxed{D_B\xi=0.}
\]

Each component of `xi` is therefore a materially advected scalar.
For an advected scalar,

\[
(\partial_\theta+\mathcal L_B)d\xi^a
=d(D_B\xi^a)=0.
\]

The sphere area form is built algebraically from `xi` and `d xi`, so its pullback satisfies

\[
\boxed{
(\partial_\theta+\mathcal L_B)\omega=0.
}
\]

Thus the director-area 2-form is exactly Lie-advected by the similarity material velocity.

---

## 6. Frozen-in vector-density law

The Hodge-dual vector of a Lie-advected 2-form obeys the standard flux-density equation

\[
D_BJ_\xi
=(J_\xi\cdot\nabla)B
-(\nabla\cdot B)J_\xi.
\]

Since

\[
\nabla\cdot B=\frac32,
\]

we obtain

\[
\boxed{
D_BJ_\xi
=(J_\xi\cdot\nabla)B
-\frac32J_\xi.
}
\]

Equivalently,

\[
\boxed{
D_BJ_\xi
=(\nabla B)J_\xi
-\frac32J_\xi.
}
\]

---

## 7. Cauchy formula

Let

\[
y=\eta_\theta(X),
\qquad
F=D_X\eta_\theta,
\qquad
D=\det F.
\]

Since

\[
D_B\log D=\nabla\cdot B=\frac32,
\]

we have

\[
D(\theta)=D(\theta_0)e^{3(\theta-\theta_0)/2}
\]

for a normalized reference.

The frozen-in law gives the Cauchy representation

\[
\boxed{
J_\xi(\eta_\theta(X),\theta)
=\frac{F(X,\theta)J_{\xi,0}(X)}{D(X,\theta)}.
}
\]

Hence flux of `J_xi` through any material surface is conserved.

---

## 8. Recover the scalar j_xi law

Take the material derivative of

\[
j_\xi=J_\xi\cdot\xi.
\]

Since

\[
D_B\xi=0,
\]

we get

\[
D_Bj_\xi
=\left[(\nabla B)J_\xi-\frac32J_\xi\right]\cdot\xi.
\]

CE-H gives

\[
(\nabla B)^T\xi
=\left(\sigma+\frac12\right)\xi.
\]

Therefore

\[
\boxed{
D_Bj_\xi
=(\sigma-1)j_\xi.
}
\]

This exactly reproduces M16-025 and is an internal cross-audit of the current formulation.

---

## 9. Vorticity as an amplified frozen-in field

The CE-H vorticity equation can be written

\[
D_BW
=\left(\nabla U+(\kappa-1)I\right)W.
\]

Since

\[
\nabla B=\nabla U+\frac12I,
\]

we obtain

\[
\boxed{
D_BW
=(\nabla B)W
+\left(\kappa-\frac32\right)W.
}
\]

Let the material amplification factor `a` solve

\[
\boxed{
D_Ba=\kappa a,
\qquad a>0.
}
\]

Define

\[
\boxed{
\widetilde W:=\frac Wa.
}
\]

Then

\[
\boxed{
D_B\widetilde W
=(\nabla B)\widetilde W
-\frac32\widetilde W.
}
\]

This is exactly the same frozen-in vector-density equation as for `J_xi`.

---

## 10. Co-frozen Cauchy pair

Both fields satisfy

\[
D_BZ
=(\nabla B)Z-\frac32Z.
\]

Therefore

\[
\boxed{
J_\xi
=\frac{FJ_{\xi,0}}{D},
\qquad
\widetilde W
=\frac{F\widetilde W_0}{D}.
}
\]

The same invertible deformation gradient acts on both.

Consequently the dimension of their span is material invariant:

\[
\boxed{
\dim\operatorname{span}\{J_\xi,\widetilde W\}
=
\dim\operatorname{span}\{J_{\xi,0},\widetilde W_0\}.
}
\]

Since `W` and `W_tilde` have the same direction,

\[
\boxed{
J_\xi\parallel W
}

is a material-invariant property, and so is linear independence.

---

## 11. Rank-two subbranch split

The rank-two branch now splits canonically into

\[
\boxed{
R_2^{parallel}
\ \lor\ 
R_2^{oblique}.
}
\]

### Parallel kernel-current branch

\[
J_\xi\parallel W.
\]

Because `J_xi` lies in `ker d xi`,

\[
\boxed{
(\xi\cdot\nabla)\xi=0.
}
\]

Thus the director does not bend along its own vortex-line direction.

### Oblique kernel-current branch

\[
J_\xi\not\parallel W.
\]

Then the director-kernel line and the vortex direction are independent, and their two-dimensional material span is preserved by the same deformation map.

No continuous regular evolution can change between these two subbranches without losing rank, losing the transverse area component, or leaving the retained co-frozen description.

---

## 12. DSD interpretation

### 12.1 Scalar area charge to flux field
M16-025 tracked director area on one infinitesimal transverse parallelogram.
M17-026 upgrades it to a divergence-free Eulerian current carrying that charge through arbitrary material surfaces.

### 12.2 Same deformation, different amplification
Raw vorticity differs from a frozen-in flux only by the scalar kappa amplification `a`.
After removing that scalar, its geometry and the director-area current are transported identically.

### 12.3 New invariant distinction
Parallel versus oblique director kernel is not a transient geometric accident.
It is frozen into the material deformation.

---

## 13. DSD audit

### Audit A — identifying J_xi with physical vorticity
Rejected.
`J_xi` is a topological/director-area current, not the vorticity field.

### Audit B — claiming the angle between J_xi and W is Euclidean-invariant
Rejected.
A general deformation gradient changes angles.
Only linear dependence/independence and the common Cauchy representation are invariant.

### Audit C — assuming finite transverse surfaces orthogonal to xi always exist
Avoided.
The current formulation does not require global integrability of the plane field `xi^perp`.

### Audit D — treating co-frozen transport as a contradiction
Rejected.
Two frozen-in flux fields can coexist in a smooth flow.

### Audit E — proof status
Rank two remains open.

---

## 14. Updated rank-two frontier

The original branch

\[
R_2^{director-area}
\]

is now

\[
\boxed{
R_2^{parallel}
\ \lor\ 
R_2^{oblique}.
}
\]

with the common exact laws

\[
\boxed{
\nabla\cdot J_\xi=0,
\qquad
D_BJ_\xi=(\nabla B)J_\xi-\frac32J_\xi,
}
\]

and

\[
\boxed{
D_B(W/a)=(\nabla B)(W/a)-\frac32(W/a).
}
\]

---

## 15. Next target — rank-two energy/area coercivity

The weighted harmonic-director equation and the rank-two singular values give the pointwise area-energy inequality

\[
2|J_\xi|\le|\nabla\xi|^2.
\]

The next calculation is to combine this with the scalar amplitude equation and the conserved/co-frozen current to determine whether a recurrent rank-two patch forces a quantitative negative-kappa payer or geometric degeneration.

This is the **Rank-Two Area-Energy Gate (R2AEG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
