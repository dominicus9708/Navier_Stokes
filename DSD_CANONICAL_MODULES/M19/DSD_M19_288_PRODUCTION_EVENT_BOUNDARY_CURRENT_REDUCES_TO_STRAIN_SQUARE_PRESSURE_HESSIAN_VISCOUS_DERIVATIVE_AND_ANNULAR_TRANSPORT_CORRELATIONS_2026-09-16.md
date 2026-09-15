# M19-288 — The production event-boundary current reduces to strain-square, pressure-Hessian, viscous-derivative, and annular-transport correlations

**Date:** 2026-09-16  
**Status:** CALCULATION / EVENT-MARKER PDE DIFFERENTIATION / ABSTRACT BOUNDARY DEFECT RESOLVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-287 identifies the only genuinely new signed term created by fixed-lag event conditioning:

\[
-\langle(\mathcal L_qm_h)j_i\rangle.
\]

To decide whether this is a new resource, the marker must be tied to the actual M5-589 production event rather than left abstract.

This module differentiates a smooth marker built from the annular vortex-stretching production functional and resolves its generator into explicit Navier--Stokes channels.

## 2. Annular production functional

Let \(\mathcal A_*\) be the fixed finite-depth annulus from M5-589. Define

\[
\boxed{
\mathscr P_A(\theta)
:=
\int_{\mathcal A_*}
W\cdot\Sigma W\,dy.
}
\]

M5-589 gives a positive-density event set on which

\[
\boxed{\mathscr P_A\ge c_{ann}>0.}
\]

Choose a smooth nondecreasing cutoff \(\chi\) with

\[
0\le\chi\le1
\]

that transitions inside a fixed interval below/around the certified production threshold, and set

\[
\boxed{m_{pd}=\chi(\mathscr P_A).}
\]

Then

\[
\boxed{
\partial_\theta m_{pd}
=\chi'(\mathscr P_A)\mathscr P_A'.
}
\]

## 3. Similarity vorticity and strain equations

Let

\[
B=U+\frac12y,
\qquad
A=\nabla U,
\qquad
A=\Sigma+R
\]

with \(R\) antisymmetric.

The similarity vorticity equation is

\[
\boxed{
D_BW
=(\Sigma-I)W+\nu\Delta W.
}
\]

The rotational part satisfies

\[
RW=0.
\]

Differentiating the velocity equation gives

\[
\boxed{
D_BA
=\nu\Delta A-A^2-A-\nabla^2P.
}
\]

Taking symmetric parts,

\[
\boxed{
D_B\Sigma
=\nu\Delta\Sigma
-\Sigma^2-R^2
-\Sigma
-\nabla^2P.
}
\]

## 4. Material derivative of stretching production density

Define

\[
\mathfrak p:=W\cdot\Sigma W.
\]

Then

\[
D_B\mathfrak p
=2(D_BW)\cdot\Sigma W
+W\cdot(D_B\Sigma)W.
\]

Using \(RW=0\), hence \(W\cdot R^2W=0\), gives

\[
\boxed{
\begin{aligned}
D_B\mathfrak p
={}&
W\cdot\Sigma^2W
-3\,W\cdot\Sigma W\\
&-W\cdot(\nabla^2P)W\\
&+2\nu\,\Delta W\cdot\Sigma W
+\nu\,W\cdot\Delta\Sigma\,W.
\end{aligned}
}
\]

The first term is nonnegative:

\[
W\cdot\Sigma^2W=|\Sigma W|^2\ge0.
\]

The pressure-Hessian and viscous derivative terms are signed.

## 5. Eulerian annulus derivative

The annulus \(\mathcal A_*\) is fixed in similarity coordinates, so

\[
\mathscr P_A'
=
\int_{\mathcal A_*}\partial_\theta\mathfrak p\,dy.
\]

Since

\[
\partial_\theta\mathfrak p
=D_B\mathfrak p-B\cdot\nabla\mathfrak p
\]

and

\[
\nabla\cdot B=\frac32,
\]

integration by parts gives

\[
-\int_{\mathcal A_*}B\cdot\nabla\mathfrak p
=
-\int_{\partial\mathcal A_*}\mathfrak p\,B\cdot n\,dS
+\frac32\int_{\mathcal A_*}\mathfrak p\,dy.
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathscr P_A'
={}&
\int_{\mathcal A_*}
\Big[
W\cdot\Sigma^2W
-\frac32W\cdot\Sigma W\\
&\qquad
-W\cdot(\nabla^2P)W
+2\nu\Delta W\cdot\Sigma W
+\nu W\cdot\Delta\Sigma\,W
\Big]dy\\
&-
\int_{\partial\mathcal A_*}
(W\cdot\Sigma W)B\cdot n\,dS.
\end{aligned}
}
\]

