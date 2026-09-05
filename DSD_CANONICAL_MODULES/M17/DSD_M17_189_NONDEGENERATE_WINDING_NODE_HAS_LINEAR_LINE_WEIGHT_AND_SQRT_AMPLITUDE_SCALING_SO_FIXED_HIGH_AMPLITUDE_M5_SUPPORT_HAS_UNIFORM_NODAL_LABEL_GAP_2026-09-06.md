# DSD M17-189 — A nondegenerate winding node has linear line-weight and square-root amplitude scaling; fixed high-amplitude M5 support has a uniform nodal-label gap

Date: 2026-09-06  
Canonical ID: **M17-189**

Status: **NODAL-COLLAR SEPARATION THEOREM / AT A VERTICAL NONDEGENERATE WINDING NODE, AFTER CHOOSING THE SIGN SO THE HORIZONTAL HESSIAN `Q` IS POSITIVE DEFINITE, `q(x_h)=1/2 x_h^T Q x_h+O(|x_h|^3)`. SMALL REGULAR LEVELS `q=c>0` ARE ELLIPTIC VORTEX LOOPS WITH `rho=|grad_h q| ASYMPTOTIC sqrt(c)`. THEIR ENCLOSED AREA IS `2pi c/sqrt(det Q)+O(c^(3/2))` AND, BY THE DIVERGENCE THEOREM, THE ENSTROPHY LINE WEIGHT IS `L_rho(c)=2pi tr(Q)c/sqrt(det Q)+O(c^(3/2))`. UNIFORM COMPACT NONDEGENERACY OF `Q` MAKES THESE ESTIMATES UNIFORM. CONSEQUENTLY ANY FIXED HIGH-AMPLITUDE CUTOFF `rho>=a_0>0` EXCLUDES ALL LABELS WITH `0<c<c_*a_0^2`; THE HIGH-AMPLITUDE M5-683/688 SUPPORT IS SEPARATED FROM THE NODAL CRITICAL LABEL BY A POSITIVE `q` GAP. THUS THE EULERIAN HIGH-AMPLITUDE CONVEYOR CANNOT BE LOCALIZED DIRECTLY TO THE NODAL OCTUPOLE AT FIXED CUTOFF. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Nondegenerate vertical winding node

Fix one vertical winding node and normalize the critical value to

\[
q(0)=0.
\]

Assume the horizontal Hessian is definite.
After replacing `q` by `-q` if necessary, take

\[
\boxed{Q:=\nabla_h^2q(0)>0.}
\]

Then

\[
\boxed{
q(x_h)
=\frac12x_h^TQx_h
+O(|x_h|^3).
}
\]

Compact regular nodal geometry gives uniform eigenvalue bounds

\[
\boxed{
0<\lambda_*\le\lambda_{min}(Q)
\le\lambda_{max}(Q)\le\lambda^*<\infty.
}
\]

---

## 2. Small regular level loops

For sufficiently small `c>0`, the level

\[
\Gamma_c:=\{x_h:q(x_h)=c\}
\]

is a smooth closed ellipse-like curve surrounding the node.

Let

\[
\Omega_c:=\{q<c\}
\]

be its enclosed horizontal domain.

The quadratic model

\[
\frac12x_h^TQx_h<c
\]

has area

\[
\frac{2\pi c}{\sqrt{\det Q}}.
\]

Morse/Taylor stability gives

\[
\boxed{
|\Omega_c|
=\frac{2\pi c}{\sqrt{\det Q}}
+O(c^{3/2}).
}
\]

The remainder is uniform on a compact nondegenerate nodal hull.

---

## 3. Square-root amplitude scaling

On the great-circle branch,

\[
\rho=|W|=|\nabla_hq|.
\]

For the quadratic model,

\[
\nabla_hq=Qx_h.
\]

On `q=c`,

\[
|x_h|\asymp\sqrt c
\]

uniformly under the eigenvalue bounds of Section 1.
Therefore

\[
\boxed{
C_1\sqrt c
\le
\rho(x_h)
\le
C_2\sqrt c
\qquad(x_h\in\Gamma_c)
}
\]

for all sufficiently small `c`, with uniform positive constants `C_1,C_2`.

In particular,

\[
\boxed{
\sup_{\Gamma_c}\rho\asymp\sqrt c.
}
\]

