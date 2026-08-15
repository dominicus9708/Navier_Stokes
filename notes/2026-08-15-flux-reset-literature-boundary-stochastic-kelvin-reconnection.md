# Flux-reset endgame: literature boundary from stochastic Kelvin theory and smooth vortex reconnection

Date: 2026-08-15

Status: **LITERATURE BOUNDARY AUDIT / TOPOLOGICAL NONRECONNECTION ROUTE REJECTED / QUANTITATIVE FLUX RESET REMAINS.**

The final proof route has been reduced to repeated material-vorticity-flux reset plus critical strain / derivative replenishment.

Before attempting to assign a universal cost to each reset, it is necessary to separate two very different statements:

1. topology of vortex lines/tubes changes;
2. a quantitatively large signed circulation/vorticity flux is rebuilt across shrinking first-hitting scales.

The literature rules out using the first statement alone as a regularity obstruction.

---

## 1. Smooth Navier--Stokes can reconnect vortex structures

Enciso, Lucà and Peralta-Salas constructed smooth high-frequency solutions of the three-dimensional Navier--Stokes equations in which vortex lines and vortex tubes of arbitrarily complicated topology are created and destroyed in arbitrarily small times.

Primary reference:

- A. Enciso, R. Lucà, D. Peralta-Salas, *Vortex reconnection in the three dimensional Navier--Stokes equations*, Adv. Math. 309 (2017), 452--486; arXiv:1606.06176.

Therefore one must not claim

\[
\boxed{
\text{vortex reconnection}
\Longrightarrow
\text{loss of smoothness or a universal positive time cost}.
}
\]

A purely topological `number of reconnections` budget cannot close the current proof route.

---

## 2. Viscous Navier--Stokes retains stochastic Lagrangian conservation laws

Constantin and Iyer derived a stochastic Lagrangian representation of the three-dimensional incompressible Navier--Stokes equations.

Primary reference:

- P. Constantin, G. Iyer, *A stochastic Lagrangian representation of the three-dimensional incompressible Navier--Stokes equations*, Comm. Pure Appl. Math. 61 (2008), 330--345.

Related stochastic Kelvin formulations show that deterministic viscous circulation is naturally represented through an ensemble of stochastic backward material loops rather than through deterministic Kelvin conservation on one material loop.

This is consistent with the current deterministic material-flux identity

\[
\frac d{dt}\Phi_S
=-\nu\oint_{\partial S(t)}(\nabla\times\omega)\cdot d\ell:
\]

viscosity permits deterministic material flux change, while a generalized conservation principle survives only after stochasticization / averaging.

---

## 3. Consequence for the present proof search

The final obstruction cannot be phrased as

\[
\boxed{
\text{`reconnection cannot happen infinitely often'}
}
\]

without a new quantitative theorem.

The literature demonstrates that reconnection events themselves are compatible with smooth Navier--Stokes dynamics and can occur on very short time scales.

The repository must instead retain the stronger quantitative data of the first-hitting coherent crossing:

\[
|\bar\Omega|\sim1,
\qquad
BR^4=1,
\qquad
R\to\infty,
\qquad
\Phi_R\sim R^2.
\]

Thus the true target is

\[
\boxed{
\text{repeated rebuilding of an increasingly large scale-invariant signed flux}
}
\]

rather than vortex-line topology by itself.

---

## 4. Compatibility with the new smooth reset-cost lemma

The smooth material-flux reset lemma assigns, under bounded probe distortion,

\[
\nu\int_I\|\omega\|_2^2dt
\gtrsim
\frac{R^5}{\sqrt W}
=
q_0^{-1/2},
\qquad
q_0=W/R^{10}.
\]

This is a quantitative amplitude/scale statement. It does not count topology changes and is therefore not contradicted by the smooth reconnection constructions.

The Enciso--Lucà--Peralta-Salas examples instead warn that one should expect a possible Zeno-style sequence of geometrical reconnections unless the **flux magnitude, scale separation, and material-probe distortion** are all retained in the estimate.

---

## 5. Current admissible final branch

After the literature audit, the honest final dichotomy remains

\[
\boxed{
\text{super-separated quantitative flux-reset Zeno}
\quad\lor\quad
\text{material-probe strain/derivative collapse}.
}
\]

No known theorem from stochastic Kelvin theory or smooth vortex-reconnection theory directly excludes this quantitative infinite sequence.

This is a useful negative result: it prevents the proof search from replacing the remaining analytic problem by an invalid topological nonreconnection assumption.

Status: **TOPOLOGICAL SHORTCUT EXCLUDED / QUANTITATIVE FLUX-RESET PROBLEM CONFIRMED AS THE CORRECT ENDGAME.**