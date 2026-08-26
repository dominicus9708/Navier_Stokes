# DSD M5-11 — Recurrent critical Lyapunov closure principle

Date: 2026-08-26

Status: **DERIVED DYNAMICAL-SYSTEMS CLOSURE PRINCIPLE / IDENTIFIES THE TYPE OF NEW FUNCTIONAL THAT WOULD ACTUALLY CLOSE W1 / ALL CURRENT CANDIDATE LEDGERS FAIL BY A SPECIFIC SOURCE OR BOUNDARY CHANNEL / GLOBAL REGULARITY UNPROVED.**

## 1. Setting

Let `M` be a compact nontrivial minimal invariant W1 set for the Leray flow `Phi_s`.

Assume there is a continuous functional

\[
\mathcal L:M\to\mathbb R
\]

which is absolutely continuous along every trajectory and satisfies

\[
\boxed{
\frac d{ds}\mathcal L(\Phi_sU)
\le
-\mathcal D(\Phi_sU)
}
\]

for a continuous function

\[
\mathcal D:M\to[0,\infty).
\]

## 2. Recurrence rigidity

Because `M` is compact and minimal, it supports an invariant probability measure `mu` with full support on `M` (or one may work on a full-support ergodic component of a minimal flow).

Invariant averaging of the trajectory inequality gives

\[
0
\le
-\int_M\mathcal D(U)d\mu(U).
\]

Since `D>=0`,

\[
\boxed{
\int_M\mathcal D\,d\mu=0.
}
\]

Continuity of `D` and full support imply

\[
\boxed{
\mathcal D\equiv0\quad\text{on }M.
}
\]

Equivalently, a continuous nonincreasing Lyapunov functional on a compact recurrent minimal set cannot undergo a strict recurrent decrease.

## 3. Immediate W1 closure criterion

If one can construct a **critical** functional `L` for which

\[
\boxed{
\mathcal D(U)=0
\Longrightarrow
U=0,
}
\]

then every compact minimal W1 set is trivial.

Since the retained W1 endpoint is nontrivial, such a functional would contradict the W1 survivor and close the endpoint.

Thus a single theorem of the form

\[
\boxed{
\text{continuous critical state functional}
+\text{strict sign-definite dissipation}
}
\]

would solve M5 inside the retained W1 corridor.

## 4. Why the known ledgers do not qualify

### 4.1 Physical kinetic energy

The ordinary physical energy is monotone, but it is subcritical relative to the blow-up renormalization. In the normalized W1 state it does not provide a finite coercive critical functional on the large `1/r` endpoint. Its per-scale physical cost is geometrically summable.

### 4.2 Gaussian relative variance

The exact Gaussian ledger has the form

\[
V_a'
+\text{positive terms}
=F_{mech,a}.
\]

The mechanical replenishment term has positive invariant mean on a nontrivial W1 set. Hence `V_a` is not a strict Lyapunov functional.

### 4.3 Critical cubic / amplitude-state ledger

The `p=3` and thresholded `K` equations contain the gauge-independent pressure/amplitude work and the critical boundary charge. They are transport/gain ledgers, not sign-definite Lyapunov laws.

### 4.4 Weighted critical energy

M5-9 gives

\[
\mathcal W'
+\nu\mathcal D_W
+\text{favorable center term}
=\Phi_W,
\]

where `Phi_W` is the critical radial energy/pressure flux. No universal sign is available.

### 4.5 Enstrophy

The Leray enstrophy law contains the vortex-stretching source

\[
\int\Omega^TS\Omega.
\]

Its invariant mean is positive on the retained nontrivial W1 class, so enstrophy is not monotone.

### 4.6 Weighted vorticity / cross-radius action

The M5-8 Hodge coercivity proves that critical shell mass pays radial variation and/or angular-vorticity action, but it does not produce a bounded monotone state functional whose derivative is minus that action.

## 5. DSD interpretation

The failed candidates fail for typed reasons, not merely because an estimate is numerically weak:

- kinetic energy: wrong scaling layer;
- Gaussian variance: interior replenishment source;
- cubic/K ledger: amplitude-boundary transport;
- weighted energy: spatial-boundary flux;
- enstrophy: strain/stretching source;
- cross-radius Hodge action: coercivity without a global Lyapunov primitive.

Therefore these channels should not be repeatedly recombined and called monotone unless a genuinely new cancellation identity is proved.

## 6. Two equivalent-looking live formulations of M5

After M5-1 through M5-10, the live endpoint can be attacked in either of two structurally meaningful ways:

### A. Critical-tail compactness

Prove the existing M5 target

\[
\lim_{L\to\infty}\sup_{t<T_*}K_L^{phys}(t)=0
\]

or an equivalent strong-critical upgrade.

### B. Critical recurrent Lyapunov rigidity

Construct a continuous critical `L` on the W1 compact state space with

\[
\frac d{ds}\mathcal L\le-\mathcal D,
\qquad
\mathcal D\ge0,
\qquad
\mathcal D^{-1}(0)=\{0\}.
\]

Either route eliminates the same large weak-critical recurrent endpoint.

## 7. What would count as genuine progress from here

A new candidate is useful only if it accomplishes at least one of:

1. removes a source term by an exact identity rather than an estimate;
2. turns the source into a boundary term already controlled by `K`-tightness;
3. produces a scale-critical quantity uniformly bounded by the physical prelimit;
4. proves that a nonzero W1 recurrent state forces strictly positive dissipation in a source-free critical ledger.

Creating additional subcritical budgets or instantaneous smallness estimates does not advance M5.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
