# DSD M5-669 — Flux-weighted high-amplitude line length and the exact amplitude-space continuity law

Date: 2026-09-03

Status: **INTERNAL AMPLITUDE-SPACE REFORMULATION / `S_a=int_{rho>a}rho` IS THE VORTEX-FLUX-WEIGHTED HIGH-AMPLITUDE LINE-LENGTH RESOURCE `int L_a dPhi`; ITS EXACT EVOLUTION IS `S_a'=int_{rho>a}rho(sigma+1/2)-D_a+a T_a`, WHERE `D_a` IS THE M5-651 ELLIPTIC SUPERLEVEL DEFICIT AND `T_a` IS THE M5-668 SIGNED MATERIAL THRESHOLD CURRENT / THIS LEDGER IS EXACTLY CONSISTENT WITH M5-652 AND DOES NOT CREATE A SECOND DISSIPATION / DIFFERENTIATING THE SUPERLEVEL-VOLUME LAW IN AMPLITUDE PRODUCES THE EXACT AMPLITUDE-SPACE CONTINUITY EQUATION `partial_theta m + partial_a T = (3/2)m` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Flux-weighted high-amplitude line length

For a fixed positive regular amplitude threshold `a`, define

\[
\boxed{
S_a(\theta):=\int_{\rho>a}\rho(y,\theta)\,dy.
}
\]

In a vortex flow box, with positive transverse vorticity-flux measure `dPhi` and arclength `ds`,

\[
dV=\frac{d\Phi\,ds}{\rho}.
\]

Hence

\[
\rho\,dV=d\Phi\,ds.
\]

Therefore

\[
\boxed{
S_a
=\int_{\mathcal L}L_a(\lambda)\,d\Phi_\lambda,
}
\]

where `L_a(lambda)` is the total arclength of the part of leaf `lambda` on which `rho>a`.

Thus `S_a` is precisely the flux-weighted high-amplitude line-length resource used implicitly in M5-651.

---

## 2. Distributional material derivative

Write

\[
H_a(\rho):=\mathbf1_{\rho>a}.
\]

Then

\[
S_a=\int \rho H_a(\rho)dy.
\]

For

\[
f_a(\rho):=\rho H_a(\rho),
\]

we have in the distributional sense

\[
f_a'(\rho)
=H_a(\rho)+\rho\,\delta(\rho-a).
\]

Using

\[
D_B\rho=\gamma\rho,
\qquad
\gamma:=\sigma+\kappa-1,
\]

and `div B=3/2`,

\[
\begin{aligned}
S_a'
&=\int f_a'(\rho)D_B\rho\,dy
+\frac32S_a\\
&=\int_{\rho>a}\gamma\rho\,dy
+a^2\int_{\rho=a}\frac{\gamma}{|\nabla\rho|}\,dS
+\frac32S_a.
\end{aligned}
\]

Since M5-668 defines

\[
\mathcal T_a
=a\int_{\rho=a}\frac{\gamma}{|\nabla\rho|}\,dS,
\]

we obtain

\[
\boxed{
S_a'
=\int_{\rho>a}\rho\left(\sigma+\kappa+\frac12\right)dy
+a\mathcal T_a.
}
\]

---

## 3. Insert the elliptic superlevel identity

M5-651 gives

\[
\boxed{
\int_{\rho>a}\kappa\rho\,dy=-D_a,
}
\]

where

\[
D_a
=\int_{\rho=a}|\nabla\rho|dS
+\int_{\rho>a}\rho|\nabla\xi|^2dy
>0
\]

on every retained nontrivial regular superlevel.

Therefore

\[
\boxed{
S_a'
=
\int_{\rho>a}\rho\left(\sigma+\frac12\right)dy
-D_a
+a\mathcal T_a.
}
\]

This places axial stretching, elliptic geometric deficit, and material amplitude turnover in one common flux-weighted line-length ledger.

---

## 4. Invariant average

On the compact recurrent hull `S_a` is bounded for every `a>0`, since

\[
S_a\le\frac1a\int\rho^2dy\le\frac{Z_*}{a}.
\]

Hence

\[
\langle S_a'\rangle=0.
\]

Using M5-668,

\[
\langle\mathcal T_a\rangle
=-\frac32\langle V_a\rangle,
\]

so

\[
\boxed{
\left\langle
\int_{\rho>a}\rho\left(\sigma+\frac12\right)dy
\right\rangle
=
\langle D_a\rangle
+\frac32a\langle V_a\rangle.
}
\]

This is exactly the invariant-average linear truncated-amplitude ledger of M5-652 after using

\[
S_a=M_a+aV_a.
\]

Thus there is no new independent global dissipation.

---

## 5. Amplitude density

Define the Eulerian amplitude distribution density

\[
\boxed{
m(a,\theta)
:=\int_{\mathbb R^3}\delta(\rho(y,\theta)-a)dy
=\int_{\rho=a}\frac{1}{|\nabla\rho|}dS
}
\]

for regular levels.

Then

\[
V_a(\theta)=\int_a^\infty m(r,\theta)dr.
\]

Also define the signed amplitude current

\[
\boxed{
\mathcal T(a,\theta)
:=
a\int_{\rho=a}
\frac{\gamma}{|\nabla\rho|}dS.
}
\]

This is exactly `T_a` from M5-668.

---

## 6. Exact amplitude-space continuity equation

M5-668 gives

\[
V_a'
=\frac32V_a+\mathcal T(a,\theta).
\]

Differentiate with respect to the amplitude threshold `a`.

Since

\[
\partial_aV_a=-m(a,\theta),
\]

we obtain

\[
-\partial_\theta m
=-\frac32m+\partial_a\mathcal T.
\]

Therefore

\[
\boxed{
\partial_\theta m(a,\theta)
+
\partial_a\mathcal T(a,\theta)
=
\frac32m(a,\theta).
}
\]

This is the exact continuity equation for material volume distributed over vorticity-amplitude space.

The right-hand side is the similarity-volume expansion source.

---

## 7. Stationary recurrent mean current

Invariant averaging removes the time derivative:

\[
\boxed{
\partial_a\overline{\mathcal T}(a)
=
\frac32\overline m(a).
}
\]

With the high-amplitude boundary condition `T(a)->0` as `a` exceeds the uniform amplitude cap, integration gives

\[
\boxed{
\overline{\mathcal T}(a)
=-\frac32\overline V_a<0.
}
\]

Thus the recurrent hard state carries a strictly downward mean current through amplitude space at every occupied positive threshold.

---

## 8. Interpretation and firewall

This downward mean current is not a monotone loss of a finite material resource.

The source term `(3/2)m` is precisely the similarity material-volume expansion and allows a stationary Eulerian amplitude distribution despite persistent downward material crossing.

Likewise, `S_a` does not give an independent flux-resource contradiction because its exact average equation is already M5-652 in another representation.

Therefore one must not claim

\[
\text{downward amplitude current}
\Rightarrow
\text{finite-time depletion}.
\]

---

## 9. Updated use of the amplitude-space picture

The value of the formulation is localization.

Any persistent carrier at the fixed threshold `a0` must coexist with:

1. a strict downward mean material current through `a0`;
2. a strict elliptic deficit `D_{a0}`;
3. positive weighted axial production;
4. recurrent replenishment/turnover events needed to keep the carrier geometry present.

Thus the unresolved mechanism is a stationary nonequilibrium amplitude cascade, not a static multi-sheet geometry.

The next calculation should test whether the **upward** current component can carry a fixed amount of scale-invariant vorticity flux indefinitely, or whether all recurrent high-amplitude carrier reconstruction must draw on the finite transverse flux measure identified in M5-647.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
