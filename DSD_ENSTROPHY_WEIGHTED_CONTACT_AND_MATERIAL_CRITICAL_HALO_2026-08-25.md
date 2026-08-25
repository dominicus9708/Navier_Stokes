# DSD Enstrophy-Weighted Contact and Material Critical Halo

Date: 2026-08-25

Status: **EXACT L2-WEIGHTED CONTACT/REPLACEMENT SPLIT PROVED / ARTIFICIAL COHERENT-BALL CONTACT LOSS REMOVED / QUIET-ANCESTOR CRITICAL CAPACITY BOUND PROVED / MATERIAL CONTACT SHOWN SCALE-NEUTRAL WITH THE 1/R CRITICAL TAIL / FIXED-AGE CONTACT DOES NOT CLOSE THE CUBIC GENEALOGY DEFICIT / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`DSD_FIXED_LAG_PACKET_IDENTITY_REPLACEMENT_GATE_2026-08-25.md` defined the R branch through the volume overlap of a coherent Eulerian subpacket with the transported material ancestor packet.

That construction is valid for a fixed shell, but it first converts shell `L2` mass to a pointwise coherent ball. For quantitative all-age work this introduces avoidable losses through the analytic Lipschitz radius.

The shell information is already an `L2` vorticity quantity, so material contact can instead be measured directly by **enstrophy-weighted overlap**.

This note derives that exact split and audits its critical scaling.

---

## 2. First-hitting and age-k variables

At current first-hitting stage `j`, use

\[
W_j=q^jW_0,
\qquad
r_j=\sqrt{\frac\nu{W_j}}.
\]

For age `k`, let

\[
n=j-k,
\]

so

\[
W_n=q^{-k}W_j,
\qquad
r_n=q^{k/2}r_j.
\]

In current normalized coordinates

\[
y=\frac{x-X_j}{r_j},
\qquad
\Omega_j=\frac\omega{W_j},
\]

use the geometric shell

\[
A_k=\{R_k\le |y|<\lambda R_k\},
\qquad
R_k=R_0q^{k/2},
\qquad
\lambda=\sqrt q.
\]

Define

\[
\boxed{
m_{j,k}(t):=\int_{A_k}|\Omega_j(y,t)|^2dy}
\]

and the vorticity critical shell number

\[
\boxed{
J^\omega_{j,k}(t):=R_km_{j,k}(t).
}
\]

Let the corresponding physical shell be

\[
\mathcal A_{j,k}(t):=X_j+r_jA_k.
\]

---

## 3. Exact ancestor-scale conversion of shell enstrophy

The physical shell enstrophy is

\[
\int_{\mathcal A_{j,k}}|\omega|^2dx
=W_j^2r_j^3m_{j,k}.
\]

Since

\[
r_j^2=\frac\nu{W_j},
\qquad
r_n=q^{k/2}r_j,
\]

we obtain exactly

\[
\begin{aligned}
\frac{r_n}{\nu^2}
\int_{\mathcal A_{j,k}}|\omega|^2dx
&=
\frac{q^{k/2}r_j}{\nu^2}
W_j^2r_j^3m_{j,k}\\
&=q^{k/2}m_{j,k}\\
&=\frac{J^\omega_{j,k}}{R_0}.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{r_n}{\nu^2}
\int_{\mathcal A_{j,k}}|\omega|^2dx
=
\frac1{R_0}J^\omega_{j,k}.
}
\]

This identity has no analyticity constant and no coherent-ball radius.

Status: **PROVED EXACTLY.**

---

## 4. Enstrophy-weighted material contact fraction

Let

\[
A_n(t)=\Phi_{t_n,t}(A_n^0)
\]

be the material image of the stage-`n` maximum packet.

When `m_{j,k}>0`, define

\[
\boxed{
\eta_{j,k}(t)
:=
\frac{
\int_{\mathcal A_{j,k}(t)\cap A_n(t)}|\omega|^2dx
}{
\int_{\mathcal A_{j,k}(t)}|\omega|^2dx
}.
}
\]

Then

\[
0\le\eta_{j,k}\le1.
\]

Fix any

\[
0<\alpha<1.
\]

This gives an exact weighted split:

\[
\boxed{
\eta_{j,k}\ge\alpha
\quad\lor\quad
\eta_{j,k}<\alpha.
}
\]

No pointwise packet extraction is required to define this split.

---

## 5. Weighted R branch: direct return certificate

If

\[
\eta_{j,k}\ge\alpha,
\]

then

\[
\int_{\mathcal A_{j,k}\cap A_n(t)}|\omega|^2dx
\ge
\alpha
\int_{\mathcal A_{j,k}}|\omega|^2dx.
\]

Using the exact conversion,

\[
\boxed{
\frac{r_n}{\nu^2}
\int_{\mathcal A_{j,k}\cap A_n(t)}|\omega|^2dx
\ge
\frac\alpha{R_0}J^\omega_{j,k}.
}
\]

Pointwise

\[
|\nabla u|^2
=|S|^2+\frac12|\omega|^2
\ge\frac12|\omega|^2,
\]

