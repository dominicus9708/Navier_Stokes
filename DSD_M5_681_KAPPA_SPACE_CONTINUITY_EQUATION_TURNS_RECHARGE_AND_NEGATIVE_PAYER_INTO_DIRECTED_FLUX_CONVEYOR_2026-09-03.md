# DSD M5-681 — Kappa-space continuity equation turns positive recharge and negative payer into one directed material-flux conveyor

Date: 2026-09-03

Status: **INTERNAL QUOTIENT-POPULATION REDUCTION / ON A MATERIAL VORTEX-LINE LABEL SPACE WITH CURRENT POSITIVE FLUX MEASURE `dmu_theta`, THE CE-H FLUX LAW `d_theta dmu = kappa dmu` AND THE MATERIAL MULTIPLIER VELOCITY `h=D_B kappa` GIVE THE EXACT KINETIC EQUATION `partial_theta F + partial_k G = k F`, WHERE `F(k,theta)=int delta(k-kappa_lambda)dmu_theta` AND `G(k,theta)=int h_lambda delta(k-kappa_lambda)dmu_theta` / ON A RECURRENT INVARIANT ENSEMBLE THIS BECOMES `partial_k Gbar = k Fbar`; IF BOTH THE M5-678 POSITIVE-RECHARGE POPULATION AND THE M5-657 NEGATIVE-PAYER POPULATION ARE PRESENT, THE MEAN KAPPA-SPACE FLUX THROUGH ZERO IS STRICTLY DIRECTED, `Gbar(0)<0` / THE LAST SURVIVOR IS THEREFORE A NONEQUILIBRIUM FLUX CONVEYOR IN KAPPA-SPACE, NOT TWO INDEPENDENT PAYER BRANCHES / CLOSURE NOW REQUIRES A PDE CONSTITUTIVE LAW FOR `G`, WHICH THE ABSTRACT M5-653/680 TOYS DO NOT HAVE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material vortex-line label space

On CE-H,

\[
D_B\xi=0
\]

so vortex-line labels can be followed materially.
Work on one finite retained flux ensemble represented on a fixed base transversal as in M5-647.

Let `lambda` denote a base material vortex-line/tube label and let

\[
d\mu_\theta(\lambda)>0
\]

be its current oriented flux weight.
The sign is fixed by the base orientation.

M5-602 gives the exact material flux law

\[
\boxed{
\partial_\theta d\mu_\theta
=\kappa_\lambda(\theta)d\mu_\theta.
}
\]

Define also

\[
\boxed{
h_\lambda(\theta):=D_B\kappa_\lambda(\theta).}
\]

---

## 2. Push the flux measure to kappa-space

Define the nonnegative kappa distribution

\[
\boxed{
F(k,\theta)
:=
\int
\delta(k-\kappa_\lambda(\theta))
\,d\mu_\theta(\lambda).
}
\]

Thus for a test function `psi`,

\[
\int\psi(k)F(k,\theta)dk
=
\int\psi(\kappa_\lambda)d\mu_\theta.
\]

Define the signed kappa-space transport current

\[
\boxed{
G(k,\theta)
:=
\int
h_\lambda(\theta)
\delta(k-\kappa_\lambda(\theta))
\,d\mu_\theta(\lambda).
}
\]

---

## 3. Exact weak evolution

Differentiate the test-function pairing:

\[
\frac d{d\theta}
\int\psi(\kappa_\lambda)d\mu_\theta
=
\int
\psi'(\kappa_\lambda)h_\lambda d\mu_\theta
+
\int
\psi(\kappa_\lambda)\kappa_\lambda d\mu_\theta.
\]

In kappa-space this is

\[
\frac d{d\theta}
\int\psi(k)F(k,\theta)dk
=
\int\psi'(k)G(k,\theta)dk
+
\int k\psi(k)F(k,\theta)dk.
\]

Integrating the first term by parts gives the distributional equation

\[
\boxed{
\partial_\theta F
+\partial_kG
=kF.
}
\]

