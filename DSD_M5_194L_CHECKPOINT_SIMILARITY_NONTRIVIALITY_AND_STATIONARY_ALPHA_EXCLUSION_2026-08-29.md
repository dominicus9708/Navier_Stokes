# DSD M5-194L — Checkpoint Similarity Nontriviality and Stationary Alpha Exclusion

Date: 2026-08-29

Parent: `DSD_M5_194K_BACKWARD_SIMILARITY_FLOW_AND_ALPHA_LIMIT_FORK_2026-08-29.md`

Status: **POSITIVE CHECKPOINT PASSAGE / NO-T CENTER NESTING AND FIRST-HITTING NORMALIZATION GIVE A UNIFORM POSITIVE SIMILARITY-VORTICITY WITNESS INSIDE ONE FIXED SIMILARITY BALL AT EVERY BACKWARD GENERATION / UNDER THE ALREADY USED STRONG LOCAL VORTICITY COMPACTNESS, A DIAGONAL PASSAGE PRODUCES CHECKPOINT PHASES `s_m -> -infinity` WITH NONVANISHING VORTICITY / ANY LOCALLY COMPACT CHECKPOINT ALPHA-LIMIT IS THEREFORE NONZERO / IF SUCH AN ALPHA-LIMIT WERE STATIONARY, IT WOULD RECONSTRUCT A NONZERO BACKWARD LERAY SELF-SIMILAR LOCAL-ENERGY SOLUTION, CONTRADICTING THE CLASSICAL SELF-SIMILAR LIOUVILLE THEORY / HENCE THE STATIONARY CHECKPOINT ALPHA-LIMIT BRANCH IS CLOSED ON THIS CORRIDOR / SURVIVORS MUST BE DYNAMIC (PERIODIC/APERIODIC) OR LOSE THE REQUIRED COMPACTNESS THROUGH A FORMED ESCAPE CHANNEL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Finite-stage checkpoint geometry

Use the first-hitting levels

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2}.
\]

At the earlier level `j-m`,

\[
W_{j-m}=q^{-m}W_j,
\qquad
r_{j-m}=q^{m/2}r_j.
\]

Let `X_*` be the limiting center from the no-turnover center-nesting lemma.

The fixed-center stage-`j` rescaling is

\[
U_j(y,\tau)
=r_j u(X_*+r_jy,t_j+r_j^2\tau),
\]

with vorticity

\[
\Omega_j(y,\tau)
=r_j^2\omega(X_*+r_jy,t_j+r_j^2\tau).
\]

Define the earlier first-hitting time in these variables by

\[
\tau_{j,m}
:=W_j(t_{j-m}-t_j)<0.
\]

The previously established stage-length bounds give constants `c_-,c_+>0` such that

\[
\boxed{
 c_-q^m
\le
|\tau_{j,m}|
\le
 c_+q^m.
}
\]

---

## 2. Exact vorticity normalization at the earlier first hit

At physical time `t_{j-m}`, the global vorticity supremum is exactly

\[
W(t_{j-m})=W_{j-m}.
\]

Choose a maximizer `X_{j-m}`. Then in stage-`j` variables

\[
\boxed{
|\Omega_j(y_{j,m},\tau_{j,m})|
=
\frac{W_{j-m}}{W_j}
=q^{-m},
}
\]

where

\[
y_{j,m}
:=
\frac{X_{j-m}-X_*}{r_j}.
\]

This is an equality at the finite-stage level, not only an upper Type-I estimate.

---

## 3. Center nesting becomes one fixed similarity ball

The no-T center-nesting result gives

\[
|X_*-X_k|
\le
C_Xr_k
\]

for every late first-hitting level `k`.

Hence

\[
|y_{j,m}|
\le
C_X\frac{r_{j-m}}{r_j}
=
C_Xq^{m/2}.
\]

Now convert the checkpoint to backward similarity coordinates. Let

\[
a_{j,m}:=|\tau_{j,m}|,
\qquad
\xi_{j,m}:=rac{y_{j,m}}{\sqrt{a_{j,m}}}.
\]

Since

\[
a_{j,m}\ge c_-q^m,
\]

we obtain

