# DSD M17-216 — Director condition number is controlled by material-flow distortion and accumulated strain spectral gap

Date: 2026-09-06  
Canonical ID: **M17-216**

Status: **MATERIAL-DISTORTION / ANCESTRY REDUCTION. ON ANY FINITE REGULAR RANK-2 MATERIAL INTERVAL, MATERIAL FROZENNESS `D_B xi=0` GIVES THE EXACT PULLBACK LAW `grad xi(theta)=grad xi(theta_0) F(theta,theta_0)^{-1}`, WHERE `F=D_a Phi` IS THE DEFORMATION GRADIENT OF THE `B`-FLOW. CONSEQUENTLY THE POSITIVE SINGULAR-VALUE CONDITION NUMBER SATISFIES `cond_+(grad xi(theta)) <= cond_+(grad xi(theta_0)) cond(F)`, AND THE REVERSE INEQUALITY HOLDS AFTER INTERCHANGING THE ENDPOINTS. THE FLOW CONDITION NUMBER IS CHARGED ONLY BY THE STRAIN SPECTRAL GAP, `log cond(F) <= int [lambda_max(Sigma)-lambda_min(Sigma)] dtheta`, BECAUSE THE SIMILARITY DILATION `+I/2` CANCELS EXACTLY. THEREFORE A DIVERGENT DIRECTOR CONDITION NUMBER WITH A UNIFORMLY BOUNDED MATERIAL ANCESTOR CONDITION NUMBER FORCES DIVERGENT ACCUMULATED STRAIN ANISOTROPY. THE M17-215 PRECHARGED-IMPORT EXIT IS NOT A FREE TERMINAL MECHANISM: IT MUST TRACE BACK TO AN ANCESTOR ANISOTROPY/RANK-INTERFACE EXIT OR TO HISTORICAL STRAIN-GAP ACCUMULATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material flow map

Let `Phi(theta,theta_0,a)` be the flow of

\[
B=U+\frac12 y,
\]

so that

\[
\frac{d}{d\theta}\Phi(\theta,\theta_0,a)
=B(\Phi(\theta,\theta_0,a),\theta),
\qquad
\Phi(\theta_0,\theta_0,a)=a.
\]

On a finite regular interval define the deformation gradient

\[
\boxed{F(\theta,\theta_0,a):=D_a\Phi(\theta,\theta_0,a).}
\]

It satisfies

\[
\boxed{
\frac{dF}{d\theta}=(\nabla B)F,
\qquad
F(\theta_0)=I.
}
\]

Regularity of the flow makes `F` invertible on the interval.

---

## 2. Exact pullback law for the director derivative

CE-H material frozenness is

\[
\boxed{D_B\xi=0.}
\]

Hence along the material flow

\[
\boxed{
\xi(\Phi(\theta,\theta_0,a),\theta)=\xi(a,\theta_0).
}
\]

Differentiate with respect to the material coordinate `a`:

\[
(\nabla_x\xi)(\Phi(\theta),\theta)F(\theta)
=\nabla_a\xi(a,\theta_0).
\]

Therefore, writing

\[
A(\theta):=\nabla\xi(\Phi(\theta),\theta),
\qquad
A_0:=\nabla\xi(a,\theta_0),
\]

we obtain the exact identity

\[
\boxed{
A(\theta)=A_0F(\theta)^{-1}.
}
\]

This is the integrated form of M17-215's local law

\[
D_BA=-A\nabla B.
\]

---

## 3. Positive singular-value condition number

On a Rank-2 interval let

\[
s_1(A)\ge s_2(A)>0
\]

be the two positive singular values of `A` and define

\[
\boxed{
\operatorname{cond}_+(A):=\frac{s_1(A)}{s_2(A)}.
}
\]

For any invertible matrix `G`, standard singular-value inequalities give

\[
s_1(AG)\le s_1(A)s_1(G),
\]

and, for the second positive singular value of a Rank-2 `A`,

