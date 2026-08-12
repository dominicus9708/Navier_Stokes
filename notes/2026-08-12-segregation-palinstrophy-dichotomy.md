# Vorticity segregation -> critical palinstrophy or dense-core dichotomy

Date: 2026-08-12

Status: **DERIVED GEOMETRIC/POINCARE DICHOTOMY + HIGHER-DERIVATIVE BRIDGE / OPEN DYNAMIC EXCLUSION**.

This note quantifies one consequence of spatially segregating dangerous channels around an intense-vorticity core.

## 1. Normalize vorticity magnitude

Fix a time and a ball

\[
B=B_r(x_0).
\]

Let

\[
W=\|\omega\|_\infty>0,
\qquad
f=\frac{|\omega|}{W}\in[0,1].
\]

Choose thresholds

\[
0<b<a<1.
\]

Define

\[
V_a=\{x\in B:f(x)\ge a\},
\]

and

\[
L_b=\{x\in B:f(x)\le b\}.
\]

Let their volume fractions be

\[
\alpha=\frac{|V_a|}{|B|},
\qquad
\beta=\frac{|L_b|}{|B|}.
\]

## 2. Exact variance lower bound from two separated levels

For every

\[
x\in V_a,
\qquad
y\in L_b,
\]

we have

\[
|f(x)-f(y)|\ge a-b.
\]

The pairwise identity for variance is

\[
\fint_B|f-f_B|^2dx
=
\frac12
\fint_B\fint_B
|f(x)-f(y)|^2dxdy.
\]

Restricting the double integral to

\[
V_a\times L_b
\quad\text{and}\quad
L_b\times V_a
\]

gives

\[
\boxed{
\fint_B|f-f_B|^2dx
\ge
\alpha\beta(a-b)^2.
}
\]

## 3. Poincare converts separation into a gradient cost

The ball Poincare inequality gives

\[
\fint_B|f-f_B|^2dx
\le
C_P r^2
\fint_B|\nabla f|^2dx.
\]

Since `W` is spatially constant at the fixed time,

\[
\nabla f
=\frac{\nabla|\omega|}{W}.
\]

Therefore

\[
\boxed{
\frac{r^2}{W^2}
\fint_B|\nabla|\omega||^2dx
\ge
C_P^{-1}
\alpha\beta(a-b)^2.
}
\]

The left-hand side is scale invariant under Navier--Stokes scaling.

## 4. Full vorticity-gradient decomposition

Where `omega != 0`, write

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|.
\]

Since

\[
\xi\cdot\partial_j\xi=0,
\]

we have the exact pointwise identity

\[
\boxed{
|\nabla\omega|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Hence define the critical local palinstrophy channel

\[
\boxed{
\mathcal P_r
=
\frac{r^2}{W^2}
\fint_B|\nabla\omega|^2dx.
}
\]

Then automatically

\[
\boxed{
\mathcal P_r
\ge
C_P^{-1}
\alpha\beta(a-b)^2.
}
\]

Thus coexistence of a substantial high-vorticity region and a substantial genuinely low-vorticity region forces a non-small second-derivative-of-velocity channel.

## 5. Natural vorticity scale

Take

\[
r=cW^{-1/2}
\]

with fixed `c>0`.

The critical local enstrophy channel is

\[
\mathcal W_r
=r\int_B|\omega|^2dx.
\]

Since `|omega|>=aW` on `V_a`,

\[
\mathcal W_r
\ge
r a^2W^2\alpha|B|
=
\boxed{
\frac{4\pi}{3}
a^2\alpha c^4.
}
\]

Thus the already-derived non-sparse intense-vorticity occupancy condition directly produces a fixed positive lower bound on the critical local enstrophy at the natural scale.

## 6. Low-vorticity fraction dichotomy

Fix a threshold `beta_0 in (0,1)`.

### Branch P: a substantial low-vorticity region exists

If

\[
\beta\ge\beta_0,
\]

and residual non-sparseness gives a lower bound `alpha>=alpha_0>0`, then

\[
\boxed{
\mathcal P_r
\ge
C_P^{-1}
\alpha_0\beta_0(a-b)^2.
}
\]

A definite critical palinstrophy cost is unavoidable.

### Branch D: the low-vorticity region is small

If

\[
\beta<\beta_0,
\]

then

\[
|\{f>b\}|>(1-\beta_0)|B|,
\]

and therefore

\[
\boxed{
\mathcal W_r
\ge
\frac{4\pi}{3}
b^2(1-\beta_0)c^4.
}
\]

The ball is then densely filled by vorticity of order `W` even at the lower threshold `bW`.

Hence a residual core must choose between

\[
\boxed{
\text{critical palinstrophy}
\quad\text{or}\quad
\text{very dense critical enstrophy occupancy}.
}
\]

## 7. Connection to direction-defect segregation

The channel-overlap note showed that to reduce the direction-gradient penalty in the intense core, a residual flow may attempt to place most of the `|grad xi|^2` channel in a lower-vorticity region.

The present note shows that if this lower-vorticity region has substantial volume while a non-sparse intense core remains, the magnitude transition itself forces `mathcal P_r` to be non-small.

If the lower-vorticity region has very small volume, the vorticity core becomes even denser instead.

Thus the informal escape

\[
\text{move direction defects away from large }|\omega|
\]

does not remove structure; it moves the residual burden into either

- critical vorticity-gradient/palinstrophy, or
- extreme vorticity occupancy.

## 8. Higher-derivative bridge

Since

\[
\omega=\nabla\times u,
\]

the palinstrophy channel contains second spatial derivatives of velocity.

It therefore belongs naturally to the `k>=2` sector of the higher-derivative DSD block and to the external higher-derivative sparseness framework.

The remaining task is not to show that `mathcal P_r` is non-small, but to prove that **persistent non-small palinstrophy at the residual natural scales must enter a known higher-derivative regularity/sparseness class or incur a non-summable dynamic cost**.

No such theorem is established here.

## 9. Revised segregation target

A useful next implication would be

\[
\boxed{
G_{\rm sparse}^c
\cap
G_{\rm logdir}^c
\Longrightarrow
\text{palinstrophy-critical branch}
\cup
\text{ultra-dense vorticity branch},
}
\]

followed by exclusion of each branch using higher-derivative or time-window estimates.

The static geometric dichotomy above supplies the first arrow only under the stated occupancy thresholds.

Status: **OPEN DYNAMIC PALINSTROPHY / DENSE-CORE EXCLUSION**.
