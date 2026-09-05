# DSD M17-156 — Critical mass envelope makes the OU packet eternal and an L2 Liouville argument forces it to vanish

Date: 2026-09-05  
Canonical ID: **M17-156**

Status: **CONDITIONAL LOW-AMPLITUDE PACKET BRANCH CLOSED / M17-155 REDUCES EVERY RELATIVE-THICK QUIET REMOTE PACKET TO THE LINEAR OU VORTICITY EQUATION AFTER AMPLITUDE NORMALIZATION. IF, IN ADDITION, THE PACKET VORTICITY MASS OBEYS THE NATURAL CRITICAL DILATION ENVELOPE ON EXPANDING TWO-SIDED SIMILARITY-TIME WINDOWS, THEN THE LIMIT IS A NONZERO ETERNAL `L2(R3)` OU SOLUTION WITH `||V(tau)||_2^2 <= C exp(-tau/2)`. THE EXACT FOURIER PROPAGATOR SHOWS THAT NO SUCH NONZERO ETERNAL `L2` SOLUTION EXISTS: BACKWARD EXTENSION TO ARBITRARILY LARGE NEGATIVE TIME WOULD FORCE THE TIME-ZERO FOURIER TRANSFORM TO HAVE FINITE GAUSSIAN MOMENTS OF ARBITRARILY LARGE STRENGTH, HENCE TO BE SUPPORTED AT FREQUENCY ZERO; AN `L2` FUNCTION WITH THAT SUPPORT IS ZERO. THIS CONTRADICTS `|V(0,0)|=1`. THEREFORE THE REMAINING RELATIVE-THICK QUIET PACKET MUST BREAK THE CRITICAL MASS ENVELOPE, THE BOUNDED-POTENTIAL/COMPACTNESS ASSUMPTION, OR THE QUIET SPACETIME CORRIDOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-155

Let `V_j` be the amplitude-normalized translated packets of M17-155.
After subsequence extraction on every fixed cylinder,

\[
V_j\to V,
\]

where

\[
\boxed{
\partial_\tau V
=\Delta V-\frac12z\cdot\nabla V-V,
}
\]

\[
\boxed{\nabla\cdot V=0,}
\]

and

\[
\boxed{|V(0,0)|=1.}
\]

Thus `V` is nonzero.

---

## 2. Critical packet-mass envelope

Let the unnormalized packet mass at the observation scale be `E_j(0)` and choose the amplitude normalization so that

\[
a_j^2\asymp E_j(0).
\]

The natural OU/Leray critical scaling for vorticity `L2` mass is

\[
E(\tau)\sim e^{-\tau/2}E(0).
\]

Assume there are time windows

\[
[-T_j,T_j],
\qquad
T_j\to\infty,
\]

such that the corresponding remote packet masses satisfy the uniform critical envelope

\[
\boxed{
E_j(\tau)
\le
C_Q e^{-\tau/2}E_j(0)
\qquad
(|\tau|\le T_j),
}
\]

with one constant `C_Q` independent of `j` and `tau`.

This is a genuine hypothesis. Its failure will be isolated separately as a mass-genealogy/turnover gate.

---

## 3. Global L2 bound of the limit

For every fixed `tau`, the translated remote shell eventually contains every fixed ball in `z`.
Dividing the packet/shell mass estimate by `a_j^2 asymp E_j(0)` gives

\[
\int_{B_L}|V_j(z,\tau)|^2dz
\le
C e^{-\tau/2}
\]

for every fixed `L`, uniformly in sufficiently large `j`.

Let `j->infinity`, then `L->infinity`.
Fatou gives

\[
\boxed{
\|V(\tau)\|_{L^2(\mathbb R^3)}^2
\le
C e^{-\tau/2}
\qquad(\tau\in\mathbb R).
}
\]

The expanding windows `T_j -> infinity` make `V` an **eternal** OU solution.

---

## 4. Exact Fourier evolution

Let

\[
\widehat V(\xi,\tau)
=\mathcal F_z[V](\xi,\tau).
\]

