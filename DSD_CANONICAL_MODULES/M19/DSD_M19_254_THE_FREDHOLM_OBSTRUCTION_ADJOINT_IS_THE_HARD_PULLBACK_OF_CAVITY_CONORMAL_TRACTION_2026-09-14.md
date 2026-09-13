# M19-254 — The Fredholm obstruction adjoint is the hard pullback of cavity conormal traction

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / EXACT GREEN-BOUNDARY IDENTIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-253 defines the exact hard boundary obstruction map

\[
\mathcal O_R:\mathscr C_R^{hard}\to K_R,
\qquad
K_R:=\ker(I-M_R^*),
\]

and reduces the desired physical adjoint realization to

\[
\ell_B\notin\operatorname{Ran}\mathcal O_R^*.
\]

This module identifies \(\mathcal O_R^*\) physically. Its rows are not abstract cavity coordinates: they are exactly the hard pullbacks of the conormal tractions of primal zero-boundary cavity unit modes.

## 2. Primal cavity unit mode associated with an obstruction vector

Let

\[
\varphi\in K_R=\ker(I-M_R^*).
\]

Undoing the time reversal/adjoint identification used in M19-230, \(\varphi\) generates a primal zero-Dirichlet relative-periodic cavity mode

\[
W_\varphi(s,y),
\qquad y\in B_R,
\]

satisfying the linearized primal system

\[
\partial_sW_\varphi
=\nu\Delta W_\varphi
-\left(\frac y2+U\right)\cdot\nabla W_\varphi
-\frac12W_\varphi
-(W_\varphi\cdot\nabla)U
-\nabla p_\varphi,
\]

\[
\nabla\cdot W_\varphi=0,
\qquad
W_\varphi|_{S_R}=0,
\]

with the same relative closing holonomy as the monodromy construction.

The normalization of \(W_\varphi\) is immaterial for the row-space identification.

## 3. Physical adjoint field from a hard boundary datum

Let

\[
C\in\mathscr C_R^{hard}
\]

be a retained hard critical dual datum. Let

\[
g_R(C)(s,\omega)
\]

be its transported physical adjoint Dirichlet trace on the spectator sphere, supplied by the M19-227--229 remote dual transport/finite-spectator construction.

Write

\[
\mathscr T_R:\mathscr C_R^{hard}\to\mathscr G_R,
\qquad
\mathscr T_RC=g_R(C),
\]

for this finite-dimensional hard-to-boundary trace map.

Any interior lifting of \(g_R(C)\) gives the same Fredholm obstruction by M19-253.

## 4. Finite-domain Green identity

Let \(\Psi_C\) be any adjoint solution candidate with boundary trace

\[
\Psi_C|_{S_R}=g_R(C).
\]

For a primal/adjoint pair, integration by parts gives the finite-domain Green identity

\[
\frac d{ds}\langle W_\varphi,\Psi_C\rangle_{B_R}
=
\mathfrak B_R[W_\varphi,\Psi_C],
\]

where the full boundary concomitant contains viscous, pressure, and drift pieces.

Because

\[
W_\varphi|_{S_R}=0,
\]

all boundary terms containing \(W_\varphi\) itself vanish. The remaining term is

\[
\boxed{
\mathfrak B_R[W_\varphi,\Psi_C]
=
\int_{S_R}
\big(\nu\partial_nW_\varphi-p_\varphi n\big)
\cdot g_R(C)\,dS,
}
\]

up to the globally fixed sign convention for the primal/adjoint Green form.

Define the primal cavity conormal traction

\[
\boxed{
\tau_R(W_\varphi)
:=
u\partial_nW_\varphi-p_\varphi n.
}
\]

Using the symmetric-stress convention instead changes the representative by the standard incompressible boundary identity; the resulting Green functional is the same once the convention is fixed consistently.

## 5. One-period closure identifies the Fredholm pairing

Integrate the Green identity over one relative period. The interior endpoint pairing cancels under the matched relative holonomy. What remains is exactly the failure of the inhomogeneous adjoint correction to satisfy the Fredholm condition.

Therefore, with the same fixed sign convention as in M19-230,

\[
\boxed{
\langle h_R(C),\varphi\rangle
=
\int_0^S\int_{S_R}
\tau_R(W_\varphi)\cdot g_R(C)\,dS\,ds.
}
\]

A global minus sign may appear if the opposite Green orientation is chosen; it has no effect on kernels or row spaces.

This identity is independent of the interior lifting by M19-253 and depends only on the physical boundary trace.

## 6. Exact formula for the obstruction adjoint

Let the boundary trace space carry the natural period-integrated \(L^2\) pairing. Then

\[
\langle\mathcal O_RC,\varphi\rangle_{K_R}
=
\langle\mathscr T_RC,\tau_R(W_\varphi)\rangle_{\partial}.
\]

Hence

\[
\boxed{
\mathcal O_R^*\varphi
=
\mathscr T_R^*\tau_R(W_\varphi),
}
\]

again up to the fixed global sign convention.

Thus \(\mathcal O_R^*\varphi\) is exactly the **hard component of the cavity conormal traction**, pulled back from the spectator sphere to the hard critical-dual coordinate space.

