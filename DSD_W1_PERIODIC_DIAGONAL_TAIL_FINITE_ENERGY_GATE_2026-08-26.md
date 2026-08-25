# DSD W1 Periodic Tail: Diagonal Inheritance and Finite-Energy Gate

Date: 2026-08-26

Status: **DIRECT FINITE-ENERGY CONTRADICTION REJECTED / A STRONG DIAGONAL-INHERITANCE STATEMENT WOULD CLOSE THE PERIODIC TAIL, BUT THE ALL-AGE CHARACTERISTIC CALCULATION SHOWS THAT FIXED PHYSICAL RADII TRACE BACK TO FIXED ABSOLUTE LERAY TIMES RATHER THAN TO THE LATE PERIODIC OMEGA-LIMIT / THE FORMER SIMPLE TWO-STEP INHERITANCE ROUTE IS WITHDRAWN / GLOBAL REGULARITY UNPROVED.**

## 1. The tempting finite-energy argument

The periodic W1 omega-limit orbit has a nonzero canonical critical trace

\[
t_*(x)
=|x-X_*|^{-1}\Phi(\widehat{x-X_*},\log|x-X_*|).
\]

A nonzero discretely homogeneous degree-`-1` field is locally `L2` near the origin but not globally `L2` at infinity.  If one canonical annular cell carries

\[
E_*:=\int_{1<|x|<\lambda}|t_*|^2dx>0,
\]

then

\[
\int_{\lambda^k<|x|<\lambda^{k+1}}|t_*|^2dx
=\lambda^kE_*.
\]

Hence

\[
\boxed{t_*\notin L^2(\mathbb R^3)}.
\]

The original smooth physical solution has finite kinetic energy before the candidate singular time.  This makes a direct contradiction look possible.

## 2. Why the omega-limit trace is not automatically a physical final trace

The periodic object `U_per` is an omega-limit ancient orbit obtained from time shifts of the original Leray trajectory,

\[
U_{orig}(s_n+\cdot)\to U_{per}(\cdot),
\]

in the W1 compact topology: smoothly on bounded Leray sets and globally in the fixed `Lp`, `p>3`, topology.

A fixed nonzero physical point at time `s_n` corresponds instead to

\[
Y_n
=\frac{x-X_*}{\sqrt{T^*-t_n}}
\asymp e^{s_n/2},
\]

which moves to spatial infinity at the same time as `s_n->infinity`.

Thus fixed-Leray-radius omega-limit convergence does not control the required diagonal.

Global `Lp`, `p>3`, convergence also does not solve this: a critical `1/R` shell has

\[
\int_{A_R}|U|^p\sim R^{3-p}\to0
\]

while its inverse-scaled physical `L2` contribution on an appropriate annulus can remain critical.  The `p>3` topology therefore loses precisely the endpoint memory relevant to this question.

## 3. The finite-energy diagonal

Let

\[
\tau_n=T^*-t_n=e^{-s_n}
\]

and fix a physical annulus

\[
A^{phys}_{a,b}
=\{a<|x-X_*|<b\}.
\]

Its Leray image is

\[
A^{Leray}_n
=\{a\tau_n^{-1/2}<|Y|<b\tau_n^{-1/2}\},
\]

so its characteristic radius satisfies

\[
\boxed{R_n\asymp e^{s_n/2}.}
\]

This simultaneous `s_n->infinity`, `R_n->infinity` regime is the finite-energy diagonal.

## 4. A sufficiently strong diagonal inheritance theorem would close the periodic trace

If, along a blow-up sequence, one could prove for every fixed physical annulus that

\[
\boxed{
\|u(t_n)-t_*\|_{L^2(A^{phys}_{a,b})}\to0,
}
\]

then the physical energy inequality would imply

\[
\int_{a<|x-X_*|<b}|t_*|^2dx\le E_0
\]

for every `0<a<b<infinity`.  Sending `a downarrow0` and `b upward infinity` would give

\[
\|t_*\|_2^2\le E_0,
\]

contradicting the nonzero degree-`-1` DSS energy scaling.

Thus the purely conditional implication remains true:

\[
\boxed{
\text{global fixed-physical-radius diagonal inheritance}
\Longrightarrow
\text{no nonzero periodic W1 trace}.
}
\]

The issue is whether such inheritance is compatible with the actual all-age transport geometry.

## 5. Exact all-age characteristic calculation

The repository has the all-age co-moving estimate, schematically,

\[
\|W_R(h)-W_R(0)\|_{H^{-1}}
\le CR^{-2}
\qquad\forall h\ge0,
\]

and by autonomy it may be started at a late base time `s_b`:

\[
W_{R,s_b}(h,z)
=e^{h/2}R\,
U_{orig}(e^{h/2}Rz,s_b+h).
\]

