# M19-003 — Boundary modes descend to palinstrophy, and the bulk source is exactly rho^p times kappa plus normalized diffusion

**Date:** 2026-09-11  
**Status:** CALCULATION / DEFECT DESCENT / TWO OF THREE CYCLE DEFECTS RETURN TO M18 CURRENCIES

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-002

A fixed nonzero conservative mean cycle forces at least one of

\[
G_{conductance\ modulation},
\qquad
G_{boundary\ mode},
\qquad
G_{bulk\ source},
\]

or connector geometry/topology degeneration.

The present module asks whether the boundary-mode and bulk-source branches define genuinely new resources.

They do not.

## 2. Amplitude potential

For fixed finite \(p\ge2\), define

\[
\boxed{
u_p:=\frac{\rho^p}{p}.}
\]

Then

\[
\boxed{
\nabla u_p
=
\rho^{p-1}\nabla\rho.
}
\]

On the compact CE-H branch,

\[
0\le\rho\le M_*<\infty.
\]

## 3. Boundary-mode energy forces an amplitude-gradient payment

M19-002 gives on the controlled connector family

\[
\boxed{
\int_C
\nabla u_p^{mode}\cdot A\nabla u_p^{mode}
\ge c_E>0
}
\]

on the fixed boundary-mode branch.

Uniform ellipticity gives

\[
\int_C|\nabla u_p^{mode}|^2
\ge c_1>0.
\]

The harmonic-mode energy is no larger than the full competitor energy carrying the same nonconstant trace, so the actual amplitude potential must carry a comparable nonconstant-trace Dirichlet cost on the controlled connector.

Using

\[
|\nabla u_p|^2
=
\rho^{2p-2}|\nabla\rho|^2
\le
M_*^{2p-2}|\nabla\rho|^2,
\]

one obtains a fixed amplitude-gradient floor

\[
\boxed{
\int_C|\nabla\rho|^2
\ge
c_{\rho,p}>0.
}
\]

## 4. Amplitude-gradient payment is part of palinstrophy

With

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

we have

\[
\boxed{
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Therefore

\[
\boxed{
\int_C|\nabla W|^2
\ge
\int_C|\nabla\rho|^2
\ge c_{\rho,p}>0.
}
\]

Hence

\[
\boxed{
G_{boundary\ mode}
\Longrightarrow
G_{palinstrophy/interface\ payer}.
}
\]

This is an already existing M18 currency. The boundary-mode branch does not create a new independent CE-H resource.

The M18 ancestry warning remains: a fixed own-scale palinstrophy payer is not by itself a fixed-parent contradiction.

## 5. Exact CE-H amplitude Laplacian identity

Now compute the bulk source in isotropic similarity coordinates.

From

\[
W=\rho\xi,
\qquad
\Delta W=\kappa W,
\]

take the dot product with \(\xi\).

Because

\[
\xi\cdot\partial_i\xi=0
\]

and

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

we get

\[
\boxed{
\Delta\rho
-
\rho|\nabla\xi|^2
=
\kappa\rho.
}
\]

Thus

\[
\boxed{
\Delta\rho
=
\rho\left(\kappa+|\nabla\xi|^2\right).
}
\]

## 6. Compute Delta u_p exactly

Since

\[
u_p=\frac{\rho^p}{p},
\]

\[
\Delta u_p
=
\rho^{p-1}\Delta\rho
+
(p-1)\rho^{p-2}|\nabla\rho|^2.
\]

Insert Section 5:

\[
\begin{aligned}
\Delta u_p
&=
\kappa\rho^p
+
\rho^p|\nabla\xi|^2
+
(p-1)\rho^{p-2}|\nabla\rho|^2.
\end{aligned}
\]

Define the M18 normalized diffusion density

\[
\boxed{
G_p
:=(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2
}
\]

on the active set in the weighted sense.

Then

\[
\rho^pG_p
=
(p-1)\rho^{p-2}|\nabla\rho|^2
+
\rho^p|\nabla\xi|^2.
\]

Therefore

\[
\boxed{
\Delta u_p
=
\rho^p(\kappa+G_p).
}
\]

This is exact on CE-H.

## 7. Bulk-source defect is not a new currency

In the isotropic connector convention of M19-001,

\[
L u_p=-\Delta u_p.
\]

Hence

\[
\boxed{
f
=-\rho^p(\kappa+G_p).
}
\]

Therefore a fixed bulk-source defect is a fixed negative-order size of an already analyzed combination:

\[
\boxed{
\text{coefficient source}
+
\text{normalized diffusion density}.
}
\]

If

\[
\|f\|_{H^{-1}(C)}
\ge c_f>0,
\]

then by the triangle inequality

\[
\boxed{
\|\rho^p\kappa\|_{H^{-1}}
+
\|\rho^pG_p\|_{H^{-1}}
\ge c_f.
}
\]

Thus at least one coefficient/diffusion component has a fixed negative-order floor.

No unjustified conversion from this \(H^{-1}\) floor to a stronger pointwise or \(L^2\) floor is made here.

## 8. Relation to M18-069--070

M18 already identifies \(G_p\) as

\[
G_p
=(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2
\]

and uses its amplitude covariance to produce the diffusive sheath/core split.

Thus the M19 bulk-source branch returns directly to

\[
\boxed{
G_{coefficient/diffusive\ sheath\ structure}
}
\]

rather than introducing a fourth current-cycle currency.

## 9. Updated M19 cycle route

Combining M19-002 and the present descent,

\[
\boxed{
\text{fixed nonzero conservative population cycle}
\Longrightarrow
\begin{cases}
G_{conductance\ pump/modulation},\\
G_{palinstrophy/interface},\\
G_{coefficient+normalized\ diffusion\ source},\\
G_{connector\ geometry/topology\ degeneration}.
\end{cases}
}
\]

Only the **conductance-pump/modulation** branch remains genuinely new at the finite-network level.

The other two are already M18-analyzed CE-H currencies.

## 10. Next calculation

M19-004 should differentiate the connector capacity/conductance on the fixed reference collar.

Because the harmonic connector profile is variationally stationary, the derivative of

\[
G(\theta)
=
\int_C\nabla h_\theta\cdot A_\theta\nabla h_\theta
\]

should depend only on the metric/operator rate \(A_\theta'\) at first order:

\[
\boxed{
G'
=
\int_C
\nabla h_\theta\cdot A_\theta'\nabla h_\theta
}
\]

under fixed pulled-back boundary data.

The next task is to verify this exactly and connect \(A_\theta'\) to the material deformation/strain ledger.

---

\[
\boxed{\text{M19-003 COMPLETE; GLOBAL REGULARITY REMAINS OPEN.}}
\]
