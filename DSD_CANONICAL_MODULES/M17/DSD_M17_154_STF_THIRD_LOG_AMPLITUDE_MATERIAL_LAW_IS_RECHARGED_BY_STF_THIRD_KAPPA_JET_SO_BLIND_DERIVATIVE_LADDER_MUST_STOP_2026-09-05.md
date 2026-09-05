# DSD M17-154 — The STF third log-amplitude material law is recharged by the STF third `kappa` jet, so the blind derivative ladder must stop

Date: 2026-09-05  
Canonical ID: **M17-154**

Status: **DERIVATIVE-LADDER AUDIT / M17-153 REDUCES THE NEW THIRD LOG-AMPLITUDE FREEDOM TO THE SEVEN-COMPONENT TENSOR `T0=STF_3(nabla^3 log rho)`. DIFFERENTIATING THE EXACT MATERIAL AMPLITUDE LAW `D_B psi=sigma+kappa-1` THREE TIMES GIVES, ON THE QUIET LOW-AMPLITUDE HIGH-JET HARD HULL, `D_B T0=STF_3(nabla^3 kappa)-(3/2)T0+o(1)`. THUS THE FOLD-VISIBLE STF THIRD JET IS NOT A CLOSED DAMPED STATE: IT IS DIRECTLY RECHARGED BY THE STF THIRD MULTIPLIER JET. DIFFERENTIATING THE M5-682 `kappa` LAW THREE TIMES WOULD IN TURN INTRODUCE FOURTH LOG-AMPLITUDE JETS CONTRACTED WITH LOWER `kappa` JETS. THERE IS NO FINITE TERMINATION FROM DIFFERENTIATION ALONE. DSD AUDIT THEREFORE STOPS THE BLIND `m -> m+1` JET ESCALATION. THE NEXT PROGRESS MUST COME FROM A WHOLE-JET/ANALYTIC-NORM, UNIQUE-CONTINUATION/LIOUVILLE, FLUX-WEIGHTED COERCIVITY, OR OTHER NEW PRINCIPLE THAT CONTROLS THE NORMALIZED JET HIERARCHY AS A UNIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input amplitude law

Set

\[
\psi:=\log\rho.
\]

The exact CE-H amplitude equation is

\[
\boxed{
D_B\psi
=\sigma+\kappa-1.
}
\]

Let

\[
T:=\nabla^3\psi,
\qquad
T^0:=STF_3(T).
\]

M17-153 shows that `T0` contains exactly the seven residual third-log-amplitude components after the scalar CE-H trace is removed.

---

## 2. Exact third-gradient material commutator structure

For a scalar `f`, repeated use of

\[
[D_B,\partial_i]f
=-(\partial_iB_\ell)\partial_\ell f
\]

gives

\[
\boxed{
\begin{aligned}
D_B(\partial_{ijk}f)
={}&
\partial_{ijk}(D_Bf)\\
&-(\partial_iB_a)\partial_{ajk}f
-(\partial_jB_a)\partial_{iak}f
-(\partial_kB_a)\partial_{ija}f\\
&-(\partial_{ij}B_a)\partial_{ak}f
-(\partial_{ik}B_a)\partial_{aj}f
-(\partial_{jk}B_a)\partial_{ia}f\\
&-(\partial_{ijk}B_a)\partial_af.
\end{aligned}
}
\]

This is the exact finite third-order commutator.

---

## 3. Apply to `psi`

Because

\[
D_B\psi=\sigma+\kappa-1,
\]

we obtain

\[
D_BT
=
\nabla^3(\sigma+\kappa)
-\mathcal A_1[T]
-\mathcal A_2[\nabla^2\psi]
-\mathcal A_3[\nabla\psi],
\]

where

- `A1` contains the three first-velocity-gradient actions on the tensor slots;
- `A2` contains second derivatives of `B` times `Hess psi`;
- `A3` contains third derivatives of `B` times `grad psi`.

No derivatives have been omitted; this is only grouped notation for the exact expression in Section 2.

---

## 4. Quiet low-amplitude high-jet reduction

On the same hard hull used in M17-147--153,

\[
\nabla B
=\frac12I+o(1).
\]

Each of the three tensor slots therefore contributes asymptotically `-1/2`, giving total bare damping

\[
-\frac32T.
\]

With sufficiently high explicit strain/velocity-jet compactness,

\[
\nabla^3\sigma=o(1),
\]

and the `A2`, `A3` terms are `o(1)` because the nontrivial velocity derivatives beyond the similarity dilation vanish on the quiet low-amplitude branch.

Hence

\[
\boxed{
D_BT
=
\nabla^3\kappa
-\frac32T
+o(1).
}
\]

Since the Euclidean metric is fixed, the STF projection commutes with this leading tensor equation.
Therefore

\[
\boxed{
D_BT^0
=
STF_3(\nabla^3\kappa)
-\frac32T^0
+o(1).
}
\]

This is the leading material law for the M17-153 seven-component firewall.

---

## 5. Fold-visible component

M17-153 gives at a peak tangency

\[
D_k^2g
=T^0_{kk\xi}
+\frac15t_\xi
+qH_{\xi n}.
\]