This is the exact production-event transition law for the fixed annulus.

## 6. q-generator conversion

At fixed similarity radius/depth,

\[
q=\log|y|-\frac\theta2.
\]

Hence q-translation and similarity-time translation have the generator relation

\[
\boxed{
\mathcal L_q=-2\mathcal L_\theta.
}
\]

For the lag-shifted marker

\[
m_h(Y)=m_{pd}(\sigma_{-h}Y),
\]

we therefore have

\[
\boxed{
\mathcal L_qm_h
=-2\chi'(\mathscr P_A)\mathscr P_A'
}
\]

with all quantities evaluated at the appropriately shifted production state.

Thus the M19-287 event-boundary current becomes

\[
\boxed{
-\langle(\mathcal L_qm_h)j_i\rangle
=
2\left\langle
\chi'(\mathscr P_A)\mathscr P_A'\,j_i
\right\rangle.
}
\]

## 7. Explicit channel decomposition

Substituting Section 5 gives the event-boundary current as a sum of correlations of \(j_i\) with:

### S2 — strain-square channel

\[
\boxed{
\int_{\mathcal A_*}|\Sigma W|^2dy.
}
\]

### S1 — production damping channel

\[
\boxed{
-\frac32\int_{\mathcal A_*}W\cdot\Sigma W\,dy.
}
\]

### PH — pressure-Hessian channel

\[
\boxed{
-\int_{\mathcal A_*}W\cdot(\nabla^2P)W\,dy.
}
\]

### VD — viscous derivative-transfer channel

\[
\boxed{
\nu\int_{\mathcal A_*}
\left(
2\Delta W\cdot\Sigma W
+W\cdot\Delta\Sigma\,W
\right)dy.
}
\]

### AB — annular transport-boundary channel

\[
\boxed{
-\int_{\partial\mathcal A_*}
(W\cdot\Sigma W)B\cdot n\,dS.
}
\]

Each is further multiplied by the transition weight

\[
2\chi'(\mathscr P_A)j_i.
\]

No untyped event-boundary remainder remains.

## 8. Audit against existing resource classes

The five channels have familiar structural types:

- **S2:** nonnegative strain-square locally, but its correlation with signed \(j_i\) is not sign-definite;
- **S1:** the existing production observable itself, multiplied by signed current;
- **PH:** nonlocal pressure-Hessian coupling; prior pressure audits show that pressure cannot be treated as a local sign-definite payer without additional structure;
- **VD:** higher-derivative viscous transfer, subject to the existing palinstrophy/raw-H2 and physical-accumulation firewalls;
- **AB:** fixed-annulus transport/export through the production region boundary.

Thus differentiating the event marker does not create a sixth unknown resource. It routes the state-space event-boundary current back into explicit PDE channels.

## 9. Important NO-GO

Because \(\chi'\) is supported near the threshold of the production event, this current measures **entry/exit dynamics**, not the sustained interior value of production.

Repeated crossings can occur indefinitely in a recurrent system. Therefore none of S2/S1/PH/VD/AB is automatically finite simply because the event set has positive measure.

In particular,

\[
\boxed{
\text{event-boundary current}\not\Rightarrow\text{finite number of production events}.
}
\]

## 10. New narrowed target

The highest-value question is now whether the correlation

\[
\boxed{
\left\langle
\chi'(\mathscr P_A)\mathscr P_A'j_i
\right\rangle
}
\]

contains a genuinely two-variable phase-lag/circulation that cannot collapse to a scalar coboundary.

If the selected energy current were a single-valued function of the production scalar alone,

\[
j_i=F(\mathscr P_A),
\]

then the event-boundary term would itself become the derivative of a scalar primitive and have zero invariant mean.

Therefore any nonzero event-boundary current requires nontrivial hysteresis/multidimensional recurrent dynamics in the joint \((\mathscr P_A,j_i)\) state.

This exact statement is the next calculation.

---

\[
\boxed{\text{M19-288 COMPLETE; THE ABSTRACT EVENT-BOUNDARY CURRENT IS FULLY RESOLVED INTO STANDARD NAVIER--STOKES PRODUCTION-EVOLUTION CHANNELS.}}
\]
