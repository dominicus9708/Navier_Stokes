# DSD M17-064 — Oblique kappa-gradient octupole has an exact h-gradient recharge law and half-slope recurrence

Date: 2026-09-04
Canonical ID: **M17-064**

Status: **INTERNAL OBLIQUE KAPPA-GRADIENT RECHARGE GATE / M17-058 SHOWS THAT ON THE SEMILINEAR REGULAR NODAL BRANCH `grad_h kappa=0`, SO `grad kappa=kappa_3 e_3`, AND THAT THE OBLIQUE-SLANT FORBIDDEN PAYER-OCTUPOLE SHARE IS A NONZERO FROZEN ANGULAR CONSTANT TIMES `kappa_3 |p| |Q|_F^2`. LET `h=D_B kappa`. THE EXACT SCALAR-GRADIENT COMMUTATOR `D_B grad kappa=grad h-(grad B)^T grad kappa`, TOGETHER WITH THE NODAL CORE `grad B=diag(lambda+1/2,lambda+1/2,-2lambda+1/2)`, GIVES `grad_h h=0` AND `D_B kappa_3=partial_3 h+(2lambda-1/2)kappa_3`. COMBINING THIS WITH `D_B|p|=3lambda|p|` AND `D_B|Q|_F^2=(2kappa-3)|Q|_F^2` YIELDS AN EXACT FORCED OCTUPOLE LAW `D_B o_kappa=(2kappa+5lambda-7/2)o_kappa+C_ang|p||Q|_F^2 partial_3h`. ON A UNIFORMLY RECURRENT OBLIQUE SUBBRANCH WITH `kappa_3` BOUNDED AWAY FROM ZERO, `mean kappa=3/2` AND `mean lambda=0` FORCE THE NEW OBLIGATION `mean[(partial_3 h)/kappa_3]=1/2`. IF `kappa_3` REACHES ZERO, IT IS NOT AN INVARIANT ZERO UNLESS `partial_3h` ALSO VANISHES; THE BRANCH MUST PASS THROUGH AN AXIAL-GRADIENT TURNOVER OR A DEGENERATE EVENT. UNDER THE ADDITIONAL SYNCHRONIZED LAW `h=f(kappa,theta)` USED IN THE M5 ZERO-LEVEL ANALYSIS, THE RATIO IS EXACTLY `f_kappa`, SO THE SAME RECURRENT OBLIQUE BRANCH REQUIRES `mean f_kappa(kappa_0(theta),theta)=1/2`. THIS IS A DIRECT DIFFERENTIAL BRIDGE BETWEEN THE LOCAL L=3 OCTUPOLE AND THE KAPPA-HYSTERESIS DERIVATIVE, BUT IT IS NOT A SIGN CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Oblique-slant input from M17-058

On the regular semilinear nodal branch,

\[
\boxed{\nabla_h\kappa=0,}
\]

so

\[
\boxed{\nabla\kappa=\kappa_3 e_3.}
\]

For genuinely oblique slant, the frozen angular factor

\[
\gamma_{Qp}
=\frac{(E_Q\widehat p)\cdot Q^2\widehat p}{|Q|_F^2}
\]

is nonzero and materially invariant.

M17-058 gives

\[
\boxed{
\mathfrak o_\kappa
=\frac4{15}\gamma_{Qp}\,
\kappa_3|p||Q|_F^2.
}
\]

Define the signed constant

\[
\boxed{c_{ang}:=\frac4{15}\gamma_{Qp}\ne0.}
\]

Then

\[
\boxed{
\mathfrak o_\kappa
=c_{ang}\kappa_3|p||Q|_F^2.
}
\]

---

## 2. Gradient transport for kappa

Let

\[
\boxed{h:=D_B\kappa.}
\]

For any scalar,

\[
D_B(\nabla\kappa)
=\nabla h-(\nabla B)^T\nabla\kappa.
\]

At a regular winding node M17-010 gives

\[
\boxed{
\nabla B
=\operatorname{diag}
\left(
\lambda+\frac12,
\lambda+\frac12,
-2\lambda+\frac12
\right).
}
\]

Insert

\[
\nabla\kappa=\kappa_3e_3.
\]

