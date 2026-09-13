# DSD M19-253 — Transparent Moving-Sphere / Galilean-Cylinder Reformulation

Date: 2026-09-14
Status: VALID REFORMULATION + TRANSFER AUDIT; NOT A CLOSURE THEOREM
Canonical role: replaces the no-slip spectator cavity as the active whole-space observation geometry. M19-231–252 remain valid only within their stated cavity hypotheses and are retained as auxiliary diagnostics.

## 0. Scope firewall

Clay (A) is a whole-space problem on \(\mathbb R^3\). A sphere introduced inside \(\mathbb R^3\) is not a material wall unless a new boundary-value problem is explicitly imposed. Therefore

\[
\boxed{\text{no-slip cavity exclusion}\not\Rightarrow\text{transparent observation-sphere regularity}.}
\]

The active object in this module is a nonmaterial moving observation ball

\[
\Omega_R(t)=B_R(X(t))\subset\mathbb R^3,
\qquad S_R(t)=\partial B_R(X(t)),
\]

with fixed radius \(R>0\), where fluid is free to cross \(S_R(t)\).

The boundary velocity is \(V_b(t)=\dot X(t)\). No condition such as \(u|_{S_R}=0\) or \(u\cdot n=0\) is imposed.

---

## 1. Whole-space equations and moving-window balances

Let

\[
\partial_tu+(u\cdot\nabla)u=\nu\Delta u-\nabla p,
\qquad \nabla\cdot u=0,
\]

and set \(e=|u|^2/2\).

### 1.1 Exact local energy balance

Pointwise for a smooth solution,

\[
\partial_t e+\nabla\cdot\big((e+p)u-\nu\nabla e\big)
=-\nu|\nabla u|^2.
\]

Reynolds transport on the moving ball gives

\[
\boxed{
\frac d{dt}\int_{\Omega_R(t)}e
+\nu\int_{\Omega_R(t)}|\nabla u|^2
=
-\int_{S_R(t)}
\Big[e(u-\dot X)\cdot n+p\,u\cdot n-\nu\partial_ne\Big]\,dS.
}
\]

Equivalently, with Cauchy stress

\[
\sigma=-pI+2\nu D(u),
\qquad D(u)=\frac12(\nabla u+\nabla u^T),
\]

one has

\[
\boxed{
\frac d{dt}\int_{\Omega_R(t)}e
=
-\int_{S_R(t)}e(u-\dot X)\cdot n\,dS
+\int_{S_R(t)}(\sigma n)\cdot u\,dS
-2\nu\int_{\Omega_R(t)}|D(u)|^2.
}
\]

Thus the observation sphere creates no wall dissipation. Energy exchange is through the actual relative advective flux and stress work.

### 1.2 Exact relative mass-flux identity

Because \(\nabla\cdot u=0\) and \(\int_{S_R}n\,dS=0\),

\[
\boxed{
\int_{S_R(t)}(u-\dot X)\cdot n\,dS=0.
}
\]

This is only a zero *net* flux statement. Pointwise inward and outward exchange generally coexist.

### 1.3 Momentum balance

Using \(\partial_tu+\nabla\cdot(u\otimes u)=\nabla\cdot\sigma\),

\[
\boxed{
\frac d{dt}\int_{\Omega_R(t)}u
=
-\int_{S_R(t)}u\,[(u-\dot X)\cdot n]\,dS
+\int_{S_R(t)}\sigma n\,dS.
}
\]

### 1.4 Vorticity balance

Let \(\omega=\nabla\times u\). Since

\[
\partial_t\omega_i+
\partial_j\big(u_j\omega_i-\omega_ju_i-\nu\partial_j\omega_i\big)=0,
\]

one obtains

\[
\boxed{
\frac d{dt}\int_{\Omega_R(t)}\omega
=
-\int_{S_R(t)}
\Big[
\omega (u-\dot X)\cdot n
-u(\omega\cdot n)
-\nu\partial_n\omega
\Big]\,dS.
}
\]

There is therefore no legitimate replacement of vorticity exchange by a no-slip wall payer in the whole-space problem.

