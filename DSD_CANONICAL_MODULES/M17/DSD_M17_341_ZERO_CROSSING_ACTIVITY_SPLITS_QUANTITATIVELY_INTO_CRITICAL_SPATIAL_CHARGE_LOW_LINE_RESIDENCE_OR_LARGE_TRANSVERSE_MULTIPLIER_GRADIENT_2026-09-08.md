# DSD M17-341 — Zero-crossing activity splits quantitatively into critical spatial charge, low line residence, or large transverse multiplier gradient

Date: 2026-09-08  
Canonical ID: **M17-341**

Status: **ACTIVE QUANTITATIVE ZERO-CROSSING TRICHOTOMY**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Crossing-event measure

On the regular physical zero-level branch define the nonnegative pure-flux crossing-event measure

\[
\boxed{
d\nu
:=
h_-\delta(\kappa)\,d\Phi\,dt.
}
\]

Its total mass on an interval `I` is the M17-326/M17-338 critical zero-crossing currency

\[
\boxed{
\nu(I)=\mathcal C_{\Phi,-}^{0}(I).
}
\]

For each crossing label/time define

\[
w:=L_\rho=\int_\Gamma\rho\,ds,
\]

\[
d:=D_{\Gamma,\kappa}
=\int_\Gamma\rho|\nabla\kappa|^2ds,
\]

and the M17-340 critical line residence

\[
\ell:=\mathcal L_{crit}
=\int_\Gamma\rho|\nabla\kappa|^{-1/3}ds.
\]

M17-340 gives the pointwise label inequality

\[
\boxed{
\ell\ge w^{7/6}d^{-1/6}.
}
\]

## 2. Fix two audit thresholds

Choose arbitrary positive constants

\[
w_*>0,
\qquad
\ell_*>0.
\]

Partition the crossing-event space into

\[
E_{sp}:=\{\ell\ge\ell_*\},
\]

\[
E_{low}:=\{\ell<\ell_*,\ w<w_*\},
\]

and

\[
E_{grad}:=\{\ell<\ell_*,\ w\ge w_*\}.
\]

These sets exhaust all regular crossing events.

## 3. Spatial-charge branch

The critical spatial currency of M17-340 is

\[
\mathcal Q_0(I)
=\int\ell\,d\nu.
\]

If

\[
\nu(E_{sp})\ge\frac13\nu(I),
\]

then

\[
\boxed{
\mathcal Q_0(I)
\ge
\frac{\ell_*}{3}\mathcal C_{\Phi,-}^{0}(I).
}
\]

Thus a fixed fraction of the pure critical crossing flux becomes a spatial critical charge.

## 4. Low-line-residence branch

If

\[
\nu(E_{low})\ge\frac13\nu(I),
\]

then a fixed fraction of all zero-crossing activity occurs on labels satisfying

\[
\boxed{
L_\rho<w_*.
}
\]

This is the explicit low line-enstrophy residence branch.

On a high-amplitude capture family, making `w_*` small forces either shrinking retained arclength, failure of the high-amplitude capture, or material/interface repartition.  No such geometric conclusion is imported without its corresponding capture hypothesis.

## 5. Large-gradient branch

Suppose an event lies in `E_grad`.  Then

\[
\ell<\ell_*,
\qquad
w\ge w_*.
\]

The M17-340 inequality gives

\[
\ell_*
>
\ell
\ge
w_*^{7/6}d^{-1/6}.
\]

Rearranging,

\[
\boxed{
D_{\Gamma,\kappa}=d
>
\frac{w_*^7}{\ell_*^6}.
}
\]

Therefore if

\[
\nu(E_{grad})\ge\frac13\nu(I),
\]

then at least one third of the downward zero-crossing flux activity occurs on labels with the fixed transverse multiplier-gradient lower bound

\[
\boxed{
D_{\Gamma,\kappa}
\ge d_*
:=
\frac{w_*^7}{\ell_*^6}.
}
\]

## 6. Quantitative trichotomy

Since one of the three event sets has at least one third of the total event measure,

\[
\boxed{
\begin{aligned}
\mathcal C_{\Phi,-}^{0}>0
\Longrightarrow{}&
\mathcal Q_0
\ge
\frac{\ell_*}{3}\mathcal C_{\Phi,-}^{0}\\
&\lor
\nu\{L_\rho<w_*\}
\ge
\frac13\mathcal C_{\Phi,-}^{0}\\
&\lor
\nu\left\{
D_{\Gamma,\kappa}
\ge\frac{w_*^7}{\ell_*^6}
\right\}
\ge
\frac13\mathcal C_{\Phi,-}^{0}.
\end{aligned}
}
\]

This holds for every chosen pair `(w_*,ell_*)` on the regular nondegenerate zero-gradient branch.

## 7. Scale audit

The three quantities are dimensionally consistent:

- `C_{Phi,-}^0` is record-scale critical;
- `Q_0` is record-scale critical;
- `ell` is dimensionless;
- `w=L_rho` scales like inverse length;
- `d=D_{Gamma,kappa}` scales like `R^7`;
- the threshold combination
  \[
  w_*^7/\ell_*^6
  \]
  has exactly the same scaling as `d` if `w_*` is transported with its physical dimension.

Thus the trichotomy itself respects the physical scaling dictionary.

## 8. Relation to M5-683/M17-196

At `kappa=0`,

\[
A_{\kappa\kappa}^{ph}(0,t)
=
\int\delta(\kappa)D_{\Gamma,\kappa}\,d\Phi
\]

in the regular vortex-line representation, modulo the explicit high-amplitude cutoff.

Therefore the third branch is not a new abstract escape: it places a fixed amount of crossing activity on labels carrying a large value of the same transverse multiplier-gradient charge entering the M5-683 diffusion density.

However the event measure contains the extra factor `h_-`; converting an activity fraction directly into a finite spacetime `A_{kappa kappa}` budget still requires a velocity/occupation transfer estimate.

## 9. DSD-theory role

The useful DSD heuristic is to refuse an untyped failure of the new critical descriptor.

If the critical spatial descriptor is small, the calculation asks **which structural channel made it small** and forces that failure into either low line residence or high coefficient gradient.

The mathematical proof is elementary partitioning plus the M17-340 Jensen inequality.

## 10. Updated frontier

On the regular zero-level branch, the M17-326 critical crossing current now has the certified refinement

\[
\boxed{
H_{critical\ zero\ crossing}
\Longrightarrow
H_{critical\ spatial\ crossing}
\lor
G_{low\ line\ residence}
\lor
H_{large\ transverse\ multiplier\ gradient}.
}
\]

The next target is to audit whether the M17-314 high-amplitude bounded-capture hypotheses already exclude the low-residence branch, and then whether the large-gradient activity can be transferred into the M5-688/M17-196 positive diffusion ledger without reintroducing a noncritical weight.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
