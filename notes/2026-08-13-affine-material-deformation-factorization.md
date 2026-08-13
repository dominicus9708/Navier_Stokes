# Affine/material deformation factorization: coarse deformation versus residual counter-deformation

Date: 2026-08-13

Status: **EXACT FACTORIZATION + CONDITION-NUMBER LEDGER / CORRECTS OVERIDENTIFICATION OF AFFINE CASCADE WITH THE FULL CAUCHY D-CHANNEL**.

The affine-background compactness route introduces a spatially common matrix `F_aff`, whereas the Cauchy amplification formula uses the **full material deformation gradient**.  These are related but are not identical.  A large coarse affine distortion can be cancelled by a large residual counter-deformation, leaving the full material map well conditioned.

This note records the exact factorization and the correct deformation trichotomy.

---

## 1. Affine plus residual velocity

On a normalized tracked window write

\[
U(y,s)=L(s)y+v(y,s),
\qquad \operatorname{tr}L=0.
\]

Let the common affine deformation solve

\[
\boxed{
F'(s)=L(s)F(s),
\qquad F(s_0)=I.
}
\]

Hence

\[
\det F(s)=1.
\]

Let `X(a,s)` be the **full** material flow and

\[
\boxed{
H(a,s)=D_aX(a,s)
}
\]

its deformation gradient.  Then

\[
H'=[L+\nabla v(X,s)]H,
\qquad H(s_0)=I.
\]

---

## 2. Exact factorization

Define the residual-frame deformation

\[
\boxed{
G(a,s)=F(s)^{-1}H(a,s).
}
\]

Then exactly

\[
\boxed{H=FG.}
\]

Differentiating gives

\[
\begin{aligned}
G'
&=-F^{-1}LF\,G
+F^{-1}[L+\nabla v(X,s)]FG\\
&=F^{-1}\nabla v(X,s)F\,G.
\end{aligned}
\]

Therefore

\[
\boxed{
G'=B_{\rm res}G,
\qquad
B_{\rm res}=F^{-1}\nabla v(X,s)F.
}
\]

Since `det H=det F=1`, also

\[
\boxed{\det G=1.}
\]

Thus the full material deformation is exactly the product of

1. the coarse/common affine deformation `F`, and
2. the residual deformation `G` measured in the affine frame.

---

## 3. Condition-number ledger

For an invertible matrix define the Euclidean condition number

\[
\kappa(M)=\|M\|_{op}\|M^{-1}\|_{op}.
\]

Submultiplicativity gives

\[
\boxed{
\kappa(H)\le \kappa(F)\kappa(G).
}
\]

Using `F=HG^{-1}` and `G=F^{-1}H` gives the two reverse bookkeeping inequalities

\[
\boxed{
\kappa(F)\le\kappa(H)\kappa(G),
}
\]

\[
\boxed{
\kappa(G)\le\kappa(F)\kappa(H).
}
\]

Introduce logarithmic distortion

\[
\boxed{d(M)=\log\kappa(M)\ge0.}
\]

Then

\[
\boxed{
|d(F)-d(G)|\le d(H)\le d(F)+d(G).
}
\]

In particular,

\[
\boxed{
d(F)\to\infty,\quad d(H)\le C
\Longrightarrow
d(G)\to\infty.
}
\]

A coarse affine cascade therefore cannot disappear for free.  If it does not survive as full material deformation, an equally large residual counter-deformation must appear.

---

## 4. Explicit cancellation example

Let

\[
F_M=\operatorname{diag}(M,M^{-1},1),
\qquad M>1,
\]

and choose

\[
G_M=F_M^{-1}.
\]

Then

\[
H_M=F_MG_M=I,
\]

but

\[
\boxed{
\kappa(F_M)=\kappa(G_M)=M^2,
\qquad
\kappa(H_M)=1.
}
\]

Hence the statement

\[
\kappa(F)\to\infty
\Longrightarrow
\kappa(H)\to\infty
\]

is false without controlling the residual factor.  This is the precise reason the affine-cascade branch must not be identified directly with the full Cauchy D-channel.

