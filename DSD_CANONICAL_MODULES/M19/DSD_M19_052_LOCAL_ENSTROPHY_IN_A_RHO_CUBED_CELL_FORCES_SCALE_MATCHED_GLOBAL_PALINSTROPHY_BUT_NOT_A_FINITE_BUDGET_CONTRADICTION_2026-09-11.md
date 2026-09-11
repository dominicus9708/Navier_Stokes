# M19-052 — Local enstrophy in a rho^3 cell forces scale-matched global palinstrophy but not a finite-budget contradiction

**Date:** 2026-09-11  
**Status:** CALCULATION / LOCAL SOBOLEV CAPACITY / SUB-NATURAL PACKET DERIVATIVE PAYMENT / BUDGET FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-051 gives a smooth divergence-free scaling model of a sub-natural packet with

\[
\|\omega\|_2^2\asymp J/\rho,
\qquad
\|u\|_2^2\asymp J\rho.
\]

The model also has

\[
\|\nabla\omega\|_2^2\asymp J/\rho^3.
\]

The present module checks whether that derivative size is merely an artifact of the chosen seed or is forced by the localization itself.

It is forced globally by the three-dimensional Sobolev inequality.

## 2. Local shell mass assumption

Let \(E_\rho\subset\mathbb R^3\) be a measurable active cell/shell collar satisfying

\[
\boxed{|E_\rho|\le C_V\rho^3.}
\]

Assume

\[
\boxed{
m_\rho
:=
\int_{E_\rho}|\omega|^2dx
\ge
c_m\frac J\rho.}
\]

No pointwise upper amplitude bound is needed for the argument below.

## 3. Finite-volume Holder lower bound on L6

On \(E_\rho\), Holder gives

\[
\|\omega\|_{L^2(E_\rho)}
\le
|E_\rho|^{1/3}
\|\omega\|_{L^6(E_\rho)}.
\]

Squaring,

\[
m_\rho
\le
|E_\rho|^{2/3}
\|\omega\|_{L^6(E_\rho)}^2.
\]

Hence

\[
\|\omega\|_{L^6(\mathbb R^3)}^2
\ge
\|\omega\|_{L^6(E_\rho)}^2
\ge
\frac{m_\rho}{|E_\rho|^{2/3}}.
\]

Using

\[
|E_\rho|^{2/3}\lesssim\rho^2
\]

and the shell mass floor,

\[
\boxed{
\|\omega\|_6^2
\gtrsim
\frac{J}{\rho^3}.}
\]

## 4. Whole-space Sobolev gives palinstrophy

For smooth decaying vorticity on \(\mathbb R^3\),

\[
\|\omega\|_6
\le
C_S\|\nabla\omega\|_2.
\]

Therefore

\[
\boxed{
P(t)
:=
\|\nabla\omega(t)\|_2^2
\gtrsim
\frac{J}{\rho^3}.}
\]

This is an unconditional snapshot consequence of putting enstrophy \(J/\rho\) into a volume of order \(\rho^3\).

It does not depend on a compact-support boundary layer, on the M19-051 toy profile, or on a local Poincare condition.

## 5. Scale invariance

The natural dimensionless ratio is

\[
\boxed{
\rho^3P(t)
\gtrsim
J.}
\]

Thus in shell-normalized variables, the palinstrophy charge is only order \(J\).

This is important: the physical divergence

\[
P\gtrsim J/\rho^3
\]

is exactly the ordinary Navier--Stokes scaling of an order-\(J\) normalized derivative charge.

Therefore one must not call the factor \(\rho^{-3}\) itself a new contradiction.

## 6. Diffusive-rate interpretation

Compare the palinstrophy with the local enstrophy mass:

\[
\frac{P}{m_\rho}
\gtrsim
\rho^{-2}.
\]

Hence the scale-matched viscous rate is

\[
\boxed{
\nu\frac{P}{m_\rho}
\gtrsim
\frac\nu{\rho^2}.}
\]

The corresponding time is the packet diffusion time

\[
\boxed{
\tau_{diff}\sim\frac{\rho^2}{\nu}.}
\]

Thus a shell-localized packet cannot be both nondegenerate and derivative-free. Its derivative scale is at least the expected diffusive scale.

## 7. Relation to M19-039 quiet-contact hypothesis

M19-039 obtains one full natural-time contact only on the branch where the already typed stretch, bulk-diffusion, shell-diffusion and population-exchange contributions do not remove a fixed fraction of the localized mark over the candidate interval.

