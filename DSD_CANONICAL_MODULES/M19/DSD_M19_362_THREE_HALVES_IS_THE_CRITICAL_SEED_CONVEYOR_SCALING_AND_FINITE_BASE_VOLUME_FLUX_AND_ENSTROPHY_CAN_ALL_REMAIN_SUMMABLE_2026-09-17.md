# DSD M19-362 — Three-halves is the critical seed-conveyor scaling, and finite base volume/flux/enstrophy can remain summable

Date: 2026-09-17  
Canonical ID: **M19-362**

Status: **ACTIVE SCALING WITNESS / RESET-AMPLIFICATION NO-GO / CRITICAL THREE-HALVES CONVEYOR**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-361 proves that a curvature label activated at a late similarity time \(\theta_j\) must have prehistory average

\[
\overline\kappa_j\ge\frac32-o(1).
\]

The present module audits whether the borderline value \(3/2\) is already incompatible with the finite base resources available in the repository.

It is not.

The following is a scaling witness only. It is not asserted to be an exact Navier--Stokes solution.

## 2. Similarity material-volume law

In backward similarity coordinates the material velocity is

\[
B=U+\frac12y,
\]

and

\[
\nabla\cdot B=\frac32.
\]

Hence a material volume element satisfies

\[
\boxed{
D_B\log dV=\frac32.
}
\]

If a future coherent packet is to have order-one normalized volume at activation time \(\theta_j\), its base preimage may therefore have volume

\[
\boxed{
v_j^0\asymp e^{-3T_j/2},
\qquad
T_j:=\theta_j-\theta_0.
}
\]

## 3. Critical flux seed

Choose a schematic base flux

\[
\boxed{
\phi_j^0\asymp e^{-3T_j/2}.
}
\]

Suppose its preactivation multiplier exposure is at the critical value

\[
\kappa_j\approx\frac32.
\]

The exact material-flux law

\[
D_B\log|\phi|=\kappa
\]

then gives

\[
|\phi_j(\theta_j)|
\asymp
\phi_j^0 e^{3T_j/2}
\asymp1.
\]

Thus the exponentially small base flux reaches the fixed-flux genealogy at order one.

## 4. Curvature amplitude is simultaneously critical

The exact curvature-amplitude law is

\[
D_B\log Z_{curv}
=
\kappa-\frac32.
\]

At the same critical exposure \(\kappa=3/2\),

\[
D_B\log Z_{curv}=0.
\]

Hence a base seed with

\[
Z_{curv,j}^0\asymp1
\]

can remain order one until activation:

\[
\boxed{
Z_{curv,j}(\theta_j)\asymp1.
}
\]

The three requirements

\[
\text{fixed future volume},
\qquad
\text{fixed future flux},
\qquad
\text{fixed curvature amplitude}
\]

therefore meet at the same exponent \(3/2\).

## 5. Positive-density activation times still have summable base resources

Take a separated event sequence

\[
T_j\ge j\tau,
\qquad \tau>0.
\]

Then

\[
\sum_jv_j^0
\lesssim
\sum_je^{-3j\tau/2}<\infty,
\]

and

\[
\sum_j|\phi_j^0|
\lesssim
\sum_je^{-3j\tau/2}<\infty.
\]

Thus neither finite material volume nor the M5-647 finite base transverse-flux resource excludes the critical conveyor by scaling alone.

## 6. Base enstrophy can also be summable

For a consistency witness, take the base seed amplitude at order one while its material support has volume \(v_j^0\asymp e^{-3T_j/2}\).

Then its base enstrophy cost scales like

\[
E_j^0
\sim
\int_{seed_j}|W_0|^2dx
\asymp
v_j^0
\asymp e^{-3T_j/2}.
\]

Hence

\[
\boxed{
\sum_jE_j^0<\infty.
}
\]

If the seed lies on an exact CE-H region with \(|\kappa|\asymp1\), then pointwise

\[
|\Delta W|^2=\kappa^2|W|^2,
\]

so the corresponding base raw-\(H^2\) cost is also geometrically summable.

This does not assert disjoint exact seed packets; it only shows that the known finite base norms do not prohibit the required scale distribution.

## 7. Relation to the global sign identity

A region with \(\kappa\approx3/2>0\) cannot dominate the global enstrophy-weighted coefficient moment because

\[
\int\kappa|W|^2dx=-\|\nabla W\|_2^2\le0.
\]

The witness therefore requires compensating negative-\(\kappa\) population elsewhere.

That is precisely compatible at the level of scaling with the mixed-sign diffuse conveyor isolated in M19-337--357.

No claim is made that the coupled configuration solves the full PDE.

## 8. Sharp consequence

The implication

\[
\text{late reset}
\Longrightarrow
\overline\kappa\ge\frac32-o(1)
\]

is not by itself a contradiction.

The borderline \(3/2\) is the exact similarity rate at which

\[
\boxed{
\begin{aligned}
&\text{material volume expansion},\\
&\text{material flux amplification},\\
&\text{curvature-amplitude maintenance}
\end{aligned}
}
\]

can be synchronized.

Thus any successful theorem must produce a **strict gap** below this rate or a nonrecyclable payer for maintaining it.

## 9. New preferred theorem gate

Define

\[
\boxed{
\mathcal T_{amp}^{gap}:
\exists\varepsilon>0\text{ such that every sufficiently late seed lineage obeys }
\frac1T\int\kappa\,d\theta\le\frac32-\varepsilon,
}
\]

unless one of the already typed exits occurs.

Such a gap would immediately contradict M19-361 for arbitrarily late curvature renewals.

If no gap exists, the frontier becomes classification of the near-critical amplification regime

\[
\boxed{
\frac1T\int\kappa\,d\theta\to\frac32.
}
\]

and its compulsory negative-\(\kappa\) compensation.

## 10. Audit verdict

**PASS-NO-GO — the three-halves threshold is scaling-sharp for the present resources.**

A positive-density sequence of future order-one curvature carriers can be fed, at the level of resource scaling, by exponentially small base seeds whose total volume, absolute flux and enstrophy remain finite. Therefore another finite static base resource is unlikely to close the curvature reset lane without a strict amplification gap or an irreversible dynamic cost.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
