# DSD M5-628 — Relabeling order preservation synchronizes persistent-flux kappa levels

Date: 2026-09-03

Status: **INTERNAL RELABELING-RIGIDITY STEP / ON THE M5-627 RELABELING BRANCH, EVERY MATERIAL KAPPA LEVEL OBEYS THE SAME SCALAR ODE `dc/dtheta=f(c,theta)` AND ORDER OF DISTINCT LEVEL VALUES IS PRESERVED / EVERY PERSISTENT FIXED-FLUX MATERIAL LINEAGE HAS ZERO LONG-TIME MEAN KAPPA BY M5-603 / THEREFORE TWO ORDERED PERSISTENT LINEAGES CANNOT HAVE DISTINCT KAPPA HISTORIES ON AN ERGODIC RECURRENT COMPONENT: THEIR NONNEGATIVE LEVEL DIFFERENCE HAS ZERO MEAN AND MUST VANISH ALMOST EVERYWHERE / THE ENTIRE FINITE PERSISTENT ACTIVE NETWORK IS FORCED ONTO ONE COMMON MATERIAL KAPPA-LEVEL HISTORY, LEAVING THE NEGATIVE GLOBAL KAPPA BUDGET ON OTHER LEVELS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Relabeling branch

M5-627 isolates the branch on a connected regular quotient region where

\[
\boxed{D_B\kappa=f(\kappa,\theta).}
\]

Hence a material vortex line with instantaneous level value

\[
c(\theta):=\kappa(Y(\theta),\theta)
\]

obeys

