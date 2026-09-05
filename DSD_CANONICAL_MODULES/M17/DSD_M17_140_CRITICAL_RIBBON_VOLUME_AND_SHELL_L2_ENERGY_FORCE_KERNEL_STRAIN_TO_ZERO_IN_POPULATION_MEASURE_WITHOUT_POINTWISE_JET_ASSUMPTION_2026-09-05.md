# DSD M17-140 — Critical ribbon volume plus shell `L^2` energy forces kernel strain to zero in population measure without a pointwise jet assumption

Date: 2026-09-05  
Canonical ID: **M17-140**

Status: **UNCONDITIONAL POPULATION-LEVEL REPLACEMENT FOR THE POINTWISE PART OF M17-139 / ON A UNIFORMLY COMPACT NONDEGENERATE COMPLETE-RIBBON FAMILY WITH ORDER-ONE DIRECTOR-AREA FLUX AND `J_R=O(1)`, THE RIBBON HAS AN `O(1)` SIMILARITY-VOLUME FLOOR WHILE THE ENTIRE SHELL STRAIN `L^2` MASS IS `O(R^{-1})`. HENCE THE KERNEL STRAIN TENDS TO ZERO IN RIBBON VOLUME MEASURE, AND—BY NONDEGENERACY—IN THE EQUIVALENT DIRECTOR-FLUX/ARCLENGTH MEASURE. ANY LOCAL MAINTENANCE OR RECHARGE OF ORDER-ONE DIRECTOR-JACOBIAN DENSITY MUST THEREFORE CONCENTRATE ON A VANISHING POPULATION SET OR ARRIVE PRECHARGED FROM OUTSIDE THE SHELL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why M17-139 remains conditional pointwise

The first-hitting analyticity corridor gives uniform analytic and finite-Sobolev control on every **fixed normalized core ball**. Its constants are recorded as `C_R` for a fixed parent radius and are not a uniform estimate as the remote shell radius `R -> infinity`.

Likewise the existing annular `H^2` tail bridge treats

\[
R^3\int_{A_R^*}|\nabla^2U|^2dy
\]

as a separate scale-critical quantity; it does not supply a remote-shell uniform bound on

\[
\|\nabla\Sigma\|_{L^\infty}.
\]

Therefore the pointwise conclusion of M17-139,

\[
|\Sigma(p)|=O(R^{-1/5}),
\]

must retain its explicit uniform-jet hypothesis.

This module derives the population analogue without that hypothesis.

---

## 2. Critical shell strain budget

Let `C_R` be the fixed-factor enlarged annulus and assume the selected critical shell satisfies

\[
\boxed{
J_R:=R\int_{C_R}|\nabla U|^2dy\le J_*.
}
\]

Since

\[
|\Sigma|\le|\nabla U|,
\]

we have

\[
\boxed{
\int_{C_R}|\Sigma|^2dy\le\frac{J_*}{R}.
}
\]

No pointwise derivative estimate is used here.

---

## 3. Compact nondegenerate ribbon has a volume floor

Use the exact director-flux coordinates from M17-122:

\[
\boxed{
dV=\frac{d\Phi_J\,ds}{|J_\xi|}.
}
\]

Assume the uniformly compact nondegenerate complete-ribbon branch:

\[
\boxed{
\Phi_R\ge\Phi_*>0,
\qquad
0<c_J\le|J_\xi|\le C_J<\infty,
\qquad
L_-\le L(\Gamma_\lambda)\le L_+,
}
\]

with constants independent of the remote radius.

Then the ribbon volume is

\[
|\mathcal T_R|
=
\int d\Phi_J
\oint_{\Gamma_\lambda}\frac{ds}{|J_\xi|}.
\]

Using the flux floor, length floor, and Jacobian upper bound,

\[
\boxed{
|\mathcal T_R|
\ge
\frac{\Phi_*L_-}{C_J}
=:V_*>0.
}
\]

Thus an order-one-flux compact nondegenerate ribbon cannot hide in a vanishing three-dimensional similarity volume.

---

## 4. Ribbon RMS strain tends to zero

Because `T_R subset C_R`,

\[
\int_{\mathcal T_R}|\sigma_k|^2dy
\le
\int_{C_R}|\Sigma|^2dy
\le
\frac{J_*}{R}.
\]

Divide by the volume floor:

\[
\boxed{
\frac1{|\mathcal T_R|}
\int_{\mathcal T_R}|\sigma_k|^2dy
\le
\frac{J_*}{V_*R}.
}
\]

Therefore

\[
\boxed{
\|\sigma_k\|_{L^2(\mathcal T_R;dV/|\mathcal T_R|)}
=O(R^{-1/2})
\to0.
}
\]

The same statement holds for every strain component bounded by `|Sigma|`.

---

## 5. Quantitative exceptional-set estimate

For any threshold `epsilon_R>0`, define

\[
E_R(\epsilon_R)
:=
\{y\in\mathcal T_R:|\sigma_k(y)|>\epsilon_R\}.
\]

Chebyshev gives

