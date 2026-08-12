# Generalized Galilean lemma for the weighted moving center

Date: 2026-08-12

Status: **DERIVED LEMMA / LOCAL SUITABILITY PRESERVED**.

This lemma closes the former fixed-cylinder transfer obligation for the present whole-space finite-energy proof track. It is not claimed as a novel theorem.

## Lemma 1. Time-dependent translational covariance of suitable solutions

Let `(u,p)` be a suitable weak solution on a spacetime region and let

\[
X\in W^{2,3/2}_{\rm loc}(I;\mathbb R^3).
\]

Set

\[
x=y+X(t),
\]

\[
v(y,t)=u(y+X(t),t)-\dot X(t),
\]

and

\[
q(y,t)=p(y+X(t),t)+\ddot X(t)\cdot y.
\]

On every bounded cylinder in the translated coordinates whose image lies in the original region, `(v,q)` is again a suitable weak solution.

### Proof: momentum equation

For smooth paths first, the chain rule gives

\[
\partial_t v
=(\partial_tu)(y+X,t)
+\dot X\cdot\nabla u(y+X,t)
-\ddot X.
\]

Also

\[
(v\cdot\nabla)v
=(u-\dot X)\cdot\nabla u.
\]

Therefore

\[
\partial_tv+(v\cdot\nabla)v
=(\partial_tu+u\cdot\nabla u)(y+X,t)-\ddot X.
\]

Since

\[
\nabla_yq
=\nabla_xp(y+X,t)+\ddot X,
\]

we obtain

\[
\partial_tv+(v\cdot\nabla)v
=-\nabla q+\nu\Delta v,
\qquad
\nabla\cdot v=0.
\]

For `X in W^{2,3/2}`, approximate `X` in `W^{2,3/2}` by smooth paths.  Translation is continuous on local Lebesgue/Sobolev spaces, so the transformed distributional equation follows by passage to the limit.

### Pressure class

On a bounded spatial ball `B_R`,

\[
|\ddot X(t)\cdot y|
\le R|\ddot X(t)|.
\]

Thus

\[
\ddot X(t)\cdot y
\in L^{3/2}(I\times B_R).
\]

Since translated `p` remains locally `L^{3/2}`, so does `q`.

### Energy-defect identity

For a divergence-free field `w` with pressure `r`, define the momentum residual

\[
\mathcal R[w,r]
=
\partial_tw+(w\cdot\nabla)w+\nabla r-\nu\Delta w
\]

and the local energy residual

\[
\mathcal D[w,r]
=
\partial_t\frac{|w|^2}{2}
+\nabla\cdot\left[\left(\frac{|w|^2}{2}+r\right)w\right]
-\nu\Delta\frac{|w|^2}{2}
+\nu|\nabla w|^2.
\]

For smooth fields,

\[
\mathcal D[w,r]=w\cdot\mathcal R[w,r].
\]

Under the translation above, the momentum residual transforms covariantly:

\[
\mathcal R[v,q](y,t)
=
\mathcal R[u,p](y+X(t),t).
\]

Writing `u=v+Xdot` gives

\[
\mathcal D[u,p](y+X,t)
=
\mathcal D[v,q](y,t)
+
\dot X(t)\cdot\mathcal R[v,q](y,t).
\]

The same identity holds distributionally by smoothing `u,p,X`, or equivalently by testing the weak momentum equation against the coherent translational component.  Since the momentum residual vanishes distributionally,

\[
\boxed{
\mathcal D[v,q]
=
\mathcal D[u,p]\circ(y+X(t)).
}
\]

Hence the sign of the local energy defect is preserved under the transformation.  Suitability of `(u,p)` therefore implies suitability of `(v,q)`.

QED.

---

## Lemma 2. The weighted-mean path has the required acceleration integrability

Use the weighted center from `2026-08-12-weighted-variance-lemma-completion.md`:

\[
\dot X(t)=\bar U(t)
=
M_\ell^{-1}
\int\phi_\ell(x-X(t))u(x,t)dx.
\]

The moving weighted momentum identity is

\[
M_\ell\dot{\bar U}
=
\int u[(u-\bar U)\cdot\nabla\varphi]dx
+
\int p\nabla\varphi dx
+
\nu\int u\Delta\varphi dx.
\]

At every fixed positive `ell`:

1. the first term belongs to `L^\infty_t` on finite intervals, using the global `L^2` energy bound and the bounded compactly supported cutoff derivatives;
2. the third term also belongs to `L^\infty_t`;
3. the pressure term belongs to `L^{3/2}_t`, because `p in L^{3/2}_{loc}(dt dx)` and the cutoff support has finite volume.

Therefore

\[
\boxed{
\bar U'\in L^{3/2}_{loc}(dt),
\qquad
X\in W^{2,3/2}_{loc}(dt).
}
\]

The weighted moving center thus satisfies Lemma 1.

---

## Corollary. Fixed-cylinder representation of the moving weighted sphere

Fix a candidate endpoint `(x_*,T)` and a positive scale `ell`.  Because the weighted mean vector field is measurable in time and Lipschitz in the center, the center ODE can be solved **backwards** with terminal condition

\[
X(T)=x_*.
\]

On the interval `[T-ell^2,T]`, define

\[
v(y,t)=u(y+X(t),t)-\dot X(t).
\]

Then `(v,q)` is a suitable weak solution on the ordinary fixed cylinder

\[
B_{c\ell}(0)\times(T-\ell^2,T)
\]

for every fixed cutoff support factor `c` allowed by the construction.

The physical candidate point `(x_*,T)` is exactly `(0,T)` in the translated coordinates.

Therefore a published **pressure-free one-scale epsilon-regularity criterion** can be applied directly to `v` on a fixed cylinder.  No moving-cylinder covering argument is required.

If the criterion yields local boundedness of `v`, then local boundedness of `u` follows because

\[
u(x,t)=v(x-X(t),t)+\dot X(t)
\]

and `dot X=bar U in W^{1,3/2}` is continuous and bounded on compact time intervals.

---

## Proof-route consequence

The former geometric transfer obligation is closed for the whole-space finite-energy track:

\[
\boxed{
\text{weighted moving sphere}
\longleftrightarrow
\text{fixed suitable cylinder for }v.
}
\]

The primary unresolved step is now quantitative rather than coordinate-theoretic:

\[
\boxed{
\text{force the pressure-free critical }L^{5/2+\delta}
\text{ smallness of }v
\text{ at some sufficiently small scale around every candidate singular point.}
}
\]

No such arbitrary-data smallness theorem is currently proved in this repository.
