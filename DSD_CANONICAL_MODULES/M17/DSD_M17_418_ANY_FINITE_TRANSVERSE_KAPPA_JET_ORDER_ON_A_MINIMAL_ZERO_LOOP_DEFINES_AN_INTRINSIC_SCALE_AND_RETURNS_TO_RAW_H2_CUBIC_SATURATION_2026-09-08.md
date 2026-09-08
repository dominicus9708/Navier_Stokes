# DSD M17-418 — Any finite transverse `kappa` jet order on a minimal zero loop defines an intrinsic scale and returns to raw-`H2` cubic saturation

Date: 2026-09-08  
Canonical ID: **M17-418**

Status: **ACTIVE HIGHER-ORDER ZERO DEGENERACY REDUCTION / FINITE-JET CONDITIONAL CLOSURE / ANALYTIC FLATNESS FRONTIER**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-417

On the retained compact minimal-loop branch, M17-416--417 reduce the coefficient geometry to

\[
\boxed{
\kappa|_\Gamma=0,
\qquad
\nabla\kappa|_\Gamma=0,
}
\]

unless an explicit geometry/scale/genealogy exit occurs.

The present question is whether a higher-order but finite transverse coefficient jet can survive.

## 2. Analytic coefficient on the regular CE-H component

On a retained smooth Navier--Stokes ancient solution, spatial analyticity holds at each finite regular time.

On a regular vorticity component where

\[
\rho=|\Omega|>0,
\]

exact CE-H gives

\[
\Delta\Omega=\kappa\Omega.
\]

Therefore

\[
\boxed{
\kappa
=
\frac{\Delta\Omega\cdot\Omega}{|\Omega|^2}
}
\]

is real analytic on that nonzero-vorticity component.

Thus the coefficient near a regular loop admits a convergent spatial Taylor expansion.

## 3. First nonzero transverse jet order

Because

\[
\kappa=0
\]

along the entire loop, all pure tangential derivatives of the loop restriction vanish.

Suppose the coefficient is not flat to infinite order at one loop point.

Let

\[
\boxed{p\ge2}
\]

be the first total derivative order at which a jet with at least one transverse derivative is nonzero.

In local coordinates `(s,n)` with `s` arclength and `n in R^2` transverse to the vortex line,

\[
\kappa(s,n)
=
P_p(s,n)
+O(|n|^{p+1}+\text{mixed higher terms}),
\]

where `P_p` is a nonzero degree-`p` transverse/mixed leading polynomial.

## 4. Higher-order intrinsic coefficient scale

Under Navier--Stokes parabolic scaling,

\[
\kappa_R(x)=R^2\kappa(Rx),
\]

so

\[
D^p\kappa_R
=
R^{p+2}D^p\kappa.
\]

Therefore the scale-invariant length determined by a nonzero `p`-jet is

\[
\boxed{
r_p
:=
|D_\perp^p\kappa|^{-1/(p+2)}.
}
\]

For `p=1` this reduces to the M17-340 scale

\[
r_1=|\nabla\kappa|^{-1/3}.
\]

The formula is therefore the natural higher-order extension of the regular-zero intrinsic gradient scale.

## 5. Own-scale normalization restores order-one coefficient variation

Assume the finite jet is record matched:

\[
\boxed{r_p\asymp r_m\asymp R_m^{-1}.}
\]

Rescale a loop neighborhood by `r_p`.

Then the normalized `p`-jet has order one,

\[
|D^p\kappa^{norm}|\asymp1,
\]

and on a fixed transverse subset of the normalized unit tube the leading polynomial satisfies

\[
|\kappa^{norm}|\ge c_p>0
\]

on a set of fixed positive volume fraction, away from its algebraic nodal directions.

Returning to physical/parent variables, this means that at distance `O(r_p)` from the zero loop,

\[
\boxed{|
\kappa|
\gtrsim
c r_p^{-2}
}
\]

on a definite own-scale subregion.

Thus a higher-order zero is not coefficient-free at its own intrinsic scale.

## 6. Fixed raw-H2 packet from a finite jet

On exact CE-H,

\[
|\Delta\Omega|^2
=
\kappa^2\rho^2.
\]

