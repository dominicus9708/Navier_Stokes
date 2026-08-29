# DSD M5-247 — Energy-Visible Residual: Flux / Derivative / Large-Structure Routing

Date: 2026-08-30

Parent: `DSD_M5_246_ENERGY_TRANSVERSE_BRANCH_TO_STRAIN_H2_LARGE_COEFFICIENT_MERGER_2026-08-30.md`

Status: **BRANCH MERGER / A LOCALLY FIRST-RG-ENERGY-VISIBLE RESIDUAL CANNOT REMAIN AN UNTYPED SCALAR CHARGE: THE EXACT IDENTITY `a=j'-j-nu d` FORCES, ON EVERY VISIBLE CELL, EITHER POSITIVE CRITICAL GRADIENT ENERGY, A LARGE CRITICAL ENERGY-CURRENT AMPLITUDE, OR LARGE LOG-RADIAL CURRENT VARIATION / THE EXPLICIT CURRENT FORMULA ROUTES THESE RESPECTIVELY TO STRAIN/DERIVATIVE, RADIAL-PRESSURE/LARGE-COEFFICIENT, OR H2/PRESSURE-DERIVATIVE CHANNELS / THUS BOTH FIRST-ORDER RG ENERGY BRANCHES MERGE INTO ONE COMMON LARGE-STRUCTURE FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input: locally energy-visible residual

From M5-243, the `E_local` branch means that for one fixed smooth compact log-cell test `w` there is an open recurrent set of tail phases with

\[
\boxed{
|\mathfrak A_w(T)|
=
\left|
\int_I w(y)a_T(y)dy
\right|
\ge a_*>0.
}
\]

Normalize `w` so that

\[
\|w\|_{L^\infty}\le1.
\]

Then

\[
\boxed{
\int_I|a_T(y)|dy
\ge a_*.
}
\]

This occurs on a positive-density family of translated cells by continuity and minimal recurrence.

---

## 2. Exact local energy density identity

M5-244 proves

