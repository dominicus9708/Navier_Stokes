# M19-046 — Type-I clock and natural-time dwell show the distinct-return-count closure target is too strong on the cubic-divergent sector

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC NEGATIVE CLOSURE RESULT / RETURN-COUNT TARGET RETIRED ON THE MAIN CUBIC-DIVERGENT CORRIDOR

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-040--045 sharpened the quiet R-AC route to the sufficient return-count target

\[
\boxed{
N_k^{dist}\rho_k
\gtrsim
J_k^{1/2}
}
\]

on a subset carrying

\[
\sum_kJ_k^{3/2}=\infty.
\]

The present module asks whether the first-hitting Type-I clock leaves enough physical time for that many natural-time contacts to occur.

The answer is negative on the main cubic-divergent shrinking-radius sector.

The return-count inequality is therefore not merely unproved; under the retained shell-comparability and Type-I hypotheses it is generically too strong to be the final R-AC closure mechanism.

## 2. Bulk shell mass forces a pointwise vorticity amplitude floor

On the retained bulk-dominant shell-comparable branch, M19-039 uses

\[
\boxed{
m_k
:=
\int_{E_{\rho_k}}|\omega|^2dx
\ge
c_m\frac{J_k}{\rho_k}.
}
\]

The active shell collar has volume

\[
|E_{\rho_k}|\le C_V\rho_k^3.
\]

Therefore

\[
\|\omega\|_{L^\infty(E_{\rho_k})}^2
\ge
\frac{m_k}{|E_{\rho_k}|}
\ge
c\frac{J_k}{\rho_k^4}.
\]

Hence every genuine bulk shell contact forces

\[
\boxed{
\|\omega(t)\|_\infty
\ge
c_\omega\frac{J_k^{1/2}}{\rho_k^2}.
}
\]

This lower floor is independent of the upper comparability bound used in M19-039.

## 3. Locate the corresponding first-hitting stage

Let

\[
A_k
:=
c_\omega\frac{J_k^{1/2}}{\rho_k^2}.
\]

The first-hitting amplitudes satisfy

\[
W_{j+1}=qW_j.
\]

Choose \(n(k)\) so that

\[
W_{n(k)}\le A_k<qW_{n(k)}.
\]

Before the first-hitting time \(t_{n(k)}\),

\[
\|\omega(t)\|_\infty<W_{n(k)}\le A_k.
\]

After adjusting the harmless fixed constants in the shell amplitude floor, a contact satisfying the bulk lower bound cannot occur before a stage with

\[
W_{n(k)}\asymp A_k.
\]

Thus all such nondegenerate shell contacts lie inside the remaining first-hitting history

\[
[t_{n(k)},T_*).
\]

## 4. Type-I clock bounds the entire available physical history

The first-hitting clock is

\[
\Theta_n
:=
W_n(T_*-t_n).
\]

On the retained Type-I corridor,

\[
0<\Theta_-\le\Theta_n\le\Theta_+<\infty.
\]

Therefore

\[
T_*-t_{n(k)}
\le
\frac{\Theta_+}{W_{n(k)}}
\lesssim
A_k^{-1}.
\]

Using the definition of \(A_k\),

\[
\boxed{
T_*-t_{n(k)}
\lesssim
\frac{\rho_k^2}{J_k^{1/2}}.
}
\]

This is an upper bound on the **entire physical time available** for all contacts carrying that shell bulk mass after the relevant amplitude first appears.

## 5. Natural-time dwell gives an upper bound on the number of distinct contacts

M19-039 gives, on the fully retained quiet branch,

\[
|I_{k,\ell}|\ge c_0\rho_k^2
\]

for every genuine contact episode.

After the standard bounded-overlap extraction with multiplicity at most \(Q\),

\[
\frac{c_0}{Q}N_k^{dist}\rho_k^2
\le
\left|\bigcup_\ell I_{k,\ell}\right|
\le
T_*-t_{n(k)}.
\]

Hence

\[
N_k^{dist}\rho_k^2
\lesssim
\frac{\rho_k^2}{J_k^{1/2}},
\]

and therefore

\[
\boxed{
N_k^{dist}
\lesssim
J_k^{-1/2}.
}
\]

This is the exact Type-I time-capacity ceiling for distinct natural-time contacts of a bulk shell mark with charge \(J_k\).

## 6. Maximum weighted return density

Multiplying by \(\rho_k\),

\[
\boxed{
N_k^{dist}\rho_k
\lesssim
\frac{\rho_k}{J_k^{1/2}}.
}
\]

But the old sufficient cubic closure target is

\[
N_k^{dist}\rho_k
\gtrsim
J_k^{1/2}.
\]

For both to hold, one must have

\[
\boxed{
J_k
\lesssim
\rho_k.
}
\]

Thus the desired return-count lower bound is kinematically compatible with the Type-I clock only on the small-charge sector \(J_k\lesssim\rho_k\).

## 7. Small-charge sector cannot carry divergent cubic mass on a geometric shrinking-radius family

Assume the standard physical ancestor radii form a geometric shrinking family, so in particular

\[
\boxed{
\sum_k\rho_k^{3/2}<\infty.
}
\]

On the compatibility sector

\[
J_k\le C\rho_k,
\]

we have

\[
J_k^{3/2}
\le
C^{3/2}\rho_k^{3/2}.
\]

Therefore

\[
\boxed{
\sum_{k:J_k\lesssim\rho_k}
J_k^{3/2}<\infty.
}
\]

