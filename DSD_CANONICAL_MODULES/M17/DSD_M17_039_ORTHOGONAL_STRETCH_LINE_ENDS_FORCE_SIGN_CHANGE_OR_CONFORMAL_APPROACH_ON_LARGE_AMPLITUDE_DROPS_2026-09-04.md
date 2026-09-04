# DSD M17-039 — Orthogonal stretch line ends force sign change or conformal approach on large amplitude drops

Date: 2026-09-04
Canonical ID: **M17-039**

Status: **INTERNAL ORTHOGONAL-STRETCH LINE-END AUDIT / M17-038 GIVES THE EXACT SPATIAL LAW `D_xi d=-E D_xi log rho`, WITH `E=A^2+B^2` AND `d=(B^2-A^2)/2`, SO `E>=2|d|`. ON ANY VORTEX-LINE SEGMENT WHERE `rho` DECREASES MONOTONICALLY, A POSITIVE DEFECT `d>0` OBEYS `D_xi log d >= -2 D_xi log rho`, HENCE IT GROWS AT LEAST LIKE `rho^{-2}`; A UNIFORMLY BOUNDED POSITIVE DEFECT CANNOT SURVIVE AN ARBITRARILY LARGE AMPLITUDE DROP. FOR A NEGATIVE DEFECT `d=-y<0`, THE SAME LAW GIVES `y(s_2)<=y(s_1)(rho(s_2)/rho(s_1))^2` ON A DECREASING SEGMENT, SO THE ANISOTROPY IS FORCED TOWARD THE CONFORMAL INTERFACE AS THE AMPLITUDE DECAYS. THE REVERSED STATEMENTS HOLD ON MONOTONICALLY INCREASING SEGMENTS. CONSEQUENTLY A COMPLETE FINITE-ENERGY LINE WITH DECAYING ENDS CANNOT CARRY A SINGLE UNIFORMLY POSITIVE STRETCH SIGN THROUGH ARBITRARILY LARGE LOG-AMPLITUDE VARIATION; IT MUST DEVELOP SIGN/CONFORMAL CROSSINGS OR AN OSCILLATORY NONMONOTONE TAIL. THE NEGATIVE-SIGN CLASS CAN SURVIVE ONLY BY BECOMING ASYMPTOTICALLY CONFORMAL AT DECAYING ENDS. THIS NARROWS BUT DOES NOT CLOSE THE ORTHOGONAL STRETCH BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact line law

On the orthogonal stretch branch M17-038 gives

\[
\boxed{
D_\xi d
=-E D_\xi\log\rho,
}
\]

where

\[
E=A^2+B^2>0,
\]

\[
d=\frac{B^2-A^2}{2}.
\]

Since

\[
E^2-4d^2=4A^2B^2>0
\]

on full rank two,

\[
\boxed{E>2|d|.}
\]

The strict inequality becomes equality only at rank loss.

---

## 2. Positive stretch defect on a decreasing-amplitude segment

Let `s` be arclength along a vortex-direction integral curve and suppose on an interval `[s_1,s_2]`

\[
D_\xi\rho<0
\]

and

\[
d>0.
\]

Then

\[
D_\xi d
=-E D_\xi\log\rho
>-2d D_\xi\log\rho.
\]

Divide by `d`:

\[
D_\xi\log d
>-2D_\xi\log\rho.
\]

Integrating gives

\[
\boxed{
\frac{d(s_2)}{d(s_1)}
>
\left(
\frac{\rho(s_1)}{\rho(s_2)}
\right)^2.
}
\]

Thus a drop

\[
\rho(s_2)=\rho(s_1)/R
\]

forces

\[
\boxed{
d(s_2)>R^2d(s_1).}
\]

A positive stretch defect is amplified rather than relaxed on a decreasing-amplitude tail.

---

## 3. Bounded hard-hull consequence for d>0

Suppose the retained compact smooth hull supplies

\[
|d|\le D_*
\]

on the relevant core/tail class.

Then any positive-sign interval with initial floor

\[
d(s_1)\ge d_*>0
\]

can sustain at most

\[
\frac{\rho(s_1)}{\rho(s_2)}
<
\sqrt{\frac{D_*}{d_*}}.
\]

Therefore

\[
\boxed{
\text{large amplitude drop}
+
 d\ge d_*>0
\Longrightarrow
\text{branch exit before the drop completes}.
}
\]

The exit may be

\[
\boxed{
d=0
\ \lor\ 
 d<0
\ \lor\ 
\text{rank/interface loss}.
}
\]

---

## 4. Negative stretch defect on a decreasing-amplitude segment

Now suppose

\[
d=-y<0,
\qquad
y>0.
\]

Then

\[
D_\xi y
=E D_\xi\log\rho.
\]

On a decreasing segment,

\[
D_\xi\log\rho<0.
\]

Since

\[
E>2y,
\]

multiplication by the negative derivative reverses the inequality:

\[
D_\xi y
<2yD_\xi\log\rho.
\]

Therefore

\[
D_\xi\log y
<2D_\xi\log\rho.
\]

Integrating,

\[
\boxed{
\frac{y(s_2)}{y(s_1)}
<
\left(
\frac{\rho(s_2)}{\rho(s_1)}
\right)^2.
}
\]

