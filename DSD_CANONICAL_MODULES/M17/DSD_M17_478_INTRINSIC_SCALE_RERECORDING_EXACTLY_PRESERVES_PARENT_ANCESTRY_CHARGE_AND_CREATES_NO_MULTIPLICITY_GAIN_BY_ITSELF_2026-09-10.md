# M17-478 — Intrinsic-scale re-recording exactly preserves parent ancestry charge and creates no multiplicity gain by itself

**Date:** 2026-09-10  
**Status:** ACTIVE SCALE-COMPOSITION FIREWALL / INTRINSIC-RECORD ANCESTRY INVARIANCE

## 1. Purpose

M17-477 showed that if endpoint temporal thickening is to defeat the cubic raw-\(H^2\) ancestry weight through spike-height growth alone, then under bounded enstrophy the normalized coefficient amplitude must decompactify. M17-393 requires such a large coefficient to be interpreted through its smaller intrinsic coefficient scale rather than as an independent scalar spike.

The immediate question is therefore:

> Does re-recording the same event at its intrinsic coefficient scale improve the parent ancestry charge?

The answer is exactly no. Homogeneous Navier--Stokes scaling makes the normalized resource charge and the ancestry weight cancel perfectly.

## 2. Scaling operator and composition

Define the vorticity scaling operator
\[
(S_R\Omega)(y,s)
:=
R^2\Omega(Ry,R^2s).
\]
Then
\[
\boxed{S_rS_R=S_{Rr}.}
\]

On exact CE-H,
\[
\Delta\Omega=\kappa\Omega,
\]
and the coefficient transforms as
\[
(S_R\kappa)(y,s)=R^2\kappa(Ry,R^2s).
\]
Thus if a normalized record has coefficient magnitude \(K\gg1\), choosing
\[
r=K^{-1/2}
\]
renormalizes that coefficient magnitude to order one.

The effective composed ancestry scale is then
\[
\widehat R=Rr.
\]
No interpretation of whether \(\widehat R\) is larger or smaller than another physical scale is needed for the algebra below; only the exact composition law is used.

## 3. Raw-H2 spacetime scaling

Let
\[
H[\Omega](s):=\|\Delta\Omega(s)\|_2^2.
\]
Under \(S_r\),
\[
\Delta(S_r\Omega)=r^4(\Delta\Omega)(r\cdot,r^2s),
\]
so in three dimensions
\[
H[S_r\Omega](s)
=
r^5H[\Omega](r^2s).
\]
Therefore for corresponding time windows,
\[
q_H[\Omega]
:=
\int H[\Omega](s)ds
\]
satisfies
\[
\boxed{q_H[S_r\Omega]=r^3q_H[\Omega].}
\]

This is the same cubic spacetime scaling used in M17-403/405/467.

## 4. Exact parent-charge invariance

Suppose a record at ancestry factor \(R\) carries normalized raw-\(H^2\) spacetime charge \(q_H\). Its parent-accounted charge is
\[
\mathcal A_H(R,q_H):=R^{-3}q_H.
\]

Re-record the same event by the additional factor \(r\). The new normalized charge is
\[
q_H'=r^3q_H
\]
and the effective ancestry factor is
\[
R'=Rr.
\]
Hence
\[
\boxed{
\mathcal A_H(R',q_H')
=(Rr)^{-3}(r^3q_H)
=R^{-3}q_H
=\mathcal A_H(R,q_H).
}
\]

Therefore
\[
\boxed{
\text{raw-H2 parent ancestry charge is exactly invariant under canonical intrinsic-scale re-recording.}
}
\]

This is an equality, not merely an estimate.

## 5. Palinstrophy invariance

Let
\[
P[\Omega](s):=\|\nabla\Omega(s)\|_2^2.
\]
Under \(S_r\),
\[
P[S_r\Omega](s)=r^3P[\Omega](r^2s),
\]
so the spacetime palinstrophy charge
\[
q_P:=\int Pds
\]
obeys
\[
\boxed{q_P[S_r\Omega]=r q_P[\Omega].}
\]

The M17-307 parent accounting uses \(R^{-1}\). Hence
\[
\boxed{
(Rr)^{-1}(r q_P)=R^{-1}q_P.
}
\]

Thus palinstrophy parent charge is also exactly invariant under re-recording.

## 6. Higher-vorticity resource

M17-444 gives the spacetime \(D^3\Omega\) resource with ancestry exponent five. Homogeneity gives
\[
q_{D^3}[S_r\Omega]=r^5q_{D^3}[\Omega],
\]
while parent accounting uses \(R^{-5}\). Therefore
\[
\boxed{
(Rr)^{-5}q_{D^3}[S_r\Omega]
=R^{-5}q_{D^3}[\Omega].
}
\]

