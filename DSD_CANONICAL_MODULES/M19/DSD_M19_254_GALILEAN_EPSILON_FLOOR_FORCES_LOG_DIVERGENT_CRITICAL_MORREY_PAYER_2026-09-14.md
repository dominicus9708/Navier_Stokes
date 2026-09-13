# DSD M19-254 — Galilean epsilon floor forces a logarithmically divergent critical Morrey payer

Date: 2026-09-14
Status: VALID NECESSARY CONDITION + NO-GO FOR NAIVE UNWEIGHTED SUMMABILITY; NOT A CLOSURE THEOREM
Parent: M19-253

## 0. Goal

M19-253 established the exact Galilean reformulation

\[
\mathcal T_{GMS}^{\varepsilon}:
\quad z_0\text{ singular}
\Longrightarrow
C_V(r)+D_V(r)\ge\varepsilon_*
\]

for every constant velocity \(V\) and every sufficiently small \(r\).

The purpose of M19-254 is to identify the actual scale-by-scale payer forced by this floor and to test whether the ordinary finite-energy spacetime integrability already contradicts it.

It does not. However, integrating the normalized floor over logarithmic scale forces a stronger **weighted critical divergence** at the singular point.

---

## 1. Finite-energy spacetime currencies

For a finite-energy whole-space solution on a finite time interval,

\[
u\in L_t^\infty L_x^2\cap L_t^2\dot H_x^1.
\]

Sobolev and interpolation give

\[
\boxed{u\in L_{x,t}^{10/3}}.
\]

Indeed, at each time,

\[
\|u(t)\|_{10/3}^{10/3}
\le C\|u(t)\|_2^{4/3}\|u(t)\|_6^2
\le C\|u(t)\|_2^{4/3}\|\nabla u(t)\|_2^2,
\]

and time integration is finite.

For the canonical whole-space pressure,

\[
-\Delta p=\partial_i\partial_j(u_i u_j),
\]

Calderón--Zygmund/Riesz-transform boundedness gives

\[
\boxed{p\in L_{x,t}^{5/3}}.
\]

These facts alone are supercritical with respect to point concentration and therefore are not expected to close the singularity problem.

---

## 2. Convert the epsilon floor to higher-integrability cost

Fix a constant Galilean velocity \(V\), a putative singular point \(z_0=(x_0,t_0)\), and

\[
Q_r^V(z_0)
=
\{t_0-r^2<t<t_0,\ |x-x_0-V(t-t_0)|<r\}.
\]

Write

\[
a_V(r)=\int_{Q_r^V}|u-V|^3,
\]

\[
b_V(r)=\int_{Q_r^V}|p-(p)_{B_r^V(t)}|^{3/2}.
\]

M19-253 gives

\[
a_V(r)+b_V(r)\ge\varepsilon_* r^2.
\]

Hence at least one of

\[
a_V(r)\ge\frac{\varepsilon_*}{2}r^2,
\qquad
b_V(r)\ge\frac{\varepsilon_*}{2}r^2
\]

holds.

The spacetime volume satisfies

\[
|Q_r^V|=c_Q r^5.
\]

### 2.1 Velocity branch

Hölder gives

\[
a_V(r)
\le
\left(\int_{Q_r^V}|u-V|^{10/3}\right)^{9/10}
|Q_r^V|^{1/10}.
\]

Therefore, if the velocity branch pays,

\[
\boxed{
\int_{Q_r^V}|u-V|^{10/3}
\ge
c\varepsilon_*^{10/9}r^{5/3}.
}
\]

### 2.2 Pressure branch

Likewise,

\[
b_V(r)
\le
\left(\int_{Q_r^V}|p-(p)_{B_r^V(t)}|^{5/3}\right)^{9/10}
|Q_r^V|^{1/10},
\]

so the pressure branch yields

\[
\int_{Q_r^V}|p-(p)_{B_r^V(t)}|^{5/3}
\ge
c\varepsilon_*^{10/9}r^{5/3}.
\]

For \(q=5/3\), Jensen and the triangle inequality imply

\[
\int_{B_r}|p-(p)_{B_r}|^q
\le C_q\int_{B_r}|p|^q.
\]

Thus

\[
\boxed{
\int_{Q_r^V}|p|^{5/3}
\ge
c\varepsilon_*^{10/9}r^{5/3}
}
\]

whenever the pressure branch pays.

### 2.3 Combined normalized payer

In either case,

\[
\boxed{
F_V(r):=
\int_{Q_r^V}
\left(|u-V|^{10/3}+|p|^{5/3}\right)
\ge
c\varepsilon_*^{10/9}r^{5/3}.
}
\]

Equivalently,

\[
\boxed{
H_V(r):=r^{-5/3}F_V(r)
\ge c\varepsilon_*^{10/9}
}
\]

for every sufficiently small \(r\) and every fixed constant \(V\).

This is a genuine scale-invariant payer.

---