---

## 4. Exact leading line-weight asymptotic

Define

\[
L_\rho(c)
:=\oint_{\Gamma_c}\rho ds
=\oint_{\Gamma_c}\partial_nq\,ds.
\]

By the horizontal divergence theorem,

\[
\boxed{
L_\rho(c)
=\int_{\Omega_c}\Delta_hq\,dA.
}
\]

Near the node,

\[
\Delta_hq
=\operatorname{tr}Q+O(|x_h|).
\]

Since `|x_h|=O(sqrt c)` in `Omega_c`, Sections 2--3 give

\[
\begin{aligned}
L_\rho(c)
&=\operatorname{tr}Q\,|\Omega_c|
+O(c^{3/2})\\
&=\frac{2\pi\operatorname{tr}Q}{\sqrt{\det Q}}c
+O(c^{3/2}).
\end{aligned}
\]

Thus

\[
\boxed{
L_\rho(c)
=\frac{2\pi\operatorname{tr}Q}{\sqrt{\det Q}}c
+O(c^{3/2}).
}
\]

In particular,

\[
\boxed{L_\rho(c)\asymp c.}
\]

---

## 5. Flux and enstrophy mass of a nodal collar

M17-179 gives the regular transverse flux element

\[
d\Phi=dq\,dx_3.
\]

At fixed `x_3`, the current flux mass of the small nodal collar

\[
0<q<\varepsilon
\]

therefore scales as

\[
\boxed{\Phi_{collar}\asymp\varepsilon.}
\]

Its enstrophy mass is weighted by `L_rho(q)`:

\[
E_{collar}
=\int_0^\varepsilon L_\rho(q)dq.
\]

Using Section 4,

\[
\boxed{E_{collar}\asymp\varepsilon^2.}
\]

Thus the nodal critical level is even thinner in enstrophy measure than in transverse-flux measure.

---

## 6. Fixed high-amplitude cutoff creates a positive label gap

Let the M5-683/M5-688 cutoff satisfy

\[
\chi(\rho)=0
\qquad(\rho\le a_0/2)
\]

and

\[
\chi(\rho)=1
\qquad(\rho\ge a_0)
\]

for a fixed `a_0>0`.

Section 3 gives

\[
\sup_{\Gamma_c}\rho\le C_2\sqrt c.
\]

Therefore if

\[
0<c<\frac{a_0^2}{4C_2^2},
\]

then the entire vortex loop satisfies

\[
\rho<a_0/2
\]

and is completely removed by the high-amplitude cutoff.

Hence there is a fixed constant

\[
\boxed{c_*=\frac1{4C_2^2}>0}
\]

such that

\[
\boxed{
\chi\neq0
\quad\Longrightarrow\quad
q\ge c_*a_0^2
}
\]

on all sufficiently small winding levels.

This is the **uniform nodal-label gap**.

---

## 7. Consequence for the M5-to-nodal strategy

M17-178--183 already show that high-amplitude M5 labels and the nodal filament are different material strata.

The present result strengthens this spatially:

\[
\boxed{
\text{fixed high-amplitude M5 support}
\cap
\{0<q<c_*a_0^2\}
=\varnothing.
}
\]

Thus even at one fixed time, the M5-683/688 high-amplitude PDE ledger cannot be squeezed arbitrarily close to the nodal critical label while keeping the cutoff fixed.

A bridge to `O_V` would require

1. sending the amplitude cutoff `a_0 -> 0` with uniform estimates;
2. or using a different low-amplitude measure/normalization;
3. or a genuinely nonlocal pressure coupling that does not rely on local label proximity.

---

## 8. DSD audit

### Audit A — assuming positive-definite `Q` without orientation
The sign of `q` is normalized so the definite Hessian is positive; negative-definite nodes are handled by replacing `q` with `-q` locally.

### Audit B — applying the result to saddle nodes
Rejected. The closed winding-loop argument is for definite nondegenerate critical points. Saddle/interface critical points are a separate branch.

### Audit C — claiming the M5 base flux measure has no nodal collar
The regular base flux collar has `O(epsilon)` mass. The stronger exclusion is for the **fixed high-amplitude cutoff** used by M5-683/688.

### Audit D — proof status
This separates the regular high-amplitude conveyor from the nodal pressure/octet block more strongly; it does not close either block.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
