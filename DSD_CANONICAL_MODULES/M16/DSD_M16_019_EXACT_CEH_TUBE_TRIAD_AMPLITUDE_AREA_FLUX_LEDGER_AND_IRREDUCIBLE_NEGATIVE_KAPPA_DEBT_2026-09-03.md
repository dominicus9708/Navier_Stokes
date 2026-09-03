# DSD M16-019 — Exact CE-H tube triad: amplitude, area, flux, and the irreducible negative-kappa debt

Date: 2026-09-03
Canonical ID: **M16-019**

Status: **INTERNAL EXACT TUBE LEDGER / ON AN INFINITESIMAL MATERIAL VORTEX TUBE IN THE CE-H DOUBLE-EIGENLINE BRANCH, AMPLITUDE, TRANSVERSE AREA, AND VORTICITY FLUX SATISFY THE EXACT TRIAD `D_B log rho = sigma+kappa-1`, `D_B log A = 1-sigma`, `D_B log Phi = kappa`. A CLOSED SAME-LINEAGE RECHARGE CYCLE RETURNING BOTH AMPLITUDE AND FLUX MUST HAVE CYCLE-MEAN `kappa=0` AND `sigma=1`. BUT THE GLOBAL IDENTITY `int kappa rho^2=-P` GIVES A STRICT ENSTROPHY-WEIGHTED NEGATIVE-KAPPA EXCESS EQUAL TO PALINSTROPHY, SO A SURVIVOR CANNOT CONSIST ONLY OF NEUTRAL CLOSED REUSE TUBES; A COMPENSATING NEGATIVE-KAPPA POPULATION REMAINS NECESSARY. THIS DOES NOT YET EXCLUDE A RECURRENT TWO-POPULATION CYCLE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material line stretching in similarity variables

Let

\[
B=U+\frac12y.
\]

Consider an infinitesimal material vortex tube whose tangent direction is

\[
\xi=\frac W{|W|}.
\]

For a material line element `ell xi`, the logarithmic length rate is

\[
D_B\log\ell
=\xi\cdot(\nabla B)\xi.
\]

Now

\[
\nabla B=\nabla U+\frac12I=\Sigma+A+\frac12I.
\]

On the CE-H branch,

\[
\Sigma\xi=\sigma\xi.
\]

Because `W` is parallel to `xi`, the antisymmetric velocity-gradient part satisfies

\[
A\xi=0.
\]

Therefore

\[
\boxed{
D_B\log\ell
=\sigma+\frac12.
}
\]

---

## 2. Exact transverse-area law

The similarity material field has

\[
\nabla\cdot B=\frac32.
\]

Hence an infinitesimal material volume element `V` obeys

\[
D_B\log V=\frac32.
\]

Write locally

\[
V\sim A\ell,
\]

where `A` is the cross-sectional area normal to `xi`.

Then

\[
D_B\log A
=
D_B\log V-D_B\log\ell.
\]

Using Section 1,

\[
\boxed{
D_B\log A
=1-\sigma.
}
\]

Thus axial strain above the similarity value `1` contracts the transverse section, while strain below `1` expands it.

---

## 3. Combine with the exact amplitude law

M16-017 gives

\[
\boxed{
D_B\log\rho
=\sigma+\kappa-1.
}
\]

Adding the amplitude and area equations gives

\[
D_B\log(\rho A)
=\kappa.
\]

For an infinitesimal transverse section whose normal is `xi`, the vorticity flux is

\[
\Phi\sim\rho A.
\]

Therefore

\[
\boxed{
D_B\log\Phi=\kappa.
}
\]

The complete local CE-H tube triad is

\[
\boxed{
\begin{aligned}
D_B\log\rho&=\sigma+\kappa-1,\\
D_B\log A&=1-\sigma,\\
D_B\log\Phi&=\kappa.
\end{aligned}
}
\]

The third equation is exactly the sum of the first two.

---

## 4. Consistency with the finite-surface material flux law

For a finite material surface `Sigma_t`, the earlier exact flux identity is

\[
\frac d{d\theta}
\int_{\Sigma_t}W\cdot n\,dA
=
\int_{\Sigma_t}\Delta W\cdot n\,dA.
\]

On the Laplacian eigenline branch,

\[
\Delta W=\kappa W,
\]

so

\[
\boxed{
\Phi'
=
\int_{\Sigma_t}\kappa W\cdot n\,dA.
}
\]

For an infinitesimal coherent tube, `kappa` is constant to leading order across the section and this reduces to

\[
\Phi'=\kappa\Phi,
\]

which is precisely

\[
D_B\log\Phi=\kappa.
\]

Thus the local tube derivation and the exact finite-surface flux law agree.

---

