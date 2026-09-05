# DSD M17-155 — Relative-thick remote ribbon packets have an amplitude-normalized Ornstein–Uhlenbeck limit

Date: 2026-09-05  
Canonical ID: **M17-155**

Status: **LOW-AMPLITUDE PACKET COMPACTNESS GATE / THE INFINITE NORMALIZED-JET LADDER OF M17-154 SHOULD NOT BE CONTINUED DERIVATIVE BY DERIVATIVE. ON THE BOUNDED-`kappa`, QUIET REMOTE RIBBON BRANCH, A PACKET POINT WHOSE AMPLITUDE IS COMPARABLE TO THE LOCAL RIBBON `L2` MASS HAS UNIFORM AMPLITUDE-NORMALIZED LOCAL BOUNDS BY THE ELLIPTIC EQUATION `Delta W=kappa W`. AFTER TRANSLATING BY A MATERIAL CENTER AND DIVIDING BY THAT SMALL AMPLITUDE, REMOTE TYPE-I VELOCITY VANISHES AND THE QUIET SPACETIME STRAIN BUDGET KILLS THE STRETCHING TERM. EVERY LOCALLY COMPACT SUBSEQUENCE THEREFORE LIMITS TO THE LINEAR ORNSTEIN–UHLENBECK VORTICITY EQUATION `V_tau + (z/2)·grad V = Delta V - V`. FAILURE OF THE REQUIRED RELATIVE-THICKNESS / BOUNDED-FLUX-VOLUME HYPOTHESIS IS AN EXPLICIT THIN/NODAL/MULTIPLICITY EXIT RATHER THAN A GENERIC HIGH-JET ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why the whole-jet route must be reorganized

M17-154 shows that repeated differentiation produces the ladder

\[
\nabla^m\kappa
\longleftrightarrow
\nabla^{m+1}\log\rho.
\]

M5-155 supplies a uniform analytic scale only with Cauchy radius loss. It does not justify same-radius derivative estimates. More importantly, absolute analyticity of `W` does not by itself control derivatives of `log rho` when `rho -> 0`.

Therefore the correct split is not

\[
\text{bounded fixed jet}\quad\lor\quad\text{differentiate once more},
\]

but

\[
\boxed{
\text{relative-thick low-amplitude packet}
\quad\lor\quad
\text{relative-thin / nodal / multiplicity packet}.
}
\]

---

## 2. Remote shell and ribbon packet

Let `C_R` be a fixed-shape enlarged remote shell and define

\[
E_R:=\int_{C_R}|W|^2dy.
\]

On the quiet critical branch,

\[
R E_R\le J_*.
\]

Assume a compact nondegenerate ribbon packet `T_R` carries a fixed fraction

\[
\int_{T_R}|W|^2dy\ge\vartheta E_R,
\qquad \vartheta>0.
\]

Retain the compact geometric bounds needed to keep its similarity volume bounded above and below; for example

\[
0<c_J\le |J_\xi|\le C_J,
\]

bounded complete-fiber length, and a bounded total packet flux

\[
0<\Phi_*\le\Phi_R\le\Phi^*<\infty.
\]

Then

\[
0<V_*\le |T_R|\le V^*<\infty.
\]

Hence there exists `p_R in T_R` with

\[
\boxed{
|W(p_R)|^2\ge c_* E_R.
}
\]

Write

\[
a_R:=|W(p_R)|.
\]

Since `E_R <= J_*/R`, we have

\[
\boxed{a_R\to0.}
\]

---

## 3. Relative-thickness from the scalar CE-H elliptic equation

Assume on every fixed-size neighborhood of the selected packet, uniformly along the finite time corridor under consideration,

\[
\boxed{\|\kappa\|_\infty\le K_0.}
\]

Because

\[
\Delta W=\kappa W,
\]

standard interior elliptic estimates give, for every fixed `L<infty`,

\[
\sup_{B_L(p_R)}|W|^2
\le C(L,K_0)\int_{B_{L+1}(p_R)}|W|^2dy
\le C(L,K_0)E_R.
\]

Using `a_R^2 >= c_*E_R`,

\[
\boxed{
\sup_{B_L(p_R)}\frac{|W|}{a_R}
\le C_L.
}
\]

Thus the low amplitude itself disappears from the local normalized profile.

This is the **relative-thick** branch.

