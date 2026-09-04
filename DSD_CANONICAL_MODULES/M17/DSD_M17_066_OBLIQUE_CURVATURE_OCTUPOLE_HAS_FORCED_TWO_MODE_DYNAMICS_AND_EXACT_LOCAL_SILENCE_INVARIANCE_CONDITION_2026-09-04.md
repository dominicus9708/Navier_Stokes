# DSD M17-066 — Oblique curvature octupole has forced two-mode dynamics and an exact local-silence invariance condition

Date: 2026-09-04
Canonical ID: **M17-066**

Status: **INTERNAL OBLIQUE CURVATURE-CANCELLATION INVARIANCE / M17-065'S CURVATURE SCALAR `Xi_vartheta` SPLITS NATURALLY INTO A ZERO-VERTICAL-SLOT MODE `X_-^vartheta` AND A ONE-VERTICAL-SLOT MODE `X_+^vartheta`. THEIR HOMOGENEOUS RATES ARE THE SAME TWO RATES AS IN THE PRINCIPAL CASE: IN THE NODAL GAUGE `G_3=-2lambda`, `mu_-=2kappa-7/2-lambda` AND `mu_+=2kappa-7/2+5lambda`, BOTH WITH RECURRENT MEAN `-1/2`. GENUINE OBLIQUITY, HOWEVER, REINTRODUCES ADDITIVE SOURCES. THE MIXED SEMILINEAR LABEL DERIVATIVE ALONE CONTRIBUTES THE EXACT TERM `S_+^(label)=P|Q|_F^2 sin(2vartheta) mathscr H_{q3}`. M17-025 REDUCES BUT DOES NOT ANNIHILATE THE THIRD-PHI VELOCITY-COMMUTATOR SOURCES: TWO HORIZONTAL THIRD-PHI DEGREES REMAIN AFTER THE TRACE-FREE SLANT ALIGNMENT. THEREFORE THE OBLIQUE MODES CAN BE RECURRENTLY RECHARGED AND THE PRINCIPAL NEGATIVE-MEAN CONTRADICTION DOES NOT TRANSFER. IF THE FULL LOCAL PAYER OCTUPOLE IS REQUIRED TO STAY SILENT, `Z:=kappa Xi_vartheta+kappa_3 P|Q|_F^2 sin(2vartheta)=0`, THEN ITS MATERIAL INVARIANCE FORCES THE EXACT COMPATIBILITY `h Xi_vartheta-6lambda kappa X_-^vartheta+kappa(S_-^vartheta+S_+^vartheta)+P|Q|_F^2 sin(2vartheta) partial_3h=0`. THIS IS A DIRECT FOUR-CHANNEL COUPLING OF HYSTERESIS (`h`), H-GRADIENT RECHARGE (`partial_3h`), CURVATURE MODE EXCHANGE, AND THIRD-PHI/LABEL SOURCES. NO SIGN CONTRADICTION IS YET AVAILABLE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen oblique frame

Use the M17-065 frame

\[
Q=\operatorname{diag}(q_1,q_2),
\]

\[
p=P(c,s),
\qquad c=\cos\vartheta,
\qquad s=\sin\vartheta,
\]

with genuine obliquity

\[
\boxed{cs\ne0.}
\]

The angle `vartheta` and the normalized Hessian shape are material invariants.

M17-065 gives

\[
\mathfrak o_{loc}
=\varepsilon_E\frac{\sqrt2}{15}Z,
\]

where

\[
\boxed{
Z
:=\kappa\Xi_\vartheta
+\kappa_3P|Q|_F^2\sin2\vartheta.
}
\]

Here the nodal value `kappa_0` is written simply as `kappa` along the marked filament.

---

## 2. Split Xi_vartheta by vertical-slot count

M17-065 gives

