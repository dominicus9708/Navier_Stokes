# Frontier after sequential reduction of the three remaining branches

Date: 2026-08-15

Overall status: **THE PREVIOUS THREE LARGE BRANCHES HAVE BEEN SEQUENTIALLY REDUCED TO ONE SOURCE-ACTIVE ENDGAME: REPEATED MATERIAL-VORTICITY-FLUX RESET SUPPORTED BY CRITICAL STRAIN / LOCAL DERIVATIVE REORGANIZATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Starting branch tree

The previous reduced frontier contained three large branches:

1. high-Hermite / high-curvature derivative structure;
2. spatial non-tightness / shell transport;
3. symmetric-affine / critical strain saturation.

They are no longer independent after the 2026-08-15 reductions.

---

# 2. Branch 1 — high Hermite / high curvature

## 2.1 Exact source descent

For every Gaussian parent/child split,

\[
\boxed{
J_p=\mathbb E[J_c]+J_{p\to c}^{\rm between},
}
\]

with

\[
\boxed{
|J_{p\to c}^{\rm between}|
\le\frac1{\sqrt2}\Delta B_{p\to c}.
}
\]

Thus high-Hermite source cannot remain an independent algebraic mean-source lane. It either

- descends to a smaller child scale; or
- becomes positive between-scale variance.

Repeated descent reaches the low-Hermite terminus or endpoint derivative concentration.

The low-Hermite material-center terminus has been closed on the stated bounded-affine track.

## 2.2 Energy-weighted derivative projective identity

For

\[
D_k=E_kJ_k,
\]

the exact derivative-covariance equation is

\[
\boxed{
\dot D_k
+2\nu E_{k+1}
\left[
J_{k+1}
+\|C_{k+1}-C_k\|_F^2
\right]
=\mathcal N_k.
}
\]

Hence viscosity cannot positively regenerate the energy-weighted derivative projective defect. It dissipates next-order defect and covariance mismatch.

After factorial weighting, the only positive obstruction is nonlinear derivative forcing / radius collapse.

## 2.3 First-hitting linear palinstrophy cone

On the terminal normalized past,

\[
\|\Omega\|_\infty\le1.
\]

Therefore

\[
|Q|\le CE.
\]

Whenever

\[
E'\ge0,
\]

we have

\[
\boxed{P\le C_\nu E.}
\]

Thus a globally dominant derivative-radius collapse cannot be the source-active global mechanism during enstrophy growth.

A small-mass local derivative spike remains possible, but by definition it is a spatial-concentration branch.

### Branch-1 status

\[
\boxed{
\text{global source-active high derivative}
\text{ removed};
}
\]

\[
\boxed{
\text{local derivative concentration}
\to
\text{spatial/material geometry}.
}
\]

Branch 1 therefore feeds Branch 2/3 rather than remaining independent.

---

# 3. Branch 2 — spatial non-tightness / shell transport

## 3.1 Coherent critical crossing

At the first Gaussian Reynolds-one crossing,

\[
BR^4=1,
\qquad
|\bar\Omega|\ge c>0,
\qquad
V_\omega\lesssim R^{-4}.
\]

Thus an `O(R^3)` region carries nearly one-axis order-one vorticity and robust signed cross-sectional flux

\[
\boxed{\Phi\sim R^2.}
\]

## 3.2 Material-flux reduction

For a material surface,

\[
\boxed{
\frac d{dt}\Phi_S
=-\nu\oint_{\partial S(t)}
(\nabla\times\omega)\cdot d\ell.
}
\]

Thus Eulerian translation/advection is not a material-vorticity-flux source.

A robust flux change routes through material-tube coarea to

\[
\boxed{
\text{palinstrophy / derivative concentration}
\quad\lor\quad
\text{large Lagrangian deformation}.
}
\]

If the flux is retained, strong geometry change is itself strain deformation; otherwise the precursor remains a material predecessor rather than a spatial-import escape.

### Branch-2 status

Spatial non-tightness is closed as an independent causal source on the coherent-crossing track:

\[
\boxed{
\text{spatial transport}
\to
\text{derivative flux}
\lor
\text{strain deformation}.
}
\]

---

# 4. Branch 3 — critical strain / material deformation

## 4.1 Material area-contraction barrier

If the current flux `Phi~R^2` is retained to a previous first-hitting checkpoint with vorticity cap `1/q`, then the previous material cross-sectional area obeys

\[
A_-\gtrsim qR^2,
\qquad
A_c\sim R^2.
\]

The exact material area identity is

\[
\frac d{dt}\log A(t)
=-\frac1{A(t)}
\int_{S(t)}n^TSn\,dA.
\]

Therefore flux retention forces

\[
\boxed{
\int
\frac1{A(t)}
\int_{S(t)}|n^TSn|\,dA\,dt
\ge
\log q-O(1),
}
\]

and hence

\[
\boxed{
\int\|S(t)\|_\infty dt
\ge\log q-O(1).
}
\]

This localizes the BKM-scale strain action on the actual material flux carriers.

## 4.2 Local axial extension cannot close on itself

The exact local Betchov divergence identity is

