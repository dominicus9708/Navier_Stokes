# DSD M17-095 — M5 hysteresis forces a positive label-weighted vertical octupole–relative-speed bias without coarea substitution

Date: 2026-09-05
Canonical ID: **M17-095**

Status: **INTERNAL VERTICAL M5–OCTUPOLE BRIDGE / M5-685 DEFINES THE KAPPA-SPACE CURRENT WITH THE ORIGINAL BASE LABEL MEASURE `dmu_0`: `G_Phi(k,theta)=int h a delta(k-kappa) dmu_0`, AND THE RETAINED RECHARGE/HYSTERESIS BRANCH REQUIRES `mean G_Phi(0)<0`. M17-090 GIVES AT A SPATIALLY REGULAR VERTICAL KAPPA-ZERO CROSSING `O_V=(O_loc^(3))_333=-(1/5)|Q|_F^2 kappa_3` AND `h=(B_3-v_0)kappa_3= -5(B_3-v_0)O_V/|Q|_F^2`. SUBSTITUTION INSIDE THE SAME LABEL LEDGER YIELDS THE EXACT POSITIVE MEAN BIAS `mean int a (B_3-v_0) O_V |Q|_F^-2 delta(kappa) dmu_0 >0`. NO CURRENT SPATIAL VOLUME, COAREA SURFACE MEASURE, OR UNJUSTIFIED PUSHFORWARD IS INTRODUCED. THE RESULT LINKS M5'S TEMPORAL CROSSING BIAS TO LOCAL VERTICAL OCTUPOLE ORIENTATION TIMES ZERO-SURFACE RELATIVE SPEED, BUT IT DOES NOT DETERMINE THE GLOBAL AXIAL STF PRESSURE MOMENT BECAUSE M17-089'S K_333 KERNEL CHANGES SIGN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Keep the original M5 measure

M5-685 defines the amplification weight

\[
\boxed{
a_\lambda(\theta)
=\exp\int\kappa_\lambda\,d\theta,
\qquad
a_\lambda'=\kappa_\lambda a_\lambda.
}
\]

The flux-weighted kappa-space current is

\[
\boxed{
G_\Phi(k,\theta)
=\int h_\lambda a_\lambda
\delta(k-\kappa_\lambda)\,d\mu_0(\lambda),
}
\]

with

\[
\boxed{h_\lambda=D_B\kappa_\lambda.}
\]

The measure `dmu_0` is the initial/base **label measure** used by M5.

On the retained recharge/hysteresis branch,

\[
\boxed{
\overline{G_\Phi(0)}<0.
}
\]

No spatial coarea interpretation is required for the calculation below.

---

## 2. Vertical regular zero-crossing geometry

Restrict to the vertical Rank-1 branch and to spatially regular kappa-zero crossings for which

\[
\kappa=0,
\qquad
\kappa_3\neq0.
\]

M17-090 defines the axial local payer octupole component

\[
\boxed{
O_V
:=(\mathcal O_{loc}^{(3)})_{333}
=-\frac15|Q|_F^2\kappa_3
}
\]

at `kappa=0`.

Let the local spatial zero surface be

\[
x_3=z_0(\theta)
\]

with coordinate speed

\[
v_0=z_0'(\theta).
\]

Define its relative velocity with respect to the similarity material flow by

\[
\boxed{r_V:=B_3-v_0.}
\]

Then M17-090 gives

\[
\boxed{
h=r_V\kappa_3.}
\]

Hence

\[
\boxed{
h
=-\frac{5r_V}{|Q|_F^2}O_V.}
\]

---

## 3. Substitute into the M5 current at kappa=0

At `k=0`,

\[
G_\Phi(0,\theta)
=\int h_\lambda a_\lambda
\delta(\kappa_\lambda)\,d\mu_0.
\]

On the regular vertical crossing population, substitute Section 2:

\[
\boxed{
G_\Phi(0,\theta)
=-5\int
 a_\lambda
\frac{r_{V,\lambda}O_{V,\lambda}}{|Q_\lambda|_F^2}
\delta(\kappa_\lambda)
\,d\mu_0(\lambda).
}
\]

This is an exact identity within the same label ensemble.

---

## 4. Hysteresis gives a positive octupole–relative-speed bias

Use

\[
\overline{G_\Phi(0)}<0.
\]

The factor `-5` is fixed and negative, so

\[
\boxed{
\overline{
\int
 a_\lambda
\frac{r_{V,\lambda}O_{V,\lambda}}{|Q_\lambda|_F^2}
\delta(\kappa_\lambda)
\,d\mu_0(\lambda)
}>0.
}
\]

