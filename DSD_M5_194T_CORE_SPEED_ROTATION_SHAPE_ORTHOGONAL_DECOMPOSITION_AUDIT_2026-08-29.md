# DSD M5-194T — Core-Speed Rotation/Shape Orthogonal-Decomposition Audit

Date: 2026-08-29

Parent: `DSD_M5_194S_TWO_LERAY_CLOCK_ALIGNMENT_AND_ALPHA_LIMIT_SPEED_FLOOR_TRANSFER_2026-08-29.md`

Status: **POSITIVE KINEMATIC REDUCTION / THE TRANSFERRED PINEAU--VICOL CORE-SPEED FLOOR CAN BE SPLIT EXACTLY INTO A ROTATIONAL-ORBIT TANGENT COMPONENT AND AN ORTHOGONAL SHAPE-TIME COMPONENT ON ONE FIXED SIMILARITY BALL / A GENERAL COMPACT ALPHA-LIMIT IS THEREFORE FORCED TO PAY EITHER A UNIFORM ROTATIONAL SPEED OR A UNIFORM SHAPE SPEED (UP TO A FIXED THRESHOLD SPLIT) / THE RSS PHASE-PAYMENT LEDGER APPLIES ONLY TO THE ROTATIONAL-TANGENT BRANCH AND MUST NOT BE IMPORTED TO THE SHAPE BRANCH / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-194S

On the spatial-Type-I / pressure-annulus / strong local compactness corridor, every checkpoint alpha-limit `V(Y,s)` satisfies, on a fixed similarity ball `B_R`,

\[
\boxed{
\|V_s(s)\|_{L^2(B_R)}\ge \sigma_0>0
\qquad\text{for every }s\in\mathbb R.
}
\]

The stationary branch is therefore excluded.

The remaining question is what kind of motion pays this speed.

It is invalid to write

\[
V_s=\alpha\mathcal GV
\]

unless the orbit has already been proved to be a rigidly rotating relative equilibrium.

---

## 2. Rotation generators on the fixed core

Let `A_1,A_2,A_3` be a fixed basis of the Lie algebra `so(3)`.

For each generator define the infinitesimal rotation action on vector fields by

\[
\boxed{
\mathcal R_a V
:=
A_aV-(A_aY)\cdot\nabla V,
\qquad a=1,2,3.
}
\]

The sign convention is immaterial for the norm decomposition.

For fixed `s`, define the rotational tangent space

\[
\boxed{
\mathscr T_{rot}(s)
:=
\operatorname{span}
\{\mathcal R_1V(s),\mathcal R_2V(s),\mathcal R_3V(s)\}
\subset L^2(B_R;\mathbb R^3).
}
\]

Its dimension may be smaller than three if the instantaneous field has rotational symmetries.

---

## 3. Orthogonal projection

Let

\[
P_{rot}(s)
:
L^2(B_R)\to\mathscr T_{rot}(s)
\]

be the Hilbert-space orthogonal projection.

Define

\[
\boxed{
V_s^{rot}:=P_{rot}V_s,
}
\]

and

\[
\boxed{
V_s^{shape}:=(I-P_{rot})V_s.
}
\]

Then exactly

\[
\boxed{
V_s=V_s^{rot}+V_s^{shape}
}
\]

and

\[
\boxed{
\langle V_s^{rot},V_s^{shape}\rangle_{L^2(B_R)}=0.
}
\]

Therefore

\[
\boxed{
\|V_s\|_2^2
=
\|V_s^{rot}\|_2^2
+
\|V_s^{shape}\|_2^2.
}
\]

This is an exact kinematic identity and requires no approximation to an RSS orbit.

---

## 4. Quantitative speed split

Since

\[
\|V_s\|_2\ge\sigma_0,
\]

we have

\[
\|V_s^{rot}\|_2^2
+
\|V_s^{shape}\|_2^2
\ge\sigma_0^2.
\]

Hence at every time at least one of

\[
\boxed{
\|V_s^{rot}\|_2
\ge\frac{\sigma_0}{\sqrt2}
}
\]

or

\[
\boxed{
\|V_s^{shape}\|_2
\ge\frac{\sigma_0}{\sqrt2}
}
\]

holds.

More generally, for any `0<eta<1`,

\[
\boxed{
\|V_s^{rot}\|_2\ge\eta\sigma_0
\quad\lor\quad
\|V_s^{shape}\|_2
\ge\sqrt{1-\eta^2}\,\sigma_0.
}
\]

Thus the perpetual core motion has a formed two-channel decomposition:

\[
\boxed{
\text{rotational tangent payment}
\quad\lor\quad
\text{shape-time payment}.
}
\]

---

## 5. Angular-velocity coefficients on the nondegenerate rotational branch

Let the Gram matrix be

\[
\boxed{
G_{ab}(s)
:=
\langle\mathcal R_aV,\mathcal R_bV\rangle_{L^2(B_R)}.
}
\]

Let

\[
b_a(s)
:=
\langle V_s,\mathcal R_aV\rangle.
\]

On the range of `G`, the minimum-norm angular coefficient vector is

\[
\boxed{
\alpha(s)=G(s)^\dagger b(s),
}
\]

where `dagger` is the Moore--Penrose inverse.

Then

\[
\boxed{
V_s^{rot}
=
\sum_{a=1}^3\alpha_a(s)\mathcal R_aV.
}
\]

If the smallest nonzero eigenvalue of `G` has a positive lower bound

\[
\lambda_{rot,-}>0
\]

