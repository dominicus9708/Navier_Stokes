# DSD M17-075 — The normalized frozen-angle shear gradient has an exact recharge law and a three-halves recurrence condition

Date: 2026-09-04
Canonical ID: **M17-075**

Status: **INTERNAL NORMALIZED SHEAR RECHARGE GATE / ON THE FROZEN-ANGLE PURE-KERNEL RANK-TWO BRANCH, DEFINE THE NONZERO NORMALIZED SHEAR `s:=m/|a|^2`, WHERE `m=a·b`. M17-041 GIVES `D_B m=(sigma_k-1)m` AND M17-033 GIVES `D_B|a|^2=-2(sigma_n+1/2)|a|^2`, SO `D_B log|s|=sigma_n-sigma`, EXACTLY THE NEGATIVE OF THE ORTHOGONAL STRETCH-RATIO MULTIPLIER. FOR THE KERNEL GRADIENT `chi_k:=D_k log|s|`, THE MATERIAL FRAME LAW `D_B k=(beta_Sigma+r_W)n` AND `(grad B)k=(sigma_k+1/2)k+(beta_Sigma+r_W)n` CANCEL ALL TRANSVERSE ROTATION, GIVING THE CLOSED FORCED COCYCLE `D_B chi_k=D_k(sigma_n-sigma)-(sigma_k+1/2)chi_k`. A UNIFORMLY RECURRENT NONZERO-CHI_K SUBBRANCH WITH THE M17-033 MEAN `mean sigma_k=1` MUST THEREFORE SATISFY `mean[D_k(sigma_n-sigma)/chi_k]=3/2`. AT `chi_k=0`, THE ZERO IS NOT INVARIANT UNLESS `D_k(sigma_n-sigma)=0`. COMBINED WITH M17-074, A MAXIMUM CAN WEAKEN THE RICCATI CORE ONLY IF THIS RECHARGED GRADIENT PAYS `p chi_k > |C|` (OR `p chi_k-Theta D_xi q>|C|` ON A TILTED SURFACE). THUS FROZEN-ANGLE RICCATI ESCAPE REQUIRES A SPECIFIC THREE-HALVES MEAN KERNEL RECHARGE, NOT MERELY NONZERO SHEAR. NO SIGN CONTRADICTION IS YET OBTAINED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen-angle normalized shear

Use the pure-kernel Rank-2 frame

\[
(\xi,k,n),
\qquad
D_k\xi=0.
\]

Let

\[
\boxed{m:=a\cdot b}
\]

be the signed frozen-angle shear, with

\[
a=D_n\xi,
\qquad
b=D_\xi\xi.
\]

On the `c != 0` full-rank branch,

\[
\boxed{m\neq0,
\qquad
|a|>0.}
\]

Define the globally meaningful normalized shear scalar

\[
\boxed{
s:=\frac{m}{|a|^2}.}
\]

Because the denominator is positive and `m` cannot change sign without leaving the frozen-angle full-rank class, `s` remains nonzero on one retained regular material carrier.

---

## 2. Exact material multiplier of s

M17-041 gives

\[
\boxed{
D_Bm=(\sigma_k-1)m.
}
\]

M17-033 gives

\[
\boxed{
D_Ba
=-\left(\sigma_n+\frac12\right)a.
}
\]

Therefore

\[
\boxed{
D_B|a|^2
=-2\left(\sigma_n+\frac12\right)|a|^2.
}
\]

Hence

\[
\begin{aligned}
D_B\log|s|
&=D_B\log|m|-D_B\log|a|^2\\
&=(\sigma_k-1)+2\left(\sigma_n+\frac12\right)\\
&=\sigma_k+2\sigma_n.
\end{aligned}
\]

Trace-free strain gives

\[
\sigma+\sigma_k+\sigma_n=0.
\]

Thus

\[
\boxed{
D_B\log|s|
=\sigma_n-\sigma.
}
\]

This is exact.

---

## 3. Relation to the stretch ratio

M17-037 defines

\[
\mathcal R_s:=\frac{|a|}{|b|}
\]

and gives

\[
\boxed{
D_B\log\mathcal R_s
=\sigma-\sigma_n.
}
\]

Therefore

\[
\boxed{
D_B\log(|s|\mathcal R_s)=0.
}
\]

This is consistent with the frozen target angle.
Indeed

\[
m=|a||b|c
\]

with material-invariant signed `c`, so

\[
\boxed{
s=c\frac{|b|}{|a|}}
\]

up to the fixed orientation convention.

