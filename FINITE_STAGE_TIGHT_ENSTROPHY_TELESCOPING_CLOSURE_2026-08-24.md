# Finite-Stage Tight-Enstrophy Telescoping Closure — 2026-08-24

Status: **NEW S-LEVEL CLOSURE CERTIFICATE FOR THE STAGE-WIDE VORTICITY-TIGHT CORRIDOR / ANCIENT LIMIT NOT NEEDED / GLOBAL REGULARITY NOT PROVED.**

This note combines

- the exact physical enstrophy identity;
- the sharp trace-free vortex-stretching coefficient;
- the optimized Dirichlet frequency floor forced by stage-wide vorticity tightness;
- the endpoint normalized-enstrophy lower/upper bounds already present in `SMOOTH_THICK_CORE_FLUX_ENSTROPHY_GATE_2026-08-21.md`.

The main gain is conceptual and quantitative: on the tight corridor, the proof does not need to pass to an ancient solution. The required geometric scale growth telescopes directly across the original smooth first-hitting stages.

---

## 1. Physical enstrophy identity

Let

\[
E_\omega(t):=\|\omega(t)\|_2^2,
\qquad
Q_\omega(t):=\|\nabla\omega(t)\|_2^2,
\]

and

\[
M(t)=\|\omega(t)\|_\infty
\]

on record-growth portions of the first-hitting construction.

The exact enstrophy identity is

\[
\boxed{
\frac12E_\omega'
+\nu Q_\omega
=\mathcal P
:=\int \omega^TS\omega\,dx.
}
\]

---

## 2. Sharp trace-free production coefficient

For every symmetric trace-free `3 x 3` strain matrix,

\[
\lambda_{max}(S)
\le\sqrt{\frac23}|S|.
\]

Using

\[
|\omega|^2\le M|\omega|,
\qquad
\|S\|_2^2=\frac12\|\omega\|_2^2,
\]

gives

\[
\boxed{
\mathcal P
\le
\frac1{\sqrt3}M E_\omega.
}
\]

Hence

\[
\frac12E_\omega'
+\nu Q_\omega
\le
\frac1{\sqrt3}ME_\omega.
\]

---

## 3. Stage-wide vorticity tightness gives pointwise viscous competition

On the dynamically normalized candidate assume, throughout each retained stage,

\[
\int_{B_{R_Z}}|\Omega|^2
\ge
(1-\varepsilon_Z)Z.
\]

The optimized Dirichlet cutoff lemma gives

\[
\frac{Q_{dyn}}{Z_{dyn}}
\ge
\lambda_{tight}
:=
\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2},
\]

where

\[
\boxed{
\Lambda_{tight}(\varepsilon_Z)
=
[\sqrt\pi(1-\varepsilon_Z)^{1/4}-\varepsilon_Z^{1/4}]^4.
}
\]

Scaling back to physical variables,

\[
\boxed{
\frac{Q_\omega}{E_\omega}
\ge
\lambda_{tight}M(t).
}
\]

Therefore

\[
\frac12E_\omega'
\le
\left(
\frac1{\sqrt3}-\nu\lambda_{tight}
\right)M E_\omega.
\]

Wherever `E_omega>0`,

\[
\boxed{
\frac d{dt}\log E_\omega
\le
2c_{tight}M(t),
}
\]

with

\[
\boxed{
c_{tight}
:=
\frac1{\sqrt3}-\nu\lambda_{tight}.
}
\]

If `c_tight<=0`, forward physical enstrophy cannot supply the geometric first-hitting scale growth and the persistent tight corridor is already impossible. The remaining calculation treats `c_tight>0`.

---

## 4. Integrate one original smooth first-hitting stage

Let the geometric first-hitting thresholds be

\[
M_{j+1}=qM_j,
\qquad q>1,
\]

and let the dynamically normalized stage length be

\[
\boxed{
L_j
:=
\int_{t_j}^{t_{j+1}}M(t)\,dt.
}
\]

Integrating the preceding inequality gives

\[
\boxed{
\log\frac{E_{\omega,j+1}}{E_{\omega,j}}
\le
2c_{tight}L_j.
}
\]

No ancient rescaling is used.

---

## 5. Endpoint normalized enstrophy forces a half-log scale increment

At a first-hitting endpoint,

\[
E_{\omega,j}
=M_j^{1/2}Z_j,
\]

where `Z_j` is the dynamically normalized enstrophy.

The endpoint Taylor-thick-core estimate gives a uniform lower bound

\[
\boxed{Z_j\ge Z_->0,}
\]

while stage-wide vorticity tightness and `||Omega||_infinity<=1` give

