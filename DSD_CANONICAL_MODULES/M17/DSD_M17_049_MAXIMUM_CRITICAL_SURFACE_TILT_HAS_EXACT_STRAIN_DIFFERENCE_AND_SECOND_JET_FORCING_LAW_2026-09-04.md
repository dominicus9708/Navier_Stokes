# DSD M17-049 — Maximum critical-surface tilt has an exact strain-difference and second-jet forcing law

Date: 2026-09-04
Canonical ID: **M17-049**

Status: **INTERNAL TILTED-MAXIMUM DYNAMICS / FOR `g=D_xi log rho`, DEFINE AT A NONDEGENERATE MAXIMUM `A=D_n g` AND `C=D_xi g<0`. USING THE EXACT PURE-KERNEL MATERIAL FRAME ROTATION FROM M17-033 AND THE M17-040 LAW `D_B g=D_xi(sigma+kappa)-(sigma+1/2)g`, THE MATERIAL DERIVATIVES ARE `D_B A=D_nD_xi(sigma+kappa)-2 beta_Sigma D_k g+(sigma_k-1)A` AND `D_B C=D_xi^2(sigma+kappa)-2(sigma+1/2)C`, WHERE `beta_Sigma:=n·Sigma k` IS THE TRANSVERSE STRAIN SHEAR. THE VORTICITY-INDUCED TRANSVERSE FRAME ROTATION CANCELS EXACTLY. FOR NONZERO TILT `Theta=A/(-C)`, THE MULTIPLICATIVE PART OF `D_B log|Theta|` IS `sigma-sigma_n`, THE SAME STRAIN DIFFERENCE THAT DRIVES THE ORTHOGONAL STRETCH RATIO, PLUS EXPLICIT SECOND-JET FORCING FROM `sigma+kappa` AND THE STRAIN-SHEAR TERM `beta_Sigma D_k g`. AUDIT CORRECTION: AN EARLIER VERSION INCORRECTLY IDENTIFIED THIS `beta_Sigma` WITH THE UNRELATED FRAME-CONNECTION COEFFICIENT CALLED `beta` IN M17-047; THAT SUBSTITUTION IS REMOVED. THE MAIN TILT LAW IS UNAFFECTED. BECAUSE CRITICAL POINTS MOVE RELATIVE TO MATERIAL LABELS, THE FULL CRITICAL-POINT EVOLUTION ALSO CONTAINS THE KNOWN `v_rel D_xi` CORRECTION AND IS NOT YET CLOSED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical descriptors

On the orthogonal pure-kernel Rank-2 branch define

\[
\boxed{g:=D_\xi\log\rho.}
\]

At a nondegenerate line maximum,

\[
\boxed{g=0,\qquad C:=D_\xi g<0.}
\]

Define the `n`-tilt numerator

\[
\boxed{A:=D_ng.}
\]

When `A!=0`, define the signed tilt ratio

\[
\boxed{
\Theta:=\frac{A}{-C}.
}
\]

Thus `Theta=0` is the n-tangent maximum class closed in M17-048, while `Theta!=0` is the tilted survivor.

---

## 2. Input: material law for g

M17-040 gives

\[
\boxed{
D_Bg
=D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g.
}
\]

At `g=0`,

\[
D_Bg=D_\xi(\sigma+\kappa).
\]

The moving maximum therefore has relative line velocity

\[
\boxed{
 v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{C}.
}
\]

---

## 3. Input: pure-kernel material frame rotation

M17-033 gives

\[
D_B\xi=0.
\]

Define the **transverse strain shear**

\[
\boxed{
\beta_\Sigma:=n\cdot\Sigma k.
}
\]

Let `r_W` be the signed transverse rotation coefficient of the antisymmetric velocity-gradient part about `xi`.
Then

\[
\boxed{D_Bn=-(\beta_\Sigma+r_W)k.}
\]

Also

\[
(\nabla B)n
=(\beta_\Sigma-r_W)k
+\left(\sigma_n+\frac12\right)n.
\]

For the vortex direction,

