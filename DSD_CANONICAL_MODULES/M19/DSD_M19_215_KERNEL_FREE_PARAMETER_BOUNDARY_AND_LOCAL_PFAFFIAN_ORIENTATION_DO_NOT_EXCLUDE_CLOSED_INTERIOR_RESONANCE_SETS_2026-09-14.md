# M19-215 — Kernel-free parameter boundary and local Pfaffian orientation do not exclude closed interior resonance sets

**Date:** 2026-09-14  
**Status:** ACTIVE AUDIT / GLOBAL-TOPOLOGY NO-GO + NEXT-TARGET REFINEMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Question after M19-213--214

M19-213 supplies a signed local Cayley–Pfaffian coordinate for \(+1\) crossings, and M19-214 rewrites RDSS kernel rigidity as the phase-gap condition

\[
\operatorname{dist}(\kappa_jL-m_j\alpha,2\pi\mathbb Z)>0.
\]

A natural next hope would be to combine known kernel-free/excluded parameter boundary regimes with topological continuation and conclude that no interior unit resonance exists.

That implication is false without an additional global monotonicity or sign theorem.

## 2. One-parameter endpoint data are insufficient

Consider the exact two-dimensional orthogonal model

\[
P(\lambda)=R(\Theta(\lambda)),
\qquad \lambda\in[0,1],
\]

with

\[
\Theta(\lambda)
=\varepsilon
\left(\lambda-\frac13\right)
\left(\lambda-\frac23\right),
\qquad 0<\varepsilon<\pi.
\]

Then

\[
\Theta(0)>0,
\qquad
\Theta(1)>0,
\]

so both endpoints are kernel-free and lie in the same \(-1\)-free Cayley chart with the same Pfaffian sign.

Nevertheless

\[
\Theta\left(\frac13\right)
=\Theta\left(\frac23\right)=0,
\]

so there are two interior \(+1\) kernel crossings.

Thus

\[
\boxed{
\text{kernel-free endpoints + same Pfaffian sign}
\not\Longrightarrow
\text{kernel-free interval}.
}
\]

Endpoint continuation controls only crossing parity/sign data, not the absence of paired interior crossings.

## 3. Multiparameter boundary data are even weaker

Let the parameter domain be the closed disk

\[
D=\{(x,y):x^2+y^2\le1\},
\]

and define

\[
P(x,y)=R(\Theta(x,y)),
\]

with

\[
\Theta(x,y)
=\varepsilon(x^2+y^2-r_0^2),
\qquad 0<r_0<1,
\qquad 0<\varepsilon<\pi.
\]

On the boundary \(x^2+y^2=1\),

\[
\Theta=\varepsilon(1-r_0^2)>0,
\]

so the entire parameter boundary is kernel-free and lies in one Cayley chart.

But on the interior circle

\[
x^2+y^2=r_0^2,
\]

we have

\[
\Theta=0,
\qquad
P=I.
\]

Hence the unit-kernel set is a closed interior resonance curve completely invisible to kernel-free boundary data.

Therefore

\[
\boxed{
\text{kernel-free parameter boundary}
\not\Longrightarrow
\text{kernel-free parameter interior}.
}
\]

This remains true even without any \(-1\) crossing.

## 4. Interpretation for the moderate RSS/RDSS compact set

M19-206 records that external Liouville theorems remove several parameter-boundary regimes and leave a compact moderate corridor.

Those boundary exclusions are essential for compactification, but they cannot by themselves establish the interior Fredholm theorem.

A nonsymmetry resonance locus

\[
\kappa_jL-m_j\alpha=2\pi n
\]

may form an interior curve/surface or a collection of paired crossings while every accessible boundary regime remains kernel-free.

Thus the following inference is permanently disallowed:

\[
\boxed{
\text{external boundary Liouville rigidity}
+\text{continuity}
\not\Longrightarrow
\text{interior kernel rigidity}.
}
\]

## 5. What a global topological route would actually need

The Cayley–Pfaffian coordinate can contribute to a proof only after an additional mechanism forbids hidden interior zero sets. Sufficient types of extra information would include:

### A. Global one-sided phase trapping

For every nonsymmetry channel,

\[
\Theta_j(\mathcal K)
\subset I_j
\]

for an interval \(I_j\) that avoids \(2\pi\mathbb Z\).

This directly gives the M19-214 phase gap.

### B. Monotonicity plus boundary phase ordering

Along every admissible one-dimensional continuation branch,

\[
\partial_\lambda\Theta_j
\]

has a certified fixed sign and the endpoint phase range stays in one resonance-free interval.

Transversality alone is insufficient; the direction and total phase range must be controlled.

### C. A signed PDE invariant

A quantity with a fixed nonzero sign whose zero set is exactly the unit-resonance set, together with a theorem that it cannot form a closed interior zero hypersurface.

The local Pfaffian alone does not provide the latter theorem.

### D. Direct kernel contradiction

A profile-specific identity may bypass parameter topology altogether by showing that any fixed vector of \(P_{rel}\) violates a Navier--Stokes PDE constraint.

## 6. Relation to spectral topology

The present no-go is stronger than the determinant-sign failure of M19-211.

M19-211 showed that \(\det(I-P)\) is locally blind because it squares the crossing. M19-213 repairs that local blindness using the Pfaffian.

M19-215 shows that even a locally signed crossing detector does **not** give global nonexistence from boundary data alone.

Therefore the remaining obstruction is not merely choosing the correct matrix invariant. It is obtaining a **global PDE control on the resonance phase or zero set**.

## 7. Revised theorem frontier

The bounded-period theorem is now most sharply stated as follows:

\[
\boxed{
\mathcal T_{phase}^{moderate}:
\exists\,\delta_*>0
\text{ such that }
\operatorname{dist}(\kappa_jL-m_j\alpha,2\pi\mathbb Z)
\ge\delta_*
}
\]

for every admissible moderate RSS/RDSS profile and every nonsymmetry hard channel.

Boundary compactification, local crossing transversality, determinant sign, and the local Pfaffian do not prove this theorem by themselves.

## 8. Next calculation

The next calculation should therefore target the q-frequency \(\kappa_j\) itself: derive a representation or estimate tying \(\kappa_j\) to a certified PDE/scattering quantity strongly enough to control the phase

\[
\kappa_jL-m_j\alpha.
\]

In particular, the useful question is no longer whether a kernel crossing is generic, but whether the Navier--Stokes hard scattering generator permits a resonance phase equal to an integer multiple of \(2\pi\) at all inside the retained moderate corridor.

The bounded-period branch remains OPEN.