\[
\begin{aligned}
\Xi_\vartheta
={}&2P(c^2q_1+s^2q_2)H_{123}
+2Pcs(q_1H_{113}+q_2H_{223})\\
&+c[(8q_1+5q_2)H_{112}-2q_2H_{222}]\\
&+s[-2q_1H_{111}+(5q_1+8q_2)H_{122}].
\end{aligned}
\]

Define the zero-vertical-slot mode

\[
\boxed{
\begin{aligned}
X_-^\vartheta
:={}&c[(8q_1+5q_2)H_{112}-2q_2H_{222}]\\
&+s[-2q_1H_{111}+(5q_1+8q_2)H_{122}],
\end{aligned}
}
\]

and the one-vertical-slot mode

\[
\boxed{
X_+^\vartheta
:=2P\left[
(c^2q_1+s^2q_2)H_{123}
+cs(q_1H_{113}+q_2H_{223})
\right].
}
\]

Then

\[
\boxed{
\Xi_\vartheta=X_-^\vartheta+X_+^\vartheta.
}
\]

---

## 3. Homogeneous rates are still the principal rates

The material third-q equation from M17-059 gives, before forcing, the rate

\[
\kappa-G_3-2-3\lambda(1-r)
\]

for an `H` component with `r` vertical slots.

The coefficient `q_i` contributes

\[
\kappa-\frac32,
\]

and `P` contributes

\[
3\lambda.
\]

Therefore

\[
\boxed{
D_BX_-^\vartheta
=\mu_-X_-^\vartheta+\mathcal S_-^\vartheta,
}
\]

\[
\boxed{
D_BX_+^\vartheta
=\mu_+X_+^\vartheta+\mathcal S_+^\vartheta,
}
\]

with

\[
\mu_-
=2\kappa-G_3-\frac72-3\lambda,
\]

\[
\mu_+
=2\kappa-G_3-\frac72+3\lambda.
\]

In the same nodal gauge as M17-061,

\[
G_3=-2\lambda.
\]

Thus

\[
\boxed{
\mu_-=2\kappa-\frac72-\lambda,
\qquad
\mu_+=2\kappa-\frac72+5\lambda.
}
\]

For uniform regular recurrence,

\[
\langle\kappa\rangle=\frac32,
\qquad
\langle\lambda\rangle=0,
\]

so

\[
\boxed{
\langle\mu_-\rangle
=\langle\mu_+\rangle
=-\frac12.
}
\]

The difference from principal slant is therefore entirely in the additive sources.

---

## 4. Genuine obliquity activates a semilinear mixed-label source

The third derivative of the material label law contains

\[
\mathscr H_{q3}
\left(
q_{ij}\delta_{k3}
+q_{ik}\delta_{j3}
+q_{jk}\delta_{i3}
\right).
\]

For the one-vertical-slot components:

\[
H_{123}:\quad q_{12}=0,
\]

\[
H_{113}:\quad q_{11}=q_1,
\]

\[
H_{223}:\quad q_{22}=q_2.
\]

Therefore the explicit label source in `X_+^vartheta` is

\[
\begin{aligned}
\mathcal S_{+,label}^\vartheta
&=2Pcs\,\mathscr H_{q3}(q_1^2+q_2^2)\\
&=P|Q|_F^2\sin2\vartheta\,\mathscr H_{q3}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal S_{+,label}^\vartheta
=P|Q|_F^2\sin2\vartheta\,\mathscr H_{q3}.
}
\]

This vanishes automatically on principal slant but is generically active on genuine oblique slant.

---

## 5. Slanted strain alignment reduces but does not annihilate third-phi forcing

M17-025 gives

\[
TF[(p\cdot\nabla_h)H_\phi]
=-(G_q-1)Q_0.
\]

In the present principal-Q frame its off-diagonal component is

\[
\boxed{
c\phi_{112}+s\phi_{122}=0.}
\]

Its diagonal trace-free component is

\[
\boxed{
P\left[
 c(\phi_{111}-\phi_{122})
+s(\phi_{112}-\phi_{222})
\right]
=-(G_q-1)(q_1-q_2).
}
\]

