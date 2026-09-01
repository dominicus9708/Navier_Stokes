# DSD M5-495 — Noncollinearity does not automatically deplete vortex stretching

Date: 2026-09-01

Status: **SCOPE CORRECTION / THE M5-494 PROPOSED NEXT STEP `Q <= (C-delta_dual) E^(3/4)P^(3/4)` CANNOT BE INFERRED FROM THE M5-490 NONCOLLINEAR DUAL-FLUX MARK ALONE / CLASSICAL VORTICITY-DIRECTION GEOMETRIC DEPLETION WORKS IN THE OPPOSITE DIRECTION: SUFFICIENT ALIGNMENT/COHERENCE OF VORTICITY DIRECTIONS SUPPRESSES THE SINGULAR VORTEX-STRETCHING INTERACTION, WHILE ORDER-ONE MISALIGNMENT REMOVES THAT CANCELLATION RATHER THAN CREATING IT / THE DUAL PAIR SHOULD THEREFORE BE TREATED AS A FIXED PALINSTROPHY DEMAND AND A POSSIBLE STRETCHING-ENABLING GEOMETRY, NOT AS AN AUTOMATIC PRODUCTION DEPLETION FACTOR / THE NEXT ROUTE IS A PRODUCTION-PAYER AUDIT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The tempting but unjustified shortcut

M5-494 proved

\[
|Q|
\le
C_*E^{3/4}P^{3/4}
\]

and suggested investigating whether recurrent noncollinear dual flux might improve the constant:

\[
Q
\stackrel{?}{\le}
(C_*-\delta_{dual})E^{3/4}P^{3/4}.
\]

That implication is **not** justified by noncollinearity alone.

---

## 2. Classical geometric-depletion orientation

The Constantin--Fefferman vorticity-direction mechanism and subsequent geometric depletion literature exploit regularity/coherence of the vorticity direction to weaken the nonlinear stretching interaction.

At a schematic singular-integral level, the stretching kernel contains geometric cancellation factors that become small when nearby intense vorticity directions are sufficiently aligned/coherent.

Therefore the useful regularizing condition is of the form

\[
\boxed{
\text{direction coherence/alignment}
\Longrightarrow
\text{depleted stretching}.
}
\]

The M5-490 mark is instead

\[
\boxed{
\angle(\xi_a,\xi_b)
\ge\alpha_0>0.
}
\]

This is a failure of alignment between two active flux populations.

Hence it cannot by itself imply stronger geometric depletion.

---

## 3. Noncollinearity may be compatible with production

At the elementary local algebraic level, let `S` be symmetric and trace free.

There can exist two noncollinear unit directions `e_a,e_b` satisfying simultaneously

\[
e_a^TSe_a>0,
\qquad
 e_b^TSe_b>0.
\]

For example a trace-free strain with two positive eigenvalues and one negative eigenvalue stretches every direction in a cone spanning the two positive eigendirections.

Thus

\[
\boxed{
\text{two noncollinear active directions}
\not\Rightarrow
\text{one of them has nonpositive longitudinal stretching}.
}
\]

The dual pair can therefore coexist with positive axial enstrophy production.

---

## 4. Spatial separation makes a common-strain argument even weaker

M5-491 already corrected the use of one common pair strain matrix.

The two persistent carriers may occupy different locations,

\[
x_a\ne x_b,
\]

so their longitudinal rates are

\[
\sigma_a
=
\xi_a^T\Sigma(x_a)\xi_a,
\]

\[
\sigma_b
=
\xi_b^T\Sigma(x_b)\xi_b.
\]

No pointwise trace-free matrix identity compares them without additional spatial coherence of `Sigma` across the pair separation.

Therefore a two-vector linear-algebra depletion bound is insufficient even before the nonlocal Biot--Savart structure is considered.

---

## 5. Correct interpretation of M5-492--494

The valid chain is

\[
\boxed{
\text{persistent noncollinear dual pair}
\Longrightarrow
\text{fixed bridge/separator palinstrophy demand}
}
\]

and

\[
\boxed{
\langle P\rangle
\ge p_{mean}>0.
}
\]

