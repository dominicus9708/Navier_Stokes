# DSD Leray strain-amplitude -> vorticity-gradient bridge

Date: 2026-08-25

Status: **ENDPOINT RIESZ OBSTRUCTION BYPASSED BY NEAR/FAR INTERPOLATION / RECURRENT H1 STRAIN FLOOR CONVERTED TO A POSITIVE VORTICITY-GRADIENT L-INFINITY FLOOR / DERIVATIVE-QUIET RECURRENT SUBCLASS GETS AN EXPLICIT SYMBOLIC EXCLUSION TEST / GLOBAL REGULARITY UNPROVED.**

This note continues `DSD_LERAY_TWO_LEVEL_RECURRENCE_TAX_2026-08-25.md`.

The previous note proved that a nonzero recurrent Leray survivor must have

\[
B_+:=\sup_s\|\Sigma(s)\|_\infty
\ge
B_{rec}
:=
\frac{3\sqrt2}{8}
+
\frac\nu{\sqrt2}c_{\log}.
\]

There is no universal endpoint estimate `||Sigma||_infinity <= C||W||_infinity`. The present calculation instead uses one additional derivative and the global enstrophy ceiling.

## 1. Biot--Savart strain representation

For vorticity `W`, the strain is a Calderon--Zygmund singular integral

\[
\Sigma(x)=\operatorname{p.v.}\int K(z)W(x-z)\,dz,
\]

with

\[
|K(z)|\le C_K|z|^{-3}
\]

and zero angular mean.

Fix any radius `R>0` and split

\[
\Sigma=\Sigma_{<R}+\Sigma_{>R}.
\]

## 2. Near field uses the vorticity gradient

By kernel cancellation,

\[
\Sigma_{<R}(x)
=
\int_{|z|<R}K(z)[W(x-z)-W(x)]\,dz.
\]

Let

\[
G:=\|\nabla W\|_\infty.
\]

Then

\[
|W(x-z)-W(x)|\le G|z|,
\]

so

\[
|\Sigma_{<R}(x)|
\le
C G
\int_0^R r^{-3}r\,r^2dr.
\]

Therefore

\[
\boxed{
\|\Sigma_{<R}\|_\infty
\le C_1RG.
}
\]

Status: **PROVED.**

## 3. Far field uses only enstrophy

By Cauchy--Schwarz,

\[
\begin{aligned}
|\Sigma_{>R}(x)|
&\le
C_K
\left(\int_{|z|>R}|z|^{-6}dz\right)^{1/2}
\|W\|_2\\
&\le
C_2R^{-3/2}\|W\|_2.
\end{aligned}
\]

Hence

\[
\boxed{
\|\Sigma_{>R}\|_\infty
\le
C_2R^{-3/2}Z^{1/2},
\qquad
Z:=\|W\|_2^2.
}
\]

Status: **PROVED.**

## 4. Optimized endpoint-free interpolation

Combine the two estimates:

\[
\boxed{
\|\Sigma\|_\infty
\le
C_1RG
+C_2R^{-3/2}Z^{1/2}.
}
\]

If `G>0`, minimize the right-hand side over `R>0`. The minimizer has scale

\[
R_*
\asymp
\left(\frac{Z^{1/2}}{G}\right)^{2/5}.
\]

Substitution yields a universal kernel-dependent constant `C_I` such that

\[
\boxed{
\|\Sigma\|_\infty
\le
C_I
G^{3/5}Z^{1/5}.
}
\]

Equivalently,

\[
\boxed{
\|\Sigma\|_\infty
\le
C_I
\|\nabla W\|_\infty^{3/5}
\|W\|_2^{2/5}.
}
\]

This has the correct Navier--Stokes scaling and does not invoke an invalid endpoint `L-infinity` Riesz bound.

The case `G=0` is trivial for a finite-enstrophy whole-space vorticity field: a spatially constant `W in L2` is zero, hence `Sigma=0`.

Status: **PROVED.**

