# M18-088 — The amplitude-moment baseline localizes exactly to one material population, but the kappa diffusion sink acquires a signed boundary-exchange term

**Date:** 2026-09-11  
**Status:** MATERIAL-POPULATION MOMENT LOCALIZATION / EXACT MULTI-P BASELINE / BOUNDARY-DIFFUSION DEFECT IDENTIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-087 reduces recurrent controlled CE-H current events, on the quiet branch, to one persistent fixed-flux material population \(P_*\) carrying current events at positive frequency.

The next question is whether the global M18-060--069 multi-\(p\) amplitude-moment identities localize to this one material population.

There are two different answers.

1. The **kinematic moment baseline** localizes exactly to a genuine material population:
   \[
   \boxed{
   \mathbb E_p^{P}[\sigma+\kappa]
   =1-\frac{3}{2p}
   }
   \]
   under recurrent nondegenerate population moments.
2. The stronger statement that \(\kappa\) is a nonpositive diffusion sink does **not** localize without correction. Integration by parts produces a signed boundary-diffusion exchange term.

Thus the global multi-\(p\) growth shift survives population localization, but the strain-versus-diffusion-depletion split must be modified by population-boundary exchange.

---

## 2. Genuine material population

Let

\[
P(\theta)\subset\mathbb R^3
\]

be a smooth material carrier region transported by the CE-H similarity material field

\[
B=U+\frac12y,
\qquad
\nabla\cdot B=\frac32.
\]

Equivalently, use a material cutoff \(\eta_P\) satisfying

\[
\boxed{D_B\eta_P=0}
\]

and interpret the formulas below in the smooth-cutoff sense.

If the carrier/cutoff cannot be made material over the interval under audit, record

\[
\boxed{G_{population\ realization/exchange}}.
\]

No silent Eulerian localization is allowed.

---

## 3. Population amplitude moment

For finite \(p\ge2\), define

\[
\boxed{
M_p^P(\theta)
:=
\int_{P(\theta)}\rho^pdy.
}
\]

The CE-H material amplitude law is

\[
D_B\rho=(\sigma+\kappa-1)\rho.
\]

Therefore

\[
D_B(\rho^p)
=p(\sigma+\kappa-1)\rho^p.
\]

The Reynolds transport formula for a region moving with \(B\) gives

\[
\frac d{d\theta}
\int_{P(\theta)}f\,dy
=
\int_{P(\theta)}
\left(D_Bf+(\nabla\cdot B)f\right)dy.
\]

Hence

\[
\boxed{
(M_p^P)'
=
\frac32M_p^P
+p\int_P(\sigma+\kappa-1)\rho^pdy.
}
\]

Equivalently,

\[
\boxed{
\frac1p(M_p^P)'
=
\int_P(\sigma+\kappa)\rho^pdy
-c_pM_p^P,
\qquad
c_p:=1-\frac{3}{2p}.
}
\]

This is the exact population-localized counterpart of M18-060.

---

## 4. No boundary term in the kinematic material-moment law

The absence of a boundary term in Section 3 is important.

The region itself moves with the material field \(B\). Thus advective transport across the moving boundary is already absorbed by the Reynolds formula.

Therefore the population baseline is not shifted by ordinary carrier motion.

A boundary term appears only when the Laplacian eigenline relation is integrated by parts to reinterpret \(\kappa\) as diffusion.

This distinction must be preserved.

---

## 5. Recurrent population baseline

Assume one persistent population satisfies, on the invariant/recurrent branch,

\[
0<m_{p,-}
\le
M_p^P(\theta)
\le
m_{p,+}<\infty
\]

in the recurrent sense needed to make the logarithmic/state drift vanish in long-time average.

Then

\[
\left\langle(M_p^P)'\right\rangle=0.
\]

Hence

\[
\boxed{
\left\langle
\int_P(\sigma+\kappa)\rho^pdy
\right\rangle
=
c_p\left\langle M_p^P\right\rangle.
}
\]

