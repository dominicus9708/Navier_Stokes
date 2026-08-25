# DSD Remote Diffuse-Multiplicity Critical Countermodel

Date: 2026-08-25

Status: **STATIC SCALING COUNTERMODEL / SHOWS REMOTE H2 ESCALATION NEED NOT YIELD ONE FIXED-CHARGE PACKET / DIFFUSE MULTIPLICITY IS A GENUINE SEPARATE FRONTIER / NOT AN EXACT NAVIER-STOKES SOLUTION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current residual branch after Campanato exclusion is

\[
\|U\|_{L^{3,\infty}}\uparrow
\Longrightarrow
E_1(R)\uparrow,
\qquad
\frac{\delta_R}{R}\downarrow0.
\]

A tempting next step would be to claim that large shell-averaged derivative activity must contain one finite local packet carrying a fixed scale-invariant derivative charge.

This note constructs a divergence-free static scaling model showing that this is false without additional dynamical/material information.

## 2. One fixed divergence-free bump

Choose a nonzero smooth compactly supported divergence-free vector field

\[
\phi\in C_c^\infty(B_1;\mathbb R^3),
\qquad
\nabla\cdot\phi=0.
\]

Normalize its fixed constants harmlessly.

For amplitude `a`, length `delta`, and center `Y_m`, define

\[
U_m(Y)
=
a\,\phi\!\left(\frac{Y-Y_m}{\delta}\right).
\]

Then

\[
\|U_m\|_2^2\asymp a^2\delta^3,
\]

\[
\|\nabla U_m\|_2^2\asymp a^2\delta,
\]

and

\[
\|\nabla^2U_m\|_2^2\asymp a^2\delta^{-1}.
\]

Also

\[
\|U_m\|_\infty\asymp a.
\]

## 3. Place many bumps in one remote shell

Fix a large shell radius `R` and choose a slowly growing parameter

\[
A=A(R)\to\infty.
\]

Set

\[
\boxed{
a_R=\frac{A}{R},
\qquad
\delta_R=\frac{R}{A^2},
\qquad
N_R=A^4.
}
\]

Place `N_R` mutually disjoint translated copies of the bump inside a fixed-thickness annulus

\[
A_R=\{R<|Y|<2R\}.
\]

The total occupied volume is

\[
N_R\delta_R^3
=A^4\frac{R^3}{A^6}
=
\boxed{\frac{R^3}{A^2}},
\]

which is a vanishing fraction `A^{-2}` of the shell volume, so packing is geometrically possible for large `A`.

Define

\[
U_R^{diff}=\sum_{m=1}^{N_R}U_m.
\]

Because supports are disjoint, all L2 derivative budgets add exactly up to fixed constants.

## 4. Relative Campanato stays critical and bounded

The total velocity L2 mass is

\[
\begin{aligned}
\|U_R^{diff}\|_2^2
&\asymp
N_R a_R^2\delta_R^3\\
&=
A^4\frac{A^2}{R^2}\frac{R^3}{A^6}\\
&=
\boxed{R}.
\end{aligned}
\]

Therefore the annular critical relative-energy scale is

\[
\boxed{
R^{-1}\|U_R^{diff}\|_2^2\asymp1.
}
\]

After subtracting the annular mean the same estimate holds, since the occupied fraction is `A^{-2}` and the mean is smaller order.

Thus

\[
\boxed{
\mathfrak C_A(R)\asymp1.
}
\]

There is no Campanato escalation.

## 5. Global enstrophy contribution tends to zero while critical H1 diverges

For one bump,

\[
\|\nabla U_m\|_2^2
\asymp
\frac{A^2}{R^2}\frac{R}{A^2}
=
R^{-1}.
\]

Summing `N_R=A^4` bumps gives

\[
\boxed{
\int_{A_R}|\nabla U_R^{diff}|^2
\asymp
\frac{A^4}{R}.
}
\]

Hence if

\[
A(R)=o(R^{1/4}),
\]

then the actual shell enstrophy tends to zero:

\[
\int_{A_R}|\nabla U|^2\to0.
\]

Nevertheless the scale-critical shell number is

\[
\boxed{
E_1(R)
=R\int_{A_R}|\nabla U|^2
\asymp A^4\to\infty.
}
\]

Thus bounded and even tight global enstrophy does not prevent critical-H1 escalation.

## 6. Actual second-derivative mass can also tend to zero while critical H2 diverges quadratically

For one bump,

\[
\|\nabla^2U_m\|_2^2
\asymp
\frac{a_R^2}{\delta_R}
=
\frac{A^4}{R^3}.
\]

Summing `A^4` bumps gives

\[
\boxed{
\int_{A_R}|\nabla^2U|^2
\asymp
\frac{A^8}{R^3}.
}
\]

If

\[
A(R)=o(R^{3/8}),
\]

this actual derivative L2 mass also tends to zero.

