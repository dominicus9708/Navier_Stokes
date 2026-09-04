# DSD M17-067 — A genuine oblique regular kappa-zero level must activate the local payer octupole; a silent synchronized crossing is spatially degenerate

Date: 2026-09-04
Canonical ID: **M17-067**

Status: **INTERNAL OGLHG ZERO-LEVEL ACTIVATION GATE / ON THE REGULAR SEMILINEAR GREAT-CIRCLE NODAL BRANCH, `grad_h kappa=0`. M17-065 GIVES THE FULL GENUINE-OBLIQUE LOCAL PAYER-OCTUPOLE SCALAR `o_loc = eps sqrt(2)/15 [kappa Xi_vartheta + kappa_3 P |Q|_F^2 sin(2 vartheta)]`. AT `kappa=0`, GENUINE OBLIQUITY AND REGULAR NONZERO SLANT REDUCE THIS EXACTLY TO A NONZERO CONSTANT TIMES `kappa_3`. THEREFORE A SPATIALLY REGULAR KAPPA-ZERO LEVEL, WHICH HERE REQUIRES `kappa_3 != 0`, MUST BE LOCAL-OCTUPOLE ACTIVE. LOCAL-OCTUPOLE SILENCE AT `kappa=0` FORCES `kappa_3=0` AND HENCE `grad kappa=0`, SO THE ZERO LEVEL IS SPATIALLY DEGENERATE. UNDER THE ADDITIONAL SYNCHRONIZED CONSTITUTIVE LAW `h=f(kappa,theta)`, SILENCE ALSO GIVES `partial_3 h=0`; IF THE MATERIAL TRAJECTORY CROSSES `kappa=0` NONDEGENERATELY WITH `h != 0`, M17-066 THEN FORCES `Xi_vartheta=0`. THE STRONGER M5-638 MATERIAL-ZERO SUBBRANCH (`f(0,theta)=0` AND `|grad kappa|>0`) IS THEREFORE NECESSARILY OCTUPOLE-ACTIVE AND CANNOT ENTER THE SILENT SUBBRANCH. THIS IS A BRANCH SEPARATION, NOT A GLOBAL CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from the oblique full-octupole reduction

Use the M17-065 frozen principal frame

\[
Q=\operatorname{diag}(q_1,q_2),
\qquad
p=P(\cos\vartheta,\sin\vartheta),
\]

with

\[
P=|p|>0,
\qquad
\det Q\neq0,
\qquad
\sin2\vartheta\neq0.
\]

The final inequality is the genuine-oblique condition.

M17-065 gives the full local payer-octupole projection into the horizontal trace-free direction orthogonal to the nodal anisotropy:

\[
\boxed{
\mathfrak o_{\rm loc}
=
\varepsilon_E\frac{\sqrt2}{15}
\left[
\kappa\Xi_\vartheta
+
\kappa_3P|Q|_F^2\sin2\vartheta
\right].
}
\]

Here

\[
\kappa_3:=\partial_3\kappa
\]

at the marked nodal filament and `Xi_vartheta` is the single curvature-octupole scalar isolated in M17-065--066.

---

## 2. Semilinear nodal geometry kills the horizontal kappa gradient

The M17-004 semilinear representation, extended to the retained regular nodal limit as already used in M17-015 and M17-058, is

\[
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q(q,x_3,\theta).
\]

At a regular nodal filament,

\[
\nabla_hq=0.
\]

Therefore

\[
\boxed{
\nabla_h\kappa
=F_{qq}\nabla_hq
=0.
}
\]

Consequently

\[
\boxed{
\nabla\kappa
=\kappa_3e_3.
}
\]

This is the OJRG reduction of M17-058.

---

## 3. Exact octupole value at a kappa-zero event

Set

\[
\boxed{\kappa=0}
\]

at the marked nodal point.

The curvature contribution in M17-065 is multiplied by `kappa` and disappears exactly.
Hence

\[
\boxed{
\mathfrak o_{\rm loc}\big|_{\kappa=0}
=
\varepsilon_E\frac{\sqrt2}{15}
\kappa_3P|Q|_F^2\sin2\vartheta.
}
\]

Since on the genuine-oblique regular-slant class

\[
P>0,
\qquad
|Q|_F^2>0,
\qquad
\sin2\vartheta\neq0,
\]

we obtain the exact equivalence

