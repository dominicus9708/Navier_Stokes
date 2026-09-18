# M19-436 — The terminal harmonic pressure dipole is an exact q-coboundary in the Hardy-excess ledger and contributes zero invariant-mean payment

Date: 2026-09-19  
Canonical ID: **M19-436**  
Status: **EXACT TERMINAL DIPOLE CANCELLATION / THE q-INVARIANT l=1 HARMONIC PRESSURE DIPOLE CONTRIBUTES TO BOTH BERNOULLI SORTING AND THE FIRST-JET RESIDUAL CORRELATION, BUT THE TWO CONTRIBUTIONS SUM TO AN EXACT q-DERIVATIVE / ITS INVARIANT-MEAN CONTRIBUTION TO THE M19-423 HARDY-EXCESS IDENTITY IS ZERO / THE DIPOLE IS A REAL FACTOR VARIABLE BUT NOT AN INDEPENDENT ENERGY PAYER / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Terminal dipole decomposition

At the terminal boundary, let the realized harmonic pressure dipole be

\[
\boxed{
P_{dip}(\omega)
=
a_*\cdot\omega,
}
\]

with the q-invariant component-wide vector \(a_*\) from M19-434.

Its pressure-gradient contribution to the first terminal residual is

\[
\boxed{
C_{dip}
=
\mathfrak G_2P_{dip}
=
W_{a_*}
=
a_*-3(a_*\cdot\omega)\omega.
}
\]

Write

\[
P=P_{dip}+P_{rem},
\]

and correspondingly separate only this explicit pressure-gradient contribution from the residual:

\[
C=C_{dip}+C_{rem}.
\]

## 2. Radial first moment of the leading velocity

Define

\[
\boxed{
M_A(q)
:=
\int_{S^2}
A_r(q,\omega)\,\omega,d\omega.
}
\]

Also define the tangential mean

\[
T_A(q)
:=
\int_{S^2}A_T(q,\omega)d\omega
\]

and total spherical mean

\[
N_A(q)
:=
\int_{S^2}A(q,\omega)d\omega
=
M_A+T_A.
\]

## 3. Leading incompressibility moment identity

The degree-minus-one divergence condition is

\[
\boxed{
(\partial_q+1)A_r
+
\operatorname{div}_{S^2}A_T
=
0.
}
\]

Multiply by \(\omega\) and integrate over the sphere.

Using

\[
\int_{S^2}
\omega\,
\operatorname{div}_{S^2}A_T
,d\omega
=
-
\int_{S^2}A_Td\omega
=
-T_A,
\]

we obtain

\[
M_A'+M_A-T_A=0.
\]

Therefore

\[
\boxed{
T_A=M_A'+M_A,
}
\]

and hence

\[
\boxed{
N_A=M_A'+2M_A.
}
\]

## 4. Bernoulli pressure-dipole contribution

The dipole contribution to the Bernoulli radial covariance is

\[
\Gamma_{P,dip}
:=
\int_{S^2}
P_{dip}A_r,d\omega.
\]

Therefore

\[
\boxed{
\Gamma_{P,dip}
=
a_*\cdot M_A.
}
\]

The subtraction of the spherical mean of \(P_{dip}\) does nothing because

\[
\int_{S^2}P_{dip}d\omega=0.
\]

## 5. Residual-correlation dipole contribution

Now pair the leading velocity with the dipole acceleration:

\[
\begin{aligned}
\int_{S^2}
A\cdot C_{dip}
,d\omega
&=
\int A\cdot
\left[
a_*-3(a_*\cdot\omega)\omega
\right]
d\omega
\\
&=
a_*\cdot N_A
-
3a_*\cdot M_A.
\end{aligned}
\]

Insert

\[
N_A=M_A'+2M_A.
\]

Then

