# DSD M17-109 — Generic director-area tangency has margin-weighted fold hysteresis but signed-flux neutrality

Date: 2026-09-05
Canonical ID: **M17-109**

Status: **INTERNAL MARGIN-WEIGHTED TANGENCY HYSTERESIS GATE / M17-099--100 SHOW THAT A GENERIC `D_k g=0` DIRECTOR-AREA/PEAK TANGENCY IS A FOLD AND THAT ITS TWO TRANSVERSE OFFSPRING HAVE OPPOSITE ORIENTED `J_xi` INTERSECTION SIGNS, SO UNWEIGHTED SIGNED DIRECTOR-AREA FLUX IS NEUTRAL. M17-108, HOWEVER, REQUIRES AN EVENT SOURCE FOR THE POSITIVE MARGIN INVENTORY. IN FROZEN TUBE COORDINATES A GENERIC MAXIMUM FOLD HAS NORMAL FORM `g=A(theta-theta_*)+(H/2)(s-s_*)^2+...`, WITH `A=D_xi(sigma+kappa)` AND `H=D_k^2 g`. FOR `C=D_xi g<0`, BOTH OFFSPRING REMAIN LINE MAXIMA NEAR THE EVENT. IF `N_*=|a|M_R2>0` AT THE FOLD, THE UNSIGNED PEAK-MARGIN SUM ON THAT TUBE JUMPS BY `+2N_*` FOR A FORWARD BIRTH (`AH<0`) AND `-2N_*` FOR A FORWARD DEATH (`AH>0`). THUS THE DISTRIBUTIONAL EVENT SOURCE IS `2 epsilon_F N_* delta(theta-tau_F)dPhi_J`, `epsilon_F=-sgn(AH)`. BY CONTRAST THE ORIENTATION-WEIGHTED SUM `sum sgn(D_k g)N` HAS NO DELTA JUMP BECAUSE THE TWO SIGNS CANCEL AND THE TWO MARGINS COALESCE TO THE SAME `N_*`. THERE IS THEREFORE AN EXACT POSITIVITY-VERSUS-CONSERVATION TRADEOFF: THE POSITIVE MARGIN INVENTORY HAS A SIGNED FOLD-HYSTERESIS SOURCE, WHILE THE ALGEBRAIC FLUX INVENTORY IS FOLD-NEUTRAL BUT NONCOERCIVE. OVER A RECURRENT CYCLE, UNWEIGHTED BIRTH/DEATH BALANCE DOES NOT FORCE THE MARGIN-WEIGHTED EVENT SUM TO ZERO; CLOSURE REQUIRES A NEW COVARIANCE/PAIRING THEOREM FOR MARGINS AT BIRTH AND DEATH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Generic tangency data

Use a frozen director-area tube label `lambda` and a local coordinate `s` along the kernel direction `k`.

A generic director-area/peak tangency satisfies

\[
\boxed{
g=0,
\qquad
D_kg=0,
\qquad
H:=D_k^2g\neq0.
}
\]

At a peak,

\[
D_Bg=D_\xi(\sigma+\kappa).
\]

Define

\[
\boxed{
A:=D_\xi(\sigma+\kappa).
}
\]

The generic time-unfolding case is

\[
\boxed{A\neq0.}
\]

M17-099 separately identifies `A=0` as the persistence condition for a tangency that does not immediately fold in material time.

---

## 2. Fold normal form

In local tube/material coordinates centered at the event,

\[
(s,\theta)=(s_*,\theta_*),
\]

the Taylor expansion has the form

\[
\boxed{
 g(s,\theta)
=A(\theta-\theta_*)
+\frac12H(s-s_*)^2
+o(|\theta-\theta_*|+|s-s_*|^2).
}
\]

The nearby roots satisfy

\[
(s-s_*)^2
\sim
-\frac{2A}{H}(\theta-\theta_*).
\]

Hence a root pair exists on the side where

\[
-\frac{A}{H}(\theta-\theta_*)>0.
\]

Define the forward event orientation

\[
\boxed{
\varepsilon_F
:=-\operatorname{sgn}(AH).
}
\]

Then

- `epsilon_F=+1`: pair birth in forward `theta`;
- `epsilon_F=-1`: pair death in forward `theta`.

---

## 3. The two transverse offspring have opposite flux orientation

Let

\[
s_\pm=s_*\pm\delta,
\qquad
\delta>0.
\]

Then

\[
D_kg(s_\pm)
=H(s_\pm-s_*)+o(\delta)
=\pm H\delta+o(\delta).
\]

Therefore

\[
\boxed{
\operatorname{sgn}D_kg(s_+)
=-\operatorname{sgn}D_kg(s_-).
}
\]

This recovers the signed director-area-flux neutrality of M17-099--100.

---

## 4. Restrict to a maximum fold

Assume additionally that

\[
\boxed{
C_*:=D_\xi g(s_*,\theta_*)<0.
}
\]

By continuity, both nearby roots satisfy

\[
D_\xi g<0
\]

for sufficiently small `delta`.

Thus both offspring are linewise amplitude maxima and both carry the positive Riccati compensation descriptor whenever

\[
\mathcal M_{R2}>0.
\]

Define

\[
\boxed{
N:=|a|\mathcal M_{R2}>0.
}
\]

At the fold let

\[
\boxed{N_*:=N(s_*,\theta_*)>0.}
\]

---

## 5. Unsigned positive margin jump

The two offspring satisfy

