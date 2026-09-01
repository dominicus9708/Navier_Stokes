# DSD M5-543 — One finite similarity radius captures all positive active marks on the recurrent hard component

Date: 2026-09-01

Status: **FINITE-CORE LOCALIZATION / M5-542 SHOWS THAT THE ADAPTIVE ENDPOINT DUST HAS VANISHING CUMULATIVE EFFECT ON A FIXED ACTIVE WINDOW / M5-535 AND ENSTROPHY TIGHTNESS ALSO MAKE GLOBAL AXIAL PRODUCTION FROM THE FAR EXTERIOR UNIFORMLY VANISH / ON THE COMMON ERGODIC COMPONENT FROM M5-514, ONE CAN THEREFORE CHOOSE A SINGLE FINITE RADIUS `R_core` SUCH THAT THE LOCAL AXIAL-PRODUCTION MEAN REMAINS STRICTLY POSITIVE AND ALL RETAINED DUAL/RATCHET MATERIAL MARKS LIE INSIDE THE SAME CORE WINDOW, WHILE THE EXTERIOR CONTRIBUTES LESS THAN ANY PRESCRIBED FRACTION OF THE MARK THRESHOLDS / THE NON-L3 TAIL IS THUS LOGICALLY SEPARATED FROM THE ACTIVE SINGULAR MECHANISM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Common ergodic component

M5-514 selected an ergodic invariant component `nu_*` carrying simultaneously

\[
\boxed{
\langle Q\rangle_{\nu_*}>0,
}
\]

\[
\boxed{
\langle a_{rat}\rangle_{\nu_*}>0,
}
\]

and recurrent dual-source activity.

Write

\[
\boxed{
q_*:=\langle Q\rangle_{\nu_*}>0.
}
\]

The present note works entirely on this component.

---

## 2. Exterior axial production vanishes uniformly

Let

\[
Q_{>R}(Y)
:=
\int_{|y|>R}
W_Y\cdot\Sigma_YW_Ydy.
\]

By M5-535,

\[
\varepsilon_\Sigma(R)
:=
\sup_{Y\in\widehat{\mathfrak H}}
\sup_{|y|>R}|\Sigma_Y(y)|
\to0.
\]

Also

\[
E_{tail}(R)
:=
\sup_Y\int_{|y|>R}|W_Y|^2dy
\to0.
\]

Therefore

\[
|Q_{>R}(Y)|
\le
\varepsilon_\Sigma(R)E_{tail}(R),
\]

so

\[
\boxed{
\sup_Y|Q_{>R}(Y)|\to0.
}
\]

This is stronger than merely saying that the far tail has small influence on a preselected marker.

It says the far exterior carries asymptotically no global axial-production budget of its own.

---

## 3. Positive production survives in one finite ball

Define

\[
Q_{<R}(Y)
:=
\int_{|y|<R}
W_Y\cdot\Sigma_YW_Ydy.
\]

Since

\[
Q=Q_{<R}+Q_{>R},
\]

we have

\[
\left|
\langle Q_{<R}\rangle_{\nu_*}
-q_*
\right|
\le
\sup_Y|Q_{>R}(Y)|.
\]

Choose `R_prod<infinity` so large that

\[
\sup_Y|Q_{>R_prod}(Y)|
\le q_*/2.
\]

Then

\[
\boxed{
\langle Q_{<R_prod}\rangle_{\nu_*}
\ge q_*/2>0.
}
\]

Thus the positive axial-production requirement is realized inside one finite similarity radius.

---

## 4. Uniform spatial support of the marked material events

The M5-485 marked hull was built only after retaining active-vorticity lower thresholds and convergent Lagrangian trajectories on the normalized marked intervals.

The set of central marked trajectories over one roof interval is therefore compact in the product hull.

Hence there exists

\[
R_{mark}<\infty
\]

such that every retained active material marker participating in the ratchet mark stays inside

\[
B_{R_{mark}}
\]

throughout its marked normalized interval.

The same applies to the coherent carrier balls used to define the M5-490 persistent dual-pair mark after the finite-label compact extraction.

Thus the dual and ratchet marks are not supported by material structures whose centers escape to infinity inside the compact hard component.

---

## 5. One common finite core radius

Set

\[
\boxed{
R_{core}
:=
\max\{R_{prod},R_{mark},4L_{act}\},
}
\]

with a harmless further enlargement chosen below.

Then

1. the local axial-production mean satisfies
   \[
   \boxed{
   \langle Q_{B_{R_core}}\rangle
   \ge q_*/2>0;
   }
   \]
