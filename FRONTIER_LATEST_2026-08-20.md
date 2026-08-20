# Latest Global Endgame Frontier — 2026-08-20

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This frontier collects the latest reductions after the aggregate halo audit, Type-I compactness bridge, fixed-center pressure reduction, continuous backward vorticity bound, and the H1 covariance near-saturation rigidity calculation.

---

## 1. Robust global/local separation

The direct strain produced at the tracked core by all vorticity outside normalized radius `R_0` satisfies

\[
\boxed{
|S_{\ge R_0}|_F^2
\lesssim
R_0^{-1}P_{\Omega,\ge R_0}.
}
\]

Thus an aggregate order-one remote strain from radii tending to infinity forces normalized palinstrophy to diverge. On the non-`H` branch the entire remote halo becomes dynamically passive, even if many weak shells add coherently.

The endpoint-critical global non-tightness remains mandatory, but it is separated from bounded-radius active production.

---

## 2. Local active tree

The A/C/M, max-mid, determinant-defect, middle-axis locking, and projection-kernel calculations reduce bounded-radius active production to

\[
\boxed{
H\lor T_{bounded}\lor P_V^*.
}
\]

Here `P_V` is the genuinely full-Navier--Stokes projective strain/vorticity/advection action. Fixed-gap positive-middle-strain production routes to derivative/interface turnover; near-max-mid projection invisibility routes to higher derivatives or projective visibility.

---

## 3. If H/T do not recur, the P_V tower is Type-I sized

The normalized `P_V` shape speed is universally bounded under the first-hitting cap, so a fixed projective action per geometric stage gives a lower stage-length bound. The local variance/Poincare gate gives an upper bound on the recurrent non-`H/T` branch:

\[
0<L_-\le L_j\le L_+<\infty.
\]

Therefore

\[
\boxed{
W_j(T^*-t_j)\asymp1
}
\]

and, in fact,

\[
\boxed{
\sup_{t_0<t<T^*}(T^*-t)\|\omega(t)\|_\infty<\infty.
}
\]

Thus the non-`H/T` survivor is a Type-I vorticity branch.

---

## 4. Fixed-center Type-I tower

Non-turnover center nesting gives a limiting point `X_*` with

\[
|X_j-X_*|\lesssim r_j,
\qquad r_j=W_j^{-1/2}.
\]

Compactness is therefore performed in an ordinary fixed-center Navier--Stokes rescaling about `X_*`, avoiding the artificial affine pressure produced by the accelerating ledger frame.

Earlier first-hitting stages appear at radii

\[
R_m=q^{m/2}
\]

with exact Type-I amplitudes

\[
|U|\sim R_m^{-1},
\qquad
|\Omega|,|S|,|P|\sim R_m^{-2}.
\]

Natural-core contributions to the CKN quantities `A,C,D,E` therefore have the correct scale, and the geometric stage sums preserve those bounds unless super-Type-I influx, multicore accumulation, or derivative mass enters; these are `T/H` events.

---

## 5. Pressure is not an independent compactness obstruction

In the fixed-center frame the pressure is the canonical whole-space pressure. The near part is controlled by cubic velocity via Calderon--Zygmund, while a remote annulus at radius `R` contributes only its pressure oscillation. Subtracting the shell constant gains one derivative of the kernel and yields a summable `R^{-3}` Type-I tail under the parent-ball energy bound.

Hence centered Type-I velocity control gives

\[
\boxed{
D(R)\lesssim C(cR)+A_*^{3/2}.
}
\]

Thus the principal compactness burden is `A,E`; `C` follows by local interpolation and `D` follows from `A,C`. Full control over all off-center subcylinders still requires a quantitative `secondary bad cylinder -> H/T` lemma.

---

## 6. Restricted ancient limit

Any ancient limit extracted from the non-`H/T` tower is nontrivial and inherits

\[
|\Omega(y_*,0)|=1,
\]

and the continuous backward Type-I vorticity bound

\[
\boxed{
\sup_{\tau\le-\tau_0}
|\tau|\,\|\Omega(\tau)\|_\infty<\infty.
}
\]

In logarithmic Leray variables the rescaled vorticity is uniformly bounded backward in logarithmic time. The candidate is therefore much narrower than a generic bounded ancient solution, but no general Liouville theorem for this precise class is established here.

---

## 7. The ancient survivor must retain a global L3-critical tail

The Albritton--Barker ancient Liouville theorem says that a mild ancient solution that is globally `L^3` bounded along any sequence of times tending to minus infinity is trivial. Since the first-hitting ancient candidate is nontrivial, its global `L^3` norm cannot possess a bounded backward subsequence.

