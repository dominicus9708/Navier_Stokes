# DSD M17-360 — Compact nondegenerate closed-loop orbit contains a recurrent minimal hull and returns to the M17-188 covariance payer

Date: 2026-09-08  
Canonical ID: **M17-360**

Status: **ACTIVE COMPACT-DYNAMICS REDUCTION / CLOSED-LOOP BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Loop-state orbit

By M17-359, on exact regular CE-H a closed material vortex loop remains the same material loop under the similarity flow until a nodal/interface/rank/domain exit occurs.

Represent the loop state by

\[
Z(\theta)
=
[\Gamma(\theta),\rho|_\Gamma,\sigma|_\Gamma,\kappa_\Gamma,\Phi_\Gamma]
\]

modulo harmless periodic reparameterization of the primitive loop.

Assume the retained branch is uniformly nondegenerate:

\[
0<\ell_*\le\ell_\Gamma(\theta)\le\ell^*<\infty,
\]

\[
0<L_*\le L_\rho(\theta)\le L^*<\infty,
\]

\[
0<\Phi_*\le\Phi_\Gamma(\theta)\le\Phi^*<\infty,
\]

and the full loop fields remain in a compact regular topology strong enough for the exact line laws and their integrands to pass to limits.

Failure of any of these assumptions is already a typed loop-state/cutoff/interface/geometry exit.

## 2. Compact orbit closure

Let

\[
\mathcal K
:=
\overline{\{Z(\theta):\theta\ge\theta_0\}}
\]

in the retained compact loop-state topology.

The CE-H material evolution induces a continuous semiflow on `K`.

The omega-limit set

\[
\omega(Z)
=
\bigcap_{T>0}
\overline{\{Z(\theta):\theta\ge T\}}
\]

is nonempty, compact, and forward invariant.

Inside it choose a nonempty compact minimal invariant subset

\[
\mathcal M\subset\omega(Z).
\]

## 3. Minimal compact states are recurrent

For any `z in M`, minimality means the forward orbit of `z` is dense in `M`.

Hence for every neighborhood `U` of `z` and every `T>0`, there exists `t>T` such that

\[
S_tz\in U.
\]

Thus every point in the minimal subsystem is recurrent.

Choose one such state `z_*` and recurrent times

\[
T_n\to\infty,
\qquad
S_{T_n}z_*\to z_*.
\]

Because all nondegeneracy bounds are closed under the compact limit, `z_*` still carries a nonzero regular closed material vortex loop with positive line weight and flux.

## 4. Exact loop laws on the recurrent limit orbit

M17-188 gives for one closed material vortex loop

\[
\frac d{d\theta}\log\ell_\Gamma
=
\bar\sigma_{ds}+\frac12,
\]

\[
\frac d{d\theta}\log\Phi
=
\kappa,
\]

and

\[
\frac d{d\theta}\log\frac{L_\rho}{\Phi}
=
2\bar\sigma_\rho-\frac12.
\]

Integrate these identities along the recurrent limit orbit from `0` to `T_n`.

Because

\[
S_{T_n}z_*\to z_*
\]

and the three positive observables remain continuous and bounded away from zero,

\[
\log\frac{\ell_\Gamma(T_n)}{\ell_\Gamma(0)}\to0,
\]

\[
\log\frac{\Phi(T_n)}{\Phi(0)}\to0,
\]

\[
\log\frac{(L_\rho/\Phi)(T_n)}{(L_\rho/\Phi)(0)}\to0.
\]

Dividing by `T_n` yields

\[
\boxed{
\langle\bar\sigma_{ds}\rangle=-\frac12,
}
\]

\[
\boxed{
\langle\kappa\rangle=0,
}
\]

and

\[
\boxed{
\langle\bar\sigma_\rho\rangle=\frac14.
}
\]

Therefore

\[
\boxed{
\left\langle
\bar\sigma_\rho-\bar\sigma_{ds}
\right\rangle
=\frac34.
}
\]

This is exactly the M17-188 recurrent covariance law.

## 5. Return to the gradient payer

M17-188 rewrites the difference as the normalized line covariance

\[
\bar\sigma_\rho-\bar\sigma_{ds}
=
\frac1{L_\rho}
\oint_\Gamma
(\sigma-\bar\sigma_{ds})(\rho-\bar\rho_{ds})ds.
\]

Circle Poincare plus the uniform loop bounds gives

\[
|\bar\sigma_\rho-\bar\sigma_{ds}|
\le
C_*
\|\partial_s\sigma\|_{L^2(ds)}
\|\partial_s\rho\|_{L^2(ds)}.
\]

Hence the recurrent minimal loop carries

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_2
\|\partial_s\rho\|_2
\right\rangle
\ge c_*>0,
}
\]

and therefore

\[
\boxed{
\left\langle
\|\partial_s\sigma\|_2^2
+
\|\partial_s\rho\|_2^2
\right\rangle
\ge2c_*>0.
}
\]

## 6. What this does and does not prove for the original orbit

The conclusion is a **compact-hull reduction**:

\[
\boxed{
\text{compact nondegenerate closed-loop orbit}
\Longrightarrow
\text{nontrivial recurrent CE-H loop in its omega-limit hull}
}
\]

and that recurrent limit loop necessarily carries the M17-188 payer.

This does not by itself prove that the original material loop spends positive density of time near that minimal subsystem, nor does it convert the normalized loop payer into a finite ancestral contradiction.

Those stronger statements are not imported.

## 7. Correct loop branch

Accordingly,

\[
\boxed{
\begin{aligned}
H_{closed\ material\ loop}
\Longrightarrow{}&
H_{recurrent\ hull\ covariance/gradient\ payer}\\
&\lor G_{loop\ state\ decompactification}\\
&\lor G_{nodal/cutoff/interface}\\
&\lor G_{CEH/rank/domain\ loss}.
\end{aligned}
}
\]

A merely nonrecurrent trajectory inside a compact nondegenerate loop-state space is not a separate terminal escape.

## 8. DSD-theory role

The heuristic is to distinguish failure of pointwise recurrence from failure of compact recurrent structure. The actual reduction is standard compact topological dynamics plus the exact M17-188 line identities.

No DSD axiom is used as a PDE hypothesis.

## 9. Audit verdict

**PASS as a compact-hull reduction.**

The closed-loop branch now ends at an explicit recurrent gradient payer or a named loss of compact regular loop structure.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
