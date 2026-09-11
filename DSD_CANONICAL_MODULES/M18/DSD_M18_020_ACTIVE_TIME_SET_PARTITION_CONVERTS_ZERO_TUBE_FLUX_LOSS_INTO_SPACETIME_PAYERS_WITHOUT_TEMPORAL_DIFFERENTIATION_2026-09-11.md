# M18-020 — Active-time-set partition converts zero-tube flux loss into spacetime payers without temporal differentiation

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / TEMPORAL-MEASURE REDUCTION / NO-D5 FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase provenance

This is the first newly numbered module after the M17-to-M18 phase split.

The direct inputs are:

- M18-019 (legacy M17-485): half-flux spatial trichotomy;
- M18-006 (legacy M17-475): raw-H2 endpoint temporal thickening when its hypotheses hold;
- M18-004 (legacy M17-473): ancestry divergence thresholds;
- the existing M17-445 first-coefficient-jet/D3 ancestry ledger.

The purpose is to answer a DSD audit question left open by M18-019:

> Must each snapshot payer be differentiated in time in order to obtain a spacetime payment?

The answer is **no**. If the flux-loss event itself occupies a positive set of normalized times, a measurable time-set partition converts the pointwise trichotomy directly into a spacetime payment. This avoids differentiating the coefficient-gradient or second-jet charges and therefore avoids an artificial escalation toward D5.

## 2. Snapshot input from M18-019

At one time, assume a regular coefficient tube and a half-flux drop

\[
F(\ell,t)=\frac12J(t),
\qquad
J(t):=F(0,t)>0.
\]

Let

\[
G(t):=\int_{T_\ell(t)}\rho^2|\nabla\kappa|^2dx,
\]

\[
P(t):=\int_{T_\ell(t)}|\nabla\Omega|^2dx,
\]

\[
S(t):=\int_{T_\ell(t)}\rho^2|\Delta\kappa|^2dx.
\]

If the regular-gradient floor is

\[
|\nabla\kappa|\ge g_*(t)>0
\]

on the relevant tube and the retained coefficient width is \(\delta(t)>0\), M18-019 gives the representation-safe trichotomy

\[
\boxed{
G(t)>J(t)\delta(t)
}
\]

or

\[
\boxed{
P(t)>\frac{J(t)}{64\delta(t)}
}
\]

or

\[
\boxed{
S(t)\ge
\frac{g_*(t)^2J(t)}{16\delta(t)}.
}
\]

Failure of the gradient floor exits through the already-separated critical-level branch and is not hidden inside the present theorem.

## 3. Compact active-time set

Fix a normalized record interval \(I\). Define the active half-flux-loss time set

\[
\mathcal A
:=
\left\{
 t\in I:
\begin{array}{l}
F(\ell(t),t)=J(t)/2,\\
J(t)\ge j_*>0,\\
\delta_*\le\delta(t)\le\delta^*,\\
g_*(t)\ge g_0>0
\end{array}
\right\}.
\]

Here \(j_*\), \(\delta_*\), \(\delta^*\), and \(g_0\) are record-uniform normalized compactness constants.

No assumption is made that \(\mathcal A\) is a single interval. It may be disconnected, intermittent, or highly fragmented in time. Only its Lebesgue measure matters.

Let

\[
\tau:=|\mathcal A|.
\]

## 4. Measurable payer partition

Define the disjoint priority partition

\[
\mathcal A_G
:=
\{t\in\mathcal A:G(t)>J(t)\delta(t)\},
\]

\[
\mathcal A_P
:=
\left\{t\in\mathcal A\setminus\mathcal A_G:
P(t)>\frac{J(t)}{64\delta(t)}
\right\},
\]

and

\[
\mathcal A_S
:=
\mathcal A\setminus(\mathcal A_G\cup\mathcal A_P).
\]

By M18-019, every time in \(\mathcal A_S\) obeys the second-jet lower bound. Hence

\[
\boxed{
\mathcal A
=
\mathcal A_G\sqcup\mathcal A_P\sqcup\mathcal A_S.
}
\]

Therefore at least one set has measure at least \(\tau/3\).

## 5. Direct spacetime payment

On \(\mathcal A_G\), compactness gives

\[
G(t)>J(t)\delta(t)
\ge j_*\delta_*.
\]

Thus

\[
\boxed{
\int_I G(t)dt
\ge
j_*\delta_*|\mathcal A_G|.
}
\]

On \(\mathcal A_P\),

\[
P(t)>
\frac{J(t)}{64\delta(t)}
\ge
\frac{j_*}{64\delta^*},
\]

so

\[
\boxed{
\int_I P(t)dt
\ge
\frac{j_*}{64\delta^*}|\mathcal A_P|.
}
\]

On \(\mathcal A_S\),

\[
S(t)
\ge
\frac{g_*(t)^2J(t)}{16\delta(t)}
\ge
\frac{g_0^2j_*}{16\delta^*},
\]

hence

\[
\boxed{
\int_I S(t)dt
\ge
\frac{g_0^2j_*}{16\delta^*}|\mathcal A_S|.
}
\]

Since one payer set has measure at least \(\tau/3\), we obtain the active-time theorem:

\[
\boxed{
\begin{aligned}
|\mathcal A|=\tau>0
\Longrightarrow{}&
\int_I Gdt
\ge
\frac{j_*\delta_*}{3}\tau\\
&\lor
\int_I Pdt
\ge
\frac{j_*}{192\delta^*}\tau\\
&\lor
\int_I Sdt
\ge
\frac{g_0^2j_*}{48\delta^*}\tau.
\end{aligned}
}
\]

