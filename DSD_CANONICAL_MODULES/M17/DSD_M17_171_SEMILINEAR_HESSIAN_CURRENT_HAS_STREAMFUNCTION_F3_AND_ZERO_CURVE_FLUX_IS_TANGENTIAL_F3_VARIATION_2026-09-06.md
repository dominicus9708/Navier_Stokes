# DSD M17-171 — The semilinear Hessian current has streamfunction `F_3`; its `kappa=0` normal flux is exactly tangential variation of `F_3`

Date: 2026-09-06  
Canonical ID: **M17-171**

Status: **STRUCTURAL INTERPRETATION / THE M17-170 CURRENT `J_F=(F_33,-F_q3)` IS EXACTLY THE ROTATED GRADIENT `grad^perp F_3` IN THE `(q,x_3)` PLANE. CONSEQUENTLY ITS NORMAL FLUX ACROSS A REGULAR `kappa=F_q=0` CURVE IS THE TANGENTIAL DERIVATIVE OF `F_3`: `J_F dot n_kappa = d_s F_3 = [F_qq H_V-25 O_V^2/|Q|^4]/|grad kappa|`. THE CLOSED-LOOP SQUARE BALANCE OF M17-170 IS THEREFORE THE PERIODICITY IDENTITY `oint d_s F_3 ds=0`, NOT A SECOND INDEPENDENT CONSERVATION LAW. IT REMAINS USEFUL BECAUSE IT CONVERTS PERIODICITY INTO A POSITIVE INTEGRATED COVARIANCE `oint F_qq H_V/|grad kappa| = 25 oint O_V^2/(|Q|^4|grad kappa|)`, BUT IT MUST NOT BE DOUBLE-COUNTED AS AN EXTRA PDE CHARGE. OPEN COMPONENTS CARRY THE ENDPOINT DIFFERENCE `F_3(end)-F_3(start)` EXACTLY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-170

At fixed similarity time `theta`, the semilinear variables are

\[
(q,x_3),
\]

with

\[
\kappa=F_q.
\]

M17-170 defines

\[
\boxed{
\mathbf J_F=(F_{33},-F_{q3}).
}
\]

It satisfies

\[
\nabla_{(q,3)}\cdot\mathbf J_F=0.
\]

At a vertical crossing,

\[
F_{33}=H_V,
\qquad
F_{q3}=-\frac{5O_V}{|Q|_F^2}.
\]

---

## 2. Exact streamfunction representation

Let

\[
\Psi_F:=F_3=\partial_3F.
\]

In the coordinate ordering `(q,x_3)`, define

\[
\nabla^\perp\Psi_F
:=
(\partial_3\Psi_F,-\partial_q\Psi_F).
\]

Then

\[
\partial_3\Psi_F=F_{33},
\qquad
\partial_q\Psi_F=F_{q3}.
\]

Therefore

\[
\boxed{
\mathbf J_F=\nabla^\perp F_3.
}
\]

The divergence-free identity is therefore the elementary two-dimensional identity

\[
\nabla\cdot\nabla^\perp F_3=0.
\]

This clarifies the structural origin of M17-170.

---

## 3. Tangent and normal to the zero curve

Let

\[
\Gamma_0=\{F_q=0\}.
\]

At a regular point,

\[
\nabla\kappa=(F_{qq},F_{q3})\neq0.
\]

Choose

\[
\boxed{
\mathbf n_\kappa
=\frac{(F_{qq},F_{q3})}{|\nabla\kappa|}
}
\]

and the positively rotated unit tangent

\[
\boxed{
\mathbf t_\kappa
=\frac{(-F_{q3},F_{qq})}{|\nabla\kappa|}.
}
\]

Then `t_kappa` is tangent because

\[
\mathbf t_\kappa\cdot\nabla\kappa=0.
\]

---

## 4. Normal Hessian-current flux is tangential `F_3` derivative

Compute

\[
\begin{aligned}
\mathbf J_F\cdot\mathbf n_\kappa
&=\frac{F_{33}F_{qq}-F_{q3}^2}{|\nabla\kappa|}.
\end{aligned}
\]

On the other hand,

