# DSD M5-194K — Backward Similarity Flow and Alpha-Limit Fork

Date: 2026-08-29

Parent: `DSD_M5_194J_TIME_HOMOGENEITY_AND_PARABOLIC_SCALING_DEFECT_EQUATIONS_2026-08-29.md`

Status: **POSITIVE RENORMALIZATION / THE CONTINUOUS BACKWARD TYPE-I VORTICITY DECAY BECOMES A UNIFORM VORTICITY BOUND FOR AN AUTONOMOUS LERAY SIMILARITY FLOW / THE CENTERED CRITICAL MORREY ENERGY IS EXACTLY INVARIANT UNDER THIS TRANSFORMATION / THE PARABOLIC SCALING DEFECT IS EXACTLY PROPORTIONAL TO SIMILARITY-TIME MOTION `partial_s V` / THEREFORE THE REMAINING K2 RIGIDITY QUESTION IS AN ALPHA-LIMIT DYNAMICS PROBLEM / A STATIONARY ALPHA-LIMIT IS IN A CLASS WHERE BACKWARD SELF-SIMILAR LIOUVILLE RESULTS CAN APPLY, WHILE PERIODIC/DSS OR APERIODIC LIMITS REQUIRE ADDITIONAL GLOBAL TAIL CONTROL / CURRENT FIRST-HITTING RECURRENCE DOES NOT YET FORCE STATIONARITY OR PERIODICITY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Similarity variables

For the ancient solution `U(y,tau)` with `tau<0`, define

\[
a:=-\tau>0,
\qquad
s:=-\log a=-\log(-\tau),
\]

\[
\xi:=\frac{y}{\sqrt a},
\]

and

\[
\boxed{
V(\xi,s)
:=\sqrt a\,U(\sqrt a\,\xi,-a).
}
\]

Define similarly

\[
\boxed{
Q(\xi,s)
:=a\,P(\sqrt a\,\xi,-a).
}
\]

The limits correspond to

\[
\tau\to-\infty
\Longleftrightarrow
s\to-\infty,
\]

and

\[
\tau\uparrow0
\Longleftrightarrow
s\to+\infty.
\]

Thus the entire ancient interval becomes the full similarity-time line

\[
s\in\mathbb R.
\]

---

## 2. Autonomous Leray evolution

A direct change of variables gives

\[
\boxed{
\partial_s V
-\Delta_\xi V
+\frac12V
+\frac12(\xi\cdot\nabla_\xi)V
+(V\cdot\nabla_\xi)V
+\nabla_\xi Q
=0,
}
\]

with

\[
\boxed{
\nabla_\xi\cdot V=0.
}
\]

This is autonomous in `s`.

A stationary point

\[
\partial_sV=0
\]

satisfies the backward Leray profile equation

\[
\boxed{
-\Delta V
+\frac12V
+\frac12(\xi\cdot\nabla)V
+(V\cdot\nabla)V
+\nabla Q=0.
}
\]

Therefore the correct second-limit rigidity target is not the stationary physical Navier--Stokes equation used in M5-194H, but first the **stationary Leray equation**.

---

## 3. Exact relation to the parabolic scaling defect

Recall from M5-194J

\[
\mathcal Z[U]
=
U+y\cdot\nabla U+2\tau\partial_\tau U.
\]

Differentiate `V` with respect to `s` at fixed `xi`. Since

\[
\frac{da}{ds}=-a,
\qquad
\frac{d\tau}{ds}=a,
\qquad
\frac{dy}{ds}=-\frac12y,
\]

we obtain

\[
\partial_sV
=
\sqrt a
\left(
-\frac12U
-\frac12y\cdot\nabla U
+a\partial_\tau U
\right).
\]

Using `a=-tau`,

\[
\boxed{
\partial_sV
=-\frac12\sqrt{-\tau}\,\mathcal Z[U].
}
\]

Equivalently,

\[
\boxed{
\mathcal Z[U]
=-2(-\tau)^{-1/2}\partial_sV.
}
\]

Thus

\[
\boxed{
\text{scaling-defect vanishing}
\Longleftrightarrow
\text{stationarity in similarity time}.
}
\]

This converts the abstract defect gate into a dynamical-systems question.

---

## 4. Vorticity transformation

Let

