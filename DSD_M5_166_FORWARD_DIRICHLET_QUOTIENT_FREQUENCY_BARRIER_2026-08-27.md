# DSD M5-166 — Forward Dirichlet-Quotient Frequency Barrier

Date: 2026-08-27

Status: **P1_B^S FORWARD FREQUENCY MECHANISM / FOR THE STABLE SLOW PARABOLIC CROSS-SECTION EQUATION, THE SECOND-ORDER PRINCIPAL OPERATOR CONTRIBUTES A NONPOSITIVE VARIANCE TO THE DIRICHLET-QUOTIENT DERIVATIVE, WHILE ALL FREQUENCY GROWTH COMES FROM THE FIRST-ORDER VARIABLE-COEFFICIENT COMMUTATOR AND IS AT MOST `C e^-tau (1+N)` / IF THE M5-160 FAST-STABLE REDUCTION PRESERVES THIS BOUND THROUGH THE PARABOLIC WINDOW, THE REQUIRED M5-154 FREQUENCY ESCAPE IS IMPOSSIBLE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Cross-section Hilbert space

On Branch `P1_B^S` let `rho` be an invariant off-diagonal same-tail pair measure.

Use the co-moving genealogical variable

\[
q=s-\tau.
\]

The invariant pair flow gives a skew-adjoint generator `G` in `L2(rho)`. Together with the spherical Laplacian define the positive self-adjoint operator

\[
\boxed{
A:=I+4(-G^2)+(-\Delta_{S^2}).
}
\]

The precise harmless positive constants may be adjusted.  What matters is that `A` is equivalent to the square of the M5-159 cross-section frequency and that the constant-coefficient cross-section viscosity commutes with it.

Let

\[
\mathscr H=L^2(\rho;L^2(S^2)).
\]

---

## 2. Stable slow model

The co-moving form of the M5-154 equation has the formal stable-slow principal structure

\[
\boxed{
F_\tau
+\nu e^{-\tau}AF
=
e^{-\tau}B_\tau F,
}
\]

up to the fast-normal terms selected by M5-160.

Here `B_tau` contains

- first-order relative transport;
- stretching;
- lower-order geometric terms;
- Biot--Savart-smoothed terms.

The audited coefficient class gives uniformly

\[
\boxed{
|\operatorname{Re}\langle B_\tau f,f\rangle|
\le C\|f\|^2
}
\]

and the first-order commutator estimate

\[
\boxed{
\|[A^{1/2},B_\tau]f\|
\le C\bigl(\|A^{1/2}f\|+\|f\|\bigr).
}
\]

These are the energy-form counterparts of the M5-163 shell estimate.

---

## 3. Energy and Dirichlet quotient

Define

\[
E:=\|F\|^2,
\qquad
H:=\langle AF,F\rangle=\|A^{1/2}F\|^2,
\]

and, when `E>0`,

\[
\boxed{
\mathcal N:=\frac HE.
}
\]

For the slow model,

\[
E'
=
-2\nu e^{-\tau}H
+2e^{-\tau}\operatorname{Re}\langle B_\tau F,F\rangle,
\]

and

\[
H'
=
-2\nu e^{-\tau}\|AF\|^2
+2e^{-\tau}\operatorname{Re}\langle AF,B_\tau F\rangle.
\]

---

## 4. Principal viscosity cannot increase frequency

Differentiate `N=H/E`.

The pure principal contribution is

\[
\boxed{
-2\nu e^{-\tau}
\left[
\frac{\|AF\|^2}{E}
-\left(\frac HE\right)^2
\right].
}
\]

By Cauchy--Schwarz,

\[
H^2
=|\langle AF,F\rangle|^2
\le
\|AF\|^2E.
\]

Therefore

\[
\boxed{
\mathcal N'_{principal}\le0.
}
\]

This is the forward counterpart of the M5-164 audit: the `j^2` diagonal channel may amplify modes in a backward reconstruction, but in actual forward evolution it preferentially damps high frequencies and cannot create frequency escape.

---

## 5. First-order transfer contribution

