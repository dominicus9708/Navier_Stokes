# DSD M5-249 — Positive Witness versus Escape-Threshold Firewall

Date: 2026-08-30

Parent: `DSD_M5_248_UNIFORM_SMALL_RHO_TAIL_CERTIFICATE_TO_FIXED_W1_WINDOW_INHERITANCE_2026-08-30.md`

Status: **SCOPE CORRECTION / M5-248 CLOSES THE TAIL-TO-FINITE-STAGE INTERFACE FOR ROBUST LOCAL CERTIFICATES, BUT A POSITIVE ORDER-ONE STRAIN OR DERIVATIVE WITNESS IS NOT AUTOMATICALLY AN `H` OR `T` ESCAPE / EXISTING `H_{1,crit}^{tail}` AND `H_{2,crit}^{tail}` WERE DEFINED BY FAILURE OF UNIFORM CRITICAL-SHELL BOUNDS, NOT BY MERE NONZERO DERIVATIVE CONTENT / THE COMMON ENDPOINT MUST THEREFORE BE SPLIT INTO THRESHOLD-EXCEEDING EXITS AND A COMPACT BOUNDED LARGE-STRUCTURE SURVIVOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. What M5-248 actually proves

M5-248 proves the valid implication

\[
\boxed{
\text{robust positive tail certificate}
\Longrightarrow
\text{robust positive finite-stage fixed-window certificate}.
}
\]

This is an interface theorem.

It does **not** by itself compare the inherited positive constant with the thresholds that define the `H/T` complements.

---

## 2. Existing annular H definitions

The annular H2 bridge defines the critical shell quantities

\[
\mathfrak E_1(R,s)
=R\int_{A_R^*}|\nabla V|^2,
\]

and

\[
\mathfrak E_2(R,s)
=R^3\int_{A_R^*}|\nabla^2V|^2.
\]

The corresponding tail failures are

\[
H_{1,crit}^{tail}:
\sup_{R\to\infty}\mathfrak E_1(R,s)=\infty,
\]

and

\[
H_{2,crit}^{tail}:
\sup_{R\to\infty}\mathfrak E_2(R,s)=\infty.
\]

Thus a critical model with

\[
\mathfrak E_1\asymp1,
\qquad
\mathfrak E_2\asymp1
\]

lies on the bounded spatial-Type-I lane, not in these unbounded H exits.

---

## 3. Positive strain is also normal on a first-hitting stage

A factor-`q` vorticity amplification requires positive accumulated stretching action.

Therefore an order-one normalized strain amplitude is not itself anomalous.

The pure corridor already contains estimates of the form

\[
\log q
\le
\int_I\|S\|_{effective}ds.
\]

Hence

\[
\boxed{
\|S\|>0
\not\Rightarrow H.
}
\]

Only a threshold violation, an unbounded derivative frequency, a projective/turnover cost, or an incompatible time-integrated action can close the stage.

---

## 4. Define pure-corridor ceilings

For each normalized fixed-window observable used after M5-248, distinguish a finite **allowed pure ceiling** when such a ceiling has been established:

\[
B_S,\qquad
B_{H1},\qquad
B_{H2},\qquad
B_L.
\]

These symbols denote the best available finite upper thresholds supplied by the retained no-H/no-T/spatial-Type-I compact corridor; they are not asserted equal and some may only be qualitative compactness ceilings.

For an inherited certificate `C>=c_*`, there are two possibilities:

### Exit

\[
\boxed{c_*>B_C}
\]

or the actual finite-stage observable exceeds the corresponding allowed threshold.  Then the stage is genuinely routed out of the pure corridor.

### Bounded survivor

\[
\boxed{0<c_*\le B_C<\infty.}
\]

Then the positive witness is compatible with the compact pure class and cannot be called an H/T contradiction.

---

## 5. Corrected interpretation of M5-247

M5-247 reduced the residual-gap tail to

\[
S_{amp}\lor H_{tail}\lor L_{tail}.
\]

After M5-248/249 the correct finite-stage reading is

\[
\boxed{
R_{gap}
\Longrightarrow
\text{threshold exit}
\lor
\text{bounded structured finite-stage survivor}.
}
\]

The bounded structured survivor has:

- nonzero strain/gradient/pressure/radial certificates;
- all relevant pure-corridor upper bounds still finite;
- the positive core-speed/no-short-return property;
- compact recurrence.

This is narrower than the original W1 survivor but is not empty by the present estimates.

---

## 6. Why a nonconstructive residual gap cannot close the threshold comparison

M5-238 gives

\[
\varepsilon_{glob}
=
\min_{T\in\mathcal T}\mathbf F(T)>0
\]

on the residual-active minimal hull.

This positive number is produced by compactness.  It is not presently given by an explicit formula in the first-hitting constants.

Therefore downstream lower bounds derived from `epsilon_glob` cannot automatically be compared numerically with the explicit/implicit pure-corridor ceilings.

The implication

\[
\varepsilon_{glob}>0
\Rightarrow
\text{H threshold exceeded}
\]

is RED without a quantitative modulus.

---

## 7. New exact remaining object

After the interface bridge and this correction, the genuinely difficult residual-active survivor is

\[
\boxed{
\begin{array}{c}
\text{compact minimal W1/tail orbit},\\
\text{uniform nonzero residual gap},\\
\text{positive core-speed floor},\\
\text{all-order unique RG/Fuchsian completion},\\
\text{fixed positive local }S/H/L\text{ witnesses},\\
\text{but all witnesses remain below the no-H/no-T escape ceilings}.
\end{array}}
\]

Call this the **bounded structured recurrent survivor**.

---

## 8. Strategic consequence

Further progress should no longer seek another mere positive lower bound for strain or derivatives.

It must produce one of:

1. an **explicit gap** exceeding a pure-corridor ceiling;
2. a **strict averaged Lyapunov/monotonicity** contradiction on the compact recurrent set;
3. a **spectral/nondegeneracy theorem** excluding the bounded structured recurrent dynamics;
4. a finite-stage accumulation law whose physical cost is non-summable despite critical scaling.

This is the correct threshold level for the next audit.

---

## 9. DSD verdict

### PROVED

M5-248's inheritance remains valid.

### CORRECTED

Positive normalized structure is not identical to an H/T escape.

### CURRENT FRONTIER

\[
\boxed{
\text{threshold exit}
\lor
\text{bounded structured recurrent survivor}.
}
\]

The next calculation should search for a **state functional with sign after invariant averaging** on this bounded survivor.  The finite-energy quotient `Q=V-B_T in L2 cap L3` is the natural place to try, because unlike the full critical tail it admits a genuine global L2 pairing.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]