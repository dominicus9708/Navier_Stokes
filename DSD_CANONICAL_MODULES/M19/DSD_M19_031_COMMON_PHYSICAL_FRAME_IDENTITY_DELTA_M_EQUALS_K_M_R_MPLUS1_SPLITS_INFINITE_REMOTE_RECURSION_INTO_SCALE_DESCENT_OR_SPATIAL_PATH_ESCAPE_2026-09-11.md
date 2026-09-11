# M19-031 — The common physical-frame identity delta_m = K_m r_{m+1} splits infinite remote recursion into scale descent or spatial path escape

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE COMMON-FRAME EMBEDDING / SCALE-PATH DICHOTOMY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-030

The residual bounded-weak-\(L^3\) remote branch is an infinite sequence of weak remote/shell-H generations unless an already typed exit occurs.

For generation \(m\), let

- \(x_m\): physical center in the original Navier--Stokes coordinates;
- \(r_m>0\): its physical natural scale;
- \(D_m\): distance from generation \(m\) to generation \(m+1\), measured in units of \(r_m\);
- \(\ell_m\): child natural scale measured in units of \(r_m\).

Then

\[
\boxed{r_{m+1}=r_m\ell_m,}
\]

and

\[
\boxed{|x_{m+1}-x_m|=r_mD_m.}
\]

Define the dimensionless remoteness ratio

\[
\boxed{K_m:=\frac{D_m}{\ell_m}.}
\]

On the genuine remote recursion,

\[
K_m\to\infty
\]

along the selected generations.

## 2. Exact common-frame identity

Set

\[
\delta_m:=|x_{m+1}-x_m|.
\]

Then

\[
\delta_m=r_mD_m
=r_mK_m\ell_m
=K_mr_{m+1}.
\]

Hence

\[
\boxed{\delta_m=K_mr_{m+1}.}
\]

Equivalently,

\[
\boxed{r_{m+1}=\frac{\delta_m}{K_m}.}
\]

This identity is in one original physical coordinate system and does not add resources across recentered frames.

## 3. Bounded spatial increments force physical scale descent

Suppose

\[
\sup_m\delta_m<\infty.
\]

Since

\[
K_m\to\infty,
\]

we obtain

\[
\boxed{r_{m+1}\to0.}
\]

More quantitatively,

\[
\boxed{r_{m+1}=O(K_m^{-1}).}
\]

If in addition

\[
\delta_m\to0,
\]

then

\[
\boxed{r_{m+1}=o(K_m^{-1}).}
\]

Thus a remote chain whose physical center jumps do not grow without bound must generate smaller and smaller physical natural scales.

## 4. Failure of scale descent forces large physical displacement

Conversely, suppose along a subsequence

\[
r_{m+1}\ge r_*>0.
\]

Then

\[
\delta_m=K_mr_{m+1}
\ge r_*K_m
\to\infty.
\]

Therefore

\[
\boxed{\text{no physical scale descent}\Longrightarrow\text{unbounded one-step spatial export}.}
\]

This is stronger than the earlier purely normalized split between \(D_m\) and \(\ell_m\).

## 5. Infinite chain classified by physical path length

Define the total physical center-path variation

\[
\boxed{\mathcal L:=\sum_{m=0}^\infty\delta_m.}
\]

### Case A: finite path length

If

\[
\mathcal L<\infty,
\]

then

\[
\delta_m\to0
\]

and the centers converge to a finite physical point

\[
x_m\to x_\infty.
\]

Moreover

\[
\boxed{r_{m+1}=\delta_m/K_m\to0.}
\]

Hence the infinite remote recursion becomes an infinitely nested small-scale cascade accumulating at one physical point.

### Case B: infinite path length

If

\[
\mathcal L=\infty,
\]

then the sequence performs infinite physical spatial travel.

This splits further into:

1. \(|x_m|\to\infty\) or an unbounded subsequence: genuine physical export;
2. bounded positions with infinite path variation: recurrent spatial wandering/reuse inside a bounded physical region.