Thus normalized shear is the signed inverse stretch ratio multiplied by the frozen angle.
It is not a new independent material-amplitude channel.

---

## 4. Kernel gradient controlling flatness compensation

M17-074 shows that the only frozen-angle correction to the critical Riccati law is

\[
\boxed{
\chi_k:=D_k\log|s|.
}
\]

At a linewise amplitude maximum,

\[
C:=D_\xi g<0,
\qquad
g=D_\xi\log\rho,
\]

and the exact n-slope is

\[
\boxed{
D_nq
=2q^2+|C|-p\chi_k.
}
\]

Thus an n-tangent sub-Riccati escape requires

\[
\boxed{p\chi_k>|C|.}
\]

For a tilted maximum surface with

\[
T=n+\Theta\xi,
\]

M17-074 gives

\[
\boxed{
D_Tq
=2q^2+|C|-p\chi_k+\Theta D_\xi q,
}
\]

so sub-Riccati compensation requires

\[
\boxed{
p\chi_k-\Theta D_\xi q>|C|.}
\]

---

## 5. Material frame law for k

M17-033 gives the material rotation of the kernel direction

\[
\boxed{
D_Bk=(\beta_\Sigma+r_W)n,
}
\]

where

\[
\beta_\Sigma:=n\cdot\Sigma k
\]

is the transverse strain shear and `r_W` is the signed transverse antisymmetric rotation coefficient.

On the other hand,

\[
\nabla B=\Sigma+\mathcal R+\frac12I,
\]

so

\[
\boxed{
(\nabla B)k
=\left(\sigma_k+\frac12\right)k
+(\beta_\Sigma+r_W)n.
}
\]

Therefore

\[
\boxed{
D_Bk-(\nabla B)k
=-\left(\sigma_k+\frac12\right)k.
}
\]

The entire transverse material-frame rotation cancels from the directional-gradient commutator.

---

## 6. Exact recharge law for chi_k

For any scalar `u` and moving unit vector `e`,

\[
D_B(D_eu)
=D_e(D_Bu)
+[D_Be-(\nabla B)e]\cdot\nabla u.
\]

Set

\[
u:=\log|s|,
\qquad
e=k.
\]

Section 2 gives

\[
D_Bu=\sigma_n-\sigma.
\]

Section 5 gives the commutator correction.
Therefore

\[
\boxed{
D_B\chi_k
=D_k(\sigma_n-\sigma)
-\left(\sigma_k+\frac12\right)\chi_k.
}
\]

This is the canonical **normalized shear-gradient recharge law**.

---

## 7. Zero-gradient events

At

\[
\chi_k=0,
\]

Section 6 reduces to

\[
\boxed{
D_B\chi_k
=D_k(\sigma_n-\sigma).
}
\]

Hence:

- if `D_k(sigma_n-sigma) != 0`, the material carrier crosses the `chi_k=0` state transversely;
- if `D_k(sigma_n-sigma)=0`, the zero is degenerate and requires higher-jet analysis;
- `chi_k=0` is not an invariant material subbranch merely because the normalized shear itself is nonzero.

Thus frozen angular shear and its kernel gradient have sharply different persistence properties.

---

## 8. Logarithmic law on the nonzero-gradient branch

Where

\[
\chi_k\neq0,
\]

we may divide Section 6 by `chi_k`:

\[
\boxed{
D_B\log|\chi_k|
=-\left(\sigma_k+\frac12\right)
+
\frac{D_k(\sigma_n-\sigma)}{\chi_k}.
}
\]

The first term is a strict homogeneous decay on the recurrent resonant frame; the second is the exact recharge rate.

---

## 9. Three-halves recurrent recharge law

Assume a uniformly regular recurrent frozen-angle subbranch with

\[
0<c_\chi\le|\chi_k|\le C_\chi<\infty.
\]

Recurrence of `chi_k` gives zero long-time logarithmic drift:

\[
0
=-\left\langle\sigma_k+\frac12\right\rangle
+
\left\langle
\frac{D_k(\sigma_n-\sigma)}{\chi_k}
\right\rangle.
\]

M17-033 gives

\[
\boxed{\langle\sigma_k\rangle=1.}
\]

Therefore

\[
\boxed{
\left\langle
\frac{D_k(\sigma_n-\sigma)}{\chi_k}
\right\rangle
=\frac32.
}
\]

This is the Rank-2 frozen-angle analogue of M17-064's oblique Rank-1 half-slope recharge law.

---

## 10. Homogeneous nonzero chi_k cannot recur without recharge

