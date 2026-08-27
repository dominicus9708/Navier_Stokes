# DSD M5-158 — Flat-Fiber Stage Closure and Next-Gate Freeze

Date: 2026-08-27

Status: **STAGE CLOSURE / M5-145–157 ARE CONSOLIDATED INTO AN ACYCLIC W1-CONDITIONAL DAG / ALGEBRAIC SAME-TAIL FREEDOM IS CLOSED / ONLY FLAT SAME-TAIL FREEDOM REMAINS / PROXIMAL FLAT FIBERS ARE INVARIANT-MEASURE A.E. INVISIBLE / STATISTICAL FLAT FIBERS REQUIRE PARABOLIC CROSS-SECTION FREQUENCY ESCAPE / EXISTING UNIQUE-CONTINUATION RESULTS DO NOT YET CLOSE THAT BRANCH / NEXT CALCULATION IS FROZEN UNTIL EXPLICITLY RESUMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose of this note

This note does **not** introduce a new proof step.

Its purpose is to close the current work interval, freeze the dependency graph, and prevent later calculations from silently reusing rejected or merely conditional implications.

The accepted workflow remains

\[
\boxed{
\text{calculate}
\to
\text{Formation audit}
\to
\text{Axis audit}
\to
\text{Static aggregation audit}
\to
\text{Dynamics audit}
\to
\text{cross-audit}
\to
\text{branch/prune}.
}
\]

No downstream conclusion is allowed to return as an upstream premise.

---

## 2. Current W1 same-tail problem

Let `M` be the compact minimal W1 set and let

\[
\pi:M\to\mathcal T
\]

be the canonical tail factor.

For two states `V,W in M` with

\[
\pi(V)=\pi(W),
\]

define their difference

\[
Z:=V-W.
\]

Earlier work gives

\[
Z\in L^2\cap L^3,
\]

and the canonical tail carries the critical residue while `Z` carries zero cubic Abel residue.

The same-tail problem is therefore a **strong-critical fiber problem over one fixed critical tail**.

---

## 3. GREEN — algebraic fiber freedom is closed

M5-145 completed the all-orders Fuchsian/Taylor recursion.

If two same-tail states agree through order `n-1`, then the pressure difference at the next pressure order solves only the homogeneous pressure-Poisson equation.

The only bounded recurrent homogeneous mode is the realized odd spherical-harmonic resonance.

M5-144 proved every realized odd resonant coefficient is a continuous flow invariant and hence constant on the compact minimal set.

Therefore the pressure difference vanishes at that order, and the velocity equation has the nonresonant divisor

\[
\boxed{n\neq0}
\]

so the next velocity coefficient also agrees.

By induction,

\[
\boxed{
H_j^V=H_j^W,
\qquad
\Pi_j^V=\Pi_j^W
\quad\forall j<\infty.
}
\]

Hence

\[
\boxed{
P1_A\;\text{(algebraic same-tail freedom)}=\text{CLOSED}.
}
\]

This is a W1-conditional statement only.

---

## 4. GREEN — half-integer algebraic sectors are excluded for realized W1 trajectories

The Fuchsian variables satisfy

\[
\boxed{
z=\frac{T_*-t}{|x-x_*|^2}.}
\]

At fixed physical `x != x_*`, `z` is proportional to terminal time.

The punctured terminal solution is `C^\infty` in time, so half-integer powers

\[
z^{1/2},z^{3/2},\dots
\]

cannot appear in a realized terminal Taylor expansion.

Thus the Poisson-allowed even-multipole half-integer sectors are not actual W1 terminal sectors.

This leaves only the integer/odd algebraic sector already closed in Section 3.

---

## 5. GREEN — only flat same-tail differences remain

After Section 3,

\[
\boxed{
H^V-H^W=O(z^N)
\quad\forall N
}
\]

and similarly for the pressure difference on every audited punctured compact region.

Equivalently, with

\[
\xi=z^{-1}=r^2,
\]

the difference is superalgebraically small at normal infinity:

\[
\boxed{
Z=O(\xi^{-N})
\quad\forall N.
}
\]

The remaining same-tail problem is therefore

\[
\boxed{P1_B=\text{flat fiber only}.}
\]

---

## 6. GREEN — principal normal operator has no decaying flat free mode

For the normal scalar model, M5-146 found

\[
4\nu z^2f''+(1+6\nu z)f'=0,
\]

whose nonconstant branch grows like

\[
e^{+1/(4\nu z)}.
\]

M5-147 extended this to stretched exponentials

\[
e^{-c/z^\alpha},\qquad c>0,
\]

