# M19-235 — A single-zero vorticity weight forces a linear-in-radius boundary-shear payer

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / BOUNDARY-LAYER PAYER EXTRACTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-232 gives, on the cavity escape branch,

\[
\boxed{
\int_0^{S_j}\|\eta_j\|_2^2ds
\to\frac1{4\nu}.
}
\]

M19-234 strengthens the spatial localization to

\[
\boxed{
\frac{|y|}{R_j}\to1
\quad\text{in the one-period vorticity-energy measure.}
}
\]

The double-zero weight used there intentionally removed all boundary terms. We now use a single-zero weight to expose the boundary flux that must sustain this nonzero vorticity currency.

## 2. Single-zero weight

Set

\[
s_j(y):=\frac{|y|^2}{R_j^2},
\qquad
\boxed{a_j(y):=1-s_j(y).}
\]

Then

\[
a_j|_{S_{R_j}}=0,
\qquad
\partial_na_j|_{S_{R_j}}=-\frac2{R_j},
\]

\[
\boxed{
y\cdot\nabla a_j=-2s_j,}
\]

and

\[
\boxed{\Delta a_j=-\frac6{R_j^2}.}
\]

The relative rotation preserves \(a_j\), so the period endpoint contribution to the weighted vorticity norm vanishes.

## 3. Diffusion now produces an exact boundary enstrophy flux

For the vorticity diffusion term,

\[
\nu\int_{B_{R_j}}a_j\eta_j\cdot\Delta\eta_j,
\]

one integration by parts removes the direct boundary term because \(a_j=0\) on \(S_{R_j}\). The derivative of the weight gives

\[
-\nu\int(\nabla a_j\cdot\nabla\eta_j)\cdot\eta_j.
\]

Integrating this scalar term once more yields

\[
\boxed{
\begin{aligned}
\nu\int a_j\eta_j\cdot\Delta\eta_j
={}&-\nu\int a_j|\nabla\eta_j|^2
+\frac\nu2\int(\Delta a_j)|\eta_j|^2\\
&-\frac\nu2\int_{S_{R_j}}(\partial_na_j)|\eta_j|^2dS.
\end{aligned}}
\]

Using the explicit derivatives,

\[
\boxed{
\nu\int a_j\eta_j\cdot\Delta\eta_j
=-\nu\int a_j|\nabla\eta_j|^2
-\frac{3\nu}{R_j^2}\int|\eta_j|^2
+\frac\nu{R_j}\int_{S_{R_j}}|\eta_j|^2dS.
}
\]

Thus the cavity boundary is the only positive diffusion source in this weighted identity.

## 4. Similarity term is uniformly negative

The amplitude/dilation coefficient is

\[
-\frac14a_j+\frac14y\cdot\nabla a_j.
\]

Since \(a_j=1-s_j\) and \(y\cdot\nabla a_j=-2s_j\),

\[
\boxed{
-\frac14a_j+\frac14y\cdot\nabla a_j
=-\frac14(1+s_j).
}
\]

Hence the negative similarity-vorticity charge does **not** degenerate at the boundary.

## 5. Exact period identity

Using the M19-233 weighted vorticity identity and integrating over one period gives

\[
\boxed{
\begin{aligned}
\frac\nu{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\eta_j|^2dSds
={}&
\nu\int_0^{S_j}\int a_j|\nabla\eta_j|^2\\
&+\frac14\int_0^{S_j}\int(1+s_j)|\eta_j|^2\\
&+\frac{3\nu}{R_j^2}
\int_0^{S_j}\int|\eta_j|^2\\
&-\mathcal E_j^{bg},
\end{aligned}}
\]

where \(\mathcal E_j^{bg}\) consists of the background transport, strain, and the two linearized vorticity-coupling terms:

\[
\frac12(U_j\cdot\nabla a_j)|\eta_j|^2,
\quad
a_j\eta_j^TS_{U_j}\eta_j,
\quad
-a_j\eta_j\cdot((w_j\cdot\nabla)\Omega_j),
\quad
a_j\eta_j\cdot((\Omega_j\cdot\nabla)w_j).
\]

Exactly as in M19-234, local escape plus the retained remote coefficient decay gives

\[
\boxed{\mathcal E_j^{bg}\to0.}
\]

## 6. M19-234 determines the similarity contribution sharply

M19-234 says that \(s_j=|y|^2/R_j^2\to1\) in the vorticity-energy measure. Therefore

\[
\int_0^{S_j}\int(1+s_j)|\eta_j|^2
\to
2\cdot\frac1{4\nu}
=\frac1{2\nu}.
\]

Hence

\[
\boxed{
\frac14
\int_0^{S_j}\int(1+s_j)|\eta_j|^2
\to\frac1{8\nu}.
}
\]

The first and third terms on the right-hand side of the exact boundary identity are nonnegative, with the third tending to zero.

Consequently

\[
\boxed{
\liminf_{j\to\infty}
\frac\nu{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\eta_j|^2dSds
\ge\frac1{8\nu}.
}
\]

Equivalently,

\[
\boxed{
\liminf_{j\to\infty}
\frac1{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\eta_j|^2dSds
\ge\frac1{8\nu^2}.
}
\]

Thus an escaping unit-multiplier cavity mode requires boundary vorticity trace growing at least linearly with the cavity radius.

## 7. Boundary vorticity equals no-slip normal shear

Because

\[
w_j|_{S_{R_j}}=0,
\]

every tangential derivative of the trace vanishes. At the boundary,

\[
\nabla w_j=(\partial_nw_j)\otimes n.
\]

The divergence-free condition gives

\[
\partial_nw_j\cdot n=0,
\]

so \(\partial_nw_j\) is tangential. Hence

\[
\eta_j|_{S_{R_j}}
=n\times\partial_nw_j
\]

up to the fixed orientation convention, and therefore

\[
\boxed{
|\eta_j|=|\partial_nw_j|
\quad\text{on }S_{R_j}.
}
\]

The boundary payer can thus be written as the no-slip shear estimate

\[
\boxed{
\liminf_{j\to\infty}
\frac1{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2dSds
\ge\frac1{8\nu^2}.
}
\]

## 8. Interpretation

The escape branch is no longer merely a spatial-loss scenario. It requires a quantitatively diverging boundary trace:

\[
\boxed{
\text{escape unit mode}
\Longrightarrow
\text{relative boundary-layer vorticity}
+\text{boundary shear payer }\gtrsim R_j.
}
\]

This lower bound is compatible with a very thin no-slip adjustment layer; fixed bulk \(H^1\) cost alone does not immediately contradict it. A boundary derivative can grow while occupying a shrinking normal layer.

Therefore

\[
\boxed{
\text{fixed bulk }H^1\text{ currency}
\neq
\text{uniform boundary-shear upper bound}.
}
\]

## 9. New frontier

The escape problem is sharpened to

\[
\boxed{
\mathcal T_{cav}^{shear}:
\begin{array}{l}
\text{prove an independent upper/Rellich/hidden-regularity estimate for the period-integrated}\\
\text{no-slip shear of a cavity unit mode that is }o(R_j),\\
\text{or classify the singular boundary layer capable of paying the forced }\gtrsim R_j\text{ trace.}
\end{array}}
\]

A successful \(o(R_j)\) boundary-shear upper bound would close the entire M19-231 escape branch.

---

\[
\boxed{\text{M19-235 COMPLETE: ESCAPE FORCES A LINEAR-IN-RADIUS NO-SLIP BOUNDARY-SHEAR PAYER.}}
\]
