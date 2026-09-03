# DSD M17-029 — The parallel rank-two branch is a straight-line congruence with an exact Riccati focusing law

Date: 2026-09-03
Canonical ID: **M17-029**

Status: **INTERNAL RANK-TWO PARALLEL CLASSIFICATION / ON `J_xi || W`, THE KERNEL PROPERTY OF THE DIRECTOR-AREA CURRENT GIVES `(xi dot grad)xi=0`. EVERY ACTIVE VORTEX-DIRECTION INTEGRAL CURVE IS THEREFORE A EUCLIDEAN STRAIGHT LINE. FOR THE TRANSVERSE DIRECTOR GRADIENT `A=grad xi|_{xi^perp}`, DIFFERENTIATING THE GEODESIC FIELD EQUATION GIVES THE EXACT RICCATI LAW `dA/ds=-A^2`, SO `A(s)=A_0(I+sA_0)^{-1}` AND THE TRANSVERSE SEPARATION JACOBIAN IS `Delta_perp(s)=det(I+sA_0)`. DIVERGENCE-FREE VORTICITY AND DIRECTOR-AREA CURRENT THEN GIVE `rho(s)=rho_0/Delta_perp(s)` AND `j_xi(s)=j_0/Delta_perp(s)`, MAKING `j_xi/rho` A VORTEX-LINE FIRST INTEGRAL. A RANK-TWO LINE THAT REMAINS SMOOTH FOR ALL `s in R` CANNOT HAVE A REAL NONZERO TRANSVERSE EIGENVALUE: `Delta_perp(s)` MUST NEVER VANISH, WHICH FOR AN INVERTIBLE REAL 2X2 `A_0` REQUIRES `det A_0>0` AND `(tr A_0)^2<4 det A_0`. THUS A GLOBAL PARALLEL RANK-TWO SURVIVOR MUST BE A TWISTING SKEW-LINE CONGRUENCE, NOT A GENERIC EXPANDING/CONTRACTING STRAIGHT BUNDLE. THIS IS A SHARP CLASSIFICATION, NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parallel rank-two hypothesis

M17-026 splits rank two into

\[
R_2^{parallel}
\ \lor\ 
R_2^{oblique}.
\]

On the parallel branch,

\[
\boxed{
J_\xi\parallel W.
}
\]

Since

\[
W=\rho\xi,
\]

and the rank-two current spans the kernel of `d xi`,

\[
(J_\xi\cdot\nabla)\xi=0
\]

implies

\[
\boxed{
(\xi\cdot\nabla)\xi=0.
}
\]

---

## 2. Vortex-direction integral curves are straight

Let `x(s)` be an integral curve of the unit director:

\[
\frac{dx}{ds}=\xi(x(s)).
\]

Because `|xi|=1`, `s` is arclength.
Differentiate again:

\[
\frac{d^2x}{ds^2}
=(\xi\cdot\nabla)\xi.
\]

Hence

\[
\boxed{
\frac{d^2x}{ds^2}=0.
}
\]

Therefore

\[
\boxed{
x(s)=x_0+s\xi_0.}
\]

Every active vortex line in the parallel rank-two patch is a Euclidean straight line, and `xi` is constant along that line.

---

## 3. Transverse director-gradient matrix

At a point on one such line, `grad xi` annihilates `xi`:

\[
(\nabla\xi)\xi=0.
\]

Unit length also gives

\[
\xi^T\nabla\xi=0.
\]

Thus `grad xi` maps the transverse plane `xi^perp` to itself.
Define its `2x2` transverse representation

\[
\boxed{
A:=\nabla\xi|_{\xi^\perp}.
}
\]

Rank two means

\[
\boxed{
\det A\ne0.
}
\]

The full director Jacobian has one zero eigen-direction `xi` and two nonzero transverse singular directions.

---

## 4. Exact Riccati equation along each straight line

Differentiate the geodesic-field identity

\[
\xi_k\partial_k\xi_i=0
\]

with respect to `x_j`:

