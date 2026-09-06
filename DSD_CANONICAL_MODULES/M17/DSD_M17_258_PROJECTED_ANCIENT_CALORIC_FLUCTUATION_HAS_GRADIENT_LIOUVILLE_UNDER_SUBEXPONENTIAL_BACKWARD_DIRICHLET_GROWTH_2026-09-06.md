# DSD M17-258 — Projected ancient caloric fluctuation has a gradient Liouville theorem under subexponential backward Dirichlet growth

Date: 2026-09-06  
Canonical ID: **M17-258**

Status: **PROJECTED-CALORIC GRADIENT LIOUVILLE GATE / M17-257 SHOWS THAT A COHERENT AMBIENT MEAN CAN BE QUOTIENTED BY MEAN-ZERO TESTING, LEAVING A CALORIC FLUCTUATION WHEN SCALED DRIFT/STRAIN AND THE MEAN-SHEAR COUPLING VANISH. THE CORRECT LIOUVILLE OBJECT IS THE GRADIENT, BECAUSE SPATIAL CONSTANTS ARE INVISIBLE TO THE PROJECTED EQUATION. IF THE ANCIENT CALORIC GRADIENT HAS SUBEXPONENTIAL BACKWARD `L2` GROWTH, FOURIER PROPAGATION FORCES ALL NONZERO FREQUENCIES TO VANISH. THUS THE GRADIENT IS ZERO, THE PROJECTED FLUCTUATION IS SPATIALLY CONSTANT, AND ITS FIXED-BALL ZERO-MEAN NORMALIZATION MAKES IT ZERO. COMBINED WITH THE M17-251 SCALE-COMPARABLE NONZERO TANGENT AND THE M17-253 NO-H2-DEFECT BRANCH, THIS IS A CONTRADICTION. THEREFORE A SURVIVING PROJECTED CALORIC BRANCH MUST EXHIBIT BACKWARD DIRICHLET GROWTH AT LEAST EXPONENTIAL ALONG A SUBSEQUENCE, OR EXIT THROUGH SUBSCALE/NODAL, NORMALIZED PALINSTROPHY, AMBIENT/COEFFICIENT, OR MEAN-SHEAR CHANNELS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-257

On the coherent-ambient-mean branch, write in intrinsic variables

\[
V_j=\bar V_j+F_j,
\qquad
\fint_{B_1}F_j=0.
\]

M17-257 shows that after testing against mean-zero spatial test functions, the large constant mean disappears except through the coupling

\[
(C_j-\bar C_j)\bar V_j.
\]

Assume on every fixed backward cylinder that

\[
A_j\to0,
\qquad
C_j\to0,
\qquad
\Gamma_j:=|\bar V_j|\,\|C_j-\bar C_j\|_\infty\to0,
\]

and that the M17-255 compactness hypotheses hold.

Then after a diagonal subsequence the projected limit satisfies

\[
\boxed{
\partial_\tau F-\Delta F=b(\tau)
}
\]

in distributions, where `b(tau)` is spatially constant.

Taking one spatial derivative eliminates `b`:

\[
\boxed{
G:=\nabla F,
\qquad
\partial_\tau G=\Delta G.
}
\]

Thus the canonical Liouville object is `G`, not the unprojected field itself.

---

## 2. Backward Dirichlet growth condition

Assume

\[
G(\tau)\in L^2(\mathbb R^3)
\qquad
(\tau\le0)
\]

and define

\[
D_G(T):=\|G(-T)\|_{L^2}.
\]

The required growth condition is only

\[
\boxed{
\limsup_{T\to\infty}
\frac1T\log^+ D_G(T)=0.
}
\]

Equivalently, for every `eps>0` there is `C_eps` such that for all sufficiently large `T`,

\[
D_G(T)\le C_\varepsilon e^{\varepsilon T}.
\]

Uniform boundedness in backward time is sufficient but not necessary.

---

## 3. Fourier propagation

For the heat equation,

\[
\widehat G(0,\xi)
=e^{-T|\xi|^2}\widehat G(-T,\xi).
\]

Fix any `delta>0`. Then

\[
\begin{aligned}
\int_{|\xi|\ge\delta}
|\widehat G(0,\xi)|^2d\xi
&\le
 e^{-2T\delta^2}
 \|G(-T)\|_2^2.
\end{aligned}
\]

