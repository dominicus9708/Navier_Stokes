# M19-402 — A compact critical seed is not Eulerian-dormant: it rides inside a positive-rate robust curvature-packet renewal background

Date: 2026-09-18

Status: **NEW RECOMPRESSION / ON THE FULLY COMPACT M19-365 CRITICAL SEED LANE, THE DISTINGUISHED MATERIAL SEED HAS UNIFORM POSITIVE VORTICITY AMPLITUDE AND ORDER-ONE CURVATURE AMPLITUDE. UNIFORM FINITE-JET BOUNDS THEREFORE THICKEN EACH SEED POINT INTO A FIXED NORMALIZED EULERIAN NEIGHBORHOOD WITH POSITIVE AMPLITUDE, DIRECTION COHERENCE, AND CURVATURE MARK. SUCH A NEIGHBORHOOD CONTAINS A NATURAL FIXED-FLUX LOCAL VORTEX-TUBE CORE. HENCE A LONG ZERO-FLUX MATERIAL PREHISTORY IS NOT A QUIET EULERIAN DORMANT REGION: THE TINY FUTURE SUBLABEL IS EMBEDDED THROUGHOUT ITS PREHISTORY IN AN ACTIVE ROBUST CURVATURE-PACKET BACKGROUND. COMBINED WITH THE FINITE SAME-LABEL CURVATURE LIFETIME / FIRST-HITTING STAGE WINDOW, A LONG COMPACT CRITICAL PREHISTORY FORCES LINEAR-IN-TIME RENEWAL OF THE AMBIENT CANONICAL CARRIER, OR A TYPED GEOMETRY/AMPLITUDE/REPRESENTATION EXIT. THIS RECONNECTS THE REMOTE ZERO-FLUX SEED TO THE EXISTING RENEWAL CONVEYOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compact critical seed hypotheses

Consider one long material seed history on the fully compact M19-365 lane.

Assume on a time interval \(I_T\) of length \(T\),

\[
\rho(X(\theta),\theta)\ge \rho_->0,
\]

and

\[
Z_{\rm curv}(X(\theta),\theta)
=
\rho|\mathcal K|
\ge z_->0.
\]

The compact all-order CE-H hull gives uniform local bounds

\[
|\nabla\rho|
+
|\nabla \xi|
+
|\nabla Z_{\rm curv}|
\le C_*.
\]

The material seed flux itself may be arbitrarily small:

\[
\phi_{\rm seed}(\theta_0)
\asymp e^{-3T/2}.
\]

The purpose is to distinguish the small **material label** from the surrounding Eulerian field.

---

## 2. Uniform Eulerian thickening around the seed

Choose

\[
r_*>
0
\]

small enough depending only on

\[
\rho_-,
\quad
z_*,
\quad
C_*.
\]

For every \(\theta\in I_T\), on

\[
B_{r_*}(X(\theta))
\]

one then has

\[
\boxed{
\rho\ge \frac{\rho_-}{2},
}
\]

\[
\boxed{
Z_{\rm curv}\ge \frac{z_*}{2},
}
\]

and the vorticity direction varies by at most a fixed small angle:

\[
\boxed{
|\xi(y,\theta)-\xi(X(\theta),\theta)|
\le \varepsilon_\xi.
}
\]

Thus each point of the long material seed history sits inside a fixed-size robust Eulerian curvature packet.

The normalized spatial size of this packet does **not** shrink with the material seed flux.

---

## 3. A fixed-flux local core exists inside the thickened patch

Let

\[
n(\theta):=\xi(X(\theta),\theta).
\]

Take a disk \(D_\theta\) of radius \(c r_*\) transverse to \(n(\theta)\) and contained in the robust patch.

For \(\varepsilon_\xi\) small enough,

\[
\xi\cdot n\ge \frac12
\]

on the disk.

Therefore the oriented vorticity flux through the disk obeys

\[
\begin{aligned}
\Phi_{\rm core}(\theta)
&=
\int_{D_\theta}
W\cdot n\,dA\\
&=
\int_{D_\theta}
\rho\,\xi\cdot n\,dA\\
&\ge
\frac{\rho_-}{4}|D_\theta|.
\end{aligned}
\]

Hence

\[
\boxed{
\Phi_{\rm core}(\theta)\ge \phi_*>0
}
\]

with \(\phi_*\) independent of the seed's tiny material flux and independent of \(T\).

This is the local canonical fixed-flux core associated with the robust Eulerian patch.

---

## 4. The tiny seed is a sublabel inside an order-one active flux neighborhood

At the same time one may have

\[
\phi_{\rm seed}\ll \phi_*.
\]

Thus

\[
\boxed{
\frac{\phi_{\rm seed}}{\Phi_{\rm core}}
\to0
}
\]

toward the remote-past end of a long critical history.

The correct picture is therefore

