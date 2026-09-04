# DSD M17-079 — A pure-kernel Rank-2 maximum has one unified compensation margin across orthogonal and frozen-angle classes

Date: 2026-09-04
Canonical ID: **M17-079**

Status: **INTERNAL RANK-TWO UNIFIED COMPENSATION GATE / THE ORTHOGONAL MIXED-HESSIAN ESCAPE OF M17-071--073 AND THE FROZEN-ANGLE NORMALIZED-SHEAR ESCAPE OF M17-074--077 ARE NOT TWO UNRELATED LOCAL FLATNESS MECHANISMS. ON THE GENERAL PURE-KERNEL RANK-TWO CRITICAL SET DEFINE THE DIVISION-FREE NORMALIZED SHEAR `s:=m/|a|^2`, WHICH IS ALLOWED TO VANISH. AT ANY REGULAR LINE MAXIMUM `g=D_xi log rho=0`, WRITE `a=r k`, `b=p k+q n`, `C=D_xi g<0`. REPEATING THE M17-074 FULL-FIELD DERIVATIVE WITHOUT ASSUMING `p!=0` GIVES THE ANGLE-UNIFORM FLATNESS LAW `D_n q=2q^2-C-rD_k s`. WITH THE TRUE MAXIMUM-SURFACE TANGENT `T=n+Theta xi`, `Theta=D_ng/(-C)`, THE COMPLETE LOCAL LAW IS `D_Tq=2q^2-M_R2`, WHERE `M_R2:=C+rD_k s-Theta D_xi q`. SUB-RICCATI SURVIVAL IS EXACTLY `M_R2>0`. ON THE EXACT ORTHOGONAL COMPONENT `s identically 0`, THIS REDUCES TO `C-Theta D_xi q>0`, EQUIVALENT TO M17-071'S `A D_xi q<-C^2` AND HENCE M17-073'S MIXED-STRETCH-HESSIAN PAYMENT. ON THE FROZEN-ANGLE COMPONENT `s!=0`, `rD_k s=pD_k log|s|=p chi_k`, RECOVERING M17-074'S `p chi_k-Theta D_xi q>|C|`. THUS THE TWO HARD RANK-TWO MAXIMUM SURVIVORS MERGE INTO ONE DIVISION-FREE COMPENSATION MARGIN; ORTHOGONALITY VERSUS FROZEN ANGLE ONLY SELECTS WHICH TERM PAYS IT. THE MATERIAL LAW `D_Bs=(sigma_n-sigma)s` AND ITS KERNEL-GRADIENT LAW ARE ALSO DIVISION-FREE ACROSS `s=0`, BUT SPATIAL ANGLE-INTERFACES REMAIN A SEPARATE TURNOVER CLASS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. General pure-kernel Rank-2 critical frame

Use the intrinsic Rank-2 frame

\[
(\xi,k,n),
\qquad
D_k\xi=0,
\qquad
n=\xi\times k.
\]

Define the two nonzero director jets

\[
\boxed{
b:=D_\xi\xi,}
\]

\[
\boxed{a:=D_n\xi.}
\]

Write generally

\[
\boxed{
b=p\,k+q\,n,}
\]

\[
\boxed{a=r\,k+t\,n.}
\]

The vorticity-amplitude line derivative is

\[
\boxed{
g:=D_\xi\log\rho.}
\]

Divergence-free vorticity gives

\[
\boxed{t=-g.}
\]

At a regular line maximum,

\[
\boxed{
g=0,
\qquad
C:=D_\xi g<0.}
\]

Therefore

\[
\boxed{t=0,
\qquad
a=rk.}
\]

Full Rank 2 requires

\[
\boxed{r\neq0,
\qquad
q\neq0.}
\]

No assumption is made on `p`.
Thus both

\[
p=0
\]

and

\[
p\neq0
\]

are included.

---

## 2. Division-free normalized shear

Define the signed director shear

\[
\boxed{m:=a\cdot b.}
\]

Instead of using `log|m|` or a frozen-angle-only variable, define the full scalar

\[
\boxed{
s:=\frac{m}{|a|^2}.}
\]

Because full Rank 2 gives `|a|>0`, this scalar is well defined even when

\[
m=0.
\]

In full components,

\[
\boxed{
s
=\frac{pr+tq}{r^2+t^2}.}
\]

At the line maximum `t=0`,

\[
\boxed{s=\frac pr.}
\]

But, as audited in M17-074, this critical equality is used only after differentiating the full field.

---

## 3. General flatness law before the normalized-shear cancellation

The Euclidean-flatness calculation of M17-074 used only the pure-kernel frame and `g=0` until the later frozen-angle specialization.
It gives, without assuming `p!=0`,

\[
\boxed{
D_nq
=2q^2-C
+\frac qrD_kg
-rD_k\left(\frac pr\right).
}
\]

This equation is therefore valid on the full regular pure-kernel critical set.

---

## 4. Full-field derivative of s

