# DSD W1 Weak-L3 Loop-Gain Threshold

Date: 2026-08-26

Status: **LORENTZ-SPACE ESTIMATE BOUNDS THE P3 PRESSURE-AMPLITUDE FEEDBACK BY `C ||U||_(3,infty) D3` / W1 RESIDUE FORCES A STRICT LARGE-WEAK-L3 THRESHOLD / GLOBAL REGULARITY UNPROVED.**

## 1. Endpoint pressure work

Let

\[
F_P
=
\int P\,e\,dY,
\qquad
e=U\cdot\nabla|U|.
\]

The invariant W1 endpoint satisfies

\[
\boxed{
\langle F_P\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+
\frac{\mathscr R_3}{6}.
}
\]

We estimate `F_P` in terms of the weak critical velocity size and `D3`.

---

## 2. D3 controls L9

Set

\[
w=|U|^{3/2}.
\]

Then

\[
|\nabla w|^2
=
\frac94|U||\nabla|U||^2
\le
\frac94|U||\nabla U|^2.
\]

Therefore

\[
\|\nabla w\|_2^2
\le C D_3.
\]

Sobolev gives

\[
\|w\|_6^2
\le C_S\|\nabla w\|_2^2,
\]

hence

\[
\boxed{
\|U\|_9^3
\le C D_3.
}
\]

---

## 3. Weak-L3 plus L9 gives a Lorentz L6 estimate

Let

\[
M:=\|U\|_{L^{3,\infty}}.
\]

Real/Lorentz interpolation between `L^(3,infty)` and `L9` yields

\[
\boxed{
\|U\|_{L^{6,2}}
\le
C
M^{1/4}
\|U\|_9^{3/4}.
}
\]

Consequently

\[
\|U\otimes U\|_{L^{3,1}}
\le
C\|U\|_{L^{6,2}}^2
\le
C M^{1/2}\|U\|_9^{3/2}.
\]

Using the `L9` estimate,

\[
\boxed{
\|U\otimes U\|_{L^{3,1}}
\le
C M^{1/2}D_3^{1/2}.
}
\]

The pressure is obtained from `U tensor U` by Riesz transforms, which are bounded on Lorentz `L^(3,1)`. Thus

\[
\boxed{
\|P\|_{L^{3,1}}
\le
C_P M^{1/2}D_3^{1/2}.
}
\]

---

## 4. The amplitude-flow field has the dual Lorentz bound

Since

\[
|e|
\le
|U||\nabla U|
=
|U|^{1/2}
\left(|U|^{1/2}|\nabla U|\right),
\]

we have

\[
\||U|^{1/2}\|_{L^{6,\infty}}
=M^{1/2}
\]

and

\[
\||U|^{1/2}|\nabla U|\|_2
\le
D_3^{1/2}.
\]

Lorentz Holder therefore gives at least

\[
\boxed{
\|e\|_{L^{3/2,\infty}}
\le
C_e M^{1/2}D_3^{1/2}.
}
\]

---

## 5. Pressure-amplitude feedback is linear in the weak-L3 size

Lorentz duality

\[
L^{3,1}\times L^{3/2,\infty}
\to L^1
\]

gives

\[
\begin{aligned}
|F_P|
&\le
C
\|P\|_{L^{3,1}}
\|e\|_{L^{3/2,\infty}}\\
&\le
C_{WL3}
M D_3.
\end{aligned}
\]

Therefore

\[
\boxed{
|F_P|
\le
C_{WL3}
\|U\|_{L^{3,\infty}}
D_3.
}
\]

This is the endpoint loop-gain estimate.

---

## 6. W1 must lie above a universal weak-L3 threshold

Assume the recurrent class obeys the uniform ceiling

\[
\sup_{U\in M}
\|U\|_{L^{3,\infty}}
\le M_*.
\]

Averaging the pointwise estimate gives

\[
\langle F_P\rangle_\mu
\le
C_{WL3}M_*
\langle D_3\rangle_\mu.
\]

Combining with the exact endpoint identity,

\[
\nu\langle D_3\rangle_\mu
+
\frac{\mathscr R_3}{6}
\le
C_{WL3}M_*
\langle D_3\rangle_\mu.
\]

Hence

\[
\boxed{
M_*
\ge
\frac{\nu}{C_{WL3}}
+
\frac{\mathscr R_3}
{6C_{WL3}\langle D_3\rangle_\mu}.
}
\]

In particular,

\[
\boxed{
M_*>\frac{\nu}{C_{WL3}}.
}
\]

Thus every nontrivial W1 endpoint is forced into a quantitatively large weak-`L3` regime.

---

## 7. Meaning of the threshold

If

\[
\sup_s\|U(s)\|_{L^{3,\infty}}
<
\frac{\nu}{C_{WL3}},
\]

then pressure-amplitude feedback can be absorbed by viscous `D3`, while the positive residue `R3/6` has no payer.

Therefore that entire small weak-critical branch is excluded.

This reproduces, inside the DSD endpoint ledger, the familiar principle behind small critical-data regularity: below a critical amplitude the nonlinear loop gain is less than the viscous loss.

The unresolved survivor is the **large weak-L3 recurrent branch** above this threshold.

---

## 8. Updated endpoint

The proof search no longer targets arbitrary weak-critical behavior.

It targets

\[
\boxed{
\text{large weak-}L^3
+
\text{recurrent critical p3 gain above one}
+
\text{positive vorticity scale current}.
}
\]

A complete closure would need a new estimate that controls this large-data weak endpoint or a global/interface mechanism that lowers its effective loop gain.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
