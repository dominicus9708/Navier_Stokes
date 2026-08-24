# Ancient Enstrophy Gronwall Small-Type-I Gate — 2026-08-24

Status: **TAIL-INDEPENDENT RIGIDITY GATE ON THE VORTICITY-TIGHT ANCIENT BRANCH / GLOBAL REGULARITY NOT PROVED.**

This note derives a rigidity criterion for the restricted ancient solution using only global vorticity quantities. The velocity tail does not enter the proof.

The input is the vorticity-tight ancient branch already established in

- `ANCIENT_CONTINUOUS_BACKWARD_VORTICITY_TYPEI_2026-08-24.md`;
- `ANCIENT_BACKWARD_ENSTROPHY_PALINSTROPHY_DECAY_2026-08-24.md`.

The main observation is that backward decay of global enstrophy competes directly with the maximal logarithmic growth allowed by a Type-I vorticity coefficient.

---

## 1. Ancient enstrophy identity

Let

\[
Z(t):=\|\Omega(t)\|_2^2,
\qquad
Q(t):=\|\nabla\Omega(t)\|_2^2.
\]

For a smooth decaying ancient Navier--Stokes solution,

\[
\boxed{
\frac12Z'(t)+\nu Q(t)
=\mathcal P(t),
}
\]

where

\[
\mathcal P(t)
:=\int S:(\Omega\otimes\Omega)\,dx.
\]

For divergence-free whole-space fields,

\[
\|S\|_2^2=\frac12\|\Omega\|_2^2=\frac12Z.
\]

Also

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2
=\|\Omega\|_\infty Z^{1/2}.
\]

Hence

\[
|\mathcal P|
\le
\|S\|_2\|\Omega\|_4^2
\le
\frac1{\sqrt2}\|\Omega\|_\infty Z.
\]

Therefore

\[
\boxed{
Z'(t)
\le
\sqrt2\,\|\Omega(t)\|_\infty Z(t).
}
\]

The negative viscous term has only been discarded, so this inequality is unconditional inside the stated ancient class.

---

## 2. General backward-decay versus Type-I lemma

Assume that for sufficiently negative `t`,

\[
\boxed{
Z(t)\le C_Z|t|^{-\alpha}
}
\]

for some `alpha>0`, and

\[
\boxed{
\|\Omega(t)\|_\infty
\le
K|t|^{-1}.
}
\]

Fix `t<0` and take `t_0<t`. Integrating the logarithmic differential inequality gives

\[
Z(t)
\le
Z(t_0)
\exp\left(
\sqrt2K
\int_{t_0}^{t}\frac{ds}{|s|}
\right).
\]

Since `t_0<t<0`,

\[
\int_{t_0}^{t}\frac{ds}{|s|}
=
\log\frac{|t_0|}{|t|}.
\]

Thus

\[
\boxed{
Z(t)
\le
Z(t_0)
\left(
\frac{|t_0|}{|t|}
\right)^{\sqrt2K}.
}
\]

Using the backward decay of `Z(t_0)`,

\[
Z(t)
\le
C_Z|t|^{-\sqrt2K}
|t_0|^{\sqrt2K-\alpha}.
\]

If

\[
\boxed{
\sqrt2K<\alpha,
}
\]

then sending

\[
t_0\to-\infty
\]

gives

\[
\boxed{Z(t)=0.}
\]

Since `t<0` was arbitrary,

\[
\boxed{
\Omega\equiv0.
}
\]

For the decaying whole-space velocity this implies `U=0` up to the harmless constant velocity gauge, and finite energy fixes that gauge to zero.

Therefore:

\[
\boxed{
Z(t)=O(|t|^{-\alpha})
+\|\Omega(t)\|_\infty\le K|t|^{-1}
+\sqrt2K<\alpha
\Longrightarrow
U\equiv0.
}
\]

---

## 3. Apply the restricted first-hitting ancient decay

The vorticity-tight ancient branch gives

\[
\boxed{
Z(t)
\le
Z_+K_I^{1/2}|t|^{-1/2}.
}
\]

Thus

\[
\boxed{\alpha=\frac12.}
\]

The continuous first-hitting Type-I cap gives

\[
\boxed{
\|\Omega(t)\|_\infty
\le
\frac{K_I}{|t|},
}
\]

where, from the geometric stage estimate,

\[
\boxed{
K_I(q)
=
\frac{q^2}{q-1}L_+(q).
}
\]

Hence the ancient branch is rigid whenever

\[
\boxed{
\sqrt2K_I<\frac12.
}
\]

Equivalently,

\[
\boxed{
K_I
<
\frac1{2\sqrt2}
\approx0.3535533906.
}
\]

This criterion is independent of the spatial velocity tail.

---

## 4. Stage-length form of the closure certificate

Substitute

\[
K_I(q)=\frac{q^2}{q-1}L_+(q).
\]

A sufficient closure condition is

\[
\boxed{
L_+(q)
<
\frac{q-1}{2\sqrt2\,q^2}.
}
\]

This is the clean quantity that future finite-stage estimates should target.

It is important not to optimize in `q` while silently holding `L_+` fixed, because the stage ceiling itself may depend on the geometric threshold `q`.

If one nevertheless freezes `L_+` only as a benchmark, the factor

\[
\frac{q^2}{q-1}
\]

