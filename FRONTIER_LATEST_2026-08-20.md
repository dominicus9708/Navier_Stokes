# Latest Global Endgame Frontier — 2026-08-20

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This frontier incorporates the latest reductions after the aggregate-halo audit, Type-I compactness bridge, fixed-center pressure reduction, first-hitting ancient vorticity cap, and sharp `P_V` H1 production analysis.

---

## 1. Robust global/local separation

For all vorticity outside normalized radius `R_0`, the direct strain at the tracked core satisfies

\[
\boxed{
|S_{\ge R_0}|_F^2
\lesssim
R_0^{-1}P_{\Omega,\ge R_0}.
}
\]

Hence an aggregate order-one remote strain from radii tending to infinity forces normalized palinstrophy to diverge. On the non-`H` branch the entire remote halo is dynamically passive, even if many weak shells add coherently.

The endpoint-critical global non-tightness remains mandatory, but it is separated from bounded-radius active production.

---

## 2. Local active tree

The A/C/M trichotomy, max-mid rigidity, determinant defect, middle-axis locking, and projection-kernel reductions give

\[
\boxed{
H\lor T_{bounded}\lor P_V^*.
}
\]

The only non-`H/T` local survivor is the genuinely full-Navier--Stokes projective strain/vorticity/advection branch `P_V`.

---

## 3. Non-H/T recurrence is Type-I sized

On the recurrent `P_V` branch the projective shape speed is uniformly bounded and each first-hitting stage requires fixed action. Together with the local variance/Poincare upper gate,

\[
0<L_-\le L_j\le L_+<\infty.
\]

Therefore

\[
\boxed{W_j(T^*-t_j)\asymp1}
\]

and continuously at late times

\[
\boxed{
\sup_{t_0<t<T^*}(T^*-t)\|\omega(t)\|_\infty<\infty.
}
\]

Thus the non-`H/T` survivor is a Type-I vorticity branch.

---

## 4. Fixed-center Type-I tower

Non-turnover center nesting gives a limiting singular point `X_*` with

\[
|X_j-X_*|\lesssim r_j,
\qquad r_j=W_j^{-1/2}.
\]

Compactness is therefore performed in a fixed-center Navier--Stokes rescaling about `X_*`, avoiding the artificial affine pressure produced by the accelerating ledger frame.

Earlier stages appear at radii

\[
R_m=q^{m/2}
\]

with exact Type-I amplitudes

\[
|U|\sim R_m^{-1},
\qquad
|\Omega|,|S|,|P|\sim R_m^{-2}.
\]

Natural-core contributions to the local Type-I quantities `A,C,D,E` have the correct geometric scaling. Super-Type-I parent-ball influx, multicore accumulation, or derivative mass is classified as `T/H`.

---

## 5. Pressure is not an independent centered obstruction

In the fixed-center frame the pressure is the canonical whole-space pressure. Near pressure is controlled by cubic velocity; subtracting the constant part of a remote pressure shell gains one power of spatial decay. Under Type-I parent-ball energy control,

\[
\boxed{
D(R)\lesssim C(cR)+A_*^{3/2}.
}
\]

Thus the centered compactness burden reduces primarily to `A,E`; `C` follows by local interpolation and `D` follows from `A,C`. A full ancient compactness theorem still needs the secondary-bad-cylinder implication `bad off-center cylinder -> H/T`.

---

## 6. Exact first-hitting ancient vorticity cap

At the first hitting time `t_j`,

\[
W(t)\le W_j\qquad(t\le t_j).
\]

Therefore the fixed-center rescaled vorticity satisfies exactly

\[
\boxed{
\|\Omega_j(\tau)\|_\infty\le1
\qquad(\tau\le0).
}
\]

Any sufficiently strong ancient limit inherits

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty\le1
\qquad(\tau\le0),
}
\]

while terminal nontriviality gives

\[
|\Omega_\infty(y_*,0)|=1.
\]

Combining with the Type-I stage-length control yields

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty
\le
\min\left\{1,\frac{C}{|\tau|}\right\},
\qquad \tau<0.
}
\]

