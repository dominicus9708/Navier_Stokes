# DSD M5-659 — Differential-silent multi-sheet patching forces transverse kappa-Hessian degeneracy

Date: 2026-09-03

Status: **INTERNAL SECOND-JET RIGIDITY / AT EVERY ACTIVE KAPPA-CRITICAL POINT, THE FIRST-INTEGRAL IDENTITY `W·grad kappa=0` FORCES `(Hess kappa)W=0`, SO THE CRITICAL GEOMETRY IS TRANSVERSE TO THE VORTEX LINE / IF THE TRANSVERSE 2x2 HESSIAN IS NONDEGENERATE AND THE ZERO-ROTATION CONDITION `grad kappa x grad h=0` HOLDS AROUND A DIFFERENTIAL-SILENT POINT, ANALYTIC MORSE NORMAL FORM FORCES `h` TO CONTINUE AS ONE SINGLE-VALUED LOCAL FUNCTION OF `kappa`; THEREFORE GENUINE SILENT MULTI-SHEET PATCHING REQUIRES `det Hess_perp(kappa)=0` / THE SURVIVING CROSS-SHEET BRANCH IS THUS A HIGH-AMPLITUDE TRANSVERSELY-DEGENERATE ANALYTIC CRITICAL SET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Silent branch from M5-658

The only sheet-patching event not already detected by generalized-force rotation or critical-force creation satisfies

\[
\boxed{
\rho>a_0,
\qquad
\nabla\kappa=0,
\qquad
\nabla h=0,
\qquad
h:=D_B\kappa.
}
\]

In a punctured neighborhood belonging to the relabeling branch one also has

\[
\boxed{
\nabla\kappa\times\nabla h=0.
}
\]

The question is whether two genuinely different analytic scalar-law sheets can meet at such a point.

---

## 2. The kappa Hessian annihilates the vortex direction

CE-H gives the exact first-integral identity

\[
\boxed{W\cdot\nabla\kappa=0.}
\]

Differentiate in an arbitrary direction `v`:

\[
\partial_v(W\cdot\nabla\kappa)
=
(\partial_vW)\cdot\nabla\kappa
+
W\cdot(\nabla^2\kappa)v
=0.
\]

At an active critical point `grad kappa=0`,

\[
W\cdot(\nabla^2\kappa)v=0
\quad\forall v.
\]

Since the Hessian is symmetric,

\[
\boxed{
(\nabla^2\kappa)W=0.
}
\]

Thus the vortex direction is an exact null eigenvector of the kappa Hessian.

---

## 3. Transverse Hessian

Because `rho>0`, write

\[
\xi=\frac W{|W|}.
\]

Define

\[
\boxed{
K_\perp
:=
P_\xi^\perp(\nabla^2\kappa)P_\xi^\perp
\big|_{\xi^\perp}.
}
\]

This is a symmetric `2x2` quadratic form.

The full Hessian has rank equal to the rank of `K_perp` at the critical point.

Hence the maximal possible critical rank is two.

---

## 4. Second-jet consequence of zero force rotation

Likewise M5-611 gives

\[
W\cdot\nabla h=0.
\]

At a silent critical point `grad h=0`, the same differentiation yields

\[
\boxed{
(\nabla^2h)W=0.
}
\]

Let

\[
H_\perp
:=
P_\xi^\perp(\nabla^2h)P_\xi^\perp.
\]

Linearize the gradients in transverse coordinates `z in xi^perp`:

\[
\nabla_\perp\kappa
=
K_\perp z+O(|z|^2),
\]

\[
\nabla_\perp h
=
H_\perp z+O(|z|^2).
\]

The punctured zero-rotation condition implies, at leading order,

\[
\boxed{
K_\perp z
\wedge
H_\perp z
=0
\quad\forall z\in\mathbb R^2.
}
\]

If `K_perp` is invertible, set `q=K_perp z`.

Then

\[
H_\perp K_\perp^{-1}q
\parallel q
\quad\forall q.
\]

A linear map that sends every vector to a parallel vector must be a scalar multiple of the identity.

Therefore

\[
\boxed{
H_\perp=\lambda K_\perp
}
\]

for one scalar `lambda`.

Thus even the second jet has one unique scalar-law slope.

---

## 5. Analytic Morse rigidity in the nondegenerate transverse case

Assume

\[
\boxed{
det K_\perp\ne0.
}
\]

Then in the two directions transverse to the vortex line, `kappa` has a nondegenerate Morse critical point.

By the real-analytic Morse lemma, after an analytic transverse coordinate change, the leading local form is one of

\[
\kappa-\kappa_0
=
\pm u^2\pm v^2
\]

with no degenerate transverse direction.

On the punctured neighborhood,

\[
dh\wedge d\kappa=0.
\]

In the Morse coordinates, analytic functions satisfying this relation are constant on the local connected components of the `kappa` levels and their Taylor series contain only powers of the Morse invariant.

Equivalently there exists one analytic germ `f` such that

\[
\boxed{
h=f(\kappa,\theta)
}
\]

through the critical point.

For the saddle normal form this can also be checked after the linear change to `uv`: the equation `dh wedge d(uv)=0` forces equal powers of `u` and `v` term by term, so `h` is a power series in `uv`.

Thus a nondegenerate transverse critical point does **not** support differential-silent multi-sheet patching.

---

## 6. Necessary degeneracy for a genuine silent branch point

The only remaining possibility is

\[
\boxed{
det K_\perp=0.
}
\]

Therefore

\[
\boxed{
K_{silent}^{analytic\ multi-sheet}
\Longrightarrow
\operatorname{rank}(\nabla^2\kappa)\le1.
}
\]

This is substantially stronger than `grad kappa=0`.

The local model

\[
\kappa=x^2,
\qquad
h=x^3
\]

illustrates exactly this degenerate case: the Hessian has only one nonzero transverse direction and the two branches obey `h=+kappa^{3/2}` and `h=-kappa^{3/2}`.

---

## 7. Geometric interpretation

A surviving silent patch is therefore a high-amplitude point where

1. `kappa` has zero first derivative;
2. the vortex direction is automatically a Hessian null direction;
3. at least one additional transverse Hessian direction is also null.

Hence at least a two-dimensional kernel is present in the full three-dimensional Hessian:

\[
\boxed{
\dim\ker(\nabla^2\kappa)\ge2.
}
\]

The branch set is a highly degenerate scalar-potential geometry, not a generic Morse critical event.

---

## 8. Updated cross-sheet frontier

Combining M5-658 and the present result,

\[
\boxed{
T_{high-amplitude\ cross-sheet}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{force}
\lor
K_{deg}^{\operatorname{rank} Hess\kappa\le1}.
}
\]

The third branch is the only differential-silent survivor.

---

## 9. Next target

At a degenerate active critical point, the first nonzero transverse Taylor polynomial of

\[
\kappa-\kappa_0
\]

has degree at least two and is degenerate in at least one transverse direction.

The next calculation should use analyticity plus compact-hull bounds to determine whether repeated order-one sheet splitting forces a **uniform finite higher-jet order** and hence a fixed higher-derivative charge of `kappa` (or of the quotient-free force `F=rho^2 grad kappa`).

This would convert the silent multi-sheet branch into a quantitative jet event rather than an arbitrary topological loophole.

---

## 10. Firewall

The statement is local and analytic.

It does not claim that all degenerate critical points produce multiple sheets.

It proves only the necessary implication:

\[
\text{silent multi-sheet patching}
\Rightarrow
\text{transverse Hessian degeneracy}.
\]

No contradiction with recurrence is yet obtained.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]