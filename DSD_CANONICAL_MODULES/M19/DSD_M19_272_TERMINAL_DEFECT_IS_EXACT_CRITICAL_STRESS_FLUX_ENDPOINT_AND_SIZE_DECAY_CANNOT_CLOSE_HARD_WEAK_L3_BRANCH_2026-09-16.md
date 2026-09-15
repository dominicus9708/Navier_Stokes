# DSD M19-272 — Terminal defect is the exact critical stress-flux endpoint; size decay cannot close the hard weak-L3 branch

Date: 2026-09-16  
Canonical ID: **M19-272**  
Status: **ACTIVE TERMINAL-DEFECT AUDIT / BLOW-DOWN FLUX IDENTIFICATION / CRITICAL ANNULAR DECAY FIREWALL / ZERO-FORCE ENDPOINT RIGIDITY OPEN / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-271 shows that the fixed-lag signed energy event cannot be absorbed by a bounded scalar coboundary. A successful continuation must expose a genuinely non-coboundary defect/resource.

The most concrete remaining candidate is the stationary terminal point defect already isolated in M5-573--579.

M5-576 and M5-579 establish two firewalls:

\[
\text{unforcedness for }s<0\not\Rightarrow\kappa=0,
\]

and

\[
\text{positive terminal energy flux}\not\Rightarrow\text{Type-I scaling contradiction}.
\]

The present module identifies exactly what the defect coefficient measures in the pre-blow-down field and what additional decay would be sufficient to kill it.

---

## 2. First-generation stationary-time field and stress

Let \((V,P)\) denote the first-generation field at the fixed regular time used by the second-generation backward blow-down.

Write the momentum stress as

\[
\boxed{
\mathbb T[V,P]
:=
\nabla V+(\nabla V)^T
-V\otimes V
-PI.
}
\]

At that fixed time the unforced equation is

\[
\partial_tV=\nabla\cdot\mathbb T.
\]

For a second-generation blow-down factor \(R\to\infty\),

\[
V_R(y)=R V(Ry),
\qquad
P_R(y)=R^2P(Ry).
\]

Hence

\[
\boxed{
\mathbb T_R(y)=R^2\mathbb T(Ry).
}
\]

---

## 3. Sphere stress flux is exactly invariant under the blow-down

Let \(S_\rho\) be a sphere in the rescaled coordinates. With \(x=Ry\),

\[
dS_x=R^2dS_y.
\]

Therefore

\[
\begin{aligned}
\int_{S_\rho}\mathbb T_Rn\,dS_y
&=
\int_{S_\rho}R^2\mathbb T(Ry)n\,dS_y\\
&=
\boxed{
\int_{S_{R\rho}}\mathbb Tn\,dS_x.
}
\end{aligned}
\]

Thus the terminal point-force/stress coefficient is not an abstract new source. It is the scale-critical large-radius stress-flux coefficient already present in the first-generation field.

On a stationary terminal branch \(C=0\), the punctured stationary equation gives

\[
\mathcal F_A'(q)=0,
\]

so

\[
\boxed{
\mathcal F_A(q)\equiv\kappa.
}
\]

Consequently, along every convergent blow-down record,

\[
\boxed{
\kappa
=
\lim_m
\int_{S_{R_m\rho}}\mathbb T[V,P]n\,dS
}
\]

for every fixed rescaled radius \(\rho>0\) at which the terminal profile is evaluated.

---

## 4. Critical annular stress-decay criterion

Define

\[
\boxed{
\mathfrak S(R)
:=
\frac1R
\int_{R<|x|<2R}|\mathbb T(x)|\,dx.
}
\]

By the coarea formula,

\[
\int_R^{2R}
\int_{S_r}|\mathbb T|\,dS\,dr
=
\int_{R<|x|<2R}|\mathbb T|dx.
\]

Hence there exists \(r_R\in[R,2R]\) such that

\[
\boxed{
\int_{S_{r_R}}|\mathbb T|dS
\le
\mathfrak S(R).
}
\]

