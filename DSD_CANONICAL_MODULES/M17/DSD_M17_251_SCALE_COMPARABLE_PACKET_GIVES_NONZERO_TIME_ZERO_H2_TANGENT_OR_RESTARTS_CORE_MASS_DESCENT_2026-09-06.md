# DSD M17-251 — Scale-comparable packet gives a nonzero time-zero H2 tangent or restarts core-mass descent

Date: 2026-09-06  
Canonical ID: **M17-251**

Status: **TIME-ZERO COMPACTNESS GATE / M17-250 PRODUCES A PHYSICAL PACKET WITH SUPPORT SCALE COMPARABLE TO ITS OWN RAW `H2/L2` SCALE, OR A NODAL-CONCENTRATION EXIT. FOR A SCALE-COMPARABLE PACKET, IF A FIXED INNER CORE CARRIES A FIXED FRACTION OF THE PACKET `L2` MASS, STANDARD INTERIOR ELLIPTIC ESTIMATES TURN THE RAW `Delta W` UPPER BOUND INTO A UNIFORM OWN-SCALE `H2` BOUND. AFTER NORMALIZING BY THE PACKET `L2` MASS AND PHYSICAL SCALE, RELLICH COMPACTNESS GIVES STRONG `L2` CONVERGENCE ON A FIXED RESCALED CORE WITH A NONZERO LIMIT. IF THE INNER MASS FRACTION VANISHES, THE RAW DERIVATIVE CORE AND THE `L2` DENOMINATOR HAVE SEPARATED; THIS IS NOT CALLED COMPACTNESS. IT RESTARTS THE M17-250/M17-232 SUBSCALE SELECTION AND, IF REPEATED WITHOUT RETURN, ENDS IN THE NODAL-CONCENTRATION BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scale-comparable packet

Take a scale-comparable M17-250 packet at time `theta_j`.

Use three fixed concentric geometric regions

\[
B_j^{in}\Subset B_j^{mid}\Subset B_j^{out}
\]

with all radii comparable to one physical scale

\[
r_j\to0.
\]

Let

\[
E_j:=\int_{B_j^{out}}|W_j|^2dy,
\]

and let the retained raw Laplacian charge be

\[
H_j:=\int_{B_j^{mid}}|\Delta W_j|^2dy.
\]

The scale-comparable stopping condition is

\[
\boxed{
 c_0
 \le
 r_j^4\frac{H_j}{E_j}
 \le
 C_0
}
\]

for fixed constants `0<c_0<C_0<infinity`.

Equivalently, if

\[
\ell_j:=\left(\frac{E_j}{H_j}\right)^{1/4},
\]

then

\[
\boxed{r_j\asymp\ell_j.}
\]

---

## 2. Inner-mass retention gate

Fix a small constant

\[
0<\eta<1.
\]

Split into two cases.

### Case A — retained inner mass

Assume

\[
\boxed{
\int_{B_j^{in}}|W_j|^2dy
\ge\eta E_j.
}
\]

### Case B — core/denominator separation

Assume

\[
\boxed{
\int_{B_j^{in}}|W_j|^2dy
<\eta E_j.
}
\]

Case B is not called a compact packet.

The raw derivative charge lives in the middle core while the normalizing `L2` mass has escaped toward the outer part of the buffer.

This is precisely the configuration in which a smaller local `H2/L2` scale can reappear.

---

## 3. Interior elliptic estimate on the retained-mass branch

On Case A, use the standard interior elliptic estimate on the fixed nested pair

\[
B_j^{in}\Subset B_j^{mid}.
\]

After scaling to unit radius, it has the form

\[
\boxed{
 r_j^4\|\nabla^2W_j\|_{L^2(B_j^{in})}^2
 +r_j^2\|\nabla W_j\|_{L^2(B_j^{in})}^2
 \le
 C_{ell}
 \left(
 r_j^4\|\Delta W_j\|_{L^2(B_j^{mid})}^2
 +\|W_j\|_{L^2(B_j^{mid})}^2
 \right).
}
\]

Since

\[
\|W_j\|_{L^2(B_j^{mid})}^2\le E_j
\]

and scale comparability gives

\[
r_j^4H_j\le C_0E_j,
\]

we obtain

\[
\boxed{
 r_j^4\|\nabla^2W_j\|_{L^2(B_j^{in})}^2
 +r_j^2\|\nabla W_j\|_{L^2(B_j^{in})}^2
 \le C E_j.
}
\]

No boundary condition is used; this is an interior estimate with a fixed geometric gap between `B_in` and `B_mid`.

