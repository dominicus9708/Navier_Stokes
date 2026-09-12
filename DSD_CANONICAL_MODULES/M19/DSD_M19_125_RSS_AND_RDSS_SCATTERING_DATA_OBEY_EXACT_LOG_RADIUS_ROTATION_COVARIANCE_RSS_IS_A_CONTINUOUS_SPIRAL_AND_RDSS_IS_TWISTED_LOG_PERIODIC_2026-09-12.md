# DSD M19-125 — RSS and RDSS scattering data obey exact log-radius rotation covariance: RSS is a continuous spiral and RDSS is twisted log-periodic

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT COMBINATION OF M5-567 SCATTERING-TIME COVARIANCE WITH ROTATION EQUIVARIANCE / THE RSS CRITICAL TAIL IS NOT AN ARBITRARY Q-HISTORY BUT A CONTINUOUS LOG-RADIUS ROTATION ORBIT; RDSS DATA SATISFY A TWISTED LOG-PERIODIC BOUNDARY CONDITION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. General scattering covariance

On the controlled passive spectator branch, M5-567 gives

\[
U_Y(y,s)
=
\frac1rA_Y(q,\omega)+O(r^{-3}),
\qquad
q=\log r-\frac s2,
\]

and exact time-shift covariance

\[
\boxed{
A_{\sigma_tY}(q,\omega)
=
A_Y(q-t/2,\omega).
}
\]

The scattering construction is also rotation-equivariant. If `Q in SO(3)` acts on vector fields by

\[
(Q\cdot U)(y)=Q\,U(Q^{-1}y),
\]

then

\[
\boxed{
A_{Q\cdot Y}(q,\omega)
=
Q\,A_Y(q,Q^{-1}\omega).
}
\]

Denote the infinitesimal rotation action on angular vector data by

\[
\boxed{
\mathcal R_\omega A
:=
A_0 A-(A_0\omega)\cdot\nabla_\omega A,
}
\]

for a fixed axis generator `A_0 in so(3)`.

---

## 2. RSS relative equilibrium

For an RSS orbit with angular rate `alpha`,

\[
\boxed{
\sigma_tY
=Q_{\alpha t}\cdot Y,
\qquad
Q_{\alpha t}=e^{\alpha tA_0}.
}
\]

Apply the two covariance laws:

\[
A_Y(q-t/2,\omega)
=
Q_{\alpha t}
A_Y(q,Q_{-\alpha t}\omega).
\]

Equivalently,

\[
\boxed{
A(q-t/2)
=Q_{\alpha t}\cdot A(q).
}
\]

Set

\[
h=-t/2.
\]

Then

\[
\boxed{
A(q+h)
=Q_{-2\alpha h}\cdot A(q).
}
\]

Thus translation in log-radius scattering coordinate is exactly compensated by spatial rotation.

---

## 3. Differential spiral law

Differentiate the preceding identity at

\[
h=0.
\]

This gives

\[
\boxed{
\partial_qA
=-2\alpha\mathcal R_\omega A.
}
\]

Hence

\[
\boxed{
A(q)
=e^{-2\alpha q\mathcal R_\omega}A(0)
}
\]

up to the arbitrary choice of the `q=0` reference phase.

Therefore the entire leading critical RSS tail is determined by **one angular profile** and the rotation rate.

It is a continuous logarithmic spiral in the combined log-radius/angular variables.

---

## 4. Immediate invariant consequences

Rotation preserves angular `L^p` norms. Therefore for every `p` for which the angular norm is defined,

\[
\boxed{
\|A(q,\cdot)\|_{L^p(S^2)}
=
\|A(0,\cdot)\|_{L^p(S^2)}
}
\]

for all `q`.

Likewise every rotation-invariant angular quadratic quantity is constant in `q`.

Thus a nonzero RSS critical tail has a **constant cubic-mass density per unit log radius**:

\[
\boxed{
\int_{S^2}|A(q,\omega)|^3d\omega
\equiv
\mathcal C_3>0.
}
\]

Consequently

\[
\int_{1<|y|<R}|U|^3dy
=
\mathcal C_3\log R+O(1).
\]

This is the continuous-spiral analogue of the DSS periodic cubic slope.

---

## 5. Angular Fourier interpretation

Around the rotation axis, decompose the angular datum into azimuthal modes.

For an eigenmode of the angular rotation generator with integer azimuthal charge `m`, schematically

