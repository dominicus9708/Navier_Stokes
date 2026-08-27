# DSD M5-102 — Mellin Uniform Strict Payer Surplus

Date: 2026-08-27

Status: **MELLIN ENDPOINT BYPASS / COMBINING THE HOMOGENEOUS-WEIGHT TRACE-FREE DOMINATION WITH THE INDEPENDENT RECURRENCE-FORCED UPSTROKE YIELDS A QUANTITATIVE STRICT PRESSURE-PAYER SURPLUS / FOR `1<alpha<3/2`, EVERY POSITIVE MELLIN UPSTROKE SATISFIES `E_surplus >= 4 nu (3/(2alpha)-1) X_alpha` / EXACT MINIMAL-PAYER SATURATION IS REMOVED FROM THIS ALTERNATIVE ROUTE WITHOUT R1/R2 / FINITE-BUDGET OR CRITICAL-TAIL ABSORPTION STILL OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inputs

Fix

\[
1<\alpha<\frac32,
\qquad
c_\alpha:=\frac{3}{2\alpha}>1.
\]

M5-100 gives

\[
\boxed{A_\alpha\ge c_\alpha T_\alpha.}
\]

M5-101 independently supplies preterminal intervals on the standard ancient cell where

\[
\boxed{X_\alpha>0.}
\]

No endpoint conclusion was used to construct these intervals.

---

# 2. Extend the M5-83 square decomposition

For truncated Mellin weights, M5-83 gives exactly

\[
\mathcal E
=C+H,
\qquad C\ge0,
\]

with

\[
H
=\frac{[\nu T-(\nu B+X)]^2}{T},
\qquad
B=A+G.
\]

M5-100 established the finite-integral cutoff passage for the homogeneous weight.
Therefore in the Mellin limit define

\[
\boxed{
\mathcal E_\alpha
:=S_{comp,\alpha}
-4\nu^2(A_\alpha+G_\alpha)
-4\nu X_\alpha
\ge0,
}
\]

and retain

\[
\boxed{
\mathcal E_\alpha
=C_\alpha+H_\alpha,
}
\]

where

\[
\boxed{
H_\alpha
=\frac{
[\nu T_\alpha-(\nu(A_\alpha+G_\alpha)+X_\alpha)]^2
}{T_\alpha}.
}
\]

If `T_alpha=0`, the pressure crossing vanishes and a positive `X_alpha` is impossible from the ledger, so the positive-upstroke case always has `T_alpha>0`.

---

# 3. Insert trace-free domination

Since

\[
A_\alpha+G_\alpha
\ge c_\alpha T_\alpha,
\]

we have on an upstroke `X_alpha>=0`

\[
\nu(A_\alpha+G_\alpha)+X_\alpha-\nu T_\alpha
\ge
\nu(c_\alpha-1)T_\alpha+X_\alpha.
\]

Hence

\[
\boxed{
H_\alpha
\ge
\frac{
[\nu(c_\alpha-1)T_\alpha+X_\alpha]^2
}{T_\alpha}.
}
\]

Let

\[
a_\alpha:=\nu(c_\alpha-1)>0.
\]

Then

\[
\frac{(a_\alpha T+X)^2}{T}
=a_\alpha^2T+2a_\alpha X+\frac{X^2}{T}.
\]

By AM--GM,

\[
a_\alpha^2T+\frac{X^2}{T}
\ge2a_\alpha X.
\]

Therefore

\[
\boxed{
H_\alpha
\ge4a_\alpha X_\alpha
=4\nu\left(\frac{3}{2\alpha}-1\right)X_\alpha.
}
\]

Since `C_alpha>=0`, the total surplus obeys

\[
\boxed{
\mathcal E_\alpha
\ge
4\nu\left(\frac{3}{2\alpha}-1\right)X_\alpha.
}
\]

This is the central new estimate.

---

# 4. Exact endpoint is impossible on every positive Mellin upstroke

If minimal-payer saturation occurred, then

\[
\mathcal E_\alpha=0.
\]

But on the M5-101 upstroke

\[
X_\alpha>0
\]

