# DSD M17-074 — Frozen-angle maximum flatness has a Riccati core plus exact kernel shear-gradient compensation

Date: 2026-09-04
Canonical ID: **M17-074**

Status: **INTERNAL FROZEN-ANGLE RANK-TWO FLATNESS GATE / ON THE `c != 0` PURE-KERNEL BRANCH, A LINEWISE AMPLITUDE CRITICAL POINT STILL HAS `g=D_xi log rho=0`, HENCE `t=div xi=0` AND `a=r k`, BUT NONORTHOGONALITY LEAVES `b=p k+q n` WITH `p != 0`; THE PRODUCT `pr` IS THE IRREDUCIBLE SHEAR `m`. RECOMPUTING EUCLIDEAN FLATNESS WITHOUT IMPORTING THE ORTHOGONAL RELATION GIVES THE EXACT CRITICAL LAW `D_n q = 2 q^2 - C + (q/r)D_k g - r D_k(p/r)`, WHERE `C=D_xi g`. THUS THE UNIVERSAL RICCATI CORE `2q^2-C` SURVIVES, WHILE FROZEN-ANGLE SHEAR CONTRIBUTES ONE KERNEL-DIRECTION COMPENSATION `H_k=(q/r)D_k g-rD_k(p/r)`. ON A MAXIMUM `C<0`, AN n-TANGENT COMPLETE CRITICAL CURVE CAN AVOID THE M17-048 RICCATI OBSTRUCTION ONLY IF `H_k<C`, I.E. THE SHEAR/KERNEL GRADIENT MUST BE NEGATIVE ENOUGH TO OVERCOME THE POSITIVE AMPLITUDE-CURVATURE EXCESS `-C`. FOR A TILTED MAXIMUM SURFACE THE TRUE TANGENT `T=n+Theta xi` ADDS THE SAME `Theta D_xi q` CHANNEL AS M17-071, SO THE FULL ESCAPE COST IS `-C+H_k+Theta D_xi q<0`. FROZEN ANGLE IS THEREFORE NOT A FREE GEOMETRIC FIREWALL; IT MUST PAY AN EXPLICIT KERNEL-SHEAR GRADIENT COST OR EXIT THROUGH INTERFACE/DEGENERATION. NO SIGN THEOREM YET FORCES THAT COST TO FAIL / GLOBAL REGULARITY REMAINS UNPROVED.**

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
\boxed{
b:=D_\xi\xi=p\,k+q\,n,}
\]

\[
\boxed{
a:=D_n\xi=r\,k+t\,n.}
\]

The frozen-angle branch has

\[
\boxed{m:=a\cdot b=pr+tq\neq0.}
\]

Define as before

\[
\boxed{g:=D_\xi\log\rho=-\nabla\cdot\xi.}
\]

M17-041 gives

\[
\nabla\cdot\xi=t,
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
\boxed{t=0,
\qquad
a=rk.}
\]

Full rank two requires

\[
r\neq0,
\qquad
q\neq0.
\]

Since `m=pr` at the critical point and the frozen-angle branch has `m != 0`,

\[
\boxed{p\neq0.}
\]

Thus the critical frame is not cross aligned: the `k` component of `b` is the irreducible angular shear.

---

## 2. General orthonormal connection at the critical point

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

At the critical point `t=0`, but derivatives of `t` are not set to zero.

The corresponding commutators are

\[
[\xi,k]
=-p\xi+\alpha n,
\]

\[
[\xi,n]
=-q\xi-(\alpha+r)k,
\]

and

\[
[k,n]
=r\xi-\gamma_k k-\delta n.
\]

---

## 3. Flatness R(xi,k)xi = 0

Compute the Euclidean curvature component

\[
R(\xi,k)\xi=0.
\]

At `t=0`, its `k` and `n` projections give

\[
\boxed{
D_kp
=q\gamma_k+p^2-\alpha r,
}
\]

and

\[
\boxed{
D_kq
=p(q-\gamma_k).
}
\]

Unlike the orthogonal critical branch, the second relation does not yet say `D_kq=0`, because `p != 0`.

---

## 4. Flatness R(k,n)xi = 0

Retain the derivative `D_k t` before setting `t=0`.
The two projections give

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

Since

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
\gamma_k
=q+\frac{D_kg}{r}.
}
\]

Also