\[
\boxed{
\omega\cdot S\omega+4\det S
=\frac43\nabla\cdot\mathcal F_A.
}
\]

For coherent axial extension

\[
S\approx a\left(e\otimes e-rac12(I-e\otimes e)\right),
\qquad
\omega\approx\Omega e,
\]

the left side is

\[
\boxed{a(\Omega^2+a^2)>0.}
\]

Hence a Burgers-vortex-like coherent extension core requires a boundary cubic flux or strain/coherence breakdown.

With a cutoff,

\[
\boxed{
\left|
\int\chi_R(\omega\cdot S\omega+4\det S)
\right|
\lesssim
R^{-1}E^{5/4}P^{1/4}.
}
\]

Therefore the coherent axial extension routes to

- a large enstrophy reservoir;
- palinstrophy;
- shape/projective defect;
- or shell/boundary nonlinear flux.

It is not a closed local amplification mechanism.

## 4.3 Compact pancake precursor is impossible

At a `q`-earlier checkpoint, retained flux requires transverse radius

\[
\rho_-\sim R\sqrt q.
\]

Using the pointwise cap `|Omega_-|<=1/q`, divergence-free side flux gives

\[
\boxed{
L_{\rm terminate}\gtrsim R\sqrt q.
}
\]

Thus the precursor cannot be a short volume-preserving pancake of thickness `R/q`.

It must instead

- persist over a super-natural scale `R sqrt(q)`;
- turn off-axis;
- develop opposite polarity;
- or change flux viscously.

## 4.4 Automatic flux-reset checkpoint

The coherent crossing also satisfies the Gaussian-tail energy bound

\[
R^5(\log R)^{5/2}\lesssim W^{1/2},
\]

hence

\[
\boxed{
W/R^{10}\gtrsim(\log R)^5\to\infty.
}
\]

If present flux were retained to a `q`-earlier checkpoint, precursor kinetic-energy duality would require

\[
\|U\|_2^2
\gtrsim
R^5q^{1/2}.
\]

Finite kinetic energy therefore imposes the inheritance ceiling

\[
\boxed{
q\lesssim C W/R^{10}.
}
\]

Choose

\[
\boxed{
q_{\rm reset}=A W/R^{10}
}
\]

with fixed `A` above the energy constant. Then `q_reset->infinity`, but the current coherent flux cannot be inherited materially to that checkpoint.

Thus every sufficiently late coherent crossing must undergo a genuine flux/geometry reset after a canonical earlier first-hitting level.

---

# 5. Merger of all three branches

The three original branches now feed one another as follows:

\[
\boxed{
\text{high derivative}
\to
\text{dissipation or local concentration},
}
\]

\[
\boxed{
\text{local concentration}
\to
\text{material flux/geometry},
}
\]

\[
\boxed{
\text{material flux/geometry}
\to
\text{palinstrophy or strain deformation},
}
\]

while compact coherent strain itself requires shell/enstrophy/palinstrophy compensation and cannot be inherited indefinitely because of the automatic flux-reset checkpoint.

Therefore the genuinely source-active endgame is now

\[
\boxed{
\textbf{Repeated material-vorticity-flux reset}
+
\textbf{critical strain / derivative replenishment}.
}
\]

---

# 6. What is now excluded as an independent final branch

The following are no longer retained as separate final escapes on their stated hypotheses:

- pure affine/heat inheritance;
- mean-vorticity skew as an energy-production source;
- quadratic `Ab` material mean creation;
- degree-two trace mean creation;
- exact slow-fast-fast resonant low-chaos source;
- positive viscous projective derivative cycling;
- high-Hermite mean source without scale descent;
- Gaussian/exact-kernel volume collapse;
- pure spatial translation of a dangerous core;
- compact flux-preserving pancake precursor;
- a coherent axial-extension core closing its Betchov budget internally;
- one persistent material vortex tube inherited unchanged from fixed smooth data.

---

# 7. Single remaining proof target

A hypothetical singular solution must now execute infinitely many late reset episodes of the form

\[
\boxed{
\begin{gathered}
\text{earlier first-hitting checkpoint}\
\downarrow\\
\text{viscous/projective/polarity flux reorganization}\
+\text{critical strain deformation}\
\downarrow\\
\text{new coherent Reynolds-one crossing}\
(|\bar\Omega|\sim1,\ BR^4=1,\ R\to\infty).
\end{gathered}
}
\]

The current missing theorem can therefore be stated as a **flux-reset nonrepeatability theorem**:

> In a finite-energy smooth incompressible Navier--Stokes flow, a sequence of coherent Reynolds-one crossings with `R_j->infinity` cannot repeatedly rebuild signed material vorticity flux `Phi_j~R_j^2` after the automatic reset checkpoints while keeping every palinstrophy, projective/polarity, and critical-strain cost compatible with the finite-time energy solution class.

No such theorem has yet been proved here.

This is substantially narrower than the original branch tree but remains a genuinely critical 3D Navier--Stokes problem.

Overall status: **THREE LARGE BRANCHES SEQUENTIALLY MERGED INTO ONE FLUX-RESET / CRITICAL-STRAIN ENDGAME / GLOBAL REGULARITY NOT PROVED.**
