# M18-070 — Negative amplitude/diffusion covariance forces a truncated low-amplitude high-diffusion sheath and high-amplitude low-diffusion core split

**Date:** 2026-09-11  
**Status:** UNBOUNDED-OBSERVABLE TRUNCATION / LAYER-CAKE COVARIANCE / DIFFUSIVE-SHEATH POPULATION THEOREM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-069 isolates the diffusion-depletion branch. For some \(q>p\ge2\), define

\[
w:=\rho^{q-p}
\]

and

\[
G_p
:=(p-1)|\nabla\log\rho|^2+|\nabla\xi|^2
\]

on the active set.

Then

\[
d_p=\mathbb E_p[G_p]
\]

and a quantitative diffusion drop

\[
d_p-d_q\ge\varepsilon>0
\]

implies

\[
\boxed{
\operatorname{Cov}_p(G_p,w)
\le
-\varepsilon\mathbb E_p[w]<0.
}
\]

The obstacle is that \(G_p\) need not be bounded pointwise near low-amplitude/zero corridors.

The present module removes that obstacle without introducing an illegitimate \(L^\infty\) assumption.

The result is a quantitative two-population theorem:

\[
\boxed{
\text{low amplitude + high normalized diffusion}
\quad\text{and}\quad
\text{high amplitude + low normalized diffusion}
}
\]

both occur with fixed positive \(\mathbb P_p\)-measure after a finite truncation.

## 2. Basic bounds

On the compact CE-H hull,

\[
0\le\rho\le M_*<\infty.
\]

Hence

\[
0\le w\le W_*:=M_*^{q-p}<\infty.
\]

Also

\[
G_p\ge0
\]

and

\[
\mathbb E_p[G_p]=d_p<\infty.
\]

Let

\[
\boxed{
C_*:=-\operatorname{Cov}_p(G_p,w)>0.
}
\]

On the M18-069 half-gap branch one may take

\[
C_*
\ge
\frac{\delta_{pq}}2\mathbb E_p[w].
\]

The proof below only needs \(C_*>0\).

## 3. Finite truncation captures a fixed fraction of the covariance

For \(K>0\), define

\[
\boxed{
G_p^{(K)}:=\min\{G_p,K\}
}
\]

and the tail

\[
T_K:=G_p-G_p^{(K)}\ge0.
\]

Then

\[
\operatorname{Cov}_p(G_p,w)
=
\operatorname{Cov}_p(G_p^{(K)},w)
+
\operatorname{Cov}_p(T_K,w).
\]

Because \(0\le w\le W_*\),

\[
\begin{aligned}
|\operatorname{Cov}_p(T_K,w)|
&\le
\mathbb E_p[T_Kw]
+
\mathbb E_p[T_K]\mathbb E_p[w]\\
&\le
2W_*\mathbb E_p[T_K].
\end{aligned}
\]

Since \(G_p\in L^1(\mathbb P_p)\),

\[
\mathbb E_p[T_K]\to0
\qquad(K\to\infty).
\]

Therefore there exists a finite

\[
\boxed{K_*<\infty}
\]

such that

\[
|\operatorname{Cov}_p(T_{K_*},w)|
\le
\frac{C_*}{2}.
\]

Hence

\[
\boxed{
\operatorname{Cov}_p(G_p^{(K_*)},w)
\le
-\frac{C_*}{2}.
}
\]

Thus an arbitrarily high diffusion tail is **not required** to carry the negative covariance on one fixed recurrent component: some finite diffusion truncation already sees a fixed fraction of it.

This is an existence statement for \(K_*\), not a universal record-independent threshold across every possible component.

## 4. Layer-cake covariance formula

Set

\[
X:=G_p^{(K_*)}
\in[0,K_*],
\qquad
Y:=w
\in[0,W_*].
\]

For bounded nonnegative variables, the covariance has the exact layer-cake representation

\[
\boxed{
\operatorname{Cov}(X,Y)
=
\int_0^{K_*}\int_0^{W_*}
\Big[
\mathbb P_p(X>s,Y>t)
-
\mathbb P_p(X>s)\mathbb P_p(Y>t)
\Big]dt\,ds.
}
\]

Since

\[
\operatorname{Cov}(X,Y)
\le
-\frac{C_*}{2},
\]

there exist thresholds

\[
\boxed{
0\le s_*<K_*,

\qquad
0<t_*<W_*
}
\]

