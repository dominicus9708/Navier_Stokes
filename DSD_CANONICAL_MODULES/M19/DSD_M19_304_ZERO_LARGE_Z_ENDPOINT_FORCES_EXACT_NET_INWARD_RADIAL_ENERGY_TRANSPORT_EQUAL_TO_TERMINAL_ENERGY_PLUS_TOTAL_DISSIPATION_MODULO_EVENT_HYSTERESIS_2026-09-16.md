# M19-304 — Zero large-z endpoint forces exact net inward radial energy transport equal to terminal energy plus total dissipation, modulo event hysteresis

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE CALCULATION / GLOBAL RADIAL-CURRENT INTEGRAL LAW / SIGNED-RADIAL ROUTE CLASSIFIED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Conditioned combined-potential law

M19-300/302 give

\[
\boxed{
\mathscr K_m'(z)
=
\mathscr D_m(z)+\mathscr J_m(z)+\mathscr B_m(z),
}
\]

where

\[
\mathscr K_m(z)
:=
\mathscr E_m(z)+2z\mathscr J_m(z).
\]

M19-303 certifies

\[
\mathscr E_m(z)\to0,
\qquad
z\mathscr J_m(z)\to0
\]

as `z->infinity`.

Therefore

\[
\boxed{
\mathscr K_m(\infty)=0.
}
\]

At the terminal boundary,

\[
\boxed{
\mathscr K_m(0)=\mathscr E_m(0),
}
\]

because the factor `2z` kills the radial-current term.

## 2. Exact integrated conditioned balance

Integrate from zero to infinity. M19-303 gives the required large-z integrability.

Then

\[
0-\mathscr E_m(0)
=
\int_0^\infty
\left(
\mathscr D_m+
\mathscr J_m+
\mathscr B_m
\right)dz.
\]

Hence

\[
\boxed{
-\int_0^\infty
\left(
\mathscr J_m(z)+\mathscr B_m(z)
\right)dz
=
\mathscr E_m(0)
+
\int_0^\infty\mathscr D_m(z)dz.
}
\]

The right side is nonnegative and is strictly positive whenever the production-conditioned terminal energy or conditioned dissipation is nonzero.

Thus conditioned radial current plus event hysteresis must have a quantitatively negative total depth integral.

## 3. Unconditioned exact inward-current theorem

Set the marker identically equal to one:

\[
m_h\equiv1.
\]

Then

\[
\mathscr B_m=0,
\]

and the identity becomes

\[
\boxed{
\int_0^\infty\mathscr J(z)dz
=
-\mathscr E(0)
-\int_0^\infty\mathscr D(z)dz.
}
\]

For every nontrivial terminal tail,

\[
\mathscr E(0)>0,
\]

so

\[
\boxed{
\int_0^\infty\mathscr J(z)dz<0.
}
\]

Therefore the exact wedge carries **net inward/negative radial local-energy transport in the depth-integrated sense**.

This is a theorem on the retained Type-I wedge branch, not a heuristic sign convention.

## 4. Sign-reversal consequence when terminal flux is outward

At `z=0`,

\[
\mathscr J(0)=\langle\Phi_E\rangle.
\]

If a branch has

\[
\boxed{
\mathscr J(0)>0,
}
\]

then continuity and the strict negative integral imply that the current cannot remain nonnegative for all depths.

Hence there exists at least one finite depth with

\[
\boxed{
\mathscr J(z)<0.
}
\]

and therefore at least one zero crossing between an outward terminal region and an inward interior region.

Thus positive terminal energy export, when present, must reverse direction deeper in the wedge.

## 5. Relation to the residual M19-269 branch

M19-269's residual branch was constructed from the terminal payer alternative that forces a positive initial energy slope rather than relying solely on a large positive terminal current.

M19-304 does not assume that `J(0)>0` on every residual state.

The unconditional conclusion that always survives is the integrated sign

\[
\boxed{
\int_0^\infty\mathscr J<0.
}
\]

The zero-crossing conclusion is conditional on a positive terminal current.

## 6. Exact weighted return identity for sqrt(z)J

Define

\[
\mathscr G_m(z)=\sqrt z\,\mathscr J_m(z).
\]

M19-303 gives

\[
\mathscr G_m(0)=0,
\qquad
\mathscr G_m(\infty)=0.
\]

M19-300 gives

\[
2\sqrt z\,\mathscr G_m'
=
\mathscr D_m+\mathscr B_m+Z_m.
\]

Therefore, with the integrability certified by M19-303,

\[
\boxed{
\int_0^\infty
\frac{
\mathscr D_m(z)+\mathscr B_m(z)+Z_m(z)
}{2\sqrt z}
\,dz
=0.
}
\]

Thus every positive finite-depth signed-current derivative is exactly compensated elsewhere in the full wedge.

## 7. Structural meaning

M19-302 introduced the signed radial current as the remaining source term in the q-z circulation balance.

M19-304 now classifies it:

\[
\boxed{
\text{signed radial current is not a forbidden payer; it is the exact inward transport required to pay terminal energy and viscous dissipation.}
}
\]

The unconditioned inward transport is mandatory rather than exceptional.

Under production conditioning, event hysteresis can share that transport burden, but the sum `J_m+B_m` still has a fixed negative total determined by terminal energy plus dissipation.

## 8. Dynamic-route consequence

The former target

\[
\mathcal T_{radial}^{signed}
\]

is therefore not a standalone contradiction route in its bare form.

It is reduced to a stronger question:

\[
\boxed{
\mathcal T_{radial}^{excess/rigidity}:
\text{does the production-conditioned fixed-lag event require inward radial transport or hysteresis exceeding the exact available wedge balance, or does a rigidity theorem forbid the required return structure?}
}
\]

Absent such an excess/rigidity theorem, inward radial current is a normal part of the exact wedge energy budget.

## 9. New primary dynamic frontier

The remaining dynamic difficulty is no longer existence of a signed radial current. Its existence and integrated sign are certified.

The hard branch is now

\[
\boxed{
\text{production-conditioned hysteresis/return geometry}
\quad\text{versus}\quad
\text{exact available inward-current budget}.
}
\]

This reconnects naturally to the recurrent factor/observability problem identified in M19-289 and M19-061--074.

---

\[
\boxed{\text{M19-304 COMPLETE; NET INWARD RADIAL ENERGY TRANSPORT IS EXACTLY REQUIRED BY THE WEDGE, NOT ITSELF A CONTRADICTION.}}
\]