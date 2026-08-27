# DSD M5-103 — Mellin Critical Limit and R3 Identification

Date: 2026-08-27

Status: **CRITICAL-LIMIT CROSS-AUDIT / THE HOMOGENEOUS MELLIN UPSTROKE HAS A FINITE NONZERO `alpha->1+` LIMIT DETERMINED BY THE EXISTING W1 CUBIC RESIDUE `R3` / THE ASSOCIATED STRICT-PAYER SURPLUS HAS A POSITIVE CRITICAL LOWER LIMIT / THIS SURPLUS IS NOT AN INDEPENDENT NEW GLOBAL RESOURCE AND MUST NOT BE DOUBLE-COUNTED AGAINST `R3` / THE REMAINING GAP IS THE PRELIMIT-TO-W1 CRITICAL DEFECT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Critical parameterization

Set

\[
\alpha=1+\varepsilon,
\qquad
p=3+\varepsilon,
\qquad
0<\varepsilon<\frac12.
\]

M5-100 gives the Mellin threshold entropy

\[
\mathfrak E_\varepsilon[U]
=
\frac{1}{(1+\varepsilon)(2+\varepsilon)(3+\varepsilon)}
\int |U|^{3+\varepsilon}dY.
\]

Write

\[
c_\varepsilon
:=\frac{1}{(1+\varepsilon)(2+\varepsilon)(3+\varepsilon)}
\to\frac16.
\]

The retained W1 endpoint has the invariant cubic residue

\[
\boxed{
\mathscr R_3
=
\lim_{\varepsilon\downarrow0}
\varepsilon
\left\langle
\int |U|^{3+\varepsilon}dY
\right\rangle_\mu
>0.
}
\]

---

# 2. Build a standard-cell segment from one W1 phase

Use the M5-44 inverse-Leray cell with

\[
\eta(0)=0,
\qquad
\sigma_h
=\sigma_*(1-e^{-h}),
\]

so that

\[
\eta(\sigma_h)=h.
\]

For a W1 phase `U_0` and its forward image `S(h)U_0`, the exact `L^{3+epsilon}` scaling gives

\[
\mathfrak E_\varepsilon(0)
=c_\varepsilon\sigma_*^{-\varepsilon/2}
\|U_0\|_{3+\varepsilon}^{3+\varepsilon},
\]

and

\[
\mathfrak E_\varepsilon(\sigma_h)
=c_\varepsilon\sigma_*^{-\varepsilon/2}
 e^{\varepsilon h/2}
\|S(h)U_0\|_{3+\varepsilon}^{3+\varepsilon}.
\]

---

# 3. Invariant averaging removes the recurrence error exactly

Average over the invariant probability measure `mu` on the W1 minimal set.
Because `mu` is invariant under `S(h)`,

\[
\left\langle
\|S(h)U\|_{3+\varepsilon}^{3+\varepsilon}
\right\rangle_\mu
=
\left\langle
\|U\|_{3+\varepsilon}^{3+\varepsilon}
\right\rangle_\mu.
\]

Therefore the mean standard-cell Mellin growth over one Leray shift `h>0` is exactly

\[
\boxed{
\begin{aligned}
\left\langle\Delta_h\mathfrak E_\varepsilon\right\rangle_\mu
&=
c_\varepsilon\sigma_*^{-\varepsilon/2}
\left(e^{\varepsilon h/2}-1\right)
\left\langle
\int |U|^{3+\varepsilon}dY
\right\rangle_\mu.
\end{aligned}
}
\]

No approximate-return estimate is needed at the invariant-average level.

---

# 4. Critical limit

Use

\[
e^{\varepsilon h/2}-1
=\frac{\varepsilon h}{2}+o(\varepsilon),
\]

\[
\sigma_*^{-\varepsilon/2}\to1,
\qquad
c_\varepsilon\to\frac16,
\]

and the definition of `R3`.
Then

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\left\langle\Delta_h\mathfrak E_\varepsilon\right\rangle_\mu
=
\frac{h\mathscr R_3}{12}.
}
\]

Thus the apparently small scale factor

\[
e^{\varepsilon h/2}-1=O(\varepsilon)
\]

is multiplied by the W1 near-critical moment

\[
\left\langle\|U\|_{3+\varepsilon}^{3+\varepsilon}\right\rangle
\sim\frac{\mathscr R_3}{\varepsilon},
\]

