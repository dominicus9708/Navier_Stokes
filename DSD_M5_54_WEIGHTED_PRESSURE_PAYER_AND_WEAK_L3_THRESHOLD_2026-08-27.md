# DSD M5-54 — Weighted Pressure Payer and the Weak-`L^3` Threshold

Date: 2026-08-27

Status: **EXACT CRITICAL CAUCHY/POISSON/SOBOLEV LEDGER / POSITIVE MEAN `D3` DISSIPATION REQUIRES A POSITIVE MEAN WEIGHTED PRESSURE PAYER `int |U||P|^2` / CALDERON--ZYGMUND PLUS LORENTZ--SOBOLEV BOUNDS THAT PAYER BY `C ||U||_{L^{3,infty}}^2 D3` / THIS RECOVERS A NONZERO WEAK-CRITICAL SIZE THRESHOLD BUT DOES NOT CLOSE THE LARGE-CRITICAL SURVIVOR / GLOBAL REGULARITY UNPROVED.**

## 1. Gate inherited from M5-53

For sufficiently large monotone cutoff radius, M5-53 reduces the positive-density pump balance to positive mean pressure work:

\[
\nu\overline{\mathcal D_{3,R}}
\lesssim
\overline{\mathcal P_R}
\]

up to errors that can be made arbitrarily small.

Here

\[
\mathcal P_R
=
\int\chi_RP\,\nabla\cdot(|U|U)dy.
\]

Since `div U=0`,

\[
\nabla\cdot(|U|U)
=
U\cdot\nabla |U|.
\]

The natural pressure payer is therefore weighted by `|U|`.

---

## 2. Pointwise structure of the `D3` dissipation

Let

\[
a:=|U|.
\]

M5-50 defined

\[
\mathcal D_3(U)
=
\int
\left[
 a|\nabla U|^2
+a^{-1}\sum_j(U\cdot\partial_jU)^2
\right]dy.
\]

Because

\[
U\cdot\partial_jU
=a\,\partial_ja,
\]

the second term is

\[
a^{-1}\sum_j(U\cdot\partial_jU)^2
=
a|\nabla a|^2.
\]

Also

\[
|U\cdot\nabla a|^2
\le
a^2|\nabla a|^2.
\]

Hence

\[
\boxed{
\frac{|U\cdot\nabla a|^2}{a}
\le
a|\nabla a|^2
\le
\text{`D3` density}.
}
\]

---

## 3. Weighted pressure payer

Define

\[
\boxed{
\mathcal W_R(U,P)
:=
\int\chi_R a|P|^2dy.
}
\]

Then Cauchy--Schwarz gives

\[
\begin{aligned}
|\mathcal P_R|
&=
\left|
\int\chi_R P\,U\cdot\nabla a\,dy
\right|\\
&\le
\left(
\int\chi_Ra|P|^2dy
\right)^{1/2}
\left(
\int\chi_R
\frac{|U\cdot\nabla a|^2}{a}dy
\right)^{1/2}\\
&\le
\boxed{
\mathcal W_R^{1/2}
\mathcal D_{3,R}^{1/2}.
}
\end{aligned}
\]

Equivalently, for any `epsilon>0`,

\[
|\mathcal P_R|
\le
\frac\epsilon2\mathcal D_{3,R}
+
\frac1{2\epsilon}\mathcal W_R.
\]

This is the critical pressure/dissipation pairing naturally associated with the cubic ledger.

---

## 4. Mean lower bound forced by a recurrent pump

Ignore for the moment the arbitrarily small large-cutoff error from M5-53.

If

\[
\nu\overline{\mathcal D_{3,R}}
\le
\overline{\mathcal P_R},
\]

then time Cauchy--Schwarz gives

\[
\overline{\mathcal P_R}
\le
\left(
\overline{\mathcal W_R}
\right)^{1/2}
\left(
\overline{\mathcal D_{3,R}}
\right)^{1/2}.
\]

For a positive-density pump,

\[
\overline{\mathcal D_{3,R}}>0.
\]