\[
\Omega_U=\nabla_y\times U,
\qquad
\Omega_V=\nabla_\xi\times V.
\]

Because

\[
\nabla_\xi=\sqrt a\,\nabla_y,
\]

we have

\[
\boxed{
\Omega_V(\xi,s)
=a\,\Omega_U(\sqrt a\,\xi,-a).
}
\]

The established backward Type-I bound is

\[
\|\Omega_U(\tau)\|_\infty
\le
\min\left\{1,\frac{K_I}{|\tau|}\right\}.
\]

Therefore

\[
\boxed{
\|\Omega_V(s)\|_\infty
\le
\min\{e^{-s},K_I\}
\le K_I.
}
\]

In particular,

\[
\boxed{
\sup_{s\in\mathbb R}
\|\Omega_V(s)\|_\infty
\le K_I.
}
\]

This is an exact positive gain: the decaying ancient vorticity becomes a uniformly bounded similarity-vorticity orbit.

At the opposite end,

\[
s\to+\infty,
\]

we have

\[
\boxed{
\|\Omega_V(s)\|_\infty
\le e^{-s}\to0.
}
\]

The difficult dynamics are therefore entirely in the alpha-limit direction

\[
s\to-\infty.
\]

---

## 5. Centered Morrey energy is exactly invariant

Assume the ancient Morrey corridor provides

\[
\sup_{R>0}
R^{-1}
\int_{B_R}|U(y,\tau)|^2dy
\le M_*
\]

in the centered fixed-frame sense recorded by the compactness branch.

For `V`,

\[
\int_{B_\rho}|V(\xi,s)|^2d\xi
=
a^{-1/2}
\int_{B_{\sqrt a\rho}}|U(y,\tau)|^2dy.
\]

Hence

\[
\boxed{
\rho^{-1}
\int_{B_\rho}|V|^2d\xi
=
(\sqrt a\rho)^{-1}
\int_{B_{\sqrt a\rho}}|U|^2dy.
}
\]

Therefore

\[
\boxed{
\sup_{s\in\mathbb R}
\sup_{\rho>0}
\rho^{-1}
\int_{B_\rho}|V(\xi,s)|^2d\xi
\le M_*.
}
\]

The critical centered Morrey channel does not deteriorate under backward similarity renormalization.

---

## 6. Similarity-time translate compactness

Because the Leray equation is autonomous, consider any sequence

\[
s_n\to-\infty
\]

and define translated similarity flows

\[
V_n(\xi,\sigma)
:=V(\xi,s_n+\sigma).
\]

The uniform vorticity bound and scale-invariant local Morrey/local-energy bounds provide the same type of fixed-cylinder compactness inputs already used in the ancient extraction, now on bounded `sigma` intervals.

Thus, on the established no-H/Morrey compactness corridor, it is natural to seek a subsequential alpha-limit

\[
V_n\to V_*
\]

locally on

\[
\mathbb R^3\times\mathbb R.
\]

The limiting object solves the same autonomous Leray evolution for all similarity times `sigma`.

This step is a **compactness target** rather than a claim that every alpha-limit is already known to exist with all global tail properties. Local extraction is the part supported by the inherited bounds; global tightness remains a separate channel.

---

## 7. Three alpha-limit classes

The K2 rigidity route now has a clean dynamical split.

### Class S — stationary alpha-limit

If

\[
\partial_\sigma V_*=0,
\]

then `V_*` is a backward Leray self-similar profile.

External rigidity is strong here.

- Nečas--Růžička--Šverák exclude nonzero `L^3` Leray profiles.
- Tsai excludes backward self-similar weak solutions satisfying the required local energy estimates in a cylinder.
- Later work excludes further Morrey/Lorentz profile classes.

Because the present route is built from suitable/local-energy compactness, a stationary alpha-limit is therefore a promising **closed external-Liouville branch**, provided the local energy inequality and pressure class pass through the alpha-limit/reconstruction exactly as required.

This prerequisite should be checked explicitly rather than assumed.

### Class P — periodic similarity-time alpha-limit

If

\[
V_*(\sigma+S)=V_*(\sigma)
\]

for some `S>0`, the reconstructed physical solution is backward discretely self-similar.

There are nonexistence results for periodic/asymptotically DSS profiles under global integrability hypotheses such as `L^3`.

