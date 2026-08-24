# DSD time-integrated derivative-occupancy descent

Date: 2026-08-25

Status: **TIME-INTEGRATED GRADIENT OCCUPANCY -> PALINSTROPHY/HESSIAN PRODUCT GATE PROVED / INSTANTANEOUS DERIVATIVE LADDER NOT REUSED AS A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

This note continues `VORTICITY_FIRST_HITTING_STRAIN_ENERGY_TAX_2026-08-25.md` and is audited against `OCCUPANCY_FAILURE_FINITE_WITNESS_DERIVATIVE_DESCENT_2026-08-25.md` and `DSD_FINITE_DERIVATIVE_WITNESS_LADDER_AUDIT_2026-08-25.md`.

The purpose is to treat the surviving **time-integrated** near-vorticity-gradient occupancy as its own formed channel rather than silently replacing it by an instantaneous derivative needle.

## 1. First-hitting input

Let

\[
W(t)=\|\omega(t)\|_\infty,
\qquad
r(t)=\left(\frac{\nu}{W(t)}\right)^{1/2}.
\]

On the first-hitting epoch

\[
I_j=(t_{j-1},t_j),
\qquad
W_j=qW_{j-1},
\]

let

\[
C_j:=I_j\cap\{\overline W=W\}
\]

be the running-maximum contact set and

\[
\Theta_j:=W_{j-1}|I_j|.
\]

The pressure-free first-hitting gate already proved

\[
1-q^{-1}
\lesssim
\mathfrak H_j+\sqrt{\Theta_j\mathfrak Z_j},
\]

where

\[
\mathfrak H_j
:=W_{j-1}\int_{C_j}h_1(t)\,dt,
\]

with

\[
\boxed{
h_1(t)
:=\frac{r(t)\|\nabla\omega(t)\|_\infty}{W(t)}
=\frac{r(t)^3}{\nu}\|\nabla\omega(t)\|_\infty.
}
\]

The present note addresses the derivative-active branch

\[
\boxed{\mathfrak H_j\ge c_q>0.}
\]

## 2. A finite spatial persistence inequality at each time

Fix a smooth pre-singular time and write

\[
G:=\|\nabla\omega\|_\infty,
\qquad
H:=\|\nabla^2\omega\|_\infty.
\]

Choose a point where `|nabla omega|` is arbitrarily close to `G`. If `H>0`, the Hessian bound makes `nabla omega` Lipschitz, so on a ball of radius comparable to

\[
\rho\sim \frac{G}{H}
\]

one has

\[
|\nabla\omega|\gtrsim G.
\]

Consequently

\[
\|\nabla\omega\|_2^2
\gtrsim
G^2\rho^3
\gtrsim
\frac{G^5}{H^3}.
\]

The degenerate case `H=0<G` is incompatible with finite `L^2` palinstrophy on the whole space; the inequality is understood by the limiting argument.

Define the scale-normalized second-vorticity derivative

\[
\boxed{
h_2(t)
:=\frac{r(t)^2\|\nabla^2\omega(t)\|_\infty}{W(t)}
=\frac{r(t)^4}{\nu}\|\nabla^2\omega(t)\|_\infty,
}
\]

and normalized palinstrophy

\[
\boxed{
P_r(t)
:=\frac{r(t)^3}{\nu^2}\|\nabla\omega(t)\|_2^2.
}
\]

Since

\[
G=\frac{\nu}{r^3}h_1,
\qquad
H=\frac{\nu}{r^4}h_2,
\]

the spatial persistence estimate becomes

\[
\boxed{
P_r(t)
\gtrsim
\frac{h_1(t)^5}{h_2(t)^3}.
}
\]

Equivalently,

\[
\boxed{
h_1(t)
\lesssim
P_r(t)^{1/5}h_2(t)^{3/5}.
}
\]

Status: **PROVED as an elementary finite-time spatial persistence inequality.**

## 3. Integrating the formed channels over a first-hitting epoch

Use the normalized time measure

\[
d\mu_j:=W_{j-1}\,dt
\]

on `C_j`. Its total mass is at most `Theta_j`.

Define

\[
\boxed{
\mathfrak P_j
:=W_{j-1}\int_{C_j}P_r(t)\,dt,
}
\]

and

\[
\boxed{
\mathfrak K_j
:=W_{j-1}\int_{C_j}h_2(t)\,dt.
}
\]

Hölder with exponents `5`, `5/3`, and `5` gives

\[
\begin{aligned}
\mathfrak H_j
&\lesssim
\int_{C_j}P_r^{1/5}h_2^{3/5}\,d\mu_j\\
&\le
\mathfrak P_j^{1/5}
\mathfrak K_j^{3/5}
\mu_j(C_j)^{1/5}\\
&\le
\Theta_j^{1/5}
\mathfrak P_j^{1/5}
\mathfrak K_j^{3/5}.
\end{aligned}
\]

Therefore every derivative-active epoch obeys the exact finite-channel product lower bound

\[
\boxed{
\Theta_j\,\mathfrak P_j\,\mathfrak K_j^3
\gtrsim_q 1.
}
\]

Status: **PROVED.**

This is the main new gate of the note.

## 4. Two quantitative descendants

For any fixed `K_*>0`, if

\[
\mathfrak K_j\le K_*,
\]

then

