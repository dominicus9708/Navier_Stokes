# First-Hitting Switching Time–Dissipation Ledger

Date: 2026-08-25

Status: **QUIET-PACKET TIME TAX PROVED / FAR-STRAIN BALANCE PROVED CONDITIONAL / STAGE-LOCAL PACKET COST IS GEOMETRICALLY SUMMABLE / PACKET COUNT ALONE DOES NOT CONTRADICT ENERGY / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The amplitude–location bridge reduces a remote ancestor to

\[
\text{local deformation/diffusion}
\lor
J\text{-contact}
\lor
\text{dephasing + center/packet switch}.
\]

This note asks whether the last alternative can already be excluded by the ordinary energy-dissipation budget.

The answer is mixed:

1. a quietly persistent critical packet has an exact enstrophy-time cost;
2. if far strain also carries a prescribed amplification on the same scale and interval, the two estimates balance to a linear exposure tax;
3. but a sequence of newly switched natural-scale packets can have geometrically summable first-order dissipation.

Therefore packet multiplicity by itself does **not** close the proof.

---

## 2. Quiet occupied packet gives an enstrophy-time tax

Let an ancestor stage \(n\) have

\[
W_n=\|\omega(t_n)\|_\infty,
\qquad
r_n=\left(\frac{\nu}{W_n}\right)^{1/2}.
\]

Suppose a material packet \(A_n(t)\) survives on an interval

\[
I=[t_n,t_*]
\]

with preserved volume

\[
|A_n(t)|=c_a r_n^3,
\qquad
c_a=\frac{4\pi}{3}a_0^3,
\]

and retained vorticity amplitude

\[
|\omega(x,t)|\ge q_AW_n
\qquad(x\in A_n(t),\ t\in I),
\]

where \(q_A>0\) is fixed by the local genealogy exposure gate.

Then for every \(t\in I\),

\[
\begin{aligned}
\|\omega(t)\|_2^2
&\ge
\int_{A_n(t)}|\omega|^2dx\\
&\ge
c_aq_A^2W_n^2r_n^3.
\end{aligned}
\]

Since

\[
W_n=\frac{\nu}{r_n^2},
\]

we obtain

\[
\boxed{
\|\omega(t)\|_2^2
\ge
c_aq_A^2\frac{\nu^2}{r_n}.
}
\]

Integrating in time,

\[
\boxed{
\int_I\|\omega(t)\|_2^2dt
\ge
c_aq_A^2\frac{\nu^2}{r_n}|I|.
}
\]

Define the parabolic time length

\[
\boxed{
\Theta_{n,I}:=\frac{\nu|I|}{r_n^2}
}
\]

and the normalized enstrophy-time cost

\[
\boxed{
\mathfrak Z_{n,I}
:=
\frac{1}{\nu r_n}
\int_I\|\omega(t)\|_2^2dt.
}
\]

Then

\[
\boxed{
\mathfrak Z_{n,I}
\ge
A_A\Theta_{n,I},
\qquad
A_A:=c_aq_A^2>0.
}
\]

**Status: PROVED.**

---

## 3. Physical first-order dissipation cost

For a smooth divergence-free field on \(\mathbb R^3\) with the required decay,

\[
\|\nabla u\|_2^2=\|\omega\|_2^2.
\]

Hence the energy identity supplies the finite global budget

\[
\nu\int_0^{T^*}\|\omega(t)\|_2^2dt
\le E_0,
\]

where \(E_0\) denotes the initial kinetic-energy budget up to the repository's conventional factor \(1/2\).

For the quiet packet interval,

\[
\boxed{
\nu\int_I\|\omega\|_2^2dt
\ge
A_A\nu^2r_n\Theta_{n,I}.
}
\]

Thus a packet that remains occupied for one natural parabolic time \(\Theta\sim1\) costs order

\[
\boxed{\nu^2r_n}
\]

in physical first-order dissipation.

**Status: PROVED.**

---

## 4. Combine with the existing far-strain tax

The repository's far-strain gate gives, on a compatible natural-scale interval,

\[
\boxed{
\mathfrak Z_{n,I}
\ge
B_R\frac{\eta_F^2}{\Theta_{n,I}},
}
\]

where \(B_R>0\) depends on the fixed normalized near/far cutoff radius and \(\eta_F\) is the normalized accumulated far-strain exposure.

If the same interval also contains the quiet occupied packet from Section 2, then

\[
\mathfrak Z_{n,I}
\ge
\max\left\{
A_A\Theta_{n,I},
B_R\frac{\eta_F^2}{\Theta_{n,I}}
\right\}.
\]

A bookkeeping warning is important: these are two lower bounds on the **same** global enstrophy-time integral, so they must not simply be added.

Using

\[
\max\{x,y\}\ge\sqrt{xy},
\]

we obtain the time-balanced estimate

\[
\boxed{
\mathfrak Z_{n,I}
\ge
\sqrt{A_AB_R}\,|\eta_F|.
}
\]

Consequently, if on this same scale and interval far strain carries at least a fixed fraction \(\beta>0\) of a logarithmic amplification \(L\),

\[
|\eta_F|\ge\beta L,
\]

