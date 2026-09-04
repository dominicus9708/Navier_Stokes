# DSD M17-132 — Ribbon tail recompressed to CE-H realization rigidity of the K^-1 weighted-flux cascade

Date: 2026-09-05
Canonical ID: **M17-132**

Status: **FRONTIER RECOMPRESSION THROUGH M17-131 / THE M5 NON-L3 DIRICHLET TAIL IS NOW AN EQUIVALENT VORTICITY CRITICAL STACK. ON A NONDEGENERATE COMPLETE-RIBBON SUBSET THIS BECOMES `sum(K_k Phi_k)^(3/2)=infinity`, WITH SHARP MODEL `Phi_k~K_k^-1`. FOUR NATURAL CLOSURE ROUTES HAVE BEEN AUDITED AND ARE TOO WEAK: UNWEIGHTED DIRECTOR FLUX IS SUMMABLE; SIGNED RADIAL FLUX/DEGREE IS BLIND TO CLOSED LOOPS; ORDINARY PALINSTROPHY COST IS ALSO SUMMABLE; AND QUIET SAME-MATERIAL ANCESTOR TRACKING LOSES `K_k^-4` IN PHYSICAL WEIGHTED ENSTROPHY. INTERNAL COMPLETE-RIBBON FLUX-CAPTURE FAILURE IN A FIXED BOUNDED CORE IS PUSHED TO DIRECTOR-AREA/RANK-ONE ACCUMULATION OR BOUNDARY/RIBBON-COVER EXIT. THE CENTRAL UNRESOLVED COMPACT-RIBBON QUESTION IS THEREFORE WHETHER THE FULL CE-H WEIGHTED-HARMONIC/MATERIAL SYSTEM CAN REALIZE A NESTED `Phi_k~K_k^-1` CASCADE AT ALL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vorticity form of the ancient critical tail

M17-121 establishes

\[
\boxed{
\sum_k(J_k^\omega)^{3/2}=\infty
}
\]

whenever the retained M5 non-`L^3` Dirichlet critical tail survives.

This uses a dyadic Biot–Savart/Herz bridge and removes the local Hodge-boundary ambiguity.

---

## 2. Ribbon flux disintegration

M17-122 gives on regular pure-kernel ribbon tubes

\[
\boxed{
dV=\frac{d\Phi_J\,ds}{|J_\xi|}
}
\]

and

\[
\boxed{
E_T^\omega
=\int\mathcal W_J(\lambda)d\Phi_J,
\qquad
\mathcal W_J
=\oint\frac{\rho^2}{|J_\xi|}ds.
}
\]

On a uniformly nondegenerate complete-ribbon class,

\[
\boxed{
J_{k,rib}^\omega
\asymp K_k\Phi_k.
}
\]

---

## 3. Internal flux-capture failure is geometrically narrowed

M17-123 gives the exact scale-invariant area-ratio law

\[
\boxed{
D_B\log\eta_J
=\sigma_k-\sigma-\kappa,
\qquad
\eta_J=|J_\xi|/\rho.
}
\]

Finite regular residence prevents arbitrarily severe area-ratio collapse from uniformly nondegenerate incoming carriers.
Persistent collapse therefore arrives through fresh carriers already approaching the `J_xi=0` rank-deficient boundary.

M17-124 shows that for a complete critical circle wholly inside a fixed bounded spatial core,

\[
\boxed{
|q|\ge2/\operatorname{diam}(\Omega).
}
\]

Hence `q->0` flattening is not an internal complete-ribbon escape; it becomes a boundary/ribbon-cover exit.

Thus

\[
\boxed{
R_2^{ribbon}(\Omega)
\Longrightarrow
F_{capture}^{nondeg}
\lor
A_{R1}^{fresh-carrier}
\lor
T_{boundary/ribbon-cover}.
}
\]

---

## 4. Corrected residence audit

M17-125 retains only

\[
\boxed{
\frac{\Delta t_{current\ carrier}}{\rho_{j,k}^2}
\lesssim K_k^{-2}.
}
\]

The earlier `K_k^2` historical carrier-count inference was retracted.
Over the actual historical similarity interval

\[
\theta_j-\theta_{j-k}=2\log K_k,
\]

a uniform finite per-carrier similarity residence yields only a conditional `O(log K_k)` sequential-count lower bound under gap-free ribbon coverage.

---

## 5. Spatial genealogy sharpened, amplitude genealogy scalarized

M17-126 proves under bounded similarity velocity that a remote material carrier at stage `j` lies at a comparable ancestor physical radius at stage `j-k`.

