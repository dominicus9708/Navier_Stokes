# DSD W1 Pressure-Gauge Repair and Exact Endpoint Routing

Date: 2026-08-26

Status: **ANNULAR PRESSURE-GAUGE GAP IDENTIFIED AND REPAIRED / ENDPOINT PRESSURE MEAN UPGRADED FROM A LOWER BOUND TO AN EXACT RESIDUE+DISSIPATION IDENTITY / LOCAL p=3 LEDGER ROUTES THE RESIDUE TO THE SIMILARITY-RADIAL BOUNDARY FLUX / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose of this audit

The preceding endpoint note established the critical-shell residue

\[
\mathscr R_3
=
\frac{M_{crit}}{\log 2}>0
\]

from the W1 invariant shell mass and used the Leray \(L^p\) identity

\[
\frac1p\frac d{ds}\|U\|_p^p
+
\frac{p-3}{2p}\|U\|_p^p
+
\nu D_p(U)
=
\Pi_p(U),
\]

where

\[
\Pi_p(U)
:=
\int_{\mathbb R^3}P\,\nabla\cdot(|U|^{p-2}U)\,dY.
\]

It then attempted to localize the pressure work shell by shell by subtracting an annular pressure mean.

That localization needs an additional gauge audit: a pressure constant may be subtracted globally, but a different constant cannot be discarded independently on every annulus unless the corresponding divergence/boundary correction is retained.

The first goal of this file is to repair that point.

The second goal is to show that, after repair, the endpoint pressure payer is not a new independent W1 mechanism. Its invariant mean splits exactly into

1. the critical similarity-radial residue \(\mathscr R_3/6\), and
2. the endpoint weighted viscous dissipation \(\nu\langle D_3\rangle_\mu\).

## 2. The annular gauge defect

Set

\[
f_p:=|U|^{p-2}U.
\]

On one annulus \(A_R=\{R<|Y|<2R\}\),

\[
\Pi_p(A_R)
=
\int_{A_R}P\,\nabla\cdot f_p\,dY.
\]

If \(m_R\) is a shell-dependent constant, then

\[
\int_{A_R}P\,\nabla\cdot f_p
=
\int_{A_R}(P-m_R)\,\nabla\cdot f_p
+
m_R\int_{A_R}\nabla\cdot f_p.
\]

The second term is generally nonzero because

\[
\int_{A_R}\nabla\cdot f_p
=
\int_{|Y|=2R}f_p\cdot n\,dS
-
\int_{|Y|=R}f_p\cdot n\,dS.
\]

Therefore the oscillation estimate for \(P-(P)_{A_R}\) does not, by itself, estimate the original annular contribution.

This is an audit gap in the uncorrected shell argument, not a contradiction in the global Leray identity.

## 3. One global asymptotic pressure gauge

Use the already established old-shell pressure oscillation estimate on fixed-thickness scale-equivalent annuli. In particular, for a thick annulus

\[
\widetilde A_R
=
\{R/2<|Y|<4R\},
\]

we use

\[
\|P-(P)_{\widetilde A_R}\|_{L^2(\widetilde A_R)}
\le C_P R^{-1/2}.
\]

The same estimate is obtained by the same scale-local pressure argument used for the dyadic old-shell bound; the enlargement by fixed factors changes only the universal localization constant.

Let

\[
m_R:=(P)_{A_R}.
\]

Because \(A_R\) and \(A_{2R}\) both lie in \(\widetilde A_R\), comparison with the thick-annulus mean gives

\[
|m_R-(P)_{\widetilde A_R}|
\le C R^{-2},
\]

and

\[
|m_{2R}-(P)_{\widetilde A_R}|
\le C R^{-2}.
\]

Hence

\[
\boxed{
|m_R-m_{2R}|
\le C R^{-2}.
}
\]

Along dyadic radii this is summable, so

\[
m_{2^kR}\to m_\infty(s)
\]

as \(k\to\infty\).

Pressure is defined only up to one time-dependent spatial constant, so choose the single global gauge

