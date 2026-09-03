# DSD M16-022 — A recycled active tube forces axial strain heterogeneity or marker turnover

Date: 2026-09-03
Canonical ID: **M16-022**

Status: **INTERNAL RECURRENCE COUPLING / ON THE RESIDENCE-COVARIANCE BRANCH OF M16-021, A PERSISTENT FIXED-FLUX MATERIAL TUBE WITH A NONDEGENERATE ACTIVE MATERIAL MARKER HAS TWO INCOMPATIBLE NATURAL STRAIN AVERAGES: THE TUBE-RESIDENCE LEDGER FORCES THE `rho`-WEIGHTED LINE STRAIN TO HAVE MEAN `1/4`, WHILE THE MARKER AMPLITUDE LEDGER FORCES THE SAME MARKER'S STRAIN TO HAVE MEAN `1`. HENCE EITHER THE ACTIVE MARKER/TUBE ROLE TURNS OVER, OR A POSITIVE-DENSITY AXIAL STRAIN-HETEROGENEITY EVENT OCCURS ON THE SAME TUBE. THIS RECONNECTS THE COVARIANCE BRANCH TO THE P1 STRAIN-GRADIENT FAMILY WITHOUT CLAIMING A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Persistent active material tube

Consider one material vortex-tube segment `Gamma(theta)` in the CE-H branch.

Assume its material flux remains nondegenerate:

\[
0<\Phi_-\le |\Phi(\theta)|\le \Phi_+<\infty.
\]

Assume also that the tube continues to contain one persistent active material marker `Y(theta)` with

\[
0<\rho_-\le \rho(Y(\theta),\theta)\le \rho_+<\infty.
\]

If this same-marker assumption fails with positive density, that is already a marker-migration / material-sheath-turnover branch and no further argument is needed here.

---

## 2. Uniform bounds for line residence

Recall

\[
L_\rho(\theta)
=\int_{\Gamma(\theta)}\rho\,ds.
\]

The tube enstrophy is

\[
e_{\rm tube}=|\Phi|L_\rho.
\]

Since the global enstrophy satisfies

\[
E(\theta)\le Z_*,
\]

and `|Phi| >= Phi_-`,

\[
\boxed{
L_\rho(\theta)
\le
\frac{Z_*}{\Phi_-}
=:L_+.
}
\]

On the other hand, the active marker has `rho >= rho_-`. Uniform spatial `C^1` bounds on the compact hull give a fixed arclength `ell_*>0` around the marker on which

\[
\rho\ge \frac{\rho_-}{2}.
\]

Hence

\[
\boxed{
L_\rho(\theta)
\ge
\frac{\rho_-}{2}\ell_*
=:L_->0.
}
\]

Thus

\[
0<L_-\le L_\rho(\theta)\le L_+<\infty.
\]

Therefore

\[
\lim_{T\to\infty}
\frac{\log L_\rho(T)-\log L_\rho(0)}{T}=0.
\]

---

## 3. Tube-residence strain mean

M16-020 gives

\[
D_B\log L_\rho
=\kappa+2\bar\sigma_\rho-\frac12,
\]

where

\[
\bar\sigma_\rho
=
\frac{\int_\Gamma\sigma\rho\,ds}
{\int_\Gamma\rho\,ds}.
\]

The bounded flux hypothesis gives

\[
\lim_{T\to\infty}
\frac{\log|\Phi(T)|-\log|\Phi(0)|}{T}
=
\langle\kappa\rangle=0.
\]

The bounded residence hypothesis then yields

\[
0
=
\left\langle
\kappa+2\bar\sigma_\rho-\frac12
\right\rangle.
\]

Hence

\[
\boxed{
\langle\bar\sigma_\rho\rangle=\frac14.
}
\]

This is the strain mean seen by the entire `rho`-weighted vortex-line residence.

---

## 4. Persistent active-marker strain mean

At the active material marker,

\[
D_B\log\rho(Y(\theta),\theta)
=\sigma_m+\kappa-1,
\]

where

\[
\sigma_m(\theta)
:=\sigma(Y(\theta),\theta).
\]

Because the same marker amplitude remains bounded above and below,

\[
\lim_{T\to\infty}
\frac{\log\rho(Y(T),T)-\log\rho(Y(0),0)}{T}=0.
\]

Together with `⟨kappa⟩=0`, this gives

\[
\boxed{
\langle\sigma_m\rangle=1.
}
\]

Therefore

\[
\boxed{
\left\langle
\sigma_m-\bar\sigma_\rho
\right\rangle
=\frac34.
}
\]

---

## 5. Positive-density heterogeneity event

The compact CE-H hull gives

\[
|\sigma|\le S_*.
\]

Hence

\[
|\sigma_m-\bar\sigma_\rho|\le2S_*.
\]

Since its time mean is `3/4`, there exist constants

\[
c_{\rm het}>0,
\qquad
\delta_{\rm het}>0
\]

such that the event

\[
\boxed{
\sigma_m-\bar\sigma_\rho
\ge c_{\rm het}
}
\]

has asymptotic time density at least `delta_het`.

For example one may choose any fixed `c_het < 3/4`; boundedness then gives a positive lower density depending only on `S_*` and `c_het`.

---

## 6. Same-tube strain variation

At every heterogeneity event, because `bar sigma_rho` is a positive `rho ds` weighted average, there exists a point `Z` on the same tube segment with

\[
\sigma(Z)\le\bar\sigma_\rho.
\]

Therefore

\[
\boxed{
\sigma(Y)-\sigma(Z)
\ge c_{\rm het}.
}
\]

If the persistent active tube segment lies in the fixed finite core `B_{R_core}`, then

\[
|Y-Z|\le2R_{\rm core}.
\]

By the mean-value theorem and global smoothness,

\[
\boxed{
\sup_{B_{R_{\rm core}}}|\nabla\sigma|
\ge
\frac{c_{\rm het}}{2R_{\rm core}}
=:g_\sigma>0.
}
\]

Uniform time/space continuity thickens this to a positive-density coherent `P1` strain-gradient event family.

Thus the residence-covariance branch is not geometrically silent.

---

## 7. Correct dichotomy

A persistent fixed-flux active tube must therefore satisfy

\[
\boxed{
\text{same-marker recycling}
\Rightarrow
\text{positive-density axial strain heterogeneity}.
}
\]

If the same active marker does not persist, then

\[
\boxed{
\text{marker migration / sheath turnover}
}
\]

occurs instead.

Hence

\[
\boxed{
B_{\rm res}^{cov}
\Longrightarrow
P_{1}^{\rm axial\ het}
\ \lor\ 
T_{\rm marker/sheath}.
}
\]

This is stronger than the generic P1 charge of M16-014 because the gradient is now tied to two different strain samplings on the **same material vortex tube**.

---

## 8. DSD firewall

This result is still not a contradiction.

M16-015 already showed that a positive strain-gradient charge can be an unsigned localization of palinstrophy-scale activity.

The gain here is genealogy coupling: the gradient is no longer an arbitrary Eulerian packet. It is forced by the same recurrent material tube that carries the neutral-flux / residence-covariance mechanism.

The next step is to use the CE-H eigenvalue and constitutive equations to determine whether this same-tube axial strain heterogeneity can remain recurrent without forcing one of the already known pressure/critical-sheet/source-turnover mechanisms.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
