# DSD M17-188 — Same-material closed winding recurrence forces a `3/4` strain-amplitude line covariance and gradient occupancy

Date: 2026-09-06  
Canonical ID: **M17-188**

Status: **CLOSED-LOOP LINE-STRAIN GATE / FOR A MATERIAL CLOSED GREAT-CIRCLE VORTEX LOOP, ITS GEOMETRIC LENGTH OBEYS `ell' = int (sigma+1/2) ds`, WHILE THE ENSTROPHY LINE WEIGHT OBEYS `L_rho'/L_rho=kappa-1/2+2 sigma_bar_rho` AND ITS MATERIAL FLUX OBEYS `Phi'/Phi=kappa`. IF THE SAME MATERIAL LOOP RETURNS RECURRENTLY WITH COMPARABLE `ell`, `L_rho`, AND `Phi`, THEN THE LONG-TIME MEANS ARE `bar sigma_ds=-1/2`, `bar sigma_rho=1/4`, AND HENCE THEIR DIFFERENCE IS EXACTLY `3/4`. AT EACH TIME THIS DIFFERENCE IS THE NORMALIZED COVARIANCE OF `sigma` AND `rho` ALONG THE LOOP. UNIFORM COMPACT LOOP BOUNDS AND THE CIRCLE POINCARE INEQUALITY THEREFORE FORCE A POSITIVE TIME-AVERAGED PRODUCT OF TANGENTIAL STRAIN- AND AMPLITUDE-GRADIENT NORMS, AND HENCE A POSITIVE FIXED-ORDER GRADIENT OCCUPANCY. THIS IDENTIFIES A CONCRETE GEOMETRIC PAYER FOR THE QUARTER-STRAIN RESIDENCE CHANNEL, BUT IT IS NOT A DISSIPATION CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material closed vortex loop

Let `Gamma(theta)` be a closed regular great-circle vortex loop transported materially by the similarity flow.

Write its geometric arclength as

\[
\boxed{
\ell_\Gamma(\theta):=\oint_\Gamma ds.
}
\]

Define the ordinary arclength mean of the aligned strain eigenvalue

\[
\boxed{
\bar\sigma_{ds}
:=\frac1{\ell_\Gamma}\oint_\Gamma\sigma ds.
}
\]

The enstrophy line weight and its `rho`-weighted strain mean are

\[
\boxed{
L_\rho:=\oint_\Gamma\rho ds,
}
\]

\[
\boxed{
\bar\sigma_\rho
:=\frac1{L_\rho}\oint_\Gamma\sigma\rho ds.
}
\]

Let `Phi` denote the material vorticity flux of the corresponding thin tube label.

---

## 2. Geometric loop-length law

For a material line element tangent to the vorticity direction,

\[
D_B ds
=\left(\sigma+\frac12\right)ds.
\]

Therefore

\[
\ell_\Gamma'
=\oint_\Gamma\left(\sigma+\frac12\right)ds.
\]

Equivalently,

\[
\boxed{
\frac d{d\theta}\log\ell_\Gamma
=\bar\sigma_{ds}+\frac12.
}
\]

---

## 3. Enstrophy line-weight and flux laws

M5-684 gives

\[
\boxed{
\frac d{d\theta}\log L_\rho
=\kappa-\frac12+2\bar\sigma_\rho.
}
\]

The material tube flux obeys

\[
\boxed{
\frac d{d\theta}\log\Phi=\kappa.
}
\]

Hence

\[
\boxed{
\frac d{d\theta}\log\frac{L_\rho}{\Phi}
=2\bar\sigma_\rho-\frac12
=2\left(\bar\sigma_\rho-\frac14\right).
}
\]

---

## 4. Same-material recurrent means

Assume one material loop remains in a compact nondegenerate class and has recurrent/comparable values of

\[
\ell_\Gamma,
\qquad
L_\rho,
\qquad
\Phi.
\]

Then along recurrence intervals the time averages of the three logarithmic derivatives vanish.

From Section 2,

\[
\boxed{
\left\langle\bar\sigma_{ds}\right\rangle=-\frac12.
}
\]

From the flux law,

\[
\boxed{\langle\kappa\rangle=0.}
\]

From the line-weight law,

\[
0=\langle\kappa\rangle-rac12+2\langle\bar\sigma_\rho\rangle,
\]

so

\[
\boxed{
\left\langle\bar\sigma_\rho\right\rangle=\frac14.
}
\]

Therefore

\[
\boxed{
\left\langle
\bar\sigma_\rho-\bar\sigma_{ds}
\right\rangle
=\frac34.
}
\]

---

## 5. Exact covariance representation

Let