## 5. Closed same-lineage recharge cycle

Consider one material tube lineage over a cycle of duration `T`.

Assume that at the end of the cycle its amplitude and flux return to their initial values:

\[
\rho(T)=\rho(0),
\qquad
\Phi(T)=\Phi(0).
\]

Because `Phi=rho A`, the transverse area also returns:

\[
A(T)=A(0).
\]

Integrating the flux equation gives

\[
0
=
\log\frac{\Phi(T)}{\Phi(0)}
=
\int_0^T\kappa d\theta.
\]

Therefore

\[
\boxed{
\frac1T\int_0^T\kappa d\theta=0.
}
\]

Integrating the area equation gives

\[
0
=
\int_0^T(1-\sigma)d\theta,
\]

hence

\[
\boxed{
\frac1T\int_0^T\sigma d\theta=1.
}
\]

The amplitude equation is then automatically consistent:

\[
\int_0^T(\sigma+\kappa-1)d\theta=0.
\]

Thus a perfectly closed same-lineage recharge cycle is a **neutral kappa cycle with unit mean axial strain** in similarity normalization.

---

## 6. This neutral cycle is not itself contradictory

The identities

\[
\langle\kappa\rangle_{cycle}=0,
\qquad
\langle\sigma\rangle_{cycle}=1
\]

are kinematically and algebraically consistent.

They explain why the hysteresis counter of earlier M16 steps cannot by itself be made monotone: positive-kappa recharge can be balanced by negative-kappa retirement on the same lineage, while axial contraction/expansion balances around mean strain `1`.

Therefore

\[
\boxed{
\text{closed tube cycle}
\not\Rightarrow
\text{contradiction}.
}
\]

A further ensemble/global constraint is required.

---

## 7. Global kappa bias is strictly negative

At every similarity time, the Laplacian eigenline identity gives

\[
\boxed{
\int\kappa\rho^2dy=-P,
\qquad
P=\int|\nabla W|^2dy.
}
\]

Decompose

\[
K_+=\int\kappa_+\rho^2dy,
\qquad
K_-=\int\kappa_-\rho^2dy.
\]

Then

\[
\boxed{
K_--K_+=P.
}
\]

On the nontrivial retained component, palinstrophy has positive invariant mean:

\[
\langle P\rangle>0.
\]

Therefore

\[
\boxed{
\langle K_-\rangle-\langle K_+\rangle
=\langle P\rangle>0.
}
\]

This is an **irreducible negative-kappa debt** at ensemble level.

---

## 8. Neutral closed tubes cannot be the whole invariant population

If every flux-carrying high-amplitude lineage were an exactly closed same-lineage cycle with zero cycle-mean `kappa`, then the flux-weighted high-amplitude population would contribute no net long-time kappa bias.

But the full field has a strictly negative enstrophy-weighted kappa bias equal to `-P`.

Therefore an additional population must carry the negative excess.

Schematically,

\[
\boxed{
\text{neutral recurrent source tubes}
+
\text{strict negative-kappa compensator population}.
}
\]

On the globally smooth tail-tight branch the compensator cannot be assigned to spatial infinity. It must recur in a fixed finite core after localization.

This is the same negative-kappa sheath/retirement population identified independently in M13--M18.

---

## 9. Two-population recurrent survivor

The remaining viable picture is now narrower:

### Population S — source/recharge tubes

- recurrent high-amplitude coherent tubes;
- positive strain during recharge;
- possibly positive kappa during flux recovery;
- closed or nearly closed material cycles.

### Population D — dissipative/negative-kappa compensators

- carries the strict excess `K_- - K_+ = P`;
- supplies negative-kappa retirement/sheath activity;
- must itself be renewed if it cannot remain high-amplitude indefinitely.

Thus the survivor requires a recurrent exchange

\[
\boxed{
S\rightleftarrows D
}
\]

or continuous creation of `D` from `S` and replenishment of `S` by recharge.

The proof problem has therefore become a finite-population exchange problem, not an unclassified PDE payer problem.

---

## 10. Remaining closure target

M16-019 still does not prove that the `S <-> D` exchange consumes a nonrenewable transverse-flux resource.

A recurrent compact flow may support two populations that exchange labels and exactly restore their macroscopic state.

The next decisive target is to derive an exchange ledger for the finite transverse vorticity flux:

\[
\text{source/recharge flux gain}
\quad\text{versus}\quad
\text{negative-kappa compensator flux loss}.
\]

One must determine whether the strict enstrophy-weighted negative-kappa excess `P` forces a strictly negative **flux-weighted** cycle bias after all covariance terms are included.

If yes, the same-lineage recycling loop closes. If not, the surviving covariance mechanism must be isolated explicitly.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
