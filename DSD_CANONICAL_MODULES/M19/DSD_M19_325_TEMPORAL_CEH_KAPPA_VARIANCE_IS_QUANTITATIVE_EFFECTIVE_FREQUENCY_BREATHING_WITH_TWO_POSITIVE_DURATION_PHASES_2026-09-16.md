# M19-325 — Temporal CE-H kappa variance is quantitative effective-frequency breathing with two positive-duration phases

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / TEMPORAL BRANCH OF M19-322 / PHASE-HYSTERESIS CLASSIFICATION / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Temporal branch from the law of total variance

On the exact CE-H lane,

\[
\Delta\Omega=\kappa\Omega.
\]

Let

\[
E(s)=\|\Omega(s)\|_2^2,
\qquad
P(s)=\|\nabla\Omega(s)\|_2^2,
\]

and

\[
q_0=\int_I E(s)ds.
\]

Define the enstrophy-weighted time probability

\[
\boxed{
d\nu(s)=\frac{E(s)}{q_0}ds.
}
\]

The snapshot coefficient mean is

\[
\bar\kappa(s)
:=
\frac{\int\kappa|\Omega|^2dx}{E(s)}.
\]

Integration by parts gives

\[
\int\kappa|\Omega|^2dx
=
\int\Omega\cdot\Delta\Omega dx
=-P(s),
\]

so

\[
\boxed{
\bar\kappa(s)=-\frac{P(s)}{E(s)}\le0.
}
\]

M19-322 gives

\[
\operatorname{Var}_{\mathbb P_\Omega}(\kappa)
=
\mathbb E_\nu[\operatorname{Var}_{\pi_s}(\kappa)]
+
\operatorname{Var}_\nu(\bar\kappa).
\]

The present module treats the temporal branch

\[
\boxed{
\operatorname{Var}_\nu(\bar\kappa)\ge c_t>0.
}
\]

## 2. Two quantitative effective-frequency phases

Compactness of the normalized hard packet gives

\[
|\bar\kappa-\langle\bar\kappa\rangle_\nu|
\le M_t<\infty.
\]

Set

\[
X(s)=\bar\kappa(s)-\langle\bar\kappa\rangle_\nu.
\]

Then

\[
\mathbb E_\nu X=0,
\qquad
\mathbb E_\nu X^2\ge c_t,
\qquad
|X|\le M_t.
\]

Exactly as in M19-324, if

\[
a=\mathbb E_\nu X_+=\mathbb E_\nu X_-,
\]

then

\[
a\ge\frac{c_t}{2M_t}.
\]

Hence there are fixed

\[
\delta_t\ge\frac{c_t}{4M_t},
\qquad
m_t:=\frac{c_t}{4M_t^2}>0,
\]

such that

\[
\boxed{
\nu\!\left(\bar\kappa\ge\langle\bar\kappa\rangle_\nu+\delta_t\right)
\ge m_t,
}
\]

and

\[
\boxed{
\nu\!\left(\bar\kappa\le\langle\bar\kappa\rangle_\nu-\delta_t\right)
\ge m_t.
}
\]

Because \(\bar\kappa=-P/E\), these are two positive-weight time populations with a fixed gap in the instantaneous dissipation-to-enstrophy ratio.

## 3. Positive weighted-time mass gives positive ordinary duration

On the compact normalized packet,

\[
E(s)\le E^*<\infty,
\qquad
q_0\ge q_{0,*}>0.
\]

For any measurable time set \(A\subset I\),

\[
\nu(A)
=\frac1{q_0}\int_AE(s)ds
\le\frac{E^*}{q_{0,*}}|A|.
\]

Therefore each of the two effective-frequency phases has ordinary time duration at least

\[
\boxed{
|A_\pm|
\ge
\frac{q_{0,*}}{E^*}m_t
=:\tau_t>0.
}
\]

Thus the temporal variance cannot be carried by instantaneous spikes of vanishing duration.

