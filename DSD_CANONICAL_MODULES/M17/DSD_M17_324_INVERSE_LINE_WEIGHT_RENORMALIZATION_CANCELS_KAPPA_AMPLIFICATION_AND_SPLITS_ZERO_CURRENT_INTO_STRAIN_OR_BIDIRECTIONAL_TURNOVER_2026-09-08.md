# DSD M17-324 — inverse-line-weight renormalization cancels kappa amplification and splits zero current into strain or bidirectional turnover

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Exact M17-318 joint equation

M17-318 gives the pushed-forward pure-flux joint density

\[
H(k,l,\theta),
\qquad l=\log L_\rho,
\]

with currents \(J_k,J_l\) satisfying

\[
\boxed{
\partial_\theta H
+\partial_kJ_k
+\partial_lJ_l
=kH.
}
\]

The line-weight velocity is

\[
r:=\dot l
=k-\frac12+2\bar\sigma_\rho,
\]

so, at the level of the joint label representation,

\[
J_l=rH.
\]

## 2. Inverse-line-weight renormalization

Define

\[
\widetilde H:=e^{-l}H,
\qquad
\widetilde J_k:=e^{-l}J_k,
\qquad
\widetilde J_l:=e^{-l}J_l.
\]

Multiplying the joint equation by \(e^{-l}\) and using

\[
e^{-l}\partial_lJ_l
=\partial_l(e^{-l}J_l)+e^{-l}J_l
\]

gives

\[
\partial_\theta\widetilde H
+\partial_k\widetilde J_k
+\partial_l\widetilde J_l
=k\widetilde H-\widetilde J_l.
\]

Since

\[
\widetilde J_l
=\left(k-\frac12+2\bar\sigma_\rho\right)\widetilde H,
\]

we obtain the exact cancellation

\[
\boxed{
\partial_\theta\widetilde H
+\partial_k\widetilde J_k
+\partial_l\widetilde J_l
=
\left(\frac12-2\bar\sigma_\rho\right)\widetilde H.
}
\]

Thus the common \(kappa\) amplification has disappeared completely from the source term.

## 3. Marginal equation

Assume the retained compact/truncated line-weight population has no unrecorded \(l\)-boundary current; otherwise record

\[
G_{l\text{-}boundary/repartition}.
\]

Define

\[
\widetilde F(k,\theta)
:=\int\widetilde H(k,l,\theta)dl,
\]

\[
\widetilde G(k,\theta)
:=\int\widetilde J_k(k,l,\theta)dl,
\]

and

\[
\widetilde S(k,\theta)
:=\int
\left(\frac12-2\bar\sigma_\rho\right)
\widetilde H(k,l,\theta)dl.
\]

Then

\[
\boxed{
\partial_\theta\widetilde F
+\partial_k\widetilde G
=\widetilde S.
}
\]

## 4. Negative-kappa occupancy balance

Let

\[
N_-(\theta)
:=\int_{-\infty}^{0}\widetilde F(k,\theta)dk.
\]

Assuming the negative-tail current vanishes at \(k=-\infty\),

\[
\boxed{
\dot N_-
=-\widetilde G(0,\theta)
+
\int_{k<0}\widetilde S(k,\theta)dk.
}
\]

On a bounded recurrent/statistically stationary retained population, the long-time average of \(\dot N_-\) vanishes.  Hence

\[
\boxed{
\overline{\widetilde G(0)}
=
\overline{
\int_{k<0}
\left(\frac12-2\bar\sigma_\rho\right)
\widetilde H\,dk\,dl
}.
}
\]

This identity is exact under the stated boundary bookkeeping.

## 5. If the renormalized net current stays negative

Suppose

\[
\overline{\widetilde G(0)}\le-\widetilde d<0.
\]

Let

\[
M_T
:=
\frac1T\int_0^T\int_{k<0}\widetilde H\,dk\,dl\,d\theta,
\]

