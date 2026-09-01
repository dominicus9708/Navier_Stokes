# DSD M5-544 — The full similarity derivative ledger localizes to the finite active core with vanishing exterior error

Date: 2026-09-01

Status: **LOCAL LEDGER CLOSURE / AFTER M5-543 FIXES ONE LARGE ACTIVE-CORE RADIUS, THE CUTOFF TRANSITION REGION CAN BE PLACED IN THE UNIFORMLY SMALL SOBOLEV TAIL / THE LOCALIZED SIMILARITY ENSTROPHY, PALINSTROPHY, AND EVERY FIXED HIGHER-DERIVATIVE BALANCE THEN DIFFER FROM THEIR WHOLE-SPACE IDENTITIES BY ERRORS THAT TEND UNIFORMLY TO ZERO AS THE CORE RADIUS IS ENLARGED / THUS THE POSITIVE AXIAL-PRODUCTION, PALINSTROPHY, PROJECTED-DIFFUSION, AND HIGHER-DERIVATIVE COSTS MUST ALL BE PAID INSIDE THE SAME FINITE RECURRENT CORE; THE NON-L3 SPECTATOR TAIL CANNOT HIDE ANY PART OF THE DERIVATIVE BUDGET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Smooth core cutoff

Choose one large radius `R` exceeding the M5-543 active radius and let

\[
\chi_R(y)=\chi(y/R)
\]

with

\[
\chi_R=1
\quad\text{on }B_R,
\]

\[
\chi_R=0
\quad\text{outside }B_{2R},
\]

and

\[
|\nabla^j\chi_R|
\le C_jR^{-j}.
\]

The transition shell is

\[
S_R:=\{R<|y|<2R\}.
\]

By M5-508, for every fixed integer `m`,

\[
\boxed{
\sup_{Y\in\widehat{\mathfrak H}}
\|W_Y\|_{H^m(S_R)}
\to0
\qquad(R\to\infty).
}
\]

M5-523 and M5-535 also give

\[
\sup_{S_R}|U|+\sup_{S_R}|\Sigma|\to0.
\]

Thus all cutoff commutator terms live in a region where every fixed Sobolev order is uniformly small.

---

## 2. Localized enstrophy

Define

\[
E_R(\theta)
:=
\int\chi_R|W|^2dy,
\]

\[
P_R(\theta)
:=
\int\chi_R|\nabla W|^2dy,
\]

and

\[
Q_R(\theta)
:=
\int\chi_R W\cdot\Sigma Wdy.
\]

Multiply the similarity-vorticity equation by `chi_R W` and integrate.

The whole-space calculation of M5-486 is unchanged in the interior. Derivatives striking `chi_R` produce only transition-shell terms.

Hence

\[
\boxed{
\frac12E_R'
+
\frac14E_R
+
P_R
=
Q_R
+
\mathcal E_R^{(0)},
}
\]

where `mathcal E_R^(0)` is a sum of terms schematically bounded by

\[
\int_{S_R}
\left(
|W|^2
+|U||W|^2
+|W||\nabla W|
\right)dy
\]

times cutoff derivative factors bounded by powers of `R^(-1)` or the scale-neutral factor `y dot grad chi_R=O(1)`.

Therefore

\[
\boxed{
\sup_Y|\mathcal E_R^{(0)}(Y)|
\to0.
}
\]

---

## 3. Invariant local enstrophy balance

Average on the common ergodic component `nu_*`.

Since `E_R` is bounded and continuous for fixed `R`, invariance gives

\[
\langle E_R'\rangle=0.
\]

Thus

\[
\boxed{
\frac14\langle E_R\rangle
+
\langle P_R\rangle
=
\langle Q_R\rangle
+o_R(1).
}
\]

By M5-543, for sufficiently large fixed `R`,

\[
\langle Q_R\rangle\ge q_*/2>0.
\]

Hence the active core itself carries the complete similarity enstrophy-maintenance budget.

The endpoint tail is not needed to pay the balance.

---

## 4. Positive core palinstrophy from recurrent dual geometry

M5-492--493 turned recurrent noncollinear dual geometry into a positive mean palinstrophy cost.

Because the marked dual carriers are contained in `B_(R_core)` and `chi_R=1` there,

\[
\boxed{
\langle P_R\rangle
\ge p_{core}>0
}
\]

for all sufficiently large fixed `R` on the retained active component.

Therefore

\[
\boxed{
\langle Q_R\rangle
\ge
\frac14\langle E_R\rangle+p_{core}-o_R(1).
}
\]

This is the localized version of the M5-493 production cost.

---

## 5. Localized palinstrophy balance

Set

\[
H_R
:=
\int\chi_R|\Delta W|^2dy.
\]

Differentiate the similarity-vorticity equation once, pair with `chi_R grad W`, and repeat M5-501.

The interior terms give

