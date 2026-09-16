# DSD M19-354 — Scale-free bi-Lipschitz compactness in the M17-448 chart transports the reference log-Sobolev bound and closes persistent sign-flux thinning

Date: 2026-09-16  
Canonical ID: **M19-354**

Status: **ACTIVE GEOMETRY-BRIDGE THEOREM / M17-448 REIMPORT / THINNING CLOSURE ON SHAPE-COMPACT BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-448 and M19-353

M17-448 represents a retained transverse cross-section as a \(C^1\) bi-Lipschitz image

\[
F_R:A_0\to A_R
\]

of one fixed connected reference cross-section \(A_0\).

M17-449 then warns that the dimensional growth of the cross-section must be separated from scale-free shape degeneration.

On the M17-450 diffuse baseline,

\[
|A_R|\asymp R.
\]

M19-353 shows that persistent sign-flux thinning is excluded if the scaled cross-sections satisfy the uniform two-dimensional log-Sobolev family

\[
\|f-c\|_{L^q(A_R)}
\lesssim
\sqrt q\,|A_R|^{1/q}
\|\nabla f\|_{L^2(A_R)}
\]

with record-independent constants.

The present module derives this estimate from the size-normalized M17-448 bi-Lipschitz chart.

## 2. Factor out isotropic transverse size

Set

\[
\boxed{
\lambda_R
:=
\left(
\frac{|A_R|}{|A_0|}
\right)^{1/2}.
}
\]

On the baseline \(|A_R|\asymp R\),

\[
\lambda_R\asymp R^{1/2}.
\]

Write

\[
\boxed{
F_R=\lambda_R\widetilde F_R.
}
\]

The map \(\widetilde F_R:A_0\to\widetilde A_R:=\lambda_R^{-1}A_R\) carries only the scale-free shape distortion.

Define the scale-free bi-Lipschitz compactness package

\[
\boxed{
0<m_*
\le
s_i(D\widetilde F_R)
\le
M_*<\infty
}
\]

uniformly in the retained record family.

Failure is a normalized geometry decompactification, not ordinary transverse size growth.

## 3. Reference two-dimensional Sobolev-q estimate

On the fixed regular reference domain \(A_0\), the standard two-dimensional Sobolev/Moser--Trudinger family gives

\[
\boxed{
\inf_{c\in\mathbb R}
\|g-c\|_{L^q(A_0)}
\le
C_0\sqrt q
\|\nabla g\|_{L^2(A_0)},
\qquad q\ge2.
}
\]

The exact optimal constant is irrelevant; only its independence of \(R\) matters.

## 4. Transport the Lq norm

Let \(f\) be a scalar on \(A_R\) and define

\[
g:=f\circ F_R.
\]

For any constant \(c\),

\[
\|f-c\|_{L^q(A_R)}^q
=
\lambda_R^2
\int_{A_0}|g-c|^qJ_{\widetilde F_R}da.
\]

The normalized singular-value bounds give

\[
m_*^2
\le
J_{\widetilde F_R}
\le
M_*^2.
\]

Therefore

\[
\boxed{
\|f-c\|_{L^q(A_R)}
\le
\lambda_R^{2/q}M_*^{2/q}
\|g-c\|_{L^q(A_0)}.
}
\]

## 5. Transport the Dirichlet energy

By the chain rule,

\[
\nabla g
=
\lambda_R
D\widetilde F_R^T
(\nabla f)\circ F_R.
\]

Hence

\[
|\nabla g|
\le
\lambda_RM_*
|\nabla f|\circ F_R.
\]

Also

\[
dx
=
\lambda_R^2
J_{\widetilde F_R}da
\ge
\lambda_R^2m_*^2da.
\]

Thus

\[
\boxed{
\|\nabla g\|_{L^2(A_0)}
\le
\frac{M_*}{m_*}
\|\nabla f\|_{L^2(A_R)}.
}
\]

The isotropic scale \(\lambda_R\) cancels exactly, as expected from two-dimensional conformal scaling of Dirichlet energy.

## 6. Uniform transported log-Sobolev estimate

Combine Sections 3--5:

\[
\inf_c
\|f-c\|_{L^q(A_R)}
\le
C_0
M_*^{2/q}
\frac{M_*}{m_*}
\sqrt q\,\lambda_R^{2/q}
\|\nabla f\|_2.
\]

Because

\[
|A_R|^{1/q}
=
|A_0|^{1/q}\lambda_R^{2/q},
\]

all fixed reference factors can be absorbed into one constant. Therefore

