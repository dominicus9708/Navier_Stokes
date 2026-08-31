# DSD M5-385 — Return/recycling age dilution and fresh-ancestry gate

Date: 2026-08-31

Status: **QUIET MATERIAL RETURN IS NOT A SCALE-NEUTRAL SUPPLY MECHANISM / A DESCENDANT EXPELLED AT GENERATION m CARRIES CIRCULATION SCALE `Gamma_m ~ r_m^(-2/5)`, WHILE THE CURRENT SHIELD AT GENERATION j=m+k REQUIRES `Gamma_j ~ q^(k/5) Gamma_m` / WITHOUT A VISCOUS CIRCULATION-GROWTH H EVENT, THE FRACTION SUPPLIED BY ONE AGE-k RETURN DECAYS LIKE `q^(-k/5)` / FINITE-MEMORY BOUNDS THE NUMBER OF SIMULTANEOUS QUIET OLD DESCENDANTS, SO ALL AGE>=K QUIET RETURNS TOGETHER CONTRIBUTE AT MOST `C N_E q^(-K/5)` OF CURRENT CIRCULATION / THEREFORE FIXED-FRACTION RECYCLING IS NECESSARILY BOUNDED-AGE OR ELSE H / A PURE FINITE-POOL RECYCLING LOOP CANNOT SUSTAIN THE UNBOUNDED SHIELD-CIRCULATION TOWER WITHOUT VISCOUS AMPLIFICATION; NO-H CONTINUATION MUST KEEP INTRODUCING FRESH ANCESTRY OR LOSE MATERIAL DESCRIPTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

After M5-384, the no-H T frontier is

\[
 T_{\rm spatial/non-tight}
 \lor
 T_{\rm descriptive/ancestry\ noncompactness}
 \lor
 T_{\rm return/recycling}.
\]

Return/recycling is potentially different from pure export because old material circulation comes back into a later active region.

The question is whether return can serve as a free renewable source for the growing saturated affine circulation.

The answer is no for old quiet descendants: their historical circulation scale becomes an exponentially smaller fraction of the later required circulation unless viscosity amplifies the material circulation.

---

## 2. Circulation growth of the active shield

On the saturated affine corridor,

\[
 r_{j+1}=q^{-1/2}r_j,
 \qquad
 d_j\asymp r_j^{4/5},
\]

and

\[
 \boxed{
 \Gamma_j\asymp r_j^{-2/5}.
 }
\]

Hence

\[
 \boxed{
 \Gamma_{j+k}
 \asymp
 q^{k/5}\Gamma_j.
 }
\]

This is the circulation-growth law already used in M5-356--359.

---

## 3. Quiet returned descendant

Let a material circulation descendant `alpha` be expelled/formed at generation `m` with

\[
 |\Gamma_\alpha(t_m)|\asymp\Gamma_m.
\]

Call its later return **quiet** if, between `m` and the return generation,

- it remains an identifiable material circulation carrier;
- it does not undergo the viscous circulation-growth H event of M5-356/380;
- it does not lose its charge through cancellation/destruction;
- it does not undergo unbounded fragmentation/microshape H from M5-382--384.

On this corridor its material circulation remains comparable to its historical value:

\[
 \boxed{
 |\Gamma_\alpha(t)|
 \le C_{ret}\Gamma_m
 }
\]

for the retained fixed quiet-comparability constant.

This is not asserted for arbitrary descendants. If this comparability fails because the circulation itself grows by an unbounded factor, that is exactly the Kelvin/viscous circulation-growth channel to be typed as H.

---

## 4. Age dilution

Suppose `alpha` returns at generation

\[
 j=m+k.
\]

The current active shield requires circulation scale `Gamma_j`.

Therefore the maximum fixed-sign fraction one quiet age-`k` descendant can supply is

\[
 \frac{|\Gamma_\alpha|}{\Gamma_j}
 \lesssim
 C_{ret}
 \frac{\Gamma_m}{\Gamma_{m+k}}
 \asymp
 C_{ret}q^{-k/5}.
\]

