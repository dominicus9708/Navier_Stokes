# Plateau Mean-Stretching -> Betchov / Transverse-Action Bridge — 2026-08-24

Status: **CONNECTS THE COHERENT ANNULAR-PLATEAU SURVIVOR BACK TO THE EXISTING POSITIVE-MIDDLE / ANTI-RIBBON MAINLINE / GLOBAL REGULARITY NOT PROVED.**

This note combines

- `MEAN_VORTICITY_PLATEAU_STAGE_LEDGER_2026-08-24.md`,
- the source-active Betchov dichotomy, and
- the alignment-free transverse interlacing lemma.

The aim is to show that a coherent low-derivative plateau does not require a new mean-field endgame. If its normalized mean vorticity survives a geometric first-hitting stage, the required mean longitudinal strain action produces actual vortex-stretching source action. Unless Betchov residual is large, a fixed part of that action lies in the positive-middle geometry and therefore generates transverse anisotropy/ribbon action.

## 1. Plateau decomposition

Use a fixed moving weight `phi` and write

\[
\bar\Omega_\phi=m n,
\qquad
m:=|\bar\Omega_\phi|>0,
\qquad
|n|=1,
\]

and

\[
\Omega=mn+\delta\Omega,
\qquad
\int\phi\delta\Omega=0.
\]

Let

\[
\mu:=\int\phi.
\]

Assume the coherent plateau corridor supplies

\[
\boxed{m\ge m_->0}
\]

and the relative vorticity variance bound

\[
\boxed{
\int\phi|\delta\Omega|^2
\le\varepsilon_\Omega m^2\mu.
}
\]

## 2. Mean-vorticity ledger supplies longitudinal mean-strain action

The exact plateau ledger gives on a retained low-error stage

\[
\boxed{
A_m
:=
\int_I n^T\bar\Sigma_\phi n\,ds
\ge a_m>0,
}
\]

where, up to endpoint and transport/diffusion/covariance errors,

\[
a_m\simeq\log q.
\]

Since

\[
\bar\Sigma_\phi=\mu^{-1}\int\phi\Sigma,
\]

this is equivalently

\[
\boxed{
\int_I\int\phi\,m^2 n^T\Sigma n\,dy\,ds
\ge
m_-^2\mu a_m.
}
\]

## 3. Replace mean-direction production by actual vortex stretching

Define

\[
q(y,s):=\Omega^T\Sigma\Omega.
\]

Expand

\[
q
=m^2n^T\Sigma n
+2m\,n^T\Sigma\delta\Omega
+\delta\Omega^T\Sigma\delta\Omega.
\]

Hence

\[
\begin{aligned}
\left|
\int\phi
\left[q-m^2n^T\Sigma n\right]
\right|
&\le
2m
\left(\int\phi|\Sigma|^2\right)^{1/2}
\left(\int\phi|\delta\Omega|^2\right)^{1/2}\\
&\quad+
\|\Sigma\|_{L^\infty(\operatorname{supp}\phi)}
\int\phi|\delta\Omega|^2.
\end{aligned}
\]

If the pure smooth corridor has

\[
\int\phi|\Sigma|^2\le E_{\Sigma,+},
\qquad
\|\Sigma\|_\infty\le B_{\Sigma,+},
\]

then using the plateau variance bound gives the integrated error ceiling

\[
\boxed{
|\mathcal E_q|
\le
2m_+\sqrt{E_{\Sigma,+}}\,
(m_+\sqrt{\mu\varepsilon_\Omega})L
+
B_{\Sigma,+}m_+^2\mu\varepsilon_\Omega L.
}
\]

More abstractly define the stage source-transfer error `e_q` by

\[
\boxed{
\left|
\int_I\int\phi q
-
\int_I\int\phi m^2n^T\Sigma n
\right|
\le e_q.
}
\]

Then

\[
\boxed{
\int_I\int\phi q
\ge
m_-^2\mu a_m-e_q.
}
\]

If

\[
\boxed{a_q:=m_-^2\mu a_m-e_q>0,}
\]

the plateau carries a fixed positive actual vortex-stretching source action.

## 4. Positive source action -> positive-middle or Betchov residual

Split the source-positive set by the sign of the middle strain eigenvalue:

\[
E_+=\{q>0,\ \lambda_2(\Sigma)>0\},
\qquad
E_-=\{q>0,\ \lambda_2(\Sigma)\le0\}.
\]

On `E_-`, trace-free strain has `det Sigma>=0`. Therefore