leaving an order-one positive limit.

This is the exact Mellin form of the weak-critical boundary defect.

---

# 5. Integrate the M5-102 strict-surplus inequality

For

\[
\alpha=1+\varepsilon,
\]

M5-102 gives on `X_epsilon>=0`

\[
\mathcal E_\varepsilon
\ge
4\nu
\left(
\frac{3}{2(1+\varepsilon)}-1
\right)
X_\varepsilon.
\]

When `X_epsilon<0`, the same displayed lower bound is automatically true because the left side is nonnegative while the right side is negative.
Hence the inequality is valid for integration over an arbitrary cell segment:

\[
\boxed{
\int_0^{\sigma_h}\mathcal E_\varepsilon d\sigma
\ge
4\nu
\left(
\frac{3}{2(1+\varepsilon)}-1
\right)
\Delta_h\mathfrak E_\varepsilon.
}
\]

Average over `mu` and pass to the critical limit.
Since

\[
4\nu
\left(
\frac{3}{2(1+\varepsilon)}-1
\right)
\to2\nu,
\]

we obtain

\[
\boxed{
\liminf_{\varepsilon\downarrow0}
\left\langle
\int_0^{\sigma_h}
\mathcal E_\varepsilon d\sigma
\right\rangle_\mu
\ge
\frac{\nu h\mathscr R_3}{6}>0.
}
\]

Thus the Mellin strict-surplus family reaches a genuine order-one critical boundary payment.

---

# 6. DSD formation audit: this is not a second independent defect

The same `R3` appears in

1. the already audited Abel/Mellin critical boundary coordinate of W1; and
2. the `alpha->1+` limit of the new homogeneous-weight upstroke/surplus.

Therefore these are **two representations of the same critical boundary defect**, not two separately consumable resources.

The following inference is forbidden:

\[
\boxed{
\text{positive }\mathscr R_3
+\text{positive Mellin critical surplus}
\Rightarrow
\text{two independent positive costs}.
}
\]

That would be a DSD static double-counting error and would reintroduce the nonlinear logical loop the current audit was designed to remove.

---

# 7. Axis/static interpretation

The critical residue is a boundary amplitude/spatial defect.
The Mellin surplus describes the interior pressure/strain payment needed as the standard cell advances toward that boundary under inverse-Leray scaling.

They occupy different descriptive locations but are linked by the same `p->3+` Mellin limit.

Thus the correct typed relation is

\[
\boxed{
\text{critical boundary charge}
\longleftrightarrow
\text{critical-limit interior payer},
}
\]

not an additive independent-budget relation.

---

# 8. Dynamic interpretation

The invariant W1 measure is stationary under normalized Leray time.
The standard-cell Mellin moment nevertheless grows because the inverse-Leray map contains the explicit factor

\[
e^{\varepsilon h/2}.
\]

Hence the growth does not mean the normalized recurrent state creates a new conserved quantity.
It is the standard-cell representation of moving toward the terminal projective boundary.

This also confirms that the M5-101 upstroke construction did not use a false physical-recurrence interpretation.

---

# 9. The actual remaining bridge is now a limit-interchange defect

For every fixed smooth finite-energy prelimit state, the near-critical moment is ordinary and carries no nonzero W1 boundary residue after taking the critical limit first.

The W1 limit instead has

\[
\mathscr R_3>0.
\]

Therefore the unresolved structure is schematically

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\lim_{j\to\infty}
\varepsilon M_{3+\varepsilon}(U_j)
\ne
\lim_{j\to\infty}
\lim_{\varepsilon\downarrow0}
\varepsilon M_{3+\varepsilon}(U_j).
}
\]

The right-hand order is zero for each sufficiently regular finite-stage state, while the W1-first order can retain `R3>0`.

This is exactly a critical lack of uniform integrability/tightness, not an algebraic payer contradiction.

---

# 10. Updated next gate

The next DSD audit should formulate the weakest **uniform-in-prelimit Mellin integrability condition** that would commute these limits.

If the existing finite-energy/W1 ancestry implied such a condition, then

\[
\mathscr R_3=0
\]

and Issue #2 would close.

If it does not, construct an explicit admissible packet/measure countermodel showing which additional PDE-specific input is missing.

This is now preferred over further R1/R2 work because it attacks the critical defect directly and preserves the stabilized acyclic dependency graph.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
