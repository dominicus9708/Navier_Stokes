# DSD M17-126 — Bounded similarity velocity upgrades ancestor radius to same-material spatial localization

Date: 2026-09-05
Canonical ID: **M17-126**

Status: **EXACT CONDITIONAL MATERIAL-LOCATION BRIDGE / THE M5 IDENTITY `R_{j,k}^{phys}=r_{j-k}` IS ONLY A SCALE CORRESPONDENCE. HOWEVER, IF THE SIMILARITY VELOCITY IS UNIFORMLY BOUNDED ON THE RELEVANT INTER-STAGE INTERVAL, A MATERIAL CARRIER OBSERVED IN A REMOTE `O(K_k)` SIMILARITY ANNULUS AT STAGE `j` CAN BE TRACKED BACK TO A COMPARABLE PHYSICAL ANNULUS OF SCALE `r_{j-k}` AT STAGE `j-k`. THE DISPLACEMENT IS AT MOST `2 M_U r_{j-k}`. CHOOSING THE REMOTE TAIL ANNULUS OUTSIDE THIS BOUNDED DISPLACEMENT GIVES A SAME-MATERIAL SPATIAL GENEALOGY. THIS DOES NOT YET GIVE AMPLITUDE RETENTION OR RIBBON-TYPE RETENTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity and physical trajectories

Write

\[
x=r(\theta)y,
\qquad
r(\theta)=e^{-\theta/2},
\qquad
u=1,
\]

and

\[
u(x,t)=r(\theta)^{-1}U(y,\theta).
\]

Since

\[
\frac{dt}{d\theta}=e^{-\theta}=r(\theta)^2,
\]

a physical material trajectory satisfies

\[
\boxed{
\frac{dx}{d\theta}
=u\frac{dt}{d\theta}
=r(\theta)U(y(\theta),\theta).
}
\]

This is equivalent to the similarity material equation `y'=B=U+y/2`.

---

## 2. Inter-stage scale relation

Let

\[
\theta_j-\theta_{j-k}=2\log K_k,
\]

so

\[
\boxed{
r_{j-k}=K_kr_j.}
\]

Assume on the tracked material trajectory and the whole inter-stage interval

\[
\boxed{|U|\le M_U.}
\]

Then

\[
\begin{aligned}
|x_j-x_{j-k}|
&\le
M_U\int_{\theta_{j-k}}^{\theta_j}r(\theta)d\theta\\
&=2M_Ur_{j-k}\left(1-e^{-(\theta_j-\theta_{j-k})/2}\right)\\
&=2M_Ur_{j-k}(1-K_k^{-1}).
\end{aligned}
\]

Hence

\[
\boxed{
|x_j-x_{j-k}|
\le2M_Ur_{j-k}.
}
\]

---

## 3. Remote annulus maps to ancestor-scale region

Suppose at stage `j`

\[
AK_k\le|y_j|\le BK_k
\]

for fixed `0<A<B`. Since `x_j=r_jy_j`,

\[
Ar_{j-k}\le|x_j|\le Br_{j-k}.
\]

Using the displacement estimate,

\[
\boxed{
(A-2M_U)r_{j-k}
\le
|x_{j-k}|
\le
(B+2M_U)r_{j-k}.
}
\]

If

\[
\boxed{A>2M_U,}
\]

then the lower bound remains positive and the same material carrier lies in a physical annulus comparable to the ancestor scale `r_{j-k}`.

---

## 4. Why the tail base may be moved outward

The M5 obstruction concerns the remote spatial tail. Removing finitely many inner dyadic annuli does not affect divergence of

\[
\sum_k(R_ke_k)^{3/2}.
\]

Therefore, on a branch with a fixed similarity-velocity bound `M_U`, the tail base radius may be chosen so that

\[
A>2M_U.
\]

This makes the same-material lower radial localization available on the retained remote tail.

---

## 5. Rank and vorticity labels remain trackable

M17-104 and M17-105 give homogeneous material laws for `J_xi` and `rho`.
Therefore if the stage-`j` carrier satisfies

\[
J_\xi\ne0,
\qquad
\rho>0,
\]

then on every finite regular backward interval to stage `j-k`,

\[
\boxed{
J_\xi\ne0,
\qquad
\rho>0.
}
\]

Thus the same spatially localized carrier remains a nonzero-vorticity Rank-2 carrier while tracked backward, although it need not remain in the critical-ribbon subtype.

On the pure-kernel material stratum, the zero parallel component remains zero as well, so the carrier does not have to cross Rank-1 merely to be tracked backward.

---

## 6. What is now proved and what is not

The previous M5 ancestor-radius identity established

\[
\boxed{
\text{remote shell radius at stage }j
=
\text{distinguished physical scale at stage }j-k.
}
\]

M17-126 adds, conditionally on bounded similarity velocity,

\[
\boxed{
\text{same remote material carrier at stage }j
\Longrightarrow
\text{same carrier lies at comparable ancestor physical radius at stage }j-k.
}
\]

But this does **not** establish

\[
\rho(\theta_{j-k})\asymp\rho(\theta_j),
\]

nor comparable vorticity/enstrophy mass, nor persistence of the critical-ribbon equations over the whole interval.

The remaining genealogy gap is now primarily an amplitude/measure-retention problem rather than a spatial-location problem.

---

## 7. DSD audit

### Audit A — subtracting first-hitting remaining-time upper bounds

Not used. The spatial estimate comes directly from integrating the material trajectory.

### Audit B — bounded U assumed without scope

The result is conditional on a uniform `M_U` over the tracked inter-stage region/time. It may be supplied by the retained compact ancient-profile branch, but must not be silently extended to an unbounded-velocity branch.

### Audit C — spatial localization implies amplitude retention

Rejected. The vorticity amplitude has its own material multiplier and may change strongly over `O(log K_k)` similarity time.

### Audit D — ribbon type persists backward

Rejected. Rank-2/nonzero-vorticity labels persist, but the critical equation `g identically 0` need not.

### Audit E — proof status

The material spatial genealogy is sharpened; the amplitude genealogy remains open.

---

## 8. Updated genealogy frontier

On the bounded-similarity-velocity Rank-2 branch,

\[
\boxed{
\text{remote critical carrier}
\Longrightarrow
\text{same Rank-2 carrier at comparable ancestor physical radius}
}
\]

with no current lower bound on its ancestor amplitude.

The next target is therefore the exact inter-stage amplitude ledger

\[
\boxed{
\log\frac{\rho_j}{\rho_{j-k}}
=
\int_{\theta_{j-k}}^{\theta_j}
(\sigma+\kappa-1)d\theta,
}
\]

and whether flux-captured critical mass can force this integral to remain bounded on a sufficiently large subset of carriers.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
