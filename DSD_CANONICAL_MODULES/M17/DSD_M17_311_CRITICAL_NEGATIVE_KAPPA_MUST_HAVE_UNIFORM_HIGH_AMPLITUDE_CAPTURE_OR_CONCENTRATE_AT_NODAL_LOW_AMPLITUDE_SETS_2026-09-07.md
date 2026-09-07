# DSD M17-311 — Critical negative-`kappa` mass must be uniformly captured at high amplitude or concentrate into nodal low-amplitude sets

Date: 2026-09-07  
Canonical ID: **M17-311**

Status: **AMPLITUDE-RETURN SPLIT FOR THE LOSSLESS COEFFICIENT CURRENCY / M17-310 FORCES `||kappa_-||_(L^(3/2)) >= S_3` ON EVERY NONZERO REGULAR CE-H STATE, INDEPENDENT OF VORTICITY AMPLITUDE AND RECORD GENERATION. THE PRESENT MODULE SPLITS THIS CRITICAL NEGATIVE-POTENTIAL MASS BY VORTICITY AMPLITUDE. EITHER THERE EXISTS ONE UNIFORM HIGH-AMPLITUDE THRESHOLD `a_*>0` ON THE RECURRENT CE-H HULL THAT CAPTURES A FIXED PORTION OF `int kappa_-^(3/2)`, OR THERE IS A SEQUENCE OF STATES AND THRESHOLDS `a_n->0` FOR WHICH A FIXED CRITICAL PORTION CONCENTRATES IN `{rho<a_n}`. ON THE HIGH-AMPLITUDE BRANCH, COMPACT REGULARITY GIVES A UNIFORM `|kappa|<=K_*`, SO THE CRITICAL `L^(3/2)` MASS CONVERTS TO A FIXED SIGNED ENSTROPHY-WEIGHTED NEGATIVE-KAPPA CHARGE `int chi rho^2 kappa_- >= d_->0`. THUS THE AMPLITUDE FIREWALL IS REMOVED ON THAT BRANCH. THE ONLY WAY TO KEEP THE LOSSLESS NEGATIVE-KAPPA CURRENCY CHEAP IN `rho^2` WEIGHT IS TO DRIVE IT TOWARD THE NODAL/LOW-AMPLITUDE SET, WHICH IS NOW AN EXPLICIT CRITICAL NODAL-CONCENTRATION FRONTIER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-310

On the regular global-coefficient CE-H branch, every nonzero state satisfies

\[
\boxed{
\|\kappa_-\|_{L^{3/2}}
\ge S_3>0.
}
\]

Equivalently,

\[
\boxed{
\int_{\mathbb R^3}
\kappa_-^{3/2}dy
\ge
K_0,
\qquad
K_0:=S_3^{3/2}>0.
}
\]

Write

\[
\rho:=|W|.
\]

For any amplitude threshold `a>0`, split the critical negative-potential mass into

\[
K_{hi}(a)
:=
\int_{\{\rho\ge a\}}
\kappa_-^{3/2}dy,
\]

and

\[
K_{lo}(a)
:=
\int_{\{\rho<a\}}
\kappa_-^{3/2}dy.
\]

Then

\[
\boxed{
K_{hi}(a)+K_{lo}(a)
\ge K_0.
}
\]

---

## 2. Uniform high-amplitude capture versus nodal concentration

Fix the recurrent CE-H state family/hull under consideration.

There are two exhaustive alternatives.

### Branch H — uniform high-amplitude capture

There exists one fixed

\[
\boxed{a_*>0}
\]

such that every retained state satisfies

\[
\boxed{
K_{hi}(a_*)
\ge\frac{K_0}{2}.
}
\]

### Branch N — nodal/low-amplitude critical concentration

Otherwise, for every `n` one can choose a state `Y_n` such that with

\[
a_n:=\frac1n
\]

one has

\[
K_{hi,Y_n}(a_n)<\frac{K_0}{2}.
\]

Hence

\[
\boxed{
K_{lo,Y_n}(a_n)
\ge\frac{K_0}{2},
\qquad
a_n\to0.
}
\]

Thus failure of uniform high-amplitude capture is exactly the existence of a sequence for which a fixed critical amount of negative coefficient mass is driven into vanishing-amplitude neighborhoods.

Define this branch as

\[
\boxed{
G_{\kappa_-\text{-}nodal}^{crit}.
}
\]

No compactness theorem is needed for this logical dichotomy.

---

## 3. Uniform coefficient ceiling away from the nodal set

Work now on Branch H.

Because

\[
\rho\ge a_*>0
\]

on the captured set, the CE-H quotient coefficient is separated from its nodal singularity.

On the retained compact smooth CE-H hull, fixed-order derivative bounds for `W` then give a finite uniform constant

\[
\boxed{
|\kappa(y)|\le K_*<\infty
\qquad
\text{whenever }\rho(y)\ge a_*.
}
\]

Indeed on the active set

\[
\kappa
=
\frac{W\cdot\Delta W}{|W|^2},
\]

so a uniform lower amplitude floor and a uniform second-derivative ceiling give the stated bound.

If this compact coefficient ceiling fails, retain the already typed coefficient/noncompactness exit rather than using the present branch.

---

## 4. Convert critical `L^(3/2)` mass to unweighted negative `L1` mass

On the high-amplitude captured set,

\[
0\le\kappa_-\le K_*.
\]

Therefore

