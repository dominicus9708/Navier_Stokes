# DSD M17-090 — The vertical local payer octupole collapses to an axial derivative; zero-crossing rate factorizes through relative velocity

Date: 2026-09-04
Canonical ID: **M17-090**

Status: **INTERNAL VERTICAL LOCAL OCTUPOLE / M5 CROSSING BRIDGE / ON A VERTICAL REGULAR GREAT-CIRCLE NODE, `kappa=F_q(q,x_3,theta)` AND `grad_h q=0` GIVE `grad_h kappa=0`, WHILE VERTICAL FILAMENT GEOMETRY GIVES `q_13=q_23=0`. HENCE `grad kappa=kappa_3 e_3`, THE VORTICITY JACOBIAN HAS `A e_3=0`, AND `A^T A=diag(Q^TQ,0)` WITH `Q=nabla_h^2q`. SUBSTITUTING THESE IDENTITIES INTO THE EXPLICIT M17-057 STF PAYER OCTUPOLE GIVES THE EXACT AXIAL COMPONENT `O_loc,333=-(1/5)[|Q|_F^2 kappa_3+kappa partial_3|Q|_F^2]=-(1/5)partial_3(kappa|Q|_F^2)`. AT A SPATIALLY REGULAR `kappa=0` CROSSING THIS REDUCES TO `O_loc,333=-(1/5)|Q|_F^2 kappa_3`, SO ITS SIGN IS THE OPPOSITE OF THE AXIAL SPATIAL CROSSING SLOPE. IF THE LOCAL ZERO SURFACE MOVES WITH AXIAL COORDINATE VELOCITY `v_0`, THEN `partial_theta kappa+v_0 kappa_3=0`, WHILE THE MATERIAL RATE IS `h=D_B kappa=partial_theta kappa+B_3 kappa_3`; THEREFORE `h=(B_3-v_0)kappa_3=-5(B_3-v_0)O_loc,333/|Q|_F^2`. THIS IDENTIFIES THE PRECISE MISSING SPACE-TIME FACTOR BETWEEN M5'S FLUX-WEIGHTED DOWNWARD-CROSSING BIAS AND THE VERTICAL LOCAL OCTUPOLE: THE RELATIVE VELOCITY OF MATERIAL LABELS THROUGH THE KAPPA-ZERO SURFACE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vertical regular nodal identities

Use the vertical great-circle representation

\[
W_h=J\nabla_hq,
\qquad
W_3=0,
\]

and center the vertical regular filament on the `x_3` axis.
At the filament,

\[
\boxed{
\nabla_hq=0,
\qquad
q_{13}=q_{23}=0.
}
\]

Define

\[
\boxed{Q:=\nabla_h^2q.}
\]

Regularity gives

\[
\det Q\neq0.
\]

---

## 2. The kappa gradient is purely axial at the filament

The semilinear branch has

\[
\kappa=F_q(q,x_3,\theta).
\]

For horizontal derivatives,

\[
\partial_a\kappa
=F_{qq}\partial_aq
\qquad(a=1,2).
\]

Since `grad_h q=0` on the filament,

\[
\boxed{
\nabla_h\kappa=0.
}
\]

Therefore

\[
\boxed{
\nabla\kappa
=\kappa_3 e_3
}
\]

at every vertical regular nodal point.

---

## 3. Vorticity Jacobian block structure

Let

\[
A:=\nabla W.
\]

Because

\[
W_h=J\nabla_hq,
\]

the horizontal block of `A` is

\[
\boxed{A_h=JQ.}
\]

The third column is

\[
A e_3
=\partial_3W
=J\partial_3\nabla_hq
=0
\]

because `q_13=q_23=0` on the vertical filament.
Also the third output row vanishes because `W_3=0` identically.
Hence

\[
\boxed{
A^TA
=
\begin{pmatrix}
Q^TQ&0\\
0&0
\end{pmatrix}.
}
\]

Consequently

\[
\boxed{
|A|_F^2=|Q|_F^2,
\qquad
(A^TA)e_3=0.
}
\]

---

## 4. Insert the vertical identities into M17-057