Write

\[
\langle AF,BF\rangle
=
\langle A^{1/2}F,A^{1/2}BF\rangle.
\]

Use

\[
A^{1/2}BF
=
B A^{1/2}F
+[A^{1/2},B]F.
\]

The symmetric part of the first-order transport on `A^{1/2}F` is controlled by the coefficient Lipschitz norm, so

\[
|\operatorname{Re}\langle A^{1/2}F,B A^{1/2}F\rangle|
\le CH.
\]

The commutator term obeys

\[
\begin{aligned}
|\langle A^{1/2}F,[A^{1/2},B]F\rangle|
&\le
C H^{1/2}(H^{1/2}+E^{1/2})\\
&\le C(H+E).
\end{aligned}
\]

Also

\[
|\langle BF,F\rangle|\le CE.
\]

Hence

\[
\boxed{
\left|
\operatorname{Re}\langle AF,BF\rangle
-\mathcal N\operatorname{Re}\langle BF,F\rangle
\right|
\le CE(1+\mathcal N).
}
\]

---

## 6. Frequency inequality

Combining Sections 4 and 5 gives

\[
\boxed{
\mathcal N'(\tau)
\le
C e^{-\tau}(1+\mathcal N(\tau)).
}
\]

Therefore

\[
\boxed{
1+\mathcal N(\tau)
\le
(1+\mathcal N(\tau_0))
\exp\{Ce^{-\tau_0}\}
}
\]

for every later `tau`, provided the stable slow equation is valid with the same quotient bounds.

Thus the forward slow parabolic system has **uniformly bounded cross-section frequency**.

---

## 7. Conflict with the flat-survivor requirement

M5-154 proved that a nonzero statistical flat fiber cannot survive with bounded cross-section frequency.  It requires

\[
\int^\infty e^{-\tau}\Omega(\tau)^2d\tau=\infty,
\]

and therefore an unbounded parabolic escape with roughly

\[
\Omega(\tau)^2\sim\mathcal N(\tau)\gtrsim e^\tau
\]

along arbitrarily deep scales.

The slow frequency inequality forbids this.

Hence the statistical flat branch would close if the exact M5-160 stable fast-normal reduction can be shown not to introduce a positive frequency-production term stronger than

\[
C e^{-\tau}(1+\mathcal N).
\]

---

## 8. Remaining compatibility lemma

The original co-moving equation contains the singularly perturbed normal terms

\[
4\nu e^{-\tau}F_{\tau\tau},
\qquad
-8\nu e^{-\tau}F_{\tau q},
\qquad
-6\nu e^{-\tau}F_\tau.
\]

M5-160 removes the exponentially growing fast-normal branch by an exact future Volterra representation.

What remains to be proved is:

\[
\boxed{
\text{on the flat-selected stable manifold and up to the first parabolic-frequency threshold,}
\text{ the fast-normal correction preserves the Section-6 quotient inequality.}
}
\]

This is narrower than proving a Gaussian spectral envelope and uses only ordinary analytic/coefficient control.

---

## 9. DSD four-chain audit

### Formation — GREEN

The quotient uses the actual invariant pair Hilbert space and actual cross-section generator; no pure-point spectral decomposition is assumed.

### Axis — GREEN

Forward frequency evolution is distinguished from backward normal reconstruction.

### Static aggregation — GREEN

Backward diagonal amplification is not counted as forward inter-band production.

### Dynamics — GREEN / YELLOW

The slow-model Dirichlet quotient estimate is GREEN.  Its transfer to the exact flat-selected fast-slow system is the one remaining YELLOW compatibility edge.

### Cross-audit — GREEN

The argument uses no finite critical budget and no Gaussian regularity assumption.

---

## 10. Relation to classical backward uniqueness

The structure is the same Dirichlet-quotient/logarithmic-convexity mechanism used in classical backward-uniqueness arguments for parabolic evolution equations with a self-adjoint principal part.  Here it is applied only as a guide to the audited W1 cross-section system; no external theorem is declared applicable until the fast-normal compatibility edge is closed.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
