# Occupied Palinstrophy Packet → Return-Weight Gate

Date: 2026-08-25

Status: **LOCAL PERSISTENCE / ENERGY-DESCENT LEMMA PROVED; GENEALOGY APPLICATION CONDITIONAL; GLOBAL REGULARITY NOT PROVED.**

This note attacks the `P` branch selected by `CUBIC_MASS_GENEALOGY_DEFICIT_LEDGER_2026-08-25.md`.

The repository's weighted-return ledger is written in the normalization `nu=1`.  We derive the local statement with general viscosity `nu>0` and state the normalized genealogy consequence afterward.

---

## 1. Occupied high-vorticity core

Fix a smooth pre-singular time `t0` and a reference vorticity amplitude `W_*>0` with natural radius

\[
r_*:=\left(\frac{\nu}{W_*}\right)^{1/2}.
\]

Suppose there is a measurable set

\[
A_0\subset B_d(x_0)
\]

such that

\[
|A_0|\ge \kappa d^3,
\qquad
|\omega(x,t_0)|\ge aW_*
\quad(x\in A_0),
\]

where `a,kappa>0` are fixed occupancy constants.

Write

\[
m:=\frac d{r_*}.
\]

The pointwise inequality

\[
|\omega|^2\le 2|\nabla u|^2
\]

gives

\[
\int_{A_0}|\nabla u|^2dx
\ge
\frac12a^2W_*^2|A_0|
\ge
c_{a,\kappa}W_*^2d^3.
\]

Since

\[
W_*^2=\frac{\nu^2}{r_*^4},
\]

we obtain

\[
\boxed{
 d\int_{A_0}|\nabla u|^2dx
\ge
c_{a,\kappa}\nu^2m^4.
}
\]

Thus occupied high vorticity already descends from the palinstrophy/direction-curvature branch to a first-order kinetic-dissipation cost.

**Status: PROVED.**

---

## 2. Lagrangian amplitude persistence

Let `X(t;t0,x)` be the classical flow map of the smooth solution and

\[
A(t):=X(t;t_0,A_0).
\]

Because `div u=0`,

\[
|A(t)|=|A_0|.
\]

Along each trajectory,

\[
\frac d{dt}\omega(X(t),t)=D_t\omega(X(t),t),
\]

where

\[
D_t\omega=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]

Suppose on a candidate interval `I=[t0,t0+tau]`

\[
\sup_I\|D_t\omega\|_{L^\infty}
\le
L_\omega\frac{\nu W_*}{d^2}.
\]

Then

\[
|\omega(X(t),t)-\omega(x,t_0)|
\le
L_\omega\frac{\nu W_*}{d^2}|t-t_0|.
\]

Hence if

\[
\frac{\nu\tau}{d^2}
\le
\frac a{2(1+L_\omega)},
\]

then throughout `I`

\[
|\omega(X(t),t)|\ge \frac a2W_*
\qquad(x\in A_0).
\]

Consequently

\[
\boxed{
\int_{A(t)}|\nabla u|^2dx
\ge
c_{a,\kappa}\frac{\nu^2d^3}{r_*^4}
\qquad(t\in I).
}
\]

No spatial ball-shape preservation is used here; only incompressible volume preservation and the material derivative bound are needed.

**Status: PROVED.**

---

## 3. Return-like residence length and dissipation cost

Define the physical residence length

\[
\boxed{
\mathfrak L_P(I;d)
:=
\frac{\nu|I|}{d}.
}
\]

In the `nu=1` normalization this is exactly `|I|/d`, the same dimensional form as each contribution `tau/rho` to the repository's return density.

Integrating the previous lower bound gives

\[
\begin{aligned}
\nu\int_I\int_{A(t)}|\nabla u|^2dxdt
&\ge
c_{a,\kappa}\nu\,|I|\frac{\nu^2d^3}{r_*^4}\\
&=
c_{a,\kappa}\nu^2
\left(\frac d{r_*}\right)^4
\frac{\nu|I|}{d}.
\end{aligned}
\]