The second case cannot be called export merely from path length; cancellation of successive displacement vectors is possible.

## 6. Cauchy center genealogy

If the centers are Cauchy, then necessarily

\[
\delta_m\to0.
\]

Thus

\[
\boxed{x_m\text{ Cauchy}\Longrightarrow r_{m+1}=o(K_m^{-1})\to0.}
\]

Therefore any infinite remote recursion accumulating at one physical center is automatically a true physical scale cascade.

This is a common-frame result; no assumption about additive energy is required.

## 7. Bounded but non-Cauchy center genealogy

A bounded sequence \(x_m\) need not be Cauchy.

If it repeatedly moves between separated physical regions, then there exists \(d_*>0\) and infinitely many generations with

\[
\delta_m\ge d_*.
\]

For those generations,

\[
\boxed{r_{m+1}\le d_m/K_m\to0}
\]

provided the increments remain uniformly bounded.

Thus even bounded wandering generally coexists with scale descent; the unresolved feature is repeated relocation/reuse of ever smaller active structures.

This is naturally an ancestry/return-alignment issue rather than a new local PDE currency.

## 8. Updated remote recursion split

The infinite residual remote chain now satisfies

\[
\boxed{
\mathcal T_{remote}
\Longrightarrow
\begin{cases}
G_{nested\ physical\ scale\ cascade\ at\ finite\ accumulation\ point},\\
G_{unbounded\ physical\ spatial\ export},\\
G_{bounded\ spatial\ wandering/reuse\ with\ scale\ descent}.
\end{cases}
}
\]

The first and third contain explicit physical scale descent.
The second is genuine export.

## 9. Root routing

### Nested scale cascade

This branch approaches one physical point through smaller and smaller scales. Its unresolved issue is whether the nested events can be embedded into a nonreused fixed-parent ancestry ledger. Therefore it interfaces directly with

\[
\boxed{\mathcal T_{AC}.}
\]

### Unbounded spatial export

This joins the remote/macroscopic-tail or escaping critical-tail branch and therefore interfaces with

\[
\boxed{\mathcal T_{critical}}
\]

or the already typed export root.

### Bounded wandering/reuse

This is repeated relocation of ever smaller active structures within a bounded parent region. Its mathematical obstruction is again material identity, reuse, and return incidence; hence it is primarily an R-AC interface.

Thus the common-frame geometry strongly suggests

\[
\boxed{
\mathcal T_{remote}
\subset
\mathcal T_{AC}
\cup
\mathcal T_{critical}
\cup
G_{typed\ export},
}
\]

provided the nested/wandering events can be certified as the same event class used by those two theorem frontiers.

The final event-class identification is not proved here.

## 10. New missing bridge

The remaining independent statement is therefore narrower than an infinite remote cascade theorem:

\[
\boxed{
\mathcal B_{remote\to AC/critical}:
\text{common-frame nested/wandering satellite events}
\Rightarrow
\text{the certified R-AC or R-critical event class}.
}
\]

This is a representation/genealogy bridge, not a new analytic estimate.

## 11. Next calculation

M19-032 should test the finite-path nested case first.

If

\[
x_m\to x_\infty,
\qquad
r_m\to0,
\]

and each generation has a fixed point-picked vorticity mark at its own scale, calculate the corresponding local scale-invariant velocity/vorticity quantity in one fixed ball around \(x_\infty\).

The aim is to decide whether this nested remote chain automatically creates either

1. critical Morrey/scattering activity, sending it to R-critical; or
2. a first-hitting ancestry ladder with the occupancy deficiency already encoded by \(\mathcal T_{AC}\).

---

\[
\boxed{\text{M19-031 COMPLETE; INFINITE REMOTE RECURSION IS NOW A COMMON-PHYSICAL-FRAME SCALE/PATH PROBLEM.}}
\]
