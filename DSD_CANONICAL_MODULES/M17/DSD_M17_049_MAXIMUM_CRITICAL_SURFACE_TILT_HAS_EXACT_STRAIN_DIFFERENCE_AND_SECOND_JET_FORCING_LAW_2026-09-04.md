# DSD M17-049 — Maximum critical-surface tilt has an exact strain-difference and second-jet forcing law

Date: 2026-09-04
Canonical ID: **M17-049**

Status: **INTERNAL TILTED-MAXIMUM DYNAMICS / FOR `g=D_xi log rho`, DEFINE AT A NONDEGENERATE MAXIMUM `A=D_n g` AND `C=D_xi g<0`. USING THE EXACT PURE-KERNEL FRAME ROTATION FROM M17-033 AND THE M17-040 LAW `D_B g=D_xi(sigma+kappa)-(sigma+1/2)g`, THE MATERIAL DERIVATIVES ARE `D_B A=D_nD_xi(sigma+kappa)-2 beta D_k g+(sigma_k-1)A` AND `D_B C=D_xi^2(sigma+kappa)-2(sigma+1/2)C`. THE VORTICITY-INDUCED TRANSVERSE FRAME ROTATION CANCELS EXACTLY. FOR NONZERO TILT `Theta=A/(-C)`, THE MULTIPLICATIVE PART OF `D_B log|Theta|` IS `sigma-sigma_n`, THE SAME STRAIN DIFFERENCE THAT DRIVES THE ORTHOGONAL STRETCH RATIO, PLUS EXPLICIT SECOND-JET FORCING FROM `sigma+kappa` AND THE CRITICAL-SURFACE SHEAR TERM `beta D_k g`. THUS TILT IS NOT A FREE ESCAPE; IT IS COUPLED TO THE EXISTING ANISOTROPY CHANNEL. BECAUSE CRITICAL POINTS MOVE RELATIVE TO MATERIAL LABELS, THE FULL CRITICAL-POINT EVOLUTION ALSO CONTAINS THE KNOWN `v_rel D_xi` CORRECTION AND IS NOT YET CLOSED. GLOBAL REGULARITY REMAINS UNPROVED.**

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

## 3. Input: pure-kernel frame rotation

M17-033 gives

\[
D_B\xi=0,
\]

and, with

\[
\beta:=n\cdot\Sigma k,
\]

and signed transverse vorticity rotation `r_W`,

\[
\boxed{D_Bn=-(\beta+r_W)k.}
\]

Also

\[
(\nabla B)n
=(\beta-r_W)k
+\left(\sigma_n+\frac12\right)n.
\]

For the vortex direction,

\[
\boxed{
(\nabla B)\xi
=\left(\sigma+\frac12\right)\xi.
}
\]

---

## 4. General directional-gradient commutator

For a scalar `f` and a time-dependent unit vector `e`,

\[
D_B(D_ef)
=D_e(D_Bf)
+\left[D_Be-(\nabla B)e\right]\cdot\nabla f.
\]

For `e=n`, Sections 2--3 give

\[
D_Bn-(\nabla B)n
=-2\beta k
-\left(\sigma_n+\frac12\right)n.
\]

The antisymmetric rotation `r_W` cancels exactly.

Hence

\[
\boxed{
D_B(D_nf)
=D_n(D_Bf)
-2\beta D_kf
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
-2\beta D_kg
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
-2\beta D_kg
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
-2\beta D_kg
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
&+\frac{D_nD_\xi(\sigma+\kappa)-2\beta D_kg}{A}\\
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
\text{stretch anisotropy drift}
\quad\text{and}\quad
\text{critical-surface tilt drift}
}
\]

share one material strain channel.

Tilt is therefore not an independent geometric escape variable.
Its additional freedom lies only in the explicit second-jet forcing terms involving `sigma+kappa` and `D_k g`.

---

## 9. Critical flatness substitution for beta

M17-047 gives at a cross-aligned critical point

\[
\boxed{
\beta=q+\frac{D_kg}{r}.
}
\]

Hence the shear forcing may be written

\[
\boxed{
-2\beta D_kg
=-2qD_kg
-\frac{2(D_kg)^2}{r}.
}
\]

This term has no universal sign because `r` is signed, but it is fully local critical-jet data rather than an unspecified frame rotation.

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

### Audit E — proof status
Tilt is coupled to the existing stretch channel but remains an open recurrent escape.

---

## 12. Updated tilted-maximum frontier

A recurrent tilted maximum must maintain

\[
\boxed{
\Theta\ne0,
}

while satisfying simultaneously

\[
\boxed{
D_B\log(|a|/|b|)=\sigma-\sigma_n,
}

and

\[
\boxed{
D_B\log|\Theta|
=(\sigma-\sigma_n)+\mathcal F_{crit}^{(2)},
}
\]

where

\[
\boxed{
\mathcal F_{crit}^{(2)}
:=
\frac{D_nD_\xi(\sigma+\kappa)-2\beta D_kg}{A}
-
\frac{D_\xi^2(\sigma+\kappa)}{C}.
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

This isolates the genuinely new critical-surface forcing from the already known stretch anisotropy.

---

## 13. Next target

The new independent Rank-2 descriptor is not the tilt itself but

\[
\boxed{
\mathcal F_{crit}^{(2)}.
}
\]

The next useful audit is to determine whether its recurrence can be linked to the amplitude multiplier `kappa`, the negative-`kappa` ridge cost of M17-027, or a finite-jet critical degeneration.

In parallel, M17-046 leaves the Rank-1 cubic far-pressure locking problem as a source-production / shell-turnover / relative-transport balance.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
