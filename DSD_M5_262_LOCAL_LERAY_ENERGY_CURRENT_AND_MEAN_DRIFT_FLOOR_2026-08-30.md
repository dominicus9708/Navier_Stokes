# DSD M5-262 — Local Leray Energy-Current Balance and Mean-Drift Floor

Date: 2026-08-30

Parent: `DSD_M5_261_STATIONARY_BERNOULLI_FLUX_TO_FINITE_DEPTH_VARIANCE_OR_MEAN_TURNOVER_2026-08-30.md`

Status: **EXACT LOCAL LERAY BALANCE / INVARIANT AVERAGING REMOVES THE TIME DERIVATIVES OF BOTH ABSOLUTE LOCAL ENERGY AND WEIGHTED-MEAN KINETIC ENERGY, BUT BACKWARD-LERAY ANTI-DAMPING REMAINS AS A REAL PAYER / ON A FIXED BALL WITH `R < pi sqrt(nu)`, POINCARE SHOWS THAT RELATIVE VARIANCE CANNOT BY ITSELF PAY A UNIFORM POSITIVE OUTWARD ENERGY-CURRENT FLOOR: THE LOCAL MEAN VELOCITY MUST HAVE A POSITIVE MEAN-SQUARE FLOOR / THIS REDUCES THE QUIET STATIONARY-TAIL BRANCH TO A FORMED MEAN-DRIFT/CENTER CORRIDOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. W1 Leray equation

Use the standard backward-Leray equation

\[
V_s-\nu\Delta V
+\frac12V
+\frac12(Y\cdot\nabla)V
+(V\cdot\nabla)V
+\nabla P=0,
\qquad
\nabla\cdot V=0.
\]

Fix a Euclidean ball

\[
B_R:=\{|Y|<R\}
\]

centered at the normalized singular/core point.

Define

\[
E_R(s):=\frac12\int_{B_R}|V|^2dY,
\]

\[
D_R(s):=\int_{B_R}|\nabla V|^2dY,
\]

and

\[
S_R(s):=\int_{\partial B_R}|V|^2dS.
\]

---

## 2. Instantaneous physical Navier--Stokes energy current

At each Leray time define the spatial Navier--Stokes energy current

\[
\boxed{
J_{NS}
:=
\left(P+\frac12|V|^2\right)V
-\nu\nabla\frac{|V|^2}{2}.
}
\]

Its outward flux through the fixed sphere is

\[
\boxed{
\mathfrak J_R(s)
:=
\int_{\partial B_R}J_{NS}\cdot n\,dS.
}
\]

This is the same instantaneous spatial flux functional used in the stationary-tail identity, evaluated now on the actual W1 state.

It is **not** by itself the full Leray local-energy flux because the similarity drift contributes additional terms.

---

## 3. Exact sharp-ball Leray local-energy identity

Pair the Leray equation with `V` on `B_R` and integrate by parts.

The linear amplitude/dilation term gives

\[
\int_{B_R}
\left(\frac12V+\frac12Y\cdot\nabla V\right)\cdot V
=
-\frac12E_R
+\frac R4S_R.
\]

The nonlinear, pressure, and viscous surface terms combine into `mathfrak J_R`.

Therefore

\[
\boxed{
E_R'
+\nu D_R
+\mathfrak J_R
+\frac R4S_R
-\frac12E_R
=0.
}
\]

Equivalently,

\[
\boxed{
E_R'
+\nu D_R
=
\frac12E_R
-\mathfrak J_R
-\frac R4S_R.
}
\]

The `+E_R/2` on the right is the local backward-Leray anti-damping payment.

---

## 4. Invariant recurrent average

On the compact W1 recurrent hull, `E_R` is a bounded continuous state observable. Hence for any invariant probability measure,

