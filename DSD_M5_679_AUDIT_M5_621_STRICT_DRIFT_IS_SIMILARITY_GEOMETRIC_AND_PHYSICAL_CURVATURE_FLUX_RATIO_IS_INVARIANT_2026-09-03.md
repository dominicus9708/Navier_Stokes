# DSD M5-679 — Audit: the M5-621 `-3/2` drift is similarity-geometric; the physical curvature-amplitude/flux ratio is invariant

Date: 2026-09-03

Status: **DSD SCALING AUDIT / THE M5-621 LAW `D_theta log[(rho_y |K_y|)/|Phi|]=-3/2` IS EXACT AND VALID ON THE SIMILARITY HULL, BUT AFTER RETURNING TO PHYSICAL VARIABLES `W=a Omega`, `K_y=sqrt(a) K_x`, `a=-s`, THE FACTOR IS EXACTLY `a^{3/2}` / THE CORRESPONDING PHYSICAL MATERIAL QUANTITY `|Omega||K_x|/|Phi|` IS CONSTANT, NOT DISSIPATIVE / THEREFORE M5-621 CAN EXCLUDE PERMANENT REUSE OF ONE FIXED-FLUX LABEL AT A FIXED NORMALIZED CURVATURE SCALE, BUT IT CANNOT BY ITSELF BE USED AS AN IRREVERSIBLE PHYSICAL FLUX-RESOURCE LOSS ACROSS GENERATIONS / THIS EXPLAINS THE CRITICAL NESTED-LABEL ESCAPE IDENTIFIED IN M5-678 / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity/physical conversion

Let

\[
a:=-s>0,
\qquad
\theta=-\log a,
\qquad
y=\frac{x}{\sqrt a}.
\]

The similarity vorticity is

\[
\boxed{W(y,\theta)=a\,\Omega(x,s).}
\]

The vorticity direction is scale invariant:

\[
\xi_y=\xi_x.
\]

Because

\[
\nabla_y=\sqrt a\,\nabla_x,
\]

the vortex-line curvature transforms as

\[
\boxed{
\mathcal K_y
=(\xi\cdot\nabla_y)\xi
=\sqrt a\,\mathcal K_x.
}
\]

Vorticity flux is scale invariant:

\[
\boxed{
\Phi_y
=\int W\cdot n_y\,dA_y
=\int \Omega\cdot n_x\,dA_x
=\Phi_x.
}
\]

---

## 2. Transformation of the M5-621 ratio

Therefore

\[
\frac{\rho_y|\mathcal K_y|}{|\Phi|}
=
\frac{a|\Omega|\,\sqrt a|\mathcal K_x|}{|\Phi|}.
\]

Thus

\[
\boxed{
\frac{\rho_y|\mathcal K_y|}{|\Phi|}
=
a^{3/2}
\frac{|\Omega||\mathcal K_x|}{|\Phi|}.
}
\]

Since

\[
a^{3/2}=e^{-3\theta/2},
\]

the universal exponential in M5-621 is exactly the similarity scaling factor.

---

## 3. Direct physical material laws

On physical CE-H, write

\[
\Delta_x\Omega
=\kappa_{phys}\Omega
\]

and

\[
\Sigma_{phys}\Omega
=\sigma_{phys}\Omega.
\]

The physical material amplitude equation is

\[
\boxed{
D_t\log|\Omega|
=\sigma_{phys}+\kappa_{phys}.
}
\]

For a material vortex line whose direction is frozen,

\[
\boxed{
D_t\log|\mathcal K_x|
=-\sigma_{phys}.
}
\]

The material vorticity-flux law is

\[
\boxed{
D_t\log|\Phi|
=\kappa_{phys}.
}
\]

Subtracting gives

\[
\boxed{
D_t\log
\frac{|\Omega||\mathcal K_x|}{|\Phi|}
=0.
}
\]

Hence

\[
\boxed{
\frac{|\Omega||\mathcal K_x|}{|\Phi|}
\quad\text{is a physical material invariant.}
}
\]

---

## 4. Recovery of the similarity `-3/2` law

Because

\[
\frac{d\theta}{ds}=\frac1a,
\]

and the physical ratio is constant, differentiating

\[
R_{sim}=a^{3/2}R_{phys}
\]

with respect to `theta` gives

\[
\boxed{
\frac d{d\theta}\log R_{sim}
=-\frac32.
}
\]

Thus M5-621 is fully consistent and exact.
The audit changes only its interpretation.

---

## 5. Geometric meaning

For a small transverse material tube section of area `A_perp`,

\[
\Phi\simeq|\Omega|A_\perp.
\]

Hence

\[
\frac{|\Omega||\mathcal K_x|}{|\Phi|}
\simeq
\frac{|\mathcal K_x|}{A_\perp}.
\]

In physical incompressible flow,

\[
D_t\log A_\perp=-\sigma_{phys},
\]

while

\[
D_t\log|\mathcal K_x|=-\sigma_{phys}.
\]

So their ratio is indeed invariant.

The similarity dilation introduces an additional universal area/curvature scaling and produces the apparent `-3/2` drift.

---

## 6. What M5-621 still legitimately proves

On the similarity recurrent phase space, a retained label has

\[
0<\phi_-\le|\Phi|\le\phi_+,
\qquad
\rho|\mathcal K_y|\ge z_*
\]

when it is counted as a fixed-strength curvature carrier.

Because the normalized ratio decays as `e^{-3 theta/2}`, one fixed retained label cannot remain at that same normalized scale forever.

Thus the conclusion

\[
\boxed{
\text{persistent normalized curvature activity requires label renewal/scale descent}
}
\]

remains valid.

What is not valid is the stronger interpretation

\[
\text{`each generation physically dissipates a fixed amount of curvature-flux resource'}.
\]

---

## 7. Why M5-678 is the correct remaining escape

A label first activated at late similarity time must have a physical invariant ratio large enough that, after multiplication by `a^{3/2}`, it still reaches the normalized event threshold.

This is achieved by taking a smaller base transverse flux element.
M5-678 quantified the necessary base scaling as

\[
\phi_0\lesssim e^{-3\Delta\theta/2}.
\]

That is exactly the same exponent as the backward material-volume scaling.

Therefore the remaining nested-label mechanism is not an artefact of a loose estimate; it is the exact scaling escape allowed by the physical invariant.

---

## 8. Consequence for the proof strategy

A final contradiction cannot rely only on the M5-621 `-3/2` similarity drift.
It must use a genuinely PDE-dissipative or elliptic fact that is absent from pure material rescaling, for example

- irreversible relative flux loss in a sign-preserving `kappa` corridor (M5-648--649),
- the elliptic eigenfield equation `Delta W=kappa W`,
- the generalized-kappa-force stress law,
- the strain/pressure identities M5-671--674,
- or a new bound preventing the critical `kappa` amplification required by M5-678.

This firewall prevents the final cycle argument from counting similarity scaling itself as viscosity-induced irreversibility.

---

## 9. Updated frontier

The hard survivor is now precisely a critical nested amplification cascade:

\[
\boxed{
\text{smaller base material flux}
\xrightarrow{\text{positive integrated }\kappa}
\text{order-one retained flux + curvature packet}
\xrightarrow{\text{normalized scale drift}}
\text{replacement by an even smaller base population}.
}
\]

The next calculation must constrain the required long-time positive `kappa` amplification using the CE-H elliptic/spatial identities rather than the similarity cocycle itself.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
