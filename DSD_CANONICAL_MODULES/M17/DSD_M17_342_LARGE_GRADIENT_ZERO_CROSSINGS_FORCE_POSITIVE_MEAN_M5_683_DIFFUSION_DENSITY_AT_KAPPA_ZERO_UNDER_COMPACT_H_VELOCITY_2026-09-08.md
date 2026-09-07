# DSD M17-342 — Large-gradient zero crossings force positive mean M5-683 diffusion density at kappa=0 under compact h-velocity

Date: 2026-09-08  
Canonical ID: **M17-342**

Status: **ACTIVE CROSSING-TO-DIFFUSION TRANSFER / SAME SIMILARITY HULL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-341

Work in the similarity recurrent hull, where the exact zero-level crossing currency is equivalent to the physical one by M17-338.

Let

\[
h:=D_B\kappa.
\]

M17-341 gives, on its large-gradient branch, a fixed fraction of downward zero-crossing activity carried by labels satisfying

\[
\boxed{
D_{\Gamma,\kappa}
:=
\int_\Gamma\rho|\nabla\kappa|^2ds
\ge d_*>0.
}
\]

Write the large-gradient crossing activity as

\[
\mathcal C_{grad}([0,T])
:=
\int_{E_{grad}}
h_-\delta(\kappa)d\Phi d\theta.
\]

If the M17-341 third branch carries at least one third of the total activity, then

\[
\boxed{
\mathcal C_{grad}([0,T])
\ge
\frac13\mathcal C_{\Phi,-}^{0}([0,T]).
}
\]

M17-323/326 give positive long-time density of the total crossing activity on the retained normalized branch.

## 2. Compact coefficient-velocity ceiling

On the compact all-order recurrent CE-H hull, `kappa` and its material derivative are uniformly bounded on the retained high-amplitude population.

Thus on the present compact branch there exists

\[
\boxed{
|h|\le H_*<\infty.
}
\]

Failure of this ceiling is the already typed coefficient/decompactification exit and is not included in this branch.

## 3. M5-683 zero-level diffusion density

M5-683 defines

\[
\boxed{
A_{\kappa\kappa}(k,\theta)
:=
\int
\delta(k-\kappa)
\chi\rho^2|\nabla\kappa|^2dy
\ge0.
}
\]

At `k=0`, vortex-line coordinates give

\[
\boxed{
A_{\kappa\kappa}(0,\theta)
=
\int
\delta(\kappa)
D_{\Gamma,\kappa}
\,d\Phi,
}
\]

up to the fixed high-amplitude cutoff convention.

## 4. Eventwise transfer inequality

On `E_grad`,

\[
D_{\Gamma,\kappa}\ge d_*.
\]

Also

\[
h_-\le H_*.
\]

Therefore, as nonnegative measures on the regular zero level,

\[
\delta(\kappa)D_{\Gamma,\kappa}
\ge
\frac{d_*}{H_*}
 h_-\delta(\kappa)
\]

on `E_grad`.

Integrating over flux labels and time gives

\[
\boxed{
\int_0^T
A_{\kappa\kappa}(0,\theta)d\theta
\ge
\frac{d_*}{H_*}
\mathcal C_{grad}([0,T]).
}
\]

Hence

\[
\boxed{
\int_0^T
A_{\kappa\kappa}(0,\theta)d\theta
\ge
\frac{d_*}{3H_*}
\mathcal C_{\Phi,-}^{0}([0,T]).
}
\]

## 5. Positive long-time mean at zero

If

\[
\mathcal C_{\Phi,-}^{0}([0,T])
\ge c_0T-o(T),
\qquad c_0>0,
\]

then

\[
\boxed{
\liminf_{T\to\infty}
\frac1T
\int_0^T
A_{\kappa\kappa}(0,\theta)d\theta
\ge
\frac{d_*c_0}{3H_*}>0.
}
\]

Thus the large-gradient crossing branch forces a genuine positive recurrent mean of the same pure multiplier-diffusion density used by M5-683/M5-688, evaluated at the zero coefficient level.

## 6. Why this is not yet the full M5-688 D_kappa ledger

M5-688 uses the `k`-integrated charge

\[
D_\kappa
=
\left\langle
\int e^{2k}A_{\kappa\kappa}(k,\theta)dk
\right\rangle.
\]

A pointwise-in-`k` lower bound at `k=0` does not automatically imply a uniform lower bound on a `k` interval.

To thicken the zero-level density into the integrated ledger one needs a **uniform regular-level thickness statement**, for example a recurrent branch on which

\[
|\nabla\kappa|\ge g_*>0
\]

through a fixed spatial neighborhood of the zero level together with uniform coefficient regularity.

Otherwise retain the typed exit

\[
\boxed{
G_{k\text{-}space\ concentration/critical\text{-}value\ degeneration}.
}
\]

## 7. Uniform regular-level branch

If the recurrent compact family satisfies a uniform regular-zero-level condition, then the coarea representation

\[
A_{\kappa\kappa}(k,\theta)
=
\int_{\{\kappa=k\}}
\chi\rho^2|\nabla\kappa|\,dS
\]

varies continuously in `k` near zero with uniform modulus on the compact family.

Then a fixed positive lower mean at `k=0` thickens to some fixed corridor

\[
|k|<\delta_*
\]

and yields

\[
\boxed{
D_\kappa
\ge c_\kappa>0.
}
\]

This reproduces a positive M5-688 multiplier-diffusion payer directly from the zero-crossing activity, rather than importing it from an unrelated occupancy argument.

The uniform-thickness condition is not silently assumed.

## 8. Relation to existing M5-688/M17-196 payer tree

Once thickened, the charge enters the already audited identity

\[
D_\kappa+X_{\kappa\sigma}
=
\frac12\mathcal S
+\frac14\mathcal C
+\frac12\mathcal R
-\frac18\mathcal M,
\]

and hence the M17-191--196 payer reductions.

Therefore the large-gradient zero-crossing branch does not create a new catch-all obstruction; it routes back into the known strain-gradient / strain-residence / threshold / palinstrophy-scale payer tree.

## 9. DSD-theory role

The useful DSD heuristic is to demand an explicit transfer between a transition event and the positive PDE density claimed to pay for it.

The transfer here is the measure inequality using the compact `h` ceiling.

The remaining thickness issue is kept as a separate typed exit rather than being hidden in the word `regular`.

## 10. Updated large-gradient branch

\[
\boxed{
H_{large\text{-}gradient\ zero\ crossing}
\Longrightarrow
H_{positive\ A_{\kappa\kappa}(0)\ mean}
\Longrightarrow
H_{M5\text{-}688\ diffusion\ payer}
\lor
G_{k\text{-}space\ concentration/critical\ degeneration}.
}
\]

The next remaining branch from M17-341 is therefore the low-line-residence branch; separately, the new `k`-space thickness gate must be audited against the compact analytic hull.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