Hence as amplitude decreases, the negative defect magnitude is driven rapidly toward zero.

---

## 5. Asymptotically decaying tail

Suppose along a monotone tail

\[
\rho(s)\to0
\qquad(s\to+\infty)
\]

while the line remains in the regular orthogonal branch.

If eventually

\[
d<0,
\]

then Section 4 gives

\[
\boxed{|d(s)|\to0.}
\]

Indeed for any fixed `s_0` in the tail,

\[
|d(s)|
<|d(s_0)|
\left(
\frac{\rho(s)}{\rho(s_0)}
\right)^2.
\]

Thus the decaying end becomes asymptotically conformal in the stretch descriptor.

---

## 6. Increasing-amplitude segments

If instead

\[
D_\xi\rho>0,
\]

the inequality directions reverse.

### Positive d

\[
D_\xi\log d
<-2D_\xi\log\rho.
\]

Thus positive `d` is strongly suppressed while amplitude rises.

### Negative d=-y

\[
D_\xi\log y
>2D_\xi\log\rho.
\]

Thus negative-defect magnitude grows strongly while amplitude rises.

This is the mirror image of the decreasing-tail behavior.

---

## 7. Complete line with two decaying ends

Assume a complete vortex-direction line has

\[
\rho(s)\to0
\qquad(s\to\pm\infty)
\]

and contains arbitrarily large monotone log-amplitude rises from the left end and drops toward the right end.

Then a single uniformly positive stretch sign cannot remain bounded away from zero through both tails:

- on the left rise, a bounded positive defect is suppressed toward zero when traced from the tail into the core;
- on the right drop, a positive defect is amplified without bound unless it crosses zero/exits.

Thus a global positive-sign orthogonal branch must undergo at least one of

\[
\boxed{
\text{conformal/sign crossing}
\ \lor\ 
\text{rank/interface exit}
\ \lor\ 
\text{persistent amplitude oscillation breaking the monotone-tail hypothesis}.
}
\]

---

## 8. Negative-sign complete-line profile

A globally negative defect behaves differently.

On both decay ends, the preceding inequalities allow

\[
\boxed{d(s)\to0^-}
\]

while remaining nonzero at every finite point.

Therefore a nonzero orthogonal stretch profile with

\[
d<0
\]

can in principle be asymptotically conformal without ever containing an open conformal component.

M17-036 does **not** exclude this possibility, because its Riccati contradiction assumes a persistent conformal branch, not merely an asymptotic approach as `|s|->infinity`.

This distinction is essential.

---

## 9. Oscillatory-tail firewall

Finite energy or pointwise decay alone does not imply eventual monotonicity of `rho` along each vortex line.

Therefore OSLEG cannot replace the exact PDE by an unproved monotone-tail assumption.

If a survivor avoids the conclusions above through infinitely many linewise amplitude reversals, it enters a distinct branch:

\[
\boxed{R_{osc-tail}^{stretch}.}
\]

Such a tail carries infinitely many alternating linewise extrema satisfying

\[
D_\xi\rho=0
\iff
D_\xi d=0.
\]

This oscillatory branch requires a separate compactness/finite-jet audit.

---

## 10. DSD interpretation

The line law does not merely correlate two fields. It makes the *sign* of the stretch descriptor select how amplitude decay acts on anisotropy:

- `d>0`: decay amplifies anisotropy;
- `d<0`: decay suppresses anisotropy toward conformality.

Thus the two signs are dynamically inequivalent even though `delta_conf` itself is unsigned.

---

## 11. DSD audit

### Audit A — assuming all decaying tails are monotone
Rejected. The oscillatory-tail branch is retained explicitly.

### Audit B — using M17-036 to exclude asymptotic d->0
Rejected. M17-036 closes a complete open conformal component, not an anisotropic solution approaching conformality only at infinity.

### Audit C — claiming positive d must blow up on every tail
Restricted correctly: the quantitative growth applies on monotone decreasing segments while the positive sign persists.

### Audit D — replacing bounded hard-hull derivatives by a global tail bound without scope
Any uniform `D_*` conclusion is used only where the retained compact/tail control supplies it.

### Audit E — proof status
OSLEG narrows but does not close the orthogonal stretch branch.

---

## 12. Updated orthogonal-stretch frontier

\[
\boxed{
R_{stretch}^{orthogonal}
\Longrightarrow
R_{d<0}^{asym-conf}
\ \lor\ 
R_{osc-tail}^{stretch}
\ \lor\ 
I_{d=0}^{conformal/sign-cross}
\ \lor\ 
T_{rank/interface}.
}
\]

The uniformly positive-sign, large-drop complete-tail subbranch is removed.

---

## 13. Next target

The cleanest new branch is the oscillatory tail, because every linewise amplitude extremum is simultaneously a stretch-defect extremum:

\[
D_\xi\rho=0
\iff
D_\xi d=0.
\]

The next calculation should combine this synchronized critical-point structure with the scalar amplitude equation

\[
\Delta\rho=(\kappa+E)\rho
\]

and compact analytic finite-jet control to determine whether infinitely many persistent linewise extrema force a recurrent finite critical-jet type or a degeneration event.

The asymptotically conformal negative-sign branch should then be tested through its limiting flat-connection/Riccati geometry.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
