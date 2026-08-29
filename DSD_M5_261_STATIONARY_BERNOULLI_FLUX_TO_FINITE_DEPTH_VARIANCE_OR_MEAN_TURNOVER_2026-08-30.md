# DSD M5-261 — Stationary Bernoulli Flux to Finite-Depth Variance / Mean-Turnover Fork

Date: 2026-08-30

Parent: `DSD_M5_260_UNIVERSAL_STATIONARY_RECURRENT_BERNOULLI_FLUX_POSITIVITY_2026-08-30.md`

Status: **POSITIVE TAIL-TO-FINITE-STAGE TURNOVER BRIDGE / ON A NONZERO COMPACT MINIMAL STATIONARY TAIL HULL THE SCALE-NORMALIZED OUTWARD PHYSICAL ENERGY CURRENT HAS A UNIFORM POSITIVE FLOOR; M5-248 TRANSFERS THIS THROUGH ONE FIXED RG DEPTH TO A SMOOTH W1 ANNULUS AND THEN TO DEEP FINITE FIRST-HITTING STAGES / ABSOLUTE LOCAL ENERGY FLUX IS NOT IDENTICAL TO MOVING RELATIVE-VARIANCE WORK: THEIR EXACT DIFFERENCE IS THE WEIGHTED-MEAN KINETIC-ENERGY / MOMENTUM CHANNEL PLUS GEOMETRIC CUTOFF MOTION / CONSEQUENTLY THE STATIONARY TAIL ENDPOINT FORCES EITHER RELATIVE-VARIANCE/BOUNDARY TURNOVER OR MEAN-MOMENTUM/CENTER TURNOVER AT FINITE SCALE / THE NUMERICAL NO-T THRESHOLD COMPARISON REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Uniform positive stationary energy current

For a stationary critical tail

\[
T=r^{-1}\Phi(\log r,\theta),
\qquad
H=P+\frac12|T|^2,
\]

M5-260 defines

\[
J_E
=HT-\nu\nabla\frac{|T|^2}{2},
\qquad
\nabla\cdot J_E=-\nu|\nabla T|^2.
\]

The physical flux through a sphere has the critical form

\[
F_E(r)=\int_{S_r}J_E\cdot n\,dS=r^{-1}j_T(\log r),
\]

with

\[
\boxed{
 j_T(y)
=
\nu\int_0^\infty e^{-a}d_T(y+a)\,da,
}
\]

where

\[
d_T(y)=\int_{S^2}
\left(
|\Phi_y-\Phi|^2+|\nabla_S\Phi|^2
\right)d\theta\ge0.
\]

Hence `j_T(y)>=0`.

---

## 2. Strict positivity on a nonzero minimal stationary hull

Fix the canonical radius `r=1`, i.e. `y=0`, and define

\[
\boxed{\mathfrak J(T):=j_T(0).}
\]

Suppose `mathfrak J(T0)=0` for a tail state in the stationary minimal hull. Since the kernel `e^-a` is strictly positive and `d>=0`,

\[
d_{T_0}(a)=0
\qquad\text{for a.e. }a\ge0.
\]

By smoothness this holds for all `a>=0`.

Thus every forward log-translate of `T0` has zero critical Dirichlet density. The forward translation orbit is dense in the compact minimal hull, so continuity gives zero density on the whole hull.

As in M5-260, zero density forces the tail to be the zero divergence-free field.

Therefore on a **nonzero** compact minimal stationary hull,

\[
\boxed{\mathfrak J(T)>0\qquad\forall T.}
\]

By compactness and continuity,

\[
\boxed{
\inf_{T\in\mathcal T_{stat}}\mathfrak J(T)
=:j_*>0.
}
\]

This is stronger than positivity only in invariant mean.

---

## 3. Fixed-depth RG transfer

The current functional on a fixed sphere depends continuously on velocity, pressure, and one spatial derivative on a slightly larger annulus.

