# DSD W1 D3 / Log-Shell Separation and Periodic Canonical Tail

Date: 2026-08-26

Status: **D3 VS LOG-SHELL ROLE SEPARATED / PREVIOUS SUBLINEAR-D3 FRONTIER DOWNGRADED / PERIODIC W1 ONE-PERIOD H^-1 DEFECT UPGRADED TO SUMMABLE STRONG-L3 SCALE DEFECT / CANONICAL LOG-PERIODIC FAR TAIL CONSTRUCTED / EXTERIOR TAIL-SUBTRACTED REMAINDER PROVED STRONG-L3 / FINAL CORE-TAIL INTERFACE RIGIDITY OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose and audit correction

The preceding endpoint calculation produced

\[
\langle D_3\rangle_\mu>0,
\]

where

\[
D_3(U)
=
\int
|U||\nabla U|^2
+
|U|^{-1}\sum_j(U\cdot\partial_jU)^2
\,dY.
\]

It was then tempting to make the next target

\[
\int_0^S D_3(U(s))ds=o(S).
\]

That target is not presently justified by the existing export/turnover ledgers.

The reason is a spatial-scale mismatch between `D3` and the already identified critical log-shell derivative cost.

This file first separates those two roles exactly. It then returns to the periodic W1 branch and upgrades the already proved one-period far-tail defect into a canonical strong-`L3` asymptotic tail.

---

## 2. `D3` is spacetime critical but discounts remote log radius at one Leray time

Use

\[
U(r\theta,s)=r^{-1}w(\rho,\theta,s),
\qquad
\rho=\log r.
\]

The exact polar derivative formula gives schematically

\[
|\nabla U|^2
=
r^{-4}\mathcal G[w]^2,
\]

where

\[
\mathcal G[w]^2
=
|\partial_\rho w-w|^2
+|\nabla_{S^2}w|^2.
\]

Since

\[
dY=r^3d\rho d\theta,
\]

we get

\[
|U||\nabla U|^2dY
=
r^{-2}|w|\mathcal G[w]^2\,d\rho d\theta.
\]

Also

\[
|U|^{-1}(U\cdot\partial_jU)^2
\le
|U||\partial_jU|^2,
\]

so

\[
\boxed{
D_3(A_R)
\le
2\int_{A_R}|U||\nabla U|^2dY.
}
\]

Thus a critical `1/r` shell contributes at the scale

\[
\boxed{D_3(A_R)\sim R^{-2}}
\]

when its log-cell amplitude and derivative profile are order one.

Therefore positive-density geometric shells can have

\[
\sum_k D_3(A_{R_k})<\infty.
\]

This agrees with the static shell-tower stress test and is an anti-proof constraint.

---

## 3. Comparison with the true shell-counting derivative functional

The repository already defined

\[
\mathfrak D_{\log}^{full}(A_R)
:=
\int_{A_R}|Y||\nabla U|^2dY.
\]

On `A_R={R<|Y|<2R}`,

\[
R\int_{A_R}|\nabla U|^2
\le
\mathfrak D_{\log}^{full}(A_R)
\le
2R\int_{A_R}|\nabla U|^2.
\]

Under the W1 Type-I shell envelope

\[
\|U\|_{L^\infty(A_R)}\le \frac{A_0}{R},
\]

we therefore have

\[
\begin{aligned}
D_3(A_R)
&\le
2\frac{A_0}{R}
\int_{A_R}|\nabla U|^2dY\\
&\le
\boxed{
2A_0R^{-2}\mathfrak D_{\log}^{full}(A_R).
}
\end{aligned}
\]

Hence

\[
\boxed{
D_3\text{ is the }R^{-2}\text{-discounted version of the log-shell derivative cost on the critical tail.}
}
\]

By contrast, the already proved shell-counting coercivity gives, on a bounded-amplitude critical tower,

