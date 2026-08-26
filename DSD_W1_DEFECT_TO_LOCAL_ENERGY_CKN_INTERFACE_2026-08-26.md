# DSD W1 Defect-to-Local-Energy CKN Interface

Date: 2026-08-26

Status: **POSITIVE LOW-AMPLITUDE WEAK-L3 DEFECT IS SHOWN TO FORCE POSITIVE SCALE-INVARIANT LOCAL KINETIC-ENERGY DENSITY AT THE CANDIDATE SINGULAR POINT / UNIFORM NO-DEFECT IS THEREFORE RECOGNIZED AS A CKN-LEVEL ENDPOINT PROBLEM, NOT A SIMPLE COMPACTNESS LEMMA / GLOBAL REGULARITY UNPROVED.**

## 1. Weak-L3 defect

Let

\[
\mathscr C_{WL3}
=
\limsup_{\lambda\downarrow0}
\lambda^3N(\lambda),
\qquad
N(\lambda)=|\{|U|>\lambda\}|.
\]

On W1,

\[
\mathscr C_{WL3}=\mathscr R_3/3>0.
\]

## 2. Type-I tail localization

The W1 far-field envelope gives, for large `|Y|`,

\[
|U(Y)|\le A_0/|Y|.
\]

Hence the superlevel set `|U|>lambda` is contained in a ball of radius comparable to

\[
R_\lambda=A_0/\lambda.
\]

On that ball,

\[
\int_{B_{R_\lambda}}|U|^2dY
\ge
\lambda^2N(\lambda).
\]

Therefore

\[
\boxed{
\frac1{R_\lambda}
\int_{B_{R_\lambda}}|U|^2dY
\ge
\frac{\lambda^3N(\lambda)}{A_0}.
}
\]

Taking the low-amplitude limit gives

\[
\boxed{
\limsup_{R\to\infty}
\frac1R\int_{B_R}|U|^2dY
\ge
\frac{\mathscr C_{WL3}}{A_0}
=
\frac{\mathscr R_3}{3A_0}>0.
}
\]

## 3. Return to physical variables without a diagonal-limit error

Fix a large but finite normalized radius `R` first, and take a prelimit sequence `s_n->infinity` converging locally to the W1 state. Set

\[
\tau_n=T_*-t_n,
\qquad
r_n=R\sqrt{\tau_n}.
\]

The Leray scaling gives exactly

\[
\boxed{
\frac1{r_n}
\int_{B_{r_n}(X_*)}|u(x,t_n)|^2dx
=
\frac1R
\int_{B_R}|U(s_n,Y)|^2dY.
}
\]

Local convergence at fixed `R` then yields

\[
\frac1{r_n}
\int_{B_{r_n}(X_*)}|u(x,t_n)|^2dx
\to
\frac1R
\int_{B_R}|U_\infty(Y)|^2dY.
\]

Taking `R` large only after this fixed-radius transfer avoids the previous expanding-diagonal mistake.

Thus positive W1 defect forces a positive sequence of scale-invariant physical local-energy densities at radii `r_n downarrow0`.

## 4. CKN-level meaning

Classical partial regularity / epsilon-regularity mechanisms say that sufficiently small scale-invariant local energy/dissipation quantities imply regularity. Therefore a candidate singular point must retain a nonzero critical concentration along arbitrarily small scales.

The W1 defect is one explicit representation of that necessary concentration:

\[
\boxed{
\text{weak-L3 boundary defect}
\Longrightarrow
\text{positive local-energy Morrey density}.
}
\]

Hence proving uniform no-defect from the currently known finite-energy bounds alone would amount to proving away a standard singular-point critical concentration.

## 5. Consequence for proof search

The primary new theorem must exploit additional W1 structure beyond ordinary energy compactness, such as the finite-amplitude pressure/viscous formation band, recurrent scale geometry, or another genuinely critical cancellation.

A simple `L2`-tightness argument cannot close W1.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
