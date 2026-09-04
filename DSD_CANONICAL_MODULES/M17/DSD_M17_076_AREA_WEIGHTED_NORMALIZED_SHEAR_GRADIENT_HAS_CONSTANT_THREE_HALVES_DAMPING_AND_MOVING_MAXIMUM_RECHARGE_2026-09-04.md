# DSD M17-076 — Area-weighted normalized shear gradient has constant three-halves damping and an exact moving-maximum recharge law

Date: 2026-09-04
Canonical ID: **M17-076**

Status: **INTERNAL AREA-WEIGHTED SHEAR-GRADIENT / MOVING-CRITICAL RECHARGE GATE / ON THE FROZEN-ANGLE PURE-KERNEL RANK-TWO BRANCH, M17-075 GIVES `D_B chi_k=D_k(sigma_n-sigma)-(sigma_k+1/2)chi_k`, WHILE THE DIRECTOR-AREA MAGNITUDE OBEYS `D_B|J_xi|=(sigma_k-1)|J_xi|`. FOR THE SIGNED AREA-WEIGHTED GRADIENT `Z_k:=|J_xi| chi_k`, THE ENTIRE `sigma_k` DEPENDENCE CANCELS POINTWISE AND ONE GETS THE DIVISION-FREE CONSTANT-DAMPING LAW `D_B Z_k=|J_xi|D_k(sigma_n-sigma)-(3/2)Z_k`. THUS THE THREE-HALVES RATE IS NOT ONLY A SAME-MARKER MEAN RESONANCE: IT IS THE EXACT HOMOGENEOUS DECAY RATE OF THE AREA-WEIGHTED COMPENSATION CARRIER. ALONG A MOVING LINE-MAXIMUM POINT `D_max=D_B+v_rel D_xi`, THE LAW BECOMES `D_max Z_k=|J_xi|D_k(sigma_n-sigma)-(3/2)Z_k+v_rel D_xi Z_k`. A RECURRENT NONZERO MOVING-MAXIMUM CARRIER THEREFORE REQUIRES `mean[D_k(sigma_n-sigma)/chi_k+v_rel D_xi log|Z_k|]=3/2`, WITHOUT IMPORTING THE SAME-MARKER CONDITION `mean sigma_k=1` TO THE MOVING CRITICAL NETWORK. THE FROZEN-ANGLE RICCATI PAYMENT BECOMES `(p/|J_xi|)Z_k-Theta D_xi q>|C|`. NO SIGN LAW YET FORCES THIS PAYMENT TO FAIL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-075

On the frozen-angle pure-kernel Rank-2 branch define

\[
\boxed{
s:=\frac{m}{|a|^2},
\qquad
\chi_k:=D_k\log|s|.
}
\]

M17-075 gives

\[
\boxed{
D_B\chi_k
=D_k(\sigma_n-\sigma)
-\left(\sigma_k+\frac12\right)\chi_k.
}
\]

For compactness write

\[
\boxed{
S_k:=D_k(\sigma_n-\sigma).
}
\]

Then

\[
D_B\chi_k=S_k-(\sigma_k+1/2)\chi_k.
\]

---

## 2. Director-area multiplier

On the pure-kernel Rank-2 branch the director-area current direction is

\[
k=J_\xi/|J_\xi|.
\]

M17-033/M17-026 give the exact magnitude law

\[
\boxed{
D_B|J_\xi|
=(\sigma_k-1)|J_\xi|.
}
\]

Equivalently,

\[
D_B\log|J_\xi|=\sigma_k-1.
\]

This quantity is nonzero on a retained full-rank-two carrier.

---

## 3. Area-weighted normalized shear gradient

Define the signed scalar

\[
\boxed{
Z_k:=|J_\xi|\,\chi_k.
}
\]

Differentiate materially:

\[
D_BZ_k
=|J_\xi|D_B\chi_k
+\chi_kD_B|J_\xi|.
\]

Insert Sections 1--2:

\[
\begin{aligned}
D_BZ_k
={}&|J_\xi|S_k
-\left(\sigma_k+\frac12\right)|J_\xi|\chi_k\\
&+(\sigma_k-1)|J_\xi|\chi_k.
\end{aligned}
\]

