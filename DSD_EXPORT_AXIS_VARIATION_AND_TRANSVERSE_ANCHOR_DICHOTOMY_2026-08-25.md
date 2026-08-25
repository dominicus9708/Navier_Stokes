# DSD Export-Axis Variation and Transverse-Anchor Dichotomy

Date: 2026-08-25

Status: **PERMANENT EXPORT TOPOLOGY FURTHER REDUCED / POSITIVE AXIS-VARIATION RATE ROUTED TO DIRECTIONAL ACTION / ZERO-RATE SURVIVOR HAS AN ASYMPTOTICALLY FIXED EXPORT AXIS PLUS A PERSISTENT TRANSVERSE ENSTROPHY ANCHOR / GLOBAL REGULARITY UNPROVED.**

## 1. Inputs

Use the following already established pieces.

1. Positive-density replacement plus finite multiflux memory forces a positive-frequency genuine exit.
2. We are now on the subbranch where material export is the positive-frequency exit and exported populations do not return.
3. Coherent permanent exports produce a critical log-radius conveyor.
4. On selected tight H2-bounded recurrent times, `DSD_DIVERGENCE_FREE_DIRECTIONAL_DEFECT_FLOOR_2026-08-25.md` gives
   \[
   \inf_{e\in S^2}\|P_{e^\perp}\Omega\|_2\ge\delta_{dir}>0.
   \]

The aim is to determine what freedom remains in the directions of successive exported flux populations.

## 2. Event-axis sequence

Let

\[
s_1<s_2<\cdots
\]

be the separated positive-frequency permanent-export event times.

Associate to event \(m\) a coherent directed-flux axis

\[
e_m\in S^2/\{\pm1\},
\]

where the sign convention is fixed by the signed flux when available.

Define the projective angular increment

\[
\boxed{
\vartheta_m
:=
\arccos|e_{m+1}\cdot e_m|
\in[0,\pi/2].
}
\]

## 3. Directional-action branch

If

\[
\boxed{
\liminf_{N\to\infty}
\frac1N\sum_{m=1}^{N-1}\vartheta_m
=\bar\vartheta>0,
}
\]

then the export mechanism cannot be regarded as a directionally quiet pure-export lane.

There is a positive mean amount of axis reorganization per export event.

Because export events themselves occur with positive Leray-time frequency, the directional variation has positive Leray-time action density.

This is routed to the already defined projective/directional/H ledger.

The routing is conservative: if the axis change is produced by material-line rotation, the vorticity-direction equation pays strain/viscous action; if it is produced by replacement by differently oriented labels, the event is itself a directional replacement rather than pure fixed-axis export.

Status: **ROUTED TO EXISTING DIRECTIONAL/PROJECTIVE T/H, NOT A NEW QUIET SURVIVOR.**

## 4. Zero-mean axis-variation branch

The only new pure-export survivor therefore satisfies

\[
\boxed{
\frac1N\sum_{m=1}^{N-1}\vartheta_m\to0.
}
\]

For every fixed \(\varepsilon>0\), the density of indices with

\[
\vartheta_m>\varepsilon
\]

tends to zero.

Consequently there are arbitrarily long event blocks on which all successive axis increments are small.

Choose \(\varepsilon_n\downarrow0\) and blocks whose lengths tend to infinity. By compactness of \(S^2/\{\pm1\}\) and a diagonal extraction, there exists an axis \(e_*\) such that for each fixed event offset \(\ell\),

\[
\boxed{
e_{m_n+\ell}\to e_*}
\]

along the selected block centers \(m_n\).

Thus the zero-action-density pure-export limit is asymptotically fixed-axis on every finite log-shell window.

## 5. The fixed-axis limit cannot be globally one-directional

At the same selected tight H2-bounded recurrent times, the divergence-free directional-defect floor applies to the export axis.

Passing to the fixed-axis subsequence gives

\[
\boxed{
\|P_{e_*^\perp}\Omega\|_2
\ge\delta_{dir}>0.
}
\]

Therefore the asymptotically fixed export conveyor must coexist with a nonvanishing transverse vorticity component.

The final quiet topology is not

\[
\text{one-axis critical tail only},
\]

but rather

\[
\boxed{
\text{fixed-axis critical export conveyor}
+
\text{persistent transverse enstrophy anchor}.
}
\]

## 6. Why the transverse anchor matters

The transverse anchor is global and order one in \(L^2\)-vorticity on the tight H2-bounded corridor.

It cannot disappear in the same limit in which the export axes become fixed.

Therefore any exact limiting model of the final survivor must contain at least two geometrically distinct vorticity sectors:

1. the scale-critical exported flux conveyor aligned with \(e_*\);
2. a transverse enstrophy sector of norm at least \(\delta_{dir}\).

This rules out a simple one-dimensional/one-axis asymptotic reduction.

## 7. What is not yet proved

The transverse anchor may be the same persistent residual structure reused through arbitrarily many export events.

Therefore its mere existence is not an additive event charge.

The next target is to prove one of:

\[
\boxed{
\begin{aligned}
&\text{fixed-axis conveyor + transverse anchor}
\Rightarrow\text{Betchov/H production},\\
&\text{or}\quad
\Rightarrow\text{multiflux replacement cost},\\
&\text{or}\quad
\Rightarrow\text{return/recycling},\\
&\text{or}\quad
\Rightarrow\text{a forbidden ancient/DSS limiting profile}.
\end{aligned}
}
\]

## 8. Relation to the known backward-DSS frontier

General nonzero backward discretely self-similar Navier--Stokes solutions remain a known open class at weak-critical decay.

Therefore merely extracting approximate or exact scale recurrence would not by itself finish the proof unless the additional transverse-anchor structure is exploited.

This is an important audit constraint: the next argument must use more than generic Type-I/DSS compactness.

## 9. Updated permanent-export frontier

The branch is now

\[
\boxed{
X_{export,+freq}^{permanent}
\Longrightarrow
\begin{cases}
X_{directional-action,+rate},\\
\text{or}\\
\text{fixed-axis critical conveyor}
+
\text{persistent transverse anchor}.
\end{cases}
}
\]

The first line is routed to existing projective/H machinery.

Only the second line is genuinely new.

## 10. Audit verdict

### PROVED/COMBINATORIAL

- positive mean projective axis variation cannot remain a pure directionally quiet export branch;
- zero mean axis variation yields arbitrarily long asymptotically fixed-axis export blocks;
- the divergence-free tight H2 lemma forces a fixed transverse-enstrophy floor along such blocks.

### LAST SURVIVOR AFTER THIS SPLIT

\[
\boxed{
\text{asymptotically fixed-axis }1/R\text{ export conveyor}
+
\text{persistent transverse enstrophy anchor}.
}
\]

### OPEN

Convert the coexistence of these two sectors into a coercive interaction or rigidity contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
