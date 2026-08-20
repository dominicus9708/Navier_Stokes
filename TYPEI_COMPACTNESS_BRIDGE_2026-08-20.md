# First-Hitting Type-I Compactness Bridge — 2026-08-20

Overall status: **CONDITIONAL BRIDGE DRAFT — NOT A PROOF OF GLOBAL REGULARITY.**

This note makes precise the proposed bridge from an eventual non-`H/T` first-hitting regime to a restricted Type-I ancient solution. It deliberately separates proved ingredients from still-unclosed compactness/gauge sublemmas.

---

## 1. First-hitting tower

Let

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\qquad
W(t_j)=W_j.
\]

Then

\[
\boxed{
r_{j-m}=q^{m/2}r_j.}
\]

Thus, after rescaling stage `j` to unit natural radius, the natural radius of stage `j-m` appears at radius

\[
R_m=q^{m/2}.
\]

If the non-`H/T` regime satisfies the rate result

\[
L_-\le L_k\le L_+
\]

for all sufficiently late stages, then

\[
\Delta t_k\asymp W_k^{-1}=r_k^2.
\]

Consequently the physical time between `t_{j-m}` and `t_j` is

\[
\sum_{k=j-m}^{j-1}\Delta t_k
\asymp
r_{j-m}^2.
\]

Therefore the first-hitting sequence is naturally organized as nested parabolic scales

\[
\boxed{
Q_{r_{j-m}}\quad\longleftrightarrow\quad
Q_{R_m}
\text{ in the stage-j variables.}
}
\]

This is exactly the geometry needed for an ancient blow-up tower.

---

## 2. Rescaled fields

At stage `j`, with tracked center `X_j`, define

\[
U_j(y,\tau)
=r_j u(X_j+r_jy,t_j+r_j^2\tau),
\]

\[
P_j(y,\tau)
=r_j^2p(X_j+r_jy,t_j+r_j^2\tau),
\]

and

\[
\Omega_j=\nabla_y\times U_j.
\]

At the first-hitting point,

\[
\boxed{\|\Omega_j(0)\|_\infty=1.}
\]

After recentering at an actual vorticity maximum one may choose the spatial origin so that

\[
|\Omega_j(0,0)|=1.
\]

The backward lifetime of the rescaled solution is

\[
t_j/r_j^2=t_jW_j\to\infty,
\]

so every fixed backward interval `[-T,0]` is eventually contained in the rescaled domain.

---

## 3. Scale-uniform Type-I quantities required

For a parabolic cylinder `Q(R)=B_R x (-R^2,0)`, define the scale-invariant local quantities

\[
A_j(R)=R^{-1}\operatorname*{ess\,sup}_{\tau\in(-R^2,0)}
\int_{B_R}|U_j|^2dy,
\]

\[
C_j(R)=R^{-2}\int_{Q(R)}|U_j|^3dyd\tau,
\]

\[
D_j(R)=R^{-2}\int_{Q(R)}|P_j-[P_j]_{B_R}|^{3/2}dyd\tau,
\]

\[
E_j(R)=R^{-1}\int_{Q(R)}|\nabla U_j|^2dyd\tau.
\]

The desired compactness hypothesis is a uniform bound

\[
\boxed{
\sup_j\sup_{R\le R_j^{max}}
[A_j(R)+C_j(R)+D_j(R)+E_j(R)]<\infty,
}
\]

where `R_j^{max}->infinity` as `j->infinity`.

This is the exact form needed to pass from a scale tower to a global-in-space ancient limit.

---

## 4. How the current route is meant to supply A,C,D,E

### A: local velocity variance / energy

The moving weighted-mean construction supplies a scale-invariant local relative-velocity variance. To convert it into `A_j`, one must fix the drift gauge consistently across scales.

### E: local dissipation

Inside a bounded normalized core, `||Omega||_infty=1` controls the antisymmetric velocity gradient. Avoidance of the derivative branch `H`, together with the local/far strain decomposition, is intended to give a uniform local strain/dissipation bound.

### C: cubic velocity

Once `A_j` and `E_j` are uniformly bounded, the standard local interpolation used in suitable-solution theory controls the cubic velocity quantity `C_j`.

### D: pressure

