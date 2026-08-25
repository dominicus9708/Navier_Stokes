# DSD W1 Supercritical Maximum: Projective Locking Gate

Date: 2026-08-26

Status: **DIRECTIONAL SUPERCRITICAL VORTICITY-MAXIMUM EVENTS SPLIT QUANTITATIVELY INTO POSITIVE-MIDDLE OVERLAP, FIXED STRAIN-DRIVEN PROJECTIVE CONVERSION, OR STRONG PRINCIPAL-AXIS LOCKING / THIS DOES NOT BY ITSELF CLOSE THE ALIGNMENT BRANCH / GLOBAL REGULARITY UNPROVED.**

## 1. Input from the vorticity-amplitude dichotomy

On the oscillatory-amplitude branch of a nontrivial compact minimal W1 set, there are syndetically recurrent finite-core times and true global-vorticity maximum points at which

\[
\boxed{
\gamma:=\xi^TS\xi\ge g_0:=1+\varepsilon_\gamma>1,
}
\]

where

\[
\xi=\Omega/|\Omega|.
\]

Because all such points lie in one fixed compact core of the compact smooth state class, there is a finite strain ceiling

\[
\boxed{
\lambda_3\le K_3<\infty
}
\]

on that event set.

Order the strain eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0,
\]

and write

\[
a_i:=(\xi\cdot e_i)^2,
\qquad
a_1+a_2+a_3=1.
\]

Then

\[
\gamma=a_1\lambda_1+a_2\lambda_2+a_3\lambda_3.
\]

## 2. Exact strain-driven projective speed

The component of `S xi` transverse to the vorticity direction is

\[
\boxed{
\mathcal C_\xi
:=P_{\xi^\perp}S\xi.
}
\]

Its exact squared magnitude is the eigenvalue variance

\[
\boxed{
|\mathcal C_\xi|^2
=
\sum_i a_i(\lambda_i-\gamma)^2
=
\sum_{i<j}a_i a_j(\lambda_i-\lambda_j)^2.
}
\]

This is the instantaneous strain-driven vorticity-direction conversion term appearing in the exact direction equation.  Diffusive direction terms are separate and are not identified with `C_xi`.

## 3. Choose a middle-strain overlap threshold

Fix any

\[
\boxed{0\le\mu<g_0.}
\]

At a supercritical maximum event, either

\[
\boxed{\lambda_2>\mu}
\]

or

\[
\boxed{\lambda_2\le\mu.}
\]

The first case is a direct simultaneous overlap between directional supercritical stretching and a positive middle-strain event of fixed amplitude `mu`.

No assertion is made that the invariant-measure middle-strain threshold `1/4+delta_M/2` must occur at the same point; `mu` is an independently chosen overlap threshold below `g0`.

## 4. If middle strain is low, the vorticity must carry a fixed principal-axis weight

Assume

\[
\lambda_2\le\mu.
\]

Since both lower eigenvalues are at most `mu`,

\[
\gamma
\le
(1-a_3)\mu+a_3\lambda_3
\le
(1-a_3)\mu+a_3K_3.
\]

Using `gamma>=g0` gives

\[
\boxed{
a_3
\ge
a_0
:=
\frac{g_0-\mu}{K_3-\mu}
>0.
}
\]

Thus a supercritical vorticity maximum with no fixed positive-middle overlap cannot place arbitrarily little vorticity in the most extensional eigendirection.

## 5. Quantitative projective conversion unless principal locking occurs

Still on `lambda_2<=mu`,

\[
\lambda_3-\lambda_i
\ge
\lambda_3-\lambda_2
\ge
g_0-\mu
\qquad(i=1,2).
\]

The exact variance identity therefore gives

\[
\begin{aligned}
|\mathcal C_\xi|^2
&\ge
\sum_{i=1}^2
a_i a_3(\lambda_3-\lambda_i)^2\\
&\ge
\boxed{
a_3(1-a_3)(g_0-\mu)^2.}
\end{aligned}
\]

Fix any locking tolerance

\[
0<\eta<1.
\]

If

\[
a_3\le1-\eta,
\]

then, using `a3>=a0`,

\[
\boxed{
|P_{\xi^\perp}S\xi|
\ge
c_{proj}
:=(g_0-\mu)\sqrt{a_0\eta}
>0.
}
\]

Thus avoiding a fixed projective-conversion charge forces

\[
\boxed{
a_3>1-\eta.}
\]

