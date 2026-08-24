# Local Enstrophy IMS Diffusion Sharpening — 2026-08-24

Status: **STRICT SHARPENING OF THE LOCALIZED CORE ENSTROPHY GATE / REMOVES THE DIFFUSIVE CUTOFF LOSS FROM THE GENERIC FLUX PARAMETER / GLOBAL REGULARITY NOT PROVED.**

This note revisits `LOCALIZED_CORE_ENSTROPHY_TELESCOPING_GATE_2026-08-24.md` and uses the special choice `phi=psi^2` more fully.

The earlier derivation treated the cutoff-gradient term in `grad(psi Omega)` by a triangle/Young estimate. That bound is valid but loses a large amount. The local enstrophy diffusion term contains the exact compensating cutoff Laplacian. Combining them first yields a sharper IMS-type identity.

## 1. Exact localized enstrophy identity

With

\[
\phi=\psi^2,
\qquad
Z_\phi=\int\psi^2|\Omega|^2,
\qquad
Q_\phi=\int\psi^2|\nabla\Omega|^2,
\]

the dynamically normalized local enstrophy identity is

\[
\frac12Z_\phi'
+\frac b4Z_\phi
+\nu Q_\phi
=P_\phi+F_{mat}
+\frac\nu2\int|\Omega|^2\Delta(\psi^2),
\]

where

\[
F_{mat}
=
\frac12\int|\Omega|^2(V-a_s)\cdot\nabla(\psi^2).
\]

Only the material/dilation crossing term remains in `F_mat`; diffusion will now be combined exactly with `Q_phi`.

## 2. Exact IMS identity

Expand

\[
\nabla(\psi\Omega)
=\psi\nabla\Omega+\Omega\otimes\nabla\psi.
\]

After one integration by parts,

\[
\boxed{
\int|\nabla(\psi\Omega)|^2
=Q_\phi-
\int\psi\Delta\psi\,|\Omega|^2.
}
\]

Since

\[
\frac12\Delta(\psi^2)
=|\nabla\psi|^2+\psi\Delta\psi,
\]

we obtain

\[
\boxed{
Q_\phi
-
\frac12\int|\Omega|^2\Delta(\psi^2)
=\|
abla(\psi\Omega)\|_2^2
-
\int|\nabla\psi|^2|\Omega|^2.
}
\]

Hence the exact local enstrophy ledger can be rewritten as

\[
\boxed{
\frac12Z_\phi'
+\frac b4Z_\phi
+\nu\|\nabla(\psi\Omega)\|_2^2
=P_\phi+F_{mat}
+\nu\int|\nabla\psi|^2|\Omega|^2.
}
\]

This is strictly better suited to Dirichlet localization than treating `Q_phi` and `Delta phi` separately.

## 3. Dirichlet gap minus a pure annular-mass error

Let

\[
\psi=1\text{ on }B_R,
\qquad
\psi=0\text{ outside }B_{LR},
\qquad L>1,
\]

with

\[
|\nabla\psi|\le[(L-1)R]^{-1}.
\]

Assume the transition-annulus mass bound

\[
\boxed{
Z_{tr}:=
\int_{\operatorname{supp}\nabla\psi}|\Omega|^2
\le\varepsilon_b Z_\phi.
}
\]

Because `psi Omega in H_0^1(B_{LR})`, the exact ball Dirichlet eigenvalue gives

\[
\boxed{
\|\nabla(\psi\Omega)\|_2^2
\ge
\frac{\pi^2}{L^2R^2}Z_\phi.
}
\]

The IMS error satisfies

\[
\boxed{
\int|\nabla\psi|^2|\Omega|^2
\le
\frac{\varepsilon_b}{(L-1)^2R^2}Z_\phi.
}
\]

Therefore the net localized viscous frequency is

\[
\boxed{
\lambda_{IMS}(L,\varepsilon_b)
=
\frac1{R^2}
\left[
\frac{\pi^2}{L^2}
-
\frac{\varepsilon_b}{(L-1)^2}
\right].
}
\]

This lower bound is positive whenever

\[
\varepsilon_b
<
\pi^2\frac{(L-1)^2}{L^2}.
\]

## 4. Optimize the cutoff factor exactly

For `0<=epsilon_b<pi^2`, optimize

\[
f(L)=\frac{\pi^2}{L^2}
-
\frac{\varepsilon_b}{(L-1)^2}.
\]

The critical point satisfies

\[
\frac{L-1}{L}
=
\frac{\varepsilon_b^{1/3}}{\pi^{2/3}}.
\]

Hence

\[
\boxed{
L_{opt}
=
\frac{\pi^{2/3}}
{\pi^{2/3}-\varepsilon_b^{1/3}}.
}
\]

Substitution gives the optimized exact constant