However, the repository already proved that a nontrivial ancient survivor must allow a global critical `L^3` tail escape. Therefore those theorems cannot yet close the generic periodic branch without an additional global-tail argument.

### Class A — aperiodic dynamic alpha-limit

If the alpha-limit is neither stationary nor periodic, then a genuine similarity-time defect persists:

\[
\boxed{
\partial_\sigma V_*\not\equiv0.
}
\]

This is the fully dynamic critical endpoint. Stationary Šverák/Leray classifications do not apply.

---

## 8. First-hitting checkpoints under similarity scaling

The original first-hitting hierarchy contains backward times with

\[
|\tau_m|\asymp q^m
\]

and vorticity scale

\[
\|\Omega_U(\tau_m)\|_\infty
\sim q^{-m}
\]

at the prelimit tower level.

After similarity normalization,

\[
\|\Omega_V(s_m)\|_\infty
=
|\tau_m|\,
\|\Omega_U(\tau_m)\|_\infty
\sim O(1).
\]

Likewise maximizer distances of order

\[
O(\sqrt{|\tau_m|})
\]

become order-one distances in `xi`.

Therefore the first-hitting construction is naturally compatible with a nontrivial alpha-limit along checkpoint phases.

However, the earlier ancient-limit note conservatively recorded only an upper bound after diagonal passage. A uniform **lower nontriviality passage** for `Omega_V` along `m -> infinity` must be proved before one may declare every alpha-limit nonzero.

This is now an explicit compactness sublemma rather than an implicit assumption.

---

## 9. No automatic Lyapunov closure from the naive weighted energy

The linear part of the Leray equation has Ornstein--Uhlenbeck structure, suggesting Gaussian weighted energies.

But the nonlinear transport term is not automatically skew with respect to the Gaussian measure because

\[
\nabla e^{-|\xi|^2/4}
=-\frac12\xi e^{-|\xi|^2/4}.
\]

Thus

\[
\int
(V\cdot\nabla)V\cdot V
\,e^{-|\xi|^2/4}d\xi
\]

does not vanish merely from `div V=0`.

The pressure term likewise interacts with the nonconstant weight.

Therefore one cannot currently assert a monotone Gaussian energy whose dissipation directly forces

\[
\partial_sV\to0.
\]

This closes another tempting but unproved shortcut.

---

## 10. DSD verdict

### POSITIVE

The Type-I ancient survivor admits the exact similarity reformulation

\[
\boxed{
V_s
-\Delta V
+\frac12V
+\frac12\xi\cdot\nabla V
+V\cdot\nabla V
+\nabla Q=0,
}
\]

with

\[
\boxed{
\|\Omega_V(s)\|_\infty\le K_I
}
\]

and invariant centered critical Morrey energy.

Also,

\[
\boxed{
V_s=-\frac12\sqrt{-\tau}\,\mathcal Z[U].
}
\]

Hence similarity-time motion is exactly the formed scaling defect.

### CLOSED AS SHORTCUTS

- Type-I decay does not itself imply `V_s -> 0`;
- first-hitting snapshot recurrence does not imply stationary or periodic similarity flow;
- a Gaussian weight does not make the nonlinear Leray flow obviously gradient-like.

### SURVIVING GATE

The K2 route is reduced to

\[
\boxed{
\text{similarity alpha-limit compactness}
+\text{checkpoint nontriviality}
+\text{classification of S/P/A dynamics}.
}
\]

---

## 11. Next calculation

The next highest-value sublemma is the **checkpoint nontriviality passage**.

One should return to the finite-stage first-hitting tower and prove, in similarity coordinates, that there exist checkpoint phases `s_m -> -infinity` and points `xi_m` in one fixed ball such that

\[
\boxed{
|\Omega_V(\xi_m,s_m)|\ge c_*>0
}
\]

with `c_*` independent of `m`.

If this succeeds, every locally convergent alpha-subsequence chosen from those checkpoints has a nonzero limit.

Then the stationary alpha-limit branch would become especially strong: a nonzero stationary local-energy Leray profile would contradict the classical self-similar Liouville theory, forcing any surviving checkpoint alpha-limit to remain genuinely time-dependent or to lose compactness through an explicitly formed global-tail/center channel.