such that

\[
\boxed{
\mathbb P_p(X>s_*)\mathbb P_p(Y>t_*)
-
\mathbb P_p(X>s_*,Y>t_*)
\ge
\eta_*
}
\]

with

\[
\boxed{
\eta_*
:=
\frac{C_*}{2K_*W_*}>0.
}
\]

A threshold with \(t_*=0\) cannot carry positive deficit, so the amplitude threshold is genuinely positive.

## 5. Two cross-populations have fixed positive measure

Define

\[
A:=\{X>s_*\},
\qquad
B:=\{Y>t_*\}.
\]

The deficit identity gives

\[
\mathbb P_p(A)\mathbb P_p(B)-\mathbb P_p(A\cap B)
\ge\eta_*.
\]

For the high-amplitude / low-diffusion cross population,

\[
\begin{aligned}
\mathbb P_p(B\cap A^c)
&=\mathbb P_p(B)-\mathbb P_p(A\cap B)\\
&\ge
\mathbb P_p(B)(1-\mathbb P_p(A))+\eta_*\\
&\ge\eta_*.
\end{aligned}
\]

Similarly, for the low-amplitude / high-diffusion cross population,

\[
\begin{aligned}
\mathbb P_p(A\cap B^c)
&=\mathbb P_p(A)-\mathbb P_p(A\cap B)\\
&\ge
\mathbb P_p(A)(1-\mathbb P_p(B))+\eta_*\\
&\ge\eta_*.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathbb P_p(B\cap A^c)
\ge\eta_*,
\qquad
\mathbb P_p(A\cap B^c)
\ge\eta_*.
}
\]

## 6. Convert thresholds back to amplitude and true diffusion

Since

\[
Y=w=\rho^{q-p},
\]

define

\[
\boxed{
a_*:=t_*^{1/(q-p)}>0.}
\]

Then

\[
B=\{\rho>a_*\}.
\]

Because \(s_*<K_*\),

\[
X>s_*
\quad\Longleftrightarrow\quad
G_p>s_*.
\]

Also

\[
X\le s_*
\quad\Longrightarrow\quad
G_p\le s_*.
\]

Hence the two positive-measure populations are

\[
\boxed{
\mathcal P_{core}
:=
\{\rho>a_*,\ G_p\le s_*\},
}
\]

and

\[
\boxed{
\mathcal P_{sheath}
:=
\{\rho\le a_*,\ G_p>s_*\}.
}
\]

They satisfy

\[
\boxed{
\mathbb P_p(\mathcal P_{core})\ge\eta_*,

\qquad
\mathbb P_p(\mathcal P_{sheath})\ge\eta_*.
}
\]

This is the desired quantitative diffusive-core/sheath split.

## 7. The sheath carries a fixed derivative payment

On \(\mathcal P_{sheath}\),

\[
G_p>s_*.
\]

Therefore

\[
\mathbb E_p
\left[
G_p\mathbf1_{\mathcal P_{sheath}}
\right]
\ge
s_*\eta_*.
\]

Restoring the normalization of \(\mathbb P_p\),

\[
\boxed{
\left\langle
\int_{\mathcal P_{sheath}}
\rho^pG_p\,dy
\right\rangle
\ge
s_*\eta_*\langle M_p\rangle.
}
\]

But

\[
\rho^pG_p
=
(p-1)\rho^{p-2}|\nabla\rho|^2
+
\rho^p|\nabla\xi|^2.
\]

Thus the lower-amplitude population carries a fixed positive weighted amplitude-gradient/director-gradient payment.

If \(s_*=0\), the cross-population theorem remains valid but this particular positive derivative floor is vacuous. In that case one may choose a nearby positive layer threshold whenever a fixed portion of the covariance lies above positive diffusion; otherwise the covariance is carried by arbitrarily small positive diffusion values and must be analyzed by the distribution near zero. No positive floor is claimed automatically.

## 8. High-amplitude core has controlled normalized diffusion

On \(\mathcal P_{core}\),

\[
G_p\le s_*<K_*.
\]

Therefore the mandatory high-amplitude population selected by the diffusion-depletion branch is not a high-gradient spike population.

It is a recurrent high-amplitude population with bounded normalized amplitude/director diffusion.

This sharpens the qualitative M18-069 picture:

\[
\boxed{
\text{diffusion-depletion branch}
\to
\text{smooth(er) high-amplitude core}
+
\text{lower-amplitude derivative sheath}.
}
\]

