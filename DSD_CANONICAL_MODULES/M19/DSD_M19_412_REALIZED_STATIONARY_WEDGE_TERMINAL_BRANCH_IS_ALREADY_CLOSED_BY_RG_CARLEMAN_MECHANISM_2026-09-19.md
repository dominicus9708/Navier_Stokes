# M19-412 — Realized stationary wedge terminal branch is already closed by the M5-268/269 RG-Carleman mechanism

Date: 2026-09-19

Status: **MAJOR CANONICAL CORRECTION / THE LATER M19 STATIONARY TERMINAL SUBBRANCH WAS OVER-RETAINED. M5-568 GIVES SMOOTH OFF-ORIGIN TERMINAL CONVERGENCE ON THE ISOLATED-CENTER BRANCH, M5-582 IDENTIFIES THE FULL PRETERMINAL ANCIENT FLOW AS AN EXACT REALIZED WEDGE, AND M5-572 IDENTIFIES \`C=0\` WITH A STATIONARY TERMINAL TRACE. THESE ARE EXACTLY THE INPUTS NEEDED TO REUSE THE M5-268/269 RG-FLATNESS + OSEEN-CARLEMAN + SMOOTH-CORE CONTRADICTION. THEREFORE A NONZERO REALIZED STATIONARY TERMINAL TRACE CANNOT OCCUR ON THE RETAINED SMOOTH WEDGE BRANCH. THE M19-272/406--411 STATIONARY FORCE/STRESS/BERNOULLI CALCULATIONS REMAIN VALID STRUCTURAL IDENTITIES AND SCOPE FIREWALLS, BUT THEY ARE NOT THE LIVE REALIZED-WEDGE SURVIVOR. THE LIVE TERMINAL TAIL MUST BE RESIDUAL-ACTIVE \`C != 0\`, OR EXIT THROUGH OFF-ORIGIN TERMINAL-REGULARITY/REPRESENTATION FAILURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact current terminal object

M5-582 gives the exact wedge representation of the ancient flow:

\[
u(x,s)
=
r^{-1}F(z,q,\omega),
\qquad
z=\frac{-s}{r^2},
\qquad
q=\log r,
\]

for

\[
s<0,
\qquad
x\neq0.
\]

The terminal trace is

\[
\boxed{
F(0,q,\omega)=A(q,\omega).
}
\]

M5-572 identifies the first terminal derivative

\[
\boxed{
C
=
\partial_zF|_{z=0}
=
\mathcal R_{\rm stat}[A,P].
}
\]

Hence the branch

\[
\boxed{C=0}
\]

is precisely the branch on which the terminal trace

\[
T(x)
=
r^{-1}A(\log r,\omega)
\]

solves the stationary Navier--Stokes equations on

\[
\mathbb R^3\setminus\{0\}.
\]

---

## 2. Off-origin terminal smoothness is available on the isolated-center branch

M5-568 explicitly records that, when the terminal singularity is localized at the blow-up center,

\[
u(\cdot,s)
\to
u_0
\]

smoothly on every compact subset of

\[
\mathbb R^3\setminus\{0\}
\]

as

\[
s\uparrow0.
\]

Thus for every

\[
K\Subset\mathbb R^3\setminus\{0\}
\]

and every finite derivative order \(m\),

\[
\boxed{
u(\cdot,s)
\to T
\quad\text{in }C^m(K)
}
\]

on the stationary branch.

Standard local parabolic regularity on such punctured compacts gives one-sided terminal-time \(C^\infty\) regularity.

This is the analogue of the actual terminal regularity audited in M5-269.

---

## 3. Use physical terminal depth as the realized RG parameter

Set

\[
\rho=-s\ge0
\]

and define on the punctured space

\[
\boxed{
\mathscr R_\rho(x)
:=
u(x,-\rho).
}
\]

Then the Navier--Stokes evolution gives exactly

\[
\boxed{
\partial_\rho\mathscr R_\rho
=
-\nu\Delta\mathscr R_\rho
+
\mathbb P\nabla\cdot
(\mathscr R_\rho\otimes\mathscr R_\rho).
}
\]

At

\[
\rho=0,
\]

\[
\boxed{
\mathscr R_0=T.
}
\]

Thus the current terminal wedge supplies the same type of **realized backward-RG path** used in M5-268.

No formal terminal series is needed for this identification.

---

## 4. Stationarity kills every actual terminal-time derivative

Let

\[
\mathcal F(U)
:=
\nu\Delta U
-
\mathbb P\nabla\cdot(U\otimes U).
\]

Stationarity of \(T\) means

\[
\boxed{
\mathcal F(T)=0.
}
\]

The realized path satisfies

\[
\partial_\rho\mathscr R
=
-\mathcal F(\mathscr R).
\]

Therefore

\[
\partial_\rho\mathscr R(0)
=
-\mathcal F(T)
=
0.
\]

Differentiate repeatedly.

If

\[
\partial_\rho^j\mathscr R(0)=0
\qquad
1\le j\le n,
\]

then every term in the \((n+1)\)-st differentiated equation contains at least one lower positive-order derivative and vanishes.

Hence

\[
\boxed{
\partial_\rho^n\mathscr R(0)=0
\qquad
\forall n\ge1.
}
\]

Because Section 2 gives actual \(C^\infty\) terminal regularity on punctured compacts, these are actual derivatives, not formal jet coefficients.

---

## 5. Actual infinite-order punctured flatness

For every fixed punctured compact \(K\), spatial derivative order \(m\), and integer \(N\),

Banach-valued Taylor remainder gives

\[
\boxed{
\|\mathscr R_\rho-T\|_{C^m(K)}
=
O_{K,m,N}(\rho^N)
\qquad
(\rho\downarrow0).
}
\]

The pressure difference is likewise flat to every order after fixing the local pressure gauge, by the same elliptic argument used in M5-269.

Thus the full flatness input of M5-268 is present.

---

## 6. Reuse the M5-268 Oseen-Carleman step

Set

\[
\tau=-\rho<0,
\qquad
U(\tau,x):=\mathscr R_{-\tau}(x),
\]

and

\[
W(\tau,x):=U(\tau,x)-T(x).
\]

On every bounded punctured domain,

\[
W_\tau
-
\nu\Delta W
+
(U\cdot\nabla)W
+
(W\cdot\nabla)T
+
\nabla q
=
0,
\]

\[
\nabla\cdot W=0.
\]

The coefficients are smooth and bounded on the fixed punctured Carleman domain.

Infinite-order terminal flatness permits zero extension through

\[
\tau=0.
\]

The M5-217/M5-268 local Oseen Carleman level-gap argument therefore gives

\[
\boxed{
W=0
}
\]

on a nonempty preterminal spacetime open set.

---

## 7. Spatial continuation at a negative time

Choose one

\[
\tau_1<0
\]

with a nonempty spatial equality set.

Then

\[
U(\tau_1,x)=T(x)
\]

on a nonempty open spatial subset away from the origin.

At the finite negative time \(\tau_1\),

\[
U(\tau_1,\cdot)
\]

is a smooth Navier--Stokes ancient slice on all of \(\mathbb R^3\).

Both fields are spatially analytic on

\[
\mathbb R^3\setminus\{0\}.
\]

Hence analytic continuation gives

\[
\boxed{
U(\tau_1,x)=T(x)
\qquad
\forall x\neq0.
}
\]

---

## 8. The terminal puncture becomes removable

Since

\[
U(\tau_1,\cdot)
\]

is smooth at the origin and equals \(T\) on the punctured neighborhood,

\[
T
\]

extends smoothly through the origin.

Thus the stationary terminal trace becomes an entire smooth stationary solution.

In particular any point-force coefficient vanishes automatically.

Therefore the M19-272 split

\[
\kappa_{\rm force}\neq0
\quad\lor\quad
\kappa_{\rm force}=0
\]

is not the final live split on this realized branch: the entire stationary branch reaches smooth removability first.

---

## 9. Entire critical-decay stationary field is zero

The terminal critical class has

\[
|T(x)|\lesssim |x|^{-1},
\]

\[
|\nabla T(x)|\lesssim |x|^{-2},
\]

\[
|P_T(x)|\lesssim |x|^{-2}
\]

at infinity.

The standard cutoff-energy argument used in M5-268 gives

\[
\nu\int_{\mathbb R^3}|\nabla T|^2dx=0.
\]

Hence \(T\) is constant.

The \(O(1/r)\) decay forces

\[
\boxed{
T\equiv0.
}
\]

But M5-571 gives on the nontrivial hard component

\[
c_3>0,
\qquad
c_\omega>0.
\]

Contradiction.

Therefore

\[
\boxed{
C=0
\quad\Longrightarrow\quad
\text{trivial terminal trace}
}
\]

on the realized off-origin-smooth wedge branch.

---

## 10. Corrected status of M19-272 and M19-406--411

The identities derived there remain mathematically useful:

- stress-flux identification;
- exact homogeneous Landau classification firewall;
- positive log-dilation derivative requirement;
- terminal energy-flux resolvent;
- shallow energy-current reversal;
- Bernoulli correlation identity.

But on the **realized smooth terminal wedge branch**, they do not define the final surviving stationary endpoint because M5-268/269 closes the stationary trace earlier and more strongly.

Thus these modules are reclassified as

\[
\boxed{
\text{STRUCTURAL CROSS-CHECK / SCOPE FIREWALL}
}
\]

for stationary punctured models.

They are not the primary current proof frontier.

---

## 11. Live terminal branch after correction

The hard terminal tail now splits as

\[
\boxed{
C\neq0
}
\]

or

\[
\boxed{
G_{\rm terminal}^{off\text{-}origin\ regularity/representation\ loss}.
}
\]

On the retained isolated-center smooth branch,

\[
\boxed{
C\neq0.
}
\]

Thus the current terminal profile is necessarily **residual-active**.

The relevant recurrent object is the joint process

\[
\boxed{
(A,C)
}
\]

from M5-572/M5-580, not a stationary \(A\) alone.

---

## 12. Revised highest-value target

The stationary rigidity target

\[
\mathcal T_{dil-stress}^{zero-force}
\]

is demoted on the realized wedge.

The live target becomes

\[
\boxed{
\mathcal T_{residual}^{active}:
\text{exclude or classify a nontrivial recurrent terminal process }(A,C)
\text{ with }C=\mathcal R_{\rm stat}[A,P]\neq0.
}
\]

The next calculations should therefore return to the residual-active terminal-jet hierarchy / wedge dynamics, not continue the stationary force-cancellation branch.

---

\[
\boxed{\text{M19-412 COMPLETE; THE REALIZED STATIONARY TERMINAL WEDGE BRANCH IS CLOSED, LEAVING THE RESIDUAL-ACTIVE TERMINAL PROCESS.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
