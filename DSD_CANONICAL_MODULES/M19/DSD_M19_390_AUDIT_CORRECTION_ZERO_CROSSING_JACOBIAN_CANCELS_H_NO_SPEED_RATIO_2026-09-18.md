# M19-390 — Audit correction: zero-crossing Jacobian cancels h, so M19-389 needs no equal-speed assumption

Date: 2026-09-18

Status: **AUDIT CORRECTION / M19-389'S MAIN QUARTER-STRAIN PHASE INEQUALITY IS VALID, BUT ONE SENTENCE IN SECTION 3 INCORRECTLY SUGGESTED AN EXTRA CROSSING-SPEED RATIO FOR UNEQUAL `|h|`. IN THE TIME-INTEGRATED ZERO-LEVEL CURRENT THE FACTOR `h delta(kappa)` GIVES `h/|h|` AT EACH REGULAR CROSSING, SO THE COAREA JACOBIAN CANCELS THE CROSSING SPEED EXACTLY. THEREFORE THE PAIR CURRENT IS PROPORTIONAL TO THE SIGNED CROSSING WEIGHTS WITH NO `|h|` RATIO, AND THE M19-389 CONDITION `J_+ <= -2 I_+` HOLDS FOR ARBITRARY REGULAR UPWARD/DOWNWARD CROSSING SPEEDS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular crossing identity

Let \(\theta_*\) be a regular zero crossing of one material label:

\[
\kappa(\theta_*)=0,
\qquad
h(\theta_*)=\kappa'(\theta_*)\ne0.
\]

For any continuous crossing weight \(W_c(\theta)\),

\[
\int h(\theta)\,\delta(\kappa(\theta))\,W_c(\theta)\,d\theta
=
\sum_{\theta_*:\kappa=0}
\frac{h(\theta_*)}{|h(\theta_*)|}
W_c(\theta_*).
\]

Hence

\[
\boxed{
\int h\,\delta(\kappa)W_c\,d\theta
=
\sum_{\rm crossings}\operatorname{sgn}(h_*)W_c(\theta_*).
}
\]

The crossing speed magnitude cancels exactly.

---

## 2. Apply to material-flux current

For the current-flux measure the crossing weight is \(W_c=\Phi\).

One upward crossing followed by one downward crossing therefore contributes

\[
\boxed{
\Phi_u-\Phi_d.
}
\]

No equality of \(|h_u|\) and \(|h_d|\) is required.

---

## 3. Apply to residence-weighted spatial current

For the line-residence weighted current the crossing weight is

\[
W_c=\Phi L_\rho.
\]

The same pair contributes

\[
\boxed{
\Phi_uL_u-\Phi_dL_d.
}
\]

again without any crossing-speed ratio.

Therefore cancellation/reversal requires exactly

\[
\Phi_uL_u\ge\Phi_dL_d.
\]

Using

\[
L=\Phi R,
\qquad
\frac{\Phi_d}{\Phi_u}=e^{I_+},
\qquad
\frac{R_d}{R_u}=e^{J_+},
\]

we recover

\[
\boxed{
J_+\le-2I_+.
}
\]

Thus the M19-389 quarter-strain conditions

\[
\boxed{
\int_{\theta_u}^{\theta_d}
\left(\frac14-\bar\sigma_\rho\right)d\theta
\ge I_+
}
\]

and, on a recurrent relative-residence cycle,

\[
\boxed{
\int_{\theta_d}^{\theta_{u,next}}
\left(\bar\sigma_\rho-\frac14\right)d\theta
\ge I_+
}
\]

are valid for arbitrary regular crossing speeds.

---

## 4. Canonical reading

Retain M19-389 in full except for the sentence suggesting an additional crossing-speed ratio in the unequal-speed case.

The corrected conclusion is stronger:

\[
\boxed{
\text{current cancellation/reversal}
\Longrightarrow
\text{quarter-strain phase separation}
}
\]

with no equal-speed hypothesis at regular zero crossings.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
