# DSD M17-038 — Orthogonal stretch rank two has diagonal weighted stress and an exact linewise amplitude–anisotropy law

Date: 2026-09-04
Canonical ID: **M17-038**

Status: **INTERNAL ORTHOGONAL-STRETCH WEIGHTED-HARMONIC REDUCTION / ON THE PURE-KERNEL ANISOTROPIC CLASS WITH `a·b=0` BUT `|a|!=|b|`, THE PULLBACK DIRECTOR METRIC AND WEIGHTED HARMONIC STRESS ARE DIAGONAL IN THE CANONICAL DOMAIN FRAME `(xi,k,n)`. WRITING `E=|a|^2+|b|^2` AND `d=(|b|^2-|a|^2)/2`, THE STRESS EIGENVALUES ARE `rho^2(d,-E/2,-d)`. PROJECTING `div S=-(E/2)grad rho^2` ALONG THE VORTEX DIRECTION AND USING `div(rho xi)=0` GIVES THE EXACT WEIGHT-INDEPENDENT LINE LAW `D_xi d = E div xi = -E D_xi log rho`. THE KERNEL PROJECTION AGAIN REDUCES TO GEOMETRIC INTEGRABILITY; THE `n` PROJECTION GIVES A SECOND SIGNED BALANCE INVOLVING THE KERNEL-FIBER CURVATURE AND THE TRANSVERSE AMPLITUDE GRADIENT. THUS UNEQUAL STRETCH CANNOT VARY INDEPENDENTLY OF VORTICITY AMPLITUDE ALONG A VORTEX LINE, BUT NO FIXED-SIGN MONOTONICITY IS FORCED. THE ORTHOGONAL STRETCH SURVIVOR REMAINS OPEN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Orthogonal stretch branch

Work on

\[
R_{stretch}^{orthogonal}
\]

from M17-037:

\[
(k\cdot\nabla)\xi=0,
\]

\[
a=(n\cdot\nabla)\xi,
\qquad
b=(\xi\cdot\nabla)\xi,
\]

with

\[
\boxed{a\cdot b=0}
\]

and

\[
\boxed{|a|\ne|b|.}
\]

Define

\[
A:=|a|,
\qquad
B:=|b|,
\]

\[
\boxed{E:=A^2+B^2}
\]

and the signed stretch defect

\[
\boxed{d:=\frac{B^2-A^2}{2}.}
\]

The conformal interface is `d=0`.

---

## 2. Diagonal pullback metric

In the domain frame `(xi,k,n)`,

\[
D_\xi\xi=b,
\qquad
D_k\xi=0,
\qquad
D_n\xi=a.
\]

Because `a·b=0`, the pullback metric

\[
G_{ij}=D_{e_i}\xi\cdot D_{e_j}\xi
\]

is diagonal:

\[
\boxed{
G
=\operatorname{diag}(B^2,0,A^2).
}
\]

---

## 3. Diagonal weighted harmonic stress

With

\[
w=\rho^2,
\]

the weighted harmonic stress is

\[
S=w\left(G-\frac12EI\right).
\]

Therefore

\[
\boxed{
S
=w\,\operatorname{diag}
\left(
 d,
-\frac E2,
-d
\right)
}
\]

in the canonical frame.

The field equation is

\[
\boxed{
\operatorname{div}S
=-\frac E2\nabla w.
}
\]

---

## 4. Connection notation

Write the director jets in components

\[
b=p\,k+q\,n,
\]

\[
a=r\,k+t\,n.
\]

Orthogonality means

\[
pr+qt=0.
\]

The relevant frame connections are

\[
D_\xi k=-p\xi+\omega_\xi n,
\]

\[
D_k k=\gamma n,
\]

\[
D_n k=-r\xi+\omega_n n.
\]

Then

\[
D_nn=-t\xi-\omega_n k.
\]

Also

\[
\boxed{
\nabla\cdot\xi=t.
}
\]

because the `xi` and `k` directional derivatives contribute no diagonal component.

---

## 5. Vortex-direction stress balance

For a symmetric tensor diagonal in a moving orthonormal frame, the `xi` component of its divergence is

\[
(\operatorname{div}S)\cdot\xi
=D_\xi(wd)
+2wd\,t.
\]

The weighted harmonic forcing gives

\[
D_\xi(wd)
+2wdt
=-\frac E2D_\xi w.
\]

Expand:

\[
wD_\xi d
+dD_\xi w
+2wdt
=-\frac E2D_\xi w.
\]

Since

\[
d+\frac E2=B^2,
\]

we get

\[
D_\xi d
+B^2D_\xi\log w
+2dt=0.
\]

---

## 6. Divergence-free vorticity removes the weight

Vorticity is

\[
W=\rho\xi
\]

and

\[
\nabla\cdot W=0.
\]

Hence

