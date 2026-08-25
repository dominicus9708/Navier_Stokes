# DSD W1 Endpoint D3 Critical-Serrin Audit

Date: 2026-08-26

Status: **ENDPOINT D3 IDENTIFIED AS A SCALE-CRITICAL PHYSICAL SPACETIME COST / FINITE D3 COST WOULD ENTER THE CLASSICAL VELOCITY SERRIN CLASS L_t^3 L_x^9 / W1 INVARIANT MEAN FORCES D3 COST TO DIVERGE ALONG THE GENERATING LERAY WINDOWS / THIS IS CONSISTENT WITH A SINGULAR SURVIVOR AND IS NOT A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the repaired endpoint routing

The preceding gauge-repair note proves, on the W1 invariant measure \(\mu\),

\[
\lim_{p\downarrow3}\langle\Pi_p\rangle_\mu
=
\frac{\mathscr R_3}{6}
+
\nu\langle D_3\rangle_\mu,
\]

with

\[
\mathscr R_3
=
\frac{M_{crit}}{\log2}>0
\]

and

\[
D_3(U)
=
\int_{\mathbb R^3}
|U||\nabla U|^2
+
|U|^{-1}\sum_j(U\cdot\partial_jU)^2
\,dY.
\]

It also gives

\[
\boxed{
\langle D_3\rangle_\mu>0.
}
\]

The question here is whether this positive endpoint dissipation already contradicts known regularity theory.

It does not.

## 2. The weighted gradient controls the critical velocity L9 norm

Set

\[
w=|U|^{3/2}.
\]

Then

\[
|\nabla w|^2
=
\frac94|U||\nabla|U||^2
\le
\frac94|U||\nabla U|^2
\le
\frac94D_3(U)
\]

at the integral level.

The homogeneous Sobolev inequality in three dimensions gives

\[
\|w\|_6^2
\le C_S\|\nabla w\|_2^2.
\]

But

\[
\|w\|_6^2
=
\left(\int|U|^9dY\right)^{1/3}
=
\|U\|_9^3.
\]

Therefore

\[
\boxed{
\|U\|_9^3
\le
C_9D_3(U).
}
\]

Thus integrability of \(D_3\) in time is stronger than the critical velocity Serrin condition \(L_s^3L_Y^9\) at the level of this direct estimate.

## 3. Physical/Leray scaling of D3

Let \(T\) be a candidate singular time and use the backward Leray variables

\[
s=-\log(T-t),
\qquad
Y=\frac{x-x_*}{\sqrt{T-t}},
\]

\[
u(x,t)
=
(T-t)^{-1/2}U(Y,s).
\]

For the physical endpoint weighted dissipation define

\[
\mathcal D_3^{phys}(t)
:=
\int
|u||\nabla u|^2
+
|u|^{-1}\sum_j(u\cdot\partial_ju)^2
\,dx.
\]

The scaling is

\[
|u|\sim(T-t)^{-1/2},
\qquad
|\nabla u|\sim(T-t)^{-1},
\qquad
dx=(T-t)^{3/2}dY.
\]

Hence

\[
\boxed{
\mathcal D_3^{phys}(t)
=
(T-t)^{-1}D_3(U(s)).
}
\]

Since

\[
dt=(T-t)ds,
\]

we obtain the exact scale-critical spacetime identity

\[
\boxed{
\int_{t_0}^{t_1}\mathcal D_3^{phys}(t)dt
=
\int_{s_0}^{s_1}D_3(U(s))ds.
}
\]

Therefore the D3 action is invariant under the Leray blow-up change of variables.

## 4. Relation to the classical velocity Serrin scale

The classical Prodi-Serrin velocity criterion uses mixed norms

\[
u\in L_t^qL_x^p,
\qquad
\frac2q+\frac3p=1,
\qquad
p>3.
\]

The pair

\[
(q,p)=(3,9)
\]

is critical because

\[
\frac23+\frac39=1.
\]

From Section 2 in physical variables,

\[
\|u(t)\|_9^3
\le
C_9\mathcal D_3^{phys}(t).
\]

Consequently

\[
\boxed{
\int_0^T\mathcal D_3^{phys}(t)dt<\infty
\quad\Longrightarrow\quad
u\in L_t^3L_x^9,
}
\]

and the classical Serrin regularity mechanism would exclude a singularity.

This is a consistency result with standard Navier-Stokes regularity theory, not a new criterion.

## 5. What a W1 singular survivor must therefore do

A genuine singular W1 survivor cannot have finite physical D3 action up to \(T\).

The repaired endpoint route already supplies a stronger dynamical statement on the invariant limiting object:

\[
\boxed{
\langle D_3\rangle_\mu=d_*>0.
}
\]

The invariant measure \(\mu\) was constructed from long Leray-time empirical measures. Because the endpoint D3 observable has a summable old-shell tail and uniform compact-core domination, it is continuous/uniformly integrable along the audited W1 compact class strongly enough for the empirical-measure passage used in the endpoint note.

Hence along the empirical sequence \(S_n\to\infty\) generating \(\mu\),

\[
\boxed{
\frac1{S_n}
\int_{s_0}^{s_0+S_n}D_3(U(s))ds
\to d_*>0.
}
\]

Therefore

\[
\boxed{
\int_{s_0}^{s_0+S_n}D_3(U(s))ds
=d_*S_n+o(S_n).
}
\]

Returning to physical time,

\[
S_n
=
\log\frac{T-t_0}{T-t_n},
\]

so the critical physical D3 cost satisfies along the same sequence

\[
\boxed{
\int_{t_0}^{t_n}\mathcal D_3^{phys}(t)dt
=
d_*
\log\frac{T-t_0}{T-t_n}
+o\!\left(\log\frac1{T-t_n}\right).
}
\]

Thus W1 predicts a logarithmically divergent scale-critical weighted-gradient action.

## 6. Why this is not yet a contradiction

The standard energy inequality controls

\[
\int_0^T\|\nabla u(t)\|_2^2dt,
\]

not

\[
\int_0^T\int|u||\nabla u|^2dxdt.
\]

The latter is a stronger scale-critical quantity.

Therefore the ordinary energy budget does not force the D3 action to be finite.

Likewise, the classical Serrin criterion says that finite \(L_t^3L_x^9\) control is regularizing; it does not say that every Leray-Hopf solution automatically has that finite norm.

Accordingly,

\[
\boxed{
\langle D_3\rangle_\mu>0
}
\]

is compatible with the singular-survivor hypothesis.

Attempting to close W1 merely by saying "positive dissipation cannot recur" would therefore be invalid.

## 7. DSD audit consequence

The endpoint branch now has the following audited interpretation:

\[
M_{crit}>0
\Longrightarrow
\mathscr R_3>0
\Longrightarrow
\langle D_3\rangle_\mu>0
\Longrightarrow
\text{persistent scale-critical D3 expenditure}.
\]

But this expenditure is replenished in the local endpoint ledger by the similarity-radial critical conveyor.

Hence the remaining problem is not to prove that dissipation is positive; that is already forced.

The remaining problem is to prove that the W1 radial replenishment mechanism cannot sustain this positive critical expenditure indefinitely while retaining all of

1. compact recurrent Leray dynamics;
2. the fixed positive critical shell mass \(M_{crit}\);
3. the old-shell Type-I/H1 ceilings;
4. avoidance of the already catalogued H/turnover/export escape channels.

## 8. New closure gate

A sufficient W1 closure would follow from any estimate forcing

\[
\boxed{
\frac1S\int_{s_0}^{s_0+S}D_3(U(s))ds\to0
}
\]

on the compact recurrent W1 class, because the invariant endpoint audit gives the opposite strict lower value \(d_*>0\).

Equivalently, it would suffice to prove a sublinear cumulative bound

\[
\boxed{
\int_{s_0}^{s_0+S}D_3(U(s))ds=o(S).
}
\]

from the previously established projective/turnover/export ledgers.

This is now a precise dynamic target.

It is not supplied by the ordinary energy inequality and therefore needs a genuinely new W1 rigidity input.

## 9. Relation to the repository's earlier Serrin baseline

The repository already contains a separate baseline recovering the critical **vorticity** Serrin relation from the off-axis projective source estimate.

The present note concerns a different object:

\[
D_3
\sim
\int |U||\nabla U|^2,
\]

which controls the critical **velocity** pair \((q,p)=(3,9)\).

The two routes should not be conflated.

Their agreement with standard critical scaling is useful as an external consistency check, but neither route alone closes global regularity.

## 10. Updated frontier

After the pressure-gauge repair and the critical-Serrin audit, the pure W1 survivor has been reduced to the quantitative compatibility problem

\[
\boxed{
\begin{gathered}
M_{crit}>0,
\qquad
\langle D_3\rangle_\mu=d_*>0,
\\
\text{compact recurrent Leray dynamics},
\\
\text{critical radial replenishment of a persistent D3 cost}.
\end{gathered}
}
\]

The next proof attempt should target a **sublinear-D3 theorem** or an equivalent statement that positive-density D3 expenditure necessarily activates one of the already excluded turnover/export/projective channels.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
