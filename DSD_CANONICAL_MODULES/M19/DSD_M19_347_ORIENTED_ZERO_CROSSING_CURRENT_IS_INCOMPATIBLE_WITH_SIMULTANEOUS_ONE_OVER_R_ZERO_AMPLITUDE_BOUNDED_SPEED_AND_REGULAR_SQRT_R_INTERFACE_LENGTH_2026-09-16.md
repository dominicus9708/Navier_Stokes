# DSD M19-347 — Oriented zero-crossing current is incompatible with simultaneous 1/R zero-amplitude, bounded speed, and regular sqrt(R) interface length

Date: 2026-09-16  
Canonical ID: **M19-347**

Status: **ACTIVE ORIENTED-CURRENT GEOMETRY PRICING / DIFFUSE-BASELINE INTERFACE COMPLEXITY / CONDITIONAL CLOSURE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-346

On a recurrent mixed-sign material-flux component, M19-346 gives

\[
\boxed{
\langle C_0^\Phi\rangle
=-\nu\langle A_+^\Phi\rangle
=-\nu\langle A_-^\Phi\rangle.
}
\]

If the sign-resolved flux-coefficient moments remain nontrivial,

\[
\langle A_+^\Phi\rangle
=\langle A_-^\Phi\rangle
\ge a_*>0,
\]

then

\[
\boxed{
\langle C_0^\Phi\rangle\le-c_*<0,
\qquad
c_*:=\nu a_*.
}
\]

M19-340 identifies the cross-sectional current as a zero-level sweep,

\[
\boxed{
C_{0,A}^\Phi
=-\int_{Z_A}\rho v_0\,d\ell,
}
\]

where

\[
v_0=-\frac{D_t\kappa}{|\nabla\kappa|}
\]

is the material-relative normal speed of the coefficient-zero curve.

## 2. Diffuse-baseline scaling to be tested

M17-450 shows that the canonical parent-length positive-flux geometry naturally has transverse area

\[
\mathfrak A_R\gtrsim R
\]

and mean flux-weighted amplitude of order at most

\[
\overline{\mathfrak a}_{\Phi,R}\lesssim R^{-1}.
\]

A regular simply scaled cross-section of area \(\asymp R\) has a characteristic linear size

\[
\asymp R^{1/2}.
\]

The present module asks whether the oriented current of M19-346 can be supported if the zero separator is simultaneously:

1. at the diffuse amplitude scale \(\rho\lesssim R^{-1}\);
2. moving with uniformly bounded normalized speed;
3. geometrically regular with total zero-curve length \(O(R^{1/2})\).

## 3. Elementary current bound

At one time,

\[
|C_{0,A}^\Phi|
\le
\|\rho\|_{L^\infty(Z_A)}
\|v_0\|_{L^\infty(Z_A)}
\mathcal H^1(Z_A).
\]

Assume

\[
\boxed{
\|\rho\|_{L^\infty(Z_A)}
\le
\frac{C_\rho}{R},
}
\]

\[
\boxed{
\|v_0\|_{L^\infty(Z_A)}
\le V_*,
}
\]

and

\[
\boxed{
\mathcal H^1(Z_A)
\le C_ZR^{1/2}.
}
\]

Then

\[
\boxed{
|C_{0,A}^\Phi|
\le
C_\rho V_*C_ZR^{-1/2}.
}
\]

Hence

\[
\boxed{
|C_{0,A}^\Phi|\to0.
}
\]

## 4. Invariant-mean contradiction under uniform regular-baseline geometry

If the three bounds of Section 3 hold uniformly on the recurrent component for sufficiently late records, then dominated averaging gives

\[
|\langle C_0^\Phi\rangle|
\lesssim R^{-1/2}\to0.
\]

This contradicts M19-346 whenever

\[
|\langle C_0^\Phi\rangle|
\ge c_*>0.
\]

Therefore the following four properties cannot all coexist on the nontrivial recurrent mixed-sign branch:

\[
\boxed{
\begin{aligned}
&\text{fixed nonzero oriented mean sign current},\\
&\rho|_{Z_A}=O(R^{-1}),\\
&|v_0|=O(1),\\
&\mathcal H^1(Z_A)=O(R^{1/2}).
\end{aligned}
}
\]

## 5. Quantitative interface-length lower bound

Suppose instead that

\[
|C_{0,A}^\Phi|\ge c_0>0
\]