\[
\frac12P_R'
+
\frac34P_R
+
H_R
=
\mathcal N_{P,R}
+
\mathcal E_R^{(1)},
\]

where `mathcal N_(P,R)` is the nonlinear derivative production localized by `chi_R`.

All new cutoff commutators contain only fixed derivatives of `chi_R` multiplied by derivatives of `W` and `U` on `S_R`.

Using M5-508 at sufficiently high fixed Sobolev order,

\[
\boxed{
\sup_Y|\mathcal E_R^{(1)}(Y)|
\to0.
}
\]

Hence

\[
\boxed{
\frac12P_R'
+
\frac34P_R
+
H_R
=
\mathcal N_{P,R}
+o_R(1).
}
\]

---

## 6. Projected-diffusion cost is also local

On the common active component, M5-500 supplies either a transverse-strain ratchet or a projected-diffusion ratchet.

For the projected-diffusion lane,

\[
H_{proj}
:=
\int
|(I-\xi\otimes\xi)\Delta W|^2dy
\]

has positive recurrent mean.

The marked active carrier lies in `B_(R_core)`, so after choosing `R` large enough,

\[
\boxed{
\left\langle
\int\chi_R
|(I-\xi\otimes\xi)\Delta W|^2dy
\right\rangle
\ge h_{core}>0.
}
\]

Since orthogonal projection does not increase norm,

\[
\boxed{
\langle H_R\rangle\ge h_{core}>0.
}
\]

Thus the second-derivative cost is also an intrinsic core expense.

---

## 7. Higher derivative hierarchy

For

\[
D_{m,R}
:=
\int\chi_R|\nabla^mW|^2dy,
\]

repeat the M5-507 differentiation at any fixed `m>=2`.

The whole-space linear similarity coefficient remains

\[
\boxed{
 c_m=\frac{2m+1}{4}.
}
\]

Thus

\[
\boxed{
\frac12D_{m,R}'
+c_mD_{m,R}
+D_{m+1,R}
=
\mathcal N_{m,R}
+
\mathcal E_R^{(m)}.
}
\]

For each fixed `m`, all cutoff errors satisfy

\[
\boxed{
\sup_Y|\mathcal E_R^{(m)}(Y)|
\to0
\qquad(R\to\infty).
}
\]

This follows from the all-order tail smallness of M5-508 and the fact that only finitely many derivatives are involved at each fixed `m`.

---

## 8. Core hierarchy versus tail hierarchy

The result is not merely that the core contains the visible geometric marks.

For every fixed derivative level, the recurrent core satisfies the same nested budget as the full solution, up to an arbitrarily small error:

\[
\boxed{
\begin{aligned}
\text{axial production}
&\to
\text{enstrophy maintenance + palinstrophy},\\
\text{derivative production}
&\to
\text{palinstrophy maintenance + }H,\\
\text{higher nonlinearities}
&\to
D_m\text{ maintenance + }D_{m+1}.
\end{aligned}
}
\]

The adaptive endpoint tail cannot be used to explain away any fixed-order cost in this hierarchy.

---

## 9. Invariant averages

For fixed `R,m`, boundedness of `D_(m,R)` and invariance give

\[
\langle D_{m,R}'\rangle=0.
\]

Therefore

\[
\boxed{
 c_m\langle D_{m,R}\rangle
+
\langle D_{m+1,R}\rangle
=
\langle\mathcal N_{m,R}\rangle
+o_R(1).
}
\]

The core is therefore a recurrent nonlinear system that must regenerate every dissipative derivative level it activates.

This is an intrinsic balance, not a boundary artifact from the non-`L3` tail.

---

## 10. What this does not prove

The localized balances are still **balances**, not strict Lyapunov inequalities.

The nonlinear production terms `Q_R` and `N_(m,R)` have the signs required to pay the positive dissipative terms on the recurrent survivor.

Thus merely localizing the known energies does not create the missing strict cocycle.

This audit is important because it shows that the previous sign obstruction was not caused by spatial infinity.

It is intrinsic to the finite active Navier--Stokes core.

---

## 11. Updated hard core

After M5-541--544, the proof obstruction splits sharply into two logically distinct objects:

1. an endpoint spectator tail that prevents global `L3` but contributes vanishing active action;
2. a finite-radius recurrent core that internally balances positive stretching, ratchet geometry, and every activated dissipative derivative level.

The second object is now the only place where a genuine new rigidity mechanism is required.

---

## 12. Highest-value next target

The next audit should revisit the natural scalar potentials **after localization** and ask which failures are intrinsic:

- localized enstrophy;
- localized palinstrophy;
- material flux/circulation;
- pair Gram determinant;
- localized kinetic energy;
- helicity or cross-helicity-type pair observables.

Any candidate whose only previous obstruction was a tail/boundary term can now be revived because that error is `o_R(1)`.

Candidates that still fail by exact sign-changing core dynamics should be retired from the proof line, leaving only genuinely new core-cycle observables for the final rigidity step.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]