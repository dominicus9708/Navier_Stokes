# DSD M5-565 — Literature firewall prunes exact self-similar but not general DSS tail

Date: 2026-09-02

Status: **EXTERNAL-LIOUVILLE PRUNING / THE INHERITED GLOBAL `L6` BOUND IS ALREADY STRONG ENOUGH TO ELIMINATE AN EXACT TIME-INDEPENDENT BACKWARD SELF-SIMILAR PROFILE BY THE CLASSICAL TSai/NRS SELF-SIMILAR LIOUVILLE THEORY / EXACT BACKWARD DSS PROFILES ARE DIFFERENT: CHAE--WOLF DERIVE THE CRITICAL POINTWISE DECAY FOR SMOOTH DSS SOLUTIONS IN `C_t L^p_x`, `p>=3`, AND REMOVE THE DSS SINGULARITY WHEN THE DISCRETE SCALING FACTOR IS SUFFICIENTLY CLOSE TO ONE, BUT GENERAL NONZERO BACKWARD DSS REMAINS AN OPEN PROBLEM IN THE LITERATURE / THEREFORE THE RECURRENT CRITICAL CONVEYOR CAN BE PRUNED OF ITS CONTINUOUS-SCALING STATIONARY SUBBRANCH, WHILE FINITE-PERIOD DSS AWAY FROM THE NEAR-ONE REGIME AND APERIODIC RECURRENT HULLS REMAIN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inherited velocity class

The finite-enstrophy ancient package gives, in similarity variables,

\[
\boxed{
\|U(\theta)\|_{L^6(\mathbb R^3)}
\le C_6
}
\]

uniformly on the complete compact hull.

This follows from

\[
\|\nabla U\|_2
=\|W\|_2
\]

and Sobolev.

Thus any stationary or periodic similarity suborbit automatically lies in global `L6` at each similarity time.

---

## 2. Exact backward self-similar branch

Suppose first that

\[
\boxed{
U(y,\theta)=U_*(y)
}
\]

is independent of similarity time.

The physical solution is exactly backward self-similar:

\[
u(x,t)
=(-t)^{-1/2}
U_*\left(\frac{x}{\sqrt{-t}}\right).
\]

The profile satisfies

\[
U_*\in L^6(\mathbb R^3).
\]

Classical backward self-similar Liouville results of Nečas--Růžička--Šverák and Tsai show triviality for profiles in `L3`, and Tsai extends this to `Lp` for every `p>3`.

Since

\[
6>3,
\]

the inherited profile class is covered.

Therefore

\[
\boxed{
U_*\equiv0.
}
\]

But the selected hard core carries a nontrivial vorticity/record mark.

Hence

\[
\boxed{
\text{nontrivial exact backward self-similar stationary branch is closed.}
}
\]

---

## 3. Why global L6 does not similarly kill periodic similarity time

Now suppose

\[
\boxed{
U(y,\theta+T)=U(y,\theta)
}
\]

for some `T>0`.

The physical ancient solution is backward discretely self-similar with factor

\[
\boxed{
\lambda=e^{T/2}>1.
}
\]

At every time,

\[
U(\theta)\in L^6.
\]

However the stationary self-similar Liouville theorem applies to the elliptic Leray profile equation and does not automatically extend to the time-periodic Leray system.

The distinction is essential.

---

## 4. Chae--Wolf DSS result

Chae and Wolf, *Removing discretely self-similar singularities for the 3D Navier--Stokes equations* (2017), consider smooth backward `lambda`-DSS solutions.

Their Theorem 1.1 states that if

\[
u\in C(( -\infty,0);L^p(\mathbb R^3))\cap C^\infty,
\qquad
3\le p<\infty,
\]

and `u` is `lambda`-DSS, then it is regular away from the possible origin singularity and satisfies a pointwise critical decay

\[
\boxed{
|u(x,t)|
\le
\frac{C_*}{\sqrt{-t}+|x|}.
}
\]

Our exact DSS subbranch has `p=6`, so it lies within the hypothesis of this decay theorem.

---

## 5. Near-one DSS scaling is excluded

Chae--Wolf Theorem 1.3 further proves that for every fixed decay constant `C_*>0`, there exists

\[
\lambda_*(C_*)>1
\]

such that a smooth backward `lambda`-DSS solution satisfying

\[
|u(x,t)|
\le
\frac{C_*}{\sqrt{-t}+|x|}
\]

is trivial whenever