The exact similarity balance then requires

\[
\boxed{
\langle Q\rangle
=
\frac14\langle E\rangle+
\langle P\rangle
\ge
\frac14\langle E\rangle+p_{mean}.
}
\]

Thus the dual geometry increases the amount of stretching production that a recurrent hull must finance.

It does **not** simultaneously imply that the financing capacity is reduced.

---

## 6. Literature firewall

Reference scope:

- P. Constantin and C. Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier--Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775--789, DOI 10.1512/iumj.1993.42.42034.
- Later geometric-depletion criteria likewise use directional coherence/alignment or controlled oscillation to suppress stretching.

No theorem from that literature is imported as a direct statement about the present dual-pair hull. The only point used here is the direction of the geometric mechanism: coherence is regularizing; mere noncollinearity is not an automatic depletion hypothesis.

---

## 7. New production-payer split

At recurrent dual-event windows, M5-493 forces a fixed local palinstrophy cost.

The global balance says this must ultimately be financed by positive vortex-stretching production.

Choose a fixed observation ball `B_R` containing the persistent dual pair and split

\[
Q
=
Q_{loc}+Q_{ext},
\]

where

\[
Q_{loc}
:=
\int_{B_R}W\cdot\Sigma W\,dy,
\]

and

\[
Q_{ext}
:=
\int_{\mathbb R^3\setminus B_R}
W\cdot\Sigma W\,dy.
\]

Then the required production has only two broad payer locations:

\[
\boxed{
\text{local dual-core payer}
\lor
\text{exterior/remote-tail payer}.
}
\]

The first must be audited against the active bridge/separator geometry.

The second reconnects directly to the existing remote-source, critical-tail, and flux-genealogy machinery.

---

## 8. Local payer questions

If a fixed fraction of the required mean `Q` is paid inside `B_R`, then the dual-core region must contain recurrent positive longitudinal strain weighted by the local enstrophy:

\[
\int_{B_R}\rho^2\sigma\,dy>0.
\]

The next local audit should determine whether this productive strain can coexist indefinitely with

1. the M5-492 direction bridge charge; or
2. the M5-492 magnitude-separator charge;

without forcing one of the already typed reformation/frequency/flux exits.

No such incompatibility is yet proved.

---

## 9. Exterior payer questions

If instead a fixed fraction of the production is paid outside every fixed dual-core ball, then one obtains recurrent remote critical production.

That must be compared with

- the terminal critical-tail occupancy of M5-479--483;
- the remote payer/projective ratchet reductions M5-469--473;
- the finite material-flux memory M5-397/M5-488;
- and possible critical enstrophy/strain mass on growing windows.

This is a more structurally faithful route than assuming orientation depletion from noncollinearity.

---

## 10. Updated hard core

The current bounded survivor is therefore

\[
\boxed{
\begin{aligned}
&\text{nonzero recurrent Type-I similarity hull},\\
&Z_*\ge Z_{min}^{dual},\\
&\text{persistent noncollinear dual-flux pair},\\
&\langle P\rangle\ge p_{mean}>0,\\
&\langle Q\rangle
=\tfrac14\langle E\rangle+\langle P\rangle,\\
&\text{positive-density ratchet/tension activity},\\
&\text{zero mean signed persistent-flux drift}.
\end{aligned}
}
\]

The missing theorem is a restriction on **how the required stretching production is spatially and genealogically paid**, not a generic dual-angle depletion inequality.

---

## 11. Highest-value next target

Construct a quantitative payer dichotomy over the M5-493 thickened dual-event windows:

\[
\boxed{
\text{dual palinstrophy demand}
\Longrightarrow
Q_{loc}^{+}\text{ recurrent}
\lor
Q_{ext}^{+}\text{ recurrent}.
}
\]

Then:

- route recurrent `Q_ext^+` into remote-tail/critical-mass escalation;
- analyze recurrent `Q_loc^+` using the bridge/separator split and material-flux identity.

This preserves the actual sign structure of vortex stretching and avoids importing a false geometric-depletion shortcut.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