\[
\kappa_-^{3/2}
\le
K_*^{1/2}\kappa_-.
\]

Integrating over `{rho>=a_*}` gives

\[
\int_{\{\rho\ge a_*\}}
\kappa_-dy
\ge
K_*^{-1/2}
K_{hi}(a_*).
\]

Using Branch H,

\[
\boxed{
\int_{\{\rho\ge a_*\}}
\kappa_-dy
\ge
\frac{K_0}{2K_*^{1/2}}.
}
\]

This lower bound is still amplitude independent.

---

## 5. Restore the enstrophy weight without losing the fixed charge

On the same set,

\[
\rho^2\ge a_*^2.
\]

Hence

\[
\begin{aligned}
\int_{\{\rho\ge a_*\}}
\rho^2\kappa_-dy
&\ge
 a_*^2
\int_{\{\rho\ge a_*\}}
\kappa_-dy\\
&\ge
\frac{a_*^2K_0}{2K_*^{1/2}}.
\end{aligned}
\]

Define

\[
\boxed{
d_-
:=
\frac{a_*^2K_0}{2K_*^{1/2}}
>0.
}
\]

Then every state on the high-amplitude-capture branch satisfies

\[
\boxed{
\int_{\{\rho\ge a_*\}}
\rho^2\kappa_-dy
\ge d_->0.
}
\]

Thus the critical negative coefficient cannot become energetically cheap through `rho->0` on this branch.

---

## 6. Cutoff/distribution form compatible with the M5-688 ledger

Choose a monotone smooth amplitude cutoff `chi_*(rho)` such that

\[
0\le\chi_*\le1,
\]

\[
\chi_*=1
\quad\text{for }\rho\ge a_*,
\]

with transition below `a_*`.

Then

\[
\boxed{
\int
\chi_*(\rho)\rho^2\kappa_-dy
\ge d_->0.
}
\]

In `kappa`-space, with

\[
F_*(k)
:=
\int\delta(k-\kappa)
\chi_*(\rho)\rho^2dy,
\]

this is

\[
\boxed{
\int_{k<0}(-k)F_*(k)dk
\ge d_->0.
}
\]

So Branch H produces a fixed **signed negative-phase enstrophy-weighted `kappa` charge** in the same type of distribution used by the M5-683/688 coefficient ledger.

---

## 7. Why this is stronger than the original amplitude-weighted firewall

M17-235 obtains a lower multiplier-gradient diffusion charge proportional to packet mass on a remote low-amplitude packet.

M17-311 instead starts with the amplitude-independent global critical threshold of M17-310 and proves:

\[
\boxed{
\text{either}
\quad
\int\chi_*\rho^2\kappa_-\ge d_->0,
\quad
\text{or}
\quad
G_{\kappa_-\text{-}nodal}^{crit}.
}
\]

Thus the low-amplitude firewall is no longer an untyped possibility.

It has been isolated as one precise alternative:

\[
\boxed{
\text{critical negative coefficient concentration near }\rho=0.
}
\]

---

## 8. Relation to the positive material mean of M17-134

M17-134 conditionally gives, along certain same-material long inter-stage carriers,

\[
\langle\kappa\rangle_{material}
\to\frac32.
\]

The present spatial signed charge

\[
\int\chi_*\rho^2\kappa_-dy
\ge d_-
\]

uses a different measure and must **not** be subtracted directly from that material-time average.

The valid new statement is only that the CE-H state carries a persistent negative coefficient phase at high amplitude unless the critical coefficient mass is pushed toward the nodal set.

The next missing theorem is therefore a measure/genealogy bridge:

\[
\boxed{
\text{high-amplitude negative spatial phase}
\Longrightarrow
\text{material/flux residence or turnover}.
}
\]

---

## 9. Record-generation behavior

The source threshold

\[
\|\kappa_-\|_{3/2}\ge S_3
\]

is record-scale invariant by M17-310.

The high-amplitude threshold `a_*`, however, is a **normalized state amplitude threshold** and need not correspond to one fixed first-generation physical vorticity amplitude across record blow-downs.

Therefore M17-311 does not claim that `d_-` itself is an invariant ancestral physical budget.

Its role is different: within each normalized CE-H state it prevents the lossless critical coefficient mass from hiding behind amplitude weighting unless a nodal concentration branch occurs.

This preserves the M17-306 generation firewall.

---

## 10. Updated coefficient frontier

Combining M17-310 and M17-311,

\[
\boxed{
H_{critical\ \kappa_-}
\Longrightarrow
H_{high\text{-}amplitude\ signed\ negative\ phase}
\lor
G_{\kappa_-\text{-}nodal}^{crit}
\lor
G_{coefficient/noncompact}.
}
\]

On the first branch,

\[
\boxed{
\int_{k<0}(-k)F_*(k)dk
\ge d_->0.
}
\]

Thus the next honest target is no longer amplitude return itself; it is transport/residence of this signed negative phase through the CE-H material genealogy.

---

## 11. DSD audit

- The `L^(3/2)` threshold from M17-310 is split before inserting any amplitude weight.
- Failure of uniform high-amplitude capture is retained as a precise nodal concentration sequence.
- The coefficient ceiling is used only away from the nodal set where `rho>=a_*`.
- The high-amplitude branch restores a fixed `rho^2`-weighted negative charge without cancelling amplitude by normalization.
- Spatial and material averages remain distinct.
- No claim is made that the restored `d_-` is a first-generation scale-invariant budget.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
