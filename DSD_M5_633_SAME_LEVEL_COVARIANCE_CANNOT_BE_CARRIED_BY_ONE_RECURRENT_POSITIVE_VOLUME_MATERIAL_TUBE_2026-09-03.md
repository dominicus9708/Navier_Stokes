# DSD M5-633 — Same-level covariance cannot be carried indefinitely by one positive-volume material tube

Date: 2026-09-03

Status: **INTERNAL MATERIAL-VOLUME RIGIDITY / M5-632 IDENTIFIES THE SAME-LEVEL KAPPA–ENSTROPHY COVARIANCE WITH A RECURRENT WEIGHTED STRETCHING SURPLUS. HOWEVER A FIXED POSITIVE-VOLUME MATERIAL TUBE SEGMENT CANNOT RECURRENTLY RETURN AS A BOUNDED SIMILARITY-SCALE CARRIER, BECAUSE `div B=3/2` GIVES THE EXACT EXPANSION `dV(theta)=dV(theta0) exp(3(theta-theta0)/2)`. THEREFORE REPEATED SAME-LEVEL COVARIANCE IN A FIXED EULERIAN ACTIVE CORE MUST BE REALIZED BY MATERIAL SHEATH TURNOVER OR BY A LOWER-DIMENSIONAL/ZERO-VOLUME PERSISTENT FLUX SPINE WITH RENEWING SURROUNDING VORTICITY LABELS. THIS DOES NOT YET CONTRADICT NAVIER–STOKES; IT REMOVES THE SAME-POSITIVE-VOLUME PERSISTENCE INTERPRETATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact material-volume law

For the similarity material velocity

\[
B=U+\frac12y,
\]

we have

\[
\nabla\cdot B=\frac32.
\]

Hence every genuine material volume element obeys

\[
\boxed{
D_B\log dV=\frac32.
}
\]

Therefore

\[
\boxed{
dV(\theta)=dV(\theta_0)e^{\frac32(\theta-\theta_0)}.
}
\]

This is the exact M5-560 expansion law.

---

## 2. Recurrent coherent positive-volume carrier hypothesis

Suppose one and the same material tube segment is claimed to carry the recurrent active enstrophy/covariance mechanism in a fixed bounded similarity core.

A genuine recurrent coherent positive-volume interpretation requires a sequence of return times

\[
\theta_j\to+\infty
\]

at which its material volume remains in a fixed nondegenerate range

\[
0<v_-\le dV(\theta_j)\le v_+<\infty.
\]

But the exact exponential law gives

\[
dV(\theta_j)
=dV(\theta_0)e^{\frac32(\theta_j-\theta_0)}\to\infty.
\]

Contradiction.

Thus

\[
\boxed{
\text{one fixed positive-volume material tube segment cannot be a recurrent bounded similarity carrier.}
}
\]

---

## 3. Consequence for M5-632 covariance/stretching surplus

M5-632 shows

\[
\langle\kappa e\rangle<0
\iff
\left\langle(\sigma-\tfrac14)e\right\rangle>0
\]

for the recurrent same-level tube balance.

M5-633 says this recurrent budget cannot be interpreted as the same positive-volume material parcel returning indefinitely.

Therefore repeated same-level activity in the finite Eulerian core must satisfy

\[
\boxed{
C_{same-level}^{\kappa-E}
\Longrightarrow
T_{sheath}^{material}
\lor
S_{spine}^{zero-volume}.
}
\]

Here

- `T_sheath^material`: the three-dimensional enstrophy-bearing material sheath is continually replaced;
- `S_spine^zero-volume`: a lower-dimensional material flux spine/surface can persist while its positive-volume neighborhood is renewed.

---

## 4. Why this does not kill the M5-603 persistent flux lineage

A vorticity flux lineage is represented by a material surface patch and is not a positive-volume material body.

The material-volume expansion law therefore does **not** imply that the persistent flux surface itself must disappear.

A consistent survivor can have

\[
\boxed{
\text{persistent material flux spine}
+
\text{renewing positive-volume enstrophy sheath}.
}
\]

This distinction is essential.

Calling the volume expansion a contradiction to the persistent flux lineage would repeat the material-object conflation already excluded by the earlier migration audit.

---

## 5. Finite-residence estimate inside a bounded core

If a complete material segment remains entirely inside a fixed ball `B_R`, then necessarily

\[
dV(\theta)\le |B_R|.
\]

Starting from volume `v0>0`, the maximal possible residence time before the material volume alone exceeds the core volume is bounded by

\[
\boxed{
T_{vol}
\le
\frac23\log\frac{|B_R|}{v_0}.
}
\]

Thus any coherent positive-volume parcel has a uniformly finite full-containment lifetime once a fixed lower initial volume is specified.

The same material set may continue to intersect the core after that time, but then only a changing subset of its labels contributes to the local coherent carrier.

That is precisely material turnover.

---

## 6. Combine with M5-621 curvature cocycle

M5-621 independently shows that a fixed material flux label cannot carry a fixed curvature charge indefinitely:

\[
D_B\log\frac{\rho|\mathcal K|}{|\phi|}=-\frac32.
\]

M5-633 now shows that a fixed positive-volume tube segment cannot carry the recurrent enstrophy covariance indefinitely either.

Thus two different material objects have finite persistence:

\[
\boxed{
\begin{array}{ll}
\text{curvature on one flux label} &\to \text{finite lifetime},\\
\text{positive-volume enstrophy parcel} &\to \text{finite bounded-core lifetime}.
\end{array}
}
\]

The remaining hard survivor is therefore naturally a persistent lower-dimensional flux skeleton with positive-density replacement of its surrounding three-dimensional sheath.

---

## 7. Updated hard object

The same-level covariance branch should now be pictured as

\[
\boxed{
\text{persistent synchronized kappa-level flux spine}
+
\text{materially renewing enstrophy sheath}.
}
\]

The next calculation should identify what exact PDE mechanism moves enstrophy across that persistent spine/sheath decomposition.

Because the CE-H direction is material (`D_B xi=0`), the natural candidate is the transverse-magnitude channel

\[
G=P_\xi^\perp\nabla\log\rho
\]

from M5-622 rather than projective direction turnover.

---

## 8. Firewall

This note does not claim that every local coherent carrier is a single material tube segment.

It proves only that **if** recurrent covariance were assigned to one fixed positive-volume material segment, that interpretation is impossible.

The valid survivor is explicitly retained as a through-flow/turnover system.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]