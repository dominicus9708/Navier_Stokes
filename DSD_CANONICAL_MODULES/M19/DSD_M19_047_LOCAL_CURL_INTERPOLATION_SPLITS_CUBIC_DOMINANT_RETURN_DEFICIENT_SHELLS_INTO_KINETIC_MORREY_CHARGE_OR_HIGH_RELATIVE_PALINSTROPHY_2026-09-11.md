# M19-047 — Local curl interpolation splits cubic-dominant return-deficient shells into kinetic Morrey charge or high relative palinstrophy

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC TO R-CRITICAL OR HIGH-FREQUENCY SPLIT / LOCAL HODGE INTERPOLATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-046

On the retained cubic-dominant R-AC sector,

\[
\sum_kJ_k^{3/2}=\infty,
\]

while on extracted mass-bearing blocks of a geometric shrinking-radius family,

\[
\boxed{\frac{J_k}{\rho_k}\to\infty.}
\]

The bulk shell enstrophy satisfies

\[
\boxed{
m_k:=\int_{E_k}|\omega|^2dx\ge c_m\frac{J_k}{\rho_k}.}
\]

M19-046 shows that repeated distinct-return counting is too weak to close this sector.

The present module asks whether large bulk enstrophy at scale \(\rho_k\) must instead become either local kinetic Morrey activity or high relative derivative content.

## 2. Controlled localization setup

Fix one shell and abbreviate

\[
\rho:=\rho_k,
\qquad
J:=J_k.
\]

Let \(E\) be the active shell collar and let \(E^+\) be a fixed-factor enlargement.

Choose

\[
\phi\in C_c^\infty(E^+),
\qquad
0\le\phi\le1,
\qquad
\phi\equiv1\text{ on }E,
\]

with

\[
|\nabla\phi|\le C_\phi\rho^{-1}.
\]

Assume the retained localization-comparability branch

\[
\boxed{
\int_{E^+}|\omega|^2dx
\le C_m^+ m,
}
\]

where

\[
m:=\int_E|\omega|^2dx.
\]

Failure of this fixed enlargement comparability is a shell-spreading / multicollar / localization exit and is kept separate.

Define the local kinetic variance

\[
\boxed{
K_{loc}
:=
\inf_{c\in\mathbb R^3}
\int_{E^+}|u-c|^2dx
}
\]

and local palinstrophy

\[
\boxed{
P_{loc}
:=
\int_{E^+}|\nabla\omega|^2dx.
}
\]

## 3. Exact cutoff curl identity

Because

\[
\omega=\nabla\times u
\]

and \(\nabla\times c=0\), integration by parts on \(\mathbb R^3\) gives

\[
\begin{aligned}
\int \phi^2|\omega|^2dx
&=
\int \phi^2(\nabla\times(u-c))\cdot\omega\,dx\\
&=
\int (u-c)\cdot\nabla\times(\phi^2\omega)\,dx.
\end{aligned}
\]

Now

\[
\nabla\times(\phi^2\omega)
=
\phi^2\nabla\times\omega
+2\phi\nabla\phi\times\omega.
\]

Hence by Cauchy--Schwarz,

\[
\int \phi^2|\omega|^2dx
\le
K_{loc}^{1/2}
\left(
P_{loc}^{1/2}
+
C\rho^{-1}
\left(\int_{E^+}|\omega|^2dx\right)^{1/2}
\right).
\]

Since \(\phi=1\) on \(E\),

\[
\boxed{
m
\le
K_{loc}^{1/2}P_{loc}^{1/2}
+
C_*\rho^{-1}K_{loc}^{1/2}m^{1/2}.}
\]

This is a fully local interpolation identity up to the explicitly stated fixed-collar comparability.

## 4. Parameterized dichotomy

Fix a small dimensionless parameter

\[
0<\varepsilon<\varepsilon_*:=(4C_*^2)^{-1}.
\]

If

\[
K_{loc}
\ge
\varepsilon\rho^2m,
\]

then the kinetic branch holds.

Otherwise

\[
K_{loc}<\varepsilon\rho^2m.
\]

The cutoff error obeys

\[
C_*\rho^{-1}K_{loc}^{1/2}m^{1/2}
<
C_*\sqrt\varepsilon\,m
\le
\frac12m.
\]

Therefore

\[
\frac12m
\le
K_{loc}^{1/2}P_{loc}^{1/2},
\]

so

\[
P_{loc}
\ge
\frac{m^2}{4K_{loc}}
>
\frac{1}{4\varepsilon}
\frac{m}{\rho^2}.
\]

Thus for every sufficiently small fixed \(\varepsilon\),

\[
\boxed{
K_{loc}
\ge
\varepsilon\rho^2m
\quad\lor\quad
P_{loc}
\ge
\frac{1}{4\varepsilon}
\frac{m}{\rho^2}.
}
\]

## 5. Rewrite in the annular cubic charge

Using

\[
m\ge c_mJ/\rho,
\]