At final Leray time `s_n`, a fixed physical radius `r` corresponds to

\[
R_n=e^{s_n/2}r.
\]

To pull this shell back to one fixed normalized base radius `R_0`, one must choose age

\[
\boxed{
h_n=2\log(R_n/R_0)
=s_n+2\log(r/R_0).}
\]

Therefore the corresponding base time is

\[
\boxed{
s_b=s_n-h_n
=2\log(R_0/r),}
\]

which is **independent of `n`**.

This is the key ancestry identity.

## 6. Consequence: fixed physical radii do not trace back to the late omega-limit phase

For fixed `r` and fixed `R0`, the all-age characteristic does not pull the diagonal shell back to a state whose Leray time tends to infinity.  It pulls it back to one fixed absolute time

\[
s_b=2\log(R_0/r).
\]

Hence the earlier proposed argument

\[
\text{pull to fixed }R_0
\quad+\quad
\text{use }U_{orig}(s_n)\to U_{per}
\]

mixes incompatible base times and is withdrawn.

The correct structural statement is

\[
\boxed{
\text{fixed physical final radius}
\longleftrightarrow
\text{its own earlier actual-orbit shell ancestry},
}
\]

not automatically the late periodic omega-limit phase.

## 7. Why allowing the base radius to vary does not immediately repair the argument

One could try to make the base time late by taking

\[
R_0=R_0(n)\to\infty.
\]

Indeed

\[
s_b(n)=2\log(R_0(n)/r)\to\infty.
\]

But then the base shell itself moves to infinity.  Fixed-radius omega-limit compactness no longer applies there.

Thus one faces the same diagonal problem in a different form:

\[
\boxed{
R_0(n)\to\infty
\quad\text{and}\quad
s_b(n)\to\infty.
}
\]

No existing W1 convergence theorem identifies such a moving base shell with the periodic canonical phase.

## 8. Physical meaning of the periodic omega-limit tail

The periodic omega-limit tail should therefore not be interpreted as a globally established final physical field on all fixed radii.

Its rigorous meaning is a critical intermediate-asymptotic structure in rescaled variables.  In physical variables, the region controlled directly by late omega-limit information shrinks toward the singular point as `t->T*`, unless an additional moving-shell inheritance theorem is proved.

This also explains why an infinite-energy ancient/DSS blow-up model can arise from a finite-energy physical solution: energy may be lost in the blow-up limit through the spatial scale sent to infinity in Leray coordinates.

## 9. Consistency with normalized finite energy

The physical energy relation is

\[
\|u(t)\|_2^2
=
\tau^{1/2}\|U_{orig}(s)\|_2^2.
\]

Thus finite physical energy permits normalized `L2` size as large as

\[
\|U_{orig}(s)\|_2^2
\lesssim E_0e^{s/2}.
\]

A critical `1/R` tail truncated at normalized radius `R\sim e^{s/2}` has exactly linear-in-R energy growth, of this admissible order.  Therefore the prelimit energy scaling itself is consistent with a growing critical conveyor over the normalized range available before the fixed physical scale is reached.

This is an anti-proof check: no hidden power mismatch appears.

## 10. What finite-energy route actually remains

A finite-energy contradiction would require a stronger theorem than ordinary omega-limit compactness.  Examples of sufficient, but presently unproved, statements include:

1. a moving-shell convergence theorem on `R_n~e^{s_n/2}` to one nonzero DSS phase;
2. a genealogy theorem forcing the same nonzero critical coefficient across a family of physical radii whose total `L2` energy diverges;
3. a uniform prelimit lower bound placing more than the allowed `O(e^{s/2})` normalized energy into the critical tail;
4. a no-loss-at-Leray-infinity compactness theorem strong enough to retain endpoint `L2` mass.

None is derived from the current W1 data.

## 11. Revised periodic closure target

The periodic branch retains the proved internal reduction

\[
\boxed{
P_{DSS}^{long}
\Longrightarrow
H_{2,crit}^{tail}
\lor
P_{ren}^{core}.
}
\]

The finite-energy route is now classified as a separate, stronger transfer problem:

\[
\boxed{
P_{DSS}^{long}
+
\text{moving-shell no-loss / genealogy theorem}
\Longrightarrow
\text{possible finite-energy contradiction}.
}
\]

It is **not** counted as a current closure lemma.

## 12. DSD audit

The argument explicitly distinguishes:

- original finite-energy physical solution;
- rescaled original orbit;
- periodic omega-limit ancient orbit;
- fixed normalized shell;
- fixed physical shell;
- moving Leray diagonal `R~e^{s/2}`;
- late omega-limit recurrence;
- fixed absolute-time shell ancestry;
- local blow-up-model validity versus global physical final-trace validity.

The corrected ancestry calculation removes an attractive but invalid shortcut.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
