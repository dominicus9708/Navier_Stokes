# Sliding-History Remaining-Time Closure — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — THE QUIET SLIDING/FORGETFUL HISTORICAL SURVIVOR IS CLOSED AT THE MODEL/LEMMA LEVEL BY REMAINING-TIME COMPRESSION; FULL GLOBAL REGULARITY IS NOT PROVED.**

This note combines:

- `TYPEI_ANCIENT_FIRST_HITTING_INHERITANCE_2026-08-20.md` for geometric first-hitting stage times;
- `LOCALIZED_SOLENOIDAL_PHASE_SPACE_TRICHOTOMY_2026-08-23.md` for forced natural-frequency occupancy of a good non-H shell;
- `LOCALIZED_PACKET_EXACT_EVOLUTION_AND_FORGETTING_GATE_2026-08-23.md` for the exact localized Duhamel forgetting gate.

The key new observation is temporal: at a very late first-hitting time, an old remembered shell has only the **current smallest-core time** left before the hypothetical singular time, not its own natural time. For a shell `K` times larger than the current core, the available fraction of its natural time is `O(K^-2)`.

This makes quiet forgetting impossible as `K->infinity`.

---

## 1. Forward remaining-time estimate from the existing stage corridor

Let

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\qquad q>1.
\]

On the non-H/T recurrent first-hitting corridor, the dynamically normalized stage lengths satisfy

\[
0<L_-\le L_k\le L_+<\infty,
\]

and the physical stage duration satisfies

\[
\Delta t_k
\le
\frac{L_k}{W_k}
\le
\frac{L_+}{W_k}.
\]

If infinitely many first-hitting stages accumulate at a hypothetical finite singular time `T*`, then

\[
\begin{aligned}
T^*-t_j
&=\sum_{k=j}^{\infty}\Delta t_k\\
&\le
L_+\sum_{k=j}^{\infty}W_k^{-1}\\
&=
\frac{L_+}{W_j}
\sum_{n=0}^{\infty}q^{-n}.
\end{aligned}
\]

Therefore

\[
\boxed{
T^*-t_j
\le
C_T r_j^2,
\qquad
C_T:=\frac{L_+}{1-q^{-1}}.
}
\]

Similarly the stage lower bound gives a comparable lower Type-I time scale, but only the upper estimate is needed below.

This is a direct smooth first-hitting estimate; no ancient limit is required.

---

## 2. A remembered old shell at time t_j

At time `t_j`, suppose the historical tower remembers `N_j` geometric shells.

Index shell age by `k=1,...,N_j`, with physical radius

\[
\boxed{
R_{j,k}
:=r_jq^{k/2}.
}
\]

Thus the shell is larger than the current core by the ratio

\[
\boxed{
K_{j,k}
:=\frac{R_{j,k}}{r_j}
=q^{k/2}.
}
\]

The shell's own natural parabolic time is

\[
R_{j,k}^2
=r_j^2q^k.
\]

But after `t_j`, the total time left before `T*` is at most `C_T r_j^2`.

Hence the fraction of one old-shell natural time remaining is

\[
\boxed{
\frac{T^*-t_j}{R_{j,k}^2}
\le
C_Tq^{-k}
=
C_TK_{j,k}^{-2}.
}
\]

For any shell age `k->infinity`, this ratio tends to zero exponentially.

---

## 3. There is a genuinely occupied old shell far from the current scale

Let the shellwise cubic masses be

\[
m_{j,k}
:=
\int_{A_{j,k}}|u(t_j)|^3dx.
\]

Suppose the historical tail has the required logarithmic occupancy

\[
\sum_{k=1}^{N_j}m_{j,k}
\ge
c_0N_j,
\]

and the Type-I envelope gives

\[
m_{j,k}\le M_A.
\]

The positive-density selection lemma from the phase-space note gives a fixed fraction

\[
\rho_*
:=
\frac{c_0}{2M_A-c_0}>0
\]

of good shells satisfying

\[
m_{j,k}\ge c_0/2.
\]

Among `N_j` shell positions, at least one good shell must have age

\[
\boxed{
k_j\ge\frac{\rho_*}{2}N_j}
\]

for all sufficiently large `N_j`: otherwise fewer than `rho_* N_j` positions would be available to contain all good shells.

