# DSD M17-313 — Divergence-free CE-H forces `D_xi kappa=0` and retracts the longitudinal `kappa` fold-recharge branch

Date: 2026-09-07  
Canonical ID: **M17-313**

Status: **MAJOR CE-H DIFFERENTIAL-COMPATIBILITY CORRECTION / THE CANONICAL CE-H RELATION IS `Delta W=kappa W` WITH `W` THE DIVERGENCE-FREE VORTICITY. TAKING DIVERGENCE GIVES `0=div(Delta W)=div(kappa W)=W dot grad kappa`, SO ON EVERY ACTIVE REGULAR COMPONENT `D_xi kappa=0` EXACTLY. THIS CONSTRAINT WAS NOT INSERTED INTO THE EARLIER M17-144--147 LONGITUDINAL KAPPA-GRADIENT FOLD PROGRAM. CONSEQUENTLY `K_xi:=D_xi kappa` IS IDENTICALLY ZERO, NOT AN ORDER-ONE FOLD DRIVER. M17-143'S EXACT GENERIC-FOLD COEFFICIENT REDUCES TO `A_T=D_xi sigma`; UNDER THE QUIET HIGH-STRAIN-JET DECAY ALREADY PROVED CONDITIONALLY IN M17-144, `A_T->0`, SO A UNIFORMLY NONDEGENERATE GENERIC FOLD CANNOT SERVICE THE QUIET REMOTE BRANCH. M17-145'S FORMAL EVOLUTION LAW FOR `K_xi` SURVIVES ONLY AS THE COMPATIBILITY IDENTITY `F_xi=0`; M17-146'S ORDER-ONE COMMUTATOR RECHARGE IS THEREFORE NOT FREE BUT MUST CANCEL THE OTHER TERMS, AND ON ITS QUIET LIMIT `C_xi[kappa]=o(1)`. FULL TRANSVERSE `grad kappa` CHANNELS SUCH AS M5-687 AND M17-234/235 ARE NOT RETRACTED: THEY ARE SHARPENED TO `grad kappa perpendicular W`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H and vorticity incompressibility

On the active regular CE-H branch,

\[
\boxed{
\Delta W=\kappa W,
}
\]

where `W` is the similarity vorticity.

Because vorticity is divergence free,

\[
\boxed{
\nabla\cdot W=0.
}
\]

The Euclidean Laplacian commutes with divergence, hence

\[
\boxed{
\nabla\cdot\Delta W
=
\Delta(\nabla\cdot W)
=0.
}
\]

Take divergence of the CE-H relation:

\[
0
=
\nabla\cdot(\kappa W)
=
\nabla\kappa\cdot W
+
\kappa\nabla\cdot W.
\]

Therefore

\[
\boxed{
W\cdot\nabla\kappa=0.
}
\]

Write

\[
W=\rho\xi,
\qquad
\rho=|W|.
\]

On the active set `rho>0`,

\[
\boxed{
D_\xi\kappa
:=
\xi\cdot\nabla\kappa
=0.
}
\]

This is an exact differential compatibility condition of CE-H.

---

## 2. Geometric meaning

The coefficient gradient is purely transverse to the vorticity direction:

\[
\boxed{
\nabla\kappa
\perp
W
\qquad(\rho>0).
}
\]

Thus `kappa` is constant along every connected regular vortex-line segment at a fixed time.

This does **not** imply

\[
\nabla\kappa=0.
\]

Transverse coefficient variation remains fully possible.

Therefore the following full-gradient channels remain meaningful:

- M5-687 division-free `kappa`-gradient polynomial;
- M17-233/234 critical coefficient/gradient return;
- M17-235 weighted full multiplier-gradient diffusion;
- transverse/oblique coefficient-gradient modules.

They must simply respect the new orthogonality condition.

---

## 3. Correction to the M17-143 generic fold coefficient

M17-143 correctly derives the generic fold time-unfolding coefficient

\[
\boxed{
A_T
=D_\xi(\sigma+\kappa).
}
\]

Insert the exact CE-H compatibility:

\[
D_\xi\kappa=0.
\]

Then

\[
\boxed{
A_T
=D_\xi\sigma.
}
\]

Hence the generic fold is driven only by longitudinal strain variation, not by a longitudinal `kappa` gradient.

This corrects the interpretation, not the normal-form derivation, of M17-143.

---

## 4. Quiet high-jet consequence

M17-144 conditionally proves on the quiet remote shell, under its stated finite strain-jet compactness,

\[
\boxed{
D_\xi\sigma
=O(R^{-1/7}).
}
\]

Therefore

\[
\boxed{
A_T
=O(R^{-1/7})
\to0.
}
\]

Consequently a branch satisfying a uniform generic-fold nondegeneracy

\[
\boxed{
|A_T|\ge a_0>0
}
\]

for arbitrarily large remote `R` is impossible under the quiet high-jet CE-H assumptions.

Thus the earlier M17-144 implication

\[
|A_T|\gtrsim1
\Rightarrow
|D_\xi\kappa|\gtrsim1
\]

is superseded.

