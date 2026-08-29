# DSD M5-278 — Albritton–Barker Contrapositive and H-Frequency Saturation

Date: 2026-08-30

Parent: `DSD_M5_277_COMPACTNESS_FAILURE_COLLAPSE_TO_H_OR_T_2026-08-30.md`

Status: **H-BRANCH SHARPENING / ON ANY COMPLETE NONTRIVIAL MILD ANCIENT BRANCH WHOSE TERMINAL TRACE SATISFIES THE ALBRITTON–BARKER BESOV CONDITION, A BOUNDED WEAK-`L^3` BACKWARD SUBSEQUENCE IS IMPOSSIBLE / HENCE THE WEAK-CRITICAL NORM MUST DIVERGE EVENTUALLY AS ANCIENT TIME GOES TO `-infinity` / IF CAMPANATO TURNOVER IS EXCLUDED, THE EXISTING ANNULAR ROUTING THEN FORCES UNBOUNDED CRITICAL SHELL H1 ENERGY AND UNBOUNDED DERIVATIVE RATIO AT EVERY SUFFICIENTLY OLD EPOCH / H IS THEREFORE AN EVENTUAL SATURATION MECHANISM, NOT A SPARSE EXCEPTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Starting master tree

M5-277 gives

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H\lor T.
}
\]

The present note does not close `H`.  It proves that the part of `H` capable of evading the weak-critical Liouville theorem must be much stronger than an occasional derivative spike.

---

## 2. Contrapositive of Albritton–Barker Theorem 4.1

Let `U` be a complete nontrivial mild ancient solution on

\[
\mathbb R^3\times(-\infty,0)
\]

with terminal trace `T=U(0)` satisfying

\[
\operatorname{dist}_{\dot B^{-1}_{\infty,\infty}}(T,\mathbb B)
<\varepsilon(M)
\]

for the relevant weak-critical size.

Albritton–Barker Theorem 4.1 says that if there exists a sequence

\[
\tau_k\downarrow-\infty
\]

with

\[
\sup_k\|U(\tau_k)\|_{L^{3,\infty}}<\infty,
\]

then `U=0`.

Therefore for a nontrivial `U`, **no bounded weak-`L^3` backward subsequence can exist**.

Equivalently,

\[
\boxed{
\|U(\tau)\|_{L^{3,\infty}}
\to\infty
\qquad(\tau\to-\infty).
}
\]

Proof of equivalence: if the norm did not tend to infinity, there would exist a finite `M` and a sequence `tau_k -> -infinity` with

\[
\|U(\tau_k)\|_{L^{3,\infty}}\le M,
\]

contradicting the theorem.

Status: **EXACT CONTRAPOSITIVE.**

---

## 3. Convert ancient time to the complete W1 orbit

The global RG identity writes

\[
U(\tau)
=
\mathscr R_{-\tau}(T)
=
R\,(S(h)V)(R\,\cdot),
\]

with

\[
R=(-\tau)^{-1/2},
\qquad
h=-\log(-\tau).
\]

The weak-`L^3` Lorentz norm is Navier–Stokes critical, hence

\[
\boxed{
\|U(\tau)\|_{L^{3,\infty}}
=
\|S(h)V\|_{L^{3,\infty}}.
}
\]

As

\[
\tau\to-\infty,
\]

we have

\[
h\to-\infty.
\]

Thus the nontrivial survivor condition becomes

\[
\boxed{
\|S(h)V\|_{L^{3,\infty}}
\to\infty
\qquad(h\to-\infty).
}
\]

---

## 4. Exclude Campanato turnover and invoke the annular weak-critical routing

Assume for this subsection that the T branch is absent in the form

\[
\boxed{
\sup_{h\le h_0}
\sup_{R\ge R_0}
\mathfrak C_A(R,h)
\le C_T<\infty.
}
\]

The existing annular weak-`L^3` gate says

\[
\sup_R E_1(R,h)<\infty,
\qquad
\sup_R\mathfrak C_A(R,h)<\infty
\Longrightarrow
\|S(h)V\|_{L^{3,\infty}}<\infty,
\]

with the bound quantitative in the two suprema.

