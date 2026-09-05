# DSD M17-151 — Mixed and transverse log-amplitude convexity payers recharge through the `kappa` Hessian, so the M17-150 half-damping closure does not extend

Date: 2026-09-05  
Canonical ID: **M17-151**

Status: **MIXED/TRANSVERSE PAYER AUDIT / M17-150 CLOSES INDEFINITE QUIET RECURRENCE OF THE AXIAL CONVEXITY PAYER BECAUSE `R_n=D_n log|r|` HAS AN ALMOST HOMOGENEOUS `-1/2` MATERIAL LAW. THE SAME ARGUMENT CANNOT BE COPIED TO THE M17-148 MIXED OR PURE-TRANSVERSE LOG-AMPLITUDE HESSIAN PAYERS. WITH `psi=log rho` AND `S=sigma+kappa`, THE EXACT HESSIAN COMMUTATOR IS `D_B Hess psi=Hess S-(grad B)^T Hess psi-(Hess psi)grad B-(Hess B)·grad psi`. AT A PEAK TANGENCY, MATERIAL FRAME ROTATION DOES NOT ADD A TERM TO `H_xin` BECAUSE `H_xik=0`. ON THE QUIET LOW-AMPLITUDE HIGH-JET BRANCH THIS REDUCES TO `D_B H_xin=(Hess kappa)_{xin}-H_xin+o(1)`. THE TRANSVERSE HESSIAN BLOCK SATISFIES THE ANALOGOUS `D_B H_perp=(Hess kappa)_perp-H_perp+o(1)` UP TO VANISHING FRAME/VELOCITY-JET TERMS. THEREFORE ORDER-ONE MIXED OR TRANSVERSE CONVEXITY CAN BE RECHARGED DIRECTLY BY ORDER-ONE SECOND `kappa` JETS. NO EXISTING QUIET STRAIN LEDGER MAKES THOSE NORMALIZED MULTIPLIER JETS SMALL. THE REMAINING GENERIC-FOLD FIREWALL IS THUS ROUTED TO A `kappa`-HESSIAN / NORMALIZED HIGHER-MULTIPLIER-JET BRANCH RATHER THAN FALSELY CLOSED BY DAMPING. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact material equation for `psi=log rho`

On CE-H,

\[
D_B\rho=(\sigma+\kappa-1)\rho.
\]

Therefore

\[
\boxed{
D_B\psi
=\sigma+\kappa-1.
}
\]

Define

\[
\boxed{S:=\sigma+\kappa.}
\]

Then

\[
D_B\psi=S-1.
\]

---

## 2. Exact Hessian commutator

Let

\[
H_\psi:=\nabla^2\psi.
\]

In Cartesian coordinates,

\[
H_{ij}=\partial_{ij}\psi.
\]

For a scalar `f`, the exact second-gradient material commutator is

\[
\boxed{
\begin{aligned}
D_B(\partial_{ij}f)
={}&
\partial_{ij}(D_Bf)
-(\partial_iB_\ell)\partial_{\ell j}f\\
&-(\partial_jB_\ell)\partial_{i\ell}f
-(\partial_{ij}B_\ell)\partial_\ell f.
\end{aligned}
}
\]

Therefore

\[
\boxed{
D_BH_\psi
=
\nabla^2S
-(\nabla B)^TH_\psi
-H_\psi\nabla B
-\mathcal Q_B(\nabla\psi),
}
\]

where the symmetric tensor

\[
\boxed{
[\mathcal Q_B(\nabla\psi)]_{ij}
:=(\partial_{ij}B_\ell)\partial_\ell\psi.
}
\]

This is exact.

---

## 3. Mixed `xi-n` component on the moving pure-kernel frame

Define

\[
\boxed{M_{\xi n}:=H_\psi(\xi,n).}
\]

The pure-kernel material frame satisfies

\[
D_B\xi=0,
\qquad
D_Bn=-\Omega k.
\]

Therefore

\[
D_BM_{\xi n}
=(D_BH_\psi)(\xi,n)
-\Omega H_\psi(\xi,k).
\]

At a director-area tangency M17-148 gives

\[
\boxed{H_\psi(\xi,k)=D_kg=0.}
\]

Hence the frame-rotation correction vanishes exactly at the contact:

\[
\boxed{
D_BM_{\xi n}
=(D_BH_\psi)(\xi,n).
}
\]

---

## 4. Quiet low-amplitude reduction of the velocity-gradient terms

On the M17-147 quiet low-amplitude high-jet hard hull,

\[
\nabla B
=
\frac12I+o(1).
\]

Thus

\[
(\nabla B)^TH_\psi+H_\psi\nabla B
=H_\psi+o(1)
\]

for uniformly bounded normalized Hessian.

With the required higher velocity/strain-jet compactness and bounded normalized `grad psi`,

\[
\mathcal Q_B(\nabla\psi)=o(1).
\]

Also

\[
\nabla^2\sigma=o(1)
\]

under the corresponding strain-jet interpolation hypothesis.

Therefore

