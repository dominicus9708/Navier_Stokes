# DSD M5-01 — Fixed-threshold K time-average and spike barrier

Date: 2026-08-26

Status: **DERIVED BASELINE LEMMA + BUDGET COUNTERMODEL / FIXED PHYSICAL THRESHOLD K-TAIL VANISHES IN TIME AVERAGE, BUT FINITE ENERGY AND TOTAL DISSIPATION DO NOT FORCE THE UNIFORM-IN-TIME K-TAIL TIGHTNESS REQUIRED BY M5 / GLOBAL REGULARITY UNPROVED.**

## 0. Place in the canonical stack

This file addresses only M5 of `CANONICAL_PROOF_STACK_2026-08-26.md`.

The target is to understand whether the standard finite-energy information can imply

\[
\lim_{L\to\infty}\sup_{t_0<t<T_*}K_L^{phys}(t)=0,
\]

where

\[
K_L^{phys}(t)
:=
\frac L2\int_{\mathbb R^3}(|u(x,t)|^2-L^2)_+\,dx.
\]

No W1 tail geometry, pressure pump, or recurrence is used until the baseline energy-class information is exhausted.

---

## 1. General q-bound

For every `q>2`, on the set `|u|>L`,

\[
|u|^2\le L^{2-q}|u|^q.
\]

Hence

\[
\begin{aligned}
K_L^{phys}(t)
&\le
\frac L2\int_{|u|>L}|u|^2dx\\
&\le
\frac12L^{3-q}\|u(t)\|_q^q.
\end{aligned}
\]

Therefore

\[
\boxed{
K_L^{phys}(t)
\le
\frac12L^{3-q}\|u(t)\|_q^q.
}
\]

For `q>3` the prefactor decays with `L`.

---

## 2. Energy-line choice q=10/3

The Leray energy class gives

\[
u\in L_t^\infty L_x^2\cap L_t^2\dot H_x^1
\hookrightarrow
L_{t,x}^{10/3}.
\]

More precisely, interpolation between `L2` and `L6` gives

\[
\|u\|_{10/3}^{10/3}
\le
C\|u\|_2^{4/3}\|u\|_6^2
\le
C\|u\|_2^{4/3}\|\nabla u\|_2^2.
\]

Taking `q=10/3` in the previous estimate,

\[
\boxed{
K_L^{phys}(t)
\le
C L^{-1/3}
\|u(t)\|_2^{4/3}
\|\nabla u(t)\|_2^2.
}
\]

Let

\[
E_0:=\sup_{t_0<t<T_*}\|u(t)\|_2^2,
\qquad
\mathcal D_0:=\int_{t_0}^{T_*}\|\nabla u(t)\|_2^2dt.
\]

Then

\[
\boxed{
\int_{t_0}^{T_*}K_L^{phys}(t)dt
\le
C E_0^{2/3}\mathcal D_0\,L^{-1/3}.
}
\]

Consequently

\[
\boxed{
K_L^{phys}\to0
\quad\text{in }L_t^1(t_0,T_*)
\quad(L\to\infty).
}
\]

This is an unconditional consequence of the standard finite-energy/dissipation class.

---

## 3. Measure estimate for large K events

For every `kappa>0`, Chebyshev in time gives

\[
\boxed{
\left|
\{t\in(t_0,T_*):K_L^{phys}(t)\ge\kappa\}
\right|
\le
\frac{C E_0^{2/3}\mathcal D_0}{\kappa}\,L^{-1/3}.
}
\]

Thus large critical-tail events become rare in physical time at large amplitude.

But M5 requires absence of all such events on a terminal interval, not merely small time measure.

---

## 4. Pointwise enstrophy cost of a K event

Using the `q=6` version,

\[
K_L^{phys}(t)
\le
\frac12L^{-3}\|u(t)\|_6^6
\le
C L^{-3}\|\nabla u(t)\|_2^6.
\]

Hence if

\[
K_L^{phys}(t)\ge\kappa>0,
\]

then

\[
\boxed{
\|\nabla u(t)\|_2^2
\ge
c\,\kappa^{1/3}L.
}
\]

This is the exact critical spike scaling: an order-one K event at amplitude `L` requires enstrophy of order `L`.

