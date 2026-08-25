# DSD W1 Zero-Amplitude Boundary Charge

Date: 2026-08-26

Status: **EXACT TRUNCATED AMPLITUDE-ENERGY LEDGER / `R3/6` ENDPOINT RESIDUE IDENTIFIED AS THE `lambda downarrow 0` BOUNDARY CHARGE OF THE VELOCITY-AMPLITUDE STATE SPACE / REPRODUCES THE GLOBAL `p=3` ENDPOINT WITHOUT TREATING THE RESIDUE AS AN INDEPENDENT PRESSURE SOURCE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The W1 endpoint identity is

\[
\boxed{
\langle F_3\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6},
\qquad
\mathscr R_3>0.
}
\]

The term `R3/6` has appeared as an Abelian `p downarrow 3` residue and as a Gaussian log-scale current.

The amplitude-level pressure-cycle decomposition suggests a more intrinsic DSD interpretation: derive the energy ledger above a strictly positive velocity-amplitude threshold and then let that threshold approach the boundary state `|U|=0`.

---

## 2. Truncated amplitude energy

Let

\[
a:=|U|.
\]

For `lambda>0`, define

\[
\boxed{
\mathcal E_\lambda(s)
:=
\frac12\int_{\mathbb R^3}
(a^2-\lambda^2)_+\,dY.
}
\]

Also define the superlevel volume

\[
V_\lambda(s)
:=
|\{Y:a(Y,s)>\lambda\}|.
\]

For every fixed `lambda>0`, the Type-I tail implies that the superlevel set is spatially bounded, so all terms below are finite.

Use the vector multiplier

\[
U\,\mathbf 1_{\{a>\lambda\}}.
\]

Smooth approximations to the Heaviside function justify the level-set terms and then allow passage to almost every regular `lambda`.

---

## 3. Time and convection terms

Because

\[
\frac{d}{da}
\frac12(a^2-\lambda^2)_+
=
a\,\mathbf 1_{a>\lambda},
\]

we have

\[
\int U_s\cdot U\,\mathbf 1_{a>\lambda}
=
\mathcal E_\lambda'.
\]

The nonlinear convection is a divergence:

\[
\int
(U\cdot\nabla U)\cdot U\,\mathbf 1_{a>\lambda}
=
\int U\cdot\nabla
\left[\frac12(a^2-\lambda^2)_+\right]
=0.
\]

Thus material convection produces no net truncated amplitude-energy source.

---

## 4. Exact Leray similarity contribution

The linear terms give

\[
\frac12\int a^2\mathbf 1_{a>\lambda}
+\frac12\int
(Y\cdot\nabla U)\cdot U\mathbf 1_{a>\lambda}.
\]

The second term is

\[
\frac12\int
Y\cdot\nabla
\left[\frac12(a^2-\lambda^2)_+\right]
=-\frac32\mathcal E_\lambda.
\]

Since

\[
\frac12\int_{a>\lambda}a^2
=
\mathcal E_\lambda
+\frac12\lambda^2V_\lambda,
\]

we obtain

\[
\boxed{
\text{similarity term}
=
-\frac12\mathcal E_\lambda
+\frac12\lambda^2V_\lambda.
}
\]

---

## 5. Exact viscous truncated cost

Integrating by parts gives

\[
-\nu\int
\Delta U\cdot U\,\mathbf 1_{a>\lambda}
=
\nu\int_{a>\lambda}|\nabla U|^2
+
\nu\lambda
\int_{\Sigma_\lambda}|\nabla a|dS,
\]

where

\[
\Sigma_\lambda:=\{a=\lambda\}.
\]

Define

\[
\boxed{
\mathcal D_\lambda
:=
\int_{a>\lambda}|\nabla U|^2dY
+
\lambda\int_{\Sigma_\lambda}|\nabla a|dS.
}
\]

This is nonnegative.

---

## 6. Pressure becomes the amplitude-boundary work

The pressure term is

\[
\int
\nabla P\cdot U\,\mathbf 1_{a>\lambda}dY.
\]

Since `div U=0`,

\[
\int
\nabla P\cdot U\,\mathbf 1_{a>\lambda}
=
-\int
P\,\delta(a-\lambda)U\cdot\nabla a\,dY.
\]

By coarea this is

\[
-J_P(\lambda),
\]

where

\[
J_P(\lambda)
:=
\int_{\Sigma_\lambda}
P\,U\cdot n_\lambda dS,
\qquad
n_\lambda:=\nabla a/|\nabla a|.
\]

Hence the exact thresholded balance is

\[
\boxed{
\mathcal E_\lambda'
-\frac12\mathcal E_\lambda
+\frac12\lambda^2V_\lambda
+\nu\mathcal D_\lambda
=
J_P(\lambda).
}
\]

---

## 7. Integrate over amplitude thresholds

Fix `epsilon>0` and integrate from `lambda=epsilon` to infinity.

Define

\[
F_{3,\epsilon}
:=
\int_{a>\epsilon}
P\,U\cdot\nabla a\,dY.
\]

By coarea,

\[
\int_\epsilon^\infty J_P(\lambda)d\lambda
=F_{3,\epsilon}.
\]

