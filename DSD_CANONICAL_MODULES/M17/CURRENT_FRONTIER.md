# M17 Current Frontier

Date: 2026-09-08  
Current tip: **M17-409**  
Status: **AUTHORITATIVE M17 NAVIGATION / CORRECTION INDEX**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

This file takes precedence over historical M17 companion indexes when status labels conflict. Historical modules remain preserved for provenance.

## 1. Permanent correction firewalls

- M17-304 is **SUPERSEDED** by M17-306.
- M17-306--307 separate first- and second-generation ancient solutions.
- M17-313 gives exact CE-H line constancy
  \[
  D_\xi\kappa=0,
  \qquad
  \nabla\kappa\perp W.
  \]
- Nonzero longitudinal `D_xi kappa` recharge readings of M17-144--146 are superseded.
- M17-330, M17-336, and M17-337 are **QUARANTINED for cross-generation use** by M17-338.
- M17-331--335 remain fixed-generation statements only.
- M17-367 forbids any `kappa`-only positive lower bound on raw `H2` because amplitude rescaling leaves `kappa` unchanged while scaling `E` and raw `H2` quadratically.
- M17-383 forbids replacing coefficient spatial thickness by solution-mass thickness without a doubling/frequency input.
- M17-396 corrects the M17-395 `Phi^2/R` physical log-diffusion lower bound: after exact parabolic normalization it is an order-one critical charge, not a supercritical divergence.
- **M17-404--406 supersede the old M17-400/402 interpretation that no finite first-generation raw-`H2` total is known.** The local reductions in M17-400/402 remain valid; only the budget-status interpretation changes.
- M17-408 permanently separates regular zero-corridor dynamics from `log|kappa|` coordinates: truncated log-diffusion diverges like `1/epsilon` at a regular active zero level.

## 2. DSD-theory scope

DSD theory is used only as a heuristic selector for variables, representation audits, failure typing, payer-equivalence checks, and candidate invariant descriptors.

It is **not** a Navier--Stokes/PDE hypothesis. Every active canonical statement must be independently derived by standard mathematics.

## 3. Global proof-tree status

The full attempt still has the upstream structure

\[
\text{hypothetical singularity}
\to
\underbrace{\text{precanonical root reduction}}_{\text{ROOT-CERT OPEN}}
\to
\text{canonical recurrent/critical survivor}.
\]

M5-598 then splits the survivor into

\[
CP\!-\!E
\lor
CP\!-\!S
\lor
CE\!-\!T
\lor
Migration
\lor
CE\!-\!H.
\]

The long M12--M17 calculation line is conditional on `CE-H`. The other four roots remain independent OPEN roots.

## 4. Certified first-generation resources and exact record weights

For the record blow-down

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

the exact derivative scaling is

\[
\int_I\|D^k\Omega_R\|_p^qds
=
R^{q(2+k-3/p)-2}
\int_{R^2I}\|D^k\Omega\|_p^qdt.
\]

### 4.1 Palinstrophy — M17-307

M5-477 gives finite first-generation palinstrophy and M17-307 gives

\[
\boxed{
\sum_mR_m^{-1}
\int_I\|\nabla\Omega_m\|_2^2ds
<\infty.
}
\]

Thus order-one normalized palinstrophy payments require essentially record-linear multiplicity to contradict the ancestor:

\[
\sum_m\frac{N_m}{R_m}=\infty.
\]

### 4.2 Raw-`H2` — M17-403--405

M17-403 computes

\[
\boxed{
\int_I\|\Delta\Omega_m\|_2^2ds
=
R_m^3
\int_{R_m^2I}\|\Delta\Omega\|_2^2dt.
}
\]

M17-404 upgrades M5-475/477 by viewing the ancient vorticity equation as a forced heat equation. The Type-I bounds

\[
\|V(t)\|_\infty\lesssim(-t)^{-1/2},
\qquad
\|\Omega(t)\|_\infty\lesssim(-t)^{-1},
\qquad
\|\Omega(t)\|_2^2\lesssim(-t)^{-1/2}
\]

and the quantitative palinstrophy tail imply on dyadic backward annuli

\[
\int_{-2T}^{-T}\|\Delta\Omega(t)\|_2^2dt
\lesssim T^{-3/2}.
\]

Hence

\[
\boxed{
\mathscr H_{anc}
:=
\int_{-\infty}^{0}\|\Delta\Omega(t)\|_2^2dt
<\infty.
}
\]

M17-405 therefore gives the genuine cross-generation finite ledger

\[
\boxed{
\sum_mR_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds
<\infty.
}
\]

For pairwise disjoint order-one normalized raw-`H2` events,

\[
\boxed{
\sum_m\frac{N_m}{R_m^3}<\infty.
}
\]

A contradiction through this resource requires essentially **record-cubic multiplicity** or another nonsummable enhancement.

