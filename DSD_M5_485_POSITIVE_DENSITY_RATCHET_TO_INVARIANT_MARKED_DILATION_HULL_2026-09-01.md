# DSD M5-485 — Positive-density ratchet action lifts to an invariant marked dilation hull

Date: 2026-09-01

Status: **RECURRENCE EXTRACTION / AFTER THE M5-484 INHERITANCE CORRECTION, THE SINGLE M5-474 RATCHET EVENT CANNOT BE USED AS AN INTERIOR MARK OF THE SECOND BLOW-DOWN; HOWEVER THE ORIGINAL M5-471--473 POSITIVE-GENERATION-DENSITY RATCHET STATEMENT CAN BE RETAINED BY A JOINT SHIFT-COMPACT EXTRACTION / ON THE BOUNDED NO-DEFECT CORRIDOR THIS PRODUCES A COMPACT TWO-SIDED MARKED LOG-SCALE HULL AND AN INVARIANT PROBABILITY MEASURE WITH STRICTLY POSITIVE MEAN RATCHET MARK / CONSEQUENTLY ANY BOUNDED CONTINUOUS OBSERVABLE WHOSE ONE-STEP DRIFT DOMINATES THE RATCHET MARK WOULD CONTRADICT INVARIANCE / THIS REDUCES THE NEW HARD CORE TO A MARKED-HULL COCYCLE/RIGIDITY PROBLEM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why a new extraction is needed

M5-484 proved

\[
\text{single M5-474 ratchet event}
\to s=0
\]

under the second backward blow-down.

Therefore a recurrent interior mark must come from the stronger original statement of M5-471--473:

\[
\boxed{
\text{order-one ratchet action occurs on a positive density of first-hitting generations}.
}
\]

The correct object is not one marked stage but the entire generation sequence.

---

## 2. Generation-level ratchet indicator

On the bounded/no-reformation/no-strong-escalation corridor, let

\[
\mathcal A_j
:=
\int_{J_j}|\tau_j|\,d\theta
+
\int_{J_j}
\frac{|(I-\xi_j\otimes\xi_j)\Delta\Omega_j|}{|\Omega_j|}
\,d\theta,
\]

where `J_j` is the normalized retained material interval of generation `j`.

Fix the M5-471 threshold `a_0>0` and define

\[
\boxed{
a_j:=\mathbf 1_{\{\mathcal A_j\ge a_0\}}.}
\]

The positive-density ratchet conclusion means that, after discarding finitely many generations,

\[
\boxed{
\liminf_{N\to\infty}
\frac1N\sum_{j=1}^{N}a_j
\ge\delta_0>0
}
\]

on the retained corridor.

If the repository's earlier density statement is used only as positive upper/Banach density, the construction below is applied to the corresponding long high-density blocks; the invariant-measure conclusion remains the same with positive mean on a selected hull component.

---

## 3. Compact stage data

For each generation retain the complete normalized stage datum

\[
Z_j
=
(\mathcal V_j,\mathcal P_j,\mathcal O_j,\lambda_j,a_j),
\]

where

- `mathcal V_j, mathcal P_j` are the normalized space-time velocity/pressure cells on a fixed family of compact cylinders;
- `mathcal O_j` denotes the old-carrier/flux/genealogy marks already retained by the bounded lane;
- `lambda_j` is the consecutive record-scale ratio;
- `a_j` is the ratchet indicator.

On the M5-482--484 compact/no-defect branch,

\[
1<\lambda_-\le\lambda_j\le\lambda_+<\infty,
\]

and the PDE cells are precompact in the local smooth topology on `s<0`.

The mark package is encoded only through quantities known to be stable under the corresponding local convergence. In particular, a ratchet event is retained only with an active-vorticity lower threshold, so the direction field remains defined and the Lagrangian flow maps converge on the marked interval.

---

## 4. Two-sided shift hull

Form the generation sequence

\[
\mathbf Z
=(\ldots,Z_{-1},Z_0,Z_1,\ldots)
\]

through the usual diagonal extension of finite-offset blocks.

Let `sigma` denote the left shift,

\[
(\sigma\mathbf Z)_n=Z_{n+1}.
\]

Take the closure of the shift orbit in the product of local compact topologies:

\[
\boxed{
\mathfrak H
:=
\overline{\{\sigma^k\mathbf Z:k\in\mathbb Z\}}.
}
\]

Then `mathfrak H` is compact and `sigma` acts continuously on it.

Every point of `mathfrak H` carries a complete two-sided parabolic dilation genealogy

\[
\boxed{
\mathcal U_{n+1}
=
\mathscr D_{\lambda_n}\mathcal U_n,
\qquad n\in\mathbb Z,
}
\]

with the M5-484 inherited Type-I/carrier/truncated-palinstrophy package.

---

## 5. Empirical measures and invariant probability

For the forward generation orbit define the empirical measures

\[
\mu_N
:=
\frac1N\sum_{j=0}^{N-1}
\delta_{\sigma^j\mathbf Z}.
\]

Compactness of `mathfrak H` gives a weak-* convergent subsequence

\[
\mu_{N_k}\rightharpoonup\mu.
\]

The standard telescoping identity gives for every continuous `F` on `mathfrak H`,

\[
\int F\circ\sigma\,d\mu_N-
\int F\,d\mu_N
=
\frac{F(\sigma^N\mathbf Z)-F(\mathbf Z)}{N}
\to0.
\]

Therefore

\[
\boxed{
\sigma_*\mu=\mu.
}
\]

Thus the marked dilation hull supports a shift-invariant probability measure.

---

## 6. Positive mean ratchet mark survives

Let

\[
a(\mathbf Y):=a_0(\mathbf Y)\in\{0,1\}
\]

denote the central ratchet indicator of a hull point.

Because `a_j` was encoded as part of the compact marked state and the active event inequality is closed on the no-defect lane,

\[
\int a\,d\mu
=
\lim_{k\to\infty}
\frac1{N_k}
\sum_{j=0}^{N_k-1}a_j.
\]

Hence

\[
\boxed{
\int_{\mathfrak H}a\,d\mu
\ge\delta_0>0.
}
\]

This is the rigorous replacement for the invalid shortcut

\[
\text{one ratchet event}
\Rightarrow
\text{ratchet mark survives every blow-down}.
\]

The correct statement is

\[
\boxed{
\text{positive-density ratchet sequence}
\Rightarrow
\text{invariant marked hull with positive mean ratchet frequency}.
}
\]

---

## 7. Ergodic component with recurrent ratchet action

By ergodic decomposition, there exists an ergodic invariant component `nu` of `mu` such that

\[
\boxed{
\int a\,d\nu>0.
}
\]

For `nu`-almost every marked genealogy, Birkhoff's theorem gives

\[
\boxed{
\lim_{N\to\infty}
\frac1N\sum_{j=0}^{N-1}a(\sigma^j\mathbf Y)
=
\int a\,d\nu
>0.
}
\]

Thus there exist individual complete dilation genealogies carrying recurrent order-one material-axis ratchet action at positive log-scale frequency.

This conclusion is valid for both

1. periodic/DSS hull components;
2. genuinely aperiodic hull components.

---

## 8. The invariant-measure drift obstruction

Let `Phi:mathfrak H->R` be bounded and continuous.

Suppose a future PDE argument proves

\[
\boxed{
\Phi(\sigma\mathbf Y)-\Phi(\mathbf Y)
\ge c_*a(\mathbf Y)
}
\]

for every point of the retained marked hull, with `c_*>0`.

Integrating against the invariant measure gives

\[
\int\Phi\circ\sigma\,d\mu
-
\int\Phi\,d\mu
\ge
c_*\int a\,d\mu.
\]

The left side is zero by invariance, whereas the right side is strictly positive.

Therefore

\[
0\ge c_*\delta_0>0,
\]

a contradiction.

Hence:

\[
\boxed{
\text{a bounded continuous strict ratchet-drift observable would close the marked compact hull.}
}
\]

This is an abstract reduction, not yet the required PDE observable.

---

## 9. More general cocycle form

It is enough to find a nonnegative continuous dissipation/defect function `D` satisfying

\[
\Phi\circ\sigma-\Phi\ge D
\]

and

\[
D\ge c_*a
\]

on the active branch.

Invariant averaging then gives

