# DSD M5-410 — Finite phase-memory carrier reuse cannot self-source a genuinely remote natural strain

Date: 2026-08-31

Status: **A FIXED FINITE COLLECTION OF NATURAL-STRENGTH COHERENT CARRIERS CANNOT, BY REPEATED REUSE ALONE, SUPPLY ORDER-ONE NATURAL STRAIN TO A TARGET THAT IS REMOTE IN THE TARGET'S OWN NATURAL SCALE / A LOCALIZED CARRIER OF SCALE `r` AT DISTANCE `d` CONTRIBUTES AT MOST `~ nu r/d^3`, OR `~nu/r^2` IN THE COARSE-CONTAINING CASE, BOTH NEGLIGIBLE COMPARED WITH THE TARGET NATURAL STRAIN `nu/s^2` UNDER PHASE-SPACE SEPARATION / THEREFORE THE FINITE-PHASE-MEMORY BRANCH OF M5-409 MUST RECRUIT AN EXTENDED/DIFFUSE SHELL RESERVOIR, LOSE NATURAL CARRIER CONTROL, OR CROSS A LOCALIZATION/PROJECTIVE INTERFACE / THE RESERVOIR IS ROUTED BY THE EXISTING ANGULAR/SHELL LEDGERS TO NEW PHASE-SPACE NOVELTY, CRITICAL SHELL H, OR REMOTE ACTIVITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-409 reduced arbitrarily long remote recursion to

\[
S_{remote}^{iterated}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor
R_{remote}^{finite\ phase\ memory}
\lor
H_{local}^{crit}
\lor
T_{interface}.
\]

The only genuinely new reuse label is

\[
R_{remote}^{finite\ phase\ memory}.
\]

It represents arbitrarily long recursive remote paths that revisit only finitely many effective position-scale cells.

This note asks whether those finitely many natural-strength carrier cells can themselves supply the remote/ambient strain that keeps the recursion active.

The answer is no under the retained coherent natural-carrier description.

---

## 2. Target and source carrier scales

Let the target carrier `A` have natural scale

\[
s>0
\]

and center `x_A`.

Its natural vorticity and strain scales are

\[
\boxed{
W_A\asymp\frac\nu{s^2},
\qquad
S_A^{nat}\asymp\frac\nu{s^2}.
}
\]

Let a reused source carrier `B` have natural scale

\[
r>0,
\]

center `x_B`, and distance

\[
d:=|x_A-x_B|.
\]

Retain the natural-strength carrier bounds on one coherent localized component:

\[
|\omega_B|
\le C_0\frac\nu{r^2}
\]

on a region of diameter `O(r)`, with corresponding fixed normalized derivative bounds when the target lies inside the smooth carrier buffer.

If these carrier bounds fail, the event is already

\[
H_{local}^{crit}
\lor T_{interface}.
\]

---

## 3. Far localized carrier estimate

Assume first that the target is outside a fixed enlargement of the source carrier:

\[
d\ge C_1r.
\]

The strain kernel satisfies

\[
|K(x)|\lesssim |x|^{-3}.
\]

The localized carrier vorticity has L1 mass

\[
\begin{aligned}
\|\omega_B\|_1
&\lesssim
\frac\nu{r^2}\,r^3\\
&\lesssim
\boxed{\nu r.}
\end{aligned}
\]

Therefore its contribution to the target strain obeys

\[
\boxed{
|S_{B\to A}|
\lesssim
\frac{\nu r}{d^3}.
}
\]

Normalize by the target natural strain:

\[
\frac{|S_{B\to A}|}{\nu/s^2}
\lesssim
\boxed{
\frac rd\left(\frac sd\right)^2.
}
\]

If the edge is genuinely remote in the target scale,

\[
\frac ds\to\infty,
\]

and `r<=Cd`, then

\[
\boxed{
\frac{|S_{B\to A}|}{S_A^{nat}}
\to0.
}
\]

Thus a remote natural packet cannot drive an order-one target natural strain through its localized vorticity field.

---

