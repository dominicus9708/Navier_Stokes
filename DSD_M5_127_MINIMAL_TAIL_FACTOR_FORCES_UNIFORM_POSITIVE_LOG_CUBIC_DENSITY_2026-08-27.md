# DSD M5-127 — Minimal Tail Factor Forces Uniform Positive Log-Cubic Density

Date: 2026-08-27

Status: **CANONICAL TAIL FACTOR SHOWN TO BE A COMPACT MINIMAL LOG-TRANSLATION SYSTEM / ANY NONZERO CONTINUOUS CUBIC LOG-CELL OBSERVABLE RECURS SYNDETICALLY ON EVERY TAIL ORBIT / POSITIVE CUBIC RESIDUE UPGRADES FROM AN ERGODIC-A.E. STATEMENT TO A UNIFORM POSITIVE LOWER CESARO DENSITY ACROSS THE ENTIRE TAIL FACTOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Tail factor is minimal

The W1 state space `M` is compact and minimal under the Leray flow `S_h`.

M5-114 gives the continuous onto factor map

\[
\pi:M\to\mathcal T
\]

with

\[
\pi(S_hV)=D_h\pi(V).
\]

The dilation maps `D_h` are invertible on the tail field space, and `S_hM=M` implies `D_h\mathcal T=\mathcal T`.

A continuous factor of a minimal compact dynamical system is minimal.  Therefore

\[
\boxed{
(\mathcal T,D_h)\text{ is a compact minimal flow.}
}
\]

Equivalently, in direct log-radius translation parameter `a=h/2`, every tail orbit is dense in the same compact factor.

---

## 2. Use a continuous log-cell observable

The exact one-sphere slice

\[
\mathfrak c(T)=\int_{S^2}|\Phi_T(0,\theta)|^3d\theta
\]

is sufficient measure-theoretically, but a topological recurrence argument is cleaner with a volume observable.

Define one unit log-cell cubic mass

\[
\boxed{
\mathfrak C(T)
:=\int_{1<|Y|<e}|T(Y)|^3dY
=
\int_0^1\int_{S^2}|\Phi_T(\rho,\theta)|^3d\theta d\rho.
}
\]

Because the tail-factor topology contains local `L3` convergence on fixed punctured annuli,

\[
\boxed{
\mathfrak C:\mathcal T\to[0,\infty)
\text{ is continuous.}
}
\]

---

## 3. Nonzero residue implies a nonempty positive cell

If the W1 critical residue is positive, M5-118 gives positive invariant mean cubic density.

Therefore `mathfrak C` cannot vanish identically on `mathcal T`.

Choose a state `T_*` with

\[
\mathfrak C(T_*)=c_*>0.
\]

By continuity, the set

\[
\boxed{
\mathcal U
:=\{T:\mathfrak C(T)>c_*/2\}
}
\]

is a nonempty open subset of the compact minimal factor.

---

## 4. Minimality gives a syndetic set of positive cubic cells

For a minimal compact flow, return times to every nonempty open set are syndetic.

A direct compactness proof is as follows.

The family of backward translates

\[
\{D_{-h}\mathcal U:h\ge0\}
\]

covers `mathcal T` by minimality.  Compactness gives a finite subcover

\[
\mathcal T
=\bigcup_{j=1}^N D_{-h_j}\mathcal U.
\]

Set

\[
L:=\max_jh_j.
\]

For every tail state `T` and every starting time `s>=0`, apply the cover to `D_sT`.  There exists `h_j<=L` such that

\[
D_{s+h_j}T\in\mathcal U.
\]

Hence every interval of factor time of length `L` contains a visit satisfying

\[
\boxed{
\mathfrak C(D_hT)>c_*/2.
}
\]

The positive-cell return set is uniformly syndetic for **every** tail orbit.

---

## 5. Convert syndetic cells into a uniform lower Cesaro density

Use the direct log-translation parameter

\[
a=h/2.
\]

One factor return with `mathfrak C>c_*/2` produces one log-radius interval of length one whose cubic mass is at least `c_*/2`.

