# M17-472 — Compact common-mode source return pays only ancestry-summable raw-H2 and palinstrophy plus endpoint temporal thickening, so no contradiction follows without multiplicity or duration gain

**Date:** 2026-09-10  
**Status:** ACTIVE SOURCE-RETURN NO-GO / SUMMABILITY FIREWALL

## 1. Scope

This module combines only previously certified reductions. It is a no-go/compression result: it identifies what the current common-mode source-return mechanism can and cannot prove.

Assume on a retained normalized CE-H record interval \(I=[t_0,t_1]\):

1. the exact M17-459/465 \(A\)-balance;
2. bounded normalized enstrophy \(E(t)\le E_*\);
3. the M17-462 amplitude hypothesis \(\rho\le M_\rho\) where that estimate is invoked;
4. the record-uniform zero-tube package of M17-470;
5. the record-uniform zero-level strain trace package of M17-460/471.

No termwise formula for \(\mathcal R_{\rm geom}\) is assumed.

## 2. Exact common-mode interval balance

M17-466 gives
\[
\boxed{
2\int_I G_{\rm cm}dt
=
\Delta A
+2\int_IJ_0dt
+2\int_IC_{0\sigma}dt
-2\int_IS_Adt
-2\int_I\Delta Qdt.
}
\]

Every non-endpoint term on the right has now been classified.

## 3. Zero-current term

M17-470 yields
\[
\boxed{
\int_IJ_0dt
\le
C_0\int_IH_{\rm raw}dt.
}
\]

## 4. Zero-level strain trace

M17-471 yields
\[
\boxed{
\int_I|C_{0\sigma}|dt
\le
C_H\int_IH_{\rm raw}dt
+C_P\int_IPdt.
}
\]

## 5. Second-moment sign asymmetry

M17-468 gives
\[
\boxed{
\left|\int_I\Delta Qdt\right|
\le
\int_IH_{\rm raw}dt.
}
\]

## 6. Strain-weighted first moment

M17-462 gives pointwise
\[
|S_A|
\lesssim
M_\rho E^{1/2}H_{\rm raw}^{1/2}.
\]
Thus, using \(E\le E_*\),
\[
\boxed{
\left|\int_IS_Adt\right|
\lesssim
M_\rho E_*^{1/2}|I|^{1/2}
\left(\int_IH_{\rm raw}dt\right)^{1/2}.
}
\]

Consequently, on normalized intervals whose lengths are uniformly controlled, a persistent order-one \(S_A\) contribution forces a positive raw-H2 spacetime payment. This is a resource lower bound, not a contradiction.

## 7. Endpoint term

M17-469 gives
\[
A^2\le EH_{\rm raw}.
\]
Hence a nontrivial endpoint jump \(|\Delta A|\) under bounded endpoint enstrophy forces an instantaneous raw-H2 spike at at least one endpoint.

However
\[
H_{\rm raw}(t_i)\gtrsim1
\]
does not imply
\[
\int_IH_{\rm raw}dt\gtrsim1
\]
without a quantitative temporal-thickening/high-jet theorem.

Therefore the endpoint channel remains the explicit exit
\[
\boxed{G_{\rm endpoint\ spike/temporal\ thickening}.}
\]

## 8. Compact source-return inequality

Collecting the estimates, there are constants depending only on the retained normalized compactness parameters such that
\[
\boxed{
\begin{aligned}
2\left|\int_I G_{\rm cm}dt\right|
\le{}&
|\Delta A|
+C_1\int_IH_{\rm raw}dt
+C_2\int_IPdt\\
&+C_3|I|^{1/2}
\left(\int_IH_{\rm raw}dt\right)^{1/2}.
\end{aligned}
}
\]

Thus a persistent common-mode interval source cannot be sustained for free. Under the compactness assumptions, it must be accompanied by:

- endpoint first-moment change;
- raw-H2 spacetime cost;
- palinstrophy spacetime cost.

## 9. Why this still does not contradict the ancestral solution

The certified ancestry ledgers are
\[
\boxed{
\sum_mR_m^{-3}
\int_IH_{{\rm raw},m}ds<\infty,
}
\]
\[
\boxed{
\sum_mR_m^{-1}
\int_IP_mds<\infty.
}
\]

For geometric records,
\[
\sum_mR_m^{-3}<\infty,
\qquad
\sum_mR_m^{-1}<\infty.
\]

Therefore an order-one normalized payment on one interval at each record scale can be completely compatible with the parent finite-resource ledgers.

This yields the central no-go statement:
\[
\boxed{
\text{fixed normalized source-return cost per geometric record}
\not\Rightarrow
\text{contradiction}.
}
\]

The source-return analysis has compressed the branches, but current ancestry accounting still permits them.

## 10. What would be needed to escape the firewall

A contradiction from this route requires at least one additional mechanism that defeats geometric summability. Examples of mathematically distinct possibilities are:

1. **record multiplicity gain:** sufficiently many essentially disjoint payable events at scale \(R_m\);
2. **duration gain:** normalized residence time growing fast enough that the total charge per record is not \(O(1)\);
3. **allocation theorem:** the same parent raw-H2/palinstrophy resource cannot be reused across the relevant descendant events, with multiplicity exceeding the summable ancestry weights;
4. **stronger scale lower bound:** a cost whose parent conversion has a non-summable weight;
5. **compactness failure:** high-jet, zero-tube, trace, topology, interface, or genealogy decompactification becomes the actual terminal branch.

M17-472 proves none of these mechanisms; it identifies them as the only ways this particular source-return route can continue toward a contradiction.

## 11. Updated source-return branch

Under the compact normalized assumptions,
\[
\boxed{
\begin{aligned}
G_{\rm common\text{-}mode\ source\ return}
\Longrightarrow{}&
G_{\rm raw\text{-}H^2}^{R^{-3}\ \rm summable}\\
&\lor G_{\rm palinstrophy}^{R^{-1}\ \rm summable}\\
&\lor G_{\rm endpoint\ temporal\ thickening}\\
&\lor G_{\rm multiplicity/duration/allocation\ gain}\\
&\lor G_{\rm high\text{-}jet/zero\text{-}tube/trace\ collapse}\\
&\lor G_{\rm interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

The raw-H2 and palinstrophy branches are **classified but not contradictory**.

## 12. Relation to the wider diffuse CE-H frontier

M17-472 concerns only the M17-459--471 common-mode source-return chain. It does not close:

- positive-flux thinning;
- extra transverse size dilution;
- scale-free transverse shape/spectral degeneration;
- remote negative compensation;
- thin/localized moderate-negative interface;
- good-time thinning;
- normalized high-jet/scale mismatch;
- normal-chart/topology loss;
- parent-to-record scale-map/genealogy failure.

## 13. Audit status

Closed/reduced here:

- any claim that the compact common-mode source-return chain alone already contradicts finite ancestral resources;
- any attempt to count one fixed normalized raw-H2/palinstrophy payment per geometric record as automatically divergent.

Still OPEN:

- multiplicity/duration/allocation gain;
- endpoint temporal thickening;
- compactness/high-jet/tube exits;
- termwise provenance of \(\mathcal R_{\rm geom}\);
- wider diffuse CE-H exits;
- ROOT-CERT and non-CE-H roots.

## 14. Next target

Audit the weakest possible multiplicity/duration condition needed to overturn the \(R^{-3}\) and \(R^{-1}\) summability firewalls. The target should be a threshold theorem, not an assumption that every record has many disjoint events.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