## 4. Interpretation as spectral breathing

The instantaneous ratio

\[
\lambda_{eff}(s):=\frac{P(s)}{E(s)}=-\bar\kappa(s)
\]

is the enstrophy-weighted mean spatial frequency squared.

Hence M19-325 gives two positive-duration phases separated by a fixed gap:

\[
\boxed{
\lambda_{eff}
\le \bar\lambda-\delta_t
\quad\text{for a positive-duration phase},
}
\]

and

\[
\boxed{
\lambda_{eff}
\ge \bar\lambda+\delta_t
\quad\text{for another positive-duration phase}.
}
\]

The retained CE-H packet therefore undergoes quantitative effective-frequency breathing. It cannot be temporally monochromatic even if each snapshot has small spatial coefficient variance.

## 5. A transition-action lower bound under compact smoothness

Assume the compact smooth hull gives a uniform bound

\[
|\partial_s\bar\kappa(s)|\le L_t.
\]

Continuity then forces at least one transition between the two separated phases whenever both occur in one connected time interval. Any such transition changes \(\bar\kappa\) by at least \(2\delta_t\).

For an interval \(J\) containing one low-to-high transition,

\[
2\delta_t
\le
\int_J|\partial_s\bar\kappa|ds.
\]

By Cauchy--Schwarz,

\[
\boxed{
\int_J|\partial_s\bar\kappa|^2ds
\ge
\frac{4\delta_t^2}{|J|}
\ge
\frac{4\delta_t^2}{|I|}.
}
\]

This is a fixed normalized temporal phase-action payment.

It is an unsigned order-one payment and therefore does not by itself evade the M18-058--059 / M19-317 accumulation firewall.

## 6. Relation to the enstrophy equation

The enstrophy identity is

\[
\frac12E'(s)+P(s)
=
\int S\Omega\cdot\Omega dx.
\]

Dividing by \(E(s)\) on the nonzero-enstrophy packet gives

\[
\boxed{
\frac12\partial_s\log E
=
\frac{\int S\Omega\cdot\Omega}{E}
+\bar\kappa(s).
}
\]

Therefore recurrent variation of \(\bar\kappa\) can be compensated by corresponding variation of normalized stretching production while \(E\) remains recurrent/bounded.

Consequently

\[
\boxed{
\text{effective-frequency breathing}
\not\Rightarrow
\text{monotone enstrophy drift}.
}
\]

It is naturally a phase/hysteresis channel unless an additional constitutive relation slaves normalized stretching to \(\bar\kappa\).

## 7. Canonical temporal branch

The M19-322 temporal branch is sharpened to

\[
\boxed{
\mathcal T_{\kappa}^{temporal}
:
\text{two positive-duration phases of }P/E
\text{ separated by a fixed gap}.
}
\]

If smoothness is retained, crossing between them carries a fixed temporal coefficient-action charge. But ordinary compact recurrence gives only order-one repetition per fixed normalized record window, so this does not supply the record-linear multiplicity required by M19-317.

The remaining temporal closure problem is therefore not existence of coefficient motion. It is whether the CE-H PDE forces that motion to couple to a signed/nonrecyclable quantity, a supercritical multiplicity, or an already typed geometry/interface/export exit.

## 8. Conclusion

M19-322 now has two quantitatively sharpened branches:

- spatial: M19-324 gives two positive-mass transverse vortex-line coefficient populations and a gradient-or-geometry exit;
- temporal: M19-325 gives two positive-duration effective-frequency phases and temporal coefficient action/hysteresis.

Neither fixed unsigned payment alone closes the global problem.

\[
\boxed{
\text{M19-325 COMPLETE; THE NEXT TARGET IS THE COUPLED SPATIAL--TEMPORAL COEFFICIENT CURRENT, NOT ANOTHER UNSIGNED VARIANCE PAYMENT.}
}
\]