\[
\boxed{
Z_j\le Z_+
=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Therefore

\[
\begin{aligned}
\log\frac{E_{\omega,j+1}}{E_{\omega,j}}
&=
\frac12\log q
+
\log\frac{Z_{j+1}}{Z_j}.
\end{aligned}
\]

So every stage satisfies

\[
\boxed{
\frac12\log q
+
\log\frac{Z_{j+1}}{Z_j}
\le
2c_{tight}L_j.
}
\]

The normalized endpoint factor may fluctuate, but it cannot drift geometrically because it remains between `Z_-` and `Z_+`.

---

## 6. Telescope many finite smooth stages

Sum from `j=j_0` to `j_0+N-1`:

\[
\boxed{
\frac N2\log q
+
\log\frac{Z_{j_0+N}}{Z_{j_0}}
\le
2c_{tight}
\sum_{j=j_0}^{j_0+N-1}L_j.
}
\]

Using

\[
Z_-/Z_+
\le
Z_{j_0+N}/Z_{j_0}
\le
Z_+/Z_-,
\]

we obtain

\[
\frac N2\log q
-
\log\frac{Z_+}{Z_-}
\le
2c_{tight}
\sum_jL_j.
\]

Suppose the existing moving-variance/low-turnover corridor gives the stage ceiling

\[
L_j\le L_{stage,+}.
\]

Then

\[
\boxed{
\frac N2\log q
-
\log\frac{Z_+}{Z_-}
\le
2c_{tight}NL_{stage,+}.
}
\]

Divide by `N` and let `N` grow. A necessary condition for an infinite tight first-hitting corridor is

\[
\boxed{
\frac12\log q
\le
2c_{tight}L_{stage,+}.
}
\]

Therefore the corridor is S-closed whenever

\[
\boxed{
2\left(
\frac1{\sqrt3}
-
u\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}
\right)_+
L_{stage,+}
<
\frac12\log q.
}
\]

Equivalently,

\[
\boxed{
4L_{stage,+}
\left(
\frac1{\sqrt3}
-
u\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}
\right)_+
<
\log q.
}
\]

This is the main finite-stage closure certificate.

---

## 7. Why this is stronger than the ancient `K_I` gate

The continuous ancient bound used

\[
K_I
\lesssim
\frac{q^2}{q-1}L_{stage,+}
\]

and then compared a logarithmic enstrophy exponent with `1/2`.

For `q=2`, this inserts roughly a factor `4` in front of `L_stage,+` before the rigidity test.

The finite-stage telescope instead uses the exact geometric scale action

\[
\frac12\log q
\]

directly and pays only the actual stage integral

\[
L_j=\int Mdt.
\]

It therefore avoids the future-stage geometric-sum loss and the extra all-times slab factor.

The ancient route remains useful for branches where finite-stage endpoint bounds are unavailable, but it is no longer the preferred route on the smooth stage-wide tight corridor.

---

## 8. Quarter-tail benchmark

For

\[
\varepsilon_Z=\frac14,
\]

\[
\Lambda_{tight}\approx0.7885770233.
\]

Thus with viscosity normalized to `nu=1` and `q=2`, the certificate is

\[
\boxed{
2\left(
\frac1{\sqrt3}
-rac{0.7885770233}{R_Z^2}
\right)_+
L_{stage,+}
<
\frac12\log2.
}
\]

If the bracket is nonpositive, i.e.

\[
R_Z\lesssim1.16869819,
\]

the tight corridor is closed independently of stage length.

For larger `R_Z`, the allowed stage length is explicitly

\[
\boxed{
L_{stage,+}
<
\frac{\log2}
{4(1/\sqrt3-0.7885770233/R_Z^2)}.
}
\]

---

## 9. Common-radius benchmark only

As a **benchmark, not a theorem identification**, suppose the vorticity-tightness radius and the moving-variance radius are represented by the same normalized number `R`, and use the existing pure-ball estimate

\[
L_{stage,+}
\le
0.7483880874R^2
\]

for the `q=2` low-turnover corridor.

Then the equality in the new finite-stage certificate occurs at approximately

\[
\boxed{R\approx1.32925.}
\]

This is numerically beyond the previously quoted pure projective benchmark near `1.303`, but the two radii arise from different definitions and must not be identified without an additional comparison lemma.

The meaningful result is the certificate itself, not this common-radius numerical substitution.

---

## 10. Anti-proof discipline

This closure uses only standard smooth Navier-Stokes identities and explicit inequalities once the stage-wide tightness and stage-length hypotheses are stated.

It does **not** prove that every candidate has a fixed universal `R_Z`, nor does it classify vorticity non-tightness as turnover by definition.

Thus the corrected global split remains

\[
\boxed{
\text{singular candidate}
\Longrightarrow
\text{stage-wide vorticity-tight corridor}
\lor
\text{vorticity non-tight/escape corridor}.
}
\]

The present note substantially strengthens and may close the first branch for a much wider parameter region. The second remains an independent anti-proof target.

Status: **ON A SMOOTH STAGE-WIDE VORTICITY-TIGHT LOW-TURNOVER CORRIDOR, PHYSICAL ENSTROPHY GROWTH TELESCOPES DIRECTLY AGAINST THE GEOMETRIC FIRST-HITTING FACTOR. THE RESULTING S-LEVEL CERTIFICATE BYPASSES `K_I`, ANCIENT COMPACTNESS, RECURRENT LERAY DYNAMICS, AND THE LOW-FREQUENCY VELOCITY TAIL. GLOBAL REGULARITY REMAINS UNPROVED.**