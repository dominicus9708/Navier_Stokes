# DSD M5-194 — Lin–Wang Epsilon Loss and W1 Endpoint Cancellation Audit

Date: 2026-08-28

Status: **P1_B CRITICAL-ENDPOINT AUDIT / THE STRICT `epsilon>0` IN THE LIN--WANG GENERALIZED-STOKES CARLEMAN PROOF IS CONSUMED IN A LOG-RADIUS CURVATURE INEQUALITY `C r^epsilon beta <= 1+psi''(-log r)` / AT `epsilon=0` THE SAME WEIGHT ARCHITECTURE WOULD REQUIRE ORDER-`beta` POSITIVE CURVATURE ON AN INFINITE LOG-RADIUS INTERVAL WHILE KEEPING `psi'~beta`, WHICH IS IMPOSSIBLE / W1 DIVERGENCE-FREE TRANSPORT REMOVES THE UNWEIGHTED FIRST-ORDER FORM BUT A RADIAL CARLEMAN WEIGHT RECREATES AN INDEFINITE CRITICAL `beta r^-2 Phi_r` POTENTIAL; ZERO SPHERICAL FLUX DOES NOT CANCEL IT AGAINST `|W|^2`, AND THE COMMON-TAIL STRAIN REMAINS SIGNED BY M5-191 / THEREFORE THE LIN--WANG SUBCRITICAL PROOF DOES NOT EXTEND TO W1 BY A SIMPLE CANCELLATION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Where `epsilon>0` is actually used

Lin--Wang introduce the logarithmic radial variable

\[
y=-\log r
\]

and a Carleman weight

\[
\varphi(r)=e^{\psi(y)}.
\]

A central design property of their weight is, schematically,

\[
\boxed{
C r^\varepsilon\beta
\le
1+\psi''(-\log r)
}
\]

for sufficiently small `r`, where `beta` is the large Carleman parameter.

The lower-order generalized-Stokes coefficients enter after multiplication by powers of `r` with exactly this extra factor `r^epsilon`; the inequality above supplies the curvature needed to absorb them.

Thus the strict gain `epsilon>0` is not cosmetic.

---

## 2. Why the same weight architecture fails at `epsilon=0`

At the endpoint,

\[
r^\varepsilon=1.
\]

The required inequality becomes

\[
1+\psi''(y)\ge c\beta
\]

through an unbounded interval

\[
y\to+\infty.
\]

For large `beta`, this implies

\[
\psi''(y)\ge c_1\beta>0.
\]

Integrating from `Y` to `y` gives

\[
\psi'(y)
\ge
\psi'(Y)+c_1\beta(y-Y).
\]

Therefore

\[
\psi'(y)\to+\infty.
\]

But the Lin--Wang resonance/weight construction requires the slope to remain at the Carleman scale

\[
\psi'(y)\simeq\beta,
\]

not to grow linearly in `y` without bound.

Hence

\[
\boxed{
\text{their subcritical log-radius weight cannot be extended to }\varepsilon=0
\text{ by simply setting }\varepsilon=0.
}
\]

This is a structural endpoint failure, not merely a constant blowing up.

---

## 3. Insert the W1 common canonical tail

Write the common tail in log-cylinder form

\[
B_T(x)
=
\frac1r\Phi(y,\theta),
\qquad
y=-\log r.
\]

Decompose

\[
\Phi=\Phi_r\theta+\Phi_\tau.
\]

The divergence-free constraint gives the known cylinder relation, and in particular the spherical flux satisfies

\[
\int_{S^2}\Phi_r(y,\theta)\,d\theta=0.
\]

The question is whether this structure removes the endpoint first-order loss that Lin--Wang treat by absolute values.

---

## 4. Unweighted transport is exactly skew

For divergence-free `B_T` and divergence-free finite-energy `W`,

\[
\int W\cdot(B_T\cdot\nabla W)dx=0.
\]

Thus the principal first-order common-tail transport has no real `L2` energy contribution before weighting.

This is genuine W1/NSE structure and is stronger than a generic coefficient estimate.

---

## 5. A radial Carleman weight recreates a critical potential

Let

\[
w(r)=\varphi(r)^2=e^{2\psi(y)}.
\]

Then

\[
\begin{aligned}
\int wW\cdot(B_T\cdot\nabla W)dx
&=
\frac12\int wB_T\cdot\nabla|W|^2dx\\
&=
-\frac12\int |W|^2\nabla\cdot(wB_T)dx\\
&=
-\int w(B_T\cdot\nabla\log\varphi)|W|^2dx.
\end{aligned}
\]

Since

\[
\nabla y=-\frac\theta r,
\]

we have

