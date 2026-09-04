# DSD M17-055 — The scalar negative-kappa payer does not control l=3 locking; the missing descriptor is octupole payer geometry

Date: 2026-09-04
Canonical ID: **M17-055**

Status: **INTERNAL KAPPA-PAYER / PRESSURE-MOMENT CROSS-AUDIT / THE GLOBAL CE-H IDENTITY `integral kappa rho^2=-P<0` AND M17-012'S POSITIVE-SHEATH/NEGATIVE-PAYER SPLIT ARE ANGULARLY UNSIGNED l=0 LEDGERS. THE CUBIC PRESSURE LOCK OF M17-052--054 IS AN l=3 STF MOMENT. CONSEQUENTLY NO SIGN OR NONZERO CONCLUSION FOR THE CUBIC LOCK FOLLOWS FROM THE NEGATIVE TOTAL KAPPA PAYER ALONE. THE KAPPA CONTRIBUTION TO CUBIC SOURCE PRODUCTION IS A WEIGHTED OCTUPOLE MOMENT OF `kappa rho^2`, CONTRACTED WITH THE FROZEN MATERIAL PAIR `(Q_0,phat)`. A LARGE NEGATIVE PAYER MAY HAVE ZERO l=3 MOMENT BY ANGULAR CANCELLATION OR INVERSION SYMMETRY. THUS THE CORRECT BRIDGE VARIABLE IS THE ANISOTROPIC SPATIAL PLACEMENT OF THE PAYER, NOT ITS TOTAL MASS. THIS CLOSES A FALSE SIGN-BRIDGE AND REFINES THE REMAINING RANK-1 GATE TO AN OCTUPOLE PAYER/HYSTERESIS GEOMETRY PROBLEM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scalar payer identity

The CE-H multiplier identity gives

\[
\boxed{
\int_{\mathbb R^3}\kappa\rho^2\,dy
=-P<0.
}
\]

M17-012 further separates positive and negative regions:

\[
Q_+
:=\int_{\kappa>0}\kappa\rho^2dy,
\]

\[
Q_-
:=\int_{\kappa<0}(-\kappa)\rho^2dy,
\]

with

\[
\boxed{Q_-=P+Q_+.}
\]

On strongly positive recurrent nodal phases,

\[
Q_+\ge Q_*>0
\]

and hence

\[
Q_-\ge P+Q_*>0.
\]

These are exact scalar weighted-mass statements.

---

## 2. Cubic locking is a different angular channel

M17-052--054 identify the harmonic cubic pressure with the STF degree-three pressure-source moment.
The corresponding Newtonian STF kernel has the form

\[
\boxed{
\mathcal K^{(3)}(z)
\sim
\frac{STF(z^{\otimes3})}{|z|^7},
}
\]

up to a fixed nonzero normalization.

It is homogeneous of degree `-4` and has angular spherical-harmonic degree three.

Therefore the `kappa rho^2` contribution is measured not by

\[
\int\kappa\rho^2
\]

but by an angularly signed tensor moment.

---

## 3. Define the kappa octupole payer tensor

For a marked core center `Y`, define schematically in the STF/principal-value sense

\[
\boxed{
\mathcal O_\kappa^{(3)}(Y)
:=
\left\langle
\kappa(y)\rho(y)^2,
\mathcal K^{(3)}(Y-y)
\right\rangle.
}
\]

Equivalently, in spherical-harmonic coordinates this is the seven-component family

\[
\boxed{
O_{\kappa,3m}
\propto
\int_0^\infty r^{-2}
\int_{S^2}
\kappa(Y+r\omega)\rho(Y+r\omega)^2
Y_{3m}(\omega)
\,d\omega\,dr.
}
\]

This is the correct l=3 descriptor of the kappa payer geometry.

---

## 4. DSAIG sees only one projected component

Let `E_Q` be the unit horizontal trace-free direction perpendicular to `Q_0`, and let `phat` be the materially frozen slant direction.

Define the scalar octupole payer mismatch

\[
\boxed{
\mathfrak O_\kappa
:=
E_Q:
TF_h[\widehat p\lrcorner\mathcal O_\kappa^{(3)}].
}
\]

This is the part of the `kappa rho^2` cubic moment that can contribute to the forbidden DSAIG direction.

It is a signed angular moment.

---

## 5. Why the scalar negative payer gives no sign for the octupole

The scalar identity uses the constant angular mode

\[
Y_{00}.
\]

The cubic moment uses

\[
Y_{3m},
\]

which changes sign on the sphere and has zero angular mean.

