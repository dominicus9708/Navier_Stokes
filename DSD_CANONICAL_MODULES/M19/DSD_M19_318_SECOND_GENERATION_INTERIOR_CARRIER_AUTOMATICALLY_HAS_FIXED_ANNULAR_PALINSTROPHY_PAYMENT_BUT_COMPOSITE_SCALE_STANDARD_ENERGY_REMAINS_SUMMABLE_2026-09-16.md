# M19-318 — The second-generation interior carrier automatically has a fixed annular palinstrophy payment, but composite-scale standard-energy costs remain summable

**Date:** 2026-09-16  
**Status:** NEW EVENT-ANNULAR PALINSTROPHY THEOREM / LOCAL BRIDGE CLOSED / COMPOSITE-SCALE GLOBAL FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-316 reduces first-hitting/GMS physical alignment to a carrier-to-payer localization problem.

M5-478 already gives a nontrivial second-generation interior carrier at normalized time `s=-1`.

This module observes that this nontrivial local enstrophy witness alone forces a fixed whole-space palinstrophy payment on a fixed annular time interval.

No CE-H identity and no GMS epsilon floor are needed for this local result.

## 2. M5-478 interior carrier

For the second-generation record cells `Omega_m`, there exist fixed

\[
\rho_0>0,
\qquad
c_0>0,
\]

and bounded centers `y_m -> y_*` such that at `s=-1`

\[
\boxed{
\int_{B_{\rho_0}(y_*)}
|\Omega_m(y,-1)|^2dy
\ge c_0
}
\]

for all sufficiently large `m` after the retained subsequence.

The sequence converges locally smoothly on compact subsets of `s<0` to a nontrivial ancient limit.

## 3. Snapshot local enstrophy forces global palinstrophy

For every whole-space `H1` vorticity field,

\[
\|\Omega\|_6
\le C_S\|\nabla\Omega\|_2.
\]

On the fixed ball, Hölder gives

\[
\|\Omega\|_{L^2(B_{\rho_0})}
\le
|B_{\rho_0}|^{1/3}
\|\Omega\|_{L^6(B_{\rho_0})}
\le
|B_{\rho_0}|^{1/3}
\|\Omega\|_6.
\]

Therefore

\[
\|\nabla\Omega_m(-1)\|_2^2
\ge
\frac{c_0}{C_S^2|B_{\rho_0}|^{2/3}}
=:p_{snap}>0.
\]

Hence

\[
\boxed{
P_m(-1):=\|\nabla\Omega_m(-1)\|_2^2
\ge p_{snap}>0.
}
\]

This lower bound is scale-normalized and record-independent.

## 4. Uniform time thickening

The M5-478 sequence is locally smooth and converges smoothly on every compact interval around `s=-1` contained in `(-infinity,0)`.

The limiting local enstrophy

\[
E_{loc}(s)
:=
\int_{B_{\rho_0}(y_*)}|\mathcal\Omega(y,s)|^2dy
\]

is continuous and satisfies

\[
E_{loc}(-1)\ge c_0.
\]

Therefore there exists a fixed

\[
\delta>0
\]

such that

\[
E_{loc}(s)\ge\frac{3c_0}{4}
\qquad
|s+1|\le\delta.
\]

Local smooth convergence then gives, for all sufficiently large `m`,

\[
\boxed{
\int_{B_{\rho_0}(y_*)}|\Omega_m(y,s)|^2dy
\ge\frac{c_0}{2}
\qquad
|s+1|\le\delta.
}
\]

Applying Section 3 at each such time yields

\[
\|\nabla\Omega_m(s)\|_2^2
\ge p_0>0
\]

with fixed `p_0`.

Thus

\[
\boxed{
q_{P,m}
:=
\int_{-1-\delta}^{-1+\delta}
\|\nabla\Omega_m(s)\|_2^2ds
\ge
2\delta p_0
=:p_*>0.
}
\]

## 5. EVENT-ANNULAR is automatic for this payer

Choose a fixed annular record interval

\[
I=[-b,-a]\Subset(-\infty,0)
\]

