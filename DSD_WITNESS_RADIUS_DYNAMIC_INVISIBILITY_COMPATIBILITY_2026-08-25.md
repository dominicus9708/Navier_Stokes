# DSD Witness-Radius / Dynamic-Invisibility Compatibility Audit

Date: 2026-08-25

Status: **FIXED-BASE COMPATIBILITY PROVED / CHANNEL-WEIGHT MISMATCH DERIVED / FIXED-BASE TAIL CONTRADICTION PRUNED / CROSS-BASE TRANSFER REMAINS OPEN / GLOBAL REGULARITY NOT PROVED.**

This note continues the DSD-internal audit. The comparison standard is not conformity with a standard Navier–Stokes proof strategy. The question is whether the objects and transitions used in the current proof attempt are legitimately formed, finitely witnessed, and dynamically distinguishable under the DSD ordering

\[
\text{Formation}\to\text{finite composition}\to\text{describability difference}\to\text{dynamics}.
\]

The previous seven-stage audit replaced an infinite tail object by arbitrarily large **finite** witnesses. The present note asks whether those finite global witnesses are incompatible with local dynamic invisibility.

---

## 1. Finite cubic witness depth and witness radius

On the corrected bounded-\(Z\), recurrent, non-\(L^3\) branch, let

\[
a_k:=J_k^{3/2}\ge0,
\qquad
\sum_{k=1}^{\infty}a_k=\infty.
\]

Do not treat the infinite sum as one Stage-VII DSD composite. For every finite threshold \(L>0\), define the finite witness depth

\[
\boxed{
K_{\rm wit}(L)
:=
\min\left\{K\in\mathbb N:
\sum_{k=1}^{K}a_k\ge L
\right\}.
}
\]

Let the corresponding shell radii be geometric,

\[
R_k=R_0\lambda^k,
\qquad \lambda>1,
\]

with the first-hitting normalization giving the special case

\[
\lambda=q^{1/2}.
\]

Define

\[
\boxed{
R_{\rm wit}(L):=R_{K_{\rm wit}(L)}.
}
\]

Every finite \(L\) therefore has a finite Stage-VII witness block.

Because every finite partial sum is finite and the total series diverges,

\[
\boxed{
K_{\rm wit}(L)\to\infty,
\qquad
R_{\rm wit}(L)\to\infty
\quad(L\to\infty).
}
\]

**Status: PROVED.**

---

## 2. Fixed-base compatibility theorem

Let \(B\) be one fixed finite DSD base, for example

\[
B=(M,T,N),
\]

where \(M\) is a fixed spatial window, \(T\) a fixed finite ancient-time window, and \(N\) a fixed finite derivative/channel depth. These are technical coordinates/indices of the description, not formal DSD axes.

Assume the already-derived far-field decoupling estimate has the abstract form

\[
\boxed{
\Delta_B(R)
\le
C_B R^{-\alpha},
\qquad \alpha>0,
}
\]

for sufficiently remote truncation radius \(R\).

Then at the finite witness radius,

\[
\Delta_B(R_{\rm wit}(L))
\le
C_B R_0^{-\alpha}
\lambda^{-\alpha K_{\rm wit}(L)}.
\]

Since \(K_{\rm wit}(L)\to\infty\),

\[
\boxed{
\Delta_B(R_{\rm wit}(L))\to0.
}
\]

Therefore

\[
\boxed{
\begin{array}{c}
\text{arbitrarily large finite global cubic witnesses}\\
+\\
\text{asymptotically vanishing local dynamic difference}
\end{array}
\quad\text{are automatically compatible on every fixed finite base.}
}
\]

There is no DSD contradiction here. The two statements live in different finite descriptions and remain simultaneously realizable.

**Status: PROVED.**

---

## 3. Explicit harmonic saturation witness

The already-established arithmetic counterexample

\[
J_k=k^{-2/3}
\]

gives

\[
a_k=J_k^{3/2}=\frac1k.
\]

Hence

\[
\sum_{k\le K}a_k
=\log K+O(1),
\]

and therefore

