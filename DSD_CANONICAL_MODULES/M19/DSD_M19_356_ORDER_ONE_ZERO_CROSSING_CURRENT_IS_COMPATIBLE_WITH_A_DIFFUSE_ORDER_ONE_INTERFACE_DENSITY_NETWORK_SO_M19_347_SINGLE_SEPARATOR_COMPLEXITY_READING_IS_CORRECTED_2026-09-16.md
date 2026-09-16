# DSD M19-356 — Order-one zero-crossing current is compatible with a diffuse order-one interface-density network; the M19-347 single-separator complexity reading is corrected

Date: 2026-09-16  
Canonical ID: **M19-356**

Status: **ACTIVE REPRESENTATION CORRECTION / ZERO-CURRENT SCALING WITNESS / M17-204 CONVEYOR REJOIN**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-355

On the scale-free bi-Lipschitz compact branch, M19-355 produces fixed away-zero material-flux coefficient actions on a positive parent-time fraction:

\[
A_+^\Phi(t)\ge a_*>0,
\qquad
A_-^\Phi(t)\ge a_*>0.
\]

The exact sign-flux balances are

\[
\dot\Phi_+
=
\nu A_+^\Phi+C_0^\Phi,
\]

\[
\dot\Phi_-
=
-\nu A_-^\Phi-C_0^\Phi.
\]

Since \(\Phi_\pm\) are bounded by the retained total material flux, integrating over a parent record \(J_R\) of length \(\asymp R^2\) gives

\[
\boxed{
-\int_{J_R}C_0^\Phi(t)dt
\gtrsim
R^2
}
\]

up to bounded endpoint terms and the explicitly controlled exceptional-time set.

Thus the negative zero-crossing current is order one in parent-time average.

## 2. Exact transverse sweep representation

M19-340 gives on a regular represented transverse section

\[
\boxed{
C_{0,A}^\Phi(t)
=
-\int_{Z_A(t)}
\rho\,v_0\,d\ell,
}
\]

where

\[
Z_A(t)=\{\kappa=0\}\cap A_t,
\qquad
v_0=-\frac{D_t\kappa}{|\nabla_\perp\kappa|}.
\]

Hence

\[
|C_0^\Phi(t)|
\le
\int_{Z_A(t)}
\rho|v_0|d\ell.
\]

Section 1 therefore forces the spacetime sweep lower bound

\[
\boxed{
\int_{J_R}dt
\int_{Z_A(t)}
\rho|v_0|d\ell
\gtrsim
R^2.
}
\]

This lower bound is rigorous within the retained representation.

## 3. Correction to the M19-347 reference scale

M19-347 compared the zero set with one regular separator across a mesoscopic cross-section of area

\[
|A_R|\asymp R.
\]

Such a single separator has natural length

\[
\mathcal H^1(Z_A)\asymp R^{1/2}.
\]

Under the diffuse amplitude \(\rho\sim R^{-1}\) and bounded speed, one separator pays only

\[
|C_0^\Phi|
\sim
R^{-1}R^{1/2}
=R^{-1/2}.
\]

M19-347 therefore correctly showed that **one** regular separator is insufficient for an order-one current.

However the conclusion

\[
\mathcal H^1(Z_A)\gtrsim R
\quad\Rightarrow\quad
\text{scale-free geometry decompactification}
\]

is too strong.

The correct geometry must be normalized by transverse area.

## 4. Canonical zero-interface density

Define the zero-interface length density

\[
\boxed{
\Lambda_0(A_R)
:=
\frac{\mathcal H^1(Z_A)}{|A_R|}.
}
\]

On the canonical diffuse baseline

\[
|A_R|\asymp R.
\]

If the coefficient-sign pattern has own-scale cells at order-one spatial density across the mesoscopic section, then the total zero-interface length naturally satisfies

\[
\boxed{
\mathcal H^1(Z_A)
\asymp R,
\qquad
\Lambda_0(A_R)\asymp1.
}
\]

This is not a shape blow-up. It is an extensive interface network with fixed interface density.

## 5. The interface-density witness pays the current exactly

Take the scaling audit

\[
\boxed{
|A_R|\sim R,
\qquad
\rho\sim R^{-1},
\qquad
|v_0|\sim1,
\qquad
\mathcal H^1(Z_A)\sim R.
}
\]

Then

\[
\boxed{
\int_{Z_A}\rho|v_0|d\ell
\sim
R^{-1}\cdot1\cdot R
\sim1.
}
\]

Thus an order-one zero-crossing current is fully compatible with the diffuse amplitude baseline if the zero-interface network has order-one length density.

This is a scaling witness, not an exact Navier--Stokes solution.

## 6. Resource audit of the same witness

