# M16 — Kappa-space conveyor, hysteresis audit, and PDE constitutive closure

Legacy source range: `M5-677~688`
Canonical IDs from legacy: `M16-001~012`
Native canonical continuation: `M16-013+`

## Independent question
Can the mandatory CE-H curvature/replacement cycle sustain an infinite nested recharge/retirement cascade once the material `kappa` current is constrained by the actual Navier–Stokes constitutive law?

## Canonical crosswalk for legacy frontier
- M16-001 = Legacy M5-677 — zero-curvature branch linearizes NS; uniform curvature floor.
- M16-002 = Legacy M5-678 — late curvature-label amplification gate.
- M16-003 = Legacy M5-679 — physical-variable audit of curvature/flux cocycle.
- M16-004 = Legacy M5-680 — nested-flux cascade anti-shortcut model.
- M16-005 = Legacy M5-681 — `kappa`-space material-flux continuity equation.
- M16-006 = Legacy M5-682 — scalar CE-H constitutive law for `h=D_B kappa`.
- M16-007 = Legacy M5-683 — enstrophy-weighted `kappa`-space PDE current.
- M16-008 = Legacy M5-684 — vortex-line residence/enstrophy weight evolution.
- M16-009 = Legacy M5-685 — flux-weighted zero-crossing hysteresis.
- M16-010 = Legacy M5-686 — hysteresis identified as exact kinematic source balance.
- M16-011 = Legacy M5-687 — uniform nonzero `grad kappa` diffusion charge.
- M16-012 = Legacy M5-688 — exponential-`kappa` ledger and quantitative PDE payer dichotomy.

## Native canonical continuation
- M16-013 — exact collapse of the CE-H geometric remainder into strain/derivative and `kappa`--magnitude couplings; curl-gradient term cancels after integration by parts.
- M16-014 — payer floor quantized into five coherent local charges: `grad sigma`, strain residence, amplitude transition, strain/`grad W` overlap, and `grad rho`.
- M16-015 — audit correction: P1/P4/P5 are unsigned derivative occupancies dominated by palinstrophy-type activity; they do not by themselves force turnover.
- M16-016 — compact-recurrence no-go: positive unsigned event charge is compatible with recurrence unless tied to a bounded-state coboundary, finite resource debit, or signed material exit.
- M16-017 — exact CE-H material law `D_B log rho = sigma+kappa-1`, `D_B xi=0`; fixed-threshold crossing sign and finite high-amplitude material-label residence.
- M16-018 — a hysteretic upward recharge requires positive strain or positive `kappa`; positive `kappa` necessarily carries larger negative-`kappa` enstrophy-weight compensation because `int kappa rho^2 = -P`.
- M16-019 — exact infinitesimal vortex-tube triad: `D_B log rho = sigma+kappa-1`, `D_B log A = 1-sigma`, `D_B log Phi = kappa`. **Audit note:** its final inference that a separate negative-`kappa` population is mandatory was retracted in M16-020 because flux-neutral tubes may still have negative enstrophy-weighted `kappa` through covariance.
- M16-020 — correction/restoration of the measure-mismatch firewall. Tube enstrophy is `e_tube = Phi L_rho`, and a neutral-flux tube may satisfy `⟨kappa e_tube⟩<0` through negative covariance with residence/enstrophy weight. Exact residence law: `D_B log L_rho = kappa + 2 bar(sigma)_rho - 1/2`.
- M16-021 — quantitative bias split: a negative enstrophy-weighted `kappa` budget forces either strict negative current-flux bias (hence flux decay/replacement) or strict negative covariance between `kappa` and line residence `L_rho`; the latter forces a residence-variance floor.
- M16-022 — same-marker recycled active tube: bounded flux and bounded line residence give `⟨bar(sigma)_rho⟩=1/4`, while bounded recurrent marker amplitude gives `⟨sigma_marker⟩=1`; therefore either marker/sheath turnover occurs or the same tube carries positive-density axial strain heterogeneity.
- M16-023 — exact CE-H resolution of axial strain heterogeneity: `W·grad sigma = Sigma:grad W - (1/2) W·curl W`. The same-tube covariance branch therefore reduces to strain--vorticity derivative interaction or vorticity self-helicity activity, unless marker/sheath turnover already occurs.

## Corrected frontier after M16-023
The old two-population statement `S <-> D` is **not canonical** because M16-020 shows that the same flux-neutral tube population may carry the negative enstrophy-weighted `kappa` debt through phase covariance.

The retained exact branch tree is

\[
\boxed{
\text{negative enstrophy-weighted `kappa`}
\Longrightarrow
B_{\rm flux}^{-}
\ \lor\ 
T_{\rm marker/sheath}
\ \lor\ 
C_{SD}^{axial}
\ \lor\ 
C_{H_W}^{axial}.
}
\]

1. **`B_flux^-`** — the current material-flux measure itself has a strict negative `kappa` mean; fixed-label flux decays and replacement is required.
2. **`T_marker/sheath`** — the tube avoids same-marker recurrence by active-marker or sheath turnover.
3. **`C_SD^axial`** — same-tube axial strain variation is paid by the signed strain--vorticity derivative contraction `Sigma:grad W`.
4. **`C_H_W^axial`** — same-tube axial strain variation is paid by vorticity self-helicity density `W dot curl W`.

### Next target
Audit the last two same-tube PDE channels. The question is whether compact recurrent CE-H dynamics can support `C_SD^axial` or `C_H_W^axial` indefinitely without forcing one of the already established Beltrami-collapse, strain-sheet, or material-turnover mechanisms.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
