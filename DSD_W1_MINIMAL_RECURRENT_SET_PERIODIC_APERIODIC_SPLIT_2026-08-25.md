# DSD W1 minimal recurrent set: periodic / aperiodic split

Date: 2026-08-25

Status: **COMPACT-DYNAMICAL REDUCTION PROVED / EQUILIBRIUM AND SHORT-PERIOD SURVIVORS REMOVED / LARGE-PERIOD PERIODIC AND APERIODIC MINIMAL SETS REMAIN OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. W1 input

Work on the surviving pure corridor with a smooth autonomous Leray trajectory `U(s)` satisfying, for one fixed `p` with `3<p<=6`,

\[
\sup_{s\ge s_0}\|U(s)\|_{L^p}<\infty
\]

and with the already proved uniform tail estimate

\[
\sup_{s\ge s_0}\int_{|Y|>R}|U(Y,s)|^p\,dY
\lesssim R^{3-p}\to0.
\]

Local first-hitting analyticity supplies compactness on every bounded space-time cylinder. Hence the forward Leray orbit is precompact in global `L^p`.

The singular-survivor one-slice speed gate supplies a fixed core ball `B_M` and

\[
\boxed{
\|U_s(s)\|_{L^2(B_M)}\ge\sigma_0>0
}
\]

for all sufficiently late `s` in the audited recurrent corridor. Local analyticity also supplies

\[
\|U_{ss}(s)\|_{L^2(B_M)}\le K_{ss}.
\]

Consequently there is a no-short-return time

\[
h_0:=\min\{1,\sigma_0/K_{ss}\}>0
\]

such that

\[
\boxed{
0<h\le h_0
\Longrightarrow
\|U(s+h)-U(s)\|_{L^2(B_M)}
\ge\frac{\sigma_0}{2}h.
}
\]

## 2. Global omega-limit set

Let `S(h)` denote the autonomous Leray time-shift semiflow on the smooth compact class, and define

\[
K
:=
\bigcap_{T>0}
\overline{\{U(s):s\ge T\}}^{L^p}.
\]

Because the orbit is precompact, `K` is nonempty and compact.
Continuity of the smooth Leray semiflow on the compact class gives

\[
S(h)K\subset K,
\qquad h\ge0.
\]

In fact `S(h)K=K`. To see surjectivity, take `V in K` and a sequence `s_n->infinity` with `U(s_n)->V`. For fixed `h>0`, precompactness gives a subsequence

\[
U(s_n-h)\to W\in K,
\]

and continuity yields

\[
S(h)W=V.
\]

Thus

\[
\boxed{S(h)K=K\quad(h\ge0).}
\]

## 3. Minimal compact invariant subset

The family of nonempty compact invariant subsets of `K`, ordered by inclusion, contains a minimal element `M` by the standard nested-compact/Zorn argument.

For every `V in M`, the closure of its forward orbit is a nonempty compact invariant subset of `M`; minimality therefore gives

\[
\boxed{
\overline{\{S(h)V:h\ge0\}}=M.
}
\]

Hence every point of `M` is recurrent in the topological-dynamical sense and every orbit is dense in `M`.

This is the exact dynamical object carried by the compact W1 survivor.

## 4. Equilibrium is impossible

If `M` contains an equilibrium `V_*`, then the singleton `{V_*}` is a nonempty compact invariant subset of `M`. Minimality forces

\[
M=\{V_*\}.
\]

But an equilibrium has `V_{*,s}=0`, contradicting the inherited local speed lower bound

\[
\|U_s\|_{L^2(B_M)}\ge\sigma_0.
\]

Therefore

\[
\boxed{M\text{ contains no equilibrium.}}
\]

No stationary self-similar Liouville theorem is needed for this internal exclusion.

## 5. If a periodic point exists, the whole minimal set is one periodic orbit

Suppose `V in M` is periodic with least period `S>0`:

\[
S(S)V=V.
\]

Its periodic orbit

\[
\mathcal O_V=\{S(h)V:0\le h\le S\}
\]

is nonempty, compact, and invariant. Minimality yields

\[
\boxed{M=\mathcal O_V.}
\]

The no-short-return cone excludes

\[
0<S\le h_0.
\]

Hence every periodic W1 survivor must satisfy

\[
\boxed{S>h_0.}
\]

In physical variables this is a backward discretely self-similar trajectory with scaling factor

\[
\boxed{\lambda=e^{S/2}>e^{h_0/2}>1.}
\]

Thus the only periodic endpoint left is a genuinely finite/large-period DSS-type profile, not a near-continuous self-similar orbit.

## 6. Otherwise the minimal set is genuinely aperiodic

If `M` contains no periodic point, then every orbit is dense in `M` but none closes exactly.
Therefore the second and only other possibility is

\[
\boxed{
M=M_{aper},
\qquad
\text{compact, minimal, recurrent, and aperiodic}.
}
\]

The no-short-return inequality also rules out recurrence with return error `o(h)` at arbitrarily short return times, but it does not rule out returns after finite or long times.

A compact metric flow can support such aperiodic minimal dynamics; compactness plus positive speed alone is therefore not a contradiction.

## 7. Exact final W1 dynamical split

The pure W1 endpoint is reduced to

\[
\boxed{
W_1
\Longrightarrow
P_{DSS}^{long}
\lor
A_{min}^{aper},
}
\]

where

\[
P_{DSS}^{long}:
\text{a nonzero periodic Leray orbit with }S>h_0,
\]

and

\[
A_{min}^{aper}:
\text{a nonzero compact aperiodic minimal recurrent Leray set}.
\]

The equilibrium branch and all periods at or below `h0` are removed internally.

## 8. Why existing endpoint theorems do not yet finish this split

Known periodic/DSS exclusions used elsewhere in the audit either require strong `L^3` control or restrict the DSS scaling factor to a neighborhood of one. The W1 tail may remain exactly at the weak-`L^3` / `1/R` endpoint, and the internal lower bound `S>h0` does not give an upper period bound.

Likewise global `L^p` precompactness for every `p>3` does not by itself exclude a compact aperiodic minimal set.

Therefore the remaining rigidity target is genuinely dynamical:

\[
\boxed{
P_{DSS}^{long}\text{ exclusion}
\quad\text{and/or}\quad
A_{min}^{aper}\text{ exclusion}.
}
\]

A strict Lyapunov functional on the W1 compact class would remove both at once, but no such functional has yet been derived.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
