# DSD M17-285 — Payer-free compact heat tangents have uniformly finite nodal vanishing order

Date: 2026-09-06  
Canonical ID: **M17-285**

Status: **COMPACT NODAL-JET GATE / M17-272 PROVIDES UNIFORM INTERIOR PARABOLIC REGULARITY OF EVERY FIXED ORDER ON THE PAYER-FREE COMPACT RAW HEAT-TANGENT CORRIDOR, WHILE M17-251/254 RETAIN A NONZERO LOCAL L2 NORMALIZATION. IF NODAL POINTS IN A FIXED COMPACT CORE HAD VANISHING ORDERS TENDING TO INFINITY, A DIAGONAL SUBSEQUENCE WOULD CONVERGE SMOOTHLY ON A SMALLER CYLINDER TO A NONZERO CALORIC LIMIT WHOSE EVERY SPATIAL DERIVATIVE VANISHES AT ONE LIMIT POINT. SPATIAL ANALYTICITY / UNIQUE CONTINUATION OF CALORIC FUNCTIONS THEN FORCES THE LIMIT TO VANISH IDENTICALLY, CONTRADICTING THE RETAINED L2 MASS. THEREFORE THE VANISHING ORDER OF COMPACT-CORE NODAL POINTS IS UNIFORMLY FINITE. ARBITRARILY HIGH NODAL COMPLEXITY CAN SURVIVE ONLY BY ESCAPING TO SPATIAL INFINITY, ENTERING A STRICT SUBSCALE, OR BREAKING THE COMPACTNESS/COEFFICIENT CORRIDOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compact payer-free tangent corridor

Fix nested cylinders

\[
Q_{in}\Subset Q_{mid}\Subset Q_{out}.
\]

On the payer-free compact raw tangent branch, M17-272 and standard parabolic bootstrapping give, for every fixed integer `m>=0`,

\[
\boxed{
\sup_j\|V_j\|_{C^m(Q_{mid})}\le C_m<\infty.
}
\]

The constants may grow with `m`, but for each fixed `m` they are independent of `j`.

At time zero, M17-251 gives a retained local mass floor

\[
\boxed{
\int_{B_{in}}|V_j(z,0)|^2dz\ge\eta>0.
}
\]

---

## 2. Assume unbounded vanishing order

Suppose there are nodal points

\[
z_j\in B_{core}\Subset B_{in}
\]

such that the spatial vanishing order of

\[
V_j(\cdot,0)
\]

at `z_j` tends to infinity:

\[
\boxed{m_j\to\infty.}
\]

Thus for every fixed multi-index `alpha`, eventually

\[
D^\alpha V_j(z_j,0)=0.
\]

After a subsequence,

\[
z_j\to z_*\in\overline{B_{core}}.
\]

---

## 3. Diagonal smooth compactness

For `m=1`, compactness gives a subsequence converging in `C^1` on a smaller cylinder.

Repeat for `m=2,3,...` and take a diagonal subsequence.

Then

\[
\boxed{
V_j\to V_\infty
\quad\text{in }C^m_{loc}
\text{ for every fixed }m.
}
\]

The limit is caloric:

\[
\partial_\tau V_\infty=\Delta V_\infty.
\]

For any fixed multi-index `alpha`, since `m_j>|alpha|` eventually,

\[
D^\alpha V_j(z_j,0)=0.
\]

Passing to the limit gives

\[
\boxed{
D^\alpha V_\infty(z_*,0)=0
\qquad\forall\alpha.
}
\]

Thus every spatial jet of the limit vanishes at one point.

---

## 4. Analyticity contradiction

For each fixed time in the interior of a heat cylinder, a caloric solution is real analytic in the spatial variables.

Therefore the infinite-order zero in Section 3 implies

\[
V_\infty(\cdot,0)\equiv0
\]

on the connected spatial component.

Heat unique continuation then gives the corresponding local spacetime vanishing.

But the strong `L2` convergence inherited from the compact branch and the retained mass floor imply

\[
\boxed{
\int_{B_{in}}|V_\infty(z,0)|^2dz\ge\eta>0,
}
\]

a contradiction.

Hence the assumed sequence `m_j->infinity` cannot exist.

---

## 5. Uniform finite-order conclusion

There exists a finite integer

\[
\boxed{m_*<\infty}
\]

depending only on the fixed compact corridor and its uniform regularity/mass constants such that every nodal point in the chosen compact core satisfies

\[
\boxed{
\operatorname{ord}_{z}V_j(\cdot,0)\le m_*.
}
\]

The same argument applies at any fixed compact rescaled time after using the M17-254 mass corridor.

---

## 6. What irregular nodal geometry can still do

M17-285 does not claim that the nodal set is globally smooth.
Finite-order analytic nodal singularities may exist.

It does show that an arbitrarily high-order / infinitely flat nodal degeneration cannot remain in a fixed compact payer-free tangent core.

Therefore

\[
\boxed{
G_{unbounded\ nodal\ jet\ complexity}
\Longrightarrow
G_{spatial\ infinity}
\lor
G_{strict\ subscale}
\lor
H_{mass/palinstrophy\ compactness\ failure}
\lor
G_{coefficient/interface}.
}
\]

Finite-order singular strata remain geometric objects, but they cannot by themselves carry an infinite hierarchy of new compact scales without entering one of the exits above.

---

## 7. Relation to M17-009

M17-009 established a finite analytic-jet-order principle for nodal topology-changing events in the earlier fixed compact hard core.

M17-285 is the intrinsic-tangent analogue:

- it applies after own-scale parabolic normalization;
- it uses the payer-free compactness and retained tangent mass;
- it does not identify a generic remote microcarrier with the old fixed core;
- it therefore avoids silently importing M17-009 outside its original scope.

---

## 8. DSD audit

- Uniform bounds are required only one derivative order at a time; diagonal extraction handles all fixed orders.
- The nonzero mass floor is essential; without it an infinite-order zero could converge to the zero solution.
- No claim is made that every finite-order nodal singularity is harmless.
- Nodal complexity escaping to infinity remains tied to M17-284's global spatial decompactification branch.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
