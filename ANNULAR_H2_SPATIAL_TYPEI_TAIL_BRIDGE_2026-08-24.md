# Annular H2 -> Spatial Type-I Tail Bridge — 2026-08-24

Status: **EXPLICIT SUFFICIENT TAIL LEMMA / GLOBAL REGULARITY NOT PROVED.**

This note identifies scale-local shell quantities sufficient to upgrade the current temporal Type-I estimate to the spatial borderline decay required by Pineau–Vicol.

## 1. Dyadic annuli and critical shell quantities

For `R>=1`, let

\[
A_R=\{R<|Y|<2R\}
\]

and let `A_R^*` denote a fixed-factor enlargement, e.g.

\[
A_R^*=\{R/2<|Y|<4R\}.
\]

Define

\[
\boxed{
\mathfrak E_1(R,s)
:=R\int_{A_R^*}|\nabla V(Y,s)|^2dY
}
\]

and

\[
\boxed{
\mathfrak E_2(R,s)
:=R^3\int_{A_R^*}|\nabla^2V(Y,s)|^2dY.
}
\]

For the critical model `V~R^{-1}` these are both order one.

Because `div V=0`, the first quantity is equivalent at the whole-space level to a vorticity-shell critical quantity. The second is a palinstrophy/derivative-shell quantity.

## 2. Scaled H2 estimate for the mean-free part

Let

\[
m_R(s)=\fint_{A_R^*}V(Y,s)dY.
\]

Scale `Y=RZ`. The Sobolev embedding `H^2 -> L^infty` on a fixed annulus and Poincare give

\[
\boxed{
\|V-m_R\|_{L^\infty(A_R)}
\le
C\left[
R^{-1/2}\|\nabla V\|_{L^2(A_R^*)}
+R^{1/2}\|\nabla^2V\|_{L^2(A_R^*)}
\right].
}
\]

In terms of the critical shell quantities,

\[
\boxed{
\|V-m_R\|_{L^\infty(A_R)}
\le
\frac{C}{R}
\left[
\mathfrak E_1(R,s)^{1/2}
+
\mathfrak E_2(R,s)^{1/2}
\right].
}
\]

Thus the only remaining issue is the annular mean.

## 3. Adjacent-shell mean difference

Let `R_k=2^kR`. Comparing the means on two adjacent overlapping shells and using Poincare on their union gives

\[
\boxed{
|m_{R_k}-m_{R_{k+1}}|
\le
\frac{C}{R_k}
\mathfrak E_1(R_k,s)^{1/2}.
}
\]

The already established bound `V(s) in L6(R3)` implies

\[
|m_{R_k}|
\le C R_k^{-1/2}\|V(s)\|_6
\to0
\quad(k\to\infty).
\]

Therefore telescoping to infinity yields

\[
\boxed{
|m_R(s)|
\le
\frac{C}{R}
\sup_{\rho\ge R}\mathfrak E_1(\rho,s)^{1/2}.
}
\]

More precisely one has the summable dyadic formula

\[
|m_R|
\le
C\sum_{k\ge0}
\frac{\mathfrak E_1(2^kR,s)^{1/2}}{2^kR}.
\]

## 4. Spatial Type-I conclusion

Assume on the late recurrent corridor

\[
\boxed{
\sup_s\sup_{R\ge R_0}\mathfrak E_1(R,s)\le E_*,
\qquad
\sup_s\sup_{R\ge R_0}\mathfrak E_2(R,s)\le H_*.
}
\]

Combining the mean and mean-free estimates gives

\[
\boxed{
|V(Y,s)|
\le
\frac{C(E_*^{1/2}+H_*^{1/2})}{|Y|}
\qquad(|Y|\ge2R_0).
}
\]

Together with the already known global boundedness of `V`,

\[
\boxed{
|V(Y,s)|
\le
\frac{C_*}{1+|Y|}
}
\]

uniformly in late Leray time.

This is exactly the borderline spatial Type-I profile bound appearing in the Pineau–Vicol 2026 theorem.

## 5. Exact failure split

Consequently the tail obstruction is reduced to

\[
\boxed{
\text{spatial Type-I tail}
\quad\lor\quad
H_{1,crit}^{tail}
\quad\lor\quad
H_{2,crit}^{tail},
}
\]

where

\[
H_{1,crit}^{tail}:
\sup_{R\to\infty}
R\int_{A_R}|\nabla V|^2=\infty,
\]

and

\[
H_{2,crit}^{tail}:
\sup_{R\to\infty}
R^3\int_{A_R}|\nabla^2V|^2=\infty.
\]

The second is a literal scale-critical derivative/palinstrophy tail. The first is a scale-critical vorticity/enstrophy shell failure, stronger than mere nonzero global L3 tail and distinct from order-one unscaled enstrophy escape.

These two failures must not be silently identified with the older `H_remote` unless the definitions are explicitly enlarged; they are the honest new tail subbranches exposed by the one-slice Type-I theorem.

## 6. Pressure-annulus input

Pineau–Vicol also assume the pressure is uniformly bounded on a fixed physical annulus away from the candidate singular center.

Once the spatial Type-I bound is available, velocity is uniformly bounded on every fixed annulus separated from the center. Standard interior Navier-Stokes regularity there gives uniform local derivative/Hölder control. Combining this local control with the pressure representation

\[
p=R_iR_j(u_iu_j)
\]

and finite global kinetic energy should supply the required annular pressure bound after fixing the additive time-dependent pressure gauge.

This pressure step is technically much smaller than the spatial tail step but is retained as a separate gauge lemma until written out completely.

## 7. Endgame implication

If both critical shell quantities are uniformly bounded, the spatial Type-I tail follows. After the pressure-annulus lemma, Pineau–Vicol Theorem 1.9 says that one sufficiently late time with small self-similar-time derivative regularizes the candidate singular point.

Therefore any survivor on this bounded-shell branch must maintain a uniform positive Leray-speed floor.

Status: **THE BORDERLINE `1/r` SPATIAL TYPE-I DECAY IS REDUCED TO TWO EXPLICIT DYADIC SHELL BOUNDS: `R int |grad V|^2` AND `R^3 int |grad^2 V|^2`. FAILURE PRODUCES A SCALE-CRITICAL ENSTROPHY OR PALINSTROPHY TAIL; SUCCESS OPENS THE 2026 ONE-SLICE REGULARITY GATE.**