M17-127 then gives the exact CE-H amplitude ledger

\[
\boxed{
\log\frac{\rho_j}{\rho_{j-k}}
=
\mathcal E_\rho(j,k)
:=
\int_{\theta_{j-k}}^{\theta_j}
(\sigma+\kappa-1)d\theta.
}
\]

The general additive diffusion-exposure branch disappears inside CE-H because `Delta W=kappa W`.

---

## 6. Quiet same-carrier tracking is still physically too weak

M17-128 shows that if

\[
|\mathcal E_\rho(j,k)|\le L,
\]

then similarity amplitudes are comparable but physical vorticity obeys

\[
|\omega_{j-k}|
\asymp_L
K_k^{-2}|\omega_j|.
\]

Physical material volume is preserved, so

\[
\boxed{
J_{j-k}^{\omega,mat}
\asymp_L
K_k^{-4}J_{j,k}^{\omega,mat}.
}
\]

Thus exact quiet genealogy does not supply an order-one ancestor weighted-enstrophy cost.

---

## 7. Weighted director-flux critical stack

M17-129 converts a cubic-divergent ribbon contribution to

\[
\boxed{
\sum_k(K_k\Phi_k)^{3/2}=\infty.
}
\]

The scale-critical model is

\[
\boxed{
\Phi_k\sim K_k^{-1}.
}
\]

Then

\[
K_k\Phi_k\sim1
\]

but

\[
\boxed{
\sum_k\Phi_k<\infty.
}
\]

Therefore unweighted director-area charge is subcritical for this obstruction.

---

## 8. Signed radial flux and degree do not see the needed quantity

M17-130 shows

\[
\nabla\cdot(f(r)J_\xi)
=f'(r)J_\xi\cdot\widehat r
\]

controls only signed radial flux.
Closed ribbon loops can carry positive internal tube flux while contributing zero to every sufficiently large enclosing sphere.

Likewise the degree of `xi|S_R`, when defined, controls only algebraic closed-surface area charge.

Hence neither provides a coercive bound for

\[
\Phi_k
\]

or its weighted cubic stack.

---

## 9. Positive palinstrophy cost is also subcritical

M17-131 gives

\[
\boxed{
2\rho^2|J_\xi|
\le
|\nabla W|^2.
}
\]

Thus ribbon flux has a positive palinstrophy cost.
But on a compact nondegenerate ribbon with

\[
\Phi_k\sim K_k^{-1},
\]

the unweighted shell cost can also be

\[
P_k^{rib}\sim K_k^{-1},
\]

which is summable.

Therefore ordinary palinstrophy does not close the critical weighted flux stack.

---

## 10. Four pruned shortcut routes

The following are now explicitly insufficient for the sharp compact-ribbon model:

\[
\boxed{
\begin{aligned}
&\text{finite unweighted director-area flux},\\
&\text{signed radial flux / degree},\\
&\text{finite ordinary palinstrophy},\\
&\text{quiet same-material ancestor tracking}.
\end{aligned}
}
\]

Each fails for a quantitatively identified reason rather than an unspecified gap.

---

## 11. Current compact-ribbon hard gate

The remaining compact-ribbon survivor is a CE-H realization problem:

\[
\boxed{
\begin{gathered}
\partial_\theta\text{/material CE-H system},\\
\Delta W=\kappa W,\\
D_B\xi=0,\\
\text{weighted-harmonic director equation},\\
J_\xi\ne0,\quad D_k\xi=0,\\
\text{critical-ribbon compatibility when applicable},\\
\sum(K_k\Phi_k)^{3/2}=\infty,\\
\Phi_k\sim K_k^{-1}\text{ at the sharp frontier}.
\end{gathered}
}
\]

The question is no longer whether one elementary conservation law sees the tail. It is whether all these equations can be satisfied by an infinite nested/recurrent ribbon family with this exact scale law.

---

## 12. Next targets

The next calculations should be ordered as follows:

1. **CE-H ribbon realization rigidity:** derive the scale law forced on `rho`, `|J_xi|`, loop curvature and weighted-harmonic shear by `Phi_k~K_k^-1` and test compatibility with the exact material exponents.
2. **Boundary-cover branch:** if loops decompactify instead, derive the corresponding transversality/throughput equations without replacing signed flux by total variation.
3. **Rank-1 accumulation branch:** pass fresh-carrier `J_xi->0` limits into the existing Rank-1 pressure/angular-defect firewalls.
4. If all three remain compatible, return the unresolved tail to the Liouville/tail-decoupling program rather than repeating unweighted moment arguments.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
