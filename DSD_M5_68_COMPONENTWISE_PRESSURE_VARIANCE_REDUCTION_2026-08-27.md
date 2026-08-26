# DSD M5-68 — Componentwise Pressure-Variance Reduction

Date: 2026-08-27

Status: **FURTHER INCOMPRESSIBILITY LOCALIZATION / THE NET VELOCITY FLUX VANISHES SEPARATELY ON THE FULL BOUNDARY OF EACH BOUNDED CONNECTED COMPONENT OF AN AMPLITUDE SUPERLEVEL SET / PRESSURE CONSTANTS MAY THEREFORE BE SUBTRACTED INDEPENDENTLY COMPONENT BY COMPONENT / EVEN PRESSURE DIFFERENCES BETWEEN DISCONNECTED HIGH-AMPLITUDE BLOBS DO NOT POWER THE THRESHOLD PUMP / ONLY INTRA-COMPONENT BOUNDARY PRESSURE OSCILLATION PAYS / GLOBAL REGULARITY UNPROVED.**

## 1. Connected superlevel decomposition

For a positive regular value `lambda`, decompose the bounded active superlevel set

\[
\Omega_\lambda
=
\{a>\lambda\}
\]

into its connected components:

\[
\boxed{
\Omega_\lambda
=
\bigsqcup_k
\Omega_{\lambda,k}.
}
\]

Each component has full boundary

\[
\Gamma_{\lambda,k}
:=
\partial\Omega_{\lambda,k}.
\]

A full component boundary may itself have several connected surface pieces if the superlevel component contains holes. The statement below is made for the entire induced boundary of each volume component.

---

## 2. Zero flux holds componentwise

Since

\[
\nabla\cdot U=0,
\]

the divergence theorem applies to every bounded connected volume component separately:

\[
\boxed{
\int_{\Gamma_{\lambda,k}}
U\cdot n_k\,dS
=0
\qquad\text{for every }k.
}
\]

Thus the global zero-flux relation from M5-67 is actually the sum of a family of independent componentwise zero-flux identities.

This is strictly stronger information.

---

## 3. Independent pressure shifts on each component boundary

Write the threshold pressure flux as

\[
J_P(\lambda)
=
\sum_k
J_{P,k}(\lambda),
\]

where

\[
J_{P,k}(\lambda)
:=
\int_{\Gamma_{\lambda,k}}
P\,U\cdot n_k\,dS.
\]

For arbitrary constants `c_k(lambda,t)`, one per volume component,

\[
\begin{aligned}
J_{P,k}
&=
\int_{\Gamma_{\lambda,k}}
(P-c_k)U\cdot n_k\,dS\\
&+c_k
\int_{\Gamma_{\lambda,k}}U\cdot n_k\,dS.
\end{aligned}
\]

The second term is zero. Hence

\[
\boxed{
J_P(\lambda)
=
\sum_k
\int_{\Gamma_{\lambda,k}}
(P-c_k)U\cdot n_k\,dS.
}
\]

Therefore one may center pressure independently on every connected high-amplitude blob.

---

## 4. Optimal componentwise weighted means

For each `Gamma_{lambda,k}`, define the weighted mean

\[
\boxed{
m_{P,k}(\lambda)
:=
\frac{
\int_{\Gamma_{\lambda,k}}
P|\nabla a|^{-1}dS
}{
\int_{\Gamma_{\lambda,k}}
|\nabla a|^{-1}dS
}.
}
\]

Define the componentwise variance density

\[
\boxed{
V_{P,comp}(\lambda)
:=
\sum_k
\int_{\Gamma_{\lambda,k}}
\frac{|P-m_{P,k}(\lambda)|^2}{|\nabla a|}dS.
}
\]

Because independent minimization over the constants `m_{P,k}` is more flexible than choosing one common level mean,

\[
\boxed{
V_{P,comp}(\lambda)
\le
V_P(\lambda)
\le
-\partial_\lambda Q_P(\lambda).
}
\]

The first inequality is strict whenever disconnected active components carry different pressure means that contributed to the global level variance in M5-67.

---

## 5. Componentwise-centered Cauchy inequality

Using the independently centered pressure on the disjoint component boundaries and applying Cauchy--Schwarz over their union gives

