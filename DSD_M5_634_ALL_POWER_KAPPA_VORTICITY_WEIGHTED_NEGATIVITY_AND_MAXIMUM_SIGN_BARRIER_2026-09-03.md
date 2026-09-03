# DSD M5-634 — All-power kappa–vorticity weighted negativity and the vorticity-maximum sign barrier

Date: 2026-09-03

Status: **INTERNAL ELLIPTIC SIGN FAMILY / ON CE-H, `Delta W = kappa W` AND `W=rho xi` GIVE THE POINTWISE IDENTITY `kappa rho^2 = (1/2) Delta(rho^2) - |grad W|^2`. AFTER MULTIPLICATION BY `rho^(p-2)` AND INTEGRATION, EVERY `p>=2` SATISFIES `integral kappa rho^p = -(p-1) integral rho^(p-2)|grad rho|^2 - integral rho^p |grad xi|^2 < 0` FOR A NONZERO FIELD. THUS KAPPA HAS NEGATIVE MEAN UNDER EVERY HIGH-AMPLITUDE VORTICITY WEIGHT, NOT ONLY THE ENSTROPHY WEIGHT. AT ANY INTERIOR SPATIAL MAXIMUM OF RHO, `kappa <= -|grad xi|^2 <= 0`. CONSEQUENTLY A POSITIVE SYNCHRONIZED KAPPA LEVEL CANNOT CARRY THE GLOBAL VORTICITY MAXIMUM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pointwise CE-H Rayleigh density identity

On CE-H,

\[
\Delta W=\kappa W.
\]

For every smooth vector field,

\[
W\cdot\Delta W
=\frac12\Delta|W|^2-|\nabla W|^2.
\]

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Then

\[
|W|=\rho
\]

and

\[
|\nabla W|^2
=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
\]

Hence

\[
\boxed{
\kappa\rho^2
=\frac12\Delta(\rho^2)
-|\nabla\rho|^2
-\rho^2|\nabla\xi|^2.
}
\]

Equivalently,

\[
\kappa
=\frac{\Delta\rho}{\rho}-|\nabla\xi|^2
\]

where `rho>0`, as already obtained in M5-600.

---

## 2. All-power weighted identity

Let `p>=2` and multiply the pointwise identity by

\[
\rho^{p-2}.
\]

Assuming the inherited decay/all-order Sobolev corridor so that the boundary term vanishes,

\[
\int \kappa\rho^pdy
=\frac12\int\rho^{p-2}\Delta(\rho^2)dy
-\int\rho^{p-2}|\nabla\rho|^2dy
-\int\rho^p|\nabla\xi|^2dy.
\]

Integrating the first term by parts,

\[
\frac12\int\rho^{p-2}\Delta(\rho^2)
=-(p-2)\int\rho^{p-2}|\nabla\rho|^2.
\]

Therefore

\[
\boxed{
\int \kappa\rho^pdy
=-(p-1)\int\rho^{p-2}|\nabla\rho|^2dy
-\int\rho^p|\nabla\xi|^2dy.
}
\]

For a nonzero whole-space `L2` CE-H state, M5-613--614 exclude simultaneous vanishing of the derivative channels, so

\[
\boxed{
\int \kappa\rho^pdy<0
\qquad\forall p\ge2.
}
\]

---

## 3. Special cases

For `p=2`,

\[
\int\kappa\rho^2
=-\int|\nabla\rho|^2
-\int\rho^2|\nabla\xi|^2
=-P,
\]

which is the M5-600 Rayleigh identity.

For larger `p`, the measure

\[
d\mu_p
:=\frac{\rho^pdy}{\int\rho^pdy}
\]

concentrates increasingly strongly on the high-amplitude vorticity region.

Thus

\[
\boxed{
\int\kappa\,d\mu_p<0
\qquad\forall p\ge2.
}
\]

The negative viscous multiplier bias persists all the way toward the amplitude-dominant part of the field.

---

## 4. Spatial maximum sign barrier

Let `y_*` be an interior spatial maximum of `rho` with `rho(y_*)>0`.

Then

\[
\nabla\rho(y_*)=0,
\qquad
\Delta\rho(y_*)\le0.
\]

Using

\[
\kappa
=\frac{\Delta\rho}{\rho}-|\nabla\xi|^2,
\]

we obtain

\[
\boxed{
\kappa(y_*)
\le
-|\nabla\xi(y_*)|^2
\le0.
}
\]

Therefore

\[
\boxed{
\kappa>0
\Longrightarrow
\text{the point cannot be a positive local maximum of }|W|.
}
\]

This is a pointwise maximum-principle barrier inside the CE-H class.

---

## 5. Consequence for a synchronized persistent kappa level

On the M5-628 relabeling branch the persistent fixed-flux network has

\[
\kappa=c_*(\theta),
\qquad
\langle c_*\rangle=0.
\]

If at some time

\[
c_*(\theta)>0,
\]

then no positive local maximum of `rho` can lie on that synchronized level.

Hence

\[
\boxed{
c_*>0
\Longrightarrow
\text{global/high-amplitude vorticity ridges must lie on other kappa levels.}
}
\]

If the synchronized level is also supposed to be the amplitude-dominant production carrier at every return, it follows that such a positive phase is impossible.

Thus a sign-changing zero-mean `c_*` forces **amplitude-ridge migration away from the persistent level during its positive phases**, unless the maximum-carrying role is abandoned.

---

## 6. Relation to M5-630 covariance

The M5-630 mechanism

\[
\langle c_*E_*\rangle<0
\]

is now geometrically natural rather than mysterious:

high vorticity weights are intrinsically biased toward nonpositive `kappa` by the elliptic eigenvalue equation.

Thus negative covariance is compatible with CE-H and cannot be used as a contradiction by itself.

The new information is that any compensating positive `c_*` phase cannot simultaneously carry an amplitude maximum.

This creates a migration/turnover requirement between the persistent flux skeleton and the amplitude-dominant enstrophy sheath.

---

## 7. High-p concentration firewall

The `p->infinity` heuristic is useful but no claim is made here that the normalized measures `mu_p` have a unique limit or that the maximum set is a single point.

The rigorous statements retained are:

\[
\int\kappa\rho^p<0
\quad\forall p\ge2,
\]

and the pointwise maximum sign condition

\[
\kappa\le0
\]

at every positive spatial maximum of `rho`.

Any stronger statement about concentration on a particular persistent lineage requires a separate carrier-attribution argument.

---

## 8. Next target

Combine the maximum sign barrier with the M5-590 production-payer carrier and the M5-633 persistent-spine/renewing-sheath picture.

The target dichotomy is

\[
\boxed{
\text{persistent level remains amplitude-dominant}
\Longrightarrow c_*\le0,
}
\]

versus

\[
\boxed{
\text{positive }c_*\text{ phase}
\Longrightarrow
\text{amplitude-dominant sheath migrates to another level}.
}
\]

Because `mean c_*=0`, this may reduce the surviving covariance mechanism to explicit positive-density sheath migration or to the degenerate subbranch `c_*\equiv0`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]