\[
\boxed{
K_{\rm wit}(L)=\exp(L+O(1)).
}
\]

Consequently

\[
R_{\rm wit}(L)
=R_0\lambda^{\exp(L+O(1))},
\]

and the fixed-base dynamic difference satisfies

\[
\boxed{
\Delta_B(R_{\rm wit}(L))
\lesssim_B
\exp\!\left[-\alpha(\log\lambda)\exp(L+O(1))\right].
}
\]

Thus a global finite witness can grow without bound while its influence on a fixed local base becomes super-exponentially small in the witness threshold \(L\).

This is an explicit realization of

\[
\boxed{
\text{global distinguishability growth}
\quad\text{with}\quad
\text{local dynamic invisibility}.
}
\]

**Status: PROVED for the explicit admissible arithmetic sequence; this does not assert that every Navier–Stokes tail has this exact sequence.**

---

## 4. Divergence alone gives no useful upper bound on witness depth

The compatibility is even stronger arithmetically.

Let \(G(m)\uparrow\infty\) be any prescribed increasing sequence. Choose strictly increasing indices

\[
N_m\ge G(m)
\]

and define

\[
a_{N_m}=\frac1m,
\qquad
a_k=0\quad(k\notin\{N_m\}).
\]

Then

\[
\sum_ka_k=\sum_m\frac1m=\infty.
\]

For

\[
L_m:=\sum_{n=1}^{m}\frac1n,
\]

one has exactly

\[
\boxed{
K_{\rm wit}(L_m)=N_m\ge G(m).
}
\]

Hence divergence of the finite-witness ledger alone permits the witness depth to grow as rapidly as any preassigned sequence along a threshold subsequence.

Therefore no universal upper bound

\[
K_{\rm wit}(L)\le F(L)
\]

can follow from \(\sum a_k=\infty\) alone.

This eliminates a possible DSD shortcut: global non-\(L^3\) distinguishability does not force the witness to remain close enough to a fixed core to retain a non-negligible dynamic channel.

**Status: PROVED as an arithmetic non-implication.**

---

## 5. Conditional shellwise upper bound makes invisibility stronger

If an additional independent estimate gives

\[
a_k\le A<\infty,
\]

then any threshold \(L\) requires

\[
K_{\rm wit}(L)\ge \frac{L}{A}
\]

up to the integer convention. Therefore

\[
R_{\rm wit}(L)
\ge
R_0\lambda^{L/A+O(1)},
\]

and

\[
\boxed{
\Delta_B(R_{\rm wit}(L))
\lesssim_B
\exp\!\left[-\frac{\alpha\log\lambda}{A}L\right].
}
\]

Thus a shellwise amplitude upper bound does **not** create a contradiction; it pushes the finite global witness farther away and strengthens local invisibility.

No claim is made here that the present bounded-\(Z\) hypothesis by itself supplies this exact uniform \(a_k\le A\) bound.

**Status: CONDITIONAL.**

---

## 6. Direct shell-to-core channel-weight mismatch

The previous theorem used an abstract decay modulus. We can also see the mismatch directly from the Biot–Savart distance weights.

Take a dyadic/geometric annulus \(A_k\) at radius \(R_k\), with \(R_k\ge2M\), and define

\[
J_k
=
R_k\int_{A_k}|\nabla u|^2dy.
\]

Let \(U_k\) denote the velocity contribution induced by vorticity on \(A_k\). For \(x\in B_M\), the Biot–Savart kernel has size \(O(R_k^{-2})\), and its \(m\)-th velocity derivative has size \(O(R_k^{-2-m})\). Also

\[
\|\omega\|_{L^1(A_k)}
\lesssim
R_k^{3/2}\|\nabla u\|_{L^2(A_k)}
=
R_kJ_k^{1/2}.
\]

Therefore

\[
\boxed{
\|\nabla^mU_k\|_{L^\infty(B_M)}
\lesssim_m
\frac{J_k^{1/2}}{R_k^{m+1}},
\qquad R_k\ge2M.
}
\]

In particular,