\[
\boxed{
(\nabla B)\xi
=\left(\sigma+\frac12\right)\xi.
}
\]

The notation `beta_Sigma` is deliberately distinguished from the unrelated connection coefficient used in M17-047.

---

## 4. General directional-gradient commutator

For a scalar `f` and a time-dependent unit vector `e`,

\[
D_B(D_ef)
=D_e(D_Bf)
+\left[D_Be-(\nabla B)e\right]\cdot\nabla f.
\]

For `e=n`, Section 3 gives

\[
D_Bn-(\nabla B)n
=-2\beta_\Sigma k
-\left(\sigma_n+\frac12\right)n.
\]

The antisymmetric rotation `r_W` cancels exactly.
Hence

\[
\boxed{
D_B(D_nf)
=D_n(D_Bf)
-2\beta_\Sigma D_kf
-\left(\sigma_n+\frac12\right)D_nf.
}
\]

For `e=xi`,

\[
\boxed{
D_B(D_\xi f)
=D_\xi(D_Bf)
-\left(\sigma+\frac12\right)D_\xi f.
}
\]

---

## 5. Exact material law for the tilt numerator A

Set `f=g` in the `n` commutator:

\[
D_BA
=D_n(D_Bg)
-2\beta_\Sigma D_kg
-\left(\sigma_n+\frac12\right)A.
\]

Using

\[
D_Bg
=D_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)g
\]

and evaluating at `g=0`,

\[
D_n(D_Bg)
=D_nD_\xi(\sigma+\kappa)
-\left(\sigma+\frac12\right)A.
\]

Therefore

\[
\boxed{
D_BA
=D_nD_\xi(\sigma+\kappa)
-2\beta_\Sigma D_kg
-(\sigma+\sigma_n+1)A.
}
\]

Trace-free strain gives

\[
\sigma+\sigma_k+\sigma_n=0,
\]

so equivalently

\[
\boxed{
D_BA
=D_nD_\xi(\sigma+\kappa)
-2\beta_\Sigma D_kg
+(\sigma_k-1)A.
}
\]

---

## 6. Exact material law for C = D_xi g

Use the `xi` commutator:

\[
D_BC
=D_\xi(D_Bg)
-\left(\sigma+\frac12\right)C.
\]

At `g=0`,

\[
D_\xi(D_Bg)
=D_\xi^2(\sigma+\kappa)
-\left(\sigma+\frac12\right)C.
\]

Hence

\[
\boxed{
D_BC
=D_\xi^2(\sigma+\kappa)
-2\left(\sigma+\frac12\right)C.
}
\]

---

## 7. Tilt ratio law

Assume

\[
A\ne0,
\qquad
C\ne0.
\]

Then

\[
D_B\log|\Theta|
=\frac{D_BA}{A}-\frac{D_BC}{C}.
\]

Insert Sections 5--6:

\[
\boxed{
\begin{aligned}
D_B\log|\Theta|
={}&(\sigma-\sigma_n)\\
&+\frac{D_nD_\xi(\sigma+\kappa)-2\beta_\Sigma D_kg}{A}\\
&-\frac{D_\xi^2(\sigma+\kappa)}{C}.
\end{aligned}
}
\]

The scalar identity

\[
\boxed{
(\sigma_k-1)+2\left(\sigma+\frac12\right)
=\sigma-\sigma_n
}
\]

produces the first term.

Define

\[
\boxed{
\mathcal F_{crit}^{(2)}
:=
\frac{D_nD_\xi(\sigma+\kappa)-2\beta_\Sigma D_kg}{A}
-
\frac{D_\xi^2(\sigma+\kappa)}{C}.
}
\]

Then

\[
\boxed{
D_B\log|\Theta|
=(\sigma-\sigma_n)+\mathcal F_{crit}^{(2)}.
}
\]

---

## 8. Connection to stretch anisotropy

M17-037 gives for the orthogonal pure-kernel jet magnitude ratio

\[
\boxed{
D_B\log\frac{|a|}{|b|}
=\sigma-\sigma_n.
}
\]