Thus the generic-fold-visible component `T0_kkxi` has the same tensor law as the rest of `T0` and can be directly replenished by

\[
\boxed{
[STF_3(\nabla^3\kappa)]_{kk\xi}
}
\]

plus frame-projection terms when one follows the moving `(xi,k,n)` component.

Those frame terms are bounded finite-jet rotations; they do not remove the direct third-`kappa` recharge.

Therefore the M17-150 homogeneous-damping compactness closure again fails at this level unless the third multiplier jet is controlled independently.

---

## 6. What happens if the `kappa` equation is differentiated again

M17-152 already shows the pattern at second order:

\[
D_B\nabla^2\kappa
=\cdots
+2\nabla^3\psi[\nabla\kappa]
+\cdots.
\]

At third order, differentiating

\[
L_\rho\kappa
=\Delta\kappa+2\nabla\psi\cdot\nabla\kappa
\]

produces terms including

\[
\boxed{
\nabla^4\psi[\nabla\kappa]
}
\]

and

\[
\boxed{
\nabla^3\psi[\nabla^2\kappa],
}
\]

in addition to the weighted diffusion of `nabla^3 kappa` and lower products.

Thus controlling

\[
STF_3(\nabla^3\kappa)
\]

by simply differentiating its material equation introduces the fourth normalized log-amplitude jet.

Repeating this step produces the general pattern

\[
\boxed{
\text{order }m\text{ multiplier jet}
\longleftrightarrow
\text{order }m+1\text{ log-amplitude jet}
}
\]

with lower-order couplings.

---

## 7. Why this is a methodological stopping point

A proof strategy that says

1. derive the `m`-jet equation;
2. discover an `(m+1)`-jet source;
3. differentiate again;
4. repeat indefinitely

has not gained coercivity or compactness.
It has only rewritten the same normalized analytic structure at successively higher resolution.

Therefore DSD audit marks the unqualified derivative ladder as

\[
\boxed{\text{NON-CLOSING ROUTE WITHOUT A NEW PRINCIPLE}.}
\]

This is analogous to M17-063, where blind higher differentiation of the principal alignment condition was stopped after it reproduced the same compatibility tower.

---

## 8. What kind of new input would be genuinely different

The next useful principle must control more than one fixed derivative order at a time.
Candidates include:

### A. Analytic/Gevrey whole-jet norm

A generating norm of the schematic form

\[
\mathcal A_\ell
=
\sum_{m\ge0}
\frac{\ell^m}{m!}
\left(
\|\nabla^m\psi\|
+\|\nabla^m\kappa\|
+\|\nabla^m\xi\|
\right)
\]

could in principle absorb the derivative shift if its radius `ell` has a controlled material law.

No such estimate has yet been derived here.

### B. Unique continuation / Liouville rigidity

The normalized elliptic system

\[
\Delta W=\kappa W
\]

plus the material equations may forbid the required recurrent low-amplitude, strong-normalized-jet pattern under a global ancient/remote-tail hypothesis.

### C. Positive director-flux-weighted coercivity

A budget measured directly against

\[
d\Phi_J
\]

rather than `rho^2 dV` could make order-one normalized jets expensive on the actual carrier population.

### D. Finite critical-type closure with a new top-jet invariant

If the analytic critical atlas supplies a materially controlled top jet rather than merely a bounded finite order, the tower could close without taking all derivatives.

None of these inputs is currently established.

---

## 9. DSD audit

### Audit A — `T0` has homogeneous `-3/2` damping and is therefore closed

Rejected.
`STF_3(nabla^3 kappa)` is an additive normalized recharge.

### Audit B — continue differentiating until the source vanishes

Rejected as an unproved assumption. The weighted diffusion has variable coefficients `grad log rho`, so each derivative generates a higher `psi` jet.

### Audit C — analyticity automatically bounds the whole ladder strongly enough

Rejected.
Analyticity supplies local derivative bounds once an analytic radius/norm is controlled; no uniform material analytic-radius estimate has yet been proved for this branch.

### Audit D — the stopping audit proves the branch survives Navier--Stokes

Rejected.
It only identifies why the current derivative-by-derivative method does not close it.

---

## 10. Updated methodological frontier

The chain M17-143--154 has achieved the following:

\[
\boxed{
\begin{aligned}
\text{frequent quiet geometry transition}
&\Rightarrow
\text{generic-fold multiplier gradient or other exits},\\
\text{generic fold}
&\Rightarrow
\text{log-amplitude Hessian }3/4\text{ gate},\\
\text{axial payer}
&\Rightarrow
\text{closed as indefinitely recurrent quiet mechanism},\\
\text{mixed/transverse payer}
&\Rightarrow
\nabla^2\kappa\text{ recharge},\\
\nabla^2\kappa\text{ recharge}
&\Rightarrow
STF_3(\nabla^3\log\rho)\text{ firewall},\\
STF_3(\nabla^3\log\rho)
&\Rightarrow
STF_3(\nabla^3\kappa)\text{ recharge}.
\end{aligned}
}
\]

The last line shows that **blind higher differentiation no longer counts as progress**.

The highest-value next gate is therefore a whole-jet or global rigidity estimate, not M17-155 = “differentiate one more time.”

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
