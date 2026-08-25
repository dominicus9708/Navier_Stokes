# DSD Coherent Permanent Export: Weak-\(L^3\) Closure

Date: 2026-08-25

Status: **COHERENT FLUX-BOUNDED PASSIVE PERMANENT-EXPORT SUBCORRIDOR CLOSED CONDITIONAL ON THE ALREADY TYPED QUIETNESS HYPOTHESES / FAILURE ROUTES TO VISCOUS-FLUX, PROJECTIVE/H, MATERIAL-RADIAL TURNOVER, RESIDUAL-TAIL, OR BOUNDED-Z LOSS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The endpoint gate

`DSD_BOUNDED_Z_WEAK_L3_ENDPOINT_EXCLUSION_GATE_2026-08-25.md`

shows that a singular bounded-Z corridor cannot also remain uniformly bounded in full-time \(L^{3,\infty}\).

The remaining question is whether the **coherent quiet permanent-export conveyor** itself supplies such a weak-\(L^3\) bound.

This note shows that it does, provided the exported material cohorts retain bounded circulation/flux, bounded geometry, derivative coherence, and bounded log-shell overlap. Every failure of those properties has an existing T/H interpretation.

## 2. Birth flux is uniformly bounded

At the birth first-hitting stage of a coherent target packet,

\[
\|\Omega\|_\infty\le1.
\]

Let its normalized material cross-section satisfy

\[
|E_{birth}|\le A_0.
\]

Then its normalized directed vorticity flux obeys

\[
\boxed{
|\Phi_{birth}|
=\left|\int_{E_{birth}}\Omega\cdot e\,dA\right|
\le A_0.
}
\]

In physical units,

\[
W_jr_j^2=\nu,
\]

so the physical circulation/flux is

\[
\boxed{
\Gamma_{birth}=\nu\Phi_{birth}.
}
\]

Hence every newly born natural-scale cohort starts with an order-one normalized flux ceiling.

## 3. Material flux changes only through viscosity

For a material surface \(S(t)\), vorticity satisfies

\[
\partial_t\omega
=\nabla\times(u\times\omega)+\nu\Delta\omega.
\]

The ideal transport/stretching term is exactly the frozen-in flux transport term. Therefore the vorticity flux through a material surface changes only through the viscous defect:

\[
\boxed{
\frac{d}{dt}
\int_{S(t)}\omega\cdot n\,dA
=
\nu\int_{S(t)}\Delta\omega\cdot n\,dA.
}
\]

Equivalently, by Stokes on the material surface, the right side can be represented as a boundary circulation of derivatives of \(\omega\).

Define the absolute cumulative viscous flux variation of one cohort by

\[
\mathcal V_{\Gamma}
:=
\int
\left|
\frac{d\Gamma}{dt}
\right|dt.
\]

On the quiet non-viscous-flux branch, require

\[
\mathcal V_{\Gamma}\le C_\Gamma\nu.
\]

Then

\[
\boxed{
|\Phi(t)|
\le
\Phi_+
:=A_0+C_\Gamma.
}
\]

If this fails by repeated order-one increments, the cohort has undergone robust viscous flux changes and is routed to the existing viscous-flux/palinstrophy H ledger.

Thus \(\Phi_+\) is not inserted as an unexplained new assumption; it is the complement of the already typed viscous-flux exit.

## 4. Flux upper bound plus derivative coherence gives the critical vorticity upper envelope

Consider one escaped coherent cohort at normalized radius \(R\).

Assume its directed component

\[
f=\Omega\cdot e
\]

has one sign and its geometry has a fixed interior-thickness constant.

Assume also the non-H derivative corridor

\[
\boxed{
|\nabla\Omega|
\le K_1R^{-3}.
}
\]

Let

\[
m=\|f\|_\infty.
\]

At a point of near-maximum, Lipschitz control keeps

\[
f\ge m/2
\]

on a transverse disk portion of radius

\[
a
\asymp
\min\left\{c_gR,\frac{mR^3}{K_1}\right\}.
\]

Hence

\[
\Phi_+
\ge
\int f\,dA
\gtrsim
m a^2.
\]

