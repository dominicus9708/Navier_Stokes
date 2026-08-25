# DSD W1 Common Gaussian Replenishment Cut

Date: 2026-08-26

Status: **A/B/D/E RETIRED AS INDEPENDENT TERMINAL BRANCHES / EXACT GAUSSIAN RELATIVE-VARIANCE LEDGER DERIVED / ALL NONTRIVIAL COMPACT MINIMAL W1 DYNAMICS FORCE POSITIVE-MEAN MECHANICAL REPLENISHMENT / FIXED-ACTION REPLENISHMENT EVENTS RECUR SYNDENTICALLY / REMOTE PRESSURE CANNOT BE THE SOLE PAYER / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current W1 frontier had been listed as five largely separate tasks:

- A: transition between principal-axis-locked supercritical stretching and positive-middle-strain production;
- B: constant-vorticity-amplitude finite-order degenerate analytic contact;
- C: remote critical H2 derivative/subscale escape;
- D: periodic finite renormalized core rigidity;
- E: aperiodic minimal trajectory-level rigidity.

The DSD logical audit asks whether these are genuinely independent terminal mechanisms.

They are not.

A, B, D, and E are different geometric descriptions of the same nontrivial compact recurrent finite-core dynamics.  The common dynamical requirement is that a nonzero formed core must be maintained against viscous and Leray-scale decay.  This note derives one exact state-space observable whose balance is independent of the A/B/D/E geometry.

The result does not solve global regularity.  It removes A/B/D/E as separate terminal proof obligations and replaces them by one recurrent mechanical-replenishment gate.  The remote H2 branch C remains a derivative escape that can be carried separately by the existing H hierarchy.

---

## 2. Standard Leray equation

Use the standard backward Leray equation

\[
\partial_sU
-\nu\Delta U
+(U\cdot\nabla)U
+\frac12U
+\frac12(Y\cdot\nabla)U
+\nabla P=0,
\qquad
\nabla\cdot U=0.
\]

Let `M` be a nontrivial compact minimal W1 invariant set.

The W1 compact class is smooth on bounded sets and globally lies in `Lp`, `p>3`, with the previously proved tail control.  Hence all Gaussian-weighted observables below are finite and continuous on `M`.

---

## 3. Gaussian relative velocity

For `a>0`, set

\[
\phi_a(Y)=e^{-a|Y|^2}.
\]

Define the Gaussian weighted mean

\[
\bar U_a(s)
:=
\frac{\int_{\mathbb R^3}\phi_aU\,dY}
{\int_{\mathbb R^3}\phi_a\,dY},
\]

and

\[
v=U-\bar U_a.
\]

Then

\[
\boxed{\int\phi_av\,dY=0.}
\]

Define

\[
\boxed{
V_a(U)
:=
\frac12\int\phi_a|v|^2dY,
}
\]

and

\[
\boxed{
D_a(U)
:=
\int\phi_a|\nabla U|^2dY.
}
\]

The time derivative of `bar U_a` produces no bulk term because of the weighted-mean cancellation.

---

## 4. Exact Gaussian relative-variance identity

Dot the Leray equation with `phi_a v` and integrate over all space.

The diffusion term gives

\[
\nu\int\phi_av\cdot\Delta U
=
-\nu D_a
+\frac\nu2\int|v|^2\Delta\phi_a.
\]

The material term gives

\[
-\int\phi_av\cdot(U\cdot\nabla U)
=
\frac12\int|v|^2U\cdot\nabla\phi_a.
\]

The linear `-U/2` term in the evolution form contributes `-V_a`.

The Leray dilation term gives

\[
-\frac12\int\phi_av\cdot(Y\cdot\nabla U)
=
\frac32V_a
+\frac14\int|v|^2Y\cdot\nabla\phi_a.
\]

For any scalar pressure gauge `c(s)`, the pressure term gives

\[
-\int\phi_av\cdot\nabla P
=
\int(P-c)v\cdot\nabla\phi_a.
\]

Therefore

\[
\boxed{
V_a'
-\frac12V_a
+\nu D_a
=
\mathcal F_{mat,a}
+\mathcal F_{pres,a}
+\mathcal K_a,
}
\]

where

\[
\mathcal F_{mat,a}
:=
\frac12\int|v|^2U\cdot\nabla\phi_a,
\]

\[
\mathcal F_{pres,a}
:=
\int(P-c)v\cdot\nabla\phi_a,
\]

and

\[
\mathcal K_a
:=
\frac\nu2\int|v|^2\Delta\phi_a
+
\frac14\int|v|^2Y\cdot\nabla\phi_a.
\]

This identity is exact.

---

## 5. Match the Gaussian to the Leray/viscous operator

For

\[
\phi_a=e^{-a|Y|^2},
\]

we have

