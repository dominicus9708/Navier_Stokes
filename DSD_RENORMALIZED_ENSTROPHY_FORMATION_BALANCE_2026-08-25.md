# DSD renormalized enstrophy formation balance

Date: 2026-08-25

Status: **EXACT FIRST-HITTING BALANCE PROVED / POSITIVE CESARO NET-FORMATION FLOOR PROVED / POSITIVE-DENSITY ACTIVE STAGES PROVED / STATE-DRIFT NOT NEEDED AS A PRIMITIVE SURVIVOR / STRETCHING BUDGET CLOSURE STILL OPEN / GLOBAL REGULARITY UNPROVED.**

This note removes an unnecessary detour through renormalization-state recurrence. The first-hitting scale change itself gives an exact finite balance for the normalized enstrophy channel.

## 1. Normalized enstrophy at first hitting

Define

\[
\boxed{
Z_j:=\|\Omega_j(\cdot,0)\|_2^2
=\frac{r_j}{\nu^2}\|\omega(t_j)\|_2^2.
}
\]

On the bounded-Z branch,

\[
\boxed{z_a\le Z_j\le Z_*}
\]

for all sufficiently late `j`, where the fixed positive lower floor `z_a` comes from the analytic occupied ball.

Let

\[
\lambda:=\frac{r_j}{r_{j+1}}=\sqrt q>1.
\]

Then

\[
\|\omega(t_j)\|_2^2
=\frac{\nu^2}{r_j}Z_j,
\qquad
\|\omega(t_{j+1})\|_2^2
=\frac{\nu^2}{r_j}\lambda Z_{j+1}.
\]

## 2. Exact finite net-formation charge

The whole-space enstrophy identity gives

\[
\frac12\left[
\|\omega(t_{j+1})\|_2^2-
\|\omega(t_j)\|_2^2
\right]
=
\int_{t_j}^{t_{j+1}}
\left[
\int\omega^TS\omega\,dx
-\nu\|\nabla\omega\|_2^2
\right]dt.
\]

Define the scale-normalized finite net-formation charge

\[
\boxed{
N_j
:=
\frac{r_j}{\nu^2}
\int_{t_j}^{t_{j+1}}
\left[
\int\omega^TS\omega\,dx
-\nu\|\nabla\omega\|_2^2
\right]dt.
}
\]

Then exactly

\[
\boxed{
N_j=\frac12\left(\lambda Z_{j+1}-Z_j\right).
}
\]

Status: **PROVED EXACTLY.**

No compactness, recurrence, material genealogy, derivative ladder, or infinite-tail object is used.

## 3. Telescoping over finitely many formed stages

For finite integers `J<N`, sum the exact balance:

\[
\begin{aligned}
\sum_{j=J}^{N-1}N_j
&=\frac12\sum_{j=J}^{N-1}(\lambda Z_{j+1}-Z_j)\\
&=\frac12\left[
(\lambda-1)\sum_{j=J+1}^{N-1}Z_j
+\lambda Z_N-Z_J
\right].
\end{aligned}
\]

Using

\[
z_a\le Z_j\le Z_*,
\]

we get the finite lower bound

\[
\boxed{
\sum_{j=J}^{N-1}N_j
\ge
\frac{\lambda-1}{2}z_a(N-J-1)
-\frac{Z_*}{2}.
}
\]

Therefore

\[
\boxed{
\liminf_{N-J\to\infty}
\frac1{N-J}
\sum_{j=J}^{N-1}N_j
\ge
\bar N_0:=\frac{\lambda-1}{2}z_a>0.
}
\]

Thus the first-hitting tower has a strictly positive **Cesaro net-formation floor** in the normalized enstrophy channel.

Status: **PROVED.**

## 4. Positive-density active stages

The same bounded-Z ceiling gives a uniform upper bound

\[
N_j
\le\frac\lambda2 Z_*
=:N_{\max}.
\]

Choose the threshold

\[
\eta:=\frac{\bar N_0}{2}>0.
\]