so

\[
\boxed{
\frac{r_n}{\nu^2}
\int_{\mathcal A_{j,k}\cap A_n(t)}|\nabla u|^2dx
\ge
\frac\alpha{2R_0}J^\omega_{j,k}.
}
\]

Thus weighted contact carries the full critical shell quantity linearly, without the small coherent-ball volume factor of the previous R certificate.

Status: **PROVED.**

---

## 6. Weighted low-contact branch: direct replacement mass

If

\[
\eta_{j,k}<\alpha,
\]

then

\[
\int_{\mathcal A_{j,k}\setminus A_n(t)}|\omega|^2dx
>(1-\alpha)
\int_{\mathcal A_{j,k}}|\omega|^2dx.
\]

Therefore

\[
\boxed{
\frac{r_n}{\nu^2}
\int_{\mathcal A_{j,k}\setminus A_n(t)}|\omega|^2dx
>
\frac{1-\alpha}{R_0}J^\omega_{j,k}.
}
\]

This is a rigorous **material replacement-mass certificate**: a fixed fraction of the shell's vorticity `L2` mass is carried by material points not belonging to the transported stage-`n` maximum packet.

It is stronger quantitatively than merely saying that some point lies outside the ancestor packet, but it does not by itself imply a spatially separated coherent second ball.

Status: **PROVED.**

---

## 7. Quiet ancestor gives an age-independent critical capacity ceiling

On the quiet material-transport branch imported from `AMPLITUDE_LOCATION_GENEALOGY_BRIDGE_2026-08-25.md`, suppose

\[
|\omega(x,t)|\le Q_LW_n
\qquad(x\in A_n(t)).
\]

Incompressibility preserves the ancestor volume:

\[
|A_n(t)|=|A_n^0|
=V_0r_n^3,
\qquad
V_0:=\frac{4\pi}{3}a_0^3.
\]

Hence

\[
\int_{A_n(t)}|\omega|^2dx
\le
V_0Q_L^2W_n^2r_n^3.
\]

If the weighted R branch holds,

\[
\alpha
\int_{\mathcal A_{j,k}}|\omega|^2dx
\le
V_0Q_L^2W_n^2r_n^3.
\]

Multiply by `r_n/nu^2`. Since

\[
W_nr_n^2=\nu,
\]

we get

\[
\frac{r_n}{\nu^2}
V_0Q_L^2W_n^2r_n^3
=V_0Q_L^2.
\]

Therefore

\[
\boxed{
J^\omega_{j,k}
\le
\frac{R_0V_0Q_L^2}{\alpha}.
}
\]

The upper bound is independent of `j` and, crucially, independent of the age `k`.

Status: **PROVED.**

---

## 8. Critical neutrality of the material-contact branch

The previous bound explains why R contact is not automatically contradictory.

A stage-`n` ancestor packet has its natural scales

\[
|\omega|\sim W_n,
\qquad
\text{radius}\sim r_n.
\]

Viewed at stage `j=n+k`,

\[
\frac{W_n}{W_j}=q^{-k}
\]

and

\[
\frac{r_n}{r_j}=q^{k/2}.
\]

Since

\[
R_k=R_0q^{k/2},
\]

the same packet has the current normalized scaling

\[
\boxed{
|\Omega_j|\sim q^{-k}
\sim R_k^{-2}.
}
\]

Its normalized volume is of order

\[
q^{3k/2}\sim R_k^3,
\]

so its shell enstrophy scales like

\[
m_k
\sim
R_k^{-4}R_k^3
=R_k^{-1}.
\]

Thus

\[
\boxed{
J_k^\omega=R_km_k\sim1.
}
\]

At the level of dimensional scaling, a coherent vortex packet with vorticity scale `W_n` and size `r_n` has velocity scale `W_nr_n=nu/r_n`. In current normalized velocity units,

\[
U_j\sim
\frac{r_j}{\nu}\frac\nu{r_n}
=\frac{r_j}{r_n}
=q^{-k/2}
\sim R_k^{-1}.
\]

Therefore persistent old material packets realize exactly the unresolved critical tail scaling

\[
\boxed{
U\sim R^{-1},
\qquad
\Omega\sim R^{-2},
\qquad
R\int_{A_R}|\nabla U|^2\sim1.
}
\]

The velocity estimate in this paragraph is a scaling model for a coherent non-cancelling packet, not a universal pointwise lower bound.

Status: **EXACT SCALE MATCH FOR VORTICITY/RADIUS; VELOCITY STATEMENT IS DIMENSIONAL/COHERENT-PACKET SCALING.**

---

## 9. Why fixed-age positive-density contact is still insufficient for the cubic-tail contradiction

For one fixed age `k_0`, positive-density weighted contact gives a genuine return certificate for that one shell class.

But the cubic-tail obstruction is

\[
\sum_kJ_k^{3/2}=\infty
\]

across unbounded shell age.

One fixed shell contributes only one term to this series.

Therefore

\[
\boxed{
R_{+dens}(k_0)
\not\Longrightarrow
\mathfrak R_k\gtrsim J_k^{1/2}
\text{ on a cubic-divergent set of ages}.
}
\]