\[
\bar\rho_{ds}:=\frac{L_\rho}{\ell_\Gamma}.
\]

A direct expansion gives

\[
\oint_\Gamma
(\sigma-\bar\sigma_{ds})
(\rho-\bar\rho_{ds})ds
=
\oint\sigma\rho ds
-\bar\sigma_{ds}L_\rho.
\]

Divide by `L_rho`:

\[
\boxed{
\bar\sigma_\rho-\bar\sigma_{ds}
=
\frac1{L_\rho}
\oint
(\sigma-\bar\sigma_{ds})
(\rho-\bar\rho_{ds})ds.
}
\]

Thus Section 4 is exactly a positive long-time strain-amplitude covariance law:

\[
\boxed{
\left\langle
\frac1{L_\rho}
\oint
(\sigma-\bar\sigma_{ds})
(\rho-\bar\rho_{ds})ds
\right\rangle
=\frac34.
}
\]

---

## 6. Tangential-gradient occupancy

At each time, Cauchy--Schwarz gives

\[
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le
\frac{
\|\sigma-\bar\sigma_{ds}\|_{L^2(ds)}
\|\rho-\bar\rho_{ds}\|_{L^2(ds)}
}{L_\rho}.
\]

For a closed loop of length `ell_Gamma`, the circle Poincare inequality gives

\[
\|f-\bar f\|_2
\le
\frac{\ell_\Gamma}{2\pi}
\|\partial_sf\|_2.
\]

Hence

\[
\boxed{
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le
\frac{\ell_\Gamma^2}{4\pi^2L_\rho}
\|\partial_s\sigma\|_2
\|\partial_s\rho\|_2.
}
\]

Assume compact loop bounds

\[
0<L_*\le L_\rho,
\qquad
\ell_\Gamma\le\ell^*<\infty.
\]

Then

\[
\boxed{
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le C_*
\|\partial_s\sigma\|_2
\|\partial_s\rho\|_2.
}
\]

Taking the recurrent time mean and using Section 4 forces

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_2
\|\partial_s\rho\|_2
\right\rangle
\ge c_*>0.
}
\]

By Young's inequality,

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_2^2
+\|\partial_s\rho\|_2^2
\right\rangle
\ge 2c_*>0.
}
\]

Thus the same-material recurrent loop must carry persistent tangential strain/amplitude-gradient occupancy.

---

## 7. Relation to the M5-688 payers

Since

\[
|\partial_s\sigma|\le|\nabla\sigma|
\]

and

\[
|\partial_s\rho|\le|\nabla\rho|\le|\nabla W|,
\]

the gradient occupancy of Section 6 lives inside the same fixed-order fields that appear in

1. the M5-688 strain-gradient charge `D_sigma`;
2. the ordinary palinstrophy / amplitude-gradient budget.

Thus a recurrent closed winding loop has a concrete geometric mechanism capable of supporting the quarter-strain residence payer.

This is progress in identifying the payer, but it also means the payer is not automatically impossible.

---

## 8. A smooth snapshot firewall

The covariance requirement itself is kinematically realizable.

On a unit circle, choose for example

\[
\rho(s)=1+\varepsilon\cos s,
\qquad
0<\varepsilon<1,
\]

and

\[
\sigma(s)=-\frac12+A\cos s.
\]

Then

\[
\bar\sigma_{ds}=-\frac12
\]

and

\[
\bar\sigma_\rho
=-\frac12+\frac{A\varepsilon}{2}.
\]

Choosing

\[
A\varepsilon=\frac32
\]

gives

\[
\bar\sigma_\rho=\frac14.
\]

The functions are smooth and have finite derivative norms.

This is not a Navier--Stokes solution; it shows only that the `3/4` covariance condition by itself is not contradictory.

---

## 9. Branch split

The same-material closed-loop branch now satisfies

\[
\boxed{
R_{1}^{closed\ loop,same\ marker}
\Longrightarrow
G_{tangential\ strain/amplitude\ gradient}^{+}
\lor
T_{loop/weight/flux\ recurrence}.
}
\]

If same-material loop recurrence fails, the escape is fresh-loop turnover / interface / noncompact geometry rather than silent reuse of the same loop.

---

## 10. DSD audit

### Audit A — using ensemble recurrence as same-label recurrence
Rejected. Section 4 is conditional on one material loop returning comparably.

### Audit B — claiming the covariance is impossible
Rejected by the explicit smooth snapshot model.

### Audit C — calling gradient occupancy dissipation
It is a fixed-order spatial occupancy. Additional spacetime budget information is required for a contradiction.

### Audit D — proof status
The line-strain payer is geometrically identified, not eliminated.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