\[
\boxed{
\mathfrak P_j
\gtrsim_q
\frac{1}{\Theta_j K_*^3}.
}
\]

Conversely, for any fixed `P_*>0`, if

\[
\mathfrak P_j\le P_*,
\]

then

\[
\boxed{
\mathfrak K_j
\gtrsim_q
\left(\frac{1}{\Theta_j P_*}\right)^{1/3}.
}
\]

Thus the time-integrated first-derivative survivor has no third option:

\[
\boxed{
\text{time-integrated }\nabla\omega\text{ occupancy}
\Longrightarrow
\text{palinstrophy-time occupancy}
\ \lor\ 
\text{second-vorticity-derivative time occupancy},
}
\]

with the tradeoff controlled explicitly by the normalized epoch duration `Theta_j`.

## 5. Physical meaning of the palinstrophy channel

On the contact set,

\[
W_{j-1}\le W(t)\le qW_{j-1},
\]

hence

\[
r(t)\asymp_q r_{j-1}.
\]

Therefore

\[
\mathfrak P_j
\asymp_q
\frac{r_{j-1}}{\nu}
\int_{C_j}\|\nabla\omega(t)\|_2^2dt.
\]

Equivalently, the physical viscous-palinstrophy charge satisfies

\[
\boxed{
\nu\int_{C_j}\|\nabla\omega(t)\|_2^2dt
\asymp_q
\frac{\nu^2}{r_{j-1}}\mathfrak P_j.
}
\]

Hence a fixed order-one `mathfrak P_j` would cost order

\[
\frac{\nu^2}{r_{j-1}},
\]

which grows toward small scales.

However there is **no known finite global palinstrophy budget through a hypothetical singularity**. The enstrophy identity permits palinstrophy and stretching to diverge together. Therefore this growing physical cost is not itself a contradiction.

## 6. Interaction with the positive net-formation stages

The bounded-`Z` formation calculation proved that a positive density of first-hitting stages satisfies

\[
N_j\ge\eta>0,
\]

where

\[
N_j
=\frac{r_j}{\nu^2}
\int_{t_j}^{t_{j+1}}
\left[
\int\omega^TS\omega\,dx
-\nu\|\nabla\omega\|_2^2
\right]dt.
\]

On a stage which is simultaneously net-formation active and carries a palinstrophy charge, the stretching source must pay both the positive net increment and the palinstrophy destruction. Thus large `mathfrak P_j` does not close the branch; it raises the required stretching charge.

This is consistent with the previously proved critical middle-strain divergence and does not produce an independent finite budget.

## 7. DSD audit against the old derivative ladder

The new statement must not be interpreted as

\[
\mathfrak K_j>0
\Longrightarrow
\text{an infinite derivative object}.
\]

`mathfrak K_j` is a **finite second-vorticity-derivative spacetime channel**. If one subsequently descends it to higher derivative orders, each order must remain a separate finite witness, exactly as required by `DSD_FINITE_DERIVATIVE_WITNESS_LADDER_AUDIT_2026-08-25.md`.

Likewise, the palinstrophy branch is not merged with kinetic-energy dissipation. Palinstrophy is one derivative above the finite energy ledger and has no a-priori finite total budget near a hypothetical singularity.

The formed channel hierarchy is therefore

\[
\boxed{
\text{vorticity first hit}
\to
\text{near-derivative occupancy or enstrophy tax}
\to
\begin{cases}
\text{palinstrophy-time occupancy},\\
\text{finite }\nabla^2\omega\text{ time occupancy}
\end{cases}
}
\]

on the derivative-active side.

## 8. Relation to known geometric regularity routes

This note does **not** assume coherence of the vorticity direction, sparseness of intense-vorticity sets, or a regularity criterion as an extra hypothesis. Such geometric assumptions are known to deplete vortex stretching, but importing them here would make the proof conditional.

The present gate uses only smooth pre-singular Navier-Stokes fields, first-hitting normalization, elementary spatial persistence, and Hölder integration.

## 9. Remaining survivor after this descent

Combining the pressure-free first-hitting gate with the present result, every sufficiently late first-hitting epoch must be routed through finite formed channels:

\[
\boxed{
\text{first hit}
\Longrightarrow
\begin{cases}
\text{enstrophy-energy tax},\\
\text{palinstrophy-time occupancy},\\
\text{second-vorticity-derivative time occupancy}.
\end{cases}
}
\]

The first channel has a finite global energy ledger but only a geometrically summable minimum cost. The second has no finite total budget. The third can be continued only as a finite derivative-witness ladder and is not contradictory to analyticity by derivative order alone.

Thus the present calculation **closes the classification of the time-integrated first-derivative survivor, but not the singular branch**.

## 10. Audit verdict

### PROVED

- pointwise normalized interpolation `P_r >= c h_1^5/h_2^3`;
- time-integrated product gate `Theta_j mathfrak P_j mathfrak K_j^3 >= c_q` on every derivative-active first-hitting epoch;
- explicit palinstrophy-versus-second-derivative tradeoff;
- physical palinstrophy scaling `nu^2/r_j` for order-one normalized occupancy;
- finite-channel DSD interpretation.

### NOT DERIVED

- a finite global palinstrophy budget;
- a contradiction from `mathfrak K_j` without additional finite-order information;
- exclusion of the Critical Strain Temporal-Concentration Gate;
- contradiction to the bounded-`Z` singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
