# DSD M5-391 — Unbounded adjacent reformation exposure collapses to H

Date: 2026-08-31

Status: **M5-390 REPLACED THE VAGUE `UNFORMED T` LABEL BY AN EXPLICIT ADJACENT-STAGE EXPOSURE/CONTACT/REPLACEMENT TRICHOTOMY / A GENUINELY UNFORMED LONG-TIME SURVIVOR WOULD HAVE TO DEFEAT QUIET CARRIER TRANSPORT FOR EVERY FIXED EXPOSURE THRESHOLD, HENCE FORCE `max{Sigma_j,Lambda_j,D_j}->infinity` ON A SUBSEQUENCE / THE EXISTING UNIFORM NORMALIZED STAGE-LENGTH CEILING THEN CONVERTS UNBOUNDED LIPSCHITZ/STRAIN EXPOSURE TO A POINTWISE SIMILARITY-GRADIENT H EVENT AND UNBOUNDED DIFFUSION EXPOSURE TO A NORMALIZED SECOND-VORTICITY-DERIVATIVE H EVENT / BY M5-371--378 THE GRADIENT EVENT RETURNS TO `H_freq/cap` OR REMOTE/FORMED TURNOVER / THEREFORE GENUINELY UNFORMED ADJACENT REFORMATION IS NOT AN INDEPENDENT T LEAF / THE REMAINING DYNAMIC BRANCH HAS UNIFORMLY BOUNDED EXPOSURE AND IS FORMED CONTACT OR REPLACEMENT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-390 proved that every sufficiently late adjacent first-hitting transition admits

\[
\boxed{
\mathcal R_j^{form}
\lor
R_j^{contact}
\lor
T_j^{replacement}.
}
\]

The reformation exposure is built from

\[
\Sigma_j
=
\int_{I_j}
\sup_{A_j(t)}|S|dt,
\]

\[
\Lambda_j
=
\int_{I_j}
\sup_{H_j(t)}|\nabla u|dt,
\]

and

\[
\mathcal D_j
=
\frac\nu{W_j}
\int_{I_j}
\sup_{A_j(t)}|\Delta\omega|dt.
\]

A fixed threshold crossing is not itself a contradiction. Indeed first-hitting growth already requires order-one stretching action.

The correct question is what happens if carrier formation **never stabilizes at any finite quiet threshold**.

---

## 2. Meaning of genuinely unformed reformation

For a fixed finite triple of thresholds

\[
L_S,L_\Lambda,L_D<\infty,
\]

M5-390 says that if all three exposures stay below those thresholds on one stage, then a coherent material ancestor packet exists at the next endpoint and the stage is classified by contact or replacement.

Therefore a long-time branch can deserve the label “unformed” only if there is no finite threshold triple that works eventually.

Equivalently, after passing to a subsequence,

\[
\boxed{
\max\{\Sigma_j,\Lambda_j,\mathcal D_j\}
\to\infty.
}
\]

If all three sequences were uniformly bounded, choose larger fixed thresholds and M5-390 would form the carrier on every sufficiently late retained stage.

Thus unformed turnover is quantitatively an **unbounded exposure** branch.

---

## 3. Normalize one first-hitting stage

Use the stage-`j` natural variables

\[
Y=\frac{x-X_j}{r_j},
\qquad
\tau=W_j(t-t_j),
\]

with

\[
r_j^2=\frac\nu{W_j}.
\]

Let

\[
U_j(Y,\tau)
\]

be the standard Navier--Stokes velocity normalization and

\[
\Omega_j=rac{\omega}{W_j}.
\]

Then

\[
\nabla_YU_j
\sim
\frac{\nabla_xu}{W_j}
\]

up to the fixed viscosity convention used by the repository, and

\[
\Delta_Y\Omega_j
=
\frac{\nu}{W_j^2}\Delta_x\omega.
\]

Since

\[
d\tau=W_jdt,
\]

the dimensionless exposures are exactly of the form

\[
\boxed{
\Lambda_j
=
\int_{\widehat I_j}
\sup_{\widehat H_j(\tau)}
|\nabla_YU_j|d\tau
}
\]

and

\[
\boxed{
\mathcal D_j
=
\int_{\widehat I_j}
\sup_{\widehat A_j(\tau)}
|\Delta_Y\Omega_j|d\tau.
}
\]

Likewise

\[
\Sigma_j
\le
\Lambda_j
\]

up to the fixed norm convention because `S` is the symmetric part of `grad u`.

Thus it is enough to track `Lambda_j` and `D_j`.

---

## 4. Use the bounded normalized stage-length ceiling

The retained first-hitting corridor already supplies a uniform normalized stage ceiling

\[
\boxed{
|\widehat I_j|\le L_*<\infty.
}
\]

This is the same ceiling used in M5-362 to convert the fixed first-hitting stretching action into an instantaneous positive normalized stretching event.

Therefore

\[
\Lambda_j
\le
L_*
\sup_{\widehat I_j}
\|\nabla_YU_j\|_{L^\infty(\widehat H_j)},
\]

and

\[
\mathcal D_j
\le
L_*
\sup_{\widehat I_j}
\|\Delta_Y\Omega_j\|_{L^\infty(\widehat A_j)}.
\]

Hence

\[
\boxed{
\Lambda_j\to\infty
\Longrightarrow
\sup_{\widehat I_j}
\|\nabla_YU_j\|_\infty\to\infty,
}
\]

and

