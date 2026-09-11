# M19-008 — Ancestral return threshold requires quadratic age multiplicity unless single-episode dwell is enhanced

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC RETURN-WEIGHT KINEMATICS / MULTIPLICITY THRESHOLD / TRAPPING-ENHANCEMENT SPLIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-005--007 exhaust the presently certified signed-budget shortcuts for R-AC.

M18-054 sharpens the surviving ancestry-conversion branch to

\[
\sum_kJ_k^{3/2}=\infty,
\qquad
\mathfrak R_k
=\frac1{\rho_k}\sum_{\ell=1}^{M_k}\tau_{k,\ell},
\]

with the desired sufficient closure threshold

\[
\mathfrak R_k\gtrsim J_k^{1/2}.
\]

For an age-\(k\) shell the scale ratio is

\[
\boxed{K_k=q^{k/2}}
\]

and M18-054 records the exact single-current-epoch age penalty

\[
\boxed{K_k^{-2}=q^{-k}}
\]

in ancestor-normalized dwell.

The present module calculates how many effective returns are required to overcome this penalty.

## 2. Episode dwell variable

Define the dimensionless episode contribution already implicit in the M18 return density by

\[
\boxed{
d_{k,\ell}:=\frac{\tau_{k,\ell}}{\rho_k}.
}
\]

Then

\[
\boxed{
\mathfrak R_k
=\sum_{\ell=1}^{M_k}d_{k,\ell}.
}
\]

A **plain current-epoch episode** means an episode whose descendant-normalized temporal width is bounded by a fixed constant and which acquires no extra trapping/residence enhancement under parent conversion.

For such an episode, the M18 age law gives

\[
\boxed{
d_{k,\ell}\le C_0K_k^{-2}}
\]

with a record-independent constant \(C_0\) on the controlled branch.

This is the precise hypothesis of the transit calculation below.

If this bound fails, that failure is not discarded; it is the enhanced-residence/trapping branch.

## 3. Plain-transit return upper bound

If all \(M_k\) return episodes at shell \(k\) are plain current-epoch episodes, then

\[
\mathfrak R_k
=\sum_{\ell=1}^{M_k}d_{k,\ell}
\le
C_0M_kK_k^{-2}.
\]

Hence

\[
\boxed{
\mathfrak R_k
\lesssim
M_kK_k^{-2}.
}
\]

This formula separates the two possible ways to defeat the age penalty:

1. many distinct/effective return episodes \(M_k\);
2. enhanced dwell in at least one episode.

## 4. Multiplicity needed for the cubic closure threshold

Suppose one wants the sufficient R-AC closure estimate

\[
\mathfrak R_k
\ge c_0J_k^{1/2}.
\]

Combining with Section 3 gives

\[
c_0J_k^{1/2}
\le
C_0M_kK_k^{-2}.
\]

Therefore

\[
\boxed{
M_k
\ge
c_1K_k^2J_k^{1/2},
\qquad
c_1:=c_0/C_0.
}
\]

This is the exact multiplicity threshold on the plain-transit branch.

Because

\[
K_k^2=q^k,
\]

the required multiplicity grows exponentially in the age index, modulo the factor \(J_k^{1/2}\).

## 5. Cubic divergence prevents all important shells from having tiny J

A potential escape would be

\[
J_k^{1/2}\lesssim K_k^{-1}.
\]

But then

\[
J_k^{3/2}\lesssim K_k^{-3}.
\]

Since

\[
K_k=q^{k/2},
\]

\[
\sum_kK_k^{-3}
=
\sum_kq^{-3k/2}
<\infty.
\]

Therefore the full divergent cubic mass cannot be carried by shells satisfying a fixed bound

\[
J_k^{1/2}\le CK_k^{-1}.
\]

More precisely, for every fixed \(C>0\), define

\[
\mathcal H_C
:=
\{k:K_kJ_k^{1/2}>C\}.
\]

On the complement,

\[
J_k^{3/2}\le C^3K_k^{-3},
\]

so

\[
\sum_{k\notin\mathcal H_C}J_k^{3/2}<\infty.
\]

Since the full cubic sum diverges,

\[
\boxed{
\sum_{k\in\mathcal H_C}J_k^{3/2}=\infty
\qquad\forall C>0.
}
\]

Thus cubic-mass divergence is always supported, up to a finite remainder, on shells where

\[
K_kJ_k^{1/2}
\]

is arbitrarily large relative to any fixed threshold.

## 6. Consequence for required multiplicity