and the largest eigenvalue is bounded by `lambda_rot,+`, rotational speed and angular coefficient are quantitatively equivalent:

\[
\lambda_{rot,-}|\alpha|^2
\le
\|V_s^{rot}\|_2^2
\le
\lambda_{rot,+}|\alpha|^2.
\]

Degeneration of this Gram matrix is itself a symmetry/axis-degeneracy channel and must be kept separate rather than dividing by a vanishing rotational generator norm.

---

## 6. Exact RSS is a special case

For a true rotating relative equilibrium,

\[
V(Y,s)=R(s)U(R(s)^{-1}Y)
\]

with constant-axis constant-speed rotation, one has

\[
V_s^{shape}=0
\]

and

\[
V_s=V_s^{rot}=\alpha\mathcal RV.
\]

Only in this case does the existing file

`DSD_RSS_SPEED_FLOOR_TO_ROTATIONAL_PHASE_PAYMENT_2026-08-25.md`

apply directly.

That note gives, in the exact RSS setting, the nontrivial phase-payment condition

\[
\boxed{
\frac{|I|}{2\sqrt A}
+
\frac{|B|}{\sqrt A}
\ge\delta_{rot}>0.
}
\]

Thus the present decomposition correctly embeds the old RSS calculation as the zero-shape-speed boundary of the general alpha-limit problem.

---

## 7. Persistent-rotation time set versus persistent-shape time set

Define

\[
E_{rot}
:=
\left\{
 s:
\|V_s^{rot}(s)\|_2
\ge\frac{\sigma_0}{\sqrt2}
\right\},
\]

\[
E_{shape}
:=
\left\{
 s:
\|V_s^{shape}(s)\|_2
\ge\frac{\sigma_0}{\sqrt2}
\right\}.
\]

Then

\[
\boxed{
E_{rot}\cup E_{shape}=\mathbb R.
}
\]

For any interval `I`,

\[
|I|
\le
|E_{rot}\cap I|
+|E_{shape}\cap I|.
\]

Hence on every arbitrarily long interval at least one channel occupies at least half the time:

\[
\boxed{
|E_{rot}\cap I|\ge\frac{|I|}{2}
\quad\lor\quad
|E_{shape}\cap I|\ge\frac{|I|}{2}.
}
\]

Along a sequence of growing intervals, a finite pigeonhole yields at least one channel with positive lower time density.

Thus perpetual motion cannot evade both channels by alternating them on ever sparser sets.

---

## 8. Action lower bounds

On the rotational set,

\[
\int_{E_{rot}\cap[0,S]}
\|V_s^{rot}\|_2ds
\ge
\frac{\sigma_0}{\sqrt2}
|E_{rot}\cap[0,S]|.
\]

On the shape set,

\[
\int_{E_{shape}\cap[0,S]}
\|V_s^{shape}\|_2ds
\ge
\frac{\sigma_0}{\sqrt2}
|E_{shape}\cap[0,S]|.
\]

Therefore the positive-density surviving channel accumulates action at a rate bounded below by a fixed positive constant.

This is path length in the corresponding quotient/tangent direction; it is not yet an energy dissipation identity.

---

## 9. What projective closure can and cannot absorb

The existing smooth projective-action/viscous-tax theorem states that, on its bounded pure anti-ribbon corridor, enough transverse projective action forces a positive frequency integral and enters the viscous `H1` ledger.

That mechanism is relevant to `E_rot` only after one additionally proves that the rotational tangent motion acts nontrivially on the strain eigenframe/projective descriptor used by that theorem.

A rigid spatial rotation of an exactly axisymmetric state can have a degenerate or invisible projective coordinate.

Likewise, `E_shape` cannot be declared an `H` or `T` event merely because it is orthogonal to rotations.

Thus the present audit deliberately does **not** make the invalid implications

\[
V_s^{rot}\ne0\Rightarrow\text{projective tax}
\]

or

\[
V_s^{shape}\ne0\Rightarrow H\lor T.
\]

Additional descriptor sensitivity is required.

---

## 10. DSD verdict

### PROVED

- exact local Hilbert decomposition of perpetual core speed into rotational-orbit and orthogonal-shape components;
- fixed positive speed floor forces one of the two components to be large at every time;
- at least one component occupies a positive fraction of arbitrarily long time intervals;
- the surviving component accumulates positive action linearly in similarity time.

### CORRECTED

The RSS rotational phase-payment formula is not a general recurrent-orbit identity. It is the exact zero-shape-speed special case.

### OPEN

- rotational tangent speed -> nondegenerate projective/eigenframe action;
- shape speed -> derivative/material/variance cost;
- degenerating rotation Gram matrix;
- periodic/relative-periodic compact motion;
- global regularity.

---

## 11. Next audit target

The next step should treat the shape branch with a **finite observable family** rather than attempting to infer `H/T` directly from an infinite-dimensional orthogonal complement.

Choose already existing normalized core observables (for example enstrophy, strain spectrum/projective coordinates, variance, center/material-overlap descriptors, and one derivative-frequency descriptor) and form their differential map

\[
D\mathcal O_V[V_s^{shape}].
\]

Then audit whether the observable family has a coercive lower bound on the compact normalized core class:

\[
\boxed{
\|V_s^{shape}\|_{L^2(B_R)}
\le
C
\left|D\mathcal O_V[V_s^{shape}]\right|.
}
\]

If such finite observability holds, positive shape speed must move one of the already costed DSD channels.

If it fails, compactness yields a nonzero **descriptor-invisible shape mode**, which becomes one precise new kernel branch instead of the vague statement `aperiodic motion`.
