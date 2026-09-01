# DSD M5-481 — Terminal L3 tail reduces to critical Dirichlet tail or strong tail amplitude

Date: 2026-09-01

Status: **TAIL-GEOMETRY SHARPENING / ON THE REGULAR TERMINAL-SUITABLE BRANCH OF M5-479--480, A NONTRIVIAL RECORD BLOW-DOWN CANNOT BE SUPPORTED BY A TERMINAL VELOCITY TAIL WHOSE SCALE-CRITICAL `L3` AMPLITUDE IS BOUNDED WHILE ITS SCALE-CRITICAL DIRICHLET CONTENT VANISHES / IN THAT CASE THE TERMINAL BLOW-DOWNS CONVERGE ON PUNCTURED ANNULI TO ONE SPATIALLY CONSTANT VECTOR, WHICH IS A GALILEAN MODE AND CAN BE REMOVED BEFORE BACKWARD UNIQUENESS / THEREFORE THE SURVIVING REGULAR TERMINAL TAIL MUST HAVE EITHER UNBOUNDED CRITICAL `L3` AMPLITUDE OR A NONZERO CRITICAL DIRICHLET/ENSTROPHY SHELL `R int_A_R |grad V|^2` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal record blow-down

At the M5-478 record radii `R_m -> infinity`, define

\[
U_m(y):=R_mV(R_my,0).
\]

For a fixed punctured annulus

\[
A_{a,b}=\{a<|y|<b\},
\]

we have

\[
\boxed{
\|U_m\|_{L^3(A_{a,b})}^3
=
\int_{aR_m<|x|<bR_m}|V(x,0)|^3dx.
}
\]

Also

\[
\nabla_yU_m(y)=R_m^2\nabla_xV(R_my,0),
\]

so

\[
\boxed{
\|\nabla U_m\|_{L^2(A_{a,b})}^2
=R_m
\int_{aR_m<|x|<bR_m}|\nabla V(x,0)|^2dx.
}
\]

Define the critical Dirichlet tail

\[
\boxed{
\mathcal G(R;a,b)
:=R
\int_{aR<|x|<bR}|\nabla V(x,0)|^2dx.
}
\]

---

## 2. Bounded terminal L3 amplitude versus strong amplitude

There are two immediate alternatives along the selected record sequence.

### Strong terminal amplitude

For some fixed annulus,

\[
\boxed{
\|U_m\|_{L^3(A_{a,b})}\to\infty.
}
\]

This is a genuine strong scale-critical tail-amplitude branch and needs no further reduction here.

### Bounded critical tail amplitude

Otherwise, after a diagonal subsequence over rational annuli,

\[
\boxed{
\sup_m\|U_m\|_{L^3(A_{a,b})}<\infty
}
\]

for every compact punctured annulus.

We analyze this branch below.

---

## 3. If critical Dirichlet content vanishes, each annulus becomes constant

Assume that on every fixed punctured annulus

\[
\boxed{
\|\nabla U_m\|_{L^2(A_{a,b})}\to0.
}
\]

Let

\[
c_m^{a,b}:=(U_m)_{A_{a,b}}
\]

be the annular mean.

Poincare--Sobolev on the fixed bounded annulus gives

\[
\|U_m-c_m^{a,b}\|_{L^6(A_{a,b})}
\le C_{a,b}\|\nabla U_m\|_2
\to0.
\]

In particular

\[
\boxed{
U_m-c_m^{a,b}\to0
\quad\text{strongly in }L^3(A_{a,b}).
}
\]

The bounded `L3` hypothesis gives a uniform bound on `c_m^{a,b}`. Pass to a subsequence:

\[
c_m^{a,b}\to c^{a,b}.
\]

Thus the terminal blow-down converges to a spatial constant on each annulus.

---

## 4. Overlap compatibility gives one global punctured constant

Take two overlapping annuli `A_1,A_2`.

On their overlap,

