# DSD M17-117 — Ribbon fresh-carrier turnover meets the same physical return-density firewall as M5 genealogy

Date: 2026-09-05
Canonical ID: **M17-117**

Status: **INTERNAL M17/M5 GENEALOGY BRIDGE / M17-116 GIVES AN EXACT `3/2` GROWTH OF THE PER-DIRECTOR-AREA-FLUX VOLUME OF EVERY CLOSED MATERIAL KERNEL LOOP, SO A COMPACT NONDEGENERATE CRITICAL-RIBBON LOOP HAS A UNIFORM FINITE SIMILARITY-TIME RESIDENCE AND CANNOT REENTER THE SAME COMPACT RIBBON CLASS AFTER ITS PER-FLUX VOLUME HAS AGED PAST THE CLASS BOUND. AN EULERIAN RECURRENT RIBBON CORE THEREFORE NEEDS CONTINUAL SUPPLY OF FRESH MATERIAL LOOP LABELS. HOWEVER, THE EXISTING M5 ANCESTOR-RADIUS / WEIGHTED RETURN-DENSITY AUDIT SHOWS THAT O(1) PERSISTENCE IN THE CURRENT SIMILARITY EPOCH DOES NOT AUTOMATICALLY GIVE THE PHYSICAL DISSIPATION WEIGHT NEEDED FOR CONTRADICTION. FOR AN AGE-k STRUCTURE AT PHYSICAL RADIUS `rho_k=r_j K_k=r_{j-k}`, A CURRENT-EPOCH PHYSICAL DWELL `tau~r_j^2` CONTRIBUTES ONLY `tau/rho_k~rho_k/K_k^2`, LOSING `K_k^-2`. THUS FAST FRESH-RIBBON TURNOVER AND FINITE MATERIAL RESIDENCE DO NOT BY THEMSELVES CLOSE THE LERAY ENERGY LEDGER. THE NEW COMMON MISSING THEOREM IS A TEMPORAL/AMPLITUDE GENEALOGY BRIDGE FROM DIRECTOR-AREA FRESH-CARRIER SUPPLY TO SUFFICIENT PHYSICAL WEIGHTED RETURN DENSITY AT THE ANCESTRAL SCALE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Uniform similarity-age bound for a compact ribbon class

On the complete circular critical-ribbon branch, M17-116 gives

\[
\boxed{
\mathscr V_J(\theta)
=\oint\frac{ds}{|J_\xi|}
=e^{\frac32(\theta-\theta_0)}
\mathscr V_J(\theta_0).
}
\]

Suppose a compact nondegenerate ribbon class has

\[
0<c_J\le|J_\xi|\le C_J,
\qquad
0<c_q\le|q|\le C_q.
\]

Since a ribbon fiber is a circle of length

\[
L_k=\frac{2\pi}{|q|},
\]

we have

\[
\boxed{
\frac{2\pi}{C_qC_J}
\le
\mathscr V_J
\le
\frac{2\pi}{c_qc_J}.
}
\]

Therefore one material loop can remain inside this compact ribbon class for at most

\[
\boxed{
\tau_{rib}
\le
\frac23
\log\left(
\frac{C_qC_J}{c_qc_J}
\right).
}
\]

This is a uniform **similarity-time upper residence bound**.

---

## 2. One-way material aging

The growth law for `mathscr V_J` holds whether or not the loop is currently inside the chosen Eulerian core.

Therefore after a loop's per-flux volume exceeds the compact-class upper bound, the same material loop cannot later reenter that same compact nondegenerate ribbon class unless one of the defining bounds is lost.

Thus repeated Eulerian ribbon recurrence requires a continuing supply of material loops whose `mathscr V_J` has not yet aged beyond the retained class.

This is stronger than mere exit/reentry freedom:

\[
\boxed{
\text{same compact ribbon class}
\Longrightarrow
\text{one-way material age conveyor}.
}
\]

---

## 3. Similarity-time turnover is not physical-time dissipation

A tempting closure is

\[
\text{uniform finite similarity residence}
\Longrightarrow
\text{uniform positive physical energy cost per replacement}.
\]

This inference is false near a possible finite-time singular scale.

The rescaling compresses later similarity epochs into shorter physical time intervals.

Therefore the replacement rate must be translated into a scale-weighted physical genealogy before using the Leray energy ledger.

---

## 4. Existing M5 ancestor-radius identity

The repository's Ancestor-Radius Identity gives for first-hitting stages

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\]

and age factor

\[
K_k=q^{k/2}.
\]

An age-`k` structure observed at current stage `j` sits at physical radius

\[
\boxed{
\rho_k
=r_jK_k
=r_{j-k}.
}
\]