## 3. NO-GO: ordinary unweighted integrability does not contradict the payer

At dyadic radii \(r_n=2^{-n}r_0\), the physical cost required by the epsilon floor is only

\[
F_V(r_n)\gtrsim r_n^{5/3}.
\]

The geometric series

\[
\sum_n r_n^{5/3}<\infty.
\]

Moreover, the cylinders \(Q_{r_n}^V\) are nested. A single central concentration can pay the lower bound at many scales simultaneously; lower bounds on nested cylinders do not provide lower bounds on the disjoint parabolic rings.

Therefore

\[
\boxed{
L^{10/3}_{x,t}\text{ velocity integrability}
+
L^{5/3}_{x,t}\text{ pressure integrability}
\not\Rightarrow
\mathcal T_{GMS}^{select}.
}
\]

Even a hypothetical annular nonreuse rule at the natural \(r^{5/3}\) physical cost would still have a geometrically summable total. A stronger scale-normalized or weighted mechanism is required.

This is the M19-254 NO-GO.

---

## 4. Logarithmic scale integration exposes the true non-summable payer

Although \(F_V(r)\) itself decays like \(r^{5/3}\), the normalized quantity \(H_V(r)\) has a positive floor at every small scale. Hence

\[
\boxed{
\int_0^{r_0}H_V(r)\,\frac{dr}{r}=\infty.
}
\]

Define the backward parabolic distance to the moving Galilean centerline

\[
\rho_V(x,t)
=
\max\left(
|x-x_0-V(t-t_0)|,
\sqrt{t_0-t}
\right).
\]

Then \((x,t)\in Q_r^V(z_0)\) exactly when \(\rho_V(x,t)<r\). Therefore, by Tonelli,

\[
\begin{aligned}
\int_0^{r_0}r^{-5/3}F_V(r)\frac{dr}{r}
&=
\int_{Q_{r_0}^V}
\left(|u-V|^{10/3}+|p|^{5/3}\right)
\left(\int_{\rho_V}^{r_0}r^{-8/3}dr\right)dxdt\\
&=
\frac35
\int_{Q_{r_0}^V}
\left(|u-V|^{10/3}+|p|^{5/3}\right)
\left(\rho_V^{-5/3}-r_0^{-5/3}\right)dxdt.
\end{aligned}
\]

Since the left-hand side diverges while the unweighted \(F_V(r_0)\) is finite, we obtain the necessary condition

\[
\boxed{
\int_{Q_{r_0}^V(z_0)}
\frac{|u-V|^{10/3}+|p|^{5/3}}
{\rho_V(x,t)^{5/3}}
\,dxdt
=\infty
}
\]

for every fixed constant \(V\), at every genuine singular point.

We name this

\[
\boxed{\mathcal P_{GMS}^{log}}.
\]

It is scale invariant under the Navier--Stokes scaling and is the first non-summable whole-space payer extracted from the transparent moving-sphere/Galilean reformulation.

---

## 5. Interpretation

M19-253 asked for a good scale/frame with subcritical \(C_V+D_V\). M19-254 shows exactly what blocks that selection:

\[
\boxed{
\text{a singularity must sustain a logarithmically nonintegrable critical concentration
around every constant Galilean centerline}.}
\]

Thus the next problem is no longer the vague statement "make the local norm small." It is the sharper question:

\[
\boxed{
\text{Can the already certified DSD ancestry/dissipation ledgers permit }\mathcal P_{GMS}^{log}?
}
\]

If an existing whole-space weighted ledger forces the above integral to be finite for at least one admissible \(V\), then the singular point is impossible.

If not, \(\mathcal P_{GMS}^{log}\) itself becomes the explicit survivor/payer that must be propagated into the root tree.

---

## 6. New firewalls

\[
\boxed{
\text{positive scale-invariant epsilon floor}
\not\Rightarrow
\text{divergent unweighted physical cost}.}
\]

\[
\boxed{
\text{nested-scale lower bounds}
\not\Rightarrow
\text{disjoint-annulus lower bounds}.}
\]

\[
\boxed{
\text{even disjoint natural }r^{5/3}\text{ payers}
\not\Rightarrow
\text{contradiction with finite }L^{10/3}+L^{5/3}.}
\]

\[
\boxed{
\text{unweighted finite spacetime integrability}
\not\Rightarrow
\text{finiteness of the critical }\rho_V^{-5/3}\text{ weighted integral}.}
\]

---

## 7. Next theorem target

Define

\[
\boxed{
\mathcal T_{GMS}^{weight}:
\quad
\text{for every hypothetical singular point, existing certified whole-space ledgers force
finiteness of }\mathcal P_{GMS}^{log}\text{ for at least one constant }V.
}
\]

At present \(\mathcal T_{GMS}^{weight}\) is OPEN.

The next calculation should audit M17/M19 ancestry weights against the parabolic kernel \(\rho_V^{-5/3}\), rather than attempting another unweighted dyadic summation.

Global regularity remains unproved.