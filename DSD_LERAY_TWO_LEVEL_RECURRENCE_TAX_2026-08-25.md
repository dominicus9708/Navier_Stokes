# DSD Leray two-level recurrence tax

Date: 2026-08-25

Status: **H0/H1 RECURRENT BALANCES COMBINED / COMMON-FREQUENCY SIMULTANEOUS VORTICITY-AND-STRAIN AMPLITUDE FLOORS PROVED / PASSIVE VELOCITY TAIL DOES NOT ENTER / NO CONTRADICTION YET / GLOBAL REGULARITY UNPROVED.**

This note combines

- `LERAY_RECURRENT_ENSTROPHY_STATISTICAL_BALANCE_2026-08-24.md`;
- `LERAY_H1_RECURRENCE_TAX_2026-08-20.md`;
- `RECURRENT_LOG_FREQUENCY_VISCOUS_GRONWALL_GATE_2026-08-24.md`;
- `DSD_CRITICAL_VELOCITY_TAIL_STRAIN_H2_DECOUPLING_2026-08-25.md`.

The goal is to impose the order-zero enstrophy recurrence tax and the order-one strain recurrence tax on the **same** recurrent Leray state.

## 1. Leray quantities

Let

\[
V(Y,s)
\]

be a smooth recurrent Leray trajectory, with

\[
W=\nabla\times V,
\qquad
\Sigma=\operatorname{sym}\nabla V.
\]

Define

\[
Z=\|W\|_2^2,
\qquad
Q=\|\nabla W\|_2^2,
\qquad
R=\|\Delta W\|_2^2.
\]

For the strain hierarchy define

\[
P=\|\nabla\Sigma\|_2^2,
\qquad
H=\|\Delta\Sigma\|_2^2.
\]

Fourier incompressibility gives the exact identities

\[
\boxed{
\|\Sigma\|_2^2=\frac12Z,
\qquad
P=\frac12Q,
\qquad
H=\frac12R.
}
\]

The same multiplier identity holds at every derivative order because differentiation commutes with the strain/vorticity Fourier relation.

## 2. H0 recurrent balance

The Leray vorticity identity is

\[
\frac12Z_s+\frac14Z+\nu Q=\mathcal P_0,
\]

where

\[
\mathcal P_0=\int W^T\Sigma W\,dY.
\]

For any long-time recurrent/invariant average for which the endpoint derivative vanishes,

\[
\boxed{
\overline{\mathcal P_0}
=\frac14\overline Z+\nu\overline Q.
}
\]

Status: **EXACT.**

## 3. H1 recurrent balance

The exact Leray strain-H1 identity is

\[
\frac12P_s+\frac34P+\nu H=N_1.
\]

Using `P=Q/2` and `H=R/2`,

\[
\frac14Q_s+\frac38Q+\frac\nu2R=N_1.
\]

Hence on the same recurrent average,

\[
\boxed{
\overline{N_1}
=\frac38\overline Q
+\frac\nu2\overline R.
}
\]

Status: **EXACT.**

The similarity tax has increased from the H0 coefficient `1/4` to the derivative-level coefficient `3/8` when expressed in vorticity variables.

## 4. A common mean frequency

Define

\[
\boxed{
\rho
:=\frac{\overline Q}{\overline Z}
}
\]

on a nonzero recurrent statistical state.

The recurrent active-core frequency result gives a positive lower floor

\[
\boxed{
\rho\ge c_{\log}>0
}
\]

whenever the previously established positive-density active-core windows and enstrophy ceiling are imported.

This `rho` is the common frequency parameter coupling the H0 and H1 recurrence taxes.

## 5. H0 forces a vorticity-amplitude floor

Let

\[
M(s):=\|W(s)\|_\infty
\]

and suppose

\[
M(s)\le M_+
\]

on the recurrent class.

The sharp trace-free stretching estimate is

\[
\boxed{
\mathcal P_0
\le\frac1{\sqrt3}MZ.
}
\]

Therefore

\[
\frac14\overline Z+\nu\overline Q
\le
\frac{M_+}{\sqrt3}\overline Z.
\]

Dividing by the positive `Zbar` gives

\[
\boxed{
M_+
\ge
\frac{\sqrt3}{4}
+\sqrt3\nu\rho.
}
\]

Using `rho>=c_log`,

\[
\boxed{
M_+
\ge
\frac{\sqrt3}{4}
+\sqrt3\nu c_{\log}.
}
\]

This is exactly the survivor-side complement of the trace-free ancient Gronwall certificate.

## 6. H1 forces an independent strain-amplitude floor

Let

\[
B(s):=\|\Sigma(s)\|_\infty
\]

and assume

\[
B(s)\le B_+.
\]