\[
\nabla\phi_a=-2aY\phi_a,
\]

\[
\Delta\phi_a
=(-6a+4a^2|Y|^2)\phi_a,
\]

and

\[
Y\cdot\nabla\phi_a
=-2a|Y|^2\phi_a.
\]

Hence

\[
\mathcal K_a
=
\int |v|^2\phi_a
\left[
-3a\nu
+a\left(2a\nu-\frac12\right)|Y|^2
\right]dY.
\]

Choose

\[
\boxed{a=\frac1{8\nu}.}
\]

Then

\[
-3a\nu=-\frac38,
\]

and

\[
a\left(2a\nu-\frac12\right)
=-\frac1{32\nu}.
\]

Thus

\[
\boxed{
\mathcal K_a
=-\frac34V_a
-\frac1{32\nu}
\int |Y|^2\phi_a|v|^2dY.
}
\]

Substitution into the exact identity yields the key balance

\[
\boxed{
V_a'
+\nu D_a
+\frac14V_a
+\frac1{32\nu}
\int |Y|^2\phi_a|v|^2dY
=
\mathcal F_{mech,a},
}
\]

where

\[
\boxed{
\mathcal F_{mech,a}
:=
\mathcal F_{mat,a}
+\mathcal F_{pres,a}.
}
\]

Equivalently,

\[
\boxed{
\mathcal F_{mech,a}
=
\int
\left[
\frac12|v|^2U+(P-c)v
\right]\cdot\nabla\phi_a\,dY.
}
\]

Because `grad phi_a` points toward the Gaussian core, positive `F_mech,a` is an inward weighted mechanical-energy replenishment.

The key structural fact is that viscosity and similarity dilation no longer appear as uncontrolled positive payers.  For this matched Gaussian they join the strictly coercive left side.

---

## 6. Nontrivial compact minimal states have a positive Gaussian variance floor

For every nonzero `U in M`,

\[
V_a(U)>0.
\]

Indeed, if `V_a(U)=0`, then `U` equals its weighted mean almost everywhere on all space because `phi_a>0` everywhere.  Smoothness gives that `U` is spatially constant.  Since `U in L^p(R^3)` for some finite `p>3`, the constant must be zero.

Thus `V_a(U)=0` would imply

\[
U\equiv0,
\]

which is the excluded equilibrium.

Since `M` is compact and `V_a` is continuous,

\[
\boxed{
V_{a,*}:=\min_{U\in M}V_a(U)>0.
}
\]

Likewise `D_a(U)>0` for every nontrivial state, and compactness gives a positive minimum if needed, but the variance floor alone already suffices below.

---

## 7. Invariant-measure mean replenishment is strictly positive

Let `mu` be any Leray-flow invariant probability measure supported on the nontrivial compact minimal set `M`.

For the differentiable bounded state observable `V_a`, invariance gives

\[
\int_M \mathcal L V_a\,d\mu=0,
\]

or equivalently the long-time average of `V_a'` vanishes.

Average the exact Gaussian ledger:

\[
\boxed{
\langle\mathcal F_{mech,a}\rangle_\mu
=
\nu\langle D_a\rangle_\mu
+\frac14\langle V_a\rangle_\mu
+\frac1{32\nu}
\left\langle
\int |Y|^2\phi_a|v|^2dY
\right\rangle_\mu.
}
\]

All terms on the right are nonnegative, and the variance floor gives

\[
\boxed{
\langle\mathcal F_{mech,a}\rangle_\mu
\ge
\frac14V_{a,*}
=:c_a>0.
}
\]

This is the universal recurrent-core replenishment gate.

It is independent of whether the state is:

- principal-axis locked or positive-middle productive;
- constant-amplitude finite-order contact or oscillatory amplitude;
- periodic or aperiodic minimal;
- represented using the periodic canonical-tail quotient or directly on the W1 minimal set.

Hence A, B, D, and E are not independent terminal branches.

---

## 8. Positive mean upgrades to recurrent fixed-action events

The functional `F_mech,a(U)` is continuous on the smooth compact W1 class and therefore bounded.

Since its invariant mean is at least `c_a>0`, the set

\[
\mathcal O_a
:=
\{U\in M:\mathcal F_{mech,a}(U)>c_a/2\}
\]

is nonempty.

By continuity it is open in `M`.

For a compact minimal continuous flow, return times of every orbit to every nonempty open subset are relatively dense.  Therefore every orbit in `M` returns to `O_a` with bounded Leray-time gaps.

Smooth compactness also bounds the time derivative of `F_mech,a` on `M`.  Hence there exists a uniform duration `delta_a>0` such that after entering a slightly stronger open sublevel, one retains for a short interval a lower bound of the form

\[
\mathcal F_{mech,a}\ge c_a/4.
\]

Consequently one can select recurrent event intervals `J_k` with bounded gaps and