M17-057 gives the cubic payer tensor before STF projection as

\[
T=T^{(\kappa)}+T^{(W)}
\]

with trace vector

\[
 t
=\frac13\left[
2Ck+(\operatorname{tr}C)k
+\kappa\nabla|A|_F^2
\right],
\]

where

\[
C=A^TA,
\qquad
k=\nabla\kappa.
\]

The STF tensor is

\[
\mathcal O_{loc}^{(3)}
=T-\frac15sym(\delta\otimes t).
\]

On the vertical filament,

\[
k=\kappa_3e_3,
\qquad
Ce_3=0.
\]

Therefore

\[
(Ck)_3=0,
\qquad
\operatorname{tr}C=|Q|_F^2.
\]

Thus

\[
\boxed{
 t_3
=\frac13\left[
|Q|_F^2\kappa_3
+\kappa\partial_3|Q|_F^2
\right].
}
\]

---

## 5. The raw cubic 333 coefficient vanishes

For the multiplier-gradient term,

\[
T_{333}^{(\kappa)}
=\kappa_3 C_{33}=0.
\]

For the vorticity-curvature term,

\[
T_{333}^{(W)}
=\kappa A_{a3}B_{a33}=0
\]

because

\[
A_{a3}=0.
\]

Hence

\[
\boxed{T_{333}=0.}
\]

The entire axial STF component comes from removal of the trace/ℓ=1 part.

---

## 6. Exact vertical local octupole formula

For three equal indices,

\[
(STF_3T)_{333}
=T_{333}-\frac35t_3.
\]

Using Sections 4--5,

\[
\boxed{
(\mathcal O_{loc}^{(3)})_{333}
=-\frac15\left[
|Q|_F^2\kappa_3
+\kappa\partial_3|Q|_F^2
\right].
}
\]

Equivalently,

\[
\boxed{
(\mathcal O_{loc}^{(3)})_{333}
=-\frac15\partial_3\left(
\kappa|Q|_F^2
\right).
}
\]

Thus the first local vertical octupole of the scalar kappa-payer density is an exact axial derivative.

---

## 7. Spatially regular kappa-zero crossing

At a zero crossing,

\[
\kappa=0.
\]

If it is spatially regular at the vertical filament, then because `grad_h kappa=0`,

\[
\boxed{\kappa_3\neq0.}
\]

Section 6 reduces to

\[
\boxed{
(\mathcal O_{loc}^{(3)})_{333}
=-\frac15|Q|_F^2\kappa_3.
}
\]

Since regularity gives `|Q|_F^2>0`,

\[
\boxed{
\operatorname{sgn}(\mathcal O_{loc,333}^{(3)})
=-\operatorname{sgn}\kappa_3.
}
\]

This is the first genuine local sign relation between the vertical payer octupole and a kappa-crossing geometry.

---

## 8. Motion of the regular zero surface

Near a spatially regular vertical crossing, the implicit function theorem writes the local zero surface along the centered filament as

\[
\boxed{x_3=z_0(\theta)}
\]

with

\[
\kappa(0,0,z_0(\theta),\theta)=0.
\]

Define its axial coordinate velocity

