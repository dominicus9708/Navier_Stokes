# DSD M5-356 — Affine-Shield Circulation Growth: Recruitment or Viscous-Palinstrophy Audit

Date: 2026-08-30

Status: **NEW NON-ENERGY CHARGE LEDGER / SATURATED AFFINE-SHIELD CIRCULATION GROWS BY `q^(1/5)` PER GENERATION / SAME-MATERIAL GROWTH REQUIRES VISCOUS FLUX AND FORCES DIVERGENT NORMALIZED PALINSTROPHY UNDER REGULAR TUBE GEOMETRY / NO-H CORRIDOR THEREFORE FORCES MATERIAL RECRUITMENT/TURNOVER / GLOBAL REGULARITY UNPROVED.**

## 1. Why circulation is worth testing

Physical kinetic-energy cost of one shrinking first-hitting packet may be geometrically summable. We therefore seek a quantity whose required size does not decay with generation.

For the saturated affine shield,

\[
W_j\asymp r_j^{-2},
\qquad
 d_j\asymp r_j^{4/5}.
\]

Take a coherent cross-section transverse to the local vorticity axis, with area comparable to `d_j^2`. Its signed vorticity flux/circulation is

\[
\Gamma_j
:=
\int_{\Sigma_j}\omega\cdot n\,dS.
\]

On the coherent affine corridor,

\[
\boxed{
|\Gamma_j|
\gtrsim
W_jd_j^2
\asymp
r_j^{-2/5}.
}
\]

## 2. Geometric growth per first-hitting generation

With

\[
r_{j+1}=q^{-1/2}r_j,
\]

we have

\[
\boxed{
\frac{|\Gamma_{j+1}|}{|\Gamma_j|}
\asymp q^{1/5}.
}
\]

Therefore a comparable same-sign shield requires an increment

\[
\boxed{
|\Delta\Gamma_j|
\gtrsim
(q^{1/5}-1)r_j^{-2/5}.
}
\]

Unlike the packet kinetic-energy cost, this increment grows as `j -> infinity`.

## 3. Material versus geometric cross-section

The shield boundary is not automatically material; M5-351 in fact showed that comparable saturated shields force fixed-fraction material replacement.

Thus there are two basic ways to produce the larger next-stage circulation:

### A. Recruitment / replacement

The next geometric shield is spanned by a different material population or incorporates new vorticity flux from outside the old material tube.

This is

\[
\boxed{T_{adv/recruit}.}
\]

### B. Same-material circulation growth

A coherent material loop/surface persists and its circulation increases.

For a material loop `C(t)`, the Navier--Stokes Kelvin identity is

\[
\boxed{
\frac d{dt}\oint_{C(t)}u\cdot dl
=
\nu\oint_{C(t)}\Delta u\cdot dl.
}
\]

Equivalently, through a material spanning surface, the circulation can change only by viscous vorticity flux.

Hence the inviscid stretching geometry cannot by itself increase circulation of the same material loop.

## 4. Mollified material-flux test

A literal surface estimate introduces trace norms. Instead take a smooth co-moving flux test `psi_j` supported in a tube of transverse radius/thickness comparable to `d_j` and normalized so that

\[
\int\omega\cdot\psi_j\,dx
\asymp
\Gamma_j.
\]

For a regular comparable tube,

\[
|\psi_j|\asymp d_j^{-1},
\qquad
|\nabla\psi_j|\asymp d_j^{-2}
\]

on volume `~d_j^3`, so

\[
\boxed{
\|\nabla\psi_j\|_2
\asymp d_j^{-1/2}.
}
\]

Choose the co-moving test according to the material 2-form transport so that the inviscid vorticity-transport/stretching contribution is absorbed into the motion of the test. If the test deformation ceases to remain comparable, that is itself axis/shape/turnover `H/T` and exits this quiet tube corridor.

The remaining circulation change is viscous:

\[
|\Delta\Gamma_j|
\lesssim
\nu\int_{I_j}
\|\nabla\omega(t)\|_{L^2(N_j(t))}
\|\nabla\psi_j(t)\|_2dt.
\]

Hence, under the regular-tube bound on `psi_j`,

\[
|\Delta\Gamma_j|
\lesssim
\nu d_j^{-1/2}|I_j|^{1/2}
\left(
\int_{I_j}\!\!\int_{N_j(t)}|\nabla\omega|^2dxdt
\right)^{1/2}.
\]

Therefore

