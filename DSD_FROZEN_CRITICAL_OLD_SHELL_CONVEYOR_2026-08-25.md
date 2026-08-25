# DSD Frozen Critical Old-Shell Conveyor

Date: 2026-08-25

Status: **QUIET OLD-SHELL ONE-STAGE VARIATION `O(q^-k)` DERIVED / TOTAL FUTURE VARIATION SUMMABLE / OLD CRITICAL SHELLS FREEZE RATHER THAN FORGET / ORDINARY ENERGY CLOSURE AUDITED AS SCALE-COMPATIBLE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The remaining bounded-`Z` obstruction is a locally recurrent active core accompanied by a passive critical tail.

The repository already proves that a natural-frequency old shell cannot be strongly forgotten over its own natural remaining-time window without an order-one nonlinear Duhamel action.

The present note asks a sharper question:

> If a shell is already old by `k` first-hitting generations, how much can it change during the **next current stage**, and over all later stages combined?

The answer is that on the quiet old-shell corridor the relative variation is `O(q^-k)` in one current stage and remains `O(q^-k)` after summing the entire future. Thus the final passive tail is naturally a frozen physical shell stack.

---

## 2. Exact age/radius relation

Use

\[
W_j=q^jW_0,
\qquad
r_j=\sqrt{\frac\nu{W_j}}.
\]

An age-`k` shell at current stage `j` has physical radius comparable to

\[
\boxed{
\rho_{j,k}=r_{j-k}=q^{k/2}r_j.
}
\]

At the next stage,

\[
\rho_{j+1,k+1}
=r_{(j+1)-(k+1)}
=r_{j-k}
=\rho_{j,k}.
\]

Hence

\[
\boxed{
\rho_{j+1,k+1}=\rho_{j,k}
}
\]

exactly: the same physical scale is relabeled by `k -> k+1` when the first-hitting normalization advances one generation.

This is the discrete physical content of the Leray dilation conveyor.

---

## 3. Current-stage time is `q^-k` of the old shell natural time

The normalized current-stage length obeys

\[
L_j\le L_+.
\]

Therefore its physical duration is

\[
\Delta t_j
\le
\frac{L_+}{W_j}.
\]

The age-`k` old shell has natural parabolic time

\[
\rho_{j,k}^2
=
\frac\nu{W_{j-k}}
=
\frac{\nu q^k}{W_j}.
\]

Thus

\[
\boxed{
\frac{\Delta t_j}{\rho_{j,k}^2}
\le
\frac{L_+}{\nu}q^{-k}
=:C_tq^{-k}.
}
\]

For large `k`, one current first-hitting stage is an exponentially small fraction of the old shell's natural evolution time.

Status: **PROVED.**

---

## 4. Imported quiet forcing scale

The old-shell forcing audit gives, after divergence-free localization and projection to the dynamically relevant shell component,

\[
\boxed{
\|F_{j,k}(t)\|_2
\le
K_*\rho_{j,k}^{-3/2}
}
\]

through a quiet old-shell stage, where `K_*` depends only on the already typed scale-invariant amplitude, derivative, pressure, and frame constants.

If this bound fails, the shell has already exited to an `H`, `T`, pressure, drift, or analyticity branch and is not part of the passive-tail survivor.

---

## 5. Natural-frequency packet

Let `P_rho` be a smooth band projection to

\[
\frac{c_f}{\rho}
\le |\xi|\le
\frac{C_f}{\rho}.
\]

Let `f_{j,k}` be the localized solenoidal old-shell packet.

On the natural-frequency occupied branch assume

\[
\boxed{
\beta_-\rho^{1/2}
\le
\|P_\rho f_{j,k}(t_j)\|_2
\le
\beta_+\rho^{1/2}
}
\]

with fixed positive constants `beta_-`, `beta_+`.

Failure of the lower occupancy bound is the already typed low/high-frequency escape branch.

---

## 6. Heat variation during one current stage

On the natural band,

\[
|\xi|^2\le C_f^2\rho^{-2}.
\]

Hence

\[
|e^{-\nu\Delta t_j|\xi|^2}-1|
\le
\nu\Delta t_j|\xi|^2
\le
C_f^2\nu\frac{\Delta t_j}{\rho^2}.
\]

Using the age-time ratio,

\[
\boxed{
\|(e^{\nu\Delta t_j\Delta}-I)P_\rho f_{j,k}(t_j)\|_2
\le
C_{heat}q^{-k}
\|P_\rho f_{j,k}(t_j)\|_2.
}
\]

Status: **PROVED.**

---

## 7. Duhamel forcing variation during one current stage

The Duhamel forcing contribution obeys

\[
\begin{aligned}
\left\|
\int_{t_j}^{t_{j+1}}
 e^{\nu(t_{j+1}-s)\Delta}
P_\rho F_{j,k}(s)ds
\right\|_2
&\le
K_*\rho^{-3/2}\Delta t_j\\
&\le
K_* C_t q^{-k}\rho^{1/2}.
\end{aligned}
\]

Therefore, relative to the occupied packet size,

