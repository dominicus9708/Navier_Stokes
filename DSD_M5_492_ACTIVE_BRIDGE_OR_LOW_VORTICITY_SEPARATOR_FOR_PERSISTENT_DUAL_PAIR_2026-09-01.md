# DSD M5-492 — Persistent dual pair forces an active-direction bridge or a low-vorticity separator

Date: 2026-09-01

Status: **GEOMETRIC DICHOTOMY / THE M5-490 RECURRENT NONCOLLINEAR DUAL-FLUX PAIR CANNOT BE TREATED AS TWO ISOLATED POINT DIRECTIONS / STAGE-WIDE ANALYTICITY THICKENS EACH ACTIVE CARRIER TO A FIXED BALL / INSIDE A FIXED OBSERVATION REGION, EITHER THE TWO CARRIER BALLS ARE JOINED THROUGH AN ACTIVE SUPERLEVEL CORRIDOR OF UNIFORMLY POSITIVE CAPACITY, IN WHICH CASE THE VORTICITY-DIRECTION DIRICHLET ENERGY HAS A FIXED LOWER BOUND; OR THE ACTIVE SUPERLEVEL SET DISCONNECTS THE TWO CARRIERS, IN WHICH CASE RELATIVE ISOPERIMETRY AND COAREA FORCE A FIXED VORTICITY-MAGNITUDE GRADIENT COST ACROSS A LOW-VORTICITY SEPARATOR / IN BOTH CASES THE DUAL EVENT PAYS A FIXED LOCAL PALINSTROPHY CHARGE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-490--491

Fix one recurrent dual-pair event in similarity variables.

Let

\[
W=\rho\xi,
\qquad
\rho=|W|,
\qquad
|\xi|=1
\]

on the active set.

M5-490 gives two persistent material-flux carriers `A` and `B` inside a fixed bounded normalized observation region `B_R`, carrying fixed flux and a fixed noncollinearity mark.

After passing from the carrier axes to fixed interior carrier points and shrinking constants harmlessly, there are constants

\[
r_0>0,
\qquad
\rho_0>0,
\qquad
\alpha_0>0
\]

such that on two disjoint balls

\[
B_A:=B_{r_0}(x_A),
\qquad
B_B:=B_{r_0}(x_B)
\]

one has

\[
\boxed{
\rho\ge\rho_0
}
\]

and representative directions `e_A,e_B` satisfying

\[
\boxed{
\angle(e_A,e_B)\ge\alpha_0.
}
\]

The fixed carrier radius follows from the M5-392 stage-wide first-hitting analyticity/derivative bound before passage to the compact hull.

---

## 2. Palinstrophy decomposition

On the active set,

