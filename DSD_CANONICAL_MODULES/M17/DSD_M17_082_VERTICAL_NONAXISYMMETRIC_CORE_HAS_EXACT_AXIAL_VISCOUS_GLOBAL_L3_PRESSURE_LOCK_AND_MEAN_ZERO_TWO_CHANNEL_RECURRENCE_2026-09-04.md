# DSD M17-082 — A vertical non-axisymmetric core has an exact axial viscous–global l=3 pressure lock and mean-zero two-channel recurrence

Date: 2026-09-04
Canonical ID: **M17-082**

Status: **INTERNAL VERTICAL RANK-1 GLOBAL PRESSURE-LOCKING GATE / ON THE VERTICAL NONCONFORMAL REGULAR CORE OF M17-015, `G_q=1` AND `partial_3 lambda=0`. EXTENDING THE REPEATED HORIZONTAL STRAIN BY `lambda_h=(Sigma_11+Sigma_22)/2` AND MATERIALLY DIFFERENTIATING `c_V=partial_3 lambda_h` WITH THE SIMILARITY STRAIN PDE GIVES, AT THE CORE, `0=D_B c_V=Delta c_V-(1/2)partial_3 Delta_h P`. THE PRESSURE SOURCE `S_P=|Sigma|^2-rho^2/2` HAS `partial_3 S_P=0` THERE, SO `partial_3 Delta_h P=-P_333` AND THEREFORE `Delta c_V=-(1/2)P_333`. BECAUSE THE TRACE CORRECTION IN `H=STF_3(nabla^3P)` IS PROPORTIONAL TO `grad S_P`, THE SAME AXIAL SOURCE STATIONARITY GIVES `H_333=P_333`. HENCE `Delta(partial_3 lambda_h)=-(1/2)H_333`. M17-053 IDENTIFIES `H` AS THE GLOBAL STF l=3 PRESSURE MOMENT WITH EXACT SOURCE-PRODUCTION PLUS RELATIVE-TRANSPORT DYNAMICS, SO ITS `333` PROJECTION GIVES `D_B V_V=-(1/2)(Pi_V^prod+Pi_V^rel)` FOR `V_V=Delta(partial_3 lambda_h)`. A UNIFORMLY RECURRENT COMPACT VERTICAL CORE THEREFORE REQUIRES `<Pi_V^prod+Pi_V^rel>=0`. THIS IS AN EXACT GLOBAL RECURRENCE OBLIGATION, NOT A SIGN CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vertical nonconformal core data

Use the fixed great-circle frame

\[
n=e_3,
\qquad
W_h=J\nabla_h q.
\]

For the vertical nonconformal regular nodal core, M17-015 gives

\[
\boxed{
G_q=1,
\qquad
\partial_3\lambda=0.
}
\]

At the core,

\[
\boxed{
\Sigma=\operatorname{diag}(\lambda,\lambda,-2\lambda),
\qquad
\Omega=0,
\qquad
W=0.
}
\]

Define the full horizontal repeated-strain scalar

\[
\boxed{
\lambda_h:=\frac12(\Sigma_{11}+\Sigma_{22})
}
\]

and its axial derivative

\[
\boxed{
c_V:=\partial_3\lambda_h.
}
\]

On the retained vertical nonconformal core,

\[
\boxed{c_V=0.}
\]

---

## 2. Similarity strain equation

M17-044 fixes the normalization

\[
D_B\Sigma
=\Delta\Sigma
-\Sigma
-\Sigma^2
-\Omega^2
-\nabla^2P,
\qquad
B=U+\frac12y.
\]

The material/spatial commutator is

\[
D_B(\partial_j f)
=\partial_j(D_B f)
-(\partial_jB_m)\partial_m f.
\]

For `j=3`, at the nodal core,

\[
\partial_3B_m
=(-2\lambda+\tfrac12)\delta_{m3}.
\]

Hence the commutator contribution to `D_B c_V` is proportional to `c_V` and vanishes on the retained branch.

---

## 3. Material persistence of axial stationarity

Take one axial derivative of the horizontal trace of the strain equation.
At the core:

- `c_V=0`;
- `Omega=0`, so `partial_3(Omega^2)=0`;
- `partial_3 tr_h Sigma=2c_V=0`;
- `partial_3 tr_h(Sigma^2)=4 lambda c_V=0`.

Therefore every lower-order local strain term vanishes and

