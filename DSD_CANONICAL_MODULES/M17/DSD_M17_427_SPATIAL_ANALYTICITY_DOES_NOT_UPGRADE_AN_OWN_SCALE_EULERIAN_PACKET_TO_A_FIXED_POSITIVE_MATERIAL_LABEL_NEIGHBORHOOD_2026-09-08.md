# DSD M17-427 — Spatial analyticity does not upgrade an own-scale Eulerian packet to a fixed positive material-label neighborhood

Date: 2026-09-08  
Canonical ID: **M17-427**

Status: **ACTIVE EULERIAN/LABEL REPRESENTATION AUDIT / CUBIC PULLBACK FIREWALL / ZERO-VOLUME CORE NO-GO**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-426

M17-426 leaves the scale-critical possibility that selected positive-flux material tube bands shrink in reference-label volume like

\[
\mu(A_m)\asymp R_m^{-3}
\]

and concentrate around a persistent zero-volume material line/core.

A tempting response is to use spatial analyticity of the exact CE-H state to thicken the persistent line into a uniform neighborhood.

The present module shows why that does not produce a **fixed positive material-label volume**.

## 2. Own-scale spatial neighborhood in similarity coordinates

Suppose analyticity, a finite coefficient jet margin, or M17-382 gives at record `m` a normalized similarity ball/cell

\[
B_{c}(y_m)
\]

of radius `c>0` independent of `m` on which the desired CE-H packet structure persists.

Its similarity volume is

\[
|B_c|\asymp1.
\]

Let

\[
r_m=R_m^{-1}=\sqrt{-t_m}.
\]

The corresponding physical cell has radius

\[
c r_m
\]

and volume

\[
\boxed{
|B_{ph,m}|
=r_m^3|B_c|
\asymp R_m^{-3}.
}
\]

Thus a uniform normalized analytic neighborhood is already a cubic-shrinking physical neighborhood.

## 3. Pullback to reference material-label space

Let `X_ph(t;t_0,a)` be the incompressible physical material flow from a fixed reference time `t0`.

Because

\[
\det D_aX_{ph}=1,
\]

material volume is preserved exactly.

Let

\[
A_m:=X_{ph}(t_m;t_0,\cdot)^{-1}(B_{ph,m})
\]

be the material-label preimage of the own-scale packet.

Then

\[
\boxed{
\mu(A_m)
=|B_{ph,m}|
\asymp R_m^{-3}.
}
\]

Therefore the analytic Eulerian thickening pulls back to precisely the same cubic material-label scale found in M17-425--426.

It does not produce a label neighborhood of record-independent positive volume.

## 4. Exact representation firewall

The implication

\[
\text{uniform similarity-space analytic ball}
\Longrightarrow
\text{uniform material-label ball}
\]

is false.

The correct dictionary is

\[
\boxed{
O(1)\text{ similarity volume}
\leftrightarrow
O(R_m^{-3})\text{ physical/material volume}.
}
\]

This is simply the three-dimensional similarity Jacobian.

## 5. Positive flux is exactly compatible with the cubic packet

On the retained normalized amplitude branch,

\[
|W_m|\lesssim1.
\]

Hence physical vorticity scales as

\[
|\Omega_{ph}|\lesssim R_m^2.
\]

An own-scale physical cross-section has area

\[
A_{ph,m}\asymp R_m^{-2}.
\]

Therefore its flux scale is

\[
|\Omega_{ph}|A_{ph,m}
\asymp
R_m^2R_m^{-2}
\asymp1.
\]

Thus a fixed order-one positive flux is exactly compatible with a cubic physical/material tube volume

\[
\ell_{ph,m}A_{ph,m}
\asymp
R_m^{-1}R_m^{-2}
=R_m^{-3}.
\]

No supercritical concentration is present.

## 6. Spatial analyticity and material persistence are different notions

Spatial analyticity controls the field as a function of current Eulerian position.

A material-label neighborhood is obtained only after pullback through the flow map.

Even though the flow is volume preserving physically, the similarity coordinate system itself contracts physical length by `R_m^{-1}` in each spatial direction. Consequently a fixed normalized neighborhood corresponds to vanishing physical/material volume.

Hence analyticity cannot by itself close the M17-426 zero-volume material-core branch.

## 7. Deformation-gradient bounds do not improve the volume exponent

Suppose additional distortion bounds control the shape of the pulled-back packet.

They may improve eccentricity or diameter estimates, but incompressibility fixes the total physical label volume exactly at

\[
R_m^{-3}.
\]

No bounded condition number can turn a set of volume `R_m^{-3}` into a record-independent positive-volume set.

Therefore shape regularity alone does not beat the cubic label firewall.

## 8. Relation to M17-420 finite-jet cover

M17-420 uses a fixed finite coefficient-jet class to produce a uniform **normalized spatial** packet and then a raw-`H2` payment.

That argument is valid.

What cannot be added is the stronger conclusion that the same packet corresponds to one fixed positive-volume material tube across all records.

The correct cross-generation endpoint remains the M17-405 cubic ancestry ledger.

## 9. Revised zero-volume-core status

The M17-426 survivor becomes

\[
\boxed{
G_{persistent\ material\ line/core}
+
G_{own\text{-}scale\ Eulerian\ analytic\ neighborhoods}
\Longrightarrow
G_{cubic\ material\ label\ concentration}.
}
\]

This is scale-critical and not a contradiction.

## 10. What stronger input is now required

To beat the zero-volume-core branch, one needs something not supplied by spatial analyticity or ordinary flow-map smoothness, for example:

1. a material-label nonconcentration theorem with a lower volume scale larger than `R_m^{-3}`;
2. record-supercubic multiplicity of distinct analytic packets;
3. a finite ancestral measure with ancestry weight weaker than `R_m^{-3}`;
4. a turnover/interface current whose accumulated cost is not diluted by the 3D similarity Jacobian;
5. failure of parent-to-record scale/genealogy persistence, which remains an explicit exit rather than a contradiction.

## 11. DSD audit

The DSD role is a representation audit: current-space thickness and material-label thickness are different quantities.

The mathematics is only the incompressible flow Jacobian and three-dimensional similarity scaling.

## 12. Audit verdict

**PASS-NO-GO.**

Spatial analyticity can provide uniform normalized Eulerian packets, but their reference material-label volume is exactly `O(R_m^{-3})`. The zero-volume material-core concentration branch therefore survives analyticity and remains tied to the cubic cross-generation firewall.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