\[
0
=
\int(\Phi\circ\sigma-\Phi)d\mu
\ge
\int Dd\mu
\ge
c_*\delta_0,
\]

again impossible.

Thus the analytic problem is converted into construction of a **strict log-scale cocycle**.

---

## 10. Audit of obvious candidate observables

The following candidates do not presently provide the required signed drift.

### 10.1 Scale-normalized enstrophy

A quantity such as

\[
(-s)^{1/2}\|\Omega(s)\|_2^2
\]

is scale invariant on the Type-I class, but the 3D stretching term destroys monotonicity.

### 10.2 Backward-truncated palinstrophy

M5-484 gives

\[
\varepsilon^{1/2}
\int_{-\infty}^{-\varepsilon}
\|\nabla\Omega\|_2^2ds
\le C.
\]

This is a critical bounded observable family, but no one-step signed drift under dilation has been proved.

Indeed exact DSS scaling can saturate the same `eps^{-1/2}` rate.

### 10.3 Endpoint material-axis orientation

The total projective direction action cannot be bounded below by a difference of a bounded endpoint angle: the direction can execute loops or oscillations and return to its initial orientation while paying positive total variation.

Thus a naive orientation potential is ruled out.

### 10.4 Strong `L3` norm

A global strong `L3` bound would enter known regularity/non-DSS rigidity theory, but the present hard branch was isolated precisely because the critical `1/r`-type tail can fail strong `L3`.

It cannot be assumed.

---

## 11. DSD interpretation

The formation-level distinction is now explicit.

### Parent fact

\[
A_{ratchet}^{dens}:
\quad
\text{positive density of scale-critical material-axis events}.
\]

### Naive but invalid descendant claim

\[
\text{one chosen event survives every blow-down}.
\]

### Correct descendant structure

\[
\boxed{
A_{ratchet}^{dens}
\Longrightarrow
(\mathfrak H,\sigma,\mu,a)
}
\]

where

- `mathfrak H` is a compact complete marked dilation hull;
- `sigma` is the generation shift;
- `mu` is shift invariant;
- `a` is the closed ratchet mark;
- `int a dmu>0`.

The mark is therefore retained statistically/dynamically rather than by falsely identifying one parent event with one fixed descendant event.

---

## 12. New periodic/aperiodic split

The M5-483 split is sharpened to

\[
\boxed{
E_{dil}^{ancient,marked}
\Longrightarrow
E_{DSS}^{marked}
\lor
E_{aper}^{marked}.
}
\]

Both branches carry an invariant measure with positive average ratchet mark.

In the periodic case the invariant measure may be the uniform measure on a finite DSS cycle.

In the aperiodic case it is supported on a compact recurrent dilation subsystem.

Therefore the next theorem should not be a generic DSS-only Liouville theorem if a marked-cocycle argument can treat both at once.

---

## 13. Highest-value next target

Search for a PDE observable/cocycle `Phi` satisfying one of the following.

### Target C1 — strict projective drift

\[
\Phi\circ\sigma-\Phi
\ge c\,a_{tilt}.
\]

### Target C2 — strict directional-diffusion drift

\[
\Phi\circ\sigma-\Phi
\ge c\,a_{diff}.
\]

### Target C3 — dual-source/flux drift

Use the retained source/flux genealogy to construct

\[
\Phi\circ\sigma-\Phi
\ge c\,a_{ratchet}
-
\text{controlled exact coboundary}.
\]

Any such bounded drift would contradict the invariant marked hull immediately.

If all natural bounded observables fail by exact scale invariance or reversible cycling, that failure itself identifies the next survivor: a genuinely conservative/recurrent marked critical element rather than an untyped DSS tail.

---

## 14. Updated frontier

After M5-484--485 the compact bounded lane is

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{amp/freq/mass}^{strong}
\lor
E_{dil}^{ancient,marked},
}
\]

where the marked compact endpoint now carries

\[
\boxed{
\text{Type-I ancient dilation dynamics}
+
\text{critical terminal tail}
+
\text{record carrier}
+
\text{truncated palinstrophy bound}
+
\text{positive-mean recurrent ratchet measure}.
}
\]

The remaining missing object is a strict PDE cocycle or an equivalent rigidity theorem for this marked invariant hull.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
