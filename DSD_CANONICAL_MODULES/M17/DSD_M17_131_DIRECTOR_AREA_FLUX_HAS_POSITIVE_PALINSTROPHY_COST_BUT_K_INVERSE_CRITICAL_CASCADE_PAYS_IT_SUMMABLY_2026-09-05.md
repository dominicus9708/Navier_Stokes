# DSD M17-131 — Director-area flux has a positive palinstrophy cost, but the K^-1 critical cascade pays it summably

Date: 2026-09-05
Canonical ID: **M17-131**

Status: **EXACT POSITIVE INEQUALITY PLUS CRITICAL-SCALING FIREWALL / THE DIRECTOR-AREA JACOBIAN SATISFIES `2|J_xi|<=|grad xi|^2`, AND `W=rho xi` GIVES `|grad W|^2=|grad rho|^2+rho^2|grad xi|^2`. HENCE `2rho^2|J_xi|<=|grad W|^2`. IN DIRECTOR-FLUX COORDINATES THIS GIVES A POSITIVE PALINSTROPHY COST FOR EVERY RIBBON TUBE. HOWEVER, ON A UNIFORMLY NONDEGENERATE COMPACT RIBBON WITH THE SHARP M17-129 FLUX SCALING `Phi_k~K_k^-1`, THE UNWEIGHTED PALINSTROPHY COST IS ALSO `O(K_k^-1)` AND IS GEOMETRICALLY SUMMABLE. THUS ORDINARY PALINSTROPHY FINITENESS DOES NOT CONTROL THE WEIGHTED CUBIC FLUX STACK; A NEW RADIAL/TAIL-WEIGHTED PALINSTROPHY OR RIGIDITY INPUT WOULD BE REQUIRED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Singular-value form of the director Jacobian

Because `xi` takes values in `S^2`, the differential

\[
d\xi:T_x\mathbb R^3\to T_{\xi(x)}S^2
\]

has rank at most two.
Let its nonzero singular values be

\[
s_1,s_2\ge0.
\]

With the canonical area-current normalization,

\[
\boxed{|J_\xi|=s_1s_2}
\]

and

\[
\boxed{|\nabla\xi|^2=s_1^2+s_2^2.}
\]

The arithmetic-geometric mean inequality gives

\[
\boxed{
2|J_\xi|
\le
|\nabla\xi|^2.
}
\]

Equality is the conformal director-jet case `s_1=s_2`.

---

## 2. Vorticity gradient decomposition

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Since

\[
\xi\cdot\partial_i\xi=0,
\]

one has pointwise

\[
\boxed{
|\nabla W|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
}
\]

Combining with Section 1,

\[
\boxed{
2\rho^2|J_\xi|
\le
\rho^2|\nabla\xi|^2
\le
|\nabla W|^2.
}
\]

This is positive and does not suffer signed-flux cancellation.

---

## 3. Ribbon flux-coordinate cost

On a regular `J_xi` flux tube,

\[
dV=\frac{d\Phi_J\,ds}{|J_\xi|}.
\]

Therefore

\[
\begin{aligned}
\int_{\mathcal T}|\nabla W|^2dV
&\ge
2\int_{\mathcal T}\rho^2|J_\xi|dV\\
&=
2\int d\Phi_J
\int_{\Gamma_\lambda}\rho^2ds.
\end{aligned}
\]

Hence

\[
\boxed{
\int_{\mathcal T}|\nabla W|^2dV
\ge
2\int d\Phi_J
\oint_{\Gamma_\lambda}\rho^2ds
}
\]

for complete ribbon loops.

---

## 4. Compact nondegenerate ribbon lower cost

If on the selected complete ribbon class

\[
\rho\ge c_\rho>0
\]

and the loop length satisfies

\[
L_\lambda\ge L_->0,
\]

then

\[
\oint\rho^2ds
\ge c_\rho^2L_-.
\]

Thus

\[
\boxed{
\int_{\mathcal T}|\nabla W|^2dV
\ge
2c_\rho^2L_-\Phi_{\mathcal T}.
}
\]

The director-area flux therefore carries a genuine positive palinstrophy cost whenever normalized vorticity amplitude does not collapse.

---

## 5. Critical K^-1 scaling remains summable

M17-129 identifies the sharp ribbon critical model

\[
\Phi_k\sim K_k^{-1}.
\]

Under fixed compact ribbon constants, Section 4 gives only an unweighted lower cost of the same order,

\[
P_k^{rib}
:=\int_{\mathcal T_k}|\nabla W|^2dV
\gtrsim
K_k^{-1}.
\]

Since `K_k` grows geometrically,

\[
\boxed{
\sum_kK_k^{-1}<\infty.
}
\]

Therefore the existence of finite total unweighted palinstrophy is compatible with the critical director-flux cascade.

The positive inequality is real but subcritical for the M17-129 weighted stack.

---

## 6. Weighted quantity that would be needed

The ribbon cubic obstruction sees

\[
K_k\Phi_k,
\]

not merely `Phi_k`.
A palinstrophy closure would therefore need a bound comparable to

\[
\boxed{
\sum_kK_kP_k^{rib}<\infty
}
\]

or another estimate strong enough to imply control of the sequence

\[
K_k\Phi_k.
\]

No such radially weighted palinstrophy bound follows from the ordinary energy ledger or from the current CE-H identities.

---

## 7. Relation to kappa payer

Globally, under sufficient decay/integrability, the CE-H Schrödinger identity

\[
\Delta W=\kappa W
\]

gives

\[
\boxed{
\int\kappa|W|^2dy
=-\int|\nabla W|^2dy.
}
\]

Thus the total palinstrophy is also a total negative signed `kappa` payer.

However, on a bounded ribbon subdomain there are boundary terms, so one may not identify each individual ribbon-shell palinstrophy with a local negative-kappa integral without adding its boundary flux.

Even globally, the critical `K_k^-1` palinstrophy cost is summable and therefore does not contradict the signed kappa ledger.

---

## 8. DSD audit

### Audit A — director flux is energetically free

Rejected. `2rho^2|J_xi|<=|grad W|^2` gives a positive local cost.

### Audit B — positive cost automatically closes the cubic tail

Rejected. The sharp cost is summable at `Phi_k~K_k^-1`.

### Audit C — using a lower amplitude bound on every diffuse tail ribbon

Not automatic. Section 4 is conditional on `rho>=c_rho`; shells whose amplitude collapses must remain in the nodal/amplitude-degeneration branch.

### Audit D — local palinstrophy equals local negative kappa payer

Rejected unless boundary terms are controlled.

### Audit E — proof status

The positive director-energy route is quantified but is too weak in its unweighted form.

---

## 9. Updated weighted-flux frontier

The two simplest global quantities are now both known to be insufficient for the sharp model:

\[
\boxed{
\sum\Phi_k<\infty
\quad\text{and}\quad
\sum P_k^{rib}<\infty
}
\]

can coexist with

\[
\boxed{
\sum(K_k\Phi_k)^{3/2}=\infty.
}
\]

The next viable target is therefore not another unweighted charge. It is either:

1. a genuine scale-weighted identity tied to the Navier–Stokes equations;
2. a CE-H realization rigidity excluding a nested `Phi_k~K_k^-1` ribbon family;
3. or the existing Liouville/tail-decoupling route.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
