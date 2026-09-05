# DSD M17-144 — Quiet remote generic fold reduces to scale-free `kappa`-gradient recharge under high-jet compactness

Date: 2026-09-05  
Canonical ID: **M17-144**

Status: **QUIET-FOLD REDUCTION / M17-143 IDENTIFIES THE TRUE GENERIC FOLD UNFOLDING COEFFICIENT AS `A_T=D_xi(sigma+kappa)`, NOT `D_B(D_k g)`. ON A QUIET REMOTE CRITICAL SHELL WITH `int |Sigma|^2=O(R^{-1})`, ONE EXTRA LEVEL OF UNIFORM STRAIN-JET COMPACTNESS GIVES POINTWISE DECAY OF `grad Sigma`, AND TWO EXTRA LEVELS GIVE DECAY OF `grad^2 Sigma`. CONSEQUENTLY, WITH UNIFORMLY BOUNDED DIRECTOR JETS, `D_xi sigma=O(R^{-1/7})` AND `D_kD_xi sigma=O(R^{-1/9})`. THE GENERIC FOLD COEFFICIENT THEREFORE SATISFIES `A_T=D_xi kappa+O(R^{-1/7})`; AT TANGENCY, `D_B(D_k g)=D_kD_xi kappa+O(R^{-1/9})`. THUS A UNIFORMLY NONDEGENERATE QUIET-REMOTE FOLD MUST BE SERVICED ASYMPTOTICALLY BY THE SCALE-FREE CE-H MULTIPLIER GRADIENT `D_xi kappa`, NOT BY ORDINARY STRAIN. THE FIXED-TIME IDENTITY `kappa=Delta log rho+|grad log rho|^2-|grad xi|^2` IS AMPLITUDE-INVARIANT UNDER `rho -> epsilon rho`, SO QUADRATIC LOW-AMPLITUDE SHELL BUDGETS DO NOT BY THEMSELVES CONTROL THIS MULTIPLIER GRADIENT. THIS IS A FIREWALL FOR THE ELLIPTIC/DIRECTOR SUBSYSTEM, NOT A CLAIM THAT AMPLITUDE SCALING PRESERVES THE FULL NONLINEAR NAVIER--STOKES DYNAMICS. PERSISTENT RIBBONS INSTEAD FORCE `D_xi kappa ->0` ON THE SAME QUIET HIGH-JET BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Quiet remote shell and finite-jet hypothesis

Let `C_R` be a fixed-shape remote shell neighborhood containing the retained Rank-2 compact ribbon/fold geometry.

M17-142 uses the quiet critical spacetime bound

\[
\boxed{
R\int_{C_R}|\nabla U|^2dy\le J_*.
}
\]

Since

\[
|\Sigma|\le|\nabla U|,
\]

we have

\[
\boxed{
\|\Sigma\|_{L^2(C_R)}^2
\le
\frac{J_*}{R}.
}
\]

M17-139 used one bounded derivative of strain to obtain pointwise decay of `Sigma` itself.

For the present fold gate we state explicitly the stronger compact finite-jet hypotheses needed below:

\[
\boxed{
\sup_{N_R}|\nabla^2\Sigma|\le M_2
}
\]

for the first derivative estimate, and

\[
\boxed{
\sup_{N_R}|\nabla^3\Sigma|\le M_3
}
\]

for the second derivative estimate, on a fixed-width buffered neighborhood `N_R` of the relevant geometry.

Their failure is a distinct high-jet/loss-of-compactness exit.

---

## 2. Local Gagliardo--Nirenberg decay hierarchy

For a tensor field `F` in three dimensions, a local interpolation estimate of the form

\[
\|\nabla^mF\|_{L^\infty}
\le
C
\|\nabla^{m+1}F\|_{L^\infty}^{\frac{2m+3}{2m+5}}
\|F\|_{L^2}^{\frac{2}{2m+5}}

\]

holds on a fixed interior subdomain, with constants depending only on the fixed geometric buffer.

Apply this to `F=Sigma`.
Because

\[
\|\Sigma\|_{L^2}=O(R^{-1/2}),
\]

we obtain the hierarchy

\[
\boxed{
\|\nabla^m\Sigma\|_{L^\infty}
=O\left(R^{-\frac1{2m+5}}\right)
}
\]

whenever `nabla^{m+1} Sigma` has a uniform `L^infty` bound.

In particular,

\[
\boxed{
\|\Sigma\|_\infty=O(R^{-1/5}),
}
\]

recovering the M17-139 exponent,

\[
\boxed{
\|\nabla\Sigma\|_\infty=O(R^{-1/7}),
}
\]

under a uniform second-jet bound, and

