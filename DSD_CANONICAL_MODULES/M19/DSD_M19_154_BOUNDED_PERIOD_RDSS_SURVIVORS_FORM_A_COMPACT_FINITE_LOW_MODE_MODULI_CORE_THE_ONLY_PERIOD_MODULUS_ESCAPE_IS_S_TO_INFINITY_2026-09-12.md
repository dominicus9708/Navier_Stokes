# DSD M19-154 — Bounded-period RDSS survivors form a compact finite-low-mode/moduli core; the only period-modulus escape is S -> infinity

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / RDSS MODULI COMPACTIFICATION / ON ANY CERTIFIED BOUNDED-PERIOD CORRIDOR THE POSITIVE PERIOD FLOOR, PRINCIPAL HOLONOMY COMPACTNESS, CUBIC-TAIL FLOOR AND SHELL-H1 CEILING REDUCE THE UNRESOLVED RDSS FAMILY TO A COMPACT FINITE-DIMENSIONAL LOW-MODE HARD SET / THE ONLY REMAINING PERIOD-MODULUS NONCOMPACTNESS IS S->INFINITY, ALREADY REPRESENTED BY THE PERIODIC-ORBIT INVARIANT-MEASURE BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Intrinsic RDSS variables

Use the representation-safe parameters

\[
\boxed{
S=2\log\lambda>0,
\qquad
\beta=\operatorname{Angle}(Q_*)\in[-\pi,\pi].
}
\]

Raw angular speed is not intrinsic because of winding ambiguity.

---

## 2. Positive lower period floor

On the certified Type-I/one-slice lane, M19-097 and M19-116 give a positive lower bound against near-identity relative-periodic steps.

Write schematically

\[
\boxed{S\ge S_->0}
\]

on an unresolved survivor corridor after the externally excluded small-step region is removed.

The exact numerical dependence belongs to the imported theorem and retained smoothness constants.

---

## 3. Fix a bounded-period sector

Choose

\[
S\le S_+<\infty.
\]

Then the intrinsic moduli lie in the compact set

\[
\boxed{
(S,\beta)
\in
[S_-,S_+]\times[-\pi,\pi].
}
\]

No period or holonomy parameter can escape inside this sector.

---

## 4. Twisted low-mode structure

The RDSS scattering datum satisfies

\[
A(q+L)=Q_*^{-1}A(q),
\qquad
L=S/2.
\]

After principal-holonomy untwisting, the log-radius/angular spectrum has mismatch

\[
\boxed{
\delta_{n,m}(\beta)=2\pi n-m\beta,
}
\]

with radial frequency

\[
\frac{\delta_{n,m}(\beta)}{L}.
\]

The shell quadratic form contains a positive frequency/angular cost comparable to

\[
1+rac{\delta_{n,m}(\beta)^2}{L^2}+c_{ang}\ell(\ell+1).
\]

---

## 5. Positive tail amplitude and q-speed

The retained nontrivial singular branch carries

\[
\boxed{
\frac1L\int_0^L\int_{S^2}|A|^3d\omega dq
\ge c_3>0
}
\]

on the quantitative DSS/RDSS concentration lane.

M19-146 also gives

\[
\boxed{
\|\partial_qA\|_{X_{sc}}
\ge v_q>0.
}
\]

Thus the critical scattering datum cannot converge to zero or to a completely q-stationary history.

---

## 6. Uniform finite low-mode cutoff

On

\[
L\in[L_-,L_+],
\qquad
\beta\in[-\pi,\pi],
\]

the shell-H1 ceiling is uniform.

By the compact Sobolev embedding on

\[
S_L^1\times S^2
\]

with `L` in a compact interval, high spectral modes carry arbitrarily little `L3` mass uniformly once the cutoff is sufficiently large.

Hence there exists one finite spectral cutoff

\[
\Lambda_*
\]

valid for the entire bounded-period corridor such that

\[
\boxed{
\|P_{\le\Lambda_*}A\|\ge c_{low}>0.
}
\]

The retained tail therefore has a uniformly nontrivial finite-dimensional low-mode component.

---

## 7. Compact bounded-period tail set

Let

\[
E_{RDSS}^{low}
\]

be the finite union/bundle of low twisted Fourier-spherical modes required over the compact moduli set.

Then unresolved bounded-period tails lie in a bounded subset

\[
K_{RDSS}^{tail}
\subset
E_{RDSS}^{low}
\times[S_-,S_+]\times[-\pi,\pi]
\]

which is separated from the zero-tail set by the amplitude floor.

After closing the retained PDE constraints, the survivor subset is compact.

---

## 8. Interior hard compactness

The twisted monodromy has

\[
r_{ess}(\mathcal M_S^{tw})
\le e^{-S/4}
\le e^{-S_-/4}<1.
\]

Thus the nonstable interior hard spectral space is finite-dimensional with a uniform essential gap over the bounded-period moduli sector.

M19-131/143 give finite-radius/scattering observability on a continuous uniformly separated hard bundle.

Therefore the bounded-period RDSS problem is a coupled compact finite-dimensional interior/tail problem.

---

## 9. What remains noncompact

If no fixed upper bound `S_+` is imposed, the only intrinsic period-modulus escape is

\[
\boxed{S_n\to\infty.}
\]

Principal holonomy remains compact automatically:

\[
\beta_n\in[-\pi,\pi].
\]

M19-119 already converts long-period sequences into invariant probability measures on the rotation quotient, provided the state corridor remains compact.

Hence the full RDSS menu is naturally

\[
\boxed{
\mathcal R_{RDSS}
\subset
\mathcal R_{RDSS}^{bounded\ period,compact}
\lor
\mathcal R_{S\to\infty}^{invariant\ measure}
\lor
\mathcal G_{state\ compactness\ loss}.
}
\]

---

## 10. Consequence

Within bounded period, an unresolved RDSS sequence cannot avoid analysis by

1. period collapse;
2. holonomy escape;
3. amplitude collapse;
4. high-mode-only migration.

All such escapes have been removed or typed.

The remaining bounded-period problem is genuinely a compact nonlinear finite-dimensional relative-periodic existence problem coupled to the finite unit-spectrum problem.

---

## 11. Audit verdict

### Certified on the retained lane

- compact intrinsic moduli for bounded period;
- a uniform finite low-mode tail core;
- uniform essential spectral gap;
- reduction of period noncompactness to `S->infinity`.

### Not certified

- bounded-period RDSS nonexistence;
- long-period invariant-measure rigidity;
- unit-spectrum nonsymmetry exclusion;
- global regularity.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