the kinetic branch yields

\[
K_{loc}
\ge
c\varepsilon J\rho.
\]

Hence the local scale-invariant kinetic Morrey charge satisfies

\[
\boxed{
\frac{K_{loc}}{\rho}
\ge
c\varepsilon J.
}
\]

The derivative branch yields

\[
\boxed{
P_{loc}
\ge
c\varepsilon^{-1}
\frac{J}{\rho^3}.
}
\]

Therefore

\[
\boxed{
G_{bulk\ cubic\ shell}(J,\rho)
\Longrightarrow
G_{kinetic\ Morrey\ charge\ \gtrsim J}
\lor
G_{palinstrophy\ \gtrsim J/\rho^3}
\lor
G_{localization\ defect}.
}
\]

## 6. Relative-frequency form

Define the dimensionless local relative-frequency ratio

\[
\boxed{
\Lambda_{rel}^2
:=
\rho^2\frac{P_{loc}}{m}.
}
\]

The parameterized dichotomy becomes

\[
\boxed{
\frac{K_{loc}}{\rho^2m}\ge\varepsilon
\quad\lor\quad
\Lambda_{rel}^2\ge\frac{1}{4\varepsilon}.
}
\]

Consequently, along any sequence for which

\[
\frac{K_{loc}}{\rho^2m}\to0,
\]

we necessarily have

\[
\boxed{
\Lambda_{rel}\to\infty.
}
\]

Thus suppression of kinetic realization of a large vorticity shell is possible only by pushing the shell to arbitrarily high frequency relative to its own geometric radius, modulo localization defects.

## 7. Cubic-mass consequence on the kinetic branch

Suppose the kinetic branch occurs on a subset \(\mathcal K\) that carries divergent cubic shell mass:

\[
\sum_{k\in\mathcal K}J_k^{3/2}=\infty.
\]

Define

\[
\mathcal M_k
:=
\frac1{\rho_k}
\inf_c\int_{E_k^+}|u-c|^2dx.
\]

Then

\[
\mathcal M_k\gtrsim J_k,
\]

and hence

\[
\boxed{
\sum_{k\in\mathcal K}\mathcal M_k^{3/2}=\infty.
}
\]

This is a genuine nonsummable family of critical kinetic Morrey charges.

It is **not yet** the fixed positive Morrey floor used by the simplest R-critical stack, because \(J_k\) may tend to zero while its \(3/2\)-sum diverges.

Therefore an additional log-scale/terminal-alignment argument is still required before identifying this with the nonzero recurrent scattering datum.

## 8. High-relative-frequency branch

If instead the kinetic fraction tends to zero on the cubic-dominant subset, then

\[
\Lambda_{rel,k}\to\infty.
\]

This is precisely the kind of derivative-tail decompactification already separated by M18 and by the high-frequency arm of M19-015.

However the present statement is local in a shell collar, whereas M19-015 uses global Littlewood--Paley projections.

Thus the safe routing is

\[
\boxed{
G_{\Lambda_{rel}\to\infty}
\to
G_{high\ relative\ frequency}
\lor
G_{frequency/localization\ defect}.
}
\]

No direct contradiction is claimed here.

## 9. Interaction with M19-046

M19-046 shows that the cubic-dominant Type-I survivor satisfies

\[
\frac{J_k}{\rho_k}\to\infty
\]

in cubic-mass density.

M19-047 now says that this rapidly growing shell enstrophy density cannot remain simultaneously

1. low in local kinetic Morrey realization, and
2. bounded in relative derivative frequency.

The sharp R-AC endpoint is therefore refined to

\[
\boxed{
\mathcal R_{AC}^{sharp}
\Longrightarrow
G_{nonsummable\ kinetic\ Morrey\ charge}
\lor
G_{high\ relative\ frequency}
\lor
G_{localization/geometry\ defect}.
}
\]

This is a substantive reduction: the return-count variable has disappeared from the local analytic endpoint.

## 10. What remains

The next question is representation, not the local inequality.

For the kinetic branch one must determine whether

\[
\sum\mathcal M_k^{3/2}=\infty
\]

along shrinking, terminal first-hitting shells forces a nontrivial log-scale scattering factor after common-center / terminal-time selection.

For the high-frequency branch one must determine whether the local \(\Lambda_{rel}\to\infty\) can be absorbed by the already typed derivative-tail / remote complex without introducing a new root.

## 11. Firewalls

This module does not infer low-frequency kinetic energy from large vorticity without a derivative alternative.

It does not identify a local shell cutoff with a global Fourier projection.

It does not claim that divergent \(\sum\mathcal M_k^{3/2}\) implies a fixed positive Morrey floor.

It does not prove R-critical scattering rigidity.

---

\[
\boxed{\text{M19-047 COMPLETE; SHARP R-AC NOW SPLITS INTO NONSUMMABLE KINETIC MORREY CHARGE OR HIGH RELATIVE FREQUENCY.}}
\]