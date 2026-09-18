# M19-407 — Nontrivial smooth zero-force stationary recurrent tails require positive mean log-dilation derivative occupation

Date: 2026-09-18

Status: **NEW DILATION-DERIVATIVE NECESSITY / M19-406 CLOSES THE SMOOTH EXACTLY (-1)-HOMOGENEOUS ZERO-FORCE STATIONARY ENDPOINT BY THE LANDAU/ŠVERÁK CLASSIFICATION. ON A COMPACT RECURRENT LOG-RADIUS HULL, THE NONNEGATIVE CONTINUOUS OBSERVABLE \`D_q(A)=int_{S2}|partial_q A|^2\` THEREFORE CANNOT HAVE ZERO INVARIANT MEAN ON A NONTRIVIAL ZERO-FORCE COMPONENT. OTHERWISE IT VANISHES ON THE SUPPORT, THE PROFILE IS Q-INDEPENDENT, AND M19-406 FORCES THE FIELD TO BE ZERO. HENCE EVERY NONTRIVIAL SMOOTH ZERO-FORCE RECURRENT TERMINAL TAIL HAS A STRICTLY POSITIVE INVARIANT LOG-DILATION DERIVATIVE OCCUPATION. THIS IS A GENUINE DYNAMICAL PAYER, BUT IT REMAINS SCALE-CRITICAL AND RECURRENTLY RECYCLABLE; IT IS NOT YET A FINITE RESOURCE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Stationary log-radius profile

Write the smooth stationary hard tail as

\[
u(x)
=
\frac1rA(q,\omega),
\qquad
p(x)
=
\frac1{r^2}P(q,\omega),
\qquad
q=\log r.
\]

Let

\[
\sigma_\tau(A,P)
=
(A(q+\tau,\omega),P(q+\tau,\omega))
\]

denote the log-radius translation.

The retained hard branch supplies a compact recurrent dilation hull

\[
\mathfrak H
=
\overline{
\{\sigma_\tau(A,P):\tau\in\mathbb R\}
}
\]

in a smooth compact-annulus topology.

Let \(\mu\) be an invariant probability measure supported on one nontrivial recurrent component of this hull.

---

## 2. Log-dilation derivative observable

Define

\[
\boxed{
D_q(Y)
:=
\int_{S^2}
|\partial_q A_Y(0,\omega)|^2
\,d\omega.
}
\]

Because the hull topology retains the required first log-radius derivative,

\[
D_q:\mathfrak H\to[0,\infty)
\]

is continuous.

Translation invariance means that along the original profile,

\[
D_q(\sigma_\tau Y)
=
\int_{S^2}
|\partial_qA(\tau,\omega)|^2d\omega.
\]

Thus

\[
\int_{\mathfrak H}D_q\,d\mu
\]

is the invariant mean radial-log derivative energy.

---

## 3. Zero invariant mean forces exact homogeneity on the support

Assume

\[
\int_{\mathfrak H}D_q\,d\mu=0.
\]

Since

\[
D_q\ge0,
\]

one has

\[
D_q=0
\]

for \(\mu\)-almost every state.

Because \(D_q\) is continuous and every open neighborhood of a support point has positive \(\mu\)-measure,

\[
\boxed{
D_q(Y)=0
\qquad
\forall Y\in\operatorname{supp}\mu.
}
\]

Hence every state in the support satisfies

\[
\partial_qA_Y=0.
\]

Therefore every supported stationary profile is exactly degree-\(-1\) homogeneous.

---

## 4. Apply M19-406 on the zero-force component

Assume in addition that the stationary stress-flux coefficient vanishes:

\[
\kappa_{\rm force}=0.
\]

M19-406, using the external Landau/Šverák classification, closes the smooth exact-homogeneous zero-force branch:

\[
\partial_qA=0
+
\kappa_{\rm force}=0
\Longrightarrow
A=0.
\]

Thus Section 3 would imply that the invariant component is trivial.

Therefore any **nontrivial** smooth zero-force invariant component must satisfy

\[
\boxed{
\int_{\mathfrak H}
D_q\,d\mu
>0.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\int_{S^2}
|\partial_qA(q,\omega)|^2d\omega
\right\rangle_q
>0.
}
\]

---

## 5. Positive occupation form

Let

\[
d_q
:=
\int D_q\,d\mu
>0.
\]

Then there exists a threshold

\[
\varepsilon_q>0
\]

such that the set

\[
E_q
=
\{Y:D_q(Y)\ge\varepsilon_q\}
\]

has positive invariant measure:

\[
\boxed{
\mu(E_q)>0.
}
\]

Otherwise \(D_q\) could be positive only on thresholds whose mass vanishes in a way incompatible with its strictly positive integral.

Hence the zero-force hard branch contains positive-density log-radius phases with quantitatively nonzero dilation derivative.

This is stronger than merely saying “the profile is not constant in \(q\).”

---

## 6. Physical radial derivative meaning

Since

\[
u=r^{-1}A(q,\omega),
\qquad
q=\log r,
\]

one has

\[
\partial_ru
=
r^{-2}
\left(
\partial_qA-A
\right).
\]

Thus \(\partial_qA\) is a genuine part of the critical radial velocity gradient.

Likewise angular derivatives contribute at the same \(r^{-2}\) scale.

Therefore a positive invariant \(D_q\) means the zero-force survivor maintains a nontrivial critical radial-modulation derivative on a positive log-scale density.

---

## 7. Annular criticality

On one geometric annulus

\[
R<r<2R,
\]

the radial-modulation contribution to

\[
\int|\nabla u|^2dx
\]

has the scaling

\[
\int_R^{2R}
r^2
\cdot
r^{-4}
\int_{S^2}
|\partial_qA|^2d\omega
\,dr.
\]

Since

\[
dr/r^2
\sim R^{-1}
\]

on the annulus,

\[
\boxed{
\int_{R<|x|<2R}
|\nabla u|^2dx
\gtrsim
R^{-1}
\int_{\log R}^{\log2R}
D_q(q)\,dq
}
\]

up to the cross terms with \(A\), which require a completed-square or full stress treatment for a coercive lower bound.

Thus the log-dilation payer remains **critical** rather than subcritical.

This is consistent with M19-405.

---

## 8. No immediate contradiction

A recurrent log-periodic or aperiodic stationary profile may support

\[
\langle D_q\rangle>0
\]

forever.

Therefore

\[
\boxed{
\langle D_q\rangle>0
\not\Rightarrow
\text{contradiction}.
}
\]

It is a required dynamical currency, not a finite-use resource.

The result is valuable because it removes the option that zero force is maintained by an almost homogeneous stationary state with no persistent dilation dynamics.

---

## 9. Refined zero-force survivor

The smooth stationary zero-force hard branch now satisfies

\[
\boxed{
\begin{aligned}
G_{\rm stationary}^{force=0,\ nontrivial}
\Longrightarrow{}&
\langle D_q\rangle>0\\
&\lor
G_{\rm angular/sphere}^{singular}\\
&\lor
G_{\rm nonstationary/representation}.
\end{aligned}
}
\]

On the retained smooth stationary compact hull,

\[
\boxed{
\langle D_q\rangle>0
}
\]

is compulsory.

---

## 10. Relation to DSS and aperiodic recurrence

If the profile is log-periodic with period \(T_q\),

\[
A(q+T_q,\omega)=A(q,\omega),
\]

then nontrivial zero force requires

\[
\boxed{
\int_0^{T_q}
\int_{S^2}
|\partial_qA|^2d\omega dq
>0.
}
\]

For an aperiodic recurrent invariant component, the corresponding invariant mean is positive.

Thus periodic and aperiodic zero-force survivors now share the same compulsory dilation-derivative currency.

A future theorem may attack both simultaneously if it can show that this currency cannot coexist with zero stress flux / the inherited ancient budgets.

---

## 11. Updated rigidity target

The next stationary theorem gate becomes

\[
\boxed{
\mathcal T_{dil}^{payer\to rigidity}:
\text{show that a smooth stationary zero-force recurrent tail with }
\langle D_q\rangle>0
\text{ is impossible or forces a typed nonstationary/critical-tail exit.}
}
\]

Possible routes include:

1. a signed stress identity coupling \(D_q\) to the zero-force condition;
2. a virial/Pohozaev identity on the log-cylinder;
3. a spectral gap for the stationary log-cylinder operator modulo Landau modes;
4. a compact recurrent Liouville theorem.

---

\[
\boxed{\text{M19-407 COMPLETE; NONTRIVIAL SMOOTH ZERO-FORCE STATIONARY RECURRENCE REQUIRES POSITIVE MEAN LOG-DILATION DERIVATIVE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