\[
\boxed{v_0:=z_0'(\theta).}
\]

Differentiate the zero condition:

\[
\boxed{
\partial_\theta\kappa
+v_0\kappa_3
=0.
}
\]

---

## 9. Material crossing rate factorization

M5 uses the material crossing rate

\[
\boxed{h:=D_B\kappa.}
\]

At the vertical filament, the horizontal kappa gradient vanishes, so

\[
D_B\kappa
=\partial_\theta\kappa+B_3\kappa_3.
\]

Use Section 8:

\[
\boxed{
h
=(B_3-v_0)\kappa_3.
}
\]

This is the exact factorization of the temporal material crossing into

1. spatial zero-surface slope `kappa_3`;
2. material/zero-surface relative axial velocity `B_3-v_0`.

---

## 10. Exact local space-time octupole bridge at kappa=0

Use Section 7 to eliminate `kappa_3`:

\[
\kappa_3
=-\frac{5}{|Q|_F^2}
(\mathcal O_{loc}^{(3)})_{333}.
\]

Then Section 9 becomes

\[
\boxed{
h
=-\frac{5(B_3-v_0)}{|Q|_F^2}
(\mathcal O_{loc}^{(3)})_{333}.
}
\]

Equivalently,

\[
\boxed{
(\mathcal O_{loc}^{(3)})_{333}
=-\frac{|Q|_F^2}{5(B_3-v_0)}h
}
\]

when the relative velocity is nonzero.

The division-free product form in the first boxed equation is canonical and remains valid even when `B_3-v_0=0`.

---

## 11. What M5 hysteresis now does and does not imply

M5-685 requires the flux-weighted crossing population to be biased toward

\[
h<0.
\]

M17-090 shows that at a regular vertical crossing this is equivalent to

\[
(B_3-v_0)
(\mathcal O_{loc}^{(3)})_{333}>0
\]

because `|Q|_F^2>0` and the numerical prefactor is negative in the formula for `h`.

Thus the missing factor is explicit:

\[
\boxed{
\text{M5 downward-crossing bias}
\Longrightarrow
\text{bias of }(B_3-v_0)\,\mathcal O_{loc,333}^{(3)},
}
\]

not a bias of `O_loc,333` alone.

To infer the octupole sign itself one must control

\[
\boxed{\operatorname{sgn}(B_3-v_0).}
\]

---

## 12. Degenerate crossing exit

If

\[
\kappa_3=0
\]

at `kappa=0`, then because the horizontal gradient already vanishes,

\[
\boxed{\nabla\kappa=0.}
\]

The spatial zero surface is critical/degenerate and the graph velocity `v_0` above is not defined by first-order implicit geometry.

This is a separate kappa-zero degeneration branch and must not be inserted into the regular factorization by division.

---

## 13. DSD analysis

The vertical local bridge now has a clean descriptor chain:

\[
\boxed{
\kappa_3
\leftrightarrow
\mathcal O_{loc,333}^{(3)}
\leftrightarrow
h/(B_3-v_0).
}
\]

The scalar temporal crossing rate and the spatial octupole are not identical descriptors.
They become related only after adding the zero-surface relative velocity.

This resolves the missing variable exposed abstractly by M17-089.

---

## 14. DSD audit

### Audit A — assuming grad kappa is axial globally
Rejected. The axial reduction is only at the vertical nodal filament, where `grad_h q=0`.

### Audit B — treating A^T A as Q^T Q in all directions
Restricted correctly. The equality uses both `W_h=J grad_h q` and verticality `q_13=q_23=0` at the filament.

### Audit C — overlooking the STF trace subtraction
Avoided. The raw `333` cubic coefficient vanishes; the entire axial octupole comes from the trace-removal term.

### Audit D — inferring octupole sign directly from h
Rejected. The relative velocity `B_3-v_0` is essential.

### Audit E — dividing by relative velocity at zero
The canonical relation is kept in division-free product form. Relative synchronization `B_3=v_0` gives `h=0` and requires separate treatment.

### Audit F — applying the regular zero-surface graph when kappa_3=0
Rejected. That is a degenerate zero-level event.

### Audit G — proof status
The local space-time bridge is exact but does not fix the global octupole sign.

---

## 15. Updated vertical crossing frontier

At every spatially regular vertical `kappa=0` crossing,

\[
\boxed{
(\mathcal O_{loc}^{(3)})_{333}
=-\frac15|Q|_F^2\kappa_3,
}
\]

\[
\boxed{
h
=-\frac{5(B_3-v_0)}{|Q|_F^2}
(\mathcal O_{loc}^{(3)})_{333}.
}
\]

Therefore the remaining vertical sign bridge is reduced to the joint statistics/geometry of

\[
\boxed{
(B_3-v_0,
\mathcal O_{loc,333}^{(3)},
\mathcal K_{333}\text{-weighted global source}).
}
\]

The next high-value calculation is to derive the material law of the relative zero-surface velocity or, equivalently, the normal transport of the regular `kappa=0` sheet and compare it with M5's flux weighting.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
