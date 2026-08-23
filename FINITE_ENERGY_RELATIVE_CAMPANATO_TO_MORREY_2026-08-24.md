# Finite Energy + Relative Campanato -> Absolute Morrey — 2026-08-24

Status: **GALILEAN AUDIT REPAIR / ALL-SCALE RELATIVE CAMPANATO CONTROL RECOVERS THE ABSOLUTE MORREY BOUND ON EACH FINITE-ENERGY FIRST-HITTING FIELD / GLOBAL REGULARITY NOT PROVED.**

`GALILEAN_RELATIVE_MEAN_ACCELERATION_AUDIT_2026-08-24.md` correctly observes that an absolute local kinetic-energy Morrey norm is not Galilean invariant in isolation.

However, the actual first-hitting fields come from finite-energy whole-space Navier--Stokes data. This fixes the large-scale Galilean gauge: the ball mean of the velocity tends to zero at spatial infinity.

Consequently, a uniform **relative** Campanato bound on all larger scales automatically yields the absolute Morrey bound used in the compactness and pressure routes.

This removes a potentially artificial drift branch without assuming that the drift is small by definition.

---

## 1. Relative Campanato quantity

For a fixed center `X` define

\[
\mathcal C_R
:=
R^{-1}
\int_{B_R(X)}
|U-(U)_{B_R(X)}|^2dy,
\]

and write

\[
m_R=(U)_{B_R(X)}.
\]

Assume

\[
\boxed{
\sup_{R\ge R_0}\mathcal C_R\le C_*<\infty.
}
\]

No absolute velocity mean bound is assumed.

---

## 2. Adjacent means differ by O(R^-1)

Using `m_{2R}` as a comparison constant on `B_R`,

\[
\begin{aligned}
|m_R-m_{2R}|
&=
\left|
\fint_{B_R}(U-m_{2R})dy
\right|\\
&\le
|B_R|^{-1/2}
\|U-m_{2R}\|_{L^2(B_R)}\\
&\le
|B_R|^{-1/2}
\|U-m_{2R}\|_{L^2(B_{2R})}.
\end{aligned}
\]

Since

\[
\int_{B_{2R}}|U-m_{2R}|^2
=(2R)\mathcal C_{2R},
\]

we get

\[
\boxed{
|m_R-m_{2R}|
\le
C_m R^{-1}\mathcal C_{2R}^{1/2}
\le
C_m C_*^{1/2}R^{-1}.
}
\]

The constant depends only on the ball-volume normalization.

---

## 3. Finite energy fixes the mean at infinity

For every individual first-hitting rescaling,

\[
U\in L^2(\mathbb R^3).
\]

Its `L2` norm may grow with the first-hitting level, but it is finite at each level.

Hence

\[
|m_R|
\le
|B_R|^{-1/2}\|U\|_2
\to0
\qquad(R\to\infty).
\]

Thus the large-scale mean is not an arbitrary Galilean constant:

\[
\boxed{m_\infty=0.}
\]

---

## 4. Telescoping from infinity

Let

\[
R_k=2^kR.
\]

Since `m_{R_k}->0`,

\[
m_R
=
\sum_{k=0}^\infty
(m_{R_k}-m_{R_{k+1}}).
\]

Therefore

\[
\begin{aligned}
|m_R|
&\le
C_mC_*^{1/2}
\sum_{k=0}^\infty R_k^{-1}\\
&=
2C_m C_*^{1/2}R^{-1}.
\end{aligned}
\]

Hence

\[
\boxed{
|m_R|
\le
C_0 C_*^{1/2}R^{-1}.
}
\]

This is the quantitative decay of the local coherent drift forced jointly by relative Campanato control and finite global kinetic energy.

---

## 5. Recover the absolute Morrey bound

Orthogonality of the mean decomposition gives

\[
\int_{B_R}|U|^2
=
\int_{B_R}|U-m_R|^2
+|B_R||m_R|^2.
\]

The first term is

\[
R\mathcal C_R\le RC_*.
\]

The second satisfies

\[
|B_R||m_R|^2
\le
C R^3\cdot C_*R^{-2}
\le C C_*R.
\]

Therefore

