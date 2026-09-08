# DSD M17-399 — The exponentially tilted quarter-strain payer splits exactly into the palinstrophy/cutoff residence excess and a `kappa`-phase-tilt covariance channel

Date: 2026-09-08  
Canonical ID: **M17-399**

Status: **ACTIVE STRAIN-RESIDENCE DECOMPOSITION / PHASE-TILT CHANNEL IDENTIFICATION / M5-688 PAYER REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-186 and M17-398

M17-186 defines the recurrent quarter-strain density

\[
q(k)
:=
\overline S_\sigma(k)
-
\frac14\overline F(k).
\]

Its unweighted integral is

\[
\boxed{
Q_\sigma^{(0)}
:=
\int q(k)dk.
}
\]

The exact recurrent cutoff identity gives

\[
\boxed{
Q_\sigma^{(0)}
=
\overline{D_\chi+B_\chi-rac12C_\chi^{tot}}.
}
\]

Here `D_chi` is cutoff vorticity palinstrophy, `B_chi` is a positive amplitude-collar gradient term, and `C_chi^tot` is the explicit cutoff-transition source.

M5-688, however, uses the exponentially tilted payer

\[
\boxed{
Q_\sigma^{(2)}
:=
\int e^{2k}q(k)dk.
}
\]

M17-398 shows that ordinary bulk gradient payers return to the M17-307 palinstrophy firewall.

The question is therefore: what part of `Q_sigma^(2)` is genuinely not already present in `Q_sigma^(0)`?

## 2. Exact tilt decomposition

Write

\[
e^{2k}=1+(e^{2k}-1).
\]

Then exactly

\[
\boxed{
Q_\sigma^{(2)}
=
Q_\sigma^{(0)}
+
\mathcal P_{\kappa\sigma}^{tilt},
}
\]

where

\[
\boxed{
\mathcal P_{\kappa\sigma}^{tilt}
:=
\int
(e^{2k}-1)
\left(
\overline S_\sigma(k)
-
\frac14\overline F(k)
\right)dk.
}
\]

Thus the tilted quarter-strain payer has only two pieces:

1. the ordinary quarter-strain residence excess;
2. a coefficient-phase tilt of that signed residence density.

No third strain-residence mechanism is hidden in the exponential weight.

## 3. Spatial form of the phase-tilt term

By the definitions of `F` and `S_sigma`,

\[
\boxed{
\mathcal P_{\kappa\sigma}^{tilt}
=
\left\langle
\int
\chi(\rho)\rho^2
\left(e^{2\kappa}-1\right)
\left(\sigma-\frac14\right)dy
\right\rangle.
}
\]

Therefore the new channel is not a new derivative norm.

It is a **signed coefficient/strain-residence phase correlation**.

If `kappa` and the quarter-strain excess are uncorrelated in the relevant weighted population, the tilt channel is small and `Q_sigma^(2)` returns to the ordinary quarter-strain payer.

## 4. The ordinary residence term returns to palinstrophy/cutoff

Insert the M17-186 identity into Section 2:

\[
\boxed{
Q_\sigma^{(2)}
=
\overline{D_\chi+B_\chi-rac12C_\chi^{tot}}
+
\mathcal P_{\kappa\sigma}^{tilt}.
}
\]

M17-398 classifies `D_chi` and the amplitude-gradient part of `B_chi` as palinstrophy-scale/collar-gradient payers.

Hence, modulo the explicit cutoff transition,

\[
\boxed{
\text{the only genuinely new non-gradient content of }Q_\sigma^{(2)}
\text{ is }\mathcal P_{\kappa\sigma}^{tilt}.
}
\]

This removes `strain residence` as a broad untyped category.

## 5. Compact-support bound for the tilt

On the recurrent compact hull,

\[
|\kappa|\le K_*.
\]

By the mean-value theorem,

\[
|e^{2k}-1|
\le
C_{K_*}|k|
\]

with, for example,

\[
C_{K_*}=2e^{2K_*}.
\]

Therefore

\[
\boxed{
|\mathcal P_{\kappa\sigma}^{tilt}|
\le
C_{K_*}
\int
|k|\,|q(k)|dk.
}
\]

Using the spatial representation and Jensen/triangle inequality,

\[
\boxed{
|\mathcal P_{\kappa\sigma}^{tilt}|
\le
C_{K_*}
\left\langle
\int
\chi\rho^2
|\kappa|
\left|\sigma-\frac14\right|dy
\right\rangle.
}
\]

Thus a large phase-tilt payer requires a genuine weighted coexistence of nontrivial coefficient phase and quarter-strain departure.