## 5. Enstrophy ceiling converts strain amplitude into derivative amplitude

On the bounded-enstrophy recurrent class,

\[
Z(s)\le Z_+.
\]

Therefore at every time

\[
\boxed{
B(s):=\|\Sigma(s)\|_\infty
\le
C_I Z_+^{1/5}G(s)^{3/5}.
}
\]

Solving for `G` gives

\[
\boxed{
G(s)
\ge
C_I^{-5/3}
Z_+^{-1/3}
B(s)^{5/3}
}
\]

whenever `B(s)>0`.

## 6. Recurrent strain tax forces a vorticity-gradient floor

The two-level recurrence note proves

\[
\sup_s B(s)
\ge B_{rec}
=
\frac{3\sqrt2}{8}
+
\frac\nu{\sqrt2}c_{\log}.
\]

Consequently

\[
\boxed{
\sup_s\|\nabla W(s)\|_\infty
\ge
G_{rec}
}
\]

with

\[
\boxed{
G_{rec}
:=
C_I^{-5/3}
Z_+^{-1/3}
\left(
\frac{3\sqrt2}{8}
+
\frac\nu{\sqrt2}c_{\log}
\right)^{5/3}
>0.
}
\]

Thus the H1 recurrence tax cannot be paid by a large nonlocal strain field without simultaneously creating a quantitatively nontrivial vorticity-gradient amplitude somewhere in the recurrent orbit.

Status: **PROVED.**

## 7. Derivative-quiet exclusion template

Suppose a candidate compact recurrent subclass has the independent upper bound

\[
\|\nabla W(s)\|_\infty
\le G_+
\]

for every state in the class.

Then recurrent survival requires

\[
\boxed{
C_I Z_+^{1/5}G_+^{3/5}
\ge
\frac{3\sqrt2}{8}
+
\frac\nu{\sqrt2}c_{\log}.
}
\]

Equivalently the subclass is excluded whenever

\[
\boxed{
G_+
<
C_I^{-5/3}
Z_+^{-1/3}
\left(
\frac{3\sqrt2}{8}
+
\frac\nu{\sqrt2}c_{\log}
\right)^{5/3}.
}
\]

This is a finite symbolic closure criterion involving exactly the normalized enstrophy ceiling, recurrent frequency tax, and first-vorticity-derivative ceiling.

## 8. Relation to the existing H branch

The repository already uses normalized derivative channels to route strong local derivative concentration into `H` or finite derivative descendants.

The new result gives a converse pressure on the recurrent `non-H` lane:

\[
\boxed{
\text{recurrent H1 production}
\Longrightarrow
\text{positive strain amplitude}
\Longrightarrow
\text{positive }\nabla W\text{ amplitude}.
}
\]

Therefore a derivative-quiet recurrent class cannot make its derivative threshold arbitrarily small. It must remain above `G_rec`.

This does not prove that the existing non-H threshold lies below `G_rec`; that numerical/class-dependent comparison remains to be made.

## 9. DSD meaning

The chain contains distinct formed channels:

1. H1 recurrent production tax;
2. strain `L-infinity` amplitude;
3. near-field vorticity-gradient channel;
4. far-field enstrophy channel.

The interpolation shows that the strain channel cannot appear from an untracked endpoint-Riesz operation. It must be supported by a finite combination of derivative amplitude and enstrophy.

This is precisely the kind of hidden bridge DSD auditing is intended to expose.

## 10. Audit verdict

### PROVED

- near/far strain interpolation `||Sigma||_infinity <= C_I ||grad W||_infinity^(3/5) ||W||_2^(2/5)`;
- on `Z<=Z_+`, recurrent H1 strain production forces a positive `||grad W||_infinity` floor;
- a derivative-quiet recurrent subclass has an explicit symbolic exclusion criterion.

### NOT DERIVED

- a numerical universal value of `C_I` for the repository normalization;
- a sufficiently small independent upper bound `G_+` on every non-H survivor;
- LRMG;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
