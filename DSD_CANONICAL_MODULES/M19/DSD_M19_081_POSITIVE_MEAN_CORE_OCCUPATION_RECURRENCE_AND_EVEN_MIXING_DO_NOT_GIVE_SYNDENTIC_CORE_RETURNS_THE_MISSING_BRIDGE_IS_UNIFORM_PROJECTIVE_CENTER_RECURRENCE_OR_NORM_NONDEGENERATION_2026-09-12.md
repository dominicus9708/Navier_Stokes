# DSD M19-081 — Positive mean core occupation, recurrence, and even mixing do not give syndetic core returns; the missing bridge is uniform projective-center recurrence or norm nondegeneration

**Date:** 2026-09-12  
**Status:** TEMPORAL OBSERVABILITY FIREWALL / M19-079 CANNOT BE UPGRADED TO M19-080 BY RECURRENCE OR ERGODICITY ALONE / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-079 proved a positive long-time core-energy fraction for every bounded nonzero neutral linearized trajectory:

\[
\overline E_c\ge\delta_R\overline E.
\]

M19-080 proved that a much stronger fixed-window estimate

\[
\|W(0)\|_X^2
\le
C_{obs}
\int_{-\tau/2}^{\tau/2}
\|W(\theta)\|_{X(B_R)}^2d\theta
\tag{OBS}
\]

would force the bounded center fiber to be finite-dimensional.

The live question is whether recurrence supplies the missing temporal uniformity.

M19-081 shows that it does not, even abstractly under ergodicity and mixing.

## 2. Symbolic recurrent countermodel

Consider the two-sided Bernoulli shift

\[
\Sigma:=\{0,1\}^{\mathbb Z},
\qquad
(\sigma x)_n=x_{n+1},
\]

with Bernoulli measure \(\mu_p\),

\[
0<p<1.
\]

This compact dynamical system is ergodic and mixing.

For \(\mu_p\)-almost every point \(x\):

1. \(x\) is recurrent;
2. by the ergodic theorem,
   \[
   \boxed{
   \lim_{N\to\infty}
   \frac1N\sum_{n=0}^{N-1}x_n=p>0;
   }
   \]
3. for every integer \(L\ge1\), the cylinder word
   \[
   0^L
   \]
   has positive measure
   \[
   (1-p)^L>0,
   \]
   so a typical orbit contains blocks of at least \(L\) consecutive zeros infinitely often.

Thus one and the same recurrent mixing orbit has positive mean occupancy but arbitrarily long inactive gaps.

## 3. Energy interpretation

Define an abstract normalized total energy

\[
E(n)\equiv1
\]

and core energy

\[
\boxed{E_c(n):=x_n.}
\]

Then exterior energy is

\[
E_o(n)=1-x_n.
\]

The long-time core fraction is exactly

\[
\boxed{
\overline E_c=p\overline E>0.
}
\]

Nevertheless, for every prescribed window length \(L\), there are infinitely many intervals

\[
[n,n+L-1]
\]

such that

\[
\boxed{
E_c(k)=0
\qquad
n\le k<n+L.
}
\]

Hence no universal finite \(L\) can guarantee a positive core observation in every translated window.

## 4. Continuous-time suspension

To match the cocycle setting more closely, take the constant-roof suspension flow over the shift.

Let one symbolic step correspond to one unit of continuous time and define a bounded observable \(g_x(t)\) which equals \(x_n\) on the bulk of each interval \([n,n+1]\), with arbitrarily short smooth interpolation layers at the endpoints if continuity is desired.

Then

\[
\boxed{
\lim_{T\to\infty}
\frac1T\int_0^Tg_x(t)dt=p>0,
}
\]

while for every \(L<\infty\) there are time intervals of length approaching \(L\), and in fact arbitrarily larger lengths as the zero blocks grow, on which

\[
g_x(t)=0
\]

away from the optional interpolation collars.

Thus the distinction survives in a continuous-time compact recurrent flow.

## 5. Consequence for M19-079

The abstract example has all of the properties

\[
\boxed{
\text{compactness of the base}
+\text{recurrence}
+\text{ergodicity}
+\text{mixing}
+\text{positive mean occupation}
}
\]

but not syndetic returns to the active set.

Therefore the inference

