# DSD M19-079 — Remote spectator damping forces every bounded zero-growth linearized mode to carry a positive long-time energy fraction in one finite active core

**Date:** 2026-09-12  
**Status:** POSITIVE CENTER-OBSERVABILITY REDUCTION / GLOBAL COMPACTNESS FAILS, BUT A GENUINE BOUNDED NEUTRAL MODE CANNOT LIVE ENTIRELY AT SIMILARITY INFINITY ON THE QUIET WEAK-CRITICAL CORRIDOR / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-077 and M19-078 showed that neither polynomial \(A_2\) smoothing nor Gaussian-vorticity confinement yields a globally compact phase space compatible with the nonlocal Navier--Stokes structure.

Those counterexamples use arbitrary bounded sequences translated to larger and larger similarity radii.

A true center mode is much more constrained: it must solve the linearized equation for all time and have zero exponential growth.

The present module asks a weaker, more targeted question:

> Does strict damping in the remote spectator region force every bounded neutral trajectory to spend a definite fraction of its weighted energy in one fixed finite core?

On the retained quiet spectator corridor, the answer is yes.

## 2. Linearized similarity equation

Let \(U(y,\theta)\) be a complete recurrent similarity trajectory and let \(W\) solve

\[
\boxed{
\partial_\theta W
+\frac12W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
+(W\cdot\nabla)U
=-\nabla Q+\nu\Delta W,
\qquad
\nabla\cdot W=0.
}
\]

The pressure variation obeys

\[
\boxed{
-\Delta Q
=\partial_i\partial_j
\bigl(U_iW_j+W_iU_j\bigr).
}
\]

Use the pressure-compatible polynomial weight from M19-063,

\[
\boxed{
w(y)=(1+\kappa|y|^2)^{-a/2}},
\qquad 1<a<3,
\]

with parameters chosen in the certified positive-gap corridor.

Define

\[
E(\theta):=\int_{\mathbb R^3}|W|^2w\,dy,
\qquad
G(\theta):=\int_{\mathbb R^3}|\nabla W|^2w\,dy.
\]

The free weighted similarity operator has

\[
\boxed{
\frac12E'
+\nu G
+c_{gap}E
\le
\text{background transport/strain/pressure defects},
}
\]

for some

\[
c_{gap}>0.
\]

## 3. Quiet spectator coefficient decay

On the controlled weak-critical spectator branch, the strong far-field norm used in M19-069 gives, for sufficiently large \(r=|y|\),

\[
\boxed{
|U(y,\theta)|\le \frac{C_U}{r},
\qquad
|\nabla U(y,\theta)|\le \frac{C_1}{r^2},
}
\]

uniformly in \(\theta\) along the compact recurrent corridor.

Failure of these uniform coefficient bounds is not silently absorbed here. It is the already typed derivative/remote/localization decompactification branch.

For the weight,

\[
\lambda_w(y)
:=\frac{|\nabla w|}{w}
=
\frac{a\kappa r}{1+\kappa r^2},
\]

so

\[
\boxed{
\lambda_w(y)\lesssim r^{-1}
\qquad(r\gg1).
}
\]

Hence all local coefficient defects become small at large similarity radius.

## 4. Core/outside decomposition

Fix \(R\gg1\) and set

\[
E_c(\theta;R)
:=
\int_{|y|\le R}|W|^2w\,dy,
\]

\[
E_o(\theta;R)
:=
\int_{|y|>R}|W|^2w\,dy.
\]

Then

\[
E=E_c+E_o.
\]

No derivative cutoff is inserted into the energy identity. We split only the already integrated lower-order defect terms, so there is no artificial collar-gradient payer.

## 5. Transport defect is remote-small

Because \(\nabla\cdot U=0\),

\[
\int (U\cdot\nabla)W\cdot W\,w
=
-\frac12
\int |W|^2U\cdot\nabla w.
\]

Therefore on \(|y|>R\),

\[
|U|\,\lambda_w
\lesssim R^{-2}.
\]

Inside \(B_R\), compactness of the retained trajectory gives a finite constant \(K_{tr}(R)\).

Hence

\[
\boxed{
|I_{tr}|
\le
C R^{-2}E_o
+K_{tr}(R)E_c.
}
\]

## 6. Strain defect is remote-small

The linearized stretching term is

\[
I_{str}
=
\int W_iW_j\partial_jU_i\,w\,dy.
\]

The spectator bound yields

\[
\boxed{
|I_{str}|
\le
C R^{-2}E_o
+K_{str}(R)E_c.
}
\]

Thus the positive recurrent stretching required for the background itself in M19-066 does not imply that a perturbation supported arbitrarily far away is neutrally stretched. At infinity the background strain is pointwise subcritical and decays like \(R^{-2}\).

## 7. Pressure defect can also be charged to outside-small plus core energy

The pressure contribution after weighted integration by parts has the form

\[
I_p
=
\int Q\,W\cdot\nabla w\,dy.
\]

Since \(w\in A_2\), weighted Calderón--Zygmund theory gives

\[
\boxed{
\|Q\|_{L^2(w)}
\le
C_{CZ}
\|UW\|_{L^2(w)}.
}
\]

Also

\[
|I_p|
\le
\|Q\|_{L^2(w)}
\|\lambda_wW\|_{L^2(w)}.
\]

Split both factors into core and exterior pieces. The exterior bounds are

\[
\|UW\|_{L^2(w;|y|>R)}
\le
C_UR^{-1}E_o^{1/2},
\]

