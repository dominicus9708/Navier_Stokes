# DSD M17-163 — Packet multiplicity is volume-compatible at critical scale and reduces to the existing M5 growing-window occupancy gate

Date: 2026-09-05  
Canonical ID: **M17-163**

Status: **MULTIPLICITY FIREWALL / M17-162 REDUCES BACKWARD MASS EXPLOSION TO A STRONGER LOCAL ANCESTOR PACKET OR TO DIVERGING SPATIALLY SEPARATED PACKET MULTIPLICITY. A PURE PACKING ARGUMENT DOES NOT CLOSE THE LATTER AT THE NAVIER--STOKES CRITICAL SCALE. A REMOTE ANNULUS OF RADIUS `R` HAS VOLUME `~R^3`; EVEN IF BOUNDED-`kappa` / ELLIPTIC NONDEGENERACY GIVES EACH OCCUPIED PACKET A FIXED UNIT-SCALE FOOTPRINT, THE SHELL CAN HOLD `O(R^3)` SUCH PACKETS. IF BACKWARD NORMALIZED MASS GROWTH REQUIRES `N_R ~ J_R^-1` COMPARABLE PACKETS, VOLUME CAPACITY FAILS ONLY WHEN `J_R << R^-3`. BUT SUCH SHELLS HAVE `J_R^(3/2) << R^-9/2` AND ARE GEOMETRICALLY SUMMABLE OVER DYADIC RADII; THEY CANNOT CARRY THE DIVERGENT NON-`L3` CRITICAL STACK. HENCE THE RELEVANT MULTIPLICITY RANGE IS VOLUME-COMPATIBLE AND IS EXACTLY THE GROWING-WINDOW CRITICAL OCCUPANCY MECHANISM ALREADY LEFT OPEN BY M5-392/M5-526. THIS IS A FIREWALL AGAINST CLAIMING A FALSE VOLUME CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Shell volume capacity

Let

\[
C_R=\{c_1R<|y|<c_2R\}
\]

be a fixed-shape remote annulus.
Then

\[
\boxed{|C_R|\asymp R^3.}
\]

Suppose the nonconcentrated branch of M17-162 is represented by spatially disjoint packet cores of a fixed normalized radius `r_*>0`.

Then each core has volume at least

\[
v_*=c r_*^3>0.
\]

Therefore the shell can contain at most

\[
\boxed{N_R\lesssim R^3.}
\]

This is the strongest conclusion available from volume packing alone.

---

## 2. Multiplicity required by a backward mass ratio

At the present relative-thick observation time,

\[
a_R^2\gtrsim E_R(0),
\]

and write the critical shell number

\[
\boxed{J_R:=R E_R(0).}
\]

Thus

\[
a_R^2\gtrsim\frac{J_R}{R}.
\]

At a fixed ancestor lag the quiet critical shell ceiling gives

\[
E_R(-T)\lesssim\frac{J_*}{R}
\]

up to a fixed lag-dependent radius factor.

Hence the maximum possible normalized ancestor mass satisfies

\[
\boxed{
\frac{E_R(-T)}{a_R^2}
\lesssim
\frac{C_TJ_*}{J_R}.
}
\]

If this upper scale is realized without one stronger concentration packet, it requires on the order of

\[
\boxed{N_R\sim J_R^{-1}}
\]

comparable low-amplitude packet units, modulo fixed constants and dyadic amplitude levels.

---

## 3. When volume capacity would contradict multiplicity

Compare

\[
N_R\sim J_R^{-1}
\]

with

\[
N_R\lesssim R^3.
\]

A volume contradiction can occur only if

\[
J_R^{-1}\gg R^3,
\]

i.e.

\[
\boxed{J_R\ll R^{-3}.}
\]

Thus volume packing sees only extremely tiny critical shell numbers.

---

## 4. But that regime is already harmless for the non-L3 cubic stack

On dyadic radii

\[
R_k=2^kR_0,
\]

if

\[
J_{R_k}\lesssim R_k^{-3},
\]

then

\[
J_{R_k}^{3/2}
\lesssim R_k^{-9/2}.
\]

Therefore

\[
\boxed{
\sum_kJ_{R_k}^{3/2}<\infty
}
\]

on that subfamily.

But the non-`L3` tail obstruction requires

\[
\sum_kJ_{R_k}^{3/2}=\infty.
\]

Hence the shells that matter to the divergent critical stack lie predominantly in a regime where the raw shell volume is large enough to accommodate the required packet multiplicity.

---

## 5. Meaning of the surviving multiplicity branch

The surviving mechanism is therefore not a local pointwise derivative blowup.
It is

\[
\boxed{
\text{bounded local packet complexity}
+\text{growing number/occupancy over a shell whose volume grows like }R^3.
}
\]

This is exactly the type of hard mechanism retained in M5-392:

- every fixed-order normalized derivative can remain bounded;
- every fixed local analytic box can remain regular;
- yet critical derivative/vorticity mass can grow because more boxes become occupied over a growing spatial window.

It also matches M5-526's dyadic Hardy packing language: failure of `L3` closure is a non-summable log-scale critical packing defect rather than necessarily a local amplitude blowup.

---

## 6. Consequence for the M17 route

The Rank-2 packet analysis has now done the following:

1. relative-thick quiet bounded-`kappa` local packet -> OU limit;
2. finite-lag `L2` packet -> OU/CE-H Liouville contradiction;
3. strong local forgetting -> order-one boundary action, then canceled on the dilation-comoving bounded-collar branch;
4. backward mass failure -> stronger concentration packet or multiplicity;
5. pure volume packing does **not** close the multiplicity at critical scale.

Thus the remaining multiplicity branch is no longer specifically a director-geometry problem.
It has rejoined the pre-existing M5 global occupancy/tail problem.

---

## 7. Updated strategic frontier

Continuing to refine local Rank-2 geometry inside the multiplicity branch is low value unless it creates a **positive per-packet resource whose sum cannot grow like `R^3`**.

The higher-value choices are now:

1. return the multiplicity branch to the M5 dyadic/Hardy/turnover ledger;
2. analyze the unbounded-`kappa` CE-H constitutive branch;
3. resume the independent Rank-1 local/global `l=3` pressure covariance gate.

---

## 8. DSD audit

1. A fixed unit packet footprint is used only for an upper capacity estimate; no stronger quantitative unique-continuation volume floor is claimed.
2. The argument explicitly shows why such a floor is insufficient at critical scale.
3. Divergent packet count is not identified with director-area flux count.
4. The conclusion is a reduction/firewall, not a contradiction.
5. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