\[
\boxed{
\mathfrak o_{\rm loc}=0
\quad\Longleftrightarrow\quad
\kappa_3=0
\qquad(\kappa=0,\ \text{genuine oblique}).
}
\]

---

## 4. A spatially regular zero level must be octupole-active

A spatially regular zero level of `kappa` requires

\[
\boxed{|\nabla\kappa|>0.}
\]

But Section 2 gives

\[
|\nabla\kappa|=|\kappa_3|.
\]

Therefore regularity of the zero level is exactly

\[
\boxed{\kappa_3\neq0}
\]

on this nodal branch.

Combining with Section 3,

\[
\boxed{
\kappa=0,
\quad
|\nabla\kappa|>0,
\quad
\sin2\vartheta\neq0
\quad\Longrightarrow\quad
\mathfrak o_{\rm loc}\neq0.
}
\]

Thus a genuine-oblique regular `kappa=0` sheet cannot hide inside the local-octupole-silent subbranch.

Equivalently,

\[
\boxed{
\kappa=0,
\quad
\mathfrak o_{\rm loc}=0
\quad\Longrightarrow\quad
\nabla\kappa=0
}
\]

for the retained genuine-oblique nodal geometry.

This is a spatial degeneracy, not merely a small octupole coefficient.

---

## 5. Add the generic synchronized constitutive law

Now impose only the constitutive synchronization

\[
\boxed{h=f(\kappa,\theta),}
\]

where

\[
h:=D_B\kappa.
\]

At a locally silent `kappa=0` event Section 3 gives

\[
\kappa_3=0.
\]

Spatial differentiation of the synchronized law gives

\[
\partial_3h
=f_\kappa(\kappa,\theta)\kappa_3.
\]

Hence

\[
\boxed{
\partial_3h=0
}
\]

at every synchronized silent genuine-oblique `kappa=0` event.

M17-064 already gives

\[
\nabla_hh=0
\]

on the regular semilinear nodal branch.
Therefore synchronized local silence at the zero event also gives

\[
\boxed{\nabla h=0.}
\]

This does not imply `h=0`; it means the spatial first jet of the temporal multiplier derivative is zero.

---

## 6. Nondegenerate temporal crossing forces Xi_vartheta = 0 on the silent synchronized subbranch

M17-066 derives the local-silence invariance law

\[
0
=
h\Xi_\vartheta
-6\lambda\kappa X_-^\vartheta
+\kappa(\mathcal S_-^\vartheta+\mathcal S_+^\vartheta)
+A_*\sin2\vartheta\,\partial_3h,
\]

where

\[
A_*:=P|Q|_F^2.
\]

At

\[
\kappa=0
\]

this reduces to

\[
\boxed{
0=h\Xi_\vartheta+A_*\sin2\vartheta\,\partial_3h.
}
\]

On the synchronized silent event, Section 5 gives

\[
\partial_3h=0.
\]

Thus

\[
\boxed{h\Xi_\vartheta=0.}
\]

If the material trajectory crosses the scalar zero nondegenerately,

\[
\boxed{h=D_B\kappa\neq0,}
\]

then necessarily

\[
\boxed{\Xi_\vartheta=0.}
\]

Hence a synchronized, locally silent, nondegenerate temporal crossing has the joint degeneracy

\[
\boxed{
\kappa=0,
\qquad
\kappa_3=0,
\qquad
\Xi_\vartheta=0,
\qquad
\partial_3h=0.
}
\]

In addition, the semilinear structure gives

\[
\nabla_h\kappa=0,
\qquad
\nabla_hh=0.
\]

This is a strong finite-jet degeneracy class, but it is not by itself impossible.

---

## 7. Important distinction: generic synchronization versus M5-638 material-zero synchronization

The previous section used only

\[
h=f(\kappa,\theta).
\]

It did **not** impose

\[
f(0,\theta)=0.
\]

Therefore it still permits a temporal crossing with

\[
h\neq0.
\]

M5-638 studies the stronger synchronized material-zero subbranch

\[
\boxed{
D_B\kappa=f(\kappa,\theta),
\qquad
f(0,\theta)=0,
}
\]

and assumes that `kappa=0` is a spatially regular level.
On that subbranch

\[
h=0
\]

on the material zero level; it is not a nondegenerate material crossing.

The two synchronized notions must therefore not be conflated.