Suppose along the blow-down tail

\[
\boxed{
\mathfrak S(R_m)\to0.
}
\]

Write

\[
r_{R_m}=\lambda_mR_m,
\qquad
1\le\lambda_m\le2.
\]

After a subsequence, \(\lambda_m\to\lambda_*\in[1,2]\). Compact-annulus convergence of the blow-down then gives

\[
\left|
\int_{S_{\lambda_*}}\mathbb T_A n\,dS
\right|
=0.
\]

But the stationary terminal flux is independent of log radius, so

\[
\boxed{
\mathfrak S(R_m)\to0
\Longrightarrow
\kappa=0.
}
\]

Thus subcritical annular stress decay is a sufficient terminal-defect exclusion theorem.

---

## 5. Why the current hard tail sits exactly at the failed endpoint

For the retained critical tail

\[
V(x)\sim\frac1rA(\log r,\omega),
\]

one has schematically

\[
\nabla V\sim r^{-2},
\qquad
V\otimes V\sim r^{-2},
\qquad
P\sim r^{-2}.
\]

Therefore

\[
|\mathbb T|\sim r^{-2},
\]

and on one geometric annulus

\[
\int_{R<|x|<2R}|\mathbb T|dx
\sim
R.
\]

Hence

\[
\boxed{
\mathfrak S(R)=O(1),
}
\]

not \(o(1)\).

The terminal point defect is therefore supported by exactly the same critical scaling that supports the weak-\(L^3\) hard tail.

Finite enstrophy and the finite higher-derivative ancestry ledgers do not improve this annular stress exponent.

---

## 6. Energy-current analogue

Let

\[
J
:=
\left(\frac12|V|^2+P\right)V
-\nabla\left(\frac12|V|^2\right).
\]

Under blow-down,

\[
\boxed{
J_R(y)=R^3J(Ry).
}
\]

Therefore

\[
\boxed{
\int_{S_\rho}J_R\cdot n\,dS_y
=
R
\int_{S_{R\rho}}J\cdot n\,dS_x.
}
\]

The terminal normalized energy flux is precisely this scale-critical limit.

Define the annular energy-current size

\[
\boxed{
\mathfrak J(R)
:=
\int_{R<|x|<2R}|J(x)|dx.
}
\]

By coarea there exists \(r_R\in[R,2R]\) such that

\[
r_R
\int_{S_{r_R}}|J|dS
\le
2\mathfrak J(R).
\]

Thus

\[
\boxed{
\mathfrak J(R_m)\to0
\Longrightarrow
\Phi_E=0
}
\]

on any stationary terminal limit obtained from those scales.

But a \(1/r\) critical tail has

\[
J\sim r^{-3},
\]

so

\[
\mathfrak J(R)=O(1).
\]

Again the hard branch lies exactly at the nondecaying critical endpoint.

---

## 7. Relation to strong L3 versus weak L3

The advective part of the annular energy current contains the cubic critical quantity

\[
\int_{R<|x|<2R}|V|^3dx.
\]

For a strong global \(L^3\) field this annular quantity tends to zero.

For

\[
V\sim r^{-1}A(\log r,\omega),
\]

it becomes

\[
\int_{\log R}^{\log 2R}
\int_{S^2}|A(q,\omega)|^3d\omega\,dq,
\]

which is order one on the positive-density hard factor.

M19-266/M5-571 give

\[
\boxed{
\left\langle
\int_{S^2}|A|^3d\omega
\right\rangle_q
=c_3>0.
}
\]

Therefore the hard ergodic branch does not approach the strong-\(L^3\) annular-decay corridor.

This explains why terminal energy-flux decay cannot be obtained from the current amplitude package.

---

## 8. External stationary removability boundary

Classical stationary isolated-singularity theorems remove the origin under genuinely subcritical conditions such as

\[
u\in L^3_{loc}
\]

or

\[
|u(x)|=o(|x|^{-1})
\quad(x\to0).
\]

The current terminal class is instead the critical endpoint

