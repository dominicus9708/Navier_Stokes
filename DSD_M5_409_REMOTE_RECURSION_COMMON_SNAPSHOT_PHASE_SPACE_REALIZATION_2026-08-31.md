# DSD M5-409 — Common-snapshot realization of finite remote recursion

Date: 2026-08-31

Status: **THE ITERATED REMOTE-SATELLITE CONSTRUCTION CAN BE PULLED BACK, FOR EVERY FINITE RECURSION DEPTH, TO A SINGLE PHYSICAL PRELIMIT SNAPSHOT WITH EXPLICIT CENTERS AND NATURAL SCALES / SUCCESSIVE NODES ARE GENUINELY SEPARATED IN THE JOINT POSITION-SCALE PHASE SPACE, EVEN THOUGH THE PHYSICAL NATURAL SCALES NEED NOT BE MONOTONE / THIS REPLACES THE OVERLY CAUTIOUS READING THAT DIFFERENT RECENTERED FRAMES CANNOT BE COMPARED AT ALL / HOWEVER NONADJACENT NODES MAY REVISIT THE SAME PHASE-SPACE CELL, SO NO TREE-WIDTH OR INFINITE-DESCENT CONTRADICTION IS CLAIMED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-402 derived the recursion

\[
S_{remote}^{(m)}
\Longrightarrow
T_{dynamic}^{(m)}
\lor A_{detached}^{(m)}
\lor S_{remote}^{(m+1)}.
\]

Its firewall correctly warned that successive satellite scales live in different recentered/rescaled coordinates and therefore cannot simply be declared monotonically decreasing or additively disjoint.

There is, however, a stronger statement available than the phrase `different frames` suggests.

Every remote-of-remote extraction in M5-402 is performed at the same normalized snapshot `sigma=0` of its parent satellite.

For every **finite** recursion depth, the affine scaling/translation maps can therefore be explicitly composed back to one physical prelimit time.

The aim is to record that common phase-space realization without introducing a false monotone-scale assumption.

---

## 2. One remote edge

Let a parent physical carrier have center and natural length

\[
(x_m,r_m).
\]

Use its normalized coordinates

\[
z=\frac{x-x_m}{r_m}.
\]

Suppose the next remote satellite is selected at normalized center

\[
z_{m+1}
\]

with normalized vorticity amplitude

\[
\mu_{m+1}>0.
\]

Its normalized natural length is

\[
\boxed{
\ell_{m+1}:=\mu_{m+1}^{-1/2}.
}
\]

Pulling the satellite back to physical variables gives

\[
\boxed{
x_{m+1}=x_m+r_mz_{m+1}}
\]

and

\[
\boxed{
r_{m+1}=r_m\ell_{m+1}.}
\]

The physical vorticity amplitude at the new center is then of natural order

\[
|\omega(x_{m+1})|
\asymp
\frac{\nu}{r_{m+1}^2}
\]

up to the retained normalization constants.

---

## 3. Remote separation is exactly invariant under pullback

The parent-frame remote condition is

\[
\frac{|z_{m+1}|}{\ell_{m+1}}
\to\infty.
\]

In physical variables,

\[
|x_{m+1}-x_m|
=r_m|z_{m+1}|,
\]

so

\[
\begin{aligned}
\frac{|x_{m+1}-x_m|}{r_{m+1}}
&=
\frac{r_m|z_{m+1}|}
{r_m\ell_{m+1}}\\
&=
\boxed{
\frac{|z_{m+1}|}{\ell_{m+1}}.
}
\end{aligned}
\]

Hence every recursive edge is a genuine physical statement:

\[
\boxed{
\frac{|x_{m+1}-x_m|}{r_{m+1}}
\to\infty.
}
\]

The child is remote relative to its own natural scale.

---

## 4. The scales are not monotone

The physical scale ratio is

\[
\boxed{
\frac{r_{m+1}}{r_m}
=\ell_{m+1}
=\mu_{m+1}^{-1/2}.
}
\]

The remote criterion controls

\[
|z_{m+1}|/\ell_{m+1},
\]

not `ell_{m+1}` itself.

Therefore any of the following may occur:

\[
r_{m+1}\ll r_m,
\qquad
r_{m+1}\asymp r_m,
\qquad
r_{m+1}\gg r_m.
\]

Thus the M5-402 firewall against a naive decreasing-scale descent remains valid.

What is corrected is only the stronger pessimistic reading that the nodes cannot be placed in one physical phase space at finite depth.

---

## 5. Adjacent nodes are phase-space separated

Fix a large constant `K` and compare two consecutive nodes.

There are two possibilities.

### A. Their scales are not comparable

If

\[
\frac{r_{m+1}}{r_m}\notin[K^{-1},K],
\]

then the two nodes are separated in logarithmic scale.

### B. Their scales are comparable

If

\[
K^{-1}r_m\le r_{m+1}\le Kr_m,
\]

then the remote edge gives

\[
\frac{|x_{m+1}-x_m|}{r_{m+1}}\to\infty,
\]

so the two nodes are separated spatially by arbitrarily many comparable natural radii.

Therefore every sufficiently remote edge satisfies the phase-space alternative

\[
\boxed{
\text{large log-scale separation}
\quad\lor\quad
\text{large normalized spatial separation}.
}
\]

This is exactly the separation required by the M5-408 critical `dot H^{-1/2}` Bessel atoms.

---

## 6. Finite recursion depth can be realized simultaneously

Consider a recursion of fixed depth `M`.

The first satellite construction is obtained after passing to a subsequence of physical first-hitting/prelimit snapshots.