The entire pointwise `sigma_k` dependence cancels:

\[
\boxed{
D_BZ_k
=|J_\xi|S_k
-\frac32Z_k.
}
\]

Thus

\[
\boxed{
D_BZ_k+rac32Z_k
=|J_\xi|D_k(\sigma_n-\sigma).
}
\]

This is the canonical **area-weighted normalized-shear recharge equation**.

---

## 4. Why the cancellation is stronger than the M17-075 mean law

M17-075 obtained the same-marker recurrence condition

\[
\left\langle\frac{S_k}{\chi_k}\right\rangle=\frac32
\]

by combining recurrence of `chi_k` with

\[
\langle\sigma_k\rangle=1.
\]

The present law is stronger in two ways.

First, the rate `3/2` is now pointwise and constant in the homogeneous equation:

\[
\boxed{
S_k=0
\Longrightarrow
D_BZ_k=-\frac32Z_k.
}
\]

Second, no division by `chi_k` is used.
Therefore the equation remains valid through

\[
\chi_k=0.
\]

---

## 5. Exact Duhamel representation

For material time `theta`, the scalar ODE gives

\[
\boxed{
\begin{aligned}
Z_k(\theta)
={}&e^{-\frac32(\theta-\theta_0)}Z_k(\theta_0)\\
&+\int_{\theta_0}^{\theta}
 e^{-\frac32(\theta-s)}
 |J_\xi(s)|S_k(s)\,ds.
\end{aligned}
}
\]

Hence a persistent nonzero area-weighted shear gradient must be continually serviced by the strain-difference gradient source

\[
|J_\xi|D_k(\sigma_n-\sigma).
\]

Without that source it decays at the exact rate `3/2`.

---

## 6. Zero events are regular in Z_k

At a zero of the normalized shear gradient,

\[
\chi_k=0
\quad\Longleftrightarrow\quad
Z_k=0
\]

because `|J_xi|>0` on full rank two.

The exact law gives

\[
\boxed{
D_BZ_k
=|J_\xi|S_k
}
\]

at that event.

Thus the sign crossing is transverse whenever

\[
S_k\ne0.
\]

No logarithmic singularity is needed to describe the crossing.

---

## 7. Moving line maximum

M17-040 gives the material-relative velocity of a nondegenerate line critical point

\[
\boxed{
 v_{rel}
=-\frac{D_\xi(\sigma+\kappa)}{C},
\qquad
C:=D_\xi g,
\qquad
g=D_\xi\log\rho.
}
\]

The derivative along the moving critical point is

\[
\boxed{
D_{max}:=D_B+v_{rel}D_\xi.
}
\]

Therefore Section 3 becomes

\[
\boxed{
D_{max}Z_k
=|J_\xi|S_k
-\frac32Z_k
+v_{rel}D_\xi Z_k.
}
\]

Equivalently,

\[
\boxed{
D_{max}Z_k
-v_{rel}D_\xi Z_k
+\frac32Z_k
=|J_\xi|D_k(\sigma_n-\sigma).
}
\]

This is the exact moving-maximum recharge equation.

---

## 8. Recurrent moving-maximum mean law

Assume along a recurrent moving maximum trajectory that

\[
0<c_Z\le|Z_k|\le C_Z<\infty.
\]

Divide Section 7 by `Z_k`:

\[
D_{max}\log|Z_k|
=\frac{|J_\xi|S_k}{Z_k}
-\frac32
+v_{rel}D_\xi\log|Z_k|.
\]

Since

\[
Z_k=|J_\xi|\chi_k,
\]

we have

\[
\frac{|J_\xi|S_k}{Z_k}
=\frac{S_k}{\chi_k}.
\]

Zero recurrent logarithmic drift therefore gives

\[
\boxed{
\left\langle
\frac{D_k(\sigma_n-\sigma)}{\chi_k}
+v_{rel}D_\xi\log|Z_k|
\right\rangle_{max}
=\frac32.
}
\]

This is the correct **moving-network three-halves recharge law**.

---