\[
\|\lambda_wW\|_{L^2(w;|y|>R)}
\le
CR^{-1}E_o^{1/2}.
\]

The core factors are bounded by finite constants times \(E_c^{1/2}\).

Therefore, after Young's inequality, for every \(\varepsilon>0\) one may choose \(R=R(\varepsilon)\) sufficiently large so that

\[
\boxed{
|I_p|
\le
\varepsilon E_o
+K_p(R,\varepsilon)E_c.
}
\]

The nonlocal pressure does couple core and exterior, but its cross terms are precisely of the form

\[
E_c^{1/2}E_o^{1/2}
\]

and can be charged by Young to a small exterior coefficient plus a finite core coefficient.

## 8. Remote damping inequality

Combining the preceding estimates with the free weighted gap, choose \(R\) large enough that all exterior defects together are at most \(\varepsilon E_o\), with

\[
0<\varepsilon<c_{gap}.
\]

Absorb the finite core pieces into

\[
K_R<\infty.
\]

Then

\[
\boxed{
\frac12E'(\theta)
+\nu G(\theta)
+(c_{gap}-\varepsilon)E_o(\theta;R)
\le
K_RE_c(\theta;R).
}
\]

Dropping the nonnegative gradient term gives the weaker but central inequality

\[
\boxed{
\frac12E'
+c_*E_o
\le
K_RE_c,
\qquad
c_*:=c_{gap}-\varepsilon>0.
}
\]

This is a true remote-observability inequality for solutions of the linearized equation, not for arbitrary vectors in the phase space.

## 9. Long-time core occupation for bounded neutral modes

Assume \(W\) is a complete bounded linearized trajectory with

\[
\boxed{
\sup_{\theta\in\mathbb R}E(\theta)<\infty
}
\]

and nonvanishing mean weighted energy

\[
\boxed{
\overline E
:=
\liminf_{T\to\infty}
\frac1T\int_0^T E(\theta)\,d\theta
>0.
}
\]

This includes the natural recurrent symmetry modes and any additional bounded recurrent center candidate.

Integrate the remote damping inequality over \([0,T]\). Since \(E(T)-E(0)=O(1)\),

\[
\frac{E(T)-E(0)}{2T}\to0.
\]

Thus along a subsequence realizing the relevant time averages,

\[
\boxed{
 c_*\,\overline E_o
\le
K_R\,\overline E_c.
}
\]

Since

\[
\overline E=\overline E_c+\overline E_o,
\]

we obtain

\[
\boxed{
\frac{\overline E_c}{\overline E}
\ge
\delta_R
:=
\frac{c_*}{K_R+c_*}
>0.
}
\]

Equivalently,

\[
\boxed{
\overline E_c
\ge
\delta_R\,\overline E.
}
\]

A bounded nonzero neutral mode therefore cannot keep asymptotically all of its weighted energy in the remote spectator region.

## 10. Interpretation

M19-077 showed that arbitrary unit vectors can be translated to infinity and defeat compactness.

M19-079 shows that a genuine bounded zero-growth solution cannot remain one of those freely escaping vectors for all time.

The distinction is:

\[
\boxed{
\text{phase-space noncompactness}
\neq
\text{neutral-cocycle nonobservability}.
}
\]

The remote similarity conveyor is strictly damped in the pressure-compatible norm. To have net zero growth, a mode must repeatedly receive enough amplification/coupling from the finite active region to offset this remote damping.

Thus every bounded center candidate is dynamically tethered to one finite core in long-time average.

## 11. What this does and does not solve

Certified:

1. remote transport defect is \(O(R^{-2})\);
2. remote strain defect is \(O(R^{-2})\);
3. the weighted pressure defect splits into exterior-small plus finite core charge;
4. every bounded nonvanishing neutral trajectory satisfies a positive long-time core-energy fraction;
5. arbitrary remote-packet noncompactness therefore does not by itself produce actual bounded center modes.

Not certified:

1. an instantaneous lower bound on \(E_c/E\) at every time;
2. a fixed finite time-window observability inequality;
3. finite-dimensionality of the center space;
4. exhaustion of the center by time/rotation symmetries;
5. absence of relative-periodic screw states;
6. global regularity.

## 12. Zero-exponent firewall

A Lyapunov exponent equal to zero does not automatically imply a uniformly bounded representative. A solution may grow subexponentially, for example polynomially.

Therefore M19-079 applies directly to **bounded complete neutral trajectories**.

Extending it to every zero Oseledets exponent requires either:

- a tempered/projective normalization argument;
- an invariant measure on the projectivized cocycle;
- or an a priori bounded-center theorem.

That extension is not silently assumed.

## 13. Next target

The new positive result suggests the exact missing bridge.

If there were fixed numbers \(R,\tau,C_{obs}\) such that every bounded center trajectory obeyed

\[
\boxed{
\|W(0)\|_{L^2(w)}^2
\le
C_{obs}
\int_{-\tau}^{\tau}
\|W(\theta)\|_{L^2(w;B_R)}^2d\theta,
}
\]

then local parabolic smoothing inside \(B_R\) could potentially turn that observability estimate into finite-dimensionality of the center.

M19-079 gives only a long-time average core fraction, not this fixed-window inequality.

The next module should prove the conditional compactness implication and isolate exactly what stronger time-uniform observability is still missing.

---

\[
\boxed{\text{M19-079 COMPLETE.}}
\]
