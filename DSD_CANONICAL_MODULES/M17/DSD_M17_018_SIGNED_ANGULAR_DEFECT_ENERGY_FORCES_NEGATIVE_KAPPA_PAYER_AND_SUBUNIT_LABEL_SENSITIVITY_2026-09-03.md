# DSD M17-018 — Signed angular-defect energy forces a negative-kappa payer and subunit label sensitivity

Date: 2026-09-03
Canonical ID: **M17-018**

Status: **INTERNAL SADTG ENERGY CLOSURE / THE ANGULAR DEFECT EQUATION `Delta chi = kappa chi` HAS AN EXACT SIGNED ENERGY IDENTITY `int kappa chi^2 = -int |grad chi|^2`. HENCE EVERY NONZERO FINITE-ENERGY NON-AXISYMMETRIC DEFECT REQUIRES A NEGATIVE-KAPPA PAYER, AND THE NEGATIVE DEFECT-WEIGHTED CHARGE EXCEEDS THE POSITIVE CHARGE BY THE FULL DIRICHLET ENERGY. THE SAME STATEMENT LOCALIZES TO EACH CHI NODAL DOMAIN. INDEPENDENTLY, THE PSI COUPLING GIVES `int |grad_h psi|^2 = int G_q(1-G_q) chi^2`, OR EQUIVALENTLY A COERCIVE HALF-SENSITIVITY BUDGET. A NONZERO DECAYING DEFECT THEREFORE CANNOT KEEP `G_q` IDENTICALLY AT THE CORE VALUE ONE; IT MUST GENERATE A REGION OF SUBUNIT LABEL SENSITIVITY. THIS CONNECTS THE M17 NON-AXISYMMETRIC SHAPE CHANNEL TO THE M17-012/M5 NEGATIVE-KAPPA PAYER AND TO A NEW `G_q` TRANSITION CHANNEL. NO CONTRADICTION YET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input system

Use M17-017 on the retained finite-energy/decay branch:

\[
\boxed{
\Delta\chi=\kappa\chi,
}
\]

\[
\boxed{
\partial_3\psi=(G_q-1)\chi,
\qquad
\Delta_h\psi=-\partial_3(G_q\chi).
}
\]

Assume the boundary terms below vanish either by the retained decay conditions or by working first with compact cutoffs and then passing to the limit.

---

## 2. Exact signed angular-defect energy identity

Multiply

\[
\Delta\chi=\kappa\chi
\]

by `chi` and integrate over space.
Integration by parts gives

\[
\int \chi\Delta\chi
=-\int|\nabla\chi|^2.
\]

Therefore

\[
\boxed{
\int\kappa\chi^2
=-\int|\nabla\chi|^2
\le0.
}
\]

Equality holds only if `grad chi = 0`; under decay/finite-energy this means `chi = 0`.
Thus every genuinely non-axisymmetric state satisfies the strict law

\[
\boxed{
\chi\not\equiv0
\Longrightarrow
\int\kappa\chi^2<0.
}
\]

This is the first signed integral closure of SADTG.

---

## 3. Positive and negative defect-weighted kappa charges

Define

\[
D_+
:=\int_{\kappa>0}\kappa\chi^2,
\]

and

\[
D_-
:=\int_{\kappa<0}(-\kappa)\chi^2.
\]

Then

\[
D_+-D_-
=-\int|\nabla\chi|^2.
\]

Hence

\[
\boxed{
D_-
=D_+
+\int|\nabla\chi|^2.
}
\]

For every nonzero defect,

\[
\boxed{
D_->D_+\ge0.
}
\]

Consequently the angular defect cannot be supported only in `kappa >= 0`.
It must overlap a region where

\[
\boxed{\kappa<0.}
\]

The negative-kappa payer of M17-012 is therefore not merely a scalar bulk bookkeeping object: non-axisymmetric angular geometry itself requires access to the negative side.

---

## 4. Nodal-domain localization

Let `Omega` be a connected nodal domain of `chi`, i.e. a connected component of

\[
\{\chi\ne0\}.
\]

On the regular nodal boundary,

\[
\chi|_{\partial\Omega}=0.
\]

Assuming the usual decay if `Omega` is unbounded, integration by parts on `Omega` gives

\[
\boxed{
\int_\Omega\kappa\chi^2
=-\int_\Omega|\nabla\chi|^2<0.
}
\]

Thus **every nontrivial angular-defect lobe has its own negative-kappa payer**.

Writing

\[
D_{\pm,\Omega}
\]

for the positive/negative charges restricted to the lobe,

\[
\boxed{
D_{-,\Omega}
=D_{+,\Omega}
+\int_\Omega|\nabla\chi|^2.
}
\]

This prevents positive and negative defect lobes from cancelling one another in the global identity.
The payer requirement is lobe-local.

---

## 5. Exact potential-defect sensitivity identity

Now use

\[
\Delta_h\psi=-\partial_3(G_q\chi).
\]

Multiply by `psi` and integrate over all space.
The horizontal left-hand side gives

\[
\int\psi\Delta_h\psi
=-\int|\nabla_h\psi|^2.
\]

On the right,

\[
-\int\psi\partial_3(G_q\chi)
=\int(\partial_3\psi)G_q\chi.
\]

Using