\[
\boxed{
q+4\det\Sigma\ge q>0.
}
\]

Consequently

\[
\boxed{
\int_{I\times E_+}\phi q
+
\int_{I\times E_-}\phi(q+4\det\Sigma)
\ge a_q.
}
\]

Hence either

\[
\boxed{
\int_{I\times E_+}\phi q
\ge \frac{a_q}{2}
}
\]

or

\[
\boxed{
\int_{I\times E_-}\phi(q+4\det\Sigma)
\ge \frac{a_q}{2}.
}
\]

The second is exactly the localized Betchov mismatch and enters the existing buffer strain-energy / derivative / residual gate.

Thus on a Betchov-residual-quiet plateau corridor, a fixed fraction of the source action must lie on the **positive-middle source-active set**.

## 5. Alignment-free transverse action on the positive-middle source set

At a point with `q>0`, define the actual vorticity direction

\[
\xi=\Omega/|\Omega|,
\qquad
\gamma=\xi^T\Sigma\xi=\frac q{|\Omega|^2}>0.
\]

On the positive-middle set `lambda_2(Sigma)>=0`, the Cauchy interlacing lemma gives for the transverse trace-free restriction relative to `xi`

\[
\boxed{
|D_{full}|_F
\ge
\frac\gamma{\sqrt2}.
}
\]

Since `|Omega|<=1`,

\[
q=|\Omega|^2\gamma\le\gamma.
\]

Therefore

\[
\boxed{
|D_{full}|_F
\ge
\frac q{\sqrt2}
}
\]

on the positive-middle source set.

Integrating the positive-middle branch gives

\[
\boxed{
\int_I\int_{E_+}\phi|D_{full}|_F
\ge
\frac1{\sqrt2}
\int_I\int_{E_+}\phi q
\ge
\frac{a_q}{2\sqrt2}.
}
\]

Thus the retained coherent plateau supplies a fixed **space-time transverse action floor** unless it pays Betchov residual.

## 6. Return to the existing anti-ribbon/projective machinery

The positive-middle transverse action now enters the already derived alternatives:

\[
\boxed{
\text{transverse action}
\to
\text{ribbonization / shape change}
\lor
\text{eigenaxis rotation}
\lor
\text{material turnover}
\lor
\text{pressure/derivative residual}.
}
\]

The alignment-free nature of Section 5 is important: the plateau mean direction need not coincide with the strongest strain eigenvector.

Therefore the coherent annular plateau is not a new terminal leaf. Its quiet continuation is the same positive-middle transverse-action corridor already present in the main proof tree.

## 7. Corrected plateau routing

Combining the preceding steps,

\[
\boxed{
\begin{aligned}
\text{retained coherent plateau}
\Longrightarrow\;&
\text{mean-stretch action }\sim\log q\\
\Longrightarrow\;&
\text{actual vortex-stretching source action}\\
\Longrightarrow\;&
\text{positive-middle transverse action}\\
&\lor\text{Betchov buffer/residual}\\
&\lor\text{plateau covariance/transport/diffusive error}.
\end{aligned}
}
\]

Thus the low-derivative large-annular-mass survivor rejoins the existing finite-stage deformation/projective/H/T/residual closure matrix.

## 8. Remaining quantitative issue

The new bridge is structural and exact up to explicit threshold errors. The remaining task is a constant comparison:

1. lower-bound `m_-` and the retained mean-stretch action `a_m` from the plateau/Poincare geometry;
2. upper-bound the source-transfer error `e_q` by the local variance/strain ceilings;
3. compare the resulting transverse action floor `a_q/(2sqrt(2))` with the existing anti-ribbon/projective finite-stage thresholds.

Status: **A COHERENT LOW-DERIVATIVE ANNULAR PLATEAU THAT RETAINS ITS NORMALIZED MEAN ACROSS A GEOMETRIC FIRST-HITTING STAGE MUST GENERATE ACTUAL POSITIVE VORTEX-STRETCHING ACTION. UNLESS A LOCAL BETCHOV MISMATCH IS LARGE, A FIXED FRACTION OF THIS SOURCE ACTION LIES IN THE POSITIVE-MIDDLE GEOMETRY AND FORCES ALIGNMENT-FREE TRANSVERSE ACTION. THE PLATEAU BRANCH THEREFORE REJOINS THE EXISTING ANTI-RIBBON/PROJECTIVE MAINLINE; ONLY THE CONSTANT TRANSFER REMAINS. GLOBAL REGULARITY REMAINS UNPROVED.**