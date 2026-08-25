# DSD W1 log-radius conveyor and p=3 neutrality

Date: 2026-08-25

Status: **EXACT LINEAR LOG-RADIUS TRANSFORM / CRITICAL NORM SCALING PROVED / TAIL-SUBTRACTION RIGIDITY OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Log-radius variables

Let

\[
r=|Y|,\qquad \rho=\log r,\qquad \theta=Y/r.
\]

For a Leray velocity `U(Y,s)`, define the critical-amplitude field

\[
\boxed{
V(\theta,\rho,s):=e^\rho U(e^\rho\theta,s).
}
\]

Equivalently,

\[
U(Y,s)=r^{-1}V(\theta,\rho,s).
\]

This is only a change of variables; no homogeneity assumption is being made.

## 2. Exact cancellation of the self-similar linear drift

Componentwise,

\[
U_s=e^{-\rho}V_s,
\]

and

\[
Y\cdot\nabla U
=\partial_\rho(e^{-\rho}V)
=e^{-\rho}(-V+V_\rho).
\]

Therefore

\[
\boxed{
U_s+\frac12U+\frac12Y\cdot\nabla U
=e^{-\rho}\left(V_s+\frac12V_\rho\right).
}
\]

Introduce the co-moving log-radius coordinate

\[
\boxed{
\eta:=\rho-\frac{s}{2}.
}
\]

If

\[
\widetilde V(\theta,\eta,s)
:=V(\theta,\eta+s/2,s),
\]

then

\[
\partial_s\widetilde V
=V_s+\frac12V_\rho.
\]

Hence the entire self-similar linear part becomes simply

\[
\boxed{
U_s+\frac12U+\frac12Y\cdot\nabla U
=e^{-\rho}\partial_s\widetilde V.
}
\]

Thus the passive linear tail is frozen in `eta`.

## 3. Exact passive conveyor

If nonlinear, pressure, and viscous terms are neglected at a remote scale, then

\[
\partial_s\widetilde V=0.
\]

Consequently

\[
\boxed{
U(Y,s)=|Y|^{-1}F\left(\theta,\log|Y|-\frac{s}{2}\right)
}
\]

for an arbitrary admissible divergence-free leading profile `F`.

This recovers the existing dilation-conveyor law. A time increment `Delta` moves a fixed log-radius feature outward by

\[
\Delta\rho=\Delta/2,
\]

so the physical normalized radius is multiplied by

\[
e^{\Delta/2}.
\]

For one first-hitting Leray increment `Delta=log q`, this is exactly

\[
q^{1/2},
\]

the historical age-ladder factor already used in the repository.

## 4. Why the nonlinear correction is lower order

For a critical tail with

\[
U\sim r^{-1},
\qquad
P\sim r^{-2},
\]

one has schematically

\[
U\cdot\nabla U\sim r^{-3},
\qquad
\nabla P\sim r^{-3},
\qquad
\nu\Delta U\sim r^{-3}.
\]

The self-similar linear term is `r^-1` before its leading conveyor cancellation.
Therefore in the co-moving equation the nonlinear/viscous/pressure correction is lower by the factor

\[
\boxed{r^{-2}=e^{-2\rho}.}
\]

This is the differential-equation version of the previously proved old-shell Duhamel fact that a sufficiently old remote shell changes by only a vanishing fraction of its own natural state during one current-core stage.

Important scope point: an *exact* pure ansatz `r^-1 F(eta,theta)` with no lower-order correction would have to satisfy the residual order-`r^-3` equations as well. But an asymptotic critical tail can absorb that residual into subleading terms, for example an `r^-3 G` correction. Hence the leading `F` is not forced to solve the full stationary Navier--Stokes equation on the log cylinder.

## 5. The critical exponent p=3 is exact in log radius

For the leading critical form,

\[
|U|^p\,dY
=
r^{-p}|F|^p r^2dr\,d\theta.
\]

Since `dr=r d rho`,

\[
\boxed{
\int |U|^p\,dY
=
\int e^{(3-p)\rho}|F(\theta,\rho-s/2)|^p\,d\rho d\theta.
}
\]

Thus:

- `p>3`: the positive-radius tail is exponentially down-weighted in log radius;
- `p=3`: the weight disappears exactly;
- `p<3`: the remote tail is amplified.

In particular,

\[
\boxed{
\|U\|_3^3
=\int |F|^3\,d\rho d\theta
}
\]

whenever the identity is meaningful.

This explains the persistent logarithmic `L3` obstruction: every order-one interval of log radius can carry order-one cubic mass.

## 6. Passive p>3 decay versus p=3 neutrality

The passive dilation law is

\[
U(Y,s+\Delta)
=e^{-\Delta/2}
U(e^{-\Delta/2}Y,s).
\]

Hence

\[
\boxed{
\|U(s+\Delta)\|_p^p
=e^{-(p-3)\Delta/2}\|U(s)\|_p^p.
}
\]

Therefore

\[
\boxed{
p>3:\text{ strict passive decay},
\qquad
p=3:\text{ exact passive neutrality}.
}
\]

This is why the W1 orbit can be globally precompact in every `Lp`, `p>3`, while a critical historical tail can remain visible to the `L3`/weak-`L3` endpoint.

## 7. Periodic Leray orbit becomes log-periodic tail

Suppose the leading tail is genuinely represented by

\[
U\sim r^{-1}F(\theta,\rho-s/2)
\]

and the Leray profile is periodic with period `S`:

\[
U(s+S)=U(s).
\]

Then the leading tail satisfies

\[
F(\theta,\eta-S/2)=F(\theta,\eta).
\]

Thus

\[
\boxed{
F\text{ is log-radius periodic with period }S/2.
}
\]

Equivalently the physical solution is discretely self-similar with factor

\[
\lambda=e^{S/2}.
\]

A nonzero log-periodic `F` has fixed cubic mass per log period and is therefore naturally compatible with weak `L3` but not strong global `L3`.

This explains precisely why the strong-`L3` periodic Liouville theorems do not automatically cover the W1 periodic endpoint.

## 8. Aperiodic minimal dynamics and the tail

For the aperiodic minimal W1 branch, global `Lp` precompactness with `p>3` is relatively insensitive to sufficiently remote log-radius changes because of the weight `e^{(3-p)rho}`.

Therefore recurrence of the **core in global `Lp`, p>3**, does not by itself imply recurrence of the remote leading tail in the unweighted log-radius topology relevant to `p=3`.

This is an important anti-proof constraint: one must not infer an almost-periodic log tail solely from `Lp`, `p>3`, recurrence of the full trajectory.

## 9. Updated rigidity target

The W1 endpoint has two coupled but topologically different parts:

\[
\boxed{
\text{compact recurrent core in }L^p,\ p>3
}
\]

and

\[
\boxed{
\text{critical log-radius memory seen at }p=3.
}
\]

The remote-H Campanato commutator gate shows that the passive memory need not transmit order-one strain back to the core. Therefore a final proof needs one of:

1. a quotient/Liouville theorem that ignores or canonically subtracts passive log-radius memory;
2. a new global critical functional controlling the unweighted log-radius `p=3` mass;
3. a dynamical theorem excluding the remaining long-period or aperiodic recurrent core independently of the passive tail.

No such final theorem is established here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