\[
\boxed{
\text{order-one active Eulerian curvature packet}
\supset
\text{exponentially tiny distinguished material sublabel}.
}
\]

The material seed is dormant only in the sense of its selected flux fraction.

The surrounding Eulerian curvature structure is not dormant.

---

## 5. One fixed material canonical core cannot cover the whole long prehistory

There are two independent finite-lifetime mechanisms already in the repository.

### Curvature-label lifetime

M19-358, using

\[
X=\log\frac{\rho|\mathcal K|}{|\phi|},
\qquad
D_BX=-\frac32,
\]

shows that a fixed-flux curvature-active material label can remain in the retained active window only for a uniformly finite similarity time

\[
T_{\rm curv}<\infty.
\]

### First-hitting ribbon stage window

M17-120 shows that one material ribbon carrier can occupy the same compact first-hitting class for at most

\[
M_{\rm stage}<\infty
\]

stages.

Therefore the robust ambient core surrounding a critical seed history of length \(T\to\infty\) cannot be represented by one fixed material canonical carrier throughout.

---

## 6. Positive-rate ambient renewal

Cover \(I_T\) by canonical curvature-core episodes, each carried by one fixed-flux material label while that label remains in the retained compact active class.

Because each label covers at most a bounded time

\[
\tau_*
:=
\max\{T_{\rm curv},\,C_{\rm stage}M_{\rm stage}\},
\]

the number \(N_{\rm amb}(T)\) of required ambient carrier renewals satisfies

\[
\boxed{
N_{\rm amb}(T)
\ge
\frac{T}{\tau_*}-O(1)
}
\]

unless one of the retained compact hypotheses fails.

Thus

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_{\rm amb}(T)}{T}
\ge
\frac1{\tau_*}
>0.
}
\]

A long compact critical seed prehistory therefore forces a positive renewal rate in the **ambient canonical curvature carrier network**.

---

## 7. Relation to M19-358--360

M19-358 proves

\[
\text{positive curvature occupation}
\Rightarrow
\text{positive material-label renewal density}.
\]

M19-402 shows that a compact critical seed with order-one \(Z_{\rm curv}\) automatically generates the required positive curvature occupation in its surrounding robust Eulerian neighborhood, even when the distinguished seed label itself has exponentially tiny flux.

Therefore the remote zero-flux seed branch does not evade M19-358 by hiding all curvature activity in a vanishing material set.

The vanishing label sits inside a nonvanishing active neighborhood.

M19-359 then routes positive renewal density to positive flux/projective discharge density.

M19-360 remains the essential firewall: the pullback absolute flux of future renewed carriers can still be exponentially discounted.

---

## 8. Corrected meaning of the stationary dormant-seed witness

M19-364 constructs a stationary age-structured seed pipeline with finite instantaneous dormant seed flux/volume.

The present result does not invalidate that scaling witness.

It refines its interpretation:

\[
\boxed{
\text{dormant seed reservoir}
\neq
\text{Eulerian quiescent reservoir}.
}
\]

On the compact critical lane, dormant material sublabels are embedded in an already active, positively renewing curvature-packet background.

Hence a full PDE realization of M19-364 must simultaneously support

1. exponentially small future material labels;
2. order-one local curvature/amplitude around them;
3. positive-rate canonical carrier renewal;
4. recurrent discharge of the renewed canonical carriers.

This is substantially more structured than the age-only witness.

---

## 9. Updated critical seed normal form

The remote-past critical seed branch now reads

\[
\boxed{
\begin{aligned}
G_{\rm zero\text{-}flux}^{3/2}
\Longrightarrow{}&
G_{\rm latent\ material\ sublabel}\\
&+
G_{\rm positive\text{-}rate\ ambient\ canonical\ renewal}\\
&\lor
G_{\rm amplitude/curvature\ compactness\ loss}\\
&\lor
G_{\rm tube/chart/genealogy\ loss}.
\end{aligned}
}
\]

The first line reconnects directly to the M19-359--360 discounted turnover problem.

---

## 10. Next theorem target

The remaining theorem is no longer a minimum seed-size statement.

It is

\[
\boxed{
\mathcal T_{\rm ambient\ renewal}^{nonreuse}:
\text{can the positive-rate canonical carrier renewal forced along one long critical seed history be paid indefinitely by the same recurrent discharge conveyor?}
}
\]

A successful closure must find a non-discounted quantity attached to the **ambient canonical renewal**, not to the exponentially tiny latent seed label.

Candidate channels remain:

\[
\text{projective replacement},
\quad
\text{viscous flux turnover},
\quad
\text{critical palinstrophy incidence},
\quad
\text{genealogical export/return}.
\]

---

\[
\boxed{\text{M19-402 COMPLETE; A COMPACT CRITICAL SEED RIDES INSIDE A POSITIVE-RATE ACTIVE CURVATURE-RENEWAL BACKGROUND.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