---

## 8. M5-638 regular zero level is necessarily octupole-active

M5-638 requires

\[
|\nabla\kappa|>0
\]

on the material `kappa=0` level.

But on the present semilinear nodal branch

\[
\nabla_h\kappa=0.
\]

Therefore the M5-638 regularity assumption becomes

\[
\boxed{\kappa_3\neq0.}
\]

on a genuine-oblique nodal intersection with that level.

Section 3 then gives

\[
\boxed{
\mathfrak o_{\rm loc}\neq0.
}
\]

Thus

\[
\boxed{
\text{M5-638 regular material }\kappa=0
\quad\Longrightarrow\quad
\text{local-octupole active}
}
\]

on every genuine-oblique regular nodal intersection.

Conversely, demanding local octupole silence would force `grad kappa=0` and violate the M5-638 regular-zero-level hypothesis.

This closes the **silent + regular-zero-level** combination, not the M5-638 branch itself.

---

## 9. Relation to M5-685 crossing hysteresis

M5-685 uses the signed temporal crossing derivative

\[
h=D_B\kappa
\]

at `kappa=0` and finds a flux-weighted bias in which downward crossings are heavier than upward crossings.

M17-067 adds a distinct local geometric statement:

- a spatially regular genuine-oblique zero event is necessarily local-octupole active;
- a synchronized locally silent nondegenerate temporal crossing must instead enter the finite-jet degeneracy of Section 6.

These statements do not yet imply a sign contradiction with the M5-685 covariance law.
The M5-685 event measure and the present same-marker local-jet descriptor must be joined explicitly before their weights can be compared.

---

## 10. DSD analysis

The zero event now splits by two independent descriptors:

\[
\boxed{
\text{temporal crossing descriptor }h
\quad\oplus\quad
\text{spatial zero-level descriptor }\nabla\kappa.
}
\]

On the great-circle nodal branch the second descriptor has only one component:

\[
\nabla\kappa=\kappa_3e_3.
\]

Genuine obliquity converts that component directly into the first nontrivial payer octupole.
Therefore the octupole is not an arbitrary additional decoration at `kappa=0`; it is the angularly resolved form of spatial zero-level regularity.

---

## 11. DSD audit

### Audit A — confusing a temporal crossing with a spatially regular zero level
Rejected.
`h != 0` and `|grad kappa|>0` are logically distinct conditions.

### Audit B — using M5-638 and h != 0 simultaneously on its material zero level
Rejected.
M5-638 additionally assumes `f(0,theta)=0`, so `h=0` on that material level.

### Audit C — claiming local-octupole silence is universally required
Rejected.
It is a subbranch condition. A regular genuine-oblique zero level instead forces octupole activity.

### Audit D — treating grad_h kappa = 0 as a generic Navier--Stokes identity
Rejected.
It belongs to the retained semilinear great-circle nodal branch and its audited analytic extension.

### Audit E — treating spatial degeneracy as singularity
Rejected.
`grad kappa=0` is a higher-order zero-level event and may remain smooth.

### Audit F — proof status
The zero-level geometry is sharply split, but no global contradiction has been obtained.

---

## 12. Updated genuine-oblique zero-event split

\[
\boxed{
R_{oblique}^{\kappa=0}
\Longrightarrow
R_{regular-zero}^{\mathfrak o_{loc}\neq0}
\ \lor\
R_{silent}^{\nabla\kappa=0}
\ \lor\
T_{nodal/rank/interface}.
}
\]

Under generic synchronization `h=f(kappa,theta)`, a locally silent nondegenerate temporal crossing further satisfies

\[
\boxed{
\kappa_3=0,
\qquad
\partial_3h=0,
\qquad
\Xi_\vartheta=0.
}
\]

The M5-638 spatially regular material-zero branch lies entirely in the first, octupole-active class.

---

## 13. Next target — exact oblique global pressure lock

M17-067 determines what happens to the local payer octupole at zero events.
The next step is to reduce the full DSAIG pressure/viscous balance on a generic genuine-oblique nodal core.

Unlike principal slant, the local Poisson source-gradient pressure tensor does not vanish automatically.
The next calculation should express its forbidden scalar explicitly in `(Q,p,G_q)` and normalize the full local-viscous/global-pressure equality by `|p|`.

This is the **Oblique Global Lock Reduction (OGLR)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