Let `p_{J,N}` be the fraction of indices `j in {J,...,N-1}` for which

\[
N_j\ge\eta.
\]

Since every inactive stage satisfies `N_j<eta` and every active stage satisfies `N_j<=N_max`,

\[
\frac1{N-J}\sum N_j
\le
p_{J,N}N_{\max}
+(1-p_{J,N})\eta.
\]

The Cesaro lower floor therefore forces

\[
\boxed{
\liminf p_{J,N}
\ge
p_0
:=
\frac{\bar N_0-\eta}{N_{\max}-\eta}
>0.
}
\]

Equivalently, a positive asymptotic fraction of late first-hitting stages obey

\[
\boxed{
N_j\ge\eta>0.
}
\]

On every such stage,

\[
\boxed{
\int_{t_j}^{t_{j+1}}
\left[
\int\omega^TS\omega\,dx
-\nu\|\nabla\omega\|_2^2
\right]dt
\ge
\eta\frac{\nu^2}{r_j}.
}
\]

This is a positive lower bound for the **net** enstrophy formation after viscous destruction has already been subtracted.

Status: **PROVED.**

## 5. Consequence: state drift is not the primitive obstruction

A renormalized shape may recur, drift, or move through a complicated compact cluster set. None of those possibilities changes the exact scalar balance above.

Therefore the previously introduced `Renormalization-State Variation Gate (RSVG)` is not required as the primitive next gate on the bounded-Z branch.

The DSD finite-channel hierarchy is sharper:

\[
\boxed{
\text{first-hitting scale transition}
\Longrightarrow
\text{positive-density net enstrophy formation stages}.
}
\]

The state-space geometry may still be useful to estimate the source, but it is not necessary to prove that a source channel is repeatedly active.

Status: **PROVED AS A DSD RECLASSIFICATION.**

## 6. What the positive net charge means dynamically

Because

\[
N_j
=
\frac{r_j}{\nu^2}
\left(
\text{stretching production}
-
\text{viscous palinstrophy destruction}
\right),
\]

an active stage satisfies, a fortiori,

\[
\boxed{
\frac{r_j}{\nu^2}
\int_{t_j}^{t_{j+1}}\int\omega^TS\omega\,dxdt
\ge\eta.
}
\]

Thus the positive stretching source is not merely balancing a large palinstrophy loss; on a positive density of generations it exceeds that loss by an order-one normalized amount.

## 7. Critical scaling barrier remains

The physical charge on an active stage is

\[
\eta\frac{\nu^2}{r_j},
\]

which grows geometrically as `r_j->0`.

However there is no established finite global spacetime budget for the stretching integral or for palinstrophy through a hypothetical singularity. The kinetic-energy budget lives one derivative lower and allows scale-wise costs of order `nu^2 r_j`, whose geometric sum is finite.

Therefore the exact balance does **not** by itself contradict blowup.

## 8. New irreducible gate

After the DSD audits, the bounded-Z branch no longer needs primitive survivors named

- infinite tail,
- occupancy failure,
- infinite derivative ladder,
- recurrence-state drift.

The irreducible source question is now:

\[
\boxed{
\text{Can the Navier-Stokes stretching channel sustain a positive-density sequence of}
\quad
N_j\ge\eta>0
\quad
\text{while every genuinely finite-budget lower channel remains summable?}
}
\]

This is the sharpened **Stretching Budget-Closure Gate (SBCG)**.

A non-circular closure must use information not already equivalent to the old `L3 -> concentration -> derivative ladder` route.

Current status:

\[
\boxed{\text{SBCG: NOT DERIVED.}}
\]

## 9. Audit verdict

### PROVED

- exact normalized first-hitting enstrophy balance;
- positive Cesaro floor for normalized net formation;
- positive asymptotic density of stages with order-one positive net formation;
- state recurrence/drift is not needed to show repeated source activity.

### NOT DERIVED

- a finite budget controlling the positive normalized source;
- a non-circular SBCG;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
