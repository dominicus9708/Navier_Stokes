# DSD M5-43 — Backward Local Extinction and Pump-to-Defect Formation from Infinity

Date: 2026-08-27

Status: **AUDITED AFTER M5-41 / THE PUMP-ANCHORED ANCIENT-TO-TERMINAL CELL VANISHES LOCALLY IN THE REMOTE PAST, HAS A FINITE-AMPLITUDE PUMP AT `sigma=0`, AND RETAINS A STATIC `1/r` RESERVOIR AT SPATIAL INFINITY / GLOBAL REGULARITY UNPROVED.**

## 1. Correct ancient-to-terminal representation

M5-41 gives

\[
V_*(z,\sigma)
=
(\lambda_c^2-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{\lambda_c^2-\sigma}},
\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}
\right),
\qquad
\sigma<\lambda_c^2,
\]

where `U^#` is a complete trajectory in the compact recurrent W1 set.

There exists `M_*<infinity` such that

\[
\sup_{\eta}\|U^\#(\eta)\|_\infty\le M_*.
\]

---

## 2. Global Type-I backward bound

Therefore

\[
\boxed{
\|V_*(\sigma)\|_\infty
\le
\frac{M_*}{\sqrt{\lambda_c^2-\sigma}}.
}
\]

As

\[
\sigma\to-\infty,
\]

one has

\[
\boxed{
V_*(\cdot,\sigma)\to0
\quad\text{locally uniformly, and in the available local smooth topology}.
}
\]

For the threshold-one quadratic excess

\[
\mathcal G(V)=\frac12\int(|V|-1)_+^2dz,
\]

if

\[
\lambda_c^2-\sigma>M_*^2,
\]

then `||V_*(sigma)||_infinity<1`, so

\[
\boxed{
\mathcal G(V_*(\sigma))=0
\quad\text{for all sufficiently negative }\sigma.
}
\]

Thus the high-amplitude state is absent in the remote ancient past.

---

## 3. Finite-amplitude pump at `sigma=0`

The corrected M5-41 anchor is not a boundary first hit. It is a recurrent pump-active event at the fixed W1 amplitude `lambda_c`.

At

\[
\sigma=0,
\]

threshold `|V|=1` corresponds exactly to `|U|=lambda_c`, and the W1 gain satisfies

\[
\boxed{
J_P(\lambda_c)-\nu D_{\lambda_c}\ge g_c>0
}
\]

on the selected pump sequence.

Hence the high-amplitude excess is actively driven at a finite ancient time before the terminal boundary is reached.

The M5-23--40 Hodge/direction-compression estimates should be read in this audited pump-event form rather than as properties of a `lambda->0` first-hit sequence.

---

## 4. Static spatial-infinity reservoir

M5-42 gives the static leading far field

\[
\boxed{
V_{tail}(z)
=\frac1{|z|}
\Phi\!\left(
\frac z{|z|},
\log\frac{|z|}{\lambda_c}
\right).
}
\]

If the W1 critical residue is nonzero, this reservoir is nontrivial in the selected hull/averaged sense.

Thus the same cell simultaneously has

\[
\boxed{
\text{local state }\to0
\quad(\sigma\to-\infty)
}
\]

and

\[
\boxed{
\text{nonzero static critical `1/r` ancestry at spatial infinity}.
}
\]

---

## 5. Forward transport to the terminal boundary

The same fixed physical threshold corresponds to the W1 amplitude

\[
\lambda(\sigma)=\sqrt{\lambda_c^2-\sigma}.
\]

Therefore

\[
\lambda(0)=\lambda_c,
\]

while

\[
\boxed{
\lambda(\sigma)\downarrow0
\qquad(\sigma\uparrow\lambda_c^2).
}
\]

Hence the complete DSD history is

\[
\boxed{
\begin{array}{c}
\text{remote-past local extinction}\\
+\\
\text{static critical reservoir at infinity}\\
\Downarrow\\
\text{finite-amplitude pump at }\sigma=0\\
\Downarrow\\
\text{same-threshold amplitude transport}\\
\Downarrow\\
\text{zero-amplitude boundary defect as }\sigma\uparrow\lambda_c^2.
\end{array}
}
\]

This is the corrected formation-from-infinity topology.

---

## 6. Fixed-ball local-energy consequence

For fixed `R`,

\[
E_R(\sigma):=\frac12\int_{B_R}|V_*|^2dz
\]

satisfies

\[
E_R(\sigma)\to0
\qquad(\sigma\to-\infty).
\]

Thus every positive later local energy amount must be accumulated through boundary flux minus local viscous loss.

This does not by itself contradict finite-energy ancestry because the ancient limit contains an infinite critical reservoir at spatial infinity.

---

## 7. Relation to Type-I ancient theory

The backward decay is consistent with standard Type-I ancient solutions. Albritton--Barker show that Type-I singularities correspond to nontrivial Type-I ancient profiles and obtain Liouville rigidity under a strong-`L^3` backward-sequence assumption.

The present cell remains on the weak-critical side because of its static `1/r` tail.

The W1-specific additions are:

- complete recurrent inverse-Leray ancestry;
- a distinguished finite-amplitude pump time;
- static far-tail memory;
- and forward transport of that same threshold into the terminal boundary sector.

---

## 8. Updated target

A genuinely new M5 rigidity theorem would have to use the **whole pump-to-defect history**, not merely backward Type-I decay or the static tail separately.

Natural next targets are:

1. a same-trajectory flux law connecting the pump event to the later boundary defect;
2. a tail-subtracted or renormalized ancient formulation;
3. a rigidity theorem for an ancient solution with local backward extinction, static critical far field, a positive finite-amplitude pump, and a finite forward terminal horizon;
4. or a bridge producing a strong-`L^3` backward sequence after a legitimate tail cancellation.

No such closure is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
