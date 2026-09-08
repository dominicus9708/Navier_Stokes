# DSD M17-394 — Sign-preserving coefficient-scale migration has an exact log-`kappa` constitutive identity and returns to weighted multiplier diffusion with the amplitude/source firewall intact

Date: 2026-09-08  
Canonical ID: **M17-394**

Status: **ACTIVE MIGRATION-TO-DIFFUSION BRIDGE / LOG-COEFFICIENT IDENTITY / ZERO-LEVEL SEPARATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-393

On a physical sign-preserving CE-H interval with

\[
\kappa\ne0,
\]

M17-393 defines the intrinsic coefficient scale

\[
r_\kappa=|\kappa|^{-1/2}
\]

and the migration action

\[
\boxed{
\mathcal A_{mig}(I)
:=
\int_I
\frac{|D_t\kappa|}{|\kappa|}dt.
}
\]

It also gives

\[
D_t\log r_\kappa
=-\frac12\frac{D_t\kappa}{\kappa}.
\]

The open question is whether this migration action connects to an already existing coefficient-diffusion ledger.

The answer is yes at the constitutive level, but not yet at the level of a finite global budget.

## 2. Physical CE-H coefficient equation

In the repository normalization `nu=1`, M17-339 gives

\[
\boxed{
D_t\kappa
=
L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{geom},
}
\]

where

\[
L_\rho f
:=
\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

All identities below are restricted to a connected spacetime region on which the sign of `kappa` is fixed.

Crossing `kappa=0` is handled separately by M17-323/326/338--346.

## 3. Exact weighted logarithmic chain rule

Set

\[
z:=\log|\kappa|.
\]

For every nonzero `kappa`,

\[
\nabla z
=\frac{\nabla\kappa}{\kappa}.
\]

A direct calculation with the weighted operator gives

\[
\boxed{
L_\rho z
=
\frac{L_\rho\kappa}{\kappa}
-
\frac{|\nabla\kappa|^2}{\kappa^2}.
}
\]

Equivalently,

\[
\boxed{
\frac{L_\rho\kappa}{\kappa}
=
L_\rho\log|\kappa|
+|
\nabla\log|\kappa|
|^2.
}
\]

Divide the M17-339 constitutive law by `kappa`:

\[
\frac{D_t\kappa}{\kappa}
=
\frac{L_\rho\kappa}{\kappa}
+
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
\]

Therefore

\[
\boxed{
D_t\log|\kappa|
=
L_\rho\log|\kappa|
+
|\nabla\log|\kappa||^2
+
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
}
\]

This is the main pointwise M17-394 identity.

## 4. Exact intrinsic-scale evolution

Since

\[
\log r_\kappa=-\frac12\log|\kappa|,
\]

Section 3 gives

\[
\boxed{
\begin{aligned}
D_t\log r_\kappa
={}&-
\frac12L_\rho\log|\kappa|\\
&-
\frac12|\nabla\log|\kappa||^2\\
&-
\frac12
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
\end{aligned}
}
\]

Thus sign-preserving scale travel is serviced by exactly three channels:

1. weighted transport/diffusion of `log |kappa|`;
2. positive log-gradient diffusion density;
3. normalized strain/geometric forcing.

There is no fourth free migration mechanism inside the smooth sign-preserving CE-H branch.

## 5. The natural spatial diffusion density

The positive pointwise term is

\[
|\nabla\log|\kappa||^2
=
\frac{|\nabla\kappa|^2}{\kappa^2}.
\]

The weighted CE-H density is therefore

\[
\boxed{
D_{\log\kappa}
:=
\rho^2
|\nabla\log|\kappa||^2
=
\rho^2
\frac{|\nabla\kappa|^2}{\kappa^2}.
}
\]

This is the natural spatial currency attached to logarithmic coefficient-scale migration.

It is not the zero-level crossing currency and must not be identified with it.

## 6. Relation to M17-235 on one intrinsic scale

On an intrinsic coefficient cell of physical radius `R` satisfying

\[
c_\kappa R^{-2}
\le
|\kappa|
\le
C_\kappa R^{-2},
\]

we have

\[
\kappa^{-2}\asymp R^4.
\]

Hence

\[
\boxed{
\int_B
\rho^2|\nabla\log|\kappa||^2dx
\asymp
R^4
\int_B
\rho^2|\nabla\kappa|^2dx.
}
\]

Thus the new log-coefficient diffusion is not an unrelated quantity.

It is the scale-normalized form of the existing M17-235 weighted multiplier-gradient diffusion.

M17-235 gives, on its mean-dominated compact branch and absent a dimensionless pointwise gradient spike,

\[
\int_B
\rho^2|\nabla\kappa|^2dx
\gtrsim
M_B R^{-6},
\]

where

\[
M_B:=\int_B\rho^2dx.
\]

Therefore

\[
\boxed{
\int_B
\rho^2|\nabla\log|\kappa||^2dx
\gtrsim
M_B R^{-2}.
}
\]

This is the intrinsic log-diffusion lower bound.

## 7. Own-scale time interpretation

If the same scale-`R` cell persists for one physical own-scale time

\[
|I_R|\asymp R^2
\]

and the M17-235 lower bound persists with comparable packet mass, then formally

\[
\int_{I_R}\int_B
\rho^2|\nabla\log|\kappa||^2dxdt
\gtrsim
M_B
\]

up to persistence and overlap constants.

Thus one persistent intrinsic scale episode carries an order-`M_B` log-diffusion payment.

However this is still amplitude weighted.

If

\[
M_B\to0,
\]

the payment can vanish.

Therefore the M17-235 amplitude firewall survives unchanged.

## 8. Material-domain integrated identity

Let `chi(x,t)` be a smooth material cutoff satisfying

\[
D_t\chi=0
\]

and supported inside one sign-preserving CE-H region.

Physical vorticity amplitude satisfies, in repository normalization,

\[
D_t\rho=(\sigma+\kappa)\rho.
\]

Hence

\[
D_t(\rho^2)
=2(\sigma+\kappa)\rho^2.
\]

Multiply the pointwise log identity by `chi rho^2` and integrate over space.

Since

\[
\rho^2L_\rho z
=
\nabla\cdot(\rho^2\nabla z),
\]

integration by parts gives

\[
\boxed{
\begin{aligned}
\frac d{dt}
\int\chi\rho^2 z\,dx
={}&
\int\chi\rho^2|\nabla z|^2dx\\
&-
\int\rho^2\nabla\chi\cdot\nabla z\,dx\\
&+
\int\chi\rho^2
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}dx\\
&+
2\int\chi\rho^2(\sigma+\kappa)z\,dx.
\end{aligned}
}
\]

