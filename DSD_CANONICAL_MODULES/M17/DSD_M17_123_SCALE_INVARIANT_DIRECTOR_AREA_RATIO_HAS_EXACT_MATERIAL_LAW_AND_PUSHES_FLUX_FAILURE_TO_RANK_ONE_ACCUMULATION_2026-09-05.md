# DSD M17-123 — Scale-invariant director-area ratio has an exact material law and pushes flux failure to Rank-1 accumulation

Date: 2026-09-05
Canonical ID: **M17-123**

Status: **EXACT MATERIAL RATIO LAW / DEFINE THE SCALE-INVARIANT DIRECTOR-AREA RATIO `eta_J=|J_xi|/rho`. ON PURE-KERNEL RANK TWO IT OBEYS `D_B log eta_J=sigma_k-sigma-kappa`. CONSEQUENTLY A REGULAR BOUNDED-COEFFICIENT CORE WITH UNIFORM FINITE RIBBON RESIDENCE CANNOT CREATE ARBITRARILY SEVERE DIRECTOR-AREA DEGENERATION FROM UNIFORMLY NONDEGENERATE INCOMING CARRIERS. IF FLUX-CAPTURE FAILURE OCCURS THROUGH `eta_J -> 0` ALONG AN INFINITE FRESH-CARRIER SEQUENCE, THE INCOMING SEQUENCE ITSELF MUST APPROACH THE `J_xi=0` RANK-ONE/RANK-DEFICIENT BOUNDARY. THIS IS SEQUENTIAL ACCUMULATION ACROSS DISTINCT CARRIERS, NOT A FORBIDDEN FINITE-TIME MATERIAL RANK CONVERSION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scale-invariant area ratio

On the regular pure-kernel Rank-2 branch define

\[
\boxed{
\eta_J:=\frac{|J_\xi|}{\rho}.
}
\]

Under Navier–Stokes similarity rescaling, both `|J_xi|` and vorticity amplitude `rho` scale as `r^{-2}`. Hence

\[
\boxed{\eta_J\text{ is similarity-scale invariant}.}
\]

M17-122 rewrites the per-flux enstrophy density as

\[
\frac{\rho^2}{|J_\xi|}
=\frac{\rho}{\eta_J}.
\]

Thus `eta_J` is the natural dimensionless flux-capture nondegeneracy descriptor.

---

## 2. Exact material law

The pure-kernel director-area law gives

\[
D_B\log|J_\xi|=\sigma_k-1.
\]

The CE-H vorticity-amplitude law gives

\[
D_B\log\rho=\sigma+\kappa-1.
\]

Subtracting,

\[
\boxed{
D_B\log\eta_J
=\sigma_k-\sigma-\kappa.
}
\]

Define

\[
\boxed{
\Gamma_J:=\sigma_k-\sigma-\kappa.
}
\]

Then for one regular material carrier,

\[
\boxed{
\eta_J(\theta)
=\eta_J(\theta_{in})
\exp\left(
\int_{\theta_{in}}^\theta\Gamma_J(s)ds
\right).
}
\]

---

## 3. Finite-residence distortion bound

Assume a compact regular ribbon core satisfies

\[
|\Gamma_J|\le M
\]

and M17-117 gives a uniform residence bound

\[
0\le\theta-\theta_{in}\le\tau_*.
\]

Then

\[
\boxed{
 e^{-M\tau_*}\eta_{J,in}
\le
\eta_J(\theta)
\le
 e^{M\tau_*}\eta_{J,in}.
}
\]

Therefore a uniform incoming lower bound

\[
\eta_{J,in}\ge c_\eta>0
\]

implies the interior lower bound

\[
\boxed{
\eta_J\ge c_\eta e^{-M\tau_*}>0.
}
\]

A bounded regular core cannot manufacture arbitrarily small `eta_J` during one finite residence episode.

---

## 4. Consequence for fresh-carrier turnover

M17-116–M17-120 exclude indefinite same-material compact ribbon recurrence. A recurrent Eulerian ribbon must therefore be serviced by a sequence of fresh material carriers.

