# Full H1 Production Saturation Rigidity — 2026-08-20

Overall status: **EXACT MAXIMAL P_V H1 PRODUCTION EXCLUDED FOR NONZERO FINITE-ENERGY PROFILES — GLOBAL REGULARITY NOT PROVED.**

This note tracks the equality conditions in the sharp bound

\[
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
\frac4{\sqrt6}\int |S||\nabla S|^2dx.
\]

The conclusion is that exact saturation forces a fixed-axis one-dimensional max-mid strain field, hence is incompatible with a nonzero whole-space `L^2` profile.

---

## 1. Three simultaneous equality requirements

The sharp bound was obtained from three inequalities.

### (a) Spatial covariance

\[
S:M_{sp}\ge s_1|\nabla S|^2.
\]

Equality requires the spatial-index covariance to be supported entirely on the compressive eigenvector `n=e_1`:

\[
\boxed{
\partial_vS=0
\qquad\text{for every }v\perp n.
}
\]

Thus all spatial variation is along `n`.

### (b) Range square bound

For every active derivative matrix `G_k=partial_k S`,

\[
S:G_k^2
\ge
-\frac1{\sqrt6}|S||G_k|^2.
\]

Equality requires

\[
\boxed{
(G_k^2)^\circ
\parallel -S.
}
\]

### (c) Strain eigenvalue bound

\[
-s_1\le\frac2{\sqrt6}|S|.
\]

Equality requires

\[
\boxed{
s_2=s_3,
}
\]

i.e. exact max-mid geometry.

---

## 2. Max-mid representation

Write

\[
S=m(I-3n\otimes n),
\qquad m>0,
\]

so the eigenvalues are

\[
(-2m,m,m).
\]

For this `S`, the negative range-saturation condition

\[
(G^2)^\circ\parallel -S
\]

forces a nonzero trace-free symmetric derivative matrix `G` to be proportional to the same axisymmetric trace-free line

\[
\boxed{
G\in\mathcal L_n
=\operatorname{span}\{I-3n\otimes n\}.
}
\]

Indeed the alternative trace-free square geometry with a zero axial eigenvalue produces `(G^2)^circ` parallel to `+S`, not `-S`, and therefore saturates the wrong sign.

Hence every active derivative obeys

\[
\boxed{
\partial_kS=\alpha_k(I-3n\otimes n).
}
\]

---

## 3. The axis cannot vary

Differentiate

\[
S=m(I-3n\otimes n).
\]

Then

\[
\partial_kS
=(\partial_km)(I-3n\otimes n)
-3m\left(
(\partial_kn)\otimes n+n\otimes(\partial_kn)
\right).
\]

The second term is off the one-dimensional line `L_n` whenever `partial_k n !=0`. Since equality requires every `partial_k S` to lie in `L_n`,

\[
\boxed{
\nabla n=0
}
\]

on every connected active region where `m>0`.

Thus the compressive axis is constant.

---

## 4. One-dimensionality

Spatial covariance saturation already gives

\[
\partial_vS=0
\qquad(v\perp n).
\]

With `n` constant, the only possible variation is

\[
\boxed{
S(x)=m(n\cdot x)(I-3n\otimes n).
}
\]

Therefore a fully H1-saturating profile is constant on every plane perpendicular to `n`.

---

## 5. Whole-space finite-energy contradiction

If `m` is nonzero on a set of positive one-dimensional measure, then `S` has the same nonzero value across an entire transverse plane of infinite area. Consequently

\[
\int_{\mathbb R^3}|S|^2dx=\infty.
\]

Hence

\[
\boxed{
S\in L^2(\mathbb R^3)
\quad\text{and exact full H1 saturation}
\Longrightarrow
S\equiv0.
}
\]

But a first-hitting blowup profile is nontrivial. Therefore exact maximal P_V H1 production is excluded from the finite-energy endgame.

---

## 6. Compactness consequence

On any normalized class of nontrivial profiles that is genuinely precompact in a topology strong enough to make the H1 production functional continuous, and which retains uniform tightness and derivative control, the absence of an exact saturator implies a **strict class-dependent efficiency gap** below the algebraic constant `4/sqrt(6)`.

This observation is useful but must be stated carefully:

- it provides a strict gap relative to the algebraic H1 production cap;
- it does **not** yet prove that the production-to-hyperdissipation ratio is below viscosity;
- therefore it does not by itself close the P_V branch.

A final closure still requires coupling this strict efficiency gap to the first-hitting scale damping and/or a lower bound for `H_S/P_S` on the compact recurrent class.

---

## 7. Near-saturation interpretation

A sequence approaching full H1 saturation must simultaneously approach:

1. max-mid eigenvalue degeneracy `s_2-s_3 ->0`;
2. one-direction spatial gradient covariance;
3. range-square alignment `(G_k^2)^circ || -S`;
4. a fixed compressive eigenaxis.

Failure of any one of these creates a positive efficiency defect. Previous results route the associated geometric failures to max-mid defect, transverse non-tightness `T`, derivative concentration `H`, or projective/eigenframe reorganization.

Status: **THE EXACT ALGEBRAIC MAXIMUM OF P_V-DRIVEN H1 PRODUCTION HAS NO NONZERO FINITE-ENERGY SATURATOR. NEAR-SATURATION REQUIRES A JOINT MAX-MID / ONE-DIMENSIONAL / FIXED-AXIS DERIVATIVE GEOMETRY. GLOBAL REGULARITY REMAINS UNPROVED.**