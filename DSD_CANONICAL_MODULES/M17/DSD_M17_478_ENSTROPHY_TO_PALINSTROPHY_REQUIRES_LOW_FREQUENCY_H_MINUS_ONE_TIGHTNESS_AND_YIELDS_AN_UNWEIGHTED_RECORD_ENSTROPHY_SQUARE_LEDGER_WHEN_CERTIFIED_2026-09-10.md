# M17-478 — Enstrophy-to-palinstrophy requires low-frequency H-minus-one tightness and yields an unweighted record enstrophy-square ledger when certified

**Date:** 2026-09-10  
**Status:** ACTIVE LOW-FREQUENCY FIREWALL / CONDITIONAL ENSTROPHY LEDGER

## 1. Purpose

M17-477 leaves normalized enstrophy decompactification as one way to weaken endpoint temporal thickening. A tempting response is to use finite kinetic energy and interpolate enstrophy against palinstrophy.

That route is mathematically correct **only if the relevant whole-space low-frequency norm survives the parent-to-record/ancient genealogy**. M17-407 already warns that high-frequency vorticity control does not by itself remove the low-frequency velocity tail.

This module identifies the missing norm exactly and states the conditional consequence without silently importing it.

## 2. Exact low-frequency quantity

Let \(u\) be whole-space divergence-free velocity with vorticity
\[
\Omega=\nabla\times u.
\]
For a divergence-free vorticity field with the Biot--Savart representative,
\[
\widehat u(\xi)
=\frac{i\xi\times\widehat\Omega(\xi)}{|\xi|^2}.
\]
Since \(\xi\cdot\widehat\Omega=0\),
\[
|\widehat u(\xi)|^2
=|\xi|^{-2}|\widehat\Omega(\xi)|^2.
\]
Therefore
\[
\boxed{
\|u\|_2^2
=\|\Omega\|_{\dot H^{-1}}^2.
}
\]

Define
\[
B_{-1}:=\|\Omega\|_{\dot H^{-1}}^2.
\]
This is exactly the low-frequency resource needed below.

## 3. Exact interpolation bridge

Let
\[
E:=\|\Omega\|_2^2,
\qquad
P:=\|\nabla\Omega\|_2^2.
\]
By Fourier Cauchy--Schwarz,
\[
\begin{aligned}
E
&=\int |\widehat\Omega|^2d\xi\\
&=\int
\left(|\xi|^{-1}|\widehat\Omega|\right)
\left(|\xi||\widehat\Omega|\right)d\xi\\
&\le
\|\Omega\|_{\dot H^{-1}}
\|\nabla\Omega\|_2.
\end{aligned}
\]
Hence
\[
\boxed{
E^2\le B_{-1}P.
}
\]
Equivalently, whenever \(B_{-1}<\infty\),
\[
\boxed{
P\ge\frac{E^2}{B_{-1}}.
}
\]

This inequality is exact at the level required for the audit; no CE-H assumption is needed beyond the whole-space divergence-free velocity-vorticity representation.

## 4. Scaling

Under the certified late-M17 scaling
\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]
the corresponding velocity scales as
\[
u_R(y,s)=R\,u(Ry,R^2s).
\]
Therefore
\[
\boxed{
B_{-1,R}
=\|u_R\|_2^2
=R^{-1}\|u\|_2^2
=R^{-1}B_{-1}.
}
\]
Also
\[
E_R=R E,
\qquad
P_R=R^3P,
\]
and indeed
\[
E_R^2\le B_{-1,R}P_R
\]
is scale-consistent.

## 5. Conditional record ledger

Suppose a certified parent-to-record family satisfies the low-frequency tightness bound
\[
\boxed{
B_{-1,m}(s)\le B_*R_m^{-1}
}
\]
on the normalized record intervals.

