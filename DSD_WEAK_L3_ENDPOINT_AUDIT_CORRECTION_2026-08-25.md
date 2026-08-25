# DSD Weak-L3 Endpoint Audit Correction

Date: 2026-08-25

Status: **CORRECTION / PREVIOUS BARKER-PRANGE-BASED WEAK-L3 EXCLUSION WITHDRAWN / UNIFORM WEAK-L3 CONVEYOR REOPENED / GLOBAL REGULARITY UNPROVED.**

## Correction

The earlier notes

- `DSD_BOUNDED_Z_WEAK_L3_ENDPOINT_EXCLUSION_GATE_2026-08-25.md`, and
- `DSD_COHERENT_PERMANENT_EXPORT_WEAK_L3_CLOSURE_2026-08-25.md`

contain an incorrect comparison with Barker--Prange.

The quantitative Type-I lower bound is logarithmic for the **cubic integral**

\[
\int_{B_R}|u(x,t)|^3dx,
\]

not logarithmic for the `L3` norm itself.

Thus the theorem gives, schematically,

\[
\int_{B_R}|u|^3\gtrsim_M \log\frac1{T^*-t},
\]

which corresponds to

\[
\|u\|_{L^3(B_R)}\gtrsim_M
\left(\log\frac1{T^*-t}\right)^{1/3}.
\]

On the other hand, uniform weak-L3 plus the bounded-Z-induced `L-infinity` ceiling gives

\[
\int_{B_R}|u|^3
\lesssim_{M,Z_+}
1+\log R.
\]

On the admissible Type-I radii, `log R` is comparable to `log(1/(T^*-t))` up to fixed constants.

Therefore the lower and upper estimates have the **same logarithmic cubic-mass order** and do not contradict one another.

## Consequence

The implication

\[
\text{bounded Z + uniform }L_t^\infty L_x^{3,\infty}
\Longrightarrow
\text{regularity}
\]

is withdrawn.

Likewise, the earlier statement that a coherent bounded-flux permanent-export conveyor is S-closed merely because it is uniformly weak-L3 is withdrawn.

The coherent-conveyor calculations that prove

\[
|U_{train}(Y,s)|\lesssim (1+|Y|)^{-1}
\]

and hence

\[
\sup_s\|U_{train}(s)\|_{L^{3,\infty}}<\infty
\]

remain valid. What fails is only the final step claiming that this weak-L3 bound itself excludes singularity.

## Corrected weak-critical frontier

Two branches must now be retained:

\[
\boxed{
W_1:
\sup_s\|U(s)\|_{L^{3,\infty}}<\infty,
}
\]

and

\[
\boxed{
W_2:
\|U(s_j)\|_{L^{3,\infty}}\to\infty.
}
\]

The new annular-H1/Campanato reductions address `W2` only.

In particular,

\[
W_2
\Longrightarrow
H_{1,crit}^{tail}
\Longrightarrow
\text{Campanato escalation}
\lor H_{2,crit}^{tail},
\]

and Campanato escalation is excluded on the bounded-Z Type-I center-nested corridor.

Thus

\[
\boxed{
W_2
\Longrightarrow
H_{2,crit}^{tail}
}
\]

up to already typed corridor failures.

However `W1` remains a genuine endpoint survivor.

## Updated global frontier

The current endgame is therefore

\[
\boxed{
\text{uniform weak-L3 critical conveyor }W_1
\quad\lor\quad
\text{remote derivative-subscale }H_{2,crit}^{tail}
}
\]

plus already typed H/T exits.

Neither of these two remaining branches is closed here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
