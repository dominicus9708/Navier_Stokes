# DSD M17-390 — Compact loop recurrence yields only logarithmic physical deformation and the similarity energy weight absorbs infinite recurrence unless normalized multiplicity or amplitude grows supercritically

Date: 2026-09-08  
Canonical ID: **M17-390**

Status: **ACTIVE RECURRENCE-ENERGY FIREWALL / SIMILARITY-TO-PHYSICAL THRESHOLD THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs and scope

This module compares four already certified late-CE-H facts:

1. M17-188 gives the exact similarity loop-length law
   \[
   \frac d{d\theta}\log\ell_\Gamma
   =\bar\sigma_{ds}^{sim}+\frac12.
   \]
2. M17-360 reduces a compact nondegenerate closed-loop orbit to a recurrent minimal hull, but explicitly does **not** prove positive-density shadowing of that hull by the original orbit.
3. M17-388 gives the physical persistent-cell deformation ledger
   \[
   \sum_j R_jK_j^2<\infty
   \]
   under bounded temporal overlap.
4. M17-389 shows that logarithmic negative-`kappa` flux exposure is a diffusive flux currency and cannot be silently identified with strain deformation.

The present goal is to determine whether compact loop recurrence or long similarity residence can by itself overcome the M17-388 energy firewall.

It cannot.

The result below is a quantitative no-go and threshold theorem, not a regularity proof.

## 2. Exact similarity/physical strain dictionary

Write

\[
s:=-t>0,
\qquad
\theta=-\log s,
\qquad
 y=\frac{x}{\sqrt s}.
\]

For the velocity gradient and aligned strain,

\[
\Sigma^{sim}=s\Sigma^{ph},
\qquad
\sigma^{sim}=s\sigma^{ph}.
\]

Also

\[
dt=s\,d\theta.
\]

For a material loop, physical and similarity arclength satisfy

\[
ds_x=\sqrt s\,ds_y,
\qquad
\ell_{ph}=\sqrt s\,\ell_{sim}.
\]

Therefore the arclength means obey

\[
\bar\sigma_{ds}^{ph}
=\frac1s\bar\sigma_{ds}^{sim}.
\]

Hence the signed line-mean strain measure is exactly representation invariant:

\[
\boxed{
\bar\sigma_{ds}^{ph}\,dt
=
\bar\sigma_{ds}^{sim}\,d\theta.
}
\]

Likewise

\[
\boxed{
\|\Sigma^{ph}\|_{L^\infty}\,dt
=
\|\Sigma^{sim}\|_{L^\infty}\,d\theta.
}
\]

Thus physical deformation can be computed directly in similarity time without a scaling ambiguity.

## 3. Compact loop length forces linear-in-similarity-time deformation

The exact M17-188 length law is

\[
\frac d{d\theta}\log\ell_\Gamma
=
\bar\sigma_{ds}^{sim}+\frac12.
\]

Integrating from `theta_0` to `theta_1`,

\[
\int_{\theta_0}^{\theta_1}
\bar\sigma_{ds}^{sim}d\theta
=
\log\frac{\ell_\Gamma(\theta_1)}{\ell_\Gamma(\theta_0)}
-
\frac12(\theta_1-\theta_0).
\]

Assume the same material loop remains in the compact nondegenerate class

\[
0<\ell_*\le\ell_\Gamma(\theta)\le\ell^*<\infty.
\]

Set

\[
C_\ell:=\log\frac{\ell^*}{\ell_*}.
\]

Then

\[
\left|
\int_{\theta_0}^{\theta_1}
\bar\sigma_{ds}^{sim}d\theta
\right|
\ge
\frac12\Delta\theta-C_\ell,
\qquad
\Delta\theta:=\theta_1-\theta_0.
\]

Since

\[
|\bar\sigma_{ds}^{sim}|
\le
\|\Sigma^{sim}\|_\infty,
\]

we obtain the exact deformation lower bound

\[
\boxed{
K^{ph}[t_0,t_1]
:=
\int_{t_0}^{t_1}\|\Sigma^{ph}\|_\infty dt
\ge
\frac12\Delta\theta-C_\ell.
}
\]

This conclusion does **not** require recurrence.

Compact persistence of the same material loop alone forces order-one strain per order-one similarity time.

Recurrence is needed for the stronger M17-188 covariance identities, but not for this length-law deformation bound.

## 4. The deformation is only logarithmic in the similarity geometric scale

The similarity geometric conversion scale is

\[
R_\theta:=\sqrt s=e^{-\theta/2}.
\]

Therefore

\[
\Delta\theta
=2\log\frac{R_{\theta_0}}{R_{\theta_1}}.
\]

Section 3 gives