\[
\mathcal R_\omega A_m
=im A_m.
\]

Then

\[
\boxed{
A_m(q)
=e^{-2im\alpha q}A_m(0).
}
\]

Thus each nonaxisymmetric angular mode acquires a fixed linear phase in log radius.

The radial logarithmic frequency is exactly

\[
\boxed{k_q=-2m\alpha.}
\]

Axisymmetric modes `m=0` are independent of `q` at leading order.

This gives a direct spectral meaning to the dilation-rotation chirality of M19-124.

---

## 6. Relation to the M19-124 chirality term

At leading critical order, the skew dilation generator acts on the scaled radial profile through log-radius differentiation, while the rotation generator acts through `R_omega`.

The RSS spiral law identifies these actions:

\[
\boxed{
\partial_qA
=-2\alpha\mathcal R_\omega A.
}
\]

Therefore the far-field contribution to the dilation-rotation quadratic form is not arbitrary: it is proportional to `alpha` times a positive rotational-anisotropy density, with a sign fixed by the convention for the two generators.

A complete evaluation requires the exact radial cutoff/renormalization because the critical `1/r` tail is not globally `L2` in velocity.

Hence this module does not yet insert the formal tail directly into the global unweighted torque identity of M19-124.

But it shows that the chirality term is the natural carrier of the RSS log-spiral phase.

---

## 7. RDSS twisted log-periodicity

For RDSS,

\[
\sigma_SY
=Q_*\cdot Y,
\qquad
S=2L.
\]

The scattering covariance gives

\[
A_Y(q-S/2)
=A_{\sigma_SY}(q)
=Q_*\cdot A_Y(q).
\]

Therefore

\[
\boxed{
A(q-L)
=Q_*\cdot A(q),
}
\]

or equivalently

\[
\boxed{
A(q+L)
=Q_*^{-1}\cdot A(q).
}
\]

This is **twisted log-periodicity**.

Ordinary DSS is the special case

\[
Q_*=I,
\]

which reduces to ordinary `L`-periodicity.

---

## 8. Untwisting the RDSS datum

Choose an axis-angle logarithm on one representation,

\[
Q_*=e^{S\alpha A_0}
=e^{2L\alpha A_0}.
\]

Define the co-rotating log-radius datum

\[
\boxed{
\widetilde A(q)
:=
e^{2\alpha q\mathcal R_\omega}A(q).
}
\]

Then

\[
\widetilde A(q+L)=\widetilde A(q).
\]

Thus every RDSS scattering datum can be represented as

\[
\boxed{
A(q)
=e^{-2\alpha q\mathcal R_\omega}
\widetilde A(q),
\qquad
\widetilde A(q+L)=\widetilde A(q),
}
\]

with the usual winding ambiguity in the chosen `alpha` representation described in M19-117.

This separates:

- continuous spiral rotation;
- genuine periodic modulation in log radius.

---

## 9. Representation-safe principal form

Using principal holonomy angle

\[
\beta\in[-\pi,\pi],
\qquad
Q_*=e^{\beta A_0},
\]

one may choose principal rate

\[
\alpha_{pr}=\frac\beta{2L}.
\]

Then

\[
\boxed{
A(q)
=e^{-(\beta/L)q\mathcal R_\omega}
\widetilde A(q),
\qquad
\widetilde A(q+L)=\widetilde A(q).
}
\]

This is the intrinsic twisted-periodic normal form.

---

## 10. New RSS/RDSS tail frontier

The periodic/relative-periodic critical tail is therefore far more rigid than a general recurrent datum:

\[
\boxed{
\begin{aligned}
\text{RSS: }&A(q)=e^{-2\alpha q\mathcal R_\omega}A_0,\\
\text{RDSS: }&A(q)=e^{-(\beta/L)q\mathcal R_\omega}\widetilde A(q),\quad \widetilde A(q+L)=\widetilde A(q).
\end{aligned}
}
\]

The next calculation should insert these exact forms into the divergence-free constraint and pressure equation to determine whether nonaxisymmetric spiral modes create a new algebraic/Fredholm obstruction at the leading critical level.

---

## 11. Firewall

The spiral/twisted-periodic normal form is an exact **necessary** consequence of relative self-similarity plus scattering covariance.

It is not by itself a Navier--Stokes Liouville theorem.

The leading critical equation remains transport-dominated, and subleading `r^-3` corrections may still accommodate nonlinear/pressure residuals.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