\[
\boxed{c'=f(c,\theta).}
\]

The same scalar law applies to every material line in the relabeled level-surface family.

---

## 2. Order preservation

Because the extracted CE-H fields are smooth on compact time intervals, the local relabeling function is locally Lipschitz in `c` on the retained compact range.

Let two level trajectories solve

\[
c_a'=f(c_a,\theta),
\qquad
c_b'=f(c_b,\theta).
\]

If at one time

\[
c_a<c_b,
\]

uniqueness for the scalar ODE prevents them from crossing.

Thus their order is preserved:

\[
\boxed{
c_a(\theta)\le c_b(\theta)
\quad\text{for all common times}.}
\]

Equality at one time implies equality thereafter on the connected local relabeling interval.

---

## 3. Persistent-flux zero-mean law

For a persistent fixed-flux material lineage, M5-603 gives

\[
\frac{d}{d\theta}\log|\Phi|
=\bar\kappa_\Phi.
\]

On an infinitesimal line/tube label in CE-H, `kappa` is constant along the vortex line and

\[
\bar\kappa_\Phi=\kappa=c.
\]

Bounded nondegenerate recurrent flux therefore yields

\[
\boxed{
\langle c\rangle=0.
}
\]

For a sufficiently thin coherent finite tube whose lines belong to one relabeled level, the same law holds exactly with the common level value.

---

## 4. Two persistent level histories

Take two persistent fixed-flux lineages `a,b` on one invariant ergodic CE-H component.

Choose their initial ordering so that

\[
c_a\le c_b.
\]

Order preservation gives

\[
\boxed{d:=c_b-c_a\ge0.}
\]

Both flux cocycles give

\[
\langle c_a\rangle=0,
\qquad
\langle c_b\rangle=0.
\]

Hence

\[
\boxed{
\langle d\rangle
=\langle c_b-c_a\rangle
=0.
}
\]

Since `d` is nonnegative,

\[
\boxed{d=0\quad\text{in invariant measure}.}
\]

Thus

\[
\boxed{
c_a=c_b\quad\text{almost everywhere along the recurrent component}.}
\]

Continuity upgrades equality on recurrent support intervals where both labels remain defined.

---

## 5. Synchronization of a finite persistent network

The finite-memory branch contains only finitely many persistent fixed-flux labels.

Apply the previous argument pairwise.

Every pair of persistent labels with bounded nondegenerate recurrent flux must share the same `kappa` history:

\[
\boxed{
\kappa_1(\theta)
=\kappa_2(\theta)
=\cdots
=\kappa_N(\theta)
=:c_*(\theta)
}
\]

on the recurrent support, modulo explicit viscous turnover events at which a label leaves the fixed-flux class.

Moreover

\[
\boxed{\langle c_*\rangle=0.}
\]

---

## 6. Persistent dual pair consequence

M5-490 and the later component-coupling audit retain noncollinear persistent/recurring dual-source geometry on the hard branch.

On the relabeling survivor, any two such persistent fixed-flux lineages therefore satisfy

\[
\boxed{
\kappa_a=\kappa_b=c_*(\theta).
}
\]

Thus the two noncollinear source lines lie, at each regular time, in the same instantaneous level set

\[
\boxed{\{\kappa=c_*(\theta)\}.}
\]

This does not imply that they intersect or have equal vorticity direction; it only synchronizes the scalar viscous multiplier.

---

## 7. Material level-surface interpretation

M5-627 shows that a connected `kappa` level surface is transported into another level surface under the relabeling law.

Therefore the synchronized active network is carried by a common material level-surface history

\[
\boxed{
\Sigma_{c_*(\theta)}
:=\{\kappa=c_*(\theta)\}.
}
\]

The vorticity is tangent to this surface because

\[
W\cdot\nabla\kappa=0.
\]

Hence the persistent active flux network becomes a finite family of material vortex lines/tubes embedded in one common moving `kappa` surface family.

---

## 8. Separation from the global negative budget

Every nonzero CE-H state satisfies

\[
\int\kappa|W|^2dy=-P<0.
\]

But the synchronized persistent active network has

\[
\langle c_*\rangle=0.
\]

Therefore the strict negative enstrophy-weighted `kappa` budget cannot be carried solely by a material network whose level value is `c_*` with zero invariant mean.

It must be supplied by other `kappa` levels and/or by explicit turnover labels leaving the persistent class.

Thus the measure-segregation issue from M5-602 is sharpened to a **level-set segregation**:

\[
\boxed{
\text{persistent active level }c_*(\theta)
\quad\text{versus}\quad
\text{negative-budget level population}.
}
\]

---

## 9. Coarea Jacobian identity

On a regular relabeled level surface with unit normal

\[
n=\nabla\kappa/|\nabla\kappa|,
\]

let `dA` be its material area element.

The material surface-area law is

\[
D_B\log dA
=1-n\cdot\Sigma n.
\]

From M5-627,

\[
D_B\log|\nabla\kappa|
=f_\kappa-n\cdot\Sigma n-\frac12.
\]

Subtracting gives the exact coarea-Jacobian law

\[
\boxed{
D_B\log
\frac{dA}{|\nabla\kappa|}
=\frac32-f_\kappa.
}
\]

This is consistent with material volume expansion `div B=3/2` together with scalar level relabeling.

---

## 10. Uniform flux scaling on one level surface

All vortex lines in one connected level surface have the same instantaneous value `kappa=c(theta)`.

For every infinitesimal material vortex tube based on that surface,

\[
D_B\log|\phi|=c(\theta).
\]

Hence for two material vortex tubes `a,b` on the same relabeled level surface,

\[
\boxed{
D_B\log\frac{|\phi_a|}{|\phi_b|}=0.
}
\]

Their flux ratio is exactly material-invariant while they remain on the same level-surface branch.

Thus the relabeling process rescales all vortex-line fluxes on a common level surface by one common scalar factor.

---

## 11. What has been closed

The relabeling branch no longer allows each persistent lineage to choose an independent sign-changing `kappa` history.

All persistent zero-mean fixed-flux lineages must synchronize to one common history `c_*(theta)`.

Therefore arbitrary independent flux oscillators are removed from this branch.

---

## 12. What remains

It is still possible in principle that

1. the active persistent network lies on the synchronized zero-mean level `c_*`;
2. other level surfaces carry enough negative enstrophy-weighted `kappa` to satisfy the global Rayleigh identity;
3. viscous turnover transfers labels between these populations.

This is now the precise surviving relabeling scenario.

---

## 13. Highest-value next target

The next calculation should study transfer between the synchronized active level surface and the negative-budget levels.

Because the scalar relabeling flow preserves ordering, a material level cannot cross another level. Therefore active/negative population exchange cannot occur by silent crossing of level values; it must occur through loss of the fixed-flux label, critical points/mergers of the level foliation, or departure from the relabeling branch.

This is the next topological/turnover obstruction.

---

## 14. Firewall

Synchronization applies to lineages governed by the **same local relabeling law on the same connected quotient branch** and carrying bounded nondegenerate recurrent flux.

Disconnected level-set components may require separate local relabeling charts before pairwise comparison.

No global connectedness of all `kappa` level surfaces is assumed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
