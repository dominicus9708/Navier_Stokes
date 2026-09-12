# DSD M19-128 — RDSS twisted scattering has a log-radius Floquet--Bloch spectrum with exact holonomy-mismatch cost in the critical shell charge

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / PRINCIPAL-HOLONOMY NORMAL FORM OF M19-125 DIAGONALIZED IN LOG-RADIUS FOURIER AND ANGULAR ROTATION MODES / THE CRITICAL SHELL CHARGE CONTAINS AN EXACT POSITIVE BLOCH-MISMATCH TERM `(2PI N-M BETA)^2/L^2` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Intrinsic twisted-periodic normal form

Let

\[
S=2L,
\qquad
Q_*=e^{\beta A_0},
\qquad
\beta\in[-\pi,\pi]
\]

be the RDSS period and principal rotation holonomy.

M19-125 gives

\[
\boxed{
A(q)
=e^{-(\beta/L)q\mathcal R_\omega}\widetilde A(q),
\qquad
\widetilde A(q+L)=\widetilde A(q).
}
\]

Set

\[
\gamma:=\beta/L.
\]

Then

\[
\boxed{
\partial_qA
=e^{-\gamma q\mathcal R_\omega}
\left(\partial_q-\gamma\mathcal R_\omega\right)\widetilde A.
}
\]

Thus the natural covariant derivative on the periodic log-radius cell is

\[
\boxed{
D_q^{\beta}
:=
\partial_q-rac\beta L\mathcal R_\omega.
}
\]

---

## 2. Shell-gradient radial term

For the leading critical velocity

\[
U=r^{-1}A(q,\omega),
\]

the radial derivative contains

\[
\partial_qA-A.
\]

Because the rotation factor is unitary on the sphere,

\[
\boxed{
\|\partial_qA-A\|_{L^2(S^2)}
=
\|D_q^{\beta}\widetilde A-\widetilde A\|_{L^2(S^2)}.
}
\]

Therefore the one-period critical shell quadratic form contains

\[
\boxed{
\int_0^L
\|\left(D_q^{\beta}-1\right)\widetilde A(q)\|_{L^2(S^2)}^2dq.
}
\]

Angular derivative terms are added separately and are nonnegative.

---

## 3. Fourier--rotation decomposition

Expand the periodic q-dependence as

\[
\widetilde A(q,\omega)
=
\sum_{n\in\mathbb Z}
 e^{2\pi inq/L}
\widetilde A_n(\omega).
\]

Decompose each angular coefficient into eigenmodes of the rotation generator:

\[
\mathcal R_\omega\Phi_m
=im\Phi_m,
\qquad m\in\mathbb Z,
\]

with the usual vector-spherical-harmonic interpretation.

For a joint mode `(n,m)`,

\[
D_q^{\beta}
\longmapsto
 i\left(
\frac{2\pi n}{L}
-
\frac{m\beta}{L}
\right).
\]

Hence

\[
\boxed{
(D_q^{\beta}-1)
\longmapsto
-1
+i\frac{2\pi n-m\beta}{L}.
}
\]

---

## 4. Exact Bloch mismatch cost

The squared modulus is

\[
\boxed{
\left|-1+i\frac{2\pi n-m\beta}{L}\right|^2
=
1+rac{(2\pi n-m\beta)^2}{L^2}.
}
\]

Therefore every joint log-radius/angular mode contributes at least

\[
\boxed{
\left[
1+rac{(2\pi n-m\beta)^2}{L^2}
\right]
\|\widetilde A_{n,m}\|_2^2
}
\]

to the radial part of the critical shell charge, before adding the positive angular-gradient cost.

The quantity

\[
\boxed{
\delta_{n,m}(\beta)
:=
2\pi n-m\beta
}
\]

is the exact **holonomy mismatch**.

---

## 5. Resonant and nonresonant modes

A joint mode is holonomy-resonant when

\[
\boxed{
2\pi n=m\beta.
}
\]

Then the extra Bloch mismatch vanishes, although the unavoidable radial `r^-1` contribution `1` remains.

If no such integer pair exists for a given low angular sector, that sector pays a strictly larger shell charge.

For principal

\[
\beta\in[-\pi,\pi],
\]

exact resonance with fixed small `m` occurs only at special rational rotation angles.

However high `|m|` can approximate irrational angles arithmetically. Such high angular modes also pay increasing angular-derivative cost, so they cannot be treated as a free low-cost approximation channel.

This creates a natural competition between:

- Diophantine holonomy mismatch;
- angular regularity cost.

No global contradiction is derived here.

---

## 6. Ordinary DSS and RSS limits

### Ordinary DSS

If

\[
\beta=0,
\]

then

\[
\delta_{n,m}=2\pi n,
\]

and the q-Fourier spectrum decouples from angular rotation.

### Continuous RSS spiral

For a pure RSS spiral there is no independent periodic modulation `n`; the continuous relation

\[
\partial_qA=-2\alpha\mathcal R_\omega A
\]

is the continuous-helical counterpart of the twisted covariant derivative.

Thus M19-126 and M19-128 are the continuous and discrete versions of the same scale-rotation geometry.

---

## 7. Add the angular Dirichlet cost

For a vector spherical harmonic of degree `ell`, angular derivatives contribute schematically

\[
\ell(\ell+1)
\]

times the mode amplitude, modulo the standard vector-harmonic shifts.

Hence the total leading shell quadratic form has the modewise structure

\[
\boxed{
\mathcal Q_{n,\ell,m}
\gtrsim
1
+
\frac{(2\pi n-m\beta)^2}{L^2}
+
 c_{ang}\ell(\ell+1).
}
\]

This shows explicitly that using high angular mode number to reduce the holonomy mismatch is not free.

---

## 8. Consequence under a shell-charge ceiling

If the spectator/Type-I corridor gives

\[
J_{shell}\le J_*,
\]

then the amplitude in strongly mismatched or high-angular modes is quantitatively limited.

For any mode,

\[
\boxed{
\|\widetilde A_{n,\ell,m}\|_2^2
\lesssim
\frac{J_*}
{1+(2\pi n-m\beta)^2/L^2+c_{ang}\ell(\ell+1)}.
}
\]

Thus a surviving RDSS tail must concentrate its critical amplitude in a finite/controlled band of low-cost Bloch-angular modes.

This is a genuine spectral narrowing of the relative-periodic hard core.

---

## 9. Why this is not yet a Liouville theorem

The lowest-cost modes still have finite positive shell charge compatible with the critical `1/r` geometry.

Nonlinear coupling and the `r^-3` correction can accommodate mode interactions at subleading order.

Therefore

\[
\boxed{
\text{Bloch mismatch positivity}
\neq
\text{RDSS nonexistence}.
}
\]

The result is a compact spectral organization of the tail, not closure.

---

## 10. Next target

The highest-value next step is to combine:

1. the positive mean cubic amplitude floor of M19-098 in the DSS case and its twisted analogue;
2. the shell quadratic spectral cost above;
3. the Type-I pointwise amplitude ceiling;

and ask whether interpolation forces a **minimum number of low-cost Bloch modes** or a finite-dimensional tail-mode compactness theorem.

That could convert the far-field RDSS hard core into a finite angular/log-Fourier mode system that can be matched to the augmented interior Fredholm problem of M19-114.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