On the strong stationary-tail corridor, the RG reconstruction satisfies uniformly on fixed punctured annuli

\[
\mathscr R_\rho(T)\to T
\]

in the corresponding local topology as `rho->0`; the pressure is reconstructed with the standard local gauge/elliptic control.

Therefore choose one fixed

\[
\boxed{0<\rho_*\ll1}
\]

such that for every stationary tail state

\[
\boxed{
\mathfrak J_{\rho_*}(T)
:=
\text{outward energy-current functional of }\mathscr R_{\rho_*}(T)
\ge\frac{j_*}{2}.
}
\]

This is precisely the M5-248 fixed-depth inheritance mechanism applied to the signed energy-current certificate.

---

## 4. Transfer to W1 and finite first-hitting stages

The fixed depth `rho_*` corresponds to one finite similarity descendant time / finite normalized scale factor.

Hence each W1 state on the stationary-tail conjugacy class carries, on one fixed normalized annulus/sphere,

\[
\boxed{
\mathfrak J_{W1}(s)\ge j_*/2
}
\]

in the fixed-depth normalization.

Strong local compactness of the finite first-hitting sequence then transfers the same strict sign, with a further harmless loss, to sufficiently deep finite stages on the corresponding physical spheres:

\[
\boxed{
\mathfrak J_j(t)
\ge j_*/4
}
\]

in scale-normalized units on the selected finite windows.

No expanding-window convergence is used.

---

## 5. Absolute local kinetic-energy identity

For a smooth physical Navier--Stokes solution and a **fixed** smooth cutoff `phi`, define

\[
E_\phi
:=
\frac12\int\phi|u|^2dx.
\]

Then

\[
\boxed{
E_\phi'
+\nu\int\phi|\nabla u|^2dx
=
\frac12\int|u|^2
(u\cdot\nabla\phi+\nu\Delta\phi)dx
+\int p\,u\cdot\nabla\phi\,dx.
}
\]

For sharp-ball approximation this becomes

\[
\boxed{
\frac{d}{dt}\frac12\int_{B_R}|u|^2dx
+\nu\int_{B_R}|\nabla u|^2dx
=-\int_{\partial B_R}J_E\cdot n\,dS.
}
\]

Thus positive outward current is a genuine local absolute-energy export.

---

## 6. Exact relation to relative variance

Let

\[
M_\phi(t):=\int\phi(x,t)dx,
\qquad
P_\phi(t):=\int\phi u\,dx,
\qquad
\bar u_\phi:=\frac{P_\phi}{M_\phi}.
\]

The weighted relative variance is

\[
V_\phi
:=
\frac12\int\phi|u-\bar u_\phi|^2dx.
\]

Exactly,

\[
\boxed{
V_\phi
=E_\phi
-\frac{|P_\phi|^2}{2M_\phi}
=E_\phi-\frac{M_\phi}{2}|\bar u_\phi|^2.
}
\]

Therefore

\[
\boxed{
V_\phi'
=E_\phi'
-\bar u_\phi\cdot P_\phi'
+\frac12|\bar u_\phi|^2M_\phi'.
}
\]

For a fixed-volume translated cutoff, `M_phi'=0`, so

\[
\boxed{
V_\phi'=E_\phi'-\bar u_\phi\cdot P_\phi'.
}
\]

Thus absolute energy export can disappear from the relative-variance ledger only by being transferred into the weighted mean-momentum energy channel.

---

## 7. Weighted momentum equation

From

\[
u_t+\nabla\cdot(u\otimes u)+\nabla p=\nu\Delta u,
\]

the weighted momentum obeys

\[
\boxed{
\begin{aligned}
P_\phi'
={}&\int\phi_tu\,dx
+\int(u\otimes u)\nabla\phi\,dx
+\int p\nabla\phi\,dx
+\nu\int u\Delta\phi\,dx.
\end{aligned}
}
\]

