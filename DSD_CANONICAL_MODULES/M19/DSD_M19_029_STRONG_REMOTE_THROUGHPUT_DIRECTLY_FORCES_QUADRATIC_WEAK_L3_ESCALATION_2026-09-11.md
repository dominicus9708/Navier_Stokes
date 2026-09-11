# M19-029 — Strong remote throughput directly forces quadratic weak-L3 escalation

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE COLLAPSE / LORENTZ LOWER BOUND / W1 EXIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. M5-443 source oscillation floor

On the strong remote source branch,

\[
R_j=K_jr_j,
\qquad
K_j\to\infty,
\]

M5-443 gives on a source domain \(D_{R_j}\) of volume comparable to \(R_j^3\)

\[
\boxed{
\inf_{c\in\mathbb R^3}
\|u(\cdot,t_j)-c\|_{L^2(D_{R_j})}
\ge
c_0\nu K_j^2R_j^{1/2}.
}
\]

This estimate is Galilean invariant because of the infimum over constants.

## 2. Finite-measure Lorentz embedding

On every measurable set \(D\) of finite measure,

\[
L^{3,\infty}(D)\hookrightarrow L^2(D),
\]

with

\[
\boxed{
\|f\|_{L^2(D)}
\le
C|D|^{1/6}
\|f\|_{L^{3,\infty}(D)}.
}
\]

Since

\[
|D_{R_j}|^{1/6}
\asymp R_j^{1/2},
\]

we obtain for every constant \(c\)

\[
\|u-c\|_{L^{3,\infty}(D_{R_j})}
\gtrsim
R_j^{-1/2}
\|u-c\|_{L^2(D_{R_j})}.
\]

Taking the infimum in \(c\),

\[
\boxed{
\inf_c
\|u(\cdot,t_j)-c\|_{L^{3,\infty}(D_{R_j})}
\ge
c_1\nu K_j^2.
}
\]

## 3. The actual physical weak-L3 norm diverges

The preceding bound holds for every constant, hence in particular for \(c=0\):

\[
\|u(\cdot,t_j)\|_{L^{3,\infty}(D_{R_j})}
\ge c_1\nu K_j^2.
\]

Restriction cannot increase the global norm downward, so

\[
\boxed{
\|u(\cdot,t_j)\|_{L^{3,\infty}(\mathbb R^3)}
\ge
c_1\nu K_j^2.
}
\]

Therefore

\[
\boxed{
K_j\to\infty
\Longrightarrow
\|u(t_j)\|_{L^{3,\infty}}
\to\infty.
}
\]

The escalation is at least quadratic in the remote scale ratio.

## 4. Strong L3 also escalates

The ordinary finite-measure embedding

\[
\|f\|_2
\le
|D|^{1/6}\|f\|_3
\]

gives likewise

\[
\boxed{
\inf_c
\|u-c\|_{L^3(D_{R_j})}
\gtrsim
\nu K_j^2.
}
\]

Thus the source is not merely a weak-L3 endpoint artifact.

## 5. Independence from the energy parameter Lambda

No use has been made of

\[
\Lambda_j=K_j^5r_j.
\]

Hence both

\[
\Lambda_j\gtrsim1
\]

and

\[
\Lambda_j\to0
\]

satisfy the same weak-L3 escalation whenever the strong remote oscillation floor of M5-443 holds.

The nondegenerate/dilute split remains useful for understanding physical energy concentration and Euler-source structure, but it is unnecessary for proving exit from the bounded weak-L3 corridor.

## 6. Root consequence

On any branch satisfying

\[
\sup_{t<T_*}
\|u(t)\|_{L^{3,\infty}}<\infty,
\]

M19-029 directly excludes

\[
K_j\to\infty
\]

strong remote sources.

Therefore

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
G_{weak\text{-}L^3\ escalation}.
}
\]

This is stronger and simpler than the indirect terminal-energy-atom route of M19-025--028 for the purpose of W1 branch classification.

## 7. What remains of R-remote

The strong remote-throughput / Type-II source is no longer an independent quiet root inside the bounded weak-L3 corridor.

The remaining remote complex consists of mechanisms not covered by the M5-443 strong oscillation floor, principally:

- historical recycling / export-return without a strong instantaneous source;
- remote satellite chains below the strong-throughput threshold;
- spatial/domain/tail noncompactness that already exits W1;
- weak-L3 escalation itself.

Thus the active independent remote question becomes whether any **weak remote/historical** branch can remain bounded in weak-L3 without generating the strong source floor.

## 8. Relation to R-critical

M18 classifies weak-L3 escalation as a W1-boundary / critical-remote exit rather than a compact survivor.

Accordingly, the strong Type-II remote source has now been pushed entirely out of the compact W1 route:

\[
\boxed{
\text{compact W1 survivor}
\cap
H_{remote}^{strong}
=\varnothing.
}
\]

This is a genuine root recompression, not a global regularity theorem.

## 9. Next calculation

M19-030 should return to the residual **weak remote/historical recycling** branch and ask whether repeated remote satellites below the strong-throughput threshold either

1. accumulate to the M5-443 strong oscillation floor;
2. remain weak and hence are summable/compact;
3. or export into the already exposed critical-tail / ancestry-conversion roots.

---

\[
\boxed{\text{M19-029 DIRECTLY IDENTIFIES STRONG REMOTE TYPE-II SOURCES WITH WEAK-L3 ESCALATION.}}
\]
