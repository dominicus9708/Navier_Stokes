# DSD M19-265 — Finite physical energy allows a normalized r^{-1} critical tail to expand to radius r_j^{-1} and explains the strong-L3 / weak-L3 gap

Date: 2026-09-15  
Canonical ID: **M19-265**  
Status: **ACTIVE LOW-FREQUENCY ECONOMICS / FINITE-ENERGY NO-GO / CRITICAL TAIL COMPATIBILITY / STRONG-L3 VS WEAK-L3 GAP EXPLAINED BY SCALE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-264 showed abstractly that Navier--Stokes dilation preserves CE-H while vorticity enstrophy decays and kinetic energy shifts toward low frequency.

The next candidate non-scale-covariant control is the finite kinetic energy of the original physical solution.

This module computes its exact first-hitting economics and shows:

\[
\boxed{
\text{finite original kinetic energy does not by itself remove the normalized critical }|y|^{-1}\text{ tail.}
}
\]

In fact the allowed normalized \(L^2\) growth matches the linear radial cost of such a tail exactly.

---

## 2. Physical-to-first-hitting energy scaling

Use the decaying whole-space gauge and suppress a nonzero Galilean constant in global \(L^2\) accounting.

At first-hitting stage \(j\), define

\[
V_j(y,\tau)
=
\frac{r_j}{\nu}
 u(X_j+r_jy,t_j+r_j^2\tau/\nu).
\]

At a fixed corresponding time,

\[
\begin{aligned}
\|V_j\|_2^2
&=
\int
\frac{r_j^2}{\nu^2}
|u(X_j+r_jy)|^2dy\\
&=
\frac{1}{\nu^2r_j}
\|u\|_2^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\|V_j\|_2^2
=
\frac{E_{kin}(t)}{\nu^2r_j}.
}
\]

If the original Leray/strong solution has a finite energy ceiling

\[
E_{kin}(t)\le E_0,
\]

then only

\[
\boxed{
r_j\|V_j\|_2^2\le E_0/\nu^2}
\]

is inherited uniformly.

The unweighted normalized kinetic energy may grow like \(r_j^{-1}\).

---

## 3. Critical 1/r tail has exactly linear L2 radial cost

Consider a normalized far-field profile of the M19-198 / scattering type

\[
V_{tail}(y)
\approx
\frac{A(\log|y|,\omega)}{|y|},
\qquad
\omega=y/|y|,
\]

with a nondegenerate angular/logarithmic amplitude on a positive portion of the sphere.

Ignoring fixed angular factors, its kinetic energy between radii \(1\) and \(R\) scales as

\[
\begin{aligned}
\int_{1<|y|<R}|V_{tail}|^2dy
&\sim
\int_1^R r^{-2}r^2dr\\
&\sim R.
\end{aligned}
\]

Hence

\[
\boxed{
E_{tail}^{norm}(R)\asymp R.
}
\]

This is exactly the growth order permitted by the first-hitting energy bound when

\[
R\asymp r_j^{-1}.
\]

---

## 4. Why radius r_j^{-1} is physically natural

A normalized radius \(R\) corresponds to physical radius

\[
\ell_{phys}=r_jR.
\]

Thus

\[
R\asymp r_j^{-1}
\]

corresponds to a fixed macroscopic physical radius

\[
\ell_{phys}\asymp1
\]

in the chosen reference units.

Therefore a normalized critical tail can occupy the enormous interval

\[
1\ll|y|\ll r_j^{-1}
\]

while still living inside only a fixed-size physical region around the singular point.

Its normalized energy is

\[
O(r_j^{-1}),
\]

which becomes physical energy

\[
r_j\,O(r_j^{-1})=O(1).
\]

Thus no energy contradiction occurs.

---

## 5. Strong L3 cost is logarithmic

For the same tail,

\[
\begin{aligned}
\int_{1<|y|<R}|V_{tail}|^3dy
&\sim
\int_1^Rr^{-3}r^2dr\\
&=\int_1^R\frac{dr}{r}\\
&\sim\log R.
\end{aligned}
\]

At \(R\asymp r_j^{-1}\),

\[
\boxed{
\|V_j\|_{L^3(1<|y|<r_j^{-1})}^3
\sim
\log\frac1{r_j}
}
\]

for a nondegenerate persistent critical tail.

Hence a finite-energy singularity corridor may fail to have a uniform strong \(L^3\) bound precisely by logarithmic accumulation over expanding normalized radii.

This is compatible with the Escauriaza--Seregin--Šverák endpoint firewall recorded in M19-262: the strong \(L_t^\infty L_x^3\) theorem cannot be imported from a bounded Lorentz weak-\(L^3\) tail.

---

## 6. Weak-L3 remains scale invariant

The distribution function of a \(1/r\) tail satisfies schematically

\[
|\{|V_{tail}|>\lambda\}|
\asymp
\lambda^{-3}
\]

