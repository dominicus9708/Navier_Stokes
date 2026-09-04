# DSD M17-110 — Tangency margin reduces to a connection mismatch but remains independent of fold orientation at current jet order

Date: 2026-09-05
Canonical ID: **M17-110**

Status: **INTERNAL TANGENCY MARGIN REDUCTION GATE / AT A PURE-KERNEL LINE MAXIMUM WRITE `b=p k+q n`, `a=r k` AND USE THE GENERAL ORTHONORMAL CONNECTION `D_xi k=-p xi+alpha n`, `D_k k=gamma_k n`, `D_n k=-r xi+delta n`. M17-074 FLATNESS GIVES `D_k g=r(gamma_k-q)` AND `D_k q=p(q-gamma_k)`. AT A DIRECTOR-AREA/PEAK TANGENCY `D_k g=0`, FULL RANK GIVES `r!=0`, SO `gamma_k=q` AND HENCE `D_k q=0`. THE FULL-FIELD NORMALIZED-SHEAR DERIVATIVE THEN REDUCES TO `r D_k s=q^2-r alpha+p delta`. CONSEQUENTLY THE POSITIVE FOLD MARGIN IS `N_F=|r|[C+q^2-r alpha+p delta-Theta D_xi q]`. THE FOLD CURVATURE, HOWEVER, IS `H=D_k^2g=r D_k gamma_k` AT TANGENCY, AND THE BIRTH/DEATH ORIENTATION IS `epsilon_F=-sgn[D_xi(sigma+kappa) r D_k gamma_k]`. THUS THE EVENT SIGN DEPENDS ON THE TIME-UNFOLDING AND A KERNEL-CURVATURE DERIVATIVE, WHILE THE MARGIN DEPENDS ON A LOWER CONNECTION-MISMATCH COMBINATION. THE WEIGHTED-HARMONIC STRESS EQUATIONS DO NOT AT THIS ORDER FIX THE SIGN OF `q^2-r alpha+p delta` OR RELATE IT MONOTONICALLY TO `D_k gamma_k`. THEREFORE M17-109'S MARGIN-WEIGHTED FOLD COVARIANCE IS NOT REMOVED BY THE TANGENCY IDENTITIES. A HIGHER-JET OR GLOBAL ESTIMATE WOULD BE REQUIRED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Peak frame and connection notation

At a pure-kernel line peak,

\[
g=D_\xi\log\rho=0.
\]

Write

\[
\boxed{
b=D_\xi\xi=p\,k+q\,n,}
\]

and because `div xi=-g`, the `n`-jet is

\[
\boxed{a=D_n\xi=r\,k.}
\]

Full Rank 2 gives

\[
\boxed{r\neq0,\qquad q\neq0.}
\]

Use the connection notation of M17-074:

\[
D_\xi k=-p\xi+\alpha n,
\]

\[
D_k k=\gamma_k n,
\qquad
D_kn=-\gamma_k k,
\]

\[
D_nk=-r\xi+\delta n.
\]

---

## 2. Tangency is a curvature resonance

M17-074 flatness gives

\[
\boxed{
D_kg=r(\gamma_k-q).
}
\]

Therefore director-area/peak tangency

\[
D_kg=0
\]

is equivalent to

\[
\boxed{\gamma_k=q}
\]

because `r!=0`.

The same flatness system gives

\[
\boxed{
D_kq=p(q-\gamma_k).
}
\]

Hence at tangency,

\[
\boxed{D_kq=0.}
\]

---

## 3. Normalized-shear derivative at tangency

Define the division-free normalized shear

\[
\boxed{
s:=\frac{m}{|a|^2}.}
\]

At the peak,

\[
m=pr,
\qquad
|a|^2=r^2,
\]

so pointwise

\[
s=\frac pr.
\]

The pointwise identity is not differentiated off the peak.
M17-074 first differentiates the full field and obtains

\[
D_ks
=D_k\left(\frac pr\right)
-\frac q{r^2}D_kg.
\]

At tangency,

\[
D_kg=0,
\]

so

\[
\boxed{
D_ks
=D_k\left(\frac pr\right).
}
\]

---

## 4. Use flatness to reduce r D_k s

M17-074 gives

\[
D_kp=q\gamma_k+p^2-\alpha r
\]

and

\[
D_kr=r(p-\delta).
\]

At tangency `gamma_k=q`, therefore

\[
D_kp=q^2+p^2-\alpha r.
\]

Now

\[
\begin{aligned}
rD_ks
&=rD_k\left(\frac pr\right)\\
&=D_kp-\frac prD_kr\\
&=(q^2+p^2-\alpha r)-p(p-\delta).
\end{aligned}
\]

Thus

\[
\boxed{
rD_ks=q^2-r\alpha+p\delta.}
\]

This is the exact lower-order connection mismatch that services the normalized-shear part of the tangency margin.

---

## 5. Tangency margin

M17-079 gives the regular maximum margin

\[
\mathcal M_{R2}
=C+rD_ks-\Theta L,
\]

where

\[
C=D_\xi g<0,
\qquad
L=D_\xi q,
\qquad
\Theta=\frac{D_ng}{-C}.
\]