Therefore there exists a good shell with scale ratio

\[
\boxed{
K_j
:=q^{k_j/2}
\ge
q^{\rho_*N_j/4}
\to\infty
}
\]

whenever

\[
N_j\to\infty.
\]

This shell has fixed cubic occupancy and hence natural kinetic packet mass

\[
\|f_j(t_j)\|_2
\gtrsim
R_j^{1/2},
\qquad
R_j:=R_{j,k_j}.
\]

---

## 4. Non-H forces a fixed natural-frequency component at t_j

Apply the compact solenoidal localization at the good shell scale `R_j`.

If the normalized derivative ratio is large, the shell is already routed to `H`.

On the non-H lane, the phase-space lemma gives fixed constants `a,b,beta_*>0` such that

\[
\boxed{
\|P_jf_j(t_j)\|_2
\ge
\beta_*\|f_j(t_j)\|_2
\ge
c_fR_j^{1/2},
}
\]

where `P_j` projects to

\[
\frac a{R_j}<|\xi|<\frac b{R_j}.
\]

Thus the old good shell present at `t_j` contains a nondegenerate natural-frequency packet.

---

## 5. Sliding history requires this shell eventually to be forgotten

A genuine sliding/forgetful history satisfies

\[
N_j\to\infty,
\qquad
j-N_j\to\infty.
\]

The second condition means that the oldest retained stage index tends to infinity. Consequently every fixed historical shell index eventually leaves the remembered window.

For the good shell selected at time `t_j`, let `t_j^f<T*` be a later time at which its original natural-band packet has been strongly forgotten:

\[
\|P_jf_j(t_j^f)\|_2
\le
\varepsilon
\|P_jf_j(t_j)\|_2,
\]

with a fixed `epsilon<1`, after accounting for the moving shell packet definition.

Necessarily

\[
0<t_j^f-t_j
\le
T^*-t_j
\le
C_Tr_j^2.
\]

In units of the old shell's own natural time,

\[
\boxed{
\tau_j^f
:=
\frac{t_j^f-t_j}{R_j^2}
\le
C_TK_j^{-2}
\to0.
}
\]

Thus the sliding window demands that a genuinely occupied old shell be erased in a vanishing fraction of its natural time.

---

## 6. Exact forgetting gate on the compressed interval

The localized packet evolution gives

\[
(\partial_t-\nu\Delta)f_j
=\mathcal N_j+\mathcal R_j.
\]

Because the available time is at most `C_T r_j^2`, the heat attenuation on the old shell's band is bounded below by

\[
\eta_j
=
\exp\left[-\nu b^2\frac{t_j^f-t_j}{R_j^2}\right].
\]

Using the remaining-time bound,

\[
\boxed{
\eta_j
\ge
\exp(-\nu b^2C_TK_j^{-2})
\to1.
}
\]

Therefore strong forgetting requires

\[
\boxed{
\int_{t_j}^{t_j^f}
\left(
\|P_j\mathcal N_j\|_2
+
\|P_j\mathcal R_j\|_2
\right)dt
\ge
(\eta_j-\varepsilon)
\|P_jf_j(t_j)\|_2.
}
\]

For all sufficiently large `j`, `eta_j-epsilon` is bounded below by a fixed positive constant `c_epsilon`.

Hence

\[
\boxed{
\int_{t_j}^{t_j^f}
\left(
\|P_j\mathcal N_j\|_2
+
\|P_j\mathcal R_j\|_2
\right)dt
\ge
c_*R_j^{1/2}.
}
\]

---

## 7. Quiet natural-scale forcing cannot pay in the remaining time

Suppose the candidate stays in the quiet non-H/non-T/non-pressure corridor at the old shell scale. Then there is a scale-independent `K_*` such that

\[
\boxed{
\|P_j\mathcal N_j(t)\|_2
+
\|P_j\mathcal R_j(t)\|_2
\le
K_*R_j^{-3/2}
}
\]

through the forgetting interval.

The total action available before `T*` is then at most

\[
\begin{aligned}
\int_{t_j}^{t_j^f}
(\cdots)dt
&\le
K_*R_j^{-3/2}(T^*-t_j)\\
&\le
K_*C_Tr_j^2R_j^{-3/2}.
\end{aligned}
\]