\[
\boxed{
R^{-1}\int_{B_R}|U|^2dy
\le
C_M C_*
}
\]

uniformly for `R>=R0`.

Thus

\[
\boxed{
\sup_{R\ge R_0}\mathcal C_R<\infty
+
U\in L^2(\mathbb R^3)
\Longrightarrow
\sup_{R\ge R_0}
R^{-1}\int_{B_R}|U|^2<\infty.
}
\]

---

## 6. Interpretation of a large coherent drift

Suppose a velocity looks almost constant with amplitude `A` on a very large ball. Relative variance can be small on inner balls, so a purely local Galilean test would regard the drift as harmless.

But finite energy forces the velocity eventually to return toward zero. The ball means must therefore change from approximately `A` to approximately zero across larger scales.

The adjacent-mean estimate implies that this change requires

\[
\boxed{
\mathcal C_R
\gtrsim A^2R^2
}
\]

on at least one transition scale, up to fixed dyadic constants.

So an arbitrarily large coherent drift cannot remain invisible to the **all-scale** relative-Campanato ledger.

It is either

1. a harmless finite local Galilean drift on scales below the transition, or
2. a genuine relative-energy/Campanato escalation when the finite-energy exterior is reached.

There is no third all-scale quiet drift branch.

---

## 7. Consequence for the compactness audit

The absolute Morrey bound used in

- `REMOTE_STRAIN_MORREY_FINITE_RADIUS_CLOSURE_2026-08-23.md`,
- `PARENT_PRESSURE_ESCALATION_FINITE_GATE_2026-08-21.md`, and
- `ANCIENT_LOCAL_COMPACTNESS_FROM_MORREY_WITHOUT_GLOBAL_Z_2026-08-24.md`

can be obtained from the more fundamental Galilean-invariant condition

\[
\boxed{
\sup_{R\ge R_0}\mathcal C_R\le C_*.
}
\]

Therefore a safe proof tree should use

\[
\boxed{
\text{relative Campanato bounded}
\Longrightarrow
\text{absolute Morrey bounded by finite energy},
}
\]

and classify failure at the level of **relative Campanato escalation**, not absolute drift.

---

## 8. Expanding-radius version

For a finite first-hitting level one may only have the desired relative-Campanato bound up to a large parent radius `R_max`.

Telescoping gives

\[
|m_R|
\le
C C_*^{1/2}R^{-1}
+|m_{R_{max}}|.
\]

The final mean obeys the global-energy estimate

\[
|m_{R_{max}}|
\le
C R_{max}^{-3/2}\|U\|_2.
\]

Hence

\[
R^{-1}\int_{B_R}|U|^2
\le
C C_*
+
C R^2R_{max}^{-3}\|U\|_2^2.
\]

Thus an expanding compactness tower also closes whenever `R_max` is chosen sufficiently large relative to the rescaled global kinetic norm. If it cannot be, the failure appears explicitly as a large-scale relative-Campanato/energy-transition branch rather than an invisible Galilean drift.

---

## 9. Updated anti-proof conclusion

The earlier warning

\[
\text{absolute Morrey failure may be only a constant drift}
\]

is correct locally but does **not** create a new all-scale survivor for finite-energy whole-space fields.

The corrected statement is

\[
\boxed{
\text{uniform all-scale relative Campanato control}
\Longrightarrow
\text{uniform absolute Morrey control},
}
\]

while

\[
\boxed{
\text{large coherent drift over expanding scales}
\Longrightarrow
\text{relative-Campanato escalation at its finite-energy transition scale}.
}
\]

The true remaining local-energy frontier is therefore relative-Campanato escalation, not Galilean drift itself.

Status: **FINITE ENERGY FIXES THE GALILEAN GAUGE AT INFINITY. A UNIFORM ALL-SCALE RELATIVE-CAMPANATO CORRIDOR AUTOMATICALLY RECOVERS THE ABSOLUTE TYPE-I MORREY BOUND. LARGE COHERENT DRIFT CANNOT REMAIN INVISIBLE THROUGH ALL SCALES; IT MUST CREATE A CAMPANATO TRANSITION BEFORE MATCHING THE FINITE-ENERGY EXTERIOR. GLOBAL REGULARITY REMAINS UNPROVED.**