and found no decaying balance for any `alpha>0`.

In inverse-Fuchsian coordinates the principal normal operator is

\[
\boxed{
4\nu\partial_{\xi\xi}-\partial_\xi,
}
\]

whose homogeneous modes are constant or exponentially growing.

Therefore a nonzero flat fiber, if it exists, must be sustained by the full transport/stretching/Biot–Savart coupling rather than by a free normal viscous mode.

---

## 7. GREEN — pressure is not the essential flat-fiber obstruction

M5-149 passes to relative vorticity.

If

\[
K\sim r^2\,\nabla\times(V-W),
\]

then the pressure disappears from the relative equation.

Biot–Savart recovers the velocity difference from relative vorticity with one derivative of smoothing.

Thus it is enough to prove flat uniqueness at the relative-vorticity level:

\[
\boxed{
K\equiv0\Rightarrow V=W.
}
\]

---

## 8. GREEN — noninjective flat fibers split into two genuinely different dynamical branches

Let

\[
\mathcal R:=M\times_{\mathcal T}M
\]

be the same-tail relation.

M5-150 separates:

### Statistical branch

\[
\boxed{P1_B^S}
\]

There exists an invariant pair measure `rho` with

\[
\rho(\mathcal R\setminus\Delta)>0.
\]

### Proximal branch

\[
\boxed{P1_B^P}
\]

Every invariant pair measure on the same-tail relation is supported on the diagonal.

This split must remain explicit.  Noninjectivity alone does not grant off-diagonal recurrence.

---

## 9. GREEN — the proximal branch is invisible to invariant averages

M5-156 disintegrates any invariant measure `mu` over the tail factor:

\[
\mu=\int\mu_T\,d\nu(T).
\]

The relative independent joining

\[
\rho_\mu
=
\int\mu_T\otimes\mu_T\,d\nu(T)
\]

is an invariant measure on the same-tail relation.

On Branch `P1_B^P`, it must be diagonal.

Hence

\[
\boxed{
\mu_T\text{ is Dirac for }\nu\text{-a.e. }T.
}
\]

Therefore the tail factor is almost everywhere injective for **every invariant measure** on the proximal branch.

Consequently, all invariant-mean arguments may isolate `P1_B^P` as an exceptional topological branch rather than a statistical obstruction.

It is **not** pointwise eliminated.

---

## 10. GREEN — the statistical branch requires frequency escape

M5-154 rewrites the flat relative-vorticity equation in log-normal depth

\[
\tau=\log\xi.
\]

The leading equation is

\[
\boxed{
K_s+K_\tau
=
 e^{-\tau}
\left[
4\nu K_{\tau\tau}
-6\nu K_\tau
+\nu(2+\Delta_{S^2})K
-\mathcal N_s
\right].
}
\]

Thus the leading channel is translation, while all dissipative/coupling corrections carry the integrable coefficient `e^-tau`.

A nonzero state cannot decay beyond all algebraic orders under bounded cross-section frequency.

Therefore a nonzero statistical flat fiber requires

\[
\boxed{
\int^\infty e^{-\tau}\Omega(\tau)^2d\tau=\infty,
}
\]

hence a necessary parabolic-frequency escape of order roughly

\[
\boxed{
\Omega(\tau)\gtrsim e^{\tau/2}=r
}
\]

along arbitrarily deep normal scales.

This is a **necessary condition**, not yet a contradiction.

---

## 11. GREEN — fixed-time axial refactor removes an artificial genealogy derivative hierarchy

M5-151 initially produced a genealogy-derivative hierarchy.

M5-152 correctly showed that analytic compactness does not justify a same-norm estimate of the form

\[
\|\partial_s f\|\le C\|f\|.
\]

M5-153 then changes to the exact fixed-Leray-time coordinates `(xi,s)` and obtains the averaged relative-vorticity identity

\[
\boxed{
\begin{aligned}
0={}&2\nu E''
-4\nu A
-\left(\frac12+\frac\nu\xi\right)E'\\
&+\frac\nu{\xi^2}(2E-B_\theta)
-\frac1{\xi^2}\langle\mathcal N_s\cdot K\rangle.
\end{aligned}
}
\]

where

\[
E=\langle|K|^2\rangle,
\qquad
A=\langle|K_\xi|^2\rangle.
\]

Invariant pair averaging kills

\[
\langle K_s,K\rangle=0
\]

exactly.

Therefore the high-genealogy-derivative hierarchy is **not** part of the preferred Branch-S route.

M5-152 remains a valid RED firewall against using analyticity incorrectly.

