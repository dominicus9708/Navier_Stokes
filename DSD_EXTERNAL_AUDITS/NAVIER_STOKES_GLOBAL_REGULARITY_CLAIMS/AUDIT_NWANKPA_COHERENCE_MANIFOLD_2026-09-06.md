# DSD Audit — Nwankpa Coherence Manifold / Logic of Fluids

Date: 2026-09-06
Source: Amarachukwu Nwankpa, *The Logic of Fluids: Coherence and Regularity in the Navier–Stokes System*, Preprints.org 202506.2259, v4.
Audit status: **CORE_HINGE_FAIL — L3 RIGIDITY INEQUALITY**

## 1. Claimed chain

The paper defines

\[
\Sigma=L^2(\mathbb R^3)\cap L^3(\mathbb R^3)
\]

and aims to prove:

\[
\text{Leray energy}
\to
\text{time-integrated critical control}
\to
\sup_t\|u(t)\|_3<\infty
\to
\text{ESS regularity and uniqueness}.
\]

The decisive step is the conversion from energy/interpolation information to the uniform-in-time critical L3 bound.

## 2. Pressure-term audit

The manuscript's Structural Rigidity Lemma states that after multiplying the momentum equation by the nonlinear L3 test, the pressure term vanishes by incompressibility.

For the natural test field

\[
\varphi=|u|u,
\]

the pressure contribution is

\[
\int_{\mathbb R^3}\nabla p\cdot |u|u\,dx
=-\int_{\mathbb R^3}p\,\nabla\cdot(|u|u)\,dx.
\]

Although

\[
\nabla\cdot u=0,
\]

one has

\[
\nabla\cdot(|u|u)=u\cdot\nabla|u|
\]

in general, which is not zero.

Therefore incompressibility does not remove the pressure term against this nonlinear test.

The cancellation rule is:

\[
\int\nabla p\cdot\varphi=0
\]

only when the test field is divergence-free (or when a separate pressure identity proves cancellation). `|u|u` is not generally divergence-free.

## 3. Integrated-to-uniform audit

Energy and Gagliardo–Nirenberg interpolation can provide spacetime integrability. But, without an additional valid differential inequality,

\[
f\in L^p_t
\not\Rightarrow
f\in L^\infty_t.
\]

Thus even a correct finite integral involving `\|u(t)\|_3` cannot by itself yield

\[
\sup_{t<T}\|u(t)\|_3<\infty.
\]

The ESS theorem requires precisely a critical uniform endpoint condition; it cannot be invoked after replacing that hypothesis by a weaker time-integrated statement.

## 4. Consequence for uniqueness

The paper's later uniqueness/regularity claims consume the unproved `L_t^∞L_x^3` persistence. Once the Structural Rigidity Lemma fails, those downstream steps become conditional rather than established.

## 5. Surviving components

The following conceptual points are not refuted by this audit:

- `L^2` and `L^3` are natural energy/critical spaces;
- pressure is nonlocally determined by velocity through the elliptic constraint;
- ESS is a powerful endpoint regularity result;
- studying invariance of an intersection space is a legitimate direction.

What fails is the claimed proof that ordinary Leray–Hopf energy control automatically supplies the needed critical uniform bound.

## 6. DSD verdict

\[
\boxed{
\text{Pressure cancellation is invalid for the L3 nonlinear test.}
}
\]

Therefore the central `Structural Rigidity` gate is open, and the global regularity claim does not follow.

Global regularity remains unproved.