\[
\boxed{
\int_{I_j}\!\!\int_{N_j(t)}|\nabla\omega|^2dxdt
\gtrsim
\frac{|\Delta\Gamma_j|^2d_j}{\nu^2|I_j|}.
}
\]

## 5. Insert saturated shield scales

Use

\[
|\Delta\Gamma_j|\gtrsim c_q r_j^{-2/5},
\qquad
 d_j\asymp r_j^{4/5}.
\]

On a critical-clock first-hitting stage,

\[
|I_j|\asymp r_j^2
\]

up to fixed normalized stage-length constants. Then

\[
\frac{|\Delta\Gamma_j|^2d_j}{|I_j|}
\asymp
\frac{r_j^{-4/5}r_j^{4/5}}{r_j^2}.
\]

Thus

\[
\boxed{
\int_{I_j}\!\!\int_{N_j(t)}|\nabla\omega|^2dxdt
\gtrsim
c(q,\nu)r_j^{-2}.
}
\]

## 6. Normalized interpretation

Under first-hitting scaling

\[
U_j(Y,\tau)=r_j u(X_j+r_jY,t_j+r_j^2\tau),
\]

\[
\Omega_j=r_j^2\omega,
\qquad
\nabla_Y\Omega_j=r_j^3\nabla_x\omega.
\]

Therefore

\[
\int|\nabla_Y\Omega_j|^2dYd\tau
=
r_j
\int|\nabla_x\omega|^2dxdt.
\]

The viscous-circulation lower bound becomes

\[
\boxed{
\int_{\widehat I_j}\!\!\int
|\nabla_Y\Omega_j|^2dYd\tau
\gtrsim
c(q,\nu)r_j^{-1}
\to\infty.
}
\]

Thus same-material circulation amplification is not merely an order-one critical palinstrophy event. It forces **diverging normalized palinstrophy**.

This is a strong `H_freq/H_der` exit.

## 7. No-H consequence

On any no-H corridor with a uniform normalized palinstrophy/derivative ceiling, the same-material viscous alternative is impossible for all sufficiently late stages.

Therefore

\[
\boxed{
\text{saturated affine circulation growth}
+	ext{no-H}
\Longrightarrow
T_{adv/recruit}.
}
\]

In words: if high derivatives are not allowed to explode, the growing circulation of the next shield must be obtained by recruiting/replacing material rather than by viscously increasing the circulation of the old material loop.

## 8. Axis-property alternatives

The derivation assumes a coherent signed cross-sectional flux. It exits to existing H/T channels if

- the vorticity axis loses coherence;
- positive and negative flux cancel strongly;
- the cross-section becomes extremely distorted;
- the material loop leaves the shield;
- the co-moving test develops large gradients beyond `d_j^{-1/2}`.

Thus the exhaustive structural statement is

\[
\boxed{
\Gamma_{j+1}/\Gamma_j\sim q^{1/5}
\Longrightarrow
T_{recruit/axis/shape}
\lor
H_{viscous-palinstrophy}.
}
\]

## 9. Why this is stronger than the energy ledger

The required circulation increment has size

\[
|\Delta\Gamma_j|\sim r_j^{-2/5}\to\infty.
\]

Thus the charge itself grows toward small scales, whereas packet kinetic-energy costs can decay geometrically.

This makes circulation a more promising descriptor for descendant-tree/nonrepeatability arguments.

## 10. Firewall

Do not use a closed sphere as the circulation surface: `div omega=0` makes the total vorticity flux through every closed surface zero. The relevant object is a coherent cross-sectional surface with a material boundary loop.

Do not assume the geometric shield cross-section is material. Failure of material persistence is exactly the recruitment/turnover alternative.

The bulk palinstrophy bound in Section 5 is conditional on regular comparable co-moving tube geometry. Degeneration of that geometry is retained as H/T rather than ignored.

## 11. Audit verdict

### PROVED ON THE REGULAR COHERENT-FLUX CORRIDOR

- shield circulation scale `Gamma_j ~ r_j^(-2/5)`;
- per-generation growth factor `q^(1/5)`;
- material Kelvin identity routes growth to viscosity;
- regular mollified flux-tube estimate converts viscous growth into normalized palinstrophy `>= c r_j^(-1)`;
- therefore no-H forces material recruitment/turnover.

### OPEN

- global contradiction from repeated recruitment/turnover;
- circulation-tree packing after material replacement;
- cancellation/fragmentation of signed flux;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]