# DSD M5-493 — Recurrent persistent dual pair forces positive mean similarity palinstrophy

Date: 2026-09-01

Status: **SPACE-TIME THICKENING / M5-492 GIVES A FIXED LOCAL PALINSTROPHY LOWER BOUND AT EVERY RETAINED NONCOLLINEAR DUAL-PAIR EVENT / COMPACT PARABOLIC REGULARITY MAKES THE LOCAL PALINSTROPHY FUNCTIONAL UNIFORMLY CONTINUOUS IN SIMILARITY TIME, SO EACH EVENT OCCUPIES A FIXED POSITIVE TIME WINDOW WITH HALF THE CHARGE / THE DILATION-HULL ROOF TIMES ARE BOUNDED ABOVE AND BELOW, SO A POSITIVE-FREQUENCY EVENT SET CONTAINS A POSITIVE-FREQUENCY SUBSET WITH DISJOINT THICKENED WINDOWS / CONSEQUENTLY EVERY RECURRENT PERSISTENT DUAL-PAIR HULL HAS A STRICTLY POSITIVE INVARIANT MEAN PALINSTROPHY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-492

At every retained noncollinear event of the persistent pair `(alpha_*,beta_*)`, M5-492 proves

\[
\boxed{
P_R(\theta_j)
:=
\int_{B_R}|\nabla W(y,\theta_j)|^2dy
\ge p_*>0.
}
\]

The lower bound is paid either by

\[
\int\rho^2|\nabla\xi|^2
\]

on an active bridge or by

\[
\int|\nabla\rho|^2
\]

on a low-vorticity separator.

M5-490 supplies a positive log-scale frequency of such noncollinear dual-pair events.

---

## 2. Why a pointwise-time charge is not enough

A lower bound at isolated times does not imply

\[
\langle P\rangle>0.
\]

The event could, in principle, occupy a zero-measure set of similarity times.

Therefore M5-492 must be combined with the compact similarity regularity of the M5-483--486 hull.

---

## 3. Uniform time regularity of local palinstrophy

On the compact Type-I hull, fix a slightly larger ball

\[
B_R\Subset B_{R_1}.
\]

Interior parabolic regularity on every similarity-time slab represented by the compact suspension hull gives fixed bounds

\[
\sup_{\mathfrak H}
\|\nabla W\|_{L^\infty(B_{R_1})}
\le C_1,
\]

and

\[
\sup_{\mathfrak H}
\|\partial_\theta\nabla W\|_{L^\infty(B_{R_1})}
\le C_t.
\]

Equivalently one may use a uniform local `L2` bound on `partial_theta grad W`; the stronger displayed form is available after shrinking to a compact interior cylinder.

Differentiate

\[
P_R(\theta)=\int_{B_R}|\nabla W|^2dy.
\]

Then

\[
\left|P_R'(\theta)\right|
\le
2\int_{B_R}
|\nabla W|\,|\partial_\theta\nabla W|dy
\le
2|B_R|C_1C_t
=:L_P.
\]

Thus