For a sharp fixed ball this is the negative momentum-stress flux through the boundary.

Consequently the correction

\[
\bar u_\phi\cdot P_\phi'
\]

is a genuine mean-momentum / translational-energy flux, not an algebraic artifact.

---

## 8. Moving/dilating cutoff

For

\[
\phi(x,t)
=\Phi\!\left(\frac{x-X(t)}{\ell(t)}\right),
\]

one additionally has the geometric terms generated by `phi_t` and by

\[
M_\phi'
=3\frac{\dot\ell}{\ell}M_\phi
\]

for a pure dilation of a fixed cutoff profile.

The exact relative-variance ledger already records these as

\[
\mathcal T_{mat},\quad
\mathcal T_{rad},\quad
\mathcal T_{vis},\quad
\mathcal T_{pres}.
\]

Therefore the absolute-energy current is **not** silently identified with any one of those terms.

---

## 9. Dilation-adapted mean center

The earlier local material-flux reduction chooses the normalized center velocity so that

\[
 a_s
=\bar U_\phi+\frac b2a.
\]

Then absolute translation and deterministic similarity dilation are separated from genuine relative crossing, and the dilation contribution has favorable sign for radial decreasing enstrophy cutoffs.

This means the extra mean-momentum channel exposed above can be represented geometrically as

\[
\boxed{
\text{weighted-mean evolution / center motion}
}
\]

rather than being hidden inside material flux.

---

## 10. Finite-stage turnover fork

On the inherited finite-stage windows, the positive outward energy current has a fixed normalized floor.

Use the identity

\[
V_\phi=E_\phi-\frac{M_\phi}{2}|\bar u_\phi|^2.
\]

If both

1. all normalized relative-variance/boundary actions are below the no-turnover thresholds; and
2. the weighted-mean kinetic/momentum term has subthreshold variation/action,

then the absolute local energy export cannot retain the inherited positive floor over the same recurrent window.

Therefore the stationary-tail endpoint forces the exact formed alternative

\[
\boxed{
T_{stat}
\Longrightarrow
T_{var/bdry}
\quad\lor\quad
T_{mean/center}.
}
\]

Here

\[
T_{var/bdry}
\]

is the existing moving relative-variance / material / pressure / viscous-boundary family, while

\[
T_{mean/center}
\]

is the weighted mean-momentum / center-motion complement required by the exact absolute-to-relative decomposition.

---

## 11. What remains quantitative

The argument above identifies the **type** of payer and supplies a positive stationary-tail current floor `j_*`.

To close the stationary branch completely, one must compare `j_*` after the fixed-depth losses with the numerical no-T thresholds already chosen for

\[
\mathcal T_{mat},\ \mathcal T_{rad},\ \mathcal T_{vis},\ \mathcal T_{pres},
\]

and define a matching normalized threshold for the mean/center term.

At present no claim is made that the inherited current floor exceeds those thresholds universally.

Thus this is a finite-channel reduction, not yet an exclusion theorem.

---

## 12. DSD verdict

### PROVED / FORMED

- nonzero compact minimal stationary tail hull gives a **uniform** positive scale-normalized outward energy-current floor;
- this floor transfers through one fixed RG depth to W1 and then to deep finite first-hitting stages;
- absolute local energy and relative variance differ exactly by weighted-mean kinetic energy;
- therefore positive export must appear as relative boundary/variance turnover or as weighted mean-momentum/center turnover.

### FIREWALL

Stationary absolute energy current is not identical to the relative-variance boundary work.

### UPDATED STATIONARY ENDPOINT

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
T_{var/bdry}\lor T_{mean/center}.
}
\]

### NEXT TARGET

Normalize the mean/center channel in the same first-hitting units and combine it with the existing center-nesting/no-T displacement bound. If the required persistent mean-momentum action forces an `O(r_j)` center displacement with a coefficient above the no-T ceiling, the stationary branch closes; otherwise record the exact surviving center-action window.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
