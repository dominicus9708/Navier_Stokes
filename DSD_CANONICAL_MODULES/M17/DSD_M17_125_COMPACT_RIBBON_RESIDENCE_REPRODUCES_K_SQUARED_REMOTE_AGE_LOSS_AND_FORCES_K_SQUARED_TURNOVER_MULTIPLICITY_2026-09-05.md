# DSD M17-125 — Compact ribbon residence reproduces the K^2 remote-age loss and forces K^2 turnover multiplicity

Date: 2026-09-05
Canonical ID: **M17-125**

Status: **EXACT SCALE/RESIDENCE AUDIT / M17-117 GIVES A UNIFORM FINITE SIMILARITY-TIME RESIDENCE FOR ONE COMPACT NONDEGENERATE MATERIAL RIBBON LOOP. IN PHYSICAL VARIABLES THIS IS ONLY `O(r_j^2)` TIME AT FIRST-HITTING STAGE `j`. AN AGE-`k` SHELL LIES AT PHYSICAL RADIUS `rho_{j,k}=r_j K_k`, WHOSE PARABOLIC TIME IS `r_j^2 K_k^2`. THUS ONE COMPACT MATERIAL CARRIER COVERS AT MOST AN `O(K_k^-2)` FRACTION OF THE ANCESTOR-SCALE DWELL. TO MAINTAIN EULERIAN RIBBON ACTIVITY FOR A FIXED FRACTION OF `rho_{j,k}^2` USING SUCH CARRIERS REQUIRES AT LEAST ORDER `K_k^2` SEQUENTIAL FRESH-CARRIER TURNOVERS. THIS IDENTIFIES THE PRECISE MULTIPLICITY MISSING FROM THE M5 RETURN-DENSITY GATE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity-to-physical time

Use the retained blow-up normalization

\[
r(\theta)=e^{-\theta/2},
\qquad
T-t=e^{-\theta}=r(\theta)^2.
\]

At first-hitting stage `j`, write

\[
r_j=r(\theta_j).
\]

If one material ribbon remains in the compact ribbon class from `theta_j` to `theta_j+Delta theta`, its physical residence time is

\[
\begin{aligned}
\Delta t
&=(T-t_j)-(T-t(\theta_j+\Delta\theta))\\
&=r_j^2\left(1-e^{-\Delta\theta}\right).
\end{aligned}
\]

---

## 2. M17-117 residence bound

M17-117 gives a uniform compact-ribbon bound

\[
0\le\Delta\theta\le\tau_*<\infty.
\]

Hence

\[
\boxed{
\Delta t_{carrier}
\le
c_*r_j^2,
\qquad
c_*:=1-e^{-\tau_*}<1.
}
\]

Thus no one compact material ribbon carrier can remain in the class for more than a current-scale parabolic time.

---

## 3. Remote age-k physical radius

The M5 ancestor-radius identity gives

\[
\boxed{
\rho_{j,k}
=R_{j,k}^{phys}
=r_jK_k
=r_{j-k},
}
\]

where

\[
K_k=q^{k/2}
\]

for the first-hitting amplitude ratio `q>1`.

The parabolic time associated with this physical radius is

\[
\boxed{
\rho_{j,k}^2
=r_j^2K_k^2.
}
\]

---

## 4. Exact remote-age residence fraction

Combining Sections 2 and 3,

\[
\boxed{
\frac{\Delta t_{carrier}}{\rho_{j,k}^2}
\le
\frac{c_*}{K_k^2}.
}
\]

Therefore the same `K_k^{-2}` loss found in the M5 weighted-return audit reappears from the independent M17 material-ribbon residence law.

This is not merely a weak estimate caused by using the current remaining time. It is structurally consistent with the fact that a compact same-material ribbon is a current-scale carrier.

---

## 5. Turnover multiplicity needed for ancestor-scale dwell

Suppose an Eulerian ribbon structure at physical radius `rho_{j,k}` is to remain active for at least

\[
\Delta t_{Eulerian}
\ge c_0\rho_{j,k}^2
\]