\[
A_T
:=
\frac1T\int_0^T\int_{k<0}
\bar\sigma_\rho\widetilde H\,dk\,dl\,d\theta,
\]

and

\[
B_T
:=
\frac1T\int_0^T\int_{k<0}
\bar\sigma_\rho^2\widetilde H\,dk\,dl\,d\theta.
\]

The occupancy balance gives asymptotically

\[
2A_T
\ge
\widetilde d+\frac12M_T-o(1).
\]

Cauchy--Schwarz gives

\[
A_T^2\le M_TB_T.
\]

Therefore

\[
B_T
\ge
\frac{(\widetilde d/2+M_T/4-o(1))^2}{M_T}.
\]

For every \(M>0\),

\[
\frac{(\widetilde d/2+M/4)^2}{M}
=
\frac{\widetilde d^2}{4M}
+\frac{\widetilde d}{4}
+\frac{M}{16}
\ge
\frac{\widetilde d}{2}.
\]

Hence

\[
\boxed{
\liminf_{T\to\infty}B_T
\ge
\frac{\widetilde d}{2}>0.
}
\]

A negative renormalized zero current therefore forces a positive time density of the nonnegative strain-residence square \(\bar\sigma_\rho^2\widetilde H\) on the negative-\(kappa\) phase.

## 6. If the renormalized net current is not negative enough

M17-323 gives a one-sided negative crossing activity.  In the renormalized variables define

\[
\widetilde A_-
:=\int e^{-l}(-j_k(0,l,\theta))_+dl,
\]

\[
\widetilde A_+
:=\int e^{-l}(j_k(0,l,\theta))_+dl.
\]

Then

\[
\widetilde G(0)=\widetilde A_+-\widetilde A_-.
\]

Suppose

\[
\overline{\widetilde A_-}\ge a_*>0.
\]

If

\[
\overline{\widetilde G(0)}> -\frac{a_*}{2},
\]

then

\[
\boxed{
\overline{\widetilde A_+}
=
\overline{\widetilde A_-}
+
\overline{\widetilde G(0)}
\ge
\frac{a_*}{2}.
}
\]

Thus failure of a fixed negative renormalized net current forces **bidirectional zero-level turnover** with positive density.

Combining with the first branch,

\[
\boxed{
\overline{\widetilde A_-}\ge a_*
\Rightarrow
H_{positive\ strain\text{-}residence\ square}
\lor
H_{bidirectional\ zero\text{-}level\ turnover}
\lor
G_{l\text{-}boundary/repartition}.
}
\]

## 7. Relation to M17-323 trace speed

On the regular label representation

\[
J_k=hH,
\qquad h=D_B\kappa.
\]

Therefore bidirectional turnover means positive density of both signs of \(h\) at the zero level.  Under the finite mean trace-mass condition of M17-323, either one-sided activity already yields a positive \(h^2\) trace ledger or the zero-level density itself concentrates.

Thus the two surviving non-boundary mechanisms are genuinely nonnegative:

\[
\bar\sigma_\rho^2\widetilde H
\quad\text{or}\quad
h^2\widetilde H|_{k=0}.
\]

## 8. Physicalization firewall

Neither quantity is yet a certified finite original-coordinate resource.  In particular,

\[
\widetilde H=e^{-l}H=L_\rho^{-1}H
\]

is an inverse-line-weighted pure-flux measure, not automatically physical volume or enstrophy measure.

Therefore

\[
\boxed{
\text{positive normalized nonnegative production}
\not\Rightarrow
\text{global contradiction}.
}
\]

The next step must convert one of the two ledgers to a standard spatial quantity and audit its Navier--Stokes scaling.

## 9. Audit verdict

**PASS as an exact renormalized-current reduction.**

This module materially improves the bookkeeping: common `kappa` amplification is removed, and the remaining zero-current obstruction is forced into strain-residence production, bidirectional coefficient turnover, or an explicit line-weight boundary/repartition exit.  It does not yet supply a finite scale-critical physical budget.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