\[
\boxed{
\|\nabla^2\Sigma\|_\infty=O(R^{-1/9})
}
\]

under a uniform third-jet bound.

The exponents are not asserted sharp; strict decay is the only required feature.

---

## 3. Directional strain derivatives decay as well

Let

\[
\sigma:=\xi\cdot\Sigma\xi.
\]

Assume the retained compact director hard hull gives uniform bounds on the director jets needed below:

\[
|\nabla\xi|+|\nabla^2\xi|\le C_\xi.
\]

Then

\[
D_\xi\sigma
\]

contains one spatial derivative of `Sigma` plus terms consisting of `Sigma` times first derivatives of `xi`.

Hence

\[
\boxed{
D_\xi\sigma
=O(R^{-1/7}).
}
\]

Similarly,

\[
D_kD_\xi\sigma
\]

contains `nabla^2 Sigma`, lower derivatives of `Sigma`, and bounded first/second director-frame jets.
Therefore

\[
\boxed{
D_kD_\xi\sigma
=O(R^{-1/9}).
}
\]

These estimates are conditional on the stated strain/director jet compactness.

---

## 4. Generic fold unfolding becomes a `kappa`-gradient law

M17-143 gives the true time-unfolding coefficient at a director-area tangency:

\[
\boxed{
A_T
=D_Bg
=D_\xi(\sigma+\kappa).
}
\]

Using the previous section,

\[
\boxed{
A_T
=
D_\xi\kappa
+O(R^{-1/7}).
}
\]

Therefore, if the generic fold remains uniformly time-nondegenerate along a remote sequence,

\[
|A_T|\ge a_*>0,
\]

then for all sufficiently large `R`,

\[
\boxed{
|D_\xi\kappa|
\ge
\frac{a_*}{2}.
}
\]

Thus quiet-remote generic fold turnover cannot be serviced asymptotically by the ordinary strain-gradient term. It must be serviced by a nontrivial multiplier gradient.

---

## 5. Material slope derivative at tangency becomes the mixed `kappa` jet

M17-143 also gives, at `g=D_kg=0`,

\[
\boxed{
D_B(D_kg)
=
D_kD_\xi(\sigma+\kappa).
}
\]

Under the stronger third-strain-jet compactness,

\[
D_kD_\xi\sigma
=O(R^{-1/9}).
\]

Hence

\[
\boxed{
D_B(D_kg)
=
D_kD_\xi\kappa
+O(R^{-1/9}).
}
\]

This does **not** restore the invalid `D_B(D_kg)` fold-cost route; M17-143 already showed that a generic fold can occur with this quantity equal to zero.

Its value is instead diagnostic: any nontrivial material evolution of the tangency slope in the quiet high-jet limit is also asymptotically a multiplier-jet effect.

---

## 6. Exact fixed-time CE-H identity for `kappa`

The CE-H equation is

\[
\boxed{\Delta W=\kappa W.}
\]

Write

\[
W=\rho\xi,
\qquad
|\xi|=1.
\]

Then

\[
\Delta(\rho\xi)
=(\Delta\rho)\xi
+2\nabla\rho\cdot\nabla\xi
+\rho\Delta\xi.
\]

Dot with `xi`.
Because

\[
\xi\cdot\partial_i\xi=0
\]

and

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

we obtain

\[
\boxed{
\kappa
=
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2.
}
\]

Set

\[
\psi:=\log\rho.
\]

Since

\[
\frac{\Delta\rho}{\rho}
=
\Delta\psi+|\nabla\psi|^2,
\]

we have the exact normalized identity

\[
\boxed{
\kappa
=
\Delta\log\rho
+|\nabla\log\rho|^2
-|\nabla\xi|^2.
}
\]

---

## 7. Why low amplitude does not control the multiplier geometry

At the fixed-time CE-H level, replace

\[
\rho\mapsto\rho_\varepsilon:=\varepsilon\rho,
\qquad
\varepsilon>0.
\]

Then

\[
\log\rho_\varepsilon
=
\log\rho+\log\varepsilon,
\]

so all spatial derivatives of `log rho` are unchanged.
The director `xi` is unchanged as well.

Hence

\[
\boxed{
\kappa_\varepsilon=\kappa,
\qquad
\nabla\kappa_\varepsilon=\nabla\kappa,
}
\]

inside the homogeneous CE-H elliptic/director subsystem.

Likewise

\[
g=D_\xi\log\rho
\]

is unchanged by constant amplitude rescaling.

Therefore a low-amplitude branch

\[
\rho\to0
\]

can remain geometrically strong in the normalized quantities