\[
\boxed{
0=D_Bc_V
=\Delta c_V
-\frac12\partial_3\Delta_hP.
}
\]

Equivalently,

\[
\boxed{
\Delta(\partial_3\lambda_h)
=\frac12\partial_3\Delta_hP.
}
\]

This is the first vertical pressure–viscous lock.

---

## 4. Axial pressure-source stationarity

The pressure Poisson source is

\[
\boxed{
-\Delta P=S_P,
\qquad
S_P=|\Sigma|^2-\frac12\rho^2.
}
\]

At the nodal core `rho=0`.
Differentiate axially:

\[
\partial_3S_P
=2\Sigma:\partial_3\Sigma
-\rho\,\partial_3\rho.
\]

The vorticity term vanishes because `rho=0`.
For the strain term, incompressibility gives

\[
\partial_3\operatorname{tr}\Sigma=0,
\]

while `partial_3 lambda=0` gives

\[
\partial_3\Sigma_{11}+\partial_3\Sigma_{22}=0.
\]

Hence also `partial_3 Sigma_33=0`, and therefore

\[
\boxed{
\partial_3S_P=0.
}
\]

Thus

\[
\partial_3\Delta P
=-\partial_3S_P
=0.
\]

Since

\[
\Delta_hP=\Delta P-P_{33},
\]

we get

\[
\boxed{
\partial_3\Delta_hP
=-P_{333}.
}
\]

Substitution into Section 3 yields

\[
\boxed{
\Delta(\partial_3\lambda_h)
=-\frac12P_{333}.
}
\]

---

## 5. The pressure third jet is purely STF in the axial channel

M17-053 defines

\[
\boxed{
\mathcal H
:=STF_3(\nabla^3P)
}
\]

with

\[
\mathcal H_{ijk}
=P_{ijk}
+\frac15\left(
\delta_{ij}\partial_kS_P
+\delta_{ik}\partial_jS_P
+\delta_{jk}\partial_iS_P
\right).
\]

For the axial component,

\[
\mathcal H_{333}
=P_{333}+\frac35\partial_3S_P.
\]

But Section 4 gives `partial_3 S_P=0`, hence

\[
\boxed{
\mathcal H_{333}=P_{333}.
}
\]

Therefore the vertical pressure–viscous lock is exactly

\[
\boxed{
\Delta(\partial_3\lambda_h)
=-\frac12\mathcal H_{333}.
}
\]

Define

\[
\boxed{
V_V:=\Delta(\partial_3\lambda_h),
\qquad
H_V:=\mathcal H_{333}.
}
\]

Then

\[
\boxed{H_V=-2V_V.}
\]

---

## 6. This is a global l=3 lock, not a local free coefficient

M17-053 identifies `mathcal H` distributionally as the pressure source paired with the STF third-derivative Newtonian kernel:

\[
\mathcal H_{ijk}(Y)
=\langle S_P,\mathcal K_{ijk}(Y-\cdot)\rangle.
\]

Thus

\[
\boxed{
H_V(Y)
=\langle S_P,\mathcal K_{333}(Y-\cdot)\rangle.
}
\]

The axial pressure third jet required by vertical persistence is therefore one coordinate of the same global seven-dimensional `l=3` pressure state already used in the slanted DSAIG analysis.

No new independent harmonic degree of freedom has been introduced.

---

## 7. Exact two-channel transport

M17-053 gives, along a material core center `Y'=B(Y)`,

\[
\boxed{
\mathcal D_Y\mathcal H
=\mathscr P^{(3)}+\mathscr R^{(3)}.
}
\]

Because the great-circle frame is fixed, `e_3` is fixed.
Define the axial scalar channels

\[
\boxed{
\Pi_V^{prod}
:=e_3^{\otimes3}:\mathscr P^{(3)},
}
\]

\[
\boxed{
\Pi_V^{rel}
:=e_3^{\otimes3}:\mathscr R^{(3)}.
}
\]

Then

\[
\boxed{
D_BH_V
=\Pi_V^{prod}+\Pi_V^{rel}.
}
\]

Since `H_V=-2V_V`,

\[
\boxed{
D_BV_V
=-\frac12\left(
\Pi_V^{prod}+\Pi_V^{rel}
\right).
}
\]

This is the canonical vertical `l=3` pressure-locking transport law.

---

## 8. Recurrent mean-zero gate

Assume the marked vertical nonconformal core remains on a uniformly regular compact recurrent branch and `V_V` stays bounded.
Then along recurrence intervals

