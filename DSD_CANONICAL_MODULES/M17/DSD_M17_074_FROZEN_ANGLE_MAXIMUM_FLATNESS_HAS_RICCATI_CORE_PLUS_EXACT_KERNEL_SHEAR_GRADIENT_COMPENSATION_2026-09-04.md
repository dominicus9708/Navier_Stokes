# DSD M17-074 — Frozen-angle maximum flatness has a Riccati core plus exact normalized-shear gradient compensation

Date: 2026-09-04
Canonical ID: **M17-074**

Status: **INTERNAL FROZEN-ANGLE RANK-TWO FLATNESS GATE / ON THE `c != 0` PURE-KERNEL BRANCH, A LINEWISE AMPLITUDE CRITICAL POINT HAS `g=D_xi log rho=0`, HENCE `t=div xi=0` AND `a=r k`, WHILE NONORTHOGONALITY LEAVES `b=p k+q n` WITH `p != 0`. DIRECT EUCLIDEAN-FLATNESS CALCULATION FIRST GIVES `D_n q=2q^2-C+(q/r)D_k g-rD_k(p/r)`, `C=D_xi g`. A CRITICAL AUDIT THEN DIFFERENTIATES THE FULL NORMALIZED SHEAR `s:=m/|a|^2=(pr+tq)/(r^2+t^2)` BEFORE SETTING `t=0`; SINCE `D_k t=-D_k g`, THE APPARENT `(q/r)D_k g` TERM CANCELS EXACTLY. THE TRUE CRITICAL LAW IS `D_n q=2q^2-C-rD_k s`. AT THE CRITICAL POINT `rs=p`, SO EQUIVALENTLY `D_n q=2q^2-C-pD_k log|s|`. THUS FROZEN ANGLE DOES NOT SUPPLY A FREE RICCATI ESCAPE: IT MUST PAY THROUGH THE KERNEL GRADIENT OF ONE NORMALIZED SHEAR SCALAR. ON A MAXIMUM `C<0`, AN N-TANGENT SUB-RICCATI ESCAPE REQUIRES `p D_k log|s|>|C|`; ON A TILTED MAXIMUM THE TRUE SURFACE TANGENT ADDS `Theta D_xi q`, AND SURVIVAL REQUIRES `p D_k log|s|-Theta D_xi q>|C|`. THIS CORRECTION STRENGTHENS THE BRANCH REDUCTION AND REMOVES A FALSE INDEPENDENT `D_k g` CHANNEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen-angle pure-kernel critical point

Use the M17-041 pure-kernel frame

\[
(\xi,k,n),
\qquad
D_k\xi=0.
\]

Write

\[
\boxed{b:=D_\xi\xi=p\,k+q\,n,}
\]

\[
\boxed{a:=D_n\xi=r\,k+t\,n.}
\]

The frozen-angle branch has nonzero signed target shear

\[
\boxed{m:=a\cdot b=pr+tq\neq0.}
\]

Define

\[
\boxed{g:=D_\xi\log\rho=-\nabla\cdot\xi.}
\]

M17-041 gives

\[
t=\nabla\cdot\xi,
\]

so

\[
\boxed{t=-g.}
\]

At a linewise amplitude critical point,

\[
\boxed{g=0,}
\]

hence

\[
\boxed{t=0,\qquad a=rk.}
\]

Full rank two requires

\[
r\neq0,
\qquad
q\neq0.
\]

Since at the critical point

\[
m=pr
\]

and the frozen-angle class has `m != 0`,

\[
\boxed{p\neq0.}
\]

---

## 2. General orthonormal connection

Use distinct connection notation

\[
D_\xi k=-p\xi+\alpha n,
\]

\[
D_\xi n=-q\xi-\alpha k,
\]

\[
D_k k=\gamma_k n,
\qquad
D_k n=-\gamma_k k,
\]

\[
D_n k=-r\xi+\delta n,
\]

\[
D_n n=-t\xi-\delta k.
\]

At the critical point `t=0`, but directional derivatives of `t` are retained.

---

## 3. Flatness R(xi,k)xi = 0

Euclidean flatness gives at `t=0`

\[
\boxed{
D_kp=q\gamma_k+p^2-\alpha r,
}
\]

and

\[
\boxed{
D_kq=p(q-\gamma_k).
}
\]

These are derived without imposing any orthogonal-stretch relation.

---

## 4. Flatness R(k,n)xi = 0

The two target components give

\[
\boxed{
D_kr-rp+\delta r=0,
}
\]