Differentiate

\[
s=\frac{pr+tq}{r^2+t^2}
\]

along `k` and only then set `t=0`.

Exactly as in the corrected M17-074 audit,

\[
\boxed{
D_ks
=D_k\left(\frac pr\right)
-\frac q{r^2}D_kg.
}
\]

Hence

\[
\boxed{
D_k\left(\frac pr\right)
=D_ks+\frac q{r^2}D_kg.
}
\]

Substitute into Section 3:

\[
\begin{aligned}
D_nq
&=2q^2-C
+\frac qrD_kg
-rD_ks
-\frac qrD_kg.
\end{aligned}
\]

The amplitude-gradient term cancels exactly:

\[
\boxed{
D_nq
=2q^2-C-rD_ks.
}
\]

This is the **angle-uniform critical flatness law**.

---

## 5. True tangent of the maximum surface

Define

\[
\boxed{A_g:=D_ng.}
\]

At a regular maximum `C<0`, define the signed tilt

\[
\boxed{
\Theta:=\frac{A_g}{-C}.
}
\]

Then

\[
\boxed{T:=n+\Theta\xi}
\]

is tangent to the critical surface `g=0`, because

\[
D_Tg=A_g+\Theta C=0.
\]

Therefore

\[
D_Tq=D_nq+\Theta D_\xi q.
\]

Use Section 4:

\[
\boxed{
D_Tq
=2q^2-C-rD_ks+\Theta D_\xi q.
}
\]

---

## 6. Unified Rank-2 compensation margin

Define

\[
\boxed{
\mathcal M_{R2}
:=C+rD_ks-\Theta D_\xi q.
}
\]

Then the entire maximum-tangent flatness law is

\[
\boxed{
D_Tq
=2q^2-\mathcal M_{R2}.
}
\]

Thus the exact regimes are

### super-Riccati

\[
\boxed{
\mathcal M_{R2}<0
\Longrightarrow
D_Tq>2q^2;
}
\]

### exact Riccati

\[
\boxed{
\mathcal M_{R2}=0
\Longrightarrow
D_Tq=2q^2;
}
\]

### sub-Riccati

\[
\boxed{
\mathcal M_{R2}>0
\Longrightarrow
D_Tq<2q^2.
}
\]

Hence every persistent maximum survivor avoiding the Riccati comparison must service the single signed gate

\[
\boxed{\mathcal M_{R2}>0.}
\]

---

## 7. Orthogonal branch is the s=0 limit

On an exact orthogonal pure-kernel component,

\[
\boxed{m\equiv0.}
\]

Therefore

\[
\boxed{s\equiv0,
\qquad
D_ks=0.}
\]

The unified margin reduces to

\[
\boxed{
\mathcal M_{R2}^{orth}
=C-\Theta D_\xi q.
}
\]

Sub-Riccati survival requires

\[
C-\Theta D_\xi q>0.
\]

Since

\[
\Theta=-\frac{A_g}{C},
\]

we have

\[
C-\Theta D_\xi q
=C+\frac{A_gD_\xi q}{C}
=\frac{C^2+A_gD_\xi q}{C}.
\]

Because `C<0`, positivity is equivalent to

\[
\boxed{
C^2+A_gD_\xi q<0,
}
\]

or

\[
\boxed{
A_gD_\xi q<-C^2.
}
\]

This is exactly M17-071.

---

## 8. Recover the orthogonal mixed-Hessian payment

M17-073 uses the orthogonal weighted-harmonic line law

\[
D_\xi d=-Eg
\]

and at the maximum obtains

\[
\boxed{
C=-\frac{D_\xi^2d}{E},
\qquad
A_g=-\frac{D_nD_\xi d}{E}.
}
\]

Substituting these into Section 7 gives

\[
\boxed{
E(D_\xi q)(D_nD_\xi d)
>(D_\xi^2d)^2.
}
\]

Thus the former orthogonal mixed-Hessian survivor is exactly the `s=0` representation of

\[
\mathcal M_{R2}>0.
\]

---

## 9. Frozen-angle branch is the s!=0 representation

On a retained frozen-angle component,

\[
\boxed{s\neq0.}
\]

At the line maximum

\[
s=\frac pr,
\]

so

\[
rs=p.
\]

Define

\[
\chi_k:=D_k\log|s|.
\]

Then

\[
D_ks=s\chi_k
\]

and therefore

\[
\boxed{rD_ks=p\chi_k.}
\]

The unified margin becomes

\[
\boxed{
\mathcal M_{R2}^{FA}
=C+p\chi_k-\Theta D_\xi q.
}
\]

Since `C<0`, positivity is exactly

\[
\boxed{
p\chi_k-\Theta D_\xi q>|C|,}
\]

which is M17-074.

Thus the former frozen-angle shear-gradient survivor is the `s!=0` representation of the same gate.

---

## 10. Division-free material law for s

M17-041 and M17-033 give

\[
D_Bm=(\sigma_k-1)m
\]

