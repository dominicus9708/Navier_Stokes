# DSD M5-19 — First-Hitting Critical Spectral Flux Gate

Date: 2026-08-26

Status: **DERIVED NECESSARY FLUX CONDITION FOR FAILURE OF THE SPECTRAL M5 TIGHTNESS / ARBITRARILY HIGH CRITICAL TAIL SPIKES REQUIRE A SCALE-INVARIANT ENERGY-FLUX FLOOR / NO CLOSURE YET / GLOBAL REGULARITY UNPROVED.**

## 1. Spectral M5 coordinate

From M5-18 define

\[
E_0:=\sup_{t<T_*}\|u(t)\|_2^2,
\]

\[
E_{>\kappa}(t)
:=\|P_{>\kappa}u(t)\|_2^2,
\]

and

\[
\boxed{
\mathfrak S(\kappa,t)
:=
E_0^{1/2}\kappa^{3/2}E_{>\kappa}(t).
}
\]

Uniform smallness of `mathfrak S` at high `kappa` is sufficient for the amplitude-tail M5 condition.

## 2. High-frequency energy balance

For a fixed Fourier cutoff `kappa`, the high-frequency component satisfies

\[
\boxed{
\frac12\frac d{dt}E_{>\kappa}(t)
+\nu\|\nabla P_{>\kappa}u(t)\|_2^2
=\Pi_E(\kappa,t),
}
\]

where `Pi_E(kappa,t)` denotes nonlinear energy flux into the retained high-frequency region, with the sign convention above.

By the Fourier support,

\[
\|\nabla P_{>\kappa}u\|_2^2
\ge
\kappa^2E_{>\kappa}.
\]

## 3. First-hitting argument

Fix `delta>0` and a sufficiently large `kappa` such that initially

\[
\mathfrak S(\kappa,t_0)<\delta.
\]

If later the critical tail reaches `delta`, let `t_kappa` be the first hitting time:

\[
\mathfrak S(\kappa,t_\kappa)=\delta.
\]

Since `kappa` is fixed,

\[
\frac d{dt}E_{>\kappa}(t_\kappa)\ge0
\]

in the one-sided first-hitting sense.

Hence the high-frequency balance gives

\[
\Pi_E(\kappa,t_\kappa)
\ge
\nu\|\nabla P_{>\kappa}u(t_\kappa)\|_2^2
\ge
\nu\kappa^2E_{>\kappa}(t_\kappa).
\]

Using

\[
E_{>\kappa}(t_\kappa)
=
\delta E_0^{-1/2}\kappa^{-3/2},
\]

we obtain

\[
\boxed{
\Pi_E(\kappa,t_\kappa)
\ge
\nu\delta E_0^{-1/2}\kappa^{1/2}.
}
\]

Equivalently,

\[
\boxed{
E_0^{1/2}\kappa^{-1/2}\Pi_E(\kappa,t_\kappa)
\ge
\nu\delta.
}
\]

The quantity on the left is scale invariant.

## 4. Consequence of M5 failure

If amplitude `K`-tightness fails along a sequence of increasing physical thresholds, M5-18 forces a corresponding sequence of spectral critical-tail events.

After choosing first hitting times, there must therefore exist

\[
\kappa_j\to\infty,
\qquad
t_j\uparrow T_*,
\]

such that

\[
\boxed{
E_0^{1/2}\kappa_j^{-1/2}
\Pi_E(\kappa_j,t_j)
\ge c_*>0.
}
\]

Thus a singular survivor requires an order-one **critical spectral energy-flux floor at arbitrarily high wavenumbers**.

## 5. DSD interpretation

This separates state storage from formation.

A large spectral tail is a state variable. At its first formation, however, the Navier--Stokes dynamics must supply a definite critical flux across the corresponding spectral boundary.

Hence the live M5 chain can be written

\[
\boxed{
\text{amplitude defect}
\Rightarrow
\text{spectral critical tail}
\Rightarrow
\text{first-hitting critical flux event}.
}
\]

The last object is genuinely dynamic and cannot be produced by static compactness alone.

## 6. Why this is not yet a contradiction

The dimensional rate grows like `kappa^{1/2}`, but the amount of high-frequency kinetic energy at the critical threshold decays like `kappa^{-3/2}`. A high-wavenumber event may therefore occur on a very short parabolic timescale without violating the finite kinetic-energy or ordinary dissipation budgets.

Thus one must not sum the pointwise flux floors without controlling event duration or an independent scale-critical flux action.

## 7. Relation to known spectral criteria

Existing spectral regularity criteria and determining-wavenumber approaches likewise identify uncontrolled energy transfer toward arbitrarily high Fourier modes as a necessary feature of blow-up. M5-19 gives the project-specific normalization naturally induced by the `K`-tail bridge.

## 8. Updated target

The next useful M5 question is whether the normalized flux

\[
\boxed{
\mathfrak F_E(\kappa,t)
:=E_0^{1/2}\kappa^{-1/2}\Pi_E(\kappa,t)
}
\]

admits a scale-critical time-action estimate, or whether persistent positive `mathfrak F_E` can be shown to require a quantitatively mixed helical state using M5-16--17.

No such closing estimate is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