\[
\begin{aligned}
\mathbf t_\kappa\cdot\nabla F_3
&=\frac{-F_{q3}F_{q3}+F_{qq}F_{33}}{|\nabla\kappa|}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathbf J_F\cdot\mathbf n_\kappa
=\mathbf t_\kappa\cdot\nabla F_3
=\partial_sF_3,
}
\]

where `s` is oriented arc length along `Gamma_0`.

Using the vertical variables,

\[
\boxed{
\partial_sF_3
=
\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}
{|\nabla\kappa|}.
}
\]

---

## 5. Closed-loop identity is exact periodic variation

If `Gamma` is a closed regular component,

\[
\oint_\Gamma\partial_sF_3\,ds=0.
\]

Therefore

\[
\boxed{
\oint_\Gamma
\frac{F_{qq}H_V}{|\nabla\kappa|}ds
=
25\oint_\Gamma
\frac{O_V^2}{|Q|_F^4|\nabla\kappa|}ds.
}
\]

This is exactly M17-170.

The identity is not an independent new conservation law beyond smooth single-valuedness of `F_3` on the closed curve.

Nevertheless, because the right side is nonnegative, it is a nontrivial and useful rewriting of that periodicity:

\[
\boxed{
\int_\Gamma F_{qq}H_V\,d\nu_\Gamma
=25\int_\Gamma\frac{O_V^2}{|Q|_F^4}d\nu_\Gamma,
\qquad
d\nu_\Gamma=\frac{ds}{|\nabla\kappa|}.
}
\]

---

## 6. Open-component endpoint law

For an oriented regular zero arc `Gamma[a,b]`,

\[
\int_{\Gamma[a,b]}\partial_sF_3\,ds
=F_3(b)-F_3(a).
\]

Thus

\[
\boxed{
\int_{\Gamma[a,b]}
\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}
{|\nabla\kappa|}ds
=F_3(b)-F_3(a).
}
\]

Therefore the open-zero branch is not merely an unspecified boundary exit. Its exact missing charge is the endpoint variation of the semilinear axial derivative `F_3`.

Possible endpoints include:

1. chart/domain boundary;
2. spatial infinity in the reduced label plane;
3. zero-set critical point where `grad kappa=0`;
4. transition to another semilinear branch.

---

## 7. Relation to the critical-value curvature

When `F_qq != 0`, graph the zero curve as

\[
q=q_*(x_3).
\]

M17-169 defines

\[
\mathcal C_*(x_3)=F(q_*(x_3),x_3).
\]

Because `F_q=0` on the root,

\[
\mathcal C_{*,3}=F_3.
\]

Therefore

\[
\boxed{
\mathcal C_{*,33}
=\frac{d}{dx_3}F_3(q_*(x_3),x_3).
}
\]

The Schur complement

\[
\mathcal C_{*,33}
=F_{33}-\frac{F_{q3}^2}{F_{qq}}
\]

is just the derivative of the streamfunction `F_3` along the graph coordinate.

This unifies M17-169 and M17-170 without introducing a second independent object.

---

## 8. DSD audit

### Audit A — counting M17-170 as a new independent conserved charge
Rejected. `J_F` is a rotated gradient and the closed-loop flux vanishes kinematically.

### Audit B — discarding the positive square identity because it is kinematic
Rejected. The rewriting still forces a positive integrated pressure/root-curvature covariance whenever `O_V` is nonzero.

### Audit C — assuming `F_3` is periodic on open components
Rejected. The exact endpoint difference must be kept.

### Audit D — confusing arc length with M5 label measure
Rejected. `ds/|grad kappa|` remains a semilinear zero-curve coarea measure.

### Audit E — proof status
The identity is clarified and de-duplicated; no temporal contradiction follows yet.

---

## 9. Updated next gate

The semilinear pressure/octupole architecture is now summarized by

\[
\boxed{
\partial_sF_3
=
\frac{F_{qq}H_V-25O_V^2/|Q|_F^4}{|\nabla\kappa|}.
}
\]

The next problem is entirely a measure/space-time problem:

> can the M5 base-flux crossing current be pushed forward to this same semilinear zero curve with a controlled density, without identifying the original transverse-flux label measure with Lebesgue label area by fiat?

That bridge must be stated conditionally until a pushforward theorem from the M5 transverse atlas is proved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