\[
s_2(AG)\ge s_2(A)s_{min}(G).
\]

Therefore

\[
\boxed{
\operatorname{cond}_+(AG)
\le
\operatorname{cond}_+(A)\operatorname{cond}(G).
}
\]

Apply this with `G=F^{-1}`. Since

\[
\operatorname{cond}(F^{-1})=\operatorname{cond}(F),
\]

we get

\[
\boxed{
\operatorname{cond}_+(A(\theta))
\le
\operatorname{cond}_+(A_0)\operatorname{cond}(F(\theta)).
}
\]

Using the inverse material map gives the reverse endpoint inequality

\[
\boxed{
\operatorname{cond}_+(A_0)
\le
\operatorname{cond}_+(A(\theta))\operatorname{cond}(F(\theta)).
}
\]

Thus

\[
\boxed{
\left|
\log\frac{\operatorname{cond}_+(A(\theta))}
{\operatorname{cond}_+(A_0)}
\right|
\le
\log\operatorname{cond}(F(\theta)).
}
\]

No simplicity of `s_1^2,s_2^2` is required.

---

## 4. Flow condition number is charged by the strain spectral gap

Let

\[
S_B:=\operatorname{sym}(\nabla B).
\]

If `q(theta)=F(theta)q_0`, then

\[
\frac{d}{d\theta}|q|^2
=2q^TS_Bq.
\]

Hence the maximal and minimal singular stretches satisfy the standard differential bounds

\[
\frac{d}{d\theta}\log s_{max}(F)
\le\lambda_{max}(S_B),
\]

\[
\frac{d}{d\theta}\log s_{min}(F)
\ge\lambda_{min}(S_B).
\]

Subtracting,

\[
\boxed{
\frac{d}{d\theta}\log\operatorname{cond}(F)
\le
\lambda_{max}(S_B)-\lambda_{min}(S_B)
}
\]

in the upper-Dini-derivative sense at multiplicity crossings.

Now

\[
S_B=\Sigma+\frac12I.
\]

The scalar similarity shift changes every eigenvalue by `1/2`, so the spectral gap is unchanged:

\[
\boxed{
\lambda_{max}(S_B)-\lambda_{min}(S_B)
=\lambda_{max}(\Sigma)-\lambda_{min}(\Sigma).
}
\]

Define

\[
\boxed{
\Gamma_\Sigma
:=\lambda_{max}(\Sigma)-\lambda_{min}(\Sigma)\ge0.
}
\]

Integration gives

\[
\boxed{
\log\operatorname{cond}(F(\theta,\theta_0))
\le
\int_{\theta_0}^{\theta}\Gamma_\Sigma(\tau)\,d\tau.
}
\]

---

## 5. Global finite-interval anisotropy inequality

Combining Sections 3 and 4 yields

\[
\boxed{
\left|
\log\frac{\operatorname{cond}_+(\nabla\xi)(\theta)}
{\operatorname{cond}_+(\nabla\xi)(\theta_0)}
\right|
\le
\int_{\theta_0}^{\theta}
\Gamma_\Sigma(\tau)\,d\tau.
}
\]

Since

\[
\Gamma_\Sigma\le2\|\Sigma\|_{op},
\]

this recovers M17-215's bound but is sharper and does not require tracking simple singular directions.

For a quiet fixed-lag corridor satisfying

\[
\int_{\theta_0}^{\theta_1}\Gamma_\Sigma d\theta=o(1),
\]

we obtain

\[
\boxed{
\frac{\operatorname{cond}_+(\nabla\xi)(\theta_1)}
{\operatorname{cond}_+(\nabla\xi)(\theta_0)}
=1+o(1).
}
\]

Thus the M17-215 quiet-corridor conclusion is now a direct finite-distortion theorem rather than a simple-eigenvalue calculation.

---

## 6. Ancestry reduction of precharged anisotropy

Suppose a sequence of current Rank-2 material carriers satisfies