\[
\boxed{
\frac{\text{forcing variation}}
{\|P_\rho f_{j,k}(t_j)\|_2}
\le
C_{force}q^{-k}.
}
\]

Status: **PROVED.**

---

## 8. One-stage frozen-shell estimate

Combining heat and forcing terms gives

\[
\boxed{
\|P_\rho f_{j+1,k+1}(t_{j+1})
-P_\rho f_{j,k}(t_j)\|_2
\le
C_{fr}q^{-k}\rho^{1/2}.
}
\]

Whenever the lower natural-band occupancy is active,

\[
\boxed{
\frac{
\|P_\rho f_{j+1,k+1}-P_\rho f_{j,k}\|_2
}{
\|P_\rho f_{j,k}\|_2
}
\le
C_{rel}q^{-k}.
}
\]

Thus an age-`k` old shell changes by only an exponentially small relative amount in the next current stage.

---

## 9. Total future variation is summable

After `h` more first-hitting stages, the same physical shell has age

\[
k+h.
\]

The corresponding relative variation is bounded by

\[
C_{rel}q^{-(k+h)}.
\]

Summing the future geometric series,

\[
\sum_{h=0}^{\infty}q^{-(k+h)}
=
\frac{q^{-k}}{1-q^{-1}}.
\]

Therefore the total future relative variation of a sufficiently old quiet shell satisfies

\[
\boxed{
\operatorname{Var}_{future}(k)
\le
\frac{C_{rel}}{1-q^{-1}}q^{-k}.
}
\]

In particular,

\[
\boxed{
\operatorname{Var}_{future}(k)\to0
\qquad(k\to\infty).
}
\]

Status: **PROVED on the quiet natural-frequency old-shell corridor.**

---

## 10. Interpretation: frozen physical shells

The final passive tail does not need to be continually destroyed and rebuilt.

Once a shell becomes sufficiently old, it may remain almost fixed in physical coordinates all the way to the hypothetical singular time, while the shrinking first-hitting normalization relabels it at larger and larger similarity radius.

Thus

\[
\boxed{
\text{old physical shell nearly frozen}
\quad\Longleftrightarrow\quad
\text{outward normalized critical conveyor}.
}
\]

This explains why local core recurrence and normalized tail escape are compatible without a large local forcing channel.

---

## 11. Strong forgetting is separated from passive freezing

The earlier Duhamel forgetting lemma says that reducing a natural-band packet by a fixed order-one fraction requires a scale-independent nonlinear action.

The present estimate says the quiet dynamics instead changes an old packet only by `O(q^-k)`.

Hence for sufficiently large `k`, the two alternatives are sharply separated:

\[
\boxed{
\text{quiet shell}
\Rightarrow\text{frozen persistence},
}
\]

while

\[
\boxed{
\text{order-one forgetting}
\Rightarrow T/H/\text{nonlinear action}.
}
\]

There is no intermediate silent strong-forgetting regime.

---

## 12. Ordinary energy audit

The frozen critical model has

\[
|u(r)|\sim r^{-1},
\qquad
|\nabla u(r)|\sim r^{-2}.
\]

On a physical dyadic shell of radius `rho`,

\[
\int_{A_\rho}|\nabla u|^2dx
\sim\rho^{-1}.
\]

For an age-`k` shell during current stage `j`,

\[
\rho=q^{k/2}r_j,
\qquad
\Delta t_j\lesssim r_j^2/\nu
\]

up to fixed first-hitting constants. Its ordinary dissipation payment over that current stage therefore has scale

\[
\Delta t_j
\int_{A_\rho}|\nabla u|^2
\lesssim
r_j q^{-k/2}
\]

up to fixed viscosity/constants.

The age sum is geometric,

\[
\sum_{k\ge0}q^{-k/2}<\infty,
\]

and the stage radii `r_j` also decay geometrically.

Therefore the frozen `1/r` conveyor is compatible with a finite ordinary energy-dissipation budget.

Status: **SCALING AUDIT / NO ENERGY CONTRADICTION.**

---

## 13. Function-space endpoint

On the spatial Type-I subbranch,

\[
|U(Y,s)|\lesssim (1+|Y|)^{-1}.
\]

This is compatible with

\[
U\in L^{3,\infty}
\]

but not with strong global `L3` for a nonzero asymptotic critical coefficient.

Thus the frozen conveyor lands exactly at the Lorentz endpoint already isolated in `ANCIENT_TAIL_LORENTZ_ENDPOINT_REFINEMENT_2026-08-24.md`.

---

## 14. DSD verdict

### CLOSED

- quiet old shell does not change by order one in one late current stage;
- the future variation of an age-`k` shell is summable and tends to zero as `k -> infinity`;
- silent strong forgetting is excluded;
- ordinary energy does not eliminate the frozen critical conveyor by scaling alone.

### REMAINING

The genuine final tail is now more sharply typed as

\[
\boxed{
\text{frozen physical critical shell stack}
\equiv
\text{normalized weak-}L^3\text{ endpoint conveyor}.
}
\]

Eliminating it requires a critical endpoint rigidity mechanism, a canonical tail subtraction with an exact core theorem, or a local self-similar-speed regularity gate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
