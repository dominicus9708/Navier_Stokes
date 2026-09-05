# DSD M17-199 — The amplitude–kappa joint state continuity equation unifies threshold turnover and multiplier transport

Date: 2026-09-06  
Canonical ID: **M17-199**

Status: **JOINT STATE-SPACE REDUCTION / WITH `r=rho` AND `k=kappa`, CE-H GIVES MATERIAL STATE VELOCITIES `r'=(sigma+k-1)r` AND `k'=h`. PUSHING SPATIAL VOLUME TO THE `(r,k)` PLANE YIELDS THE EXACT CONTINUITY EQUATION `partial_theta P + partial_r J_r + partial_k J_k = (3/2) P`, WHERE THE SOURCE `3/2` IS THE SIMILARITY-VOLUME DIVERGENCE. THE M5-668 AMPLITUDE-THRESHOLD TURNOVER IS EXACTLY THE `r`-CURRENT THROUGH `r=a`; THE M5-682/683 MULTIPLIER CONSTITUTIVE TRANSPORT IS THE `k`-CURRENT. THE EXPONENTIALLY WEIGHTED CUTOFF PAYER OF M17-192 IS THEREFORE A KAPPA-TILTED AMPLITUDE-CURRENT MOMENT, NOT A SEPARATE MECHANISM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Joint state variables

On the active set define

\[
r:=\rho=|W|>0,
\qquad
k:=\kappa.
\]

CE-H gives

\[
\boxed{
D_Br=(\sigma+k-1)r,
}
\]

and

\[
\boxed{
D_Bk=h.
}
\]

Set

\[
\gamma:=\sigma+k-1.
\]

Then the state velocity is

\[
\boxed{(r',k')=(\gamma r,h).}
\]

---

## 2. Push spatial volume to `(r,k)`

Define

\[
\boxed{
\mathcal P(r,k,\theta)
:=\int_{\mathbb R^3}
\delta(r-\rho(y,\theta))
\delta(k-\kappa(y,\theta))dy.
}
\]

Define the two state currents

\[
\boxed{
\mathcal J_r(r,k)
:=\int
\gamma\rho\,
\delta(r-\rho)\delta(k-\kappa)dy,
}
\]

\[
\boxed{
\mathcal J_k(r,k)
:=\int
h\,
\delta(r-\rho)\delta(k-\kappa)dy.
}
\]

---

## 3. Exact weak continuity equation

For any compactly supported smooth test function `phi(r,k)`,

\[
\frac d{d\theta}\int\phi(\rho,\kappa)dy
=\int D_B\phi(\rho,\kappa)dy
+\int(\nabla\cdot B)\phi(\rho,\kappa)dy.
\]

Since

\[
\nabla\cdot B=\frac32,
\]

and

\[
D_B\phi
=\phi_r\gamma\rho+\phi_kh,
\]

we obtain

\[
\boxed{
\partial_\theta\mathcal P
+\partial_r\mathcal J_r
+\partial_k\mathcal J_k
=\frac32\mathcal P
}
\]

in the distributional sense on the active state plane.

---

## 4. M5-668 threshold turnover is exactly `J_r`

Integrate the `r`-current over all `k` at a regular amplitude level `r=a`:

\[
\int\mathcal J_r(a,k)dk
=\int\gamma\rho\,\delta(a-\rho)dy.
\]

By coarea,

\[
\boxed{
\int\mathcal J_r(a,k)dk
=a\int_{\rho=a}\frac{\sigma+\kappa-1}{|\nabla\rho|}dS
=\mathcal T_a.
}
\]

Thus M5-668 is simply the integrated `r`-flux law of the joint state-space continuity equation.

---

## 5. The M17-192 cutoff payer is a kappa-tilted `r`-current moment

The M5-688 cutoff source integrated over `k` is

\[
C_\chi^{tot}
=\int\chi'(\rho)\rho^3\gamma\,dy.
\]

Using the joint current,

\[
\boxed{
C_\chi^{tot}
=\iint\chi'(r)r^2\mathcal J_r(r,k)\,dr\,dk.
}
\]

The exponentially tilted version is

\[
\boxed{
\mathcal C
=\iint e^{2k}\chi'(r)r^2\mathcal J_r(r,k)\,dr\,dk.
}
\]

Therefore the M17-192 condition that `C` become positive while the unweighted turnover is negative is exactly a **correlation between the sign of the amplitude current and the multiplier coordinate `k`**.

No new physical current is introduced by the exponential weighting.

---

## 6. M5 multiplier transport is the orthogonal state current

The `k`-current is

\[
\mathcal J_k(r,k)
=\int h\,\delta(r-\rho)\delta(k-\kappa)dy.
\]

M5-682 supplies the constitutive law

\[
h=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom}.
\]

Thus the remaining regular Rank-1 mechanism is a two-dimensional nonequilibrium conveyor:

\[
\boxed{
\text{amplitude motion in }r
\quad\text{coupled to}\quad
\text{constitutive multiplier motion in }k.
}
\]

The bulk `r`-work is the enstrophy stretching/palinstrophy cycle of M17-198; the hard part is the phase organization of the two currents near the retained threshold collar.

---

## 7. Stationary/recurrent form

For an invariant recurrent average,

\[
\boxed{
\partial_r\overline{\mathcal J_r}
+\partial_k\overline{\mathcal J_k}
=\frac32\overline{\mathcal P}.
}
\]

This is not a divergence-free circulation: the positive `3/2 P` source is the similarity-volume dilation.

Integrating over a state-space region recovers the corresponding balance between amplitude-boundary current, kappa-boundary current, and similarity-volume source.

---

## 8. DSD audit

### Audit A — confusing the volume joint current with M5's transverse-flux current
They are different measures. The present module organizes amplitude-threshold turnover and spatial constitutive transport; M17-179/184 separately organize the transverse-flux label measure.

### Audit B — claiming a state-space circulation contradiction
Rejected. The source `3/2 P` and signed currents allow recurrent nonequilibrium transport.

### Audit C — treating the exponential cutoff term as a new independent payer
Rejected. It is a weighted moment of the same amplitude current `J_r`.

---

## 9. Next target

The remaining useful question is whether the CE-H constitutive `k`-current can sustain the high-`k` upward amplitude current demanded by M17-192 without a definite threshold `|grad kappa|^2` or interface cost.

This is a genuine joint-current covariance problem, not a missing scalar sign.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