The correct conclusion is

\[
\boxed{
\text{quiet high-jet remote CE-H}
\Longrightarrow
A_T\to0.
}
\]

---

## 5. What frequent fold/type turnover can still do

M17-142's frequent geometry-transition conclusion is not automatically erased.

It is instead sharpened.

On the quiet high-jet branch, repeated transitions cannot be serviced by a uniformly nondegenerate generic fold.

They must route to at least one of

\[
\boxed{
\begin{aligned}
& G_{fold\ degeneracy}: A_T\to0,\\
& G_{higher\ tangency}: C_k\to0\text{ or higher jet controls the event},\\
& G_{high\ strain\ jet}: \text{the M17-144 jet compactness fails},\\
& G_{rank/end/interface},\\
& G_{nonquiet\ critical\ spacetime}.
\end{aligned}
}
\]

Thus one formerly open order-one fold-recharge lane is removed.

---

## 6. Correction to M17-145

M17-145 defines

\[
\boxed{
K_\xi:=D_\xi\kappa
}
\]

and derives the formal active-set equation

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
\mathcal F_\xi
=
L_\rho(D_\xi\sigma)
+\mathcal C_\xi[\kappa+\sigma]
+D_\xi\mathcal R_{geom}.
\]

But CE-H compatibility gives

\[
\boxed{K_\xi\equiv0.}
\]

Therefore the equation is not an evolution equation for a nontrivial fold driver.

It reduces identically to the compatibility constraint

\[
\boxed{
\mathcal F_\xi\equiv0.
}
\]

Thus the `rho^2 K_xi^2` energy and its proposed nonzero fold-driver interpretation are vacuous on exact CE-H.

---

## 7. Correction to M17-146

M17-146 conditionally reduces the forcing on its quiet low-amplitude hard hull to

\[
\mathcal F_\xi
=
\mathcal C_\xi[\kappa]
+o(1).
\]

M17-313 supplies the previously missing exact input

\[
\mathcal F_\xi=0.
\]

Hence under the same M17-146 quiet compactness assumptions,

\[
\boxed{
\mathcal C_\xi[\kappa]
=o(1).
}
\]

Therefore the M17-146 claim that `C_xi[kappa]` may survive as an order-one longitudinal recharge mechanism is superseded.

Instead it is a **compatibility cancellation condition** forced by divergence-free CE-H.

---

## 8. Material derivative of line constancy

M17-145 also records the exact scalar commutator

\[
D_B(D_\xi f)
=
D_\xi(D_Bf)
-\left(\sigma+\frac12\right)D_\xi f.
\]

Set

\[
f=\kappa,
\qquad
h:=D_B\kappa.
\]

Since

\[
D_\xi\kappa=0,
\]

we get

\[
0
=
D_\xi h.
\]

Thus

\[
\boxed{
D_\xi(D_B\kappa)=0.
}
\]

Both `kappa` and its material velocity `h` are constant along connected regular vortex lines at a fixed time.

This fact is important for the M5-681 material `kappa`-space conveyor and will be used in the next bridge.

---

## 9. Scope of downstream retraction

The following conclusions are superseded wherever they require a nonzero longitudinal coefficient gradient:

\[
\boxed{
D_\xi\kappa\ne0
}
\]

as an exact CE-H mechanism.

In particular:

1. M17-144's order-one `D_xi kappa` generic-fold recharge;
2. M17-145's nonzero `K_xi` fold-driver energy interpretation;
3. M17-146's order-one longitudinal commutator recharge interpretation;
4. downstream arguments whose only entry is a nonzero `K_xi`.

The following are **not** retracted:

1. M17-143's generic fold normal form and the identity `A_T=D_xi(sigma+kappa)`;
2. full transverse `grad kappa` channels;
3. M5-687's nonzero full-gradient polynomial charge;
4. M17-234/235 full-gradient coefficient return;
5. nodal/interface branches.

They are corrected by imposing

\[
\boxed{\nabla\kappa\cdot\xi=0.}
\]

---

## 10. Updated quiet-fold frontier

The corrected CE-H transition gate is

\[
\boxed{
\begin{aligned}
G_{frequent}^{quiet\ CEH}
\Longrightarrow{}&
G_{degenerate\ fold/higher\ tangency}\\
&\lor G_{high\ strain\ jet}\\
&\lor G_{transverse\ coefficient\ geometry}\\
&\lor G_{rank/end/interface}\\
&\lor G_{nonquiet\ spacetime}.
\end{aligned}
}
\]

The old longitudinal `kappa` fold-recharge branch is removed.

---

## 11. DSD audit

- The new identity uses only `div W=0`, commutation of divergence with Laplacian, and exact CE-H.
- No division by `rho` is used until restricting to the active set.
- Full `grad kappa` is not set to zero; only its vorticity-direction component vanishes.
- M17-143's normal form is retained and only its later interpretation is corrected.
- M17-145 is repurposed as a compatibility identity rather than discarded algebraically.
- The correction strengthens rather than weakens the separation between longitudinal folds and transverse coefficient geometry.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
