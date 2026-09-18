# M19-405 — The GMS palinstrophy endpoint and terminal 1/r stress tail are the same critical scaling obstruction

Date: 2026-09-18

Status: **FRONTIER MERGE / M19-403--404 SHOW THAT ORDINARY RADIAL OR COMPACT-CORE MULTIPLICITY CANNOT DEFEAT THE M17-307 PALINSTROPHY DISCOUNT, LEAVING A SUBCRITICAL PHYSICAL GAIN AS THE MAIN GMS COMPACT-BRANCH TARGET. M19-272--274 IDENTIFY THE STATIONARY TERMINAL HARD TAIL \`u~r^-1\`, \`p~r^-2\` AS EXACTLY STRESS-CRITICAL. DIRECT PARABOLIC SCALING SHOWS THAT THE SAME 1/r CORRIDOR ALSO GIVES ORDER-ONE GMS LOGARITHMIC PAYMENT PER LOG SCALE AND \`r^-1\` PHYSICAL PALINSTROPHY PER PARABOLIC SHELL. THUS THE GMS SUBCRITICAL-GAIN PROBLEM AND THE TERMINAL STRESS/WEAK-L3 RIGIDITY PROBLEM ARE NOT INDEPENDENT SIZE PROBLEMS: THEY ARE TWO FORMULATIONS OF THE SAME CRITICAL TAIL ENDPOINT. A SUCCESSFUL GMS GAIN MUST BREAK THE 1/r CORRIDOR BY PDE RIGIDITY, TIGHTNESS, CANCELLATION, OR A TYPED NONSTATIONARY EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical Type-I / terminal tail model

Consider the retained hard scaling

\[
|u|\sim r^{-1},
\qquad
|p|\sim r^{-2}
\]

on a parabolic scale \(r\).

The corresponding derivative sizes are

\[
|\nabla u|\sim r^{-2},
\qquad
|D^2u|\sim r^{-3}.
\]

A parabolic shell of scale \(r\) has spacetime volume

\[
|Q_r|\sim r^5.
\]

---

## 2. GMS velocity payer is exactly log-critical

The logarithmic GMS velocity density is

\[
\frac{|u|^{10/3}}{\rho^{5/3}}.
\]

On a shell with

\[
\rho\sim r,
\]

the critical tail gives

\[
|u|^{10/3}
\sim
r^{-10/3},
\]

and

\[
\rho^{-5/3}
\sim
r^{-5/3}.
\]

Therefore

\[
\frac{|u|^{10/3}}{\rho^{5/3}}
\sim
r^{-5}.
\]

Multiplying by the shell spacetime volume,

\[
r^{-5}\cdot r^5
\sim1.
\]

Hence

\[
\boxed{
\mathcal P_{GMS,u}^{shell}(r)
\sim O(1)
}
\]

per logarithmic parabolic scale.

Summing over infinitely many shrinking scales therefore naturally gives logarithmic divergence.

---

## 3. Pressure payer has the same critical scaling

For

\[
p\sim r^{-2},
\]

one has

\[
|p|^{5/3}
\sim
r^{-10/3}.
\]

Thus

\[
\frac{|p|^{5/3}}{\rho^{5/3}}
\sim
r^{-5},
\]

and again

\[
\boxed{
\mathcal P_{GMS,p}^{shell}(r)
\sim O(1).
}
\]

The velocity and pressure parts of the GMS payer are simultaneously saturated by the same critical \(1/r\) velocity corridor.

---

## 4. Physical palinstrophy is simultaneously r^{-1} critical

Physical velocity \(D^2\) cost satisfies

\[
|D^2u|^2
\sim
r^{-6}.
\]

Integrating over one parabolic shell gives

\[
\int_{Q_r^{ann}}
|D^2u|^2\,dx\,dt
\sim
r^{-6}r^5
=
r^{-1}.
\]

Therefore

\[
\boxed{
Q_{pal}^{phys}(r)
\sim
r^{-1}.
}
\]

This is exactly the M19-314 transfer exponent.

Multiplication by the critical scale gives

\[
\boxed{
r\,Q_{pal}^{phys}(r)
\sim O(1),
}
\]

which is the same scale-invariant charge measured by the normalized record-cell palinstrophy.

---

## 5. Terminal stress is simultaneously critical

M19-272 gives

\[
\mathbb T
=
\nabla u+\nabla u^T-u\otimes u-pI.
\]

For the \(1/r\) tail,

\[
|\mathbb T|
\sim
r^{-2}.
\]

Hence

\[
\frac1R
\int_{R<|x|<2R}
|\mathbb T|\,dx
\sim O(1),
\]

not \(o(1)\).

Likewise the terminal energy current has the scale-critical nondecaying annular size recorded in M19-272.

Thus one and the same tail simultaneously saturates:

\[
\boxed{
\begin{aligned}
&\text{GMS log payer per scale}: &&O(1),\\
&\text{physical palinstrophy}: &&r^{-1},\\
&\text{annular stress}: &&O(1),\\
&\text{velocity class}: &&L^{3,\infty}\text{ / }1/r.
\end{aligned}
}
\]

---

## 6. Strong-L3 / subcritical corridor breaks all four endpoints

If the critical tail improves to a genuinely subcritical corridor, for example

\[
u=o(r^{-1})
\]

in a sufficiently uniform form, then the corresponding shell cubic/GMS/stress quantities gain decay.

Likewise a strong-\(L^3\) annular tail satisfies

\[
\int_{R<|x|<2R}|u|^3\,dx
\to0
\]

along the relevant end and moves away from the weak-\(L^3\) hard endpoint.

M19-272 records that such subcritical decay kills the stationary defect/stress flux under appropriate stress control.

M19-313 shows that sufficiently strong physical palinstrophy control makes the GMS payer finite.

Therefore both routes are asking for a theorem that breaks the same scale-critical corridor.

---

## 7. Consequence for M19-404's subcritical target

M19-404 leaves

\[
\mathcal T_{GMS}^{subcritical}
\]

as the main compact-core GMS route after multiplicity pruning.

M19-405 refines its interpretation:

\[
\boxed{
\mathcal T_{GMS}^{subcritical}
\text{ cannot be a pure size estimate compatible with the retained }1/r\text{ tail}.
}
\]

A valid gain must instead force one of:

1. terminal stress tightness/cancellation;
2. zero-force endpoint rigidity;
3. strong-\(L^3\) or \(o(1/r)\) improvement;
4. destruction of the stationary/log-recurrent critical tail;
5. a nonstationary/remote/Type-II exit.

---

## 8. Merge with the stationary terminal frontier

M19-274 leaves the stationary branch at

\[
\boxed{
\mathcal T_{stress}^{tight}
\lor
\mathcal T_{tail}^{zero-force-rigidity}
}
\]

plus force-cancellation variants.

The GMS compact branch now joins this endpoint:

\[
\boxed{
\mathcal T_{GMS}^{subcritical}
\rightsquigarrow
\mathcal T_{tail}^{critical\text{-}break}.
}
\]

At the level of the hard branch, the open menu should therefore not count

- “GMS critical base gain”, and
- “terminal \(1/r\) stress rigidity”

as wholly independent norm problems.

They share the same critical tail obstruction.

---

## 9. What remains genuinely independent

The two proof architectures remain logically different:

- GMS uses a spacetime singularity criterion near the candidate singular point;
- terminal stress rigidity uses second-generation stationary/scattering limits.

A theorem closing one may require additional transfer to close the other.

The merge is therefore a **root-cause identification**, not a proof that the two theorems are logically equivalent in all branches.

The correct statement is

\[
\boxed{
\text{the retained }1/r\text{ critical corridor is a common sharp witness obstructing both routes}.
}
\]

---

## 10. Strategic consequence

After M19-403--405, further work on the compact hard branch should prioritize **critical-tail rigidity/cancellation**, not:

- more radial scale counting;
- more copies of the same order-one palinstrophy payer;
- another scale-covariant Morrey estimate.

The highest-value targets are

\[
\boxed{
\mathcal T_{stress}^{tight}
\lor
\mathcal T_{tail}^{force-cancel}
\lor
\mathcal T_{tail}^{zero-force-rigidity}
\lor
\mathcal T_{critical}^{factor/observability}.
}
\]

A success here would simultaneously remove the principal scaling witness obstructing the GMS subcritical-gain route.

---

\[
\boxed{\text{M19-405 COMPLETE; GMS PALINSTROPHY CRITICALITY AND TERMINAL 1/r STRESS CRITICALITY SHARE THE SAME HARD-TAIL ENDPOINT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
