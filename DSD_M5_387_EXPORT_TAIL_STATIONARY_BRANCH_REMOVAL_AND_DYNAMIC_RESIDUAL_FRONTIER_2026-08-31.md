# DSD M5-387 — Export-tail stationary branch removal and dynamic residual frontier

Date: 2026-08-31

Status: **THE CURRENT POSITIVE-FREQUENCY EXPORT SURVIVOR IS IDENTIFIED WITH THE PREVIOUS LOG-RADIUS CRITICAL CONVEYOR / THE OLD TAIL-HOMOGENEITY FORK SPLIT THIS CONVEYOR INTO RESIDUAL-ACTIVE DYNAMICS OR A REALIZED STATIONARY CRITICAL PROFILE / M5-268 SUBSEQUENTLY CLOSED THE REALIZED STATIONARY PROFILE BY RG-JET FLATNESS, OSEEN CARLEMAN CONTINUATION, REMOVABILITY OF THE PUNCTURE, AND THE ENTIRE-STATIONARY ENERGY IDENTITY / THEREFORE THE FORMED-ANCESTRY NO-H EXPORT FRONTIER HAS ONLY THE NONSTATIONARY RESIDUAL-ACTIVE CRITICAL CONVEYOR LEFT / STATIC 1/R TAIL COMPATIBILITY AND FINITE ENERGY DO NOT CLOSE IT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-386 reduced the formed-ancestry no-H T side to positive-frequency material export / spatial non-tightness.

Older repository work already analyzed exactly this permanent-export topology and converted it into a critical log-radius conveyor.

The present note updates the current proof tree using the later stationary-tail closure M5-268.

---

## 2. Permanent export gives the critical log-radius conveyor

The 2026-08-25 permanent-export analysis uses Leray variables and

\[
 \rho=\log R.
\]

For the passive critical dilation equation,

\[
 U_s+\frac12U+\frac12R\partial_RU=0,
\]

the general degree-critical solution is

\[
 \boxed{
 U(R,\theta,s)
 =R^{-1}F\!\left(\theta,\rho-\frac s2\right).
 }
\]

Thus material populations exported at positive Leray-time frequency form, after fixed thinning, a positive-density pulse train in the traveling coordinate

\[
 \eta=\rho-s/2.
\]

This is the canonical permanent-export survivor.

---

## 3. Critical energy and enstrophy do not remove the conveyor

For

\[
 U\sim R^{-1},
 \qquad
 \Omega\sim R^{-2},
\]

a geometric shell has

\[
 \int_{A_R}|\Omega|^2\sim R^{-1},
\]

so geometric shells have summable enstrophy.

The normalized kinetic energy of the tail out to the historical radius grows like the historical radius itself, exactly matching the allowed growth of normalized kinetic energy under finite physical energy.

Hence neither

\[
 \sum_R\int_{A_R}|\Omega|^2
\]

nor the ordinary physical kinetic-energy ceiling gives a contradiction.

This is the already-audited critical saturation firewall.

---

## 4. Static core-tail coexistence is also not a contradiction

The previous dynamic-maintenance audit constructed a divergence-free static witness with

\[
 |U_T|\sim R^{-1},
 \qquad
 |\nabla U_T|\sim R^{-2},
\]

which lies outside strong `L3` but has finite Dirichlet/enstrophy content and can be placed arbitrarily far from a compact recurrent core.

Its direct strain/pressure coupling to the core tends to zero with tail radius.

Therefore the current frontier cannot be closed by a purely static statement of the form

\[
 \text{nontrivial core}+	ext{critical tail}\Longrightarrow\bot.
\]

The missing information is dynamical maintenance by the actual Navier--Stokes equation.

---

## 5. Tail homogeneity defect fork

M5-220 defined the stationary projected Navier--Stokes residual of the canonical tail

\[
 \boxed{
 F_T
 :=
 \nu\Delta T
 -\mathbb P\nabla\cdot(T\otimes T).
 }
\]

On the aperiodic/minimal tail branch with nontrivial log-radius phase action, the compactness fork was

\[
 \boxed{
 \text{critical tail}
 \Longrightarrow
 R_{tail}
 \lor
 S_{crit}^{nonhom},
 }
\]

where

- `R_tail`: `F_T` is quantitatively active on a positive-density family of log cells;
- `S_crit^{nonhom}`: a subsequence converges to a nonzero stationary critical punctured-space Navier--Stokes profile.

At the time of M5-220 the stationary branch was still open.

---

## 6. M5-268 closes the realized stationary branch

M5-268 later supplied the missing realized-RG rigidity.

For a realized canonical tail `T`, the exact RG path satisfies

\[
 \partial_\rho\mathscr R_\rho(T)
 =-
u\Delta\mathscr R_\rho
 +\mathbb P\nabla\cdot
 (\mathscr R_\rho\otimes\mathscr R_\rho).
\]

If `T` is stationary,

\[
 F_T=0,
\]

the triangular RG recursion forces every positive RG coefficient/jet to vanish.

