# DSD M17-413 — A parent-length positive-flux exact CE-H loop with parent-time persistence saturates the cubic raw-`H2` ancestry threshold

Date: 2026-09-08  
Canonical ID: **M17-413**

Status: **CONDITIONAL CLOSURE THEOREM / LOOP SPACE-TIME SATURATION / RAW-H2 ANCESTRAL CONTRADICTION CRITERION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-411 shows that pure spatial raw-`H2` multiplicity needs near-cubic packing.

M17-412 shows that a parent parabolic record interval contributes at most `O(R^2)` descendant own-time units, leaving one effective power of `R` that must come from space, amplitude, flux, or another resource.

An exact CE-H positive-flux loop is a natural candidate for precisely this missing linear spatial factor.

## 2. Conditional retained-loop hypotheses

Work in one parent-normalized record cell.

Let the descendant intrinsic coefficient scale be

\[
\boxed{r=R^{-1},\qquad R\gg1.}
\]

Assume during a parent parabolic interval `J` of duration

\[
|J|\ge T_*>0
\]

there exists a same-material exact CE-H vortex tube around a closed loop `Gamma(t)` satisfying uniformly in `t in J`:

1. **parent-scale loop length**
   \[
   \boxed{L_*\le \ell_\Gamma(t)\le L^*;}
   \]
2. **intrinsic coefficient scale**
   \[
   \boxed{c_\kappa r^{-2}\le |\kappa|\le C_\kappa r^{-2};}
   \]
3. **positive retained material flux**
   \[
   \boxed{\Phi(t)\ge\Phi_*>0;}
   \]
4. **own-scale tube area control**
   \[
   A(s,t)\le C_A r^2;
   \]
5. **tubular reach / bounded-overlap geometry** allowing at least `c L_*/r` disjoint or uniformly bounded-overlap length-`O(r)` tube segments;
6. **parent-to-record genealogy compatibility** so the packet family is charged to the same M17-405 record window without cross-generation double counting.

These are explicit hypotheses. The present module does not claim they follow from recurrence alone.

## 3. Exact CE-H line constancy supplies common coefficient scale

M17-313 gives

\[
\boxed{D_\xi\kappa=0.}
\]

Hence on each connected regular vortex line at a fixed time, `kappa` is constant along arclength.

Therefore once the retained loop lies in the intrinsic coefficient bin

\[
|\kappa|\asymp r^{-2},
\]

the entire connected loop carries the same coefficient scale at that time.

This is the key structural fact that allows one parent-length loop to generate many **same-scale** spatial segments rather than merely one localized coefficient packet.

## 4. Linear spatial multiplicity along the loop

Under the tubular reach/bounded-overlap assumption, partition the loop into arclength segments of size

\[
\ell_{seg}\asymp r.
\]

Since

\[
\ell_\Gamma\ge L_*,
\]

the number of bounded-overlap own-scale segments satisfies

\[
\boxed{
N_x
\gtrsim
\frac{L_*}{r}
\asymp L_*R.
}
\]

Thus the loop provides exactly the **linear spatial multiplicity** left open by M17-412.

## 5. Flux gives an enstrophy lower bound on every segment

For one segment, let `A_s` be a transverse cross-section.

Material vorticity flux is

\[
\Phi
=
\int_{A_s}\rho\,dA.
\]

By Cauchy--Schwarz,

\[
\Phi^2
\le
A_s\int_{A_s}\rho^2dA.
\]

Since

\[
A_s\le C_A r^2,
\]

we obtain

\[
\int_{A_s}\rho^2dA
\ge
c\Phi_*^2r^{-2}.
\]

Integrating over a segment of length `c r`,

\[
\boxed{
E_{seg}
:=
\int_{seg}\rho^2dx
\gtrsim
\Phi_*^2r^{-1}.
}
\]

This is the segment version of the M17-368 flux bridge.

## 6. Exact CE-H converts segment enstrophy to raw-H2

On the retained coefficient bin,

\[
|\kappa|\asymp r^{-2}.
\]

Exact CE-H gives

\[
|\Delta\Omega|^2
=
\kappa^2\rho^2.
\]

Hence

\[
\boxed{
H_{seg}(t)
:=
\int_{seg}|\Delta\Omega|^2dx
\gtrsim
\Phi_*^2r^{-5}.
}
\]