and

\[
\boxed{
D_kt+r(\gamma_k-q)=0.
}
\]

Because

\[
t=-g,
\]

we have

\[
D_kt=-D_kg.
\]

Therefore

\[
\boxed{
\gamma_k=q+\frac{D_kg}{r},
}
\]

and

\[
\boxed{
\delta=p-\frac{D_kr}{r}.
}
\]

Consequently

\[
\boxed{
D_kq=-\frac prD_kg.
}
\]

---

## 5. Flatness R(xi,n)xi = 0

The `n` component of flatness gives

\[
\boxed{
D_nq=r\alpha+D_\xi t-p\delta+q^2.
}
\]

Let

\[
\boxed{C:=D_\xi g.}
\]

Since `t=-g`,

\[
D_\xi t=-C.
\]

Using the previous flatness identities and eliminating `alpha`, `gamma_k`, and `delta` gives

\[
\boxed{
D_nq
=2q^2-C
+\frac qrD_kg
-rD_k\left(\frac pr\right).
}
\]

This is the correct first flatness reduction.

---

## 6. Define the globally meaningful normalized shear

The pointwise critical identity

\[
\frac pr=\frac{m}{|a|^2}
\]

must not be differentiated as though it held in a neighborhood.

Instead define the full scalar field

\[
\boxed{
s:=\frac{m}{|a|^2}
=\frac{pr+tq}{r^2+t^2}.
}
\]

At the critical point `t=0`,

\[
\boxed{s=\frac pr.}
\]

But its `k` derivative must be computed from the full expression before setting `t=0`.

---

## 7. Exact derivative relation and cancellation

Differentiate

\[
s=\frac{pr+tq}{r^2+t^2}
\]

along `k` and then set `t=0`.

The numerator derivative is

\[
D_k(pr+tq)
=rD_kp+pD_kr+qD_kt.
\]

The denominator derivative is

\[
D_k(r^2+t^2)=2rD_kr.
\]

Therefore

\[
\begin{aligned}
D_ks
&=\frac1{r^2}
\left(
 rD_kp+pD_kr+qD_kt
\right)
-rac{pr}{r^4}(2rD_kr)\\
&=D_k\left(\frac pr\right)
+\frac q{r^2}D_kt.
\end{aligned}
\]

Since

\[
D_kt=-D_kg,
\]

we obtain

\[
\boxed{
D_ks
=D_k\left(\frac pr\right)
-\frac q{r^2}D_kg.
}
\]

Equivalently,

\[
\boxed{
D_k\left(\frac pr\right)
=D_ks+\frac q{r^2}D_kg.
}
\]

Substitute this into Section 5:

\[
\begin{aligned}
\frac qrD_kg
-rD_k\left(\frac pr\right)
&=\frac qrD_kg-rD_ks-\frac qrD_kg\\
&=-rD_ks.
\end{aligned}
\]

Thus the apparent `D_k g` channel cancels exactly.

---

## 8. Canonical frozen-angle critical flatness law

The exact critical law is therefore

\[
\boxed{
D_nq
=2q^2-C-rD_ks.
}
\]

At the critical point,

\[
s=\frac pr,
\]

so

\[
rs=p.
\]

Because `s != 0` on the frozen-angle branch,

\[
D_ks=sD_k\log|s|.
\]

Hence

\[
\boxed{
D_nq
=2q^2-C-pD_k\log|s|.
}
\]

This is the final **frozen-angle normalized-shear Riccati law**.

---

## 9. Maximum event and the exact compensation cost

At a nondegenerate linewise amplitude maximum,

\[
\boxed{C=D_\xi g<0.}
\]

Therefore

\[
D_nq
=2q^2+|C|-pD_k\log|s|.
\]

Define

\[
\boxed{
\chi_k:=D_k\log|s|.
}
\]

Then

\[
\boxed{
D_nq=2q^2+|C|-p\chi_k.
}
\]

The three exact regimes are:

### super-Riccati

\[
\boxed{p\chi_k<|C|
\Longrightarrow
D_nq>2q^2;}
\]

### exact Riccati

\[
\boxed{p\chi_k=|C|
\Longrightarrow
D_nq=2q^2;}
\]

### sub-Riccati

\[
\boxed{p\chi_k>|C|
\Longrightarrow
D_nq<2q^2.}
\]

Thus nonzero frozen-angle shear alone does not weaken Riccati focusing.
Its **kernel logarithmic gradient** must have the correct sign and sufficient magnitude.

