# DSD Escaping Critical Tail — Kinetic-Energy Saturation Audit

Date: 2026-08-25

Status: **PHYSICAL FINITE-ENERGY BUDGET IS EXACTLY SCALE-COMPATIBLE WITH A 1/R ESCAPING SIMILARITY TAIL / NO KINETIC-ENERGY CONTRADICTION / FALSE CLOSURE ROUTE PRUNED / GLOBAL REGULARITY UNPROVED.**

## 1. Why this audit is necessary

The compensated-turnover analysis reduces the only genuine global spatial topology to repeated material/radial export which never returns and drifts to similarity infinity.

A tempting next step is to argue that a persistent critical velocity tail

\[
|U(Y)|\sim |Y|^{-1}
\]

must eventually exceed the finite physical kinetic energy.

That argument is false at the critical scaling. The exponents match exactly.

## 2. Dynamic first-hitting velocity scaling

Use

\[
r_j=\sqrt{\frac\nu{W_j}},
\qquad
W_j=q^jW_0,
\]

and define the dimensionless dynamic velocity by

\[
\boxed{
U_j(y)
:=
\frac{u(X_j+r_jy,t_j)}{r_jW_j}
=
\frac{u(X_j+r_jy,t_j)}{\sqrt{\nu W_j}}.
}
\]

Since

\[
dy=r_j^{-3}dx
=\left(\frac{W_j}{\nu}\right)^{3/2}dx,
\]

we obtain the exact normalized kinetic-energy scaling

\[
\begin{aligned}
\|U_j\|_2^2
&=
\frac1{\nu W_j}
\left(\frac{W_j}{\nu}\right)^{3/2}
\|u(t_j)\|_2^2\\
&=
\boxed{
\frac{W_j^{1/2}}{\nu^{5/2}}
\|u(t_j)\|_2^2.
}
\end{aligned}
\]

Physical kinetic energy is nonincreasing, so if

\[
E_0:=\|u_0\|_2^2,
\]

then

\[
\boxed{
\|U_j\|_2^2
\le
\frac{E_0}{\nu^{5/2}}W_j^{1/2}.
}
\]

Thus the total normalized kinetic-energy budget itself grows like `sqrt(W_j)`.

## 3. Historical outer radius has the same exponent

Fix any sufficiently late base stage `j_0`. Its physical natural radius is

\[
r_{j_0}=\sqrt{\frac\nu{W_{j_0}}}.
\]

Viewed in stage-`j` coordinates, that same fixed physical radius has normalized size

\[
\boxed{
R_{hist}(j;j_0)
:=
\frac{r_{j_0}}{r_j}
=
\sqrt{\frac{W_j}{W_{j_0}}}.
}
\]

Therefore

\[
\boxed{
R_{hist}(j;j_0)\asymp W_j^{1/2}.
}
\]

The maximum historical age available between `j_0` and `j` thus reaches exactly the same square-root scale as the global normalized kinetic-energy budget.

## 4. Kinetic energy of a critical 1/R tail

Suppose a nontrivial angular fraction of the tail obeys the critical scaling

\[
|U(Y)|\asymp\frac c{|Y|}
\]

for

\[
R_0\lesssim|Y|\lesssim R_{hist}.
\]

Then its kinetic energy scales as

\[
\begin{aligned}
K_{tail}
&\asymp
\int_{R_0}^{R_{hist}}
\frac{c^2}{R^2}R^2dR\\
&\asymp
c^2(R_{hist}-R_0).
\end{aligned}
\]

Hence

\[
\boxed{
K_{tail}\asymp C_{tail}R_{hist}
\asymp
C_{tail}\frac{W_j^{1/2}}{W_{j_0}^{1/2}}.
}
\]

Equivalently, in the geometric shell ladder, each critical shell has kinetic-energy size `~R_k`, and the geometric sum is dominated by the oldest/largest shell:

\[
\sum_{k=0}^{j-j_0}R_k
\asymp R_{j-j_0}
\asymp R_{hist}.
\]

## 5. Compare with the available total energy

The tail requirement and total normalized budget have identical `W_j^(1/2)` growth:

\[
K_{tail}
\sim
C_{tail}W_j^{1/2}W_{j_0}^{-1/2},
\]

while

\[
K_j
\le
E_0\nu^{-5/2}W_j^{1/2}.
\]

Their ratio is stage-independent:

\[
\boxed{
\frac{K_{tail}}{K_j^{ceiling}}
\asymp
\frac{C_{tail}\nu^{5/2}}
{E_0W_{j_0}^{1/2}}.
}
\]

Moreover, by restarting the audited historical ladder at a later first-hitting level `j_0`, the right-hand side decreases like `W_{j_0}^{-1/2}`.

Therefore finite kinetic energy cannot produce a universal contradiction with the escaping critical tail.

Status: **CRITICAL COMPATIBILITY PROVED AT THE SCALING LEVEL.**

## 6. Physical-space interpretation

The normalized historical outer radius corresponds to

\[
r_jR_{hist}(j;j_0)
=r_{j_0}.
\]

Thus similarity-space escape to

\[
R_{hist}\to\infty
\]

does **not** mean that material must travel to physical spatial infinity.

It can remain inside the fixed physical neighborhood

\[
|x-X_*|\lesssim r_{j_0}
\]

while that neighborhood expands without bound in the shrinking stage-`j` similarity coordinates.

This is why ordinary far-field decay of the original Clay-class initial data does not automatically remove the similarity critical tail.

## 7. Relation to finite enstrophy

The same critical profile has

\[
|\Omega|\sim R^{-2}.
\]

Its normalized enstrophy tail satisfies

\[
\int_R^{\infty}R^{-4}R^2dR
\sim R^{-1},
\]

so it is globally summable.

Hence the pair

\[
\boxed{
U\sim R^{-1},
\qquad
\Omega\sim R^{-2}
}
\]

is simultaneously compatible with

1. finite normalized enstrophy;
2. non-`L^3` velocity;
3. linearly growing normalized kinetic energy up to the historical cutoff;
4. finite physical kinetic energy at every pre-singular time.

This is the exact critical survivor already isolated by the repository.

## 8. Audit consequence

The route

\[
\text{permanent export}
\Longrightarrow
\text{too much kinetic energy}
\Longrightarrow
\text{contradiction}
\]

is invalid without an additional gain beyond critical `1/R` scaling.

A successful energy-style closure would require at least one of:

\[
|U|=o(R^{-1}),
\]

or a growing multiplicity/coherence coefficient forcing supercritical shell energy,

or a cancellation/invariant that removes the leading `1/R` critical component.

None of these is currently proved for the final escaping-tail branch.

## 9. Updated global frontier

The compensated local turnover analysis has removed cheap local escape mechanisms, but the permanently exported tail remains exactly energy-critical.

Thus the remaining global target should not be “use finite kinetic energy again.” It should be one of:

1. prove extra decay/cancellation of the exported critical tail;
2. prove that repeated export necessarily increases the critical-tail coefficient rather than merely extending its outer cutoff;
3. obtain a Liouville/rigidity theorem for the exact ancient core-plus-critical-tail class;
4. prove historical return/recycling rather than one-way frozen export.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]