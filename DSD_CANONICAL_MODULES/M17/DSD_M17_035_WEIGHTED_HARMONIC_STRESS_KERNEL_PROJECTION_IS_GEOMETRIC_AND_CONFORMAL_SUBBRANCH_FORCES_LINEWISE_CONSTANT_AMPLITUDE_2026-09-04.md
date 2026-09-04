# DSD M17-035 — Weighted-harmonic stress kernel projection is geometric; the conformal subbranch forces linewise constant amplitude

Date: 2026-09-04
Canonical ID: **M17-035**

Status: **INTERNAL WEIGHTED-HARMONIC RESONANT-FRAME AUDIT / FOR THE PURE-TRANSVERSE-KERNEL RANK-TWO CLASS, THE WEIGHTED HARMONIC-DIRECTOR EQUATION HAS STRESS TENSOR `S=rho^2(dxi^T dxi-|dxi|^2 I/2)` WITH `div S=-(|dxi|^2/2)grad(rho^2)`. BECAUSE THE KERNEL DIRECTION `k` IS A ZERO EIGENVECTOR OF `dxi`, THE `k` PROJECTION CANCELS THE WEIGHT GRADIENT EXACTLY AND REDUCES TO THE PURE GEOMETRIC IDENTITY `D_k E+2 G:grad k=0`; IT DOES NOT PRODUCE A NEW SIGN CONTRADICTION. HOWEVER, ON THE HORIZONTALLY CONFORMAL SUBBRANCH WHERE THE TWO NONZERO JETS `b=(xi·grad)xi` AND `a=(n·grad)xi` ARE ORTHOGONAL WITH EQUAL MAGNITUDE, THE STRESS COLLAPSES TO A SINGLE NEGATIVE KERNEL PRESSURE `S=-rho^2 lambda^2 k⊗k`. THE TRANSVERSE STRESS BALANCE THEN FORCES THE KERNEL-FIBER CURVATURE TO EQUAL THE TRANSVERSE GRADIENT OF `log rho^2`; BECAUSE THE KERNEL FIBER LIES IN THE PLANE NORMAL TO THE CONSTANT DIRECTOR ALONG THAT FIBER, ITS CURVATURE HAS NO `xi` COMPONENT, AND CONSEQUENTLY `(xi·grad)rho=0`. DIVERGENCE-FREE VORTICITY THEN GIVES `div xi=0`. THE CONFORMAL SURVIVOR IS THEREFORE MUCH MORE RIGID BUT NOT YET CONTRADICTORY; THE ANISOTROPIC PURE-KERNEL BRANCH REMAINS OPEN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Weighted harmonic-director stress tensor

Write

\[
w:=\rho^2
\]

and

\[
E:=|\nabla\xi|^2.
\]

The weighted harmonic-director equation is

\[
\boxed{
\nabla\cdot(w\nabla\xi)
+wE\xi=0.
}
\]

Define the symmetric stress tensor

\[
\boxed{
S_{ij}
:=w\left(
\partial_i\xi\cdot\partial_j\xi
-\frac12E\delta_{ij}
\right).
}
\]

A direct differentiation using `xi·partial_j xi=0` gives

\[
\boxed{
\partial_iS_{ij}
=-\frac12E\,\partial_jw.
}
\]

Thus the nonconstant weight appears as an explicit stress forcing.

---

## 2. Pure-transverse-kernel frame

Use the M17-033 frame

\[
(\xi,k,n),
\qquad
n=\xi\times k,
\]

with

\[
(k\cdot\nabla)\xi=0.
\]

Define

\[
b=(\xi\cdot\nabla)\xi,
\qquad
a=(n\cdot\nabla)\xi.
\]

Then

\[
E=|b|^2+|a|^2.
\]

Let the pullback metric tensor be

\[
G_{ij}:=\partial_i\xi\cdot\partial_j\xi.
\]

Since the `k` derivative vanishes,

\[
\boxed{Gk=0.}
\]

Therefore

\[
\boxed{
Sk=-\frac12wE\,k.
}
\]

---

## 3. Kernel projection of stress divergence

Project

\[
\operatorname{div}S
=-\frac12E\nabla w
\]

onto `k`.

Using symmetry of `S`,

\[
\operatorname{div}(Sk)
=(\operatorname{div}S)\cdot k
+S:\nabla k.
\]

Since

\[
Sk=-\frac12wE\,k,
\]

we obtain

\[
-\frac12D_k(wE)
-\frac12wE\operatorname{div}k
-S:\nabla k
=-\frac12E D_kw.
\]