\[
\xi,
\quad
J_\xi,
\quad
g,
\quad
\kappa,
\quad
\nabla\kappa.
\]

This is the precise scale-free firewall behind the M17-144 fold branch.

---

## 8. Scope audit: this is **not** a full Navier--Stokes scaling symmetry

The previous section must not be overread.

Scaling `W` and the corresponding velocity amplitude by a constant does not preserve the full nonlinear similarity Navier--Stokes equation in general, because the quadratic transport term scales differently from the linear terms.

Therefore M17-144 does **not** construct a family of full Navier--Stokes solutions with fixed `kappa` geometry.

It proves only the narrower statement:

\[
\boxed{
\text{the homogeneous fixed-time CE-H/director equations plus quadratic low-amplitude shell budgets}
}
\]

\[
\boxed{
\text{do not by themselves force }D_\xi\kappa\text{ or other normalized multiplier jets to vanish.}
}
\]

Any closure must use additional full coupled material dynamics.

---

## 9. Persistent ribbon takes the opposite branch

M17-115 gives the exact material persistence condition for a critical ribbon:

\[
\boxed{
D_\xi(\sigma+\kappa)=0.
}
\]

On the quiet high-jet remote branch,

\[
D_\xi\sigma=O(R^{-1/7}).
\]

Hence any persistent remote critical ribbon satisfies

\[
\boxed{
D_\xi\kappa
=O(R^{-1/7})
\to0.
}
\]

Thus the fold/ribbon alternatives separate cleanly:

\[
\boxed{
\begin{aligned}
&\text{uniformly nondegenerate generic fold}
&&\Rightarrow
|D_\xi\kappa|\gtrsim1,\\
&\text{persistent critical ribbon}
&&\Rightarrow
D_\xi\kappa\to0,
\end{aligned}
}
\]

under the stated quiet high-jet assumptions.

---

## 10. Updated transition taxonomy

The dominant quiet remote geometry-transition branch from M17-142 now separates into

\[
\boxed{
\begin{aligned}
G_{\rm frequent}^{almost\ all\ flux}
\Longrightarrow\;&
G_{\kappa\text{-fold}}
\lor
G_{\rm persistent\ ribbon}
\lor
G_{\rm higher\ jet}
\\
&\lor
G_{\rm rank/end/interface}
\lor
G_{\rm high\ strain\ jet}.
\end{aligned}
}
\]

where

\[
G_{\kappa\text{-fold}}
:
|D_\xi\kappa|\not\to0
\]

is the newly isolated scale-free turnover firewall.

The persistent-ribbon branch instead satisfies asymptotic `xi`-flatness of `kappa`.

The higher-jet branch includes

\[
A_T\to0,
\qquad
C_k=D_k^2g\to0,
\]

or higher finite-order tangency.

---

## 11. DSD audit

### Audit A — shell `L^2` smallness alone implies `D_xi sigma ->0`

Rejected.
A higher spatial strain-jet bound is explicitly required for the interpolation step.

### Audit B — compact director geometry alone bounds all strain derivatives

Rejected.
Strain-jet compactness and director-jet compactness are distinct hypotheses.

### Audit C — `rho ->0` implies `kappa ->0`

Rejected by the exact normalized CE-H identity. Constant amplitude scaling leaves `kappa` unchanged at the fixed-time elliptic level.

### Audit D — the CE-H amplitude scaling is a symmetry of full Navier--Stokes

Rejected.
It is only a homogeneity statement for the fixed-time elliptic/director subsystem.

### Audit E — nonzero `D_xi kappa` is itself a contradiction

Rejected.
No current global budget controls the positive director-flux measure of such multiplier-gradient events.

---

## 12. Highest-value next gate

M17-142 requires frequent geometry transition for almost all dominant remote ribbon flux.
M17-143 removes the invalid `D_B(D_k g)`-cost shortcut.
M17-144 shows that, on the quiet high-jet branch, a generic fold is asymptotically driven by

\[
\boxed{D_\xi\kappa.}
\]

The next efficient question is therefore:

\[
\boxed{
\text{Can order-one director-flux measure encounter }|D_\xi\kappa|\gtrsim1
\text{ at uniformly bounded log-radius spacing}
}
\]

while

\[
\int|\nabla U|^2=O(R^{-1}),
\qquad
\int|\nabla W|^2=O(R^{-1})?
\]

A successful next step must derive either

1. a flux-weighted spacetime budget for `D_xi kappa`, or
2. a material evolution/finite-jet recurrence law forcing these multiplier-gradient fold events into a higher-order degeneracy, rank loss, or critical-shell burst.

Without such an additional normalized-dynamics estimate, the generic `kappa`-gradient fold remains a genuine survivor.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
