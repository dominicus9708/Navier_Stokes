# DSD Deep Audit — Feinstein Restricted NSE-Native Carleson / VACM

Date: 2026-09-06
Source family: Ira Feinstein, *Global Regularity for 3D Navier–Stokes via Restricted, NSE-Native Carleson Control at the Active Scale* / related restricted-Carleson VACM records.

## Status

**FAIL_ROOT for the publicly displayed theorem chain.**

This status is argument/version-specific. It does not classify the author or invalidate every microlocal lemma in the program.

---

## Public chain

The public paper defines

\[
U_j:=P_{e,j}\Delta_j u,\qquad E_j:=\|U_j\|_2^2,
\]

and states a global ledger of the form

\[
\mathcal F(t)=\sum_j 2^{3j/2}\|U_j(t)\|_2
\sim \|\omega(t)\|_{B^0_{\infty,1}},
\]

followed by

\[
\|\omega\|_{L^\infty}\lesssim \mathcal F(t)
\]

and BKM continuation.

It also states pseudo-commutator estimates

\[
\|[\Delta,P_{e,j}]f\|_2
\le C\varepsilon_j 2^{2j}\|f\|_2,
\]

\[
\|[u\cdot\nabla,P_{e,j}]f\|_2
\le C\varepsilon_j\|\nabla u\|_{\mathrm{BMO}}\|f\|_2,
\]

where

\[
\varepsilon_j=\alpha_j^{-1}\varepsilon_0+\alpha_j^{-2}\varepsilon_0^2,
\]

then claims that the single condition

\[
C\varepsilon_j\le \nu/2
\]

absorbs **both** commutators into

\[
\frac12\nu 2^{2j}E_j.
\]

---

# Root failure 1 — one spatial derivative is missing in the BKM endpoint ledger

From the definition, \(U_j\) is a conically selected piece of the **velocity** shell, not the vorticity shell.

Standard Bernstein gives

\[
\|\Delta_j\omega\|_\infty
\lesssim 2^{3j/2}\|\Delta_j\omega\|_2.
\]

Since

\[
\omega=\nabla\times u,
\]

on a dyadic shell

\[
\|\Delta_j\omega\|_2\asymp 2^j\|\Delta_j u\|_2.
\]

Therefore the quantity naturally controlling \(B^0_{\infty,1}\) vorticity is

\[
\boxed{
\sum_j 2^{5j/2}\|\Delta_j u\|_2,
}
\]

up to packet completeness/equivalence constants, not

\[
\sum_j2^{3j/2}\|U_j\|_2.
\]

Thus the displayed equivalence

\[
\mathcal F\sim\|\omega\|_{B^0_{\infty,1}}
\]

and the following conic Bernstein step

\[
\|\omega\|_\infty\lesssim\mathcal F
\]

are missing one derivative \(2^j\).

This is not a constants issue. It changes the regularity level of the controlled norm.

## Consequence

Even if the CLI inequality for the displayed \(\mathcal F\) were correct, it would not by itself yield the BKM endpoint asserted in Theorem 7.1.

---

# Root failure 2 — the transport commutator is absorbed without its BMO factor

The public theorem states

\[
\|[u\cdot\nabla,P_{e,j}]f\|_2
\le C\varepsilon_j\|\nabla u\|_{\mathrm{BMO}}\|f\|_2.
\]

Pairing with \(U_j\) yields a cost of size

\[
C\varepsilon_j\|\nabla u\|_{\mathrm{BMO}}E_j.
\]

To absorb this into dyadic viscous dissipation

\[
\nu2^{2j}E_j,
\]

one needs

\[
\boxed{
C\varepsilon_j\|\nabla u\|_{\mathrm{BMO}}
\lesssim \nu2^{2j}.
}
\]

However Corollary 6.1 publicly assumes only

\[
C\varepsilon_j\le\nu/2,
\]

which is sufficient for the Laplacian commutator but does **not** imply the required transport absorption unless an additional estimate such as

\[
\|\nabla u\|_{\mathrm{BMO}}\lesssim 2^{2j}
\]

is independently proved on the same active slab.

No such condition is part of the displayed corollary.

Hence the advertised scale-wise absorption does not follow from the preceding theorem as written.

---

# Additional audit concern — good patch is itself a local smallness/gap regime

The paper states a standing good-patch assumption containing localized vorticity smallness and a spectral-gap lower bound. The restricted Carleson and VACM bounds are then derived on that good region.

This is potentially useful conditionally, but unconditional global continuation still requires an exhaustive treatment of the complement:

- high localized enstrophy;
- small/degenerate eigen-gap;
- packet/interface leakage;
- low-high and high-high-to-low interactions;
- transition between good and bad slabs.

The two root failures above already break the public theorem chain before this completeness issue needs to be settled.

---

# Survivors worth retaining

The following ideas should **not** be discarded merely because the final chain fails:

1. heat-mollified strain eigenframes;
2. explicit gap-weighted projector derivative estimate
   \[
   \|\nabla P_1\|\lesssim \|\nabla S_r\|/\operatorname{gap}(S_r);
   \]
3. restricted rather than global Carleson control;
4. variable-axis conic packetization;
5. explicit separation of high-low and high-high bilinear regimes.

These remain relevant comparison tools for M17's director/spectral branch.

---

# Regression tests exported to M17

## VACM-R1 — endpoint derivative count

Whenever a packet functional is exported to vorticity \(L^\infty\) or BKM, count the derivative explicitly:

\[
\omega_j\sim 2^j u_j.
\]

No packet geometry may silently remove this factor.

## VACM-R2 — commutator absorption must retain coefficient amplitude

If

\[
\|[A,P_j]f\|\le \varepsilon_j M_j\|f\|,
\]

then viscosity absorbs it only if

\[
\varepsilon_jM_j\lesssim \nu2^{2j},
\]

not merely \(\varepsilon_j\ll1\).

This is directly relevant to M17-300/301 growing-lag spectral leakage: coefficient size and packet geometry must remain separate currencies.

---

## Final audit verdict

\[
\boxed{
\text{public restricted-Carleson/VACM proof chain}
\;\textbf{does not establish unconditional 3D NSE regularity as written.}
}
\]

Two independent displayed bridges fail before the final BKM step:

1. a missing dyadic derivative in the vorticity endpoint ledger;
2. missing \(\|\nabla u\|_{\mathrm{BMO}}\) in the transport-commutator absorption condition.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
