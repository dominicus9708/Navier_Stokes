# DSD M17-235 — Critical kappa gradient returns to weighted multiplier diffusion or a dimensionless gradient spike, but the amplitude firewall remains

Date: 2026-09-06  
Canonical ID: **M17-235**

Status: **UNWEIGHTED-TO-WEIGHTED COEFFICIENT RETURN / M17-234 FORCES THE AMPLITUDE-INDEPENDENT SCALE-CRITICAL LOWER BOUND `ell ||grad kappa||_(L^(3/2)) >= c`. THE ONLY WAY THIS CHARGE COULD FAIL TO ENTER THE EXISTING M5-687 / M17-145 `rho^2|grad kappa|^2` DIFFUSION CHANNEL IS TO CONCENTRATE ALMOST ENTIRELY INSIDE THE SMALL VORTICITY-CANCELLATION SET WHERE `W` IS NOT COMPARABLE TO ITS LOCAL MEAN. FIX A DIMENSIONLESS GRADIENT CEILING `ell^3||grad kappa||_infty<=G0`. THE CANCELLATION SET HAS ONLY `O(theta)` OF THE BUFFER VOLUME, SO FOR `theta<<G0^-3/2` IT CANNOT CARRY THE M17-234 CRITICAL `L^(3/2)` GRADIENT NORM. A FIXED PORTION OF THE GRADIENT THEREFORE LIES ON THE GOOD SET `|W|>=|c|/2`; HÖLDER THEN UPGRADES IT TO `int |grad kappa|^2 >= c ell^-3`, AND MEAN DOMINATION GIVES `int rho^2|grad kappa|^2 >= c M ell^-6`. IF THE GRADIENT CEILING FAILS, `ell^3||grad kappa||_infty>G0` IS AN EXPLICIT COEFFICIENT-DERIVATIVE SPIKE. THIS CONNECTS THE NEW SRG COEFFICIENT BRANCH TO THE EXISTING MULTIPLIER-DIFFUSION LEDGER, BUT THE LOWER BOUND IS STILL PROPORTIONAL TO THE VANISHING PACKET MASS `M`; THEREFORE THE LOW-AMPLITUDE FIREWALL IDENTIFIED IN M17-145 IS NOT REMOVED AND GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Root mean-dominated packet

Retain the M17-233--234 notation on a buffer

\[
B=B_{A\ell}(q).
\]

Write

\[
W=c+w,
\qquad
V:=\int_B|w|^2dy<\theta M,
\qquad
M:=\int_B|W|^2dy.
\]

Then

\[
|B||c|^2=M-V>(1-\theta)M.
\]

Define the cancellation set

\[
E:=\{|w|>|c|/2\}\cap B
\]

and the good set

\[
G:=B\setminus E.
\]

M17-233 gives

\[
|E|\le C\theta|B|.
\]

M17-234 gives

\[
\boxed{
\ell\|\nabla\kappa\|_{L^{3/2}(B)}
\ge d_1>0.
}
\]

---

## 2. Dimensionless gradient-spike alternative

Fix

\[
G_0>1.
\]

If

\[
\boxed{
\ell^3\|\nabla\kappa\|_{L^\infty(B)}>G_0,
}
\]

retain the explicit higher coefficient-spike branch

\[
\boxed{G_{\nabla\kappa\text{-}spike}^{intrinsic}.}
\]

This quantity is dimensionless because

\[
\nabla\kappa\sim \text{length}^{-3}.
\]

For the remaining branch assume

\[
\boxed{
\|\nabla\kappa\|_{L^\infty(B)}
\le G_0\ell^{-3}.
}
\]

---

## 3. The cancellation set cannot carry all critical gradient mass

The `L^(3/2)` integral on `E` obeys

\[
\int_E|\nabla\kappa|^{3/2}dy
\le
G_0^{3/2}\ell^{-9/2}|E|.
\]

Since

\[
|E|\le C\theta|B|
\le C_A\theta\ell^3,
\]

we get

\[
\boxed{
\int_E|\nabla\kappa|^{3/2}dy
\le
C_AG_0^{3/2}\theta\ell^{-3/2}.
}
\]

Equivalently,

\[
\boxed{
\ell\|\nabla\kappa\|_{L^{3/2}(E)}
\le C_AG_0\theta^{2/3}.
}
\]

Choose `theta` smaller if necessary so that

\[
C_AG_0\theta^{2/3}
\le\frac12d_1.
\]

Then M17-234 implies

\[
\boxed{
\ell\|\nabla\kappa\|_{L^{3/2}(G)}
\ge\frac12d_1.
}
\]

Thus a fixed fraction of the coefficient-gradient charge lies where the original vorticity is comparable to its local mean.

---

## 4. Upgrade the good-set gradient to L2

On a finite-measure set,

