# M19-059 — The critical pressure map is a log-radius translation-equivariant elliptic convolution off the l=1 neutral mode, and an aperiodic toroidal anti-model can avoid that neutral sector by parity

**Date:** 2026-09-12  
**Status:** CALCULATION / R-CRITICAL NONLOCAL PRESSURE TEST / LOG-RADIUS ELLIPTIC FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-055--058 removed several local finite-radius observables as automatic rigidity mechanisms for the recurrent weak-critical scattering datum

\[
U_0=r^{-1}A(q,\omega),
\qquad q=\log r-\theta/2.
\]

Pressure is different because it is nonlocal.  The Poisson equation couples angular sectors and different radii, so it is a natural candidate for a genuine constraint on the full \(q\)-history.

This module derives the exact log-radius pressure operator.  Away from one neutral angular sector it is a translation-equivariant constant-coefficient elliptic convolution in \(q\), so it preserves aperiodic recurrent histories rather than forcing periodicity.  The only neutral pressure sector is \(\ell=1\), and an explicit odd-parity toroidal leading datum has even quadratic pressure forcing and therefore does not excite that neutral sector.

Thus the ordinary pressure map does not close the recurrent toroidal branch.

## 2. Pressure Poisson equation

Taking divergence of the incompressible similarity momentum equation gives the same pressure Poisson equation as in physical variables:

\[
\boxed{
-\Delta P
=\partial_i\partial_j(U_iU_j).
}
\]

The linear similarity terms do not contribute because \(\nabla\cdot U=0\).

For the critical leading field

\[
U_0=r^{-1}A(q,\omega),
\]

the quadratic source has the form

\[
\boxed{
\partial_i\partial_j(U_{0i}U_{0j})
=r^{-4}F[A](q,\omega),
}
\]

where \(F[A]\) is quadratic in \(A\) and its angular/logarithmic derivatives.

The critical pressure ansatz is

\[
\boxed{
P_0=r^{-2}\Pi(q,\omega).
}
\]

## 3. Exact log-radius pressure operator

For a scalar field of the form

\[
r^{-2}\Pi(q,\omega),
\qquad q=\log r-\theta/2,
\]

a direct spherical-coordinate computation gives

\[
\boxed{
\Delta\left(r^{-2}\Pi\right)
=
r^{-4}
\left(
\partial_q^2-3\partial_q+2+\Delta_{S^2}
\right)\Pi.
}
\]

Therefore the leading pressure equation is

\[
\boxed{
-\left(
\partial_q^2-3\partial_q+2+\Delta_{S^2}
\right)\Pi
=F[A].
}
\]

This equation is autonomous under translations

\[
q\mapsto q+s.
\]

Hence the pressure map commutes with the scattering translation flow whenever the required bounded solution is uniquely selected.

## 4. Spherical-harmonic decomposition

Write

\[
\Pi(q,\omega)
=\sum_{\ell,m}\Pi_{\ell m}(q)Y_{\ell m}(\omega),
\]

\[
F[A](q,\omega)
=\sum_{\ell,m}F_{\ell m}(q)Y_{\ell m}(\omega).
\]

Since

\[
\Delta_{S^2}Y_{\ell m}
=-\ell(\ell+1)Y_{\ell m},
\]

each angular mode satisfies

\[
\boxed{
\mathcal L_\ell\Pi_{\ell m}
=F_{\ell m},
}
\]

with

\[
\begin{aligned}
\mathcal L_\ell
&:=-\partial_q^2+3\partial_q+\ell(\ell+1)-2\\
&=
-\bigl(\partial_q-(\ell+2)\bigr)
\bigl(\partial_q-(1-\ell)\bigr).
\end{aligned}
\]

The two homogeneous exponents are therefore

\[
\boxed{
\mu_+=\ell+2,
\qquad
\mu_-=1-\ell.
}
\]

## 5. Hyperbolic angular sectors are translation-equivariant convolutions

For \(\ell\ge2\),

\[
\mu_+>0,
\qquad
\mu_-<0.
\]

Thus the bounded whole-line inverse has an exponentially localized Green kernel.  Schematically,

\[
\boxed{
\Pi_{\ell m}(q)
=
(G_\ell*F_{\ell m})(q),
}
\]

with

\[
G_\ell(s)
\sim
\begin{cases}
 e^{-(\ell-1)s},&s>0,\\
 e^{(\ell+2)s},&s<0.
\end{cases}
\]

The precise normalization is irrelevant for the present structural conclusion.

For \(\ell=0\), both characteristic exponents are positive, but each first-order factor still has a bounded one-sided inverse on bounded/recurrent data after the physical pressure selection is fixed.  Again the operation is translation equivariant in \(q\).

Therefore, in all non-neutral sectors,

\[
\boxed{
F(q)\text{ recurrent/aperiodic}
\Longrightarrow
\Pi(q)\text{ recurrent/aperiodic}
}
\]

in general.  Elliptic nonlocality smooths and mixes the history but does not force it to become periodic or constant.

## 6. The exceptional l=1 neutral pressure mode

For \(\ell=1\),

\[
\boxed{
\mathcal L_1
=-\partial_q(\partial_q-3).
}
\]

There is a neutral homogeneous mode

\[
\Pi_{1m}(q)=\text{constant}.
\]

Consequently a bounded whole-line solution for arbitrary recurrent forcing cannot be asserted by the same hyperbolic Green-kernel argument without a compatibility/coboundary condition on the \(\ell=1\) forcing.

This is the only angular sector in which the leading pressure equation itself contains a zero log-frequency mode.

