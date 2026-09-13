# M19-191 — Type-I, weak-L3 and bounded shell frequency quantitatively imply bounded normalized enstrophy inside the simultaneous W1 subcorridor

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / INTERNAL HYPOTHESIS REDUNDANCY / M18-042 PARTIAL REFINEMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-042 classified bounded normalized enstrophy

\[
H_Z:\quad Z(s)=\int|\Omega|^2dy\le Z_+
\]

as a genuine W1 case-survivor condition.

M19-188 correctly observed that M18-042 by itself does not supply the **smallness** needed by M19-187/190.

The present module asks a narrower question:

> once the W1 Type-I, weak-L3, and bounded shell-frequency conditions hold simultaneously, is mere boundedness of `Z` still independent?

The answer is no.

## 2. Core enstrophy from Type-I vorticity amplitude

The retained Type-I condition is

\[
(T_*-t)\|\omega(t)\|_\infty\le K_I.
\]

In similarity variables

\[
\Omega(y,s)=(T_*-t)\omega(x,t),
\]

so

\[
\boxed{
\|\Omega(s)\|_\infty\le K_I.
}
\]

Therefore on the unit similarity ball,

\[
\boxed{
\int_{B_1}|\Omega|^2dy
\le C K_I^2.
}
\]

## 3. Lorentz control of shell L2 velocity

Let

\[
W_*:=\sup_s\|U(s)\|_{L^{3,\infty}}<\infty.
\]

On a shell `A_R^*` of volume comparable to `R^3`, finite-measure Lorentz embedding gives

\[
\|U\|_{L^2(A_R^*)}
\le C|A_R^*|^{1/6}W_*
\le C R^{1/2}W_*.
\]

If `m_R` is the shell average (or the retained comparable Campanato mean), then

\[
|m_R|\,|A_R^*|^{1/2}
\le C R^{1/2}W_*.
\]

Hence

\[
\boxed{
\|U-m_R\|_{L^2(A_R^*)}
\le C R^{1/2}W_*.
}
\]

No strong `L^p`, `p>3`, upgrade is needed for this estimate.

## 4. Shell-frequency control gives tail enstrophy

The W1 frequency ratio is

\[
\Gamma_R
:=
\frac{R\|\nabla(U-m_R)\|_{L^2(A_R^*)}}
{\|U-m_R\|_{L^2(A_R^*)}}
\le\Gamma_*.
\]

Since `m_R` is spatially constant,

\[
\nabla(U-m_R)=\nabla U.
\]

Therefore

\[
\|\nabla U\|_{L^2(A_R^*)}
\le
\frac{\Gamma_*}{R}
\|U-m_R\|_{L^2(A_R^*)}
\le
C\Gamma_*W_*R^{-1/2}.
\]

Squaring,

\[
\boxed{
\int_{A_R^*}|\nabla U|^2dy
\le
C\Gamma_*^2W_*^2R^{-1}.
}
\]

Since

\[
|\Omega|=|\nabla\times U|\le C|\nabla U|,
\]

we get the same shell bound for vorticity enstrophy.

## 5. Dyadic tail summation

Choose `R_k=2^k`, `k>=0`. The enlarged shells have bounded overlap and cover the exterior region.

Then

\[
\int_{|y|\ge1}|\Omega|^2dy
\le
C\Gamma_*^2W_*^2
\sum_{k=0}^\infty2^{-k}.
\]

Hence

\[
\boxed{
\int_{|y|\ge1}|\Omega|^2dy
\le C\Gamma_*^2W_*^2.
}
\]

Combining core and tail,

\[
\boxed{
Z(s)
\le
C_Z\left(K_I^2+\Gamma_*^2W_*^2\right)
\qquad\forall s.
}
\]

Thus one may take

\[
\boxed{
Z_+
\le
C_Z\left(K_I^2+\Gamma_*^2W_*^2\right).
}
\]

## 6. Precise logical refinement of M18-042

Inside the **simultaneous** corridor

\[
H_I\cap H_F\cap H_W,
\]

we have

\[
\boxed{
H_I+H_F+H_W
\Longrightarrow H_Z.
}
\]

Therefore bounded normalized enstrophy is not internally independent once those three W1 controls are already available.

## 7. Why this does not erase the upstream Z root

The existing repository routes establishing `H_F` and `H_W` on broad upstream states use corridor information that can itself depend on bounded enstrophy / Campanato control.

Therefore using M19-191 to delete `H_Z` from the global ROOT-CERT entry map without reworking those upstream routes would be circular.

The correct statement is

\[
\boxed{
\text{internal W1 redundancy}
\neq
\text{global upstream elimination of the Z-escalation root}.
}
\]

M18-042 remains authoritative for ROOT-CERT bookkeeping until the entry routes are re-audited, but its primitive-set description is sharpened inside the final simultaneous W1 lane.

## 8. Insert into the M19-190 aperiodicity criterion

M19-190 excludes genuine aperiodic recurrence if

\[
K_*^{(5)}\frac{Z_+^2}{\nu^3}<\frac14.
\]

M19-191 gives the explicit sufficient corridor condition

\[
\boxed{
K_*^{(5)}C_Z^2
\frac{\left(K_I^2+\Gamma_*^2W_*^2\right)^2}{\nu^3}
<\frac14
\Longrightarrow
\text{no genuine aperiodic recurrent hard branch}.
}
\]

Thus the remaining high-enstrophy branch can be re-expressed as a large finite combination of the Type-I amplitude, shell-frequency ceiling, and weak-L3 ceiling.

## 9. New quantitative hard branch

If genuine aperiodic recurrence survives, then necessarily

\[
\boxed{
K_I^2+\Gamma_*^2W_*^2
\ge
c_*\nu^{3/2}
}
\]

for an explicit constant `c_*` determined by `K_*^(5)` and `C_Z`.

This does not yet imply escalation to infinity. It is a large-but-finite amplitude/frequency endpoint.

---

\[
\boxed{\text{M19-191: BOUNDED Z IS DERIVED INSIDE THE SIMULTANEOUS TYPE-I + WEAK-L3 + BOUNDED-FREQUENCY W1 LANE.}}
\]