then

\[
\boxed{
\mathfrak Z_{n,I}
\ge
c\,L.
}
\]

The corresponding physical dissipation obeys

\[
\boxed{
\nu\int_I\|\omega\|_2^2dt
\ge
c\nu^2r_nL.
}
\]

**Status: PROVED CONDITIONAL on the far-strain exposure being measured on the same compatible scale and interval.**

---

## 5. Fixed-ancestor remote amplification would be expensive

For first-hitting stages with amplification factor \(q_H>1\),

\[
\frac{W_j}{W_n}=q_H^{j-n}.
\]

Set

\[
L_{n,j}:=\log\frac{W_j}{W_n}=(j-n)\log q_H.
\]

If a fixed ancestor packet at radius \(r_n\) stays quiet and occupied while a fixed fraction of this entire remote logarithmic amplification is supplied by far strain measured on the same ancestor-scale corridor, then Section 4 gives

\[
\boxed{
\mathfrak Z_{n,[t_n,t_j]}
\gtrsim
(j-n)\log q_H.
}
\]

For fixed \(n\), the physical lower bound is

\[
\nu\int_{t_n}^{t_j}\|\omega\|_2^2dt
\gtrsim
\nu^2r_n(j-n)\log q_H,
\]

which diverges as \(j\to\infty\) and is incompatible with a finite total energy-dissipation budget.

Therefore a remote first-hitting chain cannot keep charging an unbounded fraction of its amplification to **one fixed quiet ancestor-scale far-strain corridor**.

At least one ingredient must change: the active packet, the active scale, the spatial corridor, or the strain mechanism.

**Status: PROVED CONDITIONAL.**

---

## 6. Stage-local packet switching evades the ordinary energy budget

Now consider the mechanism actually relevant to center switching: each new first-hitting generation has its own natural radius

\[
r_j=\left(\frac{\nu}{W_j}\right)^{1/2}.
\]

If

\[
W_{j+1}=q_HW_j,
\qquad q_H>1,
\]

then

\[
\boxed{
r_{j+1}=q_H^{-1/2}r_j.}
\]

A critical occupied packet at scale \(r_j\) has instantaneous enstrophy of order at least

\[
W_j^2r_j^3
\sim
\frac{\nu^2}{r_j}.
\]

If it persists for a natural parabolic time

\[
\tau_j\sim\frac{r_j^2}{\nu},
\]

then its enstrophy-time cost is of order

\[
\frac{\nu^2}{r_j}\frac{r_j^2}{\nu}
\sim
\nu r_j,
\]

and its physical energy-dissipation cost is of order

\[
\boxed{\nu^2r_j.}
\]

But the radii form a geometric sequence:

\[
\sum_{j\ge j_0}r_j
=
r_{j_0}
\sum_{m\ge0}q_H^{-m/2}
<\infty.
\]

Therefore

\[
\boxed{
\sum_j\nu^2r_j<\infty.
}
\]

This is the crucial negative audit:

\[
\boxed{
\text{infinitely many natural-scale center-switched packets}
\not\Rightarrow
\text{infinite ordinary energy dissipation}.
}
\]

Packet count alone cannot prove regularity.

**Status: PROVED as a scaling/summability audit.**

---

## 7. The same obstruction survives a fixed per-stage far-strain tax

Suppose each stage incurs a normalized far-strain exposure bounded below by a fixed constant, for example the amount needed to produce the fixed amplification ratio \(q_H\):

\[
|\eta_{F,j}|\gtrsim\log q_H.
\]

The balanced estimate of Section 4 then gives at most a stagewise physical lower bound of the form

\[
\boxed{
D_j
:=
\nu\int_{I_j}\|\omega\|_2^2dt
\gtrsim
\nu^2r_j\log q_H.
}
\]

Since \(\log q_H\) is fixed and \(\sum r_j<\infty\),

\[
\sum_jD_j
\]

may remain finite.

Thus a fixed normalized tax per generation is not enough. Any energy-based contradiction would require a stage cost growing at least rapidly enough to overcome the geometric factor \(r_j\).

**Status: PROVED / NO CONTRADICTION.**

---

## 8. Required growth rate for a first-order dissipation contradiction

Let a stagewise normalized tax be \(L_j\), so the physical lower bound is schematically

\[
D_j\gtrsim\nu^2r_jL_j.
\]

With

\[
r_j=r_0q_H^{-j/2},
\]

ordinary dissipation contradicts finite energy only if one can force

\[
\boxed{
\sum_jq_H^{-j/2}L_j=\infty.
}
\]

In particular:

- bounded \(L_j\): summable;
- polynomial \(L_j\sim j^m\): still summable;
- merely linear logarithmic-age growth: still summable if attached to the *current* shrinking scale;
- one needs growth comparable to the inverse geometric shrinkage, or a different ledger whose critical weight does not contain the factor \(r_j\).

This explains why the dimensionless cubic annular ledger remains essential.

**Status: PROVED.**

---

## 9. Near-strain amplification returns to the derivative corridor

At a natural scale

\[
r(t)=\left(\frac{\nu}{M(t)}\right)^{1/2},
\qquad M(t)=\|\omega(t)\|_\infty,
\]