at a retained time while

\[
\rho|_{Z_A}\le C_\rho/R,
\qquad
|v_0|\le V_*.
\]

Then necessarily

\[
\boxed{
\mathcal H^1(Z_A)
\ge
\frac{c_0}{C_\rho V_*}R.
}
\]

Thus an order-one oriented current at diffuse zero-amplitude requires total zero-interface length of order \(R\), not the \(R^{1/2}\) length suggested by one regular separator across an area-\(R\) cross-section.

## 6. Interface-complexity ratio

Define the scale-free zero-interface complexity ratio

\[
\boxed{
\mathfrak C_{0,R}
:=
\frac{\mathcal H^1(Z_A)}{\mathfrak A_R^{1/2}}.
}
\]

On the minimal diffuse geometry

\[
\mathfrak A_R\asymp R.
\]

If the current is order one, zero amplitude is \(O(R^{-1})\), and speed remains bounded, then Section 5 gives

\[
\boxed{
\mathfrak C_{0,R}
\gtrsim
R^{1/2}.
}
\]

Hence the zero set must become increasingly labyrinthine/multicomponent relative to the natural transverse size.

This is a genuine shape/interface-complexity escalation, distinct from the baseline area growth of M17-450.

## 7. Equivalent escape thresholds

More generally write the scale laws

\[
\rho|_{Z_A}\sim R^{-a},
\qquad
|v_0|\sim R^b,
\qquad
\mathcal H^1(Z_A)\sim R^c.
\]

An order-one current requires

\[
\boxed{
-a+b+c\ge0.
}
\]

At the diffuse amplitude baseline \(a=1\) and regular interface scale \(c=1/2\), one needs

\[
\boxed{b\ge1/2.}
\]

Thus if the zero interface remains geometrically regular, its material-relative speed must grow at least like \(R^{1/2}\).

Alternatively, with bounded speed \(b=0\) and regular interface \(c=1/2\), one needs

\[
\boxed{a\le1/2,}
\]

meaning zero-level amplitude at least of order \(R^{-1/2}\), much larger than the \(R^{-1}\) diffuse baseline.

## 8. Relation to M17-446--447 and M19-340--343

A zero-level amplitude increase toward \(R^{-1/2}\) or larger reduces the low-amplitude firewall and moves the branch back toward the M17-447 robust-bottleneck / palinstrophy architecture.

A speed growth \(R^{1/2}\) or larger is an explicit zero-level speed/high-jet decompactification of the type retained by M19-340.

An interface length \(R\) or larger is a scale-free zero-set complexity/topology degeneration rather than baseline transverse size growth.

Thus the M19-346 oriented current cannot be hidden inside the ordinary M17-450 diffuse geometry without paying one of these stronger effects.

## 9. Important scope firewall

M17-450 proves an arclength-averaged amplitude scale, not the pointwise zero-level ceiling

\[
\rho|_{Z_A}\le C/R.
\]

Likewise it does not prove a regular-interface length ceiling or a bounded zero-level speed.

Therefore M19-347 is a **conditional geometry-pricing theorem**, not a closure of the full mixed-sign branch.

Its value is to identify the exact excess quantities that a persistent oriented current must generate beyond the diffuse baseline.

## 10. Updated oriented-current branch

\[
\boxed{
\begin{aligned}
H_{\langle C_0^\Phi\rangle\ne0}
\Longrightarrow{}&
G_{\rm zero\text{-}level\ amplitude\ concentration}\\
&\lor G_{\rm zero\text{-}level\ speed/high\text{-}jet\ growth}\\
&\lor G_{\rm zero\text{-}interface\ complexity/length\ escalation}\\
&\lor G_{\rm sign\ flux\text{-}moment\ thinning}\\
&\lor G_{\rm chart/topology/genealogy\ loss}.
\end{aligned}
}
\]

## 11. Audit verdict

**PASS as a conditional current-pricing theorem.**

An order-one recurrent oriented zero-crossing current is incompatible with simultaneously baseline-diffuse zero amplitude, bounded crossing speed, and a regular one-scale zero interface. Under baseline amplitude and bounded speed it forces interface length \(\Omega(R)\), i.e. \(\Omega(R^{1/2})\) excess complexity relative to an area-\(R\) regular separator.

The next step is to test the complementary sparse-residence branch and determine whether snapshot algebra already admits a sharp scaling survivor before spending effort on a false rigidity target.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