---

## 12. GREEN / CONDITIONAL — uniform time analyticity exists, but only with radius loss

M5-155 records a uniform positive normalized time-analytic scale on the compact W1 class by transferring bounded-mild NSE analyticity to finite Leray-time windows.

The permitted derivative mechanism is

\[
\boxed{
\|\partial_s^mf\|_{\delta_1}
\le
\frac{m!}{(\delta_0-\delta_1)^m}
\|f\|_{\delta_0},
\qquad
0<\delta_1<\delta_0.
}
\]

The radius loss is essential.

This input supports future spectral-transfer estimates but does **not** itself eliminate a flat fiber.

---

## 13. RED firewalls

The following implications are forbidden in all subsequent work unless a genuinely new lemma supplies the missing step.

1. `finite terminal time => finite critical action` — RED.
2. `infinitely many recurrent critical events => finite-energy contradiction` — RED.
3. `same-tail noninjectivity => off-diagonal recurrent pair` — RED.
4. `compact analyticity => derivative/amplitude bound in the same norm` — RED.
5. `superalgebraic decay => super-Gaussian decay` — RED.
6. `generic Landis/Oleinik unique continuation => flat fiber vanishes` under current assumptions — RED.
7. `nonzero tail residual => contradiction` — RED; subleading nonresonant corrections may absorb it.
8. `finite energy / unforced => all pressure multipole moments vanish` — RED.
9. `punctured terminal C-infinity => terminal analytic at the singular center` — RED.
10. `core-tail cocycle => current core actively emits each distant tail shell as a new independent cost` — RED.

These firewalls are part of the stage closure.

---

## 14. DSD four-chain final audit of the stage

### Formation — GREEN

The objects are now separated as:

- critical canonical tail;
- strong same-tail difference;
- algebraic jet;
- flat remainder;
- statistical versus proximal pair dynamics.

Undefined or non-realized formal pressure harmonics are not treated as physical degrees of freedom.

### Axis — GREEN

Different coordinates are used for different tasks:

- `(z,eta)` for Fuchsian boundary/genealogy;
- `(xi,s)` for invariant normal energy;
- `tau=log xi` for frequency escape.

No one coordinate is promoted into a physical principle.

### Static aggregation — GREEN

Tail residue, core overpay, pressure residual, and same-tail fiber energy are not counted as independent budgets when linked by exact identities/cocycles.

### Dynamics — GREEN with open terminal gate

The algebraic fiber is dynamically closed.

The remaining statistical flat branch has a necessary high-frequency escape but no proved impossibility theorem.

The proximal branch is invariant-measure a.e. injective but not pointwise closed.

### Cross-audit — STABLE

No current open statement is used to justify an earlier closed statement.

The W1-internal dependency graph is acyclic at this freeze point.

---

## 15. Frozen frontier

At the end of this stage:

\[
\boxed{
P1_A=\text{CLOSED}
}
\]

and

\[
\boxed{
P1_B
=
P1_B^S\lor P1_B^P.
}
\]

The two open branches are:

### `P1_B^S` — statistical flat fiber

Required features:

\[
\boxed{
\begin{aligned}
&K=O(\xi^{-N})\quad\forall N,\\
&\rho(\mathcal R\setminus\Delta)>0,\\
&\Omega_{cross}(\tau)\text{ must escape at parabolic scale},\\
&\text{uniform reduced analytic strip remains available.}
\end{aligned}
}
\]

### `P1_B^P` — proximal exceptional flat fiber

The tail factor is almost everywhere injective for every invariant measure, but pointwise exceptional fibers may remain.

---

## 16. Next-stage entry point — recorded but NOT started

The next calculation, when explicitly resumed, is:

\[
\boxed{
\text{derive an NSE-specific spectral-transfer inequality for }P1_B^S
}
\]

comparing

\[
\text{required frequency migration }\Omega(\tau)\gtrsim e^{\tau/2}
\]

against

\[
\text{the }e^{-\tau}\text{-weighted transport/stretching coupling and the available analytic-radius budget}.
\]

This calculation is **not part of the present stage closure**.

Only after `P1_B^S` is resolved should the pointwise `P1_B^P` branch be revisited unless a stronger argument eliminates both simultaneously.

---

## 17. Global proof firewall

All conclusions in this note are conditional on the W1 branch and its previously audited construction.

The separate global branch-completeness gate remains open:

\[
\boxed{
\text{finite-time singularity}
\Rightarrow
W1\ \lor\ \text{a branch already rigorously excluded}
}
\]

has not yet received a final universal proof audit.

Therefore

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
