# DSD M17-349 — CE-H line constancy turns a coefficient-compact unbounded vortex tail into harmonic vorticity or a tail-topology exit

Date: 2026-09-08  
Canonical ID: **M17-349**

Status: **ACTIVE CONDITIONAL TAIL-STRUCTURE REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Tail setting

M5-476 reduces the marked ancient obstruction to a finite-energy active rotational cluster plus a passive/low-frequency exterior tail.

M5-482/483 show that on the bounded critical-tail lane the record-scale blow-downs remain locally controlled on punctured annuli, unless terminal amplitude/frequency/coefficient compactness fails.

Work at one smooth terminal ancient slice on the exact CE-H branch:

\[
\Delta\Omega=\kappa\Omega,
\qquad
\nabla\cdot\Omega=0.
\]

M17-313 gives on the active set

\[
\boxed{
\Omega\cdot\nabla\kappa=0.
}
\]

Thus `kappa` is constant along every connected regular vortex line.

## 2. Coefficient-compact tail branch

Assume that on sufficiently large annuli, wherever the CE-H coefficient is defined on the retained active tail,

\[
\boxed{
|\kappa(x)|\le C_\kappa |x|^{-2}.
}
\]

This is exactly the physical scaling expected when the record-scale coefficient remains bounded on fixed punctured annuli.

Failure is retained as

\[
\boxed{G_{tail\ coefficient\ decompactification/nodal\ quotient}.}
\]

No coefficient bound is imported across vorticity zeros without a regular active-tail representation.

## 3. Unbounded vortex lines have kappa identically zero

Let `Gamma` be a connected active vortex line satisfying

\[
\sup_{x\in\Gamma}|x|=\infty.
\]

Since `kappa` is constant along `Gamma`, there exists a scalar `kappa_Gamma` such that

\[
\kappa(x)=\kappa_\Gamma
\qquad(x\in\Gamma).
\]

Choose points `x_n in Gamma` with `|x_n|->infinity`.  The tail coefficient bound gives

\[
|\kappa_\Gamma|
=|\kappa(x_n)|
\le C_\kappa|x_n|^{-2}
\to0.
\]

Hence

\[
\boxed{
\kappa_\Gamma=0.
}
\]

Therefore every coefficient-compact unbounded active vortex line lies entirely in the zero-coefficient phase.

## 4. Exterior unbounded-line foliation branch

Assume there exists `R_0` such that every active point with

\[
|x|>R_0
\]

belongs to a connected vortex line reaching arbitrarily large radius.

Then Section 3 gives

\[
\kappa(x)=0
\]

at every exterior active point.

Thus

\[
\Delta\Omega=\kappa\Omega=0
\]

where `Omega != 0` outside `R_0`.

Because `Delta Omega` is continuous, this identity extends to the closure of the active set.  On any open zero-vorticity component it is trivially true as well.

Therefore

\[
\boxed{
\Delta\Omega=0
\qquad(|x|>R_0).
}
\]

The exterior vorticity is componentwise harmonic.

## 5. Tail-topology alternative

If the exterior active set is not exhausted by vortex lines reaching arbitrarily large radius, then arbitrarily far out there exist active components/lines confined to bounded radial ranges.

Record this as

\[
\boxed{
G_{bounded\text{-}line/toroidal\ tail\ topology}.
}
\]

This includes closed loops, highly wound annular lines, or repeated bounded-radius components whose identity/reuse must be audited separately.

Thus the coefficient-compact tail has the exact split

\[
\boxed{
H_{tail\ coefficient\ compact}
\Longrightarrow
H_{harmonic\ exterior\ vorticity}
\lor
G_{bounded/winding\ tail\ topology}.
}
\]

## 6. Relation to the critical zero-crossing currency

The harmonic exterior satisfies `kappa=0` spatially.  It does **not** automatically contribute to the directed crossing currency, which also requires

\[
h=D_t\kappa\ne0.
\]

Hence M17-346's positive recurrent `Q_0` remains a marked active/genealogical phenomenon rather than being supplied for free by a static passive harmonic tail.

This separation is useful: the weak-critical tail and the directed zero-crossing core are now structurally distinct channels unless genealogy/interface motion couples them.

## 7. DSD-theory role

The retained heuristic is the distinction between an unbounded structure and a collection of bounded structures appearing at arbitrarily large positions.

The actual proof is only:

1. CE-H line constancy `Omega dot grad kappa=0`;
2. the scale-compatible coefficient decay `|kappa|<=C/r^2`;
3. continuity of `Delta Omega`.

No DSD axiom is used as a PDE hypothesis.

## 8. Next target

On the harmonic-exterior branch, finite global enstrophy

\[
\Omega\in L^2(\mathbb R^3)
\]

allows a classical exterior harmonic multipole expansion.

The next calculation is to identify exactly which leading harmonic modes obstruct strong `L^{3/2}` vorticity and hence strong `L^3` velocity.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