\[
\boxed{
|U_k|_{B_M}\lesssim\frac{J_k^{1/2}}{R_k},
\qquad
|\nabla U_k|_{B_M}\lesssim\frac{J_k^{1/2}}{R_k^2}.
}
\]

Compare this with the global cubic channel

\[
\boxed{a_k=J_k^{3/2}.}
\]

The two channels use fundamentally different aggregation weights:

\[
\boxed{
\text{global cubic witness: }J_k^{3/2},
\qquad
\text{local velocity transfer: }J_k^{1/2}R_k^{-1},
\qquad
\text{local strain transfer: }J_k^{1/2}R_k^{-2}.
}
\]

Thus equality or divergence in the global cubic aggregation channel cannot be promoted to non-negligibility in the local dynamic channel.

This is a DSD channel-typing result: the same finite shell may be strongly distinguishable in one formed channel and negligible in another.

**Status: PROVED at the level of the stated shell estimate.**

---

## 7. Finite-enstrophy tail gives summable local transfer

Let

\[
e_k:=\int_{A_k}|\nabla u|^2
=\frac{J_k}{R_k}.
\]

If the relevant time slice has finite global enstrophy/gradient energy,

\[
\sum_ke_k\le E_\nabla<\infty,
\]

then

\[
\frac{J_k^{1/2}}{R_k}
=
\frac{e_k^{1/2}}{R_k^{1/2}},
\]

and Cauchy–Schwarz gives for the remote tail

\[
\sum_{k\ge K}rac{J_k^{1/2}}{R_k}
\le
\left(\sum_{k\ge K}e_k\right)^{1/2}
\left(\sum_{k\ge K}R_k^{-1}\right)^{1/2}.
\]

Since \(R_k\) is geometric,

\[
\sum_{k\ge K}R_k^{-1}\lesssim R_K^{-1}.
\]

Hence

\[
\boxed{
\sum_{k\ge K}|U_k|_{B_M}
\lesssim
E_\nabla^{1/2}R_K^{-1/2}.
}
\]

Likewise

\[
\boxed{
\sum_{k\ge K}|\nabla U_k|_{B_M}
\lesssim
E_\nabla^{1/2}R_K^{-3/2}.
}
\]

Higher fixed derivative channels gain still stronger geometric distance weights.

Therefore a finite-enstrophy shell family can simultaneously satisfy

\[
\sum_kJ_k^{3/2}=\infty
\]

and have a summable, vanishing remote influence on every fixed local velocity/strain channel.

This is exactly the structural coexistence DSD must preserve rather than collapse into `tail exists / tail does not exist`.

**Status: PROVED conditionally on finite enstrophy/gradient energy on the slice under consideration.**

---

## 8. Why expanding the base is the only remaining static-to-dynamic route

The fixed-base route is now closed:

\[
\boxed{
\text{large finite global witness}
\not\Rightarrow
\text{non-negligible fixed-core dynamic influence}.
}
\]

To see the cubic witness itself, the spatial description must eventually extend to its radius. Introduce a finite growing base

\[
B(L)=(M(L),T(L),N(L)),
\]

with every \(B(L)\) finite for finite \(L\).

There are then two regimes.

### Regime A — separated growing base

If

\[
M(L)\le\theta R_{\rm wit}(L),
\qquad 0<\theta<1,
\]

then the witness remains genuinely remote from the observation base. The distance kernel still gives a positive fraction of \(R_{\rm wit}\) as separation, so fixed-order local dynamic channels retain geometric decay.

### Regime B — witness-containing base

If the description is enlarged until

\[
M(L)\gtrsim R_{\rm wit}(L),
\]

then the witness is no longer a remote channel. It has entered the finite descriptor itself.

But this does not prove that it drives the original local singular core. It only proves that a larger finite description contains both the core and the witness.

The missing operation is therefore not another static aggregation. It is a **cross-base dynamic transfer map** from the outer formed witness to the retained inner core channels.

---

## 9. Cross-Base Transfer Gate (CBTG)

Let \(B_{\rm in}\) be a fixed finite core base and \(B_{\rm out}(L)\) a finite base large enough to contain the cubic witness of threshold \(L\).