\[
\boxed{
|\xi_{j,m}|
\le
\frac{C_X}{\sqrt{c_-}}.
}
\]

The right side is independent of both `j` and `m`.

Thus every backward first-hitting maximizer lies in one fixed ball in similarity space:

\[
\boxed{
\xi_{j,m}\in B_{R_*},
\qquad
R_*:=C_X/\sqrt{c_-}.
}
\]

This closes the spatial-escape concern for the **tracked checkpoint maxima** themselves on the non-T branch.

---

## 4. Uniform positive similarity-vorticity witness

At a checkpoint, similarity vorticity is

\[
\Omega_{V,j}
=a_{j,m}\Omega_j.
\]

Therefore at the tracked maximizer

\[
|\Omega_{V,j}(\xi_{j,m},s_{j,m})|
=
a_{j,m}q^{-m}.
\]

Using

\[
c_-q^m
\le a_{j,m}\le c_+q^m,
\]

we obtain the two-sided bound

\[
\boxed{
 c_-
\le
|\Omega_{V,j}(\xi_{j,m},s_{j,m})|
\le
 c_+.
}
\]

Here

\[
s_{j,m}:=-\log a_{j,m}.
\]

Thus the finite-stage tower has a generation-independent positive similarity-vorticity witness.

This is stronger than the previously recorded global upper bound

\[
\|\Omega_V\|_\infty\le K_I.
\]

---

## 5. Diagonal passage to the ancient similarity orbit

Fix `m` first.

The quantities

\[
a_{j,m}q^{-m}
\]

lie in the compact interval

\[
[c_-,c_+],
\]

and the checkpoint positions `xi_{j,m}` lie in the fixed compact ball `B_{R_*}`.

Under the same strong local vorticity compactness already used to pass terminal first-hitting nontriviality, choose a subsequence so that

\[
\xi_{j,m}\to\xi_m,
\]

\[
\tau_{j,m}\to\tau_m,
\]

and the vorticity values converge locally.

Then

\[
\boxed{
|\Omega_V(\xi_m,s_m)|
\ge c_-,
}
\]

where

\[
s_m=-\log|\tau_m|.
\]

Because

\[
|\tau_m|\asymp q^m,
\]

we have

\[
\boxed{
s_m\to-\infty.}
\]

A diagonal extraction over `m=1,2,...` preserves the countable checkpoint family.

Therefore the similarity orbit contains a backward sequence with

\[
\boxed{
\xi_m\in B_{R_*},
\qquad
|\Omega_V(\xi_m,s_m)|\ge c_*>0,
\qquad
s_m\to-\infty,
}
\]

where one may take `c_*=c_-` at the ideal strong-passage level.

---

## 6. Nonzero checkpoint alpha-limits

Translate similarity time by the checkpoint phases:

\[
V_m^{tr}(\xi,\sigma)
:=V(\xi,s_m+\sigma).
\]

Suppose the local compactness corridor yields, after a subsequence,

\[
V_m^{tr}\to V_*
\]

strongly enough for vorticity to pass on a fixed neighborhood of `B_{R_*}` at `sigma=0`.

Since `xi_m` remains in the fixed compact ball, choose a further subsequence

\[
\xi_m\to\xi_*.
\]

Then

\[
\boxed{
|\Omega_{V_*}(\xi_*,0)|
\ge c_*>0.
}
\]

Hence

\[
\boxed{V_*\not\equiv0.}
\]

So **any compact alpha-limit extracted along the tracked checkpoint phases is nontrivial.**

---

## 7. Stationary checkpoint alpha-limit is impossible

Assume a checkpoint alpha-limit is stationary:

\[
\partial_\sigma V_*=0.
\]

Then `V_*` solves the stationary backward Leray profile equation

\[
-\Delta V_*
+\frac12V_*
+\frac12(\xi\cdot\nabla)V_*
+(V_*\cdot\nabla)V_*
+\nabla Q_*=0.
\]

Reconstruct the physical backward self-similar field

\[
u_*(x,t)
=
\frac1{\sqrt{-t}}
V_*\!\left(\frac{x}{\sqrt{-t}}\right),
\qquad t<0.
\]

