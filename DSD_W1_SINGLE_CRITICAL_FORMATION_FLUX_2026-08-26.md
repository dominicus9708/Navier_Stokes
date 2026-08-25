# DSD W1 Single Critical Scale Current

Date: 2026-08-26

Status: **AUDIT-CORRECTED / CRITICAL SHELL DENSITY, LOG-RADIUS DRIFT, AND THE `R3/6` ENDPOINT RESIDUE ARE ONE SIMILARITY-SCALE CURRENT / THIS IS NOT A PHYSICAL MATERIAL OR ENERGY FLUX / GLOBAL REGULARITY UNPROVED.**

## 1. Critical log-shell density

The invariant endpoint has

\[
M_{crit}>0,
\qquad
\boxed{
\mathscr R_3=
\frac{M_{crit}}{\log2}.
}
\]

`R3` is the cubic mass density per unit logarithmic Leray radius.

---

## 2. Leray log-radius drift

Let

\[
\rho=\log|Y|.
\]

The far leading transport is

\[
\partial_s+rac12\partial_\rho.
\]

Hence

\[
\boxed{
\frac{d\rho}{ds}=\frac12.
}
\]

The associated cubic scale-current is

\[
J_{3,scale}
=
\frac12\mathscr R_3.
\]

Because the `p=3` ledger carries the factor `1/3`, define

\[
\boxed{
\mathfrak J_c
:=
\frac13J_{3,scale}
=
\frac{\mathscr R_3}{6}.
}
\]

This is exactly the endpoint residue already derived independently.

---

## 3. Audit correction: this drift is not physical radial transport

The physical radius corresponding to `(rho,s)` is

\[
r_{phys}
=
\sqrt\tau\,e^\rho
=
e^{-s/2}e^\rho.
\]

Along the scale characteristic,

\[
\frac d{ds}\log r_{phys}
=
-\frac12+rac{d\rho}{ds}
=0.
\]

Therefore

\[
\boxed{
r_{phys}=\text{constant along the Leray log-radius characteristic}.}
\]

The apparent outward motion in `Y` is the zooming coordinate passing a fixed physical radius.

Hence

\[
\boxed{
\text{similarity-scale current}
\neq
\text{material turnover}
\neq
\text{physical radial energy flux}.
}
\]

This restates and strengthens the earlier audit that the similarity-radial `p=3` term cannot be charged directly to material turnover.

---

## 4. What remains true

The numerical identity

\[
\boxed{
\mathfrak J_c
=
\frac{\mathscr R_3}{6}
}
\]

remains exact.

It says that one and the same critical memory is seen as:

\[
\boxed{
\text{log-shell density}
\longleftrightarrow
\text{Leray scale drift}
\longleftrightarrow
\text{endpoint similarity residue}.
}
\]

It does **not** by itself give a causal chain from a finite core to a remote physical shell.

Any such core-to-tail statement needs an additional material, pressure, or prelimit-diagonal bridge.

---

## 5. Relation to prelimit `L3` growth

If a prelimit corridor has an expanding range of physical radii whose Leray representation carries the same critical density, then the number of occupied logarithmic Leray shells can grow like `s/2` and one obtains cubic-mass growth of order

\[
\|U(s)\|_3^3\sim
\frac{\mathscr R_3}{2}s.
\]

However this is a statement about the moving rescaling window, not proof that cubic material is physically emitted outward.

A full prelimit Cesaro growth law still requires the appropriate fixed-`R`/diagonal inheritance hypotheses.

---

## 6. Finite-energy compatibility remains unchanged

For a physical critical shell of radius `r`, Type-I amplitude control gives

\[
\int_{A_r}|u|^2dx
\ge
\frac{r}{A_0}
\int_{A_r}|u|^3dx.
\]

Thus an order-one cubic shell costs only order `r` kinetic energy.

For geometric radii,

\[
\sum_j r_j<\infty.
\]

Therefore the local `1/r` critical memory remains compatible with finite `L2` energy.

This energy calculation concerns shell occupancy and does not convert the similarity current into a physical flux.

---

## 7. Correct DSD interpretation

The current endpoint is

\[
\boxed{
M_{crit}>0
\Longrightarrow
\mathfrak J_c>0
\text{ as a similarity-scale current}.
}
\]

The remaining proof must determine whether the original unforced finite-energy parent can realize this nonzero critical scale current together with the recurrent W1 dynamics.

It is not legitimate to argue that a finite core must continuously *emit* the tail merely from `J_c>0`.

The remaining bridge is still one of:

- actual material/pressure transfer;
- prelimit diagonal inheritance;
- or another scale-critical compatibility identity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