\[
P\mapsto P-m_\infty(s).
\]

Then

\[
\boxed{
|m_R|
\le
\sum_{j\ge0}C(2^jR)^{-2}
\le C'R^{-2}.
}
\]

This is the missing global-gauge step.

## 4. Repair of the remote pressure-work estimate

The oscillatory part obeys the previous estimate. For \(3\le p\le3+\delta\),

\[
\|\nabla\cdot f_p\|_{L^2(A_R)}
\le C R^{-(p-3/2)},
\]

so

\[
\left|
\int_{A_R}(P-m_R)\nabla\cdot f_p
\right|
\le
C R^{-1/2}R^{-(p-3/2)}
=
C R^{-(p-1)}.
\]

For the mean correction, the old-shell Type-I bound

\[
\|U\|_{L^\infty(A_R)}
\le A_0R^{-1}
\]

gives

\[
\left|
\int_{A_R}\nabla\cdot f_p
\right|
\le
C R^2(R^{-1})^{p-1}
=
C R^{3-p}.
\]

Together with \(|m_R|\le C R^{-2}\),

\[
\left|
m_R\int_{A_R}\nabla\cdot f_p
\right|
\le
C R^{-2}R^{3-p}
=
C R^{-(p-1)}.
\]

Therefore the original, globally gauge-fixed shell work satisfies

\[
\boxed{
|\Pi_p(A_R)|
\le C R^{-(p-1)},
\qquad
3\le p\le3+\delta.
}
\]

At \(p=3\),

\[
|\Pi_3(A_R)|\le CR^{-2}.
\]

Hence

\[
\boxed{
\sum_{k\ge K}
\sup_{3\le p\le3+\delta}
|\Pi_p(A_{2^kR_0})|
\le C(2^KR_0)^{-2}.
}
\]

Thus the remote pressure-work summability survives the audit, but only after the global-gauge correction above is included.

## 5. Endpoint convergence of the diffusion term

Recall

\[
D_p(U)
=
\int
|U|^{p-2}|\nabla U|^2
+
(p-2)|U|^{p-4}
\sum_j(U\cdot\partial_jU)^2
\,dY.
\]

For \(p\ge3\),

\[
D_p
\le
(p-1)
\int |U|^{p-2}|\nabla U|^2.
\]

On sufficiently remote W1 shells, \(|U|\le1\), so for \(p\ge3\)

\[
|U|^{p-2}\le |U|.
\]

The old-shell bounds give

\[
\int_{A_R}|U||\nabla U|^2
\le
\|U\|_{L^\infty(A_R)}
\|\nabla U\|_{L^2(A_R)}^2
\le
C R^{-1}R^{-1}
=
CR^{-2}.
\]

The dyadic tail is summable. On every fixed core, local analyticity and compactness of the W1 recurrent class give uniform domination.

Therefore dominated convergence yields

\[
\boxed{
\lim_{p\downarrow3}
\int D_p(U)\,d\mu(U)
=
\int D_3(U)\,d\mu(U),
}
\]

where

\[
D_3(U)
=
\int
|U||\nabla U|^2
+
|U|^{-1}
\sum_j(U\cdot\partial_jU)^2
\,dY,
\]

with the second integrand interpreted continuously as zero at \(U=0\).

## 6. Exact invariant endpoint pressure identity

Invariant averaging of the global \(L^p\) balance gives

\[
\frac{p-3}{2p}
\int\|U\|_p^p\,d\mu
+
\nu\int D_p\,d\mu
=
\int\Pi_p\,d\mu.
\]

The Abelian endpoint residue already proved in the repository is

\[
\lim_{p\downarrow3}
(p-3)
\int\|U\|_p^p\,d\mu
=
\mathscr R_3
=
\frac{M_{crit}}{\log2}.
\]

Combining this with the diffusion convergence gives the exact endpoint identity

\[
\boxed{
\lim_{p\downarrow3}
\int\Pi_p\,d\mu
=
\frac{\mathscr R_3}{6}
+
\nu\int D_3\,d\mu.
}
\]

Equivalently,

