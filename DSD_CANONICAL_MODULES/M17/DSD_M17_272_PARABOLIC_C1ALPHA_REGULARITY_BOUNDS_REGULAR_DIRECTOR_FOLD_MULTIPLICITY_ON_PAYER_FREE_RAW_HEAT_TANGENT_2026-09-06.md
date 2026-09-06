# DSD M17-272 — Parabolic C1-alpha regularity bounds regular director fold multiplicity on the payer-free raw heat tangent

Date: 2026-09-06  
Canonical ID: **M17-272**

Status: **SECOND-JET RESIDUAL CLOSURE ON THE PAYER-FREE HEAT LANE / M17-268 LEFT `|D2 xi| -> infinity` AS THE COMPLEMENT OF `s2 -> 0`, AND M17-269--271 CLASSIFIED BULK VERSUS SUBSCALE JET ESCALATION. ON THE ACTUAL PAYER-FREE RAW HEAT TANGENT, HOWEVER, M17-255 PLUS THE M17-261 FIXED-K MASS CORRECTION GIVE UNIFORM LOCAL `L2` MASS AND BOUNDED LOWER-ORDER COEFFICIENTS IN `partial_tau V-Delta V=-A·grad V+C V`. STANDARD INTERIOR PARABOLIC `W^{2,1}_p` ESTIMATES, WITH LOWER-ORDER TERMS ABSORBED by interpolation, give uniform bounds for every finite `p` on a smaller cylinder. CHOOSING `p>5` YIELDS A UNIFORM SPATIAL `C^{1,alpha}` BOUND. WHERE `|V|>=a_*>0`, THE DIRECTOR `xi=V/|V|` INHERITS A UNIFORM `C^{1,alpha}` BOUND. A REGULAR TRANSVERSE PREIMAGE WITH `s2>=delta_*>0` THEN HAS A FIXED QUANTITATIVE INJECTIVITY RADIUS; A FIXED-AREA SECTION CAN CONTAIN ONLY FINITELY MANY PREIMAGES OF ONE REGULAR DIRECTOR VALUE. THUS UNBOUNDED FOLD MULTIPLICITY ON THIS LANE FORCES `s2 -> 0`, AMPLITUDE/NODAL DEGENERATION, OR FAILURE OF THE LOCAL MASS/COEFFICIENT CORRIDOR. PURE SECOND-JET SPIKING IS NOT A TERMINAL PAYER-FREE ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Payer-free finite cylinder

Fix a compact parabolic cylinder

\[
Q_2:=B_2\times[-4,0]
\]

in own-scale variables.

On the raw branch the rescaled equation has the form

\[
\boxed{
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j.
}
\]

M17-255 gives the finite-cylinder compactness gate.
M17-261 removes fixed-`K` mass decompactification as a quiet coherent-mean escape.

Therefore on the payer-free compact lane assume

\[
\boxed{
\|V_j\|_{L^2(Q_2)}\le M_0,
\qquad
\|A_j\|_{L^\infty(Q_2)}
+\|C_j\|_{L^\infty(Q_2)}
\le M_1.
}
\]

Failure of either bound is already an existing normalized-palinstrophy / ambient-coefficient exit.

---

## 2. Interior parabolic Lp bootstrap

For constant principal operator `partial_tau-Delta`, standard interior parabolic estimates give on nested cylinders

\[
\|V_j\|_{W^{2,1}_p(Q_1)}
\le
C_p\left(
\|A_j\nabla V_j\|_{L^p(Q_{3/2})}
+\|C_jV_j\|_{L^p(Q_{3/2})}
+\|V_j\|_{L^p(Q_{3/2})}
\right).
\]

Because `A_j,C_j` are bounded lower-order coefficients, interpolation gives for every `epsilon>0`

\[
\|\nabla V_j\|_{L^p}
\le
\epsilon\|D^2V_j\|_{L^p}
+C_{\epsilon,p}\|V_j\|_{L^p}.
\]

Choose `epsilon` small enough to absorb the derivative term into the left side.
Local parabolic boundedness and iteration from the uniform `L2` corridor then give, for every finite `p`,

\[
\boxed{
\|V_j\|_{W^{2,1}_p(Q_1)}\le C_{p,M_0,M_1}.
}
\]

No spatial derivative of `A_j` or `C_j` is required for this lower-order bootstrap.

---

## 3. C1-alpha compactness

The parabolic homogeneous dimension is

\[
3+2=5.
\]

Choose

\[
p>5.
\]

Parabolic Sobolev embedding yields some

\[
\alpha=1-\frac5p>0
\]

and