\[
\boxed{
\frac{|E_R(\epsilon_R)|}{|\mathcal T_R|}
\le
\frac{J_*}{V_*R\epsilon_R^2}.
}
\]

Choosing

\[
\epsilon_R=R^{-1/4}
\]

yields

\[
\boxed{
\frac{|E_R(R^{-1/4})|}{|\mathcal T_R|}
=O(R^{-1/2})\to0.
}
\]

Hence on a fraction `1-o(1)` of the ribbon volume,

\[
\boxed{\sigma_k=o(1).}
\]

---

## 6. Convert volume measure to director-flux/arclength measure

Let

\[
d\nu_J:=d\Phi_J\,ds.
\]

Because

\[
dV=\frac{d\nu_J}{|J_\xi|}
\]

and

\[
c_J\le|J_\xi|\le C_J,
\]

we have uniform measure equivalence:

\[
\boxed{
c_J\,dV\le d\nu_J\le C_J\,dV.}
\]

Therefore the same exceptional-set conclusion holds in normalized director-flux/arclength measure:

\[
\boxed{
\frac{\nu_J(E_R(R^{-1/4}))}{\nu_J(\mathcal T_R)}
=O(R^{-1/2})\to0.
}
\]

Thus the vanishing-strain statement concerns the actual inherited Rank-2 carrier population, not merely Euclidean volume.

---

## 7. Material law on the overwhelming population

The exact pure-kernel law is

\[
\boxed{
D_B\log|J_\xi|=\sigma_k-1.
}
\]

On the `1-o(1)` population outside the exceptional set,

\[
\boxed{
D_B\log|J_\xi|
=-1+O(R^{-1/4}).
}
\]

Therefore the typical remote compact-ribbon carrier is instantaneously **dilation-decaying** in director-Jacobian density.

This is the population-level version of M17-139, obtained without the pointwise `|grad Sigma|` hypothesis.

---

## 8. Spacetime corridor version

Suppose the critical shell bound

\[
R\int_{C_R}|\nabla U(\theta)|^2dy\le J_*
\]

and the same compact ribbon bounds hold throughout one `O(1)` dyadic crossing interval `I_R` from M17-138.

Integrating in time,

\[
\boxed{
\int_{I_R}\int_{\mathcal T_R(\theta)}|\sigma_k|^2dy\,d\theta
\le
\frac{J_*|I_R|}{R}.
}
\]

Hence the high-strain subset of ribbon spacetime also has vanishing relative measure for any threshold `epsilon_R` with

\[
R\epsilon_R^2\to\infty.
\]

Thus any local recharge mechanism capable of compensating the `-1` similarity-dilation term for a positive fraction of the ribbon population must become increasingly concentrated in ribbon spacetime.

---

## 9. What remains possible

The result does **not** exclude either of the following:

1. each incoming ribbon is already geometrically precharged and simply loses `|J_xi|` as it moves outward;
2. a vanishing-volume / vanishing-flux-arclength subset carries increasingly concentrated strain and acts as a recharge layer.

Therefore the correct split is

\[
\boxed{
R_{2,\rm ribbon}^{remote,compact}
\Longrightarrow
I_{\rm precharged}
\ \lor\
C_{\rm concentrated\ recharge}
\ \lor\
T_{\rm compact/nondegenerate\ exit}.
}
\]

M17-139 sharpens `I_precharged` pointwise when a uniform strain-jet bound is available.

---

## 10. DSD audit

### Audit A — first-hitting analyticity removes the M17-139 remote jet assumption

Rejected.
The existing analyticity statement is uniform on fixed normalized parent balls, not uniformly over annuli whose radius tends to infinity.

### Audit B — small shell `L2` strain can still be order one on most of an order-one ribbon

Rejected.
The director-flux/length nondegeneracy forces a fixed volume floor, so RMS ribbon strain tends to zero.

### Audit C — Euclidean ribbon volume is the wrong carrier measure

Handled.
On the nondegenerate branch, `dV` and `dPhi_J ds` are uniformly equivalent.

### Audit D — population strain decay gives pointwise decay everywhere

Rejected.
A small exceptional set may carry large strain; that is now isolated as the concentrated-recharge branch.

### Audit E — concentrated recharge is already a contradiction

Not established.
Its amplitude, width, derivative cost, pressure cost, and genealogy must be quantified separately.

---

## 11. Updated hard gate

Without any remote pointwise jet hypothesis, the critical fresh-ribbon survivor must be one of

\[
\boxed{
\begin{aligned}
&\text{precharged order-one director geometry imported from smaller radii},\\
&\text{increasingly concentrated strain-recharge layers},\\
&\text{loss of compact/nondegenerate ribbon geometry}.
\end{aligned}
}
\]

The next high-value calculation is a **bounded-shell backward genealogy gate**: if a precharged tube is followed inward while it remains in a compact low-strain corridor, the exact law makes `|J_xi|` grow by approximately a factor `4` per dyadic shell backward. Uniform compact bounds can tolerate only finitely many such crossings. Hence every order-one remote ribbon must encounter a recharge/high-strain layer or a geometry/jet exit within a uniformly bounded number of inward shell steps.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
