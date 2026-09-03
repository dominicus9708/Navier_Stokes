# DSD M17-023 — Regular kappa-zero contours are q-levels and double zeros are radial extrema

Date: 2026-09-03
Canonical ID: **M17-023**

Status: **INTERNAL KAPPA-CONTOUR GEOMETRY / IN THE GREAT-CIRCLE SYSTEM `kappa=F_q(q,x_3,theta)`, SO AT A SIMPLE ROOT `F_qq != 0` EVERY REGULAR HORIZONTAL KAPPA-ZERO COMPONENT IS A Q-LEVEL CURVE. ITS TANGENT IS THE HORIZONTAL VORTICITY `W_h=J grad_h q`. THE ANGULAR DEFECT HAS THE EXACT GEOMETRIC FORM `chi=Lq=x_h dot W_h=r W_r`; ALONG A Q-CONTOUR `chi=r|W| dr/ds`. THEREFORE A DOUBLE ZERO `chi=kappa=0` IS EXACTLY A RADIAL EXTREMUM OF THE KAPPA-ZERO CONTOUR. THE TRANSVERSALITY CONDITION `grad chi x grad kappa != 0` IS EQUIVALENT TO A NONDEGENERATE RADIAL EXTREMUM, WHILE THE M17-021 TANGENCY EVENT IS A DEGENERATE RADIAL EXTREMUM WHERE `d^2r/ds^2=0`. THUS DOUBLE-ZERO RECONNECTION IS A MORSE-TYPE CHANGE OF THE RADIAL-EXTREMUM PATTERN OF THE KAPPA TRANSITION CONTOUR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Semilinear multiplier geometry

M17-004/013 gives on every regular great-circle region

\[
\boxed{
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q(q,x_3,\theta).
}
\]

Fix `x_3` and `theta`.
A simple kappa root is a value `q_*(x_3,theta)` satisfying

\[
F_q(q_*,x_3,\theta)=0,
\qquad
F_{qq}(q_*,x_3,\theta)\ne0.
\]

By the implicit function theorem, the root is locally a smooth label value.

---

## 2. Regular horizontal kappa-zero set is a q-level curve

On the simple-root branch,

\[
\boxed{
\kappa=0
\iff
q=q_*(x_3,\theta)
}
\]

locally in the horizontal slice.

Also

\[
\boxed{
\nabla_h\kappa
=F_{qq}\nabla_hq.
}
\]

Thus the horizontal normals of the two level sets are parallel.
The tangent to the `q` contour is

\[
\boxed{
W_h=J\nabla_hq.
}
\]

Hence

\[
W_h\cdot\nabla_h\kappa=0,
\]

and the regular `kappa=0` contour is a vortex-line contour in each horizontal slice.

---

## 3. Exact radial meaning of the angular defect

With

\[
\mathcal L=x_1\partial_2-x_2\partial_1,
\]

M17-016 defines

\[
\chi=\mathcal Lq.
\]

Using

\[
W_h=(q_2,-q_1),
\]

we have

\[
\boxed{
\chi
=x_1W_1+x_2W_2
=x_h\cdot W_h.
}
\]

In polar coordinates,

\[
\boxed{
\chi=rW_r.
}
\]

Thus the non-axisymmetric angular defect is exactly radius times the radial horizontal-vorticity component.

The axisymmetric no-swirl firewall has purely azimuthal horizontal vorticity and therefore

\[
\chi=0.
\]

---

## 4. Radial derivative along a q contour

Let a regular `q`-level curve be parametrized by arclength `s` and orient its unit tangent by

\[
t=\frac{W_h}{|W_h|}.
\]

The radial coordinate obeys

\[
\frac{dr}{ds}
=t\cdot e_r
=\frac{W_r}{|W_h|}.
\]

Since

\[
W_r=\frac\chi r,
\]

we obtain

\[
\boxed{
\frac{dr}{ds}
=\frac{\chi}{r|W_h|}.
}
\]

Equivalently,

\[
\boxed{
\chi
=r|W_h|\frac{dr}{ds}.
}
\]

This is an exact contour-geometric representation of the angular defect.

---

## 5. Double zero equals radial extremum

On a regular `kappa=0` contour,

\[
q=q_*.
\]

At a point where additionally

\[
\chi=0,
\]

we have

\[
\boxed{
\frac{dr}{ds}=0.
}
\]

Therefore

\[
\boxed{
\{\chi=0\}\cap\{\kappa=0\}
}
\]

consists, on a regular horizontal simple-root contour, of the radial extrema of that contour relative to the candidate symmetry axis.

At such a point the contour tangent is purely azimuthal and its normal is radial.

---

## 6. Transversality equals nondegenerate radial extremum

Differentiate

\[
\chi
=r|W_h|\frac{dr}{ds}
\]

along the contour.
At a double zero, `dr/ds=0`, so the product-rule terms proportional to `dr/ds` vanish and

\[
\boxed{
\frac{d\chi}{ds}
=r|W_h|\frac{d^2r}{ds^2}.
}
\]

The contour tangent is perpendicular to `grad_h kappa`.
Thus

\[
\nabla_h\chi
\parallel
\nabla_h\kappa
\]

exactly when the tangential derivative of `chi` vanishes:

\[
\frac{d\chi}{ds}=0.
\]

Consequently

\[
\boxed{
\nabla_h\chi\times\nabla_h\kappa\ne0
\iff
\frac{d^2r}{ds^2}\ne0.
}
\]

A transverse double zero is a nondegenerate radial maximum or minimum.

---

## 7. Tangency equals degenerate radial extremum