\[
\boxed{
\mathcal D_j\to\infty
\Longrightarrow
\sup_{\widehat I_j}
\|\Delta_Y\Omega_j\|_\infty\to\infty.
}
\]

No time-disjoint summation is used.

---

## 5. Diffusion-exposure divergence is directly high-derivative H

If

\[
\mathcal D_j\to\infty,
\]

then at some smooth pre-singular time in each retained stage

\[
\boxed{
\|\Delta_Y\Omega_j\|_\infty\to\infty.
}
\]

This is exactly a normalized second-vorticity-derivative escape:

\[
\boxed{
H_{\Delta\Omega/high-der}.
}
\]

It is part of the existing

\[
H_{micro/freq/cap}
\]

family.

The branch may have vanishing physical kinetic mass and therefore is not claimed to produce an endpoint energy atom.

---

## 6. Lipschitz/strain-exposure divergence is similarity-gradient H

If instead

\[
\Lambda_j\to\infty,
\]

then

\[
\boxed{
\|\nabla_YU_j\|_\infty\to\infty
}
\]

at selected times.

This is the similarity-gradient H event studied in M5-370--378.

M5-371 gives the Calderon--Zygmund source decomposition

\[
H_{\nabla,sim}
\Longrightarrow
H_{\omega}
\lor
H_{Dini/dir}
\lor
H_{angular,multiscale}
\lor
T_{remote}.
\]

M5-372--378 subsequently collapse the Dini/angular/natural-partner leaves into derivative/frequency-capacity H or remote/core turnover.

Therefore

\[
\boxed{
\Lambda_j\to\infty
\Longrightarrow
H_{micro/freq/cap}
\lor
T_{remote/core}.
}
\]

If the event remains inside the adjacent formed observation hull, the remote alternative is absent and the branch is H.

If the relevant source/window escapes the hull, that escape is already a formed spatial/remote turnover mechanism rather than “unformed” reformation.

---

## 7. Main collapse of genuinely unformed T

Combine Sections 2--6.

A genuinely unformed adjacent-stage branch requires

\[
\max\{\Sigma_j,\Lambda_j,\mathcal D_j\}\to\infty.
\]

Since `Sigma_j` is controlled by the full Lipschitz exposure, one obtains

\[
\boxed{
T_{dyn}^{genuinely\ unformed}
\Longrightarrow
H_{micro/freq/cap}
\lor
T_{remote/formed}.
}
\]

Thus the “unformed” label does not survive as an independent terminal mechanism.

If the exposure remains uniformly bounded, the carrier is formed and M5-390 reduces the stage to material contact or packet replacement.

---

## 8. Updated adjacent-stage frontier

The correct adjacent-stage master split is now

\[
\boxed{
\text{late first-hitting transition}
\Longrightarrow
H_{micro/freq/cap}
\lor
T_{remote/formed}
\lor
R_{contact}^{formed}
\lor
T_{replacement}^{formed}.
}
\]

On a bounded-spatial no-H corridor this further reduces to

\[
\boxed{
\text{bounded-spatial no-H stage}
\Longrightarrow
R_{contact}^{formed}
\lor
T_{replacement}^{formed}.
}
\]

This is a much more concrete frontier than `H or unformed T`.

---

## 9. Reconnection to fixed-flux genealogy

Every endpoint has a natural signed flux carrier of order `nu` by M5-390 and the Taylor-thick cylinder theorem.

Therefore recurrent formed contact/replacement stages can be tested against the existing natural scale-invariant flux genealogy:

\[
W_jr_j^2=\nu.
\]

On coherent directed-flux subcorridors:

- replacement routes to viscous flux change, projective action, export, multiflux, or H;
- finite multiflux memory forces positive-frequency costed exits under positive-density fixed-age replacement;
- bounded-age return and export were reduced in M5-385--388.

The remaining step is not carrier formation. It is proving that recurrent formed contact/replacement enters those directed-flux hypotheses with enough density, or else that failure of directional/coherent flux itself is an H/projective capacity event.

---

## 10. DSD interpretation

The final distinction is now between

1. **formed but analytically rough** — H;
2. **formed and materially recurrent/replaced** — contact/replacement genealogy;
3. **formed but spatially escaping** — remote/export T.

There is no need for a fourth category “nothing can be described.”

On every smooth first-hitting endpoint a natural carrier is available; what changes is its analytic condition, material contact, or spatial location.

---

## 11. Firewall

- Unbounded exposure implies H/remote, but a fixed order-one exposure per stage is not a contradiction.
- The bounded normalized stage ceiling is essential to convert integrated exposure divergence into pointwise H.
- The result does not prove that formed contact/replacement has positive density; that is the next genealogy issue.
- The result does not close `H_micro/freq/cap`.
- Remote/window loss remains a formed T mechanism when it genuinely leaves the bounded observation hull.

---

## 12. Audit verdict

### REMOVED AS INDEPENDENT TERMINAL

\[
\boxed{T_{dyn}^{unformed}.}
\]

### DERIVED

\[
\boxed{
\text{unbounded adjacent reformation exposure}
\Longrightarrow
H_{micro/freq/cap}
\lor
T_{remote/formed}.
}
\]

### CURRENT FORMED NO-H FRONTIER

\[
\boxed{
R_{contact}^{formed}
\lor
T_{replacement}^{formed}
\lor
T_{remote/export}^{formed}.
}
\]

### STILL OPEN

- recurrent contact/replacement density and directed-flux coherence;
- `H_micro/freq/cap` itself;
- remaining formed remote/export outside the complete W1 corridor;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