\[
\boxed{
K^{ph}[t_0,t_1]
\ge
\log\frac{R_{\theta_0}}{R_{\theta_1}}
-C_\ell.
}
\]

Thus compact loop persistence down a geometric similarity descent forces at least logarithmic accumulated physical deformation.

Important scope correction:

- `R_theta` is the physical scale associated with the similarity map;
- it is **not automatically identical** to the physical intrinsic coefficient scale `|kappa^ph|^{-1/2}`;
- identifying the two requires the corresponding coefficient-scale/parent-to-M17 map, for example a retained `|kappa^sim| asymp 1` population.

Hence this module does not silently equate similarity scale and coefficient scale.

## 5. Exact standard-energy ledger in similarity variables

Similarity vorticity satisfies

\[
W(y,\theta)=s\Omega(x,t).
\]

Because

\[
dx=s^{3/2}dy,
\]

we have

\[
\|\Omega(t)\|_2^2
=s^{-1/2}\|W(\theta)\|_2^2.
\]

Multiplying by

\[
dt=s\,d\theta
\]

gives

\[
\boxed{
\|\Omega(t)\|_2^2dt
=
e^{-\theta/2}\|W(\theta)\|_2^2d\theta.
}
\]

Therefore the ordinary finite-energy Navier--Stokes inequality becomes

\[
\boxed{
\nu
\int_{\theta_0}^{\infty}
 e^{-\theta/2}
\|W(\theta)\|_2^2d\theta
<\infty.
}
\]

The exponentially decaying factor

\[
\boxed{e^{-\theta/2}}
\]

is the decisive recurrence firewall.

## 6. Infinite compact recurrence is compatible with finite physical energy

Suppose a recurrent compact normalized CE-H state has

\[
0<E_*\le\|W(\theta)\|_2^2\le E^*<\infty
\]

for arbitrarily large similarity times.

Even in the strongest case in which this lower bound holds for **all** sufficiently large `theta`, its physical energy-dissipation contribution is only

\[
\int_{\theta_0}^{\infty}
 e^{-\theta/2}E_*d\theta
<\infty.
\]

Thus

\[
\boxed{
\text{infinite similarity-time recurrence/residence}
\not\Rightarrow
\text{physical energy contradiction}.
}
\]

This is stronger than merely saying that infinitely many isolated recurrence times are cheap.

Even permanent normalized occupancy is compatible with the standard physical energy ledger because the physical time/space scale shrinks exponentially.

## 7. Positive-flux high-amplitude loop families and multiplicity threshold

On the compact high-amplitude loop branch used in M17-190, suppose one loop family has

\[
\rho\ge a_*>0,
\qquad
\ell_\Gamma\ge\ell_*>0,
\qquad
\Phi(\mathcal A)\ge\Phi_*>0.
\]

Using flux coordinates

\[
dy=\frac{d\Phi\,ds}{\rho},
\]

the normalized enstrophy carried by that family satisfies

\[
\int_{\mathcal T}|W|^2dy
=
\int_{\mathcal A}\int_\Gamma\rho\,ds\,d\Phi
\ge
 a_*\ell_*\Phi_*
=:
e_*>0.
\]

Now suppose there are `M(theta)` pairwise disjoint flux-tube families with the same uniform lower constants, so their normalized enstrophy contributions are genuinely additive.

Then

\[
\|W(\theta)\|_2^2
\ge e_*M(\theta).
\]

The standard energy ledger therefore requires

\[
\boxed{
\int^\infty e^{-\theta/2}M(\theta)d\theta<\infty.
}
\]

For fixed-width similarity blocks with

\[
R_j:=e^{-\theta_j/2},
\]

and a blockwise multiplicity lower bound `M_j`, this becomes schematically

\[
\boxed{
\sum_jR_jM_j<\infty.
}
\]

Thus logarithmic or polynomial-in-`theta` multiplicity is still cheap.

For a power law

\[
M_j\sim R_j^{-\alpha},
\]

the geometric series crosses the non-summability threshold only at

\[
\boxed{\alpha\ge1.}
\]

This criterion requires genuinely disjoint/additive families. Mere counting of overlapping loop descriptions does not qualify.

## 8. M17-388 deformation threshold

M17-388 gives, for bounded-overlap persistent physical own-scale episodes,

\[
\boxed{
\sum_jR_jK_j^2<\infty.
}
\]

Therefore a sufficient per-generation contradiction threshold is

\[
K_j\gtrsim R_j^{-1/2}
\]

on infinitely many geometrically separated episodes, because then each term `R_j K_j^2` is order one.

More generally, if

\[
K_j\sim R_j^{-\alpha},
\]

the geometric weighted-`l2` series becomes non-summable only for

\[
\boxed{\alpha\ge\frac12.}
\]

