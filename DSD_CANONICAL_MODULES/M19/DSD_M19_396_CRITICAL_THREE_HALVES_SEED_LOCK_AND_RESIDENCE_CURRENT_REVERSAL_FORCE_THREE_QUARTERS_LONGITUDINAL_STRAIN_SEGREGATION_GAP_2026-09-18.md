# M19-396 — Critical 3/2 seed lock and residence-current reversal force a 3/4 longitudinal strain segregation gap

Date: 2026-09-18

Status: **NEW CROSS-FRONTIER COMPATIBILITY TEST / M19-365'S CRITICAL SEED LOCK USES THE LOCAL LONGITUDINAL STRAIN ON A DISTINGUISHED MATERIAL SEED, WHILE M19-389 USES THE RHO-WEIGHTED STRAIN AVERAGE ALONG THE ASSOCIATED VORTEX-LINE SEGMENT. THEY MUST NOT BE IDENTIFIED SILENTLY. HOWEVER, ON A LONG COMPLETE POSITIVE-KAPPA EXCURSION WHOSE CRITICAL SEED PORTION DOMINATES THE DURATION, M19-365 GIVES `kappa_bar -> 3/2` AND `sigma_seed_bar -> -1/2`, WHEREAS RESIDENCE-CURRENT CANCELLATION/REVERSAL REQUIRES `sigma_bar_rho <= 1/4-kappa_bar -> -5/4`. THUS THE TWO MECHANISMS CAN COEXIST ONLY WITH A LONG-TIME LONGITUDINAL STRAIN SEGREGATION GAP OF AT LEAST `3/4`, OR WITH LINE/GENEALOGY/REPRESENTATION LOSS. IF THE LINE STRAIN IS ASYMPTOTICALLY HOMOGENEOUS, CURRENT REVERSAL IS IMPOSSIBLE AND THE SPATIAL KAPPA CURRENT RETAINS THE MATERIAL-FLUX SIGN. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two distinct strain observables

M19-365 follows a distinguished material seed point and uses its local longitudinal strain

\[
\boxed{
\sigma_{seed}(\theta)
=
\xi\cdot\Sigma\xi
}
\]

along that material trajectory.

M19-389 instead uses the rho-weighted strain average on the associated material vortex-line segment

\[
\boxed{
\bar\sigma_\rho(\theta)
=
\frac{
\int_{\Gamma(\theta)}\sigma\rho\,ds
}{
\int_{\Gamma(\theta)}\rho\,ds
}.
}
\]

These are different observables.

No proof may replace one by the other without a line-homogeneity or localization theorem.

---

## 2. Long critical positive-excursion branch

Consider a sequence of complete positive-kappa material excursions

\[
E_j=[\theta_{u,j},\theta_{d,j}]
\]

with durations

\[
T_j:=\theta_{d,j}-\theta_{u,j}\to\infty.
\]

Assume the M19-365 compact critical seed regime occupies all but \(o(T_j)\) of each excursion, so that

\[
\boxed{
\frac1{T_j}
\int_{E_j}\kappa_j\,d\theta
=
\frac32+o(1),
}
\]

and the distinguished seed strain satisfies

\[
\boxed{
\frac1{T_j}
\int_{E_j}\sigma_{seed,j}\,d\theta
=
-\frac12+o(1).
}
\]

This is the complete-excursion version of the critical seed lock. If the critical plateau does not dominate a complete excursion, that failure is retained as a phase/replacement boundary rather than silently assumed away.

---

## 3. Residence-current reversal requirement

M19-389--390 show that cancellation or reversal of the negative material-flux zero current on a complete positive excursion requires

\[
\int_{E_j}
\left(
\frac14-\bar\sigma_{\rho,j}
\right)d\theta
\ge
\int_{E_j}\kappa_j\,d\theta.
\]

Divide by \(T_j\):

\[
\frac1{T_j}
\int_{E_j}\bar\sigma_{\rho,j}\,d\theta
\le
\frac14
-
\frac1{T_j}
\int_{E_j}\kappa_j\,d\theta.
\]

Using the critical lock,

\[
\boxed{
\frac1{T_j}
\int_{E_j}\bar\sigma_{\rho,j}\,d\theta
\le
-\frac54+o(1).
}
\]

Thus the residence-weighted line strain must be substantially more compressive than the distinguished critical seed strain.

---

## 4. The 3/4 segregation gap

Subtract the two mean-strain relations:

\[
\begin{aligned}
\frac1{T_j}
\int_{E_j}
\left(
\sigma_{seed,j}
-
\bar\sigma_{\rho,j}
\right)d\theta
&\ge
\left(-\frac12\right)
-
\left(-\frac54\right)
+o(1)\\
&=
\frac34+o(1).
\end{aligned}
\]

Hence

\[
\boxed{
\liminf_{j\to\infty}
\frac1{T_j}
\int_{E_j}
\left(
\sigma_{seed,j}
-
\bar\sigma_{\rho,j}
\right)d\theta
\ge
\frac34.
}
\]

This is the critical compatibility gap.

---

## 5. Homogeneous-line corollary

Suppose instead that the critical seed line becomes asymptotically homogeneous in the sense

\[
\frac1{T_j}
\int_{E_j}
\left|
\sigma_{seed,j}
-
\bar\sigma_{\rho,j}
\right|d\theta
\to0.
\]

Then the 3/4 gap is impossible.

Therefore

\[
\boxed{
\text{critical }(3/2,-1/2)\text{ seed lock}
+
\text{linewise strain homogeneity}
\Longrightarrow
\text{no residence-current reversal}.
}
\]

On that branch the residence-weighted spatial zero current keeps the negative material-flux orientation rather than being canceled by line-residence bias.

This sends the branch back to the M5-683 constitutive-current problem with a certified current sign.

---

## 6. Segregated-line branch

If current reversal survives, then the line cannot remain strain-homogeneous.

The required branch is

\[
\boxed{
H_{\sigma,line}^{3/4}:
\quad
\frac1T
\int
\left(
\sigma_{seed}-\bar\sigma_\rho
\right)d\theta
\gtrsim
\frac34.
}
\]

This can occur through

1. strong longitudinal strain variation on one connected material line;
2. residence weight concentrating on line portions whose strain is much more negative than at the distinguished seed;
3. line-length/residence decompactification;
4. amplitude localization that causes the rho-weighted average to be carried by a different segment;
5. genealogy/representation change between the seed point and the line-residence carrier.

These are genuine geometric alternatives, not notation differences.

---

## 7. Conditional longitudinal-gradient price

On a regular material segment of length \(\ell\) where the seed point and the rho-weighted mean belong to the same represented line, a one-dimensional estimate gives schematically

\[
\left|
\sigma_{seed}-\bar\sigma_\rho
\right|^2
\lesssim
\ell
\int_\Gamma
|\partial_s\sigma|^2ds
\]

under the usual positive-amplitude comparability needed to interpret the weighted mean.

Therefore a fixed gap forces

\[
\boxed{
\int_\Gamma
|\partial_s\sigma|^2ds
\gtrsim
\frac1\ell.
}
\]

For bounded normalized line length this is an order-one strain-gradient payer.

For the canonical parent-length diffuse branch \(\ell\sim R\), however, the lower bound is only order \(R^{-1}\), exactly the critical/summable scale already warned about by M19-343.

Thus the segregation gap is structurally real but does not by itself defeat the parent-length firewall.

---

## 8. Relation to M19-365 transverse endpoint

M19-365 leaves the critical scalar lock with the split

\[
P_\perp\nabla(\sigma+\kappa)\neq0
\]

or an asymptotically homogeneous Burgers-like transverse endpoint.

M19-396 adds an independent longitudinal compatibility condition:

\[
\boxed{
\text{if spatial-current reversal survives,}
\quad
\text{the critical line must also be longitudinally strain-segregated}.
}
\]

Hence the most homogeneous critical endpoint becomes substantially narrower:

- transverse scalar forcing must be weak/homogeneous;
- longitudinal seed-vs-line strain must nevertheless differ by order one if current reversal is to occur.

A truly line-homogeneous critical endpoint cannot use residence weighting to reverse the current.

---

## 9. Updated critical-current split

The critical seed/current branch therefore refines to

\[
\boxed{
G_{seed}^{3/2}
\Longrightarrow
G_{spatial\ current}^{negative}
\lor
H_{\sigma,line}^{3/4}
\lor
G_{phase/replacement/genealogy}.
}
\]

On the first branch one can use the signed M5-683 spatial constitutive current.

On the second branch the next target is to determine whether the required longitudinal strain segregation is merely parent-length critical palinstrophy or can be attached to a nonreused productive subcarrier.

---

\[
\boxed{\text{M19-396 COMPLETE; CRITICAL CURRENT REVERSAL COSTS A 3/4 LONGITUDINAL STRAIN-SEGREGATION GAP.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
