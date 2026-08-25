# DSD Positive-Frequency Export: Energy-Cascade Neutrality

Date: 2026-08-25

Status: **CRITICAL ENERGY BUDGET AUDIT / INFINITELY MANY POSITIVE-FREQUENCY EXPORT EVENTS HAVE SUMMABLE PHYSICAL ENERGY COST / ONLY A FINITE CONSTANT-CAPACITY TEST REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The permanent-export branch contains infinitely many separated events with positive Leray-time frequency.

It is tempting to argue that each fixed-flux event costs positive energy, so infinitely many events must exceed the finite physical kinetic-energy budget.

That argument is false because the event energy decreases exactly at the critical geometric rate.

## 2. Physical energy scaling of one natural-scale packet

At first-hitting stage \(j\),

\[
r_j=\sqrt{\frac\nu{W_j}}.
\]

Use the normalized velocity

\[
u(x,t_j)
=\sqrt{\nu W_j}\,U_j(Y),
\qquad
Y=\frac{x-X_j}{r_j}.
\]

For any fixed normalized packet region \(C\),

\[
\int_{X_j+r_jC}|u|^2dx
=
\nu W_jr_j^3
\int_C|U_j|^2dY.
\]

Since

\[
\nu W_jr_j^3
=
\nu^{5/2}W_j^{-1/2}
=
\nu^2r_j,
\]

one has the exact scaling

\[
\boxed{
E_{phys,j}(C)
=
\nu^2r_j E_{norm,j}(C).
}
\]

Therefore a coherent exported packet with a fixed normalized relative-energy lower bound \(\kappa_E>0\) costs

\[
\boxed{
E_{exp,j}
\ge
\kappa_E\nu^2r_j.
}
\]

## 3. Leray-time decay of the physical natural scale

Along the first-hitting corridor,

\[
s_j=j\log q+O(1),
\qquad
r_j=r_0q^{-j/2}.
\]

Hence, up to fixed corridor constants,

\[
\boxed{
r(s)\asymp e^{-s/2}.}
\]

Thus the physical energy required by a fixed normalized export packet emitted at Leray time \(s\) is exponentially small in \(s\):

\[
E_{exp}(s)\asymp \kappa_E\nu^2e^{-s/2}.
\]

## 4. Positive event frequency is energy-summable

Let the separated permanent-export event count satisfy

\[
N_{exp}(S)\sim \rho_{exp}S
\]

at the level of positive asymptotic frequency.

The continuum comparison gives

\[
\int_{s_0}^{\infty}
\rho_{exp}\kappa_E\nu^2r(s)ds
\asymp
\rho_{exp}\kappa_E\nu^2r(s_0)
\int_0^\infty e^{-\sigma/2}d\sigma.
\]

Therefore

\[
\boxed{
E_{future,exp}(s_0)
\asymp
2\rho_{exp}\kappa_E\nu^2r(s_0)
<\infty.
}
\]

The discrete geometric sum gives the same conclusion:

\[
\sum_{j\ge J}r_j
=
\frac{r_J}{1-q^{-1/2}}<\infty.
\]

If only a positive-density subset of stages exports, the sum is smaller.

Thus infinitely many exports do not contradict finite physical kinetic energy.

## 5. The apparent q -> 1 amplification cancels

One might try to choose \(q\downarrow1\) so that

\[
\frac1{1-q^{-1/2}}
\]

becomes large.

But a fixed positive **Leray-time** event frequency corresponds to a per-stage event density proportional to the Leray stage spacing

\[
\Delta s\sim\log q.
\]

For \(q\downarrow1\),

\[
1-q^{-1/2}
\sim\frac12\log q.
\]

Hence

\[
\frac{\log q}{1-q^{-1/2}}
\to2.
\]

So no artificial contradiction is created by taking finer first-hitting stages.

The continuous coefficient \(2\rho_{exp}\) is the q-independent limiting quantity.

## 6. Dissipation has the same critical scaling

A natural-scale vorticity packet has

\[
|\omega|\sim W_j=\frac\nu{r_j^2}
\]

on volume \(\sim r_j^3\). Thus

\[
\int|\omega|^2dx
\sim
\frac{\nu^2}{r_j}.
\]

Its natural parabolic lifetime is

\[
\Delta t_j\sim\frac{r_j^2}{\nu}.
\]

The corresponding viscous kinetic-energy loss scale is

\[
\nu
\left(\frac{\nu^2}{r_j}\right)
\left(\frac{r_j^2}{\nu}\right)
\sim
\boxed{\nu^2r_j.}
\]

Thus both packet energy and one-natural-lifetime dissipation have the same summable geometric cost.

Positive-frequency emission can therefore be compatible with the total energy-dissipation budget as well.

## 7. Conditional local-energy capacity test

Suppose, on a no-inflow branch, a local scale-invariant energy/Morrey estimate gives

\[
E_{available}(s_0)
\le
M_E\nu^2r(s_0).
\]

If every future permanent export requires at least \(\kappa_E\nu^2r(s_e)\), then heuristically and, after standard event-count averaging, quantitatively one obtains a capacity restriction of the form

\[
\boxed{
2\kappa_E\rho_{exp}
\lesssim M_E.
}
\]

This is only a **finite constant comparison**.

If it fails, repeated export would require compensating inward material/pressure energy flux, which is routed back to the turnover ledger.

If it holds, the energy budget alone allows the cascade.

No universal inequality between the existing lower event-frequency bound and this capacity ceiling has been established.

## 8. Relation to the flux-loop countermodel

For the scaled loop family

\[
U_R=R^{-1}U_0(Y/R),
\]

the normalized energy is \(\sim R\).

At an ancestor physical scale \(r_n\) this becomes physical energy \(\sim\nu^2r_n\).

Thus the explicit flux-loop countermodel exactly saturates the energy-cascade scaling derived here.

## 9. Audit verdict

### PROVED / EXACT SCALING

- fixed normalized packet energy corresponds to physical energy \(\nu^2r_j\);
- \(r_j\sim e^{-s_j/2}\);
- a positive Leray-time frequency of infinitely many exports has finite total future energy cost;
- one natural-time viscous dissipation has the same \(\nu^2r_j\) scale;
- refining \(q\to1\) does not create a contradiction because event density per stage shrinks proportionally to \(\log q\).

### REDUCED TO CONSTANT TEST

A no-inflow local-energy corridor can at most provide a finite event-frequency capacity comparison.

### REJECTED ROUTE

\[
\text{infinitely many positive-frequency exports}
\Rightarrow
\text{infinite physical energy cost}
\]

is false.

### OPEN

A genuinely scale-critical monotone/coercive quantity or nonlinear recurrence-radiation rigidity remains necessary.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
