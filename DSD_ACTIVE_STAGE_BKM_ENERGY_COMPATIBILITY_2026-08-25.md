# DSD active-stage BKM / energy compatibility audit

Date: 2026-08-25

Status: **FIXED BKM CHARGE PER ACTIVE STAGE PROVED / PARABOLIC-SCALE MINIMUM PERSISTENCE PROVED / REQUIRED ENERGY COST IS GEOMETRICALLY SUMMABLE / ENERGY-ONLY CLOSURE PRUNED AT CURRENT SCALING LEVEL / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_CRITICAL_STRAIN_SPECTRAL_CHARGE_GATE_2026-08-25.md`.

The question is whether the temporal concentration forced by the critical middle-strain charge can already be excluded by the ordinary kinetic-energy budget together with the first-hitting amplitude cap.

The answer at the present level is **no**: an active stage must persist for a parabolic-scale amount of time, but the corresponding mandatory kinetic-energy dissipation is proportional to `r_j`, and those costs are geometrically summable.

## 1. First-hitting notation

Let

\[
W(t):=\|\omega(t)\|_{\infty}.
\]

At first-hitting times,

\[
W(t_j)=W_j,
\qquad
W_{j+1}=QW_j,
\qquad
Q>1.
\]

Use

\[
r_j:=\left(\frac{\nu}{W_j}\right)^{1/2}.
\]

Then

\[
W_j=\frac{\nu}{r_j^2},
\qquad
r_{j+1}=Q^{-1/2}r_j.
\]

By the definition of the next first hit,

\[
\boxed{
W(t)\le W_{j+1}
\qquad
(t_j\le t\le t_{j+1}).
}
\]

## 2. Enstrophy growth controlled by the vorticity amplitude

Define

\[
Y(t):=\frac12\|\omega(t)\|_2^2.
\]

The whole-space enstrophy identity is

\[
Y'(t)+\nu\|\nabla\omega\|_2^2
=\int S:(\omega\otimes\omega)\,dx.
\]

By Holder,

\[
\left|\int S:(\omega\otimes\omega)dx\right|
\le
\|S\|_2\|\omega\|_4^2.
\]

For incompressible flow on `R^3`,

\[
\|S\|_2\le C\|\omega\|_2,
\]

and interpolation gives

\[
\|\omega\|_4^2
\le
\|\omega\|_2\|\omega\|_\infty.
\]

Hence, for a universal constant `C_0`,

\[
\boxed{
Y'(t)
\le
C_0 W(t)Y(t).
}
\]

Therefore

\[
\boxed{
\frac{Y(t_2)}{Y(t_1)}
\le
\exp\left(C_0\int_{t_1}^{t_2}W(t)dt\right).
}
\]

This is sufficient for the present audit; no endpoint `L^infinity -> L^infinity` estimate for the strain is used.

## 3. Active stage gives a fixed BKM charge

From the previous critical-strain note, every active stage satisfies

\[
\frac{Y(t_{j+1})}{Y(t_j)}
\ge
1+\delta_*,
\qquad
\delta_*:=\frac{2\eta}{Z_*}>0.
\]

Combining with Section 2,

\[
1+\delta_*
\le
\exp\left(C_0\int_{t_j}^{t_{j+1}}W(t)dt\right).
\]

Thus every active stage carries the fixed positive vorticity-amplitude time charge

\[
\boxed{
\int_{t_j}^{t_{j+1}}\|\omega(t)\|_\infty dt
\ge
\beta_*,
\qquad
\beta_*:=\frac1{C_0}\log(1+\delta_*)>0.
}
\]

Because active stages have positive asymptotic density, this already gives a generation-by-generation version of the Beale-Kato-Majda necessary divergence:

\[
\boxed{
\int^{T^*}\|\omega(t)\|_\infty dt=+\infty
}
\]

along the hypothetical bounded-Z singular branch.

Status: **PROVED.**

## 4. Minimum active-stage duration

On the first-hitting interval,

\[
W(t)\le W_{j+1}.
\]

Therefore the fixed BKM charge implies

\[
\beta_*
\le
W_{j+1}(t_{j+1}-t_j).
\]

Hence

\[
\boxed{
\Delta t_j:=t_{j+1}-t_j
\ge
\frac{\beta_*}{W_{j+1}}
=
\beta_*\frac{r_{j+1}^2}{\nu}
=
\frac{\beta_*}{Q}\frac{r_j^2}{\nu}.
}
\]

Thus an active stage cannot be arbitrarily shorter than its local parabolic time scale.

Status: **PROVED.**

## 5. Final crossing interval avoids a false lower-bound step

The enstrophy need not remain above `Y(t_j)` throughout the entire stage; it could first decrease and then increase.

To avoid assuming monotonicity, define `tau_j` to be the last time in `[t_j,t_{j+1}]` for which

\[
Y(\tau_j)=Y(t_j).
\]

Such a time exists by continuity because

\[
Y(t_{j+1})>Y(t_j)
\]

on an active stage.

By the definition of the last crossing,

\[
Y(t)\ge Y(t_j)
\qquad
(\tau_j\le t\le t_{j+1}).
\]

Applying the growth estimate from `tau_j` to `t_{j+1}` gives the same fixed charge:

\[
\int_{\tau_j}^{t_{j+1}}W(t)dt
\ge\beta_*.
\]

Hence

\[
\boxed{
t_{j+1}-\tau_j
\ge
\frac{\beta_*}{W_{j+1}}
=
\frac{\beta_*}{Q}\frac{r_j^2}{\nu}.
}
\]

This is the interval on which a legitimate lower energy-dissipation estimate can be made.

## 6. Mandatory kinetic-energy dissipation on an active stage

The bounded-Z analytic-core floor gives

\[
Z_j\ge z_a>0,
\]

so

\[
\|\omega(t_j)\|_2^2
\ge
z_a\frac{\nu^2}{r_j}.
\]

On the final crossing interval,

\[
\|\omega(t)\|_2^2
\ge
\|\omega(t_j)\|_2^2.
\]

Therefore the kinetic-energy dissipation spent on this final crossing satisfies

\[
\begin{aligned}
D_j^{cross}
&:=
\nu\int_{\tau_j}^{t_{j+1}}\|\omega(t)\|_2^2dt\\
&\ge
\nu\left(z_a\frac{\nu^2}{r_j}\right)
\left(\frac{\beta_*}{Q}\frac{r_j^2}{\nu}\right).
\end{aligned}
\]

Thus

\[
\boxed{
D_j^{cross}
\ge
\frac{\beta_*z_a}{Q}\nu^2r_j.
}
\]

Status: **PROVED.**

## 7. The mandatory energy costs are summable

The first-hitting radii are geometric:

\[
r_j=r_JQ^{-(j-J)/2}.
\]

Therefore

\[
\sum_{j=J}^{\infty}r_j
<\infty.
\]

Consequently the total **minimum energy cost forced by the estimates above** is only

\[
\sum_{j\in A}
\frac{\beta_*z_a}{Q}\nu^2r_j,
\]

where `A` is the active-stage set, and

\[
\boxed{
\sum_{j\in A}r_j
\le
\sum_{j=J}^{\infty}r_j
<\infty.
}
\]

Hence the lower bounds established here do not force the kinetic-energy dissipation to diverge.

This does **not** prove that the actual dissipation is finite on a singular branch. It proves only that the current mandatory per-stage lower costs are fully compatible with the finite kinetic-energy budget.

Status: **PROVED AS A SCALING-COMPATIBILITY AUDIT.**

## 8. DSD interpretation

The finite channel chain is now

\[
\boxed{
\text{active formation}
\to
\text{fixed multiplicative enstrophy growth}
\to
\text{fixed BKM charge}
\to
\text{parabolic persistence}
\to
O(\nu^2r_j)\text{ minimum kinetic-energy cost}.
}
\]

The last cost is a **lower-level dissipative channel**, but its geometric scaling is summable.

Thus DSD separates two facts that must not be conflated:

- the source/critical channels diverge generation by generation;
- the mandatory energy-level cost attached to each generation decays geometrically.

The latter does not neutralize the former.

## 9. Pruned branch

The following attempted closure is now pruned:

\[
\boxed{
\text{positive-density active stages}
\overset{\text{current estimates}}{\Longrightarrow}
\text{infinite kinetic-energy dissipation}
}
\]

because the strongest mandatory cost obtained from the active-stage jump plus the first-hitting amplitude cap is proportional to `r_j`, and

\[
\sum_jr_j<\infty.
\]

A successful energy-level closure would therefore require genuinely new information, for example a non-summable lower cost per generation, not merely the already-derived parabolic persistence.

## 10. Relation to the Critical Strain Temporal-Concentration Gate

The previous note identified the open gate

\[
\text{CSTCG: can the required temporal concentration of }\lambda_2^+\text{ be forbidden?}
\]

The present audit shows that ordinary kinetic energy plus the first-hitting `L^infinity` amplitude ceiling does **not** forbid it at the current scaling level.

Thus the remaining route must use structure beyond the scalar energy budget. Possible non-circular candidates are:

1. strain-eigenvalue geometry or alignment constraints;
2. a scale-critical spatial occupancy restriction not equivalent to the previously pruned derivative ladder;
3. a pressure/strain compatibility identity that suppresses positive-middle-eigenvalue concentration;
4. another genuinely finite invariant or monotone quantity at critical scaling.

These are candidate directions only; none is assumed or proved here.

## 11. Audit verdict

### PROVED

- every active stage carries a fixed positive `integral ||omega||_infinity dt` charge;
- every active stage has a minimum parabolic-scale duration;
- a monotonicity-free final-crossing interval carries the same minimum duration;
- the mandatory kinetic-energy dissipation on that crossing is `>= c nu^2 r_j`;
- these mandatory costs are geometrically summable.

### PRUNED / NOT SUFFICIENT

- closing the singular branch using only the present energy budget plus first-hitting persistence.

### NOT DERIVED

- CSTCG;
- a non-summable critical-to-energy conversion;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