### 1.5 Enstrophy balance

With \(q=|\omega|^2/2\),

\[
\partial_tq+\nabla\cdot(qu-\nu\nabla q)
=
\omega^TS_u\omega-\nu|\nabla\omega|^2,
\qquad
S_u=\frac12(\nabla u+\nabla u^T).
\]

Hence

\[
\boxed{
\begin{aligned}
\frac d{dt}\int_{\Omega_R(t)}q
={}&\int_{\Omega_R(t)}\omega^TS_u\omega
-\nu\int_{\Omega_R(t)}|\nabla\omega|^2\\
&-\int_{S_R(t)}q(u-\dot X)\cdot n\,dS
+\nu\int_{S_R(t)}\partial_nq\,dS.
\end{aligned}}
\]

The interior stretching term, dissipation, and actual boundary transport are now separated exactly.

---

## 2. Preferred singular-scale form: smooth moving cutoffs

Sharp spherical traces are not the safest primitive at a hypothetical singular scale. Let

\[
\chi_X(x,t)=\chi(x-X(t))
\]

with smooth compactly supported \(\chi\). Then

\[
\boxed{
\frac d{dt}\int e\chi_X
+\nu\int|\nabla u|^2\chi_X
=
\int\big[e(u-\dot X)+pu\big]\cdot\nabla\chi_X
+\nu\int e\,\Delta\chi_X.
}
\]

For suitable weak solutions the corresponding local-energy statement is used as an inequality.

New firewall:

\[
\boxed{
\text{sharp moving-sphere balance}
\not\Rightarrow
\text{valid singular-scale argument without trace control}.}
\]

Accordingly, the canonical whole-space route should be formulated with cutoffs or parabolic cylinders first; sharp celestial spheres may be recovered only where regularity already justifies traces.

---

## 3. Moving centers and the acceleration-pressure audit

Let \(V(t)=\dot X(t)\), \(y=x-X(t)\), and

\[
v(y,t)=u(y+X(t),t)-V(t).
\]

Then

\[
\partial_tv+(v\cdot\nabla)v
=
\nu\Delta v-\nabla p(y+X(t),t)-\dot V(t).
\]

Defining

\[
q(y,t)=p(y+X(t),t)+\dot V(t)\cdot y
\]

restores the standard form

\[
\boxed{
\partial_tv+(v\cdot\nabla)v=\nu\Delta v-\nabla q,
\qquad \nabla\cdot v=0.
}
\]

Thus an accelerated tracking center is not the same as a constant Galilean boost unless the induced linear pressure is audited.

New firewall:

\[
\boxed{
\text{time-dependent moving center}
\not\Rightarrow
\text{Galilean-invariant }\varepsilon\text{-criterion without acceleration-pressure audit}.}
\]

---

## 4. Rigorous replacement geometry: constant-velocity Galilean cylinders

For a spacetime point \(z_0=(x_0,t_0)\), constant velocity \(V\in\mathbb R^3\), and scale \(r>0\), define

\[
Q_r^V(z_0)
=
\left\{(x,t):t_0-r^2<t<t_0,
\ |x-x_0-V(t-t_0)|<r\right\}.
\]

Under the exact Galilean change

\[
y=x-x_0-V(t-t_0),
\qquad
v(y,t)=u(x,t)-V,
\]

the Navier–Stokes equations retain their standard form (pressure changes at most by the usual irrelevant time gauge).

Define the scale-critical quantities

\[
C_V(r)
=
r^{-2}\int_{Q_r^V(z_0)}|u-V|^3\,dx\,dt,
\]

\[
D_V(r)
=
r^{-2}\int_{Q_r^V(z_0)}
|p-(p)_{B_r^V(t)}|^{3/2}\,dx\,dt,
\]

and, for bookkeeping,

\[
A_V(r)
=
r^{-1}\operatorname*{ess\,sup}_{t_0-r^2<t<t_0}
\int_{B_r(x_0+V(t-t_0))}|u-V|^2\,dx,
\]

\[
E_V(r)
=
r^{-1}\int_{Q_r^V(z_0)}|\nabla u|^2\,dx\,dt.
\]