2. all retained dual-pair carrier marks lie inside `B_(R_core)`;
3. all retained ratchet material intervals lie inside `B_(R_core)`;
4. all fixed-lineage coherent balls used in the active mark package lie inside the same radius.

Thus the three positive mechanisms live in one finite normalized region.

---

## 6. Exterior cumulative errors can be made smaller than every mark threshold

Let the positive ratchet action threshold be

\[
a_0>0
\]

and let the dual geometry carry fixed flux/angle thresholds

\[
\phi_0>0,
\qquad
s_0>0.
\]

M5-542 gives uniformly

\[
\int_{I_Y}
\|\Sigma_{>R}\|_{L^\infty(B_{R_mark})}d\theta
\to0,
\]

and similarly for remote velocity and higher harmonic jets.

Therefore enlarge `R_core` once more so that every remote cumulative error relevant to the marked event definitions is less than a chosen fraction, for example

\[
\boxed{
\varepsilon_{remote}
<
\frac1{100}
\min\{a_0,\phi_0,s_0,q_*\}.
}
\]

This single radius works uniformly on the entire recurrent component.

---

## 7. The active marks cannot be reassigned to the spectator tail

After the radius is fixed, the exterior tail may still carry

\[
\int |y||W|^2=\infty
\]

and may still be responsible for

\[
U\notin L^3.
\]

But it cannot supply an order-one fraction of

- the positive local axial-production mean;
- the projective ratchet action;
- the coherent dual-source angle/flux event;
- or the finite-lineage local deformation budget.

Any attempt to assign one of these positive marks to the exterior changes the corresponding quantity by at most `epsilon_remote`, which is below the retained threshold.

Hence the active marks survive after removing the remote contribution from their ledgers.

---

## 8. Core/tail logical factorization

The recurrent hard object now factorizes at the level needed by the proof audit:

\[
\boxed{
\mathcal H_{hard}
=
\mathcal C_{active}(R_{core})
+
\mathcal T_{endpoint},
}
\]

where

### Active core

`C_active(R_core)` contains

\[
\boxed{
\begin{aligned}
&\langle Q_{B_{R_core}}\rangle>0,\\
&\text{positive ratchet frequency},\\
&\text{persistent noncollinear dual-pair activity},\\
&\text{finite persistent lineage network}.
\end{aligned}
}
\]

### Endpoint tail

`T_endpoint` contains

\[
\boxed{
\begin{aligned}
&U\in\bigcap_{p>3}L^p\setminus L^3,\\
&\text{adaptive weighted }L3\text{ control},\\
&\mathcal M_1=\infty,\\
&\text{vanishing amplitude and strain at infinity},\\
&\text{vanishing cumulative core action per generation}.
\end{aligned}
}
\]

The second component is analytically critical but dynamically passive with respect to the retained active marks.

---

## 9. Important autonomy firewall

M5-543 does **not** claim that the restriction of the Navier--Stokes solution to `B_(R_core)` is an autonomous closed PDE.

The exterior still supplies boundary and harmonic data.

What has been proved is weaker and exactly what is currently needed:

\[
\boxed{
\text{the exterior contribution to every fixed positive active threshold can be made uniformly arbitrarily small.}
}
\]

A future localized cocycle or rigidity inequality with a strict gap larger than the exterior error would therefore survive in the full equation.

This is an approximate-decoupling statement, not an illegal truncation of Navier--Stokes.

---

## 10. Updated proof frontier

The previous two hard structures were

\[
\text{endpoint tail}
+
\text{finite recurrent active core}.
\]

M5-543 shows they no longer need to be solved simultaneously in order to understand the active singular mechanism.

The next rigidity calculation can be performed on the finite active region with exterior errors retained explicitly as an arbitrarily small perturbation.

Thus the highest-value target returns to the M5-515--519 finite-lineage geometry, now with the major nonlocal-tail ambiguity removed.

---

## 11. Highest-value next target

Construct a localized bounded observable on `B_(R_core)` whose one-generation balance has the form

\[
\boxed{
\Phi_{j+1}-\Phi_j
\ge
D_{active,j}
-
\varepsilon_{remote},
}
\]

where

\[
D_{active,j}\ge d_0>0
\]

on every unavoidable active pair/ratchet event.

Since `epsilon_remote` can be fixed below `d_0/2`, such an observable would become the strict cocycle sought since M5-485.

The natural candidates should now be re-audited **locally**, because their previous global failure could include endpoint-tail boundary defects that have now been isolated.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]