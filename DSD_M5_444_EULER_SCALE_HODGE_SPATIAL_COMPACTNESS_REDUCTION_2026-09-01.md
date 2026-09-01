# DSD M5-444 — Euler-scale Hodge spatial compactness from the first-hitting vorticity cap

Date: 2026-09-01

Status: **SOURCE-SCALE COMPACTNESS SHARPENING / IN THE EULER NORMALIZATION OF M5-443 THE FIRST-HITTING CAP GIVES UNIFORM `L-infinity` VORTICITY / ON EVERY FIXED SOURCE-SCALE BALL WHERE THE GALILEAN-QUOTIENT LOCAL `L2` VELOCITY IS UNIFORMLY BOUNDED, LOCAL DIV-CURL/HODGE ESTIMATES AUTOMATICALLY GIVE `W^{1,p}` BOUNDS FOR EVERY FINITE `p`, HENCE STRONG SPATIAL PRECOMPACTNESS OF THE VELOCITY / THE SOURCE-SCALE COMPACTNESS GAP THEREFORE REDUCES TO LOCAL ENERGY/MASS ESCALATION OR TEMPORAL HARMONIC-PRESSURE NONCOMPACTNESS, NOT AN INDEPENDENT SPATIAL DERIVATIVE AMPLITUDE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Euler-scale family

Use the M5-443 normalization on a remote source scale `R_j=K_jr_j`.

It is convenient to allow the velocity normalization `U_j` to be the actual Galilean-quotient source RMS velocity, with

\[
U_j
\ge
c\frac{\nu K_j^2}{R_j}.
\]

Set

\[
V_j(y,\tau)
=
\frac{u(x_j^s+R_jy,t_j+R_j\tau/U_j)-c_j}{U_j}.
\]

Then

\[
\partial_\tau V_j
+V_j\cdot\nabla V_j
=-\nabla P_j
+\varepsilon_j\Delta V_j,
\]

with

\[
\boxed{
\varepsilon_j
=
\frac{\nu}{U_jR_j}
\le
CK_j^{-2}
\to0.
}
\]

---

## 2. Uniform source-scale vorticity amplitude

The normalized vorticity is

\[
\Omega_j
=\nabla\times V_j
=\frac{R_j}{U_j}\omega.
\]

The first-hitting cap is

\[
|\omega|\le q\frac{\nu}{r_j^2}
=q\frac{\nu K_j^2}{R_j^2}.
\]

Therefore

\[
\boxed{
\|\Omega_j\|_\infty
\le
q\frac{\nu K_j^2}{U_jR_j}
\le C_q.
}
\]

If `U_j` is larger than the minimal M5-443 Euler scale, this normalized vorticity cap only improves.

---

## 3. Local Hodge estimate

Fix two source-scale balls

\[
B_a\Subset B_{2a}
\]

with `a` independent of `j`.

For a divergence-free vector field, the local div-curl estimate gives, for every finite `1<p<infinity`,

\[
\boxed{
\|\nabla V_j\|_{L^p(B_a)}
\le
C_{a,p}
\left(
\|\Omega_j\|_{L^p(B_{2a})}
+
\|V_j-c_{j,a}\|_{L^2(B_{2a})}
\right),
}
\]

where `c_{j,a}` is an arbitrary local constant/Galilean gauge, for example the mean on `B_{2a}`.

This is the interior elliptic estimate for

\[
-\Delta V_j
=\nabla\times\Omega_j
\]

plus control of the local harmonic part by the `L2` velocity.

Since

\[
\|\Omega_j\|_\infty\le C_q,
\]

one obtains:

> If
> \[
> \sup_j\inf_c\|V_j-c\|_{L^2(B_{2a})}<\infty,
> \]
> then
> \[
> \boxed{
> \sup_j\|\nabla V_j\|_{L^p(B_a)}<\infty
> }
> \]
> for every finite `p`.

---

## 4. Spatial precompactness

Choose `p>3`. By Morrey's embedding,

\[
W^{1,p}(B_a)
\hookrightarrow
C^{0,\alpha}(B_a),
\qquad
\alpha=1-3/p>0.
\]