Define the joint population-weighted expectation

\[
\boxed{
\mathbb E_p^P[f]
:=
\frac{
\left\langle\int_P f\rho^pdy\right\rangle
}{
\left\langle M_p^P\right\rangle
}.
}
\]

Then

\[
\boxed{
\mathbb E_p^P[\sigma+\kappa]
=
c_p
=
1-\frac{3}{2p}.
}
\]

Thus the global similarity baseline localizes exactly to every recurrent nondegenerate genuine material population.

---

## 6. Two-exponent population growth shift

For

\[
q>p\ge2,
\]

if both \(M_p^P\) and \(M_q^P\) are recurrent/nondegenerate, then

\[
\boxed{
\mathbb E_q^P[\sigma+\kappa]
-
\mathbb E_p^P[\sigma+\kappa]
=
\delta_{pq}
:=
\frac32\left(\frac1p-\frac1q\right)>0.
}
\]

Moreover the same change-of-measure identity holds inside the population:

\[
\boxed{
\mathbb E_q^P[f]
=
\frac{
\mathbb E_p^P[f\rho^{q-p}]
}{
\mathbb E_p^P[\rho^{q-p}]
}.
}
\]

Hence

\[
\boxed{
\operatorname{Cov}_p^P
(\sigma+\kappa,\rho^{q-p})
=
\delta_{pq}
\mathbb E_p^P[\rho^{q-p}].
}
\]

So one persistent current-carrying material population itself inherits the positive amplitude/growth covariance.

This result does not require one infinitesimal tube label to recur.

---

## 7. Localized kappa integration by parts

Now use

\[
\Delta W=\kappa W.
\]

Multiply by

\[
\rho^{p-2}W
\]

and integrate over \(P\):

\[
\int_P\kappa\rho^pdy
=
\int_P\rho^{p-2}W\cdot\Delta Wdy.
\]

Integration by parts yields

\[
\begin{aligned}
\int_P\kappa\rho^pdy
&=
\int_{\partial P}
\rho^{p-2}W\cdot\partial_nW\,dS\\
&\quad
-
\int_P\nabla(\rho^{p-2}W):\nabla W\,dy.
\end{aligned}
\]

The bulk term is exactly the M18-060 weighted diffusion:

\[
D_p^P
:=
\int_P\rho^{p-2}|\nabla W|^2dy
+(p-2)
\int_P\rho^{p-2}|\nabla\rho|^2dy.
\]

Since

\[
W\cdot\partial_nW
=
\rho\,\partial_n\rho,
\]

define the signed boundary exchange

\[
\boxed{
B_p^P
:=
\int_{\partial P}
\rho^{p-1}\partial_n\rho\,dS
=
\frac1p
\int_{\partial P}\partial_n(\rho^p)dS.
}
\]

Then

\[
\boxed{
\int_P\kappa\rho^pdy
=
-D_p^P+B_p^P.
}
\]

This is the exact localization defect.

---

## 8. Population source-sink-exchange balance

Substitute Section 7 into the population moment equation:

\[
\boxed{
\frac1p(M_p^P)'
=
A_p^P
-D_p^P
+B_p^P
-c_pM_p^P,
}
\]

where

\[
\boxed{
A_p^P
:=
\int_P\sigma\rho^pdy.
}
\]

Thus population amplitude maintenance has four channels:

1. aligned strain source \(A_p^P\);
2. internal weighted diffusion sink \(D_p^P\ge0\);
3. signed diffusive boundary exchange \(B_p^P\);
4. similarity damping \(c_pM_p^P\).

The global whole-space identity is recovered because the boundary term vanishes at infinity.

---

## 9. Boundary exchange is the only obstruction to localizing kappa-as-sink

Globally,

\[
\int\kappa\rho^p=-D_p\le0.
\]

On one material population,