Hence the ancient survivor has vorticity amplitude tending to zero backward in time.

---

## 7. Global L3-critical tail remains necessary

A nontrivial mild ancient candidate cannot possess a globally bounded `L^3` velocity norm along a backward sequence. Since the controlled Type-I core contributes only `O(1)` critical mass, the restricted survivor must carry a backward-growing global `L^3` tail.

Thus the non-`H/T` picture is

\[
\boxed{
\text{tight active Type-I core}
+
\text{global low-vorticity L3-critical passive tail}.
}
\]

The tail must become low-vorticity backward because `||Omega(tau)||_infty -> 0`, yet it cannot have a bounded global `L^3` subsequence. The aggregate halo barrier prevents this tail from supplying order-one core strain on the non-`H` branch.

---

## 8. Exact P_V H1 residual geometry

Define

\[
\mathcal R_{VI}
=P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right).
\]

The exact identity

\[
\langle-\Delta S,\omega\otimes\omega\rangle=0
\]

gives

\[
\boxed{
\frac12\frac d{dt}\|\nabla S\|_2^2
+\nu\|\Delta S\|_2^2
=-\langle\mathcal R_{VI},-\Delta S\rangle.
}
\]

With `G_k=partial_k S`,

\[
(M_{sp})_{k\ell}=\langle G_k,G_\ell\rangle_F,
\qquad
M_{rg}=\sum_kG_k^2,
\]

one has

\[
\boxed{
\langle\mathcal R_{VI},-\Delta S\rangle
=\int S:(M_{sp}+2M_{rg}).
}
\]

---

## 9. 7/9 covariance cap and exact covariance taxes

After normalizing the two positive gradient covariances,

\[
\overline C=(C_{sp}+2C_{rg})/3,
\]

\[
\lambda_{max}(C_{rg})\le\frac23,
\qquad
\lambda_{max}(\overline C)\le\frac79.
\]

In the strain eigenframe `s_1 <= s_2 <= s_3`, let

\[
c_i=e_i^T\overline C e_i.
\]

Then the exact H1 density decomposition is

\[
\boxed{
-3S:\overline C
=
\frac13(5s_2+7s_3)
-3\left(\frac79-c_1\right)(s_2-s_1)
-3c_3(s_3-s_2).
}
\]

Thus the theoretical covariance cap loses H1 efficiency through two explicit positive taxes: compressive-axis underfill and strongest-extensional-axis leakage.

Near `7/9` saturation also forces transverse one-dimensionality and axisymmetric derivative geometry. The transverse uncertainty inequality gives a positive saturation defect for a tight derivative-controlled coherent-axis core.

---

## 10. Sharp trace-free range bound

For every symmetric trace-free `3x3` matrix `G`,

\[
\boxed{
|(G^2)^\circ|_F=\frac1{\sqrt6}|G|_F^2.
}
\]

Hence for trace-free symmetric `S`,

\[
\boxed{
|\operatorname{tr}(SG^2)|
\le\frac1{\sqrt6}|S||G|^2.
}
\]

Applied to the exact H1 residual,

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
\int
\left(-s_1+\frac2{\sqrt6}|S|\right)|\nabla S|^2dx
\le
\frac4{\sqrt6}\int|S||\nabla S|^2dx.
}
\]

For

\[
(s_1,s_2,s_3)=(-2m,m-d,m+d),
\]

any fixed ratio `d/m >= eta > 0` incurs the universal fractional efficiency loss

\[
\boxed{
\Theta_{gap}
\le
\frac12+
\frac1{2\sqrt{1+\eta^2/3}}
<1.
}
\]

Thus only the near-max-mid derivative-active geometry can approach the sharp algebraic H1 production constant.

---

## 11. Exact full H1 saturation is impossible at finite energy

Equality in the sharp scalar H1 bound requires simultaneously:

1. exact max-mid strain `s_2=s_3`;
2. spatial derivatives only in the compressive direction;
3. every active derivative matrix on the same axisymmetric trace-free range line.

These conditions force

\[
S(x)=m(n\cdot x)(I-3n\otimes n)
\]

