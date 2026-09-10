# M17-477 — Endpoint spike thickening can defeat cubic ancestry only through supercritical H growth or compactness loss

**Date:** 2026-09-10  
**Status:** ACTIVE ENDPOINT-ANCESTRY THRESHOLD THEOREM / COEFFICIENT-SCALE DECOMPACTIFICATION REDUCTION

## 1. Purpose

M17-475 converts a normalized endpoint raw-\(H^2\) spike of height
\[
h=H_{\rm raw}(t_i)
\]
into a positive normalized spacetime raw-\(H^2\) payment.

M17-476 then shows that endpoint growth is the only non-bulk part of the compact common-mode source-return branch.

This module asks a sharper question:

> Can the M17-475 endpoint-thickening lower bound by itself grow fast enough with record scale to defeat the cubic ancestry weight \(R_m^{-3}\)?

The answer is: only if the normalized spike height grows at a supercritical rate. Under bounded enstrophy, such growth forces coefficient-scale decompactification.

## 2. M17-475 thickened endpoint charge

Let
\[
h_m:=H_{{\rm raw},m}(t_{i,m}).
\]
On a backward normalized CE-H window of length at least \(\tau_*>0\), with
\[
E_m(t)\le E_*,
\qquad
\|\Omega_m(t)\|_\infty\le M_*,
\]
M17-475 gives
\[
q_m^{\rm end}
:=
\int_{J_m}H_{{\rm raw},m}(s)ds
\ge
\frac{h_m}{2}
\min\left\{
\tau_*,
\frac{\log2}{C(M_*+E_*^{1/8}h_m^{3/8})}
\right\}.
\]

For sufficiently large \(h_m\), with \(E_*,M_*,\tau_*\) fixed,
\[
\boxed{
q_m^{\rm end}
\gtrsim
E_*^{-1/8}h_m^{5/8}.
}
\]

This exponent \(5/8\) is the exact growth supplied by the presently certified one-sided thickening estimate.

## 3. Cubic ancestry test

M17-404--405 and M17-467 give the parent ledger
\[
\boxed{
\sum_mR_m^{-3}q_m^{\rm end}<\infty
}
\]
for any genuine bounded-overlap family coming from the certified ancestor.

Therefore the M17-475 lower bound could contradict that ledger only if
\[
\boxed{
\sum_mR_m^{-3}h_m^{5/8}=\infty
}
\]
up to the fixed compactness constants.

This is the exact series criterion for the endpoint-thickening mechanism presently available.

## 4. Power-law threshold on geometric records

Assume geometric record ratios
\[
R_m\asymp\Lambda^m,
\qquad \Lambda>1,
\]
and model the normalized spike growth by
\[
h_m\asymp R_m^\beta.
\]
Then
\[
R_m^{-3}h_m^{5/8}
\asymp
R_m^{-3+5\beta/8}.
\]

Thus the power-law critical exponent is
\[
-3+\frac{5\beta}{8}=0,
\]
so
\[
\boxed{
\beta_c=\frac{24}{5}=4.8.
}
\]

Hence:

- if \(\beta>24/5\), the M17-475 lower bound is supercritical with respect to cubic ancestry;
- if \(\beta=24/5\), it produces order-one parent terms and therefore already defeats geometric summability if it occurs on infinitely many non-reused records;
- if \(\beta<24/5\), the M17-475 lower bound alone is subcritical and does not force divergence.

The last statement is only a limitation of this lower bound; it does not prove that the true spacetime charge is small.

## 5. Endpoint height versus coefficient amplitude

On exact CE-H,
\[
\Delta\Omega=\kappa\Omega.
\]
Therefore
\[
H_{\rm raw}
=
\int\kappa^2|\Omega|^2dx
\le
\|\kappa\|_\infty^2E.
\]

Thus if
\[
E\le E_*,
\]
then
\[
\boxed{
\|\kappa\|_\infty
\ge
E_*^{-1/2}H_{\rm raw}^{1/2}.
}
\]

Consequently, power-law endpoint growth
\[
h_m\gtrsim R_m^{24/5}
\]
forces
\[
\boxed{
\|\kappa_m\|_\infty
\gtrsim
E_*^{-1/2}R_m^{12/5}.
}
\]

Therefore the endpoint mechanism cannot defeat cubic ancestry while both normalized enstrophy and normalized coefficient amplitude remain compact.

## 6. Intrinsic coefficient scale

Define the intrinsic coefficient scale
\[
r_{\kappa,m}
:=
\|\kappa_m\|_\infty^{-1/2}.
\]
The threshold from Section 5 gives, heuristically at the power-law critical rate,
\[
\boxed{
r_{\kappa,m}\lesssim R_m^{-6/5}.}
\]

This should not be interpreted as a contradiction. It means that the nominal record scale is no longer the true coefficient scale.

By the M17-393 firewall, large normalized \(|\kappa|\) is to be classified as

- migration to a smaller intrinsic coefficient scale;
- normalized coefficient-scale decompactification;
- or, if spatial variation is required to connect scales, a coefficient-gradient/high-jet/interface exit.

It is not an independent scalar spike branch.

## 7. Compact coefficient corollary

If in addition to bounded normalized enstrophy one has
\[
\|\kappa_m\|_\infty\le K_*
\]
uniformly on the record family, then
\[
h_m\le K_*^2E_*.
\]
Hence M17-475 supplies at most a fixed normalized endpoint-thickening payment scale, and the ancestral contribution remains of the form
\[
O(R_m^{-3}).
\]

Therefore
\[
\boxed{
\text{uniform coefficient compactness excludes endpoint-height growth as a mechanism for defeating cubic ancestry.}
}
\]

Any contradiction must then come from multiplicity/non-reuse, a different resource, or a compactness/genealogy exit.

## 8. Full endpoint threshold split

The endpoint branch is refined to
\[
\boxed{
\begin{aligned}
G_{\rm endpoint\ thickening\ defeats\ cubic\ ancestry}
\Longrightarrow{}&
G_{\kappa_\infty\text{-decompactification}/\,intrinsic\ scale\ migration}\\
&\lor G_{E\text{-decompactification}}\\
&\lor G_{\rho_\infty\text{-decompactification}}\\
&\lor G_{\rm time\text{-}window\ thinning}\\
&\lor G_{\rm nonreuse/multiplicity\ enhancement}\\
&\lor G_{\rm genealogy/interface/domain\ loss}.
\end{aligned}
}
\]

The \(\rho_\infty\) and time-window branches appear because growth of those constants can weaken the M17-475 temporal-thickening lower bound.

## 9. Relation to M17-473

M17-473 states that a generic normalized raw-\(H^2\) charge \(Q_m\) must be roughly cubic in \(R_m\), in the power-law sense, to defeat the \(R_m^{-3}\) ancestry weight.

M17-477 is the endpoint specialization. Since M17-475 produces only
\[
Q_m\gtrsim h_m^{5/8},
\]
the endpoint height itself must be much larger:
\[
\boxed{
h_m\sim R_m^{24/5}}
\]
at the power-law threshold.

This explains quantitatively why an unbounded snapshot spike is not automatically useful for the global contradiction.

## 10. Audit cautions

- The \(24/5\) threshold is the threshold for the **currently certified M17-475 lower bound**, not a universal Navier--Stokes critical exponent.
- A subcritical M17-475 lower bound does not prove that the actual spacetime raw-\(H^2\) charge is subcritical.
- The ancestry comparison requires representation-safe parent-to-record mapping and bounded-overlap/non-reuse certification.
- The coefficient bound uses exact CE-H. Outside that branch the implication is unavailable.
- Large \(\|\kappa\|_\infty\) must be routed through the M17-393 intrinsic-scale migration firewall rather than counted twice as an independent event.

## 11. Audit status

Reduced here:

- endpoint spike-height growth as an unspecified possible way around the cubic ancestry firewall.

Now quantified:

\[
\sum_mR_m^{-3}h_m^{5/8}=\infty
\]
is required for the M17-475 endpoint-thickening lower bound itself to defeat ancestry;
for power-law geometric records this means \(h_m\) reaches the \(R_m^{24/5}\) threshold.

Still OPEN:

- whether intrinsic coefficient-scale migration can be canonically re-recorded with sufficient non-reuse to improve ancestry allocation;
- whether multiplicity/residence can reach the M17-473 thresholds;
- whether enstrophy/amplitude decompactification can be tied to a certified nonsummable standard-energy resource;
- parent-to-M17 persistence and all root-level dependencies.

## 12. Next target

Audit the coefficient-scale migration branch produced here. The key question is whether re-recording a large-\(\kappa\) endpoint at its intrinsic scale merely restores an order-one normalized event with a new cubic ancestry weight, or whether the scale migration creates a genuine non-reusable multiplicity gain. This must be checked before treating coefficient decompactification as progress toward contradiction.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