---

## 3. Horizontal h-gradient must vanish on the regular nodal branch

The horizontal components of the gradient law are

\[
D_B(\nabla_h\kappa)
=\nabla_hh.
\]

But the semilinear nodal extension gives

\[
\nabla_h\kappa=0
\]

at every retained regular material nodal time.
Therefore

\[
\boxed{\nabla_hh=0.}
\]

Thus the material derivative of the CE-H multiplier is itself horizontally stationary to first order at the regular nodal core.

This is an exact new local consequence of maintaining the semilinear nodal geometry.

---

## 4. Exact axial-gradient recharge law

The vertical component gives

\[
D_B\kappa_3
=\partial_3h
-\left(-2\lambda+\frac12\right)\kappa_3.
\]

Hence

\[
\boxed{
D_B\kappa_3
=\partial_3h
+\left(2\lambda-\frac12\right)\kappa_3.
}
\]

This shows that the axial multiplier gradient has two mechanisms:

1. homogeneous strain/similarity multiplier `2lambda-1/2`;
2. genuine recharge by the axial gradient `partial_3 h`.

Unlike the unforced principal octupole modes of M17-060--061, `kappa_3=0` is not automatically invariant.

---

## 5. Material laws for the geometric amplitudes

M17-024 gives

\[
\boxed{D_B|p|=3\lambda|p|.}
\]

M17-014 gives

\[
D_BQ=\left(\kappa-\frac32\right)Q,
\]

hence

\[
\boxed{
D_B|Q|_F^2
=(2\kappa-3)|Q|_F^2.
}
\]

The angular coefficient `c_ang` is materially constant.

---

## 6. Exact oblique kappa-octupole law

Differentiate

\[
\mathfrak o_\kappa
=c_{ang}\kappa_3|p||Q|_F^2.
\]

Using Sections 4--5,

\[
\boxed{
\begin{aligned}
D_B\mathfrak o_\kappa
={}&\left(2\kappa+5\lambda-\frac72\right)
\mathfrak o_\kappa\\
&+c_{ang}|p||Q|_F^2\,\partial_3h.
\end{aligned}
}
\]

Thus the oblique multiplier-gradient octupole is a forced scalar cocycle.

The homogeneous exponent

\[
2\kappa+5\lambda-\frac72
\]

has the same recurrent mean `-1/2` that appeared in the closed principal `X_+` mode, but here an explicit recharge channel survives.

---

## 7. Logarithmic form on the nonzero-kappa3 subbranch

Where

\[
\kappa_3\ne0,
\]

or equivalently where `o_kappa` is nonzero on genuine oblique slant,

\[
\boxed{
D_B\log|\kappa_3|
=2\lambda-\frac12
+\frac{\partial_3h}{\kappa_3}.
}
\]

Likewise

\[
\boxed{
D_B\log|\mathfrak o_\kappa|
=2\kappa+5\lambda-\frac72
+\frac{\partial_3h}{\kappa_3}.
}
\]

The ratio

\[
\frac{\partial_3h}{\kappa_3}
\]

is therefore the exact signed recharge rate not already accounted for by the known strain/kappa multipliers.

---

## 8. Recurrent half-slope law

Assume a uniformly recurrent oblique regular branch with

\[
0<c_3\le|\kappa_3|\le C_3<\infty,
\]

in addition to the existing uniform regularity bounds for `p` and `Q`.

Then recurrence of `kappa_3` gives zero mean logarithmic drift:

\[
0
=2\langle\lambda\rangle
-\frac12
+\left\langle\frac{\partial_3h}{\kappa_3}\right\rangle.
\]

M17-024 gives

\[
\langle\lambda\rangle=0.
\]

Therefore

\[
\boxed{
\left\langle
\frac{\partial_3h}{\kappa_3}
\right\rangle
=\frac12.
}
\]

The same law follows from recurrence of `o_kappa`, using

\[
\langle\kappa\rangle=\frac32
\]

and

\[
\langle\lambda\rangle=0.
\]

Thus the result is internally consistent with both the multiplier-gradient and octupole descriptions.

---

## 9. Axial-gradient zero events

If

\[
\kappa_3=0,
\]

then Section 4 reduces to

