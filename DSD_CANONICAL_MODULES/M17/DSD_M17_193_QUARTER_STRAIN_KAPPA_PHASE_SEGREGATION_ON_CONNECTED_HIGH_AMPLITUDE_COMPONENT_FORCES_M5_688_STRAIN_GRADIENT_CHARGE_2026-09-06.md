# DSD M17-193 — Quarter-strain `kappa`-phase segregation on a connected high-amplitude component forces the M5-688 strain-gradient charge

Date: 2026-09-06  
Canonical ID: **M17-193**

Status: **PHASE-SEGREGATION TO GRADIENT-CHARGE CLOSURE / M17-187 SHOWS THAT IF THE POSITIVE UNWEIGHTED QUARTER-STRAIN EXCESS `P_0` IS PRESENT BUT ITS EXPONENTIAL PAYER IS SUPPRESSED, THE NEGATIVE PART OF THE KAPPA-RESOLVED SIGNED DENSITY `Q(k)=bar S_sigma-(1/4)bar F` HAS A FIXED POSITIVE MASS. SINCE `Q(k)` IS THE KAPPA-LEVEL PUSHFORWARD OF THE SPATIAL SIGNED DENSITY `(sigma-1/4) chi rho^2`, LEVEL-SET CANCELLATION CAN ONLY DECREASE ITS POSITIVE/NEGATIVE PARTS. THEREFORE THE UNDERLYING HIGH-AMPLITUDE REGION CONTAINS FIXED POSITIVE WEIGHTED MASSES WITH `sigma>1/4` AND `sigma<1/4`. THE WEIGHTED VARIANCE SATISFIES `Var_m(sigma-1/4)>=4 P_sp N_sp/M`. ON A CONNECTED UNIFORMLY REGULAR HIGH-AMPLITUDE COMPONENT, WEIGHTED POINCARE CONVERTS THIS INTO A FIXED POSITIVE `int chi rho^2 |grad sigma|^2`, AND HENCE INTO THE M5-688 EXPONENTIAL STRAIN-GRADIENT CHARGE `D_sigma`. THUS QUARTER-STRAIN PHASE SEGREGATION IS NOT AN INDEPENDENT ESCAPE UNLESS THE OPPOSITE-SIGN POPULATIONS LIVE IN DISCONNECTED/INTERFACE-SEPARATED COMPONENTS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Spatial quarter-strain density

On the retained high-amplitude region define

\[
\boxed{
m(y):=\chi(\rho)\rho^2}
\]

and

\[
\boxed{
f(y):=\sigma(y)-\frac14.}
\]

The recurrent `kappa`-resolved signed density is

\[
\boxed{
Q(k)
=\overline{
\int\delta(k-\kappa(y))f(y)m(y)dy
}.
}
\]

Define its scalar positive and negative masses

\[
P_Q:=\int Q_+(k)dk,
\qquad
N_Q:=\int Q_-(k)dk.
\]

---

## 2. Pushforward cancellation can only reduce sign masses

Define the underlying space-time weighted positive/negative quarter-strain occupancies

\[
\boxed{
P_{sp}
:=\overline{\int f_+m\,dy},
}
\]

\[
\boxed{
N_{sp}
:=\overline{\int f_-m\,dy}.
}
\]

At each fixed `k`, positive and negative spatial contributions may cancel before producing the scalar value `Q(k)`.
Therefore taking positive/negative parts after the pushforward cannot increase either microscopic sign mass:

\[
\boxed{P_Q\le P_{sp},}
\]

\[
\boxed{N_Q\le N_{sp}.}
\]

M17-191 gives

\[
P_0:=\int Q=P_Q-N_Q>0.
\]

Hence

\[
P_Q=P_0+N_Q\ge P_0.
\]

If the M17-187 exponential payer is suppressed, then

\[
\boxed{N_Q\ge n_*>0.}
\]

for the explicit `n_*` in that module.
Thus

\[
\boxed{
P_{sp}\ge P_0>0,
\qquad
N_{sp}\ge n_*>0.
}
\]