If the kernel strain-difference gradient vanished identically along the marked branch,

\[
D_k(\sigma_n-\sigma)=0,
\]

then

\[
D_B\chi_k
=-\left(\sigma_k+\frac12\right)\chi_k.
\]

The recurrent mean exponent is

\[
-\left(1+\frac12\right)
=-\frac32.
\]

Therefore a nonzero continuous `chi_k` could not recur.

Thus any recurrent frozen-angle maximum that uses kernel-shear-gradient Riccati compensation must repeatedly recharge that gradient through

\[
\boxed{D_k(\sigma_n-\sigma).}
\]

---

## 11. Relation to the material stretch cycle

The material scalar `s` itself is already locked to inverse stretch:

\[
D_B\log|s|
=-(D_B\log\mathcal R_s).
\]

But the spatial derivative `chi_k` has an additional homogeneous decay

\[
-\left(\sigma_k+\frac12\right),
\]

which is not removed by recurrence of the stretch ratio.

Thus the frozen-angle branch has the hierarchy

\[
\boxed{
\text{frozen target angle}
\to
\text{inverse stretch }s
\to
\text{kernel gradient }\chi_k
\to
\text{strain-gradient recharge}.
}
\]

The Riccati escape sits at the third level, not at the first two.

---

## 12. Moving critical-network caveat

The law of Section 6 follows one material label.
A line maximum generally moves relative to material vortex labels with M17-040 velocity

\[
\boxed{
v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{D_\xi g}.
}
\]

Therefore along the moving maximum point,

\[
\boxed{
D_{max}\chi_k
=D_B\chi_k+v_{rel}D_\xi\chi_k.
}
\]

The same-marker three-halves law applies to a uniformly recurrent material carrier with nonzero `chi_k`.
For recurrence of the moving critical network, the additional spatial-advection term must be included.

This distinction is retained explicitly.

---

## 13. DSD analysis

The frozen-angle branch initially seemed to gain an arbitrary off-diagonal shear escape.
The audit now reduces it to one forced scalar hierarchy:

\[
\boxed{
m
\to
s=m/|a|^2
\to
\chi_k=D_k\log|s|
\to
D_k(\sigma_n-\sigma).
}
\]

The only local scalar capable of paying the maximum Riccati excess is `chi_k`, and its recurrence requires an exact mean recharge of `3/2` on the nonzero-gradient same-marker branch.

---

## 14. DSD audit

### Audit A — counting s as independent of stretch ratio
Rejected. It is the frozen-angle signed inverse stretch ratio.

### Audit B — assuming the material frame rotation forces extra terms in D_B chi_k
Rejected. The strain-shear and antisymmetric rotations cancel exactly in the commutator.

### Audit C — claiming nonzero m implies nonzero chi_k
Rejected. Spatially uniform normalized shear has `chi_k=0`.

### Audit D — dividing by chi_k across zero events
Avoided. The logarithmic/recurrent law is restricted to the uniformly nonzero-gradient subbranch.

### Audit E — applying the same-marker mean law directly to a moving maximum network
Rejected. The `v_rel D_xi` correction is separate.

### Audit F — proof status
The frozen-angle Riccati escape is substantially narrowed but remains open through explicit strain-gradient recharge and critical-network transport.

---

## 15. Updated frozen-angle frontier

On a recurrent full-rank frozen-angle material subbranch,

\[
\boxed{
D_B\chi_k
=D_k(\sigma_n-\sigma)
-\left(\sigma_k+\frac12\right)\chi_k.
}
\]

If `chi_k` stays uniformly nonzero and recurrent,

\[
\boxed{
\left\langle
\frac{D_k(\sigma_n-\sigma)}{\chi_k}
\right\rangle
=\frac32.
}
\]

At a maximum, Riccati compensation additionally requires

\[
\boxed{
p\chi_k-\Theta D_\xi q>|C|.}
\]

Thus the hard frozen-angle maximum survivor must satisfy both a **spatial sign/magnitude payment** and a **material recharge payment**.

---

## 16. Next target

The next useful test is to put the moving-critical correction into the same normalized recharge variable and determine whether a recurrent maximum network can keep

\[
p\chi_k-\Theta D_\xi q>|C|
\]

while repeatedly servicing the `3/2` material recharge.

If no sign theorem emerges, the frozen-angle maximum branch will reach a higher-jet transport firewall analogous to the Rank-1 OGLHG covariance firewall.

In parallel, the orthogonal compensated branch M17-073 has an independent mixed-Hessian payment and should be compared at the final branch-assembly stage.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
