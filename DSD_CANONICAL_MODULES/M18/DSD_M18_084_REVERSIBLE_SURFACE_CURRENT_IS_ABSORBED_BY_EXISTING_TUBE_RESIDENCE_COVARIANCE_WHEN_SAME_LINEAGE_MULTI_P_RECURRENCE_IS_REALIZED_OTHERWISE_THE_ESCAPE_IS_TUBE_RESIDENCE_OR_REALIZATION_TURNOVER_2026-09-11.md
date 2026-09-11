# M18-084 — Reversible surface current is absorbed by existing tube-residence covariance when same-lineage multi-p recurrence is realized; otherwise the escape is tube-residence or realization turnover

**Date:** 2026-09-11  
**Status:** CE-H CURRENT / MATERIAL-TUBE RECONNECTION / REVERSIBLE-BRANCH ABSORPTION / REALIZATION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-077--083 isolate a genuinely recurrent surface-current possibility:

\[
\boxed{
G_{cycle}^{rev}:
\bar j=0,
\qquad
\langle|j|\rangle>0.
}
\]

At the local material-surface level, M18-078 gives

\[
D_B\log(\rho A_\Sigma)=\kappa.
\]

M18-082 interprets the corresponding Poisson current energy as a reversible negative-order kinetic action rather than a Lyapunov functional.

Independently, M18-068--070 already develop a same-material-vortex-line residence hierarchy. The present module reconnects these two structures.

The key conclusion is conditional but sharp:

\[
\boxed{
\text{if the reversible current lives on one persistent same-lineage tube with recurrent flux and recurrent multi-p residence,}
}
\]

then it is **not a new endpoint**. It is absorbed into the already existing

\[
\boxed{
G_{strain\text{-}seg}
\lor
G_{diffusive\ sheath/core}.
}
\]

If that same-tube realization or residence recurrence fails, the failure itself is a material-turnover / realization branch.

---

## 2. Local surface flux variable and tube flux variable have the same CE-H law

On one vortex-transverse material surface element define

\[
q_\Sigma:=\rho A_\Sigma.
\]

M18-078 proves

\[
\boxed{
D_B\log q_\Sigma=\kappa.
}
\]

For one material vortex tube, M18-068 uses the absolute tube flux

\[
|\Phi|,
\]

with

\[
\boxed{
D_B\log|\Phi|=\kappa.
}
\]

Thus the local transverse flux-density element and the tube flux carry the same signed coefficient law.

The distinction is geometric scale:

- \(q_\Sigma\) is local patch flux density in a chosen material cross-section coordinate;
- \(|\Phi|\) is the integrated tube flux label.

No identification beyond a controlled same-tube realization is assumed.

---

## 3. Flux recurrence forces zero material mean kappa

Suppose one persistent tube stays nondegenerate:

\[
0<\Phi_-\le|\Phi(\theta)|\le\Phi_+<\infty.
\]

Then

\[
\frac1T
\left[
\log|\Phi(T)|-\log|\Phi(0)|
\right]
\to0.
\]

Since

\[
D_B\log|\Phi|=\kappa,
\]

one obtains

\[
\boxed{
\langle\kappa\rangle_{tube}=0.
}
\]

This is exactly the flux-neutral baseline used in M18-068.

Thus a compact reversible current loop on one genuinely recurrent tube is automatically a zero-mean material-\(\kappa\) loop.

---

## 4. Generalized residence hierarchy

For \(m\ge1\), M18-068 defines

\[
\boxed{
L_m
:=
\int_\Gamma\rho^m ds.
}
\]

The exact material law is

\[
\boxed{
D_B\log L_m
=
m\kappa
+(m+1)\bar\sigma_m
-m+\frac12,
}
\]

where

\[
\bar\sigma_m
:=
\frac{\int_\Gamma\sigma\rho^m ds}{L_m}.
\]

If the same persistent tube has recurrent nondegenerate residence

\[
0<L_{m,-}\le L_m\le L_{m,+}<\infty,
\]

then the mean logarithmic drift vanishes.

Using

\[
\langle\kappa\rangle_{tube}=0,
\]

one gets

\[
\boxed{
\langle\bar\sigma_m\rangle
=
\frac{m-1/2}{m+1}
=
1-\frac{3}{2(m+1)}.
}
\]

For

\[
m=p-1,
\]

this is

\[
\boxed{
\langle\bar\sigma_{p-1}\rangle
=c_p
:=
1-\frac{3}{2p}.
}
\]

---

## 5. Two recurrent residence exponents force same-line amplitude/strain segregation

Take

\[
q>p\ge2.
\]

If both

\[
L_{p-1}
\]

and

\[
L_{q-1}
\]

are recurrent and nondegenerate on the same material tube, M18-068 gives

\[
\boxed{
\left\langle
\bar\sigma_{q-1}-\bar\sigma_{p-1}
\right\rangle
=
\delta_{pq}
:=
\frac32\left(\frac1p-\frac1q\right)>0.
}
\]