Therefore

\[
\boxed{
\overline{\mathcal W_R}
\ge
\nu^2
\overline{\mathcal D_{3,R}}.
}
\]

With the M5-53 cutoff error retained, the same inequality holds with an arbitrarily small loss once `R` is chosen sufficiently large.

Thus the recurrent survivor needs a persistent weighted pressure-square payer, not merely occasional pressure spikes.

---

## 5. Global weighted pressure quantity is tail-integrable

Under the critical tails

\[
|U(y)|\lesssim |y|^{-1},
\qquad
|P(y)|\lesssim |y|^{-2},
\]

we have

\[
|U||P|^2
\lesssim
|y|^{-5}.
\]

Since

\[
\int_R^\infty r^{-5}r^2dr<\infty,
\]

the global weighted payer

\[
\boxed{
\mathcal W
:=
\int_{\mathbb R^3}|U||P|^2dy
}
\]

is compatible with the `1/r` weak-critical ancestry even though the global cubic mass `int |U|^3` may diverge logarithmically.

This makes `W` a better finite critical pressure descriptor than the unrenormalized global cubic mass.

---

## 6. Pressure-Poisson upper bound through `L^5`

The pressure-Poisson relation gives, for the Riesz transforms,

\[
P
=
\mathcal R_i\mathcal R_j(U_iU_j).
\]

By the Calderon--Zygmund estimate in `L^{5/2}`,

\[
\|P\|_{L^{5/2}}
\le
C_{CZ}
\|U\otimes U\|_{L^{5/2}}
\le
C_{CZ}\|U\|_{L^5}^2.
\]

Then Holder gives

\[
\begin{aligned}
\mathcal W
&=
\int |U||P|^2dy\\
&\le
\|U\|_{L^5}
\|P^2\|_{L^{5/4}}\\
&=
\|U\|_{L^5}
\|P\|_{L^{5/2}}^2\\
&\le
\boxed{
C_{CZ}^2\|U\|_{L^5}^5.
}
\end{aligned}
\]

Thus the weighted pressure payer is controlled by the critical `L^5` velocity action.

---

## 7. Lorentz--Sobolev control of `L^5`

Let

\[
f:=a^{3/2}.
\]

If

\[
U\in L^{3,\infty},
\]

then

\[
f\in L^{2,\infty}
\]

with

\[
\|f\|_{L^{2,\infty}}
\sim
\|U\|_{L^{3,\infty}}^{3/2}.
\]

Also

\[
|\nabla f|^2
=
\frac94a|\nabla a|^2
\le
\frac94\,\text{`D3` density}.
\]

The homogeneous Sobolev estimate gives

\[
\|f\|_{L^6}^2
\le
C_S\mathcal D_3(U).
\]

Interpolate

\[
L^{2,\infty}
\quad\text{and}\quad
L^6
\]

to `L^{10/3}`:

\[
\|f\|_{L^{10/3}}
\le
C
\|f\|_{L^{2,\infty}}^{2/5}
\|f\|_{L^6}^{3/5}.
\]

Raising to the power `10/3` yields

\[
\int a^5dy
\le
\boxed{
C
\|U\|_{L^{3,\infty}}^2
\mathcal D_3(U).
}
\]

Equivalently,

\[
\boxed{
\|U\|_{L^5}^5
\le
C
\|U\|_{L^{3,\infty}}^2
\mathcal D_3(U).
}
\]

---

## 8. Critical upper bound for the pressure payer

Combining Sections 6--7,

\[
\boxed{
\mathcal W
\le
C_*
\|U\|_{L^{3,\infty}}^2
\mathcal D_3(U).
}
\]

If the compact recurrent orbit obeys the uniform weak-critical bound

\[
\|U(\eta)\|_{L^{3,\infty}}
\le M
\]

then

\[
\boxed{
\mathcal W(\eta)
\le
C_*M^2\mathcal D_3(\eta).
}
\]

This is scale invariant on both sides.

---