\[
\boxed{
\lim_{p\downarrow3}
\langle\Pi_p\rangle_\mu
=
\frac{M_{crit}}{6\log2}
+
\nu\langle D_3\rangle_\mu.
}
\]

This strictly strengthens the earlier lower bound

\[
\liminf_{p\downarrow3}\langle\Pi_p\rangle_\mu
\ge
\frac{\mathscr R_3}{6}.
\]

The endpoint pressure payer consists of an exact critical residue plus endpoint weighted dissipation.

## 7. Positive weighted dissipation from the critical tail

Let

\[
w=|U|^{3/2}.
\]

Then

\[
|\nabla w|^2
\le
\frac94|U||\nabla U|^2.
\]

The three-dimensional Hardy inequality gives

\[
\int\frac{|w|^2}{|Y|^2}\,dY
\le
4\int|\nabla w|^2\,dY.
\]

Hence

\[
\boxed{
\int\frac{|U|^3}{|Y|^2}\,dY
\le
9D_3(U).
}
\]

Average in \(\mu\). Since

\[
M_\mu(R)
:=
\int\int_{R<|Y|<2R}|U|^3\,dY\,d\mu
\to
M_{crit}>0,
\]

choose one sufficiently large dyadic starting radius \(R_0\) such that

\[
M_\mu(2^kR_0)
\ge
\frac12M_{crit}
\qquad(k\ge0).
\]

Then

\[
\begin{aligned}
\langle D_3\rangle_\mu
&\ge
\frac19
\sum_{k\ge0}
\int\int_{A_{2^kR_0}}
\frac{|U|^3}{|Y|^2}
\,dY\,d\mu
\\
&\ge
\frac19
\sum_{k\ge0}
\frac{M_{crit}/2}{4(2^kR_0)^2}
\\
&=
\boxed{
\frac{M_{crit}}{54R_0^2}
}>0.
\end{aligned}
\]

Thus the endpoint pressure mean exceeds the pure Abelian residue by a strictly positive viscous amount:

\[
\boxed{
\lim_{p\downarrow3}\langle\Pi_p\rangle_\mu
\ge
\frac{M_{crit}}{6\log2}
+
\frac{\nu M_{crit}}{54R_0^2}.
}
\]

The numerical constant is not claimed optimal; only strict positivity and explicit routing are needed here.

## 8. Exact local ball ledger

The Leray equation compatible with the repository's global \(L^p\) identity is

\[
\partial_sU
-
\nu\Delta U
+
(U\cdot\nabla)U
+
\frac12U
+
\frac12(Y\cdot\nabla)U
+
\nabla P
=0,
\qquad
\nabla\cdot U=0.
\]

On \(B_R\), multiply by \(f_p=|U|^{p-2}U\). Define

\[
E_{p,R}
=
\int_{B_R}|U|^p,
\qquad
D_{p,R}
=
\int_{B_R}
|U|^{p-2}|\nabla U|^2
+(p-2)|U|^{p-4}
\sum_j(U\cdot\partial_jU)^2,
\]

and

\[
\Pi_{p,R}
=
\int_{B_R}P\,\nabla\cdot f_p.
\]

A direct integration by parts gives

\[
\boxed{
\frac1pE_{p,R}'
+
\frac{p-3}{2p}E_{p,R}
+
\nu D_{p,R}
=
\Pi_{p,R}
+
\mathcal B_{p,R},
}
\]

with

\[
\begin{aligned}
\mathcal B_{p,R}
={}&
\nu\int_{\partial B_R}\partial_nU\cdot f_p\,dS
-
\frac1p\int_{\partial B_R}|U|^pU\cdot n\,dS
\\
&-
\frac{R}{2p}\int_{\partial B_R}|U|^p\,dS
-
\int_{\partial B_R}P f_p\cdot n\,dS.
\end{aligned}
\]

The four terms are respectively

1. viscous boundary flux;
2. material/advective flux;
3. similarity-radial flux;
4. pressure boundary flux.