But the critical shell number is

\[
\boxed{
E_2(R)
=R^3\int_{A_R}|\nabla^2U|^2
\asymp A^8.
}
\]

Therefore

\[
\boxed{E_2(R)\asymp E_1(R)^2,}
\]

which exactly saturates the quadratic lower relation obtained after Campanato exclusion.

## 7. The weak-L3 norm nevertheless diverges

At level comparable to

\[
\lambda_R=a_R=A/R,
\]

the superlevel set has volume comparable to the occupied volume

\[
V_R\asymp R^3/A^2.
\]

Hence

\[
\lambda_R^3V_R
\asymp
\frac{A^3}{R^3}\frac{R^3}{A^2}
=
\boxed{A}.
\]

Thus

\[
\boxed{
\|U_R^{diff}\|_{L^{3,\infty}}^3
\gtrsim A(R)\to\infty.
}
\]

So the model simultaneously has

\[
\boxed{
\mathfrak C_A\asymp1,
\quad
\text{actual enstrophy tail}\to0,
\quad
E_1\to\infty,
\quad
E_2\sim E_1^2,
\quad
\|U\|_{3,\infty}\to\infty.
}
\]

## 8. No individual bump carries a fixed critical packet charge

The natural local critical velocity number of one bump is

\[
a_R\delta_R
=
\frac{A}{R}\frac{R}{A^2}
=
\boxed{A^{-1}\to0.}
\]

Likewise its scale-critical local H1 charge is

\[
\delta_R\int_{B_{\delta_R}}|\nabla U_m|^2
\asymp
\delta_R R^{-1}
=
\boxed{A^{-2}\to0.}
\]

And its local critical H2 charge is

\[
\delta_R^3
\int_{B_{\delta_R}}|\nabla^2U_m|^2
\asymp
\boxed{A^{-2}\to0.}
\]

Thus **every individual local packet becomes subcritical** even though the shell-level critical derivative numbers diverge.

The divergence is carried purely by multiplicity:

\[
N_R=A^4\to\infty.
\]

## 9. Compatibility with fixed-order analytic derivative ceilings

The pointwise m-th derivative of one bump scales as

\[
|\nabla^mU_m|
\asymp
\frac{a_R}{\delta_R^m}
=
\frac{A^{2m+1}}{R^{m+1}}.
\]

Choose, for example,

\[
\boxed{A(R)=\log(2+R).}
\]

Then for every fixed derivative order `m`,

\[
\frac{A(R)^{2m+1}}{R^{m+1}}\to0.
\]

Therefore this static diffuse-multiplicity model is compatible with **every fixed-order pointwise analyticity derivative ceiling** used in the first-hitting corridor.

Analyticity alone does not extract a fixed packet.

## 10. Passive-time scale

The bump scale is

\[
\delta_R=R/A^2.
\]

Its viscous time is

\[
\delta_R^2=R^2/A^4\to\infty
\]

for slowly growing `A`.

Its nonlinear turnover time is of order

\[
\frac{\delta_R}{a_R}
=\frac{R^2}{A^3}\to\infty.
\]

Thus on an `O(1)` Leray-time window these remote bumps can also be approximately passive; neither viscosity nor self-advection gives an automatic fixed short-time charge.

This does **not** prove that an exact Navier--Stokes trajectory can realize the model. It shows only that the presently available static and finite-window inequalities do not rule it out.

## 11. Consequence for the DSD tree

The proposed implication

\[
\delta_R/R\to0
\Longrightarrow
\text{one fixed-charge derivative packet}
\]

is false at the level of the current functional information.

The correct split is

\[
\boxed{
H_{2,crit}^{tail}
\Longrightarrow
H_{packet}
\lor
H_{diffuse-multi}.
}
\]

The new diffuse branch has the signature

\[
\boxed{
N_R\to\infty,
\qquad
\text{charge per cell}\to0,
\qquad
\text{total weak-critical mass}\uparrow.
}
\]

To close it one needs a genuinely dynamical/material theorem controlling the creation, persistence, merging, or genealogy of an increasing number of subcritical remote cells.

## 12. Audit verdict

### PROVED AS A STATIC SCALING COUNTERMODEL

- bounded Campanato and tight enstrophy are compatible with weak-L3 escalation;
- critical H1 and H2 can diverge while their unweighted tail masses tend to zero;
- every individual derivative cell can have vanishing critical charge;
- fixed-order analyticity does not prevent this if multiplicity increases.

### NOT CLAIMED

- the model is an exact Navier--Stokes solution;
- diffuse multiplicity can actually be generated by a smooth Clay-data solution;
- global regularity.

### NEW OPEN DYNAMIC TARGET

\[
\boxed{
H_{diffuse-multi}
\Longrightarrow
T_{creation/merger/genealogy}
\lor
H_{time-integrated}
}
\]

must be proved dynamically, not by snapshot interpolation alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
