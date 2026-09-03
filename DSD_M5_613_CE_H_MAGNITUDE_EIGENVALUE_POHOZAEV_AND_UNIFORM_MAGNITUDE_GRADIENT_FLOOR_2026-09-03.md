# DSD M5-613 — CE-H magnitude eigenvalue Pohozaev identity and uniform magnitude-gradient floor

Date: 2026-09-03

Status: **MAGNITUDE-CHANNEL RIGIDITY / THE PARALLEL PART OF `Delta W = kappa W` IS THE SCALAR EQUATION `Delta rho = lambda_mag rho` WITH `lambda_mag=kappa+|nabla xi|^2` / IT OBEYS THE SAME PAIR OF SIGNED RAYLEIGH/POHOZAEV IDENTITIES AS KAPPA BUT WITH MAGNITUDE DIRICHLET ENERGY: `int lambda_mag rho^2=-P_mag` AND `int (y·nabla lambda_mag)rho^2=2P_mag` / A NONZERO WHOLE-SPACE L2 STATE CANNOT HAVE `P_mag=0`, SINCE THEN `rho` IS CONSTANT AND MUST VANISH / COMPACTNESS, TAIL TIGHTNESS, AND THE NONZERO MARK UPGRADE THIS TO A UNIFORM POSITIVE MAGNITUDE-GRADIENT FLOOR / THUS THE M5-588 FLAT-VORTICITY SUBBRANCH IS ELIMINATED INSIDE CE-H AND EVERY CE-H SURVIVOR MUST CARRY A RECURRENT MAGNITUDE-GRADIENT CHANNEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parallel decomposition of the CE-H Laplacian equation

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

The standard decomposition gives

\[
\Delta W
=
\left(\Delta\rho-\rho|\nabla\xi|^2\right)\xi
+
P_\xi^\perp\Delta W.
\]

On CE-H,

\[
P_\xi^\perp\Delta W=0
\]

and

\[
\Delta W=\kappa\rho\xi.
\]

Therefore

\[
\boxed{
\Delta\rho
=
\left(\kappa+|\nabla\xi|^2\right)\rho.
}
\]

Define

\[
\boxed{
\lambda_{mag}
:=
\kappa+|\nabla\xi|^2.
}
\]

Then

\[
\boxed{\Delta\rho=\lambda_{mag}\rho.}
\]

---

## 2. Magnitude Rayleigh identity

Multiply the scalar equation by `rho` and integrate:

\[
\int\lambda_{mag}\rho^2
=
\int\rho\Delta\rho
=-\int|\nabla\rho|^2.
\]

Define

\[
P_{mag}:=\int|\nabla\rho|^2dy.
\]

Hence

\[
\boxed{
\int\lambda_{mag}\rho^2dy
=-P_{mag}<0
}
\]

for every state with `P_mag>0`.

This is also consistent with

\[
\int\kappa\rho^2=-P_{mag}-P_{dir},
\]

because

\[
\lambda_{mag}-\kappa=|\nabla\xi|^2.
\]

---

## 3. Magnitude Pohozaev identity

Pair

\[
\Delta\rho=\lambda_{mag}\rho
\]

with

\[
y\cdot\nabla\rho.
\]

The same finite-ball boundary audit as M5-607 applies. The M5-567--568 terminal tail gives enough decay for the scalar boundary defect to vanish.

Therefore

\[
\boxed{
\int
(y\cdot\nabla\lambda_{mag})\rho^2dy
=
2P_{mag}.
}
\]

Thus

\[
\boxed{
\int\lambda_{mag}\rho^2=-P_{mag},
\qquad
\int(y\cdot\nabla\lambda_{mag})\rho^2=2P_{mag}.
}
\]

The magnitude channel has the same critical degree-`-2` signed structure as the full viscous eigenvalue channel.

---

## 4. Difference from the full-vector Pohozaev identity

M5-607 gives

\[
\int(y\cdot\nabla\kappa)\rho^2
=2(P_{mag}+P_{dir}).
\]

Subtract the magnitude identity:

\[
\int
\rho^2 y\cdot\nabla(|\nabla\xi|^2)
=-2P_{dir}.
\]

This is equivalent to the weighted direction virial of M5-612 after integration by parts.

Hence M5-607, M5-612, and M5-613 form a mutually consistent vector/scalar/directional Pohozaev decomposition.

---

## 5. Nonzero CE-H states have P_mag > 0

Suppose

\[
P_{mag}=0.
\]

Then

\[
\nabla\rho=0
\]

almost everywhere, so `rho` is spatially constant on connected `R3`.

But

\[
\rho=|W|\in L^2(\mathbb R^3).
\]

The only constant in `L2(R3)` is zero.

Thus

\[
\rho\equiv0,
\qquad W\equiv0.
\]

Therefore

\[
\boxed{
W\neq0
\Longrightarrow
P_{mag}>0.
}
\]

This eliminates the globally flat-magnitude possibility on CE-H.

---

## 6. Uniform positive floor on the compact marked component

A quantitative floor follows from compactness and tail tightness.

Suppose there were marked states `W_n` with

\[
P_{mag}(W_n)=\|\nabla|W_n|\|_2^2\to0.
\]

Sobolev gives

\[
\||W_n|\|_6
\le C\|\nabla|W_n|\|_2
\to0.
\]

For any fixed ball `B_R`,

\[
\||W_n|\|_{L^2(B_R)}
\le
|B_R|^{1/3}\||W_n|\|_6
\to0.
\]

Uniform enstrophy tightness makes the `L2` mass outside `B_R` uniformly small for large `R`.

Therefore

\[
\|W_n\|_2\to0.
\]

This contradicts the fixed nonzero persistent carrier mark.

Hence there exists

\[
p_{mag,*}>0
\]

such that

\[
\boxed{
P_{mag}\ge p_{mag,*}>0
}
\]

throughout the compact marked CE-H component.

---

## 7. Consequence for M5-588

M5-588 had the finite-depth alternatives

\[
P_{mag,*}>0,
\qquad
P_{dir,*}>0,
\qquad
\text{or a flat-vorticity shell subbranch}.
\]

Inside global CE-H, the magnitude channel cannot vanish globally and has a uniform invariant floor.

Therefore the genuinely surviving CE-H system always carries recurrent magnitude variation.

The directional channel may additionally be nonzero, but it is no longer the only derivative charge available.

---

## 8. Updated scalar critical landscape

The CE-H hard core now contains two scalar degree-`-2` fields:

\[
\kappa,
\qquad
\lambda_{mag}=\kappa+|\nabla\xi|^2,
\]

with

\[
\int\kappa\rho^2=-(P_{mag}+P_{dir}),
\]

\[
\int\lambda_{mag}\rho^2=-P_{mag},
\]

and corresponding positive radial Pohozaev drifts.

Their difference is precisely the nonnegative directional-gradient density.

This scalar pair may be more suitable for the final measure comparison than `kappa` alone.

---

## 9. Firewall

A uniform positive `P_mag` floor is still an unsigned scale-invariant charge. M5-598 showed that such charges alone do not yield an energy contradiction across geometric physical scales.

The new value is that the flat CE-H escape is removed and the magnitude channel has its own exact signed eigenvalue/Pohozaev structure.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