\[
\mathfrak D_{\log}^{rad}
\ge
A_0^{-1}\|U\|_{L^3(\text{log interval})}^3-O(A_0^2).
\]

Thus the two observables have distinct jobs:

- `D3`: finite-core / spacetime-critical weighted dissipation;
- `Dlog`: unweighted log-radius shell-counting cost of the remote `1/r` memory.

The previous proposal to derive sublinear `D3` directly from the remote export ledger is therefore **downgraded from main frontier to an unsupported sufficient condition**.

---

## 4. Similarity-radial flux is not material turnover

At `p=3`, the local Leray identity contains the similarity-radial boundary term

\[
-\frac{R}{6}\int_{|Y|=R}|U|^3dS.
\]

Its dyadic log-radius mean reproduces

\[
-\frac{\mathscr R_3}{6}.
\]

This term comes from

\[
\frac12Y\cdot\nabla U
\]

in the Leray coordinate equation. It is therefore a similarity-coordinate dilation flux.

It must **not** be identified with the material/radial turnover term of a moving physical control volume.

Consequently

\[
\boxed{
\text{critical radial residue}
\not\Rightarrow
\text{physical turnover event}
}
\]

without an additional bridge lemma.

This prevents a false closure.

---

# Part II. Periodic W1: canonical far-tail construction

## 5. Inputs already proved for the periodic branch

Assume the surviving W1 minimal orbit is periodic with period

\[
S>0,
\qquad
U(s+S)=U(s).
\]

Set

\[
L:=S/2,
\qquad
\lambda:=e^L=e^{S/2}>1.
\]

The previous periodic-tail calculation established, in the fixed-annulus rescaled topology,

\[
\boxed{
w(\rho+L,\cdot,s)-w(\rho,\cdot,s)
=O(e^{-2\rho})
\quad\text{in }H^{-1}.
}
\]

Equivalently, if one represents each logarithmic cell on one fixed reference annulus/cylinder, there is a constant `C` independent of large `rho` and periodic time `s` such that

\[
\boxed{
\|\delta_\rho(s)\|_{H^{-1}}
\le
Ce^{-2\rho},
}
\]

where

\[
\delta_\rho
:=
w(\rho+L)-w(\rho)
\]

with the angular/log-cell variables suppressed.

The W1 shell estimates also give the uniform bound

\[
\boxed{
\|w(\rho)\|_{H^1(cell)}
\le C_1
}
\]

for every sufficiently remote log cell, hence

\[
\boxed{
\|\delta_\rho\|_{H^1(cell)}
\le 2C_1.
}
\]

---

## 6. Upgrade the one-period defect from `H^-1` to `L2`

On a fixed smooth annular cell, interpolation between `H^-1` and `H^1` gives

\[
\|f\|_{L^2}
\le
C
\|f\|_{H^{-1}}^{1/2}
\|f\|_{H^1}^{1/2}.
\]

Apply this to `delta_rho`:

\[
\begin{aligned}
\|\delta_\rho\|_2
&\le
C
(Ce^{-2\rho})^{1/2}
(2C_1)^{1/2}\\
&\le
\boxed{C_2e^{-\rho}}.
\end{aligned}
\]

Thus the periodic scale defect is already summable in `L2` across geometric periods.

---

## 7. Upgrade further to strong `L3`

The fixed-cell Sobolev bound gives

\[
\|\delta_\rho\|_6\le C_3.
\]

Interpolate between `L2` and `L6`:

\[
\|f\|_3
\le
\|f\|_2^{1/2}
\|f\|_6^{1/2}.
\]

Hence

\[
\boxed{
\|\delta_\rho\|_{L^3(cell)}
\le
C_4e^{-\rho/2}.
}
\]

Since the successive same-phase log cells are

\[
\rho_k=\rho_0+kL,
\]

we obtain

\[
\sum_{k\ge0}
\|\delta_{\rho_k}\|_3
\le
C_4e^{-\rho_0/2}
\sum_{k\ge0}e^{-kL/2}
<\infty.
\]

