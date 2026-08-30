# DSD M5-312 — Volume-Filling Transition Cloud: Mixed-Norm Decay and Weighted-Dissipation No-Go

Date: 2026-08-30

Parent: `DSD_M5_311_AFFINE_TRANSITION_VORTICITY_VARIANCE_TO_DENSE_LOCAL_CLOUD_AND_LOG_INTERACTION_GATE_2026-08-30.md`

Status: **TYPE-II AMPLIFICATION REFINEMENT / A VORTICITY-DOMINATED AFFINE TRANSITION PRODUCES `N~R^3` UNIT NATURAL PACKETS; FOR THIS VOLUME-FILLING CLOUD THE SCALE-INVARIANT SEREGIN MIXED NORM REDUCES TO `M_kappa ~ Theta_cl R^{l-2}` / IN THE IMPORTANT `1<l<2` RANGE BOUNDED NATURAL-TIME PERSISTENCE MAKES THE MIXED NORM DECAY WITH R / TO AMPLIFY, `Theta_cl` MUST GROW AT LEAST LIKE `g^{-1}R^{2-l}`, WHILE THE SEREGIN-WEIGHTED DISSIPATION FLOOR IS `E_f >= c Theta_cl^2`, SO A UNIFORMLY BOUNDED `E_f` CORRIDOR EXCLUDES THE AMPLIFIED VOLUME-FILLING CLOUD / GLOBAL REGULARITY UNPROVED.**

---

## 1. Transition-cloud geometry

M5-311 gives, outside cell-scale H/T exits, a cloud of

\[
\boxed{N\ge cR^3}
\]

genuinely occupied unit-natural-scale packets inside a ball of radius `R=R_br` in the original satellite units.

The packet scale is normalized to

\[
\ell_{cell}=1.
\]

Let the cloud persist for

\[
\Theta_{cl}
\]

cell-natural times.

---

## 2. Packet mixed norm

The packet packing model from M5-292 gives at outer scale `R`

\[
M_\kappa^{s,l}
\sim
\Theta_{cl}
R^{-\kappa}
N^{l/s}
\]

up to fixed occupancy/overlap constants.

Using

\[
N\sim R^3,
\]

\[
M_\kappa
\sim
\Theta_{cl}
R^{-\kappa+3l/s}.
\]

Since

\[
\kappa
=2+\frac{3l}{s}-l,
\]

the `s`-dependence cancels exactly:

\[
\boxed{
M_\kappa
\sim
\Theta_{cl}R^{l-2}.
}
\]

This cancellation is a useful consequence of volume-filling `N~R^3` geometry.

---

## 3. Consequence for `1<l<2`

If

\[
1<l<2,
\]

then

\[
l-2<0.
\]

Therefore any cloud with bounded persistence

\[
\Theta_{cl}=O(1)
\]

satisfies

\[
\boxed{M_\kappa\to0}
\]

as `R->infinity`.

In particular it cannot satisfy Seregin's amplified nontriviality condition

\[
g(1/R\text{-linked scale})M_\kappa\ge\varepsilon_0
\]

when the relevant `g` also tends to zero.

More abstractly, amplification requires

\[
\boxed{
\Theta_{cl}
\gtrsim
\frac{\varepsilon_0}{g}
R^{2-l}.
}
\]

Thus the cloud must persist for a growing number of its own natural times.

---

## 4. Dissipation floor

Each occupied unit packet has

\[
\int|\nabla u|^2\gtrsim1
\]

on its core.

With `N~R^3` packets persisting for `Theta_cl` natural times,

\[
\int_{Q(R)}|\nabla u|^2
\gtrsim
R^3\Theta_{cl}.
\]

Hence the outer CKN dissipation quantity satisfies

\[
\boxed{
E(R)
=R^{-1}
\int_{Q(R)}|\nabla u|^2
\gtrsim
R^2\Theta_{cl}.
}
\]

---

## 5. Weighted dissipation

For a remaining/local observation time equal to `Theta_cl` in cell-natural units, the Seregin time compression relative to the outer radius is

\[
\boxed{
f=\frac{\Theta_{cl}}{R^2}.}
\]

Therefore

\[
E_f=fE
\]

obeys

\[
\boxed{
E_f(R)
\gtrsim
\frac{\Theta_{cl}}{R^2}
\left(R^2\Theta_{cl}\right)
=
\Theta_{cl}^2.
}
\]

Thus a corridor with

\[
\boxed{E_f(R)\le M_E}
\]

forces

\[
\boxed{\Theta_{cl}\le C(M_E).}
\]

---

## 6. Amplification contradiction under bounded `E_f`

Combine:

\[
\Theta_{cl}
\gtrsim
\frac{\varepsilon_0}{g}R^{2-l}
\]

with

\[
\Theta_{cl}\le C(M_E).
\]

For `1<l<2`, `R^{2-l}->infinity`; if also `g->0`, the lower bound diverges even faster.

Hence

\[
\boxed{
\text{volume-filling occupied transition cloud}
+
E_f=O(1)
\Longrightarrow
\text{no Seregin-amplified branch}
}
\]

in the `1<l<2` range.

---

## 7. What survives

The dense transition cloud may still exist as a **non-amplified** critical configuration.

Its remaining options are:

1. noncancelling local strain -> `H_sat-local`;
2. dense tensor cancellation -> `C_dense,cancel`;
3. rapid packet birth/death/relative motion -> `T_dynamic`;
4. failure of the weighted-dissipation corridor;
5. diffuse/background mixed-norm dominance.

Thus M5-312 does not eliminate the cloud itself; it removes its simplest route into the amplified Type-II scenario.

---

## 8. Formation interpretation

A large object count does not by itself create Type-II mixed-norm amplification.

At geometric volume filling, the critical scaling exactly cancels the `s`-dependent packet multiplicity and leaves

\[
\boxed{
M_\kappa\sim\Theta_{cl}R^{l-2}.
}
\]

For `l<2`, persistence, not multiplicity, is the scarce attribute.

This is a useful distinction between **formation multiplicity** and **temporal support**.

---

## 9. Audit verdict

### DERIVED

\[
\boxed{M_\kappa\sim\Theta_{cl}R^{l-2}}
\]

for a volume-filling natural packet cloud.

### DERIVED DISSIPATION FLOOR

\[
\boxed{E_f\gtrsim\Theta_{cl}^2.}
\]

### CONDITIONAL NO-GO

For `1<l<2`, bounded `E_f` excludes Seregin-amplified volume-filling transition clouds.

### OPEN

- non-amplified dense-cancelling cloud;
- weighted pressure and diffuse background;
- dynamic turnover;
- critical detached endpoint;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]