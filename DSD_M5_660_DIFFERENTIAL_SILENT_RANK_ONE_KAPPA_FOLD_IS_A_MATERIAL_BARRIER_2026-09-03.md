# DSD M5-660 — A differential-silent rank-one kappa fold is a material barrier

Date: 2026-09-03

Status: **INTERNAL MOVING-CRITICAL-SET GEOMETRY / M5-659 SHOWS THAT A SILENT MULTI-SHEET BRANCH POINT MUST BE TRANSVERSELY DEGENERATE; IN THE GENERIC SURVIVING RANK-ONE CASE, THE ACTIVE KAPPA-CRITICAL SET IS LOCALLY A FOLD SURFACE WITH `Hess kappa = lambda n tensor n` / DIFFERENTIATING THE MOVING CRITICAL-SET CONDITION GIVES `grad h = Hess(kappa)(B-V_Sigma)`; HENCE THE DIFFERENTIAL-SILENT CONDITION `grad h=0` FORCES THE NORMAL VELOCITY OF THE FOLD TO EQUAL THE MATERIAL NORMAL VELOCITY `B·n`, SO MATERIAL LABELS DO NOT CROSS THE SILENT FOLD / THE REMAINING MULTI-SHEET SURVIVOR IS THEREFORE NOT A CROSS-SHEET MATERIAL-TRANSFER PROCESS BUT A MATERIAL BARRIER NETWORK OF DISTINCT RELABELING SHEETS COUPLED THROUGH THE GLOBAL PDE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rank-one silent fold

Consider the M5-659 silent branch at an active point with

\[
\rho>a_0,
\qquad
\nabla\kappa=0,
\qquad
\nabla h=0,
\qquad
h=D_B\kappa.
\]

Assume the full Hessian has rank one:

\[
\boxed{
\nabla^2\kappa
=
\lambda\,n\otimes n,
\qquad
\lambda\ne0.
}
\]

Because `W` lies in the Hessian kernel by M5-659,

\[
W\cdot n=0.
\]

Thus the vortex direction is tangent to the critical fold.

---

## 2. Moving critical surface

Let the local active critical set be a smooth surface

\[
\Sigma(\theta)
\]

with local parametrization

\[
X=X(a,b,\theta)
\]

satisfying

\[
\boxed{
\nabla\kappa(X(a,b,\theta),\theta)=0.
}
\]

Let

\[
V_\Sigma:=\partial_\theta X
\]

be one chosen surface velocity; only its normal component is geometrically intrinsic.

Differentiate the critical-point condition:

\[
0
=
\partial_\theta\nabla\kappa
+
( V_\Sigma\cdot\nabla)\nabla\kappa.
\]

Hence

\[
\boxed{
\partial_\theta\nabla\kappa
=-(\nabla^2\kappa)V_\Sigma.
}
\]

---

## 3. Compare with the material derivative

For a scalar field,

\[
D_B(\nabla\kappa)
=
\nabla(D_B\kappa)
-(\nabla B)^T\nabla\kappa.
\]

On the critical surface `grad kappa=0`,

\[
\boxed{
D_B(\nabla\kappa)=\nabla h.
}
\]

But also

\[
D_B(\nabla\kappa)
=
\partial_\theta\nabla\kappa
+(B\cdot\nabla)\nabla\kappa
=
-(\nabla^2\kappa)V_\Sigma
+(\nabla^2\kappa)B.
\]

Therefore the exact moving-fold identity is

\[
\boxed{
\nabla h
=
(\nabla^2\kappa)(B-V_\Sigma).
}
\]

---

## 4. Rank-one form

Insert

\[
\nabla^2\kappa=\lambda n\otimes n.
\]

Then

\[
\boxed{
\nabla h
=
\lambda\,n\,[(B-V_\Sigma)\cdot n].
}
\]

Hence the normal mismatch is

\[
\boxed{
(B-V_\Sigma)\cdot n
=
\frac{n\cdot\nabla h}{\lambda}.
}
\]

This identifies critical-force creation geometrically: a nonzero normal derivative of `h` is exactly a mismatch between material motion and fold motion.

---

## 5. Differential-silent branch is a material normal barrier

On the surviving silent branch,

\[
\nabla h=0.
\]

Therefore

\[
\boxed{
(B-V_\Sigma)\cdot n=0.
}
\]

Equivalently,

\[
\boxed{
V_\Sigma\cdot n=B\cdot n.
}
\]

Thus the fold surface moves with the same **normal velocity** as material trajectories.

Material labels may slide tangentially relative to a chosen parametrization of the fold, but they do not cross it in the normal direction.

So the two local branches separated by the silent fold form material sheet populations.

---

## 6. Relation to vortex geometry

Because

\[
W\cdot n=0,
\]

vortex lines are tangent to the fold as well.

Hence the silent fold is simultaneously:

1. a kappa-critical branch surface;
2. a material normal barrier;
3. a surface tangent to the CE-H vortex-line foliation.

No vorticity-flux leaf crosses the fold transversely at the branch point.

---

## 7. Consequence for the M5-657 language

M5-657 uses the phrase `cross-sheet patching` for the surviving payer configuration.

The present calculation shows that, on the differential-silent rank-one branch, this must **not** be interpreted as physical material transfer from one sheet to another.

Instead the rigorous picture is

\[
\boxed{
\text{distinct material relabeling sheets}
+
\text{global elliptic/Biot-Savart coupling}
+
\text{payer outsourcing across the sheet network}.
}
\]

Thus a finite-resource argument based on flux physically crossing the silent fold would be invalid.

---

## 8. Non-silent comparison

If

\[
\nabla h\ne0,
\]

then

\[
(B-V_\Sigma)\cdot n\ne0,
\]

and the material flow genuinely crosses the instantaneous critical fold.

This is precisely the M5-654 critical-force-creation branch

\[
F=0,
\qquad
D_BF=\rho^2\nabla h\ne0.
\]

Thus force creation and material fold crossing are two descriptions of the same first-order event in the rank-one case.

---

## 9. Updated silent-sheet frontier

The rank-one silent survivor is now

\[
\boxed{
R_{silent\ fold}
:
\text{a recurrent material barrier network of high-amplitude relabeling sheets, each carrying its own local scalar law and coupled nonlocally through the CE-H PDE.}
}
\]

The reference and negative payer can lie on opposite sides without exchanging material labels.

Therefore the next useful object is the **finite sheet network itself**, not a cross-sheet material flux.

One should test whether analyticity/semianalytic geometry and the uniform high-amplitude compact core force only finitely many recurrent sheet components, and if so whether the M5-657 payer assignment on that finite network forces a recurrent directed cycle with an incompatible collection of scalar-law flux averages.

---

## 10. Firewall

The moving-surface computation assumes a smooth rank-one critical fold.

Higher-order rank-zero/cusp critical sets remain separate and are not covered by the material-barrier conclusion without further stratification.

No contradiction is claimed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]