\[
\boxed{
\mathbb E_p^P[\kappa]
=
-d_p^P+b_p^P,
}
\]

where

\[
d_p^P
:=
\frac{\langle D_p^P\rangle}
{\langle M_p^P\rangle}
\ge0,
\]

and

\[
b_p^P
:=
\frac{\langle B_p^P\rangle}
{\langle M_p^P\rangle}
\]

is signed.

Therefore local \(\kappa\) can be positive on average only through net diffusive inflow across the population boundary.

This gives the exact interpretation:

\[
\boxed{
\text{population positive-kappa recharge}
=
\text{boundary diffusion import minus internal diffusion}.
}
\]

---

## 10. Correct population two-exponent split

The exact growth shift remains

\[
\delta_{pq}
=
\left(
\mathbb E_q^P[\sigma]-\mathbb E_p^P[\sigma]
\right)
+
\left(
\mathbb E_q^P[\kappa]-\mathbb E_p^P[\kappa]
\right).
\]

Using Section 9,

\[
\mathbb E_q^P[\kappa]-\mathbb E_p^P[\kappa]
=
(d_p^P-d_q^P)
+
(b_q^P-b_p^P).
\]

Hence

\[
\boxed{
\delta_{pq}
=
\Delta_{pq}^{strain,P}
+
\Delta_{pq}^{diff,P}
+
\Delta_{pq}^{bdry,P},
}
\]

where

\[
\Delta_{pq}^{strain,P}
:=
\mathbb E_q^P[\sigma]-\mathbb E_p^P[\sigma],
\]

\[
\Delta_{pq}^{diff,P}
:=
d_p^P-d_q^P,
\]

and

\[
\Delta_{pq}^{bdry,P}
:=
b_q^P-b_p^P.
\]

Thus the global M18-069 two-way dichotomy becomes a population-level **three-channel split**:

\[
\boxed{
\text{strain segregation}
\lor
\text{internal diffusion depletion}
\lor
\text{amplitude-dependent boundary diffusion exchange}.
}
\]

---

## 11. Canonical third-gap trichotomy

At least one of the three channels has magnitude at least one third of the universal shift in the appropriate signed direction.

More precisely, since

\[
\Delta_{strain}
+
\Delta_{diff}
+
\Delta_{bdry}
=
\delta_{pq}>0,
\]

one must have

\[
\boxed{
\Delta_{strain}
\ge\frac{\delta_{pq}}3
\quad\lor\quad
\Delta_{diff}
\ge\frac{\delta_{pq}}3
\quad\lor\quad
\Delta_{bdry}
\ge\frac{\delta_{pq}}3.
}
\]

Thus recurrent population growth cannot hide all three mechanisms simultaneously.

The first two recover the familiar M18-069 architecture inside the population.

The third is a new explicit **boundary-exchange branch**.

---

## 12. Meaning of the boundary-exchange branch

If

\[
\boxed{
\Delta_{pq}^{bdry,P}
=
b_q^P-b_p^P
\ge
\frac{\delta_{pq}}3,
}
\]

then stronger high-amplitude weighting sees a more favorable signed diffusive boundary exchange.

This can mean, schematically,

- high-amplitude material is preferentially imported through the population boundary;
- lower-amplitude material is preferentially exported;
- or the normal amplitude gradient is organized differently on high- and low-amplitude boundary sectors.

This is not an internal diffusion depletion.

It is an inter-population transfer mechanism, exactly the kind of current/redistribution channel isolated in M18-071--087.

Thus localization closes conceptually: the new defect is not mysterious; it is the boundary manifestation of population exchange.

---

## 13. Relation to the material surface current

The scalar boundary term

\[
B_p^P
=
\int_{\partial P}\rho^{p-1}\partial_n\rho\,dS
\]

is not identical to the vector surface-current norm

\[
\|J_G\|_2.
\]

However both are diffusive transfer observables across a material population boundary.

