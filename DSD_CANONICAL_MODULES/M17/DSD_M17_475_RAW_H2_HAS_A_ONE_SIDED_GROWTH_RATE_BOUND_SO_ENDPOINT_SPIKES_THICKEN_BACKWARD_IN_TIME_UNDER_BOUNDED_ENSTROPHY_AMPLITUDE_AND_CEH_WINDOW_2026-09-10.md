# M17-475 — Raw-H2 has a one-sided growth-rate bound, so endpoint spikes thicken backward in time under bounded enstrophy, amplitude, and CE-H window

**Date:** 2026-09-10  
**Status:** ACTIVE TEMPORAL-THICKENING THEOREM / ENDPOINT SPIKE REDUCTION

## 1. Scope

M17-469 left an endpoint debt:
\[
A(t_i)^2\le E(t_i)H_{\rm raw}(t_i)
\]
forces an instantaneous raw-H2 spike, but a snapshot lower bound was not yet a spacetime payment.

M17-474 identified temporal thickening as the nearest unresolved mechanism.

This module derives a **one-sided upper bound on the growth rate** of
\[
H(t):=H_{\rm raw}(t)=\|\Delta\Omega(t)\|_2^2
\]
in the whole-space smooth CE-H regime. The key point is that viscous third-derivative dissipation is negative and therefore cannot make an upward spike form faster.

The result requires a backward time interval contained in the same smooth whole-space CE-H branch and bounded enstrophy/vorticity amplitude there.

## 2. Vorticity equation and H derivative

The physical vorticity equation is
\[
\partial_t\Omega+u\cdot\nabla\Omega
=
\Omega\cdot\nabla u+\nu\Delta\Omega,
\qquad
\nabla\cdot u=0.
\]

Let
\[
H=\|\Delta\Omega\|_2^2.
\]
Then
\[
\frac12H'
=
\int\Delta\Omega\cdot\Delta\partial_t\Omega\,dx.
\]
Substitution gives
\[
\frac12H'
+
\nu\|\nabla\Delta\Omega\|_2^2
=
-\int\Delta\Omega\cdot\Delta(u\cdot\nabla\Omega)dx
+
\int\Delta\Omega\cdot\Delta(\Omega\cdot\nabla u)dx.
\]

The top transport term cancels:
\[
\int\Delta\Omega\cdot(u\cdot\nabla\Delta\Omega)dx=0.
\]

## 3. Commutator expansion

Expand
\[
\Delta(u\cdot\nabla\Omega)
=
u\cdot\nabla\Delta\Omega
+2\partial_i u\cdot\partial_i\nabla\Omega
+\Delta u\cdot\nabla\Omega,
\]
where the first term is \(u\cdot\nabla\Delta\Omega\) (the displayed leading character should be read as \(u\), not viscosity; no viscosity is present in this algebraic expansion).

Similarly,
\[
\Delta(\Omega\cdot\nabla u)
=
\Omega\cdot\nabla\Delta u
+2\partial_i\Omega\cdot\partial_i\nabla u
+\Delta\Omega\cdot\nabla u.
\]

Therefore the nonlinear contribution is bounded by terms of the forms
\[
\|\nabla u\|_\infty H,
\qquad
\|\Omega\|_\infty H,
\qquad
\|\nabla\Omega\|_4^2H^{1/2}.
\]

In the whole-space finite-energy setting, Calderón--Zygmund/Biot--Savart estimates give
\[
\|D^2u\|_4\lesssim\|\nabla\Omega\|_4,
\qquad
\|D^3u\|_2\lesssim\|D^2\Omega\|_2.
\]
Thus
\[
\boxed{
\frac12H'
+
u\|\nabla\Delta\Omega\|_2^2
\le
C(\|\nabla u\|_\infty+\|\Omega\|_\infty)H
+C\|\nabla\Omega\|_4^2H^{1/2}.
}
\]

