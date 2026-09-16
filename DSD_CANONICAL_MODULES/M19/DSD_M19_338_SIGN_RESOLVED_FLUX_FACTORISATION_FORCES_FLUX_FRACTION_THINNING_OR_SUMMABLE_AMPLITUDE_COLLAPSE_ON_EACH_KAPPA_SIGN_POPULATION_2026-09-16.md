# DSD M19-338 — Sign-resolved flux factorization forces flux-fraction thinning or summable amplitude collapse on each kappa-sign population

Date: 2026-09-16  
Canonical ID: **M19-338**

Status: **ACTIVE SIGN-RESOLVED FLUX CURRENCY / AMPLITUDE-COLLAPSE REFINEMENT / MIXED-SIGN SURVIVOR CLASSIFICATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

Work on the regular positive-orientation material-flux family of M17-440 and M19-337 at one retained record.

Let

\[
dp_\Phi=\frac{d\Phi}{\Phi}
\]

be the positive flux probability, and let

\[
q:=r^2\rho\ge0
\]

be the own-scale normalized vorticity amplitude used by M17-440.

The total flux-weighted normalized amplitude is

\[
\boxed{
\mathfrak a_\Phi
=\int q\,dp_\Phi
=\frac{\mathfrak Q_\Phi}{\Phi}.
}
\]

M17-441 proves, on representation-safe geometric records with retained good-time density and positive total flux floor,

\[
\boxed{
\sum_m\mathfrak a_{\Phi,m}<\infty.
}
\]

The present module resolves this nonnegative currency by coefficient sign.

## 2. Sign-resolved flux fractions

Define the coefficient sign sectors

\[
S_+:=\{\kappa>0\},
\qquad
S_-:=\{\kappa<0\},
\qquad
S_0:=\{\kappa=0\}.
\]

Their positive flux fractions are

\[
\boxed{
\eta_+:=p_\Phi(S_+),
\qquad
\eta_-:=p_\Phi(S_-),
\qquad
\eta_0:=p_\Phi(S_0),
}
\]

with

\[
\eta_++\eta_-+\eta_0=1.
\]

Whenever \(\eta_\pm>0\), define the sign-resolved flux-weighted normalized amplitudes

\[
\boxed{
\mathfrak a_+
:=\frac1{\eta_+}\int_{S_+}q\,dp_\Phi,
\qquad
\mathfrak a_-
:=\frac1{\eta_-}\int_{S_-}q\,dp_\Phi.
}
\]

Likewise define \(\mathfrak a_0\) if \(\eta_0>0\).

## 3. Exact sign factorization

Since the sign sectors partition the family,

\[
\boxed{
\mathfrak a_\Phi
=
\eta_+\mathfrak a_+
+
\eta_-\mathfrak a_-
+
\eta_0\mathfrak a_0.
}
\]

Equivalently the M17-440 quadratic currency splits as

\[
\boxed{
\mathfrak Q_\Phi
=
\Phi_+\mathfrak a_+
+
\Phi_-\mathfrak a_-
+
\Phi_0\mathfrak a_0,
}
\]

where \(\Phi_s=\eta_s\Phi\).

Every term is nonnegative.

## 4. Ancestral summability resolves by sign

M17-441 gives

\[
\sum_m\mathfrak a_{\Phi,m}<\infty.
\]

By the nonnegative decomposition,

\[
\boxed{
\sum_m\eta_{+,m}\mathfrak a_{+,m}<\infty,
\qquad
\sum_m\eta_{-,m}\mathfrak a_{-,m}<\infty,
}
\]

and similarly for the zero sector.

Thus the two signs cannot jointly retain both a fixed positive flux fraction and a fixed positive normalized amplitude on infinitely many positive-density representation-safe records.

## 5. Fixed sign-flux occupancy forces sign-resolved amplitude collapse

Suppose M19-337 transfers the mixed-sign line populations into material-flux populations with

\[
\eta_{+,m}\ge\eta_*>0,
\qquad
\eta_{-,m}\ge\eta_*>0
\]

on the retained record sequence.

Then

\[
\boxed{
\sum_m\mathfrak a_{+,m}<\infty,
\qquad
\sum_m\mathfrak a_{-,m}<\infty.
}
\]

In particular

\[
\boxed{
\mathfrak a_{+,m}\to0,
\qquad
\mathfrak a_{-,m}\to0.
}
\]