Thus

\[
 \boxed{
 f_{ret}(k)
 \lesssim
 C_{ret}q^{-k/5}.
 }
\]

Old quiet material charge is exponentially diluted relative to the growing active shield requirement.

---

## 5. Combine with finite memory

M5-357 gives a scale-independent energy floor for each quiet coherent circulation descendant:

\[
 E_\alpha^{quiet}\ge e_*>0.
\]

Finite kinetic energy therefore bounds the number of simultaneously quiet descendants by

\[
 \boxed{
 N_{quiet}(t)\le N_E<\infty.
 }
\]

At generation `j`, consider all quiet returned descendants whose age is at least `K`.

Each has historical circulation at most, up to fixed comparability constants,

\[
 \Gamma_{j-K}
 \asymp
 q^{-K/5}\Gamma_j.
\]

There are at most `N_E` of them simultaneously.

Hence their total absolute circulation satisfies

\[
 \boxed{
 \Gamma_{ret}^{age\ge K}(j)
 \lesssim
 C_{ret}N_Eq^{-K/5}\Gamma_j.
 }
\]

Therefore

\[
 \boxed{
 \frac{\Gamma_{ret}^{age\ge K}(j)}{\Gamma_j}
 \lesssim
 C_{ret}N_Eq^{-K/5}.
 }
\]

---

## 6. Old-return exclusion for any fixed supply fraction

Fix any desired current-shield supply fraction

\[
 0<\theta<1.
\]

Choose

\[
 \boxed{
 K_\theta
 >
 \frac{5}{\log q}
 \log\frac{2C_{ret}N_E}{\theta}.
 }
\]

Then

\[
 C_{ret}N_Eq^{-K_\theta/5}<\theta/2.
\]

Consequently all quiet returned descendants of age at least `K_theta` together contribute less than `theta/2` of the current circulation.

Thus if return/recycling supplies a fixed fraction `theta` of the active shield circulation on infinitely many late generations, then on each such generation at least one of the following must occur:

1. a **bounded-age return** with age `<K_theta` supplies a non-negligible part;
2. an old descendant has amplified its material circulation beyond quiet comparability, giving Kelvin/viscous H;
3. the number of old identifiable charge carriers exceeds the finite-memory quiet bound, so some carrier has undergone T/H reformation;
4. fresh material ancestry contributes the missing circulation.

This is the main age-dilution gate.

---

## 7. Pure finite-pool recycling cannot sustain the tower

Consider the stronger hypothetical **pure recycling corridor**:

- no H;
- no fresh material ancestry is introduced after some generation `J_0`;
- no descendant loses material identity through descriptive/spatial T;
- all later active-shield circulation is assembled from a fixed finite pool `P` of identifiable material circulation carriers.

By finite memory and the active-core carrier count, `P` is finite on this corridor.

The active circulation satisfies

\[
 \Gamma_j\to\infty.
\]

If every carrier in `P` retained a bounded material circulation, then

\[
 \sum_{\alpha\in P}|\Gamma_\alpha|
 <\infty
\]

would be a fixed ceiling, impossible for a current shield requiring `Gamma_j -> infinity`.

Therefore at least one material carrier in the finite pool must satisfy

\[
 \boxed{
 |\Gamma_\alpha(t_j)|\to\infty
 }
\]

along a subsequence of returns.

But material circulation cannot be increased by inviscid stretching alone. For a material loop,

\[
 \frac d{dt}\Gamma_\alpha
 =
 \nu\oint_{C_\alpha(t)}\Delta u\cdot dl.
\]

Hence unbounded amplification of a fixed material carrier requires unbounded cumulative viscous circulation transfer.

On the regular/comparable return corridor, the M5-356/380 mollified flux estimates route the required geometric-scale amplification to

\[
 \boxed{
 H_{\rm visc/pal/der}.
 }
\]

If the carrier geometry ceases to be regular/comparable while this happens, that failure is already

\[
 T_{\rm descriptive/ancestry\ noncompactness}
 \lor
 T_{\rm spatial}.
\]