Since the weak-critical norm tends to infinity while the Campanato factor remains bounded, it follows that

\[
\boxed{
\sup_R E_1(R,h)	o\infty
\qquad(h\to-\infty),
}
\]

where

\[
E_1(R,h)
:=R\int_{A_R^*}|\nabla S(h)V|^2.
\]

Thus the surviving non-T branch must carry arbitrarily large scale-critical shell derivative energy at every sufficiently old epoch.

---

## 5. Critical H1 escalation forces derivative-ratio escalation

For the localized divergence-free packet `f_R`, the existing gate gives in the genuinely escalating regime

\[
\boxed{
\Gamma_R^2
\gtrsim
\frac{E_1(R)}{\mathfrak C_A(R)},
\qquad
\Gamma_R=
\frac{R\|\nabla f_R\|_2}{\|f_R\|_2}.
}
\]

With

\[
\mathfrak C_A\le C_T
\]

and

\[
\sup_R E_1(R,h)\to\infty,
\]

we obtain

\[
\boxed{
\sup_R\Gamma_R(h)	o\infty
\qquad(h\to-\infty).
}
\]

More quantitatively, for every finite threshold `Gamma_*` there exists `h_*<0` such that for every

\[
h<h_*,
\]

at least one shell satisfies

\[
\boxed{
\Gamma_R(h)>\Gamma_*.
}
\]

Thus H cannot be a zero-density collection of isolated exceptional epochs if it is the only mechanism preventing the Liouville closure.

---

## 6. Eventual saturation formulation

The non-T ancient survivor must satisfy

\[
\boxed{
\forall \Gamma_*<\infty,
\quad
\exists h_*(\Gamma_*)
\quad\text{such that}\quad
h<h_*
\Longrightarrow
\sup_R\Gamma_R(h)>\Gamma_*.
}
\]

This is stronger than

\[
\limsup_{h\to-\infty}\sup_R\Gamma_R(h)=\infty.
\]

It is genuine **eventual divergence**.

Likewise

\[
\boxed{
\sup_R E_1(R,h)\to\infty.
}
\]

Hence every far-backward slice has an increasingly severe derivative-frequency shell.

---

## 7. Why this matters for the next H audit

Earlier genealogy ledgers were designed to charge isolated or sequential high-frequency events by critical actions.

M5-278 upgrades the required H behavior to a stronger statement:

> if T remains quiet and the terminal Besov/mildness hypotheses survive, then the orbit cannot return infinitely often to a uniformly bounded-frequency shell state.

Therefore any attempted H-only singular scenario must support an **ever-increasing high-frequency satellite somewhere in space at every sufficiently old similarity time**.

This makes the next target more concrete:

1. localize one shell realizing `Gamma_R >> 1`;
2. separate a genuine interior high-frequency/vorticity component from cutoff/Bogovskii boundary terms;
3. show that a genuine component either dissipates on its shorter frequency time or requires order-one normalized replenishment;
4. route the replenishment to T, or extract a new active satellite/core and audit its first-hitting genealogy.

---

## 8. Scope firewall

The above conclusion uses two hypotheses beyond mere existence of H:

1. the complete ancient solution remains mild;
2. its terminal trace remains within the Albritton–Barker Besov-distance class.

On M5-276's quiet corridor these are proved automatically.

On a general H branch, if either hypothesis itself fails, that failure must be kept as an explicitly typed H/T/terminal-trace exit rather than silently assuming the Liouville theorem.

Thus M5-278 is a **sharpening of the H-only survivor under the retained complete ancient/Besov corridor**, not an unconditional closure of every possible H extraction failure.

---

## 9. Updated H frontier

Under no Campanato turnover and retained ancient/Besov coherence,

\[
\boxed{
\text{nontrivial survivor}
\Longrightarrow
\begin{cases}
\|U(\tau)\|_{L^{3,\infty}}\to\infty,\\
\sup_R E_1(R,\tau)\to\infty,\\
\sup_R\Gamma_R(\tau)\to\infty,
\end{cases}
\qquad\tau\to-\infty.
}
\]

The remaining problem is no longer to prove that high frequency occurs.  It must occur **persistently and with unbounded severity**.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
