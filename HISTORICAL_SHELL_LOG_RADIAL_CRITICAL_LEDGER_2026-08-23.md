# Historical-Shell Log-Radial Critical Ledger — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — A POSITIVE CRITICAL SHELL-COUNTING DERIVATIVE LEDGER IS IDENTIFIED — GLOBAL REGULARITY NOT PROVED.**

This note continues the surviving historical-shell branch after the smooth large-core and remote-halo pruning. The purpose is to isolate exactly why a geometric `1/r` historical tower can carry the `L3` divergence required by the ancient-solution Liouville obstruction while remaining compatible with the ordinary energy/enstrophy/palinstrophy ledgers.

The new point is an exact log-radial identity: on the retained Type-I shell envelope, logarithmic `L3` occupancy forces a logarithmically growing **scale-critical weighted radial derivative cost**.

---

## 1. Historical-shell scaling already present in the tower

At a late first-hitting stage `j`, an earlier stage `m` appears at normalized radius

\[
R_{j,m}\sim \frac{K_j}{K_m},
\]

with the natural Type-I amplitudes

\[
|U|\sim R_{j,m}^{-1},
\qquad
|\Omega|,|\Sigma|\sim R_{j,m}^{-2}.
\]

For geometric radii `R_n=q^n`, one critical shell has

\[
\int_{A_n}|U|^3dy\sim O(1).
\]

Therefore `N` occupied historical shells naturally give

\[
\|U\|_3^3\sim O(N),
\qquad
N\sim \log_q K.
\]

This is the previously isolated logarithmic ancient `L3` tail.

---

## 2. Exact log-radial coordinates

Write

\[
y=r\theta,
\qquad
s=\log r,
\qquad
F(s,\theta,\tau)=e^sU(e^s\theta,\tau)=rU(r\theta,\tau).
\]

Thus

\[
U(r\theta,\tau)=r^{-1}F(\log r,\theta,\tau).
\]

Since

\[
dy=r^2dr\,d\theta=r^3ds\,d\theta,
\]

the cubic norm has the exact identity

\[
\boxed{
\int_{e^{s_0}<|y|<e^{s_1}}|U|^3dy
=
\int_{s_0}^{s_1}\int_{S^2}|F(s,\theta)|^3d\theta\,ds.
}
\]

Hence `L3` is literally the unweighted occupancy measure in logarithmic radius.

For an exact degree `-1` tail

\[
F(s,\theta)=V(\theta),
\]

we obtain

\[
\boxed{
\|U\|_{L^3(1<r<K)}^3
=(\log K)\|V\|_{L^3(S^2)}^3.
}
\]

This makes the logarithmic divergence exact rather than heuristic.

---

## 3. Why weak-L3 can stay bounded

On the natural Type-I envelope assume

\[
|F(s,\theta)|\le A,
\]

i.e.

\[
|U(y)|\le \frac{A}{|y|}
\]

through the historical tower.

Then, for every `lambda>0`,

\[
\big|\{y:|U(y)|>\lambda\}\big|
\le
\frac{4\pi}{3}\left(\frac{A}{\lambda}\right)^3,
\]

up to the finite inner/outer truncation.

Therefore

\[
\boxed{
\|U\|_{L^{3,\infty}}
\le
\left(\frac{4\pi}{3}\right)^{1/3}A,
}
\]

independently of the number of occupied shells.

Thus a longer and longer `1/r` tower can have

\[
\|U\|_{L^{3,\infty}}=O(1)
\]

while

\[
\|U\|_3^3\sim c\log K\to\infty.
\]

This is precisely the endpoint gap that lets the historical-shell survivor evade the ancient `L3` Liouville theorem.

---

## 4. Ordinary derivative budgets discount remote logarithmic length

From

\[
U=r^{-1}F(s,\theta),
\]

we have the exact Euclidean polar decomposition

\[
\partial_rU
=r^{-2}(\partial_sF-F),
\]

and

\[
|\nabla U|^2
=r^{-4}
\left(
|\partial_sF-F|^2
+|\nabla_{S^2}F|^2
\right).
\]

Consequently

