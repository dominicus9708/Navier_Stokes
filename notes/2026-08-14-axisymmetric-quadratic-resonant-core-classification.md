# Axisymmetric quadratic resonant core classification

Date: 2026-08-14

Status: **EXACT FINITE-DIMENSIONAL CLASSIFICATION AND GAUSSIAN COERCIVITY FOR THE SO(2)-RESONANT QUADRATIC CORE. EVEN THE EXACT FAST-ROTATION RESONANT LOW-HERMITE SECTOR CANNOT PRODUCE MATERIAL-CENTER MEAN VORTICITY WITHOUT COMPARABLE SECOND CHAOS. GLOBAL REGULARITY NOT PROVED.**

## 1. Resonant symmetry class

Fix the coherent mean-vorticity / rotation axis

\[
e=e_3.
\]

Consider homogeneous quadratic vector fields

\[
Q:\mathbb R^3\to\mathbb R^3
\]

that are equivariant under every rotation `R_theta` around `e3`:

\[
Q(R_\theta x)=R_\theta Q(x).
\]

The horizontal output transforms in the standard two-dimensional representation, while the vertical output is rotationally scalar.

The most general homogeneous quadratic equivariant field is therefore

\[
\boxed{
\begin{aligned}
Q_1&=\alpha zx-\beta zy,\\
Q_2&=\alpha zy+\beta zx,\\
Q_3&=\chi(x^2+y^2)+d z^2.
\end{aligned}
}
\]

Incompressibility gives

\[
\nabla\cdot Q=2(\alpha+d)z=0,
\]

hence

\[
\boxed{d=-\alpha.}
\]

Thus the entire divergence-free resonant quadratic sector is three-dimensional:

\[
\boxed{
Q_{\alpha,\beta,\chi}
=
(\alpha zx-\beta zy,
\alpha zy+\beta zx,
\chi(x^2+y^2)-\alpha z^2).
}
\]

Here `beta` is the quadratic swirl coefficient and `alpha,chi` describe meridional strain/flow.

## 2. Linear vorticity and strain

The residual vorticity is

\[
\eta=\nabla\times Q=Az,
\]

with coefficient matrix

\[
\boxed{
A=
\begin{pmatrix}
-\beta&-\alpha+2\chi&0\\
\alpha-2\chi&-\beta&0\\
0&0&2\beta
\end{pmatrix}.
}
\]

The strain is

\[
S=
\begin{pmatrix}
\alpha z&0&(\alpha+2\chi)x/2-\beta y/2\\
0&\alpha z&(\alpha+2\chi)y/2+\beta x/2\\
(\alpha+2\chi)x/2-\beta y/2&(\alpha+2\chi)y/2+\beta x/2&-2\alpha z
\end{pmatrix}.
\]

Both are first Gaussian chaos.

For the standard Gaussian,

\[
\boxed{
V_\omega
=2(\alpha^2-4\alpha\chi+3\beta^2+4\chi^2),
}
\]

\[
\boxed{
V_S
=7\alpha^2+4\alpha\chi+\beta^2+4\chi^2,
}
\]

and hence

\[
\boxed{
B=V_S+\frac12V_\omega
=4(2\alpha^2+\beta^2+2\chi^2).
}
\]

## 3. Material-center source

In the material/Taylor gauge the residual velocity is `Q` itself. The quadratic residual vorticity source is

\[
P=(\eta\cdot\nabla)Q-AQ.
\]

Its Gaussian mean is

\[
\boxed{
E_\gamma P
=(0,0,-2\beta(\alpha+4\chi)).
}
\]

Therefore

\[
\boxed{
J_{\rm res}\ne0
\quad\Longrightarrow\quad
\beta\ne0
\quad\text{and}\quad
\alpha+4\chi\ne0.
}
\]

A purely meridional quadratic resonant core cannot generate mean axial vorticity. A nonzero resonant mean source requires swirl interacting with meridional strain.

This is the local polynomial form of the fact that rapid-rotation resonance alone is not enough; the source requires a genuine swirl/strain coupling.

## 4. Exact second-chaos output

Let

\[
N_2=P-E_\gamma P
\]

be the centered degree-two vorticity source. Direct Gaussian moment calculation gives

\[
\boxed{
\|N_2\|_{L^2(\gamma)}^2
=
8\beta^2
(2\alpha^2+\beta^2+8\chi^2).
}
\]

Thus every nonzero resonant mean source is accompanied by nonzero second chaos.

Moreover,

\[
|J_{\rm res}|^2
=4\beta^2(\alpha+4\chi)^2.
\]

Using

\[
(\alpha+4\chi)^2
\le
5(\alpha^2+4\chi^2)
\]

and

\[
2\alpha^2+8\chi^2
=2(\alpha^2+4\chi^2),
\]

we obtain

\[
\begin{aligned}
|J_{\rm res}|^2
&\le20\beta^2(\alpha^2+4\chi^2)\\
&\le\frac54
\,8\beta^2(2\alpha^2+\beta^2+8\chi^2).
\end{aligned}
\]

Therefore

\[
\boxed{
|J_{\rm res}|
\le
\frac{\sqrt5}{2}
\|N_2\|_{L^2(\gamma)}.
}
\]

This is a sharper constant than the general trace bound

\[
|E_\gamma P|
\le\sqrt{3/2}\,\|N_2\|_2
\]

on this exact resonant subspace.

## 5. Consequence for the rapid-rotation endgame

The low-Hermite fast-rotation survivor had one apparent remaining possibility: concentrate on the exact resonant subspace so that oscillatory averaging gives no gain.

The present classification shows that this does not reopen a mean-only lane.

On the exact quadratic resonant sector,

\[
\boxed{
\text{resonant material-center mean source}
\Rightarrow
\text{comparable second-chaos source}.
}
\]

But the full-terminal degree-two trace telescoping estimate already gives

\[
\left|\int J_{\rm tr}dt\right|
\lesssim
\sqrt m(1+|\log m|)
\to0
\]

on the bounded-condition bounded-affine branch.

Thus exact SO(2) resonance does not rescue the bounded-affine low-Hermite quadratic core.

## 6. Relation to the translation-gauge correction

In the Gaussian-mean center the quadratic core is `Q-b0`, where

\[
b_0=E_\gamma Q=(0,0,2\chi-\alpha).
\]

That frame produces the additional constant-shift term `A b0`.

The material/Taylor center removes it exactly. The source calculated in this note is therefore the physically relevant non-translation source.

Hence the complete low-Hermite resonant ledger is:

1. translation `Ab0`: gauge/import, removed by material centering;
2. material mean source `E P`: forces second chaos;
3. second-chaos action: globally terminal-telescoping and `o(1)` on the bounded-affine low-Hermite branch.

Status: **EXACT RAPID-ROTATION QUADRATIC RESONANCE DOES NOT REOPEN THE CLOSED LOW-HERMITE LANE / ANY NONZERO RESONANT MATERIAL MEAN SOURCE REQUIRES SWIRL AND COMPARABLE SECOND CHAOS / GLOBAL REGULARITY NOT PROVED.**
