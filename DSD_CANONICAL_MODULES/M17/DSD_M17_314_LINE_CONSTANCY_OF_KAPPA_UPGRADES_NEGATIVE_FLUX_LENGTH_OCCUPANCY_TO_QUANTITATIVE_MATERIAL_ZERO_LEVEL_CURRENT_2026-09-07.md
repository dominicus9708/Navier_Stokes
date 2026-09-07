# DSD M17-314 — Line constancy of `kappa` upgrades negative flux-length occupancy to a quantitative material zero-level current

Date: 2026-09-07  
Canonical ID: **M17-314**

Status: **ARC-LENGTH-TO-MATERIAL-LABEL BRIDGE ON THE BOUNDED VORTEX-LINE FAMILY / M17-312 LEFT A FIREWALL BETWEEN NEGATIVE `kappa` FLUX-LENGTH OCCUPANCY AND THE M5-681 MATERIAL FLUX-LABEL DISTRIBUTION BECAUSE A NEGATIVE SEGMENT MIGHT MIGRATE ALONG ONE LINE. M17-313 REMOVES THAT POSSIBILITY ON EXACT REGULAR CE-H: `D_xi kappa=0` AND `D_xi(D_B kappa)=0`, SO `kappa` AND ITS MATERIAL VELOCITY ARE CONSTANT ALONG EACH CONNECTED VORTEX LINE. ON A RETAINED HIGH-AMPLITUDE VORTEX-LINE FAMILY WITH UNIFORM BOUNDED CAPTURE LENGTH `L_*`, THE M17-312 LOWER BOUND `int kappa_- ds dPhi >= c_Phi` THEREFORE IMPLIES A FIXED NEGATIVE FIRST MOMENT OF THE M5-681 MATERIAL FLUX DISTRIBUTION, `int_{k<0}(-k)F(k,theta)dk >= c_Phi/L_*`. UNDER THE COMPACT `|kappa|<=K_*` CEILING THIS ALSO GIVES A FIXED POSITIVE FLUX MASS OF NEGATIVE LABELS. AFTER RECURRENT AVERAGING, THE EXACT M5-681 STATIONARY EQUATION `partial_k Gbar=k Fbar` THEN YIELDS A QUANTITATIVE DIRECTED CURRENT THROUGH ZERO, `Gbar(0)<=-c_Phi/L_*<0`. FAILURE OF THE BOUNDED-LENGTH CAPTURE IS AN EXPLICIT WINDING/DECOMPACTIFICATION EXIT. THIS DOES NOT YET CONTRADICT NAVIER--STOKES; IT CONVERTS THE NEGATIVE PHASE INTO TRUE SAME-MATERIAL LABEL TURNOVER RATHER THAN SPATIAL SEGMENT MIGRATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact line constancy from M17-313

On exact regular CE-H,

\[
\boxed{D_\xi\kappa=0.}
\]

Therefore at each fixed time `theta`, `kappa` is constant along every connected active vortex line.

Let `lambda` denote one such material vortex-line/tube label and write

\[
\boxed{
\kappa_\lambda(\theta)
}
\]

for the common value on its retained connected segment.

M17-313 also gives

\[
\boxed{
D_\xi h=0,
\qquad
h:=D_B\kappa.
}
\]

Thus the material velocity of `kappa` is line-constant as well.

This validates the scalar material trajectory

\[
\theta\mapsto\kappa_\lambda(\theta)
\]

used in the M5-681 label-space continuity equation on this branch.

---

## 2. Negative flux-length input

M17-312 gives on a regular high-amplitude vortex-line flux family

\[
\boxed{
\int\int
\chi_*(\rho)\kappa_-\,ds\,d\Phi
\ge c_\Phi>0.
}
\]

Because `kappa_-` is constant along a line label,

\[
\kappa_-(s,\lambda,\theta)
=
(\kappa_\lambda(\theta))_-.
\]

Define the retained high-amplitude capture length of label `lambda` by

\[
\boxed{
L_*(\lambda,\theta)
:=
\int_{\Gamma_\lambda(\theta)}
\chi_*(\rho)\,ds.
}
\]

Then the flux-length moment becomes exactly

\[
\boxed{
\int
(\kappa_\lambda)_-
L_*(\lambda,\theta)
\,d\Phi_\theta(\lambda)
\ge c_\Phi.
}
\]

---

## 3. Bounded capture-length branch

Assume the retained family satisfies

\[
\boxed{
L_*(\lambda,\theta)
\le L^*<\infty
}
\]

uniformly.

This holds, for example, on the compact closed-loop branch with uniform length upper bound, or on a finite-flow-box family with uniformly bounded reuse.

If it fails, retain the explicit exit

\[
\boxed{
G_{line\ winding/decompactification/reuse}.
}
\]

On the bounded-length branch,

\[
\begin{aligned}
c_\Phi
&\le
\int
(\kappa_\lambda)_-
L_*(\lambda,\theta)d\Phi_\theta\\
&\le
L^*
\int
(\kappa_\lambda)_-
d\Phi_\theta.
\end{aligned}
\]

Hence