inside its active scaling range.

Therefore

\[
\boxed{
\sup_{\lambda>0}
\lambda^3
|\{|V_{tail}|>\lambda\}|
\asymp O(1),
}
\]

so

\[
\boxed{
\|V_{tail}\|_{L^{3,\infty}}
\asymp O(1).
}
\]

The tail can therefore have simultaneously:

\[
\text{finite physical kinetic energy},
\]

\[
\text{bounded normalized spatial weak-}L^3,
\]

and

\[
\text{normalized strong }L^3\text{ growing like }(\log r_j^{-1})^{1/3}.
\]

This exactly matches the historical R-critical / weak-L3 firewall.

---

## 7. Comparison with M19-198

M19-198 found that the leading scattering tail

\[
U_0(y,s)
=
\frac1rA(\log r-s/2,\omega)
\]

transports its weak-L3 size isometrically under similarity translation.

The present calculation adds the physical energy interpretation:

\[
\boxed{
\text{persistent normalized weak-L3 tail}
+
\text{linear normalized L2 radial growth}
}
\]

is exactly compatible with finite original kinetic energy because the first-hitting conversion contributes the factor \(r_j\).

Thus the weak-L3 persistence is not merely a functional-analysis endpoint issue; it is the natural critical-tail geometry allowed by the physical energy budget.

---

## 8. Finite energy therefore does not supply T_CEH^LF

M19-263 proposed a possible low-frequency closure through kinetic-energy inheritance.

The exact inherited information is only

\[
\boxed{
r_j\|V_j\|_2^2\lesssim1,}
\]

not

\[
\sup_j\|V_j\|_2<\infty.
\]

Consequently finite physical energy does not prevent

\[
\|V_j\|_2^2\asymp r_j^{-1}
\]

and does not force the extracted ancient profile to lie in a globally finite-energy class with tight low-frequency mass.

Therefore

\[
\boxed{
\text{physical finite energy alone}
\not\Rightarrow
\mathcal T_{CEH}^{LF}.
}
\]

---

## 9. Exact remaining low-frequency requirement

To eliminate the critical tail one needs a strict improvement over the energy-compatible linear law.

For example any one of the following would be decisive or strongly useful:

1. normalized kinetic-energy sublinear growth
   \[
   \boxed{
   \int_{|y|<R}|V|^2=o(R)
   }
   \quad(R\to\infty);
   \]
2. uniform strong-L3 control
   \[
   \sup_s\|V(s)\|_3<\infty;
   \]
3. quantitative tail tightness excluding a nonzero \(1/r\) coefficient;
4. a low-frequency \(\dot H^{-1}\) bound uniform under the first-hitting normalization;
5. a physical realization theorem showing that the critical tail cannot persist to the required macroscopic radius.

Each is stronger than finite kinetic energy and attacks the existing R-critical root directly.

---

## 10. New tail coefficient target

For the leading critical tail

\[
U_0(y,s)=r^{-1}A(q,\omega),
\qquad q=\log r-s/2,
\]

define an angular/logarithmic tail intensity schematically by

\[
\mathfrak A(q)
=
\int_{S^2}|A(q,\omega)|^2d\omega.
\]

Then the normalized kinetic energy accumulated over a logarithmic radial interval satisfies

\[
\frac{d}{dR}E_{tail}^{norm}(R)
\sim
\mathfrak A(\log R).
\]

Finite physical energy permits a bounded nonzero mean of \(\mathfrak A\) because it only produces linear \(R\)-growth in normalized coordinates.

Thus the natural stronger target is not mere boundedness but

\[
\boxed{
\frac1R
\int_1^R\mathfrak A(\log r)dr
\to0
}
\]

or another condition forcing sublinear normalized kinetic-energy growth.

This is a precise tail-tightness strengthening of the R-critical problem.

---

## 11. Permanent firewalls after M19-265

\[
\boxed{
\text{finite physical energy}
\neq
\text{uniform normalized }L^2\text{ energy}.
}
\]

\[
\boxed{
|y|^{-1}\text{ critical tail to }R\sim r_j^{-1}
\text{ is compatible with finite physical energy}.
}
\]

\[
\boxed{
L^{3,\infty}\text{ boundedness}
\neq
L^3\text{ boundedness};
\text{ the gap is logarithmic for a }1/r\text{ tail}.
}
\]

\[
\boxed{
\text{finite energy cannot by itself remove the R-critical low-frequency/tail root}.
}
\]

---

## 12. Immediate next target

Audit whether the upstream W1/scattering construction already controls the **mean square critical-tail coefficient** strongly enough to improve the linear normalized kinetic-energy law to sublinear growth.

If not, the next possible non-scale-covariant inputs are vorticity moment/cancellation conditions or a physical terminal realization theorem.

Global 3D Navier--Stokes regularity remains unproved.