Equivalently,

\[
\boxed{
|\xi\cdot e_3|^2>1-\eta,
}
\]

so the vorticity direction is quantitatively locked to the principal extensional strain axis.

## 6. Exact three-way gate

Every directional-supercritical vorticity-maximum event obeys

\[
\boxed{
\gamma\ge g_0
\Longrightarrow
\begin{cases}
\lambda_2>\mu,
\\[1mm]
\text{or }|P_{\xi^\perp}S\xi|\ge c_{proj},
\\[1mm]
\text{or }|\xi\cdot e_3|^2>1-\eta.
\end{cases}
}
\]

The constants are explicit in the compact W1 event class:

\[
\boxed{
a_0=\frac{g_0-\mu}{K_3-\mu},
\qquad
c_{proj}=(g_0-\mu)\sqrt{a_0\eta}.}
\]

This is a pointwise algebraic trichotomy and does not use an integral approximation.

## 7. Recurrent version

The supercritical maximum event is an open recurrent event after a slight weakening of `g0`.  Therefore, on the oscillatory-amplitude minimal branch, one of the following must occur infinitely often with bounded Leray-time gaps after passage to a finite subcover/subsequence:

1. **supercritical/middle overlap:** a true vorticity maximum has both `gamma>1+epsilon` and `lambda2>mu`;
2. **projective conversion:** the strain-driven transverse direction speed has a fixed lower bound;
3. **principal-axis locking:** the vorticity is uniformly close to `e3` at the supercritical maximum.

A rigorous positive-density allocation among these three alternatives can be obtained by partitioning the compact event set into closed weakened threshold sectors; this note uses only the weaker conclusion that at least one sector occurs recurrently.

## 8. Relation to the existing projective-action ledger

The repository already shows that a fixed amount of smooth projective action produces a normalized viscous-frequency/H1 tax.  It also shows that an `O(1)` normalized projective tax per geometric stage is not by itself enough for a global physical-energy contradiction because of the half-power stage weight.

Accordingly, the second branch above is **not declared closed merely because `c_proj>0` pointwise**.  It supplies a local fixed charge that must still be shown to persist for a sufficiently long interval or couple to an already non-summable recurrent functional.

The new value of the trichotomy is instead that any attempt to avoid this projective charge is forced into the quantitatively rigid third branch.

## 9. Geometry of the locked one-axis branch

On the locked branch with `lambda2<=mu`,

\[
|\xi\cdot e_3|^2>1-\eta.
\]

For the particularly important choice `mu=0`, the strain spectrum has

\[
\lambda_1\le\lambda_2\le0<\lambda_3,
\]

so the event is a two-compressive/one-extensional configuration with vorticity locked to the single extensional axis.

Such a state contributes no positive Betchov determinant production when `lambda2<=0`:

\[
-\det S\le0.
\]

Therefore a recurrent W1 orbit using these locked supercritical maxima to grow vorticity must still obtain its positive invariant Betchov production from other spacetime regions where `lambda2>0`.

This produces a genuine **geometry-alternation requirement**:

\[
\boxed{
\text{locked one-axis supercritical maxima}
\quad\leftrightarrow\quad
\text{two-extensional determinant-production regions}.
}
\]

The present note does not yet prove a fixed derivative/eigenframe cost for that alternation because the two regions need not be connected by one tracked spatial particle.

## 10. Updated finite-core frontier

The oscillatory-amplitude W1 branch is sharpened from the scalar statement

\[
\gamma>1+\varepsilon_\gamma
\]

to

\[
\boxed{
G_\gamma
\Longrightarrow
M_{overlap}(\mu)
\lor
P_{conv}(c_{proj})
\lor
A_{e3}(\eta).
}
\]

The genuinely rigid residual is

\[
\boxed{
A_{e3}(\eta):
\text{recurrent true-vorticity maxima are strongly locked to the principal extensional axis while middle strain remains low.}
}
\]

A next closure target is to couple this locked maximum geometry to the separately forced positive-frequency finite-core `lambda2^+` production, without assuming a common material trajectory.

## 11. DSD audit

The calculation keeps separate:

- principal eigenvalue magnitude versus vorticity-direction stretching;
- strain-driven projective conversion versus diffusive direction change;
- pointwise overlap versus invariant-measure coexistence;
- recurrent occurrence versus a non-summable accumulated cost;
- one-axis extension geometry versus positive-middle determinant production.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
