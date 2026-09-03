# DSD M17-017 — The angular non-axisymmetry defect has an exact coupled material-elliptic system

Date: 2026-09-03
Canonical ID: **M17-017**

Status: **INTERNAL SHAPE–HYSTERESIS COUPLING / WITH `chi=Lq` AND `psi=Lphi`, THE GREAT-CIRCLE SEMILINEAR SYSTEM GIVES NOT ONLY `Delta chi=kappa chi` BUT ALSO THE EXACT MATERIAL LAW `D_B chi=(kappa-partial_3 U_3-1/2)chi-grad_h psi dot grad_h q`. THE COMPANION POTENTIAL DEFECT SATISFIES `partial_3 psi=(G_q-1)chi` AND `Delta_h psi=-partial_3(G_q chi)`. THUS NON-AXISYMMETRY IS NOT A PASSIVE LABEL: ITS MATERIAL AMPLIFICATION IS DRIVEN BY THE SAME KAPPA CHANNEL THAT GENERATES M17-013 LABEL-AREA HYSTERESIS, BUT IS COUPLED TO VERTICAL COMPRESSION AND AN EXPLICIT ANGULAR-POTENTIAL TRANSFER TERM. ON THE VERTICAL ANISOTROPIC/NEGATIVE-INDEX CORE M17-015 FORCES `G_q=1`, SO THE AXIAL POTENTIAL-DEFECT SOURCE VANISHES AT THE CORE. THIS IS THE FIRST EXACT PDE SYSTEM COUPLING THE SCALAR HYSTERESIS CHANNEL TO THE NON-AXISYMMETRIC SHAPE CHANNEL; NO SIGN CONTRADICTION HAS YET BEEN DERIVED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Defect variables

Use the vertical great-circle coordinates of M17-016 and the horizontal rotation generator

\[
\mathcal L
=x_1\partial_2-x_2\partial_1.
\]

Define

\[
\boxed{
\chi:=\mathcal Lq,
\qquad
\psi:=\mathcal L\phi.
}
\]

M17-016 already gives

\[
\boxed{
\Delta\chi=\kappa\chi.
}
\]

We now derive its exact material evolution.

---

## 2. Start from the reduced q material law

M17-013 gives

\[
\boxed{
D_Bq=H(q,x_3,\theta)
}
\]

with

\[
\boxed{
H_q
=\kappa-G_3-\frac12.
}
\]

Apply `mathcal L`:

\[
\mathcal L(D_Bq)
=H_q\chi.
\]

Because `mathcal L` is a spatial vector field,

\[
\mathcal L(D_Bq)
=D_B(\mathcal Lq)
+[\mathcal L,B]\cdot\nabla q.
\]

Hence

\[
\boxed{
D_B\chi
=H_q\chi
-[\mathcal L,B]\cdot\nabla q.
}
\]

---

## 3. Rotation commutator with B

Write

\[
B=U+\frac12y.
\]

The isotropic similarity drift commutes with rotations:

\[
[\mathcal L,y/2]=0.
\]

Therefore

\[
[\mathcal L,B]=[\mathcal L,U].
\]

For the horizontal velocity

\[
U_h=\nabla_h\phi,
\]

the Euclidean rotation generator is Killing, and a direct calculation gives

\[
\boxed{
[\mathcal L,U_h]
=\nabla_h(\mathcal L\phi)
=\nabla_h\psi.
}
\]

For the vertical component

\[
U_3=G(q,x_3,\theta),
\]

we have

\[
\boxed{
\mathcal LU_3
=G_q\chi.
}
\]

Thus

\[
\boxed{
[\mathcal L,B]
=(\nabla_h\psi,G_q\chi).
}
\]

---

## 4. Exact material equation for chi

Since

\[
\nabla q=(\nabla_hq,q_3),
\]

we get

\[
[\mathcal L,B]\cdot\nabla q
=\nabla_h\psi\cdot\nabla_hq
+G_q q_3\chi.
\]