All are scale invariant under the Navier–Stokes scaling in the standard way.

---

## 5. Exact consequence of standard epsilon regularity

Use any standard one-scale interior epsilon-regularity theorem for suitable weak solutions of the form:

> there exists a universal \(\varepsilon_*>0\) such that sufficiently small scale-invariant velocity/pressure cost on \(Q_r\), e.g. \(C(r)+D(r)<\varepsilon_*\), implies regularity in a smaller concentric parabolic cylinder.

Because constant Galilean boosts preserve the equation and preserve singular/regular status of the corresponding spacetime point, contraposition gives the following exact reformulation.

### Theorem target already inherited from standard theory

If \(z_0\) is a singular point, then for every constant velocity \(V\) and every sufficiently small admissible \(r\),

\[
\boxed{
C_V(r)+D_V(r)\ge\varepsilon_*.
}
\]

Equivalently,

\[
\boxed{
\inf_{V\in\mathbb R^3}
\big(C_V(r)+D_V(r)\big)
\ge\varepsilon_*
}
\]

at every sufficiently small singular scale.

We name this inherited reformulation

\[
\boxed{\mathcal T_{\mathrm{GMS}}^{\varepsilon}}.
\]

It is not a new epsilon-regularity theorem; the new content here is its explicit use as a moving-observation-sphere / Galilean-frame audit primitive.

### Interpretation

A genuine singularity cannot be made locally subcritical merely by choosing a better constant tracking velocity. Thus

\[
\boxed{
\text{moving-frame minimization}
\not\Rightarrow
\text{subcriticality at a singular point}.}
\]

This is stronger and cleaner than the previous intuition that one might simply follow the dangerous packet until its local cost becomes small.

---

## 6. New active contradiction target

The whole-space route is now reduced to obtaining a *separate* global or multiscale mechanism that contradicts the universal moving-frame cost floor.

Define

\[
\boxed{
\mathcal T_{\mathrm{GMS}}^{select}:
\quad
\text{every hypothetical finite-time singularity yields some }r_j\downarrow0,\ V_j
\text{ with }
C_{V_j}(r_j)+D_{V_j}(r_j)<\varepsilon_*.
}
\]

If \(\mathcal T_{\mathrm{GMS}}^{select}\) is proved, then \(\mathcal T_{\mathrm{GMS}}^{\varepsilon}\) gives an immediate contradiction.

At present,

\[
\boxed{\mathcal T_{\mathrm{GMS}}^{select}\ \text{is OPEN}.}
\]

No argument in M19-231–252 proves it.

This is the new canonical target for the transparent moving-sphere branch.

---

## 7. Small-radius celestial-sphere geometry

Where the solution is smooth, choose the observation-center velocity

\[
\dot X(t)=u(X(t),t).
\]

For \(x=X+R\omega\), \(\omega\in S^2\),

\[
u(X+R\omega,t)-u(X,t)
=
R\nabla u(X,t)\,\omega+O(R^2).
\]

Hence the relative radial velocity is

\[
\boxed{
\big(u(X+R\omega,t)-u(X,t)\big)\cdot\omega
=
R\,\omega^TS_u(X,t)\omega+O(R^2).
}
\]

The antisymmetric rotation tensor drops from the leading radial term. Moreover,

\[
\int_{S^2}\omega^TS_u\omega\,d\omega
=
\frac{4\pi}{3}\operatorname{tr}S_u
=0
\]

by incompressibility.

Therefore, at small regular scales, the moving celestial sphere naturally decomposes into strain-controlled inward/outward lobes whose leading spherical mean is zero.

Firewall:

\[
\boxed{
\text{strain-lobe geometry is a kinematic identity, not a regularity theorem}.}
\]

---

## 8. Transfer audit of M19-231–252

### 8.1 Artificial-boundary dependent: do NOT transfer as whole-space theorems

The following results remain valid only for the no-slip cavity problem in which they were derived:

