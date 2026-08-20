# Hardy--Biot--Savart Palinstrophy Bridge — 2026-08-20

Overall status: **SYSTEM-I / SYSTEM-II BRIDGE — GLOBAL REGULARITY NOT PROVED.**

This note replaces the far-field vorticity `L2` bound in the second-order Biot--Savart estimate by the Hardy inequality. The result ties any recurrent `P_V` production rate directly to normalized vorticity palinstrophy. Thus failure of the direct System-II closure automatically feeds quantitative derivative mass into System I.

## 1. Near-field second-order cancellation

As in `PV_BIOTSAVART_SECOND_ORDER_CLOSURE_2026-08-20.md`, the strain kernel is even with zero spherical mean. Hence constant and linear Taylor terms cancel on a centered near ball.

With

\[
K_2
=\sup_x\sup_{|v|=1}|(v\cdot\nabla)^2\omega(x)|,
\]

we have

\[
\boxed{
|S_{near}|
\le
A K_2R^2,
\qquad
A=\frac{3\sqrt2}{8}.
}
\]

## 2. Far field from Hardy and palinstrophy

Let

\[
Q=\|\nabla\omega\|_2^2.
\]

Hardy's inequality centered at the observation point gives

\[
\int\frac{|\omega(y)|^2}{|x-y|^2}dy
\le
4Q.
\]

For the far strain,

\[
|S_{far}(x)|
\le
\frac{3\sqrt2}{8\pi}
\int_{|x-y|>R}
\frac{|\omega(y)|}{|x-y|^3}dy.
\]

Write

\[
\frac{|\omega|}{r^3}
=
\frac{|\omega|}{r}\frac1{r^2}.
\]

Cauchy--Schwarz and Hardy give

\[
\begin{aligned}
|S_{far}(x)|
&\le
\frac{3\sqrt2}{8\pi}
(4Q)^{1/2}
\left(\int_{r>R}r^{-4}dy\right)^{1/2}\\
&=
\boxed{
\frac{3\sqrt2}{2\sqrt\pi}
Q^{1/2}R^{-1/2}.
}
\end{aligned}
\]

Therefore

\[
\boxed{
\|S\|_\infty
\le
\frac{3\sqrt2}{8}K_2R^2
+
\frac{3\sqrt2}{2\sqrt\pi}Q^{1/2}R^{-1/2}.
}
\]

## 3. Optimize R

Set

\[
A=\frac{3\sqrt2}{8},
\qquad
D=\frac{3\sqrt2}{2\sqrt\pi}.
\]

The minimizing radius satisfies

\[
R^{5/2}
=\frac{D}{4A}
\frac{Q^{1/2}}{K_2}
=
\frac{1}{\sqrt\pi}
\frac{Q^{1/2}}{K_2}.
\]

At the optimum the far term equals four times the near term, so

\[
\boxed{
\|S\|_\infty
\le
\frac{15\sqrt2}{8}
\pi^{-2/5}
K_2^{1/5}Q^{2/5}.
}
\]

## 4. Insert the exact nonnormality H1 ceiling

The universal H1 bound

\[
N\le\sqrt2\|S\|_\infty P,
\qquad
P=\|\nabla S\|_2^2,
\]

gives

\[
q:=\frac NP
\le
\sqrt2\|S\|_\infty.
\]

Thus

\[
\boxed{
q
\le
\frac{15}{4}
\pi^{-2/5}
K_2^{1/5}Q^{2/5}.
}
\]

The numerical coefficient is

\[
\frac{15}{4}\pi^{-2/5}
\approx2.37230934.
\]

## 5. Palinstrophy floor forced by recurrent P_V

At a recurrent Leray `P`-maximum state,

\[
q\ge q_-.
\]

Therefore

\[
Q^{2/5}
\ge
\frac{4}{15}\pi^{2/5}
q_-K_2^{-1/5}.
\]

Raising to the power `5/2`,

\[
\boxed{
Q
\ge
Q_{crit}
:=
\pi\left(\frac4{15}\right)^{5/2}
q_-^{5/2}K_2^{-1/2}.
}
\]

Numerically,

\[
\boxed{
Q_{crit}
\approx
0.1153643712
\,q_-^{5/2}K_2^{-1/2}.
}
\]

Thus the recurrent projective branch cannot survive with arbitrarily small normalized palinstrophy.

## 6. Interpretation in the two-system strategy

The proof tree is now coupled quantitatively:

### System II attempt

Try to violate

\[
q\le\frac{15}{4}\pi^{-2/5}K_2^{1/5}Q^{2/5}.
\]

### If System II does not close

The survivor is forced to carry

\[
Q\ge Q_{crit}.
\]

This is handed directly to the derivative-mass side of System I.

Because first-hitting analyticity already removed pointwise derivative blow-up and fixed-ball derivative blow-up, a late `H` failure can only occur through remote derivative spatial non-tightness. Hence a `P_V` survivor that also approaches the `H` boundary must do so by carrying a quantitatively nontrivial amount of palinstrophy into an increasingly broad normalized region.

## 7. What this does and does not prove

A fixed positive palinstrophy floor is not by itself a global contradiction; the physical energy budget remains subcritical for a fixed natural-scale cost.

The gain is structural: `P_V` and `H` are no longer independent escape labels. Direct projective recurrence has a calculable derivative-mass requirement. The next System-I step is to determine whether repeated remote spreading of at least `Q_crit` can remain dynamically relevant to the core without either

- crossing the aggregate halo `P_tail >= cR` threshold;
- creating a secondary active core (`T`);
- or accumulating the half-power amplification required by the global packing budget.

Status: **RECURRENT P_V PRODUCTION FORCES THE EXPLICIT PALINSTROPHY FLOOR `Q >= pi(4/15)^(5/2) q_-^(5/2) K2^(-1/2)`. THIS PROVIDES A DIRECT QUANTITATIVE BRIDGE FROM SYSTEM II INTO THE REMOTE-DERIVATIVE SYSTEM-I BRANCH.**