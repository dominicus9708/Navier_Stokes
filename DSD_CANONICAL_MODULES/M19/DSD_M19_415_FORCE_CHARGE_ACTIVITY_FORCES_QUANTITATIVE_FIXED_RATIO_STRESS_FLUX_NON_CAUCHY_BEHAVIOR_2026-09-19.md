# M19-415 — Force-charge activity forces quantitative fixed-ratio stress-flux non-Cauchy behavior

Date: 2026-09-19  
Canonical ID: **M19-415**  
Status: **FORCE-CHARGE QUANTIFICATION / POSITIVE RECURRENT L2 FORCE ACTION UPGRADES TO A FIXED STRESS-FLUX EXCURSION BY COMPACT SMOOTHNESS / BLOW-DOWN RESTORATION FORCES FIXED-RATIO FAR-FIELD STRESS-FLUX NONCONVERGENCE / THE COST IS STILL CRITICAL AND SUMMABLE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-413 and M5-271

After M19-412--413 the nontrivial retained minimal terminal hull has the mandatory residual fork
\[
R_{gap}
\Longrightarrow
F_{charge}
\lor
A_{res}.
\]

M19-414 shows that the direct unsigned raw-H2 ancestry route from \(A_{res}\) is critical/summable.

On the force-charge branch M5-271 gives a positive-density recurrent family of fixed normalized log cells \(I\) such that
\[
\boxed{
\int_I |\mathcal B_q(q)|^2dq
\ge
\eta_F>0,
}
\]
where
\[
\boxed{
\mathcal B(q)
=
\int_{|x|=e^q}\mathbb S_T n\,dS
}
\]
is the dimensionless critical momentum-stress flux and
\[
\boxed{
\mathcal B_q(q)
=
\overline{\mathcal R}(q)
}
\]
up to the fixed first-jet sign convention.

The invariant mean of \(\mathcal B_q\) is zero, so this is recurrent oscillatory action rather than a secular force source.

## 2. Compact smoothness gives a uniform second-derivative bound

The retained terminal hull is compact in the punctured smooth topology.

The stress coefficient is built from finitely many derivatives of the terminal trace and pressure. Hence on every fixed normalized log cell there is a hull-uniform bound
\[
\boxed{
|\mathcal B_{qq}(q)|
\le
M_2<\infty.
}
\]

Likewise \(\mathcal B_q\) is uniformly bounded.

This compact regularity is the ingredient that prevents the positive \(L^2\) action from being hidden in arbitrarily small-amplitude arbitrarily high-frequency oscillations.

## 3. Every force-active cell contains a fixed derivative event

For a unit log cell \(I\),
\[
\int_I|\mathcal B_q|^2dq
\ge
\eta_F
\]
implies that at some \(q_0\in I\),
\[
|\mathcal B_q(q_0)|
\ge
\sqrt{\eta_F}.
\]

Choose a unit vector \(e\in\mathbb R^3\) in the direction of \(\mathcal B_q(q_0)\) and set
\[
b(q):=e\cdot\mathcal B(q).
\]

Then
\[
b'(q_0)
=
|\mathcal B_q(q_0)|
\ge
a_F,
\qquad
a_F:=\sqrt{\eta_F}.
\]

Since
\[
|b''|
\le
M_2,
\]
define
\[
h_F
:=
\min\left\{
\frac12,
\frac{a_F}{2M_2}
\right\}
\]
when \(M_2>0\).

On at least one one-sided interval of length \(h_F\) starting from \(q_0\),
\[
b'(q)
\ge
\frac{a_F}{2}.
\]

Therefore
\[
\boxed{
|\mathcal B(q_1)-\mathcal B(q_0)|
\ge
\delta_F
}
\]
for some
\[
0<|q_1-q_0|\le h_F,
\]
where
\[
\boxed{
\delta_F
:=
\frac{a_F h_F}{2}
>0.
}
\]

If \(M_2=0\), then \(\mathcal B_q\) is constant on the connected orbit; bounded recurrence plus zero invariant mean already forces \(\mathcal B_q=0\), so the force-active branch is impossible. Thus the nontrivial branch is covered by the estimate above.

## 4. Positive recurrent force action therefore forces a genuine oscillation amplitude

The force-active cells have positive recurrent density.

Hence the previous fixed excursion occurs recurrently:
\[
\boxed{
\text{positive-density }q\text{-set on which }
\operatorname{osc}_{[q-h_F,q+h_F]}\mathcal B
\ge
\delta_F.
}
\]

In particular \(\mathcal B(q)\) cannot converge as \(q\to+\infty\) or \(q\to-\infty\) on the force-active recurrent orbit.

Thus
\[
\boxed{
F_{charge}
\Longrightarrow
\mathcal B
\text{ is quantitatively non-Cauchy in log radius.}
}
\]

This is stronger than merely
\[
\langle|\mathcal B_q|^2\rangle>0.
\]

## 5. A weaker closure theorem than stress tightness would already kill F_charge

Define the asymptotic fixed-ratio Cauchy property
\[
\boxed{
\mathcal T_{stress}^{Cauchy}(\Lambda):
\quad
\sup_{1\le\lambda\le\Lambda}
|F(\lambda R)-F(R)|
\longrightarrow0
\qquad(R\to\infty),
}
\]
for some fixed \(\Lambda>1\), where \(F(R)\) is the sphere momentum-stress flux of the pre-blow-down field.

This condition does **not** require
\[
F(R)\to0.
\]

It requires only asymptotic constancy over bounded multiplicative changes of radius.

M19-274's uniform stress tightness implies this property, but the Cauchy property is strictly weaker.