If the Lipschitz radius is the active one,

\[
\Phi_+
\gtrsim
m^3\frac{R^6}{K_1^2},
\]

so

\[
m
\lesssim
(\Phi_+K_1^2)^{1/3}R^{-2}.
\]

If the geometric radius \(c_gR\) is active,

\[
\Phi_+\gtrsim mR^2,
\]

so again

\[
m\lesssim\Phi_+R^{-2}.
\]

Therefore

\[
\boxed{
\|\Omega\cdot e\|_{L^\infty(\text{cohort})}
\le
C_{\Phi,K,g}R^{-2}.
}
\]

On the coherent directional branch assume the already used alignment ratio

\[
|\Omega|\le C_\xi|\Omega\cdot e|.
\]

Then

\[
\boxed{
\|\Omega\|_{L^\infty(\text{cohort})}
\le C_\Omega R^{-2}.
}
\]

If alignment or the derivative bound fails, the event leaves the coherent lane and is routed to projective/noncoherent/H.

## 5. One cohort has a \(1/R\) velocity upper bound

A cohort has volume \(O(R^3)\), so

\[
\|\Omega_R\|_1
\le
C R^{-2}R^3
\le CR.
\]

Near its own support, Biot--Savart with the \(L^\infty\) vorticity bound on size \(R\) gives

\[
|U_R|\lesssim R^{-2}R=CR^{-1}.
\]

Away from the support at distance \(d\gtrsim R\),

\[
|U_R(Y)|
\lesssim
\frac{\|\Omega_R\|_1}{d^2}
\lesssim
\frac{R}{d^2}.
\]

Thus each bounded-flux coherent cohort has the critical velocity size expected from the passive conveyor.

## 6. Separated export events give bounded shell overlap

Take the already constructed separated positive-frequency export events with time separation

\[
\Delta s\ge S_{sep}>0.
\]

Under quiet passive dilation, their radii at a common later time satisfy a geometric ratio

\[
\boxed{
\frac{R_{m+1}}{R_m}
\ge
\lambda_{sep}
:=e^{S_{sep}/2}>1.
}
\]

A fixed number of neighboring shell-thickness factors therefore gives uniformly bounded overlap in log radius.

If cohorts catch up, merge, split radially, or lose this separation by an order-one amount, that is precisely a material/radial turnover event and leaves the pure passive-export lane.

## 7. Sum all coherent cohorts

Let \(Y\) lie at radius \(|Y|\asymp R_k\).

### Inner cohorts

For \(R_i\ll R_k\),

\[
|U_i(Y)|
\lesssim
\frac{R_i}{R_k^2}.
\]

Geometric summation gives

\[
\sum_{i<k}|U_i(Y)|
\lesssim
\frac1{R_k^2}
\sum_{i<k}R_i
\lesssim
\frac{C}{R_k}.
\]

### Outer cohorts

For \(R_i\gg R_k\), distance is comparable to \(R_i\), so

\[
|U_i(Y)|
\lesssim
R_i^{-1}.
\]

Thus

\[
\sum_{i>k}|U_i(Y)|
\lesssim
\sum_{i>k}R_i^{-1}
\lesssim
\frac{C}{R_k}.
\]

### Local neighboring cohorts

Only a fixed number overlap geometrically, and each contributes \(O(R_k^{-1})\).

Therefore the entire retained coherent export train satisfies

\[
\boxed{
|U_{train}(Y,s)|
\le
\frac{C_{train}}{1+|Y|}
}
\]

uniformly throughout the quiet full-time conveyor corridor.

Consequently

\[
\boxed{
\sup_s
\|U_{train}(s)\|_{L^{3,\infty}}
<\infty.
}
\]

## 8. The tight recurrent core/anchor is also weak-critical bounded

Inside a fixed tight ball, bounded Z and the first-hitting vorticity cap give a uniform velocity \(L^\infty\) bound by the Biot--Savart estimate in the endpoint-gate note.

For the compact/tight core vorticity contribution outside a larger fixed ball,

\[
|U_{core}(Y)|
\lesssim
|Y|^{-2}
\|\Omega_{core}\|_1,
\]

