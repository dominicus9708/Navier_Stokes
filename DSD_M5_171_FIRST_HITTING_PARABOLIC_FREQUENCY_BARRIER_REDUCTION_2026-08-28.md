# DSD M5-171 — First-Hitting Parabolic Frequency Barrier Reduction

Date: 2026-08-28

Status: **P1_B^S REDUCTION / IT IS NOT NECESSARY TO CONTROL THE DIRICHLET QUOTIENT AT ARBITRARILY SUPER-PARABOLIC FREQUENCY / A FREQUENCY-FUNCTION INEQUALITY ONLY ON EACH FIXED CORRIDOR `z N <= kappa` PREVENTS THE FIRST CROSSING OF THE MOVING PARABOLIC BARRIER `N=kappa/z`, AFTER WHICH THE INTEGRABLE `z=e^-tau` COEFFICIENT GIVES A UNIFORM FREQUENCY BOUND / THIS REDUCES M5-170 TO A SUB-PARABOLIC NONAUTONOMOUS PRINCIPAL-COVARIANCE LEMMA / GLOBAL REGULARITY UNPROVED.**

---

## 1. Frequency and normal depth

Use

\[
z=e^{-\tau}
\]

and the corrected M5-170 Dirichlet quotient

\[
\mathcal N(\tau)
=
\frac{\langle A F,F\rangle}{\|F\|^2}.
\]

The M5-154 necessary parabolic escape is equivalent, up to the fixed shift in `A`, to

\[
\boxed{
\mathcal N(\tau)\text{ becoming comparable to }z^{-1}=e^\tau
}
\]

along arbitrarily deep normal scales.

---

## 2. Corridor hypothesis

Fix an arbitrary finite constant

\[
\kappa>0.
\]

The only estimate needed in the present reduction is the following corridor inequality:

\[
\boxed{
\mathcal N_\tau
\le
C_\kappa z(1+\mathcal N)
\qquad
\text{whenever }z\mathcal N\le\kappa.
}
\]

The constant `C_kappa` may depend on the chosen finite parabolic corridor.  No estimate is assumed for `z N > kappa`.

This is strictly weaker than the global M5-166 target.

---

## 3. Moving parabolic barrier

Define

\[
B_\kappa(\tau):=\frac\kappa z=\kappa e^\tau.
\]

Then

\[
\boxed{B_\kappa'=B_\kappa.}
\]

Choose a finite starting time `tau_0` and then choose `kappa` so that

\[
\mathcal N(\tau_0)<B_\kappa(\tau_0).
\]

Suppose a first crossing occurs at `tau_* > tau_0`:

\[
\mathcal N(\tau_*)=B_\kappa(\tau_*),
\]

with `N < B_kappa` before `tau_*`.

At a first upward crossing,

\[
\mathcal N_\tau(\tau_*)
\ge
B_\kappa'(\tau_*)
=
\frac\kappa{z_*}.
\]

But the corridor inequality gives

\[
\mathcal N_\tau(\tau_*)
\le
C_\kappa z_*
\left(1+\frac\kappa{z_*}\right)
=
C_\kappa(z_*+\kappa).
\]

As `z_* -> 0`, the first quantity grows like `kappa/z_*`, whereas the second remains bounded by a constant depending only on `kappa`.

Therefore there is a depth

\[
z_\kappa>0
\]

such that no first upward crossing can occur for

\[
0<z<z_\kappa.
\]

---

## 4. Once inside the corridor, Gronwall gives bounded frequency

On the no-crossing tail interval the corridor inequality remains valid forever.

Thus

\[
\frac d{d\tau}\log(1+\mathcal N)
\le
C_\kappa e^{-\tau}.
\]

Since

\[
\int_{\tau_1}^{\infty}e^{-\tau}d\tau<\infty,
\]

we obtain

\[
\boxed{
\sup_{\tau\ge\tau_1}\mathcal N(\tau)<\infty.
}
\]

Hence

\[
\boxed{
z\mathcal N(\tau)\to0.
}
\]

This is incompatible with the M5-154 parabolic frequency escape required by a nonzero flat statistical fiber.

---

## 5. Why arbitrary finite `kappa` is enough

The argument does not require one universal small `kappa` chosen in advance.

For a given finite starting state, `N(tau_0)` is finite.  Choose a finite `kappa` placing the state strictly below the barrier at `tau_0`.

The remaining analytic task may have constants depending on that fixed `kappa`.

Thus the exact PDE lemma needed next is:

\[
\boxed{
\forall\kappa<\infty,
\quad
z\mathcal N\le\kappa
\Longrightarrow
\mathcal N_\tau\le C_\kappa z(1+\mathcal N)
\text{ for sufficiently small }z.
}
\]

This avoids any need to control truly super-parabolic frequencies before they are first reached.

---

## 6. Relation to M5-164

M5-164 showed that a naive backward spectral-cascade argument can be repaired by alternating first-order transfer and second-order in-band amplification in finite normal depth.

M5-171 does not reuse that invalid product argument.

Instead it works in the actual forward `tau` orientation and asks only whether the normalized frequency can **first reach** the parabolic barrier.

At the barrier:

- the barrier itself moves with speed `~z^-1`;
- first-order transfer contributes only an integrably weighted rate;
- principal second-order dynamics has the favorable frequency-variance sign.

This is a different mechanism.

---

## 7. DSD audit

### Formation — GREEN

The barrier is built from the already-defined exact Dirichlet quotient and normal depth.

### Axis — GREEN

Frequency size and normal-depth motion are compared through the dimensionless product `z N`.

### Static aggregation — GREEN

No spectral-shell transfer is multiplied independently by later in-band amplification.

### Dynamics — GREEN reduction

The first-hitting comparison is a one-way implication from the corridor differential inequality to bounded frequency.

### Cross-audit — GREEN

The reduction does not assume the conclusion `N bounded`; it only isolates the precise local inequality that would imply it.

---

## 8. New single target

The preferred next lemma is now:

\[
\boxed{
\textbf{Sub-parabolic principal-covariance lemma:}
\quad
z\mathcal N\le\kappa
\Rightarrow
\mathcal N_\tau
\le C_\kappa z(1+\mathcal N).
}
\]

Only this fixed-corridor estimate is needed to close `P1_B^S`.

`P1_B^P` remains separate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
