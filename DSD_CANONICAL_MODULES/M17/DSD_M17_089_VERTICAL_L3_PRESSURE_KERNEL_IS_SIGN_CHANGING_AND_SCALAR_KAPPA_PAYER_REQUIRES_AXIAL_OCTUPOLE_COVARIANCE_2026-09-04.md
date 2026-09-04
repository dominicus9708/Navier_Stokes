# DSD M17-089 — The vertical l=3 pressure kernel is sign-changing; the scalar kappa payer requires axial octupole covariance

Date: 2026-09-04
Canonical ID: **M17-089**

Status: **INTERNAL VERTICAL l=3 / PAYER BRIDGE AUDIT / M17-082 REQUIRES THE GLOBAL AXIAL STF PRESSURE COORDINATE `H_333`, WHILE M17-012 AND M5 SUPPLY SCALAR POSITIVE-SHEATH / NEGATIVE-KAPPA PAYER BUDGETS. THE STF NEWTONIAN KERNEL FOR THE AXIAL COORDINATE IS `K_333(z)=3 z_3(3|z|^2-5z_3^2)/(4pi|z|^7)`. IT IS ODD UNDER `z_3->-z_3` AND CHANGES SIGN AGAIN ACROSS THE CONES `|z_3|/|z|=sqrt(3/5)`. THEREFORE THE SCALAR SIGN OF `kappa` OR OF THE PAYER MASS DOES NOT DETERMINE THE SIGN OF ITS AXIAL l=3 MOMENT. THE `-kappa rho^2` PIECE OF THE GLOBAL PRESSURE-SOURCE PRODUCTION IS AN AXIAL OCTUPOLE COVARIANCE, NOT A SIGNED LIFT OF M17-012. M17-056'S EVEN LEADING POSITIVE SHEATH IS CONSISTENTLY l=3-NEUTRAL. THUS THE VERTICAL M17-082 MEAN-ZERO GLOBAL LOCK CANNOT BE CLOSED FROM THE SCALAR M5/M17 PAYER LEDGER WITHOUT ADDITIONAL SPATIAL ORIENTATION INFORMATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vertical global l=3 state

M17-082 defines

\[
H_V:=\mathcal H_{333},
\]

where

\[
\mathcal H=STF_3(\nabla^3P).
\]

M17-053 represents the global tensor as

\[
\mathcal H_{ijk}(Y)
=\langle S_P(y),\mathcal K_{ijk}(Y-y)\rangle,
\]

with

\[
G(z)=\frac1{4\pi|z|},
\qquad
\mathcal K_{ijk}=STF_3[\partial_{ijk}G].
\]

The relevant vertical coordinate is therefore

\[
\boxed{
H_V(Y)
=\langle S_P(y),\mathcal K_{333}(Y-y)\rangle.
}
\]

---

## 2. Explicit axial cubic kernel

Away from the origin, `G` is harmonic. Hence the raw third derivative is already trace free there:

\[
\partial_{iik}G
=\partial_k\Delta G
=0.
\]

The standard third derivative is

\[
\partial_{ijk}\frac1{|z|}
=
3\frac{\delta_{ij}z_k+\delta_{ik}z_j+\delta_{jk}z_i}{|z|^5}
-15\frac{z_iz_jz_k}{|z|^7}.
\]

For `i=j=k=3`,

\[
\partial_{333}\frac1{|z|}
=9\frac{z_3}{|z|^5}
-15\frac{z_3^3}{|z|^7}.
\]

Therefore

\[
\boxed{
\mathcal K_{333}(z)
=
\frac{3}{4\pi}
\frac{z_3(3|z|^2-5z_3^2)}{|z|^7}
}
\]

away from the core, with the STF distributional prescription of M17-053 at the origin.

---

## 3. The kernel has no global sign

First,

\[
\boxed{
\mathcal K_{333}(z_1,z_2,-z_3)
=-\mathcal K_{333}(z_1,z_2,z_3).
}
\]

Thus it is axially odd.

Second, for `z_3!=0`, the additional angular factor changes sign when

\[
3|z|^2-5z_3^2=0.
\]

Equivalently,

\[
\boxed{
\frac{|z_3|}{|z|}=\sqrt{\frac35}.
}
\]

Hence each half-space is itself divided into kernel-positive and kernel-negative angular sectors.

There is therefore no positivity cone covering the whole payer region without an additional localization/orientation hypothesis.

---

## 4. Isolate the kappa-rho^2 source-production channel

M17-053 gives

\[
\begin{aligned}
D_BS_P+\frac32S_P
={}&2\Sigma:\Delta\Sigma
-\frac12|\Sigma|^2
-2\operatorname{tr}(\Sigma^3)
-2\Sigma:\Omega^2\\
&-2\Sigma:\nabla^2P
-\left(\sigma+\kappa-\frac14\right)\rho^2.
\end{aligned}
\]

The part carrying the scalar kappa payer is

\[
\boxed{-\kappa\rho^2.}
\]

Its contribution to the vertical source-production channel is

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
:=-\langle\kappa\rho^2,\mathcal K_{333}(Y-\cdot)\rangle.
}
\]

---

## 5. Positive/negative kappa split does not fix the sign

Write

\[
Q_+=\int_{\{\kappa>0\}}\kappa\rho^2,
\qquad
Q_-=\int_{\{\kappa<0\}}(-\kappa)\rho^2.
\]