The checkpoint alpha-limit originates from the repository's local suitable/local-energy compactness corridor. If the local energy inequality and the required pressure class pass through this final extraction -- the standard intended compactness passage -- then `u_*` lies in the class covered by the classical backward self-similar local-energy Liouville result of Tai-Peng Tsai.

That theorem forces

\[
V_*\equiv0.
\]

But checkpoint nontriviality gives

\[
|\Omega_{V_*}(\xi_*,0)|\ge c_*>0.
\]

Contradiction.

Therefore, on the local-energy alpha-compactness corridor,

\[
\boxed{
\text{nonzero stationary checkpoint alpha-limit is impossible.}
}
\]

Since checkpoint alpha-limits are nonzero, the stationary class is excluded altogether.

---

## 8. What this does and does not prove

This is a meaningful rigidity gain, but it is not yet global regularity.

The conclusion is not

\[
V_s\to0.
\]

It is the opposite structural statement:

\[
\boxed{
\text{if a compact checkpoint alpha-limit exists, it cannot be stationary.}
}
\]

Thus a surviving first-hitting singular branch must do at least one of the following:

1. approach a genuinely time-dependent periodic/DSS alpha-limit;
2. approach a genuinely aperiodic alpha-limit;
3. fail the local alpha-compactness assumptions through an explicit formed channel;
4. lose the local-energy/pressure property needed to invoke the stationary Liouville theorem -- which must itself be identified as a concrete compactness failure rather than silently assumed.

---

## 9. Relation to M5-194H

M5-194H studied stationary physical `(-1)`-homogeneous Navier--Stokes tails and invoked the Šverák/Landau classification.

M5-194L shows that the more natural second limit of the actual Type-I ancient survivor is a Leray similarity alpha-limit.

For checkpoint alpha-limits, the stationary Leray branch is already strongly constrained by self-similar Liouville theory before one needs to force the profile into the physically stationary Landau class.

Thus the K2 route should no longer prioritize the Landau classification.

The priority becomes **dynamic similarity recurrence**.

---

## 10. DSD verdict

### PROVED ON THE NO-T / STRONG-LOCAL-COMPACTNESS CORRIDOR

At every finite-stage backward first-hitting checkpoint,

\[
\boxed{
\xi_{j,m}\in B_{R_*}
}
\]

and

\[
\boxed{
 c_-
\le
|\Omega_{V,j}(\xi_{j,m},s_{j,m})|
\le c_+.
}
\]

After the established style of diagonal strong-vorticity passage, this yields a nonvanishing backward checkpoint sequence in the similarity orbit.

### CONDITIONALLY CLOSED

Any checkpoint alpha-limit that

- exists locally with strong vorticity passage;
- retains the suitable/local-energy and pressure class needed for Tsai's theorem;
- and is stationary in similarity time

is impossible.

### REMAINS OPEN

- periodic/DSS checkpoint alpha-limits without global `L3` tightness;
- aperiodic recurrent alpha-limits;
- quantitative lower bounds on the similarity-time defect `V_s`;
- global critical tail compatibility with local recurrent core dynamics;
- generic critical-drift backward uniqueness if the dynamic route survives.

---

## 11. Next audit target

The highest-value remaining dynamic branch is periodicity.

The first-hitting scale ratio already determines

\[
\lambda=\sqrt q,
\]

corresponding to a similarity-time shift

\[
S=\log q=2\log\lambda.
\]

The next audit should compare the checkpoint-to-checkpoint normalized spacetime blocks and define an explicit recurrence defect

\[
\boxed{
\mathfrak R_m(R,T)
:=
\|V(\cdot,s_{m+1}+\cdot)-V(\cdot,s_m+\cdot)\|_{X(B_R\times[-T,T])}.
}
\]

Then separate:

\[
\boxed{
\mathfrak R_m\to0
\Rightarrow
\text{periodic/DSS alpha-limit candidate},
}
\]

from

\[
\boxed{
\limsup\mathfrak R_m>0
\Rightarrow
\text{formed aperiodic scaling-defect witness}.
}
\]

This converts the remaining vague word `dynamic` into an auditable finite-channel dichotomy.