The **same** strain difference is the multiplicative drift of the maximum-surface tilt.
Thus

\[
\boxed{
D_B\log
\left(
\frac{|\Theta|}{|a|/|b|}
\right)
=\mathcal F_{crit}^{(2)}.
}
\]

Tilt is therefore not an independent multiplicative escape variable.
Its additional freedom lies in the explicit second-jet forcing `F_crit^(2)`.

---

## 9. Audit correction — the strain shear is not the M17-047 connection beta

An earlier version of this module stated that M17-047 allowed the substitution

\[
\beta=q+\frac{D_kg}{r}
\]

inside the shear term of Section 7.
That statement conflated two different coefficients which happened to use the same symbol `beta`.

Here

\[
\boxed{
\beta_\Sigma=n\cdot\Sigma k
}
\]

is a **strain tensor component** controlling material frame rotation.

By contrast, M17-047 used a connection coefficient, here renamed

\[
\boxed{
\beta_{conn}:=n\cdot D_k k,
}
\]

and flatness gave

\[
\boxed{
\beta_{conn}=q+\frac{D_kg}{r}
}
\]

at a cross-aligned critical point.

No identity

\[
\beta_\Sigma=\beta_{conn}
\]

has been proved.
Therefore the substitution is invalid and is removed.

This correction does **not** alter Sections 1--8, whose derivation used only `beta_Sigma` from M17-033.

---

## 10. Moving critical-point derivative

The material derivative `D_B` follows a fixed material label.
A nondegenerate maximum moves relative to that label with

\[
 v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{C}.
\]

Therefore the derivative **along the moving maximum point** is

\[
\boxed{
D_{max}:=D_B+v_{rel}D_\xi.
}
\]

Thus

\[
\boxed{
D_{max}\log|\Theta|
=D_B\log|\Theta|
+v_{rel}D_\xi\log|\Theta|.
}
\]

The final term contains the next spatial jet of the critical geometry.
It is not controlled by the present identities.
Hence tilted maximum recurrence is a higher-jet problem, not a closed scalar ODE.

---

## 11. DSD audit

### Audit A — treating n as materially fixed
Rejected. `k,n` may rotate; the exact frame law is used.

### Audit B — retaining vorticity frame rotation in the tilt drift
Rejected by calculation: `r_W` cancels from `D_B(D_n g)`.

### Audit C — treating material-label tilt as critical-point tilt
Separated explicitly by the `v_rel D_xi` correction.

### Audit D — claiming sigma-sigma_n alone controls tilt
Rejected. It is only the multiplicative part; second-jet forcing remains.

### Audit E — identifying strain shear beta_Sigma with a frame-connection coefficient
Rejected and corrected. M17-047's `beta_conn` is geometrically different.

### Audit F — proof status
Tilt is coupled to the existing stretch channel but remains an open recurrent escape.

---

## 12. Updated tilted-maximum frontier

A recurrent tilted maximum must maintain

\[
\boxed{\Theta\ne0}
\]

while satisfying simultaneously

\[
\boxed{
D_B\log(|a|/|b|)=\sigma-\sigma_n,
}

and

\[
\boxed{
D_B\log|\Theta|
=(\sigma-\sigma_n)+\mathcal F_{crit}^{(2)}.
}
\]

Therefore their ratio satisfies

\[
\boxed{
D_B\log
\left(
\frac{|\Theta|}{|a|/|b|}
\right)
=\mathcal F_{crit}^{(2)}.
}
\]

---

## 13. Next target

The independent Rank-2 descriptor is

\[
\boxed{
\mathcal F_{crit}^{(2)}.
}
\]

M17-071 additionally shows that nonzero tilt is useful only when the tangent-Riccati compensation descriptor

\[
\mathcal K_{tilt}=C^2+A D_\xi q
\]

is sufficiently negative.
The next useful audit is to derive the material/moving-critical evolution of that compensation descriptor with the corrected distinction between `beta_Sigma` and all frame-connection coefficients.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
