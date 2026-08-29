# DSD M5-194O — Periodic Alpha Small-Period Exclusion and Nonsummable-Tail Audit

Date: 2026-08-29

Parent: `DSD_M5_194N_MULTI_GENERATION_DSS_RECURRENCE_AND_STAGE_DURATION_CYCLE_AUDIT_2026-08-29.md`

Status: **PARTIAL PERIODIC-BRANCH CLOSURE / ON THE SPATIAL TYPE-I TAIL CORRIDOR, A NONZERO PERIODIC SIMILARITY ALPHA-LIMIT CANNOT HAVE SUFFICIENTLY SMALL PERIOD BY THE 2026 PINEAU--VICOL DSS LIOUVILLE THEOREM / IF IT ALSO ENTERS THE CLASSICAL GLOBAL `L^3` PERIODIC PROFILE CLASS IT IS TRIVIAL FOR ANY PERIOD / THEREFORE ANY SURVIVING PERIODIC ALPHA-LIMIT MUST BE BOTH LONG-PERIOD AND GLOBALLY NON-`L^3`, WHICH FOR A `1/r` UPPER TAIL FORCES A NONSUMMABLE DYADIC CRITICAL `L^3` TAIL / THIS MERGES THE LARGE-PERIOD DSS SURVIVOR WITH THE EXISTING ESCAPING-CRITICAL-TAIL FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Periodic alpha-limit setup

Assume the dynamic checkpoint branch of M5-194N produces a nonzero periodic similarity alpha-limit

\[
V_*(Y,s+S)=V_*(Y,s),
\qquad
S>0.
\]

Its physical backward DSS factor is

\[
\boxed{\lambda=e^{S/2}>1.}
\]

Checkpoint nontriviality from M5-194L gives

\[
V_*\not\equiv0.
\]

This note audits what additional properties such a nonzero periodic limit must have.

---

## 2. Spatial Type-I tail split is prior to the DSS theorem

The repository's annular `H^2` bridge gives the exact conditional split

\[
\boxed{
|V_*(Y,s)|\le\frac{C_0}{1+|Y|}
\quad\lor\quad
H_{1,crit}^{tail}
\quad\lor\quad
H_{2,crit}^{tail}.
}
\]

Here the two failure channels are the already defined scale-critical enstrophy/palinstrophy shell escapes.

Therefore, before applying any global DSS Liouville theorem, the periodic branch has already split into

1. a spatial Type-I periodic profile;
2. a critical derivative-tail failure, which is an explicit `H_tail` branch.

The rest of this note works on branch 1.

---

## 3. 2026 small-period DSS exclusion

Pineau and Vicol (2026), *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, prove in the nonrotated DSS case that under the global Type-I bound

\[
|u(x,t)|\le\frac{C_0}{|x|+\sqrt{-t}},
\]

there exists a threshold

\[
\boxed{\lambda_{PV}(C_0)>1}
\]

such that any backward globally DSS solution with

\[
1<\lambda<\lambda_{PV}(C_0)
\]

is trivial.

The similarity-profile form of the spatial Type-I estimate is exactly

\[
|V_*(Y,s)|\le\frac{C_0}{1+|Y|}.
\]

Since the checkpoint alpha-limit is nonzero, a surviving periodic profile must therefore satisfy

\[
\boxed{
\lambda\ge\lambda_{PV}(C_0).
}
\]

Equivalently,

\[
\boxed{
S\ge S_{PV}(C_0)
:=2\log\lambda_{PV}(C_0)>0.
}
\]

Thus the periodic survivor has a strict minimum similarity-time period on the spatial Type-I corridor.

---

## 4. Generation-length consequence

If a `p`-generation recurrent branch also has the natural timing lock

\[
S=p\log q,
\]

then survival requires

\[
p\log q
\ge
S_{PV}(C_0).
\]

Hence

\[
\boxed{
p
\ge
p_{PV}(q,C_0)
:=
\left\lceil
\frac{S_{PV}(C_0)}{\log q}
\right\rceil.
}
\]

This is a genuine lower bound on the number of first-hitting generations needed by any DSS survivor in the small-period-exclusion regime.

It is conditional on the `p`-generation phase relation `S=p log q`; M5-194M/N already forbid assuming that relation without timing lock.

---

## 5. Classical `L^3` periodic-profile exclusion

Known asymptotically/discretely self-similar Liouville results exclude nonzero periodic backward similarity profiles when the profile belongs to the global critical `L^3(R^3)` class with the required smoothness.

Therefore a nonzero periodic alpha-limit cannot satisfy the uniform periodic `L^3` condition

\[
\boxed{
\sup_{s\in[0,S]}
\|V_*(s)\|_{L^3(\mathbb R^3)}<\infty.
}
\]

Thus every surviving periodic branch must evade the classical theorem through the spatial tail.

This is consistent with the repository's earlier ancient `L^3`-tail necessity result.

---

## 6. Dyadic annular `L^3` ledger under the spatial Type-I upper bound

Let

\[
A_k:=\{2^k<|Y|<2^{k+1}\},
\qquad k\ge k_0,
\]

and define

\[
\boxed{
M_k(s)
:=
\int_{A_k}|V_*(Y,s)|^3\,dY.
}
\]

The spatial Type-I pointwise upper bound gives

\[
|V_*|^3
\lesssim
2^{-3k}
\]

on `A_k`, while