Assume additionally compact coefficient transition scales

\[
|\nabla_\perp\kappa|\sim1.
\]

The cross-sectional zero-current currency is

\[
j_{0,A}
:=
\int_{Z_A}ho^2|\nabla\kappa|d\ell.
\]

Under the witness,

\[
\boxed{
j_{0,A}\sim R^{-1}.}
\]

Lifting through a parent-length tube of length \(\sim R\) gives a three-dimensional snapshot zero-current of order one:

\[
\boxed{J_0^{snap}\sim1.}
\]

This is exactly compatible with the compact M17-470 raw-H2 corridor and the M17-453 diffuse resource scaling.

Likewise the weighted coefficient-gradient currency satisfies schematically

\[
\int\rho^2|\nabla\kappa|^2dx
\sim1
\]

at snapshot level. Over \(O(R^2)\) parent time its M17-445 \(R^{-5}\) ancestry cost is only \(O(R^{-3})\), strongly summable.

Thus neither the zero-current/raw-H2 ledger nor the coefficient-gradient ledger excludes the interface-density witness.

## 7. Relation to palinstrophy

The exact whole-space CE-H identity gives

\[
P_R
=
K_- -K_+.
\]

M17-458 forces this signed difference to be very small on typical good times even though \(K_\pm\sim1\).

A dense coefficient-sign interface network does not by itself force a large amplitude gradient: the sign boundary is a \(\kappa\)-interface, not a nodal boundary of \(\Omega\).

Therefore

\[
\boxed{
\mathcal H^1(Z_A)\sim R
\not\Rightarrow
P_R\gtrsim1
}
\]

without an additional amplitude/interface coercivity theorem.

This is consistent with M17-446's low-amplitude/measure-mismatch firewall.

## 8. Rejoin M17-204

M17-204 already established that a strictly negative recurrent zero-level multiplier current is coherent with the M5 conveyor and is **not** a sign contradiction.

The current M19 chain strengthens the measure incidence:

\[
\text{sign moments}
\to
\text{threshold material flux}
\to
\text{order-one negative zero current},
\]

but Section 5 shows that the diffuse mesoscopic geometry has enough extensive interface capacity to carry that current at baseline cost.

Therefore the M17-204 firewall applies again:

\[
\boxed{
\text{further local zero-current sign chasing is duplicative without a nonrecyclable budget.}
}
\]

## 9. Corrected geometry split

M19-347 should now be read as

\[
\boxed{
\text{order-one current}
\Longrightarrow
\text{nonvanishing zero-interface density/speed/amplitude product},
}
\]

not as an automatic geometry decompactification statement.

More precisely, define

\[
\rho_Z^{eff}
:=
\frac1{|Z_A|}
\int_{Z_A}\rho d\ell,
\]

and an analogous current-weighted effective speed. Then the natural extensive balance is

\[
\boxed{
|C_0^\Phi|
\sim
|A_R|
\left(
\frac{|Z_A|}{|A_R|}
\right)
\rho_Z^{eff}v_Z^{eff}.
}
\]

With \(|A_R|\sim R\) and \(\rho_Z^{eff}\sim R^{-1}\), order-one current requires only

\[
\boxed{
\Lambda_0v_Z^{eff}\sim O(1).
}
\]

## 10. What is genuinely left

The zero-current lane can advance only if one proves that an order-one-density moving sign-interface network necessarily pays a **nonrecyclable** resource.

The live possibilities are now

\[
\boxed{
\begin{aligned}
G_{\rm diffuse\ zero\text{-}interface\ conveyor}
\Longrightarrow{}&
G_{\rm finite\ cumulative\ payer\ budget}\\
&\lor G_{\nabla_T(D_t\kappa)\rm\ coercivity}\\
&\lor G_{\rm irreversible\ component/interface\ genealogy}\\
&\lor G_{\rm amplitude\text{-}interface\ palinstrophy\ coercivity}\\
&\lor G_{\rm terminal\ dilation\text{-}hull\ coupling}.
\end{aligned}
}
\]

These are exactly the kinds of nonrecyclable mechanisms demanded by the earlier M17-204 audit.

## 11. Audit verdict

**PASS AS A CORRECTION AND NO-GO.**

M19-355 certifies an order-one integrated oriented zero-crossing current on the scale-free shape-compact branch, but the canonical mesoscopic diffuse geometry can carry it using an order-one-density moving zero-interface network. The required total zero-set length \(O(R)\) is extensive in area, not automatically a scale-free complexity blow-up.

The local sign route therefore rejoins the historical M17-204 conveyor firewall. The next useful target is not the sign of the current, but whether its extensive interface network has a finite nonrecyclable payer or irreversible genealogy cost.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
