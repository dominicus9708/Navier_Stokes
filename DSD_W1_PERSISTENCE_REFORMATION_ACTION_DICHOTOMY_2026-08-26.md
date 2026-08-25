# DSD W1 Persistence--Reformation Action Dichotomy — Corrected Audit

Date: 2026-08-26

Status: **CORRECTED: ACTUAL H1 SHELL VARIATION DISTINGUISHED FROM ITS H2 CAPACITY UPPER BOUND / FINITE ACTUAL VARIATION GIVES PERSISTENT DUAL CURRENT / INFINITE ACTUAL VARIATION SPLIT INTO CONCENTRATED VS DIFFUSE REFORMATION / H2 ESCALATION ALONE DOES NOT PROVE REFORMATION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose of the correction

The first version of this note introduced

\[
\sum_k R_k^{-2/3}(\mathfrak E_{2,k}^{pair})^{1/3}
\]

and called it a reformation action.

That terminology was too strong.

The interpolation estimate is one-sided:

\[
\|\delta F_R\|_{H^1}
\le
C R^{-2/3}(\mathfrak E_{2,R}^{pair})^{1/3}.
\]

Therefore divergence of the right-hand-side series does **not** imply divergence of the actual shell-state variation.  A state may carry very large H2 structure while the co-moving H1 profile changes little because of cancellation or internal oscillation.

The DSD audit must distinguish the actual structural change from the capacity available to pay for that change.

---

## 2. Shell state and exact weak inheritance

For a remote shell radius `R`, define

\[
F_R(z,s):=R U(Rz,s)
\]

on a fixed enlarged annulus.

The all-age W1 transport estimate gives

\[
\boxed{
\|\delta F_R(h)\|_{H^{-1}}
\le C R^{-2}
\qquad\forall h\ge0.
}
\]

Define

\[
\mathfrak E_2(R,s)
:=
R^3\int_{A_R^*}|\nabla^2U|^2dY.
\]

Then, for a co-moving comparison pair,

\[
\|\delta F_R(h)\|_{H^2}
\le C(\mathfrak E_{2,R}^{pair})^{1/2}.
\]

Interpolating `H^-1` and `H2` to `H1`,

\[
\boxed{
\|\delta F_R(h)\|_{H^1}
\le
C R^{-2/3}(\mathfrak E_{2,R}^{pair})^{1/3}.
}
\]

This estimate is retained unchanged.

---

## 3. Actual formation variation versus H2 capacity

Take

\[
h_0=2\log2,
\qquad R_k=2^kR_0.
\]

Define the actual co-moving shell-state increment

\[
\boxed{
d_k
:=
\left\|
F_{R_{k+1}}(\Phi_{h_0}U)-F_{R_k}(U)
\right\|_{H^1}.
}
\]

The **actual formation variation** is

\[
\boxed{
\mathfrak V_{form}
:=
\sum_{k=0}^{\infty}d_k.
}
\]

Separately define the **H2 reformation capacity**

\[
\boxed{
\mathfrak A_{cap}
:=
\sum_{k=0}^{\infty}
R_k^{-2/3}(\mathfrak E_{2,k}^{pair})^{1/3}.
}
\]

The rigorous relation is only

\[
\boxed{
\mathfrak V_{form}
\le C\mathfrak A_{cap}.
}
\]

Consequently

\[
\boxed{
\mathfrak A_{cap}<\infty
\Longrightarrow
\mathfrak V_{form}<\infty,
}
\]

but the converse implication is not asserted, and

\[
\boxed{
\mathfrak A_{cap}=\infty
\not\Longrightarrow
\mathfrak V_{form}=\infty.
}
\]

This is the central audit correction.

---

## 4. Subquadratic H2 growth is a sufficient persistence criterion

If for some `epsilon>0`

\[
\mathfrak E_{2,k}^{pair}
\le C R_k^{2-\varepsilon}
\]

for all sufficiently large `k`, then

\[
R_k^{-2/3}(\mathfrak E_{2,k}^{pair})^{1/3}
\le C R_k^{-\varepsilon/3}.
\]

The dyadic series converges, so

\[
\boxed{
\mathfrak E_2(R)=O(R^{2-\varepsilon})
\Longrightarrow
\mathfrak A_{cap}<\infty
\Longrightarrow
\mathfrak V_{form}<\infty.
}
\]

Thus moderate H2 growth remains firmly on the persistent side.

However near-quadratic H2 growth is only **capable** of supporting reformation; it does not prove that reformation actually occurs.

---

## 5. Finite actual variation gives persistent inherited shell state

If

\[
\boxed{
\mathfrak V_{form}<\infty,
}
\]

then the co-moving shell states form a Cauchy sequence in `H1`.

Hence there is a canonical inherited asymptotic shell state in `H1` along the dyadic ladder.

The weighted-vorticity shell charge is continuous under this H1 convergence. Together with the already proved cumulative lower bound