This is exact and uses no scalar-law assumption `h=f(kappa,theta)`.
Hence it remains valid on the multi-sheet/cross-law branch.

---

## 4. Interpretation

The term

\[
kF
\]

is not a transport term in kappa-space.
It is the local growth/decay of the material flux measure itself:

- `k>0`: flux weight is amplified;
- `k<0`: flux weight is consumed.

The current `G` transports flux weight between different `kappa` values because the same material label changes its multiplier according to `h=D_B kappa`.

Thus the two mechanisms retained after M5-676 are parts of one balance:

\[
\boxed{
\text{positive-kappa recharge}
\longrightarrow
\text{kappa-space transport}
\longrightarrow
\text{negative-kappa consumption}.
}
\]

---

## 5. Recurrent/invariant average

On a recurrent finite-flux ensemble take an invariant time/ergodic average.
The bounded population distribution has zero mean time derivative, so

\[
\boxed{
\partial_k\overline G(k)
=k\overline F(k).
}
\]

On the retained high-amplitude/finite-core part, `kappa` is bounded because `|W|` is bounded below and `|Delta W|` is uniformly bounded.
Hence we may write the support as a compact interval

\[
[-K_*,K_*]
\]

for this retained ensemble and take

\[
\overline G(\pm K_*)=0
\]

in the no-through-boundary convention after enlarging the interval slightly beyond the support.

Integrating gives

\[
\boxed{
\int_{-K_*}^{K_*}k\overline F(k)dk=0.
}
\]

This is the flux-measure analogue of the zero mean multiplier of a recurrent fixed-flux population.

---

## 6. Strict current through kappa=0

M5-678 shows that the surviving late-activation cascade requires positive `kappa` amplification.
M5-657 and the later component identities force a negative-kappa payer population.

Thus in the nontrivial nested survivor

\[
\int_0^{K_*}k\overline F(k)dk>0
\]

and

\[
\int_{-K_*}^0k\overline F(k)dk<0.
\]

Integrating the stationary equation from `0` to `K_*` gives

\[
\boxed{
\overline G(0)
=-
\int_0^{K_*}k\overline F(k)dk
<0.
}
\]

Equivalently, integrating from `-K_*` to zero,

\[
\boxed{
\overline G(0)
=
\int_{-K_*}^0k\overline F(k)dk
<0.
}
\]

Therefore the recurrent flux population carries a **strict directed mean current through the zero-multiplier level**.
With the sign convention in `G`, the net flux-weighted passage is toward decreasing `kappa`.

---

## 7. Relation to the multi-sheet oscillator

The M5-653 oscillator can realize a nonzero `G` by phase-biased branch switching.
Therefore the existence of the directed current is not itself a contradiction.

Likewise the nested M5-680 cascade can be arranged so that positive phases amplify small future populations and negative phases retire old populations.

What those toys do not provide is the Navier-Stokes constitutive relation that determines

\[
h=D_B\kappa.
\]

On CE-H, `h` is not arbitrary.
M5-601 expresses it through `kappa`, `sigma`, `W`, `U`, and their spatial derivatives.

---

## 8. Why this is progress

The last hard branch no longer consists of several loosely connected events.
It is one stationary nonequilibrium conveyor:

\[
\boxed{
F\xrightarrow{k>0\text{ amplification}}
G\text{ transports through }k=0
\xrightarrow{k<0\text{ consumption}}
F.
}
\]

Any valid closure must now attack the constitutive current `G`, rather than separately count positive and negative packets.

---

## 9. Highest-value next target

Project the M5-601 commutator identity onto `W` to obtain an exact formula for

\[
h=D_B\kappa.
\]

Then push that formula to kappa-space.
The `Delta kappa` piece inside `Delta gamma` is expected to generate a genuine positive kappa-space diffusion term involving

\[
|\nabla\kappa|^2.
\]

If the remaining strain/pressure terms cannot sustain the strict stationary current `Gbar(0)<0`, the multi-sheet/nested cascade closes.

If they can, the precise compensating PDE channel will be isolated.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