---

## 4. Own-scale and own-amplitude normalization

Let `q_j` be the packet center.

Define the packet amplitude scale

\[
\boxed{
a_j:=E_j^{1/2}r_j^{-3/2}.}
\]

Set

\[
\boxed{
V_j(z)
:=\frac{1}{a_j}
W_j(q_j+r_jz,\theta_j).
}
\]

The outer rescaled packet has `L2` mass of order one:

\[
\int_{B^{out}}|V_j|^2dz=1.
\]

Case A gives the nonzero inner mass floor

\[
\boxed{
\int_{B^{in}}|V_j|^2dz\ge\eta.
}
\]

The elliptic estimate becomes

\[
\boxed{
\|V_j\|_{H^2(B^{in})}\le C.
}
\]

All constants are independent of `j`.

---

## 5. Rellich compactness gives a nonzero time-zero tangent

By weak compactness in `H2` and Rellich compactness on a slightly smaller fixed core `B^{core}\Subset B^{in}`, after passing to a subsequence,

\[
V_j\rightharpoonup V_0
\quad\text{weakly in }H^2_{loc},
\]

and

\[
\boxed{
V_j\to V_0
\quad\text{strongly in }L^2(B^{core}).
}
\]

To retain a quantitative nonzero mass floor, choose the nested geometry in the inner-mass gate with one additional fixed core layer and apply the finite annular partition before passing to the subsequence.

Then one fixed subcore carries a fixed fraction `eta_* >0` of the retained inner mass, and after recentering by only `O(r_j)` if necessary,

\[
\boxed{
\|V_0\|_{L^2(B^{core})}^2\ge\eta_*>0.
}
\]

Thus

\[
\boxed{V_0\not\equiv0.}
\]

This is a genuine **time-zero nonzero compact tangent**.

No time evolution has yet been passed to the limit.

---

## 6. What Case B means

Suppose instead that the inner mass fraction tends to zero.

The raw derivative core still carries the spectral numerator used in the scale-comparable packet, while the `L2` denominator is increasingly outside that core.

Restrict the denominator to the raw core.

If its mass is `eta_j E_j` with `eta_j->0`, then the local derivative ratio satisfies schematically

\[
\frac{H_j}{E_j^{core}}
\gtrsim
\eta_j^{-1}\frac{H_j}{E_j}.
\]

Hence its local intrinsic scale is shorter by

\[
\boxed{
\ell_j^{core}
\lesssim
\eta_j^{1/4}\ell_j.
}
\]

The raw-core/buffer re-extraction of M17-232 and the stopping selection of M17-250 can therefore be restarted inside the packet.

Thus Case B is routed as

\[
\boxed{
G_{core/denominator\ separation}
\Longrightarrow
H_{smaller\ stopping\ packet}
\lor
G_{nodal\ concentration}.
}
\]

It is not a terminal interface artifact.

---

## 7. Finite stopping interpretation

At each finite restart one of two things happens:

1. an inner-mass-retaining scale-comparable packet is obtained;
2. the physical scale strictly decreases.

If the second alternative persists through every finite depth, the nested-ball argument of M17-250 identifies a limiting point with

\[
W=0.
\]

Therefore the DSD-safe statement is

\[
\boxed{
H_{scale\text{-}comparable\ raw\ packet}
\Longrightarrow
H_{nonzero\ time\text{-}zero\ H2\ tangent}
\lor
G_{nodal\ concentration}.
}
\]

The first branch is finite and compact; the second remains an explicit nodal branch.

---

## 8. What this does not yet prove

The time-zero tangent `V_0` is not yet an ancient solution.

Still missing are:

1. a parabolic time interval after own-scale normalization;
2. uniform spacetime compactness on every fixed backward cylinder;
3. vanishing local self-nonlinearity and ambient forcing in the same normalization;
4. elimination or classification of cutoff/interface forcing;
5. a backward lifetime tending to infinity.

M17-251 removes only the **spatial nonzero compactness** obstruction.

---

## 9. DSD audit

- Scale comparability is used as an upper as well as a lower derivative ratio.
- The nonzero limit is obtained from a fixed inner `L2` mass fraction, not from an `H2` lower bound alone.
- Interior elliptic regularity is applied on nested physical regions; no artificial boundary condition is imposed.
- If the normalizing mass leaves the raw derivative core, compactness is not claimed.
- Core/denominator separation is routed back to a strictly smaller physical scale or nodal concentration.
- No time-direction reversal has yet been used.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