\[
\boxed{
\inf_{c\in\mathbb R}
\|f-c\|_{L^q(A_R)}
\le
C_{LS}
\sqrt q\,|A_R|^{1/q}
\|\nabla f\|_{L^2(A_R)},
\qquad q\ge2,
}
\]

with \(C_{LS}\) depending only on \(A_0,m_*,M_*\), not on \(R\).

This is exactly the functional input of M19-353.

## 7. Consequence for sign-flux thinning

Under the additional M19-353 assumptions

\[
|A_R|\lesssim R,
\qquad
\rho\le M_\rho,
\qquad
\ell_R\lesssim R,
\]

and the persistent sign-enstrophy floor, M19-353 gives for a thinning sign flux fraction \(\eta_R\) present on parent-time fraction \(\gamma_R\),

\[
\boxed{
\mathcal P_{anc,R}
\gtrsim
\frac{\gamma_R}{\eta_R^2\log R}.
}
\]

Thus if

\[
\gamma_R\ge\gamma_*>0
\]

along geometric records and

\[
\eta_R\to0,
\]

finite ancestral palinstrophy is impossible.

Hence

\[
\boxed{
\text{persistent sign-flux thinning is closed on the scale-free bi-Lipschitz compact branch.}
}
\]

## 8. Exact geometry exit

The remaining geometric escape is not ordinary baseline size growth \(\lambda_R\sim R^{1/2}\).

It is

\[
\boxed{
G_{\rm scale\text{-}free\ bi\text{-}Lipschitz\ distortion}:
\quad
m_R^{norm}\to0
\quad\text{or}\quad
M_R^{norm}\to\infty,
}
\]

where

\[
m_R^{norm}:=\inf s_i(D\widetilde F_R),
\qquad
M_R^{norm}:=\sup s_i(D\widetilde F_R).
\]

This refines the M17-448/449 geometry branch after the mandatory mesoscopic size factor has been divided out.

## 9. Relation to the scale-free Poincare factor

Uniform scale-free bi-Lipschitz compactness implies bounded M17-449 shape factor \(\Pi_R\).

The converse is not asserted.

A single global spectral-gap number need not control all local distortion or small-set Sobolev constants.

Thus the hierarchy is

\[
\boxed{
\text{scale-free bi-Lipschitz compactness}
\Longrightarrow
\text{uniform transverse log-Sobolev}
\Longrightarrow
\text{bounded scale-free Poincare},
}
\]

with no reverse implication claimed by M19-354.

## 10. Material deformation interpretation

M17-448 and M17-423 relate bi-Lipschitz distortion to integrated strain.

If \(F_R\) is the material image of a retained reference cross-section, severe normalized distortion requires growth of the condition number of the material deformation gradient and hence logarithmic strain action.

However M17-423 already establishes that logarithmic strain growth across geometric records is compatible with the standard-energy ancestry weight.

Therefore

\[
\boxed{
G_{\rm scale\text{-}free\ bi\text{-}Lipschitz\ distortion}
\not\Rightarrow
\text{current standard-energy contradiction}.
}
\]

It remains a genuine named geometry exit.

## 11. Updated mixed-sign thinning split

\[
\boxed{
\begin{aligned}
G_{\rm sign\text{-}flux\ thinning}
\Longrightarrow{}&
G_{\rm palinstrophy\ ancestry\ contradiction}\\
&\lor G_{\rm scale\text{-}free\ bi\text{-}Lipschitz\ distortion}\\
&\lor G_{\rm transverse\ size\ excess}\\
&\lor G_{\rm super\text{-}parent\ line\ length/folding}\\
&\lor G_{\rm amplitude/high\text{-}jet\ loss}\\
&\lor G_{\rm parent\text{-}time\ thinning}\\
&\lor G_{\rm common\ section/genealogy/interface\ loss}.
\end{aligned}
}
\]

Thus the internal sparse-residence mechanism is no longer an independent compact survivor.

## 12. Audit verdict

**PASS — M19-353's log-Sobolev gate is supplied by the size-normalized M17-448 bi-Lipschitz compact branch.**

Once the unavoidable isotropic area factor \(|A_R|\asymp R\) is removed, bounded scale-free bi-Lipschitz distortion transports the fixed-reference two-dimensional logarithmic Sobolev estimate uniformly. Persistent sign-flux thinning then violates the favorable palinstrophy ancestry ledger.

The hard residue is explicit scale-free transverse distortion or one of the already named size/length/time/genealogy exits, not an unexplained sparse-residence state.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
