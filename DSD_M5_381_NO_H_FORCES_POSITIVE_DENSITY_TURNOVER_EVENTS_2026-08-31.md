# DSD M5-381 — No-H affine continuation forces positive-density T events

Date: 2026-08-31

Status: **M5-357 FINITE MEMORY PLUS M5-359/379/380 CIRCULATION-DISPOSAL AUDITS IMPLY THAT A LATE SATURATED AFFINE-SHIELD CASCADE CANNOT REMAIN NO-H WHILE T EVENTS ARE RARE / IF ALL DERIVATIVE, LIPSCHITZ, VISCOUS-PALINSTROPHY, AND HIGH-FREQUENCY H MECHANISMS ARE UNIFORMLY SUPPRESSED, THEN EVERY FIXED NUMBER OF LATE GENERATIONS CONTAINS A SPATIAL/MIXING/FRAGMENTATION/MICROSHAPE/RETURN TURNOVER EVENT / T THEREFORE HAS POSITIVE LOWER GENERATION DENSITY ON THE NO-H SURVIVOR / THIS IS A FREQUENCY STATEMENT, NOT YET A FINITE-BUDGET CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

The current master frontier after M5-378 is

\[
H_{\rm freq/cap}
\lor
T_{\rm dynamic/remote/compactness}.
\]

M5-379--380 sharpened the circulation-disposal side:

- a bounded-geometry cancellation reservoir either pays derivative/palinstrophy H or becomes anisotropic/spatial T;
- if a regular thin layer actually destroys the old material circulation, Kelvin-viscous flux still forces divergent normalized palinstrophy;
- apparent cancellation without material charge destruction is only a loss of coherent description and belongs to T.

The present note combines those results with the finite-memory theorem M5-357.

---

## 2. Finite-memory input

For each late saturated affine generation,

\[
\Gamma_j\asymp r_j^{-2/5},
\qquad
 d_j\asymp r_j^{4/5},
\]

so a quiet coherent expelled descendant satisfies

\[
\boxed{
E_j^{\rm desc}
\gtrsim
\Gamma_j^2d_j
\asymp1.
}
\]

Finite kinetic energy therefore bounds the number of simultaneously quiet descendants:

\[
\boxed{
N_{\rm quiet}(t)\le N_E<\infty.
}
\]

Consequently, if one new distinct descendant is produced on each late turnover generation, every block of at most

\[
N_E+1
\]

generations contains at least one descendant loss/reformation event.

Equivalently, M5-357 gives a lower generation density

\[
\boxed{
d_{\rm loss}\ge (N_E+1)^{-1}>0.}
\]

for failures of quiet persistence.

---

## 3. Older loss routing

M5-357 typed a quiet-descendant failure as

\[
H_{\rm visc/gradient}
\lor
T_{\rm spatial/fragment/mix/return}.
\]

M5-359 sharpened sequential deletion to

\[
\boxed{
\text{descendant loss}
\Longrightarrow
P_{\rm opp}^{\rm near}
\lor
H_{\rm Lip/log}
\lor
H_{\rm visc/der}
\lor
T_{\rm spatial/export}.
}
\]

The remaining concern was whether `P_opp^near` could provide a bounded-geometry cheap cancellation event.

---

## 4. Eliminate quiet cancellation on no-H

M5-379 showed that a fixed-fraction opposite reservoir under the first-hitting amplitude cap must occupy transverse area

\[
\gtrsim d_j^2.
\]

If it has effective thickness `ell_j`, then

\[
\boxed{
\mathfrak P_j
\gtrsim
\frac{\ell_j}{r_j}.
}
\]

Thus uniform no-palinstrophy-H forces

\[
\ell_j=O(r_j),
\]

which is sheet/shape T.

M5-380 then considered true destruction of the old material circulation through a regular tubular layer of thickness `h_j` and proved

\[
\boxed{
\widehat{\mathfrak P}_j
\gtrsim
\Theta_j^{-1}
\left(\frac{d_j}{r_j}\right)^2
\left(\frac{h_j}{r_j}\right)^3.
}
\]

For every non-sub-natural regular reach

\[
h_j\ge c r_j,
\]

this diverges at least as

\[
\boxed{
r_j^{-2/5}.}
\]

Therefore true material charge destruction cannot occur on a uniform no-H corridor through a regular natural-or-larger cancellation layer.

If the charge merely becomes eulerianly hidden while material circulation survives, that is

\[
T_{\rm mix/fragment/shape}.
\]

If the reach becomes sub-natural, it is

\[
H_{\rm high-freq/der}
\lor
T_{\rm microshape}.
\]

