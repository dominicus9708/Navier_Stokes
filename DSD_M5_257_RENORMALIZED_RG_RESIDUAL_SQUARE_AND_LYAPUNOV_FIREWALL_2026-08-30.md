# DSD M5-257 — Renormalized RG Residual Square and Lyapunov Firewall

Date: 2026-08-30

Parent: `DSD_M5_256_RESIDUAL_TWO_MOMENT_FIREWALL_AND_SHALLOW_RG_POSITIVITY_2026-08-30.md`

Status: **POSITIVE RENORMALIZED RESIDUAL INVARIANT / SHALLOW RG WORK DIVIDED BY RG DEPTH CONVERGES TO THE POSITIVE RESIDUAL SQUARE `||F_T||_2^2`; ON A COMPACT RESIDUAL-GAP MINIMAL HULL THIS GIVES A STRICTLY POSITIVE INVARIANT-MEAN RESIDUAL-SQUARE DENSITY / HOWEVER THIS POSITIVE DENSITY IS NOT THE TIME DERIVATIVE OF A KNOWN STATE FUNCTION, SO IT IS NOT A LYAPUNOV CONTRADICTION BY ITSELF / GLOBAL REGULARITY UNPROVED.**

---

## 1. Shallow work from M5-256

Let

\[
Q_\rho:=\mathscr R_\rho(T)-T
\]

for the exact RG reconstruction

\[
\partial_\rho\mathscr R_\rho(T)
=-\mathcal F(\mathscr R_\rho(T)),
\qquad
F_T:=\mathcal F(T).
\]

M5-256 gives

\[
Q_\rho=-\rho F_T+o_{L2}(\rho).
\]

Therefore

\[
-\langle F_T,Q_\rho\rangle
=
\rho\|F_T\|_2^2+o(\rho).
\]

---

## 2. Define the renormalized residual-work density

For `rho>0`, define

\[
\boxed{
\mathscr W_\rho(T)
:=
\frac{-\langle F_T,Q_\rho\rangle}{\rho}.
}
\]

Then

\[
\boxed{
\lim_{\rho\downarrow0}
\mathscr W_\rho(T)
=
\|F_T\|_2^2.
}
\]

Thus the first nontrivial RG work coefficient is positive definite.

---

## 3. Equivalent second-order RG separation

Also

\[
\|Q_\rho\|_2^2
=
\rho^2\|F_T\|_2^2+o(\rho^2).
\]

Hence

\[
\boxed{
\lim_{\rho\downarrow0}
\frac{\|\mathscr R_\rho(T)-T\|_2^2}{\rho^2}
=
\|F_T\|_2^2.
}
\]

The residual square is therefore both

1. the renormalized shallow signed work;
2. the quadratic coefficient of RG departure from the canonical tail.

---

## 4. Residual-gap invariant mean

Suppose the residual-active minimal tail hull has a uniform `L2` residual floor on the selected fixed-cell/compatible-extension norm:

\[
\boxed{
\|F_T\|_2\ge f_0>0
\qquad(T\in\mathcal T_{gap}).
}
\]

Then for every invariant probability measure `mu` on this hull,

\[
\boxed{
\int\|F_T\|_2^2d\mu(T)
\ge f_0^2>0.
}
\]

By uniform shallow-RG convergence on the compact hull, for sufficiently small fixed `rho_*`,

\[
\boxed{
\int\mathscr W_{\rho_*}(T)d\mu(T)
\ge\frac12f_0^2.
}
\]

Thus the residual-gap branch carries a positive **renormalized work density per unit RG depth**.

---

## 5. Dilation/log-radius covariance

On a canonical log cell, dilation acts as translation in `y=log r`. The critical residual norm is chosen in the corresponding scale-invariant cell normalization.

Therefore the residual-square observable is transported covariantly along the minimal tail translation flow.

For an ergodic invariant measure, Birkhoff averaging gives the spatial/log-radial interpretation

\[
\boxed{
\lim_{L\to\infty}
\frac1L
\int_0^L
\|F_{D_yT}\|_{2,cell}^2dy
=
\int\|F_T\|_{2,cell}^2d\mu(T)
>0
}
\]

for almost every tail state in that component.

Thus the residual-gap branch has positive density on logarithmic scales, not merely isolated residual events.

---

## 6. Why this still does not give a contradiction

A positive function `g(T)>0` on a compact recurrent orbit does not contradict recurrence unless one proves that

\[
g(T(s))
=-\frac{d}{ds}\mathcal L(T(s))
\]

for a bounded single-valued state functional `mathcal L`, or obtains another non-summable monotone budget.

Here

\[
\|F_T\|_2^2
\]

is the square of the **RG vector field at the tail boundary**, not a known gradient-flow dissipation for the W1 time dynamics.

The RG evolution

\[
\partial_\rho\mathscr R_\rho=-\mathcal F(\mathscr R_\rho)
\]

is backward-parabolic reconstruction in `rho`; it is not the same flow as the recurrent Leray time translation.

Therefore

\[
\boxed{
\text{positive RG residual square}
\not\Rightarrow
\text{strict Leray-time Lyapunov decay}.
}
\]

---

## 7. Relation to physical energy summability

The critical residual on a radius-`R` physical cell scales like `R^-3`, while the first finite-scale correction carries another `R^-2` RG factor relative to the leading tail.

Hence the unweighted physical work per geometric shell decays by a positive power of `R` and remains summable.

Thus positive log-density of the **renormalized** residual square does not contradict finite physical energy.

---

## 8. What the positive residual square does accomplish

It converts the residual-active branch into a robust quantitative certificate:

\[
\boxed{
A_{min}^{aper,\,res}
\Longrightarrow
\overline{\|F_T\|_{2,crit}^2}
\ge f_0^2>0.
}
\]

Combined with M5-248, this certificate survives to one fixed finite RG depth and then to finite first-hitting stages.

Therefore any final closure may use it as a genuine positive-density PDE defect, rather than the weaker statement `F_T !=0`.

---

## 9. DSD firewall

The following implication is RED without a new identity:

\[
\boxed{
\overline{\|F_T\|^2}>0
\Longrightarrow
\text{monotone energy loss in Leray time}.
}
\]

Likewise, RG depth `rho` must not be identified with Leray time `s`.

---

## 10. Updated residual-active endpoint

The residual-active minimal branch now satisfies simultaneously

\[
\boxed{
\begin{aligned}
&\text{compact minimal log-translation dynamics},\\
&\inf_T\mathbf F(T)>0,\\
&\overline{\|F_T\|_{2,crit}^2}>0,\\
&\text{positive shallow velocity and curl residual work},\\
&\text{finite-depth/finite-stage inheritance},\\
&\text{quotient }H^{-1}/L2/H1\text{ frequency chain},\\
&\text{M5-250/M5-255 recurrent balance constraints}.
\end{aligned}
}
\]

This is considerably narrower than a generic aperiodic tail, but it is not yet empty.

---

## 11. Next target

At this point the most useful new ingredient would be one of:

1. a state functional whose Leray-time derivative controls the RG residual square;
2. a spectral/nondegeneracy theorem showing that the compact minimal tail hull cannot remain uniformly separated from the stationary set while satisfying the W1 reconstruction constraints;
3. a quantitative comparison putting `C_rel<1/4` or `K_-<nu/12` from inherited first-hitting bounds.

Without one of these, further positive lower bounds alone will not close the branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
