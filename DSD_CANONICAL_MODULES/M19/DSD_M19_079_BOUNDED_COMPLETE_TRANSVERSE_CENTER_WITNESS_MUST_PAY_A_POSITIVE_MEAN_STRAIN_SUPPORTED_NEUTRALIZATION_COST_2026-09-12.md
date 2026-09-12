# DSD M19-079 — A bounded complete transverse center witness must pay a positive mean strain-supported neutralization cost

Date: 2026-09-12

Status: **LINEAR LIOUVILLE ENERGY AUDIT / LONG-TIME AVERAGING OF THE RADIAL-A2 ENERGY IDENTITY DOES NOT FORCE A BOUNDED COMPLETE TRANSVERSE WITNESS TO VANISH / INSTEAD EVERY ZERO-EXPONENT WITNESS MUST EXACTLY NEUTRALIZE THE POSITIVE OU/VISCOUS COERCIVITY BY BACKGROUND STRAIN TOGETHER WITH THE SMALLER WEIGHTED TRANSPORT/PRESSURE DEFECTS / AFTER THE ROTATION GAUGE, THIS PRODUCES A QUANTITATIVE NECESSARY MEAN-WORK THRESHOLD FOR ANY EXTRA CENTER MODE / THE LINEAR LIOUVILLE THEOREM THEREFORE REDUCES TO EXCLUDING PERSISTENT STRAIN-SUPPORTED NEUTRALIZATION, NOT TO BOUNDEDNESS ALONE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rotation-transverse linearized equation

After M19-076, work in the co-rotating radial-A2 gauge so that rotational modulation contributes no weighted energy.

The linearized similarity Navier--Stokes equation along the recurrent background \(U\) is

\[
\partial_\theta W
+\frac12W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
+(W\cdot\nabla)U
=-\nabla Q+\nu\Delta W,
\qquad \nabla\cdot W=0.
\]

Let

\[
E_w(\theta)=\int |W|^2w\,dy,
\qquad
G_w(\theta)=\int |\nabla W|^2w\,dy,
\]

with

\[
w(y)=(1+\kappa|y|^2)^{-a/2}
\]

in the M19-063 A2 gap corridor.

---

## 2. Exact decomposition of the weighted work terms

Multiplying by \(Ww\) and integrating gives

\[
\frac12E_w'
+\nu G_w
+\mathcal C_{OU}[W]
=\mathcal W_{tr}[W]
+\mathcal W_{pr}[W]
+\mathcal W_{str}[W],
\]

where

\[
\mathcal C_{OU}[W]\ge c_{gap}E_w
\]

is the positive linear similarity coercivity from M19-063,

\[
\mathcal W_{tr}[W]
=\frac12\int |W|^2 U\cdot\nabla w\,dy,
\]

\[
\mathcal W_{pr}[W]
=\int Q\,W\cdot\nabla w\,dy,
\]

and the true linearized strain work is

\[
\boxed{
\mathcal W_{str}[W]
=-\int W^TS_UW\,w\,dy,
}
\]

with

\[
S_U=\frac12(\nabla U+\nabla U^T).
\]

Only the symmetric velocity gradient contributes because the antisymmetric part is pointwise orthogonal to \(W\otimes W\).

---

## 3. Bounded complete center witness

Assume a normalized rotation-transverse complete solution \(W\) exists with zero Lyapunov exponent and bounded weighted energy,

\[
0<E_-\le E_w(\theta)\le E_+<\infty
\]

along a recurrent subsequence, or at minimum

\[
\sup_{\theta\in\mathbb R}E_w(\theta)<\infty
\]

with a normalization preventing local vanishing.

Integrate from \(-T\) to \(T\):

\[
\frac{E_w(T)-E_w(-T)}{2}
+\int_{-T}^T
\left[
\nu G_w+\mathcal C_{OU}
\right]d\theta
=
\int_{-T}^T
\left[
\mathcal W_{tr}+\mathcal W_{pr}+\mathcal W_{str}
\right]d\theta.
\]

Since \(E_w\) is bounded,

\[
\boxed{
\frac{E_w(T)-E_w(-T)}{2T}\to0.
}
\]

Hence every long-time averaging subsequence satisfies

\[
\boxed{
\left\langle
\nu G_w+\mathcal C_{OU}
\right\rangle
=
\left\langle
\mathcal W_{tr}+\mathcal W_{pr}+\mathcal W_{str}
\right\rangle.
}
\]

---

## 4. Positive mean neutralization threshold

Using

\[
\mathcal C_{OU}\ge c_{gap}E_w,
\]

we obtain

\[
\boxed{
\left\langle
\mathcal W_{tr}+\mathcal W_{pr}+\mathcal W_{str}
\right\rangle
\ge
\nu\langle G_w\rangle
+c_{gap}\langle E_w\rangle.
}
\]

