# DSD Bounded-Z Weak-\(L^3\) Endpoint Exclusion Gate

Date: 2026-08-25

Status: **CONDITIONAL ENDPOINT CLOSURE USING A KNOWN TYPE-I QUANTITATIVE THEOREM / BOUNDED-Z PLUS UNIFORM WEAK-\(L^3\) IS INCOMPATIBLE WITH THE SINGULAR FIRST-HITTING CORRIDOR / REMAINING SURVIVOR MUST ESCALATE ITS WEAK-\(L^3\) NORM OR LEAVE THE CORRIDOR / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The critical flux-loop model shows that a pure \(1/R\) conveyor naturally lives in the scale-invariant Lorentz space \(L^{3,\infty}\).

This note asks whether such a **uniformly weak-critical** conveyor can coexist with the additional bounded normalized-enstrophy structure of the present proof corridor.

The answer is no, provided the weak-\(L^3\) bound holds uniformly on the full near-singular time corridor required by the external Type-I theorem.

## 2. Uniform normalized velocity \(L^\infty\) bound from first hitting and bounded Z

At a first-hitting normalized time,

\[
\|\Omega\|_\infty\le1
\]

(and on an entire stage the same argument gives a fixed q-dependent bound if normalized by the stage base amplitude).

Assume

\[
\|\Omega\|_2^2\le Z_+.
\]

Biot--Savart gives

\[
|U(x)|
\le C
\int\frac{|\Omega(y)|}{|x-y|^2}dy.
\]

Split at radius \(a\):

\[
\int_{|x-y|<a}\frac{|\Omega(y)|}{|x-y|^2}dy
\le C\|\Omega\|_\infty a,
\]

while Cauchy--Schwarz gives

\[
\int_{|x-y|>a}\frac{|\Omega(y)|}{|x-y|^2}dy
\le
C\|\Omega\|_2a^{-1/2}.
\]

Optimizing

\[
a\asymp
\left(
\frac{\|\Omega\|_2}{\|\Omega\|_\infty}
\right)^{2/3}
\]

yields

\[
\boxed{
\|U\|_\infty
\le
C_{BS}\|\Omega\|_\infty^{1/3}
\|\Omega\|_2^{2/3}.
}
\]

Hence on the bounded-Z first-hitting corridor,

\[
\boxed{
\|U\|_\infty\le K_\infty
:=C_{BS}Z_+^{1/3}.
}
\]

The exact numerical Biot--Savart constant is not needed.

## 3. Weak \(L^3\) plus \(L^\infty\) gives only logarithmic local \(L^3^3\) growth

Assume now the endpoint bound

\[
\boxed{
\|U(s)\|_{L^{3,\infty}(\mathbb R^3)}
\le M
}
\]

uniformly on the near-singular corridor.

For any measurable region \(E\) of volume \(V\), the distribution function satisfies

\[
\mu_E(\lambda)
:=|\{x\in E:|U(x)|>\lambda\}|
\le
\min\{V,M^3\lambda^{-3}\}.
\]

Since \(|U|\le K_\infty\), layer cake gives

\[
\int_E|U|^3dx
=3\int_0^{K_\infty}\lambda^2\mu_E(\lambda)d\lambda.
\]

Let

\[
\lambda_0=MV^{-1/3}.
\]

Then, whenever \(\lambda_0<K_\infty\),

\[
\begin{aligned}
\int_E|U|^3dx
&\le
3V\int_0^{\lambda_0}\lambda^2d\lambda
+3M^3\int_{\lambda_0}^{K_\infty}\frac{d\lambda}{\lambda}\\
&=
M^3
+3M^3\log\frac{K_\infty V^{1/3}}{M}.
\end{aligned}
\]

Therefore for a ball \(B_R\),

\[
\boxed{
\|U\|_{L^3(B_R)}^3
\le
C M^3
\left[
1+\log_+\left(\frac{K_\infty R}{M}\right)
\right].
}
\]

In particular,

\[
\boxed{
\|U\|_{L^3(B_R)}
\lesssim_{M,Z_+}
(1+\log R)^{1/3}.
}
\]

This upper bound uses only the weak-critical distribution estimate and the bounded-Z-induced amplitude ceiling.

## 4. External Type-I quantitative lower bound

Barker--Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Communications in Mathematical Physics 385 (2021), prove a quantitative result for a first singular time under a uniform Type-I weak-critical bound

