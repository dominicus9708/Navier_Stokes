# DSD Recurrent Master Parameter Substitution

Date: 2026-08-25

Status: **MASTER PARAMETER REDUCTION DERIVED / PRIMARY QUANTITATIVE BOTTLENECK IDENTIFIED / GLOBAL REGULARITY NOT PROVED.**

## 1. Starting frequency window

From `DSD_RECURRENT_BETCHOV_FREQUENCY_WINDOW_2026-08-25.md`, every nonzero bounded-`Z` recurrent survivor must satisfy

\[
\boxed{
\nu\bar\lambda
+\frac14-\frac{K_I}{2}
\le
C_B Z_+^{1/2}\bar\lambda^{3/4},
}
\]

with

\[
\boxed{
\bar\lambda\ge c_{\log}>0,
}
\]

and

\[
C_B=rac{8}{\pi 3^{9/4}}
\approx0.21498952055.
\]

The purpose of this note is to replace `K_I` and `c_log` by the best already-derived first-hitting and active-core expressions.

---

## 2. First-hitting Type-I constant

The continuous backward first-hitting inheritance gives

\[
\boxed{
K_I
=
\frac{q^2}{q-1}L_+.
}
\]

Therefore the exact recurrent frequency window becomes

\[
\boxed{
\nu\bar\lambda
+\frac14
-
\frac{q^2}{2(q-1)}L_+
\le
C_BZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

Thus a long normalized stage directly weakens the rigidity margin.

---

## 3. Moving-variance stage ceiling

On the persistent low-turnover moving-core corridor, the repository gives

\[
\boxed{
L_+
\le
\Pi_V\frac{R_V^2}{\nu},
}
\]

where

\[
\Pi_V
=
\frac{C_{var}}
{(1-\eta)V_-}
\left[
\frac14(\log q)V_+
+F_0
+\frac12\kappa_V
\right].
\]

Hence

\[
\boxed{
K_I
\le
\frac{q^2}{q-1}
\Pi_V\frac{R_V^2}{\nu}.
}
\]

Substitution gives the sufficient comparison framework

\[
\boxed{
\nu\bar\lambda
+\frac14
-
\frac{q^2}{2(q-1)}
\Pi_V\frac{R_V^2}{\nu}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

Large `Pi_V` or large `R_V` is already typed as turnover/spreading rather than a free constant on the intended non-`T` lane.

---

## 4. Active-core logarithmic frequency floor

The recurrent active-core invariant-measure calculation gives

\[
\boxed{
c_{\log}
=
 d_*\frac{\kappa_Q(R_*)z_*}{Z_+},
}
\]

with

\[
\kappa_Q(R_*)
=S_3|B_{R_*}|^{-2/3},
\qquad
S_3=3\left(\frac\pi2\right)^{4/3}.
\]

Since

\[
|B_R|=\frac{4\pi}{3}R^3,
\]

this simplifies to

\[
\boxed{
\kappa_Q(R)
=
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac1{R^2}
\approx
\frac{2.1080877498}{R^2}.
}
\]

Therefore

\[
\boxed{
c_{\log}
=
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2Z_+}.
}
\]

The key dependence is

\[
\boxed{c_{\log}\propto Z_+^{-1}.}
\]

---

## 5. Fully substituted recurrent gate

Every survivor on this corridor must admit some

\[
\bar\lambda
\ge
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2Z_+}
\]

such that

\[
\boxed{
\nu\bar\lambda
+\frac14
-
\frac{q^2}{2(q-1)}
\Pi_V\frac{R_V^2}{\nu}
\le
\frac{8}{\pi3^{9/4}}
Z_+^{1/2}\bar\lambda^{3/4}.
}
\]

This is now expressed entirely in finite normalized core/stage quantities.

No velocity `L3` tail parameter appears.

---

## 6. Empty-window certificate after stage substitution

The Young-free quartic analysis gives an empty frequency window whenever

\[
\frac14-\frac{K_I}{2}
>
\frac{16}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
\]

Using the stage ceiling, a sufficient condition is

\[
\boxed{
\frac14
-
\frac{q^2}{2(q-1)}
\Pi_V\frac{R_V^2}{\nu}
>
\frac{16}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
}
\]

Equivalently,

\[
\boxed{
\frac{q^2}{q-1}
\Pi_V\frac{R_V^2}{\nu}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<
\frac12.
}
\]

This displays two independent costs:

1. normalized stage-time/turnover cost;
2. bounded-enstrophy residual-capacity cost.

---

## 7. Frequency-floor certificate

When `K_I<=1/2`, the frequency window implies

\[
\bar\lambda
\le
C_B^4\frac{Z_+^2}{\nu^4},
\]

where

\[
\boxed{
C_B^4
=
\frac{4096}{19683\pi^4}
\approx0.00213633406062.
}
\]

But the active core gives

\[
\bar\lambda
\ge
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2Z_+}.
\]

Therefore a convenient sufficient contradiction is

\[
\boxed{
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2Z_+}
>
C_B^4\frac{Z_+^2}{\nu^4}.
}
\]