Hence there is no remaining quiet bounded-geometry cancellation leaf.

---

## 5. No-H loss is T

Define the late no-H corridor by uniform suppression of the typed H mechanisms relevant to descendant disposal:

\[
H_{\rm visc/der},
\quad
H_{\rm Lip/log},
\quad
H_{\rm pal},
\quad
H_{\rm high-freq}.
\]

Then every quiet-descendant loss event must lie in

\[
\boxed{
T_{\rm loss}
:=
T_{\rm spatial/export}
\lor
T_{\rm fragment/mix/return}
\lor
T_{\rm sheet/microshape}.
}
\]

Thus

\[
\boxed{
\text{no-H}
+
\text{descendant loss}
\Longrightarrow
T_{\rm loss}.
}
\]

---

## 6. Positive-density T theorem

M5-357 guarantees at least one descendant loss in every block of `N_E+1` sufficiently late generations.

Section 5 says every such loss is T on the no-H corridor.

Therefore

\[
\boxed{
\#\{j\le N:T_{\rm loss}\text{ occurs at generation }j\}
\ge
\frac{N}{N_E+1}-O(1).
}
\]

Equivalently,

\[
\boxed{
\underline d_T
:=
\liminf_{N\to\infty}
\frac1N
\#\{j\le N:T_j\}
\ge
\frac1{N_E+1}
>0.
}
\]

This is the main conclusion.

A no-H saturated affine cascade must use T with a fixed positive lower generation frequency.

---

## 7. Why this is stronger than a mere H/T dichotomy

The generic statement

\[
H\lor T
\]

allows the possibility that T occurs only on a very sparse subsequence while most generations remain geometrically quiet.

M5-381 excludes that possibility on the late saturated no-H corridor.

If H is suppressed, T is not exceptional:

\[
\boxed{
T\text{ is recurrent with bounded generation gaps.}
}
\]

Indeed the gap between successive T-loss events is at most `N_E+1` generations on the retained finite-memory corridor.

This makes T a dynamically essential mechanism rather than a bookkeeping remainder.

---

## 8. DSD interpretation

The formation history now has a finite-memory property.

At most `N_E` old coherent circulation descendants can remain simultaneously in the quiet described state.

Therefore a new generation cannot be formed indefinitely merely by appending another state while leaving old structural charge untouched.

On no-H, the system must repeatedly perform a **description-changing re-formation**:

\[
\boxed{
\text{spatial export}
\lor
\text{mixing}
\lor
\text{fragmentation}
\lor
\text{shape/reach degeneration}
\lor
\text{return/recycling}.
}
\]

The distinction is now:

- H changes or concentrates analytic scale/capacity;
- T repeatedly changes ancestry, location, or geometry of the material charge.

---

## 9. Firewall inherited from M5-358

Positive-density T is **not itself a contradiction**.

M5-358 already showed that an event cost

\[
c_j\asymp r_j^\beta,
\qquad\beta>0,
\]

remains summable even if it occurs on every generation.

Therefore one must not argue

\[
\text{positive-density T}
\Longrightarrow
\text{infinite energy/dissipation}.
\]

A true closure still requires one of the following:

1. a scale-independent or growing T charge;
2. a T event that preserves a large material circulation inventory and therefore cannot be reused indefinitely;
3. a rigidity theorem showing recurrent T is incompatible with the compact/ancient limit;
4. a return/recycling theorem forcing H when the same material charge re-enters smaller cores.

---

## 10. Updated master statement

On the late saturated affine-shield corridor,

\[
\boxed{
\text{hypothetical continuation}
\Longrightarrow
\begin{cases}
H\text{ occurs infinitely/often enough},\\
\text{or}\\
T\text{ occurs with positive lower generation density}.
\end{cases}
}
\]

More sharply, on a uniform no-H subsequence,

\[
\boxed{
\underline d_T\ge (N_E+1)^{-1}>0.
}
\]

The next T-side audit should test **return/recycling** first, because unlike pure export it brings an old circulation charge back into a smaller first-hitting core and may create a scale-amplifying mismatch.

---

## 11. Audit verdict

### DERIVED BY SUBSTITUTION OF PROVED CORRIDOR RESULTS

- finite memory gives a bounded generation gap between descendant-loss events;
- M5-379--380 remove bounded-geometry true cancellation from the no-H corridor;
- therefore no-H descendant losses are T;
- T-loss events have positive lower generation density.

### NOT DERIVED

- a nonsummable scalar cost from positive-density T;
- exclusion of repeated spatial export;
- exclusion of fragmentation/mixing without charge destruction;
- exclusion of return/recycling;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