Therefore

\[
D_B\chi
=\left(H_q-G_qq_3\right)\chi
-\nabla_h\psi\cdot\nabla_hq.
\]

Using

\[
H_q=\kappa-G_3-\frac12
\]

and

\[
\partial_3U_3
=G_qq_3+G_3,
\]

we obtain

\[
\boxed{
D_B\chi
=\left(\kappa-\partial_3U_3-\frac12\right)\chi
-\nabla_h\psi\cdot\nabla_hq.
}
\]

By incompressibility,

\[
\partial_3U_3=-\Delta_h\phi,
\]

so equivalently

\[
\boxed{
D_B\chi
=\left(\kappa+\Delta_h\phi-\frac12\right)\chi
-\nabla_h\psi\cdot\nabla_hq.
}
\]

This is the exact material shape-defect equation.

---

## 5. Axial equation for psi

The reconstruction law is

\[
\partial_3\phi
=G(q,x_3,\theta)-q.
\]

Apply `mathcal L`:

\[
\boxed{
\partial_3\psi
=(G_q-1)\chi.
}
\]

Thus departure of `G_q` from one controls the axial transfer of angular defect into the horizontal velocity potential.

---

## 6. Horizontal elliptic equation for psi

Incompressibility gives

\[
\Delta_h\phi+\partial_3U_3=0.
\]

Apply `mathcal L`:

\[
\Delta_h\psi
+\partial_3(\mathcal LU_3)=0.
\]

Since

\[
\mathcal LU_3=G_q\chi,
\]

we obtain

\[
\boxed{
\Delta_h\psi
=-\partial_3(G_q\chi).
}
\]

The pair `(chi,psi)` therefore satisfies a mixed three-dimensional/two-dimensional elliptic coupling.

---

## 7. Canonical defect system

Collect the three exact equations:

\[
\boxed{
\begin{aligned}
\Delta\chi
&=\kappa\chi,\\
D_B\chi
&=\left(\kappa-\partial_3U_3-\frac12\right)\chi
-\nabla_h\psi\cdot\nabla_hq,\\
\partial_3\psi
&=(G_q-1)\chi,\\
\Delta_h\psi
&=-\partial_3(G_q\chi).
\end{aligned}
}
\]

Together with the M17-013 label system

\[
\boxed{
q'=H,
\qquad
x_3'=K,
\qquad
\operatorname{div}_{(q,x_3)}(H,K)=\kappa,
}
\]

this is the first direct coupling of

1. scalar label-area hysteresis;
2. angular non-axisymmetric geometry.

---

## 8. Core simplification on vertical non-axisymmetric filaments

M17-015 gives at every vertical genuinely non-axisymmetric regular core

\[
\boxed{
G_q=1,
\qquad
\lambda_3=0.
}
\]

Hence at the core

\[
\boxed{
\partial_3\psi=0.
}
\]

Also the rotation generator vanishes on the axis, so

\[
\chi|_\Gamma=0,
\qquad
\psi|_\Gamma=0.
\]

The actual non-axisymmetric information is therefore carried by transverse jets of `chi` and `psi`, not their point values.

For an anisotropic quadratic core, `chi` begins at order two.
For a conformal positive core separated from the firewall, M17-016 gives a finite nonzero order

\[
m_A\ge3.
\]

---

## 9. Leading-order anisotropic-core behavior

Suppose the nodal Hessian is non-scalar.
The quadratic part of `q` is

\[
q^{(2)}(z)
=\frac12z^TQz.
\]

Then

\[
\chi^{(2)}
=\mathcal Lq^{(2)}
\]

is the quadratic angular defect.

M17-014 gives

\[
D_BQ
=\left(\kappa-\frac32\right)Q.
\]

Because `mathcal L` is fixed in the centered vertical frame,

