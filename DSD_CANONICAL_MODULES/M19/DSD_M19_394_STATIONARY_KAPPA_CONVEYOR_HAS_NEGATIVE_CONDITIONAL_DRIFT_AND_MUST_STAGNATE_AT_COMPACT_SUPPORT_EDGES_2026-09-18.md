# M19-394 — The stationary kappa conveyor has negative conditional drift and must stagnate at compact support edges

Date: 2026-09-18

Status: **NEW STATIONARY ENDPOINT STRUCTURE / M19-391 GIVES `Gbar(k)<0` THROUGH EVERY ACTIVE INTERIOR KAPPA LEVEL. DISINTEGRATING THE CURRENT DEFINES THE FLUX-WEIGHTED CONDITIONAL MEAN MATERIAL VELOCITY `hbar_Phi(k)=Gbar/Fbar<0`. WRITING `v(k)=-hbar_Phi(k)>0`, THE STATIONARY EQUATION BECOMES THE EXACT ODE `J'/J=-k/v` ON THE POSITIVE HALF, WHERE `J=-Gbar`. IF THE ACTIVE CURRENT TERMINATES AT A FINITE COMPACT SUPPORT EDGE `K_+`, THEN `int^K+ k/v(k) dk=+infinity`; IN PARTICULAR `v` CANNOT STAY BOUNDED BELOW AND MUST STAGNATE TOWARD ZERO (OR THE DISINTEGRATION MUST DEGENERATE). THE SAME HOLDS AT THE NEGATIVE EDGE. THUS A COMPACT RECURRENT CE-H CONVEYOR REQUIRES COEFFICIENT-VELOCITY STAGNATION AT BOTH EXTREME KAPPA EDGES. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Conditional mean material velocity

On every regular level with

\[
\overline F(k)>0,
\]

define

\[
\boxed{
\overline h_\Phi(k)
:=
\frac{\overline G(k)}{\overline F(k)}.
}
\]

This is the current-flux weighted conditional mean of

\[
h=D_B\kappa
\]

on the level \(\kappa=k\).

M19-391 gives

\[
\overline G(k)<0
\]

at every active interior level of the nontrivial conveyor. Hence

\[
\boxed{
\overline h_\Phi(k)<0.
}
\]

The recurrent current therefore has a strictly downward **conditional mean coefficient drift** throughout its active support, even though individual material labels may move both upward and downward.

---

## 2. Positive half-space current ODE

For \(0<k<K_+\), define

\[
\boxed{
J(k):=-\overline G(k)>0
}
\]

and

\[
\boxed{
v(k):=-\overline h_\Phi(k)>0.
}
\]

Since

\[
J=v\overline F,
\]

the stationary M5-681 equation

\[
\partial_k\overline G=k\overline F
\]

becomes

\[
-J'(k)
=
k\frac{J(k)}{v(k)}.
\]

Therefore

