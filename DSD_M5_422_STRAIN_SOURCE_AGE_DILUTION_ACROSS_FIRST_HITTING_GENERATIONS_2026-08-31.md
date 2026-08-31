# DSD M5-422 — Strain-source age dilution across geometric first-hitting generations

Date: 2026-08-31

Status: **M5-396 CORRECTLY SHOWS THAT SCALE-INVARIANT VORTICITY FLUX ITSELF HAS NO AGE DILUTION, BUT M5-421 IMPLIES A DIFFERENT AND CRUCIAL FACT: THE ABILITY OF AN OLD SOURCE TO SUPPLY A FIXED FRACTION OF THE NATURAL STRAIN OF A GEOMETRICALLY SHRINKING FIRST-HITTING TARGET DOES AGE-DILUTE / IF THE OLD SOURCE SCALE AND DISTANCE DO NOT CO-SHRINK WITH THE TARGET, ITS NORMALIZED COUPLING DECAYS LIKE `q^-k` AFTER `k` GENERATIONS / MAINTAINING FIXED COUPLING THEN REQUIRES THE SOURCE CRITICAL NORM TO GROW LIKE `q^k` AND ITS SQUARED CRITICAL MASS LIKE `q^(2k)` / THUS LONG-TIME SOURCE REUSE FORCES EITHER CO-SHRINKING MATERIAL SOURCE LINEAGE, FRESH SOURCE HANDOFF, OR EXPONENTIAL CRITICAL-MASS ESCALATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-396 established an important anti-proof firewall:

\[
\Phi_j\asymp\nu
\]

for a natural flux carrier at every generation, so an old carrier does not become negligible merely because its age increases.

That statement concerns **flux amount**.

The present note concerns a different observable:

> how efficiently can the old carrier/shell generate the natural strain required by a later, smaller first-hitting target?

M5-421 shows that this coupling has a quadratic separation penalty. Because target scales shrink geometrically, old-source strain efficiency has a genuine age dilution even though flux does not.

---

## 2. Geometric first-hitting target scales

Let consecutive first-hitting vorticity levels satisfy

\[
W_{j+1}=qW_j,
\qquad q>1.
\]

The natural scale is

\[
s_j=\sqrt{\frac{\nu}{W_j}}.
\]

Hence after `k` generations,

\[
\boxed{
s_{j+k}=q^{-k/2}s_j.
}
\]

The natural target strain grows as

\[
\boxed{
S_{nat,j+k}
\asymp
\frac{\nu}{s_{j+k}^2}
=q^k\frac{\nu}{s_j^2}.
}
\]

---

## 3. An old source descriptor

Take a source carrier or diffuse source shell already present near generation `j`.

Let its physical source scale and distance from the later target be

\[
R_k,
\qquad
D_k.
\]

For the diffuse critical-shell statement it is enough to retain one characteristic source radius

\[
\mathcal R_k\asymp\max\{R_k,D_k\}.
\]

Let its localized critical vorticity norm be

\[
M_k
:=
\|\omega_{source,k}\|_{\dot H^{-1/2}}.
\]

The M5-421 critical duality law gives, schematically,

\[
\boxed{
\frac{|S_{source\to target}|}{\nu/s_{j+k}^2}
\lesssim
\left(\frac{s_{j+k}}{\mathcal R_k}\right)^2
\frac{M_k}{\nu}
}
\]

when the source is outside the target natural window.

The formed-carrier M5-416 law gives the same age exponent in its optimal remote/coarse regime.

---

## 4. Non-co-shrinking old source

Suppose the old source does **not** shrink geometrically with the target.

Precisely, assume over `k` generations

\[
\mathcal R_k
\ge
c_R\mathcal R_0
\]

for a fixed `c_R>0`.

Then

\[
\left(
\frac{s_{j+k}}{\mathcal R_k}
\right)^2
\le
C
q^{-k}
\left(
\frac{s_j}{\mathcal R_0}
\right)^2.
\]

Therefore

\[
\boxed{
\eta_{j+k}^{old}
\lesssim
q^{-k}
\frac{M_k}{M_0}
\eta_j^{old}
}
\]

up to fixed shape/localization constants.

If the old source critical norm remains within a fixed multiple of its initial value,

\[
M_k\lesssim M_0,
\]

then

\[
\boxed{
\eta_{j+k}^{old}
\lesssim
Cq^{-k}.
}
\]

This is geometric strain-source age dilution.

---

## 5. Critical norm growth needed to defeat age dilution

Suppose instead the same non-co-shrinking source is required to provide a fixed normalized strain fraction

\[
\eta_{j+k}^{old}\ge\epsilon_0>0
\]

for arbitrarily large `k`.

Then M5-421 forces

\[
\boxed{
M_k
\gtrsim
c\epsilon_0\nu
\left(
\frac{\mathcal R_k}{s_{j+k}}
\right)^2.
}
\]

Under `mathcal R_k >= c_R mathcal R_0`, this gives

\[
\boxed{
M_k
\gtrsim
c q^k
}
\]

relative to the fixed initial geometric normalization.

Thus the squared critical mass obeys

\[
\boxed{
M_k^2
\gtrsim
c q^{2k}.
}
\]

Hence defeating source-age dilution with a geometrically old source requires exponential critical-mass escalation.

This enters the strong `C_mass accum` lane rather than the near-balanced slow-growth lane of M5-419.