Therefore genuine persistent mixed-sign flux occupancy does not avoid the M17-441 collapse. It strengthens it: **both coefficient signs must move their flux into vanishing normalized-amplitude classes.**

## 6. Fixed sign-resolved amplitude instead forces flux thinning

Conversely, if for one sign

\[
\mathfrak a_{+,m}\ge a_*>0
\]

on a retained subsequence, then

\[
\sum_m\eta_{+,m}<\infty
\]

on that subsequence.

Likewise

\[
\mathfrak a_{-,m}\ge a_*>0
\Longrightarrow
\sum_m\eta_{-,m}<\infty.
\]

Thus every sign population obeys the exact alternative

\[
\boxed{
\text{sign-flux fraction thinning}
\quad\lor\quad
\text{sign-resolved normalized-amplitude collapse}.
}
\]

The primary currency is their product \(\eta_\pm\mathfrak a_\pm\).

## 7. Relation to the quadratic-payer probability

M17-442 defines

\[
d\widehat p
:=
\frac{q\,dp_\Phi}{\mathfrak a_\Phi}.
\]

Let

\[
\widehat\eta_\pm:=\widehat p(S_\pm).
\]

Then exactly

\[
\boxed{
\widehat\eta_+
=
\frac{\eta_+\mathfrak a_+}{\mathfrak a_\Phi},
\qquad
\widehat\eta_-
=
\frac{\eta_-\mathfrak a_-}{\mathfrak a_\Phi}.
}
\]

This formula explains an important survivor: a sign population may retain a fixed fraction of the **quadratic/enstrophy payer measure** even while its absolute material-flux currency

\[
\eta_\pm\mathfrak a_\pm
\]

collapses together with \(\mathfrak a_\Phi\).

Hence positive weighted coefficient heterogeneity is fully compatible with global amplitude collapse. There is no contradiction from the normalized sign fractions alone.

## 8. Quantitative measure-mismatch firewall

Assume a normalized amplitude ceiling

\[
q\le q_*<\infty.
\]

If

\[
\widehat\eta_+\ge c_*>0,
\]

then

\[
c_*\mathfrak a_\Phi
\le
\eta_+\mathfrak a_+
\le
q_*\eta_+.
\]

Therefore only

\[
\boxed{
\eta_+
\ge
\frac{c_*}{q_*}\mathfrak a_\Phi
}
\]

is forced without further amplitude comparability.

Since \(\mathfrak a_\Phi\to0\) summably on the M17-441 survivor, this lower bound itself may vanish.

Thus

\[
\boxed{
\text{fixed payer/enstrophy fraction}
\not\Rightarrow
\text{fixed material-flux fraction}
}
\]

unless an additional Radon--Nikodym/amplitude-residence comparability theorem is supplied. This is consistent with M19-337.

## 9. Combined M19-337--338 branch split

The productive mixed-sign spatial branch now has the quantitative refinement

\[
\boxed{
\begin{aligned}
H_{\rm mixed\text{-}sign\ coefficient\ population}
\Longrightarrow{}&
G_{\rm line\text{-}residence\ segregation}\\
&\lor G_{\rm positive/negative\ flux\text{-}fraction\ thinning}\\
&\lor G_{\rm simultaneous\ sign\text{-}resolved\ amplitude\ collapse}\\
&\lor G_{\rm cross\text{-}section/representation/genealogy\ loss}.
\end{aligned}
}
\]

The third branch is not an unnamed geometric dilution. By M17-442 it has an exact dynamical decomposition into strain action and coefficient/amplitude flux-measure redistribution.

## 10. Strategic consequence

The spatial mixed-sign branch no longer suggests that a long zero sheet alone should close the proof. The correct scale-invariant survivor is a **measure-reweighting architecture**:

\[
\boxed{
\text{coefficient heterogeneity survives}
\quad\text{while}
\quad
\eta_\pm\mathfrak a_\pm
\text{ becomes summable.}
}
\]

The next calculation should differentiate the sign-resolved flux currencies. Because the sign sectors move with \(\kappa\), their evolution acquires an explicit zero-level transfer current. This is the natural bridge between M17-442 amplitude redistribution and M17-459 zero-current architecture.

## 11. Audit verdict

**PASS — the mixed-sign positive-flux branch is reduced to sign-resolved flux thinning/amplitude collapse plus residence/representation exits.**

Retained positive fractions of both signs force simultaneous summable amplitude collapse. Retained amplitudes instead force summable sign-flux occupation. Positive enstrophy/payer fractions alone do not remove this firewall.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