\[
\boxed{
D_B\chi^{(2)}
=\left(\kappa-\frac32\right)\chi^{(2)}
}
\]

for the leading quadratic jet.

Thus the same recurrence condition

\[
\langle\kappa\rangle_{nodal}=\frac32
\]

that keeps the regular Jacobian bounded also keeps the leading anisotropic angular-defect amplitude recurrent on average.

This explains why the scalar `3/2` condition alone cannot damp the non-axisymmetric core.

---

## 10. Why no immediate sign contradiction appears

The material equation contains the signed source

\[
\kappa-\partial_3U_3-\frac12
\]

and the transfer term

\[
-\nabla_h\psi\cdot\nabla_hq.
\]

Neither has a fixed sign.
Moreover, at a non-axisymmetric core the leading angular jet is compatible with the same mean `kappa=3/2` multiplier that preserves nodal regularity.

Therefore the following shortcut is rejected:

\[
\boxed{
\text{nonzero angular defect}
+\text{kappa hysteresis}
\not\Longrightarrow
\text{immediate contradiction}.
}
\]

A successful closure must use a signed integral, a level-set transfer law, or a finite-jet degeneration mechanism involving the coupling term.

---

## 11. DSD analysis

### 11.1 Separate point value from jet information
At the symmetry candidate axis,

\[
\chi=\psi=0
\]

for geometric reasons even in a non-axisymmetric state.
The useful descriptor is therefore the first nonzero transverse jet.

### 11.2 Coupled channels
The scalar channel `kappa` controls label-area expansion.
The geometric channel `chi` controls angular non-axisymmetry.
The field `psi` is the transfer mediator between the angular defect and the horizontal velocity potential.

### 11.3 Exact firewall
The submanifold

\[
\chi=\psi=0
\]

is the axisymmetric no-swirl firewall of M17-016.
The remaining hard branch is a finite-jet excursion away from that submanifold.

---

## 12. DSD audit

### Audit A — assuming chi is materially passive
Rejected.
Its material law contains vertical compression and the explicit `psi-q` coupling.

### Audit B — using chi(point) as non-axisymmetry test
Rejected.
`chi=0` automatically on the axis; derivatives are required.

### Audit C — claiming G_q=1 kills the defect
Rejected.
It only removes the axial `psi` source at the core; transverse defect jets can persist.

### Audit D — claiming the mean 3/2 condition damps anisotropy
Rejected.
The leading quadratic anisotropic jet has exactly the same multiplier `kappa-3/2` as the regular nodal Jacobian.

### Audit E — proof status
No global contradiction is claimed.

---

## 13. Updated non-axisymmetric frontier

The genuinely non-axisymmetric vertical regular branch now has an explicit PDE state vector

\[
\boxed{
(\kappa,H,K;q,\chi,\psi)
}
\]

subject to

\[
\boxed{
\operatorname{div}_{(q,x_3)}(H,K)=\kappa,
\qquad
\Delta\chi=\kappa\chi,
}
\]

and the coupled material equations above.

The remaining closure problem is no longer qualitative.
It is to determine whether this system admits a compact recurrent nonzero-defect orbit satisfying simultaneously

\[
\boxed{
\langle\kappa_0\rangle=\frac32,
\qquad
Q_+\ge Q_*>0,
\qquad
Q_-\ge P+Q_*,
\qquad
\overline G_\Phi(0)<0.
}
\]

---

## 14. Next target — signed defect-transfer identity

The next calculation should seek an integral or level-set identity for the transfer term

\[
\nabla_h\psi\cdot\nabla_hq
\]

using

\[
\Delta_h\psi=-\partial_3(G_q\chi)
\]

and

\[
\Delta q=F(q,x_3,\theta).
\]

A successful identity would determine whether recurrent non-axisymmetric angular defect must be transported into the same negative-kappa payer required by M17-012, or whether the coupling admits a regular closed cycle.

This is the new **Signed Angular-Defect Transfer Gate (SADTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
