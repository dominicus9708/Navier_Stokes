# DSD M17-368 — Flux-area control breaks amplitude homogeneity and gives a raw H2 lower bound for flux-bearing critical coefficient tubes

Date: 2026-09-08  
Canonical ID: **M17-368**

Status: **ACTIVE FLUX-AMPLITUDE BRIDGE / CONDITIONAL RAW-H2 LOWER BOUND**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why flux is the missing datum

M17-367 proves that the CE-H equation

\[
\Delta W=\kappa W
\]

is invariant under

\[
W\mapsto\varepsilon W,
\]

so no `kappa`-only quantity can force a positive raw

\[
H:=\int|\Delta W|^2
\]

lower bound.

A material vorticity-flux floor breaks that amplitude homogeneity because shrinking `W` while keeping the same geometric cross-section also shrinks the flux.

## 2. Regular tube band

Let `T` be a regular vortex-tube band parameterized by material flux labels and arclength.

For each arclength position `s`, let `Sigma_s` be a transverse cross-section of the band. Because

\[
\nabla\cdot W=0,
\]

the oriented vorticity flux through homologous tube cross-sections is independent of `s`:

\[
\boxed{
\phi
:=
\int_{\Sigma_s}W\cdot n\,dA
>0.
}
\]

Assume

\[
\boxed{|\Sigma_s|\le A_*}
\]

through a retained arclength interval of length at least

\[
\boxed{\ell_* >0.}
\]

Assume also that on the corresponding coefficient subband

\[
\boxed{|\kappa|\ge\kappa_*>0.}
\]

If the coefficient condition holds only on a positive-flux subband, restrict `T` to that subband before applying the estimate.

## 3. Cross-sectional amplitude floor from flux

On a positively oriented tube cross-section,

\[
\phi
\le
\int_{\Sigma_s}|W|dA.
\]

Cauchy--Schwarz gives

\[
\left(\int_{\Sigma_s}|W|dA\right)^2
\le
|\Sigma_s|
\int_{\Sigma_s}|W|^2dA.
\]

Therefore

\[
\boxed{
\int_{\Sigma_s}|W|^2dA
\ge
\frac{\phi^2}{|\Sigma_s|}
\ge
\frac{\phi^2}{A_*}.
}
\]

This is the required amplitude-return statement at the tube level.

## 4. Raw H2 lower bound

On CE-H,

\[
|\Delta W|^2
=\kappa^2|W|^2.
\]

Hence at each cross-section in the retained coefficient band,

\[
\int_{\Sigma_s}|\Delta W|^2dA
\ge
\kappa_*^2
\int_{\Sigma_s}|W|^2dA
\ge
\kappa_*^2\frac{\phi^2}{A_*}.
\]

Integrating along arclength gives

\[
\boxed{
H_T
:=
\int_T|\Delta W|^2dy
\ge
\kappa_*^2
\frac{\phi^2}{A_*}
\ell_*.
}
\]

Thus material flux plus transverse geometry breaks the M17-367 amplitude symmetry and converts a coefficient lower scale directly into raw `H2` charge.

## 5. Companion enstrophy lower bound

The same cross-sectional estimate gives

\[
E_T
:=
\int_T|W|^2dy
\ge
\boxed{
\frac{\phi^2}{A_*}
\ell_*.
}
\]

Therefore

\[
\boxed{
\frac{H_T}{E_T}
\ge
\kappa_*^2
}
\]

for the uniformly coefficient-active tube band.

This is exactly the kind of coefficient--amplitude correlation that M17-367 showed cannot follow from `kappa` alone.

## 6. Intrinsic subscale form

Suppose the tube coefficient event is associated with an intrinsic physical scale `r` and the regular tube geometry satisfies

\[
A_*\le C_A r^2,
\]

\[
\ell_*\ge c_\ell r,
\]

and

\[
\kappa_*\ge c_\kappa r^{-2}.
\]

Then

\[
\boxed{
E_T
\ge
\frac{c_\ell}{C_A}
\phi^2 r^{-1},
}
\]

and

\[
\boxed{
H_T
\ge
\frac{c_\ell c_\kappa^2}{C_A}
\phi^2 r^{-5}.
}
\]

Consequently

\[
\boxed{
r^4\frac{H_T}{E_T}
\ge
 c_\kappa^2.
}
\]

Thus a flux-bearing critical coefficient tube is automatically scale-comparable in the M17-251 sense.

## 7. Finite enstrophy forces flux thinning at strict subscales

If the ambient state has a finite enstrophy ceiling

\[
E_{global}\le E^*,
\]

then Section 6 implies

\[
\frac{c_\ell}{C_A}
\phi^2r^{-1}
\le E^*.
\]

Hence

\[
\boxed{
\phi
\le
C(E^*)^{1/2}r^{1/2}.
}
\]

Therefore a strict subscale coefficient tube

\[
r\to0
\]

cannot carry a fixed positive flux under finite enstrophy and regular tube geometry.

Its flux must thin at least at the rate

\[
O(r^{1/2}).
\]

This quantitatively explains why the nodal/subscale branch naturally drives flux fragmentation.

## 8. Relation to M17-298

M17-368 supplies a valid local raw-`H2` lower bound **when a flux-bearing critical coefficient tube with controlled transverse geometry has already been allocated**.

It does not by itself solve M17-298, because M17-298 asks for cross-scale allocation of a fixed fraction of shell raw `H2` across many possible nested packets.

The present result says that once a critical coefficient cluster carries an independently certified flux/geometry package, it is eligible to enter that raw-`H2` allocation tree.

Without such a flux package, M17-367 remains the firewall.

## 9. Updated strict-subscale branch

For a coefficient cluster of intrinsic scale `r`,

\[
\boxed{
\begin{aligned}
H_{critical\ coefficient\ cluster}
\Longrightarrow{}&
H_{flux\text{-}bearing\ tube}
\Rightarrow H_{raw\ H2\ charge}\\
&\lor G_{flux\ thinning}\
&\lor G_{transverse\ area/length\ geometry\ degeneration}\\
&\lor G_{coefficient\ allocation/interface\ loss}.
\end{aligned}
}
\]

Under finite enstrophy, the fixed-flux strict-subscale subbranch is impossible; the flux-thinning rate is quantitatively constrained.

## 10. DSD-theory role

The heuristic is to add exactly the independent structural datum required to break a known symmetry. The proof is divergence-free flux conservation along a regular tube, Cauchy--Schwarz, and the CE-H elliptic identity.

No DSD axiom is used as a PDE hypothesis.

## 11. Audit verdict

**PASS as a conditional amplitude-return/raw-H2 bridge.**

It does not close M17-298, but it identifies precisely when a critical coefficient cluster becomes a genuine raw-`H2` packet and quantifies the flux thinning required to evade that conversion at strict subscales.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