\[
\boxed{
\delta
=p-\frac{D_kr}{r}.
}
\]

These are frame-connection identities; neither coefficient is the strain shear `beta_Sigma` of M17-049/M17-072.

---

## 5. Consequences for D_k q and alpha

Substitute the `gamma_k` law into Section 3:

\[
D_kq
=p\left(q-q-\frac{D_kg}{r}\right).
\]

Hence

\[
\boxed{
D_kq
=-\frac prD_kg.
}
\]

The first Section-3 identity gives

\[
\alpha r
=q\gamma_k+p^2-D_kp.
\]

Therefore

\[
\boxed{
\alpha
=\frac{q\gamma_k+p^2-D_kp}{r}.
}

No orthogonal relation between `p` and `g` has been used.

---

## 6. Flatness R(xi,n)xi = 0

At `t=0`, the `n` projection of

\[
R(\xi,n)\xi=0
\]

gives

\[
\boxed{
D_nq
=r\alpha+D_\xi t-p\delta+q^2.
}
\]

Since

\[
D_\xi t=-D_\xi g=-C,
\]

we have

\[
\boxed{
D_nq
=r\alpha-p\delta+q^2-C.
}
\]

Insert Sections 4--5:

\[
\begin{aligned}
D_nq
={}&q\gamma_k+p^2-D_kp\\
&-p\left(p-\frac{D_kr}{r}\right)
+q^2-C.
\end{aligned}
\]

The `p^2` terms cancel:

\[
\boxed{
D_nq
=q\gamma_k+q^2-C
-D_kp+\frac prD_kr.
}
\]

Now use

\[
\gamma_k=q+\frac{D_kg}{r}.
\]

Thus

\[
\boxed{
D_nq
=2q^2-C
+\frac qrD_kg
-D_kp+\frac prD_kr.
}
\]

Finally,

\[
D_kp-\frac prD_kr
=rD_k\left(\frac pr\right).
\]

Therefore the canonical frozen-angle critical flatness law is

\[
\boxed{
D_nq
=2q^2-C
+\frac qrD_kg
-rD_k\left(\frac pr\right).
}
\]

---

## 7. Define the kernel-shear compensation channel

Set

\[
\boxed{
\mathcal H_k
:=
\frac qrD_kg
-rD_k\left(\frac pr\right).
}
\]

Then

\[
\boxed{
D_nq
=2q^2-C+\mathcal H_k.
}
\]

The first two terms are exactly the orthogonal critical Riccati core.
All new frozen-angle freedom has collapsed to one scalar kernel-direction correction `H_k`.

---

## 8. H_k is an irreducible shear-gradient descriptor

At the critical point,

\[
a=rk,
\]

so

\[
|a|^2=r^2.
\]

Also

\[
m=pr.
\]

Hence

\[
\boxed{
\frac pr
=\frac{m}{r^2}
=\frac{m}{|a|^2}.
}
\]

Therefore

\[
\boxed{
\mathcal H_k
=
\frac qrD_kg
-rD_k\left(\frac{m}{|a|^2}\right).
}
\]

The second term is explicitly the kernel gradient of normalized frozen-angle shear.

Thus the nonorthogonal branch can alter the Riccati slope only through

1. kernel variation of the amplitude-criticality scalar `g`;
2. kernel variation of the normalized irreducible shear.

---

## 9. Maximum event: required shear compensation

At a nondegenerate linewise amplitude maximum,

\[
\boxed{C=D_\xi g<0.}
\]

Hence

\[
D_nq
=2q^2+|C|+\mathcal H_k.
\]

Therefore

### super-Riccati n-slope

\[
\boxed{
\mathcal H_k>-|C|
\Longrightarrow
D_nq>2q^2;
}
\]

### exact Riccati n-slope

\[
\boxed{
\mathcal H_k=-|C|
\Longrightarrow
D_nq=2q^2;
}
\]

### sub-Riccati n-slope

\[
\boxed{
\mathcal H_k<-|C|
\Longrightarrow
D_nq<2q^2.
}
\]

Equivalently, since `C=-|C|`, the sub-Riccati condition is

\[
\boxed{
\mathcal H_k<C.
}
\]

Thus frozen-angle shear must pay a finite signed kernel-gradient cost at every maximum if it is to weaken the Riccati core.

---

## 10. n-tangent maximum sheet

If additionally

\[
D_ng=0,
\]

then `n` is tangent to the regular critical surface as in M17-048.

If along a complete `n`-integral curve the maximum condition persists and

\[
\mathcal H_k\ge C,
\]

then

\[
D_nq\ge2q^2.
\]

The reciprocal comparison gives the same finite-parameter obstruction as M17-048.

Therefore a complete n-tangent frozen-angle maximum survivor must enter

\[
\boxed{
\mathcal H_k<C
}
\]

before the Riccati focal distance, or exit through finite interface/rank/critical degeneration.

---

## 11. Tilted maximum surface

For a general regular maximum define

\[
A:=D_ng,
\qquad
\Theta:=\frac{A}{-C}.
\]

As in M17-071, the true in-surface direction is

\[
\boxed{T=n+\Theta\xi.}
\]

Hence

\[
D_Tq
=D_nq+\Theta D_\xi q.
\]

Using Section 7,

\[
\boxed{
D_Tq
=2q^2-C
+\mathcal H_k
+\Theta D_\xi q.
}
\]

Define the total frozen-angle tangent excess

\[
\boxed{
\mathcal K_{FA}
:=-C+\mathcal H_k+\Theta D_\xi q.
}
\]

Then

\[
\boxed{
D_Tq=2q^2+\mathcal K_{FA}.
}
\]

A genuinely sub-Riccati tangent maximum therefore requires

\[
\boxed{
\mathcal K_{FA}<0.
}
\]

---

## 12. Orthogonal limit cross-audit

In the orthogonal branch `m=0` and at a critical point M17-047 gives the additional relation

\[
p=\frac{gq}{r}.
\]

Thus at `g=0`,

\[
p=0
\]

and

\[
D_kp=\frac qrD_kg.
\]

Therefore the two terms in `H_k` cancel:

\[
\boxed{\mathcal H_k=0.}
\]

The frozen-angle flatness law reduces exactly to

\[
D_nq=2q^2-C,
\]

which is M17-047.

Likewise the tilted tangent law reduces exactly to M17-071.

This is an internal cross-audit of the generalization.

---

## 13. DSD analysis

The frozen-angle branch does not erase the universal flatness structure.
Instead it adds exactly one new descriptor:

\[
\boxed{
\mathcal H_k
=
\text{kernel amplitude-criticality gradient}
-
\text{kernel normalized-shear gradient}.
}
\]

The local maximum branch is therefore

\[
\boxed{
\text{Riccati core}
+
\text{kernel shear compensation}
+
\text{surface tilt compensation}.
}
\]

This is the nonorthogonal analogue of the M17-071--073 hierarchy.

---

## 14. DSD audit

### Audit A — importing the orthogonal p=gq/r relation into c != 0
Rejected. The flatness system is recomputed from the general nonorthogonal frame.

### Audit B — setting derivatives of t=0 to zero
Avoided. `D_k t` and `D_xi t` are retained before evaluating the critical point.

### Audit C — confusing frame connection gamma_k with strain shear beta_Sigma
Avoided by distinct notation.

### Audit D — claiming frozen shear automatically compensates Riccati focusing
Rejected. Only the signed gradient `H_k`, not nonzero `m` itself, enters the compensation.

### Audit E — claiming H_k<C is impossible
Rejected. It is a sharp surviving compatibility condition.

### Audit F — proof status
The frozen-angle branch now has an explicit local flatness payment but remains open.

---

## 15. Updated frozen-angle maximum frontier

\[
\boxed{
R_{max}^{frozen-angle}
\Longrightarrow
R_{max}^{\mathcal K_{FA}<0}
\ \lor\
T_{crit/rank/interface}
}
\]

for a complete maximum network after excluding persistent nonnegative tangent excess under the same completeness/bounded-tangent assumptions used in M17-071.

The new hard local quantity is

\[
\boxed{
\mathcal H_k
=
\frac qrD_kg-rD_k(m/|a|^2).
}
\]

---

## 16. Next target

The next useful frozen-angle calculation is to combine `H_k` with the M17-041 weighted-harmonic stress balances and determine whether the same normalized shear derivative already appears there with a constrained coefficient.

If it does, the kernel-shear compensation may reduce to amplitude/anisotropy gradients rather than remain an independent flatness escape.

This is the **Frozen-Angle Stress–Flatness Merge Gate (FASFMG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
