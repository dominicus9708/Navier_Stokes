# DSD M17-289 — A growing mesoscopic horizon closes nondegenerate packet occupancy unless coefficient, shell-amplification, or infinity feed occurs

Date: 2026-09-06  
Canonical ID: **M17-289**

Status: **CONDITIONAL GROWING-MESOSCOPIC-HORIZON GATE / LET `mu_j=m_j/Esh_j` BE PACKET-TO-PARENT-SHELL MASS FRACTION AND ASSUME `mu_j/r_j^7->infinity`, SO THE CRITICAL M17-287 FEED RADIUS `L_j=r_j mu_j^(-1/7)` TENDS TO ZERO WHILE THE TANGENT HORIZON `T_j=mu_j^(-2/7)` TENDS TO INFINITY. RESCALE DIRECTLY AT THE PHYSICAL MESOSCOPIC RADIUS `L_j`. IF THE CUMULATIVE LOWER-ORDER COEFFICIENT ACTION `L_j^2 sup(|grad B|+|Sigma|+1)` TENDS TO ZERO, THE EQUATION IS A SMALL PERTURBATION OF HEAT ON A FIXED UNIT CYLINDER AND STANDARD FUNDAMENTAL-SOLUTION DERIVATIVE BOUNDS PRESERVE THE `R^7` BACKWARD-FEED SCALING. IF, IN ADDITION, THE RELEVANT PARENT/NEIGHBOR SHELL MASS DOES NOT AMPLIFY BY A FIXED LARGE FACTOR OVER THE SHORT PHYSICAL TIME `O(L_j^2)` AND NO FAR-BOUNDARY/INTERFACE REMAINDER SURVIVES, CHOOSING A SUFFICIENTLY LARGE FIXED MULTIPLIER IN THE CRITICAL RADIUS MAKES THE REQUIRED BACKWARD MASS EXCEED THE AVAILABLE SHELL MASS, A CONTRADICTION. THEREFORE THE `mu_j/r_j^7->infinity` LANE RETURNS TO MESOSCOPIC COEFFICIENT ACTION, SHELL AMPLIFICATION/REPLENISHMENT, INFINITY/INTERFACE FEED, OR CONTRADICTION. THE ONLY NO-PAYER OCCUPANCY SURVIVOR IS `mu_j=O(r_j^7)`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical mesoscopic scale

Let

\[
\mu_j:=\frac{m_j}{E_j^{sh}}.
\]

Assume the nondegenerate occupancy branch

\[
\boxed{
\frac{\mu_j}{r_j^7}\to\infty.
}
\]

Choose a fixed constant `A>>1` and define

\[
\boxed{
K_j:=A\mu_j^{-1/7},
\qquad
T_j:=K_j^2=A^2\mu_j^{-2/7}.
}
\]

The corresponding physical similarity scale is

\[
\boxed{
L_j:=r_jK_j
=A r_j\mu_j^{-1/7}\to0.
}
\]

The physical backward time interval has length

\[
\boxed{
L_j^2.
}
\]

Because the parent shell center is remote and `L_j->0`, the mesoscopic ball stays far inside the same finite-neighbor shell geometry unless an explicit interface/domain exit occurs.

---

## 2. Mesoscopic rescaling

Rescale around the packet center at length `L_j` and time `L_j^2`.

The intrinsic similarity-vorticity equation has constant principal diffusion and lower-order drift/strain/reaction terms.

After the `L_j` rescaling, the relevant dimensionless coefficient action is controlled by

\[
\boxed{
\mathfrak C_j^{meso}
:=
L_j^2
\sup_{Q_{cL_j}}
\left(
|\nabla B|+|\Sigma|+1
\right).
}
\]

Split:

### Coefficient-critical branch

If

\[
\limsup_j\mathfrak C_j^{meso}>0,
\]

retain

\[
\boxed{G_{mesoscopic\ ambient/coefficient\ action}.}
\]

### Heat-perturbative branch

If

\[
\boxed{\mathfrak C_j^{meso}\to0,}
\]

the mesoscopic equation is a uniformly small first/zero-order perturbation of the heat equation on a fixed unit cylinder.