with fixed `n`. A nonzero such field is constant on infinite transverse planes and cannot belong to `L^2(R^3)`.

Therefore

\[
\boxed{
S\in L^2(R^3),\quad
\text{exact maximal P_V H1 production}
\Longrightarrow S\equiv0.
}
\]

---

## 12. Strict efficiency gap on a precompact non-H/T class

For a genuinely precompact normalized profile class `K`, define

\[
\mathfrak E_{H1}(S)
=
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}
{(4/\sqrt6)\int|S||\nabla S|^2}.
\]

Exact saturation nonattainment and compactness imply

\[
\boxed{
\sup_{S\in K}\mathfrak E_{H1}(S)
\le1-\delta_K
}
\]

for some class-dependent `delta_K>0`.

The exact H1 ledger also gives the stronger blowup necessary condition

\[
\boxed{
\limsup_{t\uparrow T^*}
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}
{\|\Delta S\|_2^2}
\ge\nu.
}
\]

Thus the remaining local question is no longer whether full algebraic saturation is possible; it is whether a strictly submaximal compact profile can still cross the viscosity threshold.

---

## 13. Current local variational target

On an admissible precompact non-`H/T` class `K`, define

\[
\boxed{
\Lambda_K
=
\sup_{S\in K}
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}
{\|\Delta S\|_2^2}.
}
\]

The decisive local question is

\[
\boxed{\Lambda_K<\nu\ ?}
\]

If yes for every admissible first-hitting compact class, the recurrent `P_V` ancient core is eliminated directly by the H1 ledger. If `Lambda_K >= nu`, compactness produces a maximizing profile that should satisfy a far more rigid variational/elliptic system than an arbitrary Navier--Stokes trajectory.

---

## 14. Current two-system global endgame

A hypothetical finite-time singularity must lie in one of two systems.

### System I — repeated H/T

Derivative escape or bounded-radius material/multicore turnover occurs infinitely often. This still requires a global nonrepeatability/packing theorem; kinetic-energy dissipation alone is too weak because natural-scale stage costs carry the summable factor `W^{-1/2}`.

### System II — restricted Type-I P_V ancient system

If H/T do not recur, the nested first-hitting tower must produce a nontrivial ancient candidate with:

- exact backward first-hitting vorticity cap `||Omega||_infty <= 1`;
- Type-I backward decay `||Omega(tau)||_infty <= C/|tau|`;
- a tight active core;
- a globally necessary backward-growing low-vorticity `L^3` tail;
- recurrent full-NS `P_V` action;
- strict nonattainment of maximal H1 production, and a class-dependent efficiency gap if the profile class is genuinely precompact.

---

## 15. Principal next targets

1. **Variational threshold:** analyze `Lambda_K`; either prove `Lambda_K < nu` or derive the Euler--Lagrange/rigidity system of a threshold maximizer.
2. **Large shape-ratio branch:** analyze
\[
\Xi(S)=\frac{\int|S||\nabla S|^2}{\|\Delta S\|_2^2},
\]
because
\[
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{\|\Delta S\|_2^2}
\le
(1-\delta_K)\frac4{\sqrt6}\Xi(S).
\]
Large `Xi` must either be excluded on the compact first-hitting class or routed to `H/T/projective` geometry.
3. **Secondary-cylinder lemma:** convert failure of off-center local Type-I bounds into a genuine secondary core/influx (`T`) or derivative concentration (`H`).
4. **Core-tail coexistence:** test whether a backward-growing global `L^3` velocity tail with `||Omega(tau)||_infty -> 0` can remain dynamically passive while a recurrent terminal core persists.

Status: **GLOBAL REGULARITY IS NOT PROVED. THE NON-H/T LOCAL SURVIVOR HAS BEEN REDUCED TO A PRECOMPACT TYPE-I P_V VARIATIONAL THRESHOLD PROBLEM, WHILE THE ANCIENT GLOBAL SURVIVOR MUST COMBINE A NONTRIVIAL TERMINAL CORE WITH A BACKWARD-GROWING LOW-VORTICITY CRITICAL VELOCITY TAIL.**