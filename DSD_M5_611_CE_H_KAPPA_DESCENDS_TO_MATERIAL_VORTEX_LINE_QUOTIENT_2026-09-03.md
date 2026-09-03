# DSD M5-611 — CE-H kappa descends to the material vortex-line quotient

Date: 2026-09-03

Status: **VORTEX-LINE QUOTIENT STRUCTURE / CE-H MAKES VORTEX LINES MATERIAL BECAUSE BOTH THE MATERIAL VORTICITY EVOLUTION AND THE FLOW-MAP TANGENT EVOLUTION PRESERVE THE VORTICITY EIGENLINE / THE VISCOUS EIGENVALUE ALREADY SATISFIES `W·nabla kappa=0`, SO KAPPA IS CONSTANT ALONG EACH VORTEX LINE AT FIXED TIME / THE COMMUTATOR `[D_B,W·nabla]=(kappa-3/2)(W·nabla)` THEN SHOWS THAT `D_B kappa`, AND IN FACT EVERY MATERIAL-TIME DERIVATIVE OF KAPPA, IS ALSO CONSTANT ALONG EACH VORTEX LINE / THUS THE REMAINING KAPPA OSCILLATION IS A SCALAR DYNAMICS ON THE TWO-DIMENSIONAL QUOTIENT OF THE ACTIVE REGION BY MATERIAL VORTEX LINES, NOT AN ARBITRARY THREE-DIMENSIONAL POINTWISE OSCILLATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material and vortex-line operators

On the CE-H active set define

\[
D:=D_B=\partial_\theta+B\cdot\nabla,
\]

and

\[
L:=W\cdot\nabla.
\]

M5-600 gives

\[
DW=\gamma W,
\qquad
\gamma=\sigma+\kappa-1.
\]

Also

\[
(W\cdot\nabla)B
=(W\cdot\nabla)U+\frac12W
=\left(\sigma+\frac12\right)W.
\]

---

## 2. Vortex lines are material lines

A material tangent vector `ell` evolves by

\[
D\ell=(\nabla B)\ell.
\]

If initially `ell` is parallel to `W`, then

\[
D\ell
=\left(\sigma+\frac12\right)\ell
\]

in that direction, while

\[
DW=\gamma W
\]

is also parallel to `W`.

Therefore the tangent direction remains the vorticity direction:

\[
\boxed{
\text{CE-H vortex lines are transported as material lines.}
}
\]

This is a direction statement; their tangent magnitudes need not evolve at the same rate as `|W|`.

---

## 3. Kappa is constant along each vortex line

M5-600 already gave

\[
\boxed{L\kappa=W\cdot\nabla\kappa=0.}
\]

Thus at each fixed similarity time, `kappa` is constant along every connected nonzero vortex-line segment.

---

## 4. Exact commutator

For any smooth scalar `f`,

\[
[D,L]f
=
\left(DW-(\nabla B)W\right)\cdot\nabla f.
\]

Using

\[
DW=(\sigma+\kappa-1)W,
\]

and

\[
(\nabla B)W=\left(\sigma+\frac12\right)W,
\]

we obtain

\[
\boxed{
[D,L]
=
\left(\kappa-\frac32\right)L.
}
\]

---

## 5. Material derivatives of kappa remain vortex-line constants

Apply `D` to

\[
L\kappa=0.
\]

Since

\[
D(L\kappa)
=L(D\kappa)+[D,L]\kappa,
\]

and

\[
[D,L]\kappa
=\left(\kappa-\frac32\right)L\kappa=0,
\]

we obtain

\[
\boxed{L(D\kappa)=0.}
\]

Now suppose inductively

\[
L(D^m\kappa)=0.
\]

Then the same commutator gives

\[
L(D^{m+1}\kappa)=0.
\]

Therefore

\[
\boxed{
W\cdot\nabla(D_B^m\kappa)=0
\qquad
\forall m\ge0.
}
\]

---

## 6. Quotient-space interpretation

Locally away from vortex zeros, the active region is foliated by material vortex lines.

Because `kappa` and all of its material-time derivatives are constant along each leaf, they descend to scalar data on the local two-dimensional quotient of the active region by those vortex lines.

Schematically,

\[
\boxed{
\kappa(y,\theta)
=\widehat\kappa([\mathcal L_y],\theta),
}
\]

where `[L_y]` denotes the vortex-line leaf through `y`.

No global smooth quotient manifold is assumed near zeros, reconnections of the zero set, or topologically complicated foliations.

---

## 7. Consequence for the M5-606 flux-oscillation branch

M5-606 showed that the only unsaturated CE-H turnover branch has sign-changing flux-weighted `kappa` with zero signed mean.

M5-611 shows that this sign-changing dynamics cannot be interpreted as one point on a vortex line becoming positive while another point on the same line remains negative at the same time.

At each fixed time, every connected active vortex line carries one `kappa` value.

Hence recurrent positive/negative compensation is a temporal evolution of vortex-line labels in the quotient dynamics.

---

## 8. Relation to the radial Pohozaev identity

M5-607 gives

\[
\int(y_\perp\cdot\nabla\kappa)|W|^2=2P>0.
\]

Since `nabla kappa` is transverse to vortex lines, this is naturally a gradient constraint on the same two-dimensional vortex-line quotient.

Thus the remaining CE-H problem can be phrased as compatibility of:

1. zero-mean temporal `kappa` cocycles on persistent flux leaves;
2. negative enstrophy-weighted mean `kappa`;
3. positive transverse radial quotient gradient;
4. uniformly positive spatial variance;
5. the strain-eigenframe compensation law of M5-609.

---

## 9. Firewall

This reduction does not assert that the global quotient is a regular compact two-manifold, nor that vortex lines are closed.

It is a local/leafwise structural reduction on the nonzero active set.

No two-dimensional Liouville theorem is imported at this stage.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
