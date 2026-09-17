# DSD M19-370 — Critical-seed and zero-kappa sheath renewal share the same 3/2 similarity-volume exponent, so turnover costs are not automatically additive

Date: 2026-09-17  
Canonical ID: **M19-370**

Status: **ACTIVE COUPLED-RENEWAL SCALING / COMMON-EXPONENT FIREWALL / TURNOVER NONADDITIVITY**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Critical seed area law

M19-366 shows that at the critical seed lock

\[
(\kappa,\sigma)=\left(\frac32,-\frac12\right),
\]

one has

\[
D_B\log A_{seed}=\frac32,
\]

while amplitude, curvature and longitudinal line length are neutral in the ideal locked model.

Thus a dormant seed cross-section grows as

\[
\boxed{A_{seed}(\theta)=A_{seed}(\theta_0)e^{3(\theta-\theta_0)/2}.}
\]

Equivalently, in remaining-time coordinate \(s\),

\[
A_{seed}(s)=A_*e^{-3s/2}.
\]

## 2. Zero-kappa sheath law

M5-638 gives on the relabeling zero-kappa persistent surface

\[
D_B\log dA_0=1-\sigma_n,
\]

and neighboring-level normal spacing

\[
D_B\log d_\perp=\sigma_n+\frac12.
\]

Therefore the positive-thickness sheath volume element obeys exactly

\[
\boxed{
D_B\log(dA_0d_\perp)=\frac32.
}
\]

The normal strain cancels.

## 3. Common renewal exponent

Hence both mechanisms are driven by the same universal similarity-volume exponent:

\[
\boxed{
\gamma_{seed}^{area}
=\gamma_{sheath}^{volume}
=\frac32.
}
\]

This equality is not accidental. Both are manifestations of

\[
\nabla\cdot B=\frac32
\]

after the relevant lower-dimensional material object is separated from its positive-volume neighborhood.

## 4. Coupled-throughflow witness

A consistent scaling picture can therefore use one material through-flow as follows:

1. exponentially thin/low-volume incoming labels approach the active core;
2. their transverse area or local sheath volume expands at rate \(3/2\);
3. they temporarily supply active seed/sheath structure;
4. expansion ejects or decompactifies the old positive-volume labels;
5. the lower-dimensional persistent flux/kappa skeleton remains while new labels replace the sheath.

Nothing in the present exact transport laws requires the seed-renewal event and sheath-renewal event to consume disjoint material resources.

## 5. Nonadditivity firewall

Therefore the inference

\[
\text{positive seed turnover rate}
+
\text{positive sheath turnover rate}
\Longrightarrow
\text{twice the finite-memory cost}
\]

is not certified.

The two rates may be projections of the same underlying label-throughflow process.

Symbolically,

\[
\boxed{
T_{seed}^{+density}+T_{sheath}^{+density}
\not\Rightarrow
2T_{resource}^{+density}
}

without a nonreuse/disjointness theorem.

This is the renewal analogue of the earlier unsigned-payer nonreuse firewall.

## 6. Stronger interpretation of M19-369

M19-369's three-stream architecture remains valid as a functional decomposition:

\[
\text{critical seed}
+
\text{persistent spine}
+
\text{renewing sheath}.
\]

M19-370 corrects its resource interpretation: the critical-seed stream and renewing-sheath stream need not correspond to two independent positive-volume material reservoirs.

They may be successive roles of one common through-flow of labels around a persistent lower-dimensional skeleton.

## 7. What would make the two renewals genuinely additive

A true additive lower bound would require at least one of:

\[
\boxed{
\begin{aligned}
&\text{material-label disjointness/nonreuse between seed and sheath events},\\
&\text{a minimum positive dormant thickness preventing exponential seed packing},\\
&\text{a topological crossing cost between incoming and outgoing kappa levels},\\
&\text{a signed/projective resource with one-way consumption},\\
&\text{a finite-capacity transversal that each renewal crosses with nonrecyclable orientation}.
\end{aligned}
}
\]

Without such an input, the common \(3/2\) exponent makes a stationary conveyor scaling-compatible.

## 8. Relation to finite-memory storage

M5-488/M19-359 treat finite-memory storage and projective discharge. M19-370 says that future use of that machinery must count **actual nonreused transversal/discharge events**, not separately count every semantic role change as a new event.

Thus the next theorem gate is event identification, not another local rate estimate.

## 9. New target

Define

\[
\boxed{
\mathcal T_{event}^{renew}:
\text{identify a canonical material/projective crossing event that every complete seed-to-sheath renewal cycle must execute exactly once up to bounded multiplicity.}
}
\]

If such an event carries a signed nonrecyclable finite-memory charge, the common-conveyor survivor may close. If not, the age-structured stationary witness remains viable at the scaling level.

## 10. Audit verdict

**PASS-NO-GO — the two positive-density turnover requirements cannot presently be added as independent costs.**

Critical-seed transverse inflation and zero-kappa sheath expansion are governed by the same universal \(3/2\) similarity-volume exponent and may be two faces of one material through-flow conveyor. A nonreuse or one-way crossing theorem is required before renewal density becomes a contradiction.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