Therefore the same-phase sequence is Cauchy in strong `L3`.

---

## 8. Existence of a canonical log-periodic asymptotic trace

For each phase in one log period, define the strong-`L3` limit

\[
\boxed{
F_\infty
:=
\lim_{k\to\infty}w(\rho_0+kL,\cdot,s)
}
\]

on the reference cell.

The telescoping estimate yields the quantitative rate

\[
\begin{aligned}
\|w(\rho_k)-F_\infty\|_3
&\le
\sum_{j\ge k}
\|\delta_{\rho_j}\|_3\\
&\le
\boxed{
C_5e^{-\rho_k/2}.
}
\end{aligned}
\]

The construction is compatible on overlapping phase cells, so it defines a canonical asymptotic critical-amplitude field

\[
F_\infty(\theta,\rho,s)
\]

satisfying

\[
\boxed{
F_\infty(\theta,\rho+L,s)
=F_\infty(\theta,\rho,s).
}
\]

The far blow-down equation also passes to the limit:

\[
\left(\partial_s+\frac12\partial_\rho\right)F_\infty=0.
\]

Hence there exists a log-periodic profile `Phi` such that

\[
\boxed{
F_\infty(\theta,\rho,s)
=
\Phi\!\left(\theta,\rho-\frac{s}{2}\right),
\qquad
\Phi(\theta,\eta+L)=\Phi(\theta,\eta).
}
\]

This upgrades the earlier subsequential far blow-down into a canonical periodic asymptotic trace for the periodic W1 branch.

---

## 9. Canonical leading tail and strong-L3 exterior remainder

Define

\[
\boxed{
T(Y,s)
:=
|Y|^{-1}
\Phi\!\left(
\widehat Y,
\log|Y|-\frac{s}{2}
\right).
}
\]

Then `T` is an exact solution of the **linear dilation equation**

\[
T_s+\frac12T+\frac12Y\cdot\nabla T=0
\]

and is `S`-periodic in Leray time.

On the `k`th logarithmic period cell `C_k`, critical scaling gives

\[
\int_{C_k}|U-T|^3dY
=
\|w-F_\infty\|_{L^3(cell)}^3.
\]

Using the rate above,

\[
\boxed{
\int_{C_k}|U-T|^3dY
\le
C_6e^{-3\rho_k/2}.
}
\]

The geometric series converges:

\[
\sum_{k\ge0}e^{-3\rho_k/2}<\infty.
\]

Therefore for every sufficiently large fixed `R0`,

\[
\boxed{
U(\cdot,s)-T(\cdot,s)
\in
L^3(\{|Y|>R_0\})
}
\]

uniformly over periodic time `s`.

More quantitatively,

\[
\boxed{
\sup_s
\|U(s)-T(s)\|_{L^3(|Y|>R_0)}^3
\le
C R_0^{-3/2}.
}
\]

The exponent is the one obtained from the present `H^-1 -> L2 -> L3` interpolation and is not claimed optimal.

---

## 10. Nontriviality of the canonical trace

The W1 invariant positive-density shell result provides occupied far cells with

\[
\int_{A_R}|U|^3\ge m_0>0
\]

along a positive-density sequence.

Because

\[
\|U-T\|_{L^3(C_k)}\to0,
\]

any occupied same-phase subsequence forces

\[
\boxed{
\int_{cell}|F_\infty|^3>0.
}
\]

Thus on the nonzero periodic W1 branch the canonical tail is nontrivial whenever the occupied-shell sequence meets the corresponding phase class. Since there are only finitely many phase subcells in any fixed finite phase partition and occupied shells have positive lower density, at least one phase class is nontrivial.

No claim is made that every phase has positive mass without an additional density-uniformity argument.

---

## 11. What subtraction now achieves

Choose a smooth radial cutoff `chi` satisfying