\[
\operatorname{cond}_+(\nabla\xi)(\theta_n)\to\infty.
\]

Fix an earlier anchor time `theta_*` while each carrier remains in the same regular Rank-2 material stratum.

If the ancestor condition numbers are uniformly bounded,

\[
\boxed{
\operatorname{cond}_+(\nabla\xi)(\theta_*)\le K_*<\infty,
}
\]

then Section 5 forces

\[
\boxed{
\int_{\theta_*}^{\theta_n}
\Gamma_\Sigma(\tau)\,d\tau
\to\infty.
}
\]

Therefore a divergent current condition number cannot be imported for free from bounded-anisotropy ancestors.

The exact branch reduction is

\[
\boxed{
G_{precharged\ anisotropy/import}
\Longrightarrow
G_{ancestor\ anisotropy/rank\ interface}
\lor
H_{historical\ strain\ spectral\ gap}.
}
\]

The first branch includes failure of a uniform positive second singular value, a Rank-2/Rank-1 transition, director-domain loss, or an already unbounded ancestor condition number.

The second branch is a genuine cumulative geometric cost.

---

## 7. Relation to M17-213 through M17-215

M17-213 gave the exact factorization

\[
|\nabla\xi|^2
=2|J_\xi|\mathcal A_\xi,
\]

with large anisotropy equivalent to large positive condition number.

M17-214 removed enstrophy-dominant large `|J_xi|` on the relative-thick compact packet lane, modulo explicit thin/decompactification/carrier-loss exits.

M17-215 showed locally that quiet strain cannot create large anisotropy.

M17-216 strengthens this to the material-flow statement

\[
\boxed{
G_{anisotropy}
\Longrightarrow
G_{ancestor\ anisotropy/rank\ interface}
\lor
H_{accumulated\ strain\ spectral\ gap},
}
\]

whenever the carrier can be traced through a finite regular Rank-2 material interval.

Thus `precharged import` is a provenance label, not an independent terminal payer.

---

## 8. DSD analysis

### 8.1 Object separation

The proof distinguishes three objects:

1. `A=grad xi`: director differential;
2. `F=D_a Phi`: material deformation gradient;
3. `Sigma`: strain anisotropy generating distortion of `F`.

No identification of these objects is made.

### 8.2 Causal chain

The exact dependency chain is

\[
D_B\xi=0
\Longrightarrow
A=A_0F^{-1}
\Longrightarrow
\operatorname{cond}_+(A)/\operatorname{cond}_+(A_0)
\lesssim\operatorname{cond}(F)
\Longrightarrow
\log\operatorname{cond}(F)
\le\int\Gamma_\Sigma.
\]

Hence director anisotropy is a record of material-flow anisotropic deformation, up to inherited ancestor anisotropy.

### 8.3 Resolution boundary

The theorem controls the same material carrier only while the flow is regular and the director differential remains Rank-2.

Crossing a rank/interface/domain boundary is not silently continued; it is exported as an explicit branch.

---

## 9. DSD audit

- **No global regularity claim.** The accumulated spectral-gap integral may diverge; the theorem identifies a necessary payer but does not bound it.
- **No initial uniform-anisotropy assumption is hidden.** If ancestor condition numbers are not uniformly bounded, that remains an explicit ancestor-degeneration branch.
- **No simplicity assumption.** The deformation-gradient proof remains valid through singular-value multiplicity crossings as long as Rank-2 persists.
- **No Eulerian/material conflation.** Fresh Eulerian shell occupancy is controlled only after selecting and tracing its material ancestors.
- **No false rank-loss claim.** Divergent condition number means relative Rank-1 degeneration; literal Rank loss is a separate interface event.
- **Similarity dilation is not a payer.** The `+I/2` contribution cancels from the strain spectral gap exactly.
- **Finite regular interval only.** Infinite-time conclusions require a separate compactness/ancestry extraction and are not assumed here.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