This lower bound is compatible with Type-I scaling. If

\[
L\asymp (T_*-t)^{-1/2},
\]

then the required enstrophy is only

\[
\|\nabla u(t)\|_2^2\gtrsim (T_*-t)^{-1/2},
\]

whose physical-time integral is finite.

Therefore this pointwise cost alone cannot close M5.

---

## 5. Kinematic critical-spike countermodel to budget-only closure

The next question is whether finite energy plus finite total dissipation might nevertheless rule out infinitely many such events.

It does not, at the level of scaling budgets.

Choose any nonzero smooth compactly supported divergence-free profile

\[
\phi\in C_c^\infty(\mathbb R^3;\mathbb R^3),
\qquad
\nabla\cdot\phi=0.
\]

For `A>0`, define the critical rescaling

\[
\boxed{
u_A(x):=A\phi(Ax).}
\]

Then

\[
\boxed{
\|u_A\|_2^2=A^{-1}\|\phi\|_2^2,
}
\]

and

\[
\boxed{
\|\nabla u_A\|_2^2=A\|\nabla\phi\|_2^2.
}
\]

Fix `0<theta<||phi||_infinity` such that the superlevel is nonempty. At the threshold

\[
L=\theta A,
\]

we have

\[
\begin{aligned}
K_{\theta A}^{phys}[u_A]
&=
\frac{\theta A}{2}
\int
\left(A^2|\phi(Ax)|^2-\theta^2A^2\right)_+dx\\
&=
\frac\theta2
\int
\left(|\phi(y)|^2-\theta^2\right)_+dy.
\end{aligned}
\]

Therefore

\[
\boxed{
K_{\theta A}^{phys}[u_A]
=k_\theta>0
}
\]

independently of `A`.

The weak-`L3` size is likewise scale invariant.

Now choose amplitudes

\[
A_j=2^j
\]

and assign each snapshot a notional physical duration

\[
\Delta t_j\asymp A_j^{-2}.
\]

Then the total dissipation budget required by the snapshots has the scaling

\[
\sum_j
\Delta t_j\|\nabla u_{A_j}\|_2^2
\asymp
\sum_j A_j^{-2}A_j
=
\sum_jA_j^{-1}
<\infty.
\]

Meanwhile every scale carries the same order-one critical K defect:

\[
K_{\theta A_j}^{phys}[u_{A_j}]=k_\theta.
\]

This is **not** an exact Navier--Stokes solution and is not offered as a blow-up construction.
It is a DSD/scaling countermodel showing that the following information is insufficient by itself:

- uniformly finite physical `L2` energy;
- finite total physical enstrophy dissipation;
- the natural parabolic lifetime `A^{-2}` of an amplitude-`A` packet.

Those budgets permit an infinite ladder of increasingly short critical K spikes.

---

## 6. DSD conclusion of M5-01

The standard energy class gives a useful but strictly weaker statement:

\[
\boxed{
\int K_L^{phys}(t)dt\to0
\quad(L\to\infty).
}
\]

M5 requires

\[
\boxed{
\sup_tK_L^{phys}(t)\to0.
}
\]

The countermodel shows that the gap between these two statements is not removable by energy/dissipation bookkeeping alone.

Thus future M5 work must use genuinely dynamical Navier--Stokes structure, for example

- pressure-amplitude level dynamics;
- nonlinear temporal persistence stronger than the bare parabolic packet lifetime;
- a critical compactness/rigidity theorem;
- or another standard PDE property not reducible to the `L2 + L2_t H1` budget.

This locks out the route

\[
\text{finite energy + finite total dissipation}
\Longrightarrow
\text{uniform K tightness}
\]

unless an additional PDE-specific ingredient is explicitly identified.

---

## 7. Next subproblem

The next canonical step is **M5-02**:

> starting from an order-one K event at a large threshold `L`, derive how long the exact Navier--Stokes dynamics must keep a comparable critical tail, and compare that lower persistence time with the `L^{-1/3}` global time-measure budget above.

If the best PDE persistence remains only the parabolic time `cL^{-2}`, then the time-average estimate is too weak to contradict it. If the DSD/pressure-pump structure forces a longer critical persistence, M5 may advance.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]