\[
\boxed{
\frac{J'(k)}{J(k)}
=
-\frac{k}{v(k)}.
}
\]

For any \(0<k_0<k<K_+\),

\[
\boxed{
J(k)
=
J(k_0)
\exp\left[
-\int_{k_0}^{k}
\frac{s}{v(s)}ds
\right].
}
\]

---

## 3. Finite positive support edge forces stagnation

Let

\[
K_+
:=
\sup\{k>0:\overline F\text{ is active near }k\}<\infty.
\]

The compact-support/no-through-boundary condition requires

\[
\lim_{k\uparrow K_+}J(k)=0.
\]

From the representation in Section 2 this is possible only if

\[
\boxed{
\int_{k_0}^{K_+}
\frac{s}{v(s)}ds
=
+\infty.
}
\]

Since \(s\ge k_0>0\),

\[
\boxed{
\int_{k_0}^{K_+}
\frac{ds}{v(s)}
=
+\infty.
}
\]

Consequently \(v\) cannot satisfy

\[
v(k)\ge v_*>0
\]

all the way to the finite edge.

Thus, on every regular absolutely-continuous endpoint corridor,

\[
\boxed{
\liminf_{k\uparrow K_+}v(k)=0.
}
\]

Equivalently,

\[
\boxed{
\limsup_{k\uparrow K_+}
\overline h_\Phi(k)=0
}
\]

from below.

The conditional downward drift must stagnate near the maximal recurrent coefficient.

---

## 4. Negative support edge

Let

\[
K_-<0
\]

be the lower active support edge.

Again put

\[
J(k):=-\overline G(k)>0,
\qquad
v(k):=-\overline h_\Phi(k)>0.
\]

For \(K_-<k<0\),

\[
J'(k)
=
-k\overline F(k)
=
\frac{|k|}{v(k)}J(k).
\]

Hence for \(K_-<k<k_0<0\),

\[
J(k_0)
=
J(k)
\exp\left[
\int_k^{k_0}
\frac{|s|}{v(s)}ds
\right].
\]

The boundary condition

\[
J(K_-)=0
\]

at finite \(K_-\) requires

\[
\boxed{
\int_{K_-}^{k_0}
\frac{|s|}{v(s)}ds
=
+\infty,
}
\]

and therefore

\[
\boxed{
\liminf_{k\downarrow K_-}v(k)=0
}
\]

on a regular endpoint corridor.

Thus both coefficient extremes are conditional-drift stagnation boundaries.

---

## 5. Relation to the compact h bound

M19-392 uses

\[
|h|\le H_*.
\]

Therefore

\[
0<v(k)\le H_*.
\]

The new result is not the upper bound; it is the required **loss of any positive lower bound** near the compact coefficient edges.

If for some endpoint neighborhood

\[
v(k)\ge v_*>0,
\]

then

\[
\int\frac{dk}{v(k)}<\infty
\]

over the finite interval, and the stationary current could not decay to zero at that edge.

Hence the branch

\[
\boxed{
\text{compact coefficient support}
+
\text{uniformly nonzero conditional drift at the edge}
}
\]

is excluded.

---

## 6. PDE interpretation at the upper edge

M5-682 gives

\[
h
=
\mathcal F_{CEH}-\kappa,
\]

where

\[
\mathcal F_{CEH}
=
L_\rho\kappa
+
L_\rho\sigma
+
\mathcal R_{geom}.
\]

The positive support edge therefore requires conditional balance

\[
\boxed{
\mathbb E_\Phi[
\mathcal F_{CEH}-\kappa
\mid
\kappa=k
]
\to0
}
\]

along an endpoint sequence \(k\uparrow K_+\).

Equivalently,

\[
\boxed{
\mathbb E_\Phi[
\mathcal F_{CEH}
\mid
\kappa=k
]
\to K_+
}
\]

along such a sequence, provided the conditional disintegration remains regular.

At the negative edge,

\[
\boxed{
\mathbb E_\Phi[
\mathcal F_{CEH}
\mid
\kappa=k
]
\to K_-.
}
\]

Thus the compact stationary conveyor requires the spatial CE-H forcing to asymptotically balance the linear relaxation exactly at both extreme coefficient phases.

---

## 7. Endpoint alternatives / firewall

The stagnation conclusion is stated on a regular conditional-density corridor.

If the conditional disintegration fails near an endpoint, the alternative is not ignored. It is recorded as

\[
\boxed{
G_{endpoint}^{singular/disintegration},
}
\]

which includes atoms, collapsing level measure, sheet termination, nodal/interface loss, or representation degeneration.

Therefore the endpoint split is

\[
\boxed{
\text{regular drift stagnation}
\lor
G_{endpoint}^{singular/disintegration}.
}
\]

---

## 8. Why this matters

The abstract periodic witness M19-388 can recycle bounded hysteresis, but a genuine compact-support stationary coefficient conveyor must now satisfy an additional endpoint condition not encoded by an arbitrary finite-state phase graph:

\[
\boxed{
\overline h_\Phi(k)\to0
\quad
\text{near both extreme kappa phases}.
}
\]

The next high-value calculation is to test whether the CE-H constitutive law can realize this two-sided stagnation while simultaneously maintaining

\[
D_\kappa\ge d_\kappa>0
\]

and the fixed deep current/action of M19-391--393.

A failure would close the regular endpoint branch; success would identify the exact extremal payer geometry.

---

\[
\boxed{\text{M19-394 COMPLETE; COMPACT STATIONARY KAPPA TRANSPORT REQUIRES TWO-SIDED CONDITIONAL-DRIFT STAGNATION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