Equivalently, with the line probability measure

\[
d\pi_p
=
\frac{\rho^{p-1}ds}{L_{p-1}},
\]

\[
\boxed{
\left\langle
\frac{
\operatorname{Cov}_{\pi_p}
(\sigma,\rho^{q-p})
}{
\mathbb E_{\pi_p}[\rho^{q-p}]
}
\right\rangle
=
\delta_{pq}>0.
}
\]

Thus the same persistent reversible tube cannot have spatially uniform axial strain across its amplitude populations.

Higher-amplitude portions must on average sample larger axial strain.

---

## 6. The global coefficient debt is the same residence reweighting phenomenon

M18-069 gives, under the joint recurrent \(p\)-weighted measure,

\[
\boxed{
\mathbb E_p[\kappa]
=-d_p,
\qquad d_p\ge0.
}
\]

For \(p=2\), on the flux-neutral branch,

\[
\mathbb E_{\Phi}[\kappa]=0
\]

while the enstrophy/residence reweighting gives

\[
\boxed{
\mathbb E_2[\kappa]=-d_2<0
}
\]

on a nontrivial diffusive state.

Therefore

\[
\boxed{
\operatorname{Cov}_{\Phi}(\kappa,L_1)<0.
}
\]

The coefficient has zero mean in flux-time, but the longer/higher-amplitude residence populations preferentially sample more negative \(\kappa\).

This is exactly the distinction that M18-078 required between an unweighted closed material mean and the negative \(\rho^2\)-weighted coefficient debt.

---

## 7. Higher-amplitude reweighting gives the M18-069 dichotomy

For \(q>p\), M18-069 proves

