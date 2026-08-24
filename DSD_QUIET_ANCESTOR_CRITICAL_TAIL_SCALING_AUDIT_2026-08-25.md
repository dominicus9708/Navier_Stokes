# DSD Quiet-Ancestor Critical-Tail Scaling Audit

Date: 2026-08-25

Status: **QUIET MATERIAL ANCESTOR CONTRIBUTION SCALES EXACTLY LIKE THE CRITICAL 1/R VORTICITY-ENSTROPHY TAIL / ONE-ANCESTOR PERSISTENCE DOES NOT BY ITSELF CLOSE THE CUBIC RETURN-DENSITY LEDGER / MULTIPLICITY OR A NON-ENERGY RIGIDITY INPUT IS REQUIRED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The new ancestor-clock upgrade proves that an age-`k` observation occurs after a genuine order-one ancestor parabolic time.

It is tempting to infer that a quietly surviving material ancestor must therefore pay enough physical return density to close the critical cubic-tail ledger.

This note audits that inference.

The answer is **no for a single quietly transported ancestor packet**. Its exact amplitude-volume scaling is itself critical and reproduces the `1/R` tail law.

This is not a counterexample to Navier-Stokes regularity. It is a scaling audit showing which closure mechanism is too weak.

---

## 2. Ancestor packet and first-hitting scales

Let

\[
n=j-k,
\qquad
W_n=q^nW_0,
\qquad
r_n=\left(\frac\nu{W_n}\right)^{1/2}.
\]

The current scale is

\[
r_j=q^{-k/2}r_n.
\]

Define the age factor

\[
K_k:=\frac{r_n}{r_j}=q^{k/2}.
\]

The exact ancestor-radius identity is

\[
R_{j,k}^{\rm phys}=r_n,
\]

while the current normalized shell radius is `K_k`.

---

## 3. Quiet local material transport gives two-sided amplitude control

Use the localized amplitude-location genealogy theorem.

At stage `n`, the analytic first-hitting occupied packet has initial volume

\[
|A_n^0|=c_A r_n^3,
\]

with fixed `c_A>0`.

Incompressibility gives exact volume preservation:

\[
\boxed{|A_n(t)|=c_A r_n^3.}
\]

Suppose over `[t_n,t_j]` the local packet strain/diffusion and tube-deformation exposures remain under fixed quiet thresholds.

The existing two-sided amplitude-retention estimate then gives fixed constants

\[
0<q_L\le Q_L<\infty
\]

such that on the transported packet, or at least on the retained fixed-volume/fixed-fraction occupied part used below,

\[
q_LW_n
\lesssim
|\omega(x,t_j)|
\lesssim
Q_LW_n.
\]

For the upper estimate it is enough to use the whole volume-preserved packet. For the lower estimate one may use the retained ball furnished by the local tube-deformation theorem.

---

## 4. Physical enstrophy of one quiet ancestor is of order nu^2/r_n

The volume and amplitude upper bounds give

\[
\int_{A_n(t_j)}|\omega|^2dx
\le
c_AQ_L^2W_n^2r_n^3.
\]

Since

\[
W_n=\frac\nu{r_n^2},
\]

we get

\[
\boxed{
\int_{A_n(t_j)}|\omega|^2dx
\le
C_Q\frac{\nu^2}{r_n},
}
\]

with `C_Q=c_AQ_L^2`.

Under the retained occupied-ball lower bound, the same scaling holds from below:

\[
\boxed{
\int_{A_n^{ret}(t_j)}|\omega|^2dx
\ge
c_q\frac{\nu^2}{r_n}
}
\]

for a fixed `c_q>0`.

Thus a quiet coherent ancestor naturally carries physical enstrophy of scale

\[
\boxed{E_{\omega,n}^{packet}\asymp\nu^2/r_n.}
\]

---

## 5. Current parent-normalized enstrophy decays geometrically with age

At stage `j`, parent-normalized enstrophy is

\[
\widetilde m_{j,n}
:=
\frac{r_j}{\nu^2}
\int_{A_n(t_j)}|\omega|^2dx.
\]

Therefore

\[
\boxed{
\widetilde m_{j,n}
\lesssim
\frac{r_j}{r_n}
=q^{-k/2}
=K_k^{-1}.
}
\]

On a retained fixed-fraction occupied descendant,

\[
\boxed{
\widetilde m_{j,n}^{ret}
\gtrsim
K_k^{-1}.
}
\]

Hence a quiet ancestor packet contributes, at its matching age,

\[
\boxed{
\widetilde m_{j,k}^{anc}
\asymp
K_k^{-1}.
}
\]

This is the exact normalized vorticity-enstrophy law of a critical remote tail.

---

## 6. Radius times mass is order one

The matching normalized radius is

\[
K_k=q^{k/2}.
\]

Therefore

\[
\boxed{
K_k\widetilde m_{j,k}^{anc}
\asymp1.
}
\]

Thus the scale-critical shell quantity is neither decaying nor growing for one quiet ancestor.

In particular, the material genealogy scaling exactly reproduces the borderline shell law

\[
\boxed{m(R)\asymp R^{-1}.}
\]

This is the same critical law already associated with a velocity tail

\[
|U(R)|\sim R^{-1},
\qquad
|\Omega(R)|\sim R^{-2}.
\]

