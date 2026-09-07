# DSD M17-329 — K-cubed flux/area growth matches the similarity-volume Jacobian and is not by itself a physical contradiction

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CORRECTION / REPRESENTATION AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Why M17-328 requires a representation audit

M17-328 proved, conditionally on the M17-134 resonant same-genealogy branch,

\[
\frac{\Phi_j}{\Phi_{j-k}}\asymp K_k^3,
\]

and

\[
\frac{(\Phi/\rho)_j}{(\Phi/\rho)_{j-k}}\asymp K_k^3.
\]

These are exact cocycle calculations.  However, a large factor in similarity coordinates need not be an anomalous physical deformation.  The similarity representation itself has a nonzero Jacobian exponent.

## 2. Similarity material-volume Jacobian

The similarity material velocity is

\[
B=U+\frac12y.
\]

Since \(U\) is divergence free,

\[
\boxed{\nabla\cdot B=\frac32.}
\]

Therefore a similarity-material volume element \(dV_B\) obeys

\[
\frac d{d\theta}\log dV_B
=\frac32.
\]

Over the M17-134 inter-stage interval

\[
\Delta\theta_k=2\log K_k,
\]

we get

\[
\boxed{
\frac{dV_B(\theta_j)}{dV_B(\theta_{j-k})}
=
\exp\left(\frac32\,2\log K_k\right)
=K_k^3.
}
\]

Thus cubic growth is precisely the ambient similarity-volume Jacobian.

## 3. Longitudinal material-line exponent

For a material line element tangent to the vorticity direction \(\xi\), the similarity velocity gradient is

\[
\nabla B=\nabla U+\frac12I.
\]

Since on CE-H

\[
\xi\cdot\Sigma\xi=\sigma,
\]

its longitudinal stretch rate is

\[
\boxed{
D_B\log ds_\parallel
=\sigma+\frac12.
}
\]

M17-134 gives

\[
\langle\sigma\rangle
=-\frac12+O((\log K_k)^{-1}),
\]

hence

\[
\log\frac{ds_{\parallel,j}}{ds_{\parallel,j-k}}
=O(1).
\]

So the resonant branch has no polynomial longitudinal stretch over the inter-stage interval.

## 4. Transverse area exponent

Volume equals longitudinal length times transverse area.  Therefore

\[
D_B\log dA_\perp
=
\frac32-\left(\sigma+\frac12\right)
=1-\sigma.
\]

This exactly matches the independent M17-328 identity

\[
D_B\log\frac{\Phi}{\rho}
=1-\sigma.
\]

Consequently the cubic transverse growth found there is not a new mismatch:

\[
\boxed{
K_k^3\text{ transverse growth}
=
K_k^3\text{ similarity-volume growth}
\times O(1)\text{ longitudinal factor}^{-1}.
}
\]

## 5. Renormalized transverse area

Define the similarity-Jacobian-normalized transverse area proxy

\[
\boxed{
\widehat A_\perp(\theta)
:=e^{-3\theta/2}\frac{\Phi}{\rho}.
}
\]

Then

\[
D_B\log\widehat A_\perp
=
1-\sigma-\frac32
=-\sigma-\frac12.
\]

Hence on the M17-134 resonant branch

\[
\boxed{
\left\langle
D_B\log\widehat A_\perp
\right\rangle
=O((\log K_k)^{-1}).
}
\]

The renormalized area is therefore neutral at leading inter-stage order.

Notably, the exponent

\[
-\sigma-\frac12
\]

is the same exponent already appearing in M17-134 for one pure-kernel director-jet magnitude.  This is a resonance consistency, not yet a contradiction.

## 6. Renormalized flux channel

Likewise define

\[
\boxed{
\widehat\Phi(\theta)
:=e^{-3\theta/2}\Phi(\theta).
}
\]

Since

\[
D_B\log\Phi=\kappa,
\]

we have

\[
\boxed{
D_B\log\widehat\Phi
=\kappa-\frac32.
}
\]

On the M17-134 resonant branch,

\[
\left\langle\kappa-\frac32\right\rangle
=O((\log K_k)^{-1}),
\]

so \(\widehat\Phi\) is also neutral at leading inter-stage order.

This does **not** replace the physical zero-\(\kappa\) crossing current of M17-326.  It shows only that the threshold relevant to boundedness of the similarity-Jacobian-normalized flux is \(\kappa=3/2\), whereas \(\kappa=0\) is the threshold for raw material-flux growth/decay.

The two questions must not be conflated.

## 7. Consequence for the current proof strategy

M17-328 remains valid as a cocycle statement:

\[
\Phi_j/\Phi_{j-k}\asymp K_k^3.
\]

But the following interpretation is rejected:

\[
\boxed{
K_k^3\text{ growth by itself}
\Rightarrow
\text{geometric impossibility}.
}
\]

Instead, the correct reading is

\[
\boxed{
\text{raw flux/area cubic growth}
\text{ is compatible with the resonant similarity Jacobian.}
}
\]

A contradiction would require an additional statement that the relevant **renormalized** flux/area quantity must drift, leave a compact corridor, or pay a finite critical resource.

## 8. DSD-theory role

This is precisely where the DSD theoretical layer is useful as an audit heuristic: distinguish growth of the represented quantity from growth of the underlying structure after the representation's own Jacobian is removed.

The actual correction, however, follows entirely from

\[
\nabla\cdot B=3/2
\]

and the material deformation equations.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated target

There are now two distinct transition levels:

\[
\boxed{
\kappa=0
\quad\text{raw material-flux growth/decay threshold},
}
\]

and

\[
\boxed{
\kappa=\frac32
\quad\text{similarity-Jacobian-normalized flux threshold}.
}
\]

The next high-value calculation is to determine whether the fixed negative-\(\kappa\) phase and directed zero-crossing flux force nontrivial turnover across the **resonant level** \(\kappa=3/2\), or whether different material labels can permanently segregate the two phases.

## 10. Audit verdict

**PASS as a representation correction.**

M17-328's equations survive; its possible interpretation as a direct geometric contradiction does not.  The late branch is narrowed to a two-threshold transport problem plus genealogy/phase-segregation exits.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