Over one descendant own-time interval of length

\[
\Delta t_{own}\asymp r^2
\]

in viscosity-one normalized variables,

\[
\int_{I_{own}}H_{seg}(t)dt
\gtrsim
\Phi_*^2r^{-3}.
\]

Multiplying by the scale-invariant raw-`H2` spacetime factor `r^3`,

\[
\boxed{
h_{seg}^{norm}
:=
r^3\int_{I_{own}}H_{seg}dt
\gtrsim
c\Phi_*^2.
}
\]

Thus every spatial segment in every unit own-time carries an order-one normalized raw-`H2` payment.

## 7. Parent-time persistence supplies quadratic temporal multiplicity

The parent interval has duration `T_* = O(1)` while one descendant own-time has size `r^2`.

Therefore the number of bounded-overlap own-time blocks is

\[
\boxed{
N_t
\gtrsim
cT_*r^{-2}
\asymp cT_*R^2.
}
\]

This is full parent-window temporal saturation.

## 8. Cubic space-time packet count

Combine Sections 4 and 7:

\[
N_xN_t
\gtrsim
cL_*T_*R^3.
\]

Each packet pays at least `c Phi_*^2` normalized raw-`H2`.

Hence the record-level normalized raw-`H2` charge satisfies

\[
\boxed{
H_{record}^{norm}
\gtrsim
cL_*T_*\Phi_*^2R^3.
}
\]

This is exactly cubic.

## 9. Apply the M17-405 ancestry weight

M17-405 weighs the descendant record by `R^{-3}`.

Therefore

\[
\boxed{
R^{-3}H_{record}^{norm}
\gtrsim
cL_*T_*\Phi_*^2
>0.
}
\]

If such a retained loop occurs on infinitely many finite-overlap geometric record windows with uniform constants, then

\[
\sum_mR_m^{-3}H_{record,m}^{norm}
=\infty,
\]

contradicting the finite first-generation raw-`H2` ancestral ledger.

Thus:

\[
\boxed{
\begin{aligned}
&\text{uniform parent-length positive-flux exact CE-H loop}\\
&+\text{own-scale tubular reach}\\
&+\text{full parent-time persistence}\\
&+\text{representation-safe record genealogy}\\
&\Longrightarrow
\text{raw-`H2` ancestral contradiction}.
\end{aligned}
}
\]

## 10. What this theorem does and does not close

This is a genuine conditional closure criterion.

It does **not** prove that the late CE-H survivor satisfies the parent-time persistence hypothesis.

Existing M17-360/361 recurrent-loop machinery gives recurrent compact loop states and positive mean palinstrophy on a retained positive-flux family, but recurrence/minimal-hull existence is not the same as occupying a fixed positive fraction of every parent record interval.

Likewise, tubular reach must be protected against severe self-clustering/folding.

Therefore the remaining loop debt is now precise:

\[
\boxed{
G_{loop}
=
G_{record\text{-}window\ residence}
\lor
G_{tubular\ reach/spatial\ clustering}
\lor
G_{flux\ thinning}
\lor
G_{coefficient\text{-}scale\ persistence}
\lor
G_{genealogy/interface}.
}
\]

## 11. Relation to M17-390

M17-390 proved that compact loop persistence gives only logarithmic accumulated physical deformation and that recurrence alone can be absorbed by the standard-energy weight.

M17-413 uses a different resource mechanism:

- not strain deformation `K`;
- but direct positive-flux raw-`H2` occupancy over line-length times time-duration.

Therefore M17-390 does not invalidate the present conditional route.

The crucial missing input is not stronger deformation; it is **positive-density record-window occupancy of the positive-flux coefficient-scale loop**.

## 12. DSD audit

The DSD role is a factorization audit of the cubic ancestry exponent:

\[
R^3
=
R^{1}_{\text{loop length}}
\cdot
R^{2}_{\text{parent time}}.
\]

Both factors are standard geometric/parabolic facts once the retained-loop hypotheses are granted.

## 13. Audit verdict

**PASS — conditional cubic saturation theorem.**

A parent-length positive-flux exact CE-H loop that survives for a positive fraction of one parent parabolic record interval would exactly defeat the `R^{-3}` raw-`H2` ancestry discount.

The next proof target is therefore sharply reduced to a record-window occupancy theorem (or its failure classification) for the recurrent positive-flux loop family.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]