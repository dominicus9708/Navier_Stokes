# DSD M5-618 — External Beltrami Liouville theorem closes exact curl-alignment and forces a uniform non-Beltrami defect

Date: 2026-09-03

Status: **EXTERNAL-THEOREM DEPENDENCY / NADIRASHVILI'S FINITE-ENERGY BELTRAMI LIOUVILLE THEOREM APPLIES TO THE GENERAL ALIGNMENT CONDITION `v x curl v = 0`, NOT ONLY TO A CONSTANT-PROPORTIONALITY CURL EIGENFIELD / SINCE EACH CE-H VORTICITY STATE W IS SMOOTH, DIVERGENCE-FREE, AND L2, THE EXACT SUBBRANCH `W x curl W = 0` IS TRIVIAL / THE MARKED COMPACT HARD COMPONENT EXCLUDES W=0, SO CONTINUITY AND COMPACTNESS UPGRADE THIS TO A UNIFORM POSITIVE LOWER BOUND ON THE L2 NON-BELTRAMI DEFECT `||W x curl W||_2` / THIS REMOVES THE EXACT BELTRAMI-VORTICITY ESCAPE BUT DOES NOT YET RULE OUT NON-BELTRAMI CE-H / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External theorem used

Nadirashvili, *Liouville theorem for Beltrami flow* (2014), defines a Beltrami flow in `R3` by the stationary-Euler/Bernoulli condition

\[
\boxed{v\times\operatorname{curl}v=0}
\]

and proves that a `C1` Beltrami flow satisfying

\[
v\in L^p(\mathbb R^3),
\qquad 2\le p\le3,
\]

is identically zero.

In particular,

\[
\boxed{
v\in C^1\cap L^2,
\quad
\nabla\cdot v=0,
\quad
v\times\operatorname{curl}v=0
\Longrightarrow
v=0.
}
\]

The theorem does **not** require a spatially constant proportionality factor in `curl v = alpha v`.

This note therefore marks the step as an external theorem dependency.

---

## 2. Why W satisfies the theorem's regularity class

On the retained CE-H compact hard component, the all-order Sobolev bounds established in M5-503--508 give

\[
W\in C^\infty(\mathbb R^3)
\cap L^2(\mathbb R^3),
\]

with

\[
\nabla\cdot W=0.
\]

Thus if at any state

\[
\boxed{W\times(\nabla\times W)=0,}
\]

then `W` is a finite-energy Beltrami flow in the sense of the theorem.

Therefore

\[
\boxed{W=0.}
\]

---

## 3. Exact Beltrami-vorticity branch is eliminated

The marked hard component retains a fixed nonzero coherent carrier and hence excludes the zero state.

Consequently

\[
\boxed{
W\times(\nabla\times W)\not\equiv0
}
\]

for every state in that component.

This eliminates the exact subbranch

\[
\nabla\times W=\alpha W
\]

whenever such an `alpha` is defined, and more generally eliminates the alignment equation `W x curl W = 0` without dividing by `|W|`.

---

## 4. Define the non-Beltrami defect

Let

\[
C:=\nabla\times W
\]

and define

\[
\boxed{
\mathcal B(W)
:=
\|W\times C\|_{L^2(\mathbb R^3)}.
}
\]

The all-order bounds give

\[
W\in L^\infty,
\qquad
C\in L^2,
\]

so `B(W)` is finite.

Moreover the global strong compactness makes this observable continuous on the marked hull.

---

## 5. Uniform positive compactness gap

Suppose no uniform positive lower bound existed.

Then there would be marked states `W_n` with

\[
\mathcal B(W_n)\to0.
\]

By compactness, after a subsequence

\[
W_n\to W_\infty
\]

strongly in sufficiently high Sobolev topology, hence

\[
W_n\times(\nabla\times W_n)
\to
W_\infty\times(\nabla\times W_\infty)
\]

strongly in `L2`.

Thus

\[
W_\infty\times(\nabla\times W_\infty)=0.
\]

The external Liouville theorem gives

\[
W_\infty=0.
\]

But the persistent carrier mark survives compact extraction and excludes zero.

Contradiction.

Therefore there exists

\[
b_*>0
\]

such that

\[
\boxed{
\|W\times(\nabla\times W)\|_2
\ge b_*>0
}
\]

throughout the marked compact CE-H component.

---

## 6. Transverse-curl interpretation

On the active set write

\[
C=\alpha W+C_\perp,
\qquad
C_\perp\perp W.
\]

Then

\[
|W\times C|
=|W|\,|C_\perp|.
\]

Hence the uniform defect implies a persistent transverse curl population.

Using the compact `L∞` vorticity cap,

\[
\|W\times C\|_2^2
\le
\|W\|_\infty^2
\|C_\perp\|_2^2,
\]

so

\[
\boxed{
\|C_\perp\|_2
\ge c_*>0.
}
\]

Thus CE-H cannot collapse to a locally one-dimensional curl geometry globally.

---

## 7. Relation to the CE-H hard core

The survivor now simultaneously has

\[
\Delta W=\kappa W
\quad\text{a.e. on the active set},
\]

\[
\Sigma W=\sigma W,
\]

\[
D_B\xi=0,
\]

but also

\[
\boxed{
W\times(\nabla\times W)
\text{ has a uniform nonzero }L^2\text{ charge}.
}
\]

So the vorticity direction is materially frozen while its spatial curl geometry is necessarily non-Beltrami.

This is a new mandatory spatial twisting channel.

---

## 8. Audit firewall

Nadirashvili's theorem is used only on the **exact** alignment branch.

No quantitative stability theorem of the form

\[
\|W\times\operatorname{curl}W\|\ll1
\Longrightarrow W=0
\]

is imported.

The uniform positive defect follows instead from our own compactness plus exact Liouville at the limiting zero-defect state.

The external dependency must remain explicitly listed in the final proof audit.

---

## 9. Next target

The vector identity

\[
\nabla\cdot\bigl(W\times(\nabla\times W)\bigr)
=
|\nabla\times W|^2
+
W\cdot\Delta W
\]

on divergence-free `W` connects the new non-Beltrami flux directly to the CE-H negative-kappa/Rayleigh budget.

The next calculation should localize this identity and determine whether the mandatory transverse-curl flux can be absorbed by the finite persistent-lineage network or forces another separated source/turnover channel.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