Therefore

\[
\boxed{
\nu\int_I\int_{A(t)}|\nabla u|^2dxdt
\ge
c_{a,\kappa}\nu^2m^4\mathfrak L_P.
}
\]

If the material-vorticity growth cap is bounded by `L_omega`, we may take a persistence interval of order

\[
\tau_P
\gtrsim_a
\frac{d^2}{\nu(1+L_\omega)},
\]

and hence

\[
\boxed{
\mathfrak L_P
\gtrsim_a
\frac d{1+L_\omega}.
}
\]

The corresponding dissipation packet obeys

\[
\boxed{
\nu\int_{I_P}\int_{A(t)}|\nabla u|^2dxdt
\gtrsim_{a,\kappa}
\nu^2m^4\frac d{1+L_\omega}.
}
\]

**Status: PROVED whenever the displayed material-derivative cap holds on the chosen interval.**

---

## 4. PDE content of the temporal escape

From

\[
D_t\omega=(\omega\cdot\nabla)u+\nu\Delta\omega,
\]

on a packet whose vorticity amplitude is comparable to `W_*`,

\[
\frac{d^2}{\nu W_*}|D_t\omega|
\lesssim
\frac{d^2}{\nu}|\nabla u|
+
\frac{d^2}{W_*}|\Delta\omega|.
\]

Define

\[
H_d
:=
\frac{d^2}{\nu}\|\nabla u\|_{L^\infty},
\]

and

\[
K_{\omega,2;d}
:=
\frac{d^2}{W_*}\|\Delta\omega\|_{L^\infty}.
\]

Then one may take schematically

\[
\boxed{L_\omega\lesssim H_d+K_{\omega,2;d}.}
\]

Therefore a P-packet can avoid a natural-order residence interval only through at least one of

\[
\boxed{
H_d\gg1
\qquad\text{or}\qquad
K_{\omega,2;d}\gg1.
}
\]

The second quantity is a third-velocity-derivative / second-vorticity-derivative needle and therefore feeds the existing `N` branch.

The first is a normalized strong-deformation escape.  It is not declared closed here; it must be joined to the already derived pointwise-gradient / pressure-Hessian / derivative-descent gates.

**Status: PROVED as a local alternative; no contradiction yet.**

---

## 5. Connection with the direction-curvature packet

The previous direction-curvature calculation produced a spatial persistence factor

\[
m_\xi
:=
\min\left\{1,\frac b{1+k_3}\right\},
\]

with

\[
b=r_*^2|P_{\xi^\perp}\nabla^2\xi|,
\qquad
k_3=r_*^3\|\nabla^3\xi\|_\infty,
\]

and a packet radius

\[
d\gtrsim m_\xi r_*.
\]

When high-vorticity occupancy holds on that packet,

\[
m=\frac d{r_*}\gtrsim m_\xi.
\]

Thus the first-order occupied-core cost satisfies

\[
\boxed{
 d\int|\nabla u|^2
\gtrsim
\nu^2m_\xi^4.
}
\]

and, under the temporal cap,

\[
\boxed{
\mathfrak L_P
\gtrsim
\frac{m_\xi r_*}{1+H_d+K_{\omega,2;d}}.
}
\]

Consequently a genuine direction-curvature P-packet with no third-derivative needle (`k3` controlled) and no temporal-deformation escape has an order-`r_*` return residence length.

**Status: PROVED CONDITIONAL on the occupancy alternative.**

---

## 6. Genealogy return gate

Suppose a physical P-packet is identified with an ancient annular label `k` so that

1. its tracked physical scale is comparable to the ancestor scale used in `mathfrak R_k`,
2. its material packet remains inside the tracked shell family during `I_P`, and
3. the existing amplitude-retention / finite-overlap hypotheses of `ANCESTOR_RADIUS_IDENTITY_AND_WEIGHTED_RETURN_DENSITY_2026-08-25.md` hold.