\[
\boxed{
\int_{e^{s_0}<r<e^{s_1}}|\nabla U|^2dy
=
\int_{s_0}^{s_1}e^{-s}
\int_{S^2}
\left(
|\partial_sF-F|^2+|\nabla_{S^2}F|^2
\right)d\theta\,ds.
}
\]

The ordinary dissipation/enstrophy scale therefore carries the factor `e^{-s}=r^{-1}`.

For geometric shells this gives the familiar summation

\[
\sum_nR_n^{-1}<\infty.
\]

Similarly, since `Omega` has degree `-2` on the critical tower and `nabla Omega` degree `-3`, the corresponding outer-shell palinstrophy weights are of order

\[
R_n^{-3},
\]

which are even more strongly summable.

Therefore ordinary derivative budgets can stay bounded while the unweighted logarithmic `L3` occupancy grows without bound.

This agrees with the previously established remote-halo passivity: derivative control kills order-one remote strain, but does not by itself remove a dynamically passive critical `L3` reservoir.

---

## 5. New critical weighted radial derivative functional

Define

\[
\boxed{
\mathfrak D_{\log}^{rad}[U;s_0,s_1]
:=
\int_{e^{s_0}<|y|<e^{s_1}}
|y|\,|\partial_rU(y)|^2dy.
}
\]

This quantity is invariant under Navier--Stokes spatial scaling.

Using the log-radial representation,

\[
\boxed{
\mathfrak D_{\log}^{rad}
=
\int_{s_0}^{s_1}\int_{S^2}
|\partial_sF-F|^2d\theta\,ds.
}
\]

The full weighted derivative quantity

\[
\mathfrak D_{\log}^{full}
:=
\int |y|\,|\nabla U|^2dy
\]

satisfies

\[
\boxed{
\mathfrak D_{\log}^{full}
=
\int
\left(
|\partial_sF-F|^2+|\nabla_{S^2}F|^2
\right)d\theta\,ds
\ge
\mathfrak D_{\log}^{rad}.
}
\]

Unlike ordinary dissipation, this functional does **not** discount remote shells by `R^{-1}`. It counts logarithmic scales at critical weight.

---

## 6. Exact coercive identity against L3 occupancy

Expand the radial term:

\[
\begin{aligned}
\mathfrak D_{\log}^{rad}
&=
\int
\left(
|\partial_sF|^2+|F|^2
-2F\cdot\partial_sF
\right)d\theta\,ds\\
&=
\int
\left(
|\partial_sF|^2+|F|^2
\right)d\theta\,ds
-
\left[
\|F(s)\|_{L^2(S^2)}^2
\right]_{s_0}^{s_1}.
\end{aligned}
\]

Hence

\[
\mathfrak D_{\log}^{rad}
\ge
\int_{s_0}^{s_1}\|F(s)\|_2^2ds
-
\|F(s_1)\|_2^2.
\]

Under `|F|<=A`,

\[
|F|^3\le A|F|^2,
\]

so

\[
\int\|F\|_2^2ds
\ge
A^{-1}
\int\|F\|_3^3ds.
\]

Also

\[
\|F(s_1)\|_2^2\le4\pi A^2.
\]

Combining with the exact cubic identity gives

\[
\boxed{
\mathfrak D_{\log}^{rad}[U;s_0,s_1]
\ge
A^{-1}
\|U\|_{L^3(e^{s_0}<r<e^{s_1})}^3
-4\pi A^2.
}
\]

Therefore a historical tower satisfying

\[
\|U\|_3^3\ge c_0\log K-O(1)
\]

must satisfy

\[
\boxed{
\mathfrak D_{\log}^{rad}
\ge
\frac{c_0}{A}\log K-O(A^2+1).
}
\]

This is the new shell-counting tax.

---

## 7. Exact `1/r` tower test

For

\[
U(r\theta)=r^{-1}V(\theta),
\]

we have `partial_s F=0`, so

\[
\mathfrak D_{\log}^{rad}
=(\log K)\|V\|_2^2,
\]

and

\[
\mathfrak D_{\log}^{full}
=(\log K)
\left(
\|V\|_2^2+\|\nabla_{S^2}V\|_2^2
\right).
\]

Thus the new tax does not vanish even on the quietest possible perfectly scale-stationary `1/r` tail.

This is stronger than a pure log-shape defect such as `int |partial_s F|^2`, which would vanish on the exact homogeneous tower.

