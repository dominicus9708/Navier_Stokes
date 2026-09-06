# DSD M17-225 — An intrinsic moving packet has parabolic mass persistence or a local palinstrophy/interface turnover payment

Date: 2026-09-06  
Canonical ID: **M17-225**

Status: **DYNAMIC STOPPING-TIME GATE / M17-224 PROVIDES A BUFFERED REMOTE PACKET OF RADIUS `r_j=O(ell_j)` WITH ITS TRANSITION-REGION `L2` MASS INCLUDED IN THE NORMALIZATION. MOVE THE CUTOFF CENTER WITH THE MATERIAL `B`-FLOW. THE EXACT LOCALIZED ENSTROPHY IDENTITY CONTAINS NEGATIVE LOCAL PALINSTROPHY, A DIFFUSIVE CUTOFF CROSS TERM, STRAIN/REACTION TERMS, AND THE MATERIAL CUTOFF RATE `D_B zeta`. ON A LOCALLY LIPSCHITZ COEFFICIENT CORRIDOR, THE STRAIN/REACTION/MATERIAL-CUTOFF TERMS ACCUMULATE ONLY `O(ell_j^2)` OF THE PACKET MASS OVER A PARABOLIC TIME `c ell_j^2`. THE DIFFUSIVE CROSS TERM IS CONTROLLED BY LOCAL PALINSTROPHY PLUS `ell_j^-2` TIMES TRANSITION-REGION ENSTROPHY. THEREFORE A FIRST FIXED-FRACTION MASS LOSS BEFORE `c ell_j^2` FORCES A FIXED `O(M_j)` PAYMENT BY TIME-INTEGRATED LOCAL PALINSTROPHY OR TRANSITION/INTERFACE FLUX. IF NEITHER PAYMENT OCCURS, THE PACKET RETAINS A FIXED POSITIVE FRACTION OF ITS MASS FOR A PARABOLIC TIME. THIS SUPPLIES THE DYNAMIC PERSISTENCE GATE NEEDED BEFORE ANY HEAT-TANGENT LIMIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Buffered intrinsic packet

Let the observation time be `theta=0`.

M17-224 supplies a remote packet center `q_j`, an intrinsic radius

\[
\boxed{r_j\to0,}
\]

and a smooth cutoff `zeta_j(y,0)` supported in

\[
B_{C r_j}(q_j)
\]

with an inner region on which `zeta_j=1`.

Define its localized enstrophy

\[
\boxed{
M_j(0)
:=\int \zeta_j(y,0)^2|W(y,0)|^2dy
>0.
}
\]

The transition-region mass is already bounded by the same normalization:

\[
\int_{\operatorname{supp}\nabla\zeta_j(0)}|W|^2dy
\le M_j(0).
\]

---

## 2. Move the cutoff with a material center

Let `q_j(theta)` solve

\[
\boxed{
\dot q_j(\theta)=B(q_j(\theta),\theta),
\qquad
q_j(0)=q_j.
}
\]

Fix the packet radius `r_j` over the short interval and set

\[
\boxed{
\zeta_j(y,\theta)
:=\zeta_0\left(\frac{y-q_j(\theta)}{r_j}\right),
}
\]

where `zeta_0` is a fixed smooth compact profile.

Then

\[
\nabla\zeta_j=O(r_j^{-1}),
\qquad
\Delta\zeta_j=O(r_j^{-2}).
\]

Moreover

\[
D_B\zeta_j
=
\left[B(y,\theta)-B(q_j(\theta),\theta)\right]\cdot\nabla\zeta_j.
\]

Assume on the short packet corridor

\[
\boxed{
\sup_{B_{Cr_j}(q_j(\theta))}|\nabla B|\le L_*<\infty.
}
\]

Then

\[
\boxed{|D_B\zeta_j|\le C L_*.}
\]

Failure of this local Lipschitz ceiling is retained as a derivative/strain hard exit.

---

## 3. Exact localized enstrophy identity

Define

\[
M_j(\theta)
:=\int\zeta_j^2\rho^2dy,
\qquad
\rho:=|W|.
\]

The similarity vorticity equation is

\[
D_BW
=\Delta W+\Sigma W-W,
\]

and

\[
\nabla\cdot B=\frac32.
\]

For any scalar density `f`,

\[
\frac d{d\theta}\int fdy
=\int(D_Bf+f\nabla\cdot B)dy.
\]

Applying this to `f=zeta_j^2 rho^2`, integrating the Laplacian term by parts, gives

\[
\boxed{
\begin{aligned}
M_j'
={}&-2\int\zeta_j^2|\nabla W|^2dy\\
&-4\int\zeta_j W\cdot(\nabla\zeta_j\cdot\nabla W)dy\\
&+2\int\zeta_j^2 W\cdot\Sigma Wdy\\
&-\frac12M_j\\
&+2\int\zeta_j(D_B\zeta_j)\rho^2dy.
\end{aligned}
}
\]

The coefficient `-1/2` is the exact combination of the `-W` reaction and `div B=3/2`.

---

## 4. Diffusive cutoff term

Let

\[
D_j(\theta)
:=\int\zeta_j^2|\nabla W|^2dy
\]

and define transition enstrophy

\[
N_j(\theta)
:=\int_{\operatorname{supp}\nabla\zeta_j(\theta)}\rho^2dy.
\]

Young's inequality gives

\[
\begin{aligned}
4\left|
\int\zeta_j W\cdot(\nabla\zeta_j\cdot\nabla W)
\right|
&\le
D_j
+C\int|\nabla\zeta_j|^2\rho^2dy\\
&\le
D_j+C r_j^{-2}N_j.
\end{aligned}
\]

Thus the only parabolically scaled boundary quantity is