\[
\boxed{
\|V_j\|_{C^{1,\alpha}_x C^{(1+\alpha)/2}_\tau(Q_{1/2})}
\le C.
}
\]

In particular, on each fixed time slice inside the smaller cylinder,

\[
\boxed{
\|\nabla V_j\|_{C^\alpha(B_{1/2})}\le C.
}
\]

---

## 4. Transfer to the director on a nondegenerate active patch

Assume on the retained fold patch

\[
\boxed{|V_j|\ge a_*>0.}
\]

If this fails, retain

\[
G_{nodal/amplitude\ degeneration}.
\]

The normalization map

\[
F(v)=v/|v|
\]

is smooth on

\[
|v|\ge a_*.
\]

Therefore composition estimates give

\[
\boxed{
\|\xi_j\|_{C^{1,\alpha}(B_{1/2})}
\le C_{a_*}.
}
\]

Hence

\[
\boxed{
[D\xi_j]_{C^\alpha(B_{1/2})}
\le H_\alpha<\infty
}
\]

uniformly in `j`.

This is stronger for fold packing than a raw `L-infinity` bound on `D2 xi`.

---

## 5. Quantitative injectivity radius for a regular transverse preimage

Let

\[
\Sigma_j\subset B_{1/2}
\]

be a transverse two-dimensional section with uniformly controlled geometry.

Suppose

\[
x_{j,m}\in\Sigma_j
\]

is a preimage of a regular director value `eta_j` and the smallest singular value of the restricted differential satisfies

\[
\boxed{s_{2,j}(x_{j,m})\ge\delta_*>0.}
\]

By the `C^alpha` control,

\[
\|D\xi_j(x)-D\xi_j(x_{j,m})\|
\le H_\alpha |x-x_{j,m}|^\alpha.
\]

Choose

\[
\boxed{
r_*
:=
\left(\frac{\delta_*}{4H_\alpha}\right)^{1/\alpha}>0.}
\]

Then on

\[
B_{r_*}(x_{j,m})\cap\Sigma_j
\]

the restricted differential remains quantitatively nondegenerate.
The map is locally bi-Lipschitz after shrinking by one fixed factor.

Consequently two distinct preimages of the same regular director value cannot lie arbitrarily close inside the same regular chart.

---

## 6. Fixed-area multiplicity cap

Assume the transverse sections satisfy

\[
|\Sigma_j|\le A_*<\infty
\]

with a uniformly finite regular atlas.

The fixed-radius neighborhoods around distinct regular preimages can be chosen with bounded overlap, and after a standard disjoint subfamily extraction one obtains

\[
\boxed{
N_j
\le
C\frac{A_*}{r_*^2}<\infty.
}
\]

The right side is independent of `j`.

Therefore

\[
\boxed{
N_j\to\infty,
\quad s_2\ge\delta_*,
\quad |V|\ge a_*,
\quad \text{payer-free compact cylinder}
}
\]

is impossible.

---

## 7. Correct fold-multiplicity return

M17-268 gave

\[
G_{fold\ multiplicity}
\Longrightarrow
G_{s_2\to0}
\lor
G_{D^2\xi\ spike}.
\]

On the present payer-free compact heat lane, Sections 1--6 sharpen this to

\[
\boxed{
G_{fold\ multiplicity}
\Longrightarrow
G_{s_2\to0\;/\;rank\text{-}anisotropy}
\lor
G_{nodal/amplitude\ degeneration}
\lor
H_{normalized\ palinstrophy/mass\ escape}
\lor
G_{scaled\ ambient/coefficient}.
}
\]

Thus the second-jet spike is not an independent terminal escape once the actual parabolic PDE corridor is used.

---

## 8. Relation to M17-269--271

M17-269--271 remain useful as pre-limit and noncompact audits:

- bulk second-jet growth returns to first-jet/log-amplitude channels;
- first-jet bulk growth returns to area/anisotropy or a metric microcarrier;
- pointwise-only jet escalation is a strict subscale.

M17-272 adds that on the final payer-free compact raw heat branch, parabolic regularity prevents that strict fold subscale from supporting unbounded **regular** multiplicity while `s2` and amplitude remain nondegenerate.

---

## 9. DSD audit

- The regularity argument uses bounded lower-order coefficients, not nonexistent derivative bounds on those coefficients.
- The amplitude floor is explicit; failure is a nodal branch.
- The singular-value floor is explicit; failure is rank/anisotropy degeneration.
- The conclusion is a multiplicity cap, not a global injectivity theorem for the director map.
- Singular values, nodal sets, interfaces, and chart failures remain separate exits.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
