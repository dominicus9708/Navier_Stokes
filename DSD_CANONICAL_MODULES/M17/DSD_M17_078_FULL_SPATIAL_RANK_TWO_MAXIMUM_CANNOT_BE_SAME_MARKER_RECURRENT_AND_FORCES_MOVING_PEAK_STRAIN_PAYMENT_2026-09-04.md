# DSD M17-078 — A full spatial Rank-2 amplitude maximum cannot be same-marker recurrent and forces a moving-peak strain payment

Date: 2026-09-04
Canonical ID: **M17-078**

Status: **INTERNAL RECHARGE–PAYER DOMAIN AUDIT / M17-077 CONCERNS LINEWISE MAXIMA `g=D_xi log rho=0`, WHILE M17-027'S STRICT NEGATIVE-KAPPA PAYER APPLIES ONLY TO FULL SPATIAL AMPLITUDE MAXIMA `grad rho=0`, `Delta rho<=0`. THESE DESCRIPTORS MUST NOT BE IDENTIFIED. ON THEIR INTERSECTION, HOWEVER, M17-027 GIVES `kappa<=-|grad xi|^2<=-2|J_xi|<0`. A PURE-KERNEL RANK-TWO MATERIAL MARKER THAT REMAINS A FULL SPATIAL MAXIMUM AND IS UNIFORMLY RECURRENT WOULD SIMULTANEOUSLY FALL UNDER M17-033, WHICH REQUIRES `mean kappa=3/2`; THIS IS IMPOSSIBLE BECAUSE KAPPA IS POINTWISE NEGATIVE AT THE MAXIMUM. THEREFORE ANY RECURRENT FULL-SPATIAL-MAXIMUM NETWORK IN THE RETAINED RANK-TWO REGION MUST USE MAXIMUM-LOCATION TURNOVER / RELATIVE TRANSPORT RATHER THAN ONE PERSISTENT MATERIAL CARRIER. FOR A MOVING FULL MAXIMUM THE VALUE DERIVATIVE HAS NO RELATIVE-VELOCITY TERM BECAUSE `grad rho=0`, SO `d/dtheta log rho_max=sigma+kappa-1`; RECURRENCE GIVES `mean(sigma+kappa)=1`, AND THE NEGATIVE-KAPPA PAYER IMPLIES `mean sigma>=1+mean|grad xi|^2>=1+2mean|J_xi|`. THUS THE MOVING FULL MAXIMUM MUST PAY THE GEOMETRIC NEGATIVE-KAPPA COST WITH STRONG POSITIVE VORTEX-DIRECTION STRAIN. THIS DOES NOT FIX THE SIGN OF M17-077'S HIGHER-JET RECHARGE SOURCE, SO THE FROZEN-ANGLE LINE-MAXIMUM FIREWALL REMAINS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two different maximum descriptors

The current Rank-2 analysis uses two notions which must remain distinct.

### Linewise maximum

M17-040/M17-047 use

\[
\boxed{
g:=D_\xi\log\rho=0,
\qquad
C:=D_\xi g<0.}
\]

This means that `rho` is maximal only in the vortex-line direction `xi`.
It does **not** imply

\[
\nabla\rho=0.
\]

### Full spatial maximum

M17-027 uses

\[
\boxed{
\nabla\rho=0,
\qquad
\Delta\rho\le0,
\qquad
\rho>0.}
\]

This is a genuine local maximum in all three spatial directions.

Therefore

\[
\boxed{
\text{full spatial maximum}
\Longrightarrow
\text{linewise critical point},
}
\]

but the converse is false.

---

## 2. Negative-kappa payer at a full Rank-2 maximum

The scalar amplitude equation is

\[
\boxed{
\Delta\rho
=(\kappa+|\nabla\xi|^2)\rho.
}
\]

At a full spatial maximum,

\[
\Delta\rho\le0,
\]

so

\[
\boxed{
\kappa
\le-|\nabla\xi|^2.
}
\]

On Rank 2,

\[
|\nabla\xi|^2\ge2|J_\xi|>0.
\]

Hence

\[
\boxed{
\kappa
\le-|\nabla\xi|^2
\le-2|J_\xi|
<0.
}
\]

This strict sign is available only on the full-maximum descriptor.

---

## 3. Same-marker recurrent pure-kernel Rank-2 law

