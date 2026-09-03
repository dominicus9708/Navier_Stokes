# DSD M5-622 — Transverse magnitude-gradient material equation and strict-cocycle no-go

Date: 2026-09-03

Status: **INTERNAL EXACT TRANSPORT LAW / FOR `G=P_perp nabla log rho`, CE-H GIVES `D_B G = P_perp nabla(sigma+kappa) - L_perp^T G`, WHERE `L_perp=P_perp(nabla B)P_perp` IS THE TRANSVERSE MATERIAL-DEFORMATION BLOCK / UNLIKE VORTEX CURVATURE, `G` HAS A GENUINE CROSS-LINE FORCING TERM `P_perp nabla(sigma+kappa)` AND AN ANISOTROPIC TRANSVERSE-STRAIN TERM, SO NO UNIVERSAL CONSTANT-DRIFT RATIO WITH MATERIAL FLUX EXISTS / THE M5-619 TRANSVERSE-MAGNITUDE BRANCH THEREFORE SPLITS INTO A GROWTH-RATE-GRADIENT BRANCH OR A HOMOGENEOUS BURGERS-LIKE TRANSVERSE-DEFORMATION BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H scalar amplitude equation

Write

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

and define

\[
D_B=\partial_\theta+B\cdot\nabla,
\qquad
B=U+\frac12y.
\]

On CE-H,

\[
\boxed{D_B\xi=0,}
\]

and

\[
\boxed{
D_B\log\rho
=\gamma,
\qquad
\gamma:=\sigma+\kappa-1.
}
\]

---

## 2. Transverse logarithmic magnitude gradient

Let

\[
P:=I-\xi\otimes\xi
\]

and define

\[
\boxed{
G:=P\nabla\log\rho.
}
\]

This is the vorticity-amplitude gradient across vortex lines.

Since `D_B xi=0`,

\[
\boxed{D_BP=0.}
\]

---

## 3. Gradient commutator

For a scalar `f`,

\[
D_B(\nabla f)
=
\nabla(D_Bf)
-(\nabla B)^T\nabla f.
\]

Apply this to

\[
f=\log\rho.
\]

Then

\[
D_B\nabla\log\rho
=
\nabla\gamma
-(\nabla B)^T\nabla\log\rho.
\]

Decompose

\[
\nabla\log\rho
=G+a\xi,
\qquad
a:=\xi\cdot\nabla\log\rho.
\]

On CE-H,

\[
(\nabla B)^T\xi
=\left(\sigma+\frac12\right)\xi,
\]

so the parallel term disappears after applying `P`.

Therefore

\[
\boxed{
D_BG
=P\nabla\gamma
-P(\nabla B)^TG.
}
\]

Because `G` is transverse and the transverse plane is invariant under `nabla B`, define

\[
\boxed{
L_\perp:=P(\nabla B)P.
}
\]

Then

\[
\boxed{
D_BG
=P\nabla(\sigma+\kappa)
-L_\perp^TG.
}
\]

This is the exact transverse-magnitude-gradient material equation.

---

## 4. Norm equation

The skew part of `L_perp` does not contribute to `G·L_perp^TG`.

Since

\[
\operatorname{Sym}L_\perp
=P\left(\Sigma+\frac12I\right)P,
\]

we obtain

\[
\boxed{
\frac12D_B|G|^2
=G\cdot P\nabla(\sigma+\kappa)
-G\cdot\Sigma G
-\frac12|G|^2.
}
\]

Thus the evolution has three distinct channels:

1. cross-line variation of the scalar growth multiplier `sigma+kappa`;
2. anisotropic transverse strain;
3. the universal similarity `-1/2` covector damping.

The first two terms have no fixed sign.

---

## 5. Transverse strain eigenframe

Use the CE-H strain eigenframe

\[
\Sigma\xi=\sigma\xi.
\]

Let the two transverse eigenvalues be

\[
\lambda_2=-\frac\sigma2+\delta,
\qquad
\lambda_3=-\frac\sigma2-\delta.
\]

Write

\[
G=g_2e_2+g_3e_3.
\]

Then

\[
G\cdot\Sigma G
=-\frac\sigma2|G|^2
+\delta(g_2^2-g_3^2).
\]

Hence

\[
\boxed{
\frac12D_B|G|^2
=G\cdot P\nabla(\sigma+\kappa)
+\frac{\sigma-1}{2}|G|^2
-\delta(g_2^2-g_3^2).
}
\]