\[
\|u\|_{L_t^\infty L_x^{3,\infty}}\le M_{phys}.
\]

In particular, near a singular point the strong \(L^3\) norm on a ball whose physical radius is slightly larger than the parabolic scale has a lower bound of logarithmic order:

\[
\boxed{
\|u(t)\|_{L^3(B_{\mathcal R(t)})}
\ge
c(M_{phys})
\log\frac1{T^*-t}
}
\]

for an admissible

\[
\mathcal R(t)
=O\big((T^*-t)^{1/2-\delta}\big)
\]

with fixed \(\delta>0\) in the quantitative formulation.

This is an external theorem, not a new derivation in this repository.

## 5. Convert the theorem radius to normalized radius

On the present corridor,

\[
r(t)\asymp\sqrt{T^*-t}
\]

up to fixed \(\nu\) and \(\Theta\) factors.

Therefore the corresponding normalized radius is

\[
R(t)
=\frac{\mathcal R(t)}{r(t)}
\lesssim
(T^*-t)^{-\delta}.
\]

Hence

\[
\boxed{
\log R(t)
\lesssim
\delta\log\frac1{T^*-t}+O(1).
}
\]

The \(L^3\) norm is scale invariant up to the fixed \(\nu\)-normalization used in this repository.

Thus the internal weak-\(L^3\)+bounded-Z upper estimate gives

\[
\|u(t)\|_{L^3(B_{\mathcal R(t)})}
\lesssim
C(M,Z_+)
\left(
\log\frac1{T^*-t}
\right)^{1/3}.
\]

The external singularity lower bound requires

\[
\|u(t)\|_{L^3(B_{\mathcal R(t)})}
\gtrsim
c(M)
\log\frac1{T^*-t}.
\]

For sufficiently late times these are incompatible.

Therefore

\[
\boxed{
\text{bounded normalized enstrophy}
+
\text{uniform full-corridor }L^{3,\infty}
+
\text{first singular time}
\quad\text{is impossible.}
}
\]

Status: **CONDITIONAL CLOSURE, with the condition being the full-corridor weak-\(L^3\) bound needed by the external theorem.**

## 6. Consequence for the permanent conveyor

An ideal fixed-amplitude \(1/R\) pulse train with bounded overlap is uniformly bounded in \(L^{3,\infty}\).

Therefore such a genuinely uniform weak-critical permanent conveyor cannot be the final singular survivor inside the bounded-Z corridor.

Any surviving export branch must instead satisfy at least one of:

\[
\boxed{
\begin{aligned}
&\|U(s)\|_{L^{3,\infty}}\to\infty
\quad\text{along the near-singular corridor},\\
&Z\text{ loses its bounded recurrent corridor},\\
&\text{the tail ceases to be a uniformly critical bounded-overlap conveyor},\\
&\text{or another previously typed H/T complement activates.}
\end{aligned}
}
\]

This sharpens the earlier phrase “critical \(1/R\) tail.”

A singular survivor cannot remain uniformly weak-critical while also retaining the bounded-Z structure.

## 7. Important scope point

A weak-\(L^3\) bound only at the discrete first-hitting times is **not** enough to invoke the Barker--Prange \(L_t^\infty L_x^{3,\infty}\) theorem.

Therefore the next internal task is not to assume endpoint boundedness silently.

It is to prove one of:

1. the quiet passive-export corridor propagates a uniform weak-\(L^3\) bound throughout every late stage; or
2. failure of such propagation forces a typed amplitude/overlap/turnover/H event.

This is now the precise remaining bridge.

## 8. Audit verdict

### PROVED INTERNALLY

- bounded normalized vorticity amplitude and bounded normalized enstrophy imply a uniform normalized velocity \(L^\infty\) bound;
- weak \(L^3\)+\(L^\infty\) implies local strong \(L^3^3\) growth at most logarithmic in radius.

### EXTERNAL THEOREM

- a Type-I weak-\(L^3\) singularity must exhibit a much stronger logarithmic lower growth of the strong \(L^3\) norm on an admissible shrinking physical ball (Barker--Prange 2021).

### CONDITIONAL CLOSURE

- bounded Z + a uniform **full-time-corridor** weak-\(L^3\) bound excludes the singular survivor.

### NEW FRONTIER

\[
\boxed{
\text{prove weak-}L^3\text{ propagation on quiet permanent export}
\quad\text{or route its failure to H/T.}
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