with

\[
\|\Omega_{core}\|_1
\le
|B_{R_Z}|^{1/2}Z_+^{1/2}.
\]

Thus the tight core contribution lies uniformly in \(L^{3,\infty}\) (indeed its far field is better than critical).

## 9. Full pure branch has a uniform weak-\(L^3\) bound

On the pure coherent branch, decompose

\[
U=U_{core}+U_{train}+U_{quiet,res}.
\]

If the residual is absent or satisfies the same already typed tight/passive bound, Lorentz quasi-triangle gives

\[
\boxed{
\sup_{s\ge s_0}
\|U(s)\|_{L^{3,\infty}}
\le M_*<\infty.
}
\]

This bound holds on the full late-time corridor, not merely at discrete first-hitting endpoints, because the packet flux, derivative, geometry, and separation hypotheses were imposed dynamically throughout the quiet conveyor evolution.

If an uncontrolled residual instead makes the weak-\(L^3\) norm diverge, that is isolated as the residual-tail complement rather than hidden inside the pure conveyor.

## 10. Apply the bounded-Z endpoint exclusion gate

The bounded-Z weak-\(L^3\) endpoint gate combines:

1. the internal uniform velocity \(L^\infty\) bound;
2. the logarithmic local strong-\(L^3^3\) upper bound;
3. Barker--Prange's quantitative Type-I weak-\(L^3\) singularity lower bound.

It excludes a first singular time on any full-time corridor satisfying

\[
\sup_s\|U(s)\|_{3,\infty}<\infty
\]

and bounded normalized enstrophy.

Therefore

\[
\boxed{
\text{coherent flux-bounded passive permanent-export conveyor}
\quad\text{is S-closed on the bounded-Z corridor.}
}
\]

## 11. Exact failure routes

A survivor must now violate at least one ingredient:

\[
\boxed{
\begin{aligned}
X_1&:\text{ cumulative material flux/circulation becomes unbounded}\\
&\qquad\Rightarrow\text{ viscous-flux variation/H},\\
X_2&:\text{ directional or derivative coherence fails}\\
&\qquad\Rightarrow\text{ projective/noncoherent/H},\\
X_3&:\text{ log-shell separation/finite overlap fails}\\
&\qquad\Rightarrow\text{ material/radial turnover or merging},\\
X_4&:\text{ an additional residual tail drives }\|U\|_{3,\infty}\to\infty,\\
X_5&:\text{ bounded-Z/tight recurrent corridor fails}.
\end{aligned}
}
\]

The first three are already typed T/H mechanisms.

The genuinely new residual frontier is now \(X_4\): weak-critical escalation not attributable to the coherent fixed-flux export train.

## 12. Updated final frontier

The previous last survivor

\[
\text{fixed-axis }1/R\text{ conveyor}
+
\text{transverse anchor}
\]

is no longer a terminal branch when the conveyor remains coherent, bounded-flux, derivative-controlled, and passive.

It is S-closed through the weak-\(L^3\) endpoint gate.

What remains is

\[
\boxed{
\text{residual weak-}L^3\text{ escalation}
\quad\lor\quad
\text{one of the already costed T/H failures above}.
}
\]

## 13. Audit verdict

### PROVED ON THE STATED PURE COHERENT CORRIDOR

- birth flux is uniformly bounded;
- no-viscous-flux variation preserves a fixed flux ceiling;
- flux + derivative coherence gives \(|\Omega|\lesssim R^{-2}\);
- each cohort gives \(|U|\lesssim R^{-1}\);
- separated passive cohorts have bounded log-shell overlap;
- their total field is uniformly weak-\(L^3\);
- the tight core is also weak-\(L^3\) bounded;
- bounded Z + full-time weak-\(L^3\) is excluded by the previous endpoint gate.

### ROUTED

Flux escalation, coherence loss, and shell merging return to existing viscous/projective/H/T ledgers.

### NEW OPEN RESIDUAL

\[
\boxed{
\text{uncontrolled residual tail causing }
\|U\|_{L^{3,\infty}}\to\infty.
}
\]

### GLOBAL STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