## 6. Near-zero coefficient populations suppress the phase tilt

If the relevant residence population is confined to

\[
|\kappa|\le\delta,
\]

then

\[
|e^{2\kappa}-1|
\le
C_{K_*}\delta.
\]

Consequently

\[
\boxed{
|\mathcal P_{\kappa\sigma}^{tilt}|
\le
C_{K_*}\delta
\left\langle
\int
\chi\rho^2
\left|\sigma-\frac14\right|dy
\right\rangle.
}
\]

On a compact hull with a uniform weighted strain/mass bound, the right side tends to zero with `delta`.

Therefore a fixed order-one exponential tilt payer cannot be generated entirely inside an arbitrarily thin near-zero coefficient corridor unless the weighted strain-residence magnitude itself decompactifies.

This is complementary to M17-397: near-zero coefficient **diffusion** may be large, but near-zero coefficient **exponential phase tilt** is small because the exponential weight approaches one.

## 7. Fixed positive tilt forces coefficient/strain phase segregation

Suppose

\[
|\mathcal P_{\kappa\sigma}^{tilt}|
\ge p_*>0
\]

on a compact recurrent branch.

Then Section 5 implies

\[
\boxed{
\left\langle
\int
\chi\rho^2
|\kappa|
\left|\sigma-\frac14\right|dy
\right\rangle
\ge
c(K_*)p_*>0.
}
\]

Thus the remaining non-gradient M5-688 strain payer is an explicit coefficient-phase/strain-residence segregation charge.

It cannot be supplied by a population simultaneously collapsing to `kappa=0` and `sigma=1/4` in the weighted sense.

## 8. Revised M5-688 payer split

M17-398 gave

\[
D_\kappa>0
\Longrightarrow
\text{palinstrophy bulk}
\lor Q_\sigma^{(2)}
\lor B_\kappa
\lor\text{threshold/interface channels}.
\]

M17-399 sharpens this to

\[
\boxed{
\begin{aligned}
D_\kappa>0
\Longrightarrow{}&
H_{palinstrophy/collar\ gradient\ firewall}\\
&\lor H_{\kappa\text{-}phase\ tilt\ strain\ segregation}\\
&\lor H_{threshold\ coefficient\ gradient}\\
&\lor H_{cutoff/threshold\ replenishment}\\
&\lor G_{zero/interface/genealogy}.
\end{aligned}
}
\]

The broad phrase `strain-residence payer` is no longer needed as an independent terminal category.

## 9. Why the phase-tilt channel is still OPEN

The phase-tilt quantity is signed.

No monotone or globally finite ancestral functional is presently known for

\[
\int
\chi\rho^2
(e^{2\kappa}-1)
\left(\sigma-\frac14\right)dy.
\]

Nor does its order-one normalized recurrence contradict the M17-307 palinstrophy ledger, because it is not itself palinstrophy.

Thus M17-399 identifies the exact residual signed-work channel but does not close it.

## 10. Relation to M17-322

M17-322 independently decomposes line-weight memory into

\[
\log\Phi
\quad\text{and}\quad
\log(L_\rho/\Phi),
\]

with

\[
\frac d{d\theta}
\log\frac{L_\rho}{\Phi}
=
2\left(\bar\sigma_\rho-\frac14\right).
\]

Therefore the quarter-strain factor in `P_tilt` is exactly the instantaneous generator of the strain-residence memory channel.

M17-399 shows that M5-688 sees not generic residence memory, but the part of that generator **correlated with coefficient phase through `e^{2kappa}-1`**.

This identifies the next natural dynamic variable without introducing a DSD hypothesis.

## 11. DSD audit role

The DSD role is a signed-payer decomposition audit.

An exponential weighting can make an old signed quantity appear to be a new source.

Subtracting the unweighted part exposes the exact additional information carried by the weight.

The canonical decomposition is elementary algebra plus the existing M17-186 cutoff identity.

## 12. Audit verdict

**PASS — the independent strain-residence branch is reduced to a `kappa`-phase-tilt covariance channel.**

The current non-palinstrophy payer frontier is now

\[
\boxed{
\mathcal P_{\kappa\sigma}^{tilt},
\qquad
B_\kappa,
\qquad
\text{cutoff/threshold replenishment},
\qquad
\text{zero/interface/genealogy}.
}
\]

The next highest-value task is to derive the material evolution or generation cost of `P_tilt` and test whether maintaining a fixed phase tilt requires coefficient turnover, strain deformation, or threshold transport already controlled by the newer M17-388/392/393 ledgers.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
