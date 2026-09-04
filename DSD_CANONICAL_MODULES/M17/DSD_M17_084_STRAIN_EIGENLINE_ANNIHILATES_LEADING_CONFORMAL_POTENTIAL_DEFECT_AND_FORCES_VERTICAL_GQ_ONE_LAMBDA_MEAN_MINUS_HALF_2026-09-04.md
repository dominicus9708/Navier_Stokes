# DSD M17-084 — The strain eigenline annihilates the leading conformal potential defect and forces vertical G_q=1 with mean lambda = -1/2

Date: 2026-09-04
Canonical ID: **M17-084**

Status: **INTERNAL VERTICAL CONFORMAL HIGH-JET COLLAPSE / M17-083 DERIVED THE FIRST-NONZERO ANGULAR-JET MATERIAL LAW BEFORE REIMPOSING THE FULL CE-H STRAIN EIGENLINE. FOR A CONFORMAL CORE `q_2=(alpha/2)|z|^2`, `phi_2=(lambda/2)|z|^2`, LET `m>=3` BE THE FIRST NONZERO ANGULAR ORDER AND `phi_m` THE FIRST HORIZONTAL POTENTIAL TERM VISIBLE TO `psi=Lphi`. AT ANGULAR ORDER `m-1`, THE STRAIN EIGENLINE `H_phi J grad q=sigma J grad q` REDUCES TO `(H phi_m)Jz=s_{m-2}Jz`. SYMMETRY OF THE HESSIAN THEN GIVES `z^T(H phi_m)Jz=0`, WHILE HOMOGENEITY GIVES `z^T(H phi_m)Jz=(m-1)L phi_m=(m-1)Psi_m`. HENCE `Psi_m=0`. THE COMPANION LAW `partial_3 Psi_m=(G_q-1)X_m` AND `X_m!=0` FORCE `G_q=1`; THE CONFORMAL VERTICAL COMPATIBILITY THEN FORCES `partial_3 lambda=0`. THUS EVERY FINITE-ORDER VERTICAL NONAXIS CORE — NONCONFORMAL OR CONFORMAL HIGH-JET — ENTERS THE SAME M17-082 AXIAL GLOBAL l=3 PRESSURE LOCK. WITH `Psi_m=0`, THE HIGH-JET MATERIAL LAW IS PURELY MULTIPLICATIVE, AND RECURRENCE WITH `<kappa>=3/2` FORCES `<lambda>=-1/2` FOR EVERY `m>=3`. THIS IS INCOMPATIBLE WITH SAME-MARKER AXIAL LINE-ELEMENT RECURRENCE, WHICH WOULD REQUIRE `<lambda>=1/4`; THEREFORE A RECURRENT HIGH-JET CONFORMAL SURVIVOR MUST USE MATERIAL AXIAL STRETCH/CORE-MARKER TURNOVER OR APPROACH THE AXISYMMETRIC FIREWALL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-083

On a vertical conformal positive core,

\[
Q=\alpha I_2,
\qquad
\alpha\neq0,
\]

with

\[
q^{(2)}(z)=\frac\alpha2|z|^2,
\]

let

\[
m\ge3
\]

be the first nonzero transverse order of

\[
\chi=\mathcal Lq.
\]

M17-083 defines the first nonzero angular defect and potential-defect jets

\[
X_m=\chi^{(m)},
\qquad
\Psi_m=\psi^{(m)},
\qquad
\psi=\mathcal L\phi,
\]

and derives

\[
D_BX_m
=\left[
\kappa+(2-m)\lambda-\frac{m+1}{2}
\right]X_m
-m\alpha\Psi_m.
\]

M17-083 deliberately did not yet use the full CE-H strain-eigenline at order `m-1`.

---

## 2. First angular contribution to the horizontal potential

At the regular nodal core,

\[
\nabla_h^2\phi=\lambda I_2.
\]

Write the horizontal Taylor expansion as

\[
\phi
=\phi_{radial}
+\phi_m^{ang}
+\text{higher angular order},
\]

where `phi_radial` contains the rotationally invariant terms and `phi_m^{ang}` is the first degree-`m` term with

\[
\mathcal L\phi_m^{ang}=\Psi_m.
\]

All lower angular potential jets vanish by M17-083's order-consistency argument.

---

## 3. Expand the CE-H strain eigenline

The exact CE-H relation is

\[
\boxed{
(\nabla_h^2\phi)J\nabla_hq
=\sigma J\nabla_hq.
}
\]

At leading order,

\[
\nabla_hq^{(2)}=\alpha z,
\qquad
\nabla_h^2\phi^{(2)}=\lambda I_2,
\]

so the quadratic conformal core satisfies the eigenline identically.

