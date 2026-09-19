# M21-005 — The mixed transport-current branch is an exact depth coboundary: it either hides a phase transition outside the chosen corridor or can be pushed to zero at the wedge endpoints

Date: 2026-09-20  
Canonical ID: **M21-005**  
Status: **TRANSPORT-BRANCH REDUCTION / THE M21-004 MIXED CURRENT Y_M IS AN EXACT z-COBOUNDARY WITH ZERO TERMINAL AND SMOOTH-CORE ENDPOINTS / ITS CORRIDOR DIFFERENCE IS NOT AN INDEPENDENT BULK PAYER BUT THE NET PHASE CHARGE EXCHANGED WITH THE COMPLEMENTARY DEPTH REGIONS / IF THE NO-CROSSING PHASE EXTENDS WHILE THE CORRIDOR IS ENLARGED, THE ENDPOINT CURRENT CAN BE MADE ARBITRARILY SMALL; IF IT CANNOT BE ENLARGED WITHOUT LOSING THE SIGN, A PHASE-TRANSITION DEPTH HAS ALREADY BEEN FOUND / THE AUTHORITATIVE NO-CROSSING PAYERS REDUCE TO PRESSURE-DIFFUSION CORRELATION OR SIGNED LONGITUDINAL-TRANSVERSE SEGREGATION / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. M21-004 current

Recall

\[
\boxed{
\mathscr Y_M(z)
=
z^{7/2}\mathscr M(z)
+
2z^{9/2}\mathscr F_M(z).
}
\]

M21-004 gives

\[
\boxed{
\mathscr Y_M'
=
\frac12z^{7/2}\mathscr H
-
z^{7/2}(\mathscr C+\mathscr D)
+
\frac72z^{5/2}\mathscr M,
}
\]

where

\[
\mathscr H=6\mathscr A-\mathscr B.
\]

For a corridor \([a,b]\),

\[
\frac12\int_a^b z^{7/2}\mathscr H\,dz
=
\Delta Y_M
+
R_{PD}
-
R_{\Gamma K}.
\]

The present module audits whether \(\Delta Y_M\) is an independent payer.

## 2. Terminal endpoint

All terminal wedge coefficients are smooth and bounded.

Hence

\[
\mathscr M(z)=O(1),
\qquad
\mathscr F_M(z)=O(1)
\qquad
(z\downarrow0).
\]

Therefore

\[
z^{7/2}\mathscr M(z)\to0,
\]

and

\[
z^{9/2}\mathscr F_M(z)\to0.
\]

Thus

\[
\boxed{
\mathscr Y_M(0)=0.
}
\]

## 3. Smooth Type-I core endpoint

At the smooth similarity core,

\[
F=O(z^{-1/2}),
\]

\[
G=O(z^{-1}),
\]

\[
\Sigma_F=O(z^{-1}).
\]

Hence

\[
E=|G|^2=O(z^{-2}),
\]

\[
\Gamma=O(z^{-1}),
\]

\[
K=O(z^{-2}).
\]

Therefore

\[
M=E\Gamma K=O(z^{-5}),
\]

and

\[
MF_r=O(z^{-11/2}).
\]

Thus

\[
z^{7/2}\mathscr M(z)=O(z^{-3/2})\to0,
\]

and

\[
z^{9/2}\mathscr F_M(z)=O(z^{-1})\to0.
\]

Hence

\[
\boxed{
\mathscr Y_M(z)\to0
\qquad
(z\to\infty).
}
\]

## 4. Global coboundary identity

Integrate the M21-004 differential identity over the full half-line.

Because both endpoints vanish,

\[
\boxed{
\mathscr Y_M(\infty)-\mathscr Y_M(0)=0.
}
\]

Therefore

\[
\boxed{
\frac12
\int_0^\infty
z^{7/2}\mathscr H\,dz
=
\int_0^\infty
z^{7/2}(\mathscr C+\mathscr D)\,dz
-
\frac72
\int_0^\infty
z^{5/2}\mathscr M\,dz.
}
\]

The transport current disappears completely from the global ledger.

Thus

\[
\boxed{
\Delta Y_M
\text{ is not an independent global bulk payer.}
}
\]

## 5. Corridor transport is exchange with the exterior

For any finite corridor \([a,b]\),

\[
\Delta Y_M
=
\int_a^b \mathscr Y_M' dz.
\]

Since the full integral is zero,

\[
\boxed{
\Delta Y_M
=
-
\left[
\int_0^a\mathscr Y_M' dz
+
\int_b^\infty\mathscr Y_M' dz
\right].
}
\]

Therefore an order-one current difference across the M21 corridor is exactly an order-one opposite charge in the complementary depth regions.

The corridor transport term does not create a new resource.

It moves the signed phase balance between depth regions.

## 6. Endpoint-pushing principle

Because

\[
\mathscr Y_M(z)\to0
\quad
(z\downarrow0),
\]

and

\[
\mathscr Y_M(z)\to0
\quad
(z\to\infty),
\]

for every \(\varepsilon>0\) there exist

\[
a_\varepsilon>0,
\qquad
b_\varepsilon<\infty
\]

