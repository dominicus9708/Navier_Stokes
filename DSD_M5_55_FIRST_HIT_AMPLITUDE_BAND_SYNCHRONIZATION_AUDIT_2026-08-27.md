# DSD M5-55 — First-Hit Amplitude-Band Synchronization Audit

Date: 2026-08-27

Status: **DSD LOGIC/REGULARITY AUDIT / THE M5-37 FIRST-HIT ARGUMENT DOES NOT AUTOMATICALLY SYNCHRONIZE NEIGHBORING AMPLITUDE LEVELS / THE ALREADY-DERIVED STRICT GEOMETRIC MARGIN MAY PROPAGATE BY CONTINUITY ONLY UNDER A UNIFORM LEVEL-SET REGULARITY CONDITION / W1 COMPACTNESS ALONE DOES NOT YET SUPPLY THAT CONDITION / GLOBAL REGULARITY UNPROVED.**

## 1. The strict M5-37 margin

Write

\[
F(\lambda,t)
:=
\lambda[-\partial_\lambda Q_P(\lambda,t)]
-
\nu^2D_\lambda^{surf}(t).
\]

At the positive W1 defect first hit `(lambda_c,t_c)`, M5-37 gives

\[
\boxed{
F(\lambda_c,t_c)
\ge
\nu^2A_*>0.
}
\]

This is the strict pressure-tail overpay that M5-54 proposed to thicken in the amplitude direction.

---

## 2. First-hit sign is a time-direction statement

The derivation of M5-37 uses

\[
\partial_tE_{\lambda_c}(t_c)\ge0,
\]

hence

\[
J_P(\lambda_c,t_c)
\ge
\nu D_{\lambda_c}^{surf}(t_c).
\]

For a neighboring amplitude level `lambda`, however, there is no automatic implication

\[
\partial_tE_{\lambda}(t_c)\ge0.
\]

The first-hit times may depend on amplitude:

\[
t_c=t_*(\lambda_c),
\qquad
 t_*(\lambda)\neq t_c.
\]

Therefore the following inference is invalid without an additional synchronization theorem:

\[
\boxed{
\text{first hit at }\lambda_c
\not\Rightarrow
\text{first hit at all nearby }\lambda
\text{ at the same time}.
}
\]

This closes the naive branch in which one simply repeats the M5-37 first-hit proof pointwise on an amplitude interval at one fixed time.

---

## 3. Derivation propagation versus conclusion propagation

There are two logically different questions.

### A. Can the first-hit derivation be repeated at nearby amplitudes?

Not from the current hypotheses.

### B. Can the already-proved numerical inequality for `F` propagate from the central point?

Potentially yes.

If `F(lambda,t)` is continuous in a neighborhood of `(lambda_c,t_c)`, then the fixed margin

\[
F(\lambda_c,t_c)\ge\nu^2A_*
\]

implies that for sufficiently small `delta_lambda,delta_t>0`,

\[
\boxed{
F(\lambda,t)
\ge
\frac12\nu^2A_*
}
\]

whenever

\[
|\lambda-\lambda_c|<\delta_\lambda,
\qquad
|t-t_c|<\delta_t.
\]

This conclusion would not assert that neighboring amplitudes are themselves first hits. It would merely propagate an already-established strict geometric inequality.

That distinction is essential.

---

## 4. Why continuity of `F` is nontrivial

The difficult factor is

\[
-\partial_\lambda Q_P(\lambda,t)
=
\int_{\Sigma_\lambda(t)}
\frac{|P|^2}{|\nabla a|}\,dS,
\qquad
 a=|U|,
\]

at regular values.

Thus a uniform continuity estimate for `F` over the recurrent first-hit class requires quantitative control of the level geometry, schematically

\[
\boxed{
|\nabla a|
\ge m_*>0
}
\]

on a fixed amplitude band surrounding `lambda_c`, together with uniform local smoothness bounds for `U` and `P`.

The local smoothness part is compatible with the retained W1 compact phase-cell structure.

The uniform transversality part is not yet proved.

---

## 5. Pointwise regularity is not uniform transversality

Suppose every recurrent first-hit state individually has `lambda_c` as a regular value.

This only gives, state by state,

\[
\inf_{\Sigma_{\lambda_c}}|\nabla a|>0.
\]

For an infinite sequence of states the corresponding infima may still tend to zero:

\[
m_j
:=
\inf_{\Sigma_{\lambda_c}(U_j)}|\nabla |U_j||
\downarrow0.
\]

A compact limit can then acquire a degenerate level even though every approximating state was individually regular.

Therefore

\[
\boxed{
\text{regular value for each state}
\not\Rightarrow
\text{one uniform regularity constant on the recurrent class}.
}
\]

Compactness alone does not repair this unless the degenerate limit is independently excluded.

---

## 6. The active bulk-gradient floor does not immediately solve the problem

M5-37 supplies

\[
A(\lambda_c)
=
\int_{a>\lambda_c}|\nabla U|^2dy
\ge A_*>0.
\]

This is an integrated interior gradient floor.

It does not directly imply a pointwise lower bound for `|grad a|` on the threshold surface.

A field may have substantial gradient energy in the active region while developing an almost tangential or almost critical contact with one amplitude level on part of its boundary.

Hence the implication

\[
A_*>0
\Rightarrow
|\nabla a|\ge m_*>0
\text{ on }\Sigma_{\lambda_c}
\]

cannot be used without a new argument.

---

## 7. DSD audit

### GREEN

The strict central margin

\[
F(\lambda_c,t_c)\ge\nu^2A_*
\]

is valid on the retained positive-defect first-hit class.

### RED

It is invalid to infer that all nearby amplitude levels are first hits at the same time merely from amplitude continuity.

### YELLOW

The already-derived strict value of `F` would propagate to a genuine amplitude-time neighborhood if one proves uniform continuity of `F` there.

### YELLOW

Uniform continuity of the pointwise pressure-tail derivative requires a quantitative level-set regularity/transversality input not yet present in the M5 chain.

---

## 8. Consequence for the next branch

There are now two legitimate routes:

1. prove a uniform transversality theorem for the recurrent W1 first-hit class; or
2. avoid pointwise level derivatives entirely by averaging/mollifying the threshold ledger in amplitude.

The second route is structurally safer because it can convert the threshold argument into a finite-band quantity without dividing by `|grad a|` at one exact level.

This is the next calculation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
