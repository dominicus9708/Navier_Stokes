# DSD M17-288 — R^7 infinity feed requires a growing mesoscopic horizon before it can be compared with parent shell mass

Date: 2026-09-06  
Canonical ID: **M17-288**

Status: **ANTI-SHORTCUT / M17-287 SHOWS THAT A NONZERO ANCIENT SPECTRAL CORE NEEDS `R^7` BACKWARD MASS GROWTH IN TANGENT VARIABLES, BUT THE CURRENT COMPACTNESS CONSTRUCTION IS DIAGONAL ONLY ON EVERY FIXED RESCALED TIME/RADIUS. COMPARING THAT GROWTH TO THE FINITE MASS OF THE PARENT REMOTE SHELL REQUIRES A PRE-LIMIT HORIZON `T_j->infinity` AND RADIUS `K_j~sqrt(T_j)->infinity`. THIS GROWING-HORIZON PASSAGE IS NOT AUTOMATIC. WRITING THE PACKET-TO-SHELL MASS FRACTION AS `mu_j=m_j/Esh_j`, THE HORIZON NEEDED TO MAKE `m_j K_j^7` REACH `Esh_j` IS `K_j~mu_j^(-1/7)`, `T_j~mu_j^(-2/7)`. THE CORRESPONDING PHYSICAL RADIUS IS `L_j=r_j mu_j^(-1/7)`. THUS A TRUE MESOSCOPIC RETURN IS AVAILABLE ONLY IF THIS PHYSICAL RADIUS STAYS INSIDE A CORRIDOR WHERE THE NONLINEAR/SIMILARITY COEFFICIENTS REMAIN NEGLIGIBLE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Packet and shell masses

Let

\[
m_j
\]

be the selected scale-comparable packet `L2` mass and

\[
E_j^{sh}
\]

the mass of the relevant tempered parent shell/enlarged shell at the observation stage.

Define

\[
\boxed{
\mu_j:=\frac{m_j}{E_j^{sh}}.
}
\]

Typically

\[
0<\mu_j\le1,
\]

but no uniform positive lower bound is assumed.

Let the packet scale be

\[
r_j\to0.
\]

---

## 2. R7 tangent feed translated to packet units

M17-287 gives, schematically on the no-infinity-boundary branch,

\[
\boxed{
M^{tan}(K,-K^2)\gtrsim K^7
}
\]

for large tangent radius `K`, where tangent mass is normalized by `m_j`.

Therefore the corresponding physical/pre-limit mass requirement is

\[
\boxed{
M^{phys}_j(Kr_j,\theta_j-K^2r_j^2)
\gtrsim
m_jK^7.
}
\]

To make this comparable with the total available shell mass, choose `K` so that

\[
m_jK^7\asymp E_j^{sh}.
\]

This gives the critical horizon

\[
\boxed{
K_j\asymp\mu_j^{-1/7},
\qquad
T_j:=K_j^2\asymp\mu_j^{-2/7}.
}
\]

---

## 3. Physical mesoscopic radius

The growing tangent radius corresponds to physical similarity radius

\[
\boxed{
L_j:=r_jK_j
\asymp
r_j\mu_j^{-1/7}.
}
\]

The physical backward time length is

\[
\boxed{
\Delta\theta_j
=r_j^2T_j
\asymp
L_j^2.
}
\]

Therefore the desired comparison is genuinely mesoscopic if

\[
\boxed{L_j\to0.}
\]

In terms of the mass fraction,

\[
L_j\to0
\quad\Longleftrightarrow\quad
\boxed{
\frac{\mu_j}{r_j^7}\to\infty.
}
\]

---

## 4. Why fixed-T diagonal compactness is insufficient

M17-254/255 provide the following structure:

for every fixed `T,K`, either a payer appears or one can extract compactness on the corresponding cylinder.

This does **not** by itself imply compactness on a sequence

\[
T_j\to\infty,
\qquad
K_j\to\infty.
\]

A payer may first appear at a horizon tending to infinity with `j`, while every fixed horizon remains quiet.

Hence the tempting inference

\[
R^7\text{ tangent growth}
+\text{ finite parent shell mass}
\Rightarrow\bot
\]

is not yet valid.

The missing statement is a **Growing Mesoscopic Horizon Gate**.

---

## 5. Growing Mesoscopic Horizon Gate (GMHG)

A sufficient GMHG would assert that when

\[
L_j=r_j\mu_j^{-1/7}\to0,
\]

one of the following occurs before the horizon

\[
T_j\asymp\mu_j^{-2/7}:
\]

1. normalized palinstrophy payment;
2. scaled ambient/coefficient payment;
3. interface/nodal payment;
4. far-boundary/infinity-feed exit;
5. or the heat-tangent approximation remains valid on the whole growing cylinder.

In case 5, M17-287 can be compared with the parent shell mass and should yield contradiction after a sufficiently large fixed multiplicative constant in `K_j`.

---

## 6. The complementary occupancy-degeneration scale

If the mesoscopic condition fails in the strongest possible no-payer survivor, then

\[
\boxed{
\frac{\mu_j}{r_j^7}=O(1),
}
\]

i.e.

\[
\boxed{
\mu_j=O(r_j^7).
}
\]

Since

\[
\mu_j=\frac{m_j}{E_j^{sh}},
\]

this is an extremely small packet occupancy relative to the parent shell.

Equivalently,

\[
\boxed{
\frac{m_j}{r_j^7}=O(E_j^{sh}).
}
\]

The quantity `m_j/r_j^7` is precisely the absolute seventh-order amplitude-density scale already suggested by M17-231.

Thus M17-287/288 convert the vague low-amplitude escape into a sharper candidate:

\[
\boxed{G_{seventh\text{-}power\ occupancy\ degeneration}.}
\]

---

## 7. DSD audit

- No growing-horizon convergence is imported from fixed-horizon compactness.
- The shell mass comparison is deferred until a GMHG is proved.
- The exponent `1/7` comes directly from the `K^7` tangent mass requirement.
- `mu_j=O(r_j^7)` is a survivor classification, not yet a contradiction.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
