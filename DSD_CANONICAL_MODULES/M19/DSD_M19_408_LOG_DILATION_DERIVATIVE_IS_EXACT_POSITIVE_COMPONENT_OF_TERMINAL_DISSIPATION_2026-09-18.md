# M19-408 — Log-dilation derivative is an exact positive component of terminal dissipation, not an independent new payer

Date: 2026-09-18

Status: **EXACT TERMINAL ENERGY DECOMPOSITION / M19-407 FORCES POSITIVE MEAN LOG-DILATION DERIVATIVE ON EVERY NONTRIVIAL SMOOTH ZERO-FORCE STATIONARY RECURRENT TAIL. M5-583 DEFINES THE TERMINAL SCALE-NORMALIZED DISSIPATION AS \`D_A=|(partial_q-1)A|^2+|grad_S A|^2\`. ERGODIC Q-AVERAGING KILLS THE CROSS TERM \`A·partial_qA\`, GIVING THE EXACT ORTHOGONAL MEAN SPLIT \`<D_A>=<|A|^2>+<|grad_S A|^2>+<|partial_qA|^2>\`. THEREFORE THE NEW DILATION-DERIVATIVE CURRENCY IS ALREADY PART OF THE TERMINAL DISSIPATION LEDGER AND MUST NOT BE COUNTED AS AN INDEPENDENT SECOND PAYER. COMBINED WITH M5-575/M5-583, NONTRIVIAL ZERO-FORCE LOG-DILATION RECURRENCE FORCES THE ENERGY-FLUX/INTERIOR-RESIDUAL SIDE TO PAY THIS EXTRA STRICTLY POSITIVE DILATION COMPONENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal dissipation from M5-583

At terminal wedge depth

\[
z=0,
\]

write

\[
u=r^{-1}A(q,\omega),
\qquad
q=\log r.
\]

M5-583 gives the scale-normalized gradient dissipation density

\[
\boxed{
\mathcal D_A
=
|(\partial_q-1)A|^2
+
|\nabla_{S^2}A|^2.
}
\]

Define the invariant \(q\)-mean, including the sphere integral, by

\[
\langle X\rangle
:=
\left\langle
\int_{S^2}X(q,\omega)\,d\omega
\right\rangle_q.
\]

---

## 2. Expand the radial-log part

Pointwise,

\[
|(\partial_q-1)A|^2
=
|\partial_qA|^2
+
|A|^2
-
2A\cdot\partial_qA.
\]

But

\[
2A\cdot\partial_qA
=
\partial_q|A|^2.
\]

On a translation-invariant recurrent mean,

\[
\boxed{
\left\langle
\partial_q|A|^2
\right\rangle
=0.
}
\]

Therefore

\[
\boxed{
\left\langle
|(\partial_q-1)A|^2
\right\rangle
=
\left\langle
|\partial_qA|^2
\right\rangle
+
\left\langle
|A|^2
\right\rangle.
}
\]

---

## 3. Exact mean dissipation decomposition

Substitute into the terminal dissipation:

\[
\boxed{
\langle\mathcal D_A\rangle
=
\left\langle
|\partial_qA|^2
\right\rangle
+
\left\langle
|A|^2
\right\rangle
+
\left\langle
|\nabla_{S^2}A|^2
\right\rangle.
}
\]

Define

\[
D_q
:=
\left\langle
\int_{S^2}|\partial_qA|^2d\omega
\right\rangle_q,
\]

\[
E_A
:=
\left\langle
\int_{S^2}|A|^2d\omega
\right\rangle_q,
\]

and

\[
D_S
:=
\left\langle
\int_{S^2}|\nabla_{S^2}A|^2d\omega
\right\rangle_q.
\]

Then

\[
\boxed{
\langle\mathcal D_A\rangle
=
D_q+E_A+D_S.
}
\]

All three terms are nonnegative.

---

## 4. Consequence of M19-407

M19-407 proves that on a nontrivial smooth stationary zero-force recurrent component,

\[
\boxed{
D_q>0.
}
\]

Therefore

\[
\boxed{
\langle\mathcal D_A\rangle
>
E_A+D_S.
}
\]

The strict excess above the homogeneous angular/base contribution is exactly the genuine log-dilation dynamics.

Thus zero-force recurrence is not “almost homogeneous for free”; it carries a strict positive dilation share of the terminal dissipation.

---

## 5. Combine with the terminal energy payer identity

M5-575/M5-583 give

\[
\boxed{
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle_q.
}
\]

Hence

\[
\boxed{
D_q+E_A+D_S
=
\langle\Phi_E\rangle
+
\langle A\cdot C\rangle.
}
\]

Here \(C=\partial_zF|_{z=0}\) is the first interior wedge coefficient.

Thus any nontrivial smooth zero-force recurrent stationary tail requires the energy-flux/interior-response side to pay not only the base/angular terminal dissipation but also the strictly positive log-dilation component \(D_q\).

---

## 6. Double-counting firewall

The previous section does **not** give two independent payers

\[
\mathcal D_A
\quad\text{and}\quad
D_q.
\]

They satisfy

\[
D_q\le\langle\mathcal D_A\rangle
\]

and \(D_q\) is literally one summand of the same terminal derivative energy.

Therefore

\[
\boxed{
D_q>0
\text{ must not be added on top of }
\mathcal D_A
\text{ as a separate cumulative cost.}
}
\]

The value of M19-407 is structural:

- exact homogeneous zero-force states have \(D_q=0\) and are externally trivial;
- nontrivial zero-force recurrence must allocate a positive fraction of its already-existing critical dissipation to dilation dynamics.

---

## 7. Homogeneous comparison

For an exact homogeneous profile,

\[
\partial_qA=0,
\]

so

\[
\boxed{
\langle\mathcal D_A\rangle_{\rm hom}
=
E_A+D_S.
}
\]

For a nontrivial zero-force recurrent profile,

\[
\boxed{
\langle\mathcal D_A\rangle_{\rm rec}
=
E_A+D_S+D_q,
\qquad
D_q>0.
}
\]

Thus the zero-force recurrent branch is separated from the homogeneous Landau manifold by a strictly positive dilation-derivative occupation in the terminal energy norm.

This suggests a spectral-gap formulation around the homogeneous Landau/trivial manifold, but no such global gap is yet certified.

---

## 8. Relation to M19-405

M19-405 identifies the \(1/r\) tail as the common scale-critical obstruction to both GMS and terminal stress rigidity.

M19-408 shows that genuine log-radius recurrence does not improve the scaling exponent by itself.

It merely redistributes the critical terminal derivative energy:

\[
\boxed{
\text{critical derivative energy}
=
\text{base radial}
+
\text{angular}
+
\text{log-dilation}.
}
\]

Hence

\[
D_q>0
\]

is not the subcritical gain sought by GMS.

A further rigidity/cancellation theorem is still required.

---

## 9. Revised next target

The useful next theorem is not

\[
D_q>0
\]

—it is already proved.

The next target is an incompatibility of the form

\[
\boxed{
\mathcal T_{dil-stress}^{zero-force}:
\quad
\kappa_{\rm force}=0
+
D_q>0
+
\text{stationary recurrent log-cylinder equations}
\Longrightarrow
\text{contradiction or typed exit}.
}
\]

Candidate mechanisms:

1. a zero-force stress identity controlling the \(q\)-derivative modes;
2. a spectral gap on the log-cylinder around the homogeneous zero-force trivial state;
3. a wedge virial coupling \(D_q\) to the finite-depth production shell of M5-587;
4. an invariant-factor theorem excluding recurrent nonconstant dilation modes.

---

\[
\boxed{\text{M19-408 COMPLETE; LOG-DILATION ACTIVITY IS A STRICT POSITIVE COMPONENT OF THE EXISTING TERMINAL DISSIPATION LEDGER.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
