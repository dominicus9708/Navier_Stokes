# DSD M5-358 — Positive-Density Descendant Loss Does Not Force Branching: Firewall

Date: 2026-08-30

Status: **ANTI-PROOF / M5-357 POSITIVE GENERATION DENSITY OF DESCENDANT LOSS DOES NOT BY ITSELF FORCE GROWING TREE WIDTH OR A CARLESON CONTRADICTION / SEQUENTIAL RENEWAL WITH SUMMABLE SCALE COST REMAINS POSSIBLE / CIRCULATION LOSS MUST BE TRACKED EXPLICITLY / GLOBAL REGULARITY UNPROVED.**

## 1. Input

M5-357 proved that repeated saturated affine turnover cannot leave every expelled circulation descendant quietly persistent. Finite total energy forces descendant loss/reformation with a positive lower generation density.

Schematically,

\[
\boxed{
\#\{j\le N:\text{descendant-loss event at }j\}
\ge d_*N-O(1),
\qquad d_*>0.
}
\]

It is tempting to infer a branching tree with rapidly growing width. That inference is invalid.

## 2. Sequential-renewal anti-model

Consider an abstract generation process:

1. generation `j` creates one current active packet;
2. the old packet is exported;
3. before generation `j+1` finishes, the exported packet undergoes one classified H/T loss and ceases to be a quiet descendant;
4. only the new current packet remains coherent.

Then there is one loss event on every generation, but

\[
\boxed{N_{quiet}(j)\le1}
\]

for all `j`.

Thus

\[
\boxed{
\text{positive loss density}
\not\Longrightarrow
\text{growing descendant-tree width}.
}
\]

## 3. Summable physical event cost

Let the natural lengths be geometric:

\[
r_j=r_0q^{-j/2}.
\]

If a loss mechanism has a physical cost

\[
c_j\asymp r_j^\beta,
\qquad \beta>0,
\]

then even an event on every generation satisfies

\[
\boxed{
\sum_jc_j
\asymp
\sum_jq^{-\beta j/2}
<\infty.
}
\]

Therefore positive event density does not overcome the old critical/summable-cost firewall.

## 4. What a true tree contradiction would require

A Carleson/tree contradiction needs at least one additional mechanism:

- persistent branching, so the number `N_j` of simultaneous costly descendants grows fast enough;
- a per-event charge whose size does not decay with `r_j`;
- or a charge that actually grows toward small scales.

The affine circulation

\[
\Gamma_j\asymp r_j^{-2/5}
\]

is a candidate of the third type.

Thus the next question is not whether descendant **loss events** repeat, but whether sequential loss can dispose of circulation of size `Gamma_j` without paying a nonsummable viscous/mixing/spatial charge.

## 5. Correct descendant descriptor

Define two different quantities:

\[
N_j^{quiet}
:=\#\{\text{simultaneously quiet coherent descendants}\},
\]

and

\[
\mathcal C_j^{abs}
:=
\sum_{\alpha\in\mathcal D_j}
|\Gamma_\alpha|,
\]

where `D_j` is a chosen family of material circulation descendants still identifiable at generation `j`.

M5-357 controls `N_j^{quiet}` through energy.

The next audit must control the evolution of `C_j^{abs}`.

Branch width and absolute circulation inventory are not the same descriptor.

## 6. Formation-axiom interpretation

The distinction is

\[
\boxed{
\text{number of described objects}
\neq
\text{amount of structural charge carried by them}.
}
\]

A single surviving/recycled object may carry increasing charge while the object count stays bounded.

Therefore the formation decomposition must retain both

- multiplicity;
- charge magnitude.

## 7. Firewall

Do not use

\[
\text{fixed-fraction turnover every stage}
\Longrightarrow
N_j\to\infty.
\]

The sequential-renewal process is a direct counterexample.

Do not use positive generation density together with a scale-decaying cost as a contradiction; geometric summability survives.

## 8. Next target

Use Kelvin circulation and the growth

\[
\Gamma_j\sim r_j^{-2/5}
\]

to classify how an old descendant can cease to contribute to the absolute circulation inventory:

\[
\boxed{
\text{viscous destruction}
\lor
\text{opposite-sign cancellation/mixing}
\lor
\text{spatial elongation}
\lor
\text{return/recruitment}.
}
\]

The aim is to show that sequential renewal itself must pay a charge of order `Gamma_j`, not merely a scale-decaying energy cost.

## 9. Audit verdict

### PROVED AS A LOGICAL FIREWALL

- positive-density descendant loss does not force branching;
- a scale-decaying per-event physical cost remains summable at positive event density;
- multiplicity and circulation inventory must be tracked separately.

### OPEN

- absolute-circulation inventory balance;
- non-summable cost of sequential circulation disposal;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]