\[
\boxed{
\int_{J_k}\mathcal F_{mech,a}(s)ds
\ge
A_a>0
}
\]

for a state-independent fixed action `A_a`.

Thus the event-separation/density problem left in the earlier turnover notes is resolved on the W1 compact minimal class.

---

## 9. Remote pressure cannot be the sole recurrent payer

Split the pressure into sources inside and outside a large parent radius `R_P`.

The repository already proves on the bounded-enstrophy W1 corridor the far-pressure locality estimate

\[
\|\nabla P_{>R_P}\|_{L^\infty(B_R)}
\lesssim R_P^{-2}
\]

for every fixed finite core radius `R`.

Because the Gaussian factor `v grad(phi_a)` is integrable and uniformly bounded on the compact W1 class, the same source split gives

\[
\boxed{
|\mathcal F_{pres,a}^{>R_P}|
\le C_aR_P^{-2}
}
\]

with `C_a` uniform on `M`.

Therefore, after choosing `R_P` sufficiently large,

\[
\sup_{U\in M}
|\mathcal F_{pres,a}^{>R_P}(U)|
< c_a/8.
\]

The positive mean mechanical replenishment cannot be supplied solely by pressure sources at similarity infinity.

Thus the common recurrent payer reduces to

\[
\boxed{
\text{material transfer}
\quad\lor\quad
\text{finite-parent pressure transfer},
}
\]

or a mixture of the two.

Pressure infinity is removed as an independent topology.

---

## 10. DSD logical collapse of A--E

The previous five-task frontier can now be reorganized.

### A: locked strain / positive-middle transition

This geometry is one possible internal mechanism by which the finite core reorganizes, but it is not an independent terminal requirement.  Regardless of how the transition occurs, the recurrent core must satisfy the Gaussian mechanical-replenishment gate.

### B: constant-amplitude finite-order contact

The contact geometry can remain as a local diagnostic, but it is no longer an independent terminal branch.  A recurrent finite-order-contact orbit still requires the same positive mechanical replenishment.

### C: remote H2 critical tail

This remains a genuine derivative escape and belongs to the existing H hierarchy.  It can still coexist with the common Gaussian gate, but if it occurs it is already classified as a derivative-tail failure rather than a separate recurrent-core geometry.

### D: periodic finite renormalized core

Periodicity is no longer needed to prove a replenishment event.  The invariant Gaussian ledger applies directly, so the periodic core is only one realization of the common recurrent mechanical-flux corridor.

### E: aperiodic minimal trajectory

Aperiodicity is likewise irrelevant to the replenishment theorem.  Minimality is enough to upgrade the positive invariant mean to syndetically recurrent fixed-action events.

Therefore the proof tree can retire A, B, D, and E as independent terminal branches.

The sharpened frontier is

\[
\boxed{
W1
\Longrightarrow
H_{2,crit}^{tail}
\quad\lor\quad
\mathcal R_{mech}^{rec},
}
\]

where `R_mech^rec` means a nontrivial compact minimal W1 core with syndetically recurring fixed positive inward Gaussian mechanical-energy transfer.

Strictly speaking the Gaussian replenishment gate also holds on the H2-tail branch; the displayed disjunction is a proof-management partition: H2 escalation is handled by the H hierarchy, while the no-H2 corridor is handled by the single mechanical-replenishment problem.

---

## 11. What has actually been cut

The following are no longer separate endgame questions:

\[
\text{A overlap/locking},
\qquad
\text{B finite-order contact},
\qquad
\text{D periodic core},
\qquad
\text{E aperiodic core}.
\]

They may still be used as diagnostic sublemmas, but failure to finish any one of them does not leave a separate terminal survivor.

All four are subsumed by

\[
\boxed{
\mathcal R_{mech}^{rec}.
}
\]

The genuinely distinct derivative escape remains

\[
\boxed{H_{2,crit}^{tail}.}
\]

This reduces the former five-way frontier to essentially two proof obligations.

---

## 12. Remaining common cut

The next theorem target is no longer a strain/contact/periodicity theorem.

It is the single source-chain question

\[
\boxed{
\text{Can a finite-energy prelimit Navier--Stokes blow-up corridor sustain}
\\
\text{syndetically recurrent fixed Gaussian inward mechanical work}
\\
\text{at every late Leray epoch without activating H2/turnover/export?}
}
\]

The exact ledger shows that recurrent W1 cannot be mechanically closed: it must be continuously replenished.

What is not yet proved is that the required finite-scale material/finite-parent-pressure transfer contradicts the prelimit finite-energy cascade.  Because physical energy per shrinking self-similar scale decreases, a naive sum of fixed normalized event costs is not divergent.  That scaling obstruction is retained explicitly; no false global-energy contradiction is claimed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
