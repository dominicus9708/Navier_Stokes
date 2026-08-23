# Recurrent Maximum Stretching -> Positive-Middle / Betchov Routing — 2026-08-24

Status: **RECURRENT SOURCE-ACTIVE BRANCH REDUCTION / GLOBAL REGULARITY NOT PROVED.**

This note combines

- `LERAY_RECURRENT_MAXIMUM_STRETCHING_FLOOR_2026-08-24.md`, and
- `notes/2026-08-18-source-active-betchov-dichotomy-without-alignment.md`.

The aim is to remove strongest-eigenvector alignment as an independent quiet recurrent escape.

## 1. Recurrent maximum-stretching floor

For Leray vorticity

\[
W_s+W+\frac12Y\cdot\nabla W+V\cdot\nabla W
=SW+\nu\Delta W,
\]

set

\[
M(s)=\|W(s)\|_\infty
\]

and

\[
G(s)=
\sup_{Y\in\operatorname{Argmax}|W|}
\left[
\xi^TS\xi-\nu|\nabla\xi|^2
\right].
\]

A nonzero periodic orbit, and more generally a nonzero genuine recurrent-return orbit, satisfies

\[
\boxed{
\liminf_{T\to\infty}
\frac1T\int_0^T G(s)ds
\ge1.
}
\]

Assume the analytic pure corridor has a finite strain ceiling

\[
G(s)\le B_+.
\]

Then for every `0<g0<1`, the high-source set

\[
E_{g0}=\{s:G(s)>g_0\}
\]

has positive lower time density

\[
\boxed{
\underline d(E_{g0})
\ge
\frac{1-g_0}{B_+-g_0}
}
\]

in the periodic case, with the corresponding liminf version along recurrent returns.

## 2. Turn maximum effective stretching into a source-active cell

At `s in E_g0`, choose a maximum-vorticity point `Y_s`. Then

\[
\gamma(Y_s,s)
:=\xi^TS\xi
>g_0,
\]

because the direction-diffusion penalty is nonnegative.

Hence the pointwise vortex-stretching density satisfies

\[
q(Y_s,s)
:=W^TSW
=M(s)^2\gamma(Y_s,s)
>M(s)^2g_0.
\]

On a nonzero periodic orbit,

\[
0<m_-\le M(s)\le m_+.
\]

On a nonzero recurrent return set the same positive lower bound holds after restricting to a sufficiently small neighborhood of the recurrent nonzero state.

Therefore

\[
q(Y_s,s)\ge m_-^2g_0.
\]

Uniform local smoothness and bounded no-`T` similarity-center motion give a radius `r_q>0`, independent of the repeated high-source event, such that on a fixed fraction of the natural cell around `Y_s`,

\[
\boxed{
q(Y,s)\ge q_0:=\frac12m_-^2g_0>0.
}
\]

Failure of such a uniform source-active neighborhood is itself derivative/localization loss and leaves the pure recurrent lane.

## 3. Apply the existing source-active Betchov dichotomy

The repository already proved the pointwise identity/routing

\[
q>0
\Longrightarrow
\left[
\lambda_2^+>0
\right]
\quad\lor\quad
\left[
q+4\det S\ge q>0
\right].
\]

Consider the fixed source-active portion of the cell with `q>=q0`.

Either at least a fixed fraction of it belongs to

\[
\boxed{\lambda_2>0,}
\]

which is a positive-middle source-active population, or at least a fixed fraction belongs to

\[
\lambda_2\le0
\]

and carries the fixed positive Betchov mismatch

\[
\boxed{q+4\det S\ge q_0.}
\]

The existing localized Betchov-buffer estimate routes the latter to

\[
\boxed{
\text{buffer strain-energy reservoir}
\lor
\text{buffer Hessian/palinstrophy}
\lor
\text{cubic residual/shape breakdown}.
}
\]

These are already typed `T/H/residual` exits.

## 4. Recurrent pure-lane consequence

On a recurrent corridor that excludes persistent buffer/Hessian/residual payments, the high-source set must therefore contain positive-middle source-active cells with positive time density.

Symbolically,

\[
\boxed{
\text{nonzero recurrent pure Leray core}
\Longrightarrow
\text{positive-density positive-middle source action}
\lor
T/H/\text{Betchov residual}.
}
\]

Thus strongest-eigenvector alignment with `lambda_2<=0` is not a fourth quiet recurrent geometry. Repeated use of that alignment produces a fixed local Betchov mismatch which must be exported through the buffer/derivative ledger.

## 5. Connection to transverse ribbon/projective closure

On the first branch the recurrent high-vorticity cell is simultaneously

1. source active (`q>=q0`);
2. thick by analytic/max-vorticity persistence;
3. positive-middle on a fixed cell fraction.

This is exactly the geometry underlying the existing transverse-ribbon/projective-action route.

Hence the recurrent endgame can reuse, rather than duplicate,

\[
\text{positive-middle stretching}
\to
\text{ribbonization / material turnover / projective eigenframe action}
\to
\text{frequency tax / H1 ledger}.
\]

The remaining quantitative issue is to compare the positive **time density** supplied here with the per-stage/action thresholds in the finite-stage anti-ribbon closure.

## 6. Significance

The recurrent maximum-stretching identity originally left two pointwise possibilities:

\[
\text{positive middle}
\quad\lor\quad
\text{strongest-axis alignment}.
\]

After the source-active Betchov routing, the second possibility is no longer independent:

\[
\boxed{
\text{strongest-axis alignment with nonpositive middle}
\to
\text{local Betchov mismatch}
\to
T/H/\text{buffer residual}.
}
\]

Therefore every residual-quiet recurrent core is forced back into the positive-middle geometry on a positive-density set of Leray times.

Status: **A NONZERO RECURRENT PURE CORE MUST ENTER THE POSITIVE-MIDDLE SOURCE-ACTIVE GEOMETRY AT POSITIVE TIME DENSITY. REPEATED NONPOSITIVE-MIDDLE EXTENSIONAL ALIGNMENT IS NOT FREE; IT PAYS THE ALREADY DERIVED LOCAL BETCHOV BUFFER/HESSIAN/RESIDUAL TAX. GLOBAL REGULARITY REMAINS UNPROVED.**