---

## 3. A variance lower bound from two-sided sign mass

Fix one recurrent time and one connected high-amplitude component `Omega` carrying the two sign populations.

Let

\[
M:=\int_\Omega mdy,
\]

\[
P:=\int_\Omega f_+m dy,
\qquad
N:=\int_\Omega f_-m dy.
\]

Let

\[
\bar f_m:=M^{-1}\int_\Omega fm dy.
\]

By Cauchy--Schwarz,

\[
\int_\Omega f^2m dy
\ge
\frac{\left(\int|f|m dy\right)^2}{M}
=\frac{(P+N)^2}{M}.
\]

Also

\[
M\bar f_m^2
=\frac{(P-N)^2}{M}.
\]

Subtracting,

\[
\boxed{
\int_\Omega(f-\bar f_m)^2m dy
\ge
\frac{4PN}{M}.
}
\]

This is an exact weighted-variance lower bound requiring no pointwise separation threshold.

---

## 4. Uniform connected-component assumptions

Assume the relevant connected high-amplitude components satisfy uniform compact bounds:

1. `rho` is bounded above and below on the interior cutoff support;
2. the component has uniformly controlled Lipschitz geometry/diameter;
3. the weighted measure `m dy` has a uniform Poincare constant `C_P`;
4. the total weighted mass is bounded above by `M^*`.

Then

\[
\boxed{
\int_\Omega(f-\bar f_m)^2m dy
\le
C_P\int_\Omega m|\nabla f|^2dy.
}
\]

Since

\[
\nabla f=\nabla\sigma,
\]

Sections 2--3 give, whenever fixed positive sign masses occur in the same component,

\[
\boxed{
\int_\Omega\chi\rho^2|\nabla\sigma|^2dy
\ge
\frac{4PN}{C_PM}
\ge c_\sigma>0.
}
\]

---

## 5. Exponential M5-688 strain-gradient charge

On compact multiplier support

\[
|\kappa|\le K_*,
\]

we have

\[
e^{2\kappa}\ge e^{-2K_*}.
\]

Therefore

\[
\boxed{
D_\sigma
:=\overline{
\int e^{2\kappa}\chi\rho^2|\nabla\sigma|^2dy
}
\ge
e^{-2K_*}c_\sigma>0.
}
\]

Thus the M17-187 phase-segregated suppression of the quarter-strain payer lands in the M5-688 strain-gradient payer branch whenever the opposite-sign populations occupy one uniformly controlled connected component.

---

## 6. Component-segregation escape

The only way to avoid the Poincare conversion above is for the positive and negative quarter-strain populations to be separated among different components or through a degenerating connector.

Hence

\[
\boxed{
G_{quarter}^{phase\ segregation}
\Longrightarrow
G_{strain-gradient}^{+}
\lor
G_{component/interface\ segregation}.
}
\]

The latter branch must pay through amplitude-threshold topology, domain/interface transport, component birth/death, or loss of uniform Poincare geometry.

It is no longer an invisible cancellation within one regular connected carrier.

---

## 7. Relation to M17-190

M17-190 forced `D_sigma>0` from same-material closed-loop recurrence and the `3/4` line covariance.

The present result is complementary:

- M17-190: **same-loop recurrence** forces the gradient payer;
- M17-193: **kappa-phase segregation** of the quarter-strain payer also forces the gradient payer on connected components.

Thus two apparently different strain-residence escape mechanisms collapse onto the same M5-688 fixed-order charge.

---

## 8. DSD audit

### Audit A — assuming all sign populations lie in one component
Made explicit. If not, the result routes to component/interface segregation.

### Audit B — replacing scalar `Q_-` by microscopic negative mass as equality
Rejected. Only the safe inequality `Q_- <= microscopic deficit mass` is used.

### Audit C — claiming `D_sigma>0` is a contradiction
Rejected. It is a forced payer, not a finite-use resource.

### Audit D — proof status
The phase-segregated quarter-strain branch is substantially reduced but global regularity remains open.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