---

## 5. Residual deformation requires residual strain in the affine frame

For a matrix path

\[
G'=BG,
\qquad G(s_0)=I,
\]

let

\[
S_B=\frac12(B+B^T).
\]

The largest and smallest singular values satisfy, almost everywhere,

\[
\frac{d}{ds}\log\sigma_{\max}(G)
\le \lambda_{\max}(S_B),
\]

\[
\frac{d}{ds}\log\sigma_{\min}(G)
\ge \lambda_{\min}(S_B).
\]

Hence

\[
\boxed{
\log\kappa(G(s))
\le
\int_{s_0}^s
[\lambda_{\max}(S_B)-\lambda_{\min}(S_B)]\,d\tau.
}
\]

Therefore a large residual condition number forces a large accumulated **residual-frame strain spread**:

\[
\boxed{
\int
[\lambda_{\max}(\operatorname{sym}B_{\rm res})
-\lambda_{\min}(\operatorname{sym}B_{\rm res})]ds
\ge \log\kappa(G).
}
\]

This is a geometric deformation cost.  It is not yet an `L2` energetic cost in the original frame because conjugation by a poorly conditioned `F` can amplify matrix norms.

---

## 6. Correct deformation trichotomy

The former affine branch should be replaced by the exact hierarchy

\[
\boxed{
\kappa(F)\text{ large}
\Longrightarrow
\begin{cases}
\kappa(H)\text{ large}, & \text{full material D-channel},\\
\kappa(G)\text{ large}, & \text{residual counter-deformation channel},
\end{cases}
}
\]

where both can of course be large simultaneously.

Thus the current amplification structure is better written as

\[
\boxed{
\text{coarse affine deformation}
\times
\text{residual deformation}
\times
\text{viscous Cauchy rewrite}.
}
\]

The viscous factor is not literally multiplicative, but in the Cauchy representation it is the additive rewrite of the material Cauchy state before multiplication by the full deformation `H=FG`.

---

## 7. Hierarchical Cauchy representation

The full Cauchy variable is

\[
\zeta=H^{-1}\Omega=G^{-1}F^{-1}\Omega.
\]

It obeys

\[
\partial_s\zeta
=\nu H^{-1}\Delta\Omega.
\]

Hence

\[
\boxed{
\Omega(s_1)
=F(s_1)G(s_1)
\left[
\Omega(s_0)
+\nu\int_{s_0}^{s_1}
H^{-1}\Delta\Omega\,ds
\right].
}
\]

This is the exact three-layer bookkeeping identity:

1. coarse affine deformation `F`;
2. residual deformation `G`;
3. viscous rewrite of the Cauchy state.

A large amplification cannot be attributed to a coarse affine matrix alone unless the residual and viscous channels are also audited.

---

## 8. DSD interpretation

The result is naturally resolution-indexed.

At the current resolution, the remote/intermediate field is compressed into the finite-dimensional matrix `F`.  What remains after removing that describable common action is the residual deformation `G`.

If the coarse action is large but the observed full deformation is not, the discrepancy is not lost information: it reappears exactly as large residual counter-deformation.

Thus

\[
\boxed{
\text{coarse deformation}
-\text{observed full deformation}
\Rightarrow
\text{residual deformation requirement}
}
\]

in logarithmic condition-number form.

This is a cleaner adaptive-deformation ledger than treating every scale as an independent escape route.

---

## 9. Remaining open step

The remaining proof-producing target is to convert the residual-frame distortion

\[
\log\kappa(G)
\]

into one of the already controlled physical channels:

- local palinstrophy / `V2`;
- projective roughness;
- local source deficit;
- or full material deformation.

Because `B_res=F^{-1}(grad v)F`, this conversion is easy on bounded-`F` windows but becomes nontrivial exactly when the coarse affine factor is strongly anisotropic.

Status: **EXACT DEFORMATION FACTORIZATION CLOSED / LARGE-COARSE-SMALL-FULL COUNTER-DEFORMATION BRANCH REMAINS TO INTERSECT WITH LOCAL REGULARITY CHANNELS**.