\[
\boxed{
\mathbb E_q[\sigma+\kappa]
-
\mathbb E_p[\sigma+\kappa]
=
\delta_{pq}>0.
}

This splits exactly into

\[
\boxed{
G_{strain\text{-}seg}^{pq}
\lor
G_{diff\text{-}depletion}^{pq}.
}

### Branch A — strain segregation

If diffusion does not decrease enough under higher-amplitude weighting, then

\[
\boxed{
\mathbb E_q[\sigma]-\mathbb E_p[\sigma]
\ge
\frac{\delta_{pq}}2.
}

Thus the reversible same-tube loop carries positive amplitude/strain segregation.

### Branch B — diffusion depletion

Otherwise

\[
\boxed{
 d_q
<
 d_p-rac{\delta_{pq}}2,
}

and the higher-amplitude population carries smaller normalized diffusion.

M18-070 converts this into the quantitative population split

\[
\boxed{
\text{high-amplitude / low-diffusion core}
+
\text{low-amplitude / high-diffusion sheath}.
}

Thus a same-tube reversible current loop is already inside the existing CE-H population architecture.

---

## 8. What M18-084 actually absorbs

Suppose all of the following hold on a recurrent controlled component:

1. one persistent same-lineage vortex tube is realized through the current events;
2. its absolute flux remains bounded above and away from zero;
3. for two exponents \(q>p\ge2\), both generalized residence factors
   \[
   L_{p-1},\ L_{q-1}
   \]
   remain bounded above and away from zero recurrently;
4. the material labels do not turn over or switch to another lineage.

Then

\[
\boxed{
G_{cycle}^{rev}
\Longrightarrow
G_{strain\text{-}seg}^{pq}
\lor
G_{diffusive\ sheath/core}^{pq}.
}

Hence there is no independent `fixed-metric reversible-current` endpoint under this same-tube multi-residence recurrence package.

---

## 9. Realization firewall

The preceding implication is **not** automatic for an arbitrary finite-lineage graph cycle.

M18-077's graph current may be assembled from transfers occurring

- on different material tubes;
- on different Frobenius patches;
- at different recurrent phases;
- after replacement or relabeling;
- without one pair of generalized residence factors remaining recurrent on the same lineage.

Therefore

\[
\boxed{
G_{cycle}^{rev}
\not\Rightarrow
G_{same\text{-}tube\ residence}
}

without an additional realization theorem.

This is the central firewall of the present module.

---

## 10. Exact complementary split

A recurrent reversible-current branch therefore has the following exhaustive audit split:

\[
\boxed{
G_{cycle}^{rev}
\Longrightarrow
\begin{cases}
G_{same\text{-}tube\ multi\text{-}p\ recurrence},\\
G_{tube\ residence\ loss},\\
G_{tube/lineage\ replacement},\\
G_{surface/label\ realization\ loss}.
\end{cases}
}

On the first branch,

\[
\boxed{
G_{same\text{-}tube\ multi\text{-}p\ recurrence}
\Longrightarrow
G_{strain\text{-}seg}
\lor
G_{diffusive\ sheath/core}.
}

The other three branches are already material/genealogical turnover or realization exits, not quiet current breathers.

---

## 11. Residence loss is not silently called a contradiction

If one generalized residence factor satisfies

\[
L_m\to0
\quad\text{or}\quad
L_m\to\infty
\]

along the recurrent event sequence, this is not by itself impossible.

It means that the tube's amplitude-weighted arclength leaves the compact recurrence class for that exponent.

Such a branch must be routed quantitatively into one of

\[
\boxed{
\text{amplitude concentration/depletion},
\quad
\text{line stretching/compression},
\quad
\text{material export},
\quad
\text{label replacement}.
}

The present module only classifies the loss; it does not close it.

---

## 12. Relation to the sheath current chain M18-070--076

The absorption is structurally circular in a useful sense, not logically circular.

M18-070 derives a lower-amplitude high-diffusion sheath.

M18-071--076 show that a controlled CE-H sheath carries a nontrivial material surface current and then unavoidable material-label redistribution.

M18-077--083 audit what recurrent redistribution can do.

M18-084 now proves that if this redistribution returns to one persistent same-lineage multi-residence tube, it feeds back into the original strain-segregation / sheath-core architecture.

Therefore the controlled same-tube branch forms a **closed recurrent structural loop**:

\[
\boxed{
\text{multi-p covariance}
\to
\text{diffusive sheath}
\to
\text{material current}
\to
\text{redistribution}
\to
\text{same-tube recurrence}
\to
\text{multi-p covariance}.
}
\]

This is a classification closure, not a contradiction.

---

## 13. Important consequence: the remaining novelty is realization, not another local payer

Once same-tube recurrence is certified, all local current activity returns to already known amplitude/strain/diffusion structure.

Therefore further local unsigned-payer extraction is unlikely to add a new independent constraint.

The genuinely new question is now whether recurrent lineage redistribution can **avoid** same-tube multi-p recurrence indefinitely by switching tubes, phases, patches, or residence classes while the persistent lineage family remains finite.

This is a finite-state realization/genealogy question.

---

## 14. New frontier after M18-084

The CE-H current route can now be written

\[
\boxed{
\text{mandatory current}
\Longrightarrow
\begin{cases}
G_{self\text{-}helicity/twist},\\
G_{surface/label\ geometry\ loss},\\
G_{mean\ lineage\ cycle},\\
G_{same\text{-}tube\ covariance\ loop},\\
G_{tube/residence/realization\ turnover}.
\end{cases}
}

The same-tube covariance loop is internally classified by existing M18-068--070 machinery.

The unresolved current novelty is concentrated in

\[
\boxed{
G_{mean\ lineage\ cycle}
\lor
G_{tube/residence/realization\ turnover}
\lor
G_{self\text{-}helicity/twist}
\lor
G_{surface\ geometry\ loss}.
}

---

## 15. Highest-value next target

Because the persistent lineage graph is finite, the next target is a **finite-state recurrence/pigeonhole theorem with residence labels**.

The question is:

\[
\boxed{
\text{Can recurrent redistribution among finitely many persistent lineages avoid recurrent same-tube multi-p residence forever without paying replacement/export/geometry loss?}
}

A useful formulation is to enrich each lineage vertex with a finite/coarse residence-state label, for example whether

\[
L_{p-1},\ L_{q-1}
\]

lie inside fixed compact intervals.

If the compact residence classes recur with positive density, a fixed decorated lineage state must recur and M18-084 applies.

If not, some residence variable decompactifies, providing a typed amplitude/line-stretching/material-export branch.

---

## 16. Audit verdict

### Certified

1. Local CE-H cross-section flux and tube flux obey the same signed law \(D_B\log flux=\kappa\).
2. Persistent nondegenerate same-tube flux recurrence forces \(\langle\kappa\rangle_{tube}=0\).
3. Recurrence of two generalized residence moments on the same tube forces the exact multi-p axial-strain separation of M18-068.
4. The negative spatial/amplitude-weighted \(\kappa\) debt is a residence-reweighting effect and is compatible with zero unweighted material mean \(\kappa\).
5. A same-tube multi-p recurrent reversible current is absorbed into the existing strain-segregation or diffusive sheath/core dichotomy.
6. An arbitrary lineage-graph reversible cycle need not be realized by one recurrent tube; this remains a separate realization bridge.
7. The remaining new difficulty is finite-lineage residence realization/turnover, not another local current payer.

### Still open

- finite-state residence recurrence theorem;
- mean conservative lineage circulation;
- residence decompactification routing;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 17. Next target

M18-085 should decorate the finite persistent-lineage graph with two generalized residence coordinates and prove the exact compactness split:

\[
\boxed{
\text{finite decorated-state recurrence}
\lor
\text{residence decompactification}.
}

Then determine whether finite decorated-state recurrence is enough to force one fixed same-lineage tube to satisfy the M18-084 hypotheses on a positive-density event subsequence.