Then Section 3 gives
\[
E_m(s)^2
\le
B_*R_m^{-1}P_m(s).
\]
Integrating in normalized time,
\[
\boxed{
\int_{I_m}E_m(s)^2ds
\le
B_*R_m^{-1}
\int_{I_m}P_m(s)ds.
}
\]
M17-307 supplies
\[
\sum_mR_m^{-1}
\int_{I_m}P_m(s)ds<\infty.
\]
Consequently
\[
\boxed{
\sum_m
\int_{I_m}E_m(s)^2ds<\infty.
}
\]

This is an **unweighted record enstrophy-square spacetime ledger**, conditional on the \(R_m^{-1}\) low-frequency \(\dot H^{-1}\) scaling bound.

## 6. Occupation consequence

Let
\[
G_m(e_*):=\{s\in I_m:E_m(s)\ge e_*\}.
\]
Then
\[
e_*^2|G_m(e_*)|
\le
\int_{I_m}E_m(s)^2ds.
\]
Thus for every fixed \(e_*>0\),
\[
\boxed{
\sum_m|G_m(e_*)|<\infty.
}
\]

Therefore a certified record family cannot have a fixed positive normalized enstrophy floor on a non-summable amount of own-time across infinitely many records while the low-frequency \(\dot H^{-1}\) genealogy remains tight.

In particular, any proposed recurrent/positive-occupation branch with
\[
E_m\ge e_*>0
\]
on fixed normalized time fractions would contradict M17-307 **provided** the low-frequency hypothesis in Section 5 is certified.

## 7. Why this cannot be imported automatically into the ancient CE-H branch

The first-generation ancient profile may arise after a singular rescaling/compactness passage. High-frequency controls such as
\[
\int\|\nabla\Omega\|_2^2dt<\infty,
\qquad
\int\|\Delta\Omega\|_2^2dt<\infty
\]
do not control the Fourier neighborhood \(|\xi|\approx0\).

Thus they do not imply
\[
\Omega\in\dot H^{-1}
\]
or
\[
u\in L^2.
\]
A low-frequency velocity tail can survive even when all the cited high-frequency vorticity ledgers are finite.

Accordingly,
\[
\boxed{
\text{finite palinstrophy/raw-H2 does not certify the M17-478 }B_{-1}\text{ hypothesis.}
}
\]
This is the same structural warning already present in M17-407, now attached to an exact interpolation formula.

## 8. Correct branch split

For any argument that tries to convert persistent normalized enstrophy into ancestral palinstrophy, the admissible split is
\[
\boxed{
\begin{aligned}
G_{\rm persistent\ normalized\ enstrophy}
\Longrightarrow{}&
G_{\rm palinstrophy\ ancestry\ contradiction}\\
&\lor
G_{\dot H^{-1}\text{ low-frequency decompactification}}\\
&\lor
G_{\rm parent\text{-}to\text{-}record/domain/genealogy\ loss}.
\end{aligned}
}
\]
The first branch is available only if the \(B_{-1,m}\lesssim R_m^{-1}\) bound is actually certified.

## 9. Relation to M17-477

M17-477 showed that growing \(E_m^*\) weakens the endpoint raw-H2 thickening estimate. M17-478 refines the interpretation:

- if large normalized enstrophy occupies non-summable record time **and** low-frequency \(\dot H^{-1}\) tightness is retained, M17-307 closes it;
- if enstrophy becomes large only on rapidly shrinking time sets, temporal concentration remains OPEN;
- if the low-frequency \(\dot H^{-1}\) bound fails, that failure is a distinct low-frequency/genealogical exit and cannot be paid by raw-H2 or palinstrophy without additional input.

Thus `enstrophy decompactification` should no longer be treated as a single undifferentiated label.

## 10. Next target

The next audit should split M17-477's enstrophy exit into:

1. persistent high-enstrophy occupation, handled conditionally by M17-478;
2. short-time enstrophy spikes;
3. low-frequency \(\dot H^{-1}\) decompactification.

For the short-time spike branch, the natural question is whether the enstrophy evolution law plus the already certified raw-H2 control gives a one-sided minimum formation-time or integrated raw-H2 payment, analogous to M17-475 but one derivative lower.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