and the coefficient is strictly positive for `alpha<3/2`.
Therefore

\[
\boxed{
\mathcal E_\alpha>0.
}
\]

Hence

\[
\boxed{
\text{positive Mellin upstroke}
\Rightarrow
\text{strict payer surplus},
}
\]

with no exact-endpoint branch.

R1/R2 geometry is not needed for this alternative observable.

---

# 5. Robust interval form

M5-101 gives, after shrinking one smooth upstroke segment,

\[
X_\alpha\ge x_*>0.
\]

Then throughout that interval

\[
\boxed{
\mathcal E_\alpha
\ge
\varepsilon_\alpha^*
:=4\nu\left(\frac{3}{2\alpha}-1\right)x_*>0.
}
\]

Thus the strict surplus is an interval property, not merely an isolated equality-case rejection.

Integrating on any interval where `X_alpha>=0` gives

\[
\boxed{
\int_I\mathcal E_\alpha d\sigma
\ge
4\nu\left(\frac{3}{2\alpha}-1\right)
[\mathfrak E_\alpha(\sigma_2)-\mathfrak E_\alpha(\sigma_1)].
}
\]

This is a genuine positive loop-segment cost, although no finite total budget is claimed.

---

# 6. Scaling audit

Under standard Navier--Stokes scaling

\[
V_\Lambda(x,t)=\Lambda V(\Lambda x,\Lambda^2t),
\]

we have

\[
\mathfrak E_\alpha\mapsto
\Lambda^{\alpha-1}\mathfrak E_\alpha,
\]

and

\[
X_\alpha,
A_\alpha,
T_\alpha,
G_\alpha,
S_\alpha,
\mathcal E_\alpha
\mapsto
\Lambda^{\alpha+1}
(\cdot).
\]

Therefore the time-integrated surplus on one scaled event has degree

\[
\boxed{\gamma=\alpha-1>0.}
\]

This is supercritical with respect to terminal scale depth: smaller-scale copies carry increasing raw cost.

However M5-61's audit remains binding:

\[
\boxed{
\gamma>0
\not\Rightarrow
\text{contradiction without an independent finite upper budget}.
}
\]

No such budget is inserted here.

---

# 7. DSD four-chain audit

## Formation

The Mellin-weight pressure payer and all formation/crossing channels are finite formed objects by M5-100.

**GREEN.**

## Axis

`A`, `T`, and `G` retain their prior typed roles. The sharp `3/2` trace-free coefficient is a relation between already formed channels, not a new channel.

**GREEN.**

## Static aggregation

The surplus decomposition is an exact square decomposition. The lower bound uses only `A>=cT`, `G>=0`, and `X>=0`.
No recurrence is used inside the statewise estimate.

**GREEN.**

## Dynamics

Recurrence enters only through the already independent M5-101 construction of positive upstroke intervals and their scaled copies.

**GREEN.**

---

# 8. Cross-audit and mainline consequence

The new acyclic route is

\[
\boxed{
W1\text{ recurrence}
\to
\text{Mellin upstroke}
\to
\text{trace-free domination}
\to
\text{uniform strict surplus}.
}
\]

There is no arrow back from the strict surplus to recurrence or weight formation.

Therefore the **exact positive-G endpoint rigidity problem is bypassed on this alternative observable**.

This does not prove that the old narrow-band exact endpoint cannot exist as a mathematical state. It means the mainline no longer needs to use that observable: one may choose the Mellin weight and enter directly into the strict-surplus branch.

---

# 9. Updated next gate

The remaining problem is now cleaner:

\[
\boxed{
\text{Can the recurrent/supercritical Mellin payer surplus be connected to}
\quad
\text{(i) the critical K-tail defect,}
\quad
\text{(ii) a finite physical budget, or}
\quad
\text{(iii) a direct statewise absorption theorem?}
}
\]

The natural next audit is the limit

\[
\alpha\downarrow1,
\qquad p=\alpha+2\downarrow3,
\]

because the W1 critical cubic residue is already an Abel/Mellin `p->3+` boundary quantity.
This may connect the new strict-surplus family directly to Issue #2's critical K-tail endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