\[
\boxed{
\int A\cdot C_{dip}
=
a_*\cdot(M_A'-M_A).
}
\]

## 6. Exact pointwise coboundary cancellation

Add the Bernoulli and residual contributions:

\[
\begin{aligned}
\Gamma_{P,dip}
+
\int A\cdot C_{dip}
&=
a_*\cdot M_A
+
a_*\cdot(M_A'-M_A)
\\
&=
a_*\cdot M_A'.
\end{aligned}
\]

Since \(a_*\) is q-independent,

\[
\boxed{
\Gamma_{P,dip}
+
\int A\cdot C_{dip}
=
\frac d{dq}
\left(
a_*\cdot M_A
\right).
}
\]

Thus the harmonic pressure dipole is an exact q-coboundary in the terminal Hardy-excess ledger.

## 7. Invariant mean vanishes exactly

On the compact recurrent terminal hull, \(M_A\) is bounded.

Therefore

\[
\left\langle
\frac d{dq}
(a_*\cdot M_A)
\right\rangle
=
0.
\]

Hence

\[
\boxed{
\left\langle
\Gamma_{P,dip}
\right\rangle
+
\left\langle
\int A\cdot C_{dip}
\right\rangle
=
0.
}
\]

The pressure dipole may contribute positively to one term and negatively to the other, but it carries no net invariant Hardy-excess payment.

## 8. Dipole-free master identity

M19-423 gives

\[
\mathcal H_A
=
\langle\Gamma_K\rangle
+
\langle\Gamma_P\rangle
+
\left\langle
\int A\cdot C
\right\rangle.
\]

Split off the dipole pair.

Using Section 7,

\[
\boxed{
\mathcal H_A
=
\langle\Gamma_K\rangle
+
\langle\Gamma_{P,rem}\rangle
+
\left\langle
\int A\cdot C_{rem}
\right\rangle.
}
\]

Therefore the terminal energy proof tree may quotient out the entire harmonic \(l=1\) pressure-dipole sector.

## 9. Correction to the pressure-gradient master branch

M19-425 routed a positive pressure-sorting payment to a tangential pressure-gradient floor.

That statement remains algebraically correct for total pressure.

But after M19-436, the energy-relevant pressure branch should be interpreted modulo the harmonic dipole:

\[
\boxed{
P_{tan}^{critical}
\rightsquigarrow
P_{tan,rem}^{critical}
}
\]

where the explicit q-invariant \(l=1\) harmonic dipole is removed before counting the payer.

The dipole is a real pressure factor, but not an independent source of positive Hardy excess.

## 10. Relation to the M19-433--435 firewall

M19-433--435 show that the harmonic pressure dipole is invisible to vorticity and survives as a finite-dimensional pressure/momentum sector.

M19-436 adds:

\[
\boxed{
\text{vorticity-invisible dipole}
\quad\text{is also invariant-energy neutral at the terminal ledger level}.
}
\]

Thus the dipole can obstruct a curl-only observability theorem without itself paying the positive terminal variation budget.

This distinction is important.

## 11. Strategic consequence

For the terminal hard core, one may work with the quotient

\[
\boxed{
(P,C)
\mod
\mathcal D_{dip},
}
\]

where \(\mathcal D_{dip}\) is the three-dimensional harmonic pressure-dipole/gradient sector.

The positive Hardy-excess identity survives unchanged on the quotient.

Therefore any attempt to turn positive \(\mathcal H_A\) into a pressure or residual payer should use only the dipole-free remainder.

## 12. Next target

At finite wedge depth, the dipole coefficient may evolve as the three-dimensional physical-time cocycle from M19-435.

The terminal q-coboundary cancellation suggests that its full wedge contribution may likewise enter the q-z energy ledger as a boundary/transport derivative rather than a true source.

The next calculation should derive the finite-depth analogue and determine whether the dipole cocycle can be completely isolated as a conservative transport term on the compact corridor.

\[
\boxed{\text{M19-436 COMPLETE; THE TERMINAL HARMONIC PRESSURE DIPOLE IS A q-COBOUNDARY AND HAS ZERO INVARIANT-MEAN HARDY-EXCESS PAYMENT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
