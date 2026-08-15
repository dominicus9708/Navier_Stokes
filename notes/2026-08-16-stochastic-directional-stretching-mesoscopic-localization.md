# Stochastic directional stretching localizes to the mesoscopic annulus

Date: 2026-08-16

Status: **DERIVED CONDITIONAL LOCALIZATION USING THE EXISTING BUFFERED CONSTANT-AXIS CHANNEL DECOMPOSITION / CORE SELF-STRETCH AND MACROSCOPIC FAR FIELD ARE O(1) ON A CROSSING PARABOLIC BLOCK / INTERMEDIATE ANNULUS OR DIRECTION-DERIVATIVE CHANNEL REMAINS.**

## 1. Coherent crossing geometry

At the first Gaussian Reynolds-one crossing,

\[
B R^4=1,
\qquad
|\bar\Omega|\ge c_0>0,
\qquad
V_\omega\lesssim R^{-4},
\qquad
R\to\infty.
\]

Let

\[
e=\bar\Omega/|\bar\Omega|.
\]

For a Gaussian of radius `R`, its density on a fixed fractional core `B_{cR}` is bounded below by `c R^{-3}`. Hence

\[
\int_{B_{cR}}|\Omega-\bar\Omega|^2dy
\lesssim
R^3V_\omega
\lesssim
R^{-1}.
\]

In particular the off-axis vorticity satisfies

\[
\boxed{
\|P_{e^\perp}\Omega\|_{L^2(B_{cR})}
\lesssim R^{-1/2}.
}
\]

---

## 2. Buffered constant-axis strain decomposition

The whole-space exact identity for a fixed axis is

\[
2\|Se\|_2
=
\|e\times\Omega\|_2.
\]

Its local use requires a cutoff/divergence correction and therefore produces explicit annular commutator terms. We retain those rather than setting them to zero.

Write schematically on the coherent core

\[
Se
=(Se)_{\rm core}
+(Se)_{\rm ann}
+(Se)_{\rm far},
\]

where the existing buffered local constant-axis route gives

\[
\boxed{
\|(Se)_{\rm core}\|_{L^2(B_{cR})}
\lesssim
R^{-1/2}
}
\]

provided the cutoff/divergence-correction leakage is assigned to `(Se)_ann`.

Thus the coherent one-axis core has only `R^-1/2` local `L2` axial-strain content; all failure of this statement is explicitly an annular/projective/derivative channel.

---

## 3. Exact directional growth instead of the crude operator norm

For the stochastic Cauchy deformation vector `Z`, define its transported unit direction

\[
n_s=Z_s/|Z_s|.
\]

Along each stochastic history,

\[
\boxed{
\frac d{ds}\log|Z_s|
=n_s^T S(X_s,s)n_s.
}
\]

Therefore the relevant potential is directional strain, not the full operator norm.

When `n_s` remains close to the coherent axis `e`,

\[
|n_s^TSn_s-e^TSe|
\le
2|n_s-e|\,|S|.
\]

The second term is retained as the **direction-rotation / projective defect channel**.

---

## 4. Core self-stretching is O(1) over parabolic age R^2

Let `K_tau` be the backward advection--diffusion transition density from the terminal point. The divergence-free Nash estimate gives

\[
\|K_\tau\|_2
\lesssim
(\nu\tau)^{-3/4}.
\]

Hence the expected contribution of the core axial strain is bounded by

\[
\mathbb E
\left[1_{\{X_\tau\in B_{cR}\}}
|e^T(Se)_{\rm core}(X_\tau)|
\right]
\lesssim
(\nu\tau)^{-3/4}R^{-1/2}.
\]

Integrating over a crossing-parabolic backward age `0<tau<cR^2`,

\[
\begin{aligned}
A_{\rm core}
&\lesssim
R^{-1/2}
\int_0^{cR^2}(\nu\tau)^{-3/4}d\tau\\
&\lesssim_ν
R^{-1/2}(R^2)^{1/4}\\
&\lesssim_ν 1.
\end{aligned}
\]

Therefore

\[
\boxed{
A_{\rm core}=O_\nu(1).
}
\]

The coherent core cannot by its own nearly-one-axis strain produce a directional stochastic amplification whose logarithm tends to infinity.

---

## 5. Choose a mesoscopic far cutoff that is also O(1) over R^2

The finite-kinetic-energy remote-strain tail in terminal normalization is

\[
\|S_{>M}\|_\infty
\lesssim
M^{-5/2}W^{1/4}\|u_0\|_2.
\]

Choose

\[
\boxed{
M_*
=R^{4/5}W^{1/10}.
}
\]

Then

\[
M_*^{5/2}=R^2W^{1/4},
\]

so over a parabolic block of duration `O(R^2)`,

\[
\boxed{
R^2\|S_{>M_*}\|_\infty
\lesssim
C(\|u_0\|_2).
}
\]

The far-field directional action is therefore also `O(1)`.

The crossing kinetic-energy duality gives `R \lesssim W^{1/10}`. Consequently

\[
\frac{M_*}{R}
=W^{1/10}R^{-1/5}\to\infty
\]

along the late coherent branch, while

\[
\frac{M_*}{\sqrt W}
=R^{4/5}W^{-2/5}\to0.
\]

Thus the surviving annulus is broad in terminal normalized coordinates but shrinks to zero physical radius.

---

## 6. Localization of any divergent stochastic directional action

Suppose a stochastic Cauchy amplification needs

\[
\log q\to\infty.
\]

The core self-stretching and the field outside `M_*` contribute only `O(1)` on one crossing-parabolic block.

Therefore any divergent directional action must be supplied by at least one of

\[
\boxed{
\text{intermediate annulus }R\lesssim|y-x_*|\lesssim M_*,
}
\]

\[
\boxed{
\text{direction rotation / projective mismatch},
}
\]

or

\[
\boxed{
\text{cutoff commutator / Hessian / higher-derivative concentration}.
}
\]

Schematically,

\[
\boxed{
\log q
\lesssim
O(1)
+A_{R<|y|<M_*}
+A_{\rm dir}
+A_{\rm deriv}.
}
\]

Hence

\[
\boxed{
\log q\to\infty
\Longrightarrow
A_{\rm ann}+A_{\rm dir}+A_{\rm deriv}\to\infty.
}
\]

---

## 7. Relation to the stochastic ancestor escape theorem

The deep-checkpoint ancestor result independently gives

\[
\frac{L}{R_-}\gtrsim R^{(16-\beta)/6}
\quad\lor\quad
\frac{\rho_{\rm reach}}{R_-}\lesssim R^{(\beta-4)/6}.
\]

The present result says that the deformation needed to realize that geometry cannot be supplied by

- the coherent core itself; or
- the macroscopic/fixed physical far field.

Thus scale-space escape must be dynamically generated inside a shrinking mesoscopic annulus, or be paid by direction/derivative degeneration.

This is a considerably smaller spatial target than all of `R^3`.

---

## 8. Claim boundary

The local `R^-1/2` estimate uses the repository's buffered localization of the exact whole-space constant-axis identity. Annular cutoff/divergence-correction errors are not discarded; they are precisely part of the surviving intermediate-annulus channel.

No summable spacetime budget for that annular directional-strain action is proved here.

Overall status: **COHERENT SELF-STRETCH AND MACROSCOPIC FAR STRAIN REMOVED FROM THE DIVERGENT STOCHASTIC ACTION; ACTIVE SOURCE LOCALIZED TO A SHRINKING MESOSCOPIC ANNULUS OR DIRECTION/HIGH-DERIVATIVE DEGENERATION.**
