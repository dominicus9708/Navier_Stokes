# M18-066 — Recurrent-phase covariance is an oriented moment-space hysteresis circulation and forces variation but not monotone drift

**Date:** 2026-09-11  
**Status:** TEMPORAL-COVARIANCE AUDIT / MOMENT-SPACE CIRCULATION / PATH-FUNCTIONAL FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-064 splits the mandatory amplitude-growth covariance into a within-state spatial part and a between-state recurrent-phase part.

The present module treats

\[
\boxed{C_{phase}^{pq}>0.}
\]

The key question is whether this positive phase covariance is the derivative of a bounded state observable and therefore contradictory to recurrence.

It is not. It is naturally an **oriented circulation in amplitude-moment space**. A recurrent/periodic state can repeat such a loop indefinitely.

The positive circulation does, however, force nontrivial moment variation or a concentration-ratio degeneration.

## 2. Recall the phase covariance

M18-064 defines

\[
\bar h_p(Y)
=
\frac{\int(\sigma+\kappa)\rho^pdy}{M_p(Y)},
\]

and

\[
\bar w_p(Y)
=
\frac{M_q(Y)}{M_p(Y)}.
\]

With the p-weighted state measure

\[
d\nu_p
=
\frac{M_p}{\langle M_p\rangle}d\mu,
\]

the phase covariance is

\[
\boxed{
C_{phase}^{pq}
:=
\operatorname{Cov}_{\nu_p}
(\bar h_p,\bar w_p).
}
\]

Because the invariant p-moment identity gives

\[
\mathbb E_{\nu_p}[\bar h_p]=c_p,
\]

where

\[
c_p=1-\frac{3}{2p},
\]

we may write

\[
C_{phase}^{pq}
=
\mathbb E_{\nu_p}
\left[
(\bar h_p-c_p)\bar w_p
\right].
\]

## 3. Statewise logarithmic moment growth

The exact p-moment equation gives, for every nonzero state,

