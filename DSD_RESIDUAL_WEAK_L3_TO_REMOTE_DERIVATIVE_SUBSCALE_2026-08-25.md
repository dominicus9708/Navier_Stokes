# DSD Residual Weak-L3 Escape -> Remote Derivative Subscale

Date: 2026-08-25

Status: **LAST WEAK-CRITICAL RESIDUAL REDUCED TO A REMOTE SUBSCALE DERIVATIVE H-BRANCH / EXISTING FINITE-WITNESS H LEMMAS DO NOT YET AUTOMATICALLY CLOSE THE REMOTE LIMIT / GLOBAL REGULARITY UNPROVED.**

## 1. Inputs

The current endgame now has two proved reductions.

First,

\[
\|U_j\|_{L^{3,\infty}}\to\infty
\Longrightarrow
H_{1,crit}^{tail},
\]

from `DSD_WEAK_L3_FROM_UNIFORM_ANNULAR_CRITICAL_H1_2026-08-25.md`.

Second,

\[
H_{1,crit}^{tail}
\Longrightarrow
\text{Campanato escalation}
\lor
H_{2,crit}^{tail},
\]

from `CRITICAL_H1_TAIL_TO_CAMPANATO_OR_H2_2026-08-24.md`.

The Campanato alternative is excluded on the bounded-Z Type-I center-nested corridor by

`DSD_BOUNDED_Z_TYPE_I_EXCLUDES_CAMPANATO_ESCALATION_2026-08-25.md`.

Hence the only residual branch is

\[
\boxed{
H_{2,crit}^{tail}.
}
\]

## 2. Shell quantities

On an enlarged annulus `A_R^*`, set

\[
C_R
:=
R^{-1}\int_{A_R^*}|U-(U)_{A_R^*}|^2dY,
\]

\[
E_1(R)
:=
R\int_{A_R^*}|\nabla U|^2dY,
\]

and

\[
E_2(R)
:=
R^3\int_{A_R^*}|\nabla^2U|^2dY.
\]

The fixed-annulus interpolation already proved in the repository is

\[
E_1(R)
\le
C\left[
C_R^{1/2}E_2(R)^{1/2}+C_R
\right].
\]

## 3. Campanato boundedness forces quadratic H2 escalation

On the present corridor there is a fixed bound

\[
C_R\le C_0.
\]

Suppose

\[
E_1(R_n)\to\infty.
\]

For all sufficiently large `n`, the additive `CC0` term is at most half of `E1`. Therefore

\[
E_1(R_n)
\le
2C C_0^{1/2}E_2(R_n)^{1/2}.
\]

Hence

\[
\boxed{
E_2(R_n)
\ge
c\frac{E_1(R_n)^2}{C_0}.
}
\]

Thus the H2 escalation is at least quadratic relative to the H1 escalation.

## 4. Derivative correlation length

Define shell first- and second-derivative masses

\[
Z_R
:=
\int_{A_R^*}|\nabla U|^2dY,
\qquad
Q_R
:=
\int_{A_R^*}|\nabla^2U|^2dY.
\]

Whenever `Q_R>0`, define the derivative correlation length

\[
\boxed{
\delta_R^2
:=
\frac{Z_R}{Q_R}.
}
\]

Since

\[
E_1=RZ_R,
\qquad
E_2=R^3Q_R,
\]

we have the exact identity

\[
\boxed{
\left(\frac{\delta_R}{R}\right)^2
=
\frac{E_1(R)}{E_2(R)}.
}
\]

Using the quadratic lower bound for `E2`,

\[
\boxed{
\left(\frac{\delta_{R_n}}{R_n}\right)^2
\le
C\frac{C_0}{E_1(R_n)}
\to0.
}
\]

Therefore

\[
\boxed{
\frac{\delta_{R_n}}{R_n}\to0.
}
\]

## 5. Interpretation

The final residual is not a scale-coherent `1/R` conveyor.

A scale-coherent critical shell has derivative length comparable to its radius:

\[
\delta_R\asymp R.
\]

The present survivor instead requires

\[
\delta_R\ll R.
\]

Thus a remote annulus at distance/scale `R` must contain velocity/vorticity variation on a much smaller internal scale.

This is a genuine two-scale object:

\[
\boxed{
\text{remote shell scale }R
\quad+\quad
\text{internal derivative scale }\delta_R=o(R).
}
\]

## 6. Relation to existing finite-witness H lemmas

The repository already contains finite-witness descent mechanisms such as

- `OCCUPANCY_FAILURE_FINITE_WITNESS_DERIVATIVE_DESCENT_2026-08-25.md`;
- `DSD_TIME_INTEGRATED_DERIVATIVE_OCCUPANCY_DESCENT_2026-08-25.md`.

Those results show that, near a formed finite core witness, rapid spatial derivative change routes to palinstrophy or a higher derivative needle.

However the present statement concerns annuli with

\[
R_n\to\infty
\]

and a subscale ratio

\[
\delta_{R_n}/R_n\to0.
\]

Therefore one must still prove a **remote packet extraction / occupancy lemma** before applying the finite-witness H descent.

It would be invalid to identify the two scopes without that extraction.

## 7. New exact frontier

The residual chain is now

\[
\boxed{
L^{3,\infty}\text{ escalation}
\Longrightarrow
E_1(R_n)\to\infty
\Longrightarrow
\delta_{R_n}/R_n\to0.
}
\]

Thus the next missing lemma can be stated narrowly as:

\[
\boxed{
\text{remote subscale extraction:}
\quad
\delta_R/R\ll1
\Longrightarrow
\text{finite derivative packet / occupancy H witness}
\lor
T_{multi/turnover}.
}
\]

If such a lemma is proved with a fixed normalized packet charge, the existing finite-witness H ledgers can take over.

## 8. Audit verdict

### PROVED

- residual weak-L3 escalation cannot stay scale-coherent;
- after Campanato exclusion, its critical H2 quantity grows at least quadratically relative to critical H1;
- the associated derivative correlation length satisfies `delta_R/R -> 0`.

### OPEN

- extracting from the shell-averaged scale separation a finite local packet with a stage-independent normalized charge;
- excluding the possibility that the derivative mass is spread over an increasing number of individually subcritical subscale cells;
- routing that diffuse-multiplicity alternative quantitatively to existing T/H ledgers;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