Then its residence contributes to the return density:

\[
\boxed{
\mathfrak R_k
\gtrsim
\mathfrak L_{P,k}
\gtrsim
\frac{d_k}{1+H_{d_k}+K_{\omega,2;d_k}}.
}
\]

In the repository normalization `nu=1`, define the P-branch health ratio

\[
\boxed{
\Phi_k^P
:=
\frac{d_k}
{J_k^{1/2}\,[1+H_{d_k}+K_{\omega,2;d_k}]}.
}
\]

Whenever the physical/ancient scale identification makes the displayed ratio meaningful,

\[
\boxed{
\frac{\mathfrak R_k}{J_k^{1/2}}
\gtrsim
\Phi_k^P.
}
\]

This is exactly the branch-health structure targeted by the cubic-mass deficit ledger.

**Status: PROVED CONDITIONAL on the genealogy identification and return-ledger hypotheses.**

---

## 7. Consequence on a cubic-divergent P-deficit branch

Suppose the fixed survivor selected by the finite-partition lemma is `P`.

For every `epsilon>0`, its severe-deficit set carries divergent cubic mass while

\[
\frac{\mathfrak R_k}{J_k^{1/2}}<\varepsilon.
\]

The P-return gate implies on those labels

\[
\boxed{
\frac{d_k}
{J_k^{1/2}\,[1+H_{d_k}+K_{\omega,2;d_k}]}
\lesssim
\varepsilon.
}
\]

Therefore a cubic-divergent P branch cannot simultaneously retain

- packet radius comparable from below to `J_k^{1/2}`, and
- bounded normalized deformation `H_d`, and
- bounded normalized vorticity Laplacian `K_{omega,2;d}`.

Along arbitrarily severe deficit labels, it must escape through at least one of

\[
\boxed{
\frac{d_k}{J_k^{1/2}}\to0,
\qquad
H_{d_k}\to\infty,
\qquad
K_{\omega,2;d_k}\to\infty,
}
\]

in the usual subsequential sense.

The last alternative is already the higher-derivative needle branch.  The first is spatial microcollapse; the middle is temporal/geometric deformation.

**Status: PROVED CONDITIONAL on the genealogy identification.**

---

## 8. Audit table

| Claim | Status |
|---|---|
| Occupied high-vorticity core gives `d int |grad u|^2 >= c nu^2 (d/r)^4` | **PROVED** |
| Material packet volume is preserved | **PROVED for smooth pre-singular flow** |
| Bounded normalized `D_t omega` gives residence time `tau >= c d^2/[nu(1+L_omega)]` | **PROVED** |
| Residence gives first-order dissipation packet `>= c nu^2 m^4 L_P` | **PROVED** |
| Temporal escape reduces to large normalized `grad u` or normalized `Delta omega` | **PROVED** |
| Direction-curvature packet with occupancy yields `d >= c m_xi r` | **PROVED by imported spatial persistence lemma** |
| Such a packet contributes directly to the repository return density | **PROVED CONDITIONAL on physical/ancient tracking and existing return-ledger hypotheses** |
| Severe P-deficit forces microcollapse or deformation escape or derivative needle | **PROVED CONDITIONAL** |
| Any one of those escapes is impossible | **NOT DERIVED** |
| Global regularity | **UNPROVED** |

---

## 9. Updated P-branch frontier

The palinstrophy/occupied-direction-curvature branch is no longer merely a higher-order instantaneous certificate.  It descends to the first-order Leray dissipation channel and acquires a quantitative residence length:

\[
\boxed{
P
\Longrightarrow
\text{first-order occupied dissipation}
+
\begin{cases}
\text{return residence},\\
\text{spatial microcollapse},\\
\text{strong deformation},\\
\text{higher-derivative needle}.
\end{cases}
}
\]

The next useful calculation is to attack the two genuinely new escapes in this line: spatial microcollapse and strong deformation.  The derivative escape already rejoins `N`.