\[
\boxed{\langle E_R'\rangle=0.}
\]

Thus

\[
\boxed{
\nu\langle D_R\rangle
+\langle\mathfrak J_R\rangle
+\frac R4\langle S_R\rangle
=
\frac12\langle E_R\rangle.
}
\]

If M5-261 transfers a uniform positive current floor

\[
\mathfrak J_R(s)\ge j_R>0,
\]

then

\[
\boxed{
\frac12\langle E_R\rangle
\ge
j_R+\nu\langle D_R\rangle
+\frac R4\langle S_R\rangle.
}
\]

So the current must be supported by a genuine local kinetic reservoir.

---

## 5. Split absolute energy into relative variance and mean drift

Let

\[
M_R:=|B_R|=\frac{4\pi}{3}R^3,
\]

and define the ball mean

\[
\boxed{
m_R(s):=\fint_{B_R}V(Y,s)dY.}
\]

Define the relative variance energy

\[
\boxed{
\mathcal V_R(s)
:=
\frac12\int_{B_R}|V-m_R|^2dY.
}
\]

Then exactly

\[
\boxed{
E_R
=
\mathcal V_R
+\frac{M_R}{2}|m_R|^2.
}
\]

Therefore the invariant balance becomes

\[
\boxed{
\nu\langle D_R\rangle
+\langle\mathfrak J_R\rangle
+\frac R4\langle S_R\rangle
=
\frac12\langle\mathcal V_R\rangle
+\frac{M_R}{4}\langle|m_R|^2\rangle.
}
\]

The derivative of the mean kinetic energy does not appear after invariant averaging; only its **state amplitude** remains through the Leray anti-damping reservoir.

---

## 6. Ball Poincare bound

The Payne--Weinberger inequality on a ball of diameter `2R` gives

\[
\int_{B_R}|V-m_R|^2
\le
\frac{4R^2}{\pi^2}
\int_{B_R}|\nabla V|^2.
\]

Hence

\[
\boxed{
\mathcal V_R
\le
\frac{2R^2}{\pi^2}D_R.
}
\]

Insert this into the averaged balance:

\[
\nu\langle D_R\rangle
+\langle\mathfrak J_R\rangle
+\frac R4\langle S_R\rangle
\le
\frac{R^2}{\pi^2}\langle D_R\rangle
+\frac{M_R}{4}\langle|m_R|^2\rangle.
\]

Thus

\[
\boxed{
\frac{M_R}{4}\langle|m_R|^2\rangle
\ge
\langle\mathfrak J_R\rangle
+
\left(\nu-\frac{R^2}{\pi^2}\right)
\langle D_R\rangle
+
\frac R4\langle S_R\rangle.
}
\]

---

## 7. Mean-drift floor below the Poincare radius

If

\[
\boxed{R<\pi\sqrt\nu,}
\]

then

\[
\nu-\frac{R^2}{\pi^2}>0.
\]

For a positive inherited current floor

\[
\langle\mathfrak J_R\rangle\ge j_R>0,
\]

we obtain immediately

\[
\boxed{
\langle|m_R|^2\rangle
\ge
\frac{4j_R}{M_R}
=
\frac{3j_R}{\pi R^3}.
}
\]

The omitted dissipation and surface terms only strengthen this bound.

Thus a recurrent W1 state carrying the stationary-tail outward current cannot remain both

1. low relative variance/gradient;
2. and low local mean velocity.

---

## 8. Interpretation as a mean-drift corridor

The mean velocity `m_R` is a Galilean/translation-sensitive quantity. A persistent floor

\[
\langle|m_R|^2\rangle\ge m_*^2>0
\]

need not itself be a contradiction.

It represents a formed local drift channel.

The earlier dilation-adapted center equation has the schematic normalized form

\[
 a_s
=m_R+\frac b2a.
\]

Thus large `m_R` can be treated in two ways:

- the observation/core center follows it, producing center motion;
- the center does not follow it, producing relative material crossing through the shell.

This is the correct bridge to the no-T center/material framework.

---

## 9. Center-displacement firewall

The existing no-T quantity is the **net stage displacement**

\[
\mathfrak T_j
=
\frac{|X_{j+1}-X_j|}{r_j}.
\]

A mean-square velocity floor does not imply a large net displacement, because the mean direction may oscillate:

\[
\int_I|m|^2ds>0
\quad\not\Rightarrow\quad
\left|\int_Im\,ds\right|>0.
\]

Therefore

\[
\boxed{
\text{mean-drift floor}
\not\Rightarrow
\text{center-turnover displacement}
}
\]

without an additional direction/variation argument.

This prevents an invalid immediate closure of the stationary branch.

---

## 10. Correct next decomposition

If the center follows the local mean, define a dilation-compensated center path so that its derivative is proportional to the compensated mean velocity.

Then on any finite stage one has the exact temporal variance decomposition

\[
\int_I|m|^2ds
=
|I|\,|\bar m_I|^2
+
\int_I|m-\bar m_I|^2ds,
\]

where

\[
\bar m_I=|I|^{-1}\int_Imds.
\]

The first term is controlled by net center displacement.

The second term is temporal oscillation of the mean and, by one-dimensional Poincare, is controlled from below by mean acceleration / momentum-flux action.

Thus the correct future fork is

\[
\boxed{
\text{persistent mean drift}
\Longrightarrow
\text{net center displacement}
\lor
\text{mean-acceleration / momentum-boundary action}.
}
\]

---

## 11. DSD verdict

### PROVED

For every fixed ball,

\[
\boxed{
E_R'+\nu D_R+\mathfrak J_R+\frac R4S_R-\frac12E_R=0.
}
\]

On invariant averages and for `R<pi sqrt(nu)`, a positive outward-current floor implies

\[
\boxed{
\langle|m_R|^2\rangle
\ge\frac{3j_R}{\pi R^3}>0.
}
\]

### FIREWALL

Mean-square drift is not the same as net center displacement.

### UPDATED STATIONARY QUIET ENDPOINT

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
T_{var/bdry}
\lor
\text{persistent mean-drift corridor}.
}

### NEXT TARGET

Use the temporal mean decomposition and the weighted momentum equation to convert the persistent mean-drift corridor into

\[
T_{center-displacement}
\lor
T_{momentum-stress}.
\]

Then compare the first with the existing `C_T` no-T bound and the second with material/pressure/viscous boundary actions.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