## 9. Necessary weak-`L^3` size of the recurrent survivor

The mean lower requirement from Section 4 and the upper bound from Section 8 give schematically

\[
\nu^2\overline{\mathcal D_3}
\lesssim
\overline{\mathcal W}
\le
C_*M^2\overline{\mathcal D_3}.
\]

For a nonzero positive-density pump,

\[
\overline{\mathcal D_3}>0.
\]

Hence necessarily

\[
\boxed{
M
\gtrsim
\frac\nu{\sqrt{C_*}}.
}
\]

Thus a recurrent pump-to-defect survivor must live above a nonzero weak-critical size threshold.

This is consistent with classical small-critical-data regularity mechanisms.

It is not a large-data contradiction.

---

## 10. Layer-cake relation to the M5-37 pressure tail

Recall

\[
Q_P(\lambda)
:=
\int_{a>\lambda}|P|^2dy.
\]

Since

\[
a(y)
=
\int_0^\infty
\mathbf 1_{a(y)>\lambda}\,d\lambda,
\]

Fubini gives the exact layer-cake identity

\[
\boxed{
\mathcal W
=
\int_0^\infty Q_P(\lambda)d\lambda.
}
\]

Therefore the M5-37 threshold pressure-tail object and the M5-54 weighted pressure payer are not separate constructions.

They are different amplitude resolutions of the same pressure-square resource.

M5-37 controls a derivative of `Q_P` at a first-hit threshold;
M5-54 controls the amplitude integral of `Q_P` in the long-time cubic ledger.

This is the desired bridge between the two branches.

---

## 11. Why the bridge does not yet close the proof

M5-37 gives at a positive first hit

\[
\lambda[-Q_P'(\lambda)]
\ge
\nu^2D_\lambda^{surf}
+
\nu^2A_*.
\]

But a strict lower bound on `-Q_P'` at one amplitude value does not by itself force a fixed excess in

\[
\int_0^\infty Q_P(\lambda)d\lambda.
\]

To obtain such an excess one needs quantitative control of the amplitude width over which the strict derivative gap persists.

That is now the narrowest surviving use of the M5-37 margin.

---

## 12. DSD audit

### GREEN — exact critical relations

- pressure work pairs by Cauchy with `W^{1/2} D3^{1/2}`;
- `W=int |U||P|^2` is finite under `1/r` / `1/r^2` tails;
- `W <= C ||U||_5^5` by pressure-Poisson Calderon--Zygmund theory;
- `||U||_5^5 <= C ||U||_{L^{3,infty}}^2 D3` by Lorentz--Sobolev interpolation;
- `W = int_0^infty Q_P(lambda) dlambda` by layer cake.

### GREEN — pruning consequence

A sufficiently small weak-`L^3` recurrent survivor cannot sustain the required positive pressure payer. The remaining survivor is necessarily a genuinely large critical object.

### YELLOW — next pressure-tail branch

Use W1 compactness/transversality to test whether the strict M5-37 derivative gap at `lambda_c` persists on a uniform amplitude interval

\[
|\lambda-\lambda_c|<\delta_*.
\]

If so, the pointwise pressure-tail overpay would become a fixed integrated excess in `W`, which can then be compared with the M5-54 upper bound.

### RED — branch closed

The generic weighted Cauchy + weak-`L^3` estimate alone does not exclude large critical recurrence; forcing it to do so would only repackage known small-data control.

---

## 13. New proof gate

The next calculation is no longer to seek another norm.

It is to determine whether the **strict first-hit pressure-tail derivative gap has a uniform amplitude thickness** on the compact W1 pump class.

Schematically,

\[
\boxed{
\text{pointwise strict gap in }-Q_P'(\lambda_c)
\stackrel{?}{\Longrightarrow}
\text{bandwise excess in }\int Q_P(\lambda)d\lambda.
}
\]

If the answer is yes with scale-independent width, the strict W1 margin finally becomes an additive finite pressure resource.

If the answer is no, the M5-37 route must be weakened accordingly.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
