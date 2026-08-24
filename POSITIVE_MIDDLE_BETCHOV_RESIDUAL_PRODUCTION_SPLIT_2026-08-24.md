# Positive-Middle / Betchov-Residual Enstrophy-Production Split — 2026-08-24

Status: **TAIL-INDEPENDENT PRODUCTION CONSTANT REDUCTION / CONDITIONAL STRICT GAP / GLOBAL REGULARITY NOT PROVED.**

This note refines `TRACEFREE_ENSTROPHY_PRODUCTION_CONSTANT_SHARPENING_2026-08-24.md`.

The universal trace-free estimate gives

\[
\mathcal P:=\int \omega^T S\omega\,dx
\le \frac1{\sqrt3}MZ,
\qquad
M=\|\omega\|_\infty,
\quad
Z=\|\omega\|_2^2.
\]

The constant `1/sqrt(3)` is saturated pointwise only by a negative-middle strain spectrum proportional to `(-1,-1,2)` with vorticity aligned to the strongest eigenvector. However the global Betchov identity says positive mean enstrophy production is tied to negative determinant, hence positive-middle strain. The aim here is to isolate the exact residual that allows those two geometries to segregate spatially.

---

## 1. Split by the middle strain eigenvalue

Let

\[
E_+(t):=\{x:\lambda_2(S(x,t))\ge0\},
\qquad
E_-(t):=\{x:\lambda_2(S(x,t))<0\}.
\]

Set

\[
q(x,t):=\omega^T S\omega.
\]

Then

\[
\mathcal P=\int_{E_+}q+\int_{E_-}q.
\]

---

## 2. Positive-middle efficiency constant is `1/2`

On `E_+`, write the strain eigenvalues

\[
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0,
\qquad
s_2\ge0.
\]

Then

\[
|S|^2=s_1^2+s_2^2+s_3^2
\ge 2s_3^2,
\]

because `s_1=-(s_2+s_3)` and `s_2>=0`. Hence

\[
\boxed{s_3\le \frac{|S|}{\sqrt2}.}
\]

Therefore

\[
q\le s_3|\omega|^2
\le \frac1{\sqrt2}|S||\omega|^2.
\]

Using `|omega|^2<=M|omega|`, Cauchy-Schwarz, and the whole-space incompressible identity

\[
\|S\|_2^2=\frac12\|\omega\|_2^2=\frac12 Z,
\]

we obtain

\[
\begin{aligned}
\int_{E_+}q
&\le \frac{M}{\sqrt2}
\int_{E_+}|S||\omega|\\
&\le \frac{M}{\sqrt2}\|S\|_2\|\omega\|_2\\
&=\boxed{\frac12 MZ}.
\end{aligned}
\]

This is a strict improvement over the universal `1/sqrt(3)` coefficient whenever positive production is confined to positive-middle strain.

---

## 3. Negative-middle positive production is a Betchov mismatch

On `E_-`, one has

\[
s_1\le s_2<0<s_3,
\]

so

\[
\det S=s_1s_2s_3>0.
\]

Therefore, wherever `q>0`,

\[
q\le q+4\det S.
\]

Define the non-positive-middle Betchov residual

\[
\boxed{
\mathcal R_B(t)
:=\int_{E_-}(q+4\det S)_+\,dx.
}
\]

Then

\[
\int_{E_-}q
\le
\int_{E_-}q_+
\le
\mathcal R_B.
\]

Combining with Section 2 gives the exact global upper bound

\[
\boxed{
\mathcal P(t)
\le
\frac12 M(t)Z(t)
+\mathcal R_B(t).
}
\]

No localization or recurrence assumption is used in this inequality.

---

## 4. Residual-fraction form

When `MZ>0`, define

\[
\boxed{
\varepsilon_B(t)
:=\frac{\mathcal R_B(t)}{M(t)Z(t)}.
}
\]

Then

\[
\boxed{
\mathcal P(t)
\le
\left(\frac12+\varepsilon_B(t)\right)M(t)Z(t).
}
\]

Thus all improvement beyond `1/2` is now concentrated in one dimensionless scalar: the fraction of normalized production carried by negative-middle Betchov mismatch.

For comparison,

\[
\frac1{\sqrt3}-\frac12
\approx0.0773502692.
\]

Hence any eventual bound

