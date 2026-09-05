# DSD M17-145 — The `kappa`-gradient fold driver has a weighted diffusion/damping law, but its natural `rho^2` energy misses order-one director flux

Date: 2026-09-05  
Canonical ID: **M17-145**

Status: **MULTIPLIER-GRADIENT MATERIAL LAW / ON THE PURE-TRANSVERSE-KERNEL CE-H BRANCH, `xi` IS MATERIALLY FROZEN AND IS A STRAIN EIGENDIRECTION. THEREFORE FOR EVERY SCALAR `f`, `D_B(D_xi f)=D_xi(D_Bf)-(sigma+1/2)D_xi f`. APPLYING THIS TO `K_xi:=D_xi kappa` AND USING THE EXACT M5-682 CONSTITUTIVE LAW `h=D_B kappa=L_rho kappa+L_rho sigma-kappa+R_geom` GIVES AN EXACT WEIGHTED-DIFFUSION EQUATION `D_B K_xi=L_rho K_xi-(sigma+3/2)K_xi+F_xi`, WHERE `F_xi=L_rho(D_xi sigma)+C_xi[kappa+sigma]+D_xi R_geom` AND `C_xi=[D_xi,L_rho]` IS AN EXPLICIT DIRECTOR/LOG-AMPLITUDE COMMUTATOR. ON A MATERIAL DOMAIN THE NATURAL QUADRATIC ENERGY `E_K=(1/2)int rho^2 K_xi^2` OBEYS `E_K'=-int rho^2|grad K_xi|^2+int (kappa-7/4)rho^2K_xi^2+int rho^2K_xi F_xi+boundary`. THIS EXHIBITS TRUE DIFFUSION AND DAMPING, BUT THE WEIGHT IS `rho^2`. ON THE M17-133/142 LOW-AMPLITUDE STRONG-DIRECTOR SKELETON, `rho^2~R^{-1}` WHILE `dPhi_J` AND `|J_xi|` CAN REMAIN ORDER ONE, SO ORDER-ONE `K_xi` FOLD EVENTS CAN HAVE ONLY `O(R^{-1})` NATURAL WEIGHTED COST PER UNIT DIRECTOR FLUX. THE DYADIC SUM OF SUCH COSTS IS GEOMETRICALLY SUMMABLE. THEREFORE THE NEW PDE LAW IS REAL PROGRESS BUT DOES NOT YET SUPPLY THE POSITIVE DIRECTOR-FLUX-WEIGHTED COST NEEDED TO CLOSE THE FREQUENT-FOLD BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pure-kernel `xi` commutator

On the full-rank pure-transverse-kernel branch, M17-033 gives

\[
\boxed{D_B\xi=0}
\]

and

\[
\boxed{\Sigma\xi=\sigma\xi.}
\]

Because the antisymmetric part of `grad U` rotates about the vorticity direction, it annihilates `xi`. Hence

\[
(\nabla B)\xi
=
\left(\sigma+\frac12\right)\xi.
\]

For every scalar `f`,

\[
\begin{aligned}
D_B(D_\xi f)
&=D_B(\xi\cdot\nabla f)\\
&=(D_B\xi)\cdot\nabla f
+\xi\cdot\left(\nabla D_Bf-(\nabla B)^T\nabla f\right).
\end{aligned}
\]

Therefore

\[
\boxed{
D_B(D_\xi f)
=
D_\xi(D_Bf)
-\left(\sigma+\frac12\right)D_\xi f.
}
\]

The M17-040 peak equation is the special case `f=log rho`.

---

## 2. Define the fold-driver multiplier gradient

Set

\[
\boxed{K_\xi:=D_\xi\kappa.}
\]

M17-144 shows that on the quiet high-jet remote branch the generic fold coefficient is

\[
A_T
=D_\xi(\sigma+\kappa)
=K_\xi+o(1).
\]

Thus a uniformly nondegenerate quiet-remote generic fold requires

\[
|K_\xi|\gtrsim1.
\]

The next task is to determine how `K_xi` itself can be maintained.

---

## 3. M5-682 exact constitutive law for `h=D_B kappa`

M5-682 gives, on the active CE-H set `rho>0`,

\[
\boxed{
h
:=D_B\kappa
=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom},
}
\]

where

\[
\boxed{
L_\rho f
:=
\rho^{-2}\nabla\cdot(\rho^2\nabla f)
=
\Delta f+2\nabla\log\rho\cdot\nabla f,
}
\]

and

\[
\boxed{
\mathcal R_{geom}
=-\frac2\rho\Sigma:\nabla^2\rho
+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+(\nabla\times W)\cdot\nabla\log\rho.
}
\]

This law is compatible with the pure-kernel branch because `xi` is a strain eigendirection there.

---