\[
\frac{V_V(T)-V_V(0)}{T}\to0.
\]

Therefore

\[
\boxed{
\left\langle
\Pi_V^{prod}+\Pi_V^{rel}
\right\rangle
=0.
}
\]

Equivalently,

\[
\boxed{
\langle\Pi_V^{prod}\rangle
=-\langle\Pi_V^{rel}\rangle.
}
\]

The vertical branch therefore carries the same physical two-channel global pressure architecture as M17-054, but there is no slant-amplitude multiplier to normalize away.

---

## 9. Comparison with the slanted l=3 law

For the slanted branch M17-054 uses

\[
m_3=M_3/|p|
\]

because

\[
D_B|p|=3\lambda|p|.
\]

The vertical branch has `p=0`, so that normalization is undefined and must not be taken by a limiting argument.

Instead the independent vertical condition `partial_3 lambda=0` produces the scalar `V_V` directly.

Thus

\[
\boxed{
R_{1,V}^{nonconf}
\not\equiv
\lim_{p\to0}R_{1,S}^{slant}.
}
\]

Nevertheless both branches couple to coordinates of the same global STF `l=3` pressure tensor and the same two physical source channels.

---

## 10. DSD analysis

The descriptor chain is now

\[
\boxed{
\text{vertical shape incompatibility}
\to
G_q=1,\ \partial_3\lambda=0
\to
V_V=\Delta\partial_3\lambda_h
\to
H_V=\mathcal H_{333}
\to
(\Pi_V^{prod},\Pi_V^{rel}).
}
\]

This closes the previous local/global descriptor gap for the vertical nonconformal branch.

The local axial strain-stationarity condition is not self-contained: its persistence is paid by one global `l=3` pressure coordinate.

---

## 11. DSD audit

### Audit A — taking the slant limit
Rejected. `p=0` is a material subclass and the M17-054 normalization by `|p|` is unavailable there.

### Audit B — dropping the material/spatial commutator
Avoided. Its axial contribution is proportional to `c_V` and vanishes only after imposing the retained vertical branch condition.

### Audit C — assuming the pressure third jet is STF automatically
Rejected in general. It becomes purely STF in the `333` component here only because `partial_3S_P=0` is derived at the vertical core.

### Audit D — treating `mathcal H_333` as local
Rejected. M17-053 identifies it with a global STF Newtonian source moment.

### Audit E — assigning a sign to the two-channel forcing
Rejected. Both source production and relative transport are signed.

### Audit F — extending to the conformal vertical core
Rejected. The derivation uses M17-015's nonconformal consequence `G_q=1` and `partial_3 lambda=0`. The conformal positive-index vertical branch remains separate.

### Audit G — proof status
No contradiction is obtained. The vertical branch receives a new exact global recurrence obligation.

---

## 12. Updated vertical Rank-1 frontier

The nonconformal vertical survivor must now satisfy simultaneously

\[
\boxed{
\begin{aligned}
G_q&=1,\\
\partial_3\lambda&=0,\\
\Delta(\partial_3\lambda_h)&=-\frac12\mathcal H_{333},\\
D_BV_V&=-\frac12(\Pi_V^{prod}+\Pi_V^{rel}),\\
\left\langle\Pi_V^{prod}+\Pi_V^{rel}\right\rangle&=0,
\end{aligned}
}
\]

in addition to the earlier nodal mean, positive-sheath/negative-payer, angular-defect, and label-area hysteresis constraints.

The conformal positive-index vertical branch remains

\[
\boxed{
G_{conf+}^{vertical}
\Longrightarrow
G_{axis/no\text{-}swirl}
\lor
A_{high\text{-}jet}^{nonaxis}.
}
\]

and requires a separate higher-angular-jet audit.

---

## 13. Next target — vertical conformal high-jet audit

The highest-value remaining Rank-1 vertical question is the non-axisymmetric conformal core:

\[
Q=cI,
\qquad
\chi=\mathcal Lq\neq0,
\qquad
\operatorname{ord}_\Gamma\chi\ge3.
\]

M17-016--023 already force finite angular jet order, negative-`kappa` payer geometry, and lobe turnover.
The next calculation should derive the exact material multiplier of the first nonzero angular jet and determine whether a recurrent high-jet conformal core has an additional mean-`kappa` resonance incompatible with its payer cycle, or instead remains a regular firewall-like survivor.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