This conclusion uses no time derivative of \(G\), \(P\), \(S\), or \(J\).

## 6. Why this is preferable to differentiating the payer

A direct attempt to prove persistence by differentiating

\[
G(t)=\int_{T_\ell(t)}\rho^2|\nabla\kappa|^2dx
\]

must differentiate both the moving coefficient tube and \(\nabla\kappa\). This introduces \(\partial_t\nabla\kappa\) and boundary-transport terms. Through the CE-H coefficient identities, such a route risks climbing above the already-certified D3 resource.

For

\[
S(t)=\int_{T_\ell(t)}\rho^2|\Delta\kappa|^2dx,
\]

the danger is worse: temporal differentiation naturally reaches derivatives above the D4 level already isolated in M18-019.

The active-set argument avoids that escalation entirely. It asks only whether the **event** occupies positive normalized time measure.

Hence

\[
\boxed{
\text{temporal measure of the event is sufficient; payer-by-payer temporal smoothness is unnecessary.}
}
\]

## 7. Representation and ancestry classes

The snapshot scalings are

\[
G_R=R^7G,
\qquad
P_R=R^3P,
\qquad
S_R=R^9S.
\]

After time integration,

\[
\int G_Rds=R^5\int Gdt,
\]

\[
\int P_Rds=R\int Pdt,
\]

\[
\int S_Rds=R^7\int Sdt.
\]

Therefore the corresponding ancestry weights are

\[
\boxed{R^{-5},\qquad R^{-1},\qquad R^{-7}.}
\]

These match, respectively,

- the M17-445 first-coefficient-jet/D3 ledger;
- the standard palinstrophy ledger;
- the M18-019 second-coefficient-jet/D4 scaling prediction.

Thus the active-time conversion preserves the established derivative-order ancestry hierarchy.

## 8. Record-sequence consequence

For record \(m\), let

\[
\tau_m:=|\mathcal A_m|.
\]

Under uniform normalized compactness, every active record pays at least one of

\[
Q_m^{G}\gtrsim \tau_m,
\qquad
Q_m^{P}\gtrsim \tau_m,
\qquad
Q_m^{S}\gtrsim \tau_m.
\]

Consequently, along an infinite sequence of active records, a finite-label pigeonhole argument supplies an infinite subsequence on which the same payer type occurs.

However, this does **not** by itself close the global contradiction. The exact ancestry tests remain

\[
\boxed{
\sum_mR_m^{-5}Q_m^G=\infty,
}
\]

or

\[
\boxed{
\sum_mR_m^{-1}Q_m^P=\infty,
}
\]

or

\[
\boxed{
\sum_mR_m^{-7}Q_m^S=\infty.
}
\]

For geometric \(R_m\), a fixed positive normalized duration \(\tau_m\sim1\) is still summable in all three classes. Therefore active-time thickness solves the **snapshot-to-spacetime** problem but not the later **ancestry-divergence** problem.

This distinction is mandatory.

## 9. Priority ordering supplied by the ancestry audit

Among the three payer classes, palinstrophy carries the weakest ancestry penalty:

\[
R^{-1}
\quad\text{versus}\quad
R^{-5}
\quad\text{and}\quad
R^{-7}.
\]

Therefore, from the viewpoint of a future contradiction, the preferred reduction order is

\[
\boxed{
\text{palinstrophy}
\;\succ\;
\text{first coefficient jet/D3}
\;\succ\;
\text{second coefficient jet/D4}.
}
\]

This is not a claim that one branch is mathematically more likely. It is a DSD resource-ordering statement: the palinstrophy branch requires the least growth/multiplicity/duration to defeat ancestry summability.

## 10. Exact remaining temporal exit

The theorem applies only through the measure \(\tau_m\). If a record contains a selected snapshot with strong zero-tube flux loss but

\[
\boxed{
\tau_m\to0,
}
\]

then the event can evade the spacetime payment by temporal concentration.

This is now the precise remaining temporal branch:

\[
\boxed{
G_{\rm zero\text{-}tube\ flux\ loss}
\Longrightarrow
G_{\rm spacetime\ payer}
\lor
G_{\rm active\text{-}time\ thinning}
\lor
G_{\rm critical/geometry/domain/genealogy\ loss}.
}
\]

The key improvement over M18-019 is that **temporal thinning is attached to the event set itself**, not separately to each of the three payer currencies.

## 11. DSD audit verdict

### Certified here

1. Positive active-time measure directly creates a spacetime payment.
2. No temporal differentiation of \(G\), \(P\), or \(S\) is needed.
3. The argument does not climb to D5 merely to thicken the D4 branch.
4. The ancestry weights remain exactly \(R^{-5}\), \(R^{-1}\), and \(R^{-7}\).
5. The only snapshot-to-spacetime escape inside the compact regular-tube family is collapse of the active event's time measure.

### Not certified here

1. A lower bound on \(\tau_m\) from one selected time.
2. Divergence of any ancestry sum.
3. Control of critical-level degeneration.
4. Global 3D Navier--Stokes regularity.

## 12. Next analysis target

The next useful question is not to differentiate all three payers. It is narrower:

> Can the active-time measure \(\tau_m\) collapse arbitrarily fast while a normalized half-flux-loss snapshot and the compact tube constants remain nondegenerate?

A successful lower bound on \(\tau_m\), or an exact classification of the mechanism forcing \(\tau_m\to0\), would complete the local snapshot-to-spacetime analysis of this zero-tube branch before returning to the ancestry-divergence problem.