\[
\boxed{
1<\lambda<\lambda_*(C_*).
}
\]

Therefore the exact DSS survivor cannot occupy the near-continuous-scaling regime covered by this theorem.

In similarity period,

\[
T=2\log\lambda,
\]

so this removes a corresponding small-period DSS subbranch.

Firewall: without an audited uniform dependence of `C_*` on the compact-hull constants independent of `lambda`, this must not be rewritten as a universal numerical lower bound `T>=T_0` for every hypothetical DSS orbit.

---

## 6. General backward DSS is not closed by current literature

The same Chae--Wolf paper explicitly states that a general nontrivial backward DSS nonexistence theorem is not available.

Later work continues to treat nonzero backward DSS as a potential Type-I blow-up scenario.

In particular Barker--Prange's quantitative Type-I analysis discusses hypothetical nonzero `lambda`-DSS solutions even in the smooth class

\[
u\in C^\infty
\cap C(( -\infty,0);L^p(\mathbb R^3)),
\qquad
p\in[3,\infty).
\]

Thus the fact that our periodic profile lies in global `L6` does **not** invoke a known theorem eliminating arbitrary-period backward DSS.

---

## 7. Additional finite enstrophy does not yet match a known DSS Liouville theorem

Our class is stronger than merely `C_t L6_x` because it also carries

\[
\boxed{
\|W(\theta)\|_2<\infty
}
\]

uniformly, equivalently a finite Dirichlet integral for the similarity velocity.

A literature check did not identify a theorem saying that an arbitrary-period backward DSS solution is trivial solely from

\[
U(\theta)\in L^6,
\qquad
\nabla U(\theta)\in L^2
\]

uniformly over one similarity period.

This extra condition may be useful, but it cannot presently be cited as an existing closure theorem.

---

## 8. Revised recurrence classification

The tail recurrence hierarchy is now

\[
\boxed{
\text{recurrent critical conveyor}
\Longrightarrow
\begin{cases}
\text{stationary self-similar},\\
\text{periodic DSS},\\
\text{aperiodic recurrent}.
\end{cases}
}
\]

The first branch is removed by `L6` self-similar Liouville rigidity.

The second is partially removed in the near-one scaling regime but remains open for general `lambda`.

The third has no direct classical periodic/self-similar theorem.

Therefore the hard core becomes

\[
\boxed{
E_{tail}^{hard}
=
E_{DSS}^{finite\ period,\ unresolved}
\lor
E_{recurrent}^{aperiodic}.
}
\]

---

## 9. Relation to M5-562--564

M5-562 established that on a nontrivial invariant component global `L3` is infinite almost everywhere and fixed remote shells recur.

M5-563 showed that individual critical packets travel outward and therefore fixed-shell recurrence implies a historical scale genealogy.

M5-564 corrected the interpretation: the genealogy can be paid kinematically by similarity dilation and is not automatically a physical turnover event.

M5-565 now removes the limiting case where this conveyor is exactly stationary under **all** continuous scalings.

What remains is genuinely more general recurrence.

---

## 10. Next internal target

External Liouville theory does not close arbitrary DSS, so the next useful internal calculation is to use the **periodic finite-enstrophy identities themselves**.

For a hypothetical DSS orbit of period `T`, combine over one period:

\[
\frac14\int_0^T E\,d\theta
+
\int_0^T P\,d\theta
=
\int_0^T Q\,d\theta,
\]

with:

- the exact material-volume expansion factor `exp(3T/2)=lambda^3`;
- finite persistent lineage recurrence;
- fixed-shell critical Dirichlet recurrence;
- the M5-559 determinant source-shape payer identity;
- and M5-554 connector compression.

The question is whether exact periodic return makes one of the previously merely zero-mean ledgers algebraically incompatible with the volume/dilation multiplier `lambda^3`.

This is more specific than attacking the full aperiodic recurrent hull.

---

## 11. References used for this firewall

- Nečas, Růžička, Šverák, *On Leray's self-similar solutions of the Navier--Stokes equations*, Acta Math. 176 (1996).
- T.-P. Tsai, *On Leray's self-similar solutions of the Navier--Stokes equations satisfying local energy estimates*, Arch. Rational Mech. Anal. 143 (1998).
- D. Chae, J. Wolf, *Removing discretely self-similar singularities for the 3D Navier--Stokes equations*, Comm. PDE 42 (2017), 1359--1374.
- T. Barker, C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Comm. Math. Phys. 385 (2021), 717--792.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
