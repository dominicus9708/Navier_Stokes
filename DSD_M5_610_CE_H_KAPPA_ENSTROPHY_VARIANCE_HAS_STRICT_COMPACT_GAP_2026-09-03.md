# DSD M5-610 — CE-H kappa has a strict enstrophy-weighted variance gap on the compact marked hull

Date: 2026-09-03

Status: **STRICT SPECTRAL VARIANCE / CE-H GIVES `Delta W = kappa W`, SO `H=int kappa^2|W|^2` WHILE `P=-int kappa|W|^2` / THE FOURIER LOG-CONVEXITY INEQUALITY `P^2 <= E H` BECOMES EXACTLY NONNEGATIVITY OF THE ENSTROPHY-WEIGHTED VARIANCE OF KAPPA / EQUALITY WOULD FORCE `Delta W = c W` WITH ONE SPATIAL CONSTANT c, BUT THE WHOLE-SPACE LAPLACIAN HAS NO NONZERO L2 EIGENFUNCTION / THEREFORE EVERY NONZERO CE-H STATE HAS STRICT POSITIVE KAPPA VARIANCE / COMPACTNESS AND THE NONZERO CARRIER MARK UPGRADE THIS TO A UNIFORM POSITIVE GAP ON THE HARD COMPONENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H moment identities

Define

\[
E=\|W\|_2^2,
\qquad
P=\|\nabla W\|_2^2,
\qquad
H=\|\Delta W\|_2^2.
\]

On CE-H,

\[
\Delta W=\kappa W.
\]

Therefore

\[
\boxed{H=\int\kappa^2|W|^2dy.}
\]

M5-600 gives

\[
\boxed{P=-\int\kappa|W|^2dy.}
\]

---

## 2. Enstrophy probability measure

For a nonzero state define

\[
d\mu_E
:=
\frac{|W|^2}{E}dy.
\]

Then

\[
\boxed{
\mathbb E_{\mu_E}[\kappa]
=-\frac PE,
}
\]

and

\[
\boxed{
\mathbb E_{\mu_E}[\kappa^2]
=\frac HE.
}
\]

Hence

\[
\boxed{
\operatorname{Var}_{\mu_E}(\kappa)
=
\frac{EH-P^2}{E^2}.
}
\]

Thus the standard Fourier/log-convexity inequality

\[
P^2\le EH
\]

is precisely kappa-variance nonnegativity on CE-H.

---

## 3. Equality would imply a constant Laplacian eigenvalue

Equality in Cauchy--Schwarz between `W` and `Delta W` requires

\[
\Delta W=cW
\]

for one spatial constant `c` on the nonzero state.

Taking Fourier transforms,

\[
-|\zeta|^2\widehat W(\zeta)
=c\widehat W(\zeta).
\]

Thus `W-hat` would be supported on

\[
\{|\zeta|^2=-c\}
\]

when `c<0`, or on an empty/measure-zero set for `c>=0`.

Every such set has zero three-dimensional Lebesgue measure.

An `L2` Fourier transform supported on it must vanish almost everywhere.

Therefore

\[
\boxed{
EH=P^2
\Longrightarrow W=0.
}
\]

---

## 4. Strict nonzero-state gap

Every nonzero CE-H state therefore satisfies

\[
\boxed{EH-P^2>0.}
\]

Equivalently,

\[
\boxed{
\operatorname{Var}_{\mu_E}(\kappa)>0.
}
\]

The viscous eigenvalue cannot be spatially constant on the enstrophy support.

---

## 5. Uniform gap on the compact marked component

On the retained hard component:

1. `E,P,H` are continuous state observables under the all-order compactness established earlier;
2. the marked persistent carrier excludes `W=0`;
3. the component is compact.

Therefore the continuous functional

\[
\mathcal V_\kappa:=EH-P^2
\]

cannot approach zero without producing a limit state with `mathcal V_kappa=0`, hence `W=0`, contradicting the mark.

Consequently there exists

\[
v_\kappa>0
\]

such that

\[
\boxed{
EH-P^2\ge v_\kappa>0
}
\]

throughout the compact marked CE-H component.

If desired, using the compact positive lower/upper bounds on `E`, this gives a corresponding positive lower bound for `Var_muE(kappa)` itself.

---

## 6. Relation to M5-603--609

The CE-H survivor now satisfies simultaneously:

\[
\langle\bar\kappa_\Phi\rangle=0
\]

on persistent material-flux lineages,

\[
\mathbb E_{\mu_E}\kappa=-P/E<0,
\]

\[
\operatorname{Var}_{\mu_E}(\kappa)\ge c>0,
\]

and

\[
\mathbb E_{\mu_E}[y\cdot\nabla\kappa]=2P/E>0.
\]

Thus the remaining measure mismatch cannot be resolved by making `kappa` almost spatially constant.

A genuinely heterogeneous sign/level-set landscape is mandatory.

---

## 7. Firewall

Positive variance does not by itself force positive values of `kappa`; a purely negative but nonconstant distribution is possible at the scalar level.

Positive-`kappa` recurrence enters only when the material-flux oscillation branch from M5-606 is used.

Therefore M5-610 strengthens heterogeneity but is not yet a contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