\[
|A_k|\asymp2^{3k}.
\]

Hence

\[
\boxed{
M_k(s)\le C(C_0)
}
\]

uniformly in `k` and in the periodic phase `s`.

Thus each dyadic annulus carries at most order-one critical `L^3` mass.

---

## 7. A surviving periodic profile needs a nonsummable tail

Suppose, contrary to the required tail escape, that the annular masses were uniformly summable over one period:

\[
\sum_{k\ge k_0}
\sup_{s\in[0,S]}M_k(s)<\infty.
\]

Adding the finite inner-ball contribution would give

\[
\sup_{s\in[0,S]}
\|V_*(s)\|_3^3<\infty.
\]

This places the periodic profile in the classical global `L^3` Liouville class and forces

\[
V_*\equiv0,
\]

contradicting checkpoint nontriviality.

Therefore every nonzero periodic survivor must satisfy

\[
\boxed{
\sum_{k\ge k_0}
\sup_{s\in[0,S]}M_k(s)
=\infty.
}
\]

This is the **nonsummable critical-tail requirement**.

---

## 8. Quantitative sparse-tail witness

The divergence above does not imply a fixed positive lower bound on every annulus.

For example, masses of order `1/k` already produce divergence.

However it does imply the following useful formed witness.

Let `epsilon_k>0` be any summable positive sequence:

\[
\sum_k\epsilon_k<\infty.
\]

Then infinitely many `k` must satisfy

\[
\boxed{
\sup_{s\in[0,S]}M_k(s)>\epsilon_k.
}
\]

Otherwise the annular tail would eventually be dominated by a summable sequence and global `L^3` would follow.

For the concrete choice

\[
\epsilon_k=k^{-2},
\]

there are infinitely many annuli with

\[
\boxed{
\sup_{s\in[0,S]}
\int_{A_k}|V_*|^3
>k^{-2}.
}
\]

This is weaker than a fixed-cost shell but stronger than the vague statement `V notin L3`.

---

## 9. Periodicity makes the tail recurrent in similarity time

Because

\[
V_*(s+S)=V_*(s),
\]

each annular mass is periodic:

\[
M_k(s+S)=M_k(s).
\]

Therefore every tail annulus selected by the preceding witness is not a one-time excursion.

Its entire normalized time history repeats every period.

Thus the large-period DSS survivor has the structure

\[
\boxed{
\text{periodic active core}
+
\text{periodically recurrent nonsummable critical tail}.
}
\]

This is precisely the dynamic version of the repository's existing core--tail compatibility frontier.

---

## 10. Why finite-memory turnover does not by itself close this branch

The finite-memory replacement theorem bounds how many distinguishable coherent material populations can be stored simultaneously in a bounded normalized core.

The nonsummable DSS tail lives on unbounded similarity radii and may be distributed over infinitely many increasingly distant shells.

Therefore it would be invalid to infer

\[
\text{infinitely many critical tail shells}
\Longrightarrow
\text{violation of bounded-core multiflux capacity}.
\]

The correct routing is instead to the existing export/escaping-tail branch.

Any closure must show that a periodic core cannot repeatedly sustain or replenish this infinite critical tail without paying one of the already identified export, derivative, pressure, or projective costs.

---

## 11. Updated periodic branch

The nonzero periodic similarity branch now has the exhaustive conditional split

\[
\boxed{
\begin{cases}
H_{1,crit}^{tail}\lor H_{2,crit}^{tail}
&\text{if the spatial Type-I bridge fails},\\[1mm]
S<S_{PV}(C_0)
&\Rightarrow\text{trivial, branch closed},\\[1mm]
\sup_s\|V(s)\|_3<\infty
&\Rightarrow\text{trivial, branch closed},\\[1mm]
S\ge S_{PV}(C_0),\quad
\text{nonsummable critical tail}
&\text{surviving DSS frontier}.
\end{cases}
}
\]

The surviving part is therefore much narrower than an arbitrary periodic Leray orbit.

---

## 12. DSD verdict

### CLOSED / REDUCED

- all sufficiently small-period DSS profiles on the spatial Type-I branch;
- every periodic profile that has uniformly summable dyadic `L^3` tail;
- every periodic profile in the classical global `L^3` class;
- the interpretation of a surviving periodic branch as a purely local recurrent core with no formed global tail.

### SURVIVES

A nonzero periodic survivor must have

\[
\boxed{
S\ge S_{PV}(C_0)
}
\]

and a spatially unbounded, nonsummable critical `L^3` tail recurring every similarity period, unless it has already exited through `H_{1,crit}^{tail}` or `H_{2,crit}^{tail}`.

### STILL OPEN

- incompatibility of a periodic active core with the nonsummable critical tail;
- a fixed positive annular cost as opposed to a merely nonsummable sparse tail;
- the generic aperiodic alpha-limit branch;
- global regularity.

---

## 13. Next audit target

The next calculation should use the periodic Leray equation over one full period and a large-radius cutoff to derive the **annular flux balance** for the tail.

Because the time derivative integrates to zero over a period, one can ask whether the nonsummable critical `L^3` tail requires a nonzero mean flux through infinitely many large spheres.

If a fixed positive flux is forced on infinitely many shells, the branch can be charged to the existing positive-frequency export ledger.

If the flux can tend to zero while the `L^3` tail remains nonsummable, that zero-flux critical-tail topology becomes the precise remaining periodic obstruction.