Therefore

\[
 \boxed{
 \text{pure finite-pool recycling}
 \Longrightarrow
 H
 \lor
 T_{\rm description/spatial}.
 }
\]

It is not an independent quiet terminal mechanism.

---

## 8. What bounded-age recycling can still do

The argument does **not** exclude a process in which recently expelled material returns within a uniformly bounded number of generations while new material is also continually recruited.

Indeed for bounded age `k=O(1)`,

\[
 q^{-k/5}=O(1),
\]

so a recent descendant can carry a fixed fraction of the current circulation without its own material circulation changing by a divergent factor.

Thus the surviving no-H return corridor is not

\[
 \text{arbitrarily old charge recycling}.
\]

It is only

\[
 \boxed{
 \text{bounded-age recycling}
 +
 \text{continual fresh ancestry/reformation}.
 }
\]

The second term is a genuine T mechanism and cannot be removed by calling the process recycling.

---

## 9. Relation to the bounded-gap material-return theorem

The 2026-08-25 compact EMGG theorem proved that positive-measure recurrent high states generate bounded-Leray-gap material returns or local exposure.

That result is fully compatible with the present age-dilution statement:

- bounded-gap returns are exactly the type of bounded-age return that can remain significant;
- the theorem did not claim that an arbitrarily old material packet can keep supplying a fixed fraction of later shield circulation;
- long-age return weights were explicitly left open there.

M5-385 therefore sharpens the long-age interpretation without contradicting the existing compact-return gate.

---

## 10. DSD interpretation

Return has two distinct descriptors:

1. **material identity return** — the same particles/loop re-enter a described region;
2. **structural charge relevance** — how much of the current circulation that old material can actually supply.

These are not equivalent.

The age-dilution law

\[
 f_{ret}(k)\lesssim q^{-k/5}
\]

shows that material identity may persist while structural relevance decays exponentially.

Thus DSD must not classify every old material return as an order-one recycling of the current state.

---

## 11. Firewall

- Do not assume exact Kelvin conservation for viscous Navier-Stokes; circulation changes through the viscous term.
- The quiet-return comparability `|Gamma_alpha| <= C_ret Gamma_m` is a corridor definition. Failure is explicitly the circulation-growth H route.
- Finite memory bounds simultaneously quiet identifiable descendants, not all possible historical material labels.
- The theorem does not exclude bounded-age recycling accompanied by fresh recruitment.
- No finite global budget for fresh absolute circulation has yet been proved.

---

## 12. Updated T frontier

M5-385 removes **old quiet recycling as a standalone supply mechanism**.

The no-H T frontier can now be written more sharply as

\[
 \boxed{
 T_{\rm spatial/non-tight}
 \lor
 T_{\rm descriptive/ancestry\ noncompactness}
 \lor
 \bigl(T_{\rm bounded-age\ return}
 +T_{\rm fresh\ ancestry/reformation}\bigr).
 }
\]

Since bounded-age return alone cannot sustain the unbounded circulation tower, the real unresolved T content is the repeated introduction/reformation/export of material ancestry.

The next target is therefore an **ancestry-throughput ledger**: determine whether the fresh material circulation required per bounded block can be assigned a scale-independent energy/circulation charge without double counting recycled material.

---

## 13. Audit verdict

### NEW RESULTS

\[
 \boxed{
 f_{ret}(k)\lesssim C_{ret}q^{-k/5}
 }
\]

for one quiet age-`k` returned descendant, and

\[
 \boxed{
 f_{ret}^{age\ge K}
 \lesssim C_{ret}N_Eq^{-K/5}
 }
\]

for all simultaneously quiet old returns.

### REMOVED AS INDEPENDENT T

Arbitrarily old quiet recycling as a fixed-fraction current-circulation supply.

Pure finite-pool recycling without fresh ancestry or H.

### STILL OPEN

- bounded-age recycling plus continual fresh ancestry;
- scale-independent/nonsummable ancestry-throughput charge;
- pure spatial export/non-tightness;
- descriptive ancestry noncompactness;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