## 9. Critical audit: no same-marker mean is imported

The moving maximum point does not generally follow one material label.
Therefore it is not legitimate to insert

\[
\langle\sigma_k\rangle=1
\]

from M17-033 directly into a moving-critical average.

The area-weighted variable avoids that mistake because the `sigma_k` contribution has already canceled pointwise before any averaging.

Hence Section 8 remains valid as a moving-network statement under its own recurrence assumptions.

---

## 10. Riccati compensation in Z_k variables

M17-074 gives at a regular frozen-angle maximum

\[
\boxed{
p\chi_k-\Theta D_\xi q>|C|}
\]

as the condition for a genuinely sub-Riccati in-surface tangent slope.

Using

\[
\chi_k=\frac{Z_k}{|J_\xi|},
\]

this becomes

\[
\boxed{
\frac{p}{|J_\xi|}Z_k
-\Theta D_\xi q
>|C|.
}
\]

Thus the surviving maximum must satisfy simultaneously:

1. a spatial sign/magnitude payment in `Z_k` and the tilt channel;
2. a moving material recharge balance maintaining `Z_k` against exact `3/2` damping.

---

## 11. What the new variable does not prove

The law does not fix the sign of

\[
S_k=D_k(\sigma_n-\sigma),
\]

nor of

\[
\frac{p}{|J_\xi|}Z_k,
\]

nor of the tilt contribution

\[
-\Theta D_\xi q.
\]

Therefore the exact damping law is not by itself a contradiction.
A recurrent branch may in principle recharge `Z_k` with sufficiently correlated higher-jet strain data.

---

## 12. DSD interpretation

The descriptor hierarchy is now

\[
\boxed{
\text{frozen angle}
\to
s
\to
\chi_k
\to
Z_k=|J_\xi|\chi_k
\to
|J_\xi|D_k(\sigma_n-\sigma).
}
\]

The new step is useful because it merges the shear-gradient descriptor with the already existing director-area carrier and removes the moving-frame strain exponent entirely.

The resulting `3/2` is a structural decay rate rather than a bookkeeping artifact of two separate recurrent means.

---

## 13. DSD audit

### Audit A — counting Z_k as a new conserved charge
Rejected. `Z_k` is an area-weighted shear gradient, not an independent topological invariant.

### Audit B — dividing across chi_k=0
Avoided. The primary equation is linear and division free.

### Audit C — importing same-marker mean sigma_k=1 to a moving maximum
Rejected. The pointwise cancellation eliminates the need.

### Audit D — treating v_rel D_xi Z_k as negligible
Rejected. It is an exact transport channel of the moving critical network.

### Audit E — claiming exact 3/2 damping closes the branch
Rejected. The forcing `|J_xi|D_k(sigma_n-sigma)` may recharge the carrier.

### Audit F — proof status
The frozen-angle maximum branch is reduced to a constant-damping forced scalar plus explicit moving transport, but remains open.

---

## 14. Updated frozen-angle maximum frontier

A regular recurrent frozen-angle maximum survivor must service

\[
\boxed{
D_{max}Z_k
=|J_\xi|D_k(\sigma_n-\sigma)
-\frac32Z_k
+v_{rel}D_\xi Z_k,
}
\]

while maintaining

\[
\boxed{
\frac{p}{|J_\xi|}Z_k
-\Theta D_\xi q
>|C|.
}
\]

If `Z_k` is uniformly nonzero and recurrent along the moving network, then

\[
\boxed{
\left\langle
\frac{D_k(\sigma_n-\sigma)}{\chi_k}
+v_{rel}D_\xi\log|Z_k|
\right\rangle_{max}
=\frac32.
}
\]

---

## 15. Next target

The cleanest next subbranch is the `n`-tangent frozen-angle maximum,

\[
\Theta=0,
\]

because its Riccati escape depends only on

\[
p\chi_k>|C|.
\]

The next calculation should derive a division-free moving law for the compensation margin itself and test whether its positive sign can be recurrently maintained.

Only after that should the additional tilted term `-Theta D_xi q` be restored.

This is the **Frozen-Angle Compensation Margin Gate (FACMG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
