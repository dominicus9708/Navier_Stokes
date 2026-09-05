# DSD M17-215 — Director anisotropy condition number is charged only by accumulated strain anisotropy

Date: 2026-09-06  
Canonical ID: **M17-215**

Status: **ANISOTROPY MATERIAL LAW / MATERIAL FROZENNESS `D_B xi=0` IMPLIES `D_B grad xi = -(grad xi) grad B`. THE DOMAIN GRAM TENSOR `C=(grad xi)^T grad xi` THEREFORE OBEYS `D_B C = -(grad B)^T C - C grad B`. FOR SIMPLE NONZERO SINGULAR VALUES `s1>=s2>0`, THEIR LOGARITHMIC MATERIAL RATES ARE THE NEGATIVE STRAIN RATES ALONG THE CORRESPONDING RIGHT-SINGULAR DIRECTIONS. THE ISOTROPIC SIMILARITY SHIFT `+I/2` CANCELS EXACTLY IN THE RATIO, SO `D_B log(s1/s2) = -(v1^T Sigma v1 - v2^T Sigma v2)` AND `|D_B log(s1/s2)| <= 2 ||Sigma||op`. THUS LARGE DIRECTOR ANISOTROPY CANNOT BE GENERATED DURING A QUIET LOW-STRAIN PASSAGE; IT MUST BE PRECHARGED ON ENTRY OR PAID BY A NONQUIET STRAIN-ANISOTROPY EPISODE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material derivative of the director gradient

CE-H gives

\[
\boxed{D_B\xi=0.}
\]

Differentiate spatially. For each coordinate derivative,

\[
D_B(\partial_j\xi)
=\partial_j(D_B\xi)-(\partial_jB_\ell)\partial_\ell\xi.
\]

Thus, with the derivative matrix `A=grad xi` written with spatial derivative index in the domain slot,

\[
\boxed{D_BA=-A\nabla B.}
\]

---

## 2. Gram-tensor evolution

Define the positive semidefinite domain Gram tensor

\[
\boxed{C:=A^TA.}
\]

Then

\[
\begin{aligned}
D_BC
&=(D_BA)^TA+A^T(D_BA)\\
&=-(\nabla B)^TA^TA-A^TA\nabla B.
\end{aligned}
\]

Therefore

\[
\boxed{
D_BC
=-(\nabla B)^TC-C\nabla B.
}
\]

The two positive eigenvalues of `C` are

\[
s_1^2,\qquad s_2^2.
\]

---

## 3. Singular-value rate

At a point where the positive eigenvalue `s_i^2` is simple, let `v_i` be its normalized domain eigenvector:

\[
Cv_i=s_i^2v_i.
\]

Then standard symmetric-eigenvalue differentiation gives

\[
D_B(s_i^2)=v_i^T(D_BC)v_i.
\]

Using `Cv_i=s_i^2v_i`,

\[
\begin{aligned}
D_B(s_i^2)
&=-s_i^2v_i^T(\nabla B+\nabla B^T)v_i\\
&=-2s_i^2v_i^T\operatorname{sym}(\nabla B)v_i.
\end{aligned}
\]

Hence

\[
\boxed{
D_B\log s_i
=-v_i^T\operatorname{sym}(\nabla B)v_i.
}
\]

---

## 4. Similarity dilation cancels from anisotropy

Since

\[
B=U+\frac12y,
\]

\[
\operatorname{sym}(\nabla B)
=\Sigma+\frac12I.
\]

Therefore

\[
D_B\log s_i
=-\frac12-v_i^T\Sigma v_i.
\]

Subtract the two positive singular-value rates:

\[
\boxed{
D_B\log\frac{s_1}{s_2}
=-\left(v_1^T\Sigma v_1-v_2^T\Sigma v_2\right).
}
\]

The `-1/2` similarity dilation cancels exactly.

---

## 5. Strain-action bound

For unit vectors,

\[
|v_i^T\Sigma v_i|\le\|\Sigma\|_{op}.
\]

Thus

\[
\boxed{
\left|
D_B\log\frac{s_1}{s_2}
\right|
\le2\|\Sigma\|_{op}.
}
\]

Integrating along a material trajectory from `theta_0` to `theta_1`,

\[
\boxed{
\left|
\log\frac{(s_1/s_2)(\theta_1)}{(s_1/s_2)(\theta_0)}
\right|
\le
2\int_{\theta_0}^{\theta_1}\|\Sigma\|_{op}d\theta.
}
\]

---

## 6. Quiet-corridor consequence

If a material carrier crosses a remote fixed-lag corridor on which

\[
\int\|\Sigma\|_{op}d\theta=o(1),
\]

then

\[
\boxed{
\frac{(s_1/s_2)_{out}}{(s_1/s_2)_{in}}
=1+o(1).
}
\]

Thus a quiet passage cannot create a divergent condition number from a bounded one.

Consequently the M17-213 anisotropic spectral branch has the split

\[
\boxed{
G_{anisotropy}
\Longrightarrow
G_{precharged\ anisotropy/import}
\lor
H_{strain\ burst/nonquiet}.
}
\]

---

## 7. Nonsimple singular values

At a conformal crossing `s1=s2`, the individual singular directions need not be unique.
However the condition number equals one there and is not singular.
The integrated inequality may be obtained by approximation or by standard matrix singular-value Lipschitz estimates.

Thus the hard branch concerns large separated singular values, where simplicity holds automatically after a small perturbation or on open intervals away from crossings.

---

## 8. DSD audit

- The material law controls change of anisotropy along the same carrier; it does not prevent fresh highly anisotropic labels from entering an Eulerian shell.
- No finite total strain-action budget over infinite similarity time is claimed.
- The result identifies the recharge mechanism and routes the quiet branch to precharged import rather than falsely closing it.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
