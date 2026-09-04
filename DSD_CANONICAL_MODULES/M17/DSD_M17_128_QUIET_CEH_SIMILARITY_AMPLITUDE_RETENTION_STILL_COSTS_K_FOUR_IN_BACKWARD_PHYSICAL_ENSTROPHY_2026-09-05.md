# DSD M17-128 — Quiet CE-H similarity-amplitude retention still costs K^-4 in backward physical enstrophy

Date: 2026-09-05
Canonical ID: **M17-128**

Status: **EXACT ANTI-PROOF SCALING AUDIT / M17-126 SAME-MATERIAL SPATIAL LOCALIZATION PLUS M17-127 BOUNDED CE-H AMPLITUDE EXPOSURE DOES NOT MAKE THE ANCESTOR MATERIAL PACKET CARRY COMPARABLE PHYSICAL ENSTROPHY. IF `r_{j-k}=K_k r_j` AND THE SIMILARITY AMPLITUDES ARE COMPARABLE, THEN PHYSICAL VORTICITY ON THE SAME MATERIAL POINT IS SMALLER BACKWARD BY `K_k^-2`. PHYSICAL MATERIAL VOLUME IS PRESERVED, SO THE SAME CARRIER'S PHYSICAL ENSTROPHY AND ANCESTOR-RADIUS-WEIGHTED SHELL COST ARE SMALLER BY `K_k^-4`. THUS EVEN AN EXACT QUIET CE-H MATERIAL GENEALOGY DOES NOT SUPPLY THE M5 RETURN-DENSITY/AMPLITUDE LOWER BOUND. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inter-stage scale relation

Let

\[
r_{j-k}=K_kr_j,
\qquad K_k>1.
\]

Physical and similarity vorticity amplitudes satisfy

\[
\boxed{
|\omega(t)|=r(t)^{-2}\rho(\theta).
}
\]

---

## 2. Quiet CE-H amplitude exposure

For a material carrier, M17-127 gives

\[
\rho_j
=\rho_{j-k}e^{\mathcal E_\rho(j,k)}.
\]

Assume

\[
|\mathcal E_\rho(j,k)|\le L.
\]

Then

\[
e^{-L}\rho_j
\le
\rho_{j-k}
\le
e^L\rho_j.
\]

---

## 3. Physical vorticity ratio

At the descendant stage,

\[
|\omega_j|
=r_j^{-2}\rho_j.
\]

At the ancestor stage,

\[
|\omega_{j-k}|
=r_{j-k}^{-2}\rho_{j-k}
=K_k^{-2}r_j^{-2}\rho_{j-k}.
\]

Therefore

\[
\boxed{
 e^{-L}K_k^{-2}|\omega_j|
\le
|\omega_{j-k}|
\le
 e^LK_k^{-2}|\omega_j|.
}
\]

The `K_k^{-2}` factor is pure similarity scaling and remains even when the normalized material amplitude is perfectly retained.

---

## 4. Material-volume preservation

Let `A_j` be a material carrier bundle at stage `j` and `A_{j-k}` its inverse-flow image.
Physical incompressibility gives

\[
\boxed{|A_{j-k}|=|A_j|.}
\]

If the bounded-exposure estimate holds uniformly on the material bundle, then changing variables by the volume-preserving flow gives

\[
\boxed{
 e^{-2L}K_k^{-4}
\int_{A_j}|\omega_j|^2dx
\le
\int_{A_{j-k}}|\omega_{j-k}|^2dx
\le
 e^{2L}K_k^{-4}
\int_{A_j}|\omega_j|^2dx.
}
\]

Thus

\[
\boxed{
E_{j-k}^{\omega,mat}
\asymp_L
K_k^{-4}E_j^{\omega,mat}.
}
\]

---

## 5. Ancestor-radius weighted shell cost

M17-126 places the same material bundle at a physical radius comparable to

\[
r_{j-k}=\rho_{j,k}
\]

under the bounded-similarity-velocity hypothesis.

The descendant remote shell is also at this same physical radius scale by the ancestor-radius identity.
Therefore multiplying both enstrophy energies by the same shell radius yields

\[
\boxed{
J_{j-k}^{\omega,mat}
\asymp_L
K_k^{-4}J_{j,k}^{\omega,mat}.
}
\]

So even ideal normalized-amplitude retention supplies only a `K_k^{-4}` backward weighted-enstrophy fraction for the same material carrier.

---

## 6. Why this does not contradict first-hitting growth

A stage-`j-k` normalized amplitude of order one corresponds physically to vorticity of order

\[
r_{j-k}^{-2}.
\]

A stage-`j` normalized amplitude of order one corresponds physically to

\[
r_j^{-2}=K_k^2r_{j-k}^{-2}.
\]

Thus the physical `K_k^2` amplification is already built into the change of first-hitting scale. No large CE-H exposure is needed merely to produce this scale factor.

Consequently one must not interpret bounded `mathcal E_rho` as physical-vorticity constancy.

---

## 7. Consequence for reverse genealogy

Suppose a descendant remote ribbon shell carries critical weighted enstrophy `J_{j,k}^omega`.
Tracking its same material carrier backward with bounded CE-H exposure gives at best

\[
\boxed{
J_{ancestor}^{same\ carrier}
\gtrsim
K_k^{-4}J_{j,k}^\omega,
}
\]

not an order-one fraction of `J_{j,k}^omega`.

For a critical model with `J_{j,k}^omega~1`, the backward costs

\[
K_k^{-4}
\]

are geometrically summable.
Therefore no contradiction with finite historical energy/enstrophy follows from this route alone.

---

## 8. Relation to the older M5 genealogy firewall

The older M5 analysis concluded that radius matching and quiet packet transport do not automatically produce the physical weighted return density needed to close the cubic tail.

M17-126 and M17-127 sharpen the location and amplitude equations, but M17-128 shows that the same fundamental scale mismatch remains after those improvements.

Thus the unresolved object is not merely material identification. It is the production of enough **physical-time/physical-amplitude mass at the ancestor scale**.

---

## 9. DSD audit

### Audit A — normalized amplitude retention equals physical amplitude retention

Rejected. Physical vorticity carries the additional factor `r^{-2}`.

### Audit B — volume expansion in physical variables

Rejected. Physical incompressible material volume is preserved. The similarity-volume expansion is a coordinate effect.

### Audit C — current remote shell and ancestor shell use different radius weights

For the ancestor-radius genealogy they use comparable physical radius `r_{j-k}`, so the `K_k^{-4}` energy factor remains the same in the weighted shell number.

### Audit D — K^-4 proves summability for every possible tail

Rejected. It shows the quiet same-carrier route is too weak by itself. Other multiplicity, exposure, or rebuilding mechanisms may carry larger historical cost.

### Audit E — proof status

This is an anti-proof firewall, not a closure theorem.

---

## 10. Updated genealogy target

The cubic-divergent tail cannot be closed merely by proving

\[
\text{same material location}
+
|\mathcal E_\rho|\le L.
\]

A successful historical closure must additionally force at least one of:

\[
\boxed{
\begin{aligned}
&\text{large carrier multiplicity at ancestor scale},\\
&\text{large cumulative CE-H exposure},\\
&\text{shell rebuilding/turnover with a nonrecyclable cost},\\
&\text{or a Liouville/tail-decoupling rigidity theorem not based on ordinary return density}.
\end{aligned}
}
\]

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