A uniformly controlled natural Type-I core contributes only `O(1)` critical `L^3` mass. Hence any nontrivial restricted ancient survivor must carry a backward-growing global `L^3` tail outside the active core.

Thus the non-`H/T` ancient picture is necessarily

\[
\boxed{
\text{active tight Type-I core}
+\text{global L3-critical dynamically passive tail}.
}
\]

The tail is compatible with finite physical energy because a geometric stack of critical shells has energy dominated by its largest physical shell, while its scale-invariant `L^3` contributions can accumulate logarithmically.

---

## 8. Exact H1 covariance geometry of P_V

Let

\[
R_{VI}=P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right).
\]

Using the exact identity

\[
\langle-\Delta S,\omega\otimes\omega\rangle=0,
\]

the H1 nonlinear contraction is

\[
\boxed{
\langle R_{VI},-\Delta S\rangle
=\int S:(M_{sp}+2M_{rg}),
}
\]

where

\[
(M_{sp})_{k\ell}=\langle\partial_kS,\partial_\ell S\rangle_F,
\qquad
M_{rg}=\sum_k(\partial_kS)^2.
\]

After normalization the combined covariance

\[
\overline C=(C_{sp}+2C_{rg})/3
\]

is positive semidefinite, trace one, and satisfies the universal cap

\[
\boxed{
\lambda_{max}(C_{rg})\le\frac23,
\qquad
\lambda_{max}(\overline C)\le\frac79.
}
\]

---

## 9. Near-saturation rigidity and transverse uncertainty gap

If a compressive axis `n` nearly saturates the `7/9` combined covariance cap, with

\[
\varepsilon_n=\frac79-n^T\overline Cn,
\]

then

\[
\sum_{v\perp n}|\partial_vS|^2
\le3\varepsilon_n|\nabla S|^2,
\]

and

\[
\sum_k\operatorname{dist}_F(\partial_kS,\mathcal L_n)^2
\le9\varepsilon_n|\nabla S|^2,
\]

where `L_n` is the one-dimensional axisymmetric trace-free derivative line. Exact saturation forces a fixed-axis one-dimensional strain profile and is incompatible with nonzero finite whole-space `L^2` energy.

Moreover, for a fixed coherent axis the transverse uncertainty inequality gives

\[
\boxed{
\overline\varepsilon_n
\ge
\frac{\|S\|_2^2}
{3R_{\perp,S}^2\|\nabla S\|_2^2}.
}
\]

Hence a transversely tight, derivative-controlled coherent-axis core has a positive gap below exact covariance saturation. Approaching the cap forces `T`, `H`, or axis/projective reorganization.

---

## 10. Current two-level endgame

The hypothetical finite-time singularity must now fall into one of two broad systems:

### System I — repeated H/T

Derivative escape or bounded-radius material/multicore turnover occurs infinitely often. This branch still needs a global nonrepeatability/packing theorem; energy alone is too weak because natural-scale dissipation carries the summable factor `W^{-1/2}`.

### System II — restricted Type-I P_V ancient system

If H/T do not recur, a nested Type-I first-hitting tower produces a restricted ancient candidate with:

- continuous backward Type-I vorticity control;
- a tight active core;
- a necessary global `L^3`-critical passive tail;
- full-NS `P_V` projective recurrence;
- a positive gap away from maximally efficient compressive H1 covariance unless H/T/projective reorganization is activated.

---

## 11. Principal next targets

1. **Secondary-cylinder lemma:** prove quantitatively that failure of the full local Type-I `A/E` bounds on off-center subcylinders produces a genuine secondary core / influx (`T`) or derivative concentration (`H`). This would complete the ancient compactness bridge rather than only the centered tower.

2. **Non-saturated H1 efficiency theorem:** use the positive covariance saturation gap to derive a strict loss in `P_V` palinstrophy replenishment and show that the missing action must enter a tangential projective/higher-derivative channel.

3. **Core-tail coexistence theorem:** show that the globally necessary but dynamically passive `L^3` tail cannot coexist indefinitely with the recurrent active core without `T/H`, or else classify the resulting logarithmic shell tower.

Status: **REMOTE ACTIVITY IS ROBUSTLY PASSIVE ON NON-H; THE NON-H/T LOCAL SURVIVOR IS TYPE-I; PRESSURE GAUGE IS REDUCED; P_V H1 REPLENISHMENT HAS A 7/9 COVARIANCE CAP WITH A QUANTITATIVE TIGHTNESS/DERIVATIVE GAP; ANY NONTRIVIAL ANCIENT SURVIVOR MUST ALSO CARRY A GLOBAL BACKWARD-DIVERGENT L3-CRITICAL PASSIVE TAIL. GLOBAL REGULARITY REMAINS UNPROVED.**