For

\[
\partial_\tau V
=\Delta V-\frac12z\cdot\nabla V-V,
\]

we have

\[
\boxed{
\partial_\tau\widehat V
=
\frac12\xi\cdot\nabla_\xi\widehat V
+\left(\frac12-|\xi|^2\right)\widehat V.
}
\]

For `tau>s`, the characteristic formula is

\[
\boxed{
\widehat V(\xi,\tau)
=
\exp\!\left(\frac{\tau-s}{2}\right)
\exp\!\left[-|\xi|^2\left(e^{\tau-s}-1\right)\right]
\widehat V\!\left(\xi e^{(\tau-s)/2},s\right).
}
\]

---

## 5. Invert from time zero to time `-T`

Set

\[
\tau=0,
\qquad
s=-T.
\]

Then

\[
\widehat V(\xi,0)
=
 e^{T/2}
 e^{-(e^T-1)|\xi|^2}
 \widehat V(\xi e^{T/2},-T).
\]

Equivalently,

\[
\widehat V(\eta,-T)
=
 e^{-T/2}
 e^{(1-e^{-T})|\eta|^2}
 \widehat V(e^{-T/2}\eta,0).
\]

Taking `L2` norms and changing variables gives the exact identity

\[
\boxed{
\|V(-T)\|_2^2
=
 e^{T/2}
\int_{\mathbb R^3}
 e^{2(e^T-1)|\xi|^2}
 |\widehat V(\xi,0)|^2d\xi.
}
\]

---

## 6. Critical envelope kills every nonzero frequency

The critical mass envelope gives

\[
\|V(-T)\|_2^2
\le
C e^{T/2}.
\]

Combine with the exact identity:

\[
\boxed{
\int
 e^{2(e^T-1)|\xi|^2}
 |\widehat V(\xi,0)|^2d\xi
\le C
\qquad\forall T>0.
}
\]

As `T->infinity`, the weight increases monotonically to `+infinity` at every `xi != 0`.
By monotone convergence,

\[
\widehat V(\xi,0)=0
\qquad\text{for a.e. }\xi\ne0.
\]

Thus the Fourier transform is supported at the single point `xi=0`.
But an `L2` function supported on a measure-zero point is zero.
Hence

\[
\boxed{V(\cdot,0)=0.}
\]

By uniqueness of the linear equation,

\[
\boxed{V\equiv0.}
\]

---

## 7. Contradiction with the normalized ribbon point

M17-155 gives

\[
|V(0,0)|=1.
\]

The Liouville conclusion gives

\[
V(0,0)=0.
\]

Therefore

\[
\boxed{
R_{2,\rm ribbon}^{relative-thick,quiet,bounded-\kappa,critical-envelope}
\Longrightarrow\bot.
}
\]

This closes that subbranch.

---

## 8. Exact surviving exits

A low-amplitude strong-director ribbon can avoid the present contradiction only through at least one of

\[
\boxed{
\begin{aligned}
&G_{mass}: &&\text{critical packet-mass envelope fails},\\
&H_{1,crit}^{spacetime}:&&\text{quiet shell corridor fails},\\
&G_{\kappa,\infty}:&&\text{bounded CE-H potential control fails},\\
&G_{thin/nodal/multiplicity}:&&\text{relative-thick packet compactness fails},\\
&G_{boundary}:&&\text{the required material packet/shell cover exits}.
\end{aligned}
}
\]

The infinite normalized-jet ladder is no longer the preferred next route on the relative-thick branch.

---

## 9. DSD audit

1. The critical mass envelope is **not** derived here from `J_R=O(1)`; it is a separate genealogy condition.
2. No spectral theorem is imported: the Liouville step follows from the exact Fourier propagator.
3. The limit is nonzero because normalization is taken at a relative-thick ribbon point.
4. `T_j -> infinity` is required. A merely fixed finite time window is insufficient.
5. Failure of the envelope is not called a contradiction; it becomes the next explicit turnover/mass-transfer branch.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