By contrast, the compact-loop length law supplies only

\[
K(R)\gtrsim\log\frac1R,
\]

and

\[
\boxed{
\sum_jR_j\log^2\frac1{R_j}<\infty
}
\]

on geometric scales.

Hence the exact compact-loop deformation lower bound is **far below** the M17-388 contradiction threshold.

This confirms and sharpens the heuristic firewall noted after M17-389.

## 9. Recurrence count is not automatically an additive deformation cost

One must not replace

\[
\text{number of returns}
\]

by

\[
K_I
\]

without a per-return independent strain impulse theorem.

The same continuous strain history can support many close returns.

If return periods collapse to zero, the possible payer is instead a time-jet/turnover decompactification, not automatically extra `K`.

Thus a statement such as

\[
N_{return}\to\infty
\Rightarrow
K\to\infty
\]

is not canonical without a quantitative minimum return-time or minimum strain-action hypothesis.

The exact length law already captures the strain action that is definitely forced.

## 10. M17-360 minimal-hull firewall remains

M17-360 proves that a compact nondegenerate closed-loop orbit has a recurrent minimal subsystem in its omega-limit hull.

It explicitly does **not** prove that the original physical orbit spends positive density of time near that minimal subsystem.

Therefore the recurrent M17-188/M17-361 gradient or palinstrophy payer cannot be charged to every physical generation merely because it exists on the omega-limit hull.

A valid physical summation needs at least one of

1. positive-density shadowing/residence near the recurrent hull;
2. a same-material recurrence theorem on the original orbit;
3. a transfer theorem showing that the hull payer pulls back to a positive physical spacetime measure;
4. an independent compactness failure/genealogy exit.

Without such a bridge, recurrence existence and physical budget occupancy must remain distinct.

## 11. M17-379 exposure cascade also remains below the energy threshold

M17-379 gives the scale-corrected flux-exposure ledger

\[
\boxed{
\sum_m\tau_m^{own}
\gtrsim
\log\frac1r.
}
\]

M17-389 shows that this is a `kappa`-diffusive flux currency, not a strain currency.

Therefore it cannot be inserted directly into

\[
\sum_jR_jK_j^2<\infty.
\]

Even under the **stronger hypothetical identification**

\[
K\gtrsim\sum_m\tau_m^{own}
\gtrsim\log\frac1r,
\]

the energy cost would still be only

\[
R\log^2\frac1R,
\]

which is geometrically summable.

Hence neither branch of M17-379 by itself beats the standard-energy firewall:

- one diverging own-scale residence can still correspond to logarithmic or slower physical deformation;
- logarithmically many active coefficient scales are also far below the multiplicity threshold `M~R^{-1}`.

## 12. Exact threshold split for the compact recurrence branch

The compact late-CE-H recurrence branch is therefore sharpened to

\[
\boxed{
\begin{aligned}
H_{compact\ persistent/recurrent\ loop}
\Longrightarrow{}&
H_{energy\text{-}summable\ logarithmic\ deformation}\\
&\lor
G_{normalized\ enstrophy/amplitude\ growth}\\
&\lor
G_{disjoint\ multiplicity\ growth}\\
&\lor
G_{turnover/time\text{-}jet\ decompactification}\\
&\lor
G_{loop/CEH/interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

To contradict the certified standard-energy ledger through this route, a downstream theorem must force a genuinely non-summable enhancement such as

\[
\boxed{
\sum_jR_jK_j^2=\infty
}
\]

or, for disjoint additive normalized families,

\[
\boxed{
\sum_jR_jM_j=\infty.
}
\]

Order-one recurrence, logarithmic residence, and logarithmically many coefficient scales are insufficient.

## 13. DSD audit role

The DSD contribution is a currency-and-clock audit:

- similarity recurrence time is not itself a physical dissipation cost;
- normalized loop occupancy must be multiplied by the exact physical similarity weight;
- recurrence count is not automatically deformation action;
- coefficient own-scale residence is not automatically strain residence;
- spatial multiplicity is additive only for genuinely disjoint resource populations.

All canonical identities used above are standard similarity scaling, material-line kinematics, flux coordinates, and the Navier--Stokes energy inequality.

## 14. Audit verdict

**PASS — major recurrence firewall and quantitative threshold refinement.**

The compact recurrence branch does not currently produce a global contradiction.

The next high-value target is no longer to prove that recurrence or logarithmic residence occurs. Those are already too cheap.

The next target is to determine whether the remaining strict-subscale/turnover/gradient branches force **supercritical normalized growth** strong enough to violate one of the two exact thresholds

\[
\sum_jR_jK_j^2<\infty,
\qquad
\sum_jR_jM_j<\infty.
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
