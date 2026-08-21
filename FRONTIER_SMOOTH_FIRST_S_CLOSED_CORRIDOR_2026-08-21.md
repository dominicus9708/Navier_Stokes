# Frontier: First Smooth S-Closed P_V Corridor — 2026-08-21

Status: **ONE EXPLICIT PURE SUBCORRIDOR S-CLOSED; GLOBAL REGULARITY NOT PROVED.**

This file consolidates the smooth-only mainline after the record-gradient transpose audit.

## 1. Audit correction

With

\[
G_{ij}=\partial_j\Omega_i,
\]

a first-hitting maximum satisfies

\[
\boxed{G^T\xi=0,}
\]

not `G xi=0`.

Consequences:

- the universal record-growth inequality remains valid;
- the universal Böttcher–Wenzel same-point production tradeoff remains valid;
- the scalar Taylor mass floor for `g=xi dot Omega` remains valid;
- the old middle-zero-specific aligned sharpening is withdrawn.

The pure corridor closed below does not use the withdrawn sharpening.

## 2. Legitimate moving-ball persistence bound

On the actual smooth solution, pass the moving-cutoff variance identity to a Euclidean-ball limit. Payne–Weinberger then gives

\[
V_R\le\frac{4R^2}{\pi^2}D_R.
\]

Define the pure low-turnover branch by

\[
\Lambda_V=V_+/V_-\le2,
\quad
\delta_V=\kappa_V/V_-\le1,
\quad
f_V=F_0/V_-\le1,
\quad
\eta\le1/2.
\]

Then for `q=2`,

\[
\boxed{
\Pi_B
\le1.4967761748.
}
\]

Replacing the analyticity constant by

\[
c_*(2)=\max\{c(2),1\}
\]

is legitimate and gives

\[
\boxed{
\Pi_B/c_*(2)^2\le1.4967761748.
}
\]

Failure of any pure threshold is not hidden: it is routed to variance turnover, endpoint reshaping, boundary/material/pressure flux, or dissipation-absorbing transport.

## 3. Compatible projective-speed ceiling

Instead of independently maximizing `lambda` and `E`, keep the common enstrophy variable:

\[
\lambda^{3/4}E^{1/2}
=2^{-1/2}Q^{3/4}Z^{-1/4}.
\]

Using derivative tightness and the record-point Taylor mass floor gives

\[
\boxed{
C_{V,+}
\le
0.3535533906
+0.7146986969
(1-\varepsilon_Q)^{-3/4}
\left(\frac{R_Q}{\rho_0}\right)^{9/4}.
}
\]

This is the current audited projective-speed bound.

## 4. Anti-ribbon swap closure

Positive-middle transverse stretching makes a coherent material cross-section ribbonize. Avoiding the ribbon requires a transverse projective swap whose time obeys

\[
L_j
\ge
\frac{\pi}{1+2C_{V,+}}.
\]

The smooth moving-ball pure corridor gives the competing upper time

\[
L_j
\le
\frac12\frac{\Pi_B}{c_*(2)^2}r^2,
\qquad
r=R_C/\rho_0.
\]

Hence survival requires

\[
\frac{\Pi_B}{c_*(2)^2}
\ge
\frac{2\pi}{r^2(1+2C_{V,+})}.
\]

### Zero derivative tail

For `epsilon_Q=0`, the equality occurs at

\[
\boxed{r\approx1.09908244.}
\]

Thus the zero-tail pure P_V corridor is S-closed for

\[
\boxed{R_C<1.09908244\rho_0.}
\]

### Quarter-tail robust corridor

If

\[
\varepsilon_Q\le1/4,
\]

the equality occurs at

\[
\boxed{r\approx1.06060560.}
\]

Therefore

\[
\boxed{
R_C<1.06060560\rho_0
\quad\Longrightarrow\quad
\text{pure low-turnover positive-middle P_V stage is S-closed}.
}
\]

This statement is on an actual finite smooth stage and uses no ancient limit.

## 5. Current survivor

A hypothetical late smooth survivor must now satisfy at least one of

\[
\boxed{
R_C\ge1.06060560\rho_0,
}
\]

or

\[
\boxed{
\varepsilon_Q>1/4,
}
\]

or leave the pure corridor through one of

\[
\boxed{
T_{variance},
\quad T_{boundary/material},
\quad H_{remote},
\quad residual/pressure\ action.
}
\]

For a pure survivor just above the radius threshold, projective speed must nearly saturate the compatible `Q`-upper / `Z`-lower estimate. Defining

\[
\Theta(r)
=
\frac{[C_{req}(r)-\sqrt2/4]_+}
{C_{V,max}(r)-\sqrt2/4},
\]

survival requires

\[
\boxed{
Q/Q_{max}\ge\Theta^{4/3},
\qquad
Z/Z_{min}\le\Theta^{-4}.
}
\]

Thus the next pure branch is an explicit near-saturation rigidity problem, while all non-pure exits are already typed.

## 6. Next target

Attack the large-core pure survivor

\[
R_C\gtrsim1.06\rho_0
\]

by combining

1. the near-threshold `Q`-saturation / `Z`-minimality requirement;
2. analytic-scale signed-component thickness or its known sparseness regularity alternative;
3. absolute interior dissipation forced by thick vorticity;
4. the moving-ball variance ledger.

The intended outcome is either a second S-closed interval above `1.06 rho0` or an unavoidable typed turnover/remote-derivative packet.

Status: **THE MAINLINE NOW CONTAINS A GENUINE DIRECT S-CLOSED PURE-P_V CORRIDOR. AFTER THE TRANSPOSE AUDIT, THE REMAINING PURE SURVIVOR MUST BE LARGER THAN APPROXIMATELY ONE ANALYTIC STRIP SCALE AND MUST SATURATE THE COMPATIBLE PROJECTIVE-SPEED BOUNDS NEAR THAT THRESHOLD.**