On the intrinsic pure-kernel Rank-2 branch, M17-033 gives for a uniformly recurrent material carrier with recurrent nonzero director jets and vorticity amplitude

\[
\boxed{
\langle\sigma\rangle=-\frac12,
\qquad
\langle\kappa\rangle=\frac32.
}
\]

The second relation follows from

\[
D_B\log\rho=\sigma+\kappa-1
\]

combined with recurrence of `rho` and the recurrent director-jet multiplier fixing `mean sigma=-1/2`.

---

## 4. Same material marker cannot remain a recurrent full spatial maximum

Assume one full-rank-two pure-kernel material marker remains a full spatial amplitude maximum for all times in a recurrent regime.

Then Section 2 gives pointwise

\[
\boxed{\kappa<0.}
\]

Therefore its time average satisfies

\[
\boxed{\langle\kappa\rangle\le0.}
\]

But Section 3 requires

\[
\boxed{\langle\kappa\rangle=\frac32.}
\]

Contradiction.

Thus

\[
\boxed{
R_{2,pure-kernel}^{same-marker\ recurrent\ full\ maximum}
\Longrightarrow\bot.
}
\]

This is a genuine closure of a further Rank-2 subbranch.

---

## 5. What must replace same-marker persistence

A recurrent Eulerian full-maximum pattern may still exist if the maximizing location is continually occupied by different material labels.

Therefore the allowed exit is

\[
\boxed{
\text{maximum-location turnover / relative transport}
}
\]

or one of the already known exits:

\[
\boxed{
\text{rank loss},
\quad
\text{critical degeneration},
\quad
\text{branch/interface turnover}.
}
\]

This result explains why the moving-critical formulation of M17-076/M17-077 is not merely optional bookkeeping.
It is structurally required for any recurrent full-maximum survivor.

---

## 6. Value derivative at a moving full spatial maximum

Let

\[
x_*(\theta)
\]

be a smooth path of full spatial maxima.
Define

\[
\rho_*(\theta):=\rho(x_*(\theta),\theta).
\]

Because

\[
\nabla\log\rho(x_*,\theta)=0,
\]

we have

\[
\frac d{d\theta}\log\rho_*
=\partial_\theta\log\rho.
\]

Also at the maximum

\[
B\cdot\nabla\log\rho=0,
\]

so

\[
D_B\log\rho=\partial_\theta\log\rho.
\]

Using the CE-H amplitude law

\[
D_B\log\rho=\sigma+\kappa-1,
\]

we obtain the exact moving-peak value law

\[
\boxed{
\frac d{d\theta}\log\rho_*
=\sigma_*+\kappa_*-1.
}
\]

The relative velocity of the maximum does not appear in this scalar value equation because the spatial gradient vanishes.

---

## 7. Recurrent moving peak forces a strain payment

If the full-maximum amplitude is recurrent and bounded above/below, then

\[
\left\langle
\frac d{d\theta}\log\rho_*
\right\rangle=0.
\]

Hence

\[
\boxed{
\langle\sigma+\kappa\rangle_{peak}=1.
}
\]

Therefore

\[
\boxed{
\langle\sigma\rangle_{peak}
=1-\langle\kappa\rangle_{peak}.
}
\]

Section 2 gives

\[
-\kappa\ge|\nabla\xi|^2\ge2|J_\xi|.
\]

Thus

\[
\boxed{
\langle\sigma\rangle_{peak}
\ge
1+\langle|\nabla\xi|^2\rangle_{peak}
\ge
1+2\langle|J_\xi|\rangle_{peak}.
}
\]

On a rank-separated recurrent peak network with

\[
|J_\xi|\ge J_*>0,
\]

this sharpens to

\[
\boxed{
\langle\sigma\rangle_{peak}
\ge1+2J_*>1.
}
\]

The moving full maximum must therefore support strong positive vortex-direction strain to pay for its director-area negative-kappa cost.

---

## 8. Trace-free strain consequence

Because

\[
\sigma+\sigma_k+\sigma_n=0,
\]

Section 7 implies

\[
\boxed{
\langle\sigma_k+\sigma_n\rangle_{peak}
=-\langle\sigma\rangle_{peak}
\le-1-2\langle|J_\xi|\rangle_{peak}.
}
\]

Thus the full maximum is accompanied on average by strong transverse compression in the trace-free strain budget.

This does not specify how that compression is split between `k` and `n`.

---

