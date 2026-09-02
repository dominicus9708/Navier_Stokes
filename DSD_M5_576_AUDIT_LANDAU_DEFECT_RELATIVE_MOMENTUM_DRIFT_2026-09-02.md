# DSD M5-576 — Audit: Landau Defect vs Relative Momentum Drift

Date: 2026-09-02

Status: **UNFORCEDNESS FOR s<0 DOES NOT BY ITSELF FORCE THE TERMINAL LANDAU STRESS DEFECT TO VANISH. A NONZERO DEFECT CAN BE BALANCED BY TYPE-I-SCALE LINEAR RELATIVE-MOMENTUM DRIFT. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Tempting but invalid shortcut

M5-573 showed that the continuously homogeneous stationary terminal branch is Landau-type:

\[
C=0,
\qquad
\partial_qA=0,
\qquad
\mathcal F_A\equiv\kappa.
\]

A tempting argument is

\[
\text{the ancient solution is unforced for every }s<0
\Longrightarrow
\kappa=0.
\]

This is not justified because the solution has a nonintegrable \(1/r\) velocity tail and ordinary global momentum need not exist.

This note audits the actual momentum balance.

---

## 2. Full momentum equation in a ball

For the smooth unforced ancient solution,

\[
\partial_su=\nabla\cdot\mathbb T.
\]

Hence for every finite \(R\),

\[
\boxed{
\frac d{ds}
\int_{B_R}u(x,s)dx
=
\int_{S_R}\mathbb Tn\,dS.
}
\]

On the homogeneous stationary-tail branch,

\[
\int_{S_R}\mathbb Tn\,dS
\longrightarrow\kappa
\qquad(R\to\infty).
\]

---

## 3. C=0 improves the time-derivative tail

The terminal jet is

\[
u(x,s)
=
v(x)+(-s)r^{-3}C+O(s^2r^{-5}).
\]

If

\[
C=0,
\]

then

\[
\boxed{
\partial_su(x,s)
=O(|s|r^{-5})
}
\]

in the parabolic far field.

Since

\[
\int_R^\infty r^2r^{-5}dr<\infty,
\]

this tail is spatially \(L^1\).

Under the retained smooth-core bounds, it is therefore consistent to define the total time derivative of momentum and pass the finite-ball identity to infinity:

\[
\boxed{
\int_{\mathbb R^3}\partial_su(x,s)dx
=
\kappa.
}
\]

---

## 4. Relative momentum

Although

\[
\int u(x,s)dx
\]

itself diverges because \(u\sim1/r\), the common time-independent leading tail cancels in a time difference.

Define, when the higher-order tail makes the difference integrable,

\[
\boxed{
M_{rel}(s;s_0)
:=
\int_{\mathbb R^3}
[u(x,s)-u(x,s_0)]dx.
}
\]

Then

\[
\frac d{ds}M_{rel}(s;s_0)=\kappa,
\]

so

\[
\boxed{
M_{rel}(s;s_0)
=
\kappa(s-s_0).
}
\]

Thus a nonzero terminal stress defect manifests as a linear drift of **relative**, rather than absolute, momentum.

---

## 5. Type-I scaling allows exactly linear momentum drift

A Type-I ancient core at time \(s<0\) has characteristic radius and amplitude

\[
R_{core}(s)\sim\sqrt{|s|},
\qquad
|u|_{core}\sim |s|^{-1/2}.
\]

Its natural \(L^1\) momentum scale is therefore

\[
R_{core}^3|u|_{core}
\sim
|s|^{3/2}|s|^{-1/2}
=
\boxed{|s|}.
\]

Hence the relative-momentum law

\[
|M_{rel}|\sim |\kappa||s|
\]

is exactly Type-I scale-compatible.

There is no growth-rate contradiction.

---

## 6. DSD anti-proof conclusion

The implication

\[
\text{unforced smooth ancient flow}
\Longrightarrow
\text{zero terminal Landau defect}
\]

is false without an additional theorem controlling the singular terminal limit.

The correct problem is

\[
\boxed{
\text{Can a smooth unforced Type-I ancient solution generate a nonzero point-supported momentum-stress defect in its terminal trace?}
}
\]

To close this branch one needs one of:

1. a terminal defect-measure compactness theorem forcing \(\kappa=0\);
2. a weak-continuation theorem across the terminal time that excludes an atomic momentum source;
3. an inherited original-solution momentum condition strong enough to survive blow-up rescaling and kill \(\kappa\).

None is currently present in the DSD inheritance package.

---

## 7. Current stationary hard branch

The classified homogeneous stationary endpoint is therefore

\[
\boxed{
E_{Landau\ defect}^{hom}
=
\left\{
\begin{array}{l}
C=0,\\
\partial_qA=0,\\
\kappa\neq0,\\
M_{rel}'=\kappa.
\end{array}
\right.
}
\]

and this is scale-compatible with the Type-I ancient core.

Status: **THE LANDAU DEFECT BRANCH SURVIVES THE GLOBAL-MOMENTUM AUDIT. ITS REMOVAL REQUIRES A TRUE TERMINAL DEFECT-MEASURE ARGUMENT, NOT A FORMAL APPEAL TO UNFORCEDNESS. GLOBAL REGULARITY REMAINS UNPROVED.**