\[
\boxed{
r_j^{-2}N_j.}
\]

---

## 5. Lower differential inequality

Assume additionally on the short corridor

\[
\boxed{\|\Sigma\|_{L^\infty(B_{Cr_j})}\le S_*<\infty.}
\]

Failure is retained as a local strain-spike exit.

Using Sections 2--4 in the exact identity,

\[
\boxed{
M_j'
\ge
-C_DD_j
-C_Br_j^{-2}N_j
-C_0M_j
}
\]

with constants independent of `j`.

Here `C_0` depends only on `S_*`, `L_*`, and the fixed cutoff profile.

---

## 6. First downward stopping time

Fix `0<eta<1/2` and a fixed `c_p>0`.

Let

\[
\tau_j^-
\]

be the first time in

\[
[0,c_pr_j^2]
\]

at which

\[
M_j(\tau_j^-)
=(1-\eta)M_j(0),
\]

provided such a time exists before any upward exit

\[
M_j=2M_j(0).
\]

Before `tau_j^-`,

\[
M_j(\theta)\le2M_j(0).
\]

Integrating the lower differential inequality gives

\[
\eta M_j(0)
\le
C_D\int_0^{\tau_j^-}D_jd\theta
+C_Br_j^{-2}\int_0^{\tau_j^-}N_jd\theta
+2C_0c_pr_j^2M_j(0).
\]

Since `r_j->0`, for sufficiently large `j`

\[
2C_0c_pr_j^2\le\frac\eta2.
\]

Hence

\[
\boxed{
\int_0^{\tau_j^-}D_jd\theta
+r_j^{-2}\int_0^{\tau_j^-}N_jd\theta
\ge c_\eta M_j(0).
}
\]

This is the quantitative early-forgetting payment.

---

## 7. Persistence/payment dichotomy

Therefore, for sufficiently large intrinsic packets, one of the following holds over

\[
0\le\theta\le c_pr_j^2:
\]

### A. Parabolic mass persistence

\[
\boxed{
M_j(\theta)\ge(1-\eta)M_j(0)
}
\]

until the end of the interval or until an upward mass event.

In particular the packet retains a fixed nonzero fraction of its initial localized enstrophy for a parabolic time.

### B. Local palinstrophy payment

\[
\boxed{
\int_0^{c_pr_j^2}D_jd\theta
\ge cM_j(0).
}
\]

### C. Transition/interface turnover payment

\[
\boxed{
r_j^{-2}
\int_0^{c_pr_j^2}N_jd\theta
\ge cM_j(0).
}
\]

### D. Coefficient hard exit

The local `grad B` or strain ceiling fails.

Thus

\[
\boxed{
H_{buffered\ intrinsic\ packet}
\Longrightarrow
H_{parabolic\ persistence}
\lor
H_{local\ palinstrophy}
\lor
H_{interface/turnover}
\lor
G_{local\ coefficient\ spike}.
}
\]

---

## 8. Why the lower-order terms cannot erase the packet on this time scale

The material-cutoff, strain, and reaction terms are all `O(M_j)` per unit similarity time under the bounded-coefficient corridor.

The interval length is

\[
O(r_j^2).
\]

Hence their total contribution is

\[
O(r_j^2M_j(0))
=o(M_j(0)).
\]

Only diffusion/palinstrophy or transition flux has the parabolic strength needed to remove a fixed fraction of the packet in this interval.

---

## 9. Backward-side interpretation

The same exact identity may be integrated on

\[
[-c_pr_j^2,0].
\]

A failure to retain a comparable ancestor mass cannot be attributed to the dissipative term in the same direction without sign care; it must be audited as backward turnover/replenishment through the transition region, coefficient input, or a large time-integrated derivative term.

M17-225 therefore records the forward persistence theorem exactly and treats two-sided persistence as a separate next step rather than silently reversing a dissipative estimate.

---

## 10. Relation to a heat tangent

On branch A, introduce the parabolic variables

\[
y=q_j(r_j^2\tau)+r_jz,
\qquad
\theta=r_j^2\tau.
\]

Moving with the material center, the exact vorticity equation becomes schematically

\[
\partial_\tau V_j
+r_j\left[B(q_j+r_jz)-B(q_j)\right]\cdot\nabla_zV_j
=
\Delta_zV_j
+r_j^2\Sigma_jV_j
-r_j^2V_j.
\]

If local coefficient bounds persist, then on fixed `z,tau` cylinders

\[
r_j[B(q_j+r_jz)-B(q_j)]\to0,
\qquad
r_j^2\Sigma_j\to0,
\qquad
r_j^2\to0.
\]

Thus the formal tangent equation is

\[
\boxed{\partial_\tau V=\Delta V.}
\]

However M17-225 does not yet claim a nonzero heat limit because compactness, cutoff forcing, and backward lifetime still require a separate theorem.

---

## 11. DSD analysis

### 11.1 Exact versus schematic levels

The localized enstrophy identity is exact.
The heat equation is stated only as the formal rescaled tangent after the persistence gate.

### 11.2 Payment classification

Early packet loss is not called a contradiction.
It is converted into explicit time-integrated palinstrophy or interface turnover at the packet scale.

### 11.3 Direction of time

Forward diffusion is coercive; backward diffusion is not.
The proof does not reverse the forward persistence inequality without a separate argument.

---

## 12. DSD audit

- The cutoff moves with the material center rather than remaining Eulerian-fixed.
- `div B=3/2` is included in the exact localized mass law.
- The transition mass is normalized from the start by M17-224.
- Bounded local coefficient assumptions are explicit and their failure is exported.
- Early loss produces a quantitative payer, not an unsupported persistence claim.
- A nonzero eternal heat solution is not yet claimed.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