M19-052 shows that a spatially concentrated shell necessarily coexists with global palinstrophy at rate

\[
P\gtrsim J/\rho^3.
\]

However this does **not** imply that the localized material-population bulk-diffusion term

\[
D_{bulk,i}
=-2\nu\int_{P_i}\chi_R|\nabla\omega|^2
\]

has the same lower bound: the Sobolev argument is global and does not localize where the gradient is paid.

Therefore the safe conclusion is

\[
\boxed{
\text{shell concentration}
\Longrightarrow
\text{global scale-matched palinstrophy exposure},
}
\]

not automatically a lower bound on one population's \(D_{bulk,i}\).

This firewall prevents an invalid local-diffusion closure.

## 8. Interaction with M18-025

Since

\[
P(t_k)
\gtrsim
J_k/\rho_k^3,
\]

and the cubic-dominant sector has

\[
J_k/\rho_k\to\infty,
\qquad
\rho_k\to0,
\]

we obtain

\[
P(t_k)\to\infty.
\]

Thus the sharp R-AC shell family necessarily generates high global palinstrophy snapshots.

M18-025 then gives, on a smooth same-branch backward window, the alternative

\[
\boxed{
G_{high\ snapshot\ P}
\Longrightarrow
G_{P\ time\ occupation}
\lor
G_{raw-H2\ fast\ crossing}
\lor
G_{backward\ window/genealogy\ loss}.
}
\]

This is a genuine additional route out of the static packet picture.

## 9. Why high physical palinstrophy is not by itself a contradiction

The standard Leray energy budget controls

\[
\int\|\omega\|_2^2dt,
\]

not the full pre-singular integral

\[
\int\|\nabla\omega\|_2^2dt
\]

by itself.

Moreover the normalized shell relation is only

\[
\rho^3P\gtrsim J.
\]

Thus physical growth of \(P\) as \(\rho\to0\) is compatible with ordinary scaling.

Any contradiction must still use the correctly oriented record ledger, nonreuse, lower-order descent, or a separate finite resource.

Therefore

\[
\boxed{
P(t_k)\to\infty
\neq
\text{global regularity contradiction}.
}
\]

## 10. Correction to the naive filling discussion

M19-051 correctly shows that amplitude-natural volume filling is not forced by local dimensional data.

M19-052 adds that a single isolated sub-natural packet already carries the unavoidable derivative exposure

\[
P\gtrsim J/\rho^3.
\]

Therefore the correct static trichotomy is not

\[
\text{one packet}\lor\text{many packets}.
\]

It is

\[
\boxed{
\text{sub-natural kinetic packet}
+\text{scale-matched derivative exposure}
}
\]

with any additional filling/multiplicity requiring a dynamical theorem.

## 11. Updated sharp R-AC data

On the retained cubic-dominant kinetic shell family we now simultaneously have

\[
\boxed{
\begin{aligned}
&m_k\gtrsim J_k/\rho_k,\\
&\mathcal M_k^{own}\gtrsim J_k,\\
&P(t_k)\gtrsim J_k/\rho_k^3,\\
&t_k\uparrow T_*.
\end{aligned}
}
\]

Thus R-AC is no longer an abstract genealogy defect. It is a terminal sequence with simultaneous kinetic and derivative concentration at moving centers.

The unresolved issue is how this sequence embeds into one common-center / fixed-parent representation without losing the original cubic exponent.

## 12. Next target

M19-053 should combine the two simultaneous charges

\[
\mathcal M_k^{own}\gtrsim J_k,
\qquad
\rho_k^3P(t_k)\gtrsim J_k
\]

with the first-hitting amplitude scale

\[
r_A=\rho_kJ_k^{-1/4}.
\]

The objective is to test a **two-resource interpolation at the first-hitting natural scale**.

The M19-050 common-center kinetic charge loses \(J^{1/4}\):

\[
\mathcal M_k^{com}\gtrsim J_k^{5/4}.
\]

A successful mixed kinetic-palinstrophy inequality would need to recover that missing \(J^{1/4}\) without assuming packet multiplicity.

If no scale-correct combination can do this, the exponent gap should be certified as structural rather than an artifact of using kinetic energy alone.

---

\[
\boxed{\text{M19-052 COMPLETE; SUB-NATURAL SHELLS NECESSARILY CARRY SCALE-MATCHED PALINSTROPHY, BUT NO FINITE-BUDGET CONTRADICTION FOLLOWS YET.}}
\]