The second construction uses the same selected `sigma=0` snapshot in the first satellite frame and may require a further subsequence.

Continue finitely many times.

A finite nested sequence of subsequences has a diagonal subsequence on which all `M` selected nodes and all retained finite-window estimates hold simultaneously.

Pull each node back by the composition formula of Sections 2--3.

Thus for every fixed `M` there are physical prelimit snapshots

\[
t_n^{(M)}
\]

containing simultaneous phase-space nodes

\[
\boxed{
(x_{1,n},r_{1,n}),
\ldots,
(x_{M,n},r_{M,n})
}
\]

with every adjacent edge satisfying the remote phase-space separation.

No assertion is made that one single subsequence realizes literally infinite depth.

The correct quantified statement is:

\[
\boxed{
\text{arbitrarily long remote recursion}
\Longrightarrow
\text{arbitrarily long finite phase-space paths in single snapshots}.
}
\]

---

## 7. Each well-formed node carries a critical atom

Whenever the point-picked node remains on the bounded-local-derivative branch, interior analyticity gives a fixed normalized thick vorticity core.

Therefore M5-408 applies and assigns to the physical node a critical test atom

\[
\psi_{m,n}
\]

with

\[
\boxed{
|\langle\omega(t_n),\psi_{m,n}\rangle|
\ge c_*\nu.
}
\]

If the thick-core formation fails because a local derivative or localization estimate breaks, the node has already exited to

\[
H_{local}^{crit}
\lor T_{interface}.
\]

Thus on the pure recursive remote lane every realized node is a legitimate M5-408 carrier atom.

---

## 8. Adjacent separation is not global Bessel separation

A chain

\[
A\to B\to A\to B\to\cdots
\]

is logically possible at the level of phase-space labels: consecutive nodes may be remote while a later node returns to a previous phase-space cell.

Therefore one must not infer

\[
\text{path length }M
\Longrightarrow
M\text{ pairwise Bessel-separated atoms}.
\]

The correct invariant is the number of **distinct phase-space cells** visited by the path.

Let

\[
\mathcal N_M
\]

denote the maximal cardinality of a phase-space-separated subfamily extracted from the first `M` nodes.

Then M5-408 gives

\[
\boxed{
\mathcal N_M\,\nu^2
\lesssim
\|u(t_n^{(M)})\|_{\dot H^{1/2}}^2.
}
\]

This is valid after selecting a standard separated subfamily, but `mathcal N_M` may be much smaller than `M` if the path repeatedly revisits old cells.

---

## 9. Exact novelty-or-reuse dichotomy

For arbitrarily long remote paths there are only two combinatorial possibilities.

### A. Unbounded phase-space novelty

There is a sequence `M_k -> infinity` such that

\[
\mathcal N_{M_k}\to\infty.
\]

Then

\[
\boxed{
\|u(t_{n_k})\|_{\dot H^{1/2}}
\to\infty.
}
\]

This is an explicit critical-Sobolev H route.

### B. Bounded phase-space novelty

There is a fixed `N_*` such that arbitrarily long paths visit only `N_*` effective phase-space cells up to the retained separation constants.

Then the remote recursion is not producing indefinitely new scale-space structure; it is repeatedly **reusing/revisiting a finite phase-space population**.

This is a new, sharply stated reuse branch:

\[
\boxed{
R_{remote}^{finite\ phase\ memory}.
}
\]

It must not be declared contradictory merely from the path length.

The next target is to determine whether a finite set of natural-strength phase-space carriers can self-supply the remote/ambient strain required to keep the recursion active, or whether fresh diffuse/shell mass is necessarily recruited.

---

## 10. Relation to M5-285 anti-model

The affine fixed-point anti-model explains why the reuse branch cannot be dismissed by local PDE compactness alone.

However M5-403--404 subsequently showed that a nonzero affine fixed point appearing on larger and larger prelimit balls forces palinstrophy/enstrophy H.

Thus finite phase-memory reuse is narrower than the old generic affine warning.

The remaining issue is whether a finite collection of **natural-strength localized carriers plus bounded background** can generate the repeated remote strain/source requirement without importing new shell mass.

---

## 11. DSD audit

### CORRECTED

The statement

`successive satellite generations live in different frames, therefore no common physical comparison is available`

is too strong for finite recursion depth.

The correct statement is:

\[
\boxed{
\text{finite depth can be pulled back to one snapshot,}
\quad
\text{but scale monotonicity and pairwise distinctness are not automatic.}
}
\]

### DERIVED

- explicit center/scale composition;
- remote separation invariance;
- adjacent phase-space separation;
- finite-depth simultaneous realization;
- critical carrier assignment at every well-formed node;
- novelty-or-finite-reuse dichotomy.

### FIREWALL

- no infinite-depth single-subsequence realization is assumed;
- adjacent separation does not imply all nodes are mutually orthogonal;
- cycles/revisits remain possible;
- critical-norm escalation is not itself a global contradiction.

---

## 12. Updated remote target

The iterated remote branch can now be refined to

\[
\boxed{
S_{remote}^{iterated}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor
R_{remote}^{finite\ phase\ memory}
\lor
H_{local}^{crit}
\lor
T_{interface}.
}
\]

The next calculation should attack only

\[
\boxed{R_{remote}^{finite\ phase\ memory}.}
\]

Specifically: estimate the normalized strain at one carrier generated by a finite set of other natural-strength carriers and show that truly remote separated carriers have vanishing pairwise influence unless an extended/diffuse shell reservoir is present.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]