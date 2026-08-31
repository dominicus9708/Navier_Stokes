# DSD M5-370 — Euler Gradient-Type-II Escape = Similarity Derivative-H Exactly

Date: 2026-08-31

Status: **THE ONLY NON-TURNOVER ESCAPE LEFT BY M5-369 IS NOT A NEW EULER ENDPOINT / `(-tau)||grad v_E||_infty` IS EXACTLY `||grad V||_infty` IN THE `alpha=3/2` SIMILARITY VARIABLES / THEREFORE THE SATURATED AFFINE/ATOM BRANCH COLLAPSES BACK INTO THE EXISTING DERIVATIVE-H OR TURNOVER TREE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-369 proved, for the saturated energy-bearing affine-shield lineage,

\[
 \text{affine shield}
 \Longrightarrow
 T_{\rm center/compactness}
 \lor
 H_{\nabla,E}^{\rm TypeII}
 \lor
 \text{contradiction by the Chae--Wolf Euler atom theorem}.
\]

This note identifies the derivative-Type-II branch in the similarity variables.

## 2. `alpha=3/2` similarity transform

For the Euler endpoint, let

\[
 s=-\log(-\tau),
 \qquad
 y=\frac{x}{(-\tau)^{2/5}},
\]

and

\[
 V(y,s)=(-\tau)^{3/5}v_E(x,\tau).
\]

Since

\[
 x=(-\tau)^{2/5}y,
\]

we have

\[
 \nabla_y
 =(-\tau)^{2/5}\nabla_x.
\]

Therefore

\[
 \nabla_yV
 =(-\tau)^{3/5}(-\tau)^{2/5}\nabla_xv_E.
\]

Hence the exact identity

\[
 \boxed{
 \nabla_yV(y,s)
 =(-\tau)\nabla_xv_E(x,\tau).
 }
\]

## 3. Type-I / derivative-tightness equivalence

Taking `L∞` norms,

\[
 \boxed{
 \|\nabla V(s)\|_\infty
 =(-\tau)\|\nabla v_E(\tau)\|_\infty.
 }
\]

Thus

\[
 \boxed{
 \sup_{\tau<0}(-\tau)\|\nabla v_E(\tau)\|_\infty<\infty
 \iff
 \sup_s\|\nabla V(s)\|_\infty<\infty.
 }
\]

And its complement is

\[
 \boxed{
 \sup_{\tau<0}(-\tau)\|\nabla v_E(\tau)\|_\infty=\infty
 \iff
 \sup_s\|\nabla V(s)\|_\infty=\infty.
 }
\]

## 4. Interpret the Chae--Wolf theorem in similarity coordinates

The Euler Type-I gradient hypothesis used by Chae--Wolf is exactly a uniform profile-gradient bound.

Therefore M5-369 can be rewritten as

\[
 \boxed{
 \text{saturated descendant energy atom}
 \Longrightarrow
 T
 \lor
 H_{\nabla,\rm sim}
 \lor
 \text{contradiction}.
 }
\]

No additional Euler-specific terminal leaf is created.

## 5. Relation to M5-366

M5-366 used the same no-H bound

\[
 \sup_s\|\nabla V(s)\|_\infty<\infty
\]

to close exact DSS by two routes:

1. Euler Type-I gradient plus Chae--Wolf 2017;
2. finite `L2` + bounded gradient -> bounded/sublinear profile, then Chae--Wolf 2023.

M5-369--370 now show that the same bound closes the **whole saturated energy-atom lineage**, regardless of whether the similarity orbit is periodic.

Thus the atom theorem strictly dominates the DSS classification for this energy-bearing branch.

## 6. Master reduction for the saturated affine branch

The chain is now

\[
 \boxed{
 \begin{aligned}
 \text{saturated affine/dual-hyperbolic lineage}
 &\to
 \text{Euler terminal energy atom}\\
 &\to
 H_{\nabla,\rm sim}
 \lor
 T_{\rm center/compactness}.
 \end{aligned}
 }
\]

On the no-H/no-T lane the branch is impossible.

## 7. What remains of the Euler similarity analysis

The DSS/RDSS/aperiodic similarity audits M5-365--368 remain relevant for **non-atomic or nonsaturated Euler endpoints**.

They are no longer needed to close the saturated affine shield.

This prevents the proof tree from over-counting endpoint branches.

## 8. Formation-axiom consequence

The previously separate labels

- energy-bearing affine shield;
- Euler point-energy atom;
- Euler gradient-Type-II endpoint;

are not three independent structures.

They form one chain whose surviving endpoint is precisely the already existing derivative-H state.

Thus the formation reduction is

\[
 \boxed{
 A_{\rm energy}
 \subset
 H_{\nabla}\lor T.
 }
\]

## 9. Firewall

This does not eliminate `H_nabla`.

A hypothetical singular solution is allowed to have unbounded similarity-profile gradient. The result is a proof-tree reduction, not a regularity theorem.

Do not confuse

\[
 H_{\nabla,\rm sim}
\]

with a contradiction unless an additional derivative/frequency budget is proved.

## 10. Audit verdict

### EXACTLY DERIVED

\[
 \boxed{
 \|\nabla V(s)\|_\infty
 =(-\tau)\|\nabla v_E(\tau)\|_\infty.
 }
\]

### CONSEQUENCE

- the Chae--Wolf Euler Type-I atom theorem is exactly the no-similarity-gradient-H gate;
- saturated affine/atom lineage introduces no new terminal endpoint beyond H/T.

### OPEN

- elimination/pricing of similarity derivative-H;
- material/spatial turnover T;
- nonsaturated/microstructure branches already routed to higher-derivative H;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