the near-strain cancellation from the analyticity audit has the schematic form

\[
\|S_{\rm near}(t)\|_\infty
\lesssim
r(t)^2\|\nabla^2\omega(t)\|_\infty.
\]

Define the dimensionless second-vorticity-derivative concentration

\[
\boxed{
K_2(t)
:=
\frac{\nu\|\nabla^2\omega(t)\|_\infty}{M(t)^2}.
}
\]

Since \(r(t)^2=\nu/M(t)\),

\[
\boxed{
\|S_{\rm near}(t)\|_\infty
\lesssim
M(t)K_2(t).
}
\]

Hence if near strain rather than far strain supplies a logarithmic first-hitting amplification over an interval,

\[
\boxed{
\int_I M(t)K_2(t)dt
\gtrsim
\log\frac{M(t_2)}{M(t_1)}
}
\]

up to the share of amplification assigned to the near branch.

This is a higher-derivative exposure, not an ordinary energy contradiction. It reconnects directly to the derivative-concentration descent and analyticity-radius corridor.

**Status: PROVED CONDITIONAL on the near/far attribution.**

---

## 10. Several packet contacts only give a one-way \(J\) ledger

Suppose at one age-\(k\) annulus there are disjoint packet contact sets \(E_m\), each satisfying

\[
|\omega|\ge q_mW_n
\quad\text{on }E_m.
\]

Define

\[
\chi_m=\frac{|E_m|}{r_n^3}.
\]

Then

\[
\begin{aligned}
J_{j,k}
&\ge
\frac{r_n}{2}
\sum_m\int_{E_m}|\omega|^2dx\\
&\ge
\frac{\nu^2}{2}
\sum_mq_m^2\chi_m.
\end{aligned}
\]

Therefore

\[
\boxed{
J_{j,k}
\ge
\frac{\nu^2}{2}
\sum_mq_m^2\chi_m.
}
\]

This proves that many substantial packet contacts are expensive in the annular amplitude ledger.

But the reverse implication is unavailable:

\[
J_{j,k}\text{ large}
\stackrel{?}{\Longrightarrow}
\text{many identified switched packets}
\]

requires an additional covering/completeness or amplitude-occupancy statement.

**Status: FORWARD BOUND PROVED / REVERSE COVERING NOT DERIVED.**

---

## 11. Interaction with the cubic genealogy-deficit ledger

On the corrected bounded-\(Z\), recurrent, non-\(L^3\) branch,

\[
\sum_kJ_k^{3/2}=\infty,
\]

while the weighted return argument forces the divergent cubic mass onto scales with arbitrarily small return ratio.

The present note shows that such a divergence cannot be contradicted merely by counting natural-scale switched packets, because their first-order physical costs carry the summable factor \(r_j\).

Therefore the switching branch must be attacked **inside the dimensionless annular ledger itself**.

The missing implication has now sharpened to

\[
\boxed{
\text{repeated center/packet switching}
\stackrel{?}{\Longrightarrow}
\text{enough identified annular contact/coverage to charge }
\sum_kJ_k^{3/2}.
}
\]

A simple ordinary-energy packing argument is too weak.

---

## 12. Audit table

| Statement | Status |
|---|---|
| Quiet critical packet gives \(\mathfrak Z\gtrsim\Theta\) | PROVED |
| Far strain gives \(\mathfrak Z\gtrsim\eta_F^2/\Theta\) | PROVED previously |
| The two lower bounds may simply be added | FALSE |
| Combined bounds give \(\mathfrak Z\gtrsim|\eta_F|\) | PROVED |
| One fixed ancestor corridor carrying unbounded remote far amplification violates finite dissipation | PROVED CONDITIONAL |
| One natural-scale switched packet per generation forces infinite energy cost | FALSE |
| Fixed normalized per-stage tax defeats geometric radius shrinkage | FALSE |
| Polynomial stage tax defeats geometric radius shrinkage | FALSE |
| Near-strain attribution forces higher-derivative exposure | PROVED CONDITIONAL |
| Multiple identified packet contacts force annular \(J\)-cost | PROVED |
| Annular \(J\)-mass is automatically covered by switched packets | NOT DERIVED |
| Cubic nonsummability is branch-universal | FALSE; bounded-\(Z\)+recurrent+non-\(L^3\) scope retained |
| Global regularity | UNPROVED |

---

## 13. Updated frontier

The ordinary energy route has now been pruned to its exact strength:

\[
\boxed{
\text{fixed corridor + growing remote exposure}
\Rightarrow
\text{dissipation contradiction},
}
\]

but

\[
\boxed{
\text{scale-switching each generation}
\Rightarrow
\text{only }O(\nu^2r_j)\text{ physical cost, potentially summable}.
}
\]

Hence the active bottleneck is no longer packet persistence alone. It is the **coverage problem**:

\[
\boxed{
\text{Does the switched-packet family necessarily account for a fixed fraction of the divergent annular cubic mass?}
}
\]

If yes, the cubic genealogy-deficit ledger can be applied to switching. If no, the remaining mass is a genuinely non-material shell-rebuilding branch that must be analyzed separately.