At the first non-axisymmetric angular order `m-1`, the terms

\[
\lambda I_2\,J\nabla_hq_m
\]

cancel against the corresponding `lambda J grad_h q_m` term on the right.
Rotationally invariant lower higher-order terms contribute only to lower radial orders or to orders strictly above this first angular balance.

The remaining first angular equation is therefore

\[
\boxed{
(\nabla_h^2\phi_m^{ang})Jz
=s_{m-2}(z)Jz
}
\]

for some homogeneous scalar `s_{m-2}` coming from the first angular correction to `sigma`.

Thus `Jz` is an eigenvector of the symmetric Hessian `nabla_h^2 phi_m^{ang}` at every nonzero `z`.

---

## 4. Homogeneity kills the potential angular jet

Because the Hessian is symmetric, the eigenvector condition implies

\[
\boxed{
z^T(\nabla_h^2\phi_m^{ang})Jz=0.}
\]

For any homogeneous scalar polynomial `f_m` of degree `m`, Euler's identity gives

\[
(\nabla_h^2f_m)z
=(m-1)\nabla_hf_m.
\]

Hence

\[
\begin{aligned}
z^T(\nabla_h^2f_m)Jz
&=((\nabla_h^2f_m)z)\cdot Jz\\
&=(m-1)\nabla_hf_m\cdot Jz\\
&=(m-1)\mathcal Lf_m.
\end{aligned}
\]

Apply this to `f_m=phi_m^{ang}`:

\[
0=(m-1)\mathcal L\phi_m^{ang}.
\]

Since `m>=3`,

\[
\boxed{
\Psi_m=\mathcal L\phi_m^{ang}=0.
}
\]

Therefore the transfer term retained in M17-083 is actually annihilated by the full CE-H strain geometry at the first resolved conformal angular order.

---

## 5. The companion equation forces G_q=1

M17-017 gives

\[
\partial_3\psi=(G_q-1)\chi.
\]

At the first nonzero angular order,

\[
\boxed{
\partial_3\Psi_m
=(G_q-1)X_m.
}
\]

Section 4 gives `Psi_m=0` at every retained point of the vertical conformal high-jet filament.
Therefore its axial derivative also vanishes.
Since

\[
X_m\neq0,
\]

we obtain

\[
\boxed{G_q=1.}
\]

Thus the conformal high-jet branch loses the scalar freedom that remained in the purely quadratic compatibility relation of M17-015.

---

## 6. Conformal compatibility then forces lambda_3=0

M17-015's exact vertical compatibility is

\[
(G_q-1)Q
=(\partial_3\lambda)I_2.
\]

For

\[
Q=\alpha I_2,
\]

this becomes

\[
(G_q-1)\alpha
=\partial_3\lambda.
\]

Using Section 5,

\[
\boxed{
\partial_3\lambda=0.
}
\]

Hence every finite-order vertical non-axisymmetric regular core now satisfies

\[
\boxed{
G_q=1,
\qquad
\partial_3\lambda=0,
}
\]

whether its first-order nodal Hessian is nonconformal or conformal.

The only conformal vertical escape that avoids this conclusion is the exact firewall

\[
\chi\equiv0.
\]

---

## 7. The M17-082 global axial l=3 lock now covers the high-jet branch

M17-082 used precisely

\[
G_q=1,
\qquad
\partial_3\lambda=0
\]

to obtain

\[
\boxed{
\Delta(\partial_3\lambda_h)
=-\frac12\mathcal H_{333}
}
\]

and

\[
\boxed{
D_BV_V
=-\frac12(\Pi_V^{prod}+\Pi_V^{rel}).
}
\]

Therefore the vertical conformal high-jet branch is not a separate pressure-locking class.
It enters the same axial global `l=3` production/relative-transport ledger as the nonconformal vertical branch.

This removes one branch duplication identified by the M17-081 exhaustiveness audit.

---

## 8. High-jet material law becomes purely multiplicative

Since

\[
\Psi_m=0,
\]

M17-083's first-nonzero jet law reduces to

\[
\boxed{
D_BX_m
=\left[
\kappa+(2-m)\lambda-\frac{m+1}{2}
\right]X_m.
}
\]

Therefore its angular phase is materially frozen at leading order, and its amplitude obeys

\[
\boxed{
D_B\log|X_m|
=\kappa+(2-m)\lambda-\frac{m+1}{2}.
}
\]

No leading angular-potential recharge remains available.

---

## 9. Recurrent high-jet branch fixes the mean strain

Assume

\[
0<c_m\le|X_m|\le C_m<\infty
\]

on a uniformly recurrent compact high-jet branch.
Then

\[
\left\langle
D_B\log|X_m|
\right\rangle=0.
\]

