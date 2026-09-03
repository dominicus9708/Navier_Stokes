# DSD M16-018 — Hysteretic recharge requires positive strain or positive-kappa with negative-kappa compensation

Date: 2026-09-03
Canonical ID: **M16-018**

Status: **INTERNAL EXACT HYSTERESIS COST / EVERY UPWARD RECHARGE ACROSS A FIXED AMPLITUDE GAP HAS A NONZERO MATERIAL LOG-AMPLITUDE COST. USING THE CE-H LAW `D_B log rho = sigma + kappa - 1`, THIS COST FORCES POSITIVE STRAIN OR POSITIVE KAPPA. THE LAPLACIAN EIGENLINE IDENTITY `int kappa rho^2 = -P` THEN FORCES ANY POSITIVE-KAPPA SPATIAL CHARGE TO BE COMPENSATED BY AT LEAST AS MUCH NEGATIVE-KAPPA ENSTROPHY WEIGHT. THUS RECHARGE IS ROUTED BACK INTO THE M15 POSITIVE-STRAIN SOURCE GENEALOGY OR THE M13--M16 NEGATIVE-KAPPA SHEATH GENEALOGY. THIS IS A ROUTING RESULT, NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two-threshold hysteresis

Fix two amplitudes

\[
0<a_-<a_+,
\]

and define the nonzero logarithmic gap

\[
\boxed{
\Delta_a:=\log\frac{a_+}{a_-}>0.
}
\]

A completed **upward recharge segment** for one material label is a time interval `[t_-,t_+]` on which

\[
\rho(t_-)=a_-,
\qquad
\rho(t_+)=a_+.
\]

The trajectory may oscillate inside the band; monotonicity is not required.

---

## 2. Exact recharge integral

M16-017 gives

\[
D_B\log\rho
=\sigma+\kappa-1.
\]

Integrating along the material trajectory gives

\[
\log\rho(t_+)-\log\rho(t_-)
=
\int_{t_-}^{t_+}(\sigma+\kappa-1)d\theta.
\]

Therefore

\[
\boxed{
\Delta_a
=
\int_{t_-}^{t_+}(\sigma+\kappa-1)d\theta.
}
\]

Equivalently, if

\[
T_+:=t_+-t_-,
\]

then

\[
\boxed{
\int_{t_-}^{t_+}(\sigma+\kappa)d\theta
=T_++\Delta_a.
}
\]

Hence

\[
\boxed{
\int_{t_-}^{t_+}(\sigma_++\kappa_+)d\theta
\ge T_++\Delta_a
\ge\Delta_a.
}
\]

Here `f_+=max(f,0)`.

Thus every completed recharge has a strictly positive strain/kappa excitation cost.

---

## 3. Uniform pointwise excitation using the finite-residence bound

For a coherent positive-volume recharge packet that remains in the high-amplitude band `rho>=a_-`, M16-017 gives a finite residence cap.

If the packet begins with material volume `V_*>0`, then

\[
T_+
\le
T_*:=
\frac23
\log\left(\frac{Z_*}{a_-^2V_*}\right).
\]

Therefore

\[
\frac1{T_+}
\int_{t_-}^{t_+}(\sigma+\kappa)d\theta
=1+\frac{\Delta_a}{T_+}
\ge
1+\frac{\Delta_a}{T_*}.
\]

Put

\[
\delta_a:=\frac{\Delta_a}{T_*}>0.
\]

At some time along every such recharge trajectory,

\[
\boxed{
\sigma+\kappa\ge1+\delta_a.
}
\]

Hence at that time

\[
\boxed{
\sigma\ge\frac{1+\delta_a}{2}
\quad\lor\quad
\kappa\ge\frac{1+\delta_a}{2}.
}
\]

Uniform smoothness and the coherent packet thickness then convert this into a fixed-radius local excitation event after the usual spatial/time thickening.

---

## 4. Positive-strain recharge branch

If

\[
\sigma\ge s_R>0
\]

on a high-amplitude packet, then

\[
\rho^2\sigma>0
\]

there.

This is exactly the sign needed for positive local vortex stretching / enstrophy production.

Thus the recharge event is routed into the M15 source genealogy:

\[
\boxed{
R_{up}^{\sigma}
\Longrightarrow
\text{positive-strain coherent source event}.
}
\]

This does not mean every positive-strain packet produces net global growth; the global enstrophy ledger still includes diffusion and similarity damping. The result is only a sign-correct local routing statement.

---

## 5. Exact global kappa identity

On the Laplacian eigenline branch,

