# DSD M5-641 — Strongly-negative kappa mass forces coherent fixed-flux packets with one-way decay and positive-rate replacement

Date: 2026-09-03

Status: **INTERNAL COHERENT-PACKET TURNOVER / M5-640 GIVES A UNIFORM FIXED-CORE ENSTROPHY MASS ON `kappa<=-kappa_*`. GLOBAL SMOOTH COMPACTNESS THICKENS THIS INTO A FIXED-RADIUS COHERENT VORTICITY PACKET WITH NONDEGENERATE MATERIAL FLUX AND `kappa<=-kappa_*/2`. ON THE RELABELING ZERO-LEVEL BRANCH, KAPPA SIGN IS PRESERVED BY SCALAR-ODE UNIQUENESS, SO A NEGATIVE MATERIAL LABEL CAN NEVER RECOVER POSITIVE FLUX DRIFT. WHILE IT IS STRONGLY NEGATIVE ITS FLUX DECAYS AT A UNIFORM EXPONENTIAL RATE. HENCE ONE MATERIAL FLUX LABEL HAS A UNIFORM FINITE TOTAL STRONGLY-NEGATIVE COHERENT LIFETIME. BECAUSE SUCH A PACKET EXISTS AT EVERY RECURRENT STATE, THE VOLUMETRIC NEGATIVE-KAPPA SHEATH REQUIRES POSITIVE-RATE COHERENT PACKET REPLACEMENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-core strongly-negative mass

M5-640 provides constants

\[
\kappa_*>0,
\qquad
m_->0,
\qquad
R_-<\infty
\]

such that every CE-H state satisfies

\[
\boxed{
\int_{B_{R_-}\cap\{\kappa\le-\kappa_*\}}|W|^2dy
\ge\frac{m_-}{2}.
}
\]

---

## 2. Extract a point with nondegenerate vorticity

Since the integration domain lies inside a fixed finite-volume ball, there exists a point `y_0` in the strongly-negative set with

\[
|W(y_0)|^2
\ge
\frac{m_-}{2|B_{R_-}|}.
\]

Define

\[
\boxed{
w_0:=\left(\frac{m_-}{2|B_{R_-}|}\right)^{1/2}>0.
}
\]

Then for some point in every state,

\[
\boxed{
|W(y_0)|\ge w_0,
\qquad
\kappa(y_0)\le-\kappa_*.
}
\]

---

## 3. Uniform smooth thickening

The compact CE-H hull has uniform fixed-order `C^k` bounds.

Near a point where `|W|>=w_0`, the quotient

\[
\kappa=\frac{W\cdot\Delta W}{|W|^2}
\]

has a uniformly bounded spatial derivative because the denominator is bounded away from zero and `W, grad W, Delta W, grad Delta W` are uniformly bounded.

Therefore there exists a fixed radius

\[
\boxed{r_*>0}
\]

such that on a ball centered at `y_0`, after reducing `r_*` if necessary,

\[
\boxed{
|W|\ge\frac12w_0,
\qquad
\kappa\le-\frac12\kappa_*.
}
\]

Uniform direction continuity also gives a unit vector `xi_0` with

\[
W\cdot\xi_0\ge c_\xi w_0>0
\]

on a fixed transverse disk of radius comparable to `r_*`.

---

## 4. Nondegenerate coherent material flux packet

Take the transverse disk and attach it to its material image under the similarity material flow.

Its initial vorticity flux satisfies

\[
\boxed{
\Phi\ge\phi_*>0
}
\]

for a constant depending only on the compact-hull bounds and `r_*,w_0`.

There is also a fixed upper flux cap `phi^*` for a coherent disk at the extraction scale because `|W|` and the disk area are uniformly bounded.

Thus every recurrent state contains a coherent strongly-negative packet with

\[
\boxed{
\phi_*\le|\Phi|\le\phi^*.
}
\]

---