Thus the realized RG descendant is flat to all orders relative to `T` as `rho->0` on punctured compact sets.

After reversing `rho` to an ordinary forward Navier--Stokes time, the difference between the realized path and the stationary tail solves the local Oseen system used by the repository's Carleman theorem.

All-order flatness permits zero extension through the terminal slice. The Carleman weight-gap argument forces equality on a nonempty preterminal open set, and spatial analytic continuation gives

\[
 \mathscr R_{\rho_1}(T)=T
 \qquad\text{on }\mathbb R^3\setminus\{0\}
\]

at one positive RG depth `rho_1`.

The finite-depth descendant is smooth at the scaling center, so the puncture of `T` is removable.

The resulting entire smooth stationary field has

\[
 |T|=O(R^{-1}),
 \qquad
 |\nabla T|+|P|=O(R^{-2}),
\]

and the cutoff stationary energy identity forces

\[
 \nabla T=0,
 \qquad
 T=0.
\]

This contradicts the nonzero tail/homogeneity witness.

Therefore

\[
 \boxed{
 S_{crit}^{nonhom}=\varnothing
 }
\]

on the realized W1/RG corridor.

---

## 7. Current export-tail reduction

Substitute M5-268 into the M5-220 fork.

The stationary option is gone, leaving

\[
 \boxed{
 \text{realized permanent-export critical tail}
 \Longrightarrow
 R_{tail}.
 }
\]

That is,

\[
 \boxed{
 \|F_T\|_{H^{-1}(A_*^+)}
 \ge\varepsilon_F>0
 }
\]

on a positive-density family of translated log-radius cells, after choosing the retained residual threshold/subsequence supplied by M5-220.

The surviving tail is therefore **dynamically residual-active**, not merely a passive static `1/R` profile.

---

## 8. Relation to positive-frequency export

M5-386 gives positive-frequency export on the formed-ancestry no-H survivor.

The log-radius conveyor converts this to a positive-density family of historical log cells.

M5-387 now says that if those cells remained asymptotically stationary-residual quiet, compactness would create the stationary tail excluded by M5-268.

Hence permanent nonreturning export must keep paying a genuine critical Navier--Stokes residual on the conveyor.

Schematically,

\[
 \boxed{
 T_{export,+freq}
 \Longrightarrow
 R_{tail,+dens}.
 }
\]

---

## 9. What the residual means

After a divergence-free cutoff of the canonical tail, write the finite-energy quotient

\[
 Q=V-B_T.
\]

The quotient equation contains the forcing

\[
 \mathcal F_{B_T},
\]

which agrees with `F_T` away from the cutoff transition annulus.

Thus `R_tail` is not merely a failure of a descriptor to be homogeneous.

It is an actual recurrent forcing channel in the finite-energy quotient dynamics.

However critical shell scaling still leaves open whether the work done by this forcing has a nonsummable physical cost.

---

## 10. Firewall

The following inferences remain forbidden:

1. `F_T != 0` does not by itself imply a finite-energy contradiction;
2. positive-density critical residual cells do not automatically have additive physical work because historical shell costs may decay geometrically;
3. the residual cannot be replaced by the homogeneity defect algebraically — M5-220 explicitly audited this;
4. finite energy cannot be reused to reject the bare `1/R` shell stack.

The next step must be a **residual-work or residual-coercivity** estimate with a gain beyond critical scaling.

---

## 11. Updated master frontier

On the formed-ancestry no-H corridor, the chain is now

\[
 \boxed{
 \text{first-hitting cascade}
 \to
 T_{export,+freq}
 \to
 \text{log-radius critical conveyor}
 \to
 R_{tail,+dens}.
 }
\]

The stationary critical-tail endpoint is removed.

The remaining formed T obstruction is therefore one quantitative question:

\[
 \boxed{
 \text{Can a finite-energy quotient absorb a positive-density train of}
 \text{critical }H^{-1}\text{ tail residuals without a supercritical work,}
 \text{dissipation, or compactness cost?}
 }
\]

---

## 12. DSD interpretation

The final formed channels are now separated as

- **H**: local frequency/capacity escalation;
- **T export**: material ancestry moves out of the recurrent core;
- **critical conveyor**: exported ancestry is represented at growing similarity radius;
- **residual**: the conveyor must be dynamically maintained by a nonzero stationary-NS defect.

Thus `export` is no longer the terminal descriptor; it has been resolved into an actual PDE forcing channel.

---

## 13. Audit verdict

### IMPORTED / CLOSED

- permanent export -> log-radius critical conveyor;
- static energy/enstrophy/core-tail contradictions rejected;
- realized stationary critical-tail branch closed by M5-268.

### CURRENT SURVIVOR

\[
 \boxed{
 R_{tail,+dens}:
 \text{positive-density critical NS residual on the export conveyor}.
 }
\]

### NEXT TARGET

Residual-work/coercivity beyond critical scaling.

### STILL OPEN

- residual-active conveyor;
- ancestry-description noncompactness outside the formed corridor;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