## 4. Exact commutator with the weighted Laplacian

Write

\[
\psi:=\log\rho.
\]

For any scalar `f`, define

\[
\boxed{
\mathcal C_\xi[f]
:=
D_\xi(L_\rho f)-L_\rho(D_\xi f).
}
\]

A direct coordinate calculation gives

\[
\boxed{
\begin{aligned}
\mathcal C_\xi[f]
={}&
-(\Delta\xi)\cdot\nabla f
-2(\partial_i\xi_j)\partial_{ij}f\\
&+2\left(D_\xi\nabla\psi-D_{\nabla\psi}\xi\right)\cdot\nabla f.
\end{aligned}
}
\]

Thus the failure of `D_xi` to commute with `L_rho` is an explicit normalized geometry term involving

- first/second director jets,
- the log-amplitude gradient,
- first/second derivatives of the scalar being acted upon.

---

## 5. Exact material PDE for `K_xi`

Apply the `xi` commutator of Section 1 to `f=kappa`:

\[
D_BK_\xi
=D_\xi h
-\left(\sigma+\frac12\right)K_\xi.
\]

Use

\[
h=L_\rho(\kappa+\sigma)-\kappa+\mathcal R_{geom}.
\]

Then

\[
\begin{aligned}
D_\xi h
={}&
L_\rho D_\xi(\kappa+\sigma)
+\mathcal C_\xi[\kappa+\sigma]
-K_\xi
+D_\xi\mathcal R_{geom}\\
={}&
L_\rho K_\xi
+L_\rho(D_\xi\sigma)
+\mathcal C_\xi[\kappa+\sigma]
-K_\xi
+D_\xi\mathcal R_{geom}.
\end{aligned}
\]

Therefore

\[
\boxed{
D_BK_\xi
=
L_\rho K_\xi
-\left(\sigma+\frac32\right)K_\xi
+\mathcal F_\xi,
}
\]

where

\[
\boxed{
\mathcal F_\xi
:=
L_\rho(D_\xi\sigma)
+\mathcal C_\xi[\kappa+\sigma]
+D_\xi\mathcal R_{geom}.
}
\]

This is the exact multiplier-gradient evolution law sought after M17-144.

---

## 6. Structural meaning

The fold driver is not arbitrary.
Its homogeneous material dynamics contain

1. weighted diffusion `L_rho K_xi`;
2. linear damping `-(sigma+3/2)K_xi`;
3. explicit recharge `F_xi` from strain derivatives, director/log-amplitude commutators, and CE-H geometric forcing.

On a quiet remote ribbon with `sigma->0`, the bare damping approaches

\[
\boxed{-\frac32K_\xi.}
\]

Thus repeated order-one generic folds require recurrent recharge against a genuine damping mechanism.

However, this is not yet a sign contradiction because `F_xi` has no established sign and contains scale-free director/multiplier geometry.

---

## 7. Natural `rho^2`-weighted quadratic energy

Let `V(theta)` be a smooth material domain transported by `B` and contained in the active set `rho>0`.
Define

\[
\boxed{
E_K(\theta)
:=
\frac12\int_{V(\theta)}\rho^2K_\xi^2\,dy.
}
\]

The CE-H amplitude law is

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\]

so

\[
D_B\rho^2
=2(\sigma+\kappa-1)\rho^2.
\]

Also

\[
\nabla\cdot B=\frac32.
\]

Using the material-domain transport theorem and the equation for `K_xi` gives

\[
\begin{aligned}
\frac{dE_K}{d\theta}
={}&
\int_V\rho^2K_\xi L_\rho K_\xi\,dy\\
&+\int_V\left(\kappa-\frac74\right)\rho^2K_\xi^2\,dy\\
&+\int_V\rho^2K_\xi\mathcal F_\xi\,dy.
\end{aligned}
\]

Integrating the weighted Laplacian by parts,

\[
\int_V\rho^2K_\xi L_\rho K_\xi
=
-\int_V\rho^2|\nabla K_\xi|^2
+\int_{\partial V}\rho^2K_\xi\partial_nK_\xi\,dA.
\]

Hence

\[
\boxed{
\begin{aligned}
\frac{dE_K}{d\theta}
={}&
-\int_V\rho^2|\nabla K_\xi|^2dy\\
&+\int_V\left(\kappa-\frac74\right)\rho^2K_\xi^2dy\\
&+\int_V\rho^2K_\xi\mathcal F_\xi dy\\
&+\int_{\partial V}\rho^2K_\xi\partial_nK_\xi dA.
\end{aligned}
}
\]

On full space with sufficient decay, or on a boundary condition killing the last term, this is an exact dissipative/recharge identity.

---

## 8. The `7/4` coefficient is not yet a sign theorem

