# DSD M17-073 — The critical gradient ratio has exact n-transport; tilt compensation is a sharp stretch-Hessian inequality

Date: 2026-09-04
Canonical ID: **M17-073**

Status: **INTERNAL CRITICAL GRADIENT-RATIO FLATNESS GATE / ON A CROSS-ALIGNED ORTHOGONAL-STRETCH LINE MAXIMUM, M17-072'S STRAIN-FREE DESCRIPTOR `Lambda=|L/C|`, WITH `L=D_xi q` AND `C=D_xi g<0`, IS NOT SPATIALLY FREE. DIFFERENTIATING THE AUDITED M17-047 FLATNESS LAW `D_n q=2q^2-C` ALONG `xi` AND RETAINING THE NONCOMMUTING FRAME GIVES `D_nL=5qL-D_xi C`. A PARALLEL COMMUTATOR CALCULATION GIVES `D_nC=D_xi A+qC+(alpha+r)D_k g`, WITH `alpha=q^2/r`, SO `D_n log Lambda` IS AN EXPLICIT NEXT-JET EXPRESSION. MORE IMPORTANTLY, THE EXACT WEIGHTED-HARMONIC LINE LAW `D_xi d=-E g` CONVERTS THE CRITICAL AMPLITUDE JETS TO STRETCH-DEFECT HESSIAN JETS: `C=-(D_xi^2 d)/E` AND `A=-(D_nD_xi d)/E`. THEREFORE A LINEWISE AMPLITUDE MAXIMUM IS SIMULTANEOUSLY A STRICT LINEWISE MINIMUM OF `d`, AND THE M17-071 SUB-RICCATI SURVIVAL CONDITION `-A L/C^2>1` BECOMES THE SHARP PURE STRETCH/CURVATURE INEQUALITY `E (D_xi q)(D_nD_xi d) > (D_xi^2 d)^2`. THE TILTED ESCAPE IS THUS A STRONG MIXED-HESSIAN PAYMENT, NOT AN ARBITRARY SURFACE ORIENTATION. NO UNIVERSAL SIGN OF THE NEXT JETS IS YET AVAILABLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Maximum critical notation

Use the orthogonal pure-kernel critical frame

\[
D_k\xi=0,
\qquad
D_\xi\xi=q\,n,
\qquad
D_n\xi=r\,k
\]

at a nondegenerate linewise amplitude maximum.

Define

\[
\boxed{g:=D_\xi\log\rho,}
\]

with

\[
\boxed{g=0,
\qquad
C:=D_\xi g<0.}
\]

Let

\[
\boxed{A:=D_ng}
\]

and

\[
\boxed{L:=D_\xi q.}
\]

The M17-072 strain-free gradient ratio is

\[
\boxed{
\Lambda:=\left|\frac LC\right|.
}
\]

---

## 2. Flatness input

M17-047 proves at every such critical point

\[
\boxed{
D_nq=2q^2-C.
}
\]

It also gives

\[
\boxed{D_kq=0}
\]

and the connection coefficient

\[
\boxed{
\alpha=\frac{q^2}{r}
}
\]

in

\[
D_\xi n=-q\xi-\alpha k.
\]

At the same point

\[
D_n\xi=rk.
\]

Therefore the directional commutator is

\[
\boxed{
[\xi,n]
=-q\xi-(\alpha+r)k.
}
\]

---

## 3. Exact n-transport of L = D_xi q

Apply `D_xi` to the flatness law:

\[
D_\xi D_nq
=4qL-D_\xi C.
\]

For a scalar,

\[
D_\xi D_nq-D_nD_\xi q
=[\xi,n]q.
\]

Using Section 2,

\[
[\xi,n]q
=-qL-(\alpha+r)D_kq.
\]

But

\[
D_kq=0.
\]

Hence

\[
4qL-D_\xi C-D_nL=-qL.
\]

Therefore

\[
\boxed{
D_nL
=5qL-D_\xi C.
}
\]

This is the first exact spatial transport law for the numerator of `Lambda`.

---

## 4. Exact n-transport of C = D_xi g

Use

\[
A=D_ng.
\]

The scalar commutator gives

\[
D_\xi A-D_nC
=[\xi,n]g.
\]

At the critical point,

\[
[\xi,n]g
=-qC-(\alpha+r)D_kg.
\]