## 4. Coarse source carrier containing or surrounding the target

The only geometric case not covered by the far estimate is

\[
r\gg d.
\]

Because the remote edge still has

\[
d\gg s,
\]

we then have the strong scale separation

\[
\boxed{r\gg s.}
\]

Inside a smooth natural carrier of scale `r`, the retained normalized analyticity bounds give schematically

\[
|\omega_B|\lesssim\frac\nu{r^2},
\qquad
|\nabla\omega_B|\lesssim\frac\nu{r^3}.
\]

The Calderon--Zygmund near/far split at any point of the interior carrier buffer therefore gives

\[
\boxed{
|S_B(x_A)|
\lesssim
C\frac\nu{r^2}
}
\]

up to at most a harmless logarithmic factor if one keeps a broader intermediate annulus instead of the fixed normalized buffer.

Consequently

\[
\boxed{
\frac{|S_B(x_A)|}{S_A^{nat}}
\lesssim
\left(\frac sr\right)^2
\left[1+\log\frac rs\right]
\to0.
}
\]

Thus a much coarser reused carrier is also too weak, in target-natural units, to supply the target's required order-one strain.

---

## 5. Comparable scales

If

\[
r\asymp s,
\]

then a remote edge implies

\[
d\gg r\asymp s.
\]

The far estimate gives directly

\[
\boxed{
\frac{|S_{B\to A}|}{S_A^{nat}}
\lesssim
\left(\frac sd\right)^3
\to0.
}
\]

So comparable-scale remote carriers decouple even faster.

---

## 6. Finite reused populations have vanishing total remote influence

Suppose the remote recursion revisits only

\[
N_*<\infty
\]

effective natural carrier cells.

At a target remote stage, decompose the vorticity schematically into

\[
\boxed{
\omega
=
\sum_{i=1}^{N_*}\omega_i^{carrier}
+
\omega_{res}.
}
\]

Here each carrier term is localized with a smooth cutoff adapted to its retained natural cell.

The cutoff-transition corrections are not ignored; if they are large, they are typed as

\[
T_{interface}
\lor H_{boundary/derivative}.
\]

On the corridor where the decomposition remains quiet, Sections 3--5 imply that every carrier which is phase-space remote from the target contributes `o(S_A^{nat})`.

Since `N_*` is fixed,

\[
\boxed{
\sum_{i=1}^{N_*}
|S_{i\to A}|
=o(S_A^{nat}).
}
\]

Therefore a fixed finite carrier population cannot be the entire source of a repeatedly required order-one remote/ambient target strain.

---

## 7. A residual reservoir is mandatory

If the target still receives an order-one natural strain contribution, then

\[
\boxed{
|S[\omega_{res}](x_A)|
\gtrsim
c\frac\nu{s^2}
}
\]

along a subsequence.

The residual cannot be dismissed as `background`.

It is exactly the additional scale-space content that the finite carrier-memory hypothesis failed to count.

Apply the existing source-scale decomposition to this residual contribution:

1. natural-scale residual source;
2. subnatural/frequency residual source;
3. remote residual source;
4. diffuse multiscale shell spread;
5. localization/projective correction.

These are already routed by M5-362, M5-376--377, M5-392, M5-400--402 and the later carrier formation notes.

---

## 8. Natural residual source creates a new carrier cell

If a fixed fraction of the residual productive source lies at the target natural scale, M5-394 plus stage/local analyticity upgrades it to a coherent companion carrier with physical flux

\[
\Phi\gtrsim c\nu.
\]

If this carrier is not equivalent to one of the finitely reused phase-space cells, then phase-space novelty has increased.

If it is equivalent to an old cell, then it is not genuinely residual and should have been absorbed into the finite carrier sum, modulo a large interface/cutoff defect.

Thus

\[
\boxed{
\text{natural residual}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor T_{interface}.
}
\]

---

## 9. Subnatural or rough residual source

If the residual strain is supplied at scales much smaller than the target natural scale, the source is a relative-frequency/capacity event.

After M5-392 this should not be interpreted as parent-scale pointwise derivative blowup.