\[
\partial_3\psi=(G_q-1)\chi,
\]

we obtain

\[
-\int|\nabla_h\psi|^2
=\int G_q(G_q-1)\chi^2.
\]

Hence

\[
\boxed{
\int|\nabla_h\psi|^2
=\int G_q(1-G_q)\chi^2.
}
\]

This is the second exact signed identity of SADTG.

---

## 6. Coercive half-sensitivity form

Use

\[
G_q(1-G_q)
=\frac14-\left(G_q-\frac12\right)^2.
\]

Then

\[
\boxed{
\int|\nabla_h\psi|^2
+\int\left(G_q-\frac12\right)^2\chi^2
=\frac14\int\chi^2.
}
\]

In particular,

\[
\boxed{
\|\nabla_h\psi\|_2
\le\frac12\|\chi\|_2.
}
\]

Thus the angular-potential transfer field cannot become arbitrarily large relative to the angular defect itself.

---

## 7. Nonzero defect forces departure from the core value G_q = 1

M17-015 gives at a vertical genuinely non-axisymmetric regular core

\[
G_q=1.
\]

Suppose, however, that `G_q = 1` throughout the connected finite-energy defect support.
Then the sensitivity identity gives

\[
\nabla_h\psi=0.
\]

Decay implies

\[
\psi=0.
\]

The elliptic equation then gives

\[
\partial_3\chi=0.
\]

A nonzero field independent of `x_3` cannot belong to the retained full-space finite-energy class.
Hence

\[
\boxed{
\chi\not\equiv0
\Longrightarrow
G_q\not\equiv1
}
\]

on the connected defect structure.

More generally, if `G_q(1-G_q) <= 0` everywhere on the defect support, the sensitivity identity forces `grad_h psi = 0` and `G_q(1-G_q)chi^2=0`; continuity plus the decay equations again collapses the nonzero branch.
Therefore a genuine defect requires a positive-measure region with

\[
\boxed{
0<G_q<1
}
\]

unless positive and negative sensitivity regions are mixed so that the positive part strictly dominates.

Since the vertical label flow of M17-013 has

\[
K_q=G_q,
\]

this is a **subunit vertical label-sensitivity channel**.

---

## 8. DSD interpretation

### 8.1 Signed measure restoration
M17-011 showed that the nodal skeleton is thin in the `|W|^2` measure.
M17-012 restored a finite-radius positive/negative `kappa` bulk balance.
M17-018 now introduces a second independent structural measure,

\[
\boxed{\chi^2dx,}
\]

under which non-axisymmetry has a strictly negative mean `kappa`.

### 8.2 Same sign reservoir, different weights
The bulk payer is seen through

\[
|W|^2dx,
\]

while the shape payer is seen through

\[
\chi^2dx.
\]

They are not numerically interchangeable, but both are forced to use the same sign reservoir

\[
\boxed{\{\kappa<0\}.}
\]

### 8.3 Shape-to-label sensitivity transfer
The field `psi` mediates non-axisymmetric geometry into the vertical label map.
A nonzero defect cannot remain everywhere at the core sensitivity `G_q=1`; it must create a `G_q` transition away from the core.

---

## 9. DSD audit

### Audit A — treating `int kappa chi^2 < 0` as a singularity contradiction
Rejected.
A real Schrödinger-type equation with sign-changing potential can support nonzero finite-energy structure.
The identity forces a negative payer but not blow-up.

### Audit B — identifying `chi^2` and `|W|^2` measures
Rejected.
They are distinct structural weights.
The conclusion is common use of `kappa<0`, not equality of payer magnitudes.

### Audit C — global lobe cancellation
Closed.
The signed identity holds separately on each `chi` nodal domain.

### Audit D — claiming G_q must lie in `(0,1)` pointwise everywhere
Rejected.
Only an integrated positive budget is forced.
Regions with `G_q<0` or `G_q>1` remain possible if compensated by sufficient `0<G_q<1` defect weight.

### Audit E — proof status
No global regularity theorem is claimed.

---

## 10. Updated shape-payer frontier

The non-axisymmetric branch now obeys

\[
\boxed{
\chi\ne0
\Longrightarrow
D_-^{\chi}>D_+^{\chi}
\Longrightarrow
\operatorname{supp}\chi\cap\{\kappa<0\}\ne\varnothing.
}
\]

At the same time,

\[
\boxed{
G_q=1\text{ at the vertical core}
\quad\text{but}\quad
\chi\ne0
\Longrightarrow
G_q\text{ must depart from }1
}
\]

on the connected defect structure.

Thus the survivor must simultaneously realize

1. a positive-kappa winding core;
2. a negative-kappa defect payer;
3. a `G_q` sensitivity transition;
4. the M5-685 flux-weighted zero-crossing hysteresis.

---

## 11. Next target — lobe-resolved kappa crossing

The next calculation is to combine the positive-kappa core tube of M17-012 with the lobe-local identity

\[
\int_\Omega\kappa\chi^2<0.
\]

For every angular-defect lobe emerging from a positive nodal core, determine whether the same lobe is forced to contain

\[
\boxed{
\kappa>0
\to
\kappa=0
\to
\kappa<0
}
\]

and how many such channels are forced by the first nonzero angular jet.

This is the **Lobe-Resolved Payer Gate (LRPG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