\[
|u(x)|=O(|x|^{-1}),
\qquad
u\in L^{3,\infty}_{loc},
\]

where Landau solutions show that a nonzero point force can support a nonremovable singularity.

Accordingly, known subcritical removability does not by itself close the present branch.

This literature input is used only as a firewall on theorem scope; the internal flux identities above are independent of it.

---

## 9. Supported residual at the origin

On a stationary terminal profile, the stationary Navier--Stokes residual vanishes on

\[
\mathbb R^3\setminus\{0\}.
\]

The critical stress satisfies locally

\[
|\mathbb T_A(x)|\lesssim |x|^{-2},
\]

so it is locally integrable. Its divergence has critical distributional order three.

The point-supported critical contribution detected by the sphere flux is

\[
\boxed{
\nabla\cdot\mathbb T_A
=
\kappa\,\delta_0
}
\]

in the point-force channel.

Therefore the stationary terminal problem is naturally separated into

\[
\boxed{
\kappa\neq0
\quad\text{(genuine terminal point defect)}
}
\]

and

\[
\boxed{
\kappa=0
\quad\text{(zero-force critical stationary endpoint)}.
}
\]

The second branch is not automatically removable under the present weak-\(L^3\) endpoint assumptions; it needs an endpoint rigidity theorem or additional decay.

---

## 10. Main consequence

The stationary defect route is not an independent easy escape from the critical-tail problem.

It is another exact formulation of the same endpoint obstruction:

\[
\boxed{
\text{nonzero terminal defect/flux}
\Longleftrightarrow
\text{failure of subcritical annular stress/current decay at the critical }1/r\text{ scale}
}
\]

in the sense of the sufficient decay tests above.

Thus finite kinetic energy, finite enstrophy, finite palinstrophy, or the normalized raw-H2 ancestry budget cannot kill the defect by size alone.

---

## 11. Refined stationary closure target

Replace the broad target

\[
\mathcal T_{tail}^{energy-defect}
\]

by the sharper pair

\[
\boxed{
\mathcal T_{tail}^{force-cancel}:
\kappa=0
\text{ from angular/stress cancellation rather than size decay},
}
\]

and

\[
\boxed{
\mathcal T_{tail}^{zero-force-rigidity}:
\kappa=0
\Longrightarrow
A=0
\text{ or strong-}L^3/o(1/r)\text{ improvement on the recurrent stationary class}.
}
\]

If both are proved, the stationary terminal branch closes.

If force cancellation fails, the surviving nonzero \(\kappa\) is the explicit terminal defect/root.

---

## 12. Permanent firewalls after M19-272

\[
\boxed{
\text{unforced for }s<0
\not\Rightarrow
\kappa=0.
}
\]

\[
\boxed{
\text{finite energy/enstrophy}
\not\Rightarrow
\frac1R\int_{R<|x|<2R}|\mathbb T|\to0.
}
\]

\[
\boxed{
\text{positive terminal energy flux}
\not\Rightarrow
\text{Type-I contradiction}.
}
\]

\[
\boxed{
\text{strong-}L^3\text{ removability theorem}
\not\Rightarrow
\text{critical weak-}L^3\text{ endpoint removability}.
}
\]

\[
\boxed{
\text{hard }1/r\text{ tail}
\text{ is exactly stress/current critical, not subcritical}.
}
\]

---

## 13. Immediate next target

The highest-value stationary calculation is now **cancellation/rigidity**, not another norm estimate:

1. derive the angular formula for the point-force coefficient
   \[
   \kappa=\int_{S^2}\mathbb T_A(q,\omega)e_r\,d\omega,
   \]
   and test whether the recurrent/divergence-free/zero-mean constraints force any component to vanish;
2. if \(\kappa=0\) is attainable, audit endpoint stationary removability on the specific recurrent log-profile class rather than on arbitrary weak-\(L^3\) fields;
3. in parallel retain M19-271's dynamic target \(\mathcal T_{tail}^{lag-defect}\).

Global 3D Navier--Stokes regularity remains unproved.