The `D_k w` terms cancel exactly.
After dividing by `w`,

\[
D_kE
+E\operatorname{div}k
+2\left(G-\frac12EI\right):\nabla k=0.
\]

The trace term cancels the `E div k` term, leaving

\[
\boxed{
D_kE+2G:\nabla k=0.
}
\]

Thus the kernel projection is independent of the weight `rho^2`.

---

## 4. The kernel projection is a geometric integrability identity

Write

\[
b=p\,k+q\,n,
\qquad
a=r\,k+s\,n.
\]

Let the frame connection coefficients be

\[
D_\xi k=-p\xi+\omega_\xi n,
\]

\[
D_nk=-r\xi+\omega_n n.
\]

Then

\[
G:\nabla k
=-p|b|^2
+(b\cdot a)(\omega_\xi-r)
+\omega_n|a|^2.
\]

Hence

\[
\boxed{
D_kE
=2p|b|^2
-2(b\cdot a)(\omega_\xi-r)
-2\omega_n|a|^2.
}
\]

But the kernel condition itself implies, by commuting directional derivatives,

\[
\boxed{
D_kb
=p\,b-\omega_\xi a,
}
\]

and

\[
\boxed{
D_ka
=r\,b-\omega_n a.
}
\]

Differentiating

\[
E=|b|^2+|a|^2
\]

with these two identities reproduces the same formula exactly.

Therefore the `k`-projected weighted harmonic stress equation supplies **no independent closure condition** beyond geometric integrability.

This is a DSD audit result: the tempting weighted sign channel vanishes in the kernel projection.

---

## 5. Conformal versus anisotropic horizontal differential

The two nonzero columns define a `2 x 2` metric on the quotient directions `(xi,n)`.
Define the conformal defect

\[
\boxed{
\mathcal D
:=E^2-4|J_\xi|^2.
}
\]

Using

\[
|J_\xi|=|\xi\cdot(a\times b)|,
\]

we have

\[
\boxed{
\mathcal D
=(|b|^2-|a|^2)^2
+4(b\cdot a)^2
\ge0.
}
\]

Thus

### conformal subbranch

\[
\boxed{
\mathcal D=0
\iff
|a|=|b|=:\lambda,
\quad
a\cdot b=0;
}
\]

### anisotropic subbranch

\[
\boxed{
\mathcal D>0.
}
\]

---

## 6. Stress collapse on the conformal subbranch

When

\[
|a|=|b|=\lambda,
\qquad
a\cdot b=0,
\]

we have

\[
E=2\lambda^2.
\]

The pullback metric is `lambda^2` on the two quotient directions and zero on the kernel direction.
Therefore the stress tensor simplifies to

\[
\boxed{
S=-w\lambda^2\,k\otimes k.
}
\]

All stress components transverse to the kernel pressure vanish.

---

## 7. Conformal weighted-harmonic balance

The stress equation becomes

\[
-\operatorname{div}(w\lambda^2 k\otimes k)
=-\lambda^2\nabla w.
\]

Equivalently,

\[
\operatorname{div}(w\lambda^2 k\otimes k)
=\lambda^2\nabla w.
\]

Project perpendicular to `k`.
The derivative of the scalar coefficient contributes only in the `k` direction, leaving

\[
\boxed{
(k\cdot\nabla)k
=P_{k^\perp}\nabla\log w.
}
\]

Since

\[
w=\rho^2,
\]

this is

\[
\boxed{
(k\cdot\nabla)k
=2P_{k^\perp}\nabla\log\rho.
}
\]

Thus the kernel fibers bend exactly in response to the transverse vorticity-amplitude gradient.

---

## 8. Kernel fibers lie in planes normal to xi

Along a kernel integral curve,

\[
\frac{dx}{ds}=k.
\]

Because

\[
(k\cdot\nabla)\xi=0,
\]

the director `xi` is constant along that curve.
Also

\[
k\cdot\xi=0.
\]

Hence the entire kernel curve lies in an affine plane orthogonal to its constant director `xi`.

Therefore its curvature vector

\[
(k\cdot\nabla)k
\]

also lies in that plane and has no `xi` component:

\[
\boxed{
\xi\cdot(k\cdot\nabla)k=0.
}
\]

---

## 9. Vorticity amplitude is constant along the vortex direction

Take the `xi` component of

\[
(k\cdot\nabla)k
=P_{k^\perp}\nabla\log w.
\]

The left side has zero `xi` component, so

\[
\boxed{
\xi\cdot\nabla\log w=0.
}
\]