Define schematically a dynamic transfer modulus

\[
\mathcal I_L
:=
\text{describability difference induced on }B_{\rm in}
\text{ by the witness channels in }B_{\rm out}(L)\setminus B_{\rm in}.
\]

A genuine static-to-singular bridge would need an independently proved lower bound such as

\[
\boxed{
\mathcal I_L\ge c>0
}
\]

along an unbounded sequence of thresholds, or another non-summable lower-order transfer law.

The present cubic witness condition supplies no such lower bound. The direct distance estimates instead allow

\[
\mathcal I_L\to0.
\]

Therefore introduce the DSD audit gate

\[
\boxed{
\text{Cross-Base Transfer Gate (CBTG):}
\quad
\text{outer finite witness}\Rightarrow
\text{quantified non-vanishing inner dynamic channel}.
}
\]

Current status:

\[
\boxed{\text{CBTG is NOT DERIVED.}}
\]

Material recurrence or quantitative return density could in principle provide a historical transfer channel, but the previous recurrence audit classified those as R3/R4 and **NOT DERIVED**.

---

## 10. Base-growth constant formulation

If one insists on writing a growing-base decoupling estimate

\[
\Delta_{B(L)}(R)
\le
C_{B(L)}R^{-\alpha},
\]

then at the witness radius

\[
\Delta_{B(L)}(R_{\rm wit}(L))
\le
\frac{C_{B(L)}}{R_{\rm wit}(L)^\alpha}.
\]

Thus a necessary condition for a non-vanishing witness effect is failure of

\[
\boxed{
C_{B(L)}=o(R_{\rm wit}(L)^\alpha).
}
\]

However this formulation must be interpreted with the spatial-separation condition above. If \(M(L)\) reaches the witness radius, the witness is no longer part of the remote remainder and the far-field estimate has changed its meaning.

So the more invariant DSD formulation is CBTG, not merely growth of the analytic constant \(C_{B(L)}\).

---

## 11. DSD verdict on the tail route

### PROVED

1. Every finite cubic threshold has a finite witness depth/radius.
2. \(K_{\rm wit}(L),R_{\rm wit}(L)\to\infty\).
3. Any fixed-base algebraic far-field decay makes the dynamic difference at the witness radius tend to zero.
4. Cubic divergence alone gives no upper growth law for witness depth.
5. Shell-to-core velocity/strain channels carry geometric distance weights different from the global cubic channel.
6. Under finite enstrophy on the relevant slice, the remote shell influence on fixed local velocity/strain channels is summable and vanishes.

### CONDITIONAL

1. Any stronger rate derived from a uniform shellwise bound.
2. Uniform-in-time versions of the shell-to-core estimates across the whole ancient window require the corresponding uniform enstrophy control.
3. A growing-base estimate depends on how spatial window, time window, derivative depth, and retained channel family grow.

### NOT DERIVED

1. A non-vanishing cross-base transfer lower bound tied to cubic witness size.
2. Material identity of remote witnesses across first-hitting generations.
3. Quantitative return density sufficient to accumulate a historical core influence.
4. Any contradiction to candidate singular growth from the cubic tail alone.
5. Global regularity.

---

## 12. Consequence for the proof frontier

The DSD audit now prunes the following route:

\[
\boxed{
\text{global cubic finite-witness growth}
\Longrightarrow
\text{fixed-core singular forcing}
}
\]

as an unsupported inference.

The surviving possibilities are narrower:

\[
\boxed{
\begin{array}{c}
\text{(A) prove CBTG through an independently formed historical/return channel},\\[2mm]
\text{or}\\[2mm]
\text{(B) discard the global tail as the forcing mechanism and return to the formed local core channels.}
\end{array}
}
\]

Since R3/R4 material/quantitative recurrence is presently not derived, route (A) currently has no established carrier. Therefore the strongest presently formed route is (B): the local first-hitting core, including the transverse direction-curvature / sparsity / palinstrophy / higher-derivative survivor tree.

This is not an appeal to standard theory. It is the result of DSD's own formation, finite-composition, channel-typing, and describability-difference audit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