\[
\|f\|_{L^{3/2}(G)}
\le |G|^{1/6}\|f\|_{L^2(G)}.
\]

Hence

\[
\|\nabla\kappa\|_{L^2(G)}^2
\ge
|G|^{-1/3}
\|\nabla\kappa\|_{L^{3/2}(G)}^2.
\]

Since

\[
|G|\le|B|\asymp_A\ell^3
\]

and Section 3 gives

\[
\|\nabla\kappa\|_{L^{3/2}(G)}
\ge c\ell^{-1},
\]

we obtain

\[
\boxed{
\int_G|\nabla\kappa|^2dy
\ge c_{A,G_0}\ell^{-3}.
}
\]

---

## 5. Restore the vorticity weight on the good set

On `G`,

\[
|w|\le|c|/2,
\]

so

\[
\boxed{|W|\ge|c|/2.}
\]

Therefore

\[
\begin{aligned}
\int_B\rho^2|\nabla\kappa|^2dy
&\ge
\frac{|c|^2}{4}
\int_G|\nabla\kappa|^2dy\\
&\ge
c\frac{M}{|B|}\ell^{-3}.
\end{aligned}
\]

Because

\[
|B|\asymp_A\ell^3,
\]

we obtain the normalized weighted-diffusion lower bound

\[
\boxed{
\int_B\rho^2|\nabla\kappa|^2dy
\ge
c_{A,G_0}\,M\ell^{-6}.
}
\]

Equivalently,

\[
\boxed{
\frac{\ell^6}{M}
\int_B\rho^2|\nabla\kappa|^2dy
\ge c_{A,G_0}>0.
}
\]

This is the local intrinsic form of the multiplier-gradient diffusion channel used globally in M5-687 and dynamically in M17-145.

---

## 6. Relation to the original spectral charge

At the root packet,

\[
H=M\ell^{-4}.
\]

Therefore Section 5 may also be written

\[
\boxed{
\int_B\rho^2|\nabla\kappa|^2dy
\ge cH\ell^{-2}.
}
\]

Thus once the coefficient gradient becomes critical without a pointwise gradient spike, its weighted diffusion is two intrinsic derivative powers stronger than the original `H2/L2` spectral charge.

This is a genuine structural escalation.

It is not yet a contradiction because no finite global budget for this multiplier-diffusion quantity has been established on the low-amplitude remote branch.

---

## 7. Updated coefficient frontier

Combining M17-233--235 gives

\[
\boxed{
G_{intrinsic\ H2/L2\ spectral}
\Longrightarrow
H_{intrinsic\ palinstrophy}
\lor
G_{\kappa\text{-}spike}^{intrinsic}
\lor
G_{\nabla\kappa\text{-}spike}^{intrinsic}
\lor
H_{weighted\ multiplier\ diffusion}
\lor
G_{nodal/interface}.
}
\]

The finite relative-amplitude scale ladder is therefore removed as an independent canonical root exit.

The remaining coefficient branch has been returned to an already existing PDE charge, modulo explicit dimensionless coefficient spikes.

---

## 8. Why this still does not close the branch

The lower bound

\[
D_\kappa(B)
:=\int_B\rho^2|\nabla\kappa|^2dy
\ge cM\ell^{-6}
\]

still contains the packet amplitude through `M`.

On a remote low-amplitude sequence, `M` may shrink rapidly enough that no nonsummable global lower bound follows merely from this estimate.

This is the same amplitude firewall already identified in M17-145: the natural multiplier-gradient PDE energy is weighted by `rho^2` and can become cheap per unit amplitude-free geometry.

Therefore M17-235 connects ledgers but does not remove the firewall.

---

## 9. Next proof obligation

The next useful question is no longer scale return.

It is an **Amplitude-Return Gate (ARG)**:

\[
\boxed{
\text{normalized multiplier-diffusion charge}
\Longrightarrow
\text{depth/radius-independent lower-order physical cost}
\lor
G_{low\ amplitude/nodal/replenishment}.
}
\]

Candidate inputs include

1. the M17-200 finite amplitude-descent atlas for multiplier-gradient threshold charges;
2. the M5-687 division-free polynomial gap;
3. material amplitude law
   \[
   D_B\rho=(\sigma+\kappa-1)\rho;
   \]
4. fixed-lag shell genealogy and M17-207 temperedness.

No ARG is derived here.

---

## 10. DSD audit

- Small transition/cancellation volume is not confused with small derivative charge; the `L-infinity` gradient alternative is explicit.
- The gradient charge is transferred to the good amplitude region before inserting the `rho^2` weight.
- The resulting weighted diffusion is an existing physical/CE-H descriptor, not a newly invented payer.
- The amplitude factor `M` is retained and is not cancelled by normalization when discussing global budgets.
- M17-145's low-amplitude summability firewall therefore remains active.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