Therefore

\[
\boxed{
(\xi\cdot\nabla)\rho=0.
}
\]

On the conformal pure-kernel rank-two subbranch, the vorticity magnitude is exactly constant along each vortex-direction integral curve.

---

## 10. Divergence-free vorticity forces div xi = 0

Since

\[
W=\rho\xi
\]

and

\[
\nabla\cdot W=0,
\]

we have

\[
(\xi\cdot\nabla)\rho
+\rho\nabla\cdot\xi=0.
\]

Using

\[
(\xi\cdot\nabla)\rho=0
\]

and `rho>0` gives

\[
\boxed{
\nabla\cdot\xi=0.
}
\]

In the canonical frame,

\[
\nabla\cdot\xi=n\cdot a=s.
\]

Hence

\[
\boxed{s=0.}
\]

Thus

\[
a\parallel k.
\]

Since `a` is orthogonal to `b` and the two have equal norm, it follows that

\[
\boxed{
b\parallel n,
\qquad
|a|=|b|.
}
\]

The conformal frame therefore sharpens to the canonical cross-coupled form

\[
\boxed{
D_k\xi=0,
\qquad
D_\xi\xi=\lambda_1 n,
\qquad
D_n\xi=\lambda_2 k,
\qquad
|\lambda_1|=|\lambda_2|.
}
\]

---

## 11. Material compatibility of persistent conformality

M17-033 gives

\[
D_B\log|b|
=-\sigma-\frac12,
\]

and

\[
D_B\log|a|
=-\sigma_n-\frac12.
\]

If the equality

\[
|a|=|b|
\]

persists materially, then

\[
\boxed{
\sigma_n=\sigma
}
\]

pointwise on the persistent conformal branch.

Trace-free strain then gives

\[
\boxed{
\sigma_k=-2\sigma.
}
\]

This is stronger than the mean resonant frame of M17-033.

---

## 12. What remains open

The conformal pure-kernel survivor must simultaneously satisfy

\[
\boxed{
\begin{aligned}
D_k\xi&=0,\\
D_\xi\xi&=\lambda n,\\
D_n\xi&=\pm\lambda k,\\
D_\xi\rho&=0,\\
\nabla\cdot\xi&=0,\\
(k\cdot\nabla)k&=2P_{k^\perp}\nabla\log\rho,\\
\sigma_n&=\sigma,\\
\sigma_k&=-2\sigma.
\end{aligned}
}
\]

No contradiction has yet been derived from this closed geometric subsystem.

The anisotropic class `D>0` remains less rigid because its stress has nonzero shear components.

---

## 13. DSD analysis

The weighted harmonic equation behaves differently depending on the descriptor projection:

- kernel projection: weight cancels and gives only geometric integrability;
- conformal stress projection: anisotropic stress disappears, exposing the vorticity-amplitude gradient directly.

Thus the useful information appears only after the conformal/anisotropic structural split.

---

## 14. DSD audit

### Audit A — claiming the kernel projection proves a new PDE restriction
Rejected. It is identical to the derivative consequence of the kernel condition.

### Audit B — importing unweighted harmonic-map geodesic-fiber theory
Avoided. The weight produces the explicit `grad log rho` fiber-curvature term.

### Audit C — claiming conformality itself is contradictory
Rejected. It yields a sharply constrained subsystem but no sign contradiction yet.

### Audit D — assuming a and b are pointwise strain eigenvectors
Not used.

### Audit E — proof status
The conformal survivor is classified further; the anisotropic pure-kernel branch remains open.

---

## 15. Updated PTKG frontier

The exceptional intrinsic Rank-2 class is now

\[
\boxed{
R_{2,j=0}^{pure-kernel}
\Longrightarrow
R_{conf}^{pure-kernel}
\ \lor\ 
R_{aniso}^{pure-kernel}.
}
\]

The conformal branch obeys the linewise-amplitude and divergence-free-director constraints above.
The anisotropic branch retains a nonzero stress shear tensor.

---

## 16. Next target

For the conformal branch, the next calculation should apply the flat Euclidean connection identities to the canonical frame

\[
D_k\xi=0,
\quad
D_\xi\xi=\lambda n,
\quad
D_n\xi=\pm\lambda k
\]

and test whether a nonzero smooth `lambda` can exist globally with `div xi=0` and finite energy.

For the anisotropic branch, the natural object is the conformal defect

\[
\mathcal D=E^2-4|J_\xi|^2
\]

and its material/spatial transport.

The conformal connection route is cleaner and is taken next.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