---

## 10. Complete n-tangent maximum component

If

\[
D_ng=0,
\]

then `n` is tangent to the maximum critical surface.

Along a complete `n`-integral curve remaining in the maximum component, if

\[
p\chi_k\le|C|
\]

through the relevant interval, then

\[
D_nq\ge2q^2.
\]

The reciprocal comparison of M17-048 gives a finite signed-distance obstruction.

Therefore any complete n-tangent frozen-angle maximum survivor must enter

\[
\boxed{p\chi_k>|C|}
\]

before the Riccati focal distance, or exit by critical/rank/interface degeneration.

---

## 11. Tilted maximum surface

For a general regular maximum define

\[
A:=D_ng,
\qquad
\Theta:=\frac{A}{-C}.
\]

The true in-surface tangent direction is

\[
\boxed{T=n+\Theta\xi.}
\]

Therefore

\[
D_Tq
=D_nq+\Theta D_\xi q.
\]

Using Section 8,

\[
\boxed{
D_Tq
=2q^2-C-p\chi_k+\Theta D_\xi q.
}
\]

On a maximum, `-C=|C|`, so the tangent excess over Riccati is

\[
\boxed{
\mathcal K_{FA}
:=|C|-p\chi_k+\Theta D_\xi q.
}
\]

A genuinely sub-Riccati tangent maximum requires

\[
\boxed{
\mathcal K_{FA}<0,
}

or equivalently

\[
\boxed{
p\chi_k-\Theta D_\xi q>|C|.}
\]

This is the complete local frozen-angle maximum compensation law.

---

## 12. Orthogonal limit cross-audit

On the orthogonal branch

\[
m=0,
\]

so the normalized shear field `s` is absent and the present frozen-angle reduction is not divided through `s`.

Instead the orthogonal flatness calculation of M17-047 applies directly and gives

\[
D_nq=2q^2-C.
\]

Thus the `c != 0` formula should not be naively continued through `s=0` by taking `log|s|`.
The branches meet only through the corresponding rank/angle-interface analysis.

---

## 13. DSD analysis

The original frozen-angle maximum appeared to possess two additional spatial channels,

\[
D_kg
\quad\text{and}\quad
D_k(p/r).
\]

The full derivative audit shows that these are not independent.
They recombine into the single descriptor

\[
\boxed{
\chi_k
=D_k\log\left|\frac{m}{|a|^2}\right|.
}
\]

Hence the local maximum geometry is

\[
\boxed{
\text{Riccati core}
+
\text{one normalized-shear gradient}
+
\text{surface tilt}.
}
\]

This is a substantial dimensional reduction of the frozen-angle escape.

---

## 14. DSD audit

### Audit A — differentiating the critical identity p/r = m/|a|^2 off the critical set
Corrected. The full fields `m=pr+tq` and `|a|^2=r^2+t^2` are differentiated before setting `t=0`.

### Audit B — counting D_k g as a second independent compensation channel
Rejected. It cancels exactly after the full normalized-shear derivative is used.

### Audit C — importing the orthogonal relation into c != 0
Rejected. The frozen-angle flatness system is independently derived.

### Audit D — confusing connection coefficients with strain shear
Avoided by distinct notation.

### Audit E — claiming nonzero shear itself weakens the Riccati slope
Rejected. Only `D_k log|s|` enters.

### Audit F — proof status
The frozen-angle maximum branch is sharply reduced but remains open through normalized-shear-gradient recharge and tilt/interface exits.

---

## 15. Updated frozen-angle maximum frontier

Let

\[
\boxed{s:=m/|a|^2,\qquad \chi_k:=D_k\log|s|.}
\]

Then

\[
\boxed{
R_{max}^{frozen-angle}
\Longrightarrow
R_{max}^{p\chi_k-\Theta D_\xi q>|C|}
\ \lor\
T_{crit/rank/interface}.
}
\]

The remaining local frozen-angle escape is one normalized-shear-gradient scalar plus the already identified surface-tilt channel.

---

## 16. Next target — normalized-shear material recharge

M17-041 already gives material multiplier laws for `m` and `|a|`.
Therefore the next calculation can derive an exact material law for

\[
s=m/|a|^2
\]

and for its kernel derivative

\[
\chi_k=D_k\log|s|.
\]

This will determine whether recurrent Riccati compensation requires a fixed mean recharge, analogous to M17-064's oblique `kappa_3` half-slope law.

This is the **Normalized Shear Recharge Gate (NSRG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
