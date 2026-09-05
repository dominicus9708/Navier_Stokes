# DSD M17-201 — High-kappa amplitude replenishment forces a stronger downward multiplier return current

Date: 2026-09-06  
Canonical ID: **M17-201**

Status: **JOINT-CURRENT RETURN GATE / THE RECURRENT `(rho,kappa)` VOLUME CONTINUITY LAW OF M17-199 HAS POSITIVE SOURCE `(3/2) P`. INTEGRATING IT OVER THE UPPER-RIGHT STATE-SPACE QUADRANT `{rho>a, kappa>k0}` GIVES AN EXACT BOUNDARY CURRENT IDENTITY. ANY POSITIVE UPWARD AMPLITUDE CURRENT ENTERING THE RETAINED REGION AT HIGH KAPPA MUST BE OVERCOMPENSATED BY A NEGATIVE/DOWNWARD KAPPA CURRENT THROUGH `kappa=k0`, WITH AN ADDITIONAL PAYMENT EQUAL TO `(3/2)` TIMES THE QUADRANT MASS. THUS THE M17-192 HIGH-KAPPA REPLENISHMENT BRANCH IS NOT AN INDEPENDENT SOURCE: IT REQUIRES A MULTIPLIER-RETURN CONVEYOR. THE REMAINING FIREWALL IS THE MEASURE CONVERSION FROM THIS VOLUME KAPPA CURRENT TO THE ENSTROPHY/FLUX CURRENTS FOR WHICH M5-683 PROVIDES THE CLEAN CONSTITUTIVE LAW. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Recurrent joint continuity

M17-199 gives

\[
\partial_\theta\mathcal P
+\partial_r\mathcal J_r
+\partial_k\mathcal J_k
=\frac32\mathcal P.
\]

After invariant/recurrent averaging,

\[
\boxed{
\partial_r\overline{\mathcal J_r}
+\partial_k\overline{\mathcal J_k}
=\frac32\overline{\mathcal P}.
}
\]

---

## 2. Upper-right state quadrant

Fix regular positive thresholds

\[
a>0,
\qquad
k_0\in\mathbb R,
\]

and define

\[
\boxed{
\Omega_{a,k_0}
:=\{(r,k):r>a,\ k>k_0\}.
}
\]

Assume the state currents vanish at the remote state-space boundaries `r=infinity` and `k=infinity`, or equivalently work first on a large compact rectangle and pass to a limit where those outer fluxes vanish.

Integrating the stationary continuity equation over `Omega_{a,k0}` gives

\[
\int_{\partial\Omega_{a,k_0}}
\overline{\mathbf J}\cdot n\,dS
=\frac32
\iint_{\Omega_{a,k_0}}
\overline{\mathcal P}\,dr\,dk.
\]

The outward normal on the lower amplitude boundary is `-e_r`, and on the lower multiplier boundary is `-e_k`.
Therefore

\[
\boxed{
\int_{k>k_0}\overline{\mathcal J_r}(a,k)dk
+\int_{r>a}\overline{\mathcal J_k}(r,k_0)dr
=-\frac32M_{a,k_0},
}
\]

where

\[
\boxed{
M_{a,k_0}
:=\iint_{\Omega_{a,k_0}}
\overline{\mathcal P}\,dr\,dk\ge0.
}
\]

---

## 3. Replenishment implies multiplier descent

Define the net high-kappa upward amplitude current

\[
\boxed{
R_{up}(a,k_0)
:=\int_{k>k_0}\overline{\mathcal J_r}(a,k)dk.
}
\]

If

\[
R_{up}(a,k_0)>0,
\]

then the quadrant identity forces

\[
\boxed{
\int_{r>a}\overline{\mathcal J_k}(r,k_0)dr
=-R_{up}(a,k_0)-\frac32M_{a,k_0}<0.
}
\]

Thus the downward multiplier return has magnitude at least

\[
\boxed{
\left|
\int_{r>a}\overline{\mathcal J_k}(r,k_0)dr
\right|
\ge R_{up}(a,k_0).
}
\]

If the quadrant carries positive recurrent mass, the inequality is strict by the extra `3M/2` source payment.

---

## 4. Relation to M17-192

M17-192 shows that an exponentially positive amplitude-cutoff payer despite negative unweighted threshold turnover requires a fixed amount of upward amplitude current concentrated in sufficiently high-kappa phases.

The present theorem says every such replenishing phase must participate in a return conveyor:

\[
\boxed{
\text{high-kappa upward amplitude current}
\Longrightarrow
\text{stronger downward kappa current}.
}
\]

Thus high-kappa replenishment is not a terminal payer branch by itself.

---

## 5. Mandatory measure firewall

The current in Section 3 is spatial-volume weighted:

\[
\int_{r>a}\mathcal J_k(r,k_0)dr
=\int_{\rho>a}h\,\delta(k_0-\kappa)dy.
\]

M5-683 instead controls the enstrophy-weighted current

\[
G_E(k_0)
=\int h\,\delta(k_0-\kappa)\chi(\rho)\rho^2dy.
\]

M5-681 uses the transverse vortex-flux measure.

A negative volume current does not automatically imply a negative enstrophy- or flux-weighted current because positive weights can correlate with the sign of `h`.

Therefore the valid new target is a **measure/covariance transfer theorem for the downward return population**, not a claim that M5-683 already supplies a sign contradiction.

---

## 6. DSD audit

- The quadrant identity is exact kinematics plus similarity-volume source.
- No one-sign constitutive law for `h` is inferred.
- High-kappa replenishment and downward multiplier return are two boundaries of one state-space balance and must not be counted as independent costs.
- The volume/enstrophy/flux measure distinction remains explicit.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