\[
\boxed{
|J_P(\lambda)|^2
\le
V_{P,comp}(\lambda)
\sum_k
\int_{\Gamma_{\lambda,k}}
(U\cdot n_k)^2|\nabla a|dS.
}
\]

Thus no pressure mean difference between two disconnected blobs can be counted as a pump resource.

Only pressure variation **within the full boundary of each connected superlevel volume** couples to its zero-net-flux pattern.

---

## 6. Amplitude-mollified componentwise payer

Define

\[
\boxed{
S_{comp,w}
:=
\int_0^\infty
w(\lambda)\lambda
V_{P,comp}(\lambda)d\lambda.
}
\]

Then

\[
\boxed{
0\le
S_{comp,w}
\le
S_{var,w}
\le
S_w.
}
\]

The associated normal-crossing factor is unchanged. Therefore, with the M5-66 angular gap,

\[
\boxed{
|\bar J_w|^2
\le
S_{comp,w}
(D_w-A_w-G_w).
}
\]

The exact entropy ledger gives

\[
\bar J_w
=
\nu D_w+X_w.
\]

Hence

\[
\boxed{
(\nu D_w+X_w)^2
\le
S_{comp,w}
(D_w-A_w-G_w).
}
\]

---

## 7. Robust upstroke lower requirement

Repeating the M5-66 algebra for `X_w>=0` yields

\[
\boxed{
S_{comp,w}
\ge
\nu^2(A_w+G_w)
+4\nu X_w.
}
\]

Thus every robust returned pump requires one fixed normalized amount of **intra-component boundary pressure variance**.

If M5-57 gives

\[
X_w\ge c_1>0
\]

and the retained positive-excess class gives

\[
A_w\ge A_{w,*}>0,
\]

then

\[
\boxed{
S_{comp,w}
\ge
\nu^2A_{w,*}
+4\nu c_1
}
\]

even if the angular gap happens to be small.

---

## 8. DSD interpretation

The successive payer reductions are now

\[
\boxed{
\begin{array}{c}
\text{absolute pressure magnitude}\\
\Downarrow\\
\text{pressure variation along one amplitude level}\\
\Downarrow\\
\text{pressure variation within each connected active superlevel component}.
\end{array}
}
\]

The following pressure structures are now known **not** to pay the threshold pump:

1. a global time-dependent pressure gauge;
2. one common pressure offset on an amplitude level;
3. different constant pressure offsets carried by disconnected high-amplitude blobs.

The pump requires pressure to vary internally across the boundary of the same connected active volume while correlating with the zero-net normal crossing on that boundary.

---

## 9. Interaction with the angular zero-gap endpoint

If in addition

\[
G_w\to0,
\]

then velocity becomes almost normal to the amplitude level boundaries.

But every connected volume component has zero net normal flux.

Therefore a near-zero angular-gap pump must organize strong inward/outward normal-crossing cancellation **within the same component boundary**, while the centered pressure fluctuation must distinguish those opposite crossings strongly enough to produce positive net pressure work.

This gives a concrete finite-dimensional-looking geometric pattern:

\[
\boxed{
\text{zero net normal flux}
+
\text{large signed pressure/flux covariance}
+
\text{small angular defect}.
}
\]

The remaining question is whether the pressure-Poisson source can sustain this pattern recurrently.

---

## 10. Topological caution

Zero net flux is guaranteed on the **entire boundary of a connected volume component**, not necessarily on each connected surface component of that boundary.

If a superlevel component has holes, flux may enter through one boundary surface and leave through another while the total remains zero.

Therefore one must not yet assume that small `G_w` is impossible solely because velocity is approximately normal to one visible level surface.

A direct contradiction would require either:

- control of the topology of the active superlevel components; or
- an argument that works with the full component boundary without assuming simple connectivity.

This distinction is retained as a DSD audit condition.

---

## 11. New rigidity target

M5-68 reduces the direct pressure branch to the componentwise covariance

\[
\boxed{
\sum_k
\int_{\Gamma_{\lambda,k}}
(P-m_{P,k})
U\cdot n_k\,dS.
}
\]

A closure theorem can now aim to prove that, for the localized pressure-Poisson source of M5-51, this covariance cannot repeatedly achieve the lower amount demanded by

\[
S_{comp,w}
\ge
\nu^2(A_w+G_w)+4\nu X_w
\]

on syndetically recurrent pump intervals.

This is narrower than the previous total-pressure or global-level-variance targets.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