The existing pressure decomposition gives a near-pressure term controlled by local velocity and an affine-free remote term with dyadic decay. The passive-global-halo reduction is intended to prevent far pressure from producing an uncontrolled local oscillation. A consistent affine-pressure gauge is still required.

These implications are plausible within the current route but have **not yet been packaged into a complete proof with constants uniform over the entire tower**.

---

## 5. Center nesting and the role of T

A true ancient tower requires the scale centers to remain nested. The appropriate no-turnover condition should imply

\[
\boxed{
|X_{j+1}-X_j|\lesssim r_j.
}
\]

Then

\[
|X_k-X_j|
\lesssim
\sum_{n=k}^{j-1}r_n
\lesssim r_k,
\]

so all late cores converge to one physical singular point and remain inside comparable parabolic cylinders.

Without this `O(r_j)` nesting, the first-hitting maximum may jump between cores; that is precisely the bounded-radius/material-turnover channel `T` rather than the compact `P_V` branch.

A weaker convergence of centers follows already from finite kinetic energy, but it is not strong enough for natural-scale nesting; therefore the `O(r_j)` statement must be tied explicitly to the definition of avoiding `T`.

---

## 6. Compactness and nontriviality

Assuming the scale-uniform `A/C/D/E` bounds, suitable-solution compactness yields (after a diagonal subsequence) a suitable ancient limit on every finite parabolic cylinder.

To preserve nontriviality, weak compactness alone is insufficient to pass the pointwise normalization

\[
|\Omega_j(0,0)|=1.
\]

Avoidance of `H` is therefore also used as a higher-regularity compactness input so that, on compact subsets,

\[
\Omega_j\to\Omega_\infty
\]

strongly enough to obtain

\[
\boxed{|\Omega_\infty(0,0)|=1.}
\]

Hence the limit is nonzero.

---

## 7. Drift/pressure gauge gap

The moving weighted-mean frame is a time-dependent translation. Such a translation changes the pressure by an affine spatial term associated with the frame acceleration. Vorticity and local relative dynamics are unaffected, but the standard Type-I pressure quantity is not automatically invariant under arbitrary affine pressure additions.

Therefore one remaining technical sublemma is:

\[
\boxed{
\text{choose a coherent inertial/accelerated gauge so that the rescaled pressure oscillation }D_j
\text{ is uniformly controlled and the ancient limit is mild rather than parasitic.}
}
\]

This gap should not be hidden inside the word `recenter`.

---

## 8. Conditional compactness statement

If all four conditions hold:

1. eventual `L_- <= L_j <= L_+`;
2. no-`T` natural-scale center nesting;
3. no-`H` scale-uniform local derivative compactness;
4. uniform pressure gauge / `A,C,D,E` bounds over the expanding first-hitting tower;

then the first-hitting rescalings admit a nontrivial ancient limit.

The Type-I theory of Albritton--Barker (arXiv:1811.00502) identifies local Type-I singularities with nontrivial bounded mild ancient solutions satisfying the corresponding Type-I scale bounds. The remaining task is to prove that the DSD first-hitting tower satisfies those hypotheses, not merely the vorticity-rate relation `W_j(T-t_j)~1`.

---

## 9. Why this bridge matters

If established, the global endgame becomes

\[
\boxed{
\text{finite-time singularity}
\Longrightarrow
(H\lor T)\text{ infinitely often}
\quad\lor\quad
\text{restricted Type-I ancient }P_V\text{ solution}.
}
\]

The second branch would carry additional constraints already derived in this repository:

- first-hitting vorticity cap;
- bounded-radius recurrence;
- `P_V` projective action;
- exclusion of projection-invisible exact max-mid states;
- max-mid defect / middle-axis locking alternatives;
- passive far critical halo.

The aim is therefore **not** to solve the unrestricted bounded-ancient-solution conjecture, but to prove a Liouville theorem for this much narrower ancient class.

Status: **ANCIENT-TOWER GEOMETRY IDENTIFIED. COMPACTNESS BRIDGE REMAINS CONDITIONAL ON NATURAL-SCALE CENTER NESTING, UNIFORM LOCAL TYPE-I BOUNDS, PRESSURE GAUGE CONTROL, AND STRONG NONTRIVIALITY PASSAGE.**