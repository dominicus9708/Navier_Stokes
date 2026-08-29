# DSD M5-254 — Relative-Vorticity Recurrent H1 Tax and Frequency Chain

Date: 2026-08-30

Parent: `DSD_M5_253_QUOTIENT_COMPRESSIVE_HARDY_STRAIN_THRESHOLD_2026-08-30.md`

Status: **EXACT RELATIVE-VORTICITY H1 BALANCE / THE FINITE-ENERGY QUOTIENT'S RELATIVE VORTICITY HAS THE POSITIVE BACKWARD-LERAY ENSTROPHY TAX `+Z_eta/4`, IN CONTRAST TO THE VELOCITY-LEVEL `-E_Q/4` ANTI-DAMPING / FOURIER INTERPOLATION LINKS THE TWO LEVELS BY `P_eta/Z_eta >= Z_eta/E_Q` AFTER INVARIANT AVERAGING / THE NEW H1 TAX MUST BE PAID BY TOTAL-STRAIN STRETCHING, TAIL-VORTICITY/QUOTIENT CROSS COUPLING, OR CURL-RESIDUAL WORK / GLOBAL REGULARITY UNPROVED.**

---

## 1. Fields

Use

\[
V=B+Q,
\qquad
\Omega=\zeta+\eta,
\]

where

\[
\zeta:=\nabla\times B,
\qquad
\eta:=\nabla\times Q.
\]

Let

\[
S_V:=\operatorname{sym}\nabla V,
\qquad
S_B:=\operatorname{sym}\nabla B,
\qquad
S_Q:=\operatorname{sym}\nabla Q.
\]

The quotient equation is

\[
Q_s-\nu\Delta Q
+\frac12Q+\frac12(Y\cdot\nabla)Q
+(B\cdot\nabla)Q+(Q\cdot\nabla)B
+(Q\cdot\nabla)Q+\nabla\pi
=-R_B.
\]

---

## 2. Exact relative-vorticity equation

Take curl.

The Leray linear term satisfies

\[
\nabla\times\left(\frac12Q+\frac12Y\cdot\nabla Q\right)
=
\eta+\frac12Y\cdot\nabla\eta.
\]

Using the full vorticity identity for the cross nonlinearities gives

\[
\boxed{
\begin{aligned}
\eta_s-\nu\Delta\eta
+\eta+\frac12(Y\cdot\nabla)\eta
&+(B\cdot\nabla)\eta
+(Q\cdot\nabla)\eta\\
&-(\eta\cdot\nabla)B
-(\eta\cdot\nabla)Q\\
&+(Q\cdot\nabla)\zeta
-(\zeta\cdot\nabla)Q
=-\nabla\times R_B.
\end{aligned}
}
\]

No cross term has been discarded.

---

## 3. Relative enstrophy identity

Define

\[
Z_\eta:=\|\eta\|_2^2,
\qquad
P_\eta:=\|\nabla\eta\|_2^2.
\]

Pair the equation with `eta`.

The divergence-free transports vanish:

\[
\int\eta\cdot(B\cdot\nabla)\eta=0,
\qquad
\int\eta\cdot(Q\cdot\nabla)\eta=0.
\]

The Leray linear term gives

\[
\int\eta\cdot\left(\eta+\frac12Y\cdot\nabla\eta\right)
=\boxed{\frac14Z_\eta}.
\]

The two stretching terms combine to

\[
\int\eta^T(S_B+S_Q)\eta
=\int\eta^TS_V\eta.
\]

Define the tail-cross term

\[
\boxed{
\mathcal C_{B,Q}
:=
\int
\eta\cdot
\left[(Q\cdot\nabla)\zeta-(\zeta\cdot\nabla)Q\right]dY.
}
\]

Define curl-residual work

\[
\boxed{
\mathcal R_\eta
:=-\left\langle\nabla\times R_B,\eta\right\rangle.
}
\]

Then the exact identity is

\[
\boxed{
\frac12Z_\eta'
+\nu P_\eta
+\frac14Z_\eta
=
\int\eta^TS_V\eta
-\mathcal C_{B,Q}
+\mathcal R_\eta.
}
\]

Status: **EXACT** under the strong relative-vorticity regularity needed for the pairing; otherwise it is first read in the standard localized/approximation form.

---

## 4. Invariant-average H1 tax

On an invariant recurrent measure for which `Z_eta` is a bounded state observable,

\[
\langle Z_\eta'\rangle=0.
\]

Hence

\[
\boxed{
\nu\langle P_\eta\rangle
+\frac14\langle Z_\eta\rangle
=
\left\langle\int\eta^TS_V\eta\right\rangle
-\langle\mathcal C_{B,Q}\rangle
+\langle\mathcal R_\eta\rangle.
}
\]

Thus the relative-vorticity recurrent state must pay a **positive H1 tax**.

This contrasts with the velocity quotient identity

\[
\frac12E_Q'+\nu Z_\eta-\frac14E_Q+\cdots=\cdots,
\]

where the similarity term is anti-damping.

---

## 5. Exact two-level frequency chain

M5-252 proves

\[
E_Q=\|\eta\|_{\dot H^{-1}}^2,
\qquad
Z_\eta=D_Q=\|\eta\|_2^2.
\]