Therefore

\[
\boxed{
D_nC
=D_\xi A
+qC
+(\alpha+r)D_kg.
}
\]

Since

\[
\alpha+r
=\frac{q^2}{r}+r
=\frac{q^2+r^2}{r},
\]

and at the cross-aligned critical point

\[
E=q^2+r^2,
\]

we get

\[
\boxed{
D_nC
=D_\xi A+qC+\frac ErD_kg.
}
\]

---

## 5. Exact n-law for the strain-free gradient ratio

Where `L != 0`,

\[
D_n\log\Lambda
=\frac{D_nL}{L}-\frac{D_nC}{C}.
\]

Insert Sections 3--4:

\[
\boxed{
D_n\log\Lambda
=
4q
-\frac{D_\xi C}{L}
-\frac{D_\xi A}{C}
-\frac Er\frac{D_kg}{C}.
}
\]

Thus the M17-072 strain-free material descriptor also has an exact spatial transport law.

No universal sign appears because the next jets

\[
D_\xi C,
\quad
D_\xi A,
\quad
D_kg
\]

remain signed.

---

## 6. Weighted-harmonic line law converts g to the stretch defect

M17-038 gives the exact orthogonal-stretch identity

\[
\boxed{
D_\xi d=-E g,
}
\]

where

\[
\boxed{
d:=\frac{|b|^2-|a|^2}{2}.}
\]

At a critical point `g=0`,

\[
\boxed{D_\xi d=0.}
\]

Differentiate once more along `xi`:

\[
D_\xi^2d
=-(D_\xi E)g-E D_\xi g.
\]

At `g=0`,

\[
\boxed{
D_\xi^2d=-EC.
}
\]

Therefore

\[
\boxed{
C=-\frac{D_\xi^2d}{E}.
}
\]

At a linewise amplitude maximum,

\[
C<0,
\]

so

\[
\boxed{D_\xi^2d>0.}
\]

Thus every nondegenerate amplitude maximum is simultaneously a **strict linewise minimum of the signed stretch defect `d`**.

Similarly, a linewise amplitude minimum is a strict linewise maximum of `d`.

---

## 7. The tilt numerator is a mixed stretch-Hessian jet

Differentiate

\[
g=-\frac{D_\xi d}{E}
\]

along `n`.
At the critical point

\[
D_\xi d=0,
\]

so all derivatives of `1/E` multiplying `D_xi d` vanish.
Hence

\[
\boxed{
A=D_ng
=-\frac{D_nD_\xi d}{E}.
}
\]

Therefore the critical-surface tilt is

\[
\Theta=rac{A}{-C}
\]

or

\[
\boxed{
\Theta
=-\frac{D_nD_\xi d}{D_\xi^2d}.
}
\]

The tilt is exactly a ratio of mixed and pure linewise Hessian components of the stretch defect.

---

## 8. L is constrained by the first stretch derivative

At the cross-aligned critical point,

\[
|b|^2=q^2,
\qquad
|a|^2=r^2.
\]

Although cross alignment is only pointwise, differentiating the full norms at the point is legitimate:

\[
D_\xi |b|^2
=2qD_\xi q
=2qL,
\]

because the other component `p` vanishes there.

Likewise

\[
D_\xi |a|^2
=2rD_\xi r
\]

because the other component `t` vanishes there.

Therefore

\[
D_\xi d
=qL-rD_\xi r.
\]

At the critical point `D_xi d=0`, so

\[
\boxed{
qL=rD_\xi r.
}
\]

Hence

\[
\boxed{
L=\frac rqD_\xi r.
}
\]

on the full-rank critical class.

---

## 9. Lambda in pure stretch-jet form

Use Sections 6 and 8:

\[
\Lambda
=\left|\frac LC\right|
=
\frac{E|L|}{D_\xi^2d}
\]

at a maximum, since `D_xi^2 d>0`.

Thus

\[
\boxed{
\Lambda
=
\frac{E}{D_\xi^2d}
\left|
\frac rqD_\xi r
\right|.
}
\]

This writes the strain-free critical gradient ratio entirely in director/stretch spatial jets.

---

## 10. Compensation strength becomes a sharp Hessian inequality

M17-072 defines

\[
\mathcal R_{comp}
=-\frac{AL}{C^2}.
\]