\[
\boxed{D_B\kappa_3=\partial_3h.}
\]

Hence:

- if `partial_3 h != 0`, the trajectory crosses the `kappa_3=0` state transversely and the local kappa-gradient octupole changes sign;
- if `partial_3 h = 0`, the event is degenerate and requires higher-jet analysis;
- `kappa_3=0` is not an invariant subbranch unless the recharge also vanishes.

Thus the oblique survivor splits into a nonzero-gradient recurrence class and an axial-gradient-turnover/degeneration class.

---

## 10. Conditional bridge to synchronized kappa dynamics

In the synchronized/relabeling branch used in the M5 zero-level analysis, assume additionally

\[
\boxed{h=f(\kappa,\theta).}
\]

Then spatial differentiation gives

\[
\partial_3h
=f_\kappa(\kappa,\theta)\kappa_3.
\]

Therefore wherever `kappa_3 != 0`,

\[
\boxed{
\frac{\partial_3h}{\kappa_3}
=f_\kappa(\kappa,\theta).
}
\]

The recurrent oblique law becomes

\[
\boxed{
\left\langle
f_\kappa(\kappa_0(\theta),\theta)
\right\rangle
=\frac12.
}
\]

This uses the nodal value `kappa_0(theta)` along the marked filament.
It does **not** imply the pointwise zero-level value `f_kappa(0,theta)=1/2` at every kappa crossing.

Thus the result is a genuine bridge to the M5 synchronized derivative descriptor without overclaiming a zero-level pointwise identity.

---

## 11. Relation to M5 hysteresis

M5-685's hysteresis uses

\[
h=D_B\kappa
\]

at kappa-zero crossings and weights the sign of `h` by material flux amplification.

M17-064 adds a new orthogonal descriptor:

\[
\boxed{
\frac{\partial_3h}{\partial_3\kappa}
}
\]

on the oblique nodal branch.

Thus the surviving oblique geometry must simultaneously realize

1. the required signed crossing bias in `h`;
2. the recurrent mean axial derivative bias `1/2` when `kappa_3` stays nonzero;
3. the fixed oblique angular octupole factor;
4. the global l=3 pressure/viscous alignment.

No theorem presently makes items 1--2 incompatible.

---

## 12. DSD analysis

The local oblique octupole has now been factorized into

\[
\boxed{
\text{frozen angle}
\times
\text{known geometric amplitudes}
\times
\text{axial kappa gradient}.
}
\]

The only way to recurrently resist its strict `-1/2` homogeneous mean drift is an explicit recharge through `partial_3h`.

This turns an abstract higher-jet screening channel into a derivative of the same scalar `h` already used by the hysteresis ledger.

---

## 13. DSD audit

### Audit A — assuming kappa3 is materially invariant
Rejected. It is forced by `partial_3h`.

### Audit B — dividing by kappa3 across zero events
Avoided. The logarithmic and mean laws apply only on the uniformly nonzero-gradient subbranch; zero events are separated.

### Audit C — treating the half-slope law as pointwise
Rejected. It is a recurrent mean identity.

### Audit D — identifying synchronized f_kappa at arbitrary kappa with its zero-level value
Rejected.

### Audit E — declaring h-hysteresis and h-gradient recurrence contradictory
Rejected. No sign incompatibility is proved yet.

### Audit F — proof status
Oblique slant is substantially narrowed but remains open.

---

## 14. Updated oblique-slant frontier

\[
\boxed{
R_{oblique}^{\kappa_3+H_3}
\Longrightarrow
R_{oblique}^{\kappa_3\ne0,
\ \langle h_3/\kappa_3\rangle=1/2}
\ \lor\
T_{\kappa_3=0}^{turnover/degenerate}
\ \lor\
T_{nodal/rank/interface}.
}
\]

The remaining third-q curvature octupole and global pressure lock still need to be combined with this recharge law.

---

## 15. Next target

The next highest-value step is to project the **full oblique local octupole**, not only its kappa-gradient share, into a frozen basis adapted to `(Qhat, phat)` and determine whether the curvature share can absorb the required recharge law independently.

This is the **Oblique Full-Octupole Reduction Gate (OFORG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