Therefore a nonzero bounded complete center witness cannot be dynamically passive.

It must receive a positive mean amount of work from the background sufficient to cancel both diffusion and the linear similarity gap.

This is the exact center-neutralization requirement.

---

## 5. Transport and pressure are weight defects, not intrinsic center production

M19-064 bounds the two weight-generated terms schematically by

\[
|\mathcal W_{tr}|
\le C_{tr}L_wM_U E_w,
\]

\[
|\mathcal W_{pr}|
\le
\varepsilon\nu G_w
+C_{pr}(\varepsilon)L_w^2M_U^2E_w,
\]

using the A2 weighted Riesz estimate for pressure.

Thus, after absorbing a fixed fraction of \(\nu G_w\),

\[
\boxed{
\left\langle-\int W^TS_UW\,w\,dy\right\rangle
\ge
c_{eff}\langle E_w\rangle
+c_\nu\nu\langle G_w\rangle
}
\]

provided

\[
c_{eff}
:=c_{gap}-C_{tr}L_wM_U-C_{pr}L_w^2M_U^2
>0.
\]

This condition is weaker than the full M19-064 strict-contraction condition because the strain term is now left explicit rather than estimated by magnitude.

---

## 6. Geometric meaning

Let \(\lambda_{min}(S_U)\le\lambda_{mid}(S_U)\le\lambda_{max}(S_U)\) denote the strain eigenvalues.

Since

\[
\operatorname{tr}S_U=0,
\]

the quadratic form

\[
-W^TS_UW
\]

is positive only when \(W\) places sufficient mass in compressive eigendirections of \(S_U\) under the present sign convention.

Therefore any extra bounded center mode must repeatedly align with the appropriate strain eigenspaces strongly enough that

\[
\boxed{
\text{mean strain extraction}
\gtrsim
\text{OU gap}+	ext{viscous dissipation}.
}
\]

The center is therefore not merely a formal neutral solution; it is a persistently background-supported mode.

---

## 7. Positive-density high-work set

Suppose, in addition, that the normalized work ratio

\[
R_W(\theta)
:=
\frac{-\int W^TS_UW\,w\,dy}{E_w(\theta)}
\]

is uniformly bounded above by \(M_R\) on the compact corridor.

If its long-time weighted mean is at least \(c_{eff}>0\), then for any \(0<\eta<c_{eff}\), the set

\[
\mathcal A_\eta
:=\{\theta:R_W(\theta)\ge\eta\}
\]

must have positive lower density bounded in terms of \(c_{eff},\eta,M_R\).

Indeed if its density were arbitrarily small, the mean of \(R_W\) could not stay above \(c_{eff}\).

Thus

\[
\boxed{
\text{extra center}
\Longrightarrow
\text{positive-density strain-supported neutralization events}.
}
\]

This converts the center question into an occupation problem.

---

## 8. Why recurrence alone does not contradict the occupation requirement

M19-066 already showed that the nonlinear recurrent background itself has positive mean vorticity stretching,

\[
\frac{\langle\int\Omega\cdot S_U\Omega\rangle}{\langle\|\Omega\|_2^2\rangle}
\ge\frac14.
\]

Therefore recurrent Navier--Stokes dynamics is fully capable of sustaining persistent strain work.

The new center witness could in principle exploit a different strain-weighted direction.

Hence

\[
\boxed{
\text{positive-density center neutralization}
\not\Rightarrow
\text{contradiction from current ledgers}.
}
\]

---

## 9. What a linear Liouville theorem must now prove

A successful theorem cannot rely only on bounded completeness.

It must exclude the possibility that a transverse perturbation continually extracts exactly enough work from the recurrent background to offset diffusion and OU damping.

One possible target is a strict averaged inequality

\[
\boxed{
\limsup_{T\to\infty}
\frac1{2T}
\int_{-T}^T
\frac{-\int W^TS_UW\,w}{E_w}
\,d\theta
<c_{eff}
}
\]

for every rotation-transverse \(W\) independent of the time tangent.

No such inequality is currently certified.

---

## 10. Certified conclusion

M19-079 replaces a vague center problem by a quantitative necessary condition:

\[
\boxed{
\text{nontrivial bounded complete transverse center}
\Longrightarrow
\text{persistent positive mean strain-supported neutralization cost}.
}
\]

Thus the next question is no longer whether the witness is bounded, but whether the recurrent background can support **two independent neutralization channels**: the known time tangent and a second transverse one.

---

## 11. Next calculation

M19-080 should compare the strain-work identities of

\[
W=\partial_\theta U
\]

and a hypothetical independent center witness \(W_\perp\).

The key audit is whether incompressibility, trace-free strain, or a mixed bilinear identity imposes a finite-rank restriction on simultaneous zero-exponent neutralization even though the naive two-volume trace argument of M19-071 failed.