The force-active branch violates it.

## 6. Blow-down restoration gives fixed-ratio far-field stress-flux failure

Let \(T\) be a terminal-tail state on a force-active component and let \(R_m\to\infty\) be a blow-down sequence from the first-generation field \(V\):
\[
V_m(y)=R_mV(R_my)
\to
T(y)
\]
smoothly on fixed punctured annuli.

Stress-flux scaling is exact:
\[
\int_{S_\rho}\mathbb T[V_m]n\,dS
=
\int_{S_{R_m\rho}}\mathbb T[V]n\,dS.
\]

Fix the two terminal log phases \(q_0,q_1\) from Section 3 and write
\[
\rho_i=e^{q_i}.
\]

Compact-annulus convergence gives
\[
F_V(R_m\rho_i)
\to
\mathcal B(q_i)
\qquad(i=0,1).
\]

Therefore, for all sufficiently large \(m\),
\[
\boxed{
|F_V(R_m\rho_1)-F_V(R_m\rho_0)|
\ge
\frac{\delta_F}{2}.
}
\]

The radius ratio is uniformly bounded:
\[
\boxed{
e^{-h_F}
\le
\frac{\rho_1}{\rho_0}
\le
e^{h_F}.
}
\]

Hence the force branch forces a fixed-ratio large-radius stress-flux non-Cauchy defect:
\[
\boxed{
\limsup_{R\to\infty}
\sup_{e^{-h_F}\le\lambda\le e^{h_F}}
|F_V(\lambda R)-F_V(R)|
\ge
\frac{\delta_F}{2}.
}
\]

After orienting radii so that \(\lambda\ge1\), the same statement is obtained with a fixed interval \([1,\Lambda_F]\), \(\Lambda_F=e^{h_F}>1\).

## 7. This is a representation defect, not a point-force defect

On the old stationary branch,
\[
\mathcal B_q=0
\]
and \(\mathcal B\equiv\kappa\) was a constant point-force coefficient.

After M19-412 that realized stationary branch is closed.

The surviving force-channel obstruction is different:
\[
\boxed{
\text{not a constant nonzero force, but persistent scale-to-scale force-flux oscillation.}
}
\]

Therefore the correct dynamic inheritance gate is no longer merely
\[
\mathcal T_{stress}^{tight}.
\]

It is the weaker and more precise
\[
\boxed{
\mathcal T_{stress}^{Cauchy}:
\text{prove asymptotic fixed-ratio Cauchy behavior of the signed stress flux.}
}
\]

Any theorem of this type would eliminate \(F_{charge}\) even if the limiting flux were not known a priori to be zero.

## 8. Critical shell-cost firewall

The excursion identity itself gives
\[
\mathcal B(q_1)-\mathcal B(q_0)
=
\int_{e^{q_0}<|x|<e^{q_1}}F_T(x)\,dx.
\]

If the physical shell lies at radius \(R\) with fixed ratio endpoints and the flux difference is at least \(\delta_F\), Cauchy--Schwarz gives
\[
\delta_F^2
\lesssim
R^3
\int_{A(R,\Lambda_FR)}
|F_T(x)|^2dx.
\]

Thus
\[
\boxed{
\int_{A(R,\Lambda_FR)}
|F_T|^2dx
\gtrsim
\delta_F^2R^{-3}.
}
\]

This is exactly critical/summable across geometric radii:
\[
\sum_m R_m^{-3}<\infty.
\]

Therefore even recurrent fixed-amplitude stress-flux excursions do not create an unsigned divergent shell budget.

This is the force-channel analogue of the M19-414 ancestry firewall.

## 9. Total variation also need not be finite

Let
\[
M_1:=\sup_q|\mathcal B_q(q)|<\infty.
\]

On every force-active unit cell,
\[
\int_I|\mathcal B_q|dq
\ge
\frac{1}{M_1}
\int_I|\mathcal B_q|^2dq
\ge
\frac{\eta_F}{M_1}.
\]

Positive density of such cells therefore forces linear growth of total variation:
\[
\boxed{
\operatorname{TV}_{[0,L]}\mathcal B
\gtrsim
cL
}
\]
along generic force-active recurrent orbits.

But bounded recurrent functions can have infinite total variation through repeated oscillation.

No finite-TV theorem is presently inherited from the Navier--Stokes energy package.

Hence
\[
\boxed{
\text{bounded stress flux}
+
\text{linear total variation}
}
\]
is not a contradiction.

## 10. Updated terminal residual frontier

After M19-414--415,
\[
\boxed{
R_{gap}
\Longrightarrow
F_{charge}^{nonCauchy}
\lor
A_{res}^{ang,critical}.
}
\]

The angular branch is critical/summable under direct unsigned ancestry.

The force branch is now a precise far-field representation defect:
\[
\boxed{
F_{charge}^{nonCauchy}
=
\text{persistent fixed-ratio failure of signed stress-flux convergence.}
}
\]

The next high-value question is whether the original-variable solution or the first-generation ancient field supplies any **signed asymptotic Cauchy theorem** for sphere stress flux that is weaker than absolute stress tightness.

A successful theorem need not prove
\[
F(R)\to0;
\]
it only needs
\[
F(\lambda R)-F(R)\to0
\]
uniformly for \(\lambda\) in one fixed compact multiplicative interval.

\[
\boxed{\text{M19-415 COMPLETE; FORCE-CHARGE ACTIVITY IS EQUIVALENT TO A QUANTITATIVE FIXED-RATIO STRESS-FLUX NON-Cauchy DEFECT ON THE BLOW-DOWN CORRIDOR.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
