# M17-484 — The zero-tube coefficient exit is the scale-invariant delta times Laplacian-kappa over grad-kappa-squared ratio and requires a genuine second coefficient jet or critical level

**Date:** 2026-09-10  
**Status:** ACTIVE SCALE-INVARIANT COEFFICIENT-SHAPE FIREWALL / ZERO-TUBE HIGH-JET CLASSIFICATION

## 1. Purpose

M17-483 reduced the nodal-safe zero-current branch to raw-H2, palinstrophy, tube/gradient loss, or a ceiling on
\[
\left|\frac{\Delta\kappa}{|\nabla\kappa|^2}\right|.
\]

The ratio itself is dimensional. This module identifies the correct scale-invariant slab parameter and audits what its decompactification actually means.

## 2. Dimensionless coefficient-shape parameter

On a regular coefficient slab
\[
|\kappa|<\delta,
\]
define
\[
\boxed{
\Lambda_{\kappa,\delta}
:=
\delta\,
\operatorname*{ess\,sup}_{|\kappa|<\delta}
\left|
\frac{\Delta\kappa}{|\nabla\kappa|^2}
\right|.
}
\]

This is the parameter that appears in M17-483 through
\[
L_\kappa\delta.
\]
The persistence constants depend on
\[
e^{-\Lambda_{\kappa,\delta}},
\]
not on the dimensional ratio by itself.

## 3. Exact scaling audit

Under
\[
\kappa_R(y,s)=R^2\kappa(Ry,R^2s),
\]
we have
\[
\nabla_y\kappa_R=R^3\nabla_x\kappa,
\]
\[
\Delta_y\kappa_R=R^4\Delta_x\kappa.
\]
Hence
\[
\frac{\Delta\kappa_R}{|\nabla\kappa_R|^2}
=R^{-2}
\frac{\Delta\kappa}{|\nabla\kappa|^2}.
\]
The corresponding coefficient slab width scales as
\[
\delta_R=R^2\delta.
\]
Therefore
\[
\boxed{
\Lambda_{\kappa_R,\delta_R}
=
\Lambda_{\kappa,\delta}.
}
\]

Thus \(\Lambda_{\kappa,\delta}\) is representation-safe under the certified Navier--Stokes scaling.

## 4. Refined M17-483 estimate

M17-483 gives, in the small-palinstrophy alternative,
\[
F(s)
\ge
\frac14e^{-L_\kappa\delta}J_0.
\]
Writing the dimensionless parameter,
\[
\boxed{
F(s)
\ge
\frac14e^{-\Lambda_{\kappa,\delta}}J_0
\qquad(|s|\le\delta).
}
\]
Consequently
\[
\boxed{
H_{0,\delta}
\ge
\frac16G_*^{-2}
 e^{-\Lambda_{\kappa,\delta}}
\delta^3J_0.
}
\]

The palinstrophy alternative is
\[
\boxed{
P_{0,\delta}
>
\frac{1}{4\delta}
 e^{-\Lambda_{\kappa,\delta}}J_0.
}
\]

Therefore bounded \(\Lambda_{\kappa,\delta}\) gives a record-uniform raw-H2/palinstrophy dichotomy when the remaining normalized tube constants are compact.

## 5. What divergence of Lambda means

Suppose
\[
\Lambda_{\kappa,\delta}\to\infty.
\]
Then somewhere in the slab
\[
\delta|\Delta\kappa|
\gg
|\nabla\kappa|^2.
\]
This can occur only through one or both of the following invariant mechanisms:

### A. Critical-level degeneration

\[
|\nabla\kappa|^2
\ll
\delta|\Delta\kappa|.
\]
In particular, if \(\delta|\Delta\kappa|\) is bounded while \(\Lambda_{\kappa,\delta}\to\infty\), then
\[
|\nabla\kappa|\to0
\]
along a subsequence.

### B. Genuine second coefficient-jet growth

