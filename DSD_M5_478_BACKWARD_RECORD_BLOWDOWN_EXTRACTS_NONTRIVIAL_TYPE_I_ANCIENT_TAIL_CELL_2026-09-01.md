# DSD M5-478 — Backward record blow-down extracts a nontrivial Type-I ancient tail cell

Date: 2026-09-01

Status: **SECOND-GENERATION ANCIENT EXTRACTION / BLOWING DOWN THE M5-477 MARKED ANCIENT ELEMENT AT ITS SATURATED BACKWARD FIRST-HITTING TIMES PRODUCES A NONTRIVIAL TYPE-I ANCIENT NAVIER--STOKES CELL ON `s<0`; THE OLD FIRST-HITTING CARRIER REMAINS AT FINITE POSITION AND UNIT SCALE AT `s=-1`, WHILE THE TERMINAL `s=0` BOUNDARY PROBES EXACTLY THE SPATIAL CRITICAL TAIL `R_m V(R_m y,0)` OF THE M5-474 ELEMENT / THIS SETS UP A TERMINAL-TAIL VERSUS BACKWARD-UNIQUENESS DICHOTOMY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Saturated backward record sequence

Let

\[
\tau_m\to-\infty
\]

be the backward first-hitting sequence from M5-477.

Set

\[
T_m:=-\tau_m,
\qquad
R_m:=\sqrt{T_m}.
\]

Then

\[
T_m\asymp q^m,
\qquad
R_m\asymp q^{m/2}.
\]

At `tau=tau_m`, M5-477 gives

\[
\boxed{
 cT_m^{-1/2}
 \le
 \|\Omega(\tau_m)\|_2^2
 \le
 CT_m^{-1/2},
}
\]

and

\[
\boxed{
\|\Omega(\tau_m)\|_\infty
\asymp T_m^{-1}.
}
\]

---

## 2. Parabolic blow-down at backward infinity

Define

\[
\boxed{
V^{(m)}(y,s)
:=
R_mV(R_my,T_ms),
}
\]

\[
\boxed{
\Omega^{(m)}(y,s)
:=
R_m^2\Omega(R_my,T_ms)
=T_m\Omega(R_my,T_ms).
}
\]

The Navier--Stokes equations are invariant under this transformation, so each pair solves unit-viscosity 3D Navier--Stokes on

\[
s< L_*/T_m,
\]

where the original marked ancient element is smooth up to some fixed positive normalized time `L_*>0` around its marked event.

Since

\[
L_*/T_m\to0,
\]

every compact cylinder in

\[
\mathbb R^3\times(-\infty,0)
\]

lies in the domain for sufficiently large `m`.

---

## 3. Uniform Type-I bounds on the blow-down sequence

M5-475 gives

\[
\|\Omega(\tau)\|_\infty
\le C(-\tau)^{-1},
\]

\[
\|\Omega(\tau)\|_2^2
\le C(-\tau)^{-1/2}.
\]

For fixed `s<0`,

\[
\begin{aligned}
\|\Omega^{(m)}(s)\|_\infty
&=T_m\|\Omega(T_ms)\|_\infty\\
&\le C|s|^{-1},
\end{aligned}
\]

and

\[
\begin{aligned}
\|\Omega^{(m)}(s)\|_2^2
&=T_m^{1/2}
\|\Omega(T_ms)\|_2^2\\
&\le C|s|^{-1/2}.
\end{aligned}
\]

Thus

\[
\boxed{
\|\Omega^{(m)}(s)\|_\infty
\le C|s|^{-1},
\qquad
\|\Omega^{(m)}(s)\|_2^2
\le C|s|^{-1/2}.
}
\]

Optimized Biot--Savart splitting as in M5-475 gives

\[
\boxed{
\|V^{(m)}(s)\|_\infty
\le C|s|^{-1/2},
\qquad
\|V^{(m)}(s)\|_6
\le C|s|^{-1/4}.
}
\]

These constants are uniform in `m` on every compact subinterval of `(-infinity,0)`.

---

## 4. The old first-hitting carrier stays at finite blow-down position

In the coordinates of the M5-474 element, the `m`-generation-old first-hitting carrier has natural spatial radius comparable to

\[
R_m\asymp q^{m/2}.
\]

Center nesting gives its center `Y_m` with

\[
|Y_m|\le C R_m.
\]

Therefore in the blow-down coordinates its center

\[
y_m:=Y_m/R_m
\]

is uniformly bounded.

