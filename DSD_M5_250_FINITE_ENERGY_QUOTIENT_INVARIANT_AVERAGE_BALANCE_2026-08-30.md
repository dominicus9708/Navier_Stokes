# DSD M5-250 — Finite-Energy Quotient Invariant-Average Balance

Date: 2026-08-30

Parent: `DSD_M5_249_POSITIVE_WITNESS_VS_ESCAPE_THRESHOLD_GAP_AUDIT_2026-08-30.md`

Status: **EXACT RELATIVE-ENERGY REDUCTION / AFTER SUBTRACTING A DIVERGENCE-FREE CANONICAL TAIL EXTENSION, THE FINITE-ENERGY QUOTIENT HAS A GLOBAL L2 ENERGY IDENTITY; BACKWARD-LERAY SCALING CONTRIBUTES AN ANTI-DAMPING TERM `-E/4`, SO THE QUOTIENT ENERGY IS NOT A LYAPUNOV FUNCTION BY ITSELF; ON A COMPACT RECURRENT HULL THE TIME DERIVATIVE AVERAGES TO ZERO AND EVERY SURVIVOR MUST SATISFY ONE EXACT THREE-PAYER BALANCE: VISCOSITY VERSUS LERAY ANTI-DAMPING, BACKGROUND-STRAIN WORK, AND CANONICAL-TAIL RESIDUAL WORK / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Let `V(Y,s)` be a smooth W1 Leray trajectory on the current spatial-Type-I corridor,

\[
V_s-\nu\Delta V+\frac12V+\frac12(Y\cdot\nabla)V+(V\cdot\nabla)V+\nabla P=0,
\qquad \nabla\cdot V=0.
\]

Choose a divergence-free canonical-tail extension `B(Y,s)` which agrees with the canonical critical tail outside a fixed transition annulus and is smooth on the whole space.

Define

\[
\boxed{Q:=V-B.}
\]

On the audited same-tail corridor the construction is chosen so that

\[
\boxed{Q\in L^2(\mathbb R^3)\cap L^3(\mathbb R^3),\qquad \nabla Q\in L^2(\mathbb R^3).}
\]

Define the projected defect of the extension by

\[
\boxed{
R_B
:=
B_s-\nu\Delta B+\frac12B+\frac12(Y\cdot\nabla)B
+\mathbb P\nabla\cdot(B\otimes B).
}
\]

The transition-annulus cutoff errors are included in `R_B`; no claim is made that `B` itself is an exact Leray solution.

---

## 2. Exact quotient equation

Subtract the equation for `B` from the Leray equation for `V=B+Q` and apply the Leray projector. Then

\[
\boxed{
Q_s-\nu\Delta Q
+\frac12Q+\frac12(Y\cdot\nabla)Q
+\mathbb P\nabla\cdot
\bigl(B\otimes Q+Q\otimes B+Q\otimes Q\bigr)
=-R_B.
}
\]

Equivalently, before projection and modulo the relative pressure `pi`,

\[
Q_s-\nu\Delta Q
+\frac12Q+\frac12(Y\cdot\nabla)Q
+(B\cdot\nabla)Q
+(Q\cdot\nabla)B
+(Q\cdot\nabla)Q
+\nabla\pi
=-R_B.
\]

---

## 3. Global L2 pairing

Set

\[
E_Q(s):=\|Q(s)\|_2^2,
\qquad
D_Q(s):=\|\nabla Q(s)\|_2^2.
\]

Pair the quotient equation with `Q`.

Because `div Q=div B=0`,

\[
\int (B\cdot\nabla Q)\cdot Q=0,
\]

\[
\int (Q\cdot\nabla Q)\cdot Q=0,
\]

and the pressure pairing vanishes.

For the background-gradient term,

\[
\int (Q\cdot\nabla B)\cdot Q
=
\int Q^T S_B Q,
\]

where

\[
S_B:=\frac12(\nabla B+\nabla B^T).
\]

The Leray linear term has the exact sign

\[
\begin{aligned}
\int \left(\frac12Q+\frac12Y\cdot\nabla Q\right)\cdot Q
&=\frac12E_Q+\frac14\int Y\cdot\nabla |Q|^2\\
&=\frac12E_Q-\frac34E_Q\\
&=\boxed{-\frac14E_Q}.
\end{aligned}
\]