Therefore

\[
\boxed{
\int\kappa\rho^2<0
\not\Rightarrow
\mathfrak O_\kappa<0,
}
\]

and also

\[
\boxed{
Q_-\ge Q_*>0
\not\Rightarrow
\mathfrak O_\kappa\ne0.
}
\]

A large negative payer can be arranged angularly so that all degree-three moments cancel.

---

## 6. Inversion symmetry firewall

Suppose, at one retained time, the weighted payer density is inversion-even around the marked core:

\[
\kappa(Y+z)\rho(Y+z)^2
=
\kappa(Y-z)\rho(Y-z)^2.
\]

Since the degree-three kernel is odd,

\[
\mathcal K^{(3)}(-z)
=-\mathcal K^{(3)}(z),
\]

we get

\[
\boxed{
\mathcal O_\kappa^{(3)}=0.
}
\]

Thus even a strictly nonzero negative scalar payer may have zero cubic payer moment.

This is a concrete firewall against importing l=0 sign information into l=3.

---

## 7. Positive sheath plus negative payer: what is actually forced

M17-012 forces a positive-kappa sheath near the recurrent nodal core and a finite negative payer elsewhere.

This creates radial/sign separation but does not by itself determine an odd angular moment.

To force

\[
\mathfrak O_\kappa\ne0
\]

one needs additional information about at least one of:

1. angular asymmetry of the positive sheath;
2. angular displacement of the negative payer;
3. correlation between payer location and the frozen slant direction `phat`;
4. correlation between payer location and the frozen nodal anisotropy `Q_0`;
5. persistent lobe geometry from the angular defect `chi`.

Thus the missing bridge is geometric, not scalar.

---

## 8. Location inside the source-production law

M17-046/M17-053 give

\[
D_BS_P+\frac32S_P
=\cdots
-\left(\sigma+\kappa-\frac14\right)\rho^2.
\]

Hence the projected cubic source-production scalar contains

\[
\boxed{
\Pi_3^{prod}
\supset
-\mathfrak O_\kappa
}
\]

up to the fixed kernel normalization, together with separate `sigma rho^2`, strain-curvature, cubic-strain, pressure-Hessian and vorticity-rotation moments.

Therefore even a nonzero `mathfrak O_kappa` would still have to be compared with these other l=3 channels before a contradiction could be claimed.

---

## 9. Relation to angular-defect lobes

M17-019--022 already give spatial angular structure around a non-axisymmetric winding core:

- harmonic leading defect sectors;
- same-lobe `kappa>0 -> 0 -> <0` sign reversal;
- a negative spectral payer on every bounded defect lobe;
- strict lobe-boundary turnover under recurrence.

These are precisely the kinds of geometric descriptors that may control the missing l=3 payer moment.

The next bridge should therefore use **lobe-resolved payer placement**, not the whole-space scalar payer identity.

---

## 10. DSD audit

### Audit A — using total negative payer as cubic sign
Rejected; it is an l=0 to l=3 measure substitution.

### Audit B — treating positive/negative radial separation as odd angular asymmetry
Rejected; radial separation alone does not select degree three.

### Audit C — assuming non-axisymmetry implies nonzero l=3
Rejected. A non-axisymmetric field may have its first nonzero angular mode at another degree or cancel in the weighted cubic moment.

### Audit D — ignoring other source-production moments
Rejected. `kappa rho^2` is only one term in `Pi_3^prod`.

### Audit E — proof status
The scalar payer bridge is audited and the correct angular bridge variable is identified; no contradiction is obtained.

---

## 11. Updated Rank-1 bridge

The correct chain is now

\[
\boxed{
\text{positive nodal sheath + negative scalar payer}
\not\Rightarrow
\text{cubic locking sign}.
}
\]

Instead,

\[
\boxed{
\text{lobe-resolved payer geometry}
\longrightarrow
\mathcal O_\kappa^{(3)}
\longrightarrow
\mathfrak O_\kappa
\longrightarrow
\Pi_3^{prod}
}
\]

must be audited.

---

## 12. Next target — lobe-octupole transfer gate

Use the harmonic defect lobes of M17-019--022 as the angular partition around the core.
For each lobe, decompose the positive sheath and negative payer contribution to the degree-three moment.

The goal is to determine whether the alternating `2m` lobe geometry and the same-lobe kappa sign reversal force a nonzero low odd moment, or whether the lobe system can remain octupole-neutral through pairwise cancellation.

This is the **Lobe-Octupole Transfer Gate (LOTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