\[
\boxed{
D_BH_\psi
=
\nabla^2\kappa-H_\psi+o(1)
}
\]

on the quiet compact branch.

---

## 5. Mixed payer material law

Project Section 4 onto `(xi,n)` at a tangency:

\[
\boxed{
D_BM_{\xi n}
=
(\nabla^2\kappa)_{\xi n}
-M_{\xi n}
+o(1).
}
\]

Thus the mixed Hessian payer has unit damping, but it also has an order-one additive recharge channel:

\[
\boxed{(\nabla^2\kappa)_{\xi n}.}
\]

Consequently a repeated order-one mixed payer does **not** imply backward exponential growth of `M_xin` if the mixed `kappa` Hessian continually replenishes it.

The M17-150 compactness argument cannot be copied without first controlling this source.

---

## 6. Pure transverse Hessian block

Let

\[
P_\perp:=I-\xi\otimes\xi
\]

and define the transverse log-amplitude Hessian

\[
\boxed{
H_\perp:=P_\perp H_\psi P_\perp.
}
\]

Because the transverse frame may rotate, individual `(k,n)` matrix entries acquire skew frame-rotation terms.
Those terms conjugate the block and do not create its spectral size.

On the quiet hard hull, the symmetric material evolution has the schematic exact-leading form

\[
\boxed{
D_BH_\perp
=
(\nabla^2\kappa)_\perp
-H_\perp
+[\text{transverse frame rotation commutator}]
+o(1).
}
\]

The rotation commutator preserves eigenvalues instantaneously to first order because it is a skew conjugation.
Thus the top transverse eigenvalue can be recharged only through the symmetric source

\[
(\nabla^2\kappa)_\perp
\]

up to vanishing hard-hull errors.

Therefore sustained

\[
\lambda_{max}(H_\perp)\gtrsim\frac34
\]

requires an order-one transverse `kappa`-Hessian contribution somewhere in its genealogy unless the convexity is imported from a boundary.

---

## 7. New remaining normalized payer

M17-150 closes indefinite quiet recurrence of

\[
G_{axial}.
\]

M17-151 routes the other two M17-148 payers to

\[
\boxed{
G_{mix}\lor G_{trans}
\Longrightarrow
G_{\nabla^2\kappa}
\lor
G_{boundary/import}
\lor
G_{hard\ exit}
}
\]

in the recurrent quiet compact setting.

Here

\[
G_{\nabla^2\kappa}
\]

means that order-one normalized second derivatives of the CE-H multiplier are required to replenish the log-amplitude Hessian payer against its unit material damping.

---

## 8. Why `nabla^2 kappa` is not already controlled by the M17-145 energy

M17-145 derives the natural energy for

\[
K_\xi=D_\xi\kappa
\]

with weight

\[
\rho^2.
\]

Its diffusion term contains

\[
\int\rho^2|\nabla K_\xi|^2,
\]

which sees some second `kappa` derivatives.

But on the low-amplitude strong-director branch

\[
\rho^2\sim R^{-1},
\qquad
\Phi_J\asymp1,
\]

so an order-one normalized second derivative still has only `O(R^-1)` physical quadratic cost per unit director flux, which is dyadically summable.

Thus no current positive director-flux-weighted budget excludes `G_{nabla^2 kappa}`.

---

## 9. DSD audit

### Audit A — every Hessian component has homogeneous `-1` damping and is therefore closed by M17-150 logic

Rejected.
The additive `Hess kappa` source is order one in the normalized geometry and is not known to vanish.

### Audit B — frame rotation of `(k,n)` is an independent symmetric source of transverse eigenvalue growth

Rejected.
It acts by skew conjugation on the transverse block and does not itself create spectral magnitude.

### Audit C — the quiet strain ledger controls `Hess kappa`

Rejected.
`kappa` is a normalized CE-H multiplier and its jets remain amplitude-scale-free.

### Audit D — `rho^2`-weighted diffusion of `D_xi kappa` controls order-one director-flux frequency of `Hess kappa`

Rejected by the same low-amplitude weight mismatch as M17-145.

### Audit E — the mixed/transverse branches are proved realizable

Rejected.
They are merely routed to a sharper normalized second-multiplier-jet firewall.

---

## 10. Updated generic-fold frontier

Under the quiet low-amplitude high-jet compact hypotheses,

\[
\boxed{
\text{recurrent generic fold}
\Longrightarrow
G_{\nabla^2\kappa}
\lor
G_{boundary/import}
\lor
G_{rank/interface}
\lor
G_{high\ jet}
\lor
H_{1,crit}^{spacetime},
}
\]

because

1. the axial convexity payer cannot recur indefinitely by M17-150;
2. mixed/transverse convexity payers require `kappa`-Hessian recharge by M17-151.

The next honest target is the material equation for the full tensor

\[
\nabla^2\kappa.
\]

A useful result would determine whether its leading quiet dynamics are again homogeneous up to finite normalized `log rho` geometry, or whether a genuinely new third-jet source appears.
That audit decides whether the finite-jet escalation closes or merely moves one derivative upward.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