### 4.3 Away-zero log-`kappa` diffusion — M17-403/406

Whenever the same sign-preserving CE-H multiplier is defined on both sides of a scaling map,

\[
\boxed{
\mathscr D_{\log\kappa,R}(I)
=
R\,
\mathscr D_{\log\kappa}^{anc}(R^2I),
}
\]

so the formal record weight is `R^{-1}`.

However this is **representation/genealogy conditional** in the current proof tree. A late descendant CE-H multiplier cannot be silently pulled back through a first-generation record cell unless parent-to-record CE-H/domain/genealogy persistence is separately certified.

There is no global all-sign finite log-`kappa` target because M17-408 proves regular zero levels make the logarithmic coordinate singular.

## 5. Exact CE-H coefficient-scale ownership: M17-381--386

On exact CE-H,

\[
\Delta W=\kappa W,
\qquad
|\Delta W|^2=\kappa^2|W|^2.
\]

With intrinsic coefficient scale

\[
r_\kappa=|\kappa|^{-1/2},
\]

M17-381 gives exact nonoverlapping coefficient-bin ownership and

\[
r^4H_r\asymp E_r.
\]

M17-382 upgrades coefficient bins to true own-scale spatial cells under

\[
r^3|\nabla\kappa|\le G_*.
\]

M17-386 extends raw-`H2` ownership exactly through time:

\[
\boxed{
\sum_m\int_IH_m(t)dt
=
\int_IH(t)dt.
}
\]

Thus raw-`H2` scale/time double counting is closed. After M17-404--405 it also has a true first-generation finite weighted budget.

## 6. Local doubling/frequency and standard-energy deformation: M17-383--389

M17-383 defines

\[
\mathfrak D_\theta(x,R)
=
\log\frac{E(B_R(x))}{E(B_{\theta R}(x))}
\]

and proves bounded local doubling gives a mass-retaining own-scale packet. A divergence-free constant-coefficient Helmholtz family proves coefficient regularity alone does not bound vanishing order.

In physical exact CE-H,

\[
D_t\Omega=(\sigma+\nu\kappa)\Omega,
\]

so M17-384 shows pointwise nodal order is inherited along the smooth material flow.

M17-387 gives on a persistent enlarged own-scale CE-H cell

\[
\|\Sigma\|_{L^\infty(B_R)}
\lesssim
R^{-3/2}\|\Omega\|_2.
\]

M17-388 converts this to the standard-energy ledgers

\[
\boxed{
\sum_jR_jK_j^2<\infty,
\qquad
\sum_jR_j\mathfrak X_j^2<\infty,
}
\]

where `X_j` is newly generated finite-scale doubling excess after removing a bounded inherited contribution.

M17-389 shows signed negative-`kappa` exposure is representation safe but

\[
D_t\log\Phi=\nu\kappa
\]

on a material tube, so strain cancels exactly from the flux law. Logarithmic coefficient exposure alone does not generate a stronger deformation payer.

## 7. Recurrence, flux, and turnover: M17-390--392

M17-390 shows compact same-loop recurrence produces at most logarithmic physical deformation across geometric similarity descent and is compatible with finite physical energy.

M17-391 gives the retained-flux standard-energy ledger

\[
\boxed{
\sum_jR_j\Phi_j^2<\infty.
}
\]

M17-392 gives the flux-turnover ledger

\[
\boxed{
\sum_jR_j\operatorname{Var}_{I_j}(\Phi_j^2)<\infty.
}
\]

Therefore order-one recurrence, fixed flux, or logarithmic deformation remain too weak against geometric-scale summability.

## 8. Coefficient migration and M5-688 payer classification: M17-393--402

M17-393 reclassifies `|kappa|R^2 >> 1` as descent to a smaller intrinsic coefficient scale unless normalized gradient/interface/domain compactness fails.

On sign-preserving intervals,

\[
D_t\log r_\kappa
=-\frac12\frac{D_t\kappa}{\kappa}.
\]

M17-394 gives

\[
D_t\log|\kappa|
=
L_\rho\log|\kappa|
+|\nabla\log|\kappa||^2
+\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
\]

M17-395--396 identify positive-flux intrinsic coefficient diffusion as a fixed positive **normalized critical** log-diffusion payment, not a supercritical one.

M17-397 shows M5-688 contains the same away-zero coefficient/log-diffusion architecture but is a recurrent cycle-work **balance**, not a finite ancestral budget.

M17-398--402 classify every non-topological M5-688 payer by resource:

\[
\boxed{
\begin{aligned}
D_\sigma,P_W,B_\rho,B_\sigma
&\to\text{palinstrophy},\\
\mathcal P_{\kappa\sigma}^{tilt}
&\to\text{raw-`H2`},\\
B_\kappa^{away}
&\to\text{away-zero log-`kappa` diffusion},\\
B_\kappa^{near}
&\to\text{zero corridor},\\
\mathcal C_2^{positive}
&\to\text{raw-`H2`}.
\end{aligned}
}
\]