Since

\[
r_j=R_j/K_j,
\]

this becomes

\[
\boxed{
\int_{t_j}^{t_j^f}(\cdots)dt
\le
K_*C_TK_j^{-2}R_j^{1/2}.
}
\]

Comparing with the required lower action gives

\[
\boxed{
c_*
\le
K_*C_TK_j^{-2}.
}
\]

Equivalently,

\[
\boxed{
K_j^2
\le
\frac{K_*C_T}{c_*}.
}
\]

But the selected good old shell satisfies

\[
K_j\to\infty.
\]

Contradiction.

Thus a sliding historical shell cannot be forgotten while all old-shell forcing channels remain at their natural quiet size.

---

## 8. Exact branch consequence

For sufficiently late stages with `N_j` large, the selected good old shell must satisfy at least one of:

1. large normalized derivative ratio at `t_j` -> `H`;
2. internal localized nonlinear action exceeds the quiet ceiling -> nonlinear turnover `T_NL`;
3. material shell crossing exceeds the quiet ceiling -> `T`;
4. pressure transfer across the shell buffer exceeds the quiet ceiling -> pressure/T branch;
5. viscous boundary leakage or Bogovskii correction action exceeds the quiet ceiling -> shell leakage / derivative-turnover branch.

The independent quiet sliding survivor is therefore eliminated:

\[
\boxed{
\text{sliding history}
+
\text{logarithmic occupied-shell count}
+
\text{non-H/T quiet forcing}
\quad\text{is impossible.}
}
\]

This is a local remaining-time argument, not a global stage-sum argument.

---

## 9. Why this avoids the old critical-budget failure

Earlier global packing attempts failed because a physical natural packet costs only `O(r)` energy/dissipation, and

\[
\sum r_j<\infty.
\]

The present argument does not sum those costs.

Instead, at a **single late time** `t_j`, it selects one already-existing old shell with

\[
R_j/r_j=K_j\to\infty
\]

and observes that the future time available to erase it is only

\[
O(r_j^2)=O(K_j^{-2}R_j^2).
\]

The contradiction is therefore between

- a fixed positive natural-time forgetting requirement; and
- a vanishing `K_j^-2` fraction of one natural time remaining.

No finite global critical functional is needed for this reduction.

---

## 10. Remaining theorem-level caveats

The reduction is strong but not yet a completed global regularity proof. To promote it to a mainline S-level closure, the following must be written with explicit constants:

1. the time-dependent Bogovskii packet on the moving shell;
2. a uniform bound translating the quiet `H/T/pressure` hypotheses into
   \[
   \|P_j\mathcal N_j\|_2+\|P_j\mathcal R_j\|_2
   \le K_*R_j^{-3/2};
   \]
3. a precise definition of strong shell forgetting consistent with the sliding-history ledger;
4. verification that the selected positive-density good shell remains identifiable until it exits the remembered window;
5. routing of any failure of the forcing ceiling into already accepted quantitative `H/T/residual/pressure` exits.

These are now finite smooth localization estimates rather than an unknown global Liouville theorem.

---

## 11. Current status

The historical-shell route has undergone the following reductions:

\[
\text{weak-L3 historical tail}
\]

\[
\Downarrow
\]

\[
\text{positive critical log-radial derivative cost}
\]

\[
\Downarrow
\]

\[
\text{persistent history -> Hardy-gap flux/T}
\]

\[
\Downarrow
\]

\[
\text{sliding history}
\]

\[
\Downarrow
\]

\[
\text{good old shell with forced natural frequency}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{remaining time}/\text{old natural time}
\lesssim K^{-2}\to0
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{quiet forgetting impossible}
}
\]

Status: **THE SLIDING/FORGETFUL HISTORY IS NO LONGER AN INDEPENDENT QUIET ESCAPE ROUTE. FOR LATE LARGE SCALE-SEPARATION IT MUST ACTIVATE H, T, PRESSURE/RESIDUAL, OR A LARGE LOCALIZATION-BOUNDARY ACTION. GLOBAL REGULARITY REMAINS UNPROVED BECAUSE THOSE TYPED EXIT BRANCHES AND THE QUIET-FORCING CONSTANT AUDIT STILL REQUIRE FULL S-LEVEL CLOSURE.**