\[
(\partial_j\xi_k)(\partial_k\xi_i)
+\xi_k\partial_k\partial_j\xi_i=0.
\]

Therefore

\[
\boxed{
(\xi\cdot\nabla)(\nabla\xi)
=-(\nabla\xi)^2.
}
\]

Restricting to the transverse plane along the straight line gives

\[
\boxed{
\frac{dA}{ds}=-A^2.
}
\]

This is an exact matrix Riccati equation.

---

## 5. Explicit solution

As long as the inverse exists,

\[
\boxed{
A(s)=A_0(I+sA_0)^{-1}.
}
\]

Indeed

\[
\frac d{ds}
\left[A_0(I+sA_0)^{-1}\right]
=-A(s)^2.
\]

Define the transverse separation matrix

\[
\boxed{
M(s):=I+sA_0.
}
\]

Then

\[
A(s)=M'(s)M(s)^{-1}.
\]

The local transverse area factor is

\[
\boxed{
\Delta_\perp(s):=\det M(s)=\det(I+sA_0).
}
\]

---

## 6. Divergence along the line

Because the longitudinal derivative of `xi` is zero,

\[
\nabla\cdot\xi=\operatorname{tr}A.
\]

From the determinant identity,

\[
\boxed{
\frac d{ds}\log|\Delta_\perp(s)|
=\operatorname{tr}A(s)
=\nabla\cdot\xi.
}
\]

Thus `Delta_perp` is the exact geometric cross-sectional expansion factor of the straight-line congruence.

---

## 7. Exact vorticity-amplitude profile along a line

Vorticity is divergence-free:

\[
\nabla\cdot W=0.
\]

With

\[
W=\rho\xi,
\]

we have

\[
(\xi\cdot\nabla)\rho
+\rho\nabla\cdot\xi=0.
\]

Along the line,

\[
\frac d{ds}\log\rho
=-\operatorname{tr}A(s).
\]

Combining with the determinant law gives

\[
\boxed{
\rho(s)
=\frac{\rho_0}{|\Delta_\perp(s)|}
}
\]

on an orientation-fixed interval; with a continuously oriented nonvanishing determinant the absolute value can be replaced by its fixed sign convention.

Thus the vorticity amplitude is exactly the inverse transverse spreading of the straight-line congruence.

---

## 8. Director-area density has the same spatial profile

On the parallel branch,

\[
J_\xi=j_\xi\xi
\]

up to the signed orientation convention.
Because

\[
\nabla\cdot J_\xi=0,
\]

we likewise obtain

\[
\frac d{ds}\log|j_\xi|
=-\operatorname{tr}A(s).
\]

Hence

\[
\boxed{
 j_\xi(s)
=\frac{j_{\xi,0}}{\Delta_\perp(s)}.
}
\]

Therefore

\[
\boxed{
\frac{j_\xi}{\rho}
=\text{constant along each vortex line}.
}
\]

This is the spatial vortex-line version of the material invariant ratio identified in M17-028.

---

## 9. Focusing criterion

For a real `2x2` matrix `A_0`,

\[
\boxed{
\Delta_\perp(s)
=1+s\operatorname{tr}A_0+s^2\det A_0.
}
\]

If this polynomial vanishes at finite real `s`, the local transverse separation map loses invertibility and the Riccati representation develops a focusing/caustic singularity.

A smooth rank-two straight-line congruence valid for all

\[
s\in\mathbb R
\]

therefore requires

\[
\boxed{
\Delta_\perp(s)\ne0
\quad\forall s\in\mathbb R.
}
\]

---

## 10. Global rank-two no-focusing condition

Since rank two gives

\[
\det A_0\ne0,
\]

the quadratic polynomial can avoid real roots only if

\[
\boxed{
\det A_0>0
}
\]

and its discriminant is strictly negative:

\[
\boxed{
(\operatorname{tr}A_0)^2
-4\det A_0
<0.
}
\]

Equivalently, the two eigenvalues of the real transverse matrix are a nonreal complex-conjugate pair.