with

\[
[-1-\delta,-1+\delta]\Subset I.
\]

Then the carrier palinstrophy payer occurs in the same fixed normalized annular interval in every retained second-generation record.

Therefore

\[
\boxed{
\text{M5-478 interior carrier}
\Longrightarrow
\text{EVENT-ANNULAR palinstrophy payer}
}
\]

for this specific payer.

This closes the generic event-relocation gap of M18-038 for the interior-carrier palinstrophy charge.

## 6. No GMS floor is needed for the local payer

The proof used only

1. M5-478 interior local-enstrophy nontriviality;
2. whole-space homogeneous Sobolev;
3. local smooth compactness/time continuity.

Thus the palinstrophy payer exists independently of whether the M19-254 GMS floor is assigned to the same local carrier.

The GMS route and the carrier-payer route therefore meet at palinstrophy but are logically distinct.

## 7. Lower-order descent is locally available

M18-056 applies cellwise Sobolev log-convexity:

\[
q_0\ge\frac{q_P^2}{q_H},
\qquad
q_0\ge\frac{q_P^{3/2}}{q_{D3}^{1/2}}.
\]

Since `q_P >= p_*`, the carrier event either descends toward standard-energy/spacetime-enstrophy or forces quantitative higher-derivative escalation.

M18-057 then routes sufficiently strong H/D3 escalation out of the compact controlled core into derivative-tail / remote / critical / local-compactness exits.

These remain useful local structural reductions.

## 8. Composite-scale global firewall

M18-058 shows that the first-hitting and second-generation scales compose as

\[
\boxed{
\rho_{j,m}=r_jR_m=r_{j-m}.
}
\]

For the standard-energy/spacetime-enstrophy charge `q_0`, the original physical cost is

\[
\boxed{
q_{0,jm}^{phys}
=
r_{j-m}
q_{0,jm}^{(2)}.
}
\]

Therefore one fixed normalized standard-energy payment per chronological first-hitting generation costs only

\[
O(r_n)
\]

in the original solution.

Since

\[
\sum_nr_n<\infty,
\]

fixed recordwise descent remains compatible with finite original kinetic-energy dissipation.

Hence

\[
\boxed{
\text{EVENT-ANNULAR palinstrophy payer}
+\text{cellwise lower-order descent}
\not\Rightarrow
\text{global finite-energy contradiction}.
}
\]

## 9. What has genuinely improved

The following gap is now closed for the selected interior carrier:

\[
\boxed{
\text{specific payer event placement in a fixed record annulus}.
}
\]

The remaining global problem is no longer event relocation for this payer.

It is the composite-budget problem:

\[
\boxed{
\text{how can the fixed local payer acquire a nonsummable original-parent cost?}
}
\]

Possible mechanisms are

- normalized payer growth with chronological scale;
- prolonged dwell/residence;
- independent same-scale multiplicity beyond the compact O(1) bound;
- signed/monotone/rigidity structure;
- a genuinely fixed finite parent not canceled by the shrinking first-hitting base;
- routing to remote/critical/Type-II exits.

## 10. Revised interpretation of M19-317

M19-317 correctly identifies that order-one record multiplicity cannot defeat the inverse-record palinstrophy ledger.

M19-318 adds that for the canonical interior carrier, one does not need to search for a palinstrophy payer: it is automatic.

Thus future work should not spend effort re-proving `q_P >= p_*` on that carrier.

The high-value question is the **global cost amplification / rigidity of that already-certified payer**.

## 11. Verdict

A fixed EVENT-ANNULAR palinstrophy payment is now certified on every sufficiently late retained second-generation interior carrier.

This is a real local advance.

But M18-058's composite-scale firewall remains decisive: fixed normalized payments are still geometrically summable in the original physical solution.

---

\[
\boxed{\text{M19-318 COMPLETE; INTERIOR-CARRIER PALINSTROPHY LOCALIZATION IS CLOSED, BUT GLOBAL COMPOSITE-SCALE SUMMABILITY REMAINS OPEN.}}
\]