\[
\boxed{
\int
(\kappa_\lambda)_-
d\Phi_\theta
\ge
\frac{c_\Phi}{L^*}
=:d_{flux}>0.
}
\]

This is now a genuine material-flux-label moment.

---

## 4. Identify the M5-681 negative first moment

M5-681 defines

\[
F(k,\theta)
=
\int
\delta(k-\kappa_\lambda(\theta))
\,d\mu_\theta(\lambda),
\]

where the current oriented material flux weight is the retained `dPhi_theta` up to the fixed branch convention.

Therefore

\[
\begin{aligned}
\int_{k<0}(-k)F(k,\theta)dk
&=
\int
(\kappa_\lambda)_-
d\mu_\theta(\lambda).
\end{aligned}
\]

Thus the bounded-length branch gives

\[
\boxed{
\int_{k<0}(-k)F(k,\theta)dk
\ge d_{flux}>0.
}
\]

This is the precise material-label statement that M17-312 could not yet make.

---

## 5. Fixed negative-label flux mass

On the retained high-amplitude compact coefficient support,

\[
|\kappa_\lambda|\le K_*.
\]

Hence

\[
(\kappa_\lambda)_-
\le
K_*\mathbf1_{\{\kappa_\lambda<0\}}.
\]

Therefore

\[
\boxed{
\mu_\theta\{\lambda:\kappa_\lambda<0\}
\ge
\frac{d_{flux}}{K_*}
=:m_{flux,-}>0.
}
\]

A fixed positive amount of current material flux is therefore genuinely carried by negative-`kappa` labels on every retained state of this branch.

---

## 6. Recurrent average

Take the recurrent/invariant time average used in M5-681.

Since the lower bound holds statewise,

\[
\boxed{
\int_{k<0}(-k)\overline F(k)dk
\ge d_{flux}>0.
}
\]

Thus the negative material-flux population is not merely nonempty in the recurrent mean; it has a fixed negative first moment.

---

## 7. Quantitative zero-level current

M5-681 gives the exact stationary equation

\[
\boxed{
\partial_k\overline G(k)
=k\overline F(k).
}
\]

On compact coefficient support choose `-K_*` below the support so that

\[
\overline G(-K_*)=0.
\]

Integrate from `-K_*` to `0`:

\[
\overline G(0)
=
\int_{-K_*}^{0}
 k\overline F(k)dk.
\]

Hence

\[
\boxed{
\overline G(0)
=-
\int_{k<0}(-k)\overline F(k)dk
\le
-d_{flux}<0.
}
\]

Therefore the recurrent CE-H material ensemble carries a **quantitatively nonzero directed mean current through the zero-multiplier level**.

This upgrades the qualitative sign conclusion of M5-681 on the present high-amplitude bounded-length branch.

---

## 8. No along-line phase-migration escape

Before M17-313, a negative spatial segment could in principle move along one line while the same line label remained in another multiplier phase.

That escape is impossible on exact CE-H because

\[
D_\xi\kappa=0.
\]

At a fixed time, a connected regular vortex line has one multiplier value.

Moreover

\[
D_\xi h=0
\]

means the line changes its multiplier coherently in material time.

Thus a crossing of

\[
\kappa_\lambda=0
\]

is a genuine **same-material line-label phase transition**, not migration of a negative patch along that line.

---

## 9. What can still evade the current theorem

The quantitative current conclusion can fail only through an explicit branch assumption:

\[
\boxed{
G_{\kappa_-\text{-}nodal}^{crit}
\lor
G_{line\ winding/decompactification/reuse}
\lor
G_{rank/interface/flux\ capture}
\lor
G_{coefficient\ noncompact}.
}
\]

The first is the M17-311 low-amplitude critical concentration branch.

The second prevents removing arc length from the flux-length moment.

The third prevents allocating a fixed charge to a controlled vortex-line flux family.

The fourth prevents the compact `kappa` support used by M5-681.

---

## 10. Why the quantitative current is not yet a contradiction

A recurrent material population can in principle cycle repeatedly through positive and negative multiplier phases.

M5-681 already identifies this possibility as a nonequilibrium `kappa`-space conveyor.

The present result strengthens it to

\[
\boxed{
|\overline G(0)|
\ge d_{flux}>0.
}
\]

but does not yet prove a finite cumulative resource for this current.

The next target is therefore constitutive rather than combinatorial:

\[
\boxed{
\text{Can the exact CE-H law for }h=D_B\kappa
\text{ sustain a fixed zero-level current while }D_\xi\kappa=0?
}
\]

The new line-constancy constraint should be inserted into the M5-682/688 constitutive equations before any further current estimate.

---

## 11. DSD audit

- The arc-length factor is removed only under an explicit uniform upper bound.
- `D_xi kappa=0` is used to identify one multiplier value per connected material vortex line.
- The M5-681 label distribution is entered only after that identity step.
- A negative spatial phase is not silently treated as a label phase when line length/decomposition is uncontrolled.
- The zero-current estimate uses the exact stationary M5-681 equation.
- The result is a quantitative recurrent current, not a finite budget.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