Pass to a subsequence so that

\[
y_m\to y_*.
\]

The old Taylor carrier has own-scale vorticity amplitude bounded below on a fixed positive-volume cell. Under the `R_m` blow-down, both its radius and amplitude become `O(1)`.

Hence at `s=-1` there are fixed `rho_0,c_0>0` such that, after a harmless subsequence/orientation choice,

\[
\boxed{
\int_{B_{\rho_0}(y_*)}
|\Omega^{(m)}(y,-1)|^2dy
\ge c_0>0.
}
\]

This prevents loss of nontriviality through spatial escape.

---

## 5. Compactness for s<0

For every fixed interval

\[
-A\le s\le-\varepsilon<0,
\]

the uniform `L2 cap Linfinity` vorticity bounds give velocity `Linfinity`, local `W1p`, and vorticity time-equicontinuity exactly as in M5-474.

A diagonal subsequence therefore converges locally to a smooth ancient solution

\[
(\mathcal V,\mathcal\Omega)
\]

on

\[
\boxed{
\mathbb R^3\times(-\infty,0).
}
\]

The first-hitting carrier lower bound passes to the limit:

\[
\boxed{
\int_{B_{\rho_0}(y_*)}
|\mathcal\Omega(y,-1)|^2dy
\ge c_0>0.
}
\]

Thus

\[
\boxed{
\mathcal\Omega\not\equiv0.
}
\]

---

## 6. Limit class

The blow-down limit inherits

\[
\boxed{
\|\mathcal\Omega(s)\|_\infty
\le C|s|^{-1},
}
\]

\[
\boxed{
\|\mathcal\Omega(s)\|_2^2
\le C|s|^{-1/2},
}
\]

and

\[
\boxed{
\|\mathcal V(s)\|_\infty
\le C|s|^{-1/2}.
}
\]

This is a nontrivial Type-I ancient cell with finite enstrophy on every negative slice.

---

## 7. What the terminal boundary represents

At `s=0`, formally

\[
V^{(m)}(y,0)
=R_mV(R_my,0),
\]

and

\[
\Omega^{(m)}(y,0)
=R_m^2\Omega(R_my,0).
\]

Thus the terminal boundary of the second-generation ancient cell is exactly the sequence of spatial blow-downs of the marked ancient element at radii `R_m`.

For a `1/|x|` critical velocity tail these quantities remain nontrivial on fixed annuli.

For a strongly subcritical tail they vanish on every fixed annulus away from the origin.

Hence the bounded ratchet problem is now linked directly to a spatial-tail dichotomy.

---

## 8. Tail observables

For fixed `0<a<b<infinity`, define the scale-invariant terminal annular quantities

\[
\boxed{
\mathcal T_3(R;a,b)
:=
\int_{aR<|x|<bR}|V(x,0)|^3dx,
}
\]

and

\[
\boxed{
\mathcal T_\omega(R;a,b)
:=
R
\int_{aR<|x|<bR}|\Omega(x,0)|^2dx.
}
\]

These are exactly

\[
\|R V(R\cdot,0)\|_{L^3(A_{a,b})}^3
\]

and

\[
\|R^2\Omega(R\cdot,0)\|_{L^2(A_{a,b})}^2.
\]

Therefore terminal compactness/vanishing can be stated entirely in terms of these physical tail observables.

---

## 9. Highest-value next target

Prove the following dichotomy on the selected record scales `R_m`:

\[
\boxed{
\text{all terminal annular critical tails vanish}
\Longrightarrow
\mathcal\Omega\equiv0
}
\]

by suitable-solution terminal compactness plus backward uniqueness/unique continuation.

Since M5-478 has already proved `mathcal Omega != 0`, this would force a nonzero critical terminal tail:

\[
\boxed{
\limsup_m\mathcal T_3(R_m;a,b)>0
}
\]

or an equivalent scale-critical vorticity/pressure tail.

Such a result would convert the ancient-ratchet obstruction into a concrete logarithmically occupied spatial tail, reconnecting the bounded ratchet program to the earlier W1 critical-tail machinery.

---

## 10. Firewall

No terminal trace at `s=0` is claimed merely from the `s<0` compactness.

The passage to `s=0` requires suitable/local-energy compactness and pressure control on annuli away from the limiting singular core.

Backward uniqueness is also an external theorem with hypotheses that must be verified explicitly.

Thus M5-478 establishes the nontrivial ancient tail cell, not yet the terminal-tail necessity theorem.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
