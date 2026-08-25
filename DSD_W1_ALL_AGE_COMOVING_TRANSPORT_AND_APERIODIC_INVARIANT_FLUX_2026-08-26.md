# DSD W1 All-Age Co-Moving Transport and Aperiodic Invariant Flux — 2026-08-26

Status: **ALL-AGE CO-MOVING SHELL TRANSPORT PROVED / APERIODIC INVARIANT CRITICAL-FLUX POSITIVITY DERIVED CONDITIONAL ON BARKER--PRANGE INPUT / GLOBAL REGULARITY UNPROVED.**

## 1. Improvement over the finite-h transport note

For

\[
W_R(z,s)=e^{s/2}R\,U(e^{s/2}Rz,s),
\]

the exact co-moving equation is

\[
\partial_sW_R
=R^{-2}e^{-s}
\left[
\nu\Delta W_R
-\mathbb P\nabla\cdot(W_R\otimes W_R)
\right].
\]

On W1 the fixed-annulus H1 norm is uniformly bounded for all times. Therefore the bracket is uniformly bounded in H^{-1}.

Because

\[
\int_0^h e^{-s}ds\le1
\]

for every h>=0, the previous finite-h estimate upgrades to the age-uniform bound

\[
\boxed{
\|W_R(h)-W_R(0)\|_{H^{-1}}
\le CR^{-2}
\qquad\forall h\ge0.
}
\]

Interpolation with the uniform H1 bound gives

\[
\boxed{
\|W_R(h)-W_R(0)\|_2
\le CR^{-1}
}
\]

and L2--L6 interpolation gives

\[
\boxed{
\|W_R(h)-W_R(0)\|_3
\le CR^{-1/2}
\qquad\forall h\ge0.
}
\]

The constant is independent of shell age h.

## 2. All-age shell transport

Define

\[
\Psi_R(U)=\int_{R<|Y|<2R}|U(Y)|^3dY.
\]

Then for every h>=0,

\[
\boxed{
\left|
\Psi_{e^{h/2}R}(\Phi_hU)-\Psi_R(U)
\right|
\le CR^{-1/2}.
}
\]

This is the key removal of the old age-decay obstruction: a remote occupied shell can be pulled back along the co-moving dilation characteristic to one fixed reference radius without a coefficient that deteriorates with age.

## 3. Pull positive-density late shells back to one fixed radius

Let

\[
h_0=2\log2,
\qquad
R_k=2^kR_0.
\]

At a sufficiently late Leray time s, the Barker--Prange/W1 shell recovery gives

\[
\sum_{k=0}^{N(s)-1}\Psi_{R_k}(U(s))
\ge a_0N(s)
\]

with N(s)->infinity and fixed a0>0.

Choose the Barker--Prange radius exponent small enough that

\[
h_0N(s)\le \vartheta s
\]

for one fixed theta<1. Thus all pulled-back times below remain late:

\[
s-kh_0\ge(1-\vartheta)s\to\infty.
\]

Since

\[
U(s)=\Phi_{kh_0}U(s-kh_0)
\]

and

\[
e^{kh_0/2}R_0=R_k,
\]

the all-age transport estimate gives

\[
\left|
\Psi_{R_k}(U(s))
-\Psi_{R_0}(U(s-kh_0))
\right|
\le CR_0^{-1/2}.
\]

Hence

\[
\boxed{
\frac1{N(s)}
\sum_{k=0}^{N(s)-1}
\Psi_{R_0}(U(s-kh_0))
\ge
 a_0-CR_0^{-1/2}.
}
\]

Choose R0 large enough that

\[
CR_0^{-1/2}\le a_0/4.
\]

Then

\[
\boxed{
\frac1{N(s)}
\sum_{k<N(s)}
\Psi_{R_0}(U(s-kh_0))
\ge\frac{3a_0}{4}.
}
\]

## 4. Discrete invariant empirical measure

Define the backward arithmetic-progression empirical measure

\[
\mu_s^{disc}
=
\frac1{N(s)}
\sum_{k=0}^{N(s)-1}
\delta_{U(s-kh_0)}.
\]

The W1 orbit closure is compact in every global Lp topology with p>3, so a subsequence converges weakly to a probability measure mu_disc.

The endpoint loss in shifting the discrete sum by one index is O(1/N), hence

\[
\boxed{
(\Phi_{h_0})_*\mu_{disc}=\mu_{disc}.
}
\]

Moreover, continuity of the fixed-radius shell observable gives

\[
\boxed{
\int\Psi_{R_0}(U)d\mu_{disc}(U)
\ge\frac{3a_0}{4}.
}
\]

Thus the aperiodic branch carries a nontrivial invariant critical-shell population under the dyadic Leray time map.

## 5. Positive asymptotic shell density for the discrete invariant measure

Let

\[
M_{disc}(R)=\int\Psi_R(U)d\mu_{disc}(U).
\]

Using discrete invariance and the all-age shell transport with h=h0,

\[
|M_{disc}(2R)-M_{disc}(R)|
\le CR^{-1/2}.
\]

Therefore along R_k=2^kR0,

\[
M_{disc}(R_k)\to M_{disc,\infty}.
\]

Moreover

\[
M_{disc,\infty}
\ge
M_{disc}(R_0)
-C\sum_{k=0}^\infty(2^kR_0)^{-1/2}.
\]

Choosing R0 still larger if necessary gives

\[
\boxed{
M_{disc,\infty}\ge\frac{a_0}{2}>0.
}
\]

## 6. Upgrade to a full-flow invariant measure

Average the discrete invariant measure through one dyadic time interval:

\[
\mu
=
\frac1{h_0}\int_0^{h_0}(\Phi_\tau)_*\mu_{disc}\,d\tau.
\]

Then mu is invariant under the full Leray flow.

For every fixed tau, the all-age transport law shows that the asymptotic critical-shell density of (Phi_tau)_*mu_disc equals the same M_disc,infinity, because the radial factor e^{tau/2} only shifts the far shell by a fixed multiplicative amount and the transport error tends to zero.

Consequently

\[
\boxed{
M_{\mu,\infty}
=M_{disc,\infty}
\ge\frac{a_0}{2}>0.
}
\]

Thus the aperiodic W1 branch, like the periodic branch, admits a full-flow invariant probability measure with a strictly positive asymptotic cubic mass per logarithmic shell.

## 7. Updated W1 invariant descriptor

Both recurrent possibilities now share the same invariant descriptor:

\[
\boxed{
\exists\ \mu\ \text{Leray-flow invariant such that}
\quad
\lim_{R\to\infty}
\int\Psi_R(U)d\mu(U)
=M_{crit}>0.
}
\]

For a periodic orbit, mu is simply normalized period measure. For an aperiodic minimal orbit, mu is obtained by the empirical construction above.

The distinction between periodic and aperiodic recurrence is therefore no longer relevant at the level of the remote critical-memory flux.

## 8. What remains

This does not contradict finite enstrophy. A 1/r velocity tail has constant cubic mass per log shell while its vorticity/enstrophy contribution decays geometrically.

The remaining rigidity problem can now be stated without a periodic/aperiodic split:

\[
\boxed{
\text{Can a nonzero compact recurrent Leray core coexist with an invariant}
\ M_{crit}>0\text{ center-mode flux?}
}
\]

Any final closure must use a genuinely dynamical/core coercivity mechanism; far-tail age loss and sparse-shell escape are no longer available.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