\[
\chi=0\quad(|Y|\le R_0),
\qquad
\chi=1\quad(|Y|\ge2R_0).
\]

Define the tail-subtracted field

\[
\boxed{
Q:=U-\chi T.
}
\]

On the inner region, `Q=U` and is smooth.

On the outer region, `Q=U-T` and belongs to strong `L3`.

The transition annulus is bounded and smooth.

Therefore

\[
\boxed{
Q(\cdot,s)\in L^3(\mathbb R^3)
}
\]

for every `s`, with periodic time dependence.

This is the first actual construction of a global strong-`L3` quotient representative for the periodic W1 orbit after canonical subtraction of its passive critical memory.

---

## 12. Why this still does not invoke the standard periodic `L3` Liouville theorem

The quotient `Q` is **not** an unforced Navier-Stokes/Leray solution.

Substituting

\[
U=Q+\chi T
\]

into the full Leray equation produces

1. cutoff-interface forcing supported in `R0<|Y|<2R0`;
2. the nonlinear/viscous residual of the leading linear tail;
3. cross interactions between `Q` and `T`.

The leading tail satisfies only the linear dilation equation. Its nonlinear/viscous residual scales as

\[
O(|Y|^{-3}),
\]

which is spatially integrable in `L^q(|Y|>R0)` for every `q>1`, but it is not zero.

Therefore

\[
\boxed{
Q\in L^3
\not\Rightarrow
Q\text{ satisfies the unforced periodic Leray equation}.
}
\]

The strong-`L3` periodic Liouville theorem cannot yet be applied to `Q`.

---

## 13. New periodic frontier: finite interface / forced quotient

Before this note the periodic W1 endpoint was

\[
\text{recurrent core}
+
\text{nonzero asymptotically linear log-periodic memory}.
\]

It is now reduced further to

\[
\boxed{
\text{periodic W1}
=
\text{canonical linear critical tail }T
+
\text{global strong-}L^3\text{ quotient }Q,
}
\]

where the obstruction to a standard Liouville theorem is entirely the explicit coupling/forcing generated by the decomposition.

Thus the periodic branch is no longer a vague weak-`L3` tail problem. It is a **forced strong-`L3` quotient problem with a canonical weak-`L3` coefficient/tail**.

A sufficient next theorem would be one of:

\[
\boxed{
\text{periodic strong-}L^3\text{ quotient}
+
\text{canonical }1/r\text{ linear tail}
\Longrightarrow0,
}
\]

under the exact W1 coupling bounds, or

\[
\boxed{
\text{nonzero canonical tail}
\Longrightarrow
\text{finite-radius interface action of positive density},
}
\]

which could be routed to the existing H/T/projective ledgers.

---

## 14. Aperiodic branch remains separate

The construction above uses exact Leray periodicity in the one-period identity

\[
w(\rho+S/2)-w(\rho)=O(e^{-2\rho}).
\]

For an aperiodic minimal recurrent orbit there is no single exact period `S`, and `Lp`, `p>3`, recurrence does not control the unweighted log-radius topology.

Therefore this canonical-tail theorem does **not** automatically extend to the aperiodic minimal branch.

The two branches should now be attacked separately:

### Periodic

Canonical tail exists; reduce to forced `L3` quotient/interface rigidity.

### Aperiodic

Need a co-moving tail compactness/cohomology theorem or an independent recurrent-core rigidity argument.

---

## 15. Updated proof map

The audited W1 map is now

\[
W1
\Longrightarrow
P_{DSS}^{long}
\lor
A_{min}^{aper}.
\]

For the periodic branch,

\[
\boxed{
P_{DSS}^{long}
\Longrightarrow
T_{crit}^{canon}
+
Q_{L^3}^{periodic},
}
\]

with an explicit nonzero forcing/coupling obstruction.

For the aperiodic branch, the earlier invariant residue / finite-core endpoint identities remain valid, but no canonical tail has yet been produced.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
