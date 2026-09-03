# DSD M5-629 — Only the synchronized zero-mean kappa level can support persistent fixed flux

Date: 2026-09-03

Status: **INTERNAL ORDER-AND-FLUX CONSEQUENCE OF THE RELABELING BRANCH / AFTER M5-628 SYNCHRONIZES THE PERSISTENT NETWORK TO ONE ZERO-MEAN KAPPA HISTORY `c_*(theta)`, EVERY DISTINCT ORDERED LEVEL BELOW `c_*` HAS STRICTLY NEGATIVE INVARIANT-MEAN KAPPA AND ITS MATERIAL VORTICITY FLUX DECAYS, WHILE EVERY DISTINCT LEVEL ABOVE `c_*` HAS POSITIVE MEAN AND ITS FLUX CANNOT REMAIN UNIFORMLY BOUNDED / HENCE NO OTHER ORDERED KAPPA LEVEL CAN CARRY A PERSISTENT BOUNDED NONDEGENERATE FIXED-FLUX LINEAGE / THE GLOBAL NEGATIVE KAPPA/RAYLEIGH BUDGET IS THEREFORE FORCED INTO TRANSIENT OR TURNOVER MATERIAL POPULATIONS OUTSIDE THE UNIQUE PERSISTENT ACTIVE LEVEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Persistent active level

On the M5-627 relabeling branch, M5-628 gives a synchronized persistent fixed-flux history

\[
\boxed{c_*(\theta)}
\]

such that every persistent active material lineage satisfies

\[
\boxed{\kappa=c_*(\theta)}
\]

and

\[
\boxed{\langle c_*\rangle=0.}
\]

The scalar relabeling law is

\[
c'=f(c,\theta).
\]

---

## 2. Ordered lower level

Let another material level history `c_-` satisfy at one time

\[
c_-<c_*.
\]

Uniqueness of the scalar ODE preserves the strict order while both histories remain in the same connected relabeling chart:

\[
\boxed{c_-(\theta)<c_*(\theta).}
\]

Define

\[
d_-(\theta):=c_*(\theta)-c_-(\theta)>0.
\]

On an invariant ergodic component, if the two histories remain genuinely distinct on a positive-measure recurrent set, then

\[
\boxed{\langle d_-\rangle>0.}
\]

Therefore

\[
\langle c_-\rangle
=\langle c_*\rangle-\langle d_-\rangle
=-\langle d_-\rangle<0.
\]

Thus

\[
\boxed{\langle c_-\rangle<0.}
\]

---

## 3. Flux consequence on the lower level

A material vortex-tube flux on this level obeys

\[
D_B\log|\phi_-|=c_-(\theta).
\]

Hence

\[
\frac1T
\log\frac{|\phi_-(\theta+T)|}{|\phi_-(\theta)|}
\to
\langle c_-\rangle<0
\]

along the ergodic/Cesaro regime.

Therefore its flux decays exponentially on average in similarity time:

\[
\boxed{
|\phi_-|\text{ cannot remain bounded below by a fixed positive threshold forever.}
}
\]

Thus a lower level cannot define a persistent fixed-flux lineage.

It must eventually leave the retained flux class through viscous loss/turnover or leave the common relabeling branch.

---

## 4. Ordered upper level

Similarly let

\[
c_+>c_*.
\]

Order preservation gives

\[
d_+:=c_+-c_*>0.
\]

If the level remains genuinely distinct recurrently,

\[
\langle d_+\rangle>0.
\]

Thus

\[
\boxed{
\langle c_+\rangle
=\langle d_+\rangle>0.
}
\]

Its material flux satisfies

\[
D_B\log|\phi_+|=c_+,
\]

so it grows exponentially on average.

A retained coherent fixed-flux population also has an upper normalized flux cap from the compact amplitude/geometry corridor.

Therefore

\[
\boxed{
c_+\text{ cannot support a bounded persistent fixed-flux label either.}
}
\]

It must undergo turnover/repartition or exit the retained label class.

---

## 5. Uniqueness of the persistent fixed-flux level

Combining the lower and upper cases:

\[
\boxed{
\text{within one connected relabeling branch, only }c_*(\theta)
\text{ can support persistent bounded nondegenerate fixed flux.}
}
\]

Any genuinely distinct ordered level has nonzero mean `kappa` and therefore secular flux drift.

This is stronger than M5-628 synchronization: not only must persistent labels synchronize, but every other ordered level is automatically transient with respect to the fixed-flux genealogy.

---

## 6. Consequence for the global Rayleigh budget

Every nonzero CE-H state satisfies

\[
\boxed{
\int\kappa|W|^2dy=-P<0.
}
\]

The persistent active level has zero invariant mean `c_*`.

Since no distinct lower/upper level can itself remain a persistent fixed-flux population, the negative enstrophy-weighted budget must be borne by

\[
\boxed{
\text{transient / viscously turning-over material populations outside the persistent level.}
}
\]

Thus the former measure-attribution problem is sharpened to

\[
\boxed{
\text{persistent zero-mean active network}
+\text{continually nonpersistent negative-budget reservoir}.
}
\]

---

## 7. Relation to M5-605--606

M5-605 extracted coherent negative-`kappa` sink packets whenever a fixed residual negative budget remains in the finite core.

M5-606 showed that repeated such packets lead to

\[
\text{persistent network absorption}
\lor
\text{positive-density viscous-flux turnover}.
\]

The present note removes the first alternative for any sink population whose `kappa` level remains genuinely below the synchronized persistent level.

Such a lower-level packet cannot become an additional persistent fixed-flux lineage because its mean flux multiplier is negative.

Therefore on the relabeling survivor,

\[
\boxed{
\text{recurrent negative-budget sink population}
\Longrightarrow
\text{positive-density viscous-flux turnover}.
}
\]

This is a genuine strengthening of M5-606 on the relabeled branch.

---

## 8. Material-family segregation

Because scalar level trajectories cannot cross,

\[
c_-<c_*
\]

remains ordered as long as the relabeling description holds.

Thus a material line from a lower negative-budget level cannot silently become a line on the persistent active level.

An apparent transfer of active identity between them must be one of:

1. viscous loss/replacement of the fixed-flux label;
2. passage through a critical/merged level-set region where the local relabeling chart fails;
3. departure into the forced `nabla D_B kappa` branch;
4. departure from CE-H itself, already handled by the earlier branch split.

This makes active/background exchange explicitly typed.

---

## 9. Two-sided-time audit

The ancient similarity trajectory is two-sided in `theta` on the limiting hull.

A lower-level line with negative forward mean flux exponent has positive backward exponent.

This fact alone is **not** called a contradiction: the material label may cease to be a coherent finite-core fixed-flux population backward in time, and its cross-section may change dramatically.

The valid conclusion remains turnover/nonpersistence, not backward blowup of one arbitrarily chosen infinitesimal label.

---

## 10. Updated relabeling frontier

The relabeling survivor now has the schematic form

\[
\boxed{
\begin{array}{c}
\text{one synchronized material level }c_*(\theta),\ \langle c_*\rangle=0,\\
\text{carrying all persistent fixed-flux active lineages},\\
+\\
\text{strictly ordered nonpersistent levels carrying the negative Rayleigh budget},\\
\text{with positive-density viscous turnover.}
\end{array}
}
\]

The arbitrary multi-level persistent oscillator picture is eliminated.

---

## 11. Highest-value next target

The next target is now the turnover rate itself.

Because the negative Rayleigh budget has a fixed invariant mean and no lower level can retain fixed flux indefinitely, one should quantify whether the fixed negative budget forces a **uniform positive replacement rate** rather than merely qualitative turnover.

If such a lower bound is obtained, it can be compared with the finite-memory storage cocycle and the strict M5-621 curvature lifetime to test whether the synchronized active level can absorb the required replacements.

---

## 12. Firewall

The strict inequalities for mean `c_-` and `c_+` require genuine recurrent separation from `c_*` on positive invariant measure.

A level whose gap collapses to zero in invariant measure belongs to the synchronized/merging limit and must not be counted as a distinct ordered level.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