If no packet point with `a_R^2 >= c_*E_R` exists because packet volume/flux multiplicity decompactifies, or if the bounded-potential elliptic estimate fails, retain the explicit exits

\[
\boxed{
G_{thin/nodal/multiplicity}
\ \lor\ 
G_{\kappa,\infty}.
}
\]

---

## 4. Move with a material center

Let `p_R(theta)` be the material trajectory through the selected point:

\[
\dot p_R=B(p_R,\theta),
\qquad
B=U+\frac12y.
\]

For a sequence `R_j -> infinity`, set the observation time to `theta_j` and define

\[
\boxed{
V_j(z,\tau)
:=
\frac{W(p_j(\theta_j+\tau)+z,\theta_j+\tau)}{a_j},
}
\]

where

\[
a_j=|W(p_j(\theta_j),\theta_j)|.
\]

Then

\[
|V_j(0,0)|=1.
\]

The translated drift is

\[
B(p_j+z)-B(p_j)
=
\frac12 z+[U(p_j+z)-U(p_j)].
\]

---

## 5. Remote Type-I velocity disappears

The retained ancient/first-hitting tail has

\[
|U(y,\theta)|\le \frac{A_0}{1+|y|}
\]

on the remote branch.

For every fixed `T,L`, the material center remains at radius comparable to `R_j` on `|tau|<=T`. Hence

\[
\boxed{
\sup_{|\tau|\le T,|z|\le L}
|U(p_j(\tau)+z,\tau)|
\to0.
}
\]

Therefore

\[
U(p_j+z)-U(p_j)\to0
\]

uniformly on fixed translated cylinders.

---

## 6. Quiet strain removes the nonlinear stretching term

Assume the quiet critical spacetime shell bound of M17-142 on every fixed translated time window:

\[
\int_{-T}^{T}\int_{C_{R_j(\tau)}}|\Sigma|^2dy\,d\tau
\le \frac{C_T}{R_j}.
\]

Then on every fixed translated cylinder,

\[
\boxed{
\Sigma_j\to0
\quad\text{in }L^2_{loc}(dz\,d\tau).
}
\]

The antisymmetric part of `grad U` annihilates the vorticity vector, so the stretching term is exactly `Sigma W`.

Since `V_j` is locally bounded on the relative-thick branch,

\[
\Sigma_jV_j\to0
\]

in local distributions.

---

## 7. Limit equation

The similarity vorticity equation is

\[
D_BW
=
\Delta W+\Sigma W-W.
\]

In the translated variables,

\[
\partial_\tau V_j
+
\left[
\frac12z+U(p_j+z)-U(p_j)
\right]\cdot\nabla V_j
=
\Delta V_j+\Sigma_jV_j-V_j.
\]

The bounded-potential elliptic equation gives local `W^{2,p}` control after normalization; together with the equation this yields the compactness needed to pass to a subsequence on every fixed spacetime cylinder.

Thus every relative-thick quiet subsequential limit satisfies

\[
\boxed{
\partial_\tau V
+
\frac12z\cdot\nabla V
=
\Delta V-V
}
\]

distributionally, and hence smoothly by linear parabolic regularity.

Also

\[
\boxed{\nabla\cdot V=0,}
\]

and

\[
\boxed{|V(0,0)|=1.}
\]

So the limit is nonzero.

---

## 8. What has been gained

The low-amplitude strong-director packet no longer needs an infinite finite-jet audit on this branch.

Instead the entire normalized local packet is governed in the limit by one linear equation:

\[
\boxed{
\mathcal L_{OU}V
:=
\Delta V-rac12z\cdot\nabla V-V.
}
\]

The only remaining issue is the global-in-`z` / global-in-`tau` mass envelope of the normalized packet.

That is the next gate.

---

## 9. DSD audit

1. Absolute analyticity was **not** converted into an amplitude-relative derivative bound without a local mass comparison.
2. The bounded-potential assumption is explicit.
3. The ribbon volume/flux upper bound is explicit; failure is a multiplicity/decompactification exit.
4. The strain term is removed by the spacetime `L2` quiet ledger, not by an unsupported pointwise strain bound.
5. No long same-material ribbon recurrence is assumed.
6. The limit is a local packet limit; an eternal global `L2` limit requires an additional mass-envelope hypothesis.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