A direct identity between them would require the detailed geometry of \(\partial P\), the decomposition of \(\nabla W\), and the relation between population boundaries and vortex-transverse Frobenius patches.

No such identity is asserted here.

The valid statement is only:

\[
\boxed{
\text{population localization defect}
=
\text{signed diffusive boundary exchange}.
}
\]

---

## 14. Smooth-cutoff version

If a sharp material boundary is inconvenient, let \(\eta_P\) be a smooth material cutoff satisfying

\[
D_B\eta_P=0.
\]

Then

\[
M_{p,\eta}
:=
\int\eta_P\rho^pdy
\]

obeys the same kinematic baseline, while integration by parts gives the cutoff exchange term

\[
\boxed{
B_{p,\eta}
=
-\int
\rho^{p-2}W\cdot(\nabla\eta_P\cdot\nabla W)
\,dy
}
\]

in the corresponding tensor notation, equivalently the smooth localization of normal diffusive flux.

Thus the branch distinction is robust and does not depend on sharp-boundary regularity.

---

## 15. Consequence for M18-084--087

M18-087 gives one persistent fixed-flux population carrying positive-density current events.

If its \(p\)- and \(q\)-moments remain recurrent/nondegenerate, M18-088 proves that the population itself must realize one of

\[
\boxed{
G_{strain\text{-}seg}^{P}
\lor
G_{diff\text{-}depletion}^{P}
\lor
G_{boundary\text{-}exchange}^{P}.
}
\]

The first two feed back into the existing amplitude/sheath architecture.

The third feeds back into the material-current/redistribution architecture.

Thus the controlled persistent-population branch forms a closed **three-channel structural loop** rather than generating an untyped local endpoint.

---

## 16. No contradiction yet

A recurrent population can continually exchange diffusive amplitude with neighboring populations while maintaining bounded moments.

Therefore

\[
\boxed{
G_{boundary\text{-}exchange}^{P}
\not\Rightarrow
\text{monotone depletion or finite exhaustion}.
}

The exchange may reverse and recycle, just as the lineage current may.

The gain is localization and channel completeness, not closure.

---

## 17. Highest-value next target

M18-089 should compare the signed population boundary exchange

\[
B_p^P
\]

with the finite-lineage graph current of M18-077.

The key question is whether summing \(B_p^P\) over all persistent populations cancels pairwise on internal boundaries, leaving only export/outer-boundary terms.

If so, the population exchange defects form a finite conservative network:

\[
\boxed{
\sum_i B_p^{P_i}
=
B_p^{external}.
}

On a closed saturated local network with no export, the internal exchange would sum to zero, forcing the universal multi-p growth shift to be redistributed among populations rather than supplied externally.

That may sharpen the finite-cycle problem substantially.

---

## 18. Audit verdict

### Certified

1. The global amplitude-moment baseline localizes exactly to any genuine material population.
2. Recurrent nondegenerate population moments satisfy
   \[
   \mathbb E_p^P[\sigma+\kappa]=1-\frac{3}{2p}.
   \]
3. The two-exponent positive growth shift survives exactly inside the population.
4. Localizing \(\kappa\) as diffusion produces the signed boundary term
   \[
   B_p^P=\int_{\partial P}\rho^{p-1}\partial_n\rho.
   \]
5. Therefore \(\kappa\) is not necessarily a pure sink on one population.
6. The population growth shift splits into strain segregation, internal diffusion depletion, or amplitude-dependent boundary diffusion exchange.
7. The boundary-exchange branch is the expected localization of inter-population redistribution, not a new unexplained currency.

### Still open

- pairwise cancellation / graph representation of population boundary exchange;
- population residence decompactification;
- mean conservative lineage circulation;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 19. Next target

M18-089 should derive the exchange-matrix conservation law for a finite partition of the saturated persistent population network and determine whether internal boundary terms cancel exactly under compatible material interfaces.