\[
\bar I(R)\gtrsim\log R,
\]

this forces a nonzero asymptotic vorticity charge. Therefore the finite-variation corridor lies on the persistent dual-current endpoint:

\[
\boxed{
\mathfrak V_{form}<\infty
\Longrightarrow
\mathcal S_B(\infty)>0,
\qquad
\mathcal S_\Omega(\infty)>0.
}
\]

No uniform H2 ceiling is required for this conclusion once actual H1 variation itself is known to be summable.

---

## 6. Actual reformation forces an H2 payer at each changed scale

The interpolation inequality can be inverted when `d_k` is known:

\[
d_k
\le
C R_k^{-2/3}(\mathfrak E_{2,k}^{pair})^{1/3}.
\]

Therefore

\[
\boxed{
\mathfrak E_{2,k}^{pair}
\ge
c R_k^2 d_k^3.
}
\]

Thus an actual order-one shell-state change

\[
d_k\ge\delta>0
\]

forces

\[
\boxed{
\mathfrak E_{2,k}^{pair}
\ge c_\delta R_k^2.
}
\]

Equivalently the remote derivative frequency reaches the nearly absolute-scale microstructure regime identified by the earlier H hierarchy.

This is a genuine implication because it starts from actual state change, not from H2 size alone.

---

## 7. Infinite actual variation has two structurally different forms

If

\[
\mathfrak V_{form}=\infty,
\]

there are two cases.

### 7.1 Concentrated reformation

There exists `delta>0` such that

\[
\boxed{
d_k\ge\delta}
\]

for infinitely many `k`.

Each such event forces

\[
\mathfrak E_{2,k}^{pair}\gtrsim R_k^2.
\]

This is a fixed H1 reformation event accompanied by near-quadratic critical-H2 escalation. It is the correct lane for comparison with the existing quantified remote-H / shell-turnover event ledger.

The old remote-H theorem routes fixed dynamically active contraction/replacement to a fixed turnover event, but explicitly does not close the resulting T branch globally. Therefore this note does not claim that concentrated reformation is already contradictory.

### 7.2 Diffuse reformation

The remaining possibility is

\[
\boxed{
d_k\to0,
\qquad
\sum_k d_k=\infty.
}
\]

Here the shell state changes by arbitrarily small increments but accumulates infinite total H1 path length across scale.

This possibility is not captured by a fixed-jump turnover threshold.

Moreover

\[
\mathfrak E_{2,k}^{pair}\ge cR_k^2d_k^3
\]

does not by itself force a divergent ordinary palinstrophy budget. For example small `d_k` can make the cubic factor summable, and the physical/Leray shell weights further favor summability.

Thus diffuse reformation is a genuine endpoint subproblem and must not be silently routed to a fixed-event T theorem.

---

## 8. Fixed-action block extraction for diffuse variation

Although `d_k` may tend to zero, infinite total variation permits a purely metric block decomposition.

Fix any small `delta_form>0`.

Starting from a large index, choose consecutive disjoint blocks `B_n` minimally so that

\[
\boxed{
\sum_{k\in B_n}d_k
\ge\delta_{form}.
}
\]

Then infinitely many such blocks exist.

Hence diffuse reformation still produces infinitely many **fixed total H1 path-length blocks**.

However this is a state-space path-length statement, not yet a physical material-turnover statement. A long block may distribute the variation over many small increments, and the present estimates do not supply a uniform lower bound on viscous, pressure, or material action for the whole block.

The missing bridge is therefore precise:

\[
\boxed{
\text{fixed accumulated co-moving H1 shell variation}
\Longrightarrow
\text{fixed physical/critical action payer}.
}
\]

Establishing this bridge would merge diffuse reformation into the existing turnover ledger.

---

## 9. Correct DSD endpoint split

The logically exact split is now

\[
\boxed{
W1
\Longrightarrow
\begin{cases}
\mathfrak V_{form}<\infty:
&\text{persistent inherited critical memory},\\[1mm]
\mathfrak V_{form}=\infty:
&\text{actual structural reformation}.
\end{cases}
}
\]

The second line further splits as

\[
\boxed{
\text{actual reformation}
=
\text{concentrated fixed jumps}
\ \lor\
\text{diffuse infinite variation}.
}
\]

The H2 quantity is a payer/capacity descriptor attached to these events, not the definition of reformation itself.

---

## 10. What remains

The current proof attempt has two complementary endpoint mechanisms:

1. **Persistence:** finite shell-state variation forces simultaneous positive velocity/Bernoulli and vorticity critical currents.
2. **Reformation:** infinite shell-state variation requires endless structural change; fixed jumps force near-quadratic H2 microstructure, while diffuse variation requires a new path-length-to-physical-action bridge.

A successful DSD endpoint theorem should price both using one nonrepeatability functional.

No such finite global budget has yet been proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