and

\[
D_B|a|^2
=-2\left(\sigma_n+\frac12\right)|a|^2.
\]

Therefore, without dividing by `s`,

\[
\boxed{
D_Bs
=(\sigma_n-\sigma)s.
}
\]

This equation remains regular at

\[
s=0.
\]

Hence the normalized shear scalar itself supplies a material bridge across the algebraic orthogonal limit.

---

## 11. Division-free material law for D_k s

Let

\[
\boxed{w_k:=D_ks.}
\]

For a scalar `s`, the pure-kernel frame commutator gives

\[
D_B(D_ks)
=D_k(D_Bs)
-\left(\sigma_k+\frac12\right)D_ks.
\]

Use Section 10:

\[
D_k(D_Bs)
=sD_k(\sigma_n-\sigma)
+(\sigma_n-\sigma)w_k.
\]

Thus

\[
D_Bw_k
=sD_k(\sigma_n-\sigma)
+\left[
\sigma_n-\sigma-\sigma_k-\frac12
\right]w_k.
\]

Trace-free strain gives

\[
\sigma_n-\sigma-\sigma_k=2\sigma_n.
\]

Therefore

\[
\boxed{
D_Bw_k
=sD_k(\sigma_n-\sigma)
+\left(2\sigma_n-\frac12\right)w_k.
}
\]

This is the division-free kernel-gradient law across `s=0`.

---

## 12. Critical compensation carrier r D_k s

At the line maximum define

\[
\boxed{K_s:=rD_ks.}
\]

Because

\[
D_Br
=-\left(\sigma_n+\frac12\right)r
\]

at `g=0`, Sections 10--11 give

\[
\boxed{
D_BK_s
=pD_k(\sigma_n-\sigma)
+(\sigma_n-1)K_s.
}
\]

On the frozen-angle component this is the division-free form of M17-075/M17-077's `p chi_k` dynamics.

On the exact orthogonal component,

\[
s\equiv0
\quad\Longrightarrow\quad
K_s=0.
\]

---

## 13. Spatial angle-interface caveat

The material equation

\[
D_Bs=(\sigma_n-\sigma)s
\]

shows that a material carrier with `s=0` remains at `s=0` while it remains in the regular pure-kernel description.

However distinct neighboring material labels may carry different frozen target angles.
Therefore a spatial set where

\[
s=0
\]

can also be an interface between nonzero-angle carriers.

The statement

\[
D_ks=0
\]

is used only on an exact orthogonal component where `s` vanishes as a field, not at an arbitrary isolated zero/interface.

This keeps the angle-interface/turnover exit explicit.

---

## 14. DSD interpretation

The previous branch tree suggested two hard Rank-2 maximum mechanisms:

\[
\boxed{
\text{orthogonal tilt / mixed Hessian}
}
\]

and

\[
\boxed{
\text{frozen-angle shear gradient}.
}
\]

The division-free normalized shear shows that these are two descriptions of one geometric compensation margin:

\[
\boxed{
\mathcal M_{R2}
=C+rD_ks-\Theta D_\xi q.
}
\]

The structural split is therefore not at the level of the Riccati gate itself.
It occurs only in how the positive payment is supplied.

---

## 15. DSD audit

### Audit A — extending log|s| through s=0
Rejected. The unified variable is `s`, not `log|s|`.

### Audit B — assuming p!=0 in the flatness derivation
Rejected. The pre-specialization M17-074 calculation remains valid for `p=0`.

### Audit C — differentiating s=p/r off the critical set
Avoided. The full field `s=(pr+tq)/(r^2+t^2)` is differentiated first.

### Audit D — treating every s=0 point as an orthogonal component
Rejected. Spatial angle interfaces are retained separately.

### Audit E — counting orthogonal and frozen-angle local compensation as two independent gates
Rejected. They are two limits of one margin `M_R2`.

### Audit F — proof status
The local Rank-2 maximum branch is substantially unified but not closed.

---

## 16. Updated Rank-2 maximum frontier

The two previous hard local branches can be replaced by

\[
\boxed{
R_{max}^{pure-kernel}
\Longrightarrow
R_{\mathcal M_{R2}>0}
\ \lor\
T_{rank/critical/angle/interface}.
}
\]

where

\[
\boxed{
\mathcal M_{R2}
=C+rD_ks-\Theta D_\xi q.
}
\]

The exact orthogonal and frozen-angle classes are now subrepresentations of this one survivor.

---

## 17. Next target

The next highest-value calculation is no longer a branch-by-branch local flatness derivation.
It is the material/moving evolution of the **unified positive margin** itself.

The question is whether the three payment pieces

\[
C,
\qquad
rD_ks,
\qquad
-\Theta D_\xi q
\]

can be normalized so that their different strain multipliers collapse to one constant-damping law, or whether the tilt term introduces an irreducible higher-jet transport firewall.

This is the **Unified Margin Transport Gate (UMTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
