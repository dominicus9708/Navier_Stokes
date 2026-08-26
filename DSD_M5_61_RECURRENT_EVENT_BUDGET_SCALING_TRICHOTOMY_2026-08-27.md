# DSD M5-61 — Recurrent Event-Budget Scaling Trichotomy

Date: 2026-08-27

Status: **SCALING/BUDGET CLASSIFICATION / SYNDETIC W1 RETURNS PRODUCE AN EXPONENTIALLY SEPARATED PHYSICAL ZENO SUBLADDER / ANY HOMOGENEOUS PER-EVENT COST FALLS INTO A SUBCRITICAL-SUMMABLE, CRITICAL-ORDER-ONE, OR SUPERCRITICAL-GROWING CLASS / ONLY A NONSUMMABLE CLASS COUPLED TO AN INDEPENDENT FINITE TOTAL BUDGET CAN YIELD AN ACCUMULATION CONTRADICTION / THE CURRENT CLASSICAL BUDGETS LIE ON THE WRONG SIDE / GLOBAL REGULARITY UNPROVED.**

## 1. A separated recurrent subladder

M5-52 and M5-57 give robust recurrent pump intervals of uniform positive normalized width with bounded return gaps in Leray time.

Choose a disjoint subfamily of returns with centers

\[
h_n\to\infty
\]

such that for fixed constants

\[
0<d_*\le h_{n+1}-h_n\le D_*<\infty.
\]

This is possible by selecting separated visits from the syndetic robust-return family.

Hence

\[
h_n\asymp n
\]

up to affine constants.

The corresponding Navier--Stokes amplitude scale is

\[
\Lambda_n=e^{h_n/2},
\]

so

\[
\boxed{
\Lambda_n
\text{ grows geometrically in }n.
}
\]

The physical radius and remaining-time scales are

\[
r_n=\Lambda_n^{-1},
\qquad
\delta_n\asymp\Lambda_n^{-2}.
\]

---

## 2. Generic homogeneous event cost

Let `C` be a nonnegative spacetime action assigned to one robust pump interval.

Assume that under Navier--Stokes scaling

\[
u_\Lambda(x,t)
=\Lambda u(\Lambda x,\Lambda^2t)
\]

its event cost is homogeneous:

\[
\boxed{
\mathfrak C_\Lambda
=\Lambda^\gamma\mathfrak C_1.
}
\]

The exponent `gamma` is the **event-budget scaling exponent**.

On the recurrent subladder,

\[
\mathfrak C_n
\asymp
\Lambda_n^\gamma.
\]

Because `Lambda_n` grows geometrically, summability is decided sharply by the sign of `gamma`.

---

## 3. Subcritical-budget class: `gamma < 0`

If

\[
\gamma<0,
\]

then

\[
\mathfrak C_n
\lesssim
q^n
\]

for some `0<q<1`.

Thus

\[
\boxed{
\sum_{n=1}^\infty\mathfrak C_n<\infty.
}
\]

Even if a classical global estimate bounds the total action by initial data, infinitely many recurrent pump copies are compatible with that estimate because their physical costs shrink fast enough.

This is precisely the mechanism seen in M5-47/M5-49.

---

## 4. Critical class: `gamma = 0`

If

\[
\gamma=0,
\]

then every normalized recurrent copy carries the same order of event action:

\[
\mathfrak C_n
\asymp c_*>0.
\]

Hence

\[
\boxed{
\sum_{n=1}^N\mathfrak C_n
\gtrsim c_*N
\to\infty.
}
\]

Since `h_N asymp N`, this is the logarithmic critical divergence in physical terminal time:

\[
N
\asymp
\log\frac1{\delta_N}.
\]

A critical event action would therefore immediately close the recurrent survivor **if** one also had an independent finite total bound

\[
\sum_n\mathfrak C_n
\le B_0<\infty.
\]

The present difficulty is that the known critical actions do not come with such a finite budget from the Leray energy hypotheses.

---

## 5. Supercritical event class: `gamma > 0`

If

\[
\gamma>0,
\]

then the event lower bounds themselves grow:

\[
\mathfrak C_n
\gtrsim
\Lambda_n^\gamma
\to\infty.
\]

The cumulative action diverges even faster.

But this scaling fact alone is not a contradiction. Near a hypothetical singular terminal point, a supercritical quantity is precisely allowed to become unbounded unless an independent theorem makes its total amount finite.

