# DSD M17-369 — Total enstrophy strengthens comparable-scale flux-tube multiplicity to `r^{-1}`, but partition sensitivity prevents final use

Date: 2026-09-08  
Canonical ID: **M17-369**

Status: **ACTIVE INTERMEDIATE MULTIPLICITY CALCULATION / PARTITION-SENSITIVITY FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-368

Consider a family of genuinely distinct, disjoint material tube packets at one intrinsic coefficient scale `r`. For packet `i`, assume the M17-368 geometry

\[
A_i\le C_A r^2,
\qquad
\ell_i\ge c_\ell r,
\qquad
|\kappa|\ge c_\kappa r^{-2}
\]

on the retained packet portion, and let `phi_i>0` be its directed material flux.

M17-368 gives

\[
\boxed{
E_i:=\int_{T_i}|W|^2dy
\ge c_E\frac{\phi_i^2}{r},
}
\]

and

\[
\boxed{
H_i:=\int_{T_i}|\Delta W|^2dy
\ge c_H\phi_i^2r^{-5}.
}
\]

The packets are assumed spatially disjoint for the present additive calculation. If a proposed decomposition is only a repeated parameterization of one tube, M17-357 says it must first be reduced to its fundamental material orbit.

## 2. Fixed total retained flux

Suppose the family carries total directed flux

\[
\boxed{
\sum_{i=1}^{N}\phi_i\ge\Phi_*>0.
}
\]

Suppose also the selected packet family lies inside an enstrophy budget

\[
\boxed{
\sum_{i=1}^{N}E_i\le E_*<\infty.
}
\]

Then M17-368 implies

\[
\sum_i\phi_i^2
\le C r E_*.
\]

Cauchy--Schwarz gives

\[
\Phi_*^2
\le
\left(\sum_i1\right)
\left(\sum_i\phi_i^2\right)
=N\sum_i\phi_i^2.
\]

Hence

\[
\boxed{
N
\ge
c\frac{\Phi_*^2}{E_*}\,r^{-1}.
}
\]

Thus the earlier individual-tube ceiling `phi_i=O(r^{1/2})`, which by itself suggested only `N \gtrsim r^{-1/2}`, is not sharp once the **same total enstrophy budget is shared by all packets**.

## 3. Effective multiplicity

Define the flux participation ratio

\[
\boxed{
N_{eff}
:=
\frac{(\sum_i\phi_i)^2}{\sum_i\phi_i^2}.
}
\]

Then exactly

\[
1\le N_{eff}\le N,
\]

and the preceding estimate gives

\[
\boxed{
N_{eff}
\ge
c\frac{\Phi_*^2}{E_*}\,r^{-1}.
}
\]

This is a more informative statement than the raw tube count: the retained flux cannot remain concentrated in finitely many comparable-scale packets as `r -> 0`.

## 4. Raw-H2 consequence if multiplicity is near minimal

From M17-368,

\[
H_{fam}:=\sum_iH_i
\ge
c r^{-5}\sum_i\phi_i^2.
\]

Using

\[
\sum_i\phi_i^2
\ge
\frac{\Phi_*^2}{N},
\]

we obtain

\[
\boxed{
H_{fam}
\ge
c\frac{\Phi_*^2}{N}r^{-5}.
}
\]

If the realized multiplicity is of the minimal order

\[
N\lesssim r^{-1},
\]

then

\[
\boxed{
H_{fam}\gtrsim\Phi_*^2r^{-4}.
}
\]

Thus a minimally fragmented fixed-flux family produces an enormous raw-`H2` charge.

## 5. Why this does not close the branch

The problem is that `N` and `N_eff` depend on how the flux population is partitioned.

A flux band can be subdivided into smaller flux bands without changing the underlying Eulerian field. Under such a subdivision,

\[
N\uparrow,
\qquad
N_{eff}\uparrow,
\]

while the physical field and the additive currencies of M17-358 remain unchanged.

Therefore no contradiction may be based solely on

\[
N(r)\to\infty
\]

or on a required rate for a **chosen tube partition**.

This is exactly the sort of structural bookkeeping ambiguity that the DSD analysis layer should expose before the quantity is promoted into the canonical PDE argument.

## 6. Correct next target

The next step must eliminate the tube partition entirely.

The exact flux-coordinate identities are

\[
dy=\frac{ds\,d\Phi}{\rho},
\]

\[
\int \kappa_-^{3/2}dy
=
\int \kappa_-^{3/2}\rho^{-1}ds\,d\Phi,
\]

and

\[
\int |\Delta W|^2dy
=
\int \kappa^2\rho\,ds\,d\Phi.
\]

These two measures carry reciprocal amplitude weights. Cauchy--Schwarz can therefore cancel amplitude **without choosing tube packets**.

That partition-free dual-weight inequality is the target of M17-370.

## 7. Audit verdict

**PASS as an intermediate calculation.**

The strengthened multiplicity floor

\[
N\gtrsim r^{-1}
\]

is mathematically valid for a fixed disjoint packet decomposition, but tube count is not an invariant closing currency. It must not be used as the final contradiction mechanism.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]