For any `eps<delta^2`, the subexponential condition gives

\[
\|G(-T)\|_2^2
\le C_\varepsilon^2e^{2\varepsilon T}
\]

for large `T`. Hence

\[
\int_{|\xi|\ge\delta}
|\widehat G(0,\xi)|^2d\xi
\le
C_\varepsilon^2
 e^{-2(\delta^2-\varepsilon)T}
\to0.
\]

Because `delta>0` is arbitrary,

\[
\operatorname{supp}\widehat G(0)
\subset\{0\}.
\]

An `L2` Fourier function supported at one point is zero. Therefore

\[
\boxed{G(0)=0.}
\]

Time translation gives

\[
\boxed{G\equiv0\text{ on }(-\infty,0].}
\]

---

## 4. Projected fluctuation vanishes

Since

\[
\nabla F\equiv0,
\]

`F` is spatially constant on every connected time slice.

The projected normalization was chosen so that on one fixed reference ball

\[
\fint_{B_1}F(\cdot,\tau)=0.
\]

Therefore

\[
\boxed{F\equiv0.}
\]

---

## 5. Contradiction with the retained scale-comparable derivative charge

M17-251 gives a nonzero time-zero scale-comparable tangent on the retained-inner-mass branch.

M17-253 separates the possibility that the raw `H2` charge is lost in the limit:

- if derivative charge escapes to higher and higher frequencies, it is a vanishing-mass microcarrier and returns to strict subscale/nodal descent;
- on the no-defect branch, a fixed portion of the raw Laplacian charge survives in the time-zero limit.

Because subtracting a spatial constant does not change the Laplacian,

\[
\Delta F_j=\Delta V_j.
\]

Hence on the no-defect branch,

\[
\boxed{
\|\Delta F(0)\|_{L^2(B)}\ge c_*>0
}
\]

for a fixed rescaled core.

But `F identically 0` implies

\[
\Delta F(0)=0,
\]

which is impossible.

Thus the projected caloric no-defect branch cannot satisfy subexponential backward Dirichlet growth.

---

## 6. Prelimit normalized palinstrophy observable

For the intrinsic normalization

\[
V_j(z,\tau)
=
\frac{r_j^{3/2}}{E_j^{1/2}}
W(q_j+r_jz,\theta_j+r_j^2\tau),
\]

the exact global gradient identity is

\[
\boxed{
\Pi_j(\tau)
:=
\int_{\mathbb R^3}|\nabla_zV_j|^2dz
=
\frac{r_j^2}{E_j}
\int_{\mathbb R^3}|\nabla_yW|^2dy.
}
\]

Spatial mean subtraction does not change this gradient.

Therefore one sufficient prelimit route to the Liouville hypothesis is a subexponential-in-`T` bound for the normalized Dirichlet corridor, for example

\[
\boxed{
\limsup_{T\to\infty}
\frac1T
\log^+
\left(
\limsup_j
\sup_{-T\le\tau\le0}
\Pi_j(\tau)^{1/2}
\right)=0.
}
\]

This condition is stronger than the finite-cylinder bounds used in M17-255 and is not yet proved.

---

## 7. Correct branch statement

The projected ancient caloric line now satisfies

\[
\boxed{
H_{projected\ ancient\ caloric}
\Longrightarrow
G_{backward\ Dirichlet\ exponential\ growth}
\lor
G_{H2\ defect/subscale/nodal}
\lor
H_{normalized\ palinstrophy}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{mean\text{-}shear\ coupling}.
}
\]

Here `backward Dirichlet exponential growth` means failure of the subexponential condition along a subsequence.

---

## 8. DSD audit

1. The projected equation is used only modulo spatial constants; the gradient removes that ambiguity exactly.
2. Uniform backward `L2` boundedness is not assumed when subexponential growth suffices.
3. M17-254 provides finite-`T` mass corridors, not the present `T->infinity` Dirichlet growth estimate.
4. A global normalized palinstrophy divergence can be caused by remote parts of the original solution after packet normalization; it is therefore recorded as a branch, not automatically counted as a local physical contradiction.
5. The time-zero derivative charge is used only on the M17-253 no-defect branch.
6. No Liouville conclusion is claimed without an explicit backward growth condition.
7. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