On \(\mathcal H_C\),

\[
K_k^2J_k^{1/2}>CK_k.
\]

Hence the plain-transit closure threshold requires

\[
\boxed{
M_k\gtrsim CK_k
}
\]

on a cubic-mass-divergent family, for every fixed \(C\) after passing to the corresponding high-ratio sector.

Equivalently, the ratio

\[
\frac{M_k}{K_k}
\]

cannot stay uniformly bounded on every cubic-mass-dominant subsequence if the sufficient return threshold is to hold by plain-transit multiplicity alone.

The stronger exact requirement remains

\[
M_k\gtrsim K_k^2J_k^{1/2}.
\]

## 7. Define the residence-enhancement factor

To include both mechanisms in one formula, define

\[
\boxed{
\eta_{k,\ell}
:=
K_k^2d_{k,\ell}
}
\]

and the total enhancement

\[
\boxed{
\mathcal E_k
:=
\sum_{\ell=1}^{M_k}\eta_{k,\ell}
=K_k^2\mathfrak R_k.
}
\]

Then the desired closure threshold is exactly

\[
\boxed{
\mathcal E_k
\gtrsim
K_k^2J_k^{1/2}.
}
\]

Plain current-epoch returns have

\[
\eta_{k,\ell}=O(1),
\]

so

\[
\mathcal E_k=O(M_k).
\]

A large \(\eta_{k,\ell}\) is precisely a long-residence/trapping episode relative to the parabolic age baseline.

## 8. Exact multiplicity-versus-trapping split

Fix any \(A>0\).

If

\[
M_k
<
\frac{c_1}{2A}K_k^2J_k^{1/2}
\]

and every episode satisfies

\[
\eta_{k,\ell}\le A,
\]

then

\[
\mathcal E_k
\le AM_k
<
\frac{c_1}{2}K_k^2J_k^{1/2},
\]

so the sufficient return threshold fails.

Therefore whenever the threshold holds,

\[
\boxed{
M_k
\gtrsim_A
K_k^2J_k^{1/2}
\quad\lor\quad
\max_\ell\eta_{k,\ell}>A.
}
\]

Since \(A\) is arbitrary, successful ancestry conversion requires either

\[
\boxed{
\text{very large effective return multiplicity}
}
\]

or

\[
\boxed{
\text{parabolically anomalous long residence/trapping}.
}
\]

## 9. Relation to the M18-054 deficiency endpoint

M18-054 proves that an R-AC survivor has

\[
a_k
:=
\frac{\mathfrak R_k}{J_k^{1/2}}
\to0
\]

in cubic-mass density.

The present identity rewrites this as

\[
\boxed{
a_k
=\frac{\mathcal E_k}{K_k^2J_k^{1/2}}.
}
\]

Thus the return-deficient survivor is exactly the regime where the realized combined multiplicity/trapping enhancement \(\mathcal E_k\) is negligible relative to the required scale

\[
K_k^2J_k^{1/2}.
\]

This converts the abstract deficiency variable into a concrete genealogical target.

## 10. What this calculation does and does not prove

### Proved

1. Plain single-return dwell loses \(K_k^{-2}\).
2. Plain-return closure requires
   \[
   M_k\gtrsim K_k^2J_k^{1/2}.
   \]
3. Cubic divergence forces the important shells away from the uniformly tiny regime \(J_k^{1/2}=O(K_k^{-1})\).
4. Any successful return conversion must be paid by large multiplicity or anomalous residence enhancement.

### Not proved

- an upper bound on \(M_k\);
- impossibility of long trapping;
- a contradiction from cubic divergence alone;
- closure of R-AC.

## 11. Next calculation

M19-009 should calculate how large \(M_k\) can be for a coherent material carrier under controlled transport geometry.

A purely geometric crossing lemma should compare return count with the total variation of a normalized shell/radial coordinate:

\[
M_k\times(\text{shell separation})
\lesssim
\int|\dot r_{material}|dt.
\]

This will separate

\[
\boxed{
\text{rapid repeated crossing}
\lor
\text{long trapping / grazing / shell-following}
\lor
\text{geometry turnover}.
}
\]

If bounded compact transport permits only subquadratic return multiplicity, the R-AC survivor will be reduced further to a trapping/grazing mechanism rather than an unstructured lack of ancestry.

---

\[
\boxed{\text{M19-008 COMPLETE; R-AC IS NOW A MULTIPLICITY/TRAPPING PROBLEM.}}
\]