with fixed `c_0>0`, while every individual material carrier remains in the compact ribbon class for at most `c_* r_j^2`.

Even with perfect gap-free replacement, the number of sequential material carriers must satisfy

\[
N_{turn}(j,k)c_*r_j^2
\ge
c_0r_j^2K_k^2.
\]

Hence

\[
\boxed{
N_{turn}(j,k)
\ge
\frac{c_0}{c_*}K_k^2.
}
\]

Thus ancestor-scale parabolic dwell requires order-`K_k^2` fresh-carrier turnover multiplicity.

---

## 6. Relation to M5 weighted return density

M5 defines

\[
\mathfrak R_k
=\frac1{\rho_k}
\sum_\ell\tau_{k,\ell}.
\]

One compact current-scale carrier contributes at most

\[
\frac{\Delta t_{carrier}}{\rho_{j,k}}
\lesssim
\frac{r_j^2}{r_jK_k}
=
\frac{r_j}{K_k}
=
\frac{\rho_{j,k}}{K_k^2}.
\]

Therefore a lower return-density bound cannot be extracted merely from the existence of one recurrent compact carrier per first-hitting stage.

The missing quantity is precisely turnover multiplicity/duration at the same physical ancestor scale.

---

## 7. Flux-captured cost per turnover

On the nondegenerate flux-captured ribbon branch M17-122 gives

\[
J_{k,ribbon}^\omega
\asymp K_k\Phi_k.
\]

If the same order of ribbon flux must be present through each of `N_turn` sequential replacements, then the cumulative **throughput** over an ancestor-scale dwell is formally of order

\[
N_{turn}\Phi_k
\gtrsim
K_k^2\Phi_k
\asymp
K_kJ_{k,ribbon}^\omega.
\]

This is a throughput requirement, not yet a conserved-cost contradiction: the same signed geometric flux can in principle enter and leave through different carriers/boundary pieces, and no finite total-variation flux budget has yet been proved.

---

## 8. DSD interpretation

The M5 remote-age loss and the M17 fresh-carrier law describe the same structural mismatch from two viewpoints:

\[
\boxed{
\text{ancestor shell scale }\rho_{j,k}
\gg
\text{current compact carrier scale }r_j.
}
\]

The square of this scale ratio is

\[
\boxed{K_k^2.}
\]

Therefore any closure of the compact-ribbon branch must obtain one of:

1. order-`K_k^2` turnover multiplicity;
2. residence on the larger ancestor scale rather than the current compact scale;
3. a stronger amplitude-duration estimate that bypasses ordinary parabolic dwell;
4. an irrecoverable positive cost per fresh-carrier turnover.

---

## 9. DSD audit

### Audit A — one recurrent stage gives ancestor-scale dwell

Rejected. One compact carrier supplies only `O(K_k^-2)` of the ancestor parabolic time.

### Audit B — K_k^2 turnovers already contradict director-flux conservation

Rejected. Director-area flux is signed/source-free and can be transported through the boundary; no finite total-variation throughput budget has yet been derived.

### Audit C — interpreting the residence upper bound as an Eulerian lifetime upper bound

Rejected. It is an upper bound for one material carrier in the compact class. An Eulerian structure may persist by continuous replacement.

### Audit D — proof status

The missing multiplicity is quantified exactly. It is not yet forced or excluded.

---

## 10. Updated physical-return gate

On the flux-captured compact-ribbon branch,

\[
\boxed{
\text{ancestor-scale dwell}
\Longrightarrow
N_{turn}(k)\gtrsim K_k^2.
}
\]

Hence the highest-value next question is whether the boundary/margin ledgers M17-107–M17-110 impose a nonrecyclable positive cost on `K_k^2` sequential fresh-carrier turnovers, or whether such throughput can remain losslessly cyclic.

A second route is the noncompact ribbon-cover branch, where the intrinsic ribbon scale may itself grow toward the ancestor scale and the `K_k^-2` mismatch can disappear.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
