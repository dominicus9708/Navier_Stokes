# DSD M19-264 — Navier--Stokes dilation preserves exact CE-H while enstrophy vanishes and kinetic energy moves to low frequency

Date: 2026-09-15  
Canonical ID: **M19-264**  
Status: **ACTIVE SCALING NO-GO / LOW-FREQUENCY FIREWALL SHARPENED / CE-H SCALE-COVARIANT CONTROL CANNOT FORCE KINETIC EXTINCTION / R-CRITICAL INTERFACE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-263 showed that exact CE-H double-eigenline algebra occurs in nonzero finite-energy globally regular axisymmetric no-swirl solutions. It then isolated the possible stronger target

\[
\mathcal T_{CEH}^{LF}:
\text{CE-H + ancient Type-I/first-hitting structure controls }\dot H^{-1}
\]

strongly enough to force backward kinetic-energy extinction.

The present module audits what can possibly be obtained from **scale-covariant CE-H information alone**.

The result is a sharp no-go:

\[
\boxed{
\text{Navier--Stokes dilation preserves exact CE-H while sending vorticity }L^2
\text{ to zero and kinetic }L^2\text{ in the opposite direction.}
}
\]

Therefore any successful low-frequency closure must contain information that fixes or prices the absolute physical scale.

---

## 2. Navier--Stokes scaling

For \(\lambda>0\), define

\[
\boxed{
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t).}
\]

Then

\[
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t)
\]

and

\[
\boxed{
\omega_\lambda(x,t)
=\nabla\times u_\lambda
=\lambda^2\omega(\lambda x,\lambda^2t).
}
\]

This is the standard exact scaling symmetry of the three-dimensional incompressible Navier--Stokes equations.

---

## 3. CE-H is exactly scale covariant

Assume on a spacetime region

\[
S\omega=\sigma\omega,
\qquad
\Delta\omega=\kappa\omega.
\]

The scaled strain satisfies

\[
S_\lambda(x,t)=\lambda^2S(\lambda x,\lambda^2t).
\]

Therefore

\[
\begin{aligned}
S_\lambda\omega_\lambda
&=\lambda^4(S\omega)(\lambda x,\lambda^2t)\\
&=\lambda^4\sigma(\lambda x,\lambda^2t)\omega(\lambda x,\lambda^2t)\\
&=\lambda^2\sigma(\lambda x,\lambda^2t)\omega_\lambda.
\end{aligned}
\]

Hence

\[
\boxed{
\sigma_\lambda(x,t)
=\lambda^2\sigma(\lambda x,\lambda^2t).
}
\]

Likewise

\[
\Delta\omega_\lambda
=\lambda^4(\Delta\omega)(\lambda x,\lambda^2t)
=\lambda^2\kappa(\lambda x,\lambda^2t)\omega_\lambda,
\]

so

\[
\boxed{
\kappa_\lambda(x,t)
=\lambda^2\kappa(\lambda x,\lambda^2t).
}
\]

The cross-product form is consequently invariant:

\[
\omega_\lambda\times S_\lambda\omega_\lambda=0,
\qquad
\omega_\lambda\times\Delta\omega_\lambda=0.
\]

If \(D_\xi\kappa=0\), then \(\xi_\lambda(x,t)=\xi(\lambda x,\lambda^2t)\) and

\[
D_{\xi_\lambda}\kappa_\lambda
=\lambda^3(D_\xi\kappa)(\lambda x,\lambda^2t)=0.
\]

Thus the full exact CE-H algebra used in late M17 is preserved by dilation.

---

## 4. Opposite scaling of enstrophy and kinetic energy

At one fixed corresponding time,

\[
\begin{aligned}
\|\omega_\lambda\|_2^2
&=\int \lambda^4|\omega(\lambda x)|^2dx\\
&=\lambda\|\omega\|_2^2.
\end{aligned}
\]

Hence

\[
\boxed{
\|\omega_\lambda\|_2^2
=\lambda\|\omega\|_2^2.
}
\]

But

\[
\begin{aligned}
\|u_\lambda\|_2^2
&=\int\lambda^2|u(\lambda x)|^2dx\\
&=\lambda^{-1}\|u\|_2^2,
\end{aligned}
\]

so

\[
\boxed{
\|u_\lambda\|_2^2
=\lambda^{-1}\|u\|_2^2.
}
\]

Since for whole-space divergence-free fields

\[
\|u\|_2^2=\|\omega\|_{\dot H^{-1}}^2,
\]

one also has

\[
\boxed{
\|\omega_\lambda\|_{\dot H^{-1}}^2
=\lambda^{-1}\|\omega\|_{\dot H^{-1}}^2.
}
\]

Thus as \(\lambda\downarrow0\),

\[
\boxed{
\|\omega_\lambda\|_2\to0
\quad\text{while}\quad
\|u_\lambda\|_2\to\infty
}
\]

for any nonzero finite-energy seed.

This is the exact low-frequency decompactification mechanism.

---

## 5. Higher derivatives become even smaller under the same dilation

For vorticity derivatives,

\[
D^m\omega_\lambda
=\lambda^{m+2}(D^m\omega)(\lambda x),
\]

hence

\[
\boxed{
\|D^m\omega_\lambda\|_2^2
=\lambda^{2m+1}\|D^m\omega\|_2^2.
}
\]

In particular,

\[
\|\nabla\omega_\lambda\|_2^2
=\lambda^3\|\nabla\omega\|_2^2,
\]