So the critical tail is not mysterious from the genealogy viewpoint: one quiet ancestor per generation naturally has exactly the right amplitude-volume scaling to populate it.

---

## 7. One quiet ancestor per generation yields a tight L2 vorticity tail

If at most `M_0=O(1)` quiet coherent ancestor packets contribute at each age, then for ages `k>=K`,

\[
\sum_{k\ge K}\widetilde m_{j,k}^{anc}
\lesssim
M_0\sum_{k\ge K}q^{-k/2}.
\]

Therefore

\[
\boxed{
\sum_{k\ge K}\widetilde m_{j,k}^{anc}
\lesssim
q^{-K/2}
\asymp
K_K^{-1}.
}
\]

Hence the vorticity `L2` tail is uniformly tight even though the associated scale-critical shell charge remains order one on each generation.

This explains why a passive critical velocity tail can coexist with strain/vorticity Sobolev precompactness: its derivative/enstrophy tail tends to zero, while its critical velocity `L3` shell ledger can remain borderline.

---

## 8. Exact total future-time ceiling for one ancestor

The first-hitting/Leray clock gives

\[
T^*-t_n
=
\frac{\Theta_n}{W_n}
=
\Theta_n\frac{r_n^2}{\nu},
\]

with

\[
0<\Theta_n\le\Theta_+.
\]

Thus every collection of physical residence intervals belonging to one material ancestor after `t_n` satisfies

\[
\boxed{
\sum_\ell\tau_{n,\ell}
\le
\Theta_+\frac{r_n^2}{\nu}.
}
\]

If these returns are all measured at the ancestor physical scale

\[
\rho_n\asymp r_n,
\]

then their total weighted return density has the ceiling

\[
\boxed{
\mathfrak R_n^{one\ ancestor}
:=
\frac1{\rho_n}
\sum_\ell\tau_{n,\ell}
\lesssim
\Theta_+\frac{r_n}{\nu}.
}
\]

Therefore one late ancestor has only a vanishing amount of physical weighted return time as

\[
r_n\to0.
\]

This ceiling is independent of how its total future lifetime is split into many short intervals.

---

## 9. Consequence for the old return-density contradiction target

The existing cubic-tail closure target asks for a lower bound schematically of the form

\[
\mathfrak R_k
\gtrsim
J_k^{1/2}
\]

on a cubic-divergent subset.

The present audit shows that such a bound cannot be justified merely by saying

> an ancestor packet survives for one natural parabolic epoch.

A single quiet ancestor has only the total future weighted-time scale

\[
O(r_n/\nu),
\]

while its current normalized critical radius-times-mass charge is order one.

Therefore a successful return-density closure must gain something genuinely beyond single-packet persistence, for example:

1. **large material multiplicity / repeated rebuilding** at the same historical scale;
2. a stronger amplitude growth mechanism that exceeds the quiet ancestor scaling;
3. a turnover/replacement cost attached to creating those additional packets;
4. or a non-energy rigidity theorem excluding the passive critical-tail/recurrent-core configuration.

**Status: PROVED SCALING AUDIT.**

---

## 10. Multiplicity threshold interpretation

Suppose `M_n` essentially distinct comparable packets/returns at physical scale `r_n` contribute without excessive time overlap.

The parabolic future-time ceiling per packet is `O(r_n^2/nu)`, so schematically

\[
\mathfrak R_n
\lesssim
M_n\frac{r_n}{\nu}
\]

before overlap corrections.

Thus obtaining an order-one weighted return density from late scales would require multiplicity of order at least

\[
\boxed{
M_n
\gtrsim
\frac{\nu}{r_n}
}
\]

in the viscosity-restored scaling, up to the normalization conventions of the return ledger.

Such rapidly growing multiplicity is not a passive single-tail mechanism; it belongs naturally to source replacement / multicore turnover / packing analysis.

This estimate is schematic at the level of packet-count normalization and is **not** promoted to a theorem about the repository's `T` branch without a separate overlap/packet-distinctness lemma.

---

## 11. DSD audit

The finite formed objects are

- one ancestor stage `n`;
- one material packet `A_n`;
- local strain/diffusion/tube exposure bounds;
- exact preserved volume;
- descendant amplitude bounds;
- finite age `k`;
- current normalized packet mass;
- finite future residence intervals.

The infinite tail is obtained only after proving the finite-age estimate and summing the ordinary geometric series.

No material packet is silently identified with an Eulerian shell unless explicit contact is assumed.

---

## 12. Updated frontier

The genealogy tree now separates cleanly into two fundamentally different mechanisms.

### Multiplicity / rebuilding lane

If the recurrent critical tail is continually rebuilt by many distinct packets at the same historical scale, the required multiplicity must be charged to turnover, packing, relative transport, or derivative action.

### Passive critical-ancestor lane

If only `O(1)` quiet ancestors per generation survive, then

\[
\boxed{
\widetilde m_k\asymp K_k^{-1},
\qquad
K_k\widetilde m_k\asymp1,
}
\]

and the vorticity tail is `L2`-tight while the velocity tail remains critical.

Ordinary physical-energy / one-packet return-density summation does not eliminate this lane.

It must instead be attacked through the remaining Leray recurrent-motion / compact-class rigidity problem, or by proving that Navier-Stokes dynamics cannot sustain the required passive genealogy while the core continues first-hitting amplification.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