Insert

\[
A=-\frac{D_nD_\xi d}{E},
\qquad
C=-\frac{D_\xi^2d}{E}.
\]

Then

\[
\boxed{
\mathcal R_{comp}
=
\frac{
E L D_nD_\xi d
}{
(D_\xi^2d)^2
}.
}
\]

The sub-Riccati survival condition

\[
\mathcal R_{comp}>1
\]

is therefore exactly

\[
\boxed{
E(D_\xi q)(D_nD_\xi d)
>
(D_\xi^2d)^2.
}
\]

This is the central CGRFG result.

---

## 11. Immediate sign consequence

Because

\[
E>0
\]

and

\[
(D_\xi^2d)^2>0,
\]

the compensation inequality forces

\[
\boxed{
(D_\xi q)(D_nD_\xi d)>0.
}
\]

Equivalently, since

\[
A=-\frac{D_nD_\xi d}{E},
\]

we recover

\[
A D_\xi q<0.
\]

Thus the mixed stretch Hessian and vortex-curvature gradient must have the **same** sign, while the original tilt numerator and vortex-curvature gradient have opposite signs.

---

## 12. Geometric meaning

At a maximum, `d` has positive linewise curvature

\[
D_\xi^2d>0.
\]

To prevent the maximum sheet from inheriting the Riccati focusing of M17-048, its mixed Hessian must be strong enough that

\[
\boxed{
D_nD_\xi d
}
\]

coupled with

\[
D_\xi q
\]

beats the square of this positive linewise curvature.

Symbolically,

\[
\boxed{
\text{tilted escape}
\Longrightarrow
\text{mixed stretch Hessian}\times\text{curvature gradient}
>
\text{linewise stretch curvature}^2/E.
}
\]

This is a quantitative geometric payment rather than a free tilt.

---

## 13. DSD analysis

The chain of descriptors is now

\[
\boxed{
\text{amplitude maximum}
\Longleftrightarrow
\text{stretch minimum}
}
\]

at second order, followed by

\[
\boxed{
\text{tilt}
=
-\frac{\text{mixed stretch Hessian}}
{\text{linewise stretch Hessian}},
}
\]

and finally

\[
\boxed{
\text{sub-Riccati survival}
\Longleftrightarrow
\mathcal R_{comp}>1.
}
\]

Thus amplitude, stretch, critical-surface tilt, and Euclidean-flatness compensation are now one coherent finite-jet structure.

---

## 14. DSD audit

### Audit A — differentiating cross alignment as a neighborhood identity
Avoided. Norm derivatives are taken from the full vector norms and evaluated only after the pointwise vanishing components are set to zero.

### Audit B — commuting xi and n derivatives as if the frame were coordinate
Avoided. The full commutator from M17-047 is retained.

### Audit C — confusing amplitude maximum with full spatial maximum
Rejected. The statement is linewise along `xi` and concerns the corresponding linewise stretch minimum.

### Audit D — claiming the Hessian inequality is impossible
Rejected. It is a strong but signed local compatibility condition.

### Audit E — claiming Lambda is spatially invariant because its material multiplier cancels
Rejected. Section 5 gives a nontrivial `n`-transport law.

### Audit F — proof status
The compensated tilted maximum is now a sharp stretch-Hessian branch, but no universal sign/convexity theorem excludes it.

---

## 15. Updated compensated maximum frontier

A nondegenerate full-rank compensated maximum must satisfy

\[
\boxed{
D_\xi d=0,
\qquad
D_\xi^2d>0,
}
\]

\[
\boxed{
\Theta
=-\frac{D_nD_\xi d}{D_\xi^2d},
}

and

\[
\boxed{
E(D_\xi q)(D_nD_\xi d)
>
(D_\xi^2d)^2.
}
\]

Together with the exact `n`-transport law for `Lambda`, this is the current hard local geometry.

---

## 16. Next target

Two natural continuations remain:

1. test whether the strict stretch-Hessian inequality can recur on alternating maximum/minimum networks without forcing `D_xi^2 d=0` degeneracy;
2. audit the separate frozen-angle (`c != 0`) Rank-2 branch, whose irreducible shear has not yet received an equally sharp local flatness inequality.

The second route is structurally independent and is now the higher-value branch-balancing calculation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