The exact vorticity-gradient non-normality representation and the Böttcher--Wenzel bound give

\[
\boxed{
N_1
\le
\sqrt2\,B P
=\frac{B}{\sqrt2}Q.
}
\]

Therefore the recurrent H1 balance implies

\[
\frac38\overline Q
+\frac\nu2\overline R
\le
\frac{B_+}{\sqrt2}\overline Q.
\]

Thus

\[
\boxed{
B_+
\ge
\frac{3\sqrt2}{8}
+\frac\nu{\sqrt2}
\frac{\overline R}{\overline Q}.
}
\]

## 7. Frequency interpolation raises the H1 floor

For every fixed time, Fourier Cauchy--Schwarz gives

\[
Q^2
\le ZR.
\]

Apply Cauchy--Schwarz in time to the recurrent average:

\[
\overline Q^2
\le
\overline Z\,\overline R.
\]

Hence

\[
\boxed{
\frac{\overline R}{\overline Q}
\ge
\frac{\overline Q}{\overline Z}
=\rho.
}
\]

Substitution gives the clean H1 amplitude floor

\[
\boxed{
B_+
\ge
\frac{3\sqrt2}{8}
+\frac\nu{\sqrt2}\rho.
}
\]

Therefore

\[
\boxed{
B_+
\ge
\frac{3\sqrt2}{8}
+\frac\nu{\sqrt2}c_{\log}.
}
\]

Numerically, before the frequency tax is inserted,

\[
\frac{3\sqrt2}{8}
\approx0.530330086.
\]

This recovers and sharpens the interpretation of the earlier class-level strain floor: it is tied directly to the **same mean frequency** that strengthens the H0 rigidity certificate.

## 8. Simultaneous two-level survivor condition

Every recurrent nonzero survivor on this branch must therefore satisfy both

\[
\boxed{
M_+
\ge
\frac{\sqrt3}{4}
+\sqrt3\nu c_{\log}
}
\]

and

\[
\boxed{
B_+
\ge
\frac{3\sqrt2}{8}
+\frac\nu{\sqrt2}c_{\log}.
}
\]

The first is a vorticity-amplitude requirement.

The second is a strain-amplitude requirement.

They are independent because there is no universal endpoint `L^infinity` Riesz-transform estimate identifying `B_+` with `M_+`.

Consequently DSD must retain them as two separate formed channels.

## 9. Why the passive non-L3 velocity tail does not pay these taxes

A `1/r` velocity tail has

\[
|\nabla U_T|\sim r^{-2}
\]

and becomes negligible in the strain `H2` topology as its onset radius tends to infinity.

The two recurrent balance taxes above are carried by the strain/vorticity derivative hierarchy, not by the low-frequency velocity `L3` defect itself.

Thus the passive tail cannot be counted as already satisfying the required H0/H1 production.

The active recurrent derivative state must supply the two taxes independently of the tail's global `L3` mass.

## 10. A two-level exclusion template

A future compact-class estimate that supplies simultaneous upper bounds

\[
M_+\le M_{class},
\qquad
B_+\le B_{class}
\]

excludes recurrent survival if either

\[
\boxed{
M_{class}
<
\frac{\sqrt3}{4}
+\sqrt3\nu c_{\log}
}
\]

or

\[
\boxed{
B_{class}
<
\frac{3\sqrt2}{8}
+\frac\nu{\sqrt2}c_{\log}.
}
\]

More importantly, any relation between the two class ceilings can exploit the fact that **both thresholds must be exceeded simultaneously**.

The endpoint-Riesz obstruction means that such a relation must use the actual compact/analytic class, not a false universal `||S||_infinity <= C||omega||_infinity` claim.

## 11. DSD audit

The recurrent survivor now has a finite hierarchy of distinct taxes:

\[
\boxed{
\text{H0 dilation tax}
\to
\text{positive mean frequency}
\to
\begin{cases}
\text{vorticity-amplitude floor},\\
\text{H1 strain-amplitude floor}.
\end{cases}
}
\]

This hierarchy prevents one large scalar norm from being used twice to discharge two different PDE obligations.

The next non-circular target is a compact-class **joint amplitude/production compatibility inequality**, or the existing stronger covariance/non-normality saturation route.

## 12. Audit verdict

### PROVED

- exact H0 and H1 recurrent mean balances on the same orbit;
- exact derivative identities `P=Q/2`, `H=R/2`;
- common mean-frequency variable `rho=Qbar/Zbar`;
- simultaneous vorticity and strain amplitude floors;
- both floors are strictly increased by the same positive recurrent frequency tax.

### NOT DERIVED

- a universal endpoint relation between `M_+` and `B_+`;
- a class upper bound violating either floor;
- LRMG;
- contradiction to the bounded-Z singular branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