Substitute Section 4:

\[
\boxed{
\mathcal M_F
=C+q^2-r\alpha+p\delta-\Theta D_\xi q.
}
\]

Since `|a|=|r|` at the peak,

\[
\boxed{
N_F
=|r|
\left[
C+q^2-r\alpha+p\delta-\Theta D_\xi q
\right].
}
\]

A surviving sub-Riccati fold requires

\[
\boxed{N_F>0.}
\]

---

## 6. Fold curvature is a different connection channel

Differentiate the tangency identity

\[
D_kg=r(\gamma_k-q)
\]

along `k`.
At tangency the first factor multiplying `D_kr` vanishes, so

\[
D_k^2g
=r(D_k\gamma_k-D_kq).
\]

But Section 2 gives

\[
D_kq=0.
\]

Therefore

\[
\boxed{
H:=D_k^2g
=rD_k\gamma_k.
}
\]

Thus the spatial curvature of the generic fold is a **derivative of the kernel-fiber connection curvature**, not the lower connection mismatch appearing in `N_F`.

---

## 7. Event orientation

M17-109 gives

\[
\varepsilon_F
=-\operatorname{sgn}(AH),
\]

where

\[
A=D_\xi(\sigma+\kappa).
\]

Using Section 6,

\[
\boxed{
\varepsilon_F
=-\operatorname{sgn}
\left[
D_\xi(\sigma+\kappa)
\,rD_k\gamma_k
\right].
}
\]

The margin weight is therefore controlled by

\[
C+q^2-r\alpha+p\delta-\Theta D_\xi q,
\]

whereas the fold orientation is controlled by

\[
D_\xi(\sigma+\kappa)\,rD_k\gamma_k.
\]

No algebraic sign identity between these expressions has been obtained.

---

## 8. Weighted-harmonic stress cross-audit

M17-041 gives, on the frozen-angle branch, the exact weighted-harmonic stress balances

\[
D_\xi d+D_nm
+m(2D_n\log\rho-2q-\gamma_k)=0
\]

at `g=0`, and

\[
D_nd
=D_\xi m+|a|^2(2D_n\log\rho-\gamma_k)+2dq.
\]

At tangency `gamma_k=q`, these equations sharpen, but they retain signed derivatives

\[
D_nm,
\quad
D_\xi d,
\quad
D_n\log\rho,
\quad
D_\xi m.
\]

They do not determine a universal sign for

\[
q^2-r\alpha+p\delta
\]

or for

\[
D_k\gamma_k.
\]

The kernel stress projection is already known from M17-035 to be a geometric integrability identity and supplies no extra coercive sign.

Thus weighted harmonicity does not close the fold covariance at the present derivative order.

---

## 9. Consequence for margin-weighted fold hysteresis

M17-109's fold source is

\[
\mathscr B_F
=2\int
\varepsilon_FN_F
\delta(\theta-\tau_F)
\,d\Phi_J.
\]

Sections 5--7 show that the product

\[
\boxed{\varepsilon_FN_F}
\]

is a genuine covariance between two different jet channels:

1. lower connection/tilt compensation setting the positive margin;
2. time-unfolding times kernel-curvature derivative setting birth/death orientation.

The tangency equations reduce both descriptors but do not identify their signs.

---

## 10. DSD analysis

The fold event is now resolved into

\[
\boxed{
\text{tangency resonance }\gamma_k=q
\to
\begin{cases}
\text{margin mismatch }q^2-r\alpha+p\delta-\Theta D_\xi q,\\
\text{fold orientation }D_\xi(\sigma+\kappa)\,rD_k\gamma_k.
\end{cases}
}
\]

The two descendants live at different differential orders.

This explains why unweighted director-area neutrality does not determine margin hysteresis.

---

## 11. DSD audit

### Audit A — assuming tangency forces the margin to zero
Rejected.

### Audit B — differentiating `s=p/r` away from the critical set
Avoided by using the audited full-field derivative from M17-074 first.

### Audit C — identifying fold curvature `H` with the margin's `q^2` term
Rejected. `H=rD_k gamma_k` is a connection derivative.

### Audit D — claiming weighted harmonicity signs the mismatch
Rejected at the present derivative order.

### Audit E — proof status
The generic fold covariance is reduced to explicit connection jets but remains sign-indefinite.

---

## 12. Updated Rank-2 fold frontier

The generic tangency event source is now fully localised to

\[
\boxed{
\varepsilon_FN_F
=
-\operatorname{sgn}
\left[
D_\xi(\sigma+\kappa)rD_k\gamma_k
\right]
|r|
\left[
C+q^2-r\alpha+p\delta-\Theta D_\xi q
\right].
}
\]

No current local identity fixes its sign or mean.

Therefore repeatedly differentiating the same local fold equations is unlikely to close the branch without a new coercive estimate.
The next higher-value step is to combine the Rank-2 section/boundary/fold ledger with the already independent Rank-1/M5 turnover ledgers and test whether all required recharge covariances can be serviced by one recurrent conveyor.

This is the **Global Turnover Assembly Gate (GTAG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