## 7. Row-space interpretation

Define the cavity hard-export map

\[
\boxed{
\mathcal E_R:K_R\to(\mathscr C_R^{hard})^*,
\qquad
\mathcal E_R\varphi
:=\mathscr T_R^*\tau_R(W_\varphi).
}
\]

Then

\[
\boxed{
\operatorname{Ran}\mathcal O_R^*
=
\operatorname{Ran}\mathcal E_R.
}
\]

M19-253's exact compatibility criterion becomes

\[
\boxed{
\exists C\text{ physically extendible with }\ell_B(C)\neq0
\iff
\ell_B\notin\operatorname{Ran}\mathcal E_R.
}
\]

After the hard inner-product identification,

\[
\boxed{
B\notin\operatorname{Ran}\mathcal E_R.
}
\]

Therefore the actual obstruction is not merely “a cavity unit mode exists.” It is:

\[
\boxed{
\text{cavity unit modes export enough hard conormal trace to span the target critical functional }B.
}
\]

## 8. Unique continuation gives only full-traction injectivity, not hard-export injectivity

If a zero-Dirichlet cavity mode also had full conormal traction

\[
\tau_R(W_\varphi)=0
\]

on an open boundary-time set, parabolic unique continuation/overdetermined boundary rigidity would force the corresponding mode to vanish under the standard hypotheses.

But the Fredholm row only sees

\[
\mathscr T_R^*\tau_R(W_\varphi),
\]

the finite hard projection of that traction. A nonzero traction may be orthogonal to every retained hard boundary datum.

Therefore

\[
\boxed{
\tau_R(W_\varphi)\neq0
\not\Rightarrow
\mathcal E_R\varphi\neq0.
}
\]

This prevents an invalid unique-continuation shortcut.

## 9. Core/escape interpretation at the boundary level

The M19-231 dichotomy can now be re-read in terms of the exported hard traction.

### Core-tight cavity obstruction

If \(W_{\varphi_j}\) retains a nonzero whole-space core limit as \(R_j\to\infty\), then the hard export \(\mathcal E_{R_j}\varphi_j\) must be compared with the scattering label of that whole-space limit. A separate hard-bundle membership/trace-persistence theorem is required.

### Escaping/decompactifying cavity obstruction

If \(W_{\varphi_j}\) escapes to the remote boundary, M19-232--252 constrain the shell geometry and local spectrum. The remaining exact question is whether its conormal traction can nevertheless maintain a fixed nonzero projection onto the finite hard trace space:

\[
\boxed{
\mathcal T_{export}^{decomp}:
\text{can an escaping/decompactifying cavity unit mode have }\mathcal E_{R_j}\varphi_j\to B_*\neq0
\text{ in the fixed finite hard space?}
}
\]

This is sharper than controlling the entire cavity mode.

## 10. Why weak escape is not enough

Weak convergence of the normalized cavity state to zero on compact sets does not imply

\[
\mathcal E_R\varphi\to0,
\]

because \(\mathcal E_R\) is a **boundary conormal** observable and M19-235 already shows that the boundary shear can grow like \(R^{1/2}\) in \(L^2(S_R\times[0,S])\) after normalization.

Thus

\[
\boxed{
\text{interior weak escape}
\neq
\text{hard boundary-export decay}.
}
\]

The M19-245--252 boundary-layer calculations are precisely relevant to this point.

## 11. Refined bounded-period target

The compatibility problem is now reduced to two boundary-export questions:

\[
\boxed{
\mathcal T_{cav}^{core-export}:
\text{identify the hard export of a core-tight cavity obstruction},
}
\]

and

\[
\boxed{
\mathcal T_{cav}^{decomp-export}:
\text{exclude a target-sized finite-hard export from an escaping/decompactifying cavity obstruction}.
}
\]

If the target functional \(B\) lies in neither exported row space for at least one sufficiently remote \(R\), the physical adjoint datum needed by M19-225/228 exists even if unrelated cavity unit modes survive.

## 12. Next target

There is a potentially shorter route than proving either export theorem for **every** remote radius. M19-230 needs physical extension at only one sufficiently remote spectator radius.

After unitary rescaling of \(B_R\) to \(B_1\), the zero-boundary monodromy becomes a compact operator family \(M_R\) on a fixed Hilbert space. If this family is analytic in \(R\), then the analytic Fredholm alternative plus the small-radius Poincare gap would imply that radii with a cavity unit multiplier are discrete. One could then choose a sufficiently remote nonresonant radius, for which

\[
K_R=\{0\},
\qquad
\mathcal O_R=0,
\]

and the affine adjoint extension is automatically solvable.

The next module will audit this radius-analytic Fredholm route and isolate exactly which analyticity statement must be certified before it can be used.

## 13. Scope firewalls

\[
\boxed{
\text{full boundary traction nonzero}
\neq
\text{nonzero finite-hard traction projection},
}
\[
\boxed{
\text{interior weak escape}
\neq
\text{hard boundary-export decay},
}
\[
\boxed{
\text{cavity unit mode exists}
\neq
\text{target hard functional is obstructed}.
}

Global regularity remains unproved.