This is the exact vertical M5-to-local-octupole bias.

It says that the amplification-weighted zero-crossing population favors the joint sign

\[
\boxed{r_V O_V>0}
\]

in the averaged weighted sense above.

It does **not** say that every individual crossing has that sign.

---

## 5. Equivalent slope-orientation form

At a regular crossing,

\[
\operatorname{sgn}O_V
=-\operatorname{sgn}\kappa_3.
\]

Therefore

\[
h
=-r_V|\kappa_3|\operatorname{sgn}O_V.
\]

The current can be written as

\[
\boxed{
G_\Phi(0,\theta)
=-\int
 a_\lambda|\kappa_{3,\lambda}|r_{V,\lambda}
\operatorname{sgn}O_{V,\lambda}
\delta(\kappa_\lambda)
\,d\mu_0.
}
\]

Hence

\[
\boxed{
\overline{
\int
 a_\lambda|\kappa_{3,\lambda}|r_{V,\lambda}
\operatorname{sgn}O_{V,\lambda}
\delta(\kappa_\lambda)
\,d\mu_0
}>0.
}
\]

This separates the three factors:

1. crossing steepness `|kappa_3|`;
2. zero-surface relative speed `r_V`;
3. local axial octupole orientation `sgn O_V`.

---

## 6. Label-root representation

M17-091 gives

\[
\boxed{
\kappa_3
=F_{qq}(q_3-q_{*,3}),
}
\]

\[
\boxed{
h=F_{qq}V_{rel}^{label},}
\]

and therefore

\[
\boxed{
r_V
=\frac{V_{rel}^{label}}{q_3-q_{*,3}}.}
\]

Thus the relative-speed factor in Sections 3--5 is not an extra independent kinematic variable; it is the ratio of

\[
\boxed{
\text{label-root relative flow}
\quad\text{to}\quad
\text{spatial label-root slope}.
}
\]

The M5 current and M17 label-plane geometry therefore agree exactly.

---

## 7. Why this still does not fix the global pressure lock

M17-082 uses the global axial STF pressure moment

\[
\mathcal H_{333}
=\langle S_P,\mathcal K_{333}\rangle,
\qquad
S_P=|\Sigma|^2-\frac12\rho^2.
\]

M17-089 gives the sign-changing kernel

\[
\boxed{
\mathcal K_{333}(z)
=\frac{3}{4\pi}
\frac{z_3(3|z|^2-5z_3^2)}{|z|^7}.
}
\]

The M17-095 bias concerns the **local crossing octupole** `O_V` and `r_V` under the M5 label measure.
It does not provide a sign-preserving map to the global spatial pressure-source moment.

Therefore

\[
\boxed{
\overline{G_\Phi(0)}<0
\not\Longrightarrow
\operatorname{sgn}\mathcal H_{333}
\text{ is fixed}.
}
\]

---

## 8. DSD analysis

The relevant descriptor chain is now

\[
\boxed{
\text{M5 label crossing }h
\leftrightarrow
r_V\kappa_3
\leftrightarrow
r_V O_V
}
\]

inside one label measure.

The global pressure lock remains a distinct spatial STF moment descriptor.

---

## 9. DSD audit

### Audit A — replacing `dmu_0` by present spatial volume
Rejected.

### Audit B — replacing the delta label current by a coarea surface integral without a Jacobian theorem
Rejected.

### Audit C — reading the positive mean bias as a pointwise sign law
Rejected.

### Audit D — identifying the local payer octupole with the global pressure STF moment
Rejected by M17-089 and by the different source densities.

### Audit E — proof status
The vertical crossing bridge is exact, but the local-to-global axial covariance remains open.

---

## 10. Updated vertical Rank-1 gate

A recurrent vertical nonaxis survivor must now satisfy simultaneously

\[
\boxed{
G_q=1,
\qquad
\partial_3\lambda=0,
}
\]

\[
\boxed{
\Delta(\partial_3\lambda_h)
=-\frac12\mathcal H_{333},
}
\]

\[
\boxed{
\left\langle\Pi_V^{prod}+\Pi_V^{rel}\right\rangle=0,
}
\]

and the exact label-weighted crossing bias

\[
\boxed{
\overline{
\int a\,\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)\,d\mu_0
}>0.
}
\]

The missing theorem is now a local-to-global axial STF covariance/transport relation, not an undefined sign heuristic.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