Suppose there are stages `j_n -> infinity` and carriers `lambda_n` for which

\[
\eta_J^{(n)}\to0
\]

inside the recurrent core while the coefficient/residence bounds above remain uniform.
Then Section 3 forces

\[
\boxed{
\eta_{J,in}^{(n)}\to0.
}
\]

Thus severe flux-capture degeneration is inherited from the incoming genealogy; it is not generated from a uniformly transverse Rank-2 reservoir inside the core.

---

## 5. Compact-limit interpretation

Assume additionally a normalized compact hard hull with

\[
\rho_n\ge c_\rho>0
\]

at the selected carrier points and sufficient `C^1` compactness of the director fields.
Since

\[
|J_\xi^{(n)}|
=\rho_n\eta_J^{(n)},
\]

we obtain

\[
|J_\xi^{(n)}|\to0.
\]

After passage to a convergent subsequence,

\[
\boxed{
J_{\xi,\infty}=0,
\qquad
\rho_\infty\ge c_\rho>0.
}
\]

Because `J_xi` is the Hodge-dual director-area Jacobian, this means

\[
\boxed{
\operatorname{rank}(d\xi_\infty)\le1.
}
\]

Hence persistent normalized flux-capture failure through area degeneration accumulates on the Rank-1/rank-deficient boundary of director geometry.

---

## 6. No conflict with M17-111

M17-111 states that along one finite regular material trajectory,

\[
J_\xi\ne0
\]

cannot become zero.

The present conclusion concerns a sequence of **different fresh material carriers/stages**:

\[
J_\xi^{(n)}\ne0
\quad\text{for every finite }n,
\qquad
J_\xi^{(n)}\to0.
\]

Therefore

\[
\boxed{
\text{material rank conversion is still forbidden,}
\quad
\text{but sequential Rank-1 accumulation is allowed.}
}
\]

---

## 7. DSD interpretation

The flux-capture denominator is not merely a small geometric number.
Its normalized form `eta_J` has an exact carrier genealogy.

This converts

\[
\text{small director-area flux per vorticity}
\]

into

\[
\boxed{
\text{incoming near-rank-loss ancestry}
}
\]

whenever the recurrent core has uniform regularity and finite residence.

The remaining issue is then no longer an internal Rank-2 dynamics question; it is whether an infinite critical-vorticity cascade can be supplied by carriers accumulating on the Rank-1/interface boundary without falling into the already isolated Rank-1 pressure/firewall alternatives.

---

## 8. DSD audit

### Audit A — concluding finite-time `R2 -> R1`

Rejected. Every finite-stage carrier remains Rank 2. Only a sequential compact limit may have `J_xi=0`.

### Audit B — using `eta_J -> 0` without nonvanishing vorticity

Insufficient. To infer `J_xi -> 0` in a meaningful critical carrier, retain `rho>=c_rho>0` or an equivalent vorticity-mass localization condition.

### Audit C — assuming the core coefficient bound globally

The distortion conclusion is conditional on a uniform compact regular core bound for `Gamma_J` and the finite residence bound already isolated for the ribbon class.

### Audit D — proof status

The Rank-1 accumulation boundary is identified, but no theorem yet excludes infinite fresh-carrier accumulation on that boundary.

---

## 9. Updated flux-failure frontier

For normalized complete ribbons inside a uniformly regular finite-residence core,

\[
\boxed{
F_{capture}^{failure,area}
\Longrightarrow
A_{R1}^{fresh-carrier\ accumulation}
}
\]

provided the carrier retains nontrivial normalized vorticity amplitude.

Combined with M17-122,

\[
\boxed{
R_2^{ribbon}
\Longrightarrow
F_{capture}^{nondeg}
\ \lor\
A_{R1}^{fresh-carrier}
\ \lor\
D_q^{kernel-flattening}
\ \lor\
T_{ribbon-cover}.
}
\]

The next target is to remove or geometrically absorb the `q -> 0` complete-ribbon escape inside a fixed bounded recurrent core, then assemble the surviving flux-captured ribbon tail with the M5 return-density gate.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