The vertical reconstruction law gives

\[
\boxed{
\phi_{113}=(G_q-1)q_1,
\qquad
\phi_{123}=0,
\qquad
\phi_{223}=(G_q-1)q_2.
}
\]

The `q=U_3-phi_3` reconstruction gives

\[
\boxed{
\phi_{133}=-(G_q-1)Pq_1c,
\qquad
\phi_{233}=-(G_q-1)Pq_2s.
}
\]

Thus all mixed/vertical third-phi jets are fixed, but the four purely horizontal jets

\[
(\phi_{111},\phi_{112},\phi_{122},\phi_{222})
\]

are subject to only two independent alignment equations.

Therefore

\[
\boxed{
2\text{ horizontal third-phi source degrees remain.}
}
\]

The velocity-commutator parts of `S_-^vartheta,S_+^vartheta` consequently do not vanish generically.

This is precisely where principal source annihilation fails.

---

## 6. Canonical forced two-mode system

Write

\[
\boxed{
\mathcal S_+^\vartheta
=\mathcal S_{+,label}^\vartheta
+\mathcal S_{+,vel}^\vartheta,
}
\]

and

\[
\boxed{
\mathcal S_-^\vartheta
=\mathcal S_{-,vel}^\vartheta.
}
\]

Then

\[
\boxed{
\begin{aligned}
D_BX_-^\vartheta
&=\left(2\kappa-\frac72-\lambda\right)X_-^\vartheta
+\mathcal S_{-,vel}^\vartheta,\\
D_BX_+^\vartheta
&=\left(2\kappa-\frac72+5\lambda\right)X_+^\vartheta
+P|Q|_F^2\sin2\vartheta\,\mathscr H_{q3}
+\mathcal S_{+,vel}^\vartheta.
\end{aligned}
}
\]

Thus both homogeneous modes have strict negative recurrent mean but can be maintained by explicit CE-H sources.

Unlike M17-061, nonzero recurrent modes are therefore not excluded.

---

## 7. Evolution of Xi_vartheta

Define

\[
\Delta X_\vartheta
:=X_+^\vartheta-X_-^\vartheta.
\]

Let

\[
\mu
:=2\kappa+2\lambda-\frac72.
\]

Then

\[
\boxed{
D_B\Xi_\vartheta
=\mu\Xi_\vartheta
+3\lambda\Delta X_\vartheta
+\mathcal S_-^\vartheta+\mathcal S_+^\vartheta.
}
\]

This is the curvature part needed to test persistence of the local cancellation manifold.

---

## 8. Kappa-gradient factor

Define

\[
\boxed{
A_*:=P|Q|_F^2.
}
\]

M17-064 gives

\[
D_B\kappa_3
=\partial_3h
+\left(2\lambda-\frac12\right)\kappa_3.
\]

Also

\[
D_B\log A_*
=3\lambda+(2\kappa-3)
=2\kappa+3\lambda-3.
\]

Since `sin 2vartheta` is frozen,

\[
\boxed{
D_B\left(\kappa_3A_*\sin2\vartheta\right)
=\left(2\kappa+5\lambda-\frac72\right)
\kappa_3A_*\sin2\vartheta
+A_*\sin2\vartheta\,\partial_3h.
}
\]

The homogeneous rate is exactly `mu_+`.

---

## 9. Exact invariance condition for local octupole silence

Recall

\[
Z
=\kappa\Xi_\vartheta
+\kappa_3A_*\sin2\vartheta.
\]

Suppose a retained subbranch satisfies

\[
\boxed{Z=0}
\]

and asks that this local-octupole silence persist materially.
Then necessarily

\[
D_BZ=0.
\]

Use

\[
D_B\kappa=h,
\]

Section 7 for `D_B Xi_vartheta`, and Section 8 for the kappa-gradient factor.
On `Z=0`, substitute

\[
\kappa_3A_*\sin2\vartheta=-\kappa\Xi_\vartheta.
\]