M17-021 isolates tangency of the two zero surfaces by

\[
\nabla\chi\parallel\nabla\kappa.
\]

On the horizontal simple-root contour this becomes

\[
\boxed{
\frac{d^2r}{ds^2}=0
}
\]

at a point already satisfying

\[
\frac{dr}{ds}=0.
\]

Thus the double-zero tangency is precisely a degenerate radial extremum.

It is the natural Morse-type event at which radial maxima/minima can be created, annihilated, or exchange connectivity.

---

## 8. Stability of the radial-extremum count under transversality

Consider a smooth closed regular `kappa=0` contour on a horizontal slice.
Its radial coordinate `r(s)` is periodic.
Every nondegenerate critical point of `r` persists under a sufficiently small smooth deformation.

Therefore, as long as

\[
\boxed{
\nabla\chi\times\nabla\kappa\ne0
}
\]

at every double zero, the number of radial extrema on that contour is locally constant in time.

The count can change only through

1. a tangency/degenerate radial extremum;
2. loss of regularity of the `kappa=0` contour;
3. contour creation/destruction or reconnection through a critical level.

Thus M17-021's geometric rank split has a direct contour-topology meaning.

---

## 9. Relation to the harmonic angular jet

M17-019 shows that the first nonzero angular defect jet has harmonic order `m` and creates `2m` alternating local defect sectors near the core.

For a simple closed `kappa=0` contour that intersects those sectors before they globally reconnect, the double-zero points are radial extrema separating outward- and inward-moving portions of the contour.

The local `2m` sector count therefore provides the natural inner boundary data for the radial-extremum network.

However, without a no-reconnection hypothesis it is not yet valid to assert that one outer contour has exactly `2m` extrema.

---

## 10. Material crossing velocity in q-root variables

At a simple root define

\[
q_*=q_*(x_3,\theta).
\]

The material relative motion of a point across the root label is

\[
\boxed{
V_q
:=D_B(q-q_*)
=H-q_{*,\theta}-Kq_{*,3}.
}
\]

Differentiating

\[
F_q(q_*,x_3,\theta)=0
\]

gives

\[
q_{*,\theta}
=-\frac{F_{q\theta}}{F_{qq}},
\qquad
q_{*,3}
=-\frac{F_{q3}}{F_{qq}}.
\]

Therefore at `kappa=0`,

\[
\boxed{
h
=D_B\kappa
=F_{qq}V_q.
}
\]

Thus the M5-685 upward/downward kappa crossing is exactly the material crossing of the semilinear `q` label through the root contour.

---

## 11. Normal velocity of the kappa contour

Because

\[
\nabla_h\kappa=F_{qq}\nabla_hq,
\]

we have

\[
|\nabla_h\kappa|
=|F_{qq}|\,|\nabla_hq|.
\]

The material-relative normal velocity of the kappa-zero contour is

\[
(v_\kappa-B)\cdot n_\kappa
=-\frac{h}{|\nabla\kappa|}.
\]

On a horizontally regular simple root this reduces to

\[
\boxed{
(v_\kappa-B)\cdot n_\kappa
=-\operatorname{sgn}(F_{qq})
\frac{V_q}{|\nabla_hq|}
}
\]

up to the full-space normal correction if the zero surface has axial slope.

This connects the M5 hysteresis current directly to motion of the radial-extremum-carrying contour.

---

## 12. DSD interpretation

### 12.1 Scalar label becomes geometric contour
The multiplier root is not an arbitrary spatial sheet in the rank-one branch; horizontally it is a semilinear `q` contour.

### 12.2 Angular defect becomes contour deformation
`chi` measures the radial component of the vortex tangent, hence the failure of the contour to remain circular around the candidate axis.

### 12.3 Tangency becomes Morse event
The abstract rank loss of the double-zero map is the concrete degeneration of a radial maximum/minimum of the `kappa=0` contour.

---

## 13. DSD audit

### Audit A — every kappa=0 point is a simple q root
Rejected.
The contour reduction uses `F_qq != 0` and horizontal regularity.
Multiple roots form a separate critical-label branch.

### Audit B — every kappa-zero component is closed
Rejected.
Open/unbounded contours are allowed and belong to a separate geometry/tail branch.

### Audit C — equating local 2m sector count with global contour extrema count
Rejected without a no-reconnection hypothesis.

### Audit D — full 3D and horizontal normals
Distinguished.
The exact q-level statement is horizontal at fixed `x_3`; axial slope can tilt the full three-dimensional kappa-zero surface.

### Audit E — proof status
No contradiction is claimed.

---

## 14. Updated contour frontier

The regular simple-root branch now has the geometric representation

\[
\boxed{
\kappa=0
\iff
q=q_*(x_3,\theta),
}
\]

\[
\boxed{
\chi=r|W_h|\frac{dr}{ds},
}
\]

and

\[
\boxed{
\chi=\kappa=0
\iff
\text{radial extremum of the kappa-zero q contour}.
}
\]

The double-zero network is therefore a moving radial-extremum skeleton of the internal payer-transition contour.

---

## 15. Next target — persistent contour-extremum network

The next calculation is to combine

1. fixed radial-extremum count under transverse recurrence;
2. the strict signed angular-boundary turnover of M17-020;
3. the directed q-root crossing bias `h=F_qq V_q` from M5-685/M17-013;
4. the bounded-lobe spectral payer of M17-022.

The goal is to determine whether a closed noncircular kappa-zero contour can recur without a degenerate radial-extremum event or a multiple-root event `F_qq=0`.

This is the **Persistent Contour-Extremum Gate (PCEG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