M17-134 obtains the long same-carrier mean

\[
\langle\kappa\rangle\to\frac32
\]

under additional endpoint comparability hypotheses.
Formally this places the coefficient

\[
\kappa-\frac74
\]

below zero on average if the same weighting and trajectory were legitimate.

But that shortcut is rejected:

\[
\boxed{
\text{material-time mean of }\kappa
\neq
\text{spatial }\rho^2K_\xi^2\text{-weighted mean of }\kappa.
}
\]

Furthermore `F_xi` and boundary transport can recharge the energy.
Thus no sign contradiction is claimed.

---

## 9. Director-flux disintegration of the new energy

On a nondegenerate pure-kernel ribbon tube, M17-122 gives

\[
\boxed{
dV=\frac{d\Phi_J\,ds}{|J_\xi|}.}
\]

Therefore

\[
\boxed{
E_K
=
\frac12
\int
\left(
\oint
\frac{\rho^2K_\xi^2}{|J_\xi|}
\,ds
\right)
 d\Phi_J.
}
\]

This exposes the exact mismatch between the natural PDE energy and the carrier measure.

The M17-133/142 survivor has schematically

\[
\rho^2\sim R^{-1},
\qquad
|J_\xi|\asymp1,
\qquad
\Phi_J\asymp1,
\]

on fixed-size ribbon geometry.
If a generic fold requires only

\[
|K_\xi|\asymp1,
\]

then its natural energy per unit director flux is only

\[
\boxed{
\oint\frac{\rho^2K_\xi^2}{|J_\xi|}ds
=O(R^{-1}).
}
\]

Thus order-one normalized fold geometry can become quadratically cheap as amplitude vanishes.

---

## 10. Dyadic summability firewall

For remote dyadic radii

\[
R_j\sim2^jR_0,
\]

an `O(R_j^{-1})` per-flux cost satisfies

\[
\boxed{
\sum_{j\ge0}R_j^{-1}<\infty.
}
\]

Therefore infinitely many order-one `K_xi` events at dyadic spacing are not excluded merely by summing the natural `rho^2K_xi^2` energy over the remote tail.

This is the exact analogue of the earlier palinstrophy/low-amplitude firewalls: the normalized geometry can remain order one while every quadratic physical-amplitude cost becomes geometrically summable.

---

## 11. What would actually close the fold branch

A successful obstruction must bridge the positive director-flux measure to the multiplier-gradient law without losing the vanishing `rho^2` factor.

One would need, for example, a statement of the schematic form

\[
\boxed{
\int_{\text{fold block}}
|K_\xi|^p\,d\Phi_Jd\theta
\le
\text{finite global quantity}
}
\]

with a weight not degenerating like `rho^2`, or a full material recurrence theorem showing that `F_xi` cannot repeatedly overcome the `3/2` damping on an order-one flux population.

No such estimate is currently established.

---

## 12. DSD audit

### Audit A — M5-682 can be imported without checking its strain-eigendirection hypothesis

Accepted only on the retained pure-kernel branch because M17-033 explicitly gives `Sigma xi=sigma xi` and `D_B xi=0` there.

### Audit B — the `-3/2` homogeneous damping closes `K_xi`

Rejected.
`L_rho`, `C_xi`, strain-derivative forcing, and `D_xi R_geom` remain.

### Audit C — the `kappa-7/4` energy coefficient is negative because `mean kappa=3/2`

Rejected.
The available mean is not the same weighted spacetime average appearing in the energy identity.

### Audit D — finite `rho^2 K_xi^2` energy controls order-one director-flux fold frequency

Rejected.
The low-amplitude branch loses exactly the factor `rho^2` needed for such control.

### Audit E — dyadic summability proves repeated folds exist

Rejected.
It proves only that the natural quadratic weighted budget does not rule them out.

---

## 13. Updated frontier

The generic quiet-remote fold branch is now reduced to a concrete PDE cocycle:

\[
\boxed{
D_BK_\xi
=
L_\rho K_\xi
-\left(\sigma+\frac32\right)K_\xi
+\mathcal F_\xi.
}
\]

The remaining hard question is no longer whether `D_xi kappa` has dynamics; it does.
The question is whether the recharge term

\[
\boxed{
\mathcal F_\xi
=
L_\rho(D_\xi\sigma)
+\mathcal C_\xi[\kappa+\sigma]
+D_\xi\mathcal R_{geom}
}
\]

can recurrently maintain order-one `K_xi` on asymptotically full order-one director-flux measure while every physical-amplitude quadratic ledger is vanishing/summable.

The next efficient calculation is to evaluate `F_xi` on the quiet low-amplitude pure-kernel hard hull and determine which pieces vanish with strain/amplitude and which scale-free director/`kappa` commutator terms survive.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