- M19-231: compact cavity unit-mode core/escape spectral dichotomy.
- M19-232: exact cavity normalization currency.
- M19-233–234: vorticity migration/localization toward the cavity wall.
- M19-235: boundary shear payer.
- M19-237: \(d_{BL}\asymp\nu/R\) no-slip layer.
- M19-239: zero-normal-trace H(div) conclusion.
- M19-240: radial Hardy estimate in the zero-trace use made there.
- M19-245–252: passive no-slip impedance, pressure-work shell saturation/rigidity, frozen half-space determinant, and high-frequency cavity gap.

They are retained as auxiliary diagnostics for what an artificial wall adds to the problem. They are not deleted and are not mathematically retracted within their own hypotheses.

### 8.2 Potentially portable after rederivation

- M19-238: bulk scaling/curl-rigidity ideas can be recast with compactly supported moving cutoffs.
- M19-241: bare spectral-gap information may remain useful only after re-auditing the operator/domain appropriate to the whole-space or transparent setting.
- M19-242: weighted energy structure survives in global form; localized use must carry the exact moving-window flux terms.
- M19-243: the pressure source identity
  \[
  \boxed{\Delta p=-\partial_i\partial_j(u_iu_j)}
  \]
  and, for the linearized pressure in the previous branch,
  \[
  \boxed{\Delta\pi=-2\partial_iU_j\,\partial_jw_i}
  \]
  remain exact under their stated hypotheses.
- M19-244: critical-background asymptotic bookkeeping is not intrinsically a wall statement and remains available subject to the parent similarity hypotheses.

---

## 9. DSD audit result

The previous cavity branch answered a legitimate but narrower auxiliary question: what happens if a remote artificial no-slip wall is imposed? It does not by itself answer the Clay whole-space question.

The whole-space geometry should instead be organized as

\[
\boxed{
\text{hypothetical singular point}
\to
\text{nonmaterial moving/Galilean observation cylinders}
\to
\mathcal T_{\mathrm{GMS}}^{\varepsilon}
\to
\mathcal T_{\mathrm{GMS}}^{select}
\to
\bot.
}
\]

Only the first three arrows are presently justified. The selection theorem is OPEN.

### New canonical firewalls

\[
\boxed{\text{no-slip cavity exclusion}\not\Rightarrow\text{whole-space transparent-sphere exclusion}.}
\]

\[
\boxed{\text{sharp trace identity}\not\Rightarrow\text{singular-scale validity without trace control}.}
\]

\[
\boxed{\text{constant Galilean tracking}\neq\text{accelerated tracking without pressure correction}.}
\]

\[
\boxed{\text{moving-frame optimization}\not\Rightarrow\text{subcriticality}.}
\]

\[
\boxed{\mathcal T_{\mathrm{GMS}}^{\varepsilon}\not\Rightarrow\mathcal T_{\mathrm{GMS}}^{select}.}
\]

---

## 10. External-theory anchor

This module uses, but does not claim to re-prove, the classical interior epsilon-regularity framework for suitable weak 3-D Navier–Stokes solutions. Modern statements routinely use small scale-invariant \(L^3\) velocity and \(L^{3/2}\) pressure cost on a parabolic cylinder to infer regularity on a smaller cylinder; related interior criteria were developed and refined by Caffarelli–Kohn–Nirenberg, Lin, and Gustafson–Kang–Tsai among others.

The only deduction required here is exact Galilean covariance plus contraposition.

---

## 11. Next calculation

Priority is no longer to add another no-slip shell normal form. The next calculation must attack \(\mathcal T_{\mathrm{GMS}}^{select}\):

1. identify which existing DSD ancestry/energy/vorticity ledgers are genuinely whole-space and scale critical;
2. express them on \(Q_r^V\) or smooth moving cutoffs;
3. ask whether averaging in scale, center velocity, or angular strain sectors forces at least one subcritical cylinder;
4. if not, derive the exact payer required to keep
   \(\inf_V(C_V+D_V)\ge\varepsilon_*\) at every singular scale;
5. propagate that payer upward to the global root tree and test whether it contradicts any already certified ledger.

This is a clean whole-space contradiction target. Global regularity remains unproved.