This is the exact bridge that was missing between the endpoint \(L^p\) payer and the earlier turnover/boundary ledgers.

It is a bridge of mechanisms, not an identification of two previously different functionals.

## 9. Endpoint local invariant ledger

For fixed \(R\), local analyticity and compactness make \(E_{p,R}\) a bounded differentiable observable on the recurrent compact class. Invariance of \(\mu\) therefore gives

\[
\left\langle E_{p,R}'\right\rangle_\mu=0.
\]

Let \(p\downarrow3\). On a fixed ball all terms are uniformly locally controlled, so

\[
\boxed{
\nu\langle D_{3,R}\rangle_\mu
=
\langle\Pi_{3,R}\rangle_\mu
+
\langle\mathcal B_{3,R}\rangle_\mu.
}
\]

At \(p=3\),

\[
\begin{aligned}
\mathcal B_{3,R}
={}&
\nu\int_{\partial B_R}\partial_nU\cdot |U|U\,dS
-
\frac13\int_{\partial B_R}|U|^3U\cdot n\,dS
\\
&-
\frac{R}{6}\int_{\partial B_R}|U|^3\,dS
-
\int_{\partial B_R}P|U|U\cdot n\,dS.
\end{aligned}
\]

Thus the positive core pressure work is exactly routed into endpoint weighted dissipation plus physical boundary fluxes.

Recurrence alone does **not** force the pressure observable to have zero mean.

## 10. Log-radius recovery of the Abelian residue

Define the dyadic logarithmic radius average

\[
\mathfrak A_R[F]
:=
\frac1{\log2}
\int_R^{2R}F(r)\,\frac{dr}{r}.
\]

For

\[
Q_3(r,U)
:=
r\int_{|Y|=r}|U|^3\,dS,
\]

coarea gives

\[
\begin{aligned}
\mathfrak A_R[\langle Q_3(r)\rangle_\mu]
&=
\frac1{\log2}
\int\int_{R<|Y|<2R}|U|^3\,dY\,d\mu
\\
&=
\frac{M_\mu(R)}{\log2}
\to
\boxed{\mathscr R_3}.
\end{aligned}
\]

Therefore the similarity-radial part of the local \(p=3\) ledger satisfies

\[
\boxed{
\mathfrak A_R
\left[
-\frac16\langle Q_3(r)\rangle_\mu
\right]
\to
-\frac{\mathscr R_3}{6}.
}
\]

This is the physical/local-ledger representation of the same residue that appeared analytically as

\[
\lim_{p\downarrow3}
\frac{p-3}{2p}
\langle\|U\|_p^p\rangle_\mu
=
\frac{\mathscr R_3}{6}.
\]

The two are the same critical radial conveyor viewed in two different coordinates of the audit.

## 11. The remaining boundary terms vanish in log-radius average

The old-shell W1 bounds give, uniformly on remote dyadic annuli,

\[
\|U\|_\infty\lesssim R^{-1},
\qquad
\|\nabla U\|_2\lesssim R^{-1/2},
\qquad
\|P\|_2\lesssim R^{-1/2}
\]

in the globally fixed asymptotic gauge, while

\[
\int_{A_R}|U|^3
\]

stays uniformly bounded and has invariant mean tending to \(M_{crit}\).

For the advective boundary term,

\[
\mathfrak A_R
\left[
\left|
\int_{\partial B_r}|U|^3U\cdot n
\right|
\right]
=O(R^{-2}).
\]

For the viscous boundary term, coarea plus Cauchy-Schwarz gives

\[
\mathfrak A_R
\left[
\left|
\int_{\partial B_r}\partial_nU\cdot|U|U
\right|
\right]
=O(R^{-2}).
\]

For the pressure boundary term,

\[
\begin{aligned}
&\frac1{\log2}
\int_R^{2R}
\frac1r
\int_{\partial B_r}|P||U|^2\,dS\,dr
\\
&\qquad\le
\frac{C}{R}
\|P\|_{L^2(A_R)}
\||U|^2\|_{L^2(A_R)}
=O(R^{-2}),
\end{aligned}
\]

because