\[
\boxed{
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Thus a dual event may pay palinstrophy through either

1. direction variation while vorticity remains active; or
2. magnitude variation through a low-vorticity separator.

M5-492 makes this split quantitative.

---

## 3. Choose an active threshold

Fix

\[
0<\rho_s<\rho_0.
\]

Define the active superlevel set inside the observation ball

\[
\mathcal A_s
:=
\{x\in B_R:\rho(x)>\rho_s\}.
\]

There are two cases.

---

## 4. Case I — active bridge of positive capacity

Suppose there is a connected active corridor `Omega_b subset mathcal A_s` joining fixed subballs

\[
B_A'\Subset B_A,
\qquad
B_B'\Subset B_B
\]

and having uniformly positive condenser capacity

\[
\boxed{
\operatorname{Cap}_{\Omega_b}(B_A',B_B')
\ge c_{cap}>0.
}
\]

A fixed-radius tube of bounded length is a sufficient, but not necessary, geometric realization of this condition.

Let `f` be any scalar projection of `xi` in a direction chosen so that the two endpoint direction neighborhoods differ by a fixed amount.

Because

\[
\angle(e_A,e_B)\ge\alpha_0,
\]

one can choose a unit vector `q` and a fixed number `d_0=d_0(alpha_0)>0` such that

\[
q\cdot\xi\ge c_A
\]

on `B_A'` and

\[
q\cdot\xi\le c_A-d_0
\]

on `B_B'`, after shrinking the carrier balls using the fixed derivative bound.

Set

\[
f:=q\cdot\xi.
\]

The condenser-capacity variational inequality gives

\[
\boxed{
\int_{\Omega_b}|\nabla f|^2dx
\ge
c_{cap}d_0^2.
}
\]

Since

\[
|\nabla f|\le|\nabla\xi|
\]

and

\[
\rho\ge\rho_s
\]

throughout the active corridor,

\[
\boxed{
\int_{\Omega_b}
\rho^2|\nabla\xi|^2dx
\ge
\rho_s^2c_{cap}d_0^2
=:p_{dir}>0.
}
\]

Therefore an active bridge pays a fixed direction-palinstrophy charge.

---

## 5. Equivalent tube estimate

If the bridge contains a family of active curves of length at most `L_b` filling a transverse area at least `A_b>0`, the same conclusion can be seen directly.

For one connecting curve `gamma`,

\[
|\xi(B)-\xi(A)|
\le
\int_\gamma|\partial_s\xi|ds.
\]

Since

\[
|e_A-e_B|
=2\sin\frac{\angle(e_A,e_B)}2
\ge2\sin\frac{\alpha_0}2,
\]

Cauchy--Schwarz gives

\[
\int_\gamma|\partial_s\xi|^2ds
\ge
\frac{4\sin^2(\alpha_0/2)}{L_b}
\]

up to the fixed endpoint-neighborhood loss.

Integrating over the transverse curve family yields

\[
\int_{\Omega_b}ho^2|\nabla\xi|^2dx
\ge
c(\rho_s,\alpha_0,A_b,L_b)>0.
\]

This is the geometric form of the capacity argument.

---

## 6. Case II — low-vorticity separator

Suppose no component of `mathcal A_s` contains both carrier balls.

Let `C_t` denote, for every regular value

\[
t\in[\rho_s,\rho_1]
\]

with some fixed `rho_1<rho_0`, the component of

\[
\{\rho>t\}\cap B_R
\]

containing `B_A'`.

Because `B_A'` and `B_B'` both lie in the higher-amplitude region while they are disconnected already at level `rho_s`, one has uniformly

\[
|C_t|\ge |B_A'|=:v_0>0
\]

and

\[
|B_R\setminus C_t|
\ge |B_B'|=:v_0>0.
\]

The relative isoperimetric inequality in the fixed ball `B_R` therefore gives

\[
\boxed{
\operatorname{Per}(C_t;B_R)
\ge c_{iso}(R,v_0)>0
}
\]

for almost every

\[
t\in[\rho_s,\rho_1].
\]

---

## 7. Coarea forces magnitude-gradient charge

Apply the coarea formula to `rho` on the transition set

\[
\mathcal S
:=
\{\rho_s<\rho<\rho_1\}\cap B_R.
\]

Then

\[
\int_{\mathcal S}|\nabla\rho|dx
=
\int_{\rho_s}^{\rho_1}
\mathcal H^2(\{\rho=t\}\cap B_R)dt.
\]

The separating component boundary contributes at least its relative perimeter, hence

\[
\boxed{
\int_{\mathcal S}|\nabla\rho|dx
\ge
c_{iso}(\rho_1-\rho_s).
}
\]

Since `mathcal S subset B_R` has uniformly bounded volume, Cauchy--Schwarz gives

\[
\boxed{
\int_{\mathcal S}|\nabla\rho|^2dx
\ge
\frac{c_{iso}^2(\rho_1-\rho_s)^2}{|B_R|}
=:p_{mag}>0.
}
\]

Thus a low-vorticity separator pays a fixed magnitude-palinstrophy charge.

---

## 8. Exact dual-event palinstrophy dichotomy

Combining the two cases with

\[
|\nabla W|^2
=
|\nabla\rho|^2+ho^2|\nabla\xi|^2,
\]

one obtains

\[
\boxed{
\int_{B_R}|\nabla W|^2dx
\ge
p_*
:=
\min(p_{dir},p_{mag})>0
}
\]

at every retained noncollinear dual-pair event satisfying the compact carrier geometry.

Equivalently,

\[
\boxed{
\text{persistent noncollinear dual event}
\Longrightarrow
P_{bridge}^{dir}
\lor
P_{separator}^{mag}
}
\]

with a fixed quantitative charge in either branch.

---

## 9. DSD interpretation

The two carrier directions are not merely two labels.

To be simultaneously representable in one bounded smooth vorticity field they must be related through one of two formation mechanisms.

### Active internal relation

The active vorticity set itself connects them, forcing a nonzero direction-gradient cost.

### Boundary/separator relation

The active set splits, and the transition between active components is encoded in the vorticity magnitude, forcing a nonzero magnitude-gradient cost.

Thus the apparently qualitative distinction

\[
\text{connected versus separated dual source}
\]

is converted into the same quantitative palinstrophy ledger.

---

## 10. Firewall

This result does **not** prove that one arbitrarily chosen one-dimensional path between the carriers gives a three-dimensional energy lower bound.

The active-bridge branch requires positive condenser capacity, equivalently a nondegenerate family of connecting paths or another uniform-connectivity condition.

If active connectivity survives only through necks whose capacity tends to zero, that degeneration belongs to the separator/capacity-collapse side and must be retained as such rather than silently treated as a thick bridge.

The result also does not identify the separator with a material surface. It is a geometric vorticity-superlevel separator at the observed similarity time.

---

## 11. Highest-value next target

M5-490 gives positive-frequency recurrence of one persistent noncollinear pair. M5-492 therefore suggests summing the fixed charge over those recurrent dual events.

The next audit is:

\[
\boxed{
\text{positive-frequency dual pair}
\Longrightarrow
\text{positive mean similarity palinstrophy}.
}
\]

Then compare that lower mean with the exact M5-486 similarity-enstrophy balance

\[
\frac14\langle E\rangle+
\langle P\rangle
=
\langle Q\rangle.
\]

One must then determine whether the extra palinstrophy burden can be paid indefinitely by the axial stretching channel or whether dual-source geometry quantitatively depletes that production.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