---

## 8. Why this still does not prove global regularity

The new functional has two properties that the ordinary energy budget lacked:

1. it is scale-critical;
2. it is positive and coercive on a bounded-amplitude historical `L3` tower.

But the third property is still missing:

3. no a priori finite global bound for

\[
\int |x-x_c|\,|\nabla u(x,t)|^2dx
\]

is presently available at each time for arbitrary large smooth finite-energy data.

Indeed the same calculation shows exactly why the ordinary dissipation can remain finite:

\[
\int|\nabla U|^2
\]

uses the extra `e^{-s}` weight, whereas `mathfrak D_log` does not.

So this note does **not** close the historical-shell branch by itself. It identifies a concrete critical functional rather than merely stating that some new functional is needed.

---

## 9. Updated historical-shell dichotomy

The surviving branch can now be divided quantitatively.

### Branch H1 — natural Type-I amplitude envelope survives

If

\[
|rU(r\theta)|\le A
\]

through the historical tower and the required ancient `L3` mass grows like `c log K`, then

\[
\boxed{
\mathfrak D_{\log}^{rad}\gtrsim \log K.
}
\]

The survivor therefore carries an ever-growing critical weighted derivative moment.

### Branch H2 — the envelope fails

If `|rU|` is not uniformly bounded on the historical shells, then the tower is no longer the passive natural Type-I `1/r` survivor. The excess amplitude must be reclassified through the existing alternatives:

- super-Type-I parent-ball influx / multicore accumulation -> `T`;
- derivative concentration or remote active halo -> `H`;
- or a failure of the coherent projective/pressure frame.

This branch-routing still needs theorem-level quantitative thresholds, but the passive `1/r` branch itself is now assigned a definite critical cost.

---

## 10. Precise next theorem target

The next missing implication is no longer vague.

One needs to prove that, along a recurrent first-hitting Type-I sequence, logarithmic growth

\[
\boxed{
\mathfrak D_{\log}^{rad}(t_j;1,K_j)
\gtrsim
\log K_j
\to\infty
}
\]

cannot remain dynamically passive forever.

A successful closure may take one of the forms

\[
\mathfrak D_{\log}^{rad}\to\infty
\Longrightarrow
H,
\]

or

\[
\mathfrak D_{\log}^{rad}\to\infty
\Longrightarrow
T,
\]

or a projective-action inequality showing that recurrent `P_V` replenishment cannot coexist with this growing weighted derivative moment.

The important structural point is that the historical-shell escape route is now characterized by a **specific positive scale-critical observable**:

\[
\boxed{
\mathfrak D_{\log}^{rad}
=
\int |y|\,|\partial_rU|^2dy.
}
\]

---

## 11. Relation to known Liouville/self-similar exclusions

The Albritton--Barker ancient-solution Liouville theorem excludes a nontrivial mild bounded ancient survivor that stays bounded in global `L3` along a backward sequence. The historical tower intentionally avoids this by making global `L3` grow logarithmically.

Standard asymptotically discretely self-similar exclusions with an `L3` profile likewise do not directly eliminate the present tower because the limiting `1/r` tail is precisely at the weak-`L3` endpoint and is not globally `L3`.

Thus the new weighted derivative ledger targets the actual endpoint survivor rather than reusing a theorem whose hypotheses the survivor is designed to evade.

---

## 12. Current status

The previous global audit concluded that no standard positive scale-critical functional with a finite global total had been found.

This note improves that statement:

- a concrete **positive scale-critical shell-counting functional** has now been found;
- it is coercive on the bounded-amplitude historical `L3` tower;
- it grows at least logarithmically with the number of occupied historical scales;
- but its finite/global or dynamical routing side is not yet proved.

Status: **THE HISTORICAL `1/r` TOWER CAN NO LONGER BE CALLED COST-FREE AT CRITICAL SCALE. IT MUST PAY `mathfrak D_log^rad >= A^{-1} L3^3 - 4pi A^2`. THE REMAINING BOTTLENECK IS TO CONVERT THIS GROWING CRITICAL WEIGHTED DERIVATIVE MOMENT INTO `H`, `T`, PROJECTIVE FAILURE, OR A GLOBAL CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**
