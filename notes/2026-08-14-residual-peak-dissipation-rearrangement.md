# Residual-peak lower bound from Gaussian volume and physical dissipation

Date: 2026-08-14

Status: **DERIVED PEAK-HEIGHT / DISSIPATION TRADEOFF ON THE BOUNDED-AFFINE FIRST-HITTING BRANCH; GLOBAL REGULARITY NOT PROVED**.

This note combines four ingredients already established in the repository:

1. terminal first-hitting normalization;
2. the exact mean-vorticity cancellation, which makes the endpoint residual Duhamel source linear in the Gaussian residual variance `B_gamma`;
3. bounded-affine covariance growth `R_gamma(tau) ~ sqrt(tau)`;
4. the finite physical kinetic-energy dissipation budget.

The result rules out an infinitely repeated **very-low residual plateau**.  It does not yet rule out intermediate or high residual pulses.

---

## 1. Setup

At terminal first-hitting level

\[
W=\|\omega(T)\|_\infty,
\qquad
r=W^{-1/2},
\]

use normalized backward time

\[
\tau=T-s\ge0.
\]

On the bounded-affine branch, the endpoint affine heat covariance satisfies

\[
c_K\tau I\preceq\Sigma(\tau)\preceq C_K\tau I,
\]

hence the Gaussian volume radius

\[
R_\gamma=(\det\Sigma)^{1/6}
\]

obeys

\[
\boxed{R_\gamma(\tau)\asymp_K\tau^{1/2}.}
\]

Write

\[
B(\tau)=\mathcal B_\gamma(\tau)
=\int\gamma_\tau|\nabla U-L|^2.
\]

The mean-vorticity cancellation gives, on every bounded-affine time set `J`,

\[
\boxed{
\mathfrak R_{\gamma,J}
\le C_K\int_J B(\tau)\,d\tau.
}
\]

Therefore if a residual-dominant endpoint contribution has size at least `rho>0`, then necessarily

\[
\boxed{
\int_I B(\tau)d\tau\ge c_K\rho=:\rho_0>0
}
\]

on the responsible first-hitting interval `I`.

---

## 2. Terminal-layer improvement: `delta^2`

The earlier conditional terminal-collapse estimate gives

\[
B(\tau)\le C\tau
\]

for sufficiently small `tau`, provided the bounded-affine and weighted pressure conditions of that lemma hold.

Using the newer **linear** residual-source estimate rather than the older square-root estimate,

\[
\mathfrak R_{\gamma,[0,\delta]}
\le C_K\int_0^\delta B(\tau)d\tau
\le C\int_0^\delta\tau d\tau.
\]

Hence

\[
\boxed{
\mathfrak R_{\gamma,[0,\delta]}
\lesssim_{K}\delta^2.
}
\]

Thus an order-one endpoint residual cannot be created in an arbitrarily thin terminal layer on this branch.

---

## 3. Gaussian volume converts residual height into global gradient cost

Because `L` is the Gaussian mean of `grad U`,

\[
B(\tau)
\le P_{\Sigma(\tau)}|\nabla U|^2.
\]

The Gaussian density satisfies

\[
\|\gamma_{\Sigma}\|_\infty
=C R_\gamma^{-3}.
\]

Therefore

\[
B(\tau)
\le C R_\gamma(\tau)^{-3}
\|\nabla U(\tau)\|_2^2.
\]

Using `R_gamma(tau) ~ sqrt(tau)`, this reverses to

\[
\boxed{
\|\nabla U(\tau)\|_2^2
\ge c_K\tau^{3/2}B(\tau).
}
\]

The weight `tau^(3/2)` is the spatial Gaussian-volume cost.

---

## 4. Rearrangement lemma at fixed residual peak

Let

\[
m=\|B\|_{L^\infty(I)}.
\]

Assume

\[
0\le B\le m,
\qquad
\int_I B(\tau)d\tau\ge\rho_0.
\]

Since the weight `tau^(3/2)` is increasing, the smallest possible value of

\[
\int_I\tau^{3/2}B(\tau)d\tau
\]

under only these constraints is obtained by placing the residual mass as close to `tau=0` as possible at maximal height `m`.

Allowing the interval to start at zero only makes the lower-bound problem more permissive.  The bathtub/rearrangement calculation gives

\[
\begin{aligned}
\int_I\tau^{3/2}B(\tau)d\tau
&\ge
m\int_0^{\rho_0/m}\tau^{3/2}d\tau\\
&=
\boxed{
\frac25\rho_0^{5/2}m^{-3/2}.
}
\end{aligned}
\]

The terminal-collapse restriction `B(tau)<=C tau` can only increase this minimum; it is not needed for the exponent below.

Combining with the Gaussian-volume estimate,

\[
\boxed{
\int_I\|\nabla U(\tau)\|_2^2d\tau
\ge
c_{K,\rho_0}m^{-3/2}.
}
\]

---