## 4. Reduction to E, H, and amplitude

Let
\[
E=\|\Omega\|_2^2,
\qquad
P=\|\nabla\Omega\|_2^2.
\]

First,
\[
P
=-\int\Omega\cdot\Delta\Omega dx
\le E^{1/2}H^{1/2}.
\]
Hence
\[
\boxed{P\le E^{1/2}H^{1/2}.}
\]

Next, the 3D Gagliardo--Nirenberg inequality gives
\[
\|\nabla\Omega\|_4
\lesssim
\|\nabla\Omega\|_2^{1/4}
\|D^2\Omega\|_2^{3/4},
\]
so
\[
\|\nabla\Omega\|_4^2H^{1/2}
\lesssim
P^{1/4}H^{5/4}
\lesssim
E^{1/8}H^{11/8}.
\]

For the velocity gradient,
\[
\nabla u=\Sigma+A,
\]
where the antisymmetric part \(A\) is pointwise controlled by \(|\Omega|\). M17-385 supplies
\[
\|\Sigma\|_\infty
\lesssim E^{1/8}H^{3/8}.
\]
Therefore, if
\[
\|\Omega\|_\infty\le M_\rho,
\]
then
\[
\|\nabla u\|_\infty
\lesssim
M_\rho+E^{1/8}H^{3/8}.
\]

Substitution yields
\[
\boxed{
\frac12H'
+
u\|\nabla\Delta\Omega\|_2^2
\le
C M_\rho H
+C E^{1/8}H^{11/8}.
}
\]
Dropping the nonnegative dissipation term gives the one-sided growth inequality
\[
\boxed{
H'
\le
C_1M_\rho H
+C_2E^{1/8}H^{11/8}.
}
\]

This is the key temporal-thickening estimate.

## 5. Why only the one-sided derivative is needed

