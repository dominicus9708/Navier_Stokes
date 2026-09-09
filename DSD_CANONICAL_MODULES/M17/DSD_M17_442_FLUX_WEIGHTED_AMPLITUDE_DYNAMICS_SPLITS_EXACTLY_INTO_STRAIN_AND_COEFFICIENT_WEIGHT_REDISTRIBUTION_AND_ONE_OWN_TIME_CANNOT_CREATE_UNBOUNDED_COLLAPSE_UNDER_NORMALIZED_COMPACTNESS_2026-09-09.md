# DSD M17-442 — Flux-weighted normalized amplitude dynamics split exactly into strain and coefficient-weight redistribution, and one own-time cannot create unbounded collapse under normalized compactness

Date: 2026-09-09  
Canonical ID: **M17-442**

Status: **ACTIVE AMPLITUDE-DYNAMICS DECOMPOSITION / COEFFICIENT-REDISTRIBUTION FRONTIER**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Goal

M17-440--441 reduce quadratic flux dilution at retained positive flux to a summable collapse of the flux-weighted normalized amplitude

\[
\mathfrak a_\Phi.
\]

The present module asks what exact dynamics can produce that collapse.

The answer is: on a coherent positive material-flux family, there is no separate `area source`. The logarithmic derivative of `mathfrak a_Phi` is exactly a combination of flux-weighted strain and coefficient-weight redistribution.

## 2. Fixed own-scale normalization

Work on one physical own-scale record interval with fixed normalization radius `r`.

For each coherent material flux element, define

\[
q:=r^2\rho.
\]

Exact CE-H material amplitude transport gives

\[
\boxed{
D_tq=(\sigma+\nu\kappa)q.
}
\]

For the positive material flux measure, the exact CE-H flux law gives

\[
\boxed{
\partial_t(d\Phi)=\nu\kappa\,d\Phi.
}
\]

This is the differential measure form of `D_t log Phi = nu kappa` on coherent material tube labels.

If material genealogy, positive orientation, or the common CE-H tube representation fails, retain the corresponding explicit exit instead of using this section.

## 3. Total flux and quadratic currency

Define

\[
\Phi:=\int d\Phi,
\]

and

\[
Q:=\int q\,d\Phi.
\]

By M17-440,

\[
\boxed{
Q=\mathfrak Q_\Phi,
\qquad
\mathfrak a_\Phi=Q/\Phi.
}
\]

Differentiate total flux:

\[
\boxed{
\dot\Phi
=\nu\int\kappa\,d\Phi.
}
\]

Differentiate the quadratic currency:

\[
\begin{aligned}
\dot Q
&=\int D_tq\,d\Phi
+\int q\,\partial_t(d\Phi)\\
&=\int(\sigma+\nu\kappa)q\,d\Phi
+\nu\int\kappa q\,d\Phi\\
&=\int(\sigma+2\nu\kappa)q\,d\Phi.
\end{aligned}
\]

Thus

\[
\boxed{
\dot Q
=\int(\sigma+2\nu\kappa)q\,d\Phi.
}
\]

## 4. Two canonical probability measures

Define the positive flux probability

\[
\boxed{
dp:=\frac{d\Phi}{\Phi}
}
\]

and the quadratic-payer probability

\[
\boxed{
d\widehat p:=\frac{q\,d\Phi}{Q}.
}
\]

Then

\[
\frac{\dot\Phi}{\Phi}
=\nu\langle\kappa\rangle_p,
\]

while

\[
\frac{\dot Q}{Q}
=\langle\sigma+2\nu\kappa\rangle_{\widehat p}.
\]

Since

\[
\mathfrak a_\Phi=Q/\Phi,
\]

we obtain the exact identity

\[
\boxed{
\frac d{dt}\log\mathfrak a_\Phi
=
\langle\sigma\rangle_{\widehat p}
+\nu\left(
2\langle\kappa\rangle_{\widehat p}
-\langle\kappa\rangle_p
\right).
}
\]

This is the central M17-442 formula.

## 5. Coefficient covariance form

Because

\[
\langle\kappa\rangle_{\widehat p}
=\frac{\langle q\kappa\rangle_p}{\langle q\rangle_p},
\qquad
\langle q\rangle_p=\mathfrak a_\Phi,
\]

we have

\[
\langle\kappa\rangle_{\widehat p}
-\langle\kappa\rangle_p
=
\frac{\operatorname{Cov}_p(q,\kappa)}{\mathfrak a_\Phi}.
\]

Therefore

\[
\boxed{
\frac d{dt}\log\mathfrak a_\Phi
=
\langle\sigma\rangle_{\widehat p}
+\nu\langle\kappa\rangle_{\widehat p}
+\nu\frac{\operatorname{Cov}_p(q,\kappa)}{\mathfrak a_\Phi}.
}
\]

