# DSD M17-286 — Compact nodal neighborhoods have uniformly vanishing volume and cannot carry bulk charge

Date: 2026-09-06  
Canonical ID: **M17-286**

Status: **NODAL-VOLUME GATE / ON THE PAYER-FREE COMPACT HEAT-TANGENT CORRIDOR, M17-272/285 GIVE UNIFORM C1 CONTROL, SMOOTH COMPACTNESS, A NONZERO LIMIT, AND FINITE NODAL VANISHING ORDER. IF EPSILON-NEIGHBORHOODS OF THE NODAL SET OCCUPIED A FIXED POSITIVE FRACTION OF A COMPACT CORE FOR EPSILON->0, THE UNIFORM LIPSCHITZ BOUND WOULD MAKE `|V_j|=O(epsilon)` ON A FIXED POSITIVE-VOLUME SET. UNIFORM CONVERGENCE WOULD THEN FORCE THE NONZERO ANALYTIC LIMIT TO VANISH ON A POSITIVE-MEASURE SET, IMPOSSIBLE UNLESS IT VANISHES IDENTICALLY. THEREFORE NODAL TUBULAR NEIGHBORHOODS HAVE UNIFORMLY VANISHING VOLUME. COMPACT NODAL GEOMETRY CANNOT ITSELF CARRY A FIXED-FRACTION SPECTRAL/COEFFICIENT CHARGE; SUCH CHARGE NEAR NODES MUST ENTER A VANISHING-MEASURE MICROCARRIER/SUBSCALE OR BREAK THE COMPACTNESS CORRIDOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compact nodal sets

At time zero, let

\[
Z_j:=\{z\in B_{core}:V_j(z,0)=0\}.
\]

On the payer-free compact branch, after passing to a subsequence,

\[
V_j\to V_\infty
\]

uniformly on a slightly larger compact core, and

\[
\boxed{\sup_j\|\nabla V_j\|_{L^\infty}\le C_1.}
\]

The limit is nonzero by the retained `L2` mass floor.

---

## 2. Assume a thick sequence of shrinking nodal neighborhoods

Suppose for contradiction that there are

\[
\varepsilon_j\downarrow0
\]

and a fixed

\[
c_0>0
\]

such that

\[
\boxed{
|N_{\varepsilon_j}(Z_j)\cap B_{core}|
\ge c_0.
}
\]

For every

\[
z\in N_{\varepsilon_j}(Z_j),
\]

choose

\[
z_j^*\in Z_j
\]

with

\[
|z-z_j^*|\le\varepsilon_j.
\]

Since `V_j(z_j^*,0)=0`, the uniform Lipschitz bound gives

\[
\boxed{
|V_j(z,0)|\le C_1\varepsilon_j.
}
\]

Thus a fixed positive-volume set lies inside the small-amplitude set

\[
\{|V_j|\le C_1\varepsilon_j\}.
\]

---

## 3. Pass to the analytic limit

Uniform convergence gives, for any fixed `delta>0`, for sufficiently large `j`,

\[
\{|V_j|\le C_1\varepsilon_j\}
\subset
\{|V_\infty|\le\delta\}
\]

up to the chosen compact core.

Hence

\[
|\{|V_\infty|\le\delta\}\cap B_{core}|
\ge c_0
\]

for every `delta>0`.

Letting `delta->0` and using continuity from above of Lebesgue measure yields

\[
\boxed{
|\{V_\infty=0\}\cap B_{core}|
\ge c_0>0.
}
\]

But a nontrivial real-analytic spatial slice cannot vanish on a positive-measure set.

Therefore

\[
V_\infty(\cdot,0)\equiv0
\]

would be forced, contradicting the nonzero mass normalization.

---

## 4. Uniform tubular-volume conclusion

For every

\[
\delta_V>0
\]

there exists

\[
\varepsilon_*(\delta_V)>0
\]

such that, for all sufficiently large `j`,

\[
\boxed{
|N_{\varepsilon}(Z_j)\cap B_{core}|<\delta_V
\qquad
\forall0<\varepsilon<\varepsilon_*.
}
\]

Thus compact nodal sets cannot become volume filling at arbitrarily small scale while the payer-free compact tangent corridor survives.

---

## 5. Consequence for coefficient/spectral charge

Suppose a fixed fraction of an amplitude-independent coefficient charge, director charge, or raw spectral numerator is supported inside

\[
N_{\varepsilon_j}(Z_j)
\]

with

\[
\varepsilon_j\to0.
\]

Because the carrier volume tends to zero uniformly, this is not a bulk nodal mechanism.

It is precisely a

\[
\boxed{G_{vanishing\text{-}measure\ nodal\ microcarrier}}
\]

and must be treated by the existing strict-subscale / coefficient-spike / amplitude-degeneration ledger.

Hence

\[
\boxed{
G_{compact\ irregular\ nodal\ geometry}
\Longrightarrow
G_{finite\text{-}order\ thin\ nodal\ set}
\lor
G_{vanishing\text{-}measure\ subscale}
\lor
G_{compactness/coefficient\ failure}.
}
\]

---

## 6. DSD audit

- No quantitative Minkowski-dimension theorem is assumed.
- Uniform vanishing of tubular volume follows by compactness, Lipschitz control, analyticity, and nonzero mass.
- The result concerns compact payer-free tangent cores; nodal complexity escaping to spatial infinity remains in M17-284.
- A finite-order nodal hypersurface is not declared impossible; it is shown unable to carry fixed positive **volume** by itself.
- Global 3D Navier--Stokes regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