The drift-flow distortion is also small because the relevant Lipschitz accumulation is exactly `O(mathfrak C_j^meso)`.

---

## 3. Fundamental-solution derivative scaling

For constant principal diffusion with uniformly small bounded Lipschitz drift and bounded zero-order coefficient, standard interior/fundamental-solution estimates preserve the heat-kernel derivative scale.

In root packet variables this gives, with constants independent of `j`,

\[
\boxed{
\|\nabla_x^2\Gamma_j(T_j;\cdot)\|_{L^2}
\le C T_j^{-7/4}.
}
\]

As in M17-287, if the cutoff boundary remainder vanishes, the retained present raw Laplacian charge implies

\[
\boxed{
M_j^{back}(K_j)
\ge c m_j K_j^7.
}
\]

With

\[
K_j=A\mu_j^{-1/7},
\]

this becomes

\[
\boxed{
M_j^{back}(K_j)
\ge cA^7 E_j^{sh}.
}
\]

Choose `A` so large that `cA^7` dominates the fixed shell-comparability constant used below.

---

## 4. Parent-shell mass corridor

To convert the feed lower bound into contradiction, one needs an upper bound for the mass available in the relevant parent/enlarged shell at time

\[
\theta_j-L_j^2.
\]

Retain the explicit alternative:

### Shell amplification / replenishment

If

\[
\boxed{
E_j^{sh}(\theta_j-L_j^2)
>C_{sh}E_j^{sh}(\theta_j)
}
\]

for a fixed large threshold `C_sh`, record

\[
\boxed{G_{short\text{-}time\ parent\text{-}shell\ mass\ amplification/replenishment}.}
\]

### Shell corridor

Otherwise

\[
\boxed{
E_j^{sh}(\theta_j-L_j^2)
\le C_{sh}E_j^{sh}(\theta_j).
}
\]

Since the mesoscopic ball is contained in the enlarged shell on the no-interface branch,

\[
M_j^{back}(K_j)
\le C_{sh}E_j^{sh}.
\]

For `A` chosen so that

\[
cA^7>C_{sh},
\]

this contradicts Section 3.

---

## 5. Far-boundary remainder

The derivative-feed representation is again audited with spatial cutoffs.

If the far-boundary remainder does not vanish on the growing mesoscopic cylinder, retain

\[
\boxed{G_{far\text{-}boundary/infinity/interface\ feed}.}
\]

No contradiction is claimed on that branch.

---

## 6. Growing Mesoscopic Horizon Gate

Combining the previous sections gives

\[
\boxed{
\frac{\mu_j}{r_j^7}\to\infty
\Longrightarrow
G_{mesoscopic\ coefficient\ action}
\lor
G_{short\text{-}time\ shell\ amplification}
\lor
G_{far\text{-}boundary/interface\ feed}
\lor
\bot.
}
\]

Therefore, on the no-payer/no-interface survivor,

\[
\boxed{
\mu_j=O(r_j^7).
}
\]

Equivalently,

\[
\boxed{
\frac{m_j}{r_j^7}
=O(E_j^{sh}).
}
\]

This is the **seventh-power occupancy degeneration**.

---

## 7. What remains open

M17-289 does not yet close the seventh-power occupancy branch.

Its remaining content is extremely low absolute packet density:

\[
\boxed{
\delta_j:=\frac{m_j}{r_j^7}\to0
}
\]

at least as fast as the remote parent shell mass.

The next task is to determine whether such a packet can still retain the scale-comparable raw Laplacian charge and CE-H sign-balanced multiplier without forcing

1. amplitude/nodal degeneration;
2. a still smaller derivative carrier;
3. or short-time shell replenishment.

---

## 8. DSD audit

- The theorem is conditional on the explicitly stated mesoscopic coefficient and shell-mass corridors.
- Failure of either corridor is retained as a physical/analytic payer rather than treated as a contradiction.
- Growing-horizon compactness is replaced by direct mesoscopic rescaling at the physical scale `L_j`.
- The fundamental-solution derivative estimate is used only on the small-coefficient branch.
- The remaining `mu_j=O(r_j^7)` branch is not declared impossible.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