This explicitly displays why the magnitude-gradient branch does not inherit the curvature branch's universal drift.

---

## 6. Why the curvature/flux trick does not repeat

For curvature,

\[
D_B\log(\rho|\mathcal K|)
=\kappa-\frac32,
\]

while flux obeys

\[
D_B\log|\phi|=\kappa,
\]

and subtraction gave the strict constant drift `-3/2`.

For `G`, the equation contains the additive vector source

\[
\boxed{P\nabla(\sigma+\kappa).}
\]

Therefore no division by material flux can remove the forcing term.

Even when this forcing vanishes, the anisotropic quadratic term

\[
G\cdot\Sigma G
\]

depends on the instantaneous orientation of `G` in the transverse strain plane.

Hence the implication

\[
\text{transverse magnitude charge}
\Longrightarrow
\text{universal constant signed drift}
\]

is false at the present level.

This is a DSD no-go result, not a failure of the CE-H equations.

---

## 7. Forced branch

Define

\[
\boxed{
F_\gamma:=P\nabla(\sigma+\kappa).
}
\]

If a positive fraction of the recurrent transverse-magnitude charge requires

\[
|F_\gamma|\ge f_*>0,
\]

then the branch has a new fixed cross-vortex-line multiplier-gradient charge.

Since

\[
F_\gamma=P\nabla\sigma+P\nabla\kappa,
\]

this further splits into

\[
\boxed{
|P\nabla\kappa|\text{ positive}
\quad\lor\quad
|P\nabla\sigma|\text{ positive}.
}
\]

The first is directly related to the M5-615--617 generalized `kappa`-force dipole; the second is a strain-eigenvalue-gradient channel.

---

## 8. Homogeneous transverse-deformation branch

If instead

\[
F_\gamma=0
\]

on a persistent material lane, then

\[
\boxed{
D_BG=-L_\perp^TG.
}
\]

Thus `G` behaves as a material transverse covector.

For a recurrent nonzero `G`, the signed strain sampled in its own direction must balance the universal half-rate:

\[
D_B\log|G|
=-\widehat G\cdot\Sigma\widehat G-rac12.
\]

Hence a same-label recurrent magnitude-gradient marker requires

\[
\boxed{
\left\langle
\widehat G\cdot\Sigma\widehat G
\right\rangle
=-\frac12.
}
\]

If the same material tube also has amplitude/flux recurrence giving `mean sigma=1`, then the trace-free relation makes the remaining transverse principal strain average `-1/2` as well.

This is exactly the mean transverse-strain pattern of a Burgers-type axisymmetric extensional balance, so it is **not a contradiction**.

---

## 9. Axisymmetric no-swirl firewall

Axisymmetric no-swirl velocity fields provide an important consistency example:

\[
W=\omega_\theta e_\theta.
\]

Then `W` is a strain eigenvector, `Delta W` is parallel to `W`, and the azimuthal vortex lines have material curvature `1/r`.

Therefore any argument that declares the local CE-H eigenline algebra or the homogeneous transverse-deformation balance impossible would incorrectly eliminate a known regular Navier--Stokes geometry.

The present proof attempt must use the whole-space finite-enstrophy ancient/recurrent constraints, not local alignment alone.

---

## 10. Updated M5-619 split

The non-Beltrami dichotomy has now become

\[
\boxed{
E_{CEH}
\Longrightarrow
T_{viscous\ turnover}^{curv}
\lor
F_{\nabla(\sigma+\kappa)}
\lor
H_{transverse\ covector}^{Burgers-like}.
}
\]

Here

- the curvature channel was converted by M5-621 into viscous material-label turnover;
- the forced magnitude channel carries a fixed cross-line gradient of the total multiplier;
- the homogeneous magnitude channel is a Burgers-like transverse covector recurrence and remains open.

---

## 11. Highest-value next target

The most promising new target is the forced branch because

\[
P\nabla\kappa
\]

already has a global stress/virial structure, while

\[
P\nabla\sigma
\]

can be obtained by differentiating the strain eigenline equation

\[
\Sigma W=\sigma W.
\]

The homogeneous branch should be retained as an explicit regular-geometry firewall until a genuinely global ancient Liouville argument is available.

---

## 12. Audit status

No strict scalar cocycle analogous to M5-621 exists for `G` without additional assumptions.

The additive cross-line forcing and anisotropic transverse deformation are genuine and cannot be discarded.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
