# DSD M18-045 — Upper stage clock is equivalent to Type-I remaining-time control

Date: 2026-09-11

Status: **ROOT-CERT CLOCK REDUCTION. THE UNIFORM UPPER FIRST-HITTING STAGE CLOCK IS NOT AN INDEPENDENT SURVIVOR ASSUMPTION. ON THE GEOMETRIC FIRST-HITTING TOWER IT IS EQUIVALENT, UP TO FIXED `q` CONSTANTS, TO UNIFORM BOUNDEDNESS OF THE VORTICITY TYPE-I REMAINING-TIME AMPLITUDE `Theta_j=W_j(T^*-t_j)`. FAILURE OF `L_+` THEREFORE ROUTES DIRECTLY TO THE VORTICITY TYPE-II ROOT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Definitions

Let

\[
W_{j+1}=qW_j,
\qquad q>1,
\]

and define the first-hitting stage interval

\[
\Delta t_j:=t_{j+1}-t_j.
\]

During this stage, by first-hitting monotonicity of the running maximum,

\[
W_j\le\overline W(t)\le W_{j+1}=qW_j.
\]

Define

\[
L_j:=\int_{t_j}^{t_{j+1}}\overline W(t)\,dt,
\]

\[
\tau_j:=W_j\Delta t_j,
\]

and the remaining-time amplitude

\[
\Theta_j:=W_j(T^*-t_j).
\]

---

## 2. Exact one-stage comparability

Integrating the first-hitting amplitude bounds gives

\[
W_j\Delta t_j
\le
L_j
\le
qW_j\Delta t_j.
\]

Hence

\[
\boxed{
\tau_j\le L_j\le q\tau_j.
}
\]

Thus uniform boundedness of `L_j` and uniform boundedness of `tau_j` are equivalent up to the fixed factor `q`.

---

## 3. Remaining-time amplitude dominates the current stage clock

Since

\[
T^*-t_j\ge\Delta t_j,
\]

we have

\[
\boxed{
\Theta_j\ge\tau_j\ge q^{-1}L_j.
}
\]

Therefore any upper-clock failure

\[
L_{j_n}\to\infty
\]

forces

\[
\boxed{
\Theta_{j_n}\to\infty.
}
\]

But bounded `Theta_j` is precisely the vorticity Type-I remaining-time condition along the first-hitting sequence:

\[
W_j(T^*-t_j)\le C.
\]

Hence

\[
\boxed{
L_j\to\infty
\Longrightarrow
\text{vorticity Type-II}.
}
\]

---

## 4. Converse: bounded upper stage clock gives Type-I remaining time

Because the first-hitting levels are geometric,

\[
W_{j+n}=q^nW_j.
\]

Also

\[
T^*-t_j
=\sum_{n=0}^{\infty}\Delta t_{j+n}.
\]

Therefore

\[
\Theta_j
=W_j(T^*-t_j)
=\sum_{n=0}^{\infty}q^{-n}\tau_{j+n}.
\]

If

\[
\sup_kL_k\le L_+<\infty,
\]

then `tau_k<=L_k`, hence

\[
\Theta_j
\le
L_+\sum_{n=0}^{\infty}q^{-n}
=
\frac{L_+}{1-q^{-1}}.
\]

Thus

\[
\boxed{
\sup_jL_j<\infty
\Longrightarrow
\sup_j\Theta_j<\infty.
}
\]

---

## 5. Converse in the other direction

If

\[
\sup_j\Theta_j\le\Theta_+<\infty,
\]

then Section 3 gives

\[
L_j\le q\Theta_j\le q\Theta_+.
\]

Therefore

\[
\boxed{
\sup_j\Theta_j<\infty
\Longrightarrow
\sup_jL_j<\infty.
}
\]

Combining Sections 4 and 5,

\[
\boxed{
\sup_jL_j<\infty
\iff
\sup_j\Theta_j<\infty
}
\]

up to fixed constants depending only on `q`.

---

## 6. ROOT-CERT consequence

M18-044 isolated the upper stage clock as the only remaining independent clock-side input after `L_-` was derived from amplification.

The present module removes that independence:

\[
\boxed{
\text{upper CLOCK-CERT}
=
\text{vorticity Type-I certificate}.
}
\]

Its failure is not a new branch:

\[
\boxed{
\neg\text{CLOCK-CERT}_{upper}
\Longrightarrow
\text{Type-II root}.
}
\]

Therefore the primitive root menu should not count both

- upper first-hitting clock failure, and
- vorticity Type-II

as separate possibilities.

They are the same escape expressed in two coordinate systems.

---

## 7. Updated first-hitting clock package

On the bounded-normalized-strain Type-I survivor,

\[
\log q\le B_+L_j
\]

gives

\[
L_j\ge\frac{\log q}{B_+},
\]

while Type-I gives

\[
L_j\le q\Theta_+.
\]

Hence the full two-sided stage clock is derived:

\[
\boxed{
0<\frac{\log q}{B_+}
\le L_j
\le q\Theta_+<\infty.
}
\]

No additional `L_-` or `L_+` primitive assumption is required once bounded normalized strain and Type-I are certified.

---

## 8. Audit firewall

This is a branch-routing result, not a Type-II closure theorem.

The Type-II branch remains open at the Euler-scaling/remote-source frontier identified in M5-443 and subsequent modules.

Thus the gain is a reduction of branch count:

\[
\boxed{
\text{clock degeneration}
\notin
\text{independent root menu}.
}
\]

It is absorbed into the existing Type-II root.

---

## 9. Next target

With the clock root removed, the next ROOT-CERT audit should distinguish the genuinely primitive complements of the Type-I/nested/bounded-Z W1 entry corridor.

Current evidence suggests that several of these already collapse into the common remote/Type-II frontier.

The high-value next question is whether all upstream noncompact failures can be organized as

\[
\boxed{
\text{remote/Type-II}
\lor
\text{local critical H/action}
\lor
\text{projective/export/realization failure},
}
\]

without hidden untyped complements.

---

## 10. Status

\[
\boxed{
\text{UPPER STAGE CLOCK FAILURE IS TYPE-II, NOT A NEW ROOT.}
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