The integrated viscous term is

\[
\begin{aligned}
D_{3,\epsilon}
:={}&
\int_{a>\epsilon}
(a-\epsilon)|\nabla U|^2dY
+
\int_{a>\epsilon}
a|\nabla a|^2dY.
\end{aligned}
\]

Indeed

\[
\int_\epsilon^\infty
\int_{a>\lambda}|\nabla U|^2dYd\lambda
=
\int_{a>\epsilon}(a-\epsilon)|\nabla U|^2dY,
\]

and

\[
\int_\epsilon^\infty
\lambda\int_{\Sigma_\lambda}|\nabla a|dSd\lambda
=
\int_{a>\epsilon}a|\nabla a|^2dY.
\]

As `epsilon downarrow 0`,

\[
D_{3,\epsilon}\uparrow D_3.
\]

---

## 8. The similarity terms collapse to one boundary charge

A pointwise integration in `lambda` gives

\[
\boxed{
\int_\epsilon^\infty
\left[
-\frac12\mathcal E_\lambda
+\frac12\lambda^2V_\lambda
\right]d\lambda
=
\frac\epsilon2\mathcal E_\epsilon.
}
\]

The cancellation would be complete if the threshold integral started at `lambda=0` and the cubic moment were integrable. At the weak-`L3` endpoint it is not, and the missing lower boundary leaves the finite remainder `epsilon E_epsilon/2`.

Let

\[
\mathcal H_\epsilon(s)
:=
\int_\epsilon^\infty
\mathcal E_\lambda(s)d\lambda.
\]

For every fixed `epsilon>0`, `H_epsilon` is finite on W1.

The integrated identity is therefore

\[
\boxed{
\mathcal H_\epsilon'
+
\nu D_{3,\epsilon}
+
\frac\epsilon2\mathcal E_\epsilon
=
F_{3,\epsilon}.
}
\]

---

## 9. Invariant averaging removes the finite-threshold time derivative

On an invariant probability measure `mu` supported on the compact W1 minimal set,

\[
\langle\mathcal H_\epsilon'\rangle_\mu=0.
\]

Hence for every `epsilon>0`,

\[
\boxed{
\langle F_{3,\epsilon}\rangle_\mu
=
\nu\langle D_{3,\epsilon}\rangle_\mu
+
\frac\epsilon2
\langle\mathcal E_\epsilon\rangle_\mu.
}
\]

This is an exact finite-amplitude threshold identity.

---

## 10. The `R3/6` residue is the zero-amplitude boundary charge

As `epsilon downarrow 0`,

\[
F_{3,\epsilon}\to F_3,
\qquad
D_{3,\epsilon}\to D_3,
\]

under the previously established endpoint tail estimates.

Comparing the finite-threshold identity with

\[
\langle F_3\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+
\frac{\mathscr R_3}{6},
\]

we obtain

\[
\boxed{
\lim_{\epsilon\downarrow0}
\frac\epsilon2
\langle\mathcal E_\epsilon\rangle_\mu
=
\frac{\mathscr R_3}{6}.
}
\]

Equivalently,

\[
\boxed{
\mathscr R_3
=
3\lim_{\epsilon\downarrow0}
\epsilon
\langle\mathcal E_\epsilon\rangle_\mu.
}
\]

For a model `a=A/r` critical tail,

\[
\mathcal E_\epsilon
\sim
\frac{4\pi A^3}{3\epsilon},
\]

so

\[
\frac\epsilon2\mathcal E_\epsilon
\to
\frac{2\pi A^3}{3},
\]

while the cubic mass per unit log radius is `4 pi A^3`, giving exactly `R3/6`.

---

## 11. DSD interpretation

The endpoint residue is not an independent pressure source.

For every strictly positive amplitude threshold, the state space is finite and the exact ledger contains only:

1. truncated-state variation;
2. viscosity;
3. Leray similarity geometry;
4. pressure work across the amplitude boundary.

When the threshold approaches the boundary state

\[
a=|U|=0,
\]

the weak-`L3` critical tail causes the truncated kinetic reservoir to diverge like `1/epsilon`. The product

\[
\epsilon\mathcal E_\epsilon
\]

has a finite nonzero limit, producing the endpoint charge.

Thus

\[
\boxed{
\frac{\mathscr R_3}{6}
=
\text{zero-amplitude boundary charge of the amplitude-state ledger}.
}
\]

Spatially, this boundary corresponds to the remote `1/r` memory where `|U|->0` while the logarithmic cubic density remains nonzero.

This is exactly the DSD distinction between an interior state and a boundary approached with nonvanishing structural weight.

---

## 12. Updated proof target

The W1 endpoint can now be stated without treating `R3/6` as a mysterious extra forcing:

\[
\boxed{
\text{interior critical pressure/viscous balance}
+
\text{nonzero zero-amplitude boundary charge}.
}
\]

To close W1 one may equivalently prove

\[
\boxed{
\lim_{\epsilon\downarrow0}
\epsilon\langle\mathcal E_\epsilon\rangle_\mu
=0.
}
\]

That condition is essentially a strong-`L3` improvement over the large weak-`L3` endpoint and is not known from the current assumptions.

No contradiction is claimed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