For every fixed time, Fourier Cauchy--Schwarz gives

\[
\left(\int|\widehat\eta|^2\right)^2
\le
\left(\int|\xi|^{-2}|\widehat\eta|^2\right)
\left(\int|\xi|^2|\widehat\eta|^2\right).
\]

Therefore

\[
\boxed{
Z_\eta^2\le E_QP_\eta.
}
\]

Apply Cauchy--Schwarz to the invariant averages:

\[
\langle Z_\eta\rangle^2
\le
\langle E_Q\rangle\langle P_\eta\rangle.
\]

Thus

\[
\boxed{
\frac{\langle P_\eta\rangle}
{\langle Z_\eta\rangle}
\ge
\frac{\langle Z_\eta\rangle}
{\langle E_Q\rangle}.
}
\]

Define

\[
\boxed{
\lambda_0
:=
\frac{\langle Z_\eta\rangle}
{\langle E_Q\rangle},
\qquad
\lambda_1
:=
\frac{\langle P_\eta\rangle}
{\langle Z_\eta\rangle}.
}
\]

Then

\[
\boxed{\lambda_1\ge\lambda_0.}
\]

This is an exact same-field frequency chain.

---

## 6. Consequence on the M5-250 anti-damping branch

Anti-damping dominance gives

\[
\boxed{\lambda_0\le\frac{3}{4\nu}.}
\]

The H1 interpolation gives only

\[
\lambda_1\ge\lambda_0,
\]

which does **not** by itself contradict the upper bound on `lambda_0`.

Thus the existence of the H1 tax alone does not close the anti-damping branch.

A closure requires an upper estimate on the H1 production side, or a lower estimate on `lambda_0` strong enough to cross `3/(4nu)`.

---

## 7. Finite H1 payer fork

Since

\[
\nu\langle P_\eta\rangle
+\frac14\langle Z_\eta\rangle>0
\]

for a nonzero relative vorticity, at least one of the three right-hand channels must be positive and quantitatively significant:

1. total-strain stretching
   \[
   \left\langle\int\eta^TS_V\eta\right\rangle;
   \]
2. tail-vorticity/quotient cross coupling
   \[
   -\langle\mathcal C_{B,Q}\rangle;
   \]
3. curl-residual work
   \[
   \langle\mathcal R_\eta\rangle.
   \]

For example, one of them is at least one third of

\[
\nu\langle P_\eta\rangle+\frac14\langle Z_\eta\rangle.
\]

This is the relative-vorticity analogue of the M5-250 three-payer split.

---

## 8. Safe amplitude bounds and their limitation

The strain term has the elementary bound

\[
\int\eta^TS_V\eta
\le
\|\lambda_{\max}^+(S_V)\|_\infty Z_\eta.
\]

The cross term obeys schematically, when the indicated coefficients are bounded,

\[
\left|\int\eta\cdot(\zeta\cdot\nabla)Q\right|
\le
\|\zeta\|_\infty Z_\eta,
\]

because

\[
\|\nabla Q\|_2=\|\eta\|_2.
\]

Also

\[
\left|\int\eta\cdot(Q\cdot\nabla)\zeta\right|
\le
\|\nabla\zeta\|_\infty
E_Q^{1/2}Z_\eta^{1/2}.
\]

The last term becomes large when `lambda_0=Z_eta/E_Q` is small:

\[
E_Q^{1/2}Z_\eta^{1/2}
=
\frac{Z_\eta}{\sqrt{Z_\eta/E_Q}}.
\]

Hence the anti-damping low-frequency branch naturally weakens direct control of the tail-cross coupling. This is a genuine mechanism, not an algebraic defect.

---

## 9. Relation to the earlier total-field H0/H1 recurrence tax

The repository already contains an H0/H1 recurrence tax for the **total Leray field**.

The present identity is different:

- it applies to the finite-energy **relative** vorticity `eta`;
- it contains canonical-tail cross terms and residual work;
- its low frequency `lambda_0` is exactly the M5-250 quotient frequency.

Therefore the two hierarchies complement each other but are not silently identified.

---

## 10. DSD verdict

### PROVED

\[
\boxed{
\frac12Z_\eta'
+\nu P_\eta
+\frac14Z_\eta
=
\int\eta^TS_V\eta
-\mathcal C_{B,Q}
+\mathcal R_\eta.
}
\]

and on recurrent averages

\[
\boxed{\lambda_1\ge\lambda_0.}
\]

### IMPORTANT SIGN STRUCTURE

- velocity quotient level: `-E_Q/4` anti-damping;
- relative-vorticity level: `+Z_eta/4` damping tax.

### NOT YET A CONTRADICTION

The H1 tax can be paid by strain, tail-cross coupling, or curl-residual work.

### NEXT TARGET

The anti-damping branch should now be tested against the **tail-cross term**. Its dangerous component scales like

\[
\|\nabla\zeta\|_\infty/\sqrt{\lambda_0}.
\]

Thus either `lambda_0` cannot be too small, or the canonical tail must carry a large derivative coefficient. This creates a promising low-frequency-versus-tail-H2 dichotomy in the same relative hierarchy.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
