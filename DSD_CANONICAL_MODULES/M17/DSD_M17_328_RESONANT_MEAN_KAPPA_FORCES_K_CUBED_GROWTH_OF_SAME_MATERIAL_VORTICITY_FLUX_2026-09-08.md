# DSD M17-328 — resonant mean kappa forces K-cubed growth of same-material vorticity flux

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION / SAME-GENEALOGY FLUX COCYCLE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-134

M17-134 tracks one pure-kernel material carrier over the inter-stage interval

\[
\Delta\theta_k
=\theta_j-\theta_{j-k}
=2\log K_k.
\]

Under its endpoint compactness assumptions,

\[
\boxed{
\langle\sigma\rangle_{j-k:j}
=-\frac12+O((\log K_k)^{-1}),
}
\]

and, if the similarity-vorticity amplitude ratio is also bounded,

\[
\boxed{
\langle\kappa\rangle_{j-k:j}
=\frac32+O((\log K_k)^{-1}).
}
\]

The conclusion is along the same material genealogy; it is not a spatial \(\rho^2\)-weighted average.

## 2. Same-material vorticity-flux law

M5-684/M17-318 gives for one retained material vortex-tube flux element

\[
\boxed{
\frac d{d\theta}\log\Phi=\kappa.
}
\]

Assume that the material flux element is carried by the same genealogy over the M17-134 inter-stage interval.  If that identity fails because of tube replacement, cutting, end loss, or relabelling, record the typed exit

\[
G_{material\ flux\ genealogy/replacement}.
\]

Otherwise integrate:

\[
\log\frac{\Phi_j}{\Phi_{j-k}}
=
\int_{\theta_{j-k}}^{\theta_j}\kappa\,d\theta.
\]

Using the M17-134 mean,

\[
\int\kappa d\theta
=
\left(
\frac32+O((\log K_k)^{-1})
\right)
2\log K_k.
\]

Therefore

\[
\boxed{
\log\frac{\Phi_j}{\Phi_{j-k}}
=3\log K_k+O(1).
}
\]

Exponentiating,

\[
\boxed{
\frac{\Phi_j}{\Phi_{j-k}}
\asymp K_k^3.
}
\]

More explicitly, there exist constants \(0<c<C<\infty\), independent of sufficiently large \(k\), such that

\[
\boxed{
cK_k^3
\le
\frac{\Phi_j}{\Phi_{j-k}}
\le
CK_k^3.
}
\]

## 3. Bounded same-label flux recurrence is impossible on this branch

If one attempted to impose the same-label compact flux corridor

\[
0<c_\Phi
\le
\Phi_{j-k},\Phi_j
\le C_\Phi<\infty
\]

uniformly in remote age \(k\), then

\[
\frac{\Phi_j}{\Phi_{j-k}}
\le\frac{C_\Phi}{c_\Phi},
\]

contradicting

\[
\frac{\Phi_j}{\Phi_{j-k}}\asymp K_k^3\to\infty.
\]

Hence

\[
\boxed{
\text{M17-134 resonant mean branch}
\Rightarrow
\text{unbounded same-material flux cocycle}
\lor
G_{material\ flux\ genealogy/replacement}.
}
\]

This is stronger than saying merely that a bounded state-function cocycle cannot give a strict recurrence contradiction: the exact flux law fixes the growth exponent.

## 4. Transverse-area proxy

On an infinitesimal regular vortex tube,

\[
d\Phi=\rho\,dA_\perp.
\]

Thus the material transverse area element is

\[
dA_\perp=\frac{d\Phi}{\rho}.
\]

Using

\[
D_B\log\rho=\sigma+\kappa-1
\]

and

\[
D_B\log\Phi=\kappa,
\]

we obtain the exact area law

\[
\boxed{
D_B\log\frac{\Phi}{\rho}
=1-\sigma.
}
\]

M17-134 gives

\[
\langle\sigma\rangle
=-\frac12+O((\log K_k)^{-1}),
\]

therefore

\[
\log
\frac{(\Phi/\rho)_j}{(\Phi/\rho)_{j-k}}
=
3\log K_k+O(1),
\]

and hence

\[
\boxed{
\frac{(\Phi/\rho)_j}{(\Phi/\rho)_{j-k}}
\asymp K_k^3.
}
\]

So the same resonant genealogy requires cubic growth of the infinitesimal transverse-area proxy as well.

## 5. Compatibility with the bounded-amplitude hypothesis

M17-134 already assumes the endpoint amplitude ratio is bounded in the branch yielding \(\langle\kappa\rangle\to3/2\).  Therefore the cubic flux growth cannot be hidden inside a compensating cubic amplitude ratio.

Instead, it must appear in material-tube geometry or in a failure of same-tube genealogy.

This gives the typed refinement

\[
\boxed{
H_{resonant\ mean\ frame}
\Rightarrow
H_{K^3\ transverse\ material\ area\ expansion}
\lor
G_{tube\ replacement/end/relabel}.
}
\]

No contradiction is yet claimed: material cross-sectional area can in principle grow strongly even while the normalized Eulerian field remains recurrent, because material genealogy is path dependent.

## 6. Relation to M17-326 critical crossing flux

M17-326's directed crossing measure is scale critical and is naturally carried by material flux labels.  M17-328 now shows that the same material flux weights are not bounded state weights on the long resonant genealogy; they acquire a cubic inter-stage cocycle.

Therefore any accumulation theorem for the critical crossing measure must specify whether it uses

1. ancestor flux weights;
2. descendant flux weights;
3. a renormalized flux weight;
4. replacement-invariant crossing counts.

Silently identifying these weights is forbidden.

## 7. DSD-theory role

The DSD channel-separation heuristic suggested checking whether the `kappa` channel and the material-flux channel could both remain structurally compact.  The answer is an exact standard-math no-go on the M17-134 resonant branch:

\[
\boxed{
\text{bounded amplitude + resonant mean kappa}
\Rightarrow
\Phi\text{ grows like }K^3.
}
\]

DSD theory is not used as an axiom; it only selected the compatibility test.

## 8. Audit verdict

**PASS as a conditional same-genealogy cocycle calculation.**

The result removes bounded same-label material flux from the resonant survivor.  The remaining possibilities are unbounded material-tube expansion or explicit genealogy/replacement.  Neither is yet excluded by a finite critical budget.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