such that

\[
\boxed{
|\mathscr Y_M(a_\varepsilon)|
+
|\mathscr Y_M(b_\varepsilon)|
<
\varepsilon.
}
\]

Therefore

\[
\boxed{
|\Delta Y_M[a_\varepsilon,b_\varepsilon]|
<
\varepsilon.
}
\]

Any corridor containing the forced witnesses may be enlarged toward these endpoints.

## 7. Enlargement dichotomy

Start with the compact witness corridor

\[
[a_{21},b_{21}].
\]

Suppose it is a no-crossing phase:

\[
\mathscr H\neq0
\quad
\text{on }[a_{21},b_{21}].
\]

Enlarge the interval toward

\[
[a_\varepsilon,b_\varepsilon].
\]

Exactly one of two things happens.

### Branch A — transition appears during enlargement

There exists

\[
z_*
\in
[a_\varepsilon,b_\varepsilon]
\]

such that

\[
\boxed{
\mathscr H(z_*)=0.
}
\]

Then the phase-transition branch is realized.

### Branch B — same sign persists on the enlarged interval

Then the no-crossing phase survives to the enlarged interval, but

\[
\boxed{
|\Delta Y_M|<\varepsilon.
}
\]

Thus the transport-current payer can be made arbitrarily small.

## 8. Quantitative reduced no-crossing balance

Assume Branch B and

\[
|\mathscr H(z)|\ge\delta_H>0
\]

with fixed sign on the enlarged interval.

Define the weighted phase charge

\[
\boxed{
L_H(\varepsilon)
:=
\frac12
\left|
\int_{a_\varepsilon}^{b_\varepsilon}
z^{7/2}\mathscr H\,dz
\right|.
}
\]

Then

\[
L_H(\varepsilon)>0.
\]

The exact identity gives

\[
L_H
\le
|\Delta Y_M|
+
|R_{PD}|
+
|R_{\Gamma K}|.
\]

Choose

\[
\varepsilon<L_H/3
\]

when the phase charge has a fixed positive lower bound.

Then

\[
\boxed{
|R_{PD}|+|R_{\Gamma K}|
\ge
\frac23L_H.
}
\]

Hence at least one of

\[
\boxed{
|R_{PD}|
\ge
\frac13L_H,
}
\]

or

\[
\boxed{
|R_{\Gamma K}|
\ge
\frac13L_H
}
\]

holds.

The transport branch has disappeared from the final bulk alternative.

## 9. Sign-aware form

For a longitudinal phase

\[
\mathscr H>0,
\]

after endpoint pushing, the positive phase charge must be paid by either

\[
\boxed{
R_{PD}>0
}
\]

or

\[
\boxed{
R_{\Gamma K}<0.
}
\]

The latter is compressive/projective segregation.

For a transverse phase

\[
\mathscr H<0,
\]

the negative phase charge must be paid by either

\[
\boxed{
R_{PD}<0
}
\]

or

\[
\boxed{
R_{\Gamma K}>0.
}
\]

The latter is extensional/projective segregation.

## 10. Authoritative M21 phase frontier

The M21-004 four-way branch

\[
T_{\rm phase}
\lor
P_{\rm transport}
\lor
P_{\rm pressure/diffusion}
\lor
P_{\rm segregation}
\]

reduces to

\[
\boxed{
T_{\rm phase}
\lor
P_{\rm pressure/diffusion}
\lor
P_{\rm segregation}.
}
\]

The transport current is a depth coboundary, not an independent bulk mechanism.

## 11. Important scope

This reduction does not say

\[
\mathscr Y_M(z)=0
\]

at every finite depth.

Nor does it say that finite-depth transport is dynamically irrelevant.

It says only:

\[
\boxed{
\text{its interval total is endpoint exchange and cannot be counted as an independent global payer.}
}
\]

Local transport may still determine where compensation is placed in z.

## 12. Relation to earlier coboundary audits

This is structurally analogous to earlier corrections where:

- a flux/work pair;
- an amplitude moment current;
- or a common-mode source

became a state-difference/coboundary after exact balance reconstruction.

The lesson is the same:

\[
\boxed{
\text{do not count a conservative current and the bulk source it transports as two independent payments.}
}
\]

## 13. Next target

After M21-005 the no-crossing hard branch has only two genuine bulk compensators:

\[
\boxed{
R_{PD}
}
\]

and

\[
\boxed{
R_{\Gamma K}.
}
\]

M21-006 should audit the scaling and algebraic independence of

\[
R_{PD}
=
\int z^{7/2}(\mathscr C+\mathscr D)\,dz.
\]

The main question is whether its pressure/diffusion pieces collapse to already known critical raw-H2 / Calderon--Zygmund resources, as M20-007 suggests.

If so, the only structurally distinct no-crossing branch left will be the signed longitudinal-transverse segregation integral

\[
R_{\Gamma K}.
\]

\[
\boxed{\text{M21-005 COMPLETE; THE MIXED TRANSPORT-CURRENT BRANCH IS AN EXACT DEPTH COBBOUNDARY AND IS NOT AN INDEPENDENT BULK PAYER.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