\[
\boxed{
\Lambda_{IMS}(\varepsilon_b)
=
\left(
\pi^{2/3}-\varepsilon_b^{1/3}
\right)^3.
}
\]

Thus

\[
\boxed{
\lambda_{IMS}^{opt}
=
\frac{\Lambda_{IMS}(\varepsilon_b)}{R^2}.
}
\]

Useful values are

\[
\boxed{
\Lambda_{IMS}(1/4)
\approx3.4777401279,
}
\]

\[
\boxed{
\Lambda_{IMS}(1/2)
\approx2.4676477571,
}
\]

\[
\boxed{
\Lambda_{IMS}(1)
\approx1.5012392490.
}
\]

For `epsilon_b=1`,

\[
L_{opt}\approx1.873340023<2.
\]

Therefore the one-step condition

\[
\int_{B_{2R}\setminus B_R}|\Omega|^2
\le
\int_{B_R}|\Omega|^2
\]

already suffices to use the optimized `epsilon_b=1` cutoff, because its support lies strictly inside `B_{2R}`.

## 5. Sharpened local finite-stage inequality

Retain the localized production estimate

\[
P_\phi
\le C_{prod}(\beta_S)Z_\phi,
\qquad
C_{prod}(\beta_S)=\sqrt{\frac{1+2\beta_S}{3}}.
\]

Parameterize only the **material crossing** term by

\[
\boxed{
F_{mat}\le f_{mat}Z_\phi+
\eta_{mat}\nu
\|\nabla(\psi\Omega)\|_2^2,
\qquad 0\le\eta_{mat}<1.
}
\]

Then

\[
\boxed{
\frac12(\log Z_\phi)'
+\frac b4
\le
C_{prod}(\beta_S)+f_{mat}
-(1-\eta_{mat})\nu
\frac{\Lambda_{IMS}(\varepsilon_b)}{R^2}.
}
\]

Hence an infinite retained-packet corridor is impossible whenever

\[
\boxed{
\left[
C_{prod}(\beta_S)+f_{mat}
-(1-\eta_{mat})\nu
\frac{\Lambda_{IMS}(\varepsilon_b)}{R^2}
\right]_+
L_{stage,+}
<\frac14\log q.
}
\]

The generic diffusive-boundary parameter `eta_b` from the previous version is no longer needed: the diffusion cutoff term is already incorporated exactly into the IMS frequency.

## 6. New timing-independent benchmark

In the ideal quiet case

\[
\beta_S=f_{mat}=\eta_{mat}=0,
\qquad
\nu=1,
\]

timing is irrelevant if

\[
\frac{\Lambda_{IMS}(\varepsilon_b)}{R^2}
\ge\frac1{\sqrt3}.
\]

For the robust one-step value `epsilon_b=1`,

\[
\boxed{
R
\le
\sqrt{\sqrt3\,\Lambda_{IMS}(1)}
\approx1.6126
}
\]

(up to the displayed rounding) is timing-independently excluded on the zero-error local lane.

This is stronger than the previous triangle-estimate benchmark and requires only that the first doubling annulus carry no more vorticity enstrophy than the core.

## 7. Anti-proof significance

The earlier local frequency floor

\[
(\sqrt\pi-\varepsilon_b^{1/4})^4/R^2
\]
remains a valid lower estimate, but it is not sharp for the actual localized enstrophy ledger because it ignores the exact cancellation between `Q_phi` and the cutoff Laplacian diffusion term.

The correct preferred local ledger is the IMS form derived here.

The amplitude-cap annular-growth audit still cannot by itself guarantee a transition satisfying the positive-frequency condition; a coherent constant-vorticity plateau remains a genuine static survivor. That survivor is handled dynamically by `MEAN_VORTICITY_PLATEAU_STAGE_LEDGER_2026-08-24.md`.

Status: **USING `phi=psi^2`, THE LOCAL DIFFUSION TERMS COMBINE INTO AN EXACT IMS IDENTITY. THE OPTIMIZED NET FREQUENCY CONSTANT IMPROVES FROM `(sqrt(pi)-epsilon^(1/4))^4` TO `(pi^(2/3)-epsilon^(1/3))^3`. FOR A FIRST DOUBLING ANNULUS WITH MASS AT MOST THE CORE (`epsilon=1`), THE OPTIMIZED CONSTANT IS ABOUT `1.50124` AND THE IDEAL TIMING-INDEPENDENT EXCLUSION RADIUS RISES TO ABOUT `1.61 sqrt(nu)`. THE LARGE-ANNULUS COMPLEMENT REMAINS THE COHERENT-PLATEAU/DERIVATIVE BRANCH, NOT AN AUTOMATIC T LABEL. GLOBAL REGULARITY REMAINS UNPROVED.**