\[
\varepsilon_B\le\varepsilon_*<0.0773502692
\]

strictly improves the universal trace-free coefficient `1/sqrt(3)`.

---

## 5. Insert into the ancient enstrophy rigidity gate

Suppose the restricted ancient solution satisfies

\[
M(t)\le \frac K{|t|},
\qquad
Z(t)=O(|t|^{-\alpha})
\quad(t\to-\infty).
\]

If eventually

\[
\varepsilon_B(t)\le\varepsilon_*,
\]

then from

\[
\frac12Z'+\nu Q=\mathcal P
\]

we obtain

\[
Z'+2\nu Q
\le
2\left(\frac12+\varepsilon_*\right)
\frac K{|t|}Z.
\]

Ignoring viscosity gives the sufficient rigidity condition

\[
\boxed{
2\left(\frac12+\varepsilon_*\right)K<\alpha
\quad\Longrightarrow\quad
Z\equiv0.
}
\]

For the current first-hitting ancient decay exponent

\[
\alpha=\frac12,
\]

this becomes

\[
\boxed{
K<\frac{1}{4(1/2+\varepsilon_*)}.
}
\]

Special cases:

\[
\varepsilon_*=0
\quad\Longrightarrow\quad
K<\frac12,
\]

while

\[
\varepsilon_*=\frac1{\sqrt3}-\frac12
\quad\Longrightarrow\quad
K<\frac{\sqrt3}{4},
\]

which recovers the universal trace-free gate.

---

## 6. Viscously improved version

If in addition the recurrent pure branch supplies a logarithmic frequency floor

\[
\liminf_{T\to\infty}
\frac1{\log T}
\int_{-T}^{-1}
\frac{Q(t)}{Z(t)}\,dt
\ge c_{\log}>0,
\]

then the effective logarithmic exponent is reduced by `2 nu c_log`. The sufficient condition becomes

\[
\boxed{
2\left(\frac12+\varepsilon_*\right)K
-2\nu c_{\log}
<\alpha.
}
\]

For `alpha=1/2`,

\[
\boxed{
(1+2\varepsilon_*)K
<\frac12+2\nu c_{\log}.
}
\]

This is the current strongest tail-independent enstrophy certificate on the Betchov-residual-quiet branch.

---

## 7. How a large residual is routed

The exact inequality above does **not** itself show that `epsilon_B` is small. A large `epsilon_B` is a genuine alternative, not an error.

However, the repository already contains the localized identity

\[
q+4\det S
=\frac43\nabla\cdot\mathcal F_A(u-c)
\]

and the local Betchov-buffer estimate

\[
\text{coherent positive mismatch}
\Longrightarrow
\text{buffer strain reservoir}
\lor
\text{buffer derivative concentration}.
\]

Therefore the remaining bridge is now precise:

> convert a recurrent lower bound on the normalized global residual fraction `epsilon_B` into either a fixed-cell Betchov mismatch or a remote/diffuse residual tail.

A fixed-cell mismatch is already routed to buffer strain/Hessian/residual. A remote/diffuse residual must be classified separately and must not be silently called `T`.

---

## 8. Corrected production frontier

The enstrophy-production endgame is now

\[
\boxed{
\begin{aligned}
\mathcal P
&\le \left(\frac12+\varepsilon_B\right)MZ,\\
\varepsilon_B\text{ small}
&\Longrightarrow \text{improved tail-independent Gronwall gate},\\
\varepsilon_B\text{ recurrently large}
&\Longrightarrow
\text{localized Betchov mismatch}
\lor
\text{remote/diffuse residual escape}.
\end{aligned}
}
\]

The previous hope of an unconditional global constant `<1/sqrt(3)` is therefore too strong without controlling spatial segregation. The correct strict-gap variable is `epsilon_B`.

Status: **THE UNIVERSAL `1/sqrt(3)` STRETCHING COEFFICIENT SPLITS EXACTLY INTO A `1/2` POSITIVE-MIDDLE CONTRIBUTION PLUS A SINGLE NORMALIZED NEGATIVE-MIDDLE BETCHOV RESIDUAL. SPATIAL SEGREGATION IS NOT IGNORED; IT IS NOW EXPLICITLY REPRESENTED BY `epsilon_B`. GLOBAL REGULARITY REMAINS UNPROVED.**