Equivalently,

\[
\boxed{
Z_+^3
<
\frac{
u^4}{C_B^4}
\frac{3^{5/3}\pi^{2/3}}{2^{8/3}}
\frac{d_*z_*}{R_*^2}.
}
\]

Thus sufficiently small normalized enstrophy ceiling relative to the occupied active-core mass closes the recurrent branch.

---

## 8. Why `Z_+` is the main quantitative bottleneck

The three relevant scalings are

\[
\text{Betchov residual capacity}
\sim Z_+^{1/2},
\]

\[
	ext{cubic correction in the empty-window test}
\sim Z_+^2,
\]

and

\[
	ext{active-core frequency floor}
\sim Z_+^{-1}.
\]

Hence increasing `Z_+` helps the survivor in all three ways:

- it enlarges available residual production;
- it enlarges the cubic correction;
- it weakens the guaranteed frequency floor.

Therefore

\[
\boxed{
\text{mere boundedness of }Z
\text{ is qualitatively insufficient; the magnitude of }Z_+
\text{ is decisive.}
}
\]

This explains why a proof based only on `sup Z<infinity` stalls even after the tail is removed from the rigidity certificate.

---

## 9. Secondary bottleneck: stage persistence

The second adverse parameter is

\[
\boxed{
K_I
\lesssim
\frac{q^2}{q-1}
\Pi_V\frac{R_V^2}{\nu}.
}
\]

If this term is large, the recurrent orbit has enough normalized time per first-hitting generation to pay the required stretching.

But unlike `Z_+`, a large stage factor is already structurally typed:

\[
\Pi_V\uparrow
\Longrightarrow
\text{loss of persistent variance / shell flux / endpoint reshaping},
\]

and

\[
R_V\uparrow
\Longrightarrow
\text{moving-core spatial spreading}.
\]

Thus on the strict non-`T` corridor the stage term is in principle attackable by the existing turnover ledger.

---

## 10. DSD audit and updated proof map

The bounded-`Z` recurrent branch is reduced to the finite tuple

\[
\boxed{
(q,\nu,Z_+,d_*,z_*,R_*,\Pi_V,R_V).
}
\]

Every quantity has a formed mathematical role:

- `q`: fixed first-hitting scale ratio;
- `nu`: viscosity;
- `Z_+`: normalized enstrophy ceiling;
- `d_*`: active-window density;
- `z_*`: occupied core enstrophy floor;
- `R_*`: active-core radius;
- `Pi_V`: moving-variance persistence/turnover factor;
- `R_V`: moving variance radius.

The primary unresolved quantitative task on this branch is now

\[
\boxed{
\text{derive a sufficiently strong upper control of }Z_+
\text{ from bounded-}Z\text{ recurrence, or else route large }Z_+
\text{ into remote enstrophy/turnover structure.}
}
\]

This links the bounded-`Z` endgame directly to the separately identified normalized-enstrophy escape audit rather than treating `Z_+` as a harmless constant.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