\[
\int_{A_R}|U|^4
\le
\|U\|_{L^\infty(A_R)}
\int_{A_R}|U|^3
=O(R^{-1}).
\]

Hence all non-radial boundary terms vanish in dyadic log-radius average.

Also

\[
D_3(A_R)\lesssim R^{-2},
\]

so \(D_{3,R}\uparrow D_3\) with a summable tail.

Applying \(\mathfrak A_R\) to the invariant local ledger and sending \(R\to\infty\) yields

\[
\boxed{
\lim_{R\to\infty}
\mathfrak A_R
[\langle\Pi_{3,r}\rangle_\mu]
=
\nu\langle D_3\rangle_\mu
+
\frac{\mathscr R_3}{6}.
}
\]

This exactly matches the global \(p\downarrow3\) identity from Section 6.

The match is a nontrivial consistency check on the repaired pressure routing.

## 12. DSD audit classification

### Formation / definition layer

The critical residue \(\mathscr R_3\), endpoint dissipation \(D_3\), and local boundary ledger are separately defined and gauge-audited.

### Axis/property layer

The W1 survivor retains

\[
M_{crit}>0,
\]

precompact recurrent Leray dynamics, old-shell Type-I decay, and local analyticity.

### Static aggregation layer

The \(p\downarrow3\) pole residue is exactly matched by the log-radius similarity flux.

### Dynamic routing layer

The formerly named finite-core pressure payer is not an independent terminal branch. In invariant mean it is routed as

\[
\boxed{
\text{endpoint pressure work}
=
\text{critical radial residue}
+
\text{weighted viscous dissipation}.
}
\]

The earlier moving-variance pressure term and the present \(L^3\) pressure term remain distinct functionals; they are connected only through explicit local boundary ledgers and must not be identified by name alone.

## 13. What this closes and what it does not

Closed by this note:

1. the shell-dependent pressure-gauge defect in the remote pressure summation;
2. the existence of one global asymptotic pressure gauge with \(|(P)_{A_R}|=O(R^{-2})\);
3. uniform \(R^{-(p-1)}\) remote pressure-work summability in that gauge;
4. endpoint convergence of the diffusion term;
5. the exact endpoint pressure identity
   \[
   \langle\Pi_{3+}\rangle
   =\mathscr R_3/6+\nu\langle D_3\rangle;
   \]
6. the local-ball bridge showing that \(\mathscr R_3/6\) is the similarity-radial boundary residue;
7. strict positivity of \(\langle D_3\rangle\) under positive invariant critical shell mass.

Not closed:

1. a contradiction between positive \(M_{crit}\) and compact recurrent W1 dynamics;
2. a strict Lyapunov functional on the recurrent W1 class;
3. a proof that the positive endpoint weighted dissipation cannot be replenished by the critical radial conveyor;
4. exclusion of the surviving long-period DSS and aperiodic minimal recurrent branches.

## 14. Updated W1 frontier

The previous frontier

\[
M_{crit}>0
\Longrightarrow
\text{positive finite-core pressure payer}
\]

is replaced by the sharper audited routing

\[
\boxed{
M_{crit}>0
\Longrightarrow
\begin{cases}
\mathscr R_3=M_{crit}/\log2>0,\\
\langle D_3\rangle_\mu>0,\\
\displaystyle
\lim_{p\downarrow3}\langle\Pi_p\rangle_\mu
=
\mathscr R_3/6+\nu\langle D_3\rangle_\mu,
\end{cases}
}
\]

with the residue \(\mathscr R_3/6\) identified locally as the similarity-radial boundary conveyor.

Therefore the next genuine rigidity problem is no longer simply

> can recurrent dynamics carry positive core pressure work?

The sharper question is

\[
\boxed{
\text{Can a compact recurrent W1 orbit sustain simultaneously}
\quad
M_{crit}>0
\quad\text{and}\quad
\langle D_3\rangle_\mu>0
\]

through a perpetual critical radial replenishment loop without activating one of the already excluded H/turnover/export channels?

That is the next audited branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