\[
\boxed{
|P_R(\theta)-P_R(\theta')|
\le L_P|\theta-\theta'|.
}
\]

---

## 4. Every dual event has fixed temporal thickness

At an event time `theta_j`,

\[
P_R(\theta_j)\ge p_*.
\]

Choose

\[
\boxed{
\delta_\theta
:=
\min\left(\frac{p_*}{2L_P},\delta_{int}\right)>0,
}
\]

where `delta_int` is a fixed interior-time margin allowed by the compact stage/suspension charts.

Then for

\[
|\theta-\theta_j|\le\delta_\theta
\]

one has

\[
\boxed{
P_R(\theta)\ge\frac{p_*}{2}.
}
\]

Hence each event pays at least

\[
\boxed{
\int_{\theta_j-\delta_\theta}^{\theta_j+\delta_\theta}
P_R(\theta)d\theta
\ge
p_*\delta_\theta.
}
\]

---

## 5. Event spacing in similarity time

The M5-485 suspension roof is

\[
\Theta_j=2\log\lambda_j
\]

with

\[
\boxed{
0<\Theta_-
\le\Theta_j
\le\Theta_+<\infty.
}
\]

Therefore one generation occupies a uniformly nonzero amount of similarity time.

Suppose the persistent pair is noncollinear on a generation set `J_dual` of lower density

\[
\underline d(J_{dual})=d_{dual}>0.
\]

The corresponding event times have upper local multiplicity bounded solely in terms of `Theta_-` and `delta_theta`.

By a greedy selection, extract a subfamily `J_dis subset J_dual` whose thickened intervals

\[
I_j=[\theta_j-\delta_\theta,\theta_j+\delta_\theta]
\]

are disjoint and whose generation density still obeys

\[
\boxed{
\underline d(J_{dis})
\ge c_{sep}d_{dual}>0.
}
\]

---

## 6. Positive mean palinstrophy

Over a long similarity-time interval `[0,T]`, sum the disjoint event windows.

Since each selected event contributes at least `p_* delta_theta`, while the number of generations per unit similarity time is bounded below and above by the roof constants,

\[
\liminf_{T\to\infty}
\frac1T
\int_0^T P_R(\theta)d\theta
\ge
c(\Theta_+,\Theta_-,d_{dual})
\,p_*\delta_\theta.
\]

Define

\[
\boxed{
p_{mean}>0
}
\]

to be this fixed lower bound.

Since global palinstrophy dominates the local one,

\[
P(\theta)
:=
\int_{\mathbb R^3}|\nabla W|^2dy
\ge P_R(\theta),
\]

we obtain

\[
\boxed{
\langle P\rangle
\ge p_{mean}>0.
}
\]

The same statement holds directly for the invariant suspension measure of M5-485:

\[
\boxed{
\int_{\widehat{\mathfrak H}}P\,d\widehat\mu
\ge p_{mean}>0.
}
\]

---

## 7. Insert into the M5-486 enstrophy balance

M5-486 gives on every invariant nonzero component

\[
\boxed{
\frac14\langle E\rangle
+
\langle P\rangle
=
\langle Q\rangle.
}
\]

Therefore the recurrent dual pair sharpens this to

\[
\boxed{
\langle Q\rangle
\ge
\frac14\langle E\rangle
+p_{mean}.
}
\]

Thus the axial stretching channel must pay not merely the self-similar damping of nonzero enstrophy but also a fixed mean geometric price caused by recurrent noncollinear dual-flux structure.

---

## 8. Bridge/separator decomposition of the mean cost

Let `b(theta)` mark active-bridge events and `s(theta)` mark low-vorticity-separator events.

On the recurrent dual-event set,

\[
b+s\ge1.
\]

After temporal thickening one obtains a mean split

\[
\boxed{
p_{mean}
\le
\left\langle
\int\rho^2|\nabla\xi|^2
\right\rangle
+
\left\langle
\int|\nabla\rho|^2
\right\rangle.
}
\]

This is consistent with the exact decomposition

\[
P
=
\int\rho^2|\nabla\xi|^2
+
\int|\nabla\rho|^2.
\]

The compact survivor may alternate between the two payment mechanisms; M5-493 does not assume that one of them dominates globally.

---

## 9. Relation to M5-487

M5-487 proved that weighted directional tension

\[
\mathcal D_\xi
=
\rho^{-2}(I-\xi\otimes\xi)\nabla\cdot(\rho^2\nabla\xi)
\]

is not coercive over the direction Dirichlet energy.

M5-492--493 therefore do **not** infer direction energy from directional tension.

Instead they derive direction energy from a geometric boundary-value condition: two active carrier regions must realize different direction values inside one positive-capacity active corridor.

This avoids the harmonic-map counterexample of M5-487.

---

## 10. Firewall

The positive mean `P` is not itself a contradiction.

Similarity enstrophy dynamics explicitly allow positive mean palinstrophy provided axial stretching production `Q` pays the same amount.

Hence one must not conclude

\[
\langle P\rangle>0
\Rightarrow
\text{no recurrent hull}.
\]

The correct next question is quantitative:

\[
\boxed{
\text{Can a bounded critical-enstrophy hull produce enough }Q
\text{ to pay }p_{mean}
\text{ indefinitely?}
}
\]

---

## 11. Highest-value next target

Use Calderon--Zygmund plus Sobolev interpolation to compare axial production and palinstrophy:

\[
Q
=
\int W\cdot\Sigma W.
\]

A natural bound is expected in the form

\[
|Q|
\le
C E^{3/4}P^{3/4}.
\]

Averaging this over the invariant hull and combining with

\[
\langle P\rangle\ge p_{mean}
\]

may produce a quantitative lower threshold on the compact normalized enstrophy required by the recurrent dual-pair survivor.

If the required threshold exceeds the bounded corridor's permitted normalized enstrophy, that subbranch closes; otherwise the hard core is narrowed to a quantitatively large critical-enstrophy recurrent hull.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