Thus

\[
\boxed{
\frac12E_Q'(s)
+\nu D_Q(s)
-\frac14E_Q(s)
+\int_{\mathbb R^3}Q^TS_BQ\,dY
=-\langle R_B,Q\rangle.
}
\]

Status: **EXACT**, under the already audited global `L2/H1` quotient regularity and standard cutoff approximation for the integration by parts.

---

## 4. The main sign correction

It is tempting to claim that subtracting the critical tail leaves a dissipative finite-energy equation.

That is false because the backward-Leray drift contributes

\[
\boxed{-\frac14E_Q.}
\]

Therefore even with

\[
S_B=0,
\qquad R_B=0,
\]

the energy relation would be

\[
\frac12E_Q'+\nu D_Q-\frac14E_Q=0,
\]

which is not a monotone decay identity on `R3`.

There is no whole-space Poincare inequality of the form

\[
D_Q\ge cE_Q.
\]

Hence

\[
\boxed{
Q\in L^2\cap H^1
\not\Rightarrow
\text{strict quotient-energy Lyapunov decay}.
}
\]

This is a required firewall.

---

## 5. Invariant-average balance on the compact recurrent hull

On the compact recurrent W1 hull, the quotient construction is canonical once the tail extension convention is fixed. The scalar `E_Q` is therefore a bounded continuous state observable on the audited strong quotient topology.

Let `mu` be any invariant probability measure supported on the recurrent hull. Then the average of the derivative of the bounded state observable vanishes:

\[
\boxed{\langle E_Q'\rangle_\mu=0.}
\]

Averaging the exact identity gives

\[
\boxed{
\nu\langle D_Q\rangle
-\frac14\langle E_Q\rangle
+\left\langle\int Q^TS_BQ\right\rangle
=-\langle\langle R_B,Q\rangle\rangle.
}
\]

Equivalently,

\[
\boxed{
\nu\langle D_Q\rangle
=
\frac14\langle E_Q\rangle
-\left\langle\int Q^TS_BQ\right\rangle
-\langle\langle R_B,Q\rangle\rangle.
}
\]

This is the exact quotient master balance.

---

## 6. Three payer channels

Define

\[
\mathcal A_Q:=\frac14E_Q,
\]

\[
\mathcal S_Q:=-\int Q^TS_BQ,
\]

and

\[
\mathcal R_Q:=-\langle R_B,Q\rangle.
\]

Then

\[
\boxed{
\nu\langle D_Q\rangle
=
\langle\mathcal A_Q+\mathcal S_Q+\mathcal R_Q\rangle.
}
\]

Interpretation:

1. `A_Q`: backward-Leray anti-damping payment;
2. `S_Q`: energy extracted from compressive directions of the canonical-tail strain;
3. `R_Q`: work of the stationary/tail-cutoff residual on the finite-energy quotient.

The first payer is intrinsic to similarity coordinates and is not a physical external force.

The latter two are genuine coupling channels.

---

## 7. A rigorous finite partition when quotient dissipation is positive

Suppose

\[
\langle D_Q\rangle>0.
\]

Then

\[
\langle\mathcal A_Q+\mathcal S_Q+\mathcal R_Q\rangle
=\nu\langle D_Q\rangle>0.
\]

Hence at least one payer satisfies

\[
\boxed{
\langle\mathcal A_Q\rangle
\ge\frac\nu3\langle D_Q\rangle,
}
\]

or

\[
\boxed{
\langle\mathcal S_Q\rangle
\ge\frac\nu3\langle D_Q\rangle,
}
\]

or

\[
\boxed{
\langle\mathcal R_Q\rangle
\ge\frac\nu3\langle D_Q\rangle.
}
\]

This is only a payer classification; none of the three inequalities is yet a contradiction.

---

## 8. Anti-damping-dominant branch

If

\[
\frac14\langle E_Q\rangle
\ge\frac\nu3\langle D_Q\rangle,
\]

then

\[
\boxed{
\frac{\langle D_Q\rangle}{\langle E_Q\rangle}
\le\frac{3}{4\nu}.
}
\]

Thus this branch is a **low mean quotient-frequency** branch.

This is useful because the repository already contains lower-frequency constraints generated by localization/tightness/Dirichlet structure. The next audit should compare the same normalization before claiming incompatibility.

---

## 9. Strain-work-dominant branch

If

\[
-\left\langle\int Q^TS_BQ\right\rangle
\ge\frac\nu3\langle D_Q\rangle,
\]

then the finite-energy quotient must spend positive measure in compressive spectral sectors of `S_B`.

This is structurally similar to M5-232, but `Q` is a genuine finite-energy global mode rather than a finite-dilate tail difference.

The safe estimate is

\[
\left|\int Q^TS_BQ\right|
\le
\int |S_B||Q|^2.
\]

On the critical far field `|S_B|\lesssim |Y|^{-2}`, Hardy gives

\[
\int_{|Y|>R}|S_B||Q|^2
\lesssim C_B\int \frac{|Q|^2}{|Y|^2}
\le4C_B\|\nabla Q\|_2^2.
\]

This is critical and has no smallness for arbitrary `C_B`. Therefore the strain payer is a genuine large-critical channel, not an automatic contradiction.

---

## 10. Residual-work-dominant branch

If

\[
-\langle\langle R_B,Q\rangle\rangle
\ge\frac\nu3\langle D_Q\rangle,
\]

then the canonical-tail residual does positive average work on the finite-energy quotient.

This is stronger than merely

\[
\|R_B\|_{H^{-1}}>0,
\]

because it fixes the sign of the actual relative-energy pairing.

However Cauchy--Schwarz/duality only gives

\[
|\langle R_B,Q\rangle|
\le
\|R_B\|_{H^{-1}}\|Q\|_{H^1},
\]

so a residual norm floor alone does not force this branch. The sign-correlated work is a separate formed observable.

---

## 11. Zero-dissipation endpoint

If

\[
\langle D_Q\rangle=0,
\]

then invariance and nonnegativity imply

\[
D_Q=0
\]

for `mu`-almost every state. Since `Q\in L2(R3)` and `grad Q=0`,

\[
\boxed{Q=0.}
\]

Thus the recurrent state equals its canonical tail extension almost everywhere.

For a smooth whole-space W1 state and a genuine `1/r` critical tail, this can occur only if the extension itself is globally admissible and solves the full equation; otherwise the transition/core mismatch prevents `Q=0`.

Therefore a nontrivial recurrent quotient branch has

\[
\boxed{\langle D_Q\rangle>0.}
\]

subject to the canonical-extension nondegeneracy just stated.

---

## 12. DSD verdict

### PROVED

The canonical-tail subtraction yields the exact global finite-energy balance

\[
\boxed{
\frac12E_Q'
+\nu D_Q
-\frac14E_Q
+\int Q^TS_BQ
=-\langle R_B,Q\rangle.
}
\]

On any invariant recurrent measure,

\[
\boxed{
\nu\langle D_Q\rangle
=
\frac14\langle E_Q\rangle
-\left\langle\int Q^TS_BQ\right\rangle
-\langle\langle R_B,Q\rangle\rangle.
}
\]

### FIREWALL

Finite energy after tail subtraction does **not** create a strict Lyapunov function because backward-Leray scaling contributes `-E_Q/4` and whole-space Poincare is unavailable.

### NEW FINITE FORK

Every nontrivial recurrent quotient must pay its mean dissipation through at least one of

\[
\boxed{
\text{low-frequency anti-damping}
\lor
\text{compressive tail-strain work}
\lor
\text{positive residual work}.
}
\]

---

## 13. Next target

The strongest immediate opportunity is to compare the anti-damping branch

\[
\frac{\langle D_Q\rangle}{\langle E_Q\rangle}
\le\frac{3}{4\nu}
\]

with already proved quotient/localization Dirichlet-frequency lower bounds in the same normalization.

If that interval is empty, the anti-damping payer closes and only the two genuinely critical correlation channels remain.

If it is not empty, record the surviving quotient-frequency window and proceed to the signed strain/residual-work branches separately.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
