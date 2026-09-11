# DSD M19-078 — Gaussian vorticity removes pressure but the non-A2 obstruction reappears as unbounded Biot–Savart recovery, while adding unweighted control restores remote noncompactness

**Date:** 2026-09-12  
**Status:** GAUSSIAN-VORTICITY SHORTCUT FIREWALL / PRESSURE DISAPPEARS BUT NONLOCAL VELOCITY RECOVERY IS NOT CONTROLLED BY THE GAUSSIAN NORM / GLOBAL REGULARITY REMAINS UNPROVED

## 1. Motivation

M19-062 found a strong Gaussian Ornstein--Uhlenbeck gap but failed in velocity variables because the Gaussian weight is not in \(A_2\), so weighted pressure/Riesz control is unavailable.

A natural repair is to use vorticity, where pressure disappears explicitly.

Let

\[
\Omega=\nabla\times U,
\qquad
\Xi=\nabla\times W.
\]

The question is whether a Gaussian vorticity phase space can simultaneously provide:

1. compact/confining OU behavior;
2. a closed linearized Navier--Stokes cocycle.

The answer is negative without additional global control.

## 2. Linearized similarity-vorticity equation

The similarity vorticity equation is

\[
\partial_\theta\Omega
+\Omega
+\frac12y\cdot\nabla\Omega
+(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U
=\nu\Delta\Omega.
\]

Linearization gives

\[
\boxed{
\begin{aligned}
\partial_\theta\Xi
&+\Xi
+\frac12y\cdot\nabla\Xi
+(U\cdot\nabla)\Xi
+(W\cdot\nabla)\Omega\\
&-(\Xi\cdot\nabla)U
-(\Omega\cdot\nabla)W
=\nu\Delta\Xi,
\end{aligned}
}
\]

with

\[
\nabla\cdot\Xi=0.
\]

There is no pressure term.

However

\[
\boxed{
W=\mathrm{BS}[\Xi]
}
\]

is the whole-space Biot--Savart recovery.

Thus nonlocality has not disappeared; it has moved into the coefficients of the vorticity equation.

## 3. Gaussian phase-space candidate

Take

\[
\gamma_\beta(y)=C_\beta e^{-\beta|y|^2},
\qquad \beta>0.
\]

The free OU part has strong confinement properties in

\[
L^2(\gamma_\beta).
\]

If Biot--Savart were bounded in this norm, one could hope to close the nonlinear linearized terms without pressure.

But Gaussian weights are not \(A_2\), and the same failure appears directly in velocity recovery.

## 4. Remote normalized vorticity packet

Choose a nonzero smooth compactly supported divergence-free vorticity packet \(\phi\).

For \(R\gg1\), set

\[
\Xi_R(y)=A_R\phi(y-Re_1).
\]

On its support,

\[
\gamma_\beta(y)\asymp e^{-\beta R^2}
\]

up to subleading exponential factors that can be absorbed by choosing the support fixed and, if desired, centering along a thin transverse packet.

Normalize so that

\[
\boxed{
\|\Xi_R\|_{L^2(\gamma_\beta)}=1.
}
\]

Then the normalization amplitude grows exponentially:

\[
\boxed{
A_R=e^{\frac12\beta R^2+O(R)}.
}
\]

The exact lower-order exponential correction depends on the packet support and is irrelevant to the conclusion: the growth beats every algebraic power of \(R\).

## 5. Biot--Savart far field is only algebraically small

The Biot--Savart kernel satisfies

\[
K(z)=O(|z|^{-2}).
\]

Because \(\phi\) is compactly supported, the velocity produced at a fixed bounded observation region by a packet translated to \(Re_1\) has a multipole expansion in powers of \(R^{-1}\).

A compact divergence-free packet may have vanishing lowest moments, so one must not assume a nonzero monopole term.

However a nonzero compact smooth packet cannot have **all** polynomial moments equal to zero: its Fourier transform is entire, and vanishing of every moment would make every derivative at the origin vanish, hence the entire Fourier transform and the packet itself vanish.

Therefore for a suitable nonzero packet there is a finite integer \(N\) and a bounded observation set \(B\) such that

\[
\boxed{
\|\mathrm{BS}[\phi(\cdot-Re_1)]\|_{L^2(B)}
\ge cR^{-N}
}
\]

along all sufficiently large \(R\), after fixing a packet whose first nonzero multipole coefficient does not vanish on \(B\).

Thus

\[
\boxed{
\|\mathrm{BS}[\Xi_R]\|_{L^2(B)}
\gtrsim
A_RR^{-N}.
}
\]

Since \(A_R\) grows exponentially,

\[
\boxed{
A_RR^{-N}\to\infty.
}
\]

## 6. Failure of Gaussian Biot--Savart boundedness

On a fixed bounded set \(B\), the Gaussian weight is bounded above and below by positive constants. Hence

\[
\|W_R\|_{L^2(\gamma_\beta;B)}
\asymp
\|W_R\|_{L^2(B)}.
\]

Therefore

\[
\boxed{
\|\Xi_R\|_{L^2(\gamma_\beta)}=1,
\qquad
\|\mathrm{BS}[\Xi_R]\|_{L^2(\gamma_\beta)}\to\infty.
}
\]

Consequently

\[
\boxed{
\mathrm{BS}:L^2(\gamma_\beta)
\to L^2(\gamma_\beta)
\text{ is not bounded.}
}
\]

This is the vorticity analogue of the Gaussian pressure failure in M19-062.

## 7. Why this prevents closure of the linearized vorticity energy

The terms

\[
(W\cdot\nabla)\Omega,
\qquad
(\Omega\cdot\nabla)W
\]

require control of \(W\) or \(\nabla W\) by \(\Xi\).

A Gaussian estimate of the form

\[
\|W\|_{L^2(\gamma)}
+\|\nabla W\|_{L^2(\gamma)}
\le C\|\Xi\|_{L^2(\gamma)}
\]

is unavailable.

Therefore the pressure-free equation is not a closed Gaussian Hilbert-space evolution merely because pressure has disappeared algebraically.

## 8. Add global unweighted vorticity control?

One may try the combined norm

\[
\boxed{
\|\Xi\|_X
:=
\|\Xi\|_{L^2}
+\|\Xi\|_{L^2(\gamma)}.
}
\]

The unweighted \(L^2\) component restores standard Biot--Savart/Sobolev control, for example

\[
\|W\|_{L^6}\lesssim\|\Xi\|_{L^2}.
\]

This blocks the exponentially amplified Gaussian counterexample because Gaussian normalization can no longer be achieved with arbitrarily large unweighted amplitude inside a bounded X-ball.

But now the compactness advantage is lost.

Translated unweighted packets

\[
\Xi_R(y)=\phi(y-Re_1)
\]

have constant \(L^2\) norm and Gaussian norm tending to zero. They form a bounded sequence in \(X\) with no strongly convergent subsequence in the unweighted component.

Hence

\[
\boxed{
\text{adding enough global control to bound Biot--Savart}
\text{ restores remote translation noncompactness.}
}
\]

## 9. Two-norm dilemma

The Gaussian-vorticity strategy therefore splits into two incompatible advantages:

\[
\boxed{
\begin{array}{c|c|c}
\text{phase space} & \text{OU compactness/confinement} & \text{nonlocal velocity recovery}\\
\hline
L^2(\gamma) & \text{strong} & \text{not bounded}\\
L^2(\gamma)\cap L^2 & \text{remote translation survives} & \text{standard control restored}
\end{array}
}
\]

At present there is no certified norm in this line that simultaneously provides:

1. global compactness of the relevant cocycle;
2. bounded pressure/Biot--Savart recovery;
3. enough strength to control the weak-critical recurrent branch.

## 10. Relation to M19-062 and M19-077

M19-062:

\[
\text{Gaussian velocity}
\Rightarrow
\text{pressure obstruction}.
\]

M19-078:

\[
\text{Gaussian vorticity}
\Rightarrow
\text{Biot--Savart obstruction}.
\]

M19-077:

\[
\text{polynomial A2 velocity}
\Rightarrow
\text{pressure controlled but remote noncompactness survives}.
\]

Together they identify a stable three-way firewall:

\[
\boxed{
\text{nonlocal recovery compatibility}
\leftrightarrow
\text{tail tightness}
\leftrightarrow
\text{compactness}
}
\]

cannot currently be obtained for free from a single standard weighted Hilbert norm.

## 11. Important scope firewall

The remote Gaussian counterexample is a functional-analytic boundedness test.

It is **not** a claim that actual recurrent Navier--Stokes tangent modes have exponentially large unweighted vorticity.

If the actual tangent class carries an additional scale-uniform unweighted bound, then the first counterexample is excluded—but the combined-space translation noncompactness of Section 8 becomes the relevant obstruction.

Thus the conclusion is about the proposed proof mechanism, not about existence of a singular solution.

## 12. Next target

The failed compactness shortcuts suggest a more quantitative question:

> If a genuine zero-growth cocycle mode cannot be eliminated by global compactness, must it nevertheless spend a definite fraction of its weighted energy inside a finite active core, because the remote spectator region is strictly linearly damped?

This is weaker than compactness and is compatible with translation escape for arbitrary bounded sequences.

A positive answer would produce a **core-occupation/observability condition for actual center modes**, rather than for all perturbations.

---

\[
\boxed{\text{M19-078 COMPLETE.}}
\]
