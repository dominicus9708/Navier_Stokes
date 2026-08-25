# DSD Transverse Anchor: Projective-Coercivity Counterexample

Date: 2026-08-25

Status: **PROPOSED DIRECT COERCIVITY ROUTE REJECTED BY AN EXPLICIT FOURIER MODE / TRANSVERSE VORTICITY DOES NOT FORCE EXPORT-AXIS TILTING / GLOBAL REGULARITY UNPROVED.**

## 1. Question

The previous directional-defect lemma forces, for every asymptotically fixed export axis \(e\), a nonzero transverse vorticity component

\[
\|P_{e^\perp}\Omega\|_2\ge\delta_{dir}>0.
\]

A tempting next step is to hope for an elliptic coercive inequality of the form

\[
\|P_{e^\perp}Se\|_2
\gtrsim
\|P_{e^\perp}\Omega\|_2,
\]

which would force projective tilting of the export axis.

This note shows that such an inequality is false.

## 2. Fourier representation

For a divergence-free Fourier mode with wave vector \(k\),

\[
k\cdot\widehat\Omega=0,
\]

Biot--Savart gives

\[
\widehat U
=
\frac{i\,k\times\widehat\Omega}{|k|^2}.
\]

The strain symbol is

\[
\widehat S_{ij}
=
\frac{i}{2}
\left(k_i\widehat U_j+k_j\widehat U_i\right).
\]

Fix

\[
e=e_3.
\]

## 3. Explicit null mode

Take

\[
\boxed{
k=(1,0,1)}
\]

(up to irrelevant normalization) and

\[
\boxed{
\widehat\Omega=(0,1,0).
}
\]

Then

\[
k\cdot\widehat\Omega=0,
\qquad
\widehat\Omega\perp e_3.
\]

Biot--Savart gives

\[
\widehat U
=
\frac{i}{2}(-1,0,1).
\]

Now

\[
\widehat S_{13}
=
\frac{i}{2}
\left(k_1\widehat U_3+k_3\widehat U_1\right)
=0,
\]

and

\[
\widehat S_{23}=0.
\]

Therefore

\[
\boxed{
P_{e_3^\perp}\widehat S e_3=0
}
\]

while

\[
\boxed{
P_{e_3^\perp}\widehat\Omega
=\widehat\Omega\ne0.
}
\]

Thus a purely transverse vorticity mode can leave \(e_3\) as an exact strain eigenaxis.

## 4. Consequence

There is no universal constant \(c>0\) such that

\[
\boxed{
\|P_{e^\perp}Se\|_2
\ge
c\|P_{e^\perp}\Omega\|_2
}
\]

for all divergence-free fields and all axes \(e\).

The persistent transverse-enstrophy anchor found previously therefore does **not** automatically imply a projective-axis-rotation charge.

Status: **DIRECT ROUTE CLOSED NEGATIVELY.**

## 5. Geometric interpretation

The Biot--Savart/Riesz map from vorticity to strain has a nontrivial symbol kernel relative to a selected axis.

Transverse vorticity can produce strain that stretches or compresses the selected axis without tilting it.

Thus the final survivor can, at least at the linear-symbol level, maintain

\[
\text{fixed export axis}
+
\text{transverse vorticity anchor}
\]

without paying an obligatory \(P_{e^\perp}Se\) cost.

## 6. What remains viable

The anchor must instead be attacked through a mechanism that uses more information than the linear vorticity-to-axis-tilt map, for example:

1. nonlinear interaction/Betchov structure;
2. signed flux topology and replacement;
3. scale-to-scale recurrence of the transverse anchor itself;
4. a critical norm or weighted-moment rigidity;
5. a special ancient/DSS limit carrying both sectors.

## 7. Audit verdict

### REJECTED

\[
\text{transverse enstrophy}
\Rightarrow
\text{uniform projective tilting}
\]

is false.

### SURVIVING FRONTIER

\[
\boxed{
\text{fixed-axis critical export conveyor}
+
\text{persistent transverse anchor}
}
\]

still survives this test.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
