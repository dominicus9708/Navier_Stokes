# DSD first-hitting / Leray clock coboundary gate

Date: 2026-08-25

Status: **EXACT CLOCK-DEFECT IDENTITY PROVED / TWO-SIDED TYPE-I CLOCK COMPARABILITY PROVED ON THE EXISTING NON-H/T RECURRENT STAGE CORRIDOR / CUMULATIVE CLOCK DRIFT IS BOUNDED / GENERATION INDEX AND LERAY TIME ARE ASYMPTOTICALLY LOCKED / DSS STILL NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_CORE_TAIL_STATIC_COMPATIBILITY_DYNAMIC_MAINTENANCE_2026-08-25.md` and audits the temporal channel left after the passive critical-tail compatibility calculation.

The key question is whether the geometric first-hitting clock

\[
W_j=q^jW_0
\]

can drift arbitrarily far from the standard backward self-similar/Leray clock near a hypothetical singular time `T*`.

The answer is **no on the already established non-H/T recurrent stage corridor**: the discrepancy is an exact bounded coboundary. This is a branch-restricted result and is not promoted to the whole bounded-Z branch.

## 1. Scope and existing stage corridor

Use viscosity `nu>0` and

\[
W_j=q^jW_0,
\qquad
r_j=\left(\frac{\nu}{W_j}\right)^{1/2},
\qquad q>1.
\]

Let

\[
\Delta t_j:=t_{j+1}-t_j.
\]

The existing `SLIDING_HISTORY_REMAINING_TIME_CLOSURE_2026-08-23.md` records that on the non-H/T recurrent first-hitting corridor the dynamically normalized stage lengths obey

\[
0<L_-\le L_j\le L_+<\infty.
\]

During the first-hitting stage, the running maximum lies between the two geometric levels,

\[
W_j\le \overline W(t)\le W_{j+1}=qW_j.
\]

For the dynamic time length

\[
L_j=\int_{t_j}^{t_{j+1}}\overline W(t)\,dt,
\]

this gives

\[
W_j\Delta t_j
\le L_j
\le qW_j\Delta t_j.
\]

Define the exact adjacent first-hitting parabolic gap

\[
\boxed{
\tau_j:=W_j\Delta t_j
=\frac{\nu\Delta t_j}{r_j^2}.
}
\]

Then the corridor bounds imply

\[
\boxed{
\tau_-:=\frac{L_-}{q}
\le\tau_j\le
L_+=:\tau_+.
}
\]

Status: **PROVED on the stated existing corridor.**

## 2. Exact remaining-time amplitude variable

Let

\[
\delta_j:=T^*-t_j>0
\]

and define the dimensionless remaining-time amplitude

\[
\boxed{
\Theta_j
:=W_j\delta_j
=\frac{\nu(T^*-t_j)}{r_j^2}.
}
\]

Because the first-hitting times accumulate at `T*`, one has exactly

\[
\delta_j
=\sum_{n=0}^{\infty}\Delta t_{j+n}.
\]

Using

\[
W_{j+n}=q^nW_j,
\qquad
\Delta t_{j+n}=\frac{\tau_{j+n}}{W_{j+n}},
\]

we obtain the exact geometric convolution

\[
\boxed{
\Theta_j
=\sum_{n=0}^{\infty}q^{-n}\tau_{j+n}.
}
\]

Hence the stage corridor yields the two-sided Type-I remaining-time bound

\[
\boxed{
\Theta_-
:=\frac{\tau_-}{1-q^{-1}}
\le
\Theta_j
\le
\frac{\tau_+}{1-q^{-1}}
=: \Theta_+.
}
\]

Equivalently,

\[
\boxed{
\frac{\Theta_-}{W_j}
\le
T^*-t_j
\le
\frac{\Theta_+}{W_j}.
}
\]

Restoring the radius,

\[
\boxed{
\Theta_-\frac{r_j^2}{\nu}
\le
T^*-t_j
\le
\Theta_+\frac{r_j^2}{\nu}.
}
\]

Thus the first-hitting scale and remaining singular time are genuinely comparable from both sides on this corridor.

Status: **PROVED.**

## 3. Exact one-step recursion

Since

\[
\delta_j=\Delta t_j+\delta_{j+1},
\]

multiplication by `W_j` gives

\[
\Theta_j
=\tau_j+W_j\delta_{j+1}.
\]

But

\[
W_j=q^{-1}W_{j+1},
\]

so

\[
\boxed{
\Theta_j
=\tau_j+q^{-1}\Theta_{j+1}.
}
\]

Equivalently,

\[
\boxed{
\tau_j
=\Theta_j-q^{-1}\Theta_{j+1}.
}
\]

This is an exact finite first-hitting clock identity.

## 4. Leray clock and exact defect formula

Define the standard backward self-similar time, up to an irrelevant additive constant, by

\[
\boxed{
s_j:=-\log(T^*-t_j)=-\log\delta_j.}
\]

Since

\[
\delta_j=\frac{\Theta_j}{W_j},
\]

we have

\[
s_j
=\log W_j-\log\Theta_j.
\]

Using `W_j=q^jW_0`,

\[
\boxed{
s_j
=j\log q+\log W_0-\log\Theta_j.}
\]

Therefore the difference between the physical Leray clock and the exact arithmetic first-hitting clock is simply

\[
\boxed{
\mathcal C_j
:=s_j-j\log q
=\log W_0-\log\Theta_j.
}
\]

Because

\[
0<\Theta_-\le\Theta_j\le\Theta_+<\infty,
\]

we get the uniform clock-defect bound

\[
\boxed{
|\mathcal C_j|
\le C_{clock}<\infty
}
\]

for all sufficiently late stages on the corridor.

Thus

\[
\boxed{
s_j=j\log q+O(1).}
\]

Status: **PROVED.**

## 5. Adjacent Leray-gap defect is a coboundary

Subtract consecutive clock values:

\[
\begin{aligned}
s_{j+1}-s_j
&=\log q
+\log\Theta_j-\log\Theta_{j+1}.
\end{aligned}
\]

Define

\[
\boxed{
\varepsilon_j
:=(s_{j+1}-s_j)-\log q.
}
\]

Then exactly

\[
\boxed{
\varepsilon_j
=\log\Theta_j-\log\Theta_{j+1}.
}
\]

Therefore the clock defect is a discrete coboundary.

For every finite block `J<N`,

\[
\boxed{
\sum_{j=J}^{N-1}\varepsilon_j
=\log\Theta_J-\log\Theta_N.
}
\]

Consequently

\[
\boxed{
\left|
\sum_{j=J}^{N-1}
\big[(s_{j+1}-s_j)-\log q\big]
\right|
\le
\log\frac{\Theta_+}{\Theta_-}.
}
\]

The cumulative discrepancy from exact DSS clock spacing is uniformly bounded, independently of the number of generations.

Status: **PROVED.**

## 6. Asymptotic mean Leray spacing

Divide the finite-block identity by `N-J`:

\[
\frac{s_N-s_J}{N-J}
=
\log q
+
\frac{\log\Theta_J-\log\Theta_N}{N-J}.
\]

The endpoint term vanishes in the long-block limit. Hence

\[
\boxed{
\lim_{N-J\to\infty}
\frac{s_N-s_J}{N-J}
=\log q.
}
\]

Thus one first-hitting generation corresponds asymptotically to exactly `log q` of Leray time on average.

This conclusion does not require `Theta_j` to converge.

## 7. Fixed finite generation blocks

For a fixed integer `m>=1`,

\[
\boxed{
s_{j+m}-s_j
=m\log q
+\log\frac{\Theta_j}{\Theta_{j+m}}.}
\]

Since the `Theta` channel is compact in `[Theta_-,Theta_+]`, every sequence of `m`-block clock gaps has a convergent subsequence in the finite interval

\[
\boxed{
\left[
m\log q-\log\frac{\Theta_+}{\Theta_-},
\quad
m\log q+\log\frac{\Theta_+}{\Theta_-}
\right].
}
\]

If, on a recurrent subsequence, the remaining-time amplitudes also recur,

\[
\Theta_{j_n+m}-\Theta_{j_n}\to0
\]

with both bounded away from zero, then

\[
\boxed{
s_{j_n+m}-s_{j_n}\to m\log q.}
\]

This is the exact temporal bridge needed to turn an `m`-generation recurrent normalized spacetime state into an asymptotic DSS clock relation.

The recurrence of `Theta` over the same fixed `m` is an additional formed channel and is **not** assumed automatically.

## 8. DSD audit: clock drift is not an independent unbounded escape

The normalized state should distinguish at least

- local normalized fields;
- global critical tail channels;
- center/provenance channels;
- the remaining-time amplitude `Theta_j`;
- transition/stage data.

On the non-H/T recurrent corridor, `Theta_j` lives in a fixed compact positive interval and its cumulative logarithmic drift telescopes.

Therefore the survivor cannot evade self-similar comparison merely by letting the first-hitting clock and Leray clock separate without bound.

In DSD terms,

\[
\boxed{
\text{unbounded clock desynchronization is pruned on this corridor.}
}
\]

What remains is genuine state/tail dynamics, not an arbitrary time-reparametrization escape.

## 9. Relation to one-slice approximate self-similarity

The Pineau--Vicol one-slice criterion used elsewhere in the repository says, under its spatial Type-I and pressure-annulus hypotheses, that sufficiently small self-similar-time velocity `partial_s V` at one sufficiently late time regularizes the point.

The present clock theorem does **not** force

\[
\partial_sV\to0.
\]

A bounded recurrent orbit can move with nonzero speed while its sampling clock remains asymptotically arithmetic.

Hence the correct implication is only

\[
\boxed{
\text{recurrent first-hitting state}
+
\text{two-sided Type-I clock}
\Longrightarrow
\text{recurrent dynamics sampled at }s_j=j\log q+O(1),
}
\]

not stationarity or DSS.

This respects the known periodic/rotating counterexample to the invalid inference `recurrence => small speed`.

## 10. New sharpened dynamic frontier

Combining the passive-tail audit with the clock result, the non-H/T recurrent survivor can no longer use either

1. static incompatibility of core and a `1/r` critical tail, or
2. unbounded desynchronization between the first-hitting and Leray clocks,

as a primitive terminal mechanism.

The remaining dynamic object is a bounded recurrent Leray trajectory with

- an asymptotically arithmetic first-hitting sampling clock;
- a non-L3 critical tail or one of its critical derivative escape channels;
- positive source/formation charges from the bounded-Z first-hitting ledger;
- and, on the spatial Type-I subbranch, the positive late Leray-speed floor required by the one-slice regularity theorem.

A next successful closure must therefore control **phase-space motion per Leray cycle**, not merely norm size or clock spacing.

Call the remaining branch-restricted question the

\[
\boxed{\text{Leray Recurrent Motion Gate (LRMG).}}
\]

It asks whether the Navier--Stokes/Leray equations can sustain a bounded recurrent nontrivial orbit with the required critical tail and positive first-hitting formation charges indefinitely while avoiding every one-slice small-speed time.

Current status:

\[
\boxed{\text{LRMG: NOT DERIVED.}}
\]

## 11. Audit verdict

### PROVED on the existing non-H/T recurrent first-hitting corridor

- adjacent physical first-hitting gaps are two-sided comparable to `1/W_j`;
- `Theta_j=W_j(T*-t_j)` is exactly a geometrically weighted future-gap convolution;
- `Theta_j` has fixed positive upper and lower bounds;
- `s_j=j log q+O(1)`;
- adjacent Leray-clock defect is the coboundary `log Theta_j-log Theta_{j+1}`;
- cumulative clock drift over arbitrarily many generations is uniformly bounded;
- mean Leray time per first-hitting generation tends exactly to `log q`.

### NOT DERIVED

- the same two-sided clock theorem on every bounded-Z branch outside the stated corridor;
- convergence of `Theta_j`;
- fixed-period DSS;
- small `partial_s V` at any late time;
- LRMG;
- contradiction to the singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