Thus bounded local source-scale energy modulo constants implies

\[
\boxed{
V_j-c_{j,a}
\text{ is strongly precompact in }C^{0,\alpha'}(B_a)
}
\]

for every `alpha'<alpha`, at each fixed time slice and uniformly on time intervals where the same local energy bound holds.

Therefore source-scale spatial derivative blowup is not an independent compactness obstruction once:

1. the first-hitting vorticity cap is used in Euler variables;
2. local Galilean-quotient `L2` mass is bounded.

---

## 5. What can still destroy spatial compactness

The only spatial escape left in a fixed source-scale ball is

\[
\boxed{
\inf_c\|V_j-c\|_{L^2(B_a)}\to\infty.
}
\]

This is precisely source-scale local energy/mass escalation.

It belongs to the strong critical/delocalized mass branch and should not be relabeled as an unexplained derivative singularity.

Thus the M5-443 Euler-noncompact branch sharpens to

\[
\boxed{
H_{Euler\text{-}scale\ spatial\ noncompact}
\Longrightarrow
H_{local\ energy/mass}^{strong}.
}
\]

---

## 6. Time compactness is a different issue

Spatial precompactness at each time does not by itself give strong space-time convergence.

The vorticity equation is

\[
\partial_\tau\Omega_j
+\nabla\cdot
(V_j\otimes\Omega_j-\Omega_j\otimes V_j)
=
\varepsilon_j\Delta\Omega_j.
\]

On bounded local-energy balls, `V_j` is locally bounded and `Omega_j` is uniformly `L-infinity`, so the non-pressure part has a uniform negative-Sobolev time-derivative bound.

However reconstructing the full velocity from vorticity leaves a local harmonic/div-curl-null component. Rapid time oscillation of that component is tied to pressure/affine forcing and is not controlled merely by the vorticity amplitude.

Therefore the remaining compactness split is

\[
\boxed{
\text{bounded local source energy}
\Longrightarrow
\text{spatially compact}
+
\big(
\text{time compact}
\lor
H_{pressure/harmonic\ time}^{strong}
\big).
}
\]

This is consistent with the earlier ambient/harmonic strain audits.

---

## 7. Consequence for the Euler-profile route

The remote strong branch now has the sharper source-scale alternatives:

\[
\boxed{
H_{remote}^{strong}
\Longrightarrow
\begin{cases}
H_{local\ Euler\ energy}^{strong},\\
H_{pressure/harmonic\ time}^{strong},\\
E_{ancient}^{Euler,compact}.
\end{cases}
}
\]

On the third branch, local energy is bounded on every fixed ball, pressure/harmonic time oscillation is controlled, viscosity tends to zero, and the spatial Hodge estimate gives the compactness needed to extract a nontrivial Euler profile.

---

## 8. Relation to recent Type-II literature

Seregin's 2026 Type-II analysis obtains Euler limits under explicit scale-weighted bounds on local energy, gradients, pressure, and mixed norms.

M5-444 shows that in the present first-hitting source normalization, **the gradient part is partly redundant** once local energy and the global first-hitting vorticity cap are available: div-curl elliptic regularity supplies interior gradient bounds automatically.

This does not imply Seregin's theorem applies, because his full hypotheses include additional scale-weighted and pressure/time information not yet derived here.

---

## 9. Firewall

The local Hodge estimate is interior. It does not give uniform global energy or tail control in the Euler variables.

It also does not control arbitrary time-dependent harmonic velocity components without pressure/frame information.

Thus no ancient Euler Liouville conclusion is claimed.

---

## 10. Audit verdict

### Removed as independent source-scale obstacle

Spatial derivative compactness on a fixed Euler-scale ball, provided local Galilean-quotient `L2` velocity is bounded.

### Remaining Euler-scale hard core

\[
\boxed{
H_{local\ energy/mass}^{strong}
\lor
H_{pressure/harmonic\ time}^{strong}
\lor
E_{ancient}^{Euler,compact}.
}
\]

### Still open

- pressure/harmonic time control;
- local energy growth across expanding Euler-scale balls;
- rigidity/Liouville of the resulting ancient Euler profile;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