## 5. One-way flux decay on the zero-level relabeling branch

Now restrict to the M5-636 no-turnover synchronized branch

\[
c_*\equiv0.
\]

The relabeling equation is

\[
D_B\kappa=f(\kappa,\theta),
\qquad
f(0,\theta)=0.
\]

Scalar ODE uniqueness prevents a material level starting with

\[
\kappa<0
\]

from crossing through zero.

Hence every vortex line in a negative material packet remains on the negative side for all future times for which the relabeling description remains valid.

The material flux law is

\[
\Phi'
=\int_S\kappa W\cdot n\,dA.
\]

For an oriented coherent vortex-tube cross-section with positive directed flux, negative kappa gives

\[
\boxed{\Phi'\le0.}
\]

Thus a negative material flux label has **one-way nonincreasing flux** and cannot later restore lost flux by a positive-kappa phase.

---

## 6. Uniform decay while strongly negative

Whenever the whole coherent material packet lies in

\[
\kappa\le-\frac12\kappa_*,
\]

its flux-weighted multiplier satisfies

\[
\bar\kappa_\Phi\le-\frac12\kappa_*.
\]

Therefore

\[
\boxed{
\frac{d}{d\theta}\log|\Phi|
\le-\frac12\kappa_*.
}
\]

Over total strongly-negative exposure time `T_-`,

\[
|\Phi|\le|\Phi_0|e^{-\kappa_*T_-/2}.
\]

A packet extracted with flux at most `phi^*` can remain a coherent fixed-strength packet with flux at least `phi_*` for total strongly-negative time no larger than

\[
\boxed{
T_-^{max}
\le
\frac{2}{\kappa_*}
\log\frac{\phi^*}{\phi_*}.
}
\]

This is a uniform finite material-label lifetime in the strongly-negative coherent role.

---

## 7. Positive-rate replacement

M5-640 says a fixed amount of strongly-negative enstrophy exists **at every recurrent state**.

M5-641 says one material coherent packet can occupy that fixed-strength strongly-negative role only for uniformly finite total time and can never recover its lost material flux afterward on the zero-level relabeling branch.

Therefore indefinite recurrent operation requires continual introduction of new coherent material labels into the strongly-negative packet role.

After the standard event-thickening/finite-memory extraction used earlier in M5-488--493, this yields

\[
\boxed{
\text{positive-density / positive-rate strongly-negative coherent packet replacement}.
}
\]

The precise numerical replacement rate depends on overlap multiplicity in the finite packet cover, but the no-replacement alternative is eliminated.

---

## 8. Updated relabeling geometry

The no-turnover synchronized zero-level skeleton therefore does **not** eliminate turnover from the full three-dimensional solution.

Instead the structure is

\[
\boxed{
\text{persistent measure-zero zero-kappa flux skeleton}
+
\text{positive-rate strongly-negative coherent packet turnover}.
}
\]

Thus every enstrophy-bearing CE-H relabeling survivor has an irreversible one-way negative-flux conveyor around the persistent skeleton.

---

## 9. What is not yet a contradiction

A recurrent Eulerian field can in principle be maintained by a continuous through-flow of material labels.

The finite lifetime of one label does not by itself prevent infinitely many replacements over an ancient time interval.

Therefore M5-641 is a turnover theorem, not yet a Navier--Stokes nonexistence theorem.

The next target must determine whether an unforced compact recurrent ancient solution can sustain this one-way negative-flux conveyor while simultaneously balancing the positive-kappa/growing-flux population and the finite global enstrophy/production ledgers.

---

## 10. Firewall

The uniform packet extraction uses the uniform derivative/tail compactness already established on the compact CE-H branch.

If the final proof audit only retains time-averaged rather than pointwise lower bounds on `P`, the conclusion must be weakened from every-time replacement to positive-density-in-time replacement.

No assumption is made that one coherent disk keeps a fixed Euclidean shape under material transport.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]