\[
N(s_\pm,\theta)
=N_*\pm(D_kN)_*\delta+O(\delta^2)+O(|\theta-\theta_*|).
\]

Hence their unsigned sum is

\[
\boxed{
N(s_+)+N(s_-)
=2N_*+O(\delta^2).
}
\]

Therefore the all-maxima positive-margin inventory on this tube gains or loses, at the fold event,

\[
\boxed{
\Delta\mathscr N_{F,\lambda}
=2\varepsilon_FN_*\,d\Phi_J(\lambda).
}
\]

This is the margin-weighted event missed by the unweighted signed-flux ledger.

---

## 6. Distributional fold source over a tube family

Let the fold time of tube label `lambda` be

\[
\theta=\tau_F(\lambda).
\]

For a family of generic folds, the distributional event contribution to the positive margin inventory is

\[
\boxed{
\mathscr B_F(\theta)
=2\int
\varepsilon_F(\lambda)
N_F(\lambda)
\delta(\theta-\tau_F(\lambda))
\,d\Phi_J(\lambda),
}
\]

where

\[
\boxed{
\varepsilon_F
=-\operatorname{sgn}\!\left[
D_\xi(\sigma+\kappa)
\,D_k^2g
\right]_{F}.
}
\]

Thus each generic fold has a definite birth/death sign, but the sign is not determined by the positivity of the margin.

---

## 7. Orientation-weighted margin has no delta jump

Instead define the local algebraic margin sum

\[
\widetilde N_F
:=
\sum_{g=0}
\operatorname{sgn}(D_kg)N.
\]

Near the pair,

\[
\widetilde N_F
=\operatorname{sgn}(H)
\left[N(s_+)-N(s_-)\right]
+o(1).
\]

Therefore

\[
\widetilde N_F
=2\operatorname{sgn}(H)(D_kN)_*\delta
+o(\delta)
\to0
\]

as the pair coalesces.

Hence

\[
\boxed{
\text{the algebraically signed margin inventory has no fold delta source.}
}
\]

The price is that this signed inventory is not positive and cannot control the Riccati compensation burden.

---

## 8. Positivity-versus-conservation tradeoff

The generic fold therefore produces the exact dichotomy

\[
\boxed{
\begin{array}{ccl}
\text{positive/unsigned margin inventory}
&:&
\text{coercive but has }\mathscr B_F,\\[1mm]
\text{orientation-signed margin inventory}
&:&
\text{fold-neutral but noncoercive}.
\end{array}
}
\]

No descriptor currently possesses both properties simultaneously.

This is the central DSD result of the gate.

---

## 9. Recurrent fold hysteresis

Over a recurrence interval containing fold events,

\[
\boxed{
\int\mathscr B_F(\theta)\,d\theta
=2\int d\Phi_J(\lambda)
\sum_{e\in F(\lambda)}
\varepsilon_eN_e.
}
\]

If the unweighted number of peak pairs returns, then births and deaths balance in number/flux weight:

\[
\sum_e\varepsilon_e=0
\]

in the corresponding clean tube genealogy.

But this does **not** imply

\[
\sum_e\varepsilon_eN_e=0.
\]

For example, births at systematically larger margin than deaths give a positive net event recharge even though unweighted flux is completely recycled.

Thus the remaining event freedom is exactly a margin-weighted birth/death covariance.

---

## 10. Insert into the spatial-core ledger

M17-108 becomes, including generic folds,

\[
\boxed{
\frac d{d\theta}\mathscr N_\Omega
=-\frac32\mathscr N_\Omega
+\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
+\mathscr B_F
+\mathscr B_{other}.
}
\]

For a recurrent positive-margin population,

\[
\boxed{
\left\langle
\mathscr P_\Omega
+\mathscr S_\Omega
+\mathscr F_{in}
-\mathscr F_{out}
+\mathscr B_F
+\mathscr B_{other}
\right\rangle
=\frac32\left\langle\mathscr N_\Omega\right\rangle>0.
}
\]

The generic fold contribution is now explicit rather than hidden inside an abstract event source.

---

## 11. DSD audit

### Audit A — concluding signed-flux neutrality makes the positive margin event-neutral
Rejected.

### Audit B — concluding pair birth always supplies positive long-time recharge
Rejected. Birth is positive and death negative; the cycle average depends on event weighting by `N_e`.

### Audit C — using the algebraically signed inventory as a positive Riccati control
Rejected. It is noncoercive by construction.

### Audit D — assuming all tangencies are generic folds
Rejected. Persistent/higher-order tangencies remain separate finite-jet event classes.

### Audit E — proof status
The generic tangency contribution is explicit, but its recurrent margin covariance has no current fixed sign.

---

## 12. Updated event frontier

Generic tangency no longer appears as an unspecified event source.
Its exact contribution is

\[
\boxed{
\mathscr B_F
=2\int
\varepsilon_FN_F
\delta(\theta-\tau_F)
\,d\Phi_J.
}
\]

Thus the remaining Rank-2 event firewall is

\[
\boxed{
\text{positive }3/2\text{ damping payment}
\;\leftrightarrow?\;
\text{PDE/slide/boundary recharge}
+
\text{margin-weighted fold covariance}.
}
\]

The next useful calculation is to determine whether the fold margin `N_F` itself can be reduced by the tangency identities `D_k g=0` and the flatness resonance `gamma_k=q`, potentially eliminating part of this covariance freedom.

This is the **Tangency Margin Reduction Gate (TMRG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