\[
D_\xi\log\rho
=-\nabla\cdot\xi
=-t.
\]

Therefore

\[
D_\xi\log w=-2t.
\]

Substitute into Section 5:

\[
D_\xi d
-2B^2t
+2dt=0.
\]

Because

\[
d-B^2=-\frac E2,
\]

we obtain

\[
\boxed{
D_\xi d=Et.
}
\]

Thus

\[
\boxed{
D_\xi d
=E\nabla\cdot\xi.
}
\]

Using again

\[
D_\xi\log\rho=-\nabla\cdot\xi,
\]

we get the canonical linewise law

\[
\boxed{
D_\xi d
=-E D_\xi\log\rho.
}
\]

---

## 7. Interpretation of the line law

Along a vortex-direction integral curve, stretch anisotropy and amplitude cannot change independently.

If

\[
D_\xi d>0,
\]

then

\[
D_\xi\rho<0.
\]

If

\[
D_\xi d<0,
\]

then

\[
D_\xi\rho>0.
\]

At a point where

\[
D_\xi d=0,
\]

we have

\[
\boxed{
\nabla\cdot\xi=0
}
\]

and

\[
\boxed{
D_\xi\rho=0.
}
\]

Thus every linewise critical point of the signed stretch defect is simultaneously a linewise critical point of vorticity magnitude.

---

## 8. Kernel-direction balance remains geometric

The `k` projection gives

\[
\boxed{
D_kE
=2(B^2p-A^2\omega_n).
}
\]

This is exactly the `a·b=0` specialization of M17-035's geometric integrability identity.

It does not contain the weight `rho` and supplies no new signed harmonic restriction.

---

## 9. n-direction weighted balance

The `n` component of the stress divergence is

\[
-D_n(wd)
+2wdq
-wA^2\gamma.
\]

Set this equal to

\[
-\frac E2D_nw.
\]

After division by `w`,

\[
\boxed{
D_nd
=A^2\left(D_n\log w-\gamma\right)
+2dq.
}
\]

Equivalently,

\[
\boxed{
D_nd
=A^2\left(2D_n\log\rho-\gamma\right)
+2dq.
}
\]

Here

- `gamma` is the curvature coefficient of the kernel fibers through `D_k k=gamma n`;
- `q=n·b` is the `n` component of vortex-line curvature.

This equation couples anisotropy, transverse amplitude gradient, kernel-fiber curvature, and vortex-line curvature.

---

## 10. No fixed-sign monotonicity

Neither

\[
D_\xi d=-E D_\xi\log\rho
\]

nor

\[
D_nd
=A^2(2D_n\log\rho-\gamma)+2dq
\]

has a universal sign.

Therefore weighted harmonicity does not force `d` monotonically toward zero or away from zero.

The tempting shortcut

\[
\text{orthogonal anisotropy}
\Rightarrow
\text{automatic conformal relaxation}
\]

is rejected.

---

## 11. DSD interpretation

The orthogonal branch has one shape descriptor `d` and one amplitude descriptor `rho`.
The vortex-direction projection reveals that their linewise gradients are not independent:

\[
\boxed{
\text{stretch gradient}
=-\text{energy}\times\text{log-amplitude gradient}.
}
\]

The `n` projection adds the geometric compensation channels from the two line families.

Thus weighted harmonicity converts the branch into a coupled two-direction transport problem rather than a scalar relaxation law.

---

## 12. DSD audit

### Audit A — assuming diagonal stress means constant frame
Rejected. Connection coefficients generate the curvature terms explicitly.

### Audit B — interpreting D_xi d as a material derivative
Rejected. It is a spatial derivative along the vortex direction at fixed similarity time.

### Audit C — claiming d extrema are full spatial amplitude extrema
Rejected. Only the `xi` directional derivative is controlled.

### Audit D — claiming the n balance is sign-definite
Rejected.

### Audit E — proof status
The orthogonal stretch branch is reduced but remains open.

---

## 13. Updated orthogonal-stretch frontier

A persistent orthogonal stretch survivor must satisfy

\[
\boxed{
\begin{aligned}
D_\xi d&=-E D_\xi\log\rho,\\
D_nd&=A^2(2D_n\log\rho-\gamma)+2dq,\\
D_kE&=2(B^2p-A^2\omega_n),\\
D_B\log(A/B)&=\sigma-\sigma_n.
\end{aligned}
}
\]

with

\[
d\ne0.
\]

---

## 14. Next target

The next useful closure test is global/linewise rather than another local projection:

- audit whether a complete vortex line with finite enstrophy can support a nonzero `d` profile satisfying
  \[
  D_\xi d=-E D_\xi\log\rho
  \]
  at both spatial ends;
- separately test whether bounded recurrent material evolution of the same line profile can cross `d=0` without entering the M17-036 finite-distance conformal exit.

This is the **Orthogonal Stretch Line-End Gate (OSLEG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