Thus the coefficient contribution consists of a payer-weighted mean coefficient plus a coefficient-amplitude segregation/covariance term.

No independent geometric-area production term appears.

## 6. Single-label cancellation as a consistency check

For one coherent infinitesimal material tube label, let its flux be `phi` and normalized amplitude be `q`.

Then

\[
\frac d{dt}\log q=\sigma+\nu\kappa,
\qquad
\frac d{dt}\log\phi=\nu\kappa.
\]

Hence

\[
\boxed{
\frac d{dt}\log\frac{q}{\phi}=\sigma.
}
\]

So on one material label, coefficient diffusion changes amplitude and flux together; their relative change is pure strain.

The extra coefficient term in the aggregate M17-442 identity comes entirely from redistribution of flux weight among labels with different `kappa` and different `q`.

## 7. One-own-time compactness firewall

Assume on an own-scale interval of duration

\[
|I_r|\le C_tr^2/\nu
\]

that the normalized strain and coefficient remain bounded on the retained flux family:

\[
\boxed{
r^2|\sigma|\le S_*,
\qquad
r^2|\kappa|\le K_*.
}
\]

Then

\[
\left|
\frac d{dt}\log\mathfrak a_\Phi
\right|
\le
\|\sigma\|_\infty
+3\nu\|\kappa\|_\infty
\lesssim
r^{-2}(S_*+3\nu K_*).
\]

Integrating over one own-time gives

\[
\boxed{
\left|
\log\frac{\mathfrak a_\Phi(t_1)}{\mathfrak a_\Phi(t_0)}
\right|
\le C(S_*,K_*,C_t,\nu).
}
\]

Therefore one own-time cannot create an arbitrarily large amplitude-collapse factor while normalized strain/coefficient compactness persists.

Unbounded one-step collapse forces normalized strain/coefficient decompactification, label-state/genealogy loss, or failure of the coherent positive-flux representation.

## 8. But gradual summable collapse remains possible

M17-441 requires, on retained positive-flux and positive-good-time geometric records,

\[
\sum_m\mathfrak a_{\Phi,m}<\infty.
\]

At the power threshold one may have

\[
\mathfrak a_{\Phi,m}\sim m^{-p},
\qquad p>1.
\]

The logarithmic decrement from record `1` to record `m` is only

\[
\left|\log\mathfrak a_{\Phi,m}\right|
\sim p\log m
\sim p\log\log R_m.
\]

A parent record window contains `O(R_m^2)` own-time units, so normalized compactness alone does not prevent such a very slow cumulative collapse.

Therefore M17-442 is a dynamics classification, not a contradiction theorem.

## 9. Relation to M17-434--438

M17-434--438 strongly constrain a **single retained positive-flux own-scale loop/tube history**: long sign-preserving coefficient phases force flux amplification/thinning or many zero transitions, and compact regular finite-order transitions close by the raw-`H2` ancestry ledger.

M17-442 shows the aggregate amplitude-collapse survivor can still avoid that single-label mechanism only by one of the following:

1. flux measure continually redistributes among labels with different coefficient histories;
2. individual flux labels thin while total positive flux is replenished elsewhere;
3. coefficient-amplitude covariance decompactifies;
4. good-time/scale/tube/genealogy compactness fails;
5. normalized strain/coefficient bounds fail.

Thus the new narrow object is not generic area dispersion but **flux-measure redistribution coupled to coefficient/amplitude covariance**.

## 10. Updated branch split

\[
\boxed{
\begin{aligned}
G_{summable\ flux\text{-}weighted\ amplitude\ collapse}
\Longrightarrow{}&
G_{negative\ payer\text{-}weighted\ strain\ action}\\
&\lor G_{coefficient\ mean/covariance\ redistribution}\\
&\lor G_{positive\ flux\ replenishment/turnover}\\
&\lor G_{normalized\ strain/coefficient\ decompactification}\\
&\lor G_{scale/tube/genealogy/interface\ loss}.
\end{aligned}
}
\]

The coefficient-covariance/replenishment route is the genuinely new aggregate frontier left after the single-loop zero-transition closures.

## 11. DSD audit role

DSD is used only to separate single-label material dynamics from ensemble measure reweighting. The proof is differentiation of positive measures and exact CE-H transport laws.

## 12. Audit verdict

**PASS — flux-weighted amplitude collapse has an exact dynamical payer identity.**

Under normalized compactness it cannot occur in one abrupt own-time event, but the summable gradual collapse required by M17-441 remains compatible with current local estimates through coefficient/flux-measure redistribution. That redistribution is the next narrow late-CE-H target.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