## 9. Intersection with the frozen-angle recharge problem

A full spatial maximum on the frozen-angle branch is also a linewise maximum, so M17-077 may apply if the additional `n`-tangent and regularity hypotheses hold.

However M17-077's recharge source is

\[
\boxed{
\mathscr R_{FA}
=pD_k(\sigma_n-\sigma)
+D_\xi^2(\sigma+\kappa)
-(\sigma-\sigma_k)C.
}
\]

The full-maximum inequality supplies the value/sign information

\[
\kappa<0,
\]

and the moving-peak average supplies

\[
\langle\sigma+\kappa\rangle=1.
\]

Neither determines the signs of

\[
D_k(\sigma_n-\sigma),
\qquad
D_\xi^2(\sigma+\kappa),
\qquad
(\sigma-\sigma_k)C.
\]

Therefore the negative-kappa payer cannot presently be converted into a sign theorem for `R_FA`.

---

## 10. Hessian information at the full maximum

At a full spatial maximum of `log rho`, its Hessian is negative semidefinite.
In particular,

\[
\boxed{
C=D_\xi^2\log\rho\le0.
}
\]

At a nondegenerate line maximum,

\[
C<0.
\]

Mixed Hessian components satisfy the usual negative-semidefinite Cauchy bounds, but these involve second derivatives of `log rho`.
The M17-077 recharge source instead contains derivatives of strain and `kappa`.

No current identity converts the Hessian semidefiniteness into the required sign of `R_FA`.

---

## 11. DSD interpretation

The word `maximum` was carrying two distinct descriptor levels:

\[
\boxed{
\text{line maximum}
\subsetneq
\text{full spatial maximum condition set only after extra derivatives vanish}.
}
\]

The negative-kappa payer belongs to the stronger full-spatial descriptor.
Once that distinction is respected, one legitimate closure appears: a full maximum cannot be both same-marker and recurrent in the pure-kernel Rank-2 branch.

The surviving recurrent peak must be a turnover object.

---

## 12. DSD audit

### Audit A — applying M17-027 to every line maximum
Rejected. `D_xi rho=0` is insufficient for the full maximum principle.

### Audit B — using same-marker `mean kappa=3/2` on a moving peak
Rejected. It applies only to one recurrent material carrier.

### Audit C — same-marker full-maximum contradiction
Accepted under the explicit M17-033 recurrence hypotheses: pointwise `kappa<0` is incompatible with `mean kappa=3/2`.

### Audit D — claiming the moving peak has the same mean strain frame as M17-033
Rejected. The moving network has its own exact value law instead.

### Audit E — claiming negative kappa signs the M17-077 recharge source
Rejected. The source is higher-jet and remains signed.

### Audit F — proof status
One further same-marker Rank-2 maximum subbranch is closed; moving peak turnover remains open.

---

## 13. Updated Rank-2 maximum frontier

\[
\boxed{
R_{2}^{full\ spatial\ maximum,recurrent}
\Longrightarrow
R_{peak}^{moving/turnover}
\ \lor\
T_{rank/critical/interface}.
}
\]

The same-marker recurrent full-maximum branch is removed.

A recurrent moving full maximum must satisfy

\[
\boxed{
\langle\sigma+\kappa\rangle_{peak}=1,
}
\]

with

\[
\boxed{
\kappa\le-|\nabla\xi|^2\le-2|J_\xi|<0.
}
\]

Hence

\[
\boxed{
\langle\sigma\rangle_{peak}
\ge1+2\langle|J_\xi|\rangle_{peak}.
}
\]

---

## 14. Next target

The present payer coupling does not sign the frozen-angle higher-jet recharge.
The next highest-value Rank-2 step is therefore to compare the two genuinely surviving compensation mechanisms:

1. orthogonal stretch — mixed-Hessian payment
   \[
   E(D_\xi q)(D_nD_\xi d)>(D_\xi^2d)^2;
   \]
2. frozen angle — normalized-shear/margin payment with exact `3/2` damping
   \[
   N_{FA}>0,
   \qquad
   D_{max}N_{FA}=-\frac32N_{FA}+|a|\mathscr R_{FA}+v_{rel}D_\xi N_{FA}.
   \]

The purpose is to determine whether these are truly disjoint mechanisms or two limits of one normalized anisotropy-Hessian transport law.

This is the **Rank-Two Unified Compensation Gate (R2UCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