A direct cancellation yields

\[
\boxed{
0
=h\Xi_\vartheta
-6\lambda\kappa X_-^\vartheta
+\kappa(\mathcal S_-^\vartheta+\mathcal S_+^\vartheta)
+A_*\sin2\vartheta\,\partial_3h.
}
\]

This is the exact **oblique local-silence invariance condition**.

---

## 10. Interpretation of the four terms

The invariance law contains four distinct channels:

\[
\boxed{
\begin{array}{ll}
1.& h\Xi_\vartheta \quad\text{material kappa hysteresis acting on curvature},\\
2.& -6\lambda\kappa X_-^\vartheta \quad\text{internal two-mode strain splitting},\\
3.& \kappa(\mathcal S_-^\vartheta+\mathcal S_+^\vartheta) \quad\text{label/velocity third-jet recharge},\\
4.& A_*\sin2\vartheta\,\partial_3h \quad\text{axial h-gradient recharge}.
\end{array}
}
\]

Thus local-octupole silence cannot be maintained by a static algebraic cancellation alone.
It requires an exact dynamic balance among the same scalar `h`, its axial gradient, strain splitting, and higher CE-H geometry.

---

## 11. Zero-kappa phase on the silence manifold

If

\[
\kappa=0
\]

and

\[
Z=0
\]

on genuine oblique slant, M17-065 gives

\[
\boxed{\kappa_3=0.}
\]

At such an event the invariance law reduces to

\[
\boxed{
0
=h\Xi_\vartheta
+A_*\sin2\vartheta\,\partial_3h.
}
\]

Therefore a nondegenerate temporal kappa crossing with

\[
h\ne0
\]

and local octupole silence fixes the axial recharge by

\[
\boxed{
\partial_3h
=-\frac{h\Xi_\vartheta}{A_*\sin2\vartheta}.
}
\]

If in addition

\[
\Xi_\vartheta=0,
\]

then

\[
\boxed{\partial_3h=0,}
\]

so the simultaneous zero becomes more degenerate.

No contradiction follows because local octupole silence is a subbranch condition, not a universal DSAIG requirement.

---

## 12. DSD analysis

The principal branch was characterized by source annihilation.
The oblique branch is instead characterized by **source compensation**:

\[
\boxed{
\text{negative mean homogeneous drift}
+\text{label source}
+\text{velocity source}
+\text{h-gradient recharge}.
}
\]

This difference is not cosmetic. It is why the principal recurrence closed to local octupole zero while the oblique branch remains a genuine driven cocycle.

---

## 13. DSD audit

### Audit A — importing principal source silence to oblique slant
Rejected explicitly.

### Audit B — assuming the same seven H components must be followed independently
Rejected; two mode projections suffice for the local forbidden scalar dynamics.

### Audit C — assuming negative mean homogeneous exponents close the forced modes
Rejected; additive source terms remain.

### Audit D — treating local silence as automatically invariant
Rejected; Section 9 gives the required extra dynamic condition.

### Audit E — treating the zero-kappa reduced law as a contradiction
Rejected; it is only a compatibility relation on the local-silence subbranch.

### Audit F — proof status
Oblique slant remains open as an explicit forced two-mode/recharge system.

---

## 14. Updated oblique frontier

\[
\boxed{
R_{oblique}
\Longrightarrow
R_{driven}^{X_-^\vartheta,X_+^\vartheta,\kappa_3}
\ \lor\
T_{\kappa_3/nodal/rank/interface}.
}
\]

If the driven branch also keeps the local payer octupole silent, it must satisfy the exact four-channel invariance law of Section 9.

---

## 15. Next target

The remaining high-value question is no longer local octupole algebra.
It is whether the driven oblique system can also satisfy the **global pressure/viscous DSAIG scalar lock and M5 flux-weighted h-hysteresis simultaneously**.

The next target is the **Oblique Global Lock–Hysteresis Gate (OGLHG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