M17-012 gives a fixed positive sheath contribution and forces a larger negative payer budget in the scalar measure.

But the vertical octupole contribution is

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=
-\int_{\kappa>0}\kappa\rho^2\mathcal K_{333}
+
\int_{\kappa<0}(-\kappa)\rho^2\mathcal K_{333}.
}
\]

Neither integral has a fixed sign because `K_333` changes sign spatially.
Therefore

\[
\boxed{
Q_->Q_+
\not\Longrightarrow
\operatorname{sgn}\Pi_{V,\kappa}^{prod}.
}
\]

The scalar payer magnitude and the vertical l=3 orientation are different descriptors.

---

## 6. Define the required axial octupole covariance

Let the positive payer measure be

\[
d\mu_+=\mathbf1_{\kappa>0}\kappa\rho^2dy
\]

and the negative payer measure

\[
d\mu_-=\mathbf1_{\kappa<0}(-\kappa)\rho^2dy.
\]

Define their kernel averages relative to the marked vertical core `Y`:

\[
\boxed{
\bar K_+(Y)
:=\frac1{Q_+}\int\mathcal K_{333}(Y-y)d\mu_+(y),
}
\]

\[
\boxed{
\bar K_-(Y)
:=\frac1{Q_-}\int\mathcal K_{333}(Y-y)d\mu_-(y),
}
\]

when the corresponding masses are nonzero.
Then

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=-Q_+\bar K_+
+Q_-\bar K_-.
}
\]

Thus a sign bridge requires information about

\[
\boxed{(Q_+,Q_-;\bar K_+,\bar K_-),}
\]

not merely `Q_+-Q_-`.

This is the **axial octupole covariance** missing from the scalar payer ledger.

---

## 7. Leading positive nodal sheath is correctly neutral

M17-056 shows that near a regular nodal core

\[
\kappa\rho^2
=F_2+F_3+O(|x|^4),
\]

with the leading term

\[
F_2=\kappa_0 x^TCx
\]

inversion-even and containing only `l=0,2` angular content.
Therefore

\[
\boxed{
\Pi_{l=3}F_2=0.
}
\]

This matches the odd/sign-changing structure of `K_333`: the leading symmetric positive sheath cannot by itself generate the vertical cubic pressure moment.

The first local contribution appears only at the cubic third-jet level of M17-056--057.

---

## 8. M5 hysteresis also lacks the missing spatial orientation

M5-685 controls a flux-weighted temporal crossing bias at

\[
\kappa=0
\]

through

\[
\overline G_\Phi(0)<0.
\]

This distinguishes downward and upward temporal zero crossings in the amplification measure.
It does not determine where the corresponding payer mass lies relative to the angular sign sectors of `K_333` around the marked core.

Thus

\[
\boxed{
\text{M5 temporal crossing sign}
\not\Rightarrow
\text{vertical spatial l=3 sign}.
}
\]

A joint space-time orientation covariance would be needed to bridge them.

---

## 9. Consequence for the M17-082 recurrence lock

M17-082 requires

\[
\boxed{
\left\langle
\Pi_V^{prod}+\Pi_V^{rel}
\right\rangle=0.
}
\]

Even after isolating the `-kappa rho^2` source piece, the scalar payer theorem gives no fixed sign for `Pi_{V,kappa}^{prod}`.
Moreover `Pi_V^prod` contains other signed strain/pressure source terms and `Pi_V^rel` is itself signed.

Therefore the vertical global lock is not contradicted by the existing scalar payer/hysteresis ledger.

Instead it is narrowed to a coupled covariance problem.

---

## 10. DSD analysis

Three descriptors must remain distinct:

1. scalar payer mass: `Q_+,Q_-`;
2. temporal crossing bias: `G_Phi(0)`;
3. spatial axial octupole orientation: `bar K_+,bar K_-`.

The required bridge is not equality of these descriptors but a joint law relating them.

This is exactly the kind of measure/descriptor separation that the DSD audit is intended to preserve.

---

## 11. DSD audit

### Audit A — treating K_333 as positive on z_3>0
Rejected. It changes sign across the cone `|z_3|/|z|=sqrt(3/5)` even within one half-space.

### Audit B — using Q_->Q_+ as an l=3 sign theorem
Rejected. The kernel-weighted averages are essential.

### Audit C — using the positive nodal sheath to force H_333
Rejected by M17-056 parity: the leading sheath is l=3-neutral.

### Audit D — identifying temporal downward crossings with a spatial octupole orientation
Rejected. M5 crossing current and K_333 covariance live on different descriptor spaces.

### Audit E — claiming the covariance firewall closes the vertical branch
Rejected. It only identifies the missing information required for a sign-preserving bridge.

### Audit F — proof status
No contradiction is obtained.

---

## 12. Updated vertical l=3 frontier

Every finite-order vertical nonaxis branch satisfies the M17-082 axial global lock, but the scalar payer contribution enters it as

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=-Q_+\bar K_++Q_-\bar K_-.
}
\]

Therefore

\[
\boxed{
R_{1,V}^{nonaxis}
\Longrightarrow
R_{V}^{axial\ l=3\ covariance}
\ \lor\
T_{1,V}.
}
\]

The next useful local reduction is to compute the vertical `333` component of the explicit M17-057 local payer octupole under the vertical nodal identities `grad_h kappa=0` and `q_{13}=q_{23}=0`.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