Consequently the divergent cubic mass

\[
\sum_kJ_k^{3/2}=\infty
\]

must be carried, in cubic-mass density, by shells for which

\[
\boxed{
\frac{J_k}{\rho_k}
\to\infty
}
\]

along appropriate extracted blocks.

But on precisely that sector the lower target

\[
N_k^{dist}\rho_k\gtrsim J_k^{1/2}
\]

is incompatible with the Type-I time-capacity ceiling.

## 8. Arithmetic firewall

The mismatch is visible in the simple model

\[
J_k=k^{-2/3},
\qquad
\rho_k=q^{-k/2}.
\]

Then

\[
\sum_kJ_k^{3/2}
=
\sum_k\frac1k
=
\infty,
\]

while

\[
\frac{J_k}{\rho_k}
=k^{-2/3}q^{k/2}
\to\infty.
\]

The Type-I capacity ceiling gives

\[
N_k^{dist}
\lesssim
k^{1/3},
\]

whereas the old closure target would require

\[
N_k^{dist}
\gtrsim
k^{-1/3}q^{k/2}.
\]

The gap is exponential.

Therefore no argument based only on fitting repeated natural-time returns after the relevant first-hitting amplitude can prove the old count target on the full cubic-divergent corridor.

## 9. Interpretation

M19-039 successfully solved the dwell-duration defect of one actual contact.

But that very natural-time thickness, combined with the finite Type-I remaining-time clock, creates a hard upper bound on how many distinct contacts can occur after the shell amplitude becomes possible.

Thus

\[
\boxed{
\text{natural-time thickening}
+\text{Type-I clock}
\Longrightarrow
\text{finite return capacity }N_k^{dist}\lesssim J_k^{-1/2}.
}
\]

The old sufficient target demands the opposite scale growth on the cubic-dominant sector.

Hence the direct return-count closure route is structurally mismatched.

## 10. Consequence for M19-045 historical span

M19-045 required

\[
L_k^{hist}
\gtrsim
J_k^{1/2}\rho_k
\]

for the old return-count closure.

The Type-I amplitude clock supplies at most

\[
L_{k,max}^{hist}
\lesssim
\frac{\rho_k^2}{J_k^{1/2}}.
\]

Therefore

\[
\boxed{
\frac{L_{k,max}^{hist}}
{J_k^{1/2}\rho_k}
\lesssim
\frac{\rho_k}{J_k}.
}
\]

On the cubic-dominant sector \(J_k/\rho_k\to\infty\), the available historical span is asymptotically far too short.

This independently confirms the return-count mismatch.

## 11. R-AC frontier must be changed

The theorem target

\[
\mathcal T_{count}^{dist}:
N_k^{dist}\rho_k\gtrsim J_k^{1/2}
\]

should no longer be treated as the primary expected closure theorem on the retained Type-I cubic-divergent branch.

It remains a valid **sufficient condition**, but M19-046 shows that it cannot be supplied by the current first-hitting natural-time genealogy on the cubic-dominant sector.

The R-AC survivor must therefore be attacked by another mechanism, such as:

1. a rigidity theorem for asymptotically return-deficient cubic mass;
2. a stronger finite parent budget whose per-contact price does not contain the shrinking factor \(\rho_k\);
3. a nonlocal interaction between different shell ages rather than repeated returns of one age;
4. a signed/critical observable with a genuine fixed-parent finite-variation law;
5. routing the return-deficient sector into the R-critical scattering object.

## 12. New endpoint

The most precise retained endpoint is now the return-deficient concentration already exposed in M18-054, strengthened by the new capacity ceiling:

\[
\boxed{
\mathcal R_{AC}^{sharp}:
\sum_kJ_k^{3/2}=\infty,
\qquad
\mathfrak R_k/J_k^{1/2}\to0
\text{ in cubic-mass density},
\qquad
N_k^{dist}\lesssim J_k^{-1/2}.
}
\]

On the geometric shrinking-radius cubic-dominant sector,

\[
\boxed{
J_k/\rho_k\to\infty
}
\]

in the extracted mass-bearing blocks.

This is now a much sharper target than a generic ancestry-conversion deficiency.

## 13. What is not proved

This module does not rule out R-AC.

It rules out the expectation that the old sufficient distinct-return count can be forced from the retained first-hitting Type-I natural-time genealogy on the cubic-dominant sector.

It also does not apply if the Type-I clock, bulk shell comparability, bounded weak-\(L^3\), controlled center, or quiet-source assumptions fail; those failures are already separate typed exits.

Global 3D Navier--Stokes regularity remains unproved.

## 14. Next calculation

The highest-value next question is now whether the sharp return-deficient sector automatically produces a **critical spatial/scattering object**.

The key asymptotic regime is

\[
J_k/\rho_k\to\infty,
\]

with shell bulk enstrophy

\[
m_k\gtrsim J_k/\rho_k.
\]

One should test whether this forces a scale-invariant kinetic Morrey or weak-\(L^3\) tail at a common physical center, or else requires spatial export / multicore decorrelation already typed by the remote analysis.

If such a bridge exists, R-AC could collapse into R-critical rather than being closed by ancestry return counting.

---

\[
\boxed{\text{M19-046 COMPLETE; DISTINCT-RETURN COUNT IS RETIRED AS THE PRIMARY R-AC CLOSURE TARGET ON THE CUBIC-DIVERGENT TYPE-I CORRIDOR.}}
\]