M17-404--406 update the interpretation of the raw-`H2` entries: they now return to the finite `R_m^{-3}` ancestral ledger rather than to an unbudgeted resource.

## 9. Zero-corridor correction and resource return: M17-408--409

M17-408 defines the truncated zero-corridor log-diffusion

\[
D_{\log\kappa}^{\varepsilon,\delta}
=
\int_{\varepsilon\le|k|\le\delta}
 k^{-2}A_{\kappa\kappa}(k)dk.
\]

Using M17-343 regular level-set thickening,

\[
A_{\kappa\kappa}(k)
\ge e^{-C|k|}A_{\kappa\kappa}(0),
\]

so

\[
\boxed{
D_{\log\kappa}^{\varepsilon,\delta}
\gtrsim
A_{\kappa\kappa}(0)
\left(\frac1\varepsilon-\frac1\delta\right).
}
\]

Thus the log coordinate is intrinsically singular at a regular active zero level. This divergence is not a physical contradiction; it is a coordinate singularity carrying real zero-level diffusion.

M17-409 then uses coarea and the compact gradient ceiling to show

\[
\boxed{
H_{0,\delta}
:=
\int_{|\kappa|\le\delta}
\chi|\Delta W|^2dy
\ge
c_{0H}
A_{\kappa\kappa}(0).
}
\]

Hence a uniform regular compact zero corridor carries fixed normalized raw-`H2` occupancy and returns to the finite `R_m^{-3}` ancestral ledger.

The remaining genuinely distinct zero exits are therefore

\[
G_{zero\text{-}level\ criticality}
\lor
G_{coefficient\ gradient\ decompactification}
\lor
G_{amplitude/interface}
\lor
G_{component/tube/genealogy\ loss}.
\]

## 10. Low-frequency ancient firewall: M17-407

M17-404 does **not** imply a global strong-`L3` velocity theorem.

M5-476 gives `L2 cap L3 cap L6` only for a compactly localized rotational velocity, not for the full ancient velocity. In Fourier variables, raw-`H2` controls high frequency while velocity `L2/L3` has an independent zero-frequency obstruction.

Therefore no strong-`L3` Liouville shortcut is claimed.

## 11. Current narrow CE-H frontier

The compact analytic CE-H branch is now much narrower.

### Route A — raw-`H2` paid branches

Phase-tilt strain work, positive cutoff replenishment, and a uniform regular zero corridor all return to

\[
\boxed{
\sum_mR_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds<\infty.
}
\]

To contradict the first-generation ancestor, mapped descendant events must force

\[
\boxed{
\sum_mR_m^{-3}\sum_jh_{m,j}=\infty.
}
\]

For order-one events this is essentially a record-cubic multiplicity/duration requirement.

### Route B — sign-preserving away-zero log-`kappa`

This route has the milder formal `R_m^{-1}` scaling, but it still requires a representation-safe parent-to-record CE-H/domain/genealogy theorem and a finite/rigid sign-preserving source architecture.

It cannot pass through regular zero crossings because M17-408 shows the log coordinate diverges there.

### Route C — explicit degenerations

The remaining non-resource exits are coefficient-gradient decompactification, zero-level criticality, amplitude-threshold/interface loss, rank/domain loss, spatial/genealogy replacement, and failure of persistent own-scale cells.

## 12. Separate inherited OPEN dependencies

The proof attempt still inherits:

- `ROOT-CERT` recertification of the early root reduction;
- the four non-CE-H M5-598 roots `CP-E`, `CP-S`, `CE-T`, `Migration`;
- parent-to-M17 scale-map/domain/genealogy persistence;
- representation-safe mapping of descendant CE-H coefficient structures back to actual record cells;
- whether recurrence/strict-subscale dynamics can force record-linear palinstrophy multiplicity or record-cubic raw-`H2` multiplicity;
- whether the sign-preserving away-zero log-`kappa` branch admits a genuine finite ancestral budget or recurrence rigidity;
- explicit zero/interface/rank/domain/genealogy degenerations.

## 13. Current verdict

The most important new fact since M17-402 is

\[
\boxed{
\int_{-\infty}^{0}\|\Delta\Omega(t)\|_2^2dt<\infty
}
\]

for the first-generation ancient element, together with the exact record ledger

\[
\boxed{
\sum_mR_m^{-3}
\int_I\|\Delta\Omega_m\|_2^2ds<\infty.
}
\]

Thus raw-`H2` is now a certified ancestral resource, but geometric record blow-down discounts normalized descendant payments by `R_m^{-3}`.

The proof has therefore not reached a contradiction. The main remaining quantitative problem is to force enough mapped duration/multiplicity to defeat the exact ancestry discounts, or to establish a genuinely scale-critical rigidity/budget on the sign-preserving coefficient branch.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
