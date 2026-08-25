# DSD W1 Current Frontier after Diagonal and Loop-Gain Audit

Date: 2026-08-26

Status: **CURRENT PROOF MAP / MAJOR DIAGONAL OVERREACH CORRECTED / SMALL WEAK-L3 BRANCH EXCLUDED BY A DIRECT LOOP-GAIN ESTIMATE / LARGE WEAK-CRITICAL RECURRENT ENDPOINT REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. What was corrected

The periodic omega-limit orbit has a canonical critical far tail and its own inverse-Leray DSS solution has a static physical `1/r` trace.

However the original finite-energy parent is not automatically equal to that DSS solution on fixed physical annuli.

The missing diagonal is

\[
|Y|\sim e^{s/2}.
\]

If

\[
\varepsilon_n
=
\|U_{orig}(s_n)-U_{per}(0)\|_p,
\qquad p>3,
\]

then a sufficient parent-to-periodic fixed-annulus inheritance rate is

\[
\boxed{
\varepsilon_n
=o\left(e^{-\frac{p-3}{2p}s_n}\right).
}
\]

Compact recurrence alone does not give this rate.

Therefore no current W1 proof may identify the periodic omega-limit trace with the finite-energy parent's terminal trace without an extra diagonal theorem.

---

## 2. What remains independent of that correction

The following W1 conclusions are still valid because they were obtained at fixed Leray scale before taking the large-radius endpoint:

- compact minimal recurrent dynamics;
- positive critical shell density `Mcrit`;
- endpoint residue `R3/6`;
- pressure gauge repair;
- D3 / log-weighted derivative separation;
- invariant enstrophy and strain gates;
- Gaussian Bernoulli scale ledger;
- pressure-free weighted-vorticity scale current;
- critical-clock and weak-Lorentz saturation.

---

## 3. Current nonlinear loop

Define

\[
\sigma_P
=|S|^2-\frac12|\Omega|^2,
\qquad
P=(-\Delta)^{-1}\sigma_P,
\]

and

\[
e=U\cdot\nabla|U|.
\]

Then

\[
\int\sigma_P=0,
\qquad
\int |U|^2e=0,
\]

while the critical pressure work is

\[
F_P=\int Pe.
\]

The invariant endpoint balance is

\[
\boxed{
\langle F_P\rangle
=
\nu\langle D_3\rangle
+
\frac{\mathscr R_3}{6}.
}
\]

Thus the W1 survivor requires a recurrent paired strain/rotation--amplitude feedback loop with mean gain strictly above viscous loss.

---

## 4. Direct weak-L3 loop-gain estimate

Let

\[
M_*=
\sup_{U\in M}\|U\|_{L^{3,\infty}}.
\]

The Lorentz endpoint estimate gives

\[
\boxed{
|F_P|
\le
C_{WL3}
\|U\|_{L^{3,\infty}}D_3.
}
\]

Therefore

\[
\boxed{
M_*
\ge
\frac{\nu}{C_{WL3}}
+
\frac{\mathscr R_3}
{6C_{WL3}\langle D_3\rangle}.
}
\]

In particular the small weak-`L3` branch is removed.

---

## 5. Universal weak-critical saturation

For every `p>3`, with

\[
q_p=\frac{2p}{p-3},
\]

the W1 Type-I class lies at

\[
\boxed{
u\in L_t^{q_p,\infty}L_x^p}
\]

while recurrence forces failure of

\[
\boxed{
u\in L_t^{q_p}L_x^p.}
\]

Likewise

\[
\boxed{
u\cdot\nabla|u|
\in
L_t^{2,\infty}L_x^{3/2}
\setminus
L_t^2L_x^{3/2}}
\]

and `D3` occupies the weak-`L1`/non-`L1` time endpoint.

Thus the current survivor is a **large weak-critical recurrent endpoint**, not a generic uncontrolled branch.

---

## 6. Scaling-budget barrier

Any repeated event whose physical cost scales like

\[
r^\beta,
\qquad \beta>0,
\]

is geometrically summable and cannot by itself close W1.

Hence ordinary energy, ordinary dissipation, raw turnover energy, or raw Lamb budgets are no longer useful terminal targets.

A successful theorem must use:

- a `beta=0` critical budget;
- a sign-definite critical monotonicity;
- a scale-invariant topological obstruction genuinely forced by W1;
- or a fixed parent/interface scale that breaks self-similar homogeneity.

---

## 7. Correct current endpoint

The proof map is now

\[
\boxed{
\text{hypothetical finite-time blow-up}
\to
W1
\to
\text{compact recurrent critical element}
\to
\text{large weak-critical pressure-amplitude loop}
\to
\text{missing large-endpoint rigidity theorem}.
}
\]

For the periodic subcase an additional optional route is

\[
\boxed{
\text{omega-limit periodic tail}
\to
\text{diagonal inheritance rate gate}
}
\]

but that route is not currently established and is not needed for the fixed-scale W1 endpoint identities.

---

## 8. Immediate next target

The most direct remaining estimate would improve

\[
|F_P|
\le
C_{WL3}M D_3
\]

on the recurrent W1 class in one of the following ways:

1. replace the large global weak-`L3` coefficient by a smaller effective local/interface coefficient;
2. obtain a logarithmic gain that moves the weak critical endpoint into a strong critical class;
3. use the simultaneous vorticity scale current to reduce the admissible pressure-amplitude gain;
4. or show that the paired sign-changing pressure/amplitude loop cannot remain recurrent at gain greater than one.

No such final improvement is proved yet.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