If
\[
|\nabla\kappa|\ge g_*>0
\]
in normalized coordinates and \(\delta\) has a fixed positive normalized width, then
\[
\Lambda_{\kappa,\delta}\to\infty
\]
forces
\[
|\Delta\kappa|\to\infty.
\]

Hence
\[
\boxed{
G_{\Lambda_\kappa\text{-}decompactification}
\Longrightarrow
G_{\rm critical\ level}
\lor
G_{\rm second\ coefficient\ jet}.
}
\]

## 6. Derivative-order firewall relative to existing vorticity ledgers

The exact CE-H equation is
\[
\Delta\Omega=\kappa\Omega.
\]
Applying another Laplacian gives
\[
\Delta^2\Omega
=(\Delta\kappa)\Omega
+2\nabla\kappa\cdot\nabla\Omega
+\kappa\Delta\Omega.
\]
Since \(\Delta\Omega=\kappa\Omega\),
\[
\boxed{
\Delta^2\Omega
=(\Delta\kappa)\Omega
+2\nabla\kappa\cdot\nabla\Omega
+\kappa^2\Omega.
}
\]
Where \(\rho=|\Omega|>0\) and \(\xi=\Omega/\rho\), taking the \(\xi\)-component yields
\[
\boxed{
\rho\,\Delta\kappa
=
\xi\cdot\Delta^2\Omega
-2\nabla\kappa\cdot\nabla\rho
-\kappa^2\rho.
}
\]

Thus pointwise control of \(\Delta\kappa\) naturally reaches the \(D^4\Omega\) level. The certified late-M17 high-vorticity ledger currently reaches \(D^3\Omega\), together with the weighted \(\rho^2|\nabla\kappa|^2\) resource.

Therefore
\[
\boxed{
\text{M17-444/445 do not automatically control }\Delta\kappa.
}
\]
Absorbing \(\Lambda_{\kappa,\delta}\) into the existing D3/coefficient-gradient ledger without an additional identity would be a derivative-order error.

## 7. Zero-level specialization

At \(\kappa=0\), the identity reduces to
\[
\boxed{
\rho\,\Delta\kappa
=
\xi\cdot\Delta^2\Omega
-2\nabla\kappa\cdot\nabla\rho.
}
\]
The second term is lower-order and its amplitude-gradient component is compatible with the palinstrophy reduction of M17-483. The first term still contains \(D^4\Omega\).

Thus even exactly on the regular zero level, the second coefficient jet is not certified by the current D3 ledger.

## 8. Updated zero-current branch

Combining M17-483 and M17-484,
\[
\boxed{
\begin{aligned}
G_{J_0}
\Longrightarrow{}&
G_{\rm raw-H^2}^{R^{-3}}\\
&\lor G_{\rm palinstrophy}^{R^{-1}}\\
&\lor G_{\rm critical\ level}\\
&\lor G_{\rm second\ coefficient\ jet/D4}\\
&\lor G_{\rm coefficient\ gradient\ ceiling/tube/interface/domain\ loss}.
\end{aligned}
}
\]

The amplitude-normal/nodal relative-ratio branch has been removed by M17-483. The coefficient-shape branch is now dimensionless and derivative-order typed.

## 9. Ancestry interpretation

Bounded \(\Lambda_{\kappa,\delta}\) gives only fixed normalized raw-H2/palinstrophy payments, so M17-473 remains the ancestry firewall.

Unbounded \(\Lambda_{\kappa,\delta}\) is not itself a contradiction. It is a scale-invariant decompactification witness that routes to critical-level geometry or a genuine second coefficient jet beyond the currently certified derivative budget.

## 10. Next target

The nearest new branch is now the second coefficient jet / \(D^4\Omega\) channel. Before trying to create a new D4 energy estimate, the next audit should check whether the exact coefficient equation or existing M17/M5 identities contain a cancellation that lowers \(\Delta\kappa\) back to certified D3 quantities. M17-463 remains mandatory: no termwise \(\mathcal R_{\rm geom}\) formula may be guessed.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