\[
\boxed{
\bar h_p-c_p
=
\frac1p\frac{M_p'}{M_p}
=
\frac1p\frac{d}{d\theta}\log M_p.
}
\]

Therefore

\[
\begin{aligned}
C_{phase}^{pq}
&=
\frac1{\langle M_p\rangle}
\left\langle
M_p
\left(\frac1p\frac{M_p'}{M_p}\right)
\frac{M_q}{M_p}
\right\rangle_\mu\\
&=
\boxed{
\frac1{p\langle M_p\rangle}
\left\langle
M_q\frac{d}{d\theta}\log M_p
\right\rangle_\mu.
}
\end{aligned}
\]

This is an exact representation of the phase covariance.

## 4. Periodic-orbit interpretation

Suppose first that the recurrent orbit is periodic with similarity period \(T\).

Then time averaging gives

\[
\boxed{
C_{phase}^{pq}
=
\frac1{p\langle M_p\rangle T}
\oint
M_q\,d(\log M_p).
}
\]

The relevant 1-form in the positive moment quadrant is

\[
\boxed{
\alpha_{pq}
:=
M_q\,d(\log M_p)
=
\frac{M_q}{M_p}dM_p.
}
\]

Its exterior derivative is

\[
\boxed{
d\alpha_{pq}
=
\frac1{M_p}\,dM_q\wedge dM_p,
}
\]

up to orientation sign convention.

Hence \(\alpha_{pq}\) is not exact on the two-dimensional moment plane.

A closed loop can therefore have

\[
\oint\alpha_{pq}\ne0.
\]

Thus positive phase covariance is geometrically an **oriented hysteresis area/circulation** in \((M_p,M_q)\)-space.

## 5. Why compact recurrence allows this circulation

A bounded state observable \(F(M_p,M_q)\) would satisfy

\[
\oint dF=0
\]

on a periodic orbit.

But

\[
\alpha_{pq}
=
\frac{M_q}{M_p}dM_p
\]

is not generally \(dF\).

Therefore

\[
\boxed{
C_{phase}^{pq}>0
\not\Rightarrow
\text{bounded-state monotone drift}.
}
\]

The state may return exactly to its initial moments while enclosing a nonzero oriented area each cycle.

This is the moment-space version of the M16-016 path-functional firewall.

## 6. Aperiodic recurrent interpretation

For a general invariant recurrent component, the same expression

\[
\left\langle
M_q(\log M_p)'
\right\rangle
\]

is a stationary circulation current in moment space.

It need not come from a periodic geometric loop, but it still represents an antisymmetric state-current rather than the derivative of one bounded scalar resource.

Hence the periodic conclusion extends structurally:

\[
\boxed{
\text{positive phase covariance}
=
\text{recurrent moment-space circulation},
}
\]

not consumptive accumulation.

## 7. Exact concentration-shape coordinate

Define the amplitude-concentration ratio

\[
\boxed{
\mathcal C_{pq}
:=
\frac{M_q^{1/q}}{M_p^{1/p}}.
}
\]

Using

\[
\frac1r\frac{d}{d\theta}\log M_r
=
\bar h_r-c_r,
\]

we obtain

\[
\boxed{
\frac{d}{d\theta}\log\mathcal C_{pq}
=
(\bar h_q-\bar h_p)
-(c_q-c_p).
}
\]

Thus concentration-shape growth is exactly the conditional p-to-q growth-field gap after subtracting the universal baseline shift

\[
\delta_{pq}=c_q-c_p.
\]

A phase with

\[
\bar h_q-\bar h_p>\delta_{pq}
\]

increases concentration, while a phase below that baseline decreases it.

## 8. Concentration-ratio compactness split

There are two possibilities.

### A. Nondegenerate concentration coordinate

If \(\mathcal C_{pq}\) remains bounded above and away from zero on the recurrent subcomponent under study, then

\[
\log\mathcal C_{pq}
\]

is a bounded state observable.

Invariant averaging yields

\[
\boxed{
\left\langle
\bar h_q-\bar h_p
\right\rangle_\mu
=
\delta_{pq}.
}
\]

The concentration coordinate executes recurrent growth/decay around this exact mean; no monotone contradiction follows.

### B. Concentration degeneration

If \(\mathcal C_{pq}\) approaches zero or otherwise loses compactness along the survivor, then the amplitude distribution is becoming increasingly diffuse/degenerate between the p- and q-scales.

This is a genuine

\[
\boxed{
G_{amplitude\ concentration/diffuse\ decompactification}
}
\]

branch and must be kept rather than dividing by \(\mathcal C_{pq}\) silently.

## 9. Fixed circulation forces moment variation

Assume \(M_q\le M_q^*<\infty\), which follows from the compact amplitude/enstrophy caps for fixed finite \(q\).

From Section 3,

\[
|C_{phase}^{pq}|
\le
\frac{M_q^*}{p\langle M_p\rangle}
\left\langle
\left|\frac{d}{d\theta}\log M_p\right|
\right\rangle.
\]

Therefore a fixed positive phase covariance

\[
C_{phase}^{pq}\ge c_*>0
\]

forces

\[
\boxed{
\left\langle
\left|\frac{d}{d\theta}\log M_p\right|
\right\rangle
\ge
c_*\,rac{p\langle M_p\rangle}{M_q^*}
>0.
}
\]

Thus the phase branch has a fixed positive total-variation rate in the p-moment scale.

This is a path cost, not yet a finite resource.

## 10. Temporal-thickness routing

On a compact smooth branch, \(M_p\) and its finite-order time derivatives are controlled on fixed similarity windows unless a time-jet decompactification occurs.

A fixed positive total-variation rate therefore produces repeated finite-amplitude concentration/deconcentration transitions with positive temporal thickness after a two-threshold extraction.

Failure of such thickness is a

\[
\boxed{
G_{time\text{-}jet/window\ decompactification}
}

exit of the M18-021 type.

If thickness holds, the branch is a genuine recurrent hysteresis cycle in the bounded moment variables.

## 11. Why total variation still does not close the cycle

Even with

\[
\left\langle| (\log M_p)' |\right\rangle>0,
\]

a periodic function can have the same positive variation on every period forever.

Thus

\[
\boxed{
\text{fixed moment variation per cycle}
\not\Rightarrow
\text{finite-resource exhaustion}.
}
\]

To close the branch, the circulation must be linked to

- a finite material label/flux resource;
- an unsigned derivative payment with non-summable ancestry growth;
- a bounded exact state potential after adding another variable;
- or a rigidity theorem forbidding the recurrent moment loop.

## 12. Audit verdict

### Certified

1. The recurrent-phase covariance has the exact circulation form
   \[
   C_{phase}^{pq}
   =
   [p\langle M_p\rangle]^{-1}
   \langle M_q(\log M_p)'\rangle.
   \]
2. On a periodic orbit it is an oriented line integral
   \[
   \oint M_q\,d\log M_p.
   \]
3. The corresponding 1-form is non-exact, so a closed recurrent cycle may carry nonzero circulation indefinitely.
4. The concentration ratio satisfies
   \[
   (\log\mathcal C_{pq})'
   =\bar h_q-\bar h_p-\delta_{pq}.
   \]
5. Fixed positive phase covariance forces a positive p-moment total-variation rate unless the moment/concentration coordinate degenerates.
6. Positive total variation remains a path functional and is not itself a contradiction.

### Still open

- physical/derivative cost of one concentration-deconcentration loop;
- whether adding a third moment makes the circulation exact or forces nonzero curvature of moment-space dynamics;
- concentration-coordinate degeneration;
- ancestry closure of any time-transition derivative payer;
- remote and critical roots;
- global regularity.

## 13. Next target

M18-067 should test whether the moment-space circulation can be converted into a **gradient/diffusion cost over one loop** using the exact identities

\[
\frac1rM_r'=A_r-D_r-c_rM_r
\]

for at least two exponents.

The key question is whether an oriented loop in \((M_p,M_q)\) necessarily carries a nonzero integrated difference of the weighted diffusion ratios

\[
\frac{D_q}{M_q}-\frac{D_p}{M_p},
\]

or whether strain source covariance can generate the loop without a new derivative cost beyond the already known palinstrophy firewall.