Partition a long log interval into blocks of length larger than the syndetic gap plus two cell widths.  From each block select one positive cubic cell; the selected cells may be chosen disjoint.

Therefore there exists a constant

\[
\boxed{r_*>0}
\]

depending only on the compact minimal tail factor and the chosen open positive-cell neighborhood such that for **every** `T in mathcal T`,

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int_0^L\int_{S^2}|\Phi_T(\rho,\theta)|^3d\theta d\rho
\ge r_*>0.
}
\]

The same statement holds on the backward half-line by invertibility/minimality of the log-translation factor.

---

## 6. Uniform consequence for all invariant measures

Let `nu` be any invariant probability measure on the minimal tail factor.

Integrating the previous lower-density statement, or applying the syndetic-cell estimate directly, gives

\[
\boxed{
\int_{\mathcal T}\mathfrak c(T)d\nu(T)
\ge r_*>0
}
\]

with the consistent normalization between one-slice and one-cell averages.

Hence every invariant measure on a nonzero minimal tail factor carries positive cubic residue.

The residue is no longer a feature of one specially selected ergodic measure.

---

## 7. W1 consequence

Push any W1 invariant measure through the canonical factor.  M5-118 then gives

\[
\boxed{
\mathscr R_3\ge r_*>0
}
\]

for every invariant measure supported on this nonzero minimal W1/tail component.

Moreover every individual tail state has positive lower log-Cesaro cubic density, independently of whether the factor is uniquely ergodic.

Thus the periodic and aperiodic cases are again unified:

\[
\boxed{
\text{nonzero minimal tail}
\Longrightarrow
\text{uniformly recurrent critical cubic memory}.
}
\]

---

## 8. Transfer to the diagonal prelimit

M5-126 may now be strengthened conceptually.

The diagonal growing-window sequence need not be selected from an ergodic-generic tail state to see arbitrarily deep cubic mass.

Every W1 tail state in the nonzero minimal factor obeys the uniform lower-density estimate.  Therefore for sufficiently large diagonal radii,

\[
\boxed{
\int_{R_*<|Y|<R_n}|V|^3dY
\ge c\log R_n-O(1)
}

with one positive `c` uniform on the compact factor.

After diagonal transfer, the same original-solution shrinking-annulus concentration law follows uniformly along the retained W1 survivor class.

---

## 9. DSD four-chain audit

### Formation — GREEN

A continuous volume cell observable is used; no unproved trace continuity is required.

### Axis — GREEN

Factor time and log radius differ by the fixed factor two and are not conflated.

### Static aggregation — GREEN

Disjoint positive cells are selected before summing, so no overlapping log intervals are double counted.

### Dynamics — GREEN

Minimality supplies syndetic returns independently of invariant-measure ergodicity.

### Cross-audit — GREEN

Positive residue is used only to show `mathfrak C` is nonzero somewhere; the uniform recurrence conclusion then follows topologically and is not fed back to establish minimality.

---

## 10. What this does not prove

Uniform positive cubic log density remains compatible with the rotational countermodels of M5-123 and with weak-`L3` critical scaling.

Therefore

\[
\boxed{
\text{uniform log-Cesaro positivity alone is not a contradiction.}
}
\]

Its importance is that all subsequent tail/core and prelimit estimates may now use one **uniform positive density floor** rather than an ergodic-a.e. residue.

---

## 11. Updated frontier

The main unresolved question is now fully uniform over the surviving W1 minimal class:

\[
\boxed{
\text{Can an unforced finite-energy Navier--Stokes prelimit realize a nonzero compact minimal canonical-tail factor whose cubic memory has a uniform positive log-density floor, while the associated finite-core pressure/strain residual obeys the M5-120--122 cocycle?}
}
\]

Pure geometry, net momentum flux, ordinary energy, and residual/quotient shell work have all been pruned as standalone closures.

The next useful direction is therefore either:

1. a stronger prelimit interface estimate that uses the uniform positive density floor; or
2. a relative/fiber rigidity theorem for the strong-critical quotient dynamics.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