\[
\Delta W=\kappa W.
\]

Multiply by `W` and integrate over `R^3`:

\[
\int W\cdot\Delta Wdy
=
\int\kappa|W|^2dy.
\]

Integration by parts gives

\[
\int W\cdot\Delta Wdy
=-\int|\nabla W|^2dy.
\]

Therefore

\[
\boxed{
\int_{\mathbb R^3}\kappa\rho^2dy
=-P,
\qquad
P:=\int|\nabla W|^2dy.
}
\]

This is exact.

Let

\[
K_+
:=
\int\kappa_+\rho^2dy,
\qquad
K_-
:=
\int\kappa_-\rho^2dy,
\]

where `kappa_- = max(-kappa,0)`.

Then

\[
K_+-K_-=-P,
\]

so

\[
\boxed{
K_-=K_++P.
}
\]

In particular,

\[
\boxed{
K_-\ge K_+,
\qquad
K_-\ge P.
}
\]

Any positive-kappa enstrophy weight is therefore accompanied, at the same time, by strictly larger negative-kappa enstrophy weight globally.

---

## 6. Positive-kappa recharge branch

Suppose the recharge excitation is paid by

\[
\kappa\ge k_R>0
\]

on a coherent high-amplitude packet of volume `V_R>0`, with

\[
\rho\ge a_->0.
\]

Then

\[
K_+
\ge
k_Ra_-^2V_R
=:q_R>0.
\]

The exact identity of Section 5 gives

\[
\boxed{
K_-
\ge q_R+P.
}
\]

Thus a positive-kappa recharge packet necessarily forces a simultaneous negative-kappa payer elsewhere.

By the global smooth compactness and tail tightness of the retained branch, a fixed fraction of this negative enstrophy-weighted kappa charge can be localized in a sufficiently large but fixed finite core.

After uniform spatial thickening, the positive-kappa recharge branch therefore comes with a recurrent negative-kappa coherent payer family.

Schematically,

\[
\boxed{
R_{up}^{\kappa+}
\Longrightarrow
\text{negative-kappa compensation / sheath payer}.
}
\]

This reconnects directly to the M13--M16 negative-kappa sheath genealogy.

---

## 7. Recharge routing theorem

Every coherent upward recharge across the fixed hysteretic gap satisfies

\[
\boxed{
R_{up}
\Longrightarrow
R_{up}^{\sigma+}
\lor
R_{up}^{\kappa+}.
}
\]

The two branches obey

\[
\boxed{
R_{up}^{\sigma+}
\Longrightarrow
\text{positive-strain source genealogy},
}
\]

and

\[
\boxed{
R_{up}^{\kappa+}
\Longrightarrow
\text{positive-kappa packet + larger negative-kappa compensation}.
}
\]

Hence

\[
\boxed{
\text{hysteretic material recharge}
\Longrightarrow
\text{M15 positive-strain source}
\lor
\text{M13--M16 negative-kappa payer}.
}
\]

No independent recharge mechanism remains at the level of scalar sign accounting.

---

## 8. Completed-cycle variation floor

For completeness, a full down-and-up hysteretic cycle has a pathwise total-variation floor.

For the upward segment,

\[
\int g_+d\theta\ge\Delta_a,
\]

while for a completed downward segment from `a_+` to `a_-`,

\[
\int g_-d\theta\ge\Delta_a,
\]

where

\[
g=\sigma+\kappa-1.
\]

Therefore one completed cycle satisfies

\[
\boxed{
\int_{cycle}|\sigma+\kappa-1|d\theta
\ge2\Delta_a.
}
\]

For `N` completed cycles along a label,

\[
\boxed{
\int|\sigma+\kappa-1|d\theta
\ge2N\Delta_a.
}
\]

By M16-016 this growing path functional is **not** itself a contradiction. Its value is that the upward half of every cycle has now been routed to signed PDE payers.

---

## 9. Remaining obstruction

The survivor can still attempt a closed recurrent loop:

\[
\text{negative-kappa retirement}
\to
\text{low-amplitude phase}
\to
\text{positive-strain or positive-kappa recharge}
\to
\text{negative-kappa compensation}
\to\cdots
\]

M16-018 does not yet show that this loop consumes a nonrenewable amount of transverse flux.

The next target is therefore sharper:

> determine whether the positive-strain source and the mandatory negative-kappa compensation can be supported repeatedly by the **same finite flux lineage** without a net debit in the finite transverse-vorticity-flux resource identified in M13--M15.

This is now the principal remaining cycle-closure problem.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