## 9. Spatial/material realization split

The theorem so far is joint recurrent measure-theoretic.

As in M18-064--065, there are two geometric realizations.

### A. Same-state / same-component core-sheath realization

If fixed fractions of \(\mathcal P_{core}\) and \(\mathcal P_{sheath}\) occur in one bounded controlled state/component, then there is an actual amplitude transition between

\[
\rho>a_*
\]

and

\[
\rho\le a_*.
\]

The sheath already carries derivative payment; no derivative of \(G_p\) is needed.

This routes directly to the existing

\[
\boxed{
G_{amplitude\ gradient/director\ sheath}
\lor
G_{zero/interface}
}
\]

architecture.

### B. Component / lineage / phase segregation

If the populations do not coexist in one controlled connected realization, then the branch is

\[
\boxed{
G_{component/genealogy/recurrent\ phase\ core\text{-}sheath\ segregation}.
}
\]

This is already a typed material/phase exit.

## 10. Relation to the M16 residence covariance branch

For \(p=2\), the sheath payment is

\[
\rho^2G_2
=|\nabla W|^2.
\]

Thus the low-amplitude/high-diffusion population carries ordinary palinstrophy density.

Combining with M16-021, the flux-neutral residence-covariance survivor has the ordered picture

\[
\boxed{
\begin{array}{c}
\text{high-amplitude concentration: less negative }\kappa,
\text{ lower normalized palinstrophy},\\[1mm]
\text{lower-amplitude residence/sheath: more negative }\kappa,
\text{ higher normalized palinstrophy}.
\end{array}
}
\]

This places the negative coefficient debt and the derivative burden in the same lower-amplitude side of the recurrent material architecture.

That is a genuine structural gain, but it remains compatible with a recurrent sheath/core cycle.

## 11. Ancestry firewall

The fixed sheath derivative payment does not evade M18-058--059.

For \(p=2\), it is palinstrophy-scale and therefore inherits the same ancestry/economics limitations already audited.

For higher \(p\), the weighted derivative charge is bounded by compact-amplitude multiples of palinstrophy and does not create a new finite original-parent resource.

Hence

\[
\boxed{
\text{quantitative diffusive sheath}
\not\Rightarrow
\text{global ancestry contradiction}.
}
\]

The gain is localization and material interpretation.

## 12. Audit verdict

### Certified

1. Finite \(L^1(\mathbb P_p)\) control of \(G_p\) is sufficient; no pointwise \(L^\infty\) bound is needed.
2. A finite truncation \(G_p^{(K_*)}\) captures a fixed fraction of the negative amplitude/diffusion covariance.
3. The bounded covariance has an exact layer-cake representation.
4. Therefore there exist finite thresholds \(a_*>0\) and \(s_*<\infty\) with fixed positive recurrent mass in both
   \[
   \{\rho>a_*,\ G_p\le s_*\}
   \]
   and
   \[
   \{\rho\le a_*,\ G_p>s_*\}.
   \]
5. The lower-amplitude population is the derivative sheath and the high-amplitude population is normalized-diffusion depleted.
6. For \(p=2\), the sheath payment is ordinary palinstrophy and aligns with the M16 negative-\(\kappa\) residence architecture.

### Not certified

- a universal truncation threshold independent of recurrent component;
- same-state/component coexistence of the two populations;
- a new finite resource beyond palinstrophy/weighted diffusion;
- ancestry closure;
- remote/critical closure;
- global regularity.

## 13. Next target

After M18-070, the CE-H multi-p survivor has two sharply typed local realizations:

1. **strain-segregation:** higher amplitude sees larger axial strain;
2. **diffusion-depletion:** higher amplitude forms a lower-diffusion core surrounded statistically/materially by a lower-amplitude derivative sheath.

Both are compatible with a source-core / dissipative-sheath cycle.

The next useful step is therefore not another moment identity. M18-071 should combine the **source-core / diffusive-sheath architecture** with the exact material flux law

\[
D_B\log\Phi=\kappa
\]

and test whether a sheath that carries both more negative \(\kappa\) and more derivative cost can remain attached to the same persistent flux lineage without inducing

- transverse flux loss/replacement;
- sheath-marker turnover;
- or a bounded-core interface current already priced by M5-521--522.

That is the next place where the signed material route can potentially produce a nonrecyclable event rather than another stationary covariance.
