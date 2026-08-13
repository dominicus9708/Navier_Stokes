# Time-dependent fixed-axis biaxial strain: bounded affine rate still forces the compression-diffusion barrier

Date: 2026-08-13

Status: **DERIVED LINEAR TIME-DEPENDENT AFFINE LEMMA / FOUR ESCAPE CHANNELS IDENTIFIED**.

The constant-strain benchmark extends directly to a time-dependent biaxial rate as long as the compressive/extensional eigendirections remain fixed and the positive affine rate is bounded.

This removes constancy of the strain magnitude as the main weakness of the benchmark.

---

## 1. Model

Let

\[
S(t)=a(t)\operatorname{diag}(-2,1,1),
\qquad
0\le a(t)\le M.
\]

For an extensional-plane vorticity component `w`, consider

\[
\boxed{
\partial_t w
+(-2a(t)x_1,a(t)x_2,a(t)x_3)\cdot\nabla w
=a(t)w+\nu\Delta w.
}
\]

Define accumulated affine strain

\[
\boxed{
A(t)=\int_0^t a(s)ds.
}
\]

The nominal inviscid amplification at time `T` is

\[
\boxed{q=e^{A(T)}.}
\]

---

## 2. Exact time-dependent affine coordinates

Set

\[
y_1=e^{2A(t)}x_1,
\qquad
y_2=e^{-A(t)}x_2,
\qquad
y_3=e^{-A(t)}x_3,
\]

and

\[
w=e^{A(t)}v.
\]

Then exactly

\[
\boxed{
\partial_t v
=\nu\left[
 e^{4A(t)}\partial_{y_1}^2v
+e^{-2A(t)}(\partial_{y_2}^2+\partial_{y_3}^2)v
\right].
}
\]

The accumulated normal heat time is

\[
\boxed{
\tau_1(T)=\int_0^T e^{4A(s)}ds.
}
\]

---

## 3. Lower bound the normal heat time from the affine-rate cap

Since

\[
A'(s)=a(s)\le M,
\]

for every `s<=T`,

\[
A(s)
\ge A(T)-M(T-s)
\]

as long as the right-hand side is traced backward from the final value.

Because reaching `A(T)=log q` from `A(0)=0` requires

\[
T\ge\frac{\log q}{M},
\]

the final interval of length `log(q)/M` exists.

On that interval,

\[
A(s)\ge\log q-M(T-s).
\]

Hence

\[
\begin{aligned}
\tau_1(T)
&\ge
\int_{T-\log(q)/M}^T
q^4e^{-4M(T-s)}ds\\
&=
\frac{q^4-1}{4M}.
\end{aligned}
\]

Therefore

\[
\boxed{
\tau_1(T)
\ge
\frac{q^4-1}{4M}.
}
\]

---

## 4. Mixed-norm heat estimate

The same one-dimensional normal heat estimate gives

\[
\|v(T)\|_\infty
\le
C(\nu\tau_1(T))^{-1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}.
\]

Multiplying by the affine stretch `q`,

\[
\boxed{
\|w(T)\|_\infty
\le
Cq
\left[
\frac{\nu(q^4-1)}{4M}
\right]^{-1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}.
}
\]

As `q->infinity`,

\[
q(q^4-1)^{-1/4}\to1.
\]

Hence

\[
\boxed{
\|w(T)\|_\infty
\lesssim
\left(\frac M\nu\right)^{1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}
}
\]

uniformly in the target affine amplification factor.

---

## 5. Four escape channels for the nonlinear problem

A full Navier--Stokes first-hitting window can evade the linear fixed-axis barrier only if at least one of the benchmark hypotheses fails quantitatively.

The natural typed escapes are:

### A. Affine-rate concentration

The local biaxial rate is not uniformly bounded:

\[
\boxed{\sup a(t)\to\infty.}
\]

Under the optimal local affine representative this returns to local normalized strain-energy concentration.

### B. Eigenspace rotation

The compressive normal / extensional plane rotates fast enough that no fixed-axis accumulated heat-time argument applies.

### C. Residual nonlinear forcing

The mean-free/local residual strain, pressure-compatible transport, or viscous Cauchy rewrite contributes at the same order as the affine model and invalidates perturbative transfer.

### D. Long precursor reservoir

The earlier vorticity has sufficiently large

\[
L^\infty_{x_\perp}L^2_{x_1}
\]

mass along the compressive normal to pay for the desired final amplification despite heat smoothing.

Thus

\[
\boxed{
\text{biaxial amplification}
\Longrightarrow
A\ \text{or}\ B\ \text{or}\ C\ \text{or}\ D.
}
\]

for any future perturbative theorem that quantitatively approximates this model.

---

## 6. Why channel A is already largely typed

The optimal local affine representative satisfies an exact weighted strain-energy lower bound in terms of its condition number.  Therefore a diverging affine-rate/affine-deformation branch is not hidden complexity; it is visible as a local normalized coherent-strain concentration.

This leaves `B/C/D` as the genuinely new biaxial escapes.

---

## 7. Next target: rotating-axis perturbation

The compressive eigenvector is separated from the twofold extensional eigenvalue by a gap `3a` in the ideal Betchov shape.  Therefore its spectral projector is stable under small strain perturbations.

A promising next quantity is the compressive-axis projector

\[
P_-(t)=e_-(t)\otimes e_-(t)
\]

and its temporal variation.

One seeks a dichotomy

\[
\boxed{
\int|\dot P_-|dt\ \text{small}
\Longrightarrow
\text{fixed-axis compression-diffusion survives perturbatively},
}
\]

or

\[
\boxed{
\int|\dot P_-|dt\ \text{large}
\Longrightarrow
\text{eigenframe-rotation cost / residual channel}.
}
\]

No such full nonlinear estimate is yet proved here.

Status: **TIME-DEPENDENT RATE CLOSED / ROTATING AXIS, RESIDUAL FORCING, OR LONG PRECURSOR ARE THE REMAINING BIAXIAL ESCAPES**.