\[
\nabla\log\varphi
=-\frac{\psi'(y)}r\theta.
\]

Therefore

\[
\boxed{
B_T\cdot\nabla\log\varphi
=
-\psi'(y)\frac{\Phi_r(y,\theta)}{r^2}.
}
\]

Hence the weighted transport contribution becomes

\[
\boxed{
\int w\psi'(y)\frac{\Phi_r}{r^2}|W|^2dx.
}
\]

With

\[
\psi'\simeq\beta,
\]

this is exactly an order

\[
\boxed{\beta r^{-2}}
\]

critical signed potential.

Thus radial weighting destroys the exact unweighted skew cancellation at precisely the endpoint order one hoped to remove.

---

## 6. Zero spherical flux is insufficient

Although

\[
\int_{S^2}\Phi_r\,d\theta=0,
\]

the weighted transport form contains

\[
\int_{S^2}\Phi_r(y,\theta)|W(y,\theta)|^2d\theta.
\]

There is no reason for this to vanish.

Indeed `|W|^2` can correlate with the positive or negative sectors of `Phi_r`.

Therefore

\[
\boxed{
\text{zero spherical flux of the tail}
\not\Rightarrow
\text{zero weighted transport commutator}.
}
\]

This blocks the simplest W1 endpoint replacement for the missing `r^epsilon` factor.

---

## 7. Stretching remains a second signed critical channel

The common-tail stretching form is

\[
\int wW^TS_{B_T}Wdx.
\]

M5-191 gives an explicit divergence-free zero-flux `1/r` rotational tail whose strain has eigenvalues

\[
\pm c(\theta)r^{-2},\quad0.
\]

Thus neither divergence freeness nor zero flux provides a sign for the stretching channel.

Consequently at the endpoint a radial Carleman must simultaneously control two signed critical pieces:

\[
\boxed{
\beta\Phi_r r^{-2}|W|^2
}
\]

from the weighted transport commutator, and

\[
\boxed{
W^TS_{B_T}W\sim r^{-2}|W|^2
}
\]

from stretching.

---

## 8. Strong-L3 quotient does not change this conclusion

M5-190 proves that the same-tail strong-`L3` quotient is infinitesimally form-bounded:

\[
|\mathfrak q_Q[W]|
\le
\varepsilon\|\nabla W\|_2^2
+C_\varepsilon\|W\|_2^2.
\]

Thus the subcritical/strong quotient is not responsible for the endpoint failure.

The obstruction is concentrated entirely in the common canonical weak-`L3` tail.

---

## 9. What a true endpoint extension must change

A successful W1 endpoint argument cannot simply reuse the radial Lin--Wang weight and estimate the common tail absolutely.

At least one of the following must happen:

1. **adapt the weight to the common-tail streamlines**, reducing
   \[
   B_T\cdot\nabla\Phi_{Carleman};
   \]
2. build a matrix/vector symmetrizer combining weighted transport and stretching;
3. put the full common-tail Oseen operator on the principal side and derive its own log-convexity;
4. discover a genuinely canonical-tail dynamical identity not shared by generic divergence-free `1/r` fields.

These are structural changes, not coefficient bookkeeping.

---

## 10. Conditional easy subbranch

If the common tail were purely tangential,

\[
\Phi_r\equiv0,
\]

then the radial-weight transport commutator vanishes exactly.

If, in addition, the remaining strain has sufficiently small Hardy form constant, the endpoint becomes perturbatively coercive.

This is only a conditional subbranch.

General W1 tails are not known to satisfy either condition.

---

## 11. DSD four-chain audit

### Formation — GREEN

The epsilon loss is located in an explicit inequality from the external proof; W1 tail terms are then inserted directly.

### Axis — GREEN

Log-radius curvature, radial tail velocity, tangential tail velocity, and stretching are separated.

### Static aggregation — GREEN

Zero spherical mean is not promoted to cancellation against the nonconstant density `|W|^2`.

### Dynamics — GREEN NEGATIVE RESULT / ENDPOINT STILL OPEN

The straightforward subcritical-to-critical extension is ruled out.  A tail-adapted principal structure remains open.

### Cross-audit — GREEN

This is consistent with M5-190/M5-191 and does not revive the corrected arbitrary-amplitude absorption claim of M5-185.

---

## 12. Updated frontier

The exact endpoint problem is now

\[
\boxed{
\text{construct an adapted Carleman/symmetrizer for the full common-tail Oseen operator,}
}
\]

not

\[
\text{send }\varepsilon\downarrow0\text{ in a generic generalized-Stokes theorem}.
\]

The next calculation should test the most direct adapted-weight condition

\[
\boxed{B_T\cdot\nabla\Psi=0}
\]

(or a bounded version of it) while preserving the radial Carleman growth needed for unique continuation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
