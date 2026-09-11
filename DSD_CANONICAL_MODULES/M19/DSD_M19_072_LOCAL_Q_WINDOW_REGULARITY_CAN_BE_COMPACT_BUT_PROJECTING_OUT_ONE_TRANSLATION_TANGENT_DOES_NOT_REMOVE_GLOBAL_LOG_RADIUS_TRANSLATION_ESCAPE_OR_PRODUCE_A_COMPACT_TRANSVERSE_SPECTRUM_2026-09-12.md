# M19-072 — Local q-window regularity can be compact, but projecting out one translation tangent does not remove global log-radius translation escape or produce a compact transverse spectrum

**Date:** 2026-09-12  
**Status:** CALCULATION / SCATTERING TOPOLOGY / TRANSVERSE-COMPACTNESS FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-071 showed that the bulk weighted two-volume estimate does not automatically control the second center exponent.  A possible alternative is that the **scattering space itself** has stronger compactness after the one exact translation tangent is removed.

This module separates local and global behavior in the log-radius variable \(q\).

On every fixed finite \(q\)-window, sufficiently strong derivative bounds can indeed give compactness by Rellich.  Globally, however, the translation action

\[
(T_sB)(q,\omega)=B(q+s,\omega)
\]

produces the standard loss of compactness on \(\mathbb R_q\).  Removing one tangent direction \(\partial_qA\) is only a codimension-one operation and does not remove translated perturbations escaping to infinity in \(q\).

Thus a compact-resolvent/simple-center theorem cannot be obtained merely by projecting out the phase tangent in a translation-invariant global scattering norm.

## 2. Local scattering regularity

Suppose a family of scattering perturbations \(B\) is uniformly bounded in a strong local norm, schematically

\[
\boxed{
\|B\|_{H^s([-L,L]\times S^2)}\le C_L,
\qquad s>0,
}
\]

for each finite \(L\).

Then, for example when \(s>0\) is large enough for the desired target topology, Rellich compactness gives

\[
H^s([-L,L]\times S^2)
\Subset
L^2([-L,L]\times S^2).
\]

Therefore

\[
\boxed{
\text{fixed-window scattering profiles can be precompact.}
}
\]

This is consistent with the compact local similarity hull used throughout the repository.

## 3. Global translation is the missing compactness

Let \(B_0(q,\omega)\) be a nonzero smooth perturbation supported in a bounded \(q\)-interval.  Define

\[
\boxed{
B_n(q,\omega)
:=B_0(q-n,\omega).
}
\]

In every translation-invariant global Sobolev norm,

\[
\boxed{
\|B_n\|_{H^s(\mathbb R\times S^2)}
=\|B_0\|_{H^s}.
}
\]

But for \(|n-m|\) larger than the support width,

\[
\langle B_n,B_m\rangle=0
\]

in \(L^2\), so

\[
\boxed{
\|B_n-B_m\|_2^2
=2\|B_0\|_2^2.
}
\]

Hence \(\{B_n\}\) has no strongly convergent global subsequence.

At the same time, for each fixed finite window,

\[
B_n\to0
\]

locally as \(n\to+\infty\).

This is the exact concentration-compactness pattern of **translation escape** in log radius.

## 4. Removing one tangent does not repair global compactness

Let \(Z_A\) denote one fixed normalized phase tangent, formally proportional to

\[
\partial_qA.
\]

In a global Hilbert scattering space in which \(Z_A\) is square integrable, define

\[
\Pi_A^\perp B
:=
B-\langle B,Z_A\rangle Z_A.
\]

For the translated sequence \(B_n=T_{-n}B_0\), weak translation implies

\[
\langle B_n,Z_A\rangle\to0
\]

whenever \(B_0,Z_A\) lie in the usual translation-invariant \(L^2\)-based space.

Therefore

\[
\boxed{
\|\Pi_A^\perp B_n-B_n\|\to0.
}
\]

The projected sequence inherits the same noncompactness:

\[
\boxed{
\{\Pi_A^\perp B_n\}
\text{ has no strongly convergent global subsequence.}
}
\]

Thus quotienting by one tangent direction does not remove the translation defect.

## 5. The same conclusion in a local-hull topology

The actual recurrent scattering datum need not belong to global \(L^2_q\); indeed the surviving weak-critical branch is generally nonintegrable in unweighted \(q\).

In the natural local topology, the conclusion is even more direct:

\[
T_{-n}B_0\to0
\quad\text{on every fixed compact }q\text{-window},
\]

while the perturbation remains nontrivial in its moving window.

A local topology therefore cannot distinguish disappearance by translation from genuine decay.

This is precisely why local hull compactness does not produce global scattering rigidity.

## 6. Finite-codimensional quotient is still insufficient

The argument is not special to one tangent direction.

Let \(F\) be any fixed finite-dimensional subspace of a translation-invariant global Hilbert scattering space.  Orthogonal projection onto \(F^\perp\) changes \(B_n\) by a quantity tending to zero as \(|n|\to\infty\), because each fixed basis vector has vanishing correlation with a translated compact packet.

Hence

\[
\boxed{
\text{no fixed finite-codimensional quotient removes global }q\text{-translation noncompactness.}
}
\]

Therefore even proving a finite number of neutral directions does not by itself create compact resolvent structure on the full line.

## 7. Weighted q-spaces change the problem rather than solve it

One may use a non-translation-invariant weight in \(q\), such as the exponential factor naturally appearing in finite enstrophy.

This can compactify one direction of translation, but then

\[
\|T_sB\|_{weighted}
\]

changes exponentially with \(s\).

Such a norm is not invariant under the scattering dynamics

\[
A(q)\mapsto A(q-t/2).
\]

It therefore cannot by itself define a recurrent isometric/compact center spectrum without reintroducing time-dependent renormalization.

The old finite-enstrophy weight

\[
e^{-q}
\]

is exactly why a nondecaying recurrent tail can have finite energy: it discounts remote log-radius phases rather than identifying them.

Thus

\[
\boxed{
\text{weighted compactness}\neq\text{translation rigidity}.
}

## 8. Consequence for the center-cocycle program

M19-067--071 sought a simple-center plus transverse-gap theorem.  M19-072 shows that even after one tangent is removed, the natural global scattering space retains an infinite translation-escape mechanism.

Therefore any compact-resolvent version of the center theorem must use more than local regularity or finite-dimensional phase projection.

It must somehow identify or penalize **all remote translated copies** of a perturbation through the interior PDE/genealogy.

Equivalently, the missing theorem is global in \(q\):

\[
\boxed{
\text{transverse realizability must fail uniformly across all translated log-radius windows.}
}
\]

## 9. Relation to M19-069

M19-069 showed that outward spectator propagation is near identity in a strong norm and therefore does not smooth away boundary degrees of freedom.

M19-072 complements that result:

- the tail map is not smoothing;
- local scattering regularity is not globally compact;
- phase projection does not remove translated packets.

Hence the last compactness defect is already present at the finite spectator-boundary history level and is carried essentially unchanged to infinity.

## 10. Certified / not certified

### Certified

1. Fixed \(q\)-window strong regularity can give local compactness.
2. Global translations of one fixed perturbation produce a noncompact sequence in translation-invariant scattering norms.
3. Projecting out one phase tangent does not remove that sequence.
4. More generally, no fixed finite-codimensional quotient removes translation escape.
5. Non-translation-invariant weights compactify only by changing the scattering dynamics and do not directly give rigidity.

### Not certified

1. Impossibility of every infinite-dimensional quotient/renormalized topology.
2. Interior PDE exclusion of translated boundary packets.
3. Simple center of the true recurrent NS cocycle.
4. Global weak-critical scattering rigidity.
5. Global 3D Navier--Stokes regularity.

## 11. Next target

The remaining translation defect is now visibly a **genealogical observability problem**: a packet translated by \(n\) in \(q\) corresponds to the same fixed spectator radius observed at a historical time shifted by \(2n\).

M19-073 should therefore convert the sequence

\[
B_n(q)=B_0(q-n)
\]

back into finite-radius boundary times and ask whether infinitely many mutually separated historical boundary packets can be realized without paying a nonreusable physical-time budget.

This reconnects the final scattering-center problem with the earlier ancestry/genealogy machinery, but now at one fixed spectator radius where the spatial scale no longer changes.  If a fixed-radius time history has a genuine finite variation or finite dissipation budget, translation escape may be eliminated without the old ancestry scaling penalty.

---

\[
\boxed{\text{M19-072 COMPLETE; LOCAL COMPACTNESS PLUS FINITE-DIMENSIONAL PHASE QUOTIENT DOES NOT REMOVE GLOBAL LOG-RADIUS TRANSLATION ESCAPE.}}
\]