The same cancellation is a general feature of a correctly matched homogeneous resource and its exact ancestry exponent.

## 7. General homogeneous ledger principle

If a normalized spacetime resource \(q_\alpha\) has scaling
\[
q_\alpha[S_r\Omega]=r^\alpha q_\alpha[\Omega]
\]
and its certified parent ledger carries weight \(R^{-\alpha}\), then
\[
\boxed{
(Rr)^{-\alpha}q_\alpha[S_r\Omega]
=R^{-\alpha}q_\alpha[\Omega].
}
\]

Therefore canonical scale refinement of the **same physical/genealogical event** cannot improve or worsen the parent-accounted homogeneous charge.

This is the correct anti-double-counting principle for intrinsic-scale migration.

## 8. Consequence for M17-477

M17-477 routed endpoint spike growth to large normalized \(\|\kappa\|_\infty\), hence to smaller intrinsic coefficient scale.

M17-478 now shows that if this is merely a one-to-one re-recording of the same event,
\[
\boxed{
G_{\kappa\text{-scale migration}}
\not\Rightarrow
\text{ancestry gain}.
}
\]

The apparent improvement obtained by making the coefficient order one at the new scale is exactly offset by the changed ancestry factor.

Thus coefficient decompactification can help only if it supplies something beyond pure rescaling, such as:

- several genuinely distinct non-reused intrinsic-scale packets;
- nontrivial residence/multiplicity at the new scale;
- loss of one-to-one genealogical identification;
- interface or domain structure creating independent resource support.

## 9. No multiplicity from nested relabeling

Consider a nested chain of descriptions of one event,
\[
(R,q)
\to
(Rr_1,r_1^\alpha q)
\to
(Rr_1r_2,(r_1r_2)^\alpha q)
\to\cdots.
\]
Each representation has the same parent charge
\[
R^{-\alpha}q.
\]

Summing all of these representations as though they were independent events would therefore double-count the same ancestral resource.

Hence
\[
\boxed{
\text{nested intrinsic-scale relabelings do not constitute the M17-473 multiplicity required for contradiction.}
}
\]

A multiplicity theorem must prove disjointness, bounded overlap, distinct material labels, distinct time support, or another certified non-reuse criterion.

## 10. Relation to coefficient bins

This firewall is consistent with M17-381/386. Coefficient bins may decompose a snapshot/spacetime raw-\(H^2\) measure into disjoint pieces,
\[
\sum_jH_j=H_{\rm raw},
\]
but changing the normalization scale of one piece does not create new measure.

Therefore coefficient-scale decomposition and intrinsic-scale re-recording are both ownership tools, not resource generators.

## 11. Updated migration split

The large-coefficient branch is now refined to
\[
\boxed{
\begin{aligned}
G_{\kappa_\infty\text{-decompactification}}
\Longrightarrow{}&
G_{\rm pure\ intrinsic\ rerecording}^{\rm no\ ancestry\ gain}\\
&\lor G_{\rm distinct\ nonreuse\ multiplicity/residence}\\
&\lor G_{\nabla\kappa/high\text{-}jet/interface}\\
&\lor G_{\rm genealogy/scale\text{-}map/domain\ loss}.
\end{aligned}
}
\]

The first branch is now closed as a possible ancestry-escape mechanism.

## 12. Audit cautions

- The invariance applies to one-to-one canonical re-recording of the same event. It does not identify two events as the same without a genealogy map.
- The relevant time windows must be mapped by the exact parabolic scaling.
- Localized cutoff resources can carry additional boundary terms; only the homogeneous bulk resource itself enjoys the exact identity stated here.
- This does not close coefficient-gradient/high-jet or interface exits.
- A family of genuinely disjoint subscale packets may create real multiplicity; M17-478 only prevents counting nested representations of one packet repeatedly.

## 13. Audit status

Closed here:

- pure intrinsic coefficient-scale re-recording as a mechanism for defeating the raw-\(H^2\), palinstrophy, or homogeneous higher-vorticity ancestry firewall;
- nested scale relabeling as fake multiplicity.

Still OPEN:

- a certified non-reuse theorem for genuinely distinct intrinsic-scale packets;
- residence/multiplicity strong enough to meet M17-473;
- coefficient-gradient/high-jet/interface branches;
- genealogy/scale-map persistence;
- ROOT-CERT and non-CE-H roots.

## 14. Next target

The only potentially useful scale-migration route left is **genuine multiplicity** rather than re-normalization. The next audit should formulate a representation-safe criterion distinguishing nested relabelings from genuinely distinct intrinsic-scale events and compare the maximum possible non-reused multiplicity with the cubic/raw-H2 and linear/palinstrophy thresholds of M17-473.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