is minimized at

\[
q=2,
\]

where it equals `4`. In that benchmark,

\[
\boxed{
L_+
<
\frac1{8\sqrt2}
\approx0.08838834765
}
\]

suffices.

This benchmark is not asserted to be the globally optimal choice of `q`.

---

## 5. Comparison with the existing q=2 moving-ball pure corridor

The existing pure low-turnover ball-variance estimate at `q=2` gives, in the zero/quarter-tail analytic-scale benchmark,

\[
L_j
\le
0.7483880874\,r^2
\]

when the same normalization and `nu=1` convention are used.

If this particular ceiling is inserted into the new Gronwall criterion, then

\[
0.7483880874\,r^2
<
0.08838834765
\]

requires

\[
\boxed{
r<0.34366403.}
\]

This is only a numerical benchmark. That radius is already inside a subrange closed by stronger finite-stage pure-corridor arguments, so this substitution does not create a new global closure by itself.

The significance of the new gate is instead that **any future improvement of the stage Type-I coefficient immediately yields ancient rigidity without controlling the persistent velocity tail.**

---

## 6. Logarithmic form retaining viscosity

Do not discard viscosity and divide the enstrophy identity by `Z>0`:

\[
\boxed{
\frac d{dt}\log Z
\le
\sqrt2\|\Omega\|_\infty
-2\nu\frac QZ.
}
\]

Integrating from `t_0` to `t` gives

\[
\boxed{
\log\frac{Z(t)}{Z(t_0)}
\le
\sqrt2\int_{t_0}^{t}\|\Omega(s)\|_\infty ds
-2\nu\int_{t_0}^{t}\frac{Q(s)}{Z(s)}ds.
}
\]

Thus a logarithmic lower bound

\[
\int_{t_0}^{t}\frac{Q}{Z}ds
\ge
c_{log}\log\frac{|t_0|}{|t|}-O(1)
\]

would improve the effective exponent from

\[
\sqrt2K
\]

to

\[
\boxed{
\sqrt2K-2\nu c_{log}.
}
\]

The generalized closure condition would then be

\[
\boxed{
\sqrt2K-2\nu c_{log}<\alpha.
}
\]

For the present ancient decay `alpha=1/2`,

\[
\boxed{
\sqrt2K-2\nu c_{log}<\frac12.
}
\]

This is the natural next strengthening if the raw Type-I constant is too large.

---

## 7. Leray-variable interpretation of the viscous logarithmic tax

Let

\[
T=-t,
\qquad
s=-\log T,
\]

and

\[
W(Y,s)=T\Omega(x,t).
\]

Then

\[
Z_L(s)=\|W(s)\|_2^2
=T^{1/2}Z(t),
\]

and

\[
Q_L(s)=\|\nabla_YW(s)\|_2^2
=T^{3/2}Q(t).
\]

Therefore

\[
\boxed{
\frac{Q(t)}{Z(t)}dt
=
\frac{Q_L(s)}{Z_L(s)}ds.
}
\]

So `c_log` is precisely a long-Leray-time lower average of the frequency ratio

\[
\boxed{
\lambda_L(s)=\frac{Q_L(s)}{Z_L(s)}.
}
\]

This connects the new Gronwall gate directly to the already developed recurrent/projective frequency ledgers.

However, a positive average `Q_L` alone is not enough; one needs a lower average of the ratio `Q_L/Z_L`, or a uniform upper bound on `Z_L` together with sufficient active-window density.

---

## 8. Scope and anti-proof audit

This argument applies only to the **vorticity-tight ancient branch**, because the backward enstrophy decay

\[
Z(t)=O(|t|^{-1/2})
\]

was derived from the dynamic bound

\[
M(t)^{-1/2}\|\omega(t)\|_2^2\le Z_+.
\]

It does not close the broader diffuse-global-enstrophy-escape branch merely from relative Morrey compactness.

It also does not prove that the current numerical first-hitting constant satisfies the smallness condition.

The valid new result is the conditional tail-independent rigidity certificate

\[
\boxed{
K_I<1/(2\sqrt2)
\Longrightarrow
\text{the nontrivial vorticity-tight ancient survivor is impossible.}
}
\]

---

## 9. Current next calculation

There are now two ways to improve this gate without touching the persistent velocity tail:

1. sharpen the continuous first-hitting Type-I coefficient `K_I`, preferably by replacing the slabwise worst-case `q` loss by a continuous growth ledger;
2. obtain a positive logarithmic frequency tax
   \[
   c_{log}>0
   \]
   from the recurrent thick-core / projective / palinstrophy structure.

Either improvement lowers the required stage-smallness threshold.

Status: **ON THE VORTICITY-TIGHT ANCIENT BRANCH, BACKWARD ENSTROPHY DECAY AND A SMALL CONTINUOUS TYPE-I VORTICITY COEFFICIENT FORCE THE ANCIENT SOLUTION TO VANISH. THE SUFFICIENT THRESHOLD IS `K_I<1/(2sqrt2)`. THIS RIGIDITY GATE DOES NOT SEE THE VELOCITY TAIL. THE PRESENT PROOF PROGRAM HAS NOT YET SHOWN THAT THE REQUIRED CONSTANT SMALLNESS HOLDS. GLOBAL REGULARITY REMAINS UNPROVED.**