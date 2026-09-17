# M19-386 — Residence–velocity covariance is exactly cross-level forcing or multi-sheet sorting

Date: 2026-09-18

Status: **NEW CANONICAL SYNTHESIS / M19-385 COVARIANCE GATE IS NOT AN INDEPENDENT ESCAPE. ON A CONNECTED COMMON-LAW RELABELING SHEET, `h=D_B kappa` IS CONSTANT ON EACH CONNECTED `kappa` LEVEL, SO THE CONDITIONAL RESIDENCE–VELOCITY COVARIANCE VANISHES. MORE GENERALLY, DISINTEGRATING THE `kappa=0` FLUX POPULATION BY CONNECTED LEVEL COMPONENTS SPLITS THE COVARIANCE INTO AN INTRA-COMPONENT PART, WHICH REQUIRES GENUINE CROSS-LEVEL FORCING, AND AN INTER-COMPONENT PART, WHICH IS EXACTLY MULTI-SHEET RESIDENCE/VELOCITY SORTING. THEREFORE FAILURE TO TRANSFER THE STRICT NEGATIVE MATERIAL-FLUX CURRENT TO THE SPATIAL PDE CURRENT IS PRECISELY THE SAME QUOTIENT FRONTIER AS M19-373/374, NOT A THIRD INDEPENDENT BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M19-385

At a meaningful conditional zero-coefficient level,

\[
G_E^\chi(0)
=
\bar L_0\,G_\Phi(0)
+
F_\Phi(0)\operatorname{Cov}_0^\Phi(L_\chi,h),
\qquad h=D_B\kappa.
\]

M5-681/M19-385 give the strict directed material current

\[
\boxed{G_\Phi(0)<0.}
\]

Hence failure of the spatial current to inherit the negative sign requires

\[
\boxed{
\operatorname{Cov}_0^\Phi(L_\chi,h)>0
}
\]

at a quantitatively comparable scale.

---

## 2. Connected common-law sheet

On a connected regular relabeling sheet,

\[
D_B\kappa=f(\kappa,\theta).
\]

Therefore, at fixed time and fixed coefficient level \(\kappa=k\),

\[
\boxed{h=f(k,\theta)}
\]

is constant over the connected level component.

Consequently

\[
\boxed{
\operatorname{Cov}_{k,\,sheet}^\Phi(L_\chi,h)=0.
}
\]

At \(k=0\), if the entire conditional population lies on one such sheet,

\[
\boxed{
G_E^\chi(0)=\bar L_0G_\Phi(0)<0.
}
\]

Thus the M19-385 sign-mismatch gate cannot occur on one connected common-law sheet.

This is consistent with M5-648--650: one connected common-law persistent sheet is already the finite-relative-flux closure lane.

---

## 3. Decompose by connected zero-level components

Let the conditional \(\kappa=0\) material-flux population be partitioned into connected regular components/sheets \(\mathscr S_a\).

Write the component label random variable as \(A\).

The law of total covariance gives

\[
\boxed{
\operatorname{Cov}(L_\chi,h)
=
\mathbb E\big[\operatorname{Cov}(L_\chi,h\mid A)\big]
+
\operatorname{Cov}\big(\mathbb E[L_\chi\mid A],\mathbb E[h\mid A]\big).
}
\]

Define

\[
\bar L_a:=\mathbb E[L_\chi\mid A=a],
\qquad
\bar h_a:=\mathbb E[h\mid A=a].
\]

Then

\[
\boxed{
\operatorname{Cov}_0^\Phi(L_\chi,h)
=
C_{intra}+C_{sheet},
}
\]

with

\[
C_{intra}
:=
\mathbb E_A\left[\operatorname{Cov}(L_\chi,h\mid A)\right],
\]

and

\[
C_{sheet}
:=
\operatorname{Cov}_A(\bar L_a,\bar h_a).
\]

---

## 4. Meaning of the intra-component term

If one connected level component obeys local scalar relabeling, then \(h\) is constant on that coefficient level and its intra-component covariance vanishes.

Therefore

\[
C_{intra}\ne0
\]

requires that, on a connected regular \(\kappa=0\) component, \(h\) varies tangentially.

Equivalently, at regular points,

\[
\nabla\kappa\times\nabla h\ne0
\]

somewhere on the active component, or the quotient-free polynomial observable of M5-650/M19-373 is nonzero:

\[
\boxed{
\mathfrak A
=
|W|^{10}
\big[\nabla\kappa\times\nabla(D_B\kappa)\big]
\ne0.
}
\]

Thus

\[
\boxed{
C_{intra}\ne0
\Longrightarrow
F_{cross-level}^{\mathfrak A\ne0}
\quad\text{or a critical/nodal quotient failure.}
}
\]

---

## 5. Meaning of the inter-component term

Suppose each connected zero-level component is locally relabeling, so \(C_{intra}=0\).

Then all required sign-cancelling covariance is

\[
\boxed{
C_{sheet}
=
\operatorname{Cov}_A(\bar L_a,\bar h_a).
}
\]

Hence a positive covariance requires that sheets with larger line-residence weight carry systematically larger/upward coefficient velocity.

This is precisely a **multi-sheet residence/velocity sorting law**.

In particular, it is not an unstructured measure mismatch.

It is the dynamic version of the M19-337 residence reweighting and the M19-374 patch-transfer architecture.

---

## 6. Canonical quotient compression

The M19-385 current-sign dichotomy

\[
\text{negative spatial current}
\lor
H_{Lh}^{0,+}
\]

therefore refines to

\[
\boxed{
\text{negative spatial }\kappa\text{-current}
\lor
F_{cross-level}^{\mathfrak A\ne0}
\lor
H_{sheet}^{sort}
\lor
G_{critical/nodal}.
}
\]

where

\[
\boxed{
H_{sheet}^{sort}:
\operatorname{Cov}_A(\bar L_a,\bar h_a)>0
\text{ at the scale needed to cancel }G_\Phi(0).
}
\]

The last noncritical term is not a new branch: it is the quantitative dynamic form of multi-sheet patching.

---

## 7. Quantitative consequence

If

\[
G_E^\chi(0)\ge0
\]

and the intra-component/cross-level contribution is absent, then

\[
\boxed{
C_{sheet}
\ge
-\frac{\bar L_0}{F_\Phi(0)}G_\Phi(0)>0.
}
\]

Thus multi-sheet survival must maintain an order-one positive sorting between

1. sheet residence \(\bar L_a\), and
2. sheet coefficient velocity \(\bar h_a\).

A static collection of disconnected sheets with unrelated but time-independent weights is therefore insufficient unless it already carries this directed sorting.

---

## 8. What this does not prove

Positive sheet sorting can recur on a compact state space.

This module does **not** prove a contradiction from \(C_{sheet}>0\).

It only removes the apparent third `measure mismatch` branch and identifies its exact mechanism.

The next closure must show that maintaining positive sheet sorting requires one of the already exposed positive-rate dynamic events from M19-374:

\[
C_{rot}^{force}
\lor
C_{crit}^{higher-jet}
\lor
T_{sheath}^{\rho=a_0},
\]

with a nonreusable or finite-resource charge.

---

## 9. Updated frontier

\[
\boxed{
H_{Lh}^{0,+}
\Longrightarrow
F_{cross-level}^{\mathfrak A\ne0}
\lor
H_{sheet}^{sort}
\lor
G_{critical/nodal}.
}
\]

Thus the M19-385 covariance gate and the M19-373 quotient gate are two descriptions of the same hard geometry.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
