# DSD M19-134 — If the scattering-observable hard bundle integrates to a compact center manifold, the recurrent flow reduces to a finite-dimensional torus isometry

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / CONDITIONAL NONLINEAR UPGRADE OF M19-133 / A COMPACT FINITE-DIMENSIONAL CENTER MANIFOLD WITH SCATTERING-PULLBACK METRIC CARRIES AN ISOMETRIC ONE-PARAMETER FLOW / THE CLOSURE OF THAT FLOW IS A COMPACT ABELIAN LIE GROUP AND ORBIT CLOSURES ARE FINITE-DIMENSIONAL TORI / GENERAL APERIODIC RECURRENCE IS REDUCED TO FINITE-RANK QUASIPERIODIC RECURRENCE / THE CENTER-MANIFOLD AND NONLINEAR-IMMERSION GATES REMAIN EXPLICIT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. What M19-133 proves and what it does not

M19-133 proves an exact isometry on the **linearized observable hard bundle**:

\[
\|\Phi_t(U)v\|_{sc,\sigma_tU}
=
\|v\|_{sc,U}.
\]

This by itself does not imply that the nonlinear recurrent set is a torus or even a smooth manifold.

To upgrade the linear result, assume the following additional gates.

### Gate A: finite-dimensional center manifold

There exists a compact finite-dimensional invariant manifold `M_c` containing the recurrent hard orbit and tangent to the certified complete observable neutral bundle.

### Gate B: nonlinear scattering immersion

The nonlinear scattering map restricted to `M_c`,

\[
\mathscr S|_{M_c}:M_c\to X_{sc},
\]

is a `C^1` immersion with uniformly injective derivative.

The M19-131 observability lower bound is the tangent-level input for this gate.

### Gate C: translation-invariant target metric

The scattering space carries a translation-invariant norm/metric on the image of `M_c`.

---

## 2. Pull back the scattering metric nonlinearly

For `U_1,U_2` sufficiently close in `M_c`, define the local scattering distance

\[
d_{sc}(U_1,U_2)
:=
\|\mathscr S(U_1)-\mathscr S(U_2)\|_{X_{sc}}.
\]

Because the scattering map is a uniformly immersive `C^1` map on a compact finite-dimensional manifold, this local metric is uniformly equivalent to any retained smooth manifold metric.

Exact nonlinear covariance gives

\[
\mathscr S(\sigma_tU)=T_{-t/2}\mathscr S(U).
\]

Hence

\[
\begin{aligned}
d_{sc}(\sigma_tU_1,\sigma_tU_2)
&=
\|T_{-t/2}\mathscr S(U_1)-T_{-t/2}\mathscr S(U_2)\|_{X_{sc}}\\
&=
d_{sc}(U_1,U_2).
\end{aligned}
\]

Thus the recurrent flow restricted to `M_c` is a local isometry in the scattering-pullback metric.

After the standard compact-manifold completion of the metric, the time maps form a one-parameter subgroup of the isometry group of `M_c`.

---

## 3. Compact closure of the time flow

The isometry group of a compact finite-dimensional Riemannian manifold is a compact Lie group.

The closure of the one-parameter subgroup

\[
\{\sigma_t|_{M_c}:t\in\mathbb R\}
\]

inside that compact Lie group is compact and abelian.

Its identity component is therefore a torus:

\[
\boxed{
G_0\simeq\mathbb T^d
}
\]

for some finite `d`.

Hence every connected orbit closure of the recurrent center flow is a homogeneous torus quotient and, after removing a finite isotropy group, is represented by a linear torus flow.

---

## 4. Recurrent dynamics becomes finite-rank quasiperiodic

In angle variables

\[
\varphi\in\mathbb T^d,
\]

the flow has the form

\[
\boxed{
\varphi(t)=\varphi_0+t\omega
\pmod{2\pi}
}
\]

for a fixed frequency vector

\[
\omega\in\mathbb R^d.
\]

Therefore the recurrent center dynamics is one of:

1. an equilibrium/relative equilibrium (`omega=0` modulo isotropy);
2. a periodic/relative-periodic orbit (rational frequency relations);
3. a finite-rank quasiperiodic torus orbit (at least two rationally independent frequencies).

In particular, arbitrary chaotic/hyperbolic recurrence is excluded **once the nonlinear isometric-center gates hold**.

This is consistent with M19-120 because the present conclusion uses much more than one-dimensional center: it uses M19-132/133 isometry plus a compact nonlinear center manifold.

---

## 5. Consequence for the scattering datum

Because scattering is an equivariant factor,

\[
\mathscr S(\sigma_tU)
=
T_{-t/2}\mathscr S(U),
\]

while the center orbit is

\[
\varphi(t)=\varphi_0+t\omega,
\]

there exists a smooth center observable

\[
\mathcal A:\mathbb T^d\times S^2\to\mathbb R^3
\]

such that the leading critical scattering history may be written schematically as

\[
\boxed{
A(q,\omega_{S^2})
=
\mathcal A(\varphi_0-2q\,\omega,\omega_{S^2}).
}
\]

Thus the `q`-history is finite-rank quasiperiodic.

Its Bohr frequencies belong to the finitely generated additive group

\[
\boxed{
\Gamma_q
=
\{ -2k\cdot\omega : k\in\mathbb Z^d\}.
}
\]

This is a much narrower class than arbitrary bounded recurrent `q`-history.

---

## 6. Exact RSS/RDSS are the low-rank special cases

For `d=1`:

- rational closure gives periodic or relative-periodic dynamics, hence DSS/RDSS;
- a continuous one-frequency group drift gives the RSS spiral normal form of M19-125.

For `d>=2`, the new genuinely aperiodic hard core is a finite-rank quasiperiodic scattering torus.

Hence the analytic menu becomes

\[
\boxed{
\mathcal R_{critical}^{recurrent}
\Longrightarrow
\mathcal R_{RSS/RDSS}
\lor
\mathcal R_{QP}^{finite-rank}
\lor
\text{failure of the nonlinear isometric-center gates}.
}
\]

---

## 7. What remains to prove

The module is conditional because the following are not yet certified globally:

1. integration of the observable zero-growth hard bundle to a compact invariant `C^1` center manifold;
2. nonlinear scattering immersion with a uniform lower derivative bound on that manifold;
3. compatibility of the pulled-back scattering metric with the required global manifold topology.

Failure of any of these conditions must remain an explicit branch.

The next useful calculation is to analyze the finite-rank quasiperiodic ansatz itself and determine whether the Navier--Stokes correction hierarchy or pressure coupling creates a resonance/solvability obstruction unavailable for arbitrary recurrent histories.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