This is the same scope distinction already required in the fixed-shell and DEMHCT audits.

Status: **PROVED AS A LOGICAL SCOPE AUDIT.**

---

## 10. Positive Leray-time density does not remove the physical shrinking-scale weight

For an event in stage `j` at fixed age `k`, write

\[
\widehat\Theta_j(t):=W_j(T^*-t).
\]

On the two-sided first-hitting corridor, `widehat Theta_j(t)` is bounded above and below by fixed positive constants throughout the stage, up to the already established corridor constants.

Since

\[
ds=\frac{dt}{T^*-t},
\]

we have

\[
dt=\frac{\widehat\Theta_j(t)}{W_j}ds.
\]

Also

\[
r_n=q^{k/2}\sqrt{\frac\nu{W_j}}.
\]

Hence

\[
\boxed{
\frac{dt}{r_n}
=
\frac{\widehat\Theta_j(t)}{\nu}
q^{-k/2}r_j\,ds
=
\frac{\widehat\Theta_j(t)}{\nu}
q^{-k}r_n\,ds.
}
\]

Thus a positive density in Leray time still carries the shrinking physical factor `r_j` in the ordinary dissipation/return-density ledger.

Consequently fixed-age recurrent contact is not automatically an infinite physical dissipation cost.

Status: **PROVED.**

---

## 11. Relation to the passive critical tail

The critical-contact scaling is not an accidental match.

`ANCIENT_CRITICAL_TAIL_DILATION_CONVEYOR_2026-08-24.md` proves that the passive far-tail Leray equation transports a shell outward by

\[
R\mapsto e^{\Delta s/2}R
\]

while preserving the critical shell quantities.

The first-hitting/Leray clock satisfies

\[
s_j=j\log q+O(1).
\]

Therefore one first-hitting generation corresponds, up to bounded clock defect, to the dilation factor

\[
e^{(\log q)/2}=q^{1/2}.
\]

This is exactly the age-shell factor

\[
R_{k+1}/R_k=q^{1/2}.
\]

Hence a genealogical chain of retained material ancestors is the natural material-scale realization of the Leray critical dilation conveyor.

This statement identifies the scale correspondence; it does not assert exact DSS or exact spatial trajectory recurrence.

---

## 12. Updated R-branch interpretation

The R branch should no longer be viewed primarily as an isolated contact event awaiting a local energy contradiction.

Its critical form is

\[
\boxed{
\text{old material packet retained at scale }r_{j-k}
\Longleftrightarrow
\text{current remote shell at }R_k\sim q^{k/2}
}
\]

with the scale-neutral critical quantities

\[
\boxed{
\Omega\sim R^{-2},
\qquad
m_R\sim R^{-1},
\qquad
J_R^\omega\sim1.
}
\]

Therefore an all-age R survivor is a candidate **material critical halo**, not something ordinary energy estimates should be expected to eliminate automatically.

---

## 13. DSD audit

The following objects remain distinct:

- gradient critical shell number `J_k` from the non-L3 velocity-tail ledger;
- vorticity critical shell number `J_k^omega=R_km_k`;
- enstrophy-weighted material contact fraction `eta_j,k`;
- material replacement mass outside `A_n(t)`;
- coherent pointwise subpacket from analyticity.

The new weighted R/T split uses `J_k^omega` only.

No claim is made that cubic divergence of the gradient `J_k` stack automatically implies cubic divergence of the vorticity `J_k^omega` stack.

That gradient-vorticity tail bridge remains a separate obligation.

---

## 14. Updated frontier

The R route has been sharpened to two tasks:

1. **tail-wide genealogy:** determine whether a cubic-divergent set of critical remote shell ages is carried by weighted material contact rather than replacement;
2. **material critical-halo dynamics:** if so, use the established dilation-conveyor and local-tail-decoupling results to reduce a globally recurrent halo to historical replenishment, or classify it as a nonrecurrent passive tail escaping to infinity.

The first task is a gradient/vorticity-shell and all-age selection problem.

The second is a global recurrence/topology problem rather than an ordinary local energy-budget problem.

---

## 15. Audit verdict

### PROVED

- exact ancestor-scale conversion of shell vorticity enstrophy;
- exact enstrophy-weighted contact/replacement split;
- direct critical gradient-energy lower bound on the weighted contact portion;
- direct critical vorticity replacement mass on the low-contact portion;
- quiet ancestor imposes an age-independent upper capacity on `J_k^omega` in the contact branch;
- old material packet scales as `Omega ~ R^-2` in current coordinates;
- its critical vorticity shell number is scale-neutral;
- the first-hitting generation factor matches the Leray dilation-conveyor factor;
- fixed-age positive-density contact alone does not close the cubic-tail genealogy deficit.

### NOT DERIVED

- cubic divergence of the vorticity critical shell stack;
- tail-wide material contact on a cubic-divergent set;
- a scale-uniform weighted-return-density lower bound;
- exact global recurrence/DSS of the material halo;
- closure of the escaping passive-tail topology problem;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
