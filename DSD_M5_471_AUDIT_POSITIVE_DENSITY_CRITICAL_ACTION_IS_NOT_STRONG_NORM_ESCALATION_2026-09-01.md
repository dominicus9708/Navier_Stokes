# DSD M5-471 — Positive-density critical ratchet action is not strong norm escalation

Date: 2026-09-01

Status: **SCOPE CORRECTION / M5-469--470 FORCE ORDER-ONE SCALE-CRITICAL PROJECTIVE/DIFFUSIVE ACTION AT POSITIVE GENERATION DENSITY, BUT THIS DOES NOT BY ITSELF FORCE AN UNBOUNDED SINGLE-STAGE NORM OR VIOLATE THE LERAY ENERGY BUDGET / THE LABEL `H_crit^strong` MUST BE SPLIT INTO GENUINE AMPLITUDE/FREQUENCY ESCALATION AND A POSITIVE-DENSITY CRITICAL-ACTION CORRIDOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-469--470

On a bounded outer-deformation lane, if the remote affine source contributes a fixed positive fraction of the first-hitting stretching action over `N` generations, M5-469 yields

\[
\int |r|\,d\tau \ge cN-O(1),
\]

where the residual axis action `r` consists of local tilt, directional diffusion, active-threshold exit, or flux reformation.

Equivalently, after routing threshold exits and reformation into the already constructed flux genealogy, the retained-material lane has positive generation density of intervals on which

\[
\int_J |\tau|\,d\tau
+\int_J
\frac{|(I-\xi\otimes\xi)\Delta\Omega|}{|\Omega|}\,d\tau
\ge c_0>0.
\]

This is genuinely scale critical.

However it is an integrated action statement, not a pointwise norm blow-up theorem.

---

## 2. Exact scaling of a coherent tilt episode

Let a first-hitting stage have physical natural scale

\[
r_j=\sqrt{\nu/W_j}.
\]

In normalized variables

\[
Y=(x-X_j)/r_j,
\qquad
d\tau=\frac{\nu}{r_j^2}dt,
\]

and physical strain scales as

\[
S_{phys}=\frac{\nu}{r_j^2}\Sigma.
\]

Suppose a projective episode is spatially coherent on an `O(1)` normalized region and occupies an `O(1)` normalized time interval, so that

\[
\int\!\int |\widetilde\tau|^2\,dYd\tau\ge c_1>0.
\]

Then its physical strain-`L2` spacetime cost is only

\[
\begin{aligned}
\int_{I_j}\int |S|^2dxdt
&=\left(\frac{\nu^2}{r_j^4}\right)
(r_j^3)
\left(\frac{r_j^2}{\nu}\right)
\int\!\int |\Sigma|^2dYd\tau\\
&\gtrsim c_1\nu r_j.
\end{aligned}
\]

Hence

\[
\boxed{
\text{one coherent scale-critical ratchet episode costs only }O(\nu r_j)
\text{ in the ordinary energy-dissipation ledger.}
}
\]

Since the first-hitting scales are geometric,

\[
\sum_j r_j<\infty.
\]

Therefore positive-density repetition of such episodes is compatible with finite total Leray energy dissipation.

---

## 3. Directional-diffusion action is also not automatically globally budgeted

The exact direction equation on an active carrier is

\[
D_t\xi
=\tau
+\frac{\nu}{|\omega|}(I-\xi\otimes\xi)\Delta\omega.
\]

The normalized directional-diffusion action

\[
\int
\frac{|(I-\xi\otimes\xi)\Delta_Y\Omega|}{|\Omega|}
\,d\tau
\]

is scale invariant.

But the corresponding physical higher-derivative quantities scale supercritically:

\[
\int_{I_j}\int |\nabla\omega|^2dxdt
\sim \frac{\nu}{r_j},
\]

and

\[
\int_{I_j}\int |\Delta\omega|^2dxdt
\sim \frac{\nu}{r_j^3}
\]

for an `O(1)` normalized packet.

No globally finite Leray-level ledger controls these quantities up to a hypothetical singular time.

Thus large directional-diffusion action is a genuine higher-derivative critical branch, but repeated order-one action is not itself a contradiction.

---

## 4. Strong amplitude and positive-density action must be separated

Define two distinct classes.

### A. Genuine strong escalation

\[
H_{amp/freq}^{strong}:
\]

some normalized amplitude, relative frequency, source-scale enstrophy, or comparable critical norm tends to infinity along the selected tower.

### B. Positive-density critical action

\[
A_{ratchet}^{dens}:
\]

all instantaneous normalized quantities may remain bounded, but on a positive density of generations the carrier pays an order-one critical projective/tilt/directional-diffusion action.

M5-469 proves a route into

\[
A_{ratchet}^{dens}
\]

unless a genuine strong escalation/reformation branch is already active.

It does **not** by itself prove

\[
A_{ratchet}^{dens}\Rightarrow H_{amp/freq}^{strong}.
\]

---

## 5. Why this correction matters

If the two classes are conflated, the proof tree appears artificially closed:

\[
\text{remote payer}\to H_{crit}^{strong}.
\]

The accurate audited statement is

\[
\boxed{
\text{remote payer}
\Longrightarrow
H_{amp/freq}^{strong}
\lor
A_{ratchet}^{dens}
\lor
T_{reformation}^{formed}.
}
\]

The formed reformation branch is already routed through the fixed-flux finite-memory genealogy, but the positive-density critical-action lane remains a genuine hard core.

---

## 6. Existing anti-shortcut firewall

The repository already contains an explicit Fourier counterexample showing

\[
\text{transverse vorticity}
\not\Rightarrow
\text{projective tilt}.
\]

Therefore the new hard lane must always be formulated through the **actual direction equation / actual material-axis motion**, not merely through transverse vorticity mass.

---

## 7. Updated frontier after the correction

The most accurate current master split is

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{amp/freq}^{strong}
\lor
A_{ratchet}^{dens}.
}
\]

Here `A_ratchet^dens` includes the bounded-amplitude case where stretching, tilt and/or directional diffusion recur at natural scale with positive generation density.

This is smaller and more precise than the earlier large H/T tree, but it is not yet a contradiction.

---

## 8. Highest-value next target

The next calculation should ask whether `A_ratchet^dens` forces a **scale-critical spacetime norm with a non-summable stage charge**, for example a Serrin/strain-critical quantity, and if so whether that charge has a globally finite ledger or only reproduces a standard blow-up criterion.

If every available critical charge is itself allowed to diverge at blow-up, then the correct next object is a minimal/recurrent critical element carrying persistent ratchet action rather than another stage-sum argument.

---

## 9. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