The recurrent regular nodal Jacobian gives

\[
\boxed{\langle\kappa\rangle=\frac32.}
\]

Hence

\[
0
=\frac32+(2-m)\langle\lambda\rangle
-\frac{m+1}{2}.
\]

For

\[
m\ge3,
\]

we may divide by `2-m` and obtain

\[
\boxed{
\langle\lambda\rangle=-\frac12.
}
\]

Remarkably, the value is independent of the finite angular multipole order `m`.

---

## 10. Same-marker axial recurrence is impossible

M17-083 gives the vertical material line-element law

\[
D_B\log\ell_3
=-2\lambda+\frac12.
\]

With

\[
\langle\lambda\rangle=-\frac12,
\]

we obtain

\[
\boxed{
\left\langle D_B\log\ell_3\right\rangle
=\frac32.
}
\]

Thus a material axial line element grows exponentially in similarity time on average:

\[
\boxed{
\ell_3(\theta)\sim e^{3\theta/2}
}
\]

at the level of the long-time exponent.

It cannot remain bounded and recurrent.

Therefore

\[
\boxed{
A_m^{nonaxis}
+\text{same-marker axial recurrence}
\Longrightarrow\bot.
}
\]

A recurrent Eulerian/shape high-jet survivor must instead use at least one of:

1. axial material stretching with nonrecurrent marker spacing;
2. motion of the selected recurrent core through material labels;
3. finite-jet degeneration/order change;
4. approach to the axisymmetric no-swirl firewall.

---

## 11. DSD analysis

The conformal branch has undergone the descriptor collapse

\[
\boxed{
Q=\alpha I
+X_m\neq0
\to
\Psi_m=0
\to
G_q=1
\to
\lambda_3=0
\to
\text{M17-082 global axial }l=3\text{ lock}.
}
\]

Thus the apparent conformal exception in M17-015 was only a first-order exception.
Once a finite higher angular descriptor is resolved, the same vertical scalar constraints reappear.

---

## 12. DSD audit

### Audit A — declaring all conformal cores nonexceptional
Rejected. The conclusion requires a nonzero finite angular defect `X_m`. The exact axisymmetric firewall `chi=0` remains exempt and regular.

### Audit B — using harmonicity to prove Psi_m=0
Not needed. The stronger homogeneity plus strain-eigenline identity already forces `L phi_m=0`. Harmonicity remains consistent but is not the closure mechanism.

### Audit C — forgetting first-angular-order cancellation of q_m
Avoided. The isotropic quadratic Hessian `lambda I` acts on `J grad q_m` on both sides of the eigenline and cancels exactly.

### Audit D — treating <lambda>=-1/2 as pointwise
Rejected. Only the recurrent long-time mean is fixed.

### Audit E — turning Lagrangian stretching into an Eulerian contradiction
Rejected. Exponential material line stretching can coexist with recurrence of Eulerian shape. The contradiction applies only if the same material axial spacing is also assumed recurrent/bounded.

### Audit F — proof status
The conformal high-jet branch is much narrower but is not globally closed because marker turnover/stretch and firewall approach remain legitimate exits.

---

## 13. Updated vertical Rank-1 branch tree

The vertical great-circle branch now has the sharper split

\[
\boxed{
R_{1,V}
\Longrightarrow
G_{axis/no\text{-}swirl}
\lor
R_{1,V}^{nonaxis}.
}
\]

Every finite-order regular nonaxis vertical branch satisfies

\[
\boxed{
G_q=1,
\qquad
\lambda_3=0,
\qquad
\Delta(\partial_3\lambda_h)=-\frac12\mathcal H_{333}.
}
\]

If its first nonaxis order is conformal-high-jet `m>=3`, it additionally satisfies

\[
\boxed{
\langle\lambda\rangle=-\frac12
}
\]

and cannot have bounded same-marker axial recurrence.

The nonconformal `m=2` class retains the resonance

\[
D_BX_2=(\kappa-3/2)X_2
\]

and therefore does not acquire the `lambda=-1/2` mean condition from this calculation.

---

## 14. Next target — vertical nonconformal m=2 versus marker-turnover gate

After M17-084, the difficult vertical Rank-1 survivor is no longer the conformal high-jet geometry itself.
The remaining hard tasks are:

1. determine whether the nonconformal `m=2` class has an independent marker-stretch/pressure-lock obstruction;
2. determine whether the high-jet `m>=3` branch can realize recurrent Eulerian shape while continually replacing/stretched material axial labels;
3. connect the common M17-082 global `l=3` lock to the M17-019/M5 negative-payer and hysteresis network.

These are turnover/recurrence questions, not unresolved local tensor identities.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