---

## 6. Co-shrinking source lineage

The only way for one source identity to avoid the separation penalty without exponential critical amplification is to shrink its characteristic scale/distance along with the target:

\[
\boxed{
\mathcal R_k
\asymp
s_{j+k}.
}
\]

For a material source carrier this means a genuine co-shrinking source lineage undergoing the same order of cross-sectional deformation as the main first-hitting funnel.

This is not a generic remote reservoir anymore.

It is exactly the persistent local main/companion genealogy developed in M5-393, M5-394, and M5-418.

Therefore

\[
\boxed{
\text{old efficient source reuse}
\Longrightarrow
G_{co\text{-}shrinking\ dual\ lineage}
\lor
C_{mass\,exp}.
}
\]

---

## 7. Fresh source handoff

If the old source does not co-shrink and does not amplify its critical mass exponentially, its strain contribution becomes negligible after bounded generation age.

The required M5-362 stretching floor must then be supplied by a new source descriptor at the current target scale.

By M5-416/M5-421, an efficient new source must enter the current natural phase-space window.

Hence

\[
\boxed{
\text{no co-shrinking old source}
+
\text{no exponential mass growth}
\Longrightarrow
\text{fresh natural source handoff}.
}
\]

This is the source-side nonreuse mechanism sought after M5-415.

---

## 8. Important distinction from M5-385 and M5-396

There are now three different age laws in the repository.

### Shield circulation age dilution — M5-385

The required shield circulation itself grows with generation, so old shield circulation loses relative weight.

### Natural flux — M5-396

\[
\Phi\asymp\nu
\]

at every generation, so **flux amount has no age dilution**.

### Natural stretching-source efficiency — present note

The later target strain grows like `s^-2`, so a fixed-scale old source loses coupling efficiency:

\[
\boxed{
\eta_{source}(k)\sim q^{-k}
}
\]

unless it co-shrinks or amplifies.

These statements concern different observables and are mutually consistent.

---

## 9. Material interpretation

A material companion can remain an `O(nu)` flux carrier indefinitely in principle.

But if its material tube does not contract alongside the main target, its strain field becomes too coarse to drive later first-hitting growth.

Thus persistent **flux ancestry** is weaker than persistent **source ancestry**.

For persistent source ancestry one needs both:

\[
\boxed{
\text{flux retention}
+
\text{co-shrinking geometric coupling}.
}
\]

This refinement is important for future genealogy audits.

---

## 10. Relation to M5-419 near balance

The M5-419 `C_bal` branch assumes critical norm growth is slow relative to the accumulated critical dissipation over long blocks.

Exponential source-mass growth

\[
M_k^2\gtrsim q^{2k}
\]

is incompatible with that interpretation over a long reused-source epoch; it belongs to the explicit strong mass-accumulation lane.

Therefore a near-balanced late tower must predominantly use

\[
\boxed{
\text{co-shrinking local source lineages}
\quad\text{or}\quad
\text{repeated fresh natural-source handoffs}.
}
\]

This removes a passive old remote reservoir as the main long-time payer of near-balanced first-hitting stretching.

---

## 11. Freshness rate

Fix a tolerated old-source contribution fraction `epsilon_old`.

Because old non-co-shrinking source efficiency decays like `q^-k`, there exists a finite age

\[
\boxed{
K_{src}
\asymp
\frac{\log(C/\epsilon_{old})}{\log q}
}
\]

such that any source older than `K_src` generations contributes at most `epsilon_old` unless it has entered co-shrinking lineage or critical-mass escalation.

Thus source freshness has a finite generation memory even though flux identity itself may have infinite age.

This is a new finite-memory statement at the level of **stretching function**, not material identity.

---

## 12. Updated source genealogy

A source carrier born at generation `m` and observed at generation `j=m+k` satisfies the audited trichotomy

\[
\boxed{
\text{source ancestry}
\Longrightarrow
\begin{cases}
\text{co-shrinking efficient material lineage},\\
\text{critical source-mass amplification }\gtrsim q^k,\\
\text{age-diluted source requiring fresh handoff}.
\end{cases}
}
\]

This is stronger than the earlier material-flux genealogy because it tracks **functional ability to stretch the current core**.

---

## 13. What remains for fresh handoffs

Repeated fresh source handoff does not yet contradict any Leray-level quantity.

Each handoff creates a new natural critical source event and, by M5-418, a fixed natural-time critical derivative charge.

The missing step is to show that these fresh source actions cannot be continually charged to the same critical nonlinear production reservoir without either:

1. critical mass accumulating at a forbidden rate; or
2. converging to a rigid near-balanced recurrent element.

Thus the problem is now a true novelty-to-dissipation nonreuse problem.

---

## 14. Audit verdict

### DERIVED

For non-co-shrinking old sources,

\[
\boxed{
\eta_{source}(k)
\lesssim
q^{-k}
\times
\text{critical-amplification factor}.
}
\]

Fixed efficient reuse requires either

\[
\boxed{
\text{co-shrinking source lineage}
}

or

\[
\boxed{
M_k\gtrsim q^k,
\quad M_k^2\gtrsim q^{2k}.
}
\]

Otherwise a fresh natural source is required after bounded generation age.

### CURRENT HARD CORE

- co-shrinking near-balanced main/source lineage;
- repeated fresh natural source handoffs;
- explicit strong critical-mass accumulation;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