\[
\boxed{
\overline E_c>0
\Longrightarrow
\text{fixed-window observability}
}
\]

is false without an additional dynamical property.

In particular, Poincare recurrence and Birkhoff positive density do not supply the bounded-gap estimate needed by M19-080.

## 6. Minimality would help for one fixed open set, but is not yet available in the center bundle

For a compact minimal topological flow, return times to any fixed nonempty open set are syndetic.

Indeed, if \(\mathcal G\) is nonempty open and the flow is minimal, finitely many translates of \(\mathcal G\) cover the compact minimal set. This gives a finite return-gap bound.

However the M19 center problem is not merely a flow on the base hull.

The relevant state is a pair

\[
\boxed{
(Y,[W])
}
\]

in a projectivized linear cocycle, because the core fraction depends on the perturbation direction as well as on the base state.

The good set is schematically

\[
\boxed{
\mathcal G_\eta
:=
\left\{
(Y,[W]):
\frac{E_c(W;R)}{E(W)}\ge\eta
\right\}.
}
\]

Base minimality alone does not imply syndetic return of every projective center direction to \(\mathcal G_\eta\).

## 7. Why projective compactness cannot simply be assumed

One might try to declare the projectivized bounded center fiber compact and then use minimality there.

But if the **entire** projective unit sphere of an infinite-dimensional linear center were compact in the strong topology, the center would already be finite-dimensional.

Thus

\[
\boxed{
\text{strong compactness of all projective center directions}
}
\]

would largely assume the conclusion sought in M19-080.

It cannot be used as a free replacement for observability.

## 8. Two genuinely noncircular sufficient routes

The present audit leaves two plausible types of additional input.

### Route A — uniform center norm nondegeneration

If the bounded center cocycle satisfied a two-sided uniform estimate

\[
\boxed{
 m\|W(s)\|_X
\le
\|W(t)\|_X
\le
M\|W(s)\|_X
\qquad
\forall s,t,
}
\tag{UC}
\]

for some

\[
0<m\le M<\infty,
\]

then arbitrarily long remote-damped intervals would be impossible without a compensating amount of core activity inside the same interval.

This route is analyzed next.

### Route B — a PDE-specific unique/projective recurrence mechanism

Alternatively one could prove directly that every non-symmetry center direction has a core-observation episode with a uniform bounded return gap, using:

- analyticity or unique continuation;
- a projective Harnack-type inequality;
- a Carleman observability estimate;
- or a PDE-specific cocycle recurrence theorem.

No such estimate has yet been certified in M19.

## 9. Relevance of the relative-periodic branch

A relative-periodic screw state from M19-076 has an exact finite return time modulo rotation.

For that branch, temporal syndeticity is automatic after modulation.

Thus the present firewall is primarily aimed at the genuinely aperiodic recurrent quotient branch.

This gives the updated branch distinction:

\[
\boxed{
\begin{aligned}
\text{relative periodic modulo }SO(3)
&\Rightarrow
\text{bounded return time available},\\
\text{aperiodic recurrent quotient}
&\Rightarrow
\text{positive mean alone does not bound return gaps}.
\end{aligned}
}
\]

## 10. What is certified

M19-081 certifies:

1. positive long-time occupation does not imply bounded-gap occupation;
2. recurrence does not repair that implication;
3. ergodicity does not repair it;
4. even mixing does not repair it;
5. the missing M19-079 \(\to\) M19-080 bridge must contain genuinely uniform information about the center cocycle, not merely the base invariant measure.

## 11. What is not claimed

The Bernoulli/suspension construction is an abstract dynamical countermodel.

It is **not** claimed to be an exact Navier--Stokes recurrent hull.

Its purpose is to certify that a proof using only recurrence/ergodicity/positive mean occupation is logically insufficient.

## 12. Next target

The most economical remaining route is to combine the remote damping inequality

\[
\frac12E'+c_*E_o\le K_RE_c
\]

with a uniform two-sided center bound (UC).

If this forces a fixed-window lower bound on

\[
\int E_c,
\]

then M19-080 immediately converts it to finite-dimensionality.

The next module should derive the sharp window length and observability constant under (UC), and then audit whether (UC) is actually known for the symmetry center or for any larger bounded-center bundle.

---

\[
\boxed{\text{M19-081 COMPLETE.}}
\]
