# DSD M17-326 — directed zero-kappa crossing flux is parabolic scale-critical and counts simple material sign transitions

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION / CRITICAL-CURRENCY CANDIDATE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation and scope

M17-323 produced a noncancelling directed zero-\(\kappa\) turnover activity.  M17-325 showed that the strain-square physicalization is supercritical by three record-scale powers.

This module asks whether the **transition measure itself**, rather than a squared spatial payer, has critical Navier--Stokes scaling.

The DSD-theoretical motivation is only heuristic: a structural transition count is a better cross-representation candidate than a signed state average.  The calculation below is entirely standard scaling/coarea mathematics.

## 2. Material crossing measure

Let

\[
h:=D_B\kappa
\]

along a regular material flux label and let \(d\Phi\) denote oriented material vorticity flux.

Define the downward zero-crossing measure on a time interval \(I\) by

\[
\boxed{
\mathcal C_-(I)
:=
\int_I\int
h_-\,\delta(\kappa)\,d\Phi\,ds,
\qquad
h_-:=(-h)_+.
}
\]

Likewise

\[
\mathcal C_+(I)
:=
\int_I\int
h_+\,\delta(\kappa)\,d\Phi\,ds.
\]

These are nonnegative measures.  Their signed difference recovers the net zero-level material current integrated in time.

## 3. Relation to M17-323

Resolving the zero-level current by the line-weight coordinate gives

\[
A_-(s)
=\int(-j_k(0,l,s))_+dl.
\]

On the deterministic regular label representation \(j_k=hH\), the coarea/distributional reading is

\[
\boxed{
\mathcal C_-(I)
=\int_I A_-(s)ds
}
\]

provided the zero level is represented without hidden label-boundary/replacement loss.

Thus the M17-323 lower long-time density becomes

\[
\mathcal C_-([0,T])
\ge d_{flux}T-o(T)
\]

on the retained normalized branch.

## 4. Parabolic scaling of the ingredients

Under standard Navier--Stokes scaling

\[
V_R(y,s)=R V(Ry,R^2s),
\]

we have

\[
\Omega_R=R^2\Omega,
\qquad
\kappa_R=R^2\kappa.
\]

The coefficient velocity scales with two additional derivatives in parabolic time:

\[
\boxed{
h_R=D_{B_R}\kappa_R=R^4h}
\]

under the corresponding pulled-back material trajectory.

Material vorticity flux is scale invariant:

\[
d\Phi_R
=\rho_R\,dA_R
=(R^2\rho)(R^{-2}dA)
=\boxed{d\Phi}.
\]

The delta distribution scales as

\[
\delta(\kappa_R)
=\delta(R^2\kappa)
=R^{-2}\delta(\kappa),
\]

and

\[
ds=R^{-2}dt.
\]

Therefore

\[
h_{R,-}\delta(\kappa_R)d\Phi_Rds
=
R^4h_-
\cdot R^{-2}\delta(\kappa)
\cdot d\Phi
\cdot R^{-2}dt.
\]

All powers cancel:

\[
\boxed{
\mathcal C_{-,R}(I)
=
\mathcal C_-(R^2I).
}
\]

Hence the directed crossing flux is exactly parabolic scale critical.

## 5. Simple-crossing coarea interpretation

Fix one material label \(\lambda\) and suppose \(\kappa_\lambda(s)\) has only simple zeroes in a compact interval \(I\):

\[
\kappa_\lambda(s_j)=0,
\qquad
h_\lambda(s_j)=\dot\kappa_\lambda(s_j)\ne0.
\]

The one-dimensional delta/coarea identity gives

\[
\int_I
|h_\lambda(s)|\delta(\kappa_\lambda(s))ds
=
\#\{s_j\in I\}.
\]

Moreover

\[
\boxed{
\int_I
h_{\lambda,-}\delta(\kappa_\lambda)ds
=N^-_\lambda(I),
}
\]

where \(N^-_\lambda(I)\) is the number of simple downward sign crossings.

Integrating over material flux labels,

\[
\boxed{
\mathcal C_-(I)
=
\int N^-_\lambda(I)\,d\Phi(\lambda)
}
\]

on the transverse-simple-zero branch.

Thus \(\mathcal C_-\) is not merely an algebraic current norm: it is the material-vorticity-flux-weighted count of directed coefficient sign transitions.

## 6. Degenerate-zero firewall

If

\[
\kappa=0,
\qquad h=0,
\]

at a zero level, the simple coarea count cannot be used without examining higher time jets.  Record the typed alternatives

\[
G_{degenerate\ zero\text{-}jet}
\lor
G_{zero\text{-}level\ sticking}.
\]

Time analyticity, where available on the relevant same-generation material representation, can make isolated zeroes finite-order locally, but it does **not** by itself supply a uniform global crossing count on an unbounded time interval.

Therefore no degenerate crossing is silently counted as one unit.

## 7. Why this is better than the M17-325 payer

M17-325 found

\[
\int\sigma^2\rho^2dxdt
\mapsto R^3
\int\sigma^2\rho^2dxdt,
\]

which is strongly supercritical.

By contrast

\[
\boxed{
\mathcal C_-
\mapsto\mathcal C_-
}
\]

under record blow-down.

Thus directed crossing flux is the first late-current quantity in this route that survives the cross-generation scaling audit without an inverse power of the record scale.

## 8. Remaining obstruction

Scale criticality alone does not imply a contradiction.  To use \(\mathcal C_-\) globally one still needs one of:

1. a finite total crossing-flux theorem on the first ancient element;
2. a rigidity theorem excluding positive-density recurrent downward crossings on the compact CE-H hull;
3. bounded-multiplicity genealogy showing repeated second-generation crossing flux pulls back to disjoint ancestral crossing events;
4. a proof that replacement/migration needed to avoid such counting pays another certified critical resource.

None is currently established.

In particular,

\[
\boxed{
\text{critical crossing flux}
\not\Rightarrow
\text{finite crossing budget}.
}
\]

## 9. Updated target

The next calculation should exploit the exact flux-channel law

\[
\dot u=\kappa,
\qquad u=\log\Phi,
\]

and ask whether repeated directed zero crossings can coexist with compact/recurrent same-label flux behavior without either

\[
\text{unbounded flux cocycle}
\quad\text{or}\quad
\text{material replacement/genealogy turnover}.
\]

## 10. Audit verdict

**PASS as a scale-critical transition currency.**

This is a genuine gain over the supercritical strain payer, but it remains a candidate obstruction rather than a completed proof step to global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
