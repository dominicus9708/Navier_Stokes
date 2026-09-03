# DSD M5-631 — Material-tube enstrophy per flux squared is the geometric aspect ratio

Date: 2026-09-03

Status: **INTERNAL EXACT TUBE GEOMETRY / ON THE CE-H DOUBLE-EIGENLINE BRANCH, AN INFINITESIMAL MATERIAL VORTEX-TUBE SEGMENT WITH CROSS-SECTION `A_perp`, MATERIAL LENGTH `ell`, VORTICITY MAGNITUDE `rho`, FLUX `phi=rho A_perp`, AND ENSTROPHY `dE=rho^2 A_perp ell` SATISFIES `dE/phi^2 = ell/A_perp`. ITS MATERIAL LOG-DRIFT IS `2 sigma - 1/2`, SO THE VISCOUS MULTIPLIER `kappa` CANCELS EXACTLY. THE M5-630 SAME-LEVEL KAPPA–ENSTROPHY COVARIANCE IS THEREFORE NOT AN EXTRA VISCOUS DEGREE OF FREEDOM: AFTER DIVIDING BY THE SCALE-INVARIANT FLUX IT IS STORED IN MATERIAL TUBE ASPECT-RATIO GEOMETRY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H tube inputs

On the CE-H branch,

\[
D_B\log\rho=\sigma+\kappa-1,
\]

\[
D_B\log A_\perp=1-\sigma,
\]

and for an infinitesimal material line element tangent to the vortex line,

\[
D_B\log\ell=\sigma+\frac12.
\]

The infinitesimal material vorticity flux is

\[
\boxed{\phi=\rho A_\perp}
\]

and M5-602 gives

\[
\boxed{D_B\log|\phi|=\kappa.}
\]

---

## 2. Material tube-segment volume

Let

\[
dV=A_\perp\ell.
\]

Then

\[
D_B\log dV
=(1-\sigma)+(\sigma+\tfrac12)
=\frac32.
\]

Thus

\[
\boxed{D_B\log dV=\frac32.}
\]

This exactly reproduces the material-volume expansion law from M5-560.

---

## 3. Infinitesimal tube enstrophy

Define the infinitesimal enstrophy content

\[
d\mathcal E:=\rho^2dV
=\rho^2A_\perp\ell.
\]

Its log derivative is

\[
D_B\log d\mathcal E
=2(\sigma+\kappa-1)+\frac32,
\]

hence

\[
\boxed{
D_B\log d\mathcal E
=2\sigma+2\kappa-\frac12.
}
\]

---

## 4. Divide by flux squared

Since

\[
\phi^2=\rho^2A_\perp^2,
\]

we have the exact geometric identity

\[
\boxed{
\frac{d\mathcal E}{\phi^2}
=\frac{\ell}{A_\perp}.
}
\]

Define

\[
\mathcal R_{tube}:=rac{d\mathcal E}{\phi^2}.
\]

Then

\[
D_B\log\mathcal R_{tube}
=(2\sigma+2\kappa-\tfrac12)-2\kappa,
\]

so

\[
\boxed{
D_B\log\mathcal R_{tube}
=2\sigma-\frac12.
}
\]

The viscous multiplier `kappa` cancels identically.

---

## 5. Interpretation

`dE/phi^2` is not a mysterious analytic quantity.

It is simply the material tube aspect ratio

\[
\boxed{
\mathcal R_{tube}=\ell/A_\perp.
}
\]

Thus fixed/recurrent flux does not fix the tube enstrophy because enstrophy can change through geometric redistribution between

\[
\ell
\quad\text{and}\quad
A_\perp.
\]

This is precisely the degree of freedom exposed by the M5-630 covariance correction.

---

## 6. Equivalent algebraic reconstruction

Using

\[
dV=A_\perp\ell
\]

and

\[
\mathcal R_{tube}=\ell/A_\perp,
\]

one has

\[
\ell=(dV\,\mathcal R_{tube})^{1/2},
\qquad
A_\perp=(dV/\mathcal R_{tube})^{1/2}.
\]

Since

\[
dV(\theta)=dV(\theta_0)e^{3(\theta-\theta_0)/2},
\]

no positive-volume material tube segment can keep both its length and its cross-sectional area in a fixed similarity-scale compact range indefinitely.

This is another form of the M5-560 firewall.

---

## 7. Relation to M5-630

M5-630 retained the survivor possibility

\[
\langle\kappa\rangle_{flux}=0,
\qquad
\langle\kappa E_A\rangle<0.
\]

M5-631 shows that after normalizing one material tube by its scale-critical flux, the remaining enstrophy degree of freedom is controlled by

\[
2\sigma-\frac12,
\]

not directly by `kappa`.

Therefore the same-level covariance problem should be re-expressed as a **phase relation among flux, stretching, and tube aspect ratio**, rather than as an independent viscous measure defect.

---

## 8. Firewall

This calculation is exact for an infinitesimal material tube segment.

It does not assert that a finite Eulerian coherent carrier is one fixed positive-volume material segment for all time. M5-560 already shows that such a persistent positive-volume interpretation is impossible.

The next calculation should use the exact recurrent product identity

\[
d\mathcal E=\phi^2\mathcal R_{tube}
\]

to rewrite the negative `kappa`–enstrophy covariance as a weighted stretching/aspect-ratio balance.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]