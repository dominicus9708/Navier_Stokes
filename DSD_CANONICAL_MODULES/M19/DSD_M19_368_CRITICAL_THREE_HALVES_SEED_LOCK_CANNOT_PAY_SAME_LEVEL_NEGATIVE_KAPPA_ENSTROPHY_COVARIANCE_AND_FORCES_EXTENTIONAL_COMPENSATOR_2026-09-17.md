# DSD M19-368 — Critical three-halves seed lock cannot pay same-level negative kappa–enstrophy covariance and forces an extensional compensator

Date: 2026-09-17  
Canonical ID: **M19-368**

Status: **ACTIVE PHASE-SEPARATION THEOREM / CRITICAL-SEED COMPRESSION VERSUS STRETCHING-SURPLUS COMPENSATOR / CONDITIONAL QUANTITATIVE LOWER BOUND**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

M19-365 gives the compact critical-seed lock

\[
(\bar\kappa,\bar\sigma)\to\left(\frac32,-\frac12\right).
\]

M5-632 gives, for a recurrent integrable material-tube ensemble with tube enstrophy weight \(e\),

\[
\boxed{
\langle \kappa e\rangle
=-\left\langle\left(\sigma-\frac14\right)e\right\rangle.
}
\]

Hence the same-level negative kappa–enstrophy covariance branch

\[
\langle\kappa e\rangle<0
\]

is equivalent to the positive weighted stretching-surplus condition

\[
\boxed{
\left\langle\left(\sigma-\frac14\right)e\right\rangle>0.
}
\]

## 2. Sign of the critical seed contribution

On a locked critical seed phase,

\[
\sigma\approx-\frac12.
\]

Therefore

\[
\boxed{
\sigma-\frac14\approx-\frac34<0.
}
\]

The critical seed contributes negatively to the stretching-surplus ledger:

\[
\boxed{
\left(\sigma-\frac14\right)e
\approx-\frac34e.
}
\]

Thus a critical seed cannot by itself pay the positive stretching surplus required for same-level negative kappa–enstrophy covariance.

## 3. Robust locked-set estimate

Fix \(0<\varepsilon<3/4\), and define a critical locked event set \(C\) on which

\[
\sigma\le-\frac12+\varepsilon.
\]

Then on \(C\),

\[
\sigma-\frac14
\le
-\left(\frac34-\varepsilon\right).
\]

Hence

\[
\boxed{
\int_C\left(\sigma-\frac14\right)e
\le
-\left(\frac34-\varepsilon\right)\int_C e.
}
\]

If the full recurrent same-level ensemble has positive surplus

\[
\left\langle\left(\sigma-\frac14\right)e\right\rangle=S_*>0,
\]

then the complement must satisfy

\[
\boxed{
\left\langle 1_{C^c}
\left(\sigma-\frac14\right)e\right\rangle
\ge
S_*
+
\left(\frac34-\varepsilon\right)
\langle1_Ce\rangle.
}
\]

Thus critical-seed occupation strengthens rather than weakens the required compensating positive stretching.

## 4. Extensional phase is necessary

The integrand

\[
\left(\sigma-\frac14\right)e
\]

is nonpositive whenever

\[
\sigma\le\frac14.
\]

Therefore any positive total surplus requires a set of positive enstrophy-time measure on which

\[
\boxed{
\sigma>\frac14.
}
\]

Hence the recurrent same-level covariance branch with a positive-density critical seed phase has a genuine two-phase strain architecture:

\[
\boxed{
\text{critical compressive phase }\sigma\approx-\frac12
\quad+\quad
\text{extensional compensator }\sigma>\frac14.
}
\]

## 5. Quantitative mass lower bound under compact strain cap

Assume the retained compact branch has

\[
\sigma\le S_{max}<\infty.
\]

Let

\[
E_C:=\langle1_Ce\rangle
\]

and

\[
E_+:=\left\langle1_{\{\sigma>1/4\}}e\right\rangle.
\]

Since on the positive set

\[
\sigma-\frac14\le S_{max}-\frac14,
\]

we obtain

\[
\boxed{
E_+
\ge
\frac{
S_*+(3/4-\varepsilon)E_C
}{S_{max}-1/4}.
}
\]

Thus any fixed positive enstrophy-time mass of critical seeds forces a fixed positive enstrophy-time mass of extensional compensators, provided the strain remains uniformly capped.

## 6. Curvature consequence on the compensator

M5-621 gives

\[
D_B\log|\mathcal K|=-\sigma-\frac12.
\]

On the extensional compensator \(\sigma>1/4\),

\[
\boxed{
D_B\log|\mathcal K|<-rac34.
}
\]

Thus the compensating phase has strict material curvature decay at rate at least \(3/4\) while it persists.

Therefore the two phases have sharply different geometric roles:

- critical seed phase: \(\sigma\approx-1/2\), curvature approximately neutral, transverse area inflates;
- extensional compensator: \(\sigma>1/4\), curvature decays strictly and longitudinal material length grows.

## 7. Consequence for renewal

A positive-density sequence of critical seed activations cannot be supported solely by the locked seed population if the recurrent Rayleigh budget is paid through same-level covariance.

It requires repeated access to an extensional compensator population whose material curvature is being depleted.

Hence the covariance route is converted into a **curvature-renewal demand**:

\[
\boxed{
G_{same-level\ covariance}
+
G_{critical\ seed}^{3/2}
\Longrightarrow
G_{extensional\ curvature\ depletion}
+
G_{renewal/turnover}.
}
\]

This rejoins the M19-358--365 renewal architecture from a different exact ledger.

## 8. Firewall

The result does not prove that the extensional compensator is the same material label as the critical seed, nor that curvature depletion is globally nonrecyclable. Population exchange, label turnover, and projective/genealogy resets remain explicit exits.

The statement is an invariant weighted phase-separation result, not a global contradiction.

## 9. New target

The next high-value theorem gate is

\[
\boxed{
\mathcal T_{comp}^{curv}:
\text{determine whether the extensional compensator required by M19-368 can be recycled at positive density without exhausting a finite material-curvature/turnover resource.}
}
\]

This should be compared with M5-621 curvature strict cocycle, M5-488 finite-memory storage, and M19-358--364 renewal resets.

## 10. Audit verdict

**PASS — critical seeds and same-level covariance cannot be the same self-sufficient phase.**

The critical \((3/2,-1/2)\) seed lock contributes the wrong sign to the stretching-surplus ledger. A recurrent covariance payer therefore requires a separate positive-mass extensional strain phase, which in turn pays strict curvature decay and recreates a renewal/turnover requirement.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
