# DSD M17-249 — Linear similarity vorticity has strict L2 decay and no nonzero uniformly bounded ancient state

Date: 2026-09-06  
Canonical ID: **M17-249**

Status: **EXACT LINEAR ENDPOINT / AFTER M17-242, M17-245, AND M17-248, THE LOW-AMPLITUDE SELF-NONLINEARITY-FREE BRANCH NATURALLY APPROACHES THE LINEAR SIMILARITY VORTICITY EQUATION `D_(y/2) W=Delta W-W`. THIS EQUATION HAS THE EXACT ENSTROPHY IDENTITY `E'=-2P-(1/2)E`, HENCE `E(theta)>=0` DECAYS AT LEAST LIKE `exp(-theta/2)` FORWARD. CONSEQUENTLY ANY ANCIENT SOLUTION DEFINED ON `(-infinity,0]` WITH A UNIFORM `L2` BOUND MUST BE IDENTICALLY ZERO: `E(0)<=exp(-T/2)E(-T)` AND `T->infinity`. THEREFORE A NONZERO UNIFORMLY-L2-BOUNDED ANCIENT LINEAR TANGENT WOULD CONTRADICT THE LINEAR ENDPOINT IMMEDIATELY. THE HARD STEP IS NOT THE LINEAR LIOUVILLE THEOREM; IT IS EXTRACTING SUCH A NONZERO ANCIENT TANGENT FROM THE LOW-AMPLITUDE INTRINSIC PACKETS WHILE CONTROLLING AMBIENT FORCING, INTERFACE INPUT, SCALE COMPARABILITY, AND BACKWARD LIFETIME. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Linear similarity equation

Remove the self-induced and ambient Navier--Stokes velocity/strain contributions and retain only the linear similarity drift, diffusion, and reaction.

Let

\[
B_0(y)=\frac12y,
\qquad
\nabla\cdot B_0=\frac32.
\]

The linear similarity vorticity equation is

\[
\boxed{
D_{B_0}W
=\Delta W-W,
}
\]

that is,

\[
\partial_\theta W
+\frac12y\cdot\nabla W
=\Delta W-W.
\]

Assume sufficient smoothness and decay for the integrations below.

---

## 2. Exact L2 identity

Define

\[
E(\theta):=\int_{\mathbb R^3}|W|^2dy,
\qquad
P(\theta):=\int_{\mathbb R^3}|\nabla W|^2dy.
\]

For a scalar/vector density \(f\),

\[
\frac d{d\theta}\int fdy
=
\int(D_{B_0}f+f\nabla\cdot B_0)dy.
\]

Since

\[
D_{B_0}|W|^2
=2W\cdot(\Delta W-W),
\]

we obtain

\[
\begin{aligned}
E'
&=
2\int W\cdot\Delta Wdy
-2E
+\frac32E\\
&=
-2P-rac12E.
\end{aligned}
\]

Therefore

\[
\boxed{
E'(\theta)
=-2P(\theta)-\frac12E(\theta).
}
\]

This identity is exact.

---

## 3. Strict forward contraction

Since \(P\ge0\),

\[
E'\le-\frac12E.
\]

Gronwall gives, for \(\theta_2\ge\theta_1\),

\[
\boxed{
E(\theta_2)
\le
\exp\left(-\frac{\theta_2-\theta_1}{2}\right)
E(\theta_1).
}
\]

Equivalently,

\[
\boxed{
\|W(\theta_2)\|_2
\le
\exp\left(-\frac{\theta_2-\theta_1}{4}\right)
\|W(\theta_1)\|_2.
}
\]

Thus the exact linear similarity flow has no nonzero recurrent finite-energy orbit.

---

## 4. Uniformly bounded ancient Liouville theorem

Assume \(W\) is defined for all

\[
\theta\le0
\]

and

\[
\boxed{
\sup_{\theta\le0}E(\theta)\le E_*<\infty.
}
\]

For every \(T>0\), apply the forward contraction from \(-T\) to \(0\):

\[
E(0)
\le
e^{-T/2}E(-T)
\le
E_*e^{-T/2}.
\]

Letting \(T\to\infty\),

\[
\boxed{E(0)=0.}
\]

Hence

\[
W(\cdot,0)=0.
\]

Applying the same argument with any terminal time \(\theta_0\le0\),

\[
\boxed{W\equiv0.}
\]

Therefore

\[
\boxed{
\text{uniformly L2-bounded ancient linear similarity vorticity}
\Longrightarrow
W\equiv0.
}
\]

---

## 5. Recurrent version

A nonzero recurrent orbit would require, along a sequence of positive time gaps, return of the L2 mass to a previous nonzero level.

But strict contraction gives

\[
E(\theta+T)
\le e^{-T/2}E(\theta)
<E(\theta)
\]

for every \(T>0\) whenever \(E(\theta)>0\).

Thus

\[
\boxed{
\text{nonzero finite-energy recurrence}
\text{ is impossible for the exact linear similarity equation}.
}
\]

---

## 6. Relation to M17-248

M17-248 shows that \(\kappa\) can turn over through purely linear diffusion without paying an amplitude-independent physical energy cost.

M17-249 supplies the complementary long-time fact:

\[
\boxed{
\text{linear diffusion may reform kappa locally,}
\quad
\text{but it cannot sustain a nonzero bounded ancient/recurrent L2 state.}
}
\]

Thus the linear-diffusive escape is not a terminal recurrent mechanism if a nonzero bounded ancient linear limit can be extracted.

---

## 7. What is required to apply this endpoint to M17 packets

For a sequence of low-amplitude intrinsic packets, one would need to construct rescaled normalized fields \(V_j\) such that, after subsequence,

\[
V_j\to V
\]

and prove all of the following:

1. **nonzero mass:**
   \[
   \|V(0)\|_2>0;
   \]
2. **uniform L2 control on every backward compact time interval;**
3. **backward lifetime tending to infinity in parabolic units;**
4. **ambient/nonlocal forcing vanishes in the limit;**
5. **interface/cutoff forcing vanishes on interior cylinders;**
6. **scale comparability/compactness:** enough upper derivative control to pass to the linear equation.

Only then may M17-249 be invoked.

---

## 8. Current status of these prerequisites

- M17-224/M17-232 provide buffered/nested raw spatial extraction.
- M17-225--226 provide only fixed-order parabolic persistence/payment bookkeeping, not arbitrarily long backward lifetime.
- M17-243 removes local self-strain as an order-one payer at low amplitude.
- M17-244 restricts quiet ambient strain cancellation to \(\ell\lesssim R^{-1}\).
- M17-245 shows the full local self-nonlinearity is \(o(1)\) relative to diffusion.
- M17-247 removes quiet strain cancellation as the dominant **scale-comparable shell spectral carrier**.

Still missing are a scale-comparable nonzero tangent extraction and a backward genealogy theorem producing ancient lifetime.

---

## 9. DSD audit

- The linear L2 identity is exact and global.
- Ancient boundedness is an explicit hypothesis of the Liouville endpoint.
- A forward diffusion estimate is not reversed.
- A local packet is not declared to be a global linear solution.
- M17-249 identifies the endpoint theorem; it does not assert that the nonlinear packet sequence already satisfies its hypotheses.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