The absolute derivative \(|H'|\) contains the viscous high-jet term
\[
\nu\|\nabla\Delta\Omega\|_2^2
\]
and would require a separate high-jet variation estimate.

For backward thickening of an **upward endpoint spike**, however, only an upper bound on positive growth is needed. Viscosity lowers \(H\), so it cannot accelerate the rise from \(h/2\) to \(h\).

Thus M17-475 avoids paying a third-derivative ledger merely to establish a minimum spike-formation time.

## 6. Doubling-time lower bound

Assume on a backward CE-H interval
\[
E(t)\le E_*,
\qquad
\|\Omega(t)\|_\infty\le M_*.
\]
Suppose \(H\) rises from \(h/2\) to \(h\) while remaining in
\[
h/2\le H(t)\le h.
\]
Then
\[
\frac{H'}{H}
\le
C\left(M_*+E_*^{1/8}h^{3/8}\right).
\]
Integrating over the crossing interval \([t_-,t_+]\),
\[
\log2
\le
C\left(M_*+E_*^{1/8}h^{3/8}\right)(t_+-t_-).
\]
Therefore
\[
\boxed{
 t_+-t_-
\ge
\frac{\log2}
{C\left(M_*+E_*^{1/8}h^{3/8}\right)}.
}
\]

## 7. Spacetime raw-H2 thickening

Throughout the crossing,
\[
H(t)\ge h/2.
\]
Hence
\[
\int_{t_-}^{t_+}H(t)dt
\ge
\frac h2(t_+-t_-).
\]
Combining with the doubling-time bound,
\[
\boxed{
\int_{t_-}^{t_+}H(t)dt
\ge
\frac{h\log2}
{2C\left(M_*+E_*^{1/8}h^{3/8}\right)}.
}
\]

For large \(h\) with \(E_*,M_*\) fixed,
\[
\boxed{
\int Hdt
\gtrsim
E_*^{-1/8}h^{5/8}.
}
\]

For a fixed normalized endpoint height \(h\gtrsim h_*>0\), bounded \(E_*\) and \(M_*\) give a fixed positive normalized spacetime raw-H2 payment.

## 8. Terminal endpoint formulation

Let \(t_1\) be the endpoint of a backward available CE-H window of length \(T>0\), with
\[
H(t_1)=h>0.
\]
There are two cases.

### Case A: no half-height crossing occurs

If
\[
H(t)\ge h/2
\quad\text{for all }t\in[t_1-T,t_1],
\]
then
\[
\boxed{
\int_{t_1-T}^{t_1}Hdt\ge\frac h2T.
}
\]

### Case B: a last half-height crossing occurs

Let \(t_-\) be the last time before \(t_1\) with
\[
H(t_-)=h/2,
\]
and \(H\in[h/2,h]\) until its first subsequent attainment of \(h\). Then Section 7 applies.

Thus in either case,
\[
\boxed{
\int_{t_1-T}^{t_1}Hdt
\ge
\frac h2
\min\left\{
T,
\frac{\log2}{C(M_*+E_*^{1/8}h^{3/8})}
\right\}.
}
\]

This is the endpoint temporal-thickening theorem.

## 9. Combination with M17-469

M17-469 gives, under endpoint enstrophy control,
\[
|\Delta A|\ge a_*
\quad\Longrightarrow\quad
H(t_i)\ge\frac{a_*^2}{E_*}
\]
at at least one endpoint.

If that endpoint has a backward CE-H window satisfying the M17-475 bounds, then the snapshot raw-H2 spike acquires an explicit positive spacetime thickness through Section 8.

Therefore the previous endpoint debt reduces to
\[
\boxed{
G_{\rm endpoint\ spike}
\Longrightarrow
G_{\rm spacetime\ raw\text{-}H^2}
\lor
G_{E\text{-decompactification}}
\lor
G_{\rho_\infty\text{-}decompactification}
\lor
G_{\rm CE\text{-}H/time\text{-}window/genealogy\ loss}.
}
\]

## 10. Scaling and ancestry firewall

M17-475 supplies temporal thickness, but for a fixed normalized spike height and fixed normalized compactness constants it gives only an order-one normalized raw-H2 payment.

By M17-467/404--405, this still converts to the parent with cubic ancestry weight
\[
R_m^{-3}.
\]
Thus
\[
\boxed{
\text{endpoint temporal thickening closes a local debt but does not by itself defeat cubic ancestry summability.}
}
\]

If normalized spike heights \(h_m\) decompactify, the large-height lower bound grows like \(h_m^{5/8}\). M17-473 then supplies the exact weighted-series test; no contradiction is asserted without checking that growth against \(R_m^{-3}\).

## 11. Audit caveats

- The estimate is whole-space and uses the Biot--Savart/Calderón--Zygmund velocity-vorticity relation. Domain/harmonic components must be treated separately outside this setting.
- The backward interval must remain within the same smooth CE-H/genealogically certified regime.
- Uniform \(E_*\) and \(M_*\) are explicit assumptions; their failure is an exit, not a contradiction.
- This is a one-sided spike-formation estimate. It does not bound arbitrarily fast downward decay without a high-jet estimate.

## 12. Audit status

Reduced/closed here:

- endpoint raw-H2 snapshot as an unthickened debt under bounded enstrophy/amplitude and an available backward CE-H window.

Still OPEN:

- whether normalized spike heights can grow strongly enough to meet M17-473's cubic threshold;
- amplitude/enstrophy decompactification;
- loss of backward CE-H/time-window/genealogy persistence;
- non-reusable allocation across records;
- high-jet/tube/interface exits;
- root-level dependencies.

## 13. Next target

Insert M17-475 back into M17-472. Under bounded enstrophy/amplitude and compact zero-tube/trace/time-window hypotheses, the entire common-mode source-return branch should collapse to ancestry-summable raw-H2 plus palinstrophy. Then audit the residual decompactification exits separately rather than continuing to search for an internal common-mode payer.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