Therefore

\[
\boxed{
\gamma>0
\text{ is stronger divergence but not stronger closure without a finite budget.}
}
\]

---

## 6. Placement of the known M5 quantities

### Kinetic energy

Instantaneous kinetic energy scales as

\[
\int|u_\Lambda|^2dx
=\Lambda^{-1}\int|u|^2dx.
\]

Thus nested energy content shrinks with exponent `-1`.

### Ordinary spacetime enstrophy

Instantaneous enstrophy scales as

\[
\int|\nabla u_\Lambda|^2dx
=\Lambda\int|\nabla u|^2dx,
\]

while the event duration scales as `Lambda^{-2}`.

Therefore

\[
\boxed{
\int_{I_\Lambda}\int|\nabla u_\Lambda|^2dxdt
\sim\Lambda^{-1}.
}
\]

This is the finite classical dissipation budget, but it belongs to `gamma=-1` and is summable.

### M5 critical `D3` action

For

\[
D_3(u)=\int|u||\nabla u|^2dx,
\]

the instantaneous scaling is `Lambda^2`; multiplying by duration `Lambda^{-2}` gives

\[
\boxed{\gamma=0.}
\]

Thus every recurrent pump contributes order one, but no finite total `D3` budget is known from the energy inequality.

### M5-54/M5-56 weighted pressure-square payer

Pressure scales as

\[
p_\Lambda=\Lambda^2p(\Lambda x,\Lambda^2t).
\]

Hence the instantaneous quantity

\[
\int|u||p|^2dx
\]

scales as `Lambda^2`, and its spacetime event integral is critical:

\[
\boxed{\gamma=0.}
\]

The amplitude-mollified band payer is the corresponding normalized finite-band localization and inherits the same critical event accounting when the amplitude band is transported with the recurrent scaling.

Again the event lower bound is nonsummable, but no independent finite total pressure-square budget has yet been derived.

---

## 7. The exact location of the obstruction

The known estimates now line up as follows:

\[
\boxed{
\begin{array}{c|c|c}
\text{quantity} & \text{event exponent} & \text{finite global budget?}\\
\hline
L^2\text{ energy content} & -1 & \text{yes/bounded, but nested content shrinks}\\
\text{spacetime enstrophy} & -1 & \text{yes}\\
D_3\text{ critical action} & 0 & \text{not from energy theory}\\
\text{weighted pressure-square action} & 0 & \text{not currently}\\
\text{signed mollified overpay} & 0\text{-type} & \text{bounded primitive, but exact/telescoping}
\end{array}
}
\]

Therefore the current proof gap is not merely a missing estimate constant.

It is an **exponent-budget mismatch**:

\[
\boxed{
\text{known finite budgets are summable per copy, while known nonsummable actions lack finite budgets.}
}
\]

---

## 8. Closure criterion

For an accumulation contradiction based on recurrent events, it is enough to produce a nonnegative action `A` satisfying both:

\[
\boxed{
\mathfrak A(I_n)
\ge c\Lambda_n^\gamma
}
\]

with

\[
\gamma\ge0
\]

on the separated recurrent subladder, and

\[
\boxed{
\sum_n\mathfrak A(I_n)
\le B(u_0,\nu)<\infty.
}
\]

The first condition makes the recurrent lower bounds nonsummable.

The second turns that divergence into a contradiction.

If no such action exists, the remaining route is direct rigidity/nonexistence of the recurrent pump cell.

---

## 9. DSD consequence

This classification prevents three recurring category errors:

1. a finite global budget is useless for contradiction if the per-copy lower costs are geometrically summable;
2. a scale-critical positive cost is not enough if its total is not independently bounded;
3. a growing supercritical diagnostic is not itself forbidden near the hypothetical singularity.

The proof search should therefore stop generating additional beta-zero/critical diagnostics unless they can be connected to a finite initial-data-controlled budget or to a direct no-loop rigidity theorem.

---

## 10. New branch priority

The budget route is now sharply formulated but currently has no known payer.

The more promising immediate branch is therefore the structural one:

\[
\boxed{
\text{use the localized core + finitely adjacent log-shell pressure/Hodge geometry to exclude the recurrent finite-band pump loop directly.}
}
\]

A parallel secondary branch remains open:

\[
\boxed{
\text{search specifically for a hidden finite critical budget, not merely another critical norm.}
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