Thus the spatial scale correspondence to the ancestral first-hitting scale is exact.

---

## 5. Current-epoch dwell suffers the same remote-age loss

An `O(1)` similarity-time dwell at the current stage corresponds to a physical duration of order

\[
\boxed{
\tau_{phys}\asymp r_j^2
}
\]

up to the fixed normalization constants of the rescaling.

For the age-`k` physical radius

\[
\rho_k=r_jK_k,
\]

the weighted return-density contribution is therefore only

\[
\begin{aligned}
\frac{\tau_{phys}}{\rho_k}
&\asymp
\frac{r_j^2}{r_jK_k}\\
&=\frac{r_j}{K_k}\\
&=\frac{\rho_k}{K_k^2}.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{\tau_{phys}}{\rho_k}
\text{ carries the loss }
K_k^{-2}=q^{-k}.
}
\]

This is exactly the remote-age loss already isolated by the M5 weighted return-density audit.

---

## 6. Why frequent fresh loops are still not enough

M17-116 says an Eulerian recurrent ribbon core needs fresh material carriers in similarity time.

But if each fresh appearance is seen only during a current-epoch physical window of size `r_j^2`, then the cumulative physical weighted return may remain summable across remote ages.

Therefore

\[
\boxed{
\text{high similarity-time replacement frequency}
\not\Rightarrow
\text{large enough physical weighted return density}.
}
\]

No Leray dissipation contradiction follows from the residence upper bound alone.

---

## 7. Conditional energy closure target

The existing M5 weighted return-density ledger has the form

\[
\boxed{
\sum_kJ_k\mathfrak R_k<\infty
}
\]

under its shell-amplitude/comparability and bounded-overlap hypotheses.

On a subset carrying divergent cubic mass,

\[
\sum_{k\in S}J_k^{3/2}=\infty,
\]

it would be enough to prove

\[
\boxed{
\mathfrak R_k
\gtrsim
J_k^{1/2}.
}
\]

Thus a ribbon-based closure would need a theorem of the form

\[
\boxed{
\text{fresh director-area ribbon carrier at stage }j
\Longrightarrow
\text{sufficiently long/repeated physical activity near }r_{j-k}
}
\]

for a cubic-divergent family of ages.

M17-116 does not provide this lower dwell/return statement; it provides an upper material residence time.

---

## 8. Exact point of convergence between M5 and M17

The M5 and M17 analyses now meet at the same missing bridge:

### M17 supplies

- exact carrier identity `dPhi_J`;
- finite same-material ribbon residence;
- one-way per-flux-volume aging;
- necessity of fresh Eulerian carriers.

### M5 supplies

- exact ancestral physical radius;
- finite weighted physical return-density ledger;
- a conditional cubic-tail contradiction if return density is large enough.

### Missing

\[
\boxed{
\text{similarity carrier replacement}
\to
\text{ancestral physical return density lower bound}.
}
\]

This is a temporal/amplitude theorem, not another spatial-scale matching problem.

---

## 9. DSD analysis

The two theories use different time descriptors:

\[
\boxed{
\text{similarity material age}
\neq
\text{physical dissipation dwell}.
}
\]

M17-116 controls the first.
M5's energy closure needs the second.

The exact ancestor-radius identity aligns the spatial scale but does not identify the required temporal genealogy.

---

## 10. DSD audit

### Audit A — converting a similarity-time residence upper bound into a physical dwell lower bound
Rejected.

### Audit B — assuming fresh ribbon carriers are automatically distinct expensive energy packets
Rejected. Physical cost must be derived with scale and overlap control.

### Audit C — re-deriving the ancestor radius
Not needed; the existing exact identity is reused.

### Audit D — claiming the `K_k^-2` loss closes or destroys the ribbon branch
Rejected. It identifies the firewall; a stronger genealogy theorem may still overcome it.

### Audit E — proof status
M17 ribbon turnover and M5 weighted return density are now structurally connected, but the decisive lower physical return bound remains unproved.

---

## 11. Updated cross-module frontier

The complete compact same-material ribbon is closed by M17-116.
The Eulerian ribbon turnover survivor reduces to

\[
\boxed{
\text{fresh director-area carrier conveyor}
\stackrel{?}{\Longrightarrow}
\mathfrak R_k\gtrsim J_k^{1/2}
\text{ on a cubic-divergent subset}.
}
\]

If this implication is proved with the existing M5 hypotheses, the finite Leray weighted return ledger would close that turnover branch.

If it fails, the survivor is a sparse/nested fresh-carrier cascade whose physical return weight remains summable despite recurrent similarity geometry.

The next high-value work should target this temporal genealogy bridge or, in parallel, the Rank-1 global pressure covariance closure.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