Thus a global smooth rank-two parallel congruence cannot be a generic purely expanding/contracting bundle with real principal directions.
It must contain sufficient transverse twist to prevent line focusing.

---

## 11. Large-|s| profile

Under the global no-focusing condition,

\[
\det A_0>0.
\]

Therefore

\[
\Delta_\perp(s)
\sim
(\det A_0)s^2
\qquad(|s|\to\infty).
\]

Hence along the straight line,

\[
\boxed{
\rho(s)
\sim
\frac{\rho_0}{\det A_0}\,|s|^{-2},
}
\]

and similarly

\[
\boxed{
|j_\xi(s)|
\sim C_j|s|^{-2}.
}
\]

Thus the global nonfocusing geometry naturally produces algebraic decay rather than a finite-distance zero.
This behavior is compatible with linewise finite `L^2` mass and is not by itself contradictory.

---

## 12. Twist versus strain form

Write the transverse matrix as

\[
A=S+\Omega,
\]

with `S` symmetric and `Omega` antisymmetric on the two-dimensional transverse plane.

The no-real-eigenvalue condition

\[
(\operatorname{tr}A)^2<4\det A
\]

is exactly the statement that the discriminant of the transverse line-deformation map is negative.
It requires the rotational/twist part to dominate the eigenvalue-splitting tendency strongly enough to prevent real focusing directions.

This gives the parallel rank-two survivor the structure of a **twisting skew-line congruence**.

No claim is made that every such abstract congruence satisfies the full CE-H equations.

---

## 13. DSD interpretation

### 13.1 Kernel current becomes line geometry
The abstract condition `J_xi || W` converts the director-area kernel into the actual vortex-line tangent.

### 13.2 Rank-two area becomes nonfocusing twist
Maintaining two transverse director degrees of freedom along an entire straight line requires an invertible transverse Riccati map with no real focal root.

### 13.3 Same spatial dilution for rho and j_xi
Vorticity flux and director-area flux dilute through exactly the same transverse line-bundle area factor.

---

## 14. DSD audit

### Audit A — local straight segment versus global line
The all-`s` no-focusing condition applies only if the active rank-two parallel branch extends smoothly along the complete straight integral line. A finite patch needs only local invertibility.

### Audit B — interpreting a congruence caustic as established Navier-Stokes blow-up
Rejected. Loss of this rank-two coordinate description can instead signal rank loss, branch exit, or failure of the assumed global straight-line patch.

### Audit C — claiming complex eigenvalues make grad xi complex
Rejected. `A` is a real matrix; only its eigenvalues are a complex-conjugate pair, representing twist-dominated real geometry.

### Audit D — algebraic decay as contradiction
Rejected. The `|s|^{-2}` line profile is compatible with linewise finite energy.

### Audit E — proof status
The parallel rank-two branch is sharply classified but remains open.

---

## 15. Updated parallel-rank-two frontier

A complete-line parallel rank-two survivor must satisfy

\[
\boxed{
\begin{aligned}
(\xi\cdot\nabla)\xi&=0,\\
A'&=-A^2,\\
A(s)&=A_0(I+sA_0)^{-1},\\
\rho(s)&=\rho_0/\Delta_\perp(s),\\
j_\xi(s)&=j_{\xi,0}/\Delta_\perp(s),\\
\det A_0&>0,\\
(\operatorname{tr}A_0)^2&<4\det A_0.
\end{aligned}
}
\]

The remaining parallel branch is therefore a twisting skew-line congruence constrained simultaneously by the weighted harmonic-director equation and CE-H strain/Laplacian eigenline conditions.

---

## 16. Next target — straight-line weighted-harmonic compatibility

The next calculation is to substitute the exact Riccati/line profile into

\[
\nabla\cdot(\rho^2\nabla\xi)
+\rho^2|\nabla\xi|^2\xi=0
\]

and determine whether a globally nonfocusing rank-two skew-line congruence can satisfy the weighted harmonic-director equation with finite three-dimensional enstrophy.

This is the **Straight-Line Weighted Harmonic Gate (SLWHG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