## 5. Convert back to physical dissipation

Under

\[
U(y,s)=r u(x_*+ry,T+r^2s),
\]

one has

\[
\int\|\nabla U\|_2^2ds
=r^{-1}\int\|\nabla u\|_2^2dt.
\]

Therefore the physical dissipation paid on this first-hitting interval satisfies

\[
\boxed{
D_{\rm phys}(I)
:=\int_I\|\nabla u(t)\|_2^2dt
\ge
c_{K,\rho_0}
W^{-1/2}m^{-3/2}.
}
\]

This is the main peak-height / dissipation tradeoff.

---

## 6. Insert the adaptive one-step factor

Use the current checkpoint alignment

\[
q=W^{1/3+2\varepsilon},
\]

with the non-affine mesoscopic window nonempty when

\[
0<\varepsilon<1/30.
\]

Suppose the entire responsible residual state remains below

\[
m\lesssim q^{-\alpha}.
\]

Then

\[
D_{\rm phys}(I)
\gtrsim
W^{-1/2}q^{3\alpha/2}.
\]

Since

\[
q^{3\alpha/2}
=W^{\alpha(1/2+3\varepsilon)},
\]

we obtain

\[
\boxed{
D_{\rm phys}(I)
\gtrsim
W^{-1/2+\alpha(1/2+3\varepsilon)}.
}
\]

The exponent is nonnegative exactly when

\[
-\frac12
+\alpha\left(\frac12+3\varepsilon\right)
\ge0,
\]

i.e.

\[
\boxed{
\alpha\ge\alpha_*(\varepsilon)
:=\frac{1}{1+6\varepsilon}.
}
\]

For consecutive first-hitting intervals these physical time intervals are disjoint.  The global kinetic-energy identity permits only finite total dissipation.  Hence an infinite bounded-affine singular cascade cannot repeatedly satisfy an order-one endpoint residual requirement while also maintaining

\[
\boxed{
m\lesssim q^{-\alpha}}
\]

for any fixed

\[
\alpha\ge\frac1{1+6\varepsilon}.
\]

Equivalently, along any surviving infinite residual branch one must eventually have, up to fixed constants/subpower losses,

\[
\boxed{
\sup_I\mathcal B_\gamma
\gtrsim
q^{-1/(1+6\varepsilon)}.
}
\]

Examples:

- `epsilon=1/60` gives `alpha_*=10/11`;
- as `epsilon -> (1/30)^-`, `alpha_* -> 5/6`, although the mesoscopic window simultaneously narrows to zero width.

---

## 7. Osgood audit

At the previous checkpoint the four-channel state begins at

\[
B(s_0)\lesssim q^{-2}.
\]

The present lemma forces a surviving residual branch to rise at least to approximately

\[
q^{-\alpha_*},
\qquad
\alpha_*<1.
\]

However the small-state Osgood inequality

\[
B'\lesssim A(s)B[1+\log(C/B)]
\]

requires only

\[
\int A(s)ds
\gtrsim
\log\frac{2}{\alpha_*}+O((\log q)^{-1})
\]

to move from `q^(-2)` to `q^(-alpha_*)`.

This is an order-one action, not a growing `log log q` action.  Therefore the new peak lower bound **does not yet close** the surviving intermediate-pulse branch.

---

## 8. Revised residual trichotomy

The bounded-affine residual route can now be split more sharply.

### A. Very-low plateau

\[
\sup B\lesssim q^{-\alpha},
\qquad
\alpha\ge\frac1{1+6\varepsilon}.
\]

Repeated order-one endpoint action forces non-summable physical dissipation.

**This branch is excluded on an infinite disjoint checkpoint cascade.**

### B. Intermediate pulse

\[
q^{-1/(1+6\varepsilon)}
\lesssim
\sup B
\ll1.
\]

Finite dissipation and the current Osgood estimate do not yet exclude this branch.

### C. Order-one pulse

\[
\sup B\gtrsim b_*>0.
\]

The earlier Osgood result requires `log log q` multiplicative action or a pressure-forced alternative, but conversion to a globally non-summable physical budget remains open.

Thus the immediate remaining target is no longer an arbitrary low residual history.  It is the **intermediate-to-high residual pulse regime**, together with affine degeneration / parent harmonic pressure escalation.

---

## 9. Next rigidity target

A potentially useful next step is to test whether the surviving intermediate/high pulse can simultaneously near-saturate

1. Gaussian Poincare/coercivity;
2. the residual-to-curvature square-function identity;
3. the Gaussian-volume dissipation lower bound;
4. first-hitting vorticity boundedness;
5. the four-channel strain/vorticity decomposition.

A quantitative incompatibility among these saturation conditions would produce the strict gain still missing from the mesoscopic window.

Status: **VERY-LOW RESIDUAL PLATEAU EXCLUDED / INTERMEDIATE-TO-HIGH PULSE SATURATION REMAINS OPEN**.