The surviving statement is

\[
\boxed{
\text{subnatural residual}
\Longrightarrow
H_{shell/frequency/capacity}^{crit}.
}
\]

Such an event may itself point-pick to another formed natural carrier at its own smaller scale, returning to the critical atom ledger.

---

## 10. Remote or diffuse residual source

If the residual source is carried at distance much larger than the target natural scale, it is already

\[
S_{remote}^{new}.
\]

If no bounded set of dyadic source scales carries a fixed fraction, then the residual is a genuine multiscale shell reservoir.

The older scale-distribution audits show that one may not sum the same shell mass repeatedly. The correct label is

\[
\boxed{
H_{shell/distributed}^{crit}
\lor S_{remote}^{new},
}

until a separated critical carrier can be extracted.

Thus a finite reused carrier set cannot hide a diffuse reservoir by calling it the same ancestry.

---

## 11. Consequence for finite phase memory

Combining the previous sections,

\[
\boxed{
R_{remote}^{finite\ phase\ memory}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor
H_{shell/frequency/capacity}^{crit}
\lor
S_{remote}^{new}
\lor
T_{interface}.
}
\]

But `S_remote^new` is precisely another phase-space source which, under further recursion, is again subjected to the M5-409 novelty/reuse dichotomy.

Therefore there is no self-contained quiet mechanism consisting only of endlessly reusing a fixed finite set of natural carrier cells.

The recursion must continuously recruit new critical phase-space content or pay an already typed local/interface H/T cost.

---

## 12. Important source-versus-object distinction

This theorem does **not** say that two finite remote vortices can never interact.

It says something narrower:

> a fixed finite collection of natural-strength localized carriers whose phase-space separation from the target tends to infinity cannot provide an order-one fraction of the target's own natural strain scale.

A broad extended vortex structure may have far more source mass than one natural carrier cell.

Such an extended structure is exactly the residual shell reservoir retained in Sections 7--10 and must be priced separately.

This is a DSD source/object distinction: one formed local carrier is not equivalent to the whole nonlocal field that may surround it.

---

## 13. Updated remote recursion

M5-409 gave

\[
S_{remote}^{iterated}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor
R_{remote}^{finite\ phase\ memory}
\lor
H_{local}^{crit}
\lor
T_{interface}.
\]

The present note removes the finite-memory leaf as a self-sourcing terminal:

\[
\boxed{
S_{remote}^{iterated}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor
H_{shell/frequency/capacity}^{crit}
\lor
T_{interface}
\lor
\text{continued fresh remote recruitment}.
}
\]

Continued fresh remote recruitment is no longer conceptually distinct from unbounded phase-space novelty once well-formed carriers are extracted; failure of extraction is itself shell/localization H/T.

Thus the remote hard core is being absorbed into a single critical scale-space throughput problem.

---

## 14. Firewall

- The carrier decomposition is not canonical. Large cutoff/overlap corrections are explicitly `T_interface/H_boundary` rather than ignored.
- A broad extended reservoir is not approximated by one natural packet.
- The far decay estimate applies to the localized carrier contribution, not to the entire original vorticity field.
- No claim is made that `H_{dot H1/2}` is globally bounded.
- No time-summation of critical atoms is performed.

---

## 15. Audit verdict

### DERIVED

- remote influence of one natural localized carrier is negligible in target-natural units;
- a much coarser smooth carrier is also negligible because its strain scale is `nu/r^2`;
- a fixed finite reused carrier set cannot self-supply repeated remote natural strain;
- a residual extended source is mandatory;
- the residual routes to fresh critical carrier novelty, shell/frequency H, further remote recruitment, or interface action.

### REMOVED AS QUIET TERMINAL

\[
\boxed{R_{remote}^{finite\ phase\ memory}.}
\]

### CURRENT HARD CORE

A genuine survivor must keep generating new critical phase-space content or pay local/interface critical action.

This is a stronger unification of `H_local^crit` and `S_remote^iterated`, but it is not a global contradiction because the common critical throughput can still diverge.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]