However this does **not** yield a general rigidity theorem for \(A\).  One must still show that every nonzero recurrent scattering state necessarily excites an incompatible \(\ell=1\) pressure source.  That statement is false at the leading-order level, as the next section shows.

## 7. An explicit aperiodic toroidal datum avoids the neutral pressure sector

Fix a constant vector \(a\neq0\) and choose

\[
\boxed{
A(q,\omega)
=b(q)\,a\times\omega,
}
\]

where, for example,

\[
\boxed{
b(q)=\sin q+\frac12\sin(\sqrt2\,q).}
\]

This is a smooth bounded aperiodic/quasiperiodic pure toroidal leading datum.

It is odd under spatial inversion:

\[
A(q,-\omega)=-A(q,\omega).
\]

Hence the quadratic tensor is even:

\[
A\otimes A(q,-\omega)
=A\otimes A(q,\omega).
\]

The pressure source

\[
\partial_i\partial_j(U_{0i}U_{0j})
\]

contains two spatial derivatives.  Two derivatives preserve parity, so the resulting angular pressure forcing is even.

Therefore only even spherical-harmonic degrees occur in the leading pressure source:

\[
\boxed{
F_{\ell m}=0
\qquad\text{for odd }\ell.
}
\]

In particular,

\[
\boxed{F_{1m}=0.}
\]

Thus this aperiodic toroidal anti-model completely avoids the only neutral pressure sector.

## 8. Quasiperiodic log frequencies survive the pressure inverse

The quadratic source generated by the chosen \(b(q)\) contains frequencies such as

\[
0,
\quad
2,
\quad
2\sqrt2,
\quad
1+\sqrt2,
\quad
|1-\sqrt2|.
\]

In every excited even angular sector the operator \(\mathcal L_\ell\) has no zero log-frequency obstruction relevant to those harmonics.  Its bounded inverse acts by a finite Fourier multiplier on each quasiperiodic frequency.

Therefore the pressure response remains quasiperiodic rather than collapsing to a periodic/constant state:

\[
\boxed{
A\text{ aperiodic quasiperiodic}
\Longrightarrow
F[A]\text{ quasiperiodic}
\Longrightarrow
\Pi\text{ quasiperiodic}.
}
\]

This is a leading-order compatibility construction, not an exact Navier--Stokes solution.

## 9. Consequence for nonlocal pressure rigidity

The pressure map is genuinely nonlocal in radius, but its nonlocality has the wrong structural form for the desired rigidity.  In log radius it is mostly a translation-equivariant convolution.

Translation-equivariant convolution preserves the recurrent hull:

\[
\boxed{
\Pi_{\sigma_sA}
=\sigma_s\Pi_A.
}
\]

Hence pressure does not by itself select a privileged \(q\)-phase or identify distant phases of an aperiodic recurrent history.

The only possible leading exception is the \(\ell=1\) neutral mode, but the explicit toroidal parity example shows that this mode is not universally excited.

Thus

\[
\boxed{
\text{ordinary critical pressure coupling does not supply the missing global }q\text{-rigidity.}
}
\]

## 10. Relation to previous M19 firewalls

The tested mechanisms now include:

- scalar finite-radius energy balance;
- angular momentum;
- all fixed-degree polynomial momentum moments;
- helicity;
- nonlocal leading pressure response.

None forces the recurrent aperiodic toroidal datum to become periodic or vanish.

The common reason is increasingly clear:

\[
\boxed{
\text{the leading critical sector is a translation dynamical system in }q,
}
\]

and all tested local/elliptic observables are equivariant under that same translation rather than breaking it.

## 11. Certified / not certified

### Certified

1. Exact log-radius pressure operator for \(P_0=r^{-2}\Pi\).
2. Spherical-harmonic factorization
   \[
   \mathcal L_\ell
   =-(\partial_q-(\ell+2))(\partial_q-(1-\ell)).
   \]
3. Exponentially localized translation-equivariant bounded pressure inversion in the hyperbolic sectors \(\ell\ge2\).
4. Identification of \(\ell=1\) as the unique neutral pressure sector.
5. Construction of a smooth aperiodic pure-toroidal leading datum whose quadratic pressure source is even and therefore has no \(\ell=1\) component.
6. Therefore the leading pressure equation does not generically eliminate aperiodic recurrent critical scattering.

### Not certified

1. Exact Navier--Stokes realization of the displayed anti-model.
2. Absence of a deeper core-tail pressure compatibility involving the non-asymptotic interior.
3. Global unique continuation from the interior to the complete recurrent boundary history.
4. Global 3D Navier--Stokes regularity.

## 12. Next target

After M19-059, ordinary local conservation laws and the leading elliptic pressure map have both failed to break log-translation symmetry.

The next calculation should therefore target a genuinely **global interior-to-boundary constraint**, not another local moment.  Two concrete options remain:

1. a core-tail pressure/stress pairing after subtracting the translation-equivariant far-tail response;
2. a unique-continuation / observability estimate asking whether one compact recurrent interior trajectory can support an arbitrary aperiodic \(q\)-boundary history.

M19-060 should first isolate the pressure into

\[
\Pi=\Pi_{tail}[A]+\Pi_{core}
\]

and determine the decay/multipole structure of \(\Pi_{core}\) at large radius.  If the core contribution is only a finite-dimensional exponentially decaying multipole in \(q\), it cannot rigidify an infinite-dimensional recurrent tail and the frontier can be stated as a genuine global observability theorem.

---

\[
\boxed{\text{M19-059 COMPLETE; LEADING NONLOCAL PRESSURE IS TRANSLATION EQUIVARIANT AND DOES NOT GENERICALLY CLOSE APERIODIC WEAK-CRITICAL SCATTERING.}}
\]
