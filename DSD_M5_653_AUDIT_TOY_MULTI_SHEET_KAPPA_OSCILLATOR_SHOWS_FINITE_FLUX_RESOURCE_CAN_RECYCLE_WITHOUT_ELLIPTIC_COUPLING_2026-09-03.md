# DSD M5-653 — Audit toy: a multi-sheet kappa oscillator recycles finite flux forever unless the elliptic PDE coupling is used

Date: 2026-09-03

Status: **DSD ANTI-SHORTCUT COUNTERMODEL / A ONE-DIMENSIONAL VORTEX-QUOTIENT OSCILLATOR `kappa=sin(q+theta)`, `h=cos(q+theta)` HAS TWO LOCAL `h(kappa)` SHEETS, ZERO-MEAN MATERIAL KAPPA, BOUNDED RECURRENT MATERIAL FLUX, FINITE TOTAL LEAF-FLUX RESOURCE, AND CAN ALSO SUPPORT NEGATIVE KAPPA-AMPLITUDE COVARIANCE BY PHASE BIAS / THEREFORE FINITE TRANSVERSE RESOURCE PLUS FLUX RECURRENCE PLUS MULTI-SHEET RELABELING KINEMATICS DO NOT ALONE CONTRADICT RECURRENCE / THE MODEL IS NOT A NAVIER-STOKES SOLUTION AND DELIBERATELY OMITS THE CE-H ELLIPTIC EQUATION `Delta W=kappa W`; HENCE ANY FURTHER CLOSURE MUST USE THAT SPATIAL PDE COUPLING OR AN EQUIVALENT NS IDENTITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-647 gives a finite base transverse-flux resource.

M5-648--649 show that one common scalar relabeling law cannot recycle a fixed-flux population forever because lower relative flux is monotone.

M5-650 correctly retains multi-sheet relabeling, where the same `kappa` value can have different local values of

\[
h=D_B\kappa.
\]

Before treating finite flux as a contradiction on that branch, construct the simplest abstract quotient dynamics that tests whether sheet switching can recharge the same finite leaf resource indefinitely.

---

## 2. Quotient phase variable

Let the abstract vortex-line quotient be a circle

\[
q\in\mathbb S^1.
\]

Treat `q` as a material label:

\[
D_Bq=0.
\]

Define

\[
\boxed{
\kappa(q,\theta)
=
\sin(q+\theta).
}
\]

Then

\[
\boxed{
h(q,\theta):=D_B\kappa
=
\cos(q+\theta).
}
\]

---

## 3. Explicit multi-sheet relation

At a fixed `theta`,

\[
\kappa^2+h^2=1.
\]

Thus for every `|kappa|<1`,

\[
\boxed{
h=\pm\sqrt{1-\kappa^2}.}
\]

There are two branches of `h` over the same `kappa` value.

Locally on either semicircle, `h` is a function of `kappa`, but there is no single global scalar law `h=f(kappa,theta)` on the full quotient.

Branch switching occurs at the turning points `kappa=+/-1`.

This is the elementary prototype of the M5-650 multi-sheet loophole.

---

## 4. Material flux is bounded and recurrent

Let a leaf flux obey the CE-H kinematic law

\[
\frac d{d\theta}\log\Phi_q
=
\kappa(q,\theta).
\]

Then

\[
\int_0^\theta\sin(q+s)ds
=
\cos q-\cos(q+\theta).
\]

Hence

\[
\boxed{
\Phi_q(\theta)
=
\Phi_q(0)
\exp[\cos q-\cos(q+\theta)].
}
\]

Therefore

\[
e^{-2}\Phi_q(0)
\le
\Phi_q(\theta)
\le
e^2\Phi_q(0).
\]

Every leaf has a bounded nondegenerate recurrent flux despite alternating negative and positive `kappa` phases.

Moreover

\[
\boxed{
\langle\kappa(q,\cdot)\rangle_\theta=0.
}
\]

---

## 5. Finite total flux resource can recycle forever

Take a finite initial transverse measure

\[
\int_{\mathbb S^1}\Phi_q(0)dq<\infty.
\]

For example set

\[
\Phi_q(0)=e^{-\cos q}.
\]

Then

\[
\Phi_q(\theta)=e^{-\cos(q+\theta)}.
\]

Thus

\[
\boxed{
\int_{\mathbb S^1}\Phi_q(\theta)dq
=
\int_{\mathbb S^1}e^{-\cos q}dq
<\infty
}
\]

for every time.

The finite resource does not monotonically decrease; it is simply redistributed in phase.

Negative-phase flux loss is exactly recharged during positive phases.

This directly shows why M5-648's monotone-loss proof cannot be extended to arbitrary multi-sheet dynamics without an additional PDE sign mechanism.

---

## 6. Negative kappa-amplitude covariance is also compatible

Choose an abstract positive amplitude weight

\[
E_q(\theta)
=
1-\varepsilon\sin(q+\theta),
\qquad0<\varepsilon<1.
\]

Then over the quotient circle

\[
\int\kappa E_qdq
=
\int\sin(q+\theta)
[1-\varepsilon\sin(q+\theta)]dq
=-\varepsilon\pi<0.
\]

Thus the same model simultaneously has

\[
\boxed{
\langle\kappa\rangle=0,
\qquad
\langle\kappa E\rangle<0.
}
\]

This reproduces the qualitative M5-630 covariance mechanism.

---

## 7. What the toy intentionally omits

The construction is **not** asserted to solve Navier-Stokes.

It does not provide vector fields `W,U` satisfying

\[
\Delta W=\kappa W,
\qquad
\Sigma W=\sigma W,
\qquad
\nabla\cdot W=0,
\]

nor the Biot-Savart coupling between `W` and `Sigma`.

It also does not enforce the M5-651 strict superlevel identities.

Its role is only to show that the following ingredients are insufficient by themselves:

1. finite total leaf-flux resource;
2. zero-mean material `kappa`;
3. bounded recurrent flux;
4. multi-sheet local relabeling;
5. negative `kappa`-amplitude covariance.

---

## 8. DSD audit verdict

Any future contradiction that can also be derived from the present toy model is not using enough Navier-Stokes structure.

The next closure must employ at least one genuinely PDE-specific CE-H identity, for example

\[
\boxed{
\Delta W=\kappa W,
}
\]

through

- the M5-651 superlevel deficit,
- the generalized-kappa-force stress tensor,
- the non-Beltrami divergence law,
- or the strain/pressure compatibility equation.

This is an anti-shortcut firewall.

---

## 9. Updated hard target

The multi-sheet survivor is now best phrased as:

\[
\boxed{
\text{Can the elliptic eigenfield system }\Delta W=\kappa W
\text{ realize a bounded recurrent branched kappa oscillator on a finite-enstrophy CE-H ancient flow?}
}
\]

That is a substantially narrower PDE question than arbitrary material flux recurrence.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]