\[
\|\Delta\omega_\lambda\|_2^2
=\lambda^5\|\Delta\omega\|_2^2.
\]

Thus the same low-frequency dilation makes all currently certified high-frequency resources smaller while worsening kinetic-energy control.

Therefore

\[
\boxed{
\text{more derivative control alone cannot repair the low-frequency gap.}
}
\]

---

## 6. The coefficient scale also drifts to zero

Because

\[
\kappa_\lambda=\lambda^2\kappa(\lambda x),
\]

one has, whenever an appropriate essential supremum is finite,

\[
\boxed{
\|\kappa_\lambda\|_\infty
=\lambda^2\|\kappa\|_\infty.
}
\]

Likewise the strain eigenvalue scales as

\[
\|\sigma_\lambda\|_\infty
=\lambda^2\|\sigma\|_\infty.
\]

Hence low-frequency decompactification appears in CE-H coefficient language as

\[
\boxed{
|\kappa|,|\sigma|\to0
\text{ on the expanding physical scale.}
}
\]

A lower bound on an intrinsic coefficient scale would therefore break the dilation escape, but no such absolute-scale lower bound follows from scale-covariant CE-H algebra alone.

---

## 7. Relation to the M5-475 backward Type-I rates

M5-475 gives for the extracted ancient element

\[
\|\Omega(\tau)\|_2^2\lesssim(-\tau)^{-1/2},
\]

\[
\|\Omega(\tau)\|_\infty\lesssim(-\tau)^{-1},
\]

\[
\|V(\tau)\|_\infty\lesssim(-\tau)^{-1/2}.
\]

These exponents are precisely compatible with a characteristic length

\[
L(\tau)\asymp(-\tau)^{1/2}
\]

moving to larger physical scales backward in time.

Indeed the dilation parameter

\[
\lambda(\tau)\asymp(-\tau)^{-1/2}
\]

produces the same vorticity amplitude and enstrophy scaling orders for a scale-fixed profile.

This does **not** assert existence of a backward self-similar CE-H Navier--Stokes solution of the required class. It shows that the certified decay exponents themselves do not exclude pure scale migration.

---

## 8. First-hitting normalization removes, rather than detects, this dilation

The first-hitting scale is

\[
r_j\sim W_j^{-1/2}.
\]

Rescaling every stage to its own natural first-hitting coordinates precisely normalizes the dilation factor away.

Thus an order-one normalized carrier can coexist with physical scales

\[
r_j\to0
\]

or, when viewed backward from a marked stage, with ancestor scales

\[
r_{j-k}=r_jK_k
\]

that expand geometrically.

Consequently

\[
\boxed{
\text{order-one normalized CE-H structure}
\not\Rightarrow
\text{absolute low-frequency tightness in original variables}.
}
\]

This is an exact representation firewall.

---

## 9. What kind of information could break the dilation symmetry

Any successful \(\mathcal T_{CEH}^{LF}\) theorem must add a quantity whose scaling distinguishes the expanding branch.

Candidates include:

1. **finite kinetic energy with quantitative backward control**
   \[
   \|u(\tau)\|_2;
   \]
2. **a low-frequency moment or cancellation condition** on vorticity;
3. **uniform spatial tightness** of a critical or subcritical norm;
4. **a nonzero absolute coefficient-scale floor** not renormalized away;
5. **physical return/incidence to a fixed spatial region** rather than only own-scale recurrence;
6. **a critical-tail theorem** excluding persistent export to similarity infinity.

All of these are forms of low-frequency/realization information already associated with the R-critical root.

---

## 10. Revised CE-H / R-critical interface

The CE-H branch can still generate strong local geometry and sign identities, but if every such identity remains compatible with dilation, then the unresolved escape is not another CE-H internal coefficient branch.

It is

\[
\boxed{
\mathcal R_{critical}^{LF}
:
\text{physical scale escapes to low frequency / large distance while own-scale CE-H structure remains regular.}
}
\]

Therefore low-frequency failure should be routed upward to the existing R-critical complex rather than counted as an independent CE-H mystery.

---

## 11. Permanent firewalls after M19-264

\[
\boxed{
\text{CE-H is exactly Navier--Stokes scale covariant.}
}
\]

\[
\boxed{
\|\omega\|_2\to0
\text{ under dilation}
\not\Rightarrow
\|u\|_2\to0.
}
\]

\[
\boxed{
\text{palinstrophy/raw-H2 decay}
\not\Rightarrow
\text{low-frequency tightness}.
}
\]

\[
\boxed{
\text{first-hitting normalization can hide absolute scale migration by design.}
}
\]

\[
\boxed{
\text{a CE-H low-frequency closure must use non-scale-covariant physical information.}
}
\]

---

## 12. Immediate next target

Search the certified upstream first-hitting/energy/tail structure for a genuinely non-scale-covariant low-frequency quantity.

The highest-leverage candidates are:

1. kinetic-energy inheritance from the original Leray solution;
2. physical-space tightness/center nesting plus a vorticity moment bound;
3. a Fourier low-frequency estimate obtained from divergence-free cancellation or finite impulse;
4. a terminal critical-tail condition that prevents the dilation family from exporting all kinetic energy to \(|\xi|\to0\).

If none is inherited through the ancient extraction, then \(\mathcal R_{critical}^{LF}\) remains an explicit upstream root and CE-H cannot close it internally.

Global 3D Navier--Stokes regularity remains unproved.