\[
\boxed{
a(y)=j'(y)-j(y)-\nu d(y),}
\]

with

\[
d(y)
=
\int_{S^2}r^4|\nabla T|^2d\theta
\ge0,
\]

and

\[
\begin{aligned}
j(y)=\int_{S^2}\Bigg[
&\frac\nu2\partial_y|\Phi|^2
-\nu|\Phi|^2\\
&-\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\Bigg]d\theta.
\end{aligned}
\]

Therefore

\[
\int_I|a|
\le
\int_I|j'|
+
\int_I|j|
+
\nu\int_Id.
\]

If all three right-hand terms were below `a_*/3`, the visible charge would be impossible.

Hence every visible cell satisfies the exact finite fork

\[
\boxed{
\int_I|j'|\ge\frac{a_*}{3}
\quad\lor\quad
\int_I|j|\ge\frac{a_*}{3}
\quad\lor\quad
\nu\int_Id\ge\frac{a_*}{3}.
}
\]

---

## 3. D-channel: critical gradient energy

If

\[
\nu\int_Id\ge\frac{a_*}{3},
\]

then

\[
\boxed{
\int_{I\times S^2}
r^4|\nabla T|^2
\ge
\frac{a_*}{3\nu}.
}
\]

Using

\[
r^4|\nabla T|^2
=|\Phi_y-\Phi|^2+|\nabla_S\Phi|^2,
\]

this gives a fixed critical first-derivative/amplitude cell certificate.

With the recurrent mean identities of M5-235/245, persistent radial portions of this energy force strain energy; the remaining tangential/log derivative portion is directly an H-type normalized derivative channel.

Thus

\[
\boxed{D\to S_{amp}\lor H1_{tail}\lor L_{tail}.}
\]

No ordinary physical-energy divergence is claimed.

---

## 4. J-channel: large critical energy current

Suppose

\[
\int_I|j|dy\ge\frac{a_*}{3}.
\]

The explicit current obeys

\[
\begin{aligned}
|j(y)|
\le
\int_{S^2}\Bigg[
&\nu|\Phi||\Phi_y|
+\nu|\Phi|^2\\
&+\left(\frac{|\Phi|^2}{2}+|\Pi|\right)|\Phi_r|
\Bigg]d\theta.
\end{aligned}
\]

Therefore a fixed lower bound on `int |j|` forces at least one of:

\[
\boxed{
\int|\Phi||\Phi_y|
\text{ large},
}
\]

\[
\boxed{
\int|\Phi|^2
\text{ large},
}
\]

or

\[
\boxed{
\int
\left(\frac{|\Phi|^2}{2}+|\Pi|\right)|\Phi_r|
\text{ large}.
}
\]

These route respectively to:

1. log-shape derivative / H1;
2. large critical velocity amplitude;
3. radial-sector kinetic/pressure correlation.

The third branch is exactly the structural family already audited in M5-233--246 and routes to strain, H2, or large coefficient.

Thus

\[
\boxed{J\to H1_{tail}\lor S_{amp}\lor P_{rad}\lor L_{tail}.}
\]

---

## 5. J'-channel: current variation

Suppose

\[
\int_I|j'|dy\ge\frac{a_*}{3}.
\]

Differentiate the explicit current formula.

Every term in `j'` contains one of the following structural types:

- `Phi_{yy}` or `nabla_S Phi_y` after differentiating velocity gradients;
- products of `Phi_y` with `Phi`, `Phi_r`, or first angular derivatives;
- `Pi_y Phi_r`;
- `Pi (Phi_r)_y`;
- lower-order amplitude terms.

Therefore on a compact tail coefficient class, a fixed `L1(I)` lower bound for `j'` gives the safe alternative

\[
\boxed{
J'	o H2_{tail}
\lor P_{y}
\lor L_{tail,1}.
}
\]

The pressure derivative is not independent: differentiating the pressure Poisson equation expresses it through first/second derivatives of `Phi` and quadratic coefficient products.  Consequently it further routes to

\[
\boxed{
P_y\to H2_{tail}\lor L_{tail,1}.
}
\]

Hence

\[
\boxed{J'\to H2_{tail}\lor L_{tail,1}.}
\]

---

## 6. No total-variation assumption is needed

A continuous scalar observable on an aperiodic minimal hull may be constant and nonzero.

Therefore the shortcut

\[
\mathfrak A\not\equiv0
\Rightarrow
\text{sign changes or positive total variation}
\]

is false.

M5-247 does not use it.

The routing follows from the **local magnitude** of the visible charge and the exact PDE current identity on each recurrent cell.

---

## 7. Merge with the transverse branch

M5-246 gives

\[
E_{trans}
\Longrightarrow
S_{amp}
\lor H2_{tail}
\lor L_{tail,1}.
\]

M5-247 gives, after including the H1 branch into the general derivative frontier,

\[
E_{local}
\Longrightarrow
S_{amp}
\lor H1/H2_{tail}
\lor P_{rad}
\lor L_{tail,1}.
\]

And M5-233--246 route `P_rad` back into strain/H2/large coefficients.

Therefore the entire residual-gap branch satisfies

\[
\boxed{
R_{gap}
\Longrightarrow
S_{amp}
\lor H_{tail}
\lor L_{tail}.
}
\]

Here:

- `S_amp` = fixed recurrent critical strain amplitude/correlation;
- `H_tail` = fixed normalized first/second derivative tail certificate;
- `L_tail` = sufficiently large remaining critical velocity/pressure/gradient coefficient.

---

## 8. Major branch convergence

The stationary all-tail branch M5-232--236 had already reduced to essentially the same structural frontier:

\[
\boxed{
S_{all}
\Longrightarrow
S_{amp}
\lor H_{rel/tail}
\lor L_{tail}
\quad\text{or the unresolved fixed-force nondegeneracy core}.
}
\]

The residual-active branch now joins it.

Thus the previous major split

\[
\text{stationary tail}
\quad\lor\quad
\text{residual-active tail}
\]

is no longer the most useful proof-tree separation.

Both are driven toward one common endpoint:

\[
\boxed{
\text{large critical structure}
\lor
\text{normalized derivative structure}
\lor
\text{large fixed-force stationary nondegeneracy problem}.
}
\]

---

## 9. Remaining scope gap

The tail derivative certificates in this note are properties of the formed W1 canonical tail.

They are **not yet automatically finite-prelimit H events**.

The key remaining bridge is therefore an inheritance/interface statement:

\[
\boxed{
\text{persistent normalized tail }S/H/L\text{ certificate}
\Longrightarrow
\text{finite-stage }H/T\text{ cost or expanding-window contradiction}.
}
\]

This is now more central than further algebraic splitting of the tail endpoint.

---

## 10. DSD verdict

### CLOSED AS INDEPENDENT ENDPOINTS

- first-order energy-visible residual;
- first-order energy-transverse residual;
- pressure as a free residual channel.

### COMMON FRONTIER

\[
\boxed{
R_{gap}
\to
S_{amp}\lor H_{tail}\lor L_{tail}.
}
\]

### NEXT TARGET

Return to the **W1-to-prelimit / Expanding-Window Gate**.  Audit exactly which of `S_amp`, `H_tail`, and `L_tail` can be pulled back through the first-hitting tower on generation-aligned windows without assuming full expanding-window convergence.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]