The compact regular loop branch supplies a positive vorticity amplitude floor on a sufficiently small tube around the selected regular loop arc, unless a nodal/amplitude exit occurs.

Hence in own-scale normalized coordinates, the fixed positive-volume region from Section 5 gives

\[
\boxed{
\int_{Q_{seg}^{norm}}|\Delta\Omega^{norm}|^2dxds
\ge h_p>0
}
\]

for one normalized length-one segment and one normalized own-time interval, with `h_p` depending only on the compact jet/amplitude margins.

Equivalently, each finite-jet own-scale space-time packet pays an order-one normalized raw-`H2` charge.

No logarithmic coordinate is used.

## 7. One nonzero jet point gives a fixed parent-length arc

If the first nonzero `p`-jet has a strict lower bound at one state and one loop point, continuity of the analytic jet in state and arclength gives:

- a nonempty open state neighborhood `U_p`;
- a fixed parent-length loop arc of length `ell_p>0`;
- uniform upper/lower `p`-jet bounds;
- uniform amplitude and tubular geometry margins.

Therefore at descendant scale `r_m`, the arc contains

\[
\boxed{
N_{x,m}^{(p)}\gtrsim cR_m
}
\]

bounded-overlap own-scale segments.

## 8. Minimality and record occupancy

If the full omega-limit is minimal, M17-415 makes the robust `p`-jet state set syndetic.

Hence the corresponding record occupancy fractions satisfy

\[
\boxed{
\sum_m\alpha_m^{(p)}=\infty
}
\]

on the representation-safe bounded-length record map.

Each good record therefore contains

\[
N_{x,m}^{(p)}
\cdot
N_{t,m}^{(p)}
\gtrsim
cR_m\cdot\alpha_m^{(p)}R_m^2
\]

order-one raw-`H2` packets.

Thus

\[
H_{m,p}^{norm}
\gtrsim
c h_p\alpha_m^{(p)}R_m^3.
\]

## 9. M17-405 contradiction

Apply the ancestry weight:

\[
R_m^{-3}H_{m,p}^{norm}
\gtrsim
c h_p\alpha_m^{(p)}.
\]

Since

\[
\sum_m\alpha_m^{(p)}=\infty,
\]

the M17-405 finite raw-`H2` ancestral ledger is contradicted.

Therefore any **finite** record-matched transverse vanishing order closes under the retained minimal-loop geometry.

## 10. Consequence: surviving minimal loop must be infinitely flat

Combining M17-416--418, a surviving compact minimal loop must satisfy, along the loop,

\[
\boxed{
D^\alpha\kappa=0
\quad\text{for every finite transverse/mixed jet }\alpha
}
\]

unless the corresponding jet scale fails to match the record, or amplitude/tubular/genealogy/interface compactness fails.

Thus the analytic coefficient must be **flat to all finite orders** at the loop.

## 11. Analyticity makes infinite flatness decisive

For a real-analytic function, vanishing of every Taylor coefficient at one point implies vanishing in a neighborhood of that point.

Therefore the natural next step is:

\[
\boxed{
\text{all transverse jets vanish}
\Longrightarrow
\kappa\equiv0
\text{ on an open tubular neighborhood}.
}
\]

Then analytic continuation on the connected nonzero-vorticity CE-H component can potentially promote local harmonicity to componentwise harmonicity.

This is the next module.

## 12. Scope firewall

A finite nonzero jet whose intrinsic scale `r_p` is not comparable to the record descendant scale must not be forced into the record packet count.

It is reassigned to its true intrinsic scale or typed as jet-scale/genealogy decompactification.

Thus the theorem is a scale-correct finite-jet closure, not an arbitrary Taylor-series contradiction.

## 13. DSD audit

The DSD role is a degeneracy hierarchy audit:

\[
\text{value}
\to
\text{gradient}
\to
\text{finite higher jet}
\to
\text{analytic flatness}.
\]

At each finite stage, the standard parabolic dimension of `D^p kappa` defines the correct intrinsic scale.

## 14. Audit verdict

**PASS — every finite record-matched transverse coefficient jet order is conditionally closed on the minimal loop branch.**

The surviving coefficient-flat loop is now an analytic local-harmonicity problem, not an untyped high-order zero escape.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]