Here

\[
z=\log|\kappa|.
\]

This identity spatializes the sign-preserving migration channel.

The positive diffusion term is explicit, but so are the cutoff, normalized forcing, and amplitude-growth terms.

Therefore no monotonicity is claimed.

## 9. Why M17-343/346 do not directly close migration

M17-343/346 concern regular crossings of the level

\[
\kappa=0
\]

and produce a scale-critical spatial zero-crossing currency.

By contrast, `log |kappa|` is singular at zero.

A regular crossing

\[
\kappa(t)\sim a(t-t_0)
\]

would make

\[
\int
\frac{|D_t\kappa|}{|\kappa|}dt
\]

logarithmically divergent near `t_0`, even though the physical zero-crossing event has a finite canonical M17-338/346 charge.

Therefore

\[
\boxed{
\mathcal A_{mig}
\text{ is not a valid zero-crossing currency.}
}
\]

The correct split is:

- use log-`kappa` migration only away from zero on sign-preserving intervals;
- use M17-323/326/338--346 at zero.

This prevents a coordinate singularity from being mistaken for a physical infinite payer.

## 10. Migration-action payer split

Combining Sections 3--9, a large sign-preserving coefficient-scale journey satisfies

\[
\boxed{
\begin{aligned}
H_{large\ log\text{-}scale\ migration}
\Longrightarrow{}&
H_{log\text{-}coefficient\ weighted\ diffusion}\\
&\lor H_{normalized\ strain\ diffusion/source}\\
&\lor H_{normalized\ geometric\ source}\\
&\lor G_{amplitude/cutoff\ boundary}\\
&\lor H_{zero\text{-}level\ crossing}.
\end{aligned}
}
\]

On a fixed intrinsic scale, the first branch is exactly the scale-normalized M17-235 multiplier-diffusion channel.

## 11. Why the global proof is still open

No certified finite first-generation total budget is presently available for

\[
\int\rho^2
|\nabla\log|\kappa||^2dxdt,
\]

nor for the normalized source integrals

\[
\int
\rho^2
\frac{|L_\rho\sigma+\mathcal R_{geom}|}{|\kappa|}dxdt.
\]

Moreover the M17-235 lower bound retains the packet mass factor `M_B`.

Therefore migration has been returned to existing PDE channels without eliminating the low-amplitude/source firewall.

## 12. DSD audit role

The DSD role is a representation and coordinate audit:

- the correct variable for scale migration is `log |kappa|`, not raw `kappa`;
- the correct spatial gradient is therefore `grad log |kappa|`;
- the zero level must be excised because logarithmic coordinates are singular there;
- intrinsic-scale comparison converts the log-gradient channel back to the already existing weighted multiplier diffusion.

The canonical mathematics is the weighted chain rule, the M17-339 physical constitutive law, and integration by parts.

## 13. Audit verdict

**PASS — sign-preserving scale migration is returned to an existing diffusion/source architecture.**

The untyped migration action of M17-393 is sharpened to

\[
\boxed{
D_t\log|\kappa|
=
L_\rho\log|\kappa|
+|\nabla\log|\kappa||^2
+\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
}
\]

The remaining hard firewall is now explicit:

\[
\boxed{
\text{amplitude-weighted log-diffusion}
\quad\text{and}\quad
\text{normalized strain/geometric source control}.
}
\]

The next highest-value task is to determine whether the persistent high-amplitude/positive-flux branches already established in M17-190/361/391 can remove the amplitude factor on a non-negligible part of this log-diffusion channel, or whether low-amplitude segregation remains a genuine escape.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
