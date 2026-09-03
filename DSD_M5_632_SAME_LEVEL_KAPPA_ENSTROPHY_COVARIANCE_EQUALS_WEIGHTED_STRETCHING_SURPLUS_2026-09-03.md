# DSD M5-632 — Same-level kappa–enstrophy covariance is exactly the weighted stretching-surplus ledger

Date: 2026-09-03

Status: **INTERNAL EXACT BALANCE / FOR AN INFINITESIMAL MATERIAL CE-H VORTEX-TUBE SEGMENT, THE ENSTROPHY CONTENT SATISFIES `e' = 2(sigma+kappa-1/4)e`. ON A BOUNDED RECURRENT TUBE ENSEMBLE THIS GIVES `mean(kappa e) = -mean((sigma-1/4)e)`. HENCE THE M5-630 NEGATIVE SAME-LEVEL KAPPA–ENSTROPHY COVARIANCE IS NOT AN INDEPENDENT NEW VISCOUS ESCAPE: IT IS EXACTLY THE MATERIAL-TUBE FORM OF THE POSITIVE ENSTROPHY STRETCHING SURPLUS. SUMMED OVER SPACE IT REPRODUCES THE M5-486 INVARIANT ENSTROPHY LEDGER. THE GEOMETRIC MECHANISM SUPPORTING THAT SURPLUS REMAINS OPEN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Tube enstrophy evolution

From M5-631, for an infinitesimal material tube segment,

\[
e:=\rho^2 A_\perp\ell
\]

satisfies

\[
D_B\log e
=2\sigma+2\kappa-\frac12.
\]

Equivalently,

\[
\boxed{
D_B e
=2\left(\sigma+\kappa-\frac14\right)e.
}
\]

---

## 2. Recurrent bounded ensemble average

Suppose a material-tube observable is sampled on an invariant recurrent ensemble for which `e` is integrable and the derivative has zero invariant mean.

Then

\[
0
=\left\langle D_Be\right\rangle
=2\left\langle
\left(\sigma+\kappa-\frac14\right)e
\right\rangle.
\]

Therefore

\[
\boxed{
\langle\kappa e\rangle
=-\left\langle
\left(\sigma-\frac14\right)e
\right\rangle.
}
\]

---

## 3. Covariance branch equivalence

On the synchronized persistent level of M5-628--630,

\[
\kappa=c_*(\theta),
\qquad
\langle c_*\rangle_{flux-time}=0.
\]

If the same-level contribution has

\[
\boxed{
\langle c_* e\rangle<0,
}
\]

then necessarily

\[
\boxed{
\left\langle
\left(\sigma-\frac14\right)e
\right\rangle>0.
}
\]

Conversely a positive weighted stretching surplus produces the negative same-level viscous covariance.

Thus

\[
\boxed{
C_{same-level}^{\kappa-E}
\Longleftrightarrow
S_{same-level}^{\sigma-1/4}
}
\]

at the exact tube-balance level.

---

## 4. Relation to the M5-486 global ledger

The global CE-H identities are

\[
Q=\int \sigma|W|^2dy,
\qquad
\int\kappa|W|^2dy=-P.
\]

M5-486 gives

\[
\frac12E'+\frac14E+P=Q.
\]

Hence

\[
\boxed{
\frac12E'
=\int
\left(\sigma+\kappa-\frac14\right)|W|^2dy.
}
\]

On invariant averaging,

\[
\boxed{
\left\langle
\int
\left(\sigma+\kappa-\frac14\right)|W|^2dy
\right\rangle=0.
}
\]

This is precisely the spatially summed version of the material-tube identity above.

Therefore the M5-630 covariance branch does not create a new independent balance beyond the existing enstrophy ledger.

---

## 5. What is genuinely still open

The fact that the covariance is a recycled stretching ledger does **not** prove impossibility.

The remaining geometric problem is how a recurrent active system sustains

\[
\left\langle
\left(\sigma-\frac14\right)e
\right\rangle>0
\]

while simultaneously satisfying the CE-H constraints:

- material vortex-line direction freezing;
- scale-invariant flux recurrence;
- curvature strict decay on a fixed material label (M5-621);
- non-Beltrami defect floor (M5-618--619);
- transverse magnitude/direction derivative floors;
- `kappa` relabeling or cross-level forcing branches.

Thus the covariance label should be merged back into the **production-geometry problem**, not counted as an independent terminal branch.

---

## 6. Aspect-ratio form

M5-631 gives

\[
e=\phi^2\mathcal R_{tube},
\qquad
\mathcal R_{tube}=\ell/A_\perp,
\]

and

\[
D_B\log\mathcal R_{tube}=2\sigma-\frac12.
\]

Hence the same-level covariance can equivalently be written as a phase relation among

\[
\phi^2,
\qquad
\mathcal R_{tube},
\qquad
\sigma.
\]

The viscous multiplier controls the flux phase, while stretching controls the geometric aspect-ratio phase.

---

## 7. DSD audit correction to the frontier

M5-630 correctly exposed the covariance mechanism and prevented a false measure-identification contradiction.

M5-632 now shows that this mechanism should not be retained as a wholly independent final branch.

The corrected interpretation is

\[
\boxed{
C_{same-level}^{\kappa-E}
=\text{material representation of recurrent stretching surplus}.
}
\]

The next useful question is whether that stretching surplus can be carried by one persistent positive-volume material tube segment. M5-560 suggests it cannot, because material volume expands exactly at rate `3/2`.

---

## 8. Firewall

The zero derivative average is used only for an invariant/recurrent integrable tube ensemble. No claim is made that one arbitrarily chosen nonrecurrent material segment has zero endpoint contribution.

No sign is inferred for the stretching term without the covariance hypothesis.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]