\[
U_m\to c^{A_1}
\quad\text{and}\quad
U_m\to c^{A_2}
\]

strongly in `L3`.

Therefore

\[
c^{A_1}=c^{A_2}.
\]

Using a connected chain of overlapping annuli covering

\[
\mathbb R^3\setminus\{0\},
\]

we obtain one vector

\[
\boxed{c_\infty\in\mathbb R^3}
\]

such that

\[
\boxed{
U_m\to c_\infty
\quad\text{locally in }L^3(\mathbb R^3\setminus\{0\}).
}
\]

Thus the only zero-Dirichlet critical terminal tail is a Galilean mode.

---

## 5. Remove the Galilean mode

For the second-generation space-time blow-down, subtract the same terminal constant `c_infinity` by the standard Galilean transformation.

A constant velocity has zero vorticity and no strain. After the Galilean removal, the terminal trace becomes

\[
\boxed{
\mathcal V(\cdot,0)=0
\quad\text{on }\mathbb R^3\setminus\{0\}
}
\]

in the local suitable sense, provided the M5-479 terminal compactness branch is active.

Then the same backward-uniqueness/unique-continuation step as M5-479 forces

\[
\mathcal\Omega\equiv0,
\]

contradicting the nontrivial first-hitting carrier at `s=-1`.

Therefore the zero-Dirichlet branch is impossible on the regular suitable-terminal corridor.

---

## 6. Critical Dirichlet tail is forced

Hence, outside strong terminal `L3` amplitude and terminal suitable-defect branches, there exist fixed `0<a<b<infinity` and `g_*>0` such that

\[
\boxed{
\limsup_{m\to\infty}
R_m
\int_{aR_m<|x|<bR_m}
|\nabla V(x,0)|^2dx
\ge g_*>0.
}
\]

Because `div V=0`, globally

\[
\|\nabla V\|_2^2=\|\Omega\|_2^2.
\]

Locally the exact equality requires boundary terms, but the shell quantity is the correct velocity-Dirichlet critical observable and is equivalent, after fixed enlarged-annulus localization, to a critical vorticity/enstrophy tail plus harmless harmonic terms.

Thus the surviving tail is a genuine rotational/gradient tail, not a pure low-frequency Galilean drift.

---

## 7. Compatibility with finite enstrophy

The forced physical shell cost is only

\[
\int_{A_{R_m}}|\nabla V|^2dx
\gtrsim\frac{g_*}{R_m}.
\]

Since the record radii grow geometrically,

\[
\sum_m\frac1{R_m}<\infty.
\]

Therefore infinitely many critical Dirichlet shells are compatible with

\[
\int_{\mathbb R^3}|\nabla V|^2dx<\infty.
\]

This is the exact spatial analogue of the earlier natural-scale summability barrier.

So the new tail is sharply critical but not contradictory.

---

## 8. Updated bounded-ratchet frontier

The regular terminal branch now satisfies

\[
\boxed{
E_{ratchet}^{ancient}
\Longrightarrow
H_{tail,L3}^{strong}
\lor
T_{Dir}^{crit}
\lor
H_{terminal\ suitable}^{crit},
}
\]

where

\[
T_{Dir}^{crit}:
\quad
\limsup_m
R_m\int_{A_{R_m}}|\nabla V(0)|^2>0.
\]

M5-480 has already absorbed the independent pressure-tail branch into the velocity side.

---

## 9. Highest-value next target

The next step is to analyze the critical Dirichlet tail itself.

Because the same record scaling makes

\[
R_mV(R_m\cdot,0)
\]

have bounded `H1` energy on fixed annuli, a bounded-amplitude subbranch should admit a punctured terminal profile or dilation hull.

The main question is whether its scale-to-scale recurrence is forced to be

- discretely self-similar,
- compact aperiodic in log radius, or
- dynamically replenished by the terminal suitable-defect branch.

This reconnects directly to the earlier canonical W1 tail machinery, now with